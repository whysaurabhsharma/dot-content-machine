"""PreToolUse hook for the blind reviewers: file tools may touch only the reviewer's allowlist.

Usage, from an agent's frontmatter:
    python -I "$CLAUDE_PROJECT_DIR/scripts/hooks/read_allowlist.py" <reviewer>

Covers Read, Grep, Glob, Write and Edit (memory: project turns on Write and Edit
for the fact-checker). Paths are resolved against the project directory first, so
"..", absolute paths and symlinks can't step outside the list. Exits 0 when the
path is allowed, 2 (block) otherwise, with the reason on stderr.
"""
import fnmatch
import json
import os
import sys
from pathlib import Path

READ = {
    "reader": ["reviews/*/draft.md"],
    "lift-tester": ["reviews/*/draft.md"],
    "fact-checker": ["reviews/*/draft.md", "figures/*-figures.csv", "runs/*-run.md",
                     ".claude/agent-memory/fact-checker/*"],
}
WRITE = {"fact-checker": [".claude/agent-memory/fact-checker/*"]}


def main():
    reviewer = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = json.load(sys.stdin)
    tool = payload.get("tool_name", "")
    args = payload.get("tool_input", {})
    root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or ".").resolve()

    allowed = (WRITE if tool in ("Write", "Edit") else READ).get(reviewer, [])
    if tool in ("Grep", "Glob"):
        target = args.get("path") or ""
        if not target:
            return block(f"{tool} without a path searches the whole repo")
    else:
        target = args.get("file_path") or ""
    path = (root / target).resolve() if not Path(target).is_absolute() else Path(target).resolve()
    try:
        rel = path.relative_to(root).as_posix()
    except ValueError:
        return block(f"{target} is outside the project")
    if any(fnmatch.fnmatchcase(rel, p) for p in allowed):
        return 0
    return block(f"{tool} {rel} is not on the {reviewer} allowlist {allowed}")


def block(reason):
    print(f"Blocked for a blind reviewer: {reason}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
