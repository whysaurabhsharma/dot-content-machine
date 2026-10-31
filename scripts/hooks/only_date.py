"""PreToolUse hook for dot-runner: allow Bash only for the clock and the run timer.

Allowed, exactly:
- `date`, with plain options (for each entry's Time line);
- `python [-I] scripts/timing.py <piece> run start|end` (the dot-runner logs its own
  run stage; no other stage, no other script).

Reads the hook payload on stdin. Exits 0 for an allowed command, exits 2 (block)
for anything else, with the reason on stderr.
"""
import json
import re
import sys

ALLOWED = [
    re.compile(r"date( +[-+][A-Za-z0-9%:_ -]*)?"),
    re.compile(r"python3? +(-I +)?scripts/timing\.py +[a-z0-9-]+ +run +(start|end)"),
]

payload = json.load(sys.stdin)
command = payload.get("tool_input", {}).get("command", "").strip()

if any(p.fullmatch(command) for p in ALLOWED):
    sys.exit(0)

print(f"dot-runner may only run `date` or `python scripts/timing.py <piece> run start|end`; blocked: {command}",
      file=sys.stderr)
sys.exit(2)
