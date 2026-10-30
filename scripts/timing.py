#!/usr/bin/env python3
"""timing.py - log when a stage starts and ends, for time per piece.

Usage:
    python scripts/timing.py <piece> <stage> start
    python scripts/timing.py <piece> <stage> end

Appends one row per call to runs/<piece>-timing.csv: stage, event, time (local, with
offset) and, on "end", the minutes since that stage's last unmatched "start". A skill
calls it once at its start and once at its finish. Rows are only ever appended.
"""
import csv
import datetime as dt
import os
import sys

FIELDS = ["stage", "event", "time", "minutes"]


def main(argv):
    if len(argv) != 4 or argv[3] not in ("start", "end"):
        print(__doc__)
        return 2
    piece, stage, event = argv[1], argv[2], argv[3]
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
            if r["stage"] == stage:
                open_start = r if r["event"] == "start" else None
        if open_start is None:
            print(f"No open start for stage '{stage}' in {path}; logging the end without minutes.")
        else:
            started = dt.datetime.fromisoformat(open_start["time"])
            minutes = round((now - started).total_seconds() / 60, 1)

    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if not rows and os.path.getsize(path) == 0:
            w.writeheader()
        w.writerow({"stage": stage, "event": event, "time": now.isoformat(timespec="seconds"), "minutes": minutes})
    print(f"{path}: {stage} {event} {now.isoformat(timespec='seconds')}" + (f" ({minutes} min)" if minutes != "" else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
