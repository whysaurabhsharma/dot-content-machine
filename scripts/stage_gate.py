#!/usr/bin/env python3
"""stage_gate.py - where a piece stands, read only from the files. The workflow's checkpoint.

Usage:
    python scripts/stage_gate.py <slug>            # report, for a person
    python scripts/stage_gate.py <slug> --json     # the same, for the workflow
    python scripts/stage_gate.py start <slug> --bank <id> [--format research|teardown|guide] [--practice]
    python scripts/stage_gate.py waive <slug> --rule 14 --batch <n> --by "<name, YYYY-MM-DD>"
    python scripts/stage_gate.py clear <slug> --by "<name, YYYY-MM-DD>" --basis "<how a PIECE IF condition was met>"

It remembers nothing: every answer comes from files in the repo, so it gives the same
answer in a new session as in the one that wrote them. Stages are checked in order;
the first not done is the next one. A stage that needs a person is reported as
"waiting", with what the person must do; one whose inputs are wrong is "blocked".

`start` writes runs/<slug>-piece.json, the piece's manifest: its bank question
(Decision 1), its format (research if not given; CLAUDE.md, "What this machine makes")
and whether it is practice. A teardown or guide has no run of its own: truth, run and
mark are reported done as "not used by format", and a "figures" stage takes their place. It refuses unless that question is unwritten
and its evidence score is confirmed by a person, and refuses the rehearsal slug
without --practice (hard rule 4).

Gates enforced here that the skills only stated in prose:
- outline/draft/seo-geo/linkedin/export never overwrite: a done stage is never redone;
- the rehearsal is refused without --practice;
- draft waits for the outline's "Approved by" and "Date" (Decision 2);
- a batch waits for its conditions block (rules 14, 15, 17) and, for a piece that isn't
  practice, for its four screenshot files, unless the batch has a recorded rule 14 waiver;
  marking waits for the credits-after reading and, without a waiver, its screenshot file.
  A waiver is a recorded state, not a flag: `waive` writes it into the manifest
  (runs/<slug>-piece.json, "waivers"), and refuses unless the batch's conditions block already
  states it in a line starting "**Rule 14 waived" (who, and what it costs). The gate reads both,
  every time, so a waived batch never shows as stuck. (Until 1 November 2026 the waiver was a
  --no-screenshots flag that had to be passed on every call; without it, a finished piece
  reported as stuck at its run. That flag is now ignored.)
- export waits for check_piece.py to report no FAIL, and for Decision 3;
- linkedin stops when all five opening structures are used;
- the run waits for the truth spec's "reviewed_by" (rival definitions before the run);
- after the reviews, the writer must log every fix, or why a point stands, in
  reviews/<slug>/revisions.md, newer than the reviews.
"""
import csv
import json
import re
import subprocess
import sys
from pathlib import Path

BANK = Path("bank/questions.csv")
STRUCTURES = 5
HUMAN_CHECKS = ["headline test", "lift test in Perplexity and Claude", "second fact-check on a different model",
                "read aloud on a phone"]


def read(path):
    p = Path(path)
    return p.read_text(encoding="utf-8") if p.exists() else None


def front(text):
    m = re.match(r"---\n(.*?)\n---", text or "", re.S)
    return dict(re.findall(r"^(\w+):\s*(.*)$", m.group(1), re.M)) if m else {}


def bank_row(qid):
    with open(BANK, encoding="utf-8") as f:
        return next((r for r in csv.DictReader(f) if r["id"] == str(qid)), None)


def check_piece(args):
    r = subprocess.run([sys.executable, "scripts/check_piece.py", *args], capture_output=True, text=True)
    fails = [l.strip() for l in r.stdout.splitlines() if re.match(r"\s*\w+\s+FAIL\b", l)]
    return fails


