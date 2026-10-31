#!/usr/bin/env python3
"""timing.py - log when a stage starts and ends, for time per piece.

Usage:
    python scripts/timing.py <piece> <stage> start
    python scripts/timing.py <piece> <stage> end

Appends one row per call to runs/<piece>-timing.csv: stage, event, time (local, with
offset), on "end" the minutes since that stage's last unmatched "start", and a note
("logged" for every row this script writes). A skill or agent calls it once at its
start and once at its finish. Rows are only ever appended.

The stage must be one of STAGES, the names defined in runs/README.md#timing. Add a
name there and here together.
"""
import csv
import datetime as dt
import os
import sys

FIELDS = ["stage", "event", "time", "minutes", "note"]
STAGES = ("research", "truth", "run", "mark", "findings", "outline", "draft", "seo-geo", "linkedin", "export")


def main(argv):
    if len(argv) != 4 or argv[3] not in ("start", "end"):
        print(__doc__)
        return 2
    piece, stage, event = argv[1], argv[2], argv[3]
    if stage not in STAGES:
        print(f"Unknown stage '{stage}'. Use one of: {', '.join(STAGES)} (runs/README.md#timing).")
        return 2
    path = f"runs/{piece}-timing.csv"
    now = dt.datetime.now().astimezone()

    rows = []
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            rows = list(csv.DictReader(f))

    minutes = ""
    if event == "end":
        open_start = None
        for r in rows:
            if r["stage"] == stage and r["time"]:
                open_start = r if r["event"] == "start" else None
        if open_start is None:
            print(f"No open start for stage '{stage}' in {path}; logging the end without minutes.")
        else:
            started = dt.datetime.fromisoformat(open_start["time"])
            minutes = round((now - started).total_seconds() / 60, 1)

    new_file = not os.path.exists(path) or os.path.getsize(path) == 0
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if new_file:
            w.writeheader()
        w.writerow({"stage": stage, "event": event, "time": now.isoformat(timespec="seconds"),
                    "minutes": minutes, "note": "logged"})
    print(f"{path}: {stage} {event} {now.isoformat(timespec='seconds')}" + (f" ({minutes} min)" if minutes != "" else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
