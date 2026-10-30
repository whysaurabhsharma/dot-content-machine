#!/usr/bin/env python3
"""mark_run.py - mark each answer in a run file against the ground truth.

Usage:
    python scripts/mark_run.py <piece>
    python scripts/mark_run.py <piece> --map Q1=Q13b --map Q2=Q05
    python scripts/mark_run.py <piece> --run <run.md> --truth <truth.csv> --figures <figures.csv>

Reads runs/<piece>-run.md (format: facts/run-format.md) and figures/<piece>-truth.csv
(written by ground_truth_from_spec.py). Appends one row per answer to
figures/<piece>-figures.csv and prints "N of M correct". Never writes the run file or
the truth file.

Matching, in this order:
  1. the truth row named with --map;
  2. the truth row with the same id as the run entry;
  3. the truth row with exactly the same question text;
  4. only when none of those exists, the one definition (table, filter, formula)
     whose filter literals are exactly those in the answer's Basis quotes.
Several truth rows sharing one definition is expected (three teams asking the same
metric in different words) and is never treated as ambiguous.

Definitions. The answer is marked under the definition it stated, not the one we
assumed. The candidates are the truth rows with the same formula as the matched row
(for example, average order value over all orders, and over delivered orders). Each
candidate's filter literals ('delivered', '2017') are looked for in the answer's
Basis quotes. The candidate whose literals are exactly the ones the answer stated
is the definition it used. If that's not the matched row, the row says so. A stated
population that no candidate expresses ("shipped orders only") matches no row: the
answer is reported as a different definition, never marked wrong.

Gaps (CLAUDE.md hard rule 12). Under 0.1% of the expected value is rounding, and
counts as correct. Anything larger is a real gap.

The number is the first number in the answer text, skipping dates and years in
dates. The row records the text it was taken from, so a person can check it.
"""
import csv
import datetime as dt
import os
import re
import sys

ROUNDING_PCT = 0.1
FIGURE_FIELDS = ["id", "value", "description", "where_computed", "date"]

HEADING = re.compile(r"^### (\w+): (.*)$", re.M)
FIELD = re.compile(r"^- ([A-Za-z ,]+): (.*)$", re.M)
ANSWER = re.compile(r"\*\*Answer\*\*\s*```text\n(.*?)\n```", re.S)
NUMBER = re.compile(r"(?<![\w.,])[-+]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?%?")
DATE_PART = re.compile(r"\d{4}-\d{2}|\d{2}:\d{2}")
MONTHS = r"(?:January|February|March|April|May|June|July|August|September|October|November|December)"
YEAR_IN_DATE = re.compile(MONTHS + r"\s+(\d{4})")
LITERAL = re.compile(r"'([^']*)'")


def norm(text):
    return " ".join(text.lower().split())


def parse_run(text):
    """Split a run file into entries: id, question, fields, answer text."""
    entries = []
    heads = list(HEADING.finditer(text))
    for i, h in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        nxt = re.search(r"^## ", text[h.end():end], re.M)
        body = text[h.end():h.end() + nxt.start()] if nxt else text[h.end():end]
        fields = {k.strip().lower(): v.strip() for k, v in FIELD.findall(body)}
        answer = ANSWER.search(body)
        entries.append({"id": h.group(1), "question": h.group(2).strip(),
                        "fields": fields, "answer": answer.group(1) if answer else None})
    return entries


def first_number(answer):
    """First number in the answer that isn't part of a date. Returns (value, text) or (None, None)."""
    skip = set()
    for m in DATE_PART.finditer(answer):
        skip.update(range(m.start(), m.end()))
    for m in YEAR_IN_DATE.finditer(answer):
        skip.update(range(m.start(1), m.end(1)))
    for m in NUMBER.finditer(answer):
        if m.start() in skip:
            continue
        token = m.group(0)
        return float(token.rstrip("%").replace(",", "")), token
    return None, None


def stated_basis(fields):
    """The answer's Basis quotes, lower-cased: (all parts joined, population alone).

    The first is None if no basis was stated; the second is "" if no population was.
    """
    quotes = {}
    for part in ("population", "period", "definition"):
        value = fields.get(f"basis, {part}", "")
        if value.lower().startswith("yes"):
            quotes[part] = norm(value[3:].strip(" -\"'"))
    return (" ".join(quotes.values()) or None), quotes.get("population", "")


def definition(row):
    return (row["table"], row["filter"], row["formula"])


def fitting_rows(candidates, basis, population):
    """Candidates whose filter literals are exactly those the answer stated.

    An unfiltered row fits only if the answer stated no population, or one that
    says "all". A stated population the truth rows can't express fits nothing.
    """
    literals = {r["question_id"]: {l.lower() for l in LITERAL.findall(r["filter"])} for r in candidates}
    present = {l for ls in literals.values() for l in ls if l in basis}
    fits = [r for r in candidates if literals[r["question_id"]] == present]
    if fits and not present and population and "all" not in population.split():
        return []
    return fits


