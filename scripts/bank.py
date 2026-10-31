#!/usr/bin/env python3
"""bank.py - score the question bank on the PDF's four factors and pick the next piece.

Usage:
    python scripts/bank.py rescore
    python scripts/bank.py set <id> <gap|incumbent|evidence|demand> <1-3> --basis "..." --by model|human
    python scripts/bank.py confirm <id> <factor>
    python scripts/bank.py shortlist [--n 15]
    python scripts/bank.py add --question "..." --ai-form "..." --persona "..." --type <problem|evaluation|comparison|implementation> --source "..." [--sales-call]
    python scripts/bank.py top

Factors, each 1 to 3 (ICP question bank PDF, page 4):
- demand: counted here from the sources the row names. 1 = none named, 2 = one or two,
  3 = three or more. A vendor having built a page also makes 3, but that can't be read
  reliably from the notes, so such rows are flagged for a person. Ahrefs volume is a
  note only (ahrefs_volume_us), never part of the score; a phrase with no Ahrefs row is
  "not measured".
- gap, incumbent, evidence: judgements. The /bank skill proposes them with `set --by
  model`, which marks them "model-unconfirmed"; a person confirms with `confirm`.
  incumbent is scored only for a shortlist (the top 15 by the other three factors);
  every other row says "not scored".

`top` puts sales-call questions first (CLAUDE.md hard rule 1), then total, then Ahrefs
volume where measured. It refuses to recommend a question whose evidence score is
unconfirmed. `rescore` writes a dated copy, bank/scores-YYYY-MM-DD.csv; nothing in the
bank's text columns is ever changed.
"""
import csv
import datetime as dt
import re
import sys
from pathlib import Path

BANK = Path("bank/questions.csv")
KEYWORDS = Path("data/ahrefs/keywords.csv")
FACTORS = ("demand", "gap", "incumbent", "evidence")
NEW_COLUMNS = ["from_sales_call", "ahrefs_volume_us"] + \
    [f"{f}_{s}" for f in FACTORS for s in ("score", "basis", "by")] + ["total", "scored_on"]
# External sources the bank's notes name. Dot's own pages are not evidence that buyers ask.
SOURCES = ["Querio", "Metabase", "Sigma", "Fabi", "Coefficient", "Chargebee", "Basedash", "Buster",
           "Atlan", "Tableau", "neurlcreators", "Snowflake", "Cortex", "DABstep", "vutr", "InfiniSynapse",
           "Immuta", "Reddit", "dbt community", "G2"]
PAGE_HINT = re.compile(r"\bpages?\b|\bpiece\b|'[^']+'", re.I)
TODAY = dt.date.today().isoformat()


def load():
    with open(BANK, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        if "score" in r and "pdf_score" not in r:
            r["pdf_score"] = r.pop("score")
        for c in NEW_COLUMNS:
            r.setdefault(c, "")
        if not r["from_sales_call"]:
            r["from_sales_call"] = "no"
    return rows


def save(rows, path=BANK):
    base = [c for c in rows[0] if c not in NEW_COLUMNS]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=base + NEW_COLUMNS)
        w.writeheader()
        w.writerows(rows)


def score_demand(r):
    if r["demand_by"] == "human":
        return
    text = f"{r['demand']} {r['weak_competition']}"
    named = [s for s in SOURCES if re.search(rf"\b{re.escape(s)}\b", text, re.I)]
    score = 1 if not named else 2 if len(named) < 3 else 3
    basis = f"sources named: {', '.join(named) if named else 'none'}"
    if score < 3 and PAGE_HINT.search(r["demand"]):
        basis += "; notes mention a page or piece: if a vendor built a page for it, a person should raise this to 3"
    r["demand_score"], r["demand_basis"], r["demand_by"] = str(score), basis, "data"


def total(r):
    scores = [r[f"{f}_score"] for f in FACTORS]
    return str(sum(int(s) for s in scores)) if all(s.isdigit() for s in scores) else ""


def rescore(argv):
    rows = load()
    with open(KEYWORDS, encoding="utf-8") as f:
        volume = {k["phrase"].strip().lower(): k["volume_us"] for k in csv.DictReader(f)}
    for r in rows:
        r["ahrefs_volume_us"] = volume.get(r["question"].strip().lower(), "not measured")
        score_demand(r)
        if not r["incumbent_score"]:
            r["incumbent_basis"], r["incumbent_by"] = "not scored: outside the shortlist", ""
        r["total"], r["scored_on"] = total(r), TODAY
    save(rows)
    snap = BANK.parent / f"scores-{TODAY}.csv"
    save(rows, snap)
    measured = sum(r["ahrefs_volume_us"] != "not measured" for r in rows)
    print(f"Rescored {len(rows)} questions; Ahrefs row for {measured}; full total for "
          f"{sum(bool(r['total']) for r in rows)}. Wrote {BANK} and {snap}.")
    return 0


