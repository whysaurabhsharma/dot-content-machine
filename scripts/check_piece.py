#!/usr/bin/env python3
"""check_piece.py - run the 25-check gate from CLAUDE.md on one piece.

Usage:
    python scripts/check_piece.py pieces/ai-analyst-follow-up-questions.md
    python scripts/check_piece.py --post posts/ai-analyst-follow-up-questions-posts.md

--post checks each post in a posts/ file against stage 7 and style rule 17
(P1-P6), plus the evidence checks a post shares with its piece: 15 (numbers
against the piece's figures file), 17 (assumptions, superseded ones included)
and 19 (brackets, placeholders, banned words).

The piece is markdown with front matter (title, seo_title, meta, slug, queries,
playbook_url, figures, reverse_links). Each check prints PASS, FAIL, PARTIAL or
HUMAN; HUMAN lines need a person, using the gate list in CLAUDE.md.
Exit code 1 if any check fails.
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FACTS = ROOT / "facts" / "dot-facts.md"
CTA = "If this excites you, we'd love to hear from you. Get in touch."
BANNED = ["unlock", "leverage", "seamless", "robust", "game-changer", "revolutionary", "delve",
          "in today's fast-paced world", "it's important to note", "at the end of the day"]
STOP = {"a", "an", "the", "to", "of", "in", "for", "and", "or", "how", "is", "on", "with", "your", "you", "best", "vs"}
QUESTION_WORDS = ("how ", "what ", "why ", "when ", "which ", "who ", "is ", "are ", "can ", "do ", "does ", "should ")
PROMISE = re.compile(r"by the end|you will have|you'll have|you will know|you'll know|you will get|you'll get", re.I)
MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"
DATE = re.compile(rf"\b\d{{1,2}} (?:{MONTHS})(?: \d{{4}})?\b|\b(?:{MONTHS}) \d{{1,2}}(?:, \d{{4}})?\b|\b\d{{4}}-\d{{2}}-\d{{2}}\b")


# ---------- parsing ----------
def unquote(s):
    """Strip one matching pair of surrounding double quotes, not a quote that ends a value
    ('anchor "x"' kept its closing quote stripped until 1 November 2026)."""
    return s[1:-1] if len(s) >= 2 and s[0] == s[-1] == '"' else s


def parse_front_matter(text):
    if not text.startswith("---"):
        return {}, text
    _, fm, body = text.split("---", 2)
    meta, key = {}, None
    for line in fm.strip().splitlines():
        if re.match(r"^\s+-\s+", line) and key:
            meta.setdefault(key, []).append(unquote(line.split("-", 1)[1].strip()))
        elif ":" in line:
            key, val = line.split(":", 1)
            key, val = key.strip(), unquote(val.strip())
            meta[key] = val if val else []
    return meta, body


def clean(t):
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", t)
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)
    t = t.replace("**", "").replace("`", "")
    t = re.sub(r"(?<!\w)\*(?!\s)([^*]+)\*(?!\w)", r"\1", t)
    return t.strip()


# Fenced code is quoted output (Dot's SQL), not the writer's prose: kept whole, left out
# of every prose check, and required verbatim from the piece's run file (check 15).
FENCE = re.compile(r"^```[^\n]*\n.*?^```[ \t]*$", re.M | re.S)
CODE = "\u0000code\u0000"


def blocks_of(body):
    out = []
    codes = FENCE.findall(body)
    body = FENCE.sub("\n\n" + CODE + "\n\n", body)
    for raw in re.split(r"\n\s*\n", body.strip()):
        b = raw.strip()
        if not b:
            continue
        if b == CODE:
            kind, b = "code", codes.pop(0)
        elif b.startswith("## "):
            kind = "h2"
        elif b.startswith("|"):
            kind = "table"
        elif b.startswith("!["):
            kind = "image"
        elif b == "---":
            kind = "hr"
        elif re.match(r"^\d+\.\s", b):
            kind = "olist"
        elif b.startswith("- "):
            kind = "ulist"
        elif b.startswith("*") and b.endswith("*") and not b.startswith("**"):
            kind = "italic"
        else:
            kind = "para"
        out.append((kind, b))
    return out


def sentences(text):
    s = re.sub(r"(\d)\.(\d)", r"\1<D>\2", text.replace("\n", " "))
    parts = re.split(r'(?<=[.!?]["\u201d])\s+(?=[A-Z"\u201c])|(?<=[.!?])\s+(?=[A-Z"\u201c])', s)
    return [p.replace("<D>", ".") for p in parts if p.strip()]


def words(t):
    return re.findall(r"\S+", t)


def tokens(t):
    return [w for w in re.findall(r"[a-z0-9]+", t.lower()) if w not in STOP]


def norm_number(s):
    s = s.replace(",", "").rstrip("%")
    try:
        return round(float(s), 6)
    except ValueError:
        return None


def numbers_in(t):
    t = DATE.sub(" ", t)
    t = re.sub(r"\b(?:Stage|Run|run|stage|[Qq]uestions?)\s+\d+", " ", t)
    found = []
    # v1.8.19: a range's upper end ("10-16%") was skipped, because a number after a hyphen isn't read.
    # Read both ends of a range explicitly; ranges in the figures file are split the same way.
    for m in re.finditer(r"(?<![\w/.\-])(\d[\d,]*(?:\.\d+)?)%?\s*[-–]\s*(\d[\d,]*(?:\.\d+)?)%?", t):
        for raw in m.groups():
            v = norm_number(raw)
            if v is not None and not (raw.isdigit() and 1990 <= int(raw) <= 2035):
                found.append((raw, v))
    for m in re.finditer(r"(?<![\w/.\-])\d[\d,]*(?:\.\d+)?%?", t):
        raw = m.group(0).rstrip(",")
        v = norm_number(raw)
        if v is None:
            continue
        if raw.isdigit() and 1990 <= int(raw) <= 2035:
            continue  # a year
        found.append((raw, v))
    return found


def section_keywords(section, column):
    """(id, keyword) pairs from one table section of facts/dot-facts.md; column is the Keywords index."""
    if not FACTS.exists():
        return []
    kws, inside = [], False
    for line in FACTS.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            inside = line.strip() == section
            continue
        if inside and (line.startswith("| A") or line.startswith("| P-")):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) > column and cells[column] not in ("", "—", "-"):
                kws += [(cells[0], k.strip().lower()) for k in cells[column].split(",") if k.strip()]
    return kws


def assumption_keywords():
    return section_keywords("## Assumptions", 3)


def pending_keywords():
    """Keywords of assumptions pending Dot's confirmation (v1.8.16). A sentence using one needs its label:
    "assumption" (untested) or "not re-checked since" (observed once)."""
    return section_keywords("## Pending Dot's confirmation", 3)


def superseded_keywords():
    """Keywords of assumptions a later observation contradicted. Using one fails check 17, labelled or not."""
    return section_keywords("## Superseded", 5)


# ---------- evidence checks shared by pieces and posts (15, 17, 19) ----------
def check_figures(text, fig_file, body=""):
    name = "Every number has a Figures row"
    if not fig_file or not fig_file.exists():
        return "FAIL", name, "no figures file found"
    with open(fig_file, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    vals = {norm_number(r["value"]) for r in rows}
    for r in rows:  # a range value ("10-15") also vouches for each of its ends
        for end in re.split(r"\s*[-–]\s*", r["value"] or ""):
            if norm_number(end) is not None:
                vals.add(norm_number(end))
    # A number from a cited publication (hard rule 4) must link its source in the piece.
    published = {}
    # a value that also has a row from our own census or runs may be that number, so it isn't held to a link
    own = {norm_number(r["value"]) for r in rows if not (r.get("where_computed") or "").startswith("published:")}
    for r in rows:
        m = re.match(r"published:\s*(\S+?),?\s", (r.get("where_computed") or "") + " ")
        if m:
            published.setdefault(norm_number(r["value"]), set()).add(m.group(1))
    found = numbers_in(text)
    missing = sorted({raw for raw, v in found if v not in vals})
    # v1.8.8: the source is linked somewhere in the piece, at the company's first substantive mention
    # or in its table row, so every claim is one tap from its source without a wall of repeated links.
    # (v1.8.6 required the same sentence; that repeated a company's link four or five times on a phone.)
    unlinked = sorted({raw for raw, v in found
                       if v in published and v not in own and not any(u in body for u in published[v])})
    detail = f"{len(found)} numbers checked; not in Figures: {missing if missing else 'none'}"
    if published:
        detail += f"; published but source not linked in the piece: {unlinked if unlinked else 'none'}"
    return ("PASS" if not missing and not unlinked else "FAIL", name, detail + ". verify_sources.py: run separately")


def check_assumptions(prose):
    unlabelled = []
    for aid, kw in assumption_keywords():
        for s in sentences(prose):
            if kw in s.lower() and "assumption" not in s.lower():
                unlabelled.append(f"{aid} \"{kw}\": {s[:50]}")
    # A P label may sit in the claim's sentence or the one after it ("…says: '…95%.' Assumption: …").
    labelled_by = lambda s: "assumption" in s.lower() or "not re-checked since" in s.lower()
    for aid, kw in pending_keywords():
        ss = sentences(prose)
        for i, s in enumerate(ss):
            low = s.lower()
            if kw in low and not labelled_by(s) and not (i + 1 < len(ss) and labelled_by(ss[i + 1])):
                unlabelled.append(f"{aid} \"{kw}\": {s[:50]}")
    superseded = []
    for aid, kw in superseded_keywords():
        for s in sentences(prose):
            if kw in s.lower():
                superseded.append(f"{aid} \"{kw}\": {s[:50]}")
    labelled = len(re.findall(r"\bAssumption\b", prose))
    return ("PASS" if not unlabelled and not superseded else "FAIL",
            "Product claims evidenced, confirmed or labelled \"Assumption\"",
            f"{labelled} labelled" + (f"; unlabelled: {unlabelled}" if unlabelled else "; none unlabelled")
            + (f"; rests on a superseded assumption: {superseded}" if superseded else "; none superseded"))


def check_banned(body, prose):
    bad_brackets = re.findall(r"\[[^\]]+\](?!\()", body)
    placeholders = re.findall(r"\b(?:TODO|TBD|TK|XXX+|lorem ipsum)\b|\[UNVERIFIED", body)
    banned = [w for w in BANNED if re.search(rf"\b{re.escape(w)}\b", prose, re.I)]
    ok = not bad_brackets and not placeholders and not banned
    return ("PASS" if ok else "FAIL", "No brackets, placeholders or banned words",
            f"brackets {bad_brackets or 'none'}; placeholders {placeholders or 'none'}; banned {banned or 'none'}")


NUMBER_WORDS = r"\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|hundred|thousand|million|half)\b"


def entity_sentences():
    """The sentences of facts/dot-entity.md's entity paragraph (hard rule 23)."""
    f = ROOT / "facts" / "dot-entity.md"
    if not f.exists():
        return []
    quote = next((l[1:].strip() for l in f.read_text(encoding="utf-8").splitlines() if l.startswith(">")), "")
    return [s.strip().lower() for s in re.split(r"(?<=\.)\s+", quote) if s.strip()]


