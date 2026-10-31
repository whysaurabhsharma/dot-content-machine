#!/usr/bin/env python3
"""check_piece.py - run the 24-check gate from CLAUDE.md on one piece.

Usage:
    python scripts/check_piece.py pieces/piece-1.md

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
def parse_front_matter(text):
    if not text.startswith("---"):
        return {}, text
    _, fm, body = text.split("---", 2)
    meta, key = {}, None
    for line in fm.strip().splitlines():
        if re.match(r"^\s+-\s+", line) and key:
            meta.setdefault(key, []).append(line.split("-", 1)[1].strip().strip('"'))
        elif ":" in line:
            key, val = line.split(":", 1)
            key, val = key.strip(), val.strip().strip('"')
            meta[key] = val if val else []
    return meta, body


def clean(t):
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", t)
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)
    t = t.replace("**", "").replace("`", "")
    t = re.sub(r"(?<!\w)\*(?!\s)([^*]+)\*(?!\w)", r"\1", t)
    return t.strip()


def blocks_of(body):
    out = []
    for raw in re.split(r"\n\s*\n", body.strip()):
        b = raw.strip()
        if not b:
            continue
        if b.startswith("## "):
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
        if inside and line.startswith("| A"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) > column and cells[column] not in ("", "—", "-"):
                kws += [(cells[0], k.strip().lower()) for k in cells[column].split(",") if k.strip()]
    return kws


def assumption_keywords():
    return section_keywords("## Assumptions", 3)


def superseded_keywords():
    """Keywords of assumptions a later observation contradicted. Using one fails check 17, labelled or not."""
    return section_keywords("## Superseded", 5)


# ---------- the checks ----------
def run(path):
    text = Path(path).read_text()
    meta, body = parse_front_matter(text)
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

    # 1 title
    cue = re.search(r"\b(test|checklist|guide|how to|measured|cost|fix|steps|template|tested|compared)\b", title, re.I)
    hit = query_hit(title)
    if hit >= 0.6 and cue:
        add(1, "PASS", "Title uses buyers' words and says what the reader gets",
            f"query words {hit:.0%}; promise word \"{cue.group(0)}\". Human: confirm the three-second test")
    else:
        add(1, "FAIL", "Title uses buyers' words and says what the reader gets",
            f"query words {hit:.0%} (need 60%); promise word: {'yes' if cue else 'none'}")

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
    add(6, "PASS" if 900 <= n_words <= 1300 else "FAIL", "900-1,300 words", f"{n_words} words")
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
    add(10, "PASS" if has_table and alt_ok and cap_ok else "FAIL", "One table; one chart with alt text and a dated caption",
        f"table {has_table}; chart {bool(img)}; alt text {alt_ok}; dated caption {cap_ok}")

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
    fig_file = (ROOT / fig_path) if fig_path else None
    if not fig_file or not fig_file.exists():
        add(15, "FAIL", "Every number has a Figures row", "no figures file in front matter")
    else:
        with open(fig_file) as f:
            vals = {norm_number(r["value"]) for r in csv.DictReader(f)}
        table_text = []
        for k, b in blocks:
            if k == "table":
                for line in b.splitlines()[2:]:
                    cells = [c.strip() for c in line.strip("|").split("|")]
                    table_text.append(" ".join(cells[1:]))
        found = numbers_in(prose + "\n" + "\n".join(table_text))
        missing = sorted({raw for raw, v in found if v not in vals})
        add(15, "PASS" if not missing else "FAIL", "Every number has a Figures row",
            f"{len(found)} numbers checked; not in Figures: {missing if missing else 'none'}. verify_sources.py: run separately")

    add(16, "HUMAN", "Every finding comes from this dataset's run", "check against the Run Log")

    # 17 assumptions labelled
    unlabelled = []
    for aid, kw in assumption_keywords():
        for s in sentences(prose):
            if kw in s.lower() and "assumption" not in s.lower():
                unlabelled.append(f"{aid} \"{kw}\": {s[:50]}")
    superseded = []
    for aid, kw in superseded_keywords():
        for s in sentences(prose):
            if kw in s.lower():
                superseded.append(f"{aid} \"{kw}\": {s[:50]}")
    labelled = len(re.findall(r"\bAssumption\b", prose))
    add(17, "PASS" if not unlabelled and not superseded else "FAIL",
        "Product claims evidenced, confirmed or labelled \"Assumption\"",
        f"{labelled} labelled" + (f"; unlabelled: {unlabelled}" if unlabelled else "; none unlabelled")
        + (f"; rests on a superseded assumption: {superseded}" if superseded else "; none superseded"))

    add(18, "HUMAN", "Dataset and licence recorded in Sources", "Sources tab")

    # 19 placeholders and banned words
    bad_brackets = re.findall(r"\[[^\]]+\](?!\()", body)
    placeholders = re.findall(r"\b(?:TODO|TBD|TK|XXX+|lorem ipsum)\b|\[UNVERIFIED", body)
    banned = [w for w in BANNED if re.search(rf"\b{re.escape(w)}\b", prose, re.I)]
    ok19 = not bad_brackets and not placeholders and not banned
    add(19, "PASS" if ok19 else "FAIL", "No brackets, placeholders or banned words",
        f"brackets {bad_brackets or 'none'}; placeholders {placeholders or 'none'}; banned {banned or 'none'}")

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

    print(f"\ncheck_piece.py  {path}\n")
    for n, st, name, detail in results:
        print(f"{n:>2}  {st:<7} {name}\n             {detail}")
    counts = {s: sum(1 for r in results if r[1] == s) for s in ("PASS", "FAIL", "PARTIAL", "HUMAN")}
    print(f"\n{counts['PASS']} pass, {counts['FAIL']} fail, {counts['PARTIAL']} partial, {counts['HUMAN']} for a human\n")
    return 1 if counts["FAIL"] else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(run(sys.argv[1]))