def batches(run_text):
    """[(n, conditions_text, [entry ids])] from a run file."""
    out = []
    parts = re.split(r"^## Batch (\d+): conditions\s*$", run_text, flags=re.M)
    for i in range(1, len(parts), 2):
        body = re.split(r"^## (?!Batch \d+: conditions)", parts[i + 1], maxsplit=1, flags=re.M)[0]
        conditions = body.split("\n### ", 1)[0]
        out.append((int(parts[i]), conditions, re.findall(r"^### (\w+): ", parts[i + 1], re.M)))
    return out


def recorded(conditions, label):
    m = re.search(rf"^- {label}: (.*)$", conditions, re.M)
    return bool(m) and not re.search(r"not yet recorded|^\s*$", m.group(1))


WAIVER = re.compile(r"^\*\*Rule 14 waived", re.M)


def waived(manifest, slug, n, cond):
    """A rule 14 waiver for batch n: recorded in the manifest and stated in the conditions block."""
    rec = any(w.get("rule") == 14 and int(w.get("batch", -1)) == int(n) for w in manifest.get("waivers", []))
    return rec and bool(WAIVER.search(cond))


def assess(slug):
    stages = []

    def add(name, state, detail):
        stages.append({"stage": name, "state": state, "detail": detail})

    manifest = json.loads(read(f"runs/{slug}-piece.json") or "null")
    # Decision 1
    if manifest is None:
        add("question", "waiting", f"Decision 1: a person runs `python scripts/stage_gate.py start {slug} --bank <id>`")
        return stages
    row = bank_row(manifest["bank_id"])
    add("question", "done", f"bank #{manifest['bank_id']}: {row['question'] if row else 'NOT IN BANK'}"
        + (" (practice)" if manifest.get("practice") else ""))

    fmt = manifest.get("format", "research")
    section7 = {"research": "## 7. Test questions", "teardown": "## 7. Sources",
                "guide": "## 7. Evidence for each step"}.get(fmt)
    if section7 is None:
        add("research", "blocked", f"unknown format '{fmt}' in runs/{slug}-piece.json")
        return stages
    research = read(f"runs/{slug}-research.md")
    if not research or section7 not in research:
        add("research", "next", f"runs/{slug}-research.md missing or without '{section7}'")
        return stages
    if re.search(r"^\*\*NOT A PIECE, BUT A SURFACE", research, re.M):
        add("research", "waiting", "the verdict is NOT A PIECE, BUT A SURFACE: a person records the surface in "
            f"bank/questions.csv (python scripts/bank.py surface {manifest['bank_id']} <surface> --basis \"...\"); no piece is written")
        return stages
    if re.search(r"^\*\*NOT A PIECE", research, re.M):
        add("research", "blocked", "the verdict is NOT A PIECE")
        return stages
    # PIECE IF (1 November 2026, from the cold-start test): the condition is a person's to check, and the
    # check is recorded in the manifest, so the gate can see it. Until then the piece waits at research.
    m_if = re.search(r"^\*\*PIECE IF\*\*\s*(.*)$", research, re.M)
    if m_if and not manifest.get("piece_if_cleared"):
        add("research", "waiting", "the verdict is PIECE IF: " + m_if.group(1).strip()[:200]
            + f" A person checks the condition, then runs python scripts/stage_gate.py clear {slug} "
            "--by \"<name, date>\" --basis \"<how it was met>\"")
        return stages
    add("research", "done", f"runs/{slug}-research.md"
        + (f" (PIECE IF cleared by {manifest['piece_if_cleared']['by']})" if m_if else ""))

    if fmt != "research":
        for s in ("truth", "run", "mark"):
            add(s, "done", f"not used by format {fmt}")
        figs = read(f"figures/{slug}-figures.csv") or ""
        if len([l for l in figs.splitlines()[1:] if l.strip()]) == 0:
            add("figures", "next", f"figures/{slug}-figures.csv: one row per number the piece will use, each "
                "'published: <URL>, read <date>' (hard rule 4) or copied from a cited run's figures file")
            return stages
        add("figures", "done", f"figures/{slug}-figures.csv")
        return stages + writing(slug, manifest)

    spec_text, truth = read(f"specs/{slug}-truth.json"), read(f"figures/{slug}-truth.csv")
    if not spec_text or not truth:
        add("truth", "next", f"specs/{slug}-truth.json and figures/{slug}-truth.csv")
        return stages
    spec = json.loads(spec_text)
    if any(r["error"] for r in csv.DictReader(truth.splitlines())):
        add("truth", "blocked", "figures/<slug>-truth.csv has rows that failed to compute")
        return stages
    if not spec.get("reviewed_by"):
        add("truth", "waiting", f"a person checks specs/{slug}-truth.json (rival definitions in before the run) "
            "and adds \"reviewed_by\": \"<name, date>\"")
        return stages
    add("truth", "done", f"reviewed by {spec['reviewed_by']}")
    asked = [q for q in spec["questions"] if q.get("asked", True)]

    run_text = read(f"runs/{slug}-run.md") or ""
    bs = batches(run_text)
    if not bs:
        add("run", "waiting", f"batch 1: a person records the conditions in Dot's UI (mode, environment, context "
            f"notes, credits before) as '## Batch 1: conditions' in runs/{slug}-run.md (rules 14, 15, 17)")
        return stages
    last_n, last_cond, last_ids = bs[-1]
    if not last_ids:
        missing = [l for l in ("Mode", "Environment", "Context notes", "Credits before") if not recorded(last_cond, l)]
        shots = [] if manifest.get("practice") else [s for s in ("mode", "environment", "notes", "credits-before")
                                                      if not Path(f"runs/screenshots/{slug}-batch-{last_n}-{s}.png").exists()]
        if missing:
            add("run", "waiting", f"batch {last_n}: a person records {', '.join(missing)} in its conditions block "
                "(rules 14, 15, 17)")
        elif shots and not waived(manifest, slug, last_n, last_cond):
            add("run", "waiting", f"batch {last_n}: screenshot files missing in runs/screenshots/: "
                + ", ".join(f"{slug}-batch-{last_n}-{s}.png" for s in shots) + " (rule 14; a real piece needs all five). "
                f"To waive instead, a person states it in the conditions block ('**Rule 14 waived ...') and runs "
                f"python scripts/stage_gate.py waive {slug} --rule 14 --batch {last_n} --by \"<name, date>\"")
        else:
            add("run", "next", f"batch {last_n}: dot-runner asks the {len(asked)} questions")
        return stages
    if len(last_ids) < len(asked):
        add("run", "next", f"batch {last_n} has {len(last_ids)} of {len(asked)} entries: dot-runner continues")
        return stages
    after_shot = Path(f"runs/screenshots/{slug}-batch-{last_n}-credits-after.png")
    if not manifest.get("practice") and not waived(manifest, slug, last_n, last_cond) and recorded(last_cond, "Credits after") and not after_shot.exists():
        add("run", "waiting", f"batch {last_n}: screenshot file missing: {after_shot.as_posix()} (rule 15)")
        return stages
    if not recorded(last_cond, "Credits after"):
        add("run", "waiting", f"batch {last_n}: a person reads credits after in Dot's UI and records it")
        return stages
    add("run", "done", f"batch {last_n}: {len(last_ids)} entries")

    figures = read(f"figures/{slug}-figures.csv") or ""
    marked = set(re.findall(r"^MR-(\w+),", figures, re.M))
    if not set(last_ids) <= marked:
        add("mark", "next", f"python scripts/mark_run.py {slug} --batch {last_n}")
        return stages
    add("mark", "done", f"{len(last_ids)} rows in figures/{slug}-figures.csv")

    stages.extend(writing(slug, manifest))
    return stages