def set_score(argv):
    if len(argv) < 5 or "--basis" not in argv or "--by" not in argv:
        print(__doc__)
        return 2
    qid, factor, score = argv[2], argv[3], argv[4]
    basis, by = argv[argv.index("--basis") + 1], argv[argv.index("--by") + 1]
    if factor not in FACTORS or score not in ("1", "2", "3") or by not in ("model", "human"):
        print("factor must be demand|gap|incumbent|evidence, score 1-3, --by model|human")
        return 2
    rows = load()
    row = next((r for r in rows if r["id"] == qid), None)
    if row is None:
        print(f"No question {qid}")
        return 1
    row[f"{factor}_score"], row[f"{factor}_basis"] = score, basis
    row[f"{factor}_by"] = "human" if by == "human" else "model-unconfirmed"
    row["total"], row["scored_on"] = total(row), TODAY
    save(rows)
    print(f"{qid} {factor} = {score} ({row[f'{factor}_by']})")
    return 0


def confirm(argv):
    qid, factor = argv[2], argv[3]
    rows = load()
    row = next((r for r in rows if r["id"] == qid), None)
    if row is None or not row[f"{factor}_score"]:
        print(f"No {factor} score on question {qid} to confirm")
        return 1
    row[f"{factor}_by"] = "human"
    save(rows)
    print(f"{qid} {factor} = {row[f'{factor}_score']} confirmed by a person")
    return 0


def shortlist(argv):
    n = int(argv[argv.index("--n") + 1]) if "--n" in argv else 15
    rows = [r for r in load() if r["status"] == "unwritten"
            and all(r[f"{f}_score"].isdigit() for f in ("demand", "gap", "evidence"))]
    rows.sort(key=lambda r: -sum(int(r[f"{f}_score"]) for f in ("demand", "gap", "evidence")))
    for r in rows[:n]:
        three = sum(int(r[f"{f}_score"]) for f in ("demand", "gap", "evidence"))
        print(f"{r['id']:>4}  {three}/9  {r['question']}")
    print(f"\n{min(n, len(rows))} shortlisted for the incumbent reading, of {len(rows)} unwritten questions "
          "with demand, gap and evidence scored.")
    return 0


def add(argv):
    need = ["--question", "--ai-form", "--persona", "--type", "--source"]
    if any(k not in argv for k in need):
        print(__doc__)
        return 2
    rows = load()
    new = {k: "" for k in rows[0]}
    new.update(id=str(max(int(r["id"]) for r in rows) + 1), status="unwritten",
               question=argv[argv.index("--question") + 1], ai_form=argv[argv.index("--ai-form") + 1],
               persona=argv[argv.index("--persona") + 1], type=argv[argv.index("--type") + 1],
               source=argv[argv.index("--source") + 1], observed_or_inferred="observed",
               from_sales_call="yes" if "--sales-call" in argv else "no", pdf_score="")
    rows.append(new)
    save(rows)
    print(f"Added question {new['id']} ({'sales call' if new['from_sales_call'] == 'yes' else 'not a sales call'}). "
          "Run rescore, then score its judgement factors.")
    return 0


def top(argv):
    rows = [r for r in load() if r["status"] == "unwritten"]
    sales = [r for r in rows if r["from_sales_call"] == "yes"]
    if not sales:
        print("No question in the bank comes from a sales call. Hard rule 1 puts them first, so this is a "
              "ranking by score alone until sales-call questions are added (bank.py add --sales-call).\n")
    scored = [r for r in rows if r["total"]]
    if not scored:
        print(f"No unwritten question has all four factors scored ({len(rows)} unwritten). Nothing to recommend.")
        return 1

    def vol(r):
        v = r["ahrefs_volume_us"].upper()
        m = re.fullmatch(r"([\d.]+)(K?)", v)
        return float(m.group(1)) * (1000 if m.group(2) else 1) if m else -1

    scored.sort(key=lambda r: (r["from_sales_call"] != "yes", -int(r["total"]), -vol(r), int(r["id"])))
    blocked = []
    for r in scored:
        if r["evidence_by"] != "human":
            blocked.append(r)
            continue
        if blocked:
            print("Refusing to recommend: these rank above the best confirmed question, and their evidence "
                  "score is unconfirmed. Confirm or rescore them first:")
            for b in blocked:
                print(f"  {b['id']:>4}  total {b['total']}  evidence {b['evidence_score']} ({b['evidence_by']})  {b['question']}")
            return 1
        print(f"Top unwritten question: {r['id']}  total {r['total']}/12  "
              f"(demand {r['demand_score']}, gap {r['gap_score']}, incumbent {r['incumbent_score']}, "
              f"evidence {r['evidence_score']})  sales call: {r['from_sales_call']}  "
              f"Ahrefs US: {r['ahrefs_volume_us']}\n  {r['question']}\n  {r['ai_form']}")
        return 0
    print("Every scored question's evidence score is unconfirmed. Nothing to recommend.")
    return 1


COMMANDS = {"rescore": rescore, "set": set_score, "confirm": confirm, "shortlist": shortlist,
            "add": add, "top": top}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print(__doc__)
        sys.exit(2)
    sys.exit(COMMANDS[sys.argv[1]](sys.argv))