def check_entity(prose):
    """A sentence that defines Dot ("Dot, an ...", "Dot is a ...") must use the entity file's words."""
    ents = entity_sentences()
    found = [m.group(0) for m in re.finditer(r"\bDot(?:,\s+(?:an?|the|your)\s|\s+is\s+(?:an?|the|your)\s)[^.;:]*", prose)]
    bad = [s for s in found if not any(s.lower().rstrip(" ,") in e or e.rstrip(".") in s.lower() for e in ents)]
    return found, bad


def check_lift(slug):
    """Check 25: the blind lift-tester's lifted lines reproduce the outline's quotable line in substance."""
    name = "Lift-tester reproduces the outline's quotable line"
    outline = ROOT / "pieces" / f"{slug}-outline.md"
    q = re.search(r"^\**Quotable line:?\**:?\s*(.+)$", outline.read_text(encoding="utf-8"), re.M | re.I) if outline.exists() else None
    if not q:
        return "HUMAN", name, "the outline has no quotable line (it predates v1.8); judge the lift test by hand (check 23)"
    line = re.sub(r"\s*\((?:figures?|ID|IDs?)[^)]*\)\s*$", "", q.group(1).strip(), flags=re.I).strip(" *\"“”")
    lift = ROOT / "reviews" / slug / "lift-tester.md"
    if not lift.exists():
        return "HUMAN", name, f"reviews/{slug}/lift-tester.md not written yet. Quotable line: \"{line}\""
    # Pair quote marks line by line, then keep quotes of 15+ characters. One regex over the whole file
    # with the length floor inside it fell out of step after a short quote ("how to") and missed a
    # verbatim lift on the next line (F, 1 November 2026).
    lifted = [q for ln in lift.read_text(encoding="utf-8").splitlines()
              for q in re.findall(r"[\"“]([^\"”]+)[\"”]", ln) if len(q) >= 15]
    words = lambda s: set(re.findall(r"[a-z0-9]+", s.lower())) - STOP
    nums = lambda s: set(re.findall(r"\d[\d,.]*", s)) | set(w.lower() for w in re.findall(NUMBER_WORDS, s, re.I))
    target_w, target_n = words(line), nums(line)
    best, best_score = "", 0.0
    for l in lifted:
        if target_n and not (target_n & nums(l)):
            continue
        score = len(target_w & words(l)) / max(len(target_w), 1)
        if score > best_score:
            best, best_score = l, score
    ok = best_score >= 0.5
    # The lifted line must still be in the piece: a lift-tester report older than a revision can
    # quote a sentence the piece no longer has (F, 1 November 2026: "both correct" was revised out).
    piece = ROOT / "pieces" / f"{slug}.md"
    norm = lambda s: re.sub(r"\s+", " ", re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)).replace("**", "").strip(" .")
    if ok and piece.exists() and norm(best) not in norm(piece.read_text(encoding="utf-8")):
        return ("FAIL", name, f"best lifted match {best_score:.0%}, but that line is no longer in the piece: "
                f"\"{best[:70]}\". Re-run the lift-tester on the current draft")
    return ("PASS" if ok else "FAIL", name,
            f"quotable line: \"{line}\"; best lifted match {best_score:.0%}" + (f": \"{best[:70]}\"" if best else ": none with its number"))