def writing(slug, manifest):
    """Outline to publish: the same for every format."""
    stages = []
    row = bank_row(manifest["bank_id"])

    def add(name, state, detail):
        stages.append({"stage": name, "state": state, "detail": detail})

    outline = read(f"pieces/{slug}-outline.md")
    if not outline:
        add("outline", "next", f"pieces/{slug}-outline.md")
        return stages
    # The quotable line and the freshness line (v1.8). An outline already drafted from is not reopened.
    if not Path(f"pieces/{slug}.md").exists():
        q = re.search(r"^\**Quotable line:?\**:?\s*(.+)$", outline, re.M | re.I)
        fresh = re.search(r"^\**Freshness:?\**:?\s*\S", outline, re.M | re.I)
        problems = []
        if not q:
            problems.append("no 'Quotable line:' line")
        else:
            sentence = re.sub(r"\s*\((?:figures?|ID|IDs?)[^)]*\)\s*$", "", q.group(1).strip(), flags=re.I)
            n_words = len(re.findall(r"\S+", re.sub(r"[*\"“”]", "", sentence)))
            number_word = r"\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|hundred|thousand|million|half)\b"
            id_part = re.search(r"\(ID:?\s*([^)]*)\)", q.group(1))
            ids = re.findall(r"[A-Z]{1,4}-?\d+", id_part.group(1)) if id_part else []
            fig_ids = set(re.findall(r"^([^,\n]+),", read(f"figures/{slug}-figures.csv") or "", re.M))
            supported = bool(ids) and all(i in fig_ids for i in ids)
            if not (re.search(r"\d", sentence) or re.search(number_word, sentence, re.I) or supported):
                problems.append("the quotable line has no number and no (ID: ...) of a figure in the figures file that supports it")
            if n_words >= 25:
                problems.append(f"the quotable line is {n_words} words (under 25)")
        if not fresh:
            problems.append("no 'Freshness:' line")
        if problems:
            add("outline", "blocked", f"pieces/{slug}-outline.md: {'; '.join(problems)} (/outline items 11 and 12)")
            return stages
    approved = re.search(r"^Approved by:\s*(\S.*)$", outline, re.M)
    dated = re.search(r"^Date:\s*(\S.*)$", outline, re.M)
    if not (approved and dated):
        add("outline", "waiting", f"Decision 2: a person fills 'Approved by' and 'Date' in pieces/{slug}-outline.md")
        return stages
    add("outline", "done", f"approved by {approved.group(1)}, {dated.group(1)}")

    piece = read(f"pieces/{slug}.md")
    if not piece:
        add("draft", "next", f"pieces/{slug}.md")
        return stages
    add("draft", "done", f"pieces/{slug}.md")
    fm = front(piece)
    if not all(fm.get(k) is not None for k in ("seo_title", "meta", "slug")) or "reverse_links:" not in piece:
        add("seo-geo", "next", "seo_title, meta, slug and reverse_links in the front matter")
        return stages
    add("seo-geo", "done", f"slug {fm.get('slug')}")

    missing = [r for r in ("reader", "fact-checker", "lift-tester") if not Path(f"reviews/{slug}/{r}.md").exists()]
    if missing:
        add("reviews", "next", f"python scripts/run_reviewer.py <reviewer> {slug} for: {', '.join(missing)}")
        return stages
    add("reviews", "done", "reader, fact-checker, lift-tester")

    log = Path(f"reviews/{slug}/revisions.md")
    newest_review = max(Path(f"reviews/{slug}/{r}.md").stat().st_mtime for r in ("reader", "fact-checker", "lift-tester"))
    if not log.exists() or log.stat().st_mtime < newest_review:
        add("revise", "next", f"the writer fixes the reader's three stopping points and every fact-checker problem, "
            f"and logs each fix, or one line on why it stands, in {log}")
        return stages
    add("revise", "done", str(log))

    fails = check_piece([f"pieces/{slug}.md"])
    if fails:
        add("edit", "next", f"check_piece.py FAILs: {'; '.join(fails)}")
        return stages
    add("edit", "done", "check_piece.py: no FAIL")

    human = read(f"reviews/{slug}/human.md") or ""
    ticked = [c for c in HUMAN_CHECKS if re.search(rf"^- \[x\] {re.escape(c)}", human, re.M | re.I)]
    title_ok = fm.get("title_approved_by")
    reviewed = fm.get("reviewed_on")
    if len(ticked) < len(HUMAN_CHECKS) or not title_ok or not reviewed:
        todo = [c for c in HUMAN_CHECKS if c not in ticked]
        add("title", "waiting", "Decision 3: a person sets title_approved_by and reviewed_on (hard rule 22) in the front matter"
            + (f", and ticks in reviews/{slug}/human.md: {'; '.join(todo)}" if todo else ""))
        return stages
    add("title", "done", f"approved by {title_ok}")

    posts = read(f"posts/{slug}-posts.md") or ""
    n_posts = len(re.findall(r"^## Post \w+ · ", posts, re.M))
    if n_posts == 0:
        add("linkedin", "next", f"posts/{slug}-posts.md")
        return stages
    post_fails = check_piece(["--post", f"posts/{slug}-posts.md"])
    if post_fails:
        add("linkedin", "blocked", f"check_piece.py --post FAILs: {'; '.join(post_fails)}")
        return stages
    add("linkedin", "done", f"{n_posts} of {STRUCTURES} opening structures used")

    out = Path(f"exports/{slug}-practice" if manifest.get("practice") else f"exports/{slug}")
    # Webflow files are optional since v1.8: Dot's team publishes; export_webflow.py stays for whoever wants it.
    if not (out.exists() and list(out.glob("*.docx")) and list(out.glob("*.md"))):
        add("export", "next", f"{out}/ (.docx and clean .md; webflow.html and webflow-fields.json optional)")
        return stages
    add("export", "done", str(out))

    if manifest.get("practice"):
        add("publish", "blocked", "practice piece: not for publication (hard rule 4)")
    elif row and row["status"] == "published":
        add("publish", "done", "bank status published")
    elif not re.search(r"^\*\*Read by:\*\*[ \t]*\S", read(f"reviews/{slug}/publish-note.md") or "", re.M):
        # v1.8.16: the note says what is assumed and what to paste if Dot says no; it is read before publishing.
        add("publish", "waiting", f"Decision 4 waits on the publish note: whoever publishes reads "
            f"reviews/{slug}/publish-note.md (copied to exports/{slug}/PUBLISH-NOTE.md) and fills its '**Read by:**' line")
    else:
        add("publish", "waiting", f"Decision 4: a person publishes, then runs "
            f"`python scripts/bank.py status {manifest['bank_id']} published --basis \"<URL>\"`")
    return stages