def stated_definition(matched, truth, basis, population):
    """The truth row for the definition the answer stated: the matched row if it
    fits, otherwise the one definition that does. Rows sharing a definition count once."""
    candidates = [r for r in truth if r["formula"] == matched["formula"]]
    fits = fitting_rows(candidates, basis, population)
    if matched in fits:
        return matched
    return fits[0] if len({definition(r) for r in fits}) == 1 else None


def mark(entry, truth, mapping):
    """Return (verdict, description, value) for one run entry."""
    f = entry["fields"]
    cls = f.get("classification", "").lower()
    by_text = {r["question"].strip(): r for r in truth}
    by_id = {r["question_id"]: r for r in truth}

    if cls != "answered":
        return "not marked", f"Classification is '{cls or 'missing'}'; no answer to mark", ""
    if entry["answer"] is None:
        return "not marked", "No answer block found in the run file", ""
    value, token = first_number(entry["answer"])
    if value is None:
        return "not marked", "The answer contains no number", ""

    basis, population = stated_basis(f)
    how = ""
    if entry["id"] in mapping:
        matched, how = by_id.get(mapping[entry["id"]]), "--map"
    elif entry["id"] in by_id:
        matched, how = by_id[entry["id"]], "id"
    else:
        matched, how = by_text.get(entry["question"].strip()), "question text"
    if matched is None:
        fits = fitting_rows(truth, basis, population) if basis else []
        if not fits or len({definition(r) for r in fits}) != 1:
            return "not marked", (f"No truth row by id or question text, and the stated basis fits "
                                  f"{len({definition(r) for r in fits})} definitions (answer gave {token})"), value
        matched, how = fits[0], "definition only"
    if matched["error"]:
        return "not marked", f"Truth row {matched['question_id']} failed: {matched['error']}", value

    note = ""
    used = matched
    if basis is None:
        note = "; the answer stated no basis, so it is compared under the asked definition"
    else:
        fit = stated_definition(matched, truth, basis, population)
        if fit is None:
            return ("different definition",
                    f"Answer gave {token}, under a stated basis ('{basis}') that matches no truth row; not marked wrong",
                    value)
        if fit["question_id"] != matched["question_id"]:
            used = fit
            note = (f"; the answer stated a different definition ('{basis}') from the one asked"
                    f" ({matched['question_id']}), so it is compared under {fit['question_id']}")

    expected = float(used["value"])
    gap = abs(value - expected) / abs(expected) * 100 if expected else abs(value)
    kind = "exact" if gap == 0 else "rounding" if gap < ROUNDING_PCT else "real"
    verdict = "correct" if kind != "real" else "real gap"
    if used is not matched and verdict == "correct":
        verdict = "correct under stated definition"
    desc = (f"{entry['id']} vs {used['question_id']} ({used['metric']}), matched by {how}: answer {token}, expected {used['value']} "
            f"{used['unit']}; gap {gap:.4f}% ({kind}); {verdict}{note}")
    return verdict, desc, value


def main(argv):
    if len(argv) < 2 or argv[1].startswith("-"):
        print(__doc__)
        return 2
    piece = argv[1]
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    def opt(name, default):
        return argv[argv.index(name) + 1] if name in argv else default

    run_path = opt("--run", f"runs/{piece}-run.md")
    truth_path = opt("--truth", f"figures/{piece}-truth.csv")
    figures_path = opt("--figures", f"figures/{piece}-figures.csv")
    mapping = dict(argv[i + 1].split("=", 1) for i, a in enumerate(argv) if a == "--map")

    with open(run_path, encoding="utf-8") as fh:
        entries = parse_run(fh.read())
    with open(truth_path, encoding="utf-8") as fh:
        truth = list(csv.DictReader(fh))

    existing = set()
    if os.path.exists(figures_path):
        with open(figures_path, encoding="utf-8") as fh:
            existing = {r["id"] for r in csv.DictReader(fh)}
    ids = [f"MR-{e['id']}" for e in entries]
    already = [i for i in ids if i in existing]
    if already:
        print(f"Already marked in {figures_path}: {', '.join(already)}. Remove those rows to re-mark.")
        return 1

    today = dt.date.today().isoformat()
    rows, counts = [], {}
    for entry, row_id in zip(entries, ids):
        verdict, desc, value = mark(entry, truth, mapping)
        counts[verdict] = counts.get(verdict, 0) + 1
        rows.append({"id": row_id, "value": value, "description": desc,
                     "where_computed": f"mark_run.py: {run_path} {entry['id']} vs {truth_path}", "date": today})
        print(f"{entry['id']:>5}  {verdict:<32}  {desc}")

    new_file = not os.path.exists(figures_path)
    with open(figures_path, "a", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIGURE_FIELDS)
        if new_file:
            w.writeheader()
        w.writerows(rows)

    correct = counts.get("correct", 0) + counts.get("correct under stated definition", 0)
    print(f"\n{correct} of {len(entries)} correct")
    print("  " + "; ".join(f"{k}: {v}" for k, v in sorted(counts.items())))
    print(f"Appended {len(rows)} rows to {figures_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