# ---------- the checks ----------
def run(path):
    text = Path(path).read_text(encoding="utf-8")
    meta, body = parse_front_matter(text)
    fmt = (meta.get("format") or "research").strip().lower()
    blocks = blocks_of(body)
    prose_kinds = ("para", "olist", "ulist", "italic")
    h2s = [b[3:].strip() for k, b in blocks if k == "h2"]
    first_h2 = next((i for i, (k, _) in enumerate(blocks) if k == "h2"), len(blocks))

    # prose excludes headings, tables, images and the caption that follows an image
    prose_blocks = []
    for i, (k, b) in enumerate(blocks):
        if k in prose_kinds and not (k == "italic" and i > 0 and blocks[i - 1][0] == "image"):
            prose_blocks.append(b)
    items = []
    for b in prose_blocks:
        for line in b.splitlines():
            items.append(clean(re.sub(r"^(\d+\.|-)\s+", "", line)))
    prose = "\n\n".join(items)
    sents = sentences(" ".join(items))
    lens = [len(words(s)) for s in sents]
    results = []

    def add(n, status, name, detail=""):
        results.append((n, status, name, detail))

    queries = meta.get("queries", []) or []
    if isinstance(queries, str):
        queries = [q.strip() for q in queries.strip("[]").split(",")]
    title = meta.get("title", "")

    def query_hit(t):
        best = 0.0
        for q in queries:
            qt = set(tokens(q))
            if qt:
                best = max(best, len(qt & set(tokens(t))) / len(qt))
        return best

    # 1 title (v1.8.4: a teardown title is 8-13 words; other formats' lengths are judged by a person)
    n_title = len(title.split())
    shape_bad = fmt == "teardown" and not 8 <= n_title <= 13
    cue = re.search(r"\b(test|checklist|guide|how to|measured|cost|fix|steps|template|tested|compared)\b", title, re.I)
    hit = query_hit(title)
    seo_hit = query_hit(meta.get("seo_title", ""))
    if shape_bad:
        add(1, "FAIL", "Title uses buyers' words and says what the reader gets",
            f"a teardown title is 8-13 words (style rule 15); this one is {n_title}")
    elif hit < 0.6 and seo_hit >= 0.6:
        # v1.8.3: a claim title may leave the buyers' words to the SEO title, which is what search shows.
        add(1, "PARTIAL", "Title uses buyers' words and says what the reader gets",
            f"claim title, query words {hit:.0%}; the SEO title carries them ({seo_hit:.0%}). "
            "The headline test must pass on this title, and the lede must carry the promise (check 2)")
    elif hit < 0.6:
        add(1, "FAIL", "Title uses buyers' words and says what the reader gets",
            f"query words {hit:.0%} (need 60%); promise word: {'yes' if cue else 'none'}")
    elif cue:
        add(1, "PASS", "Title uses buyers' words and says what the reader gets",
            f"query words {hit:.0%}; promise word \"{cue.group(0)}\". Human: confirm the three-second test")
    else:
        # A flat claim can say what the reader gets by stating the finding (style rule 15).
        # The script can't judge that; the headline test does, and the lede must carry the promise (check 2).
        add(1, "PARTIAL", "Title uses buyers' words and says what the reader gets",
            f"query words {hit:.0%}; claim title, no promise word: the headline test must pass on this title, "
            "and the lede must carry the promise (check 2)")

    # 2 opening promise
    opening = clean(next((b for k, b in blocks if k == "para"), ""))
    first60 = " ".join(words(opening)[:60])
    add(2, "PASS" if PROMISE.search(first60) else "FAIL", "First 60 words say what the reader will have",
        f"opening is {len(words(opening))} words; promise {'found' if PROMISE.search(first60) else 'missing'}")

    # 3 SEO fields
    seo, desc, slug = meta.get("seo_title", ""), meta.get("meta", ""), meta.get("slug", "")
    slug_words = len([w for w in slug.split("-") if w])
    ok3 = 0 < len(seo) <= 60 and query_hit(seo) >= 0.6 and 0 < len(desc) <= 155 and 4 <= slug_words <= 6
    add(3, "PASS" if ok3 else "FAIL", "SEO title has the query; meta under 155; slug 4-6 words",
        f"SEO title {len(seo)} chars, query words {query_hit(seo):.0%}; meta {len(desc)} chars; slug {slug_words} words")

    # 4 bold lede
    lede = next((b for k, b in blocks if k == "para"), "")
    bold = lede.startswith("**") and lede.rstrip().endswith("**")
    named = next((m for m in re.finditer(r"(?<=[a-z,] )[A-Z][a-zA-Z]+", clean(lede))
                  if m.group(0) not in {"AI", "I", "BI", "SQL", "US", "UK", "EU"}), None)
    ok4 = bold and re.search(r"\d", lede) and named
    add(4, "PASS" if ok4 else "FAIL", "Bold lede with a number and a named thing",
        f"bold {bold}; number {bool(re.search(r'[0-9]', lede))}; named thing {named.group(0) if named else 'none'}")

    # 5 pocket guide
    pocket = [b for k, b in blocks[:first_h2] if k == "olist"]
    n_items = len(pocket[0].splitlines()) if pocket else 0
    add(5, "PASS" if 5 <= n_items <= 8 else "FAIL", "Pocket guide of five to eight lines", f"{n_items} lines before the first H2")

    # 6-8 length
    n_words = len(words(prose))
    lo, hi = {"research": (900, 1300), "teardown": (1000, 1600), "guide": (1000, 1900)}.get(fmt, (0, 0))
    label6 = "900-1,300 words" if fmt == "research" else (f"{lo:,}-{hi:,} words ({fmt})" if hi else f"unknown format '{fmt}'")
    add(6, "PASS" if lo <= n_words <= hi else "FAIL", label6, f"{n_words} words")
    avg = sum(lens) / len(lens) if lens else 0
    long = [s[:60] for s, n in zip(sents, lens) if n > 25]
    add(7, "PASS" if avg < 18 and not long else "FAIL", "Sentences average under 18 words; none over 25",
        f"average {avg:.1f}; longest {max(lens) if lens else 0}" + (f"; over 25: {long}" if long else ""))
    over = [clean(b)[:50] for k, b in blocks if k == "para" and len(sentences(clean(b))) > 4]
    add(8, "PASS" if not over else "FAIL", "No paragraph over four sentences", f"{len(over)} over" + (f": {over}" if over else ""))

    # 9 H2s
    bad = [h for h in h2s if h.endswith("?") or h.lower().startswith(QUESTION_WORDS)]
    add(9, "PASS" if not bad else "FAIL", "Every H2 is a claim, not a question", f"{len(h2s)} H2s" + (f"; questions: {bad}" if bad else ""))

    # 10 table and chart
    has_table = any(k == "table" for k, _ in blocks)
    img = [(i, b) for i, (k, b) in enumerate(blocks) if k == "image"]
    alt_ok = bool(img) and bool(re.match(r"!\[\s*[^\]\s][^\]]*\]", img[0][1]))
    cap_ok = bool(img) and img[0][0] + 1 < len(blocks) and blocks[img[0][0] + 1][0] == "italic" \
        and bool(DATE.search(blocks[img[0][0] + 1][1]))
    if fmt == "research":
        add(10, "PASS" if has_table and alt_ok and cap_ok else "FAIL", "One table; one chart with alt text and a dated caption",
            f"table {has_table}; chart {bool(img)}; alt text {alt_ok}; dated caption {cap_ok}")
    else:
        chart_ok = not img or (alt_ok and cap_ok)  # any chart present must be complete
        tables = [b for k, b in blocks if k == "table"]
        census = max((len(tb.splitlines()) - 2 for tb in tables), default=0)
        linked = max((sum(1 for l in tb.splitlines()[2:] if re.search(r"\]\(https?://", l)) for tb in tables), default=0)
        steps = next((b for k, b in blocks[first_h2:] if k == "olist"), "")
        n_steps = len(steps.splitlines()) if steps else 0
        verbs = bool(steps) and all(not re.match(r"^\d+\.\s+(The|A|An|This|It|We|Our|Your)\b", l) for l in steps.splitlines())
        ok10 = {"teardown": census >= 5 and linked == census and chart_ok,
                "guide": 5 <= n_steps <= 9 and verbs and chart_ok}.get(fmt, False)
        add(10, "PASS" if ok10 else "FAIL", f"Body for format {fmt} (style rule 5)",
            f"tables {len(tables)}; census rows {census}, linked {linked}; chart {bool(img)}, complete {chart_ok}; "
            f"steps {n_steps}, verb-first {verbs}")

    # 11 caveats
    try:
        ci = next(i for i, (k, b) in enumerate(blocks) if k == "h2" and "things to keep in mind" in b.lower())
        n_cav = len(blocks[ci + 1][1].splitlines()) if blocks[ci + 1][0] == "ulist" else 0
    except StopIteration:
        n_cav = 0
    add(11, "PASS" if 2 <= n_cav <= 4 else "FAIL", "One caveats box with two to four caveats", f"{n_cav} caveats")

    # 12 Where Dot fits
    wdf_i = next((i for i, (k, b) in enumerate(blocks) if k == "h2" and "where dot fits" in b.lower()), None)
    if wdf_i is None:
        add(12, "FAIL", "\"Where Dot fits\" last, under 80 words, with a docs link", "section missing")
    else:
        sec = []
        for k, b in blocks[wdf_i + 1:]:
            if k in ("h2", "hr"):
                break
            sec.append(b)
        raw = "\n".join(sec)
        n = len(words(clean(raw)))
        last = h2s[-1].lower().startswith("where dot fits")
        docs = "docs.getdot.ai" in raw
        ok = last and n < 80 and docs
        status = "PASS" if ok else ("PARTIAL" if last and n < 80 else "FAIL")
        add(12, status, "\"Where Dot fits\" last, under 80 words, with a docs link",
            f"last H2 {last}; {n} words; docs link {docs}")

    # 13 ending
    prose_tail = [b for k, b in blocks if k in ("para", "italic", "olist", "ulist")]
    cta_ok = bool(prose_tail) and clean(prose_tail[-1]).replace("\u2019", "'") == CTA
    pen = clean(prose_tail[-2]) if len(prose_tail) > 1 else ""
    imperative = bool(pen) and pen.split()[0] not in ("The", "A", "An", "This", "It", "I", "We", "Our", "There")
    add(13, "PASS" if cta_ok and imperative else "FAIL", "Ends on an instruction, then the CTA",
        f"CTA {cta_ok}; instruction before it: \"{pen[:45]}\"")

    # 14 voice
    unquoted = re.sub(r'["\u201c][^"\u201d]*["\u201d]', " ", prose)  # quotes are someone else's voice
    we = len(re.findall(r"\b(we|our|us)\b", unquoted, re.I)) - 1  # the CTA's "we" is allowed
    i_count = len(re.findall(r"\bI\b", unquoted))
    add(14, "HUMAN", "\"We\" means Dot", f"\"we/our/us\" outside the CTA: {max(we, 0)}; \"I\": {i_count}")

    # 15 figures
    fig_path = meta.get("figures", "")
    table_text = []
    for k, b in blocks:
        if k == "table":
            for line in b.splitlines()[2:]:
                cells = [c.strip() for c in line.strip("|").split("|")]
                table_text.append(" ".join(cells[1:]))
    status, name, detail = check_figures(prose + "\n" + "\n".join(table_text), (ROOT / fig_path) if fig_path else None, body)
    run_file = (ROOT / "runs" / (Path(fig_path).name.removesuffix("-figures.csv") + "-run.md")) if fig_path else None
    run_text = run_file.read_text(encoding="utf-8") if run_file and run_file.exists() else ""

    def as_lines(t):  # line endings and trailing spaces normalised; indentation kept
        return "\n".join(l.rstrip() for l in t.splitlines())
    run_norm = "\n" + as_lines(run_text) + "\n"
    # Each code block must appear in the run file whole, as consecutive full lines:
    # lines borrowed from different queries in the same run file don't pass.
    not_in_run = [inner.split("\n")[0].strip() + (" …" if "\n" in inner else "")
                  for k, b in blocks if k == "code"
                  for inner in [as_lines("\n".join(b.splitlines()[1:-1])).strip("\n")]
                  if inner and "\n" + inner + "\n" not in run_norm]
    if not_in_run:
        status, detail = "FAIL", detail + f"; code not verbatim in {run_file.name if run_file else 'run file'}: {not_in_run}"
    add(15, status, name, detail)

    add(16, "HUMAN", "Findings from this run, a cited run of ours, or a cited publication (rule 4); no untested remedy (rule 19)",
        "check against the Run Log and the sources")
    st17, nm17, dt17 = check_assumptions(prose)
    ent_found, ent_bad = check_entity(prose)
    if ent_bad:
        st17, dt17 = "FAIL", dt17 + f"; Dot described in words not in facts/dot-entity.md (hard rule 23): {[s[:50] for s in ent_bad]}"
    elif ent_found:
        dt17 += f"; {len(ent_found)} definition(s) of Dot, all in facts/dot-entity.md's words"
    add(17, st17, nm17, dt17)
    add(18, "HUMAN", "Dataset and licence recorded in Sources", "Sources tab")
    st19, nm19, dt19 = check_banned(FENCE.sub("", body), prose)
    # v1.8.20: the front matter must parse as YAML. Our own parser splits each line at its first
    # colon and so read A's broken "title_approved_by" fine, but Webflow imports and editors use real
    # YAML; an unparseable front matter breaks an import, not a sentence, so no reader would catch it.
    try:
        import yaml
        yaml.safe_load(text.split("---", 2)[1]) if text.startswith("---") else None
    except ImportError:
        st19, dt19 = "FAIL", dt19 + "; PyYAML not installed, so the front matter can't be checked (pip install pyyaml)"
    except Exception as e:
        st19, dt19 = "FAIL", dt19 + f"; front matter is not valid YAML: {str(e).splitlines()[0]} (quote any value containing a colon, #, or a leading quote)"
    rev_on = meta.get("reviewed_on", "")
    if rev_on:
        dt19 += f"; reviewed_on {rev_on}"
    # v1.8.17: a named author needs Dot's recorded approval beside it (hard rule 22).
    author, approved = meta.get("author", ""), meta.get("author_approved_by", "")
    if author and not approved:
        st19, dt19 = "FAIL", dt19 + f"; byline '{author}' has no author_approved_by (hard rule 22)"
    elif author:
        dt19 += f"; byline {author}, approved by {approved}"
    add(19, st19, nm19, dt19)

    # 20 internal links
    urls = re.findall(r"\]\((https?://[^)\s]+)\)", body)
    internal = sorted({u.rstrip("/") for u in urls if "getdot.ai" in u})
    playbook = meta.get("playbook_url", "").rstrip("/")
    ok20 = len(internal) >= 5 and playbook in internal
    add(20, "PASS" if ok20 else "FAIL", "Five or more internal links, including the Playbook stage",
        f"{len(internal)} unique internal; Playbook linked {playbook in internal}. Then run verify_sources.py")

    rev = meta.get("reverse_links", []) or []
    add(21, "PASS" if len(rev) >= 3 else "FAIL", "Three reverse links listed", f"{len(rev)} listed")
    add(22, "HUMAN", "READER pass done; stopping points fixed", "prompts/04-reader.md")
    add(23, "HUMAN", "Lift test in Perplexity and Claude", "prompts/06-edit.md")
    add(24, "HUMAN", "Read aloud once, on a phone", "")
    add(25, *check_lift(Path(path).stem))

    print(f"\ncheck_piece.py  {path}\n")
    for n, st, name, detail in results:
        print(f"{n:>2}  {st:<7} {name}\n             {detail}")
    counts = {s: sum(1 for r in results if r[1] == s) for s in ("PASS", "FAIL", "PARTIAL", "HUMAN")}
    print(f"\n{counts['PASS']} pass, {counts['FAIL']} fail, {counts['PARTIAL']} partial, {counts['HUMAN']} for a human\n")
    return 1 if counts["FAIL"] else 0


