"""PreToolUse hook for dot-runner: allow Bash only for the `date` command.

Reads the hook payload on stdin. Exits 0 for `date` with plain options,
exits 2 (block) for anything else, with the reason on stderr.
"""
import json
import re
import sys

ALLOWED = re.compile(r"date( +[-+][A-Za-z0-9%:_ -]*)?")

payload = json.load(sys.stdin)
command = payload.get("tool_input", {}).get("command", "").strip()

if ALLOWED.fullmatch(command):
    sys.exit(0)

print(f"dot-runner may only run `date`; blocked: {command}", file=sys.stderr)
sys.exit(2)
