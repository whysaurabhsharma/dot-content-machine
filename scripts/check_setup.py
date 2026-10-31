#!/usr/bin/env python3
"""check_setup.py - is this machine ready to run a piece? Prints one line per check, with the fix.

Usage:
    python scripts/check_setup.py

Checks: Python version; the packages in requirements.txt; the two Olist CSVs the specs read;
the Claude Code CLI; the ask_dot MCP server; the repo's agents. Exit code 0 when all pass.
"""
import importlib
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KAGGLE = "https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce"
results = []


def check(name, ok, fix=""):
    results.append(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + ("" if ok else f"\n      fix: {fix}"))


check(f"Python 3.10+ (this is {sys.version.split()[0]})", sys.version_info >= (3, 10),
      "install Python 3.10 or later from python.org")
for module, package in (("pandas", "pandas"), ("matplotlib", "matplotlib"), ("docx", "python-docx"), ("yaml", "pyyaml")):
    try:
        importlib.import_module(module)
        check(f"package {package}", True)
    except ImportError:
        check(f"package {package}", False, f"{sys.executable} -m pip install -r requirements.txt")
for csv in ("olist_orders_dataset.csv", "olist_order_items_dataset.csv"):
    path = ROOT / "data" / "olist" / csv
    check(f"data/olist/{csv}", path.exists(),
          f"download the dataset from {KAGGLE} (free Kaggle account), unzip it, and put {csv} at {path}")
claude = shutil.which("claude")
check("Claude Code CLI on PATH", bool(claude), "install Claude Code: https://docs.claude.com/en/docs/claude-code")
if claude:
    try:
        out = subprocess.run([claude, "mcp", "list"], capture_output=True, text=True, timeout=90, cwd=ROOT).stdout
        check("ask_dot MCP connected", "ask_dot" in out and "Connected" in out.split("ask_dot", 1)[1].splitlines()[0],
              "claude mcp add --transport http ask_dot https://app.getdot.ai/ai/mcp ; then in claude, /mcp, choose ask_dot, sign in")
    except Exception as e:
        check("ask_dot MCP connected", False, f"could not run 'claude mcp list' ({e}); check it by hand with /mcp")
for agent in ("researcher", "dot-runner", "reader", "fact-checker", "lift-tester"):
    check(f"agent {agent}", (ROOT / ".claude" / "agents" / f"{agent}.md").exists(), "the repo is incomplete: clone it again")
print(f"\n{sum(results)} of {len(results)} passed." + ("" if all(results) else " Fix the FAIL lines above, then run this again."))
sys.exit(0 if all(results) else 1)