# ---------- posts ----------
POST_HEADING = re.compile(r"^#{1,2} (Post \w+)\b(.*)$", re.M)
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿️]")
LABELLED = re.compile(r"^\*\*[^*]+:\*\*")  # "**First comment:**", "**Image:**"


def post_figures(heading, h1, path):
    """The figures file of a post's piece. Tried in order: "piece N" in the post heading,
    a slug in the heading (a "·"-separated part naming figures/<slug>-figures.csv),
    "piece N" in the file's H1, then the slug in the file name (posts/<slug>-posts.md)."""
    def by_number(t):
        m = re.search(r"\bpiece (\d+)", t, re.I)
        return ROOT / "figures" / f"piece-{m.group(1)}-figures.csv" if m else None

    def by_slug(t):
        for part in re.split(r"[·|]", t.lstrip("# ")):
            f = ROOT / "figures" / f"{part.strip()}-figures.csv"
            if part.strip() and f.exists():
                return f
        return None

    stem = Path(path).stem
    from_name = ROOT / "figures" / f"{stem[:-len('-posts')]}-figures.csv" if stem.endswith("-posts") else None
    for f in (by_number(heading), by_slug(heading), by_number(h1), from_name):
        if f is not None:
            return f
    return None


def run_posts(path):
    """Check every post in a posts/ file: CLAUDE.md stage 7 and style rule 17, plus checks 15, 17 and 19.

    A post's figures are its piece's, found by post_figures().
    """
    text = Path(path).read_text(encoding="utf-8")
    h1 = re.search(r"^# .*$", text, re.M)
    heads = list(POST_HEADING.finditer(text))
    headings = [m.start() for m in re.finditer(r"^#{1,2} ", text, re.M)]
    if not heads:
        print(f"\ncheck_piece.py --post  {path}\n\nNo post headings found (\"# Post X\" or \"## Post X\").\n")
        return 1
    failed = 0
    for i, h in enumerate(heads):
        end = next((s for s in headings if s > h.start()), len(text))  # a post ends at the next heading
        paras = [p.strip() for p in re.split(r"\n\s*\n", text[h.end():end]) if p.strip()]
        labelled = [p for p in paras if LABELLED.match(p)]
        body = [p for p in paras if not LABELLED.match(p)]
        body = ["\n".join(re.sub(r"^(\d+\.|-)\s+", "", line) for line in p.splitlines()) for p in body]
        prose = "\n\n".join(clean(p) for p in body)
        fig = post_figures(h.group(0), h1.group(0) if h1 else "", path)
        results = []

        def add(n, status, name, detail=""):
            results.append((n, status, name, detail))

        n_words = len(words(prose))
        add("P1", "PASS" if n_words < 150 else "FAIL", "Under 150 words", f"{n_words} words")
        early = numbers_in("\n\n".join(clean(p) for p in body[:3]))
        add("P2", "PASS" if early else "FAIL", "A number within the first three lines",
            f"first number: {early[0][0] if early else 'none'}")
        tags, emoji = re.findall(r"(?<![\w&])#\w+", prose), EMOJI.findall(prose)
        add("P3", "PASS" if not tags and not emoji else "FAIL", "No hashtags, no emoji",
            f"hashtags {tags or 'none'}; emoji {emoji or 'none'}")
        body_urls = re.findall(r"https?://\S+", "\n".join(body))
        comment = next((p for p in labelled if p.lower().startswith("**first comment:**")), "")
        utm = re.search(r"https?://\S+utm_source=", comment)
        add("P4", "PASS" if utm and not body_urls else "FAIL", "Link only in the first comment, with a UTM",
            f"links in body: {len(body_urls)}; first comment has UTM link: {bool(utm)}")
        last = body[-1].lower() if body else ""
        delivers = bool(re.search(r"\blink\b|\bthe piece\b|\bfirst comment\b", last))
        # v1.8.15: what the link delivers may sit in the first comment, beside the link, so the
        # post can end on its strongest line. The comment must say it in words before the URL.
        said = re.sub(r"^\*\*first comment:\*\*\s*", "", comment.strip(), flags=re.I).split("http")[0].strip(" :")
        in_comment = len(said.split()) >= 4
        add("P5", "PASS" if delivers or in_comment else "FAIL", "Says what the link delivers (last line or first comment)",
            f"last line: {clean(body[-1])[:60] if body else 'none'}" + (f"; first comment: {said[:60]}" if in_comment else ""))
        # v1.8.13: a post carries no links (the link is in the first comment, to its piece), so a
        # published number's source is looked for in the piece the post links to.
        piece_md = ROOT / "pieces" / (fig.name[:-len("-figures.csv")] + ".md") if fig else None
        piece_body = piece_md.read_text(encoding="utf-8") if piece_md and piece_md.exists() else ""
        add(15, *check_figures(prose, fig, piece_body))
        add(17, *check_assumptions(prose))
        add(19, *check_banned("\n\n".join(body), prose))
        add("P6", "HUMAN", "Three first lines tried; the most specific kept", "prompts/07-linkedin.md")

        print(f"\ncheck_piece.py --post  {path}  -  {h.group(1)}"
              f"  (figures: {fig.relative_to(ROOT).as_posix() if fig else 'piece not named'})\n")
        for n, st, name, detail in results:
            print(f"{n:>3}  {st:<7} {name}\n              {detail}")
        counts = {s: sum(1 for r in results if r[1] == s) for s in ("PASS", "FAIL", "HUMAN")}
        print(f"\n{counts['PASS']} pass, {counts['FAIL']} fail, {counts['HUMAN']} for a human")
        failed += bool(counts["FAIL"])
    print(f"\n{len(heads) - failed} of {len(heads)} posts with no FAIL\n")
    return 1 if failed else 0


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--post":
        sys.exit(run_posts(sys.argv[2]))
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(run(sys.argv[1]))
