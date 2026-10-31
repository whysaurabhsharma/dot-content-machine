#!/usr/bin/env python3
# TRUST: spec files are trusted repo content only. The formula and filter fields are
# run as Python, so a spec is never accepted from outside this repo. A spec from
# anywhere else must be read in full before it is run.
"""ground_truth_from_spec.py - compute every expected value in a spec from the raw CSVs.

Usage:
    python scripts/ground_truth_from_spec.py specs/ai-analyst-follow-up-questions-truth.json
    python scripts/ground_truth_from_spec.py <spec.json> --out figures/<piece>-truth.csv

The spec names the piece, the CSV files and the questions. Each question gives the
table, a filter, a formula, and the unit and grain of the figure:

    {
      "piece": "piece-1",
      "csv": {"orders": "data/olist/olist_orders_dataset.csv",
              "items": "data/olist/olist_order_items_dataset.csv"},
      "questions": [
        {"id": "Q12", "question": "...", "metric": "...",
         "table": "items_x_orders", "filter": "order_status == 'delivered'",
         "formula": "df.price.sum()", "unit": "BRL", "grain": "all item rows"}
      ]
    }

- table: a key of "csv", or "items_x_orders" (items left-joined to orders on order_id).
- filter: a pandas query string (python engine), or "" for every row.
- formula: one expression over df, the filtered table, with pd available.
- family (optional): rows that are rival definitions of one metric share a family.
- signals (optional): phrases an answer uses when it states this row's formula,
  such as "including shipping". mark_run.py reads them.
- follow_up_of (optional): the id of the question this one is asked after, in the same
  chat. Its definition must still be complete on its own: the filters carried over from
  the earlier turn are written into this row's filter.
- asked (optional, default true): false for a rival reading that is computed but not asked,
  so stage_gate.py counts only the questions a batch must ask.
- reviewed_by (top level, optional): set by a person after checking the spec; the run
  waits for it (stage_gate.py).

Every value is computed from the raw CSVs; nothing is hard-coded and no figures file
is read (CLAUDE.md hard rules 2 and 3). A question that can't be computed is written
with its reason, never skipped. Output defaults to figures/<piece>-truth.csv.
"""
import csv
import datetime as dt
import json
import os
import sys

import pandas as pd

FIELDS = ["question_id", "question", "metric", "family", "table", "filter", "formula", "signals",
          "value", "unit", "grain", "row_count", "csv_files", "computed_on", "error"]


def load_tables(csv_paths):
    tables, sources = {}, []
    missing = [p for p in csv_paths.values() if not os.path.exists(p)]
    if missing:
        sys.exit("Missing data file(s): " + ", ".join(missing) + "\n"
                 "The Olist CSVs are not in the repo (data/olist/ is gitignored). Download the dataset from\n"
                 "  https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce\n"
                 "(a free Kaggle account is needed), unzip it, and put the CSVs in data/olist/ under the repo root,\n"
                 "e.g. data/olist/olist_orders_dataset.csv. Then run: python scripts/check_setup.py")
    for name, path in csv_paths.items():
        tables[name] = pd.read_csv(path)
        mtime = dt.datetime.fromtimestamp(os.path.getmtime(path)).isoformat(timespec="seconds")
        sources.append(f"{path} (modified {mtime})")
    if "orders" in tables and "items" in tables:
        tables["items_x_orders"] = tables["items"].merge(
            tables["orders"], on="order_id", how="left", validate="many_to_one")
    return tables, "; ".join(sources)


def compute(q, tables):
    """Return (value, row_count) for one spec question. Raises on any failure."""
    if q["table"] not in tables:
        raise KeyError(f"unknown table {q['table']!r}")
    df = tables[q["table"]]
    if q.get("filter"):
        df = df.query(q["filter"], engine="python")
    value = eval(q["formula"], {"__builtins__": {"len": len}}, {"df": df, "pd": pd})
    if hasattr(value, "item"):
        value = value.item()
    if not isinstance(value, (int, float)):
        raise TypeError(f"formula returned {type(value).__name__}, not a number")
    return value, len(df)


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    with open(argv[1], encoding="utf-8") as f:
        spec = json.load(f)
    out = argv[argv.index("--out") + 1] if "--out" in argv else f"figures/{spec['piece']}-truth.csv"

    missing = [p for p in spec["csv"].values() if not os.path.exists(p)]
    if missing:
        print("Missing CSV files; nothing computed:\n  " + "\n  ".join(missing))
        return 1
    tables, csv_files = load_tables(spec["csv"])
    today = dt.date.today().isoformat()

    rows, failed = [], 0
    for q in spec["questions"]:
        row = {k: q.get(k, "") for k in ("question", "metric", "family", "table", "filter", "formula", "unit", "grain")}
        row["signals"] = "; ".join(q.get("signals", []))
        row.update(question_id=q["id"], csv_files=csv_files, computed_on=today,
                   value="", row_count="", error="")
        try:
            value, row["row_count"] = compute(q, tables)
            row["value"] = round(value, 6) if isinstance(value, float) else value
        except Exception as e:  # recorded in the row, never skipped
            row["error"] = f"{type(e).__name__}: {e}"
            failed += 1
        rows.append(row)
        print(f"{row['question_id']:>6}  {str(row['value']) or 'FAILED':>18}  {row['unit']:<8}  {row['metric']}"
              + (f"  [{row['error']}]" if row["error"] else ""))

    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)
    print(f"\n{len(rows) - failed} computed, {failed} failed. Wrote {out}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