def start(argv):
    if len(argv) < 5 or "--bank" not in argv:
        print(__doc__)
        return 2
    slug, qid = argv[2], argv[argv.index("--bank") + 1]
    practice = "--practice" in argv
    fmt = argv[argv.index("--format") + 1] if "--format" in argv else "research"
    if fmt not in ("research", "teardown", "guide"):
        print(f"Refused: --format must be research, teardown or guide, not '{fmt}'.")
        return 1
    if slug == "rehearsal" and not practice:
        print("Refused: the rehearsal's findings can't appear in a piece (hard rule 4). Use --practice.")
        return 1
    row = bank_row(qid)
    if row is None:
        print(f"Refused: no question {qid} in the bank.")
        return 1
    if row["status"] != "unwritten" and not practice:
        print(f"Refused: question {qid} is {row['status']}, not unwritten.")
        return 1
    if row["evidence_by"] != "human" and not practice:
        print(f"Refused: question {qid}'s evidence score is {row['evidence_by'] or 'unscored'}. "
              f"Confirm it first: python scripts/bank.py confirm {qid} evidence")
        return 1
    path = Path(f"runs/{slug}-piece.json")
    if path.exists():
        print(f"Refused: {path} already exists.")
        return 1
    path.write_text(json.dumps({"slug": slug, "bank_id": qid, "question": row["question"],
                                "format": fmt, "practice": practice}, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {path}: Decision 1 recorded for bank #{qid}.")
    return 0


def waive(argv):
    """Record a person's rule 14 waiver for one batch in the manifest. Refuses unless the run file states it."""
    def opt(name):
        return argv[argv.index(name) + 1] if name in argv and argv.index(name) + 1 < len(argv) else None
    if len(argv) < 3 or not opt("--batch") or not opt("--by") or opt("--rule") != "14":
        print(__doc__)
        return 2
    slug, n, by = argv[2], int(opt("--batch")), opt("--by")
    path = Path(f"runs/{slug}-piece.json")
    if not path.exists():
        print(f"Refused: {path} doesn't exist; Decision 1 first.")
        return 1
    manifest = json.loads(path.read_text(encoding="utf-8"))
    conds = {num: c for num, c, _ in batches(read(f"runs/{slug}-run.md") or "")}
    if n not in conds:
        print(f"Refused: runs/{slug}-run.md has no '## Batch {n}: conditions' block.")
        return 1
    cond = conds[n]
    if not WAIVER.search(cond):
        print(f"Refused: batch {n}'s conditions block doesn't state the waiver. A person adds a line starting "
              "'**Rule 14 waived' saying who waived it and what it costs, then runs this again.")
        return 1
    ws = manifest.setdefault("waivers", [])
    if any(w.get("rule") == 14 and int(w.get("batch", -1)) == n for w in ws):
        print(f"Already recorded: rule 14 waiver for batch {n}.")
        return 0
    ws.append({"rule": 14, "batch": n, "by": by,
               "stated_in": f"runs/{slug}-run.md, Batch {n}: conditions",
               "cost": "no claim about mode, credits, environment or context notes in the piece"})
    path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {path}: rule 14 waiver for batch {n}, by {by}.")
    return 0


def clear(argv):
    """Record that a person checked a PIECE IF verdict's condition, and how it was met."""
    def opt(name):
        return argv[argv.index(name) + 1] if name in argv and argv.index(name) + 1 < len(argv) else None
    if len(argv) < 3 or not opt("--by") or not opt("--basis"):
        print(__doc__)
        return 2
    slug = argv[2]
    path = Path(f"runs/{slug}-piece.json")
    research = read(f"runs/{slug}-research.md") or ""
    if not path.exists():
        print(f"Refused: {path} doesn't exist; Decision 1 first.")
        return 1
    if not re.search(r"^\*\*PIECE IF\*\*", research, re.M):
        print(f"Refused: runs/{slug}-research.md has no PIECE IF verdict to clear.")
        return 1
    manifest = json.loads(path.read_text(encoding="utf-8"))
    manifest["piece_if_cleared"] = {"by": opt("--by"), "basis": opt("--basis")}
    path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {path}: PIECE IF condition cleared by {opt('--by')}.")
    return 0


def main(argv):
    if len(argv) >= 2 and argv[1] in ("--help", "-h", "help"):
        print(__doc__)
        return 0
    if len(argv) >= 2 and argv[1] == "clear":
        return clear(argv)
    if len(argv) >= 2 and argv[1] == "start":
        return start(argv)
    if len(argv) >= 2 and argv[1] == "waive":
        return waive(argv)
    if len(argv) < 2:
        print(__doc__)
        return 2
    slug = argv[1]
    if "--no-screenshots" in argv:
        print("Note: --no-screenshots is ignored. A rule 14 waiver is now recorded once with `waive` "
              "and read from the manifest.", file=sys.stderr)
    stages = assess(slug)
    last = stages[-1]
    result = {"slug": slug, "stages": stages, "next": last["stage"], "state": last["state"], "detail": last["detail"]}
    if "--json" in argv:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        for s in stages:
            print(f"{s['state']:>8}  {s['stage']:<9} {s['detail']}")
        print(f"\nNext: {last['stage']} ({last['state']})")
    return {"done": 0, "next": 0, "waiting": 3, "blocked": 4}[last["state"]]


if __name__ == "__main__":
    sys.exit(main(sys.argv))
