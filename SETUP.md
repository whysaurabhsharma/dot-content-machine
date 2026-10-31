# Setup: from a fresh machine to a first piece

Two parts. **Part 1 is all you need for a teardown or a guide**, which work from other organisations' publications and need no Dot account and no data. Part 2 adds what a **research** piece needs: a Dot workspace and the Olist data. Two of the first three pieces (B and F) needed only Part 1.

## Part 1 · Required for any piece (about 15 minutes)

| # | Do | It worked when |
|---|---|---|
| 1 | **Install Python 3.10 or later** (python.org) and **Git** (git-scm.com; on Windows it brings Git Bash). | `python --version` prints 3.10 or higher; `git --version` prints a version. |
| 2 | **Install Claude Code** (https://docs.claude.com/en/docs/claude-code) and sign in. | `claude --version` prints a version. |
| 3 | **Clone this repo** and open a terminal in it (on Windows, Git Bash). | `ls` shows `CLAUDE.md`, `SETUP.md`, `scripts/`. |
| 4 | **Install the packages:** `python -m pip install -r requirements.txt` | No errors. |
| 5 | **Run the setup check:** `python scripts/check_setup.py` | Every line is PASS or SKIP; it ends "ready for teardowns and guides". Each FAIL prints its fix. |
| 6 | **Check the rules loaded:** run `claude` in the repo and ask "What are the four human decisions?" | It answers: the question, the outline, the title, the publish. |

**Next: the first test.** `HANDOVER.md` section 3, "First test: a teardown, no Dot needed". It proves the machine works before you set up anything else.

## Part 2 · Also required for a research piece (about 30 minutes more)

| # | Do | It worked when |
|---|---|---|
| 7 | **Create a free Kaggle account** and download the Olist dataset: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce. Unzip it. | You have `olist_orders_dataset.csv` and `olist_order_items_dataset.csv`. |
| 8 | **Put the two CSVs in `data/olist/`** in the repo (gitignored, so they never get committed). | `ls data/olist/` lists both files. |
| 9 | **Create a Dot account** at https://app.getdot.ai/register (a work email; Gmail is refused). | You can sign in to Dot. |
| 10 | **Set up the Dot workspace:** upload the two CSVs, add the two context notes, turn them on, as `facts/dot-workspace-setup.md` says (it has the metrics note's full text). | Model → Notes shows both notes, on. |
| 11 | **Connect Dot to Claude Code:** `claude mcp add --transport http ask_dot https://app.getdot.ai/ai/mcp`, then in `claude` type `/mcp`, choose `ask_dot`, sign in. | `/mcp` shows ask_dot connected. |
| 12 | **Run the research check:** `python scripts/check_setup.py --research` | It ends "ready for research pieces too". |
| 13 | **Verify the workspace:** ask Dot "How many orders were delivered in 2017?" in a fresh chat. | Dot answers **43,428**, using purchase date. |

**Next: the second test.** `HANDOVER.md` section 3, "Second test: a research run".

## If something fails

- **"Missing data file(s)":** step 8 wasn't done; the message names the exact path.
- **ask_dot not connected:** redo step 11; the sign-in happens inside `claude`, not in the terminal.
- **Dot's answer in step 13 isn't 43,428:** a table, note or date basis differs from `facts/dot-workspace-setup.md`. Fix that before any run.
- **Before you rely on any of it:** read `HANDOVER.md`, "For a newcomer: what you're inheriting". It says what has and hasn't been tested, and which gaps are still open.
