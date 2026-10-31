# Setup: from a fresh machine to a first run

Do these in order. Each step says how to know it worked. About 45 minutes, most of it the Dot workspace.

| # | Do | It worked when |
|---|---|---|
| 1 | **Install Python 3.10 or later** (python.org). | `python --version` prints 3.10 or higher. |
| 2 | **Install Claude Code** (https://docs.claude.com/en/docs/claude-code) and sign in. | `claude --version` prints a version. |
| 3 | **Clone this repo** and open a terminal in it (on Windows, Git Bash). | `ls` shows `CLAUDE.md`, `SETUP.md`, `scripts/`. |
| 4 | **Install the packages:** `python -m pip install -r requirements.txt` | No errors. |
| 5 | **Create a free Kaggle account** and download the Olist dataset: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce. Unzip it. | You have `olist_orders_dataset.csv` and `olist_order_items_dataset.csv`. |
| 6 | **Put the two CSVs in `data/olist/`** in the repo (the folder is gitignored, so they never get committed). | `ls data/olist/` lists both files. |
| 7 | **Create a Dot account** at https://app.getdot.ai/register (a work email; Gmail is refused). | You can sign in to Dot. |
| 8 | **Set up the Dot workspace:** upload the two CSVs, add the two context notes, turn them on. Follow `facts/dot-workspace-setup.md`, which has the metrics note's full text. | Model → Notes shows both notes, on. |
| 9 | **Connect Dot to Claude Code:** `claude mcp add --transport http ask_dot https://app.getdot.ai/ai/mcp`, then run `claude` in the repo, type `/mcp`, choose `ask_dot`, sign in. | `/mcp` shows ask_dot connected. |
| 10 | **Run the setup check:** `python scripts/check_setup.py` | It ends "14 of 14 passed". Each FAIL line prints its fix. |
| 11 | **Verify the workspace**, `facts/dot-workspace-setup.md` section 3: ask Dot "How many orders were delivered in 2017?" in a fresh chat. | Dot answers **43,428**, using purchase date. |
| 12 | **Check the rules loaded:** in `claude`, ask "What are the four human decisions?" | It answers: the question, the outline, the title, the publish. |

## Then run a first piece

Follow `HANDOVER.md` section 3, "A 30-minute first test". At any point, `python scripts/stage_gate.py <slug>` says what comes next. Use `--practice` on `stage_gate.py start` for a test that will never be published: practice pieces record conditions as text instead of screenshots.

## If something fails

- **A script stops with "Missing data file(s)":** step 6 wasn't done; the message names the exact path.
- **check_setup.py fails "ask_dot MCP connected":** redo step 9; the sign-in happens inside `claude`, not in the terminal.
- **Dot's answer in step 11 isn't 43,428:** a table, note or date basis differs from `facts/dot-workspace-setup.md`. Fix that before any run, or the specs' expected answers don't apply.
- **Anything else:** `HANDOVER.md` section 6 lists the known gaps, including those a cold-start test found (`runs/coldstart/`).
