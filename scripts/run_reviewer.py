#!/usr/bin/env python3
"""run_reviewer.py - start one blind reviewer the only way that keeps it blind.

Usage:
    python scripts/run_reviewer.py <reader|fact-checker|lift-tester> <slug>

1. Writes the body-only review copy (review_copy.py).
2. Starts a headless Claude Code session with --strict-mcp-config and an empty MCP
   config, so no MCP server is connected and no server instructions (including
   ask_dot's description of Dot) can reach the reviewer. Started from an
   interactive session instead, every connected server's instructions reach it
   (facts/reviewer-blindness.md, B4).
3. That session starts the reviewer with its fixed sentence from
   runs/README.md#reviewers, and nothing else.
4. Saves the report to reviews/<slug>/<reviewer>.md.

It sets DOT_REVIEWER_LAUNCH=<reviewer> in that session; the reviewers' hook blocks every
file call without it, so a reviewer started any other way can read nothing.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SENTENCES = {
    "reader": "Read reviews/{slug}/draft.md and give your report.",
    "fact-checker": "Fact-check reviews/{slug}/draft.md against figures/{slug}-figures.csv and runs/{slug}-run.md.",
    "lift-tester": "Read reviews/{slug}/draft.md as an answer engine and report what you would and would not lift.",
}
# The fact-checker's memory turns on Write and Edit; the allowlist hook still confines them to its folder.
MEMORY_TOOLS = ["Write(.claude/agent-memory/fact-checker/**)", "Edit(.claude/agent-memory/fact-checker/**)"]


def main(argv):
    if len(argv) != 3 or argv[1] not in SENTENCES:
        print(__doc__)
        return 2
    reviewer, slug = argv[1], argv[2]
    copy = subprocess.run([sys.executable, "scripts/review_copy.py", slug])
    if copy.returncode:
        return copy.returncode

    sentence = SENTENCES[reviewer].format(slug=slug)
    task = (f"Use the Agent tool once, with subagent_type {reviewer} and exactly this prompt, "
            f"adding nothing to it: {json.dumps(sentence)} "
            "Then return the agent's report verbatim, and do nothing else.")
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump({"mcpServers": {}}, f)
    tools = ["Agent"] + (MEMORY_TOOLS if reviewer == "fact-checker" else [])
    claude = shutil.which("claude")  # claude.cmd on Windows
    if not claude:
        print("claude is not on PATH")
        return 1
    result = subprocess.run([claude, "-p", task, "--strict-mcp-config", "--mcp-config", f.name,
                             "--allowedTools", *tools],
                            capture_output=True, text=True, encoding="utf-8", timeout=1200,
                            env={**os.environ, "DOT_REVIEWER_LAUNCH": reviewer, "MSYS_NO_PATHCONV": "1"})
    Path(f.name).unlink(missing_ok=True)
    if result.returncode:
        print(result.stdout + result.stderr)
        return result.returncode
    out = Path("reviews") / slug / f"{reviewer}.md"
    out.write_text(f"# {reviewer} · {slug}\n\nStarted with: {sentence}\n\n{result.stdout.strip()}\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
