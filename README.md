# Dot content machine

Turns a buyer's question into an evidence-led piece for getdot.ai, checks it harder than a reader would, and measures whether Dot gets chosen.

It runs in Claude Code, in this repo. Claude Code reads `CLAUDE.md` automatically, runs the stage subagents in `.claude/agents/`, and talks to Dot through the `ask_dot` MCP.

**Start here: [SETUP.md](SETUP.md).** It takes a fresh machine to a first test, one checked step at a time, and ends by pointing you at the first test.

## This submission

Where the submission stands (what is delivered, what each item waits on, the pre-publish sequence): [STATUS.md](STATUS.md).

Three pieces, one topic cluster, three formats (research, teardown, guide): can you trust an AI analyst's answers before you roll it out? Six LinkedIn posts, two per piece.

| # | Piece | Posts | State (1 November 2026) |
|---|---|---|---|
| A | Research, `ai-analyst-follow-up-questions` (bank #43) | 2 of 2 (structures 2 and 6) | Through the gate and exported; Decision 4 (publish) open |
| B | Teardown, `how-companies-test-ai-data-analysts` (bank #36) | 2 of 2 (structures 1 and 3) | Through Decision 3 and exported; Decision 4 open (one labelled assumption, see its publish note) |
| F | Guide, `test-ai-analyst-before-rollout` (bank #35), the cluster's hub | 2 of 2 (structures 4 and 5) | Through Decision 3 and exported; Decision 4 open |

Where each piece stands is read from the files by `python scripts/stage_gate.py <slug>`, not from this table. What's left and what needs Rick: `HANDOVER.md`.

The plan, what each piece proves and which runs feed which: `PLAN.md`.

The earlier Claude Project trial's pieces and posts are in `archive/` and are not part of this submission.

## What's here

| Path | What it is |
|---|---|
| `HANDOVER.md` | Set-up in Claude Code, a first test (a teardown, about 10 minutes of machine time), how to run a full piece, the monthly loop, what's still open |
| `CLAUDE.md` | Every rule: 23 hard rules, 17 style rules, the seven stages, the 25-check gate, a dated change log (v1.8.27). Claude Code reads it automatically |
| `.claude/agents/researcher.md` | Stage 1 RESEARCH as a subagent. Reads the Ahrefs snapshot and the citation series, fetches the top three pages, writes `runs/<piece>-research.md` |
| `.claude/agents/dot-runner.md` | The evidence run as a subagent. Asks Dot each test question verbatim through `ask_dot` and appends every answer to `runs/<piece>-run.md` |
| `prompts/01-research.md` … `07-linkedin.md` | The seven stage prompts. 01 runs as the `researcher` subagent; 02, 03 and 07 as the `/outline`, `/draft` and `/linkedin` skills; 04–06 are not yet built |
| `.claude/skills/` | The five writing skills: `/outline`, `/draft`, `/seo-geo`, `/linkedin`, `/export`. Each takes the piece slug, times itself with `timing.py`, and is started only by a person or the workflow |
| `scripts/export_docx.py`, `scripts/export_webflow.py` | `/export`'s scripts: the piece as .docx, clean Markdown, and paste-ready Webflow files. They create no draft in Webflow |
| `runs/` | Every Dot answer, word for word, one file per piece. The screenshot scheme and batching rules are in `runs/README.md` |
| `runs/screenshots/` | The five conditions screenshots per batch, taken in Dot's UI |
| `runs/smoke-test.md` | The 31 October 2026 smoke test of the `ask_dot` MCP |
| `facts/dot-facts.md` | Observed in Dot (O1–O11), assumed (A1–A10, with basis), confirmed (D1: Dot's voice, "we" = Dot; P-2; the Olist licence; the byline) |
| `facts/dot-mcp.md` | What the `ask_dot` MCP exposes, observed 31 October 2026, and what it can't show |
| `facts/run-format.md` | The run-file format that `dot-runner` writes and check 16 and `mark_run.py` read, with a worked example |
| `facts/house-structure-and-links.md` | The anatomy of a piece; ten internal links verified 28 October 2026 |
| `bank/questions.csv` | The question bank, from the ICP question bank PDF, scored on its four factors. **Read `bank/README.md` first**: only 3 of 102 phrases have an Ahrefs row, none has a Search Console row, and none yet comes from a sales call |
| `scripts/bank.py`, `.claude/skills/bank/` | The monthly entry point: `/bank add`, `/bank rescore`, `/bank top` |
| `ICP_question_bank_what_Dot_s_buyers_ask__October_2026.pdf` | The source of the question bank |
| `data/ahrefs/` | The Ahrefs snapshot, 27–28 October 2026: keywords, Search Console, Site Explorer, Rank Tracker. Frozen; access ended 31 October 2026 |
| `data/` | A note on the Olist dataset (CC BY-NC-SA 4.0; Dot confirmed on 1 November 2026 that it may publish figures from it) and where to download it. The CSVs are not included |
| `measure/README.md` | How to take a baseline reading: the conditions, which are rules, and the method |
| `measure/baseline-YYYY-MM-DD.md` | The baseline: buyer queries read in Google, Perplexity and ChatGPT, one dated file per reading, never edited. First: 1 November 2026, 5 of 18 queries |
| `measure/citations.md` | The earlier Perplexity series (27–29 October 2026, topic labels). Closed; kept for the record |
| `scripts/check_piece.py` | Runs the 25-check gate on a piece: 15 checks decided alone, 3 with a person, 6 flagged for a human. With `--post`, checks each LinkedIn post in a `posts/` file against stage 7 and checks 15, 17 and 19 |
| `scripts/verify_sources.py` | Opens every link in a piece |
| `scripts/ground_truth_from_spec.py` | Computes every expected value in a JSON spec from the raw CSVs and writes `figures/<piece>-truth.csv`, with each definition, row count and CSV date. A row that can't be computed carries its reason |
| `scripts/mark_run.py` | Marks each answer in `runs/<piece>-run.md` against `figures/<piece>-truth.csv`, under the definition the answer stated; gaps under 0.1% are rounding. Appends to `figures/<piece>-figures.csv` and prints how many were correct under the definition asked and how many only under another reading, never a bare total (CLAUDE.md v1.8.10) |
| `scripts/timing.py` | Logs a stage's start and end to `runs/<piece>-timing.csv`, with minutes, for time per piece |
| `scripts/charts.py` | One chart per piece from a JSON spec, with alt text and caption |
| `.claude/agents/reader.md`, `fact-checker.md`, `lift-tester.md` | The three blind reviewers: no CLAUDE.md, a Read allowlist enforced by `scripts/hooks/read_allowlist.py`, a body-only review copy. Start them only with `scripts/run_reviewer.py`; what still reaches them is in `facts/reviewer-blindness.md` |
| `.claude/workflows/piece.js` | The piece workflow, `/piece <slug>`: runs the stages in the order `stage_gate.py` allows and stops at every human decision. Re-run it after each decision |
| `scripts/stage_gate.py` | Where a piece stands, read only from files: the checkpoint the workflow starts from. `start <slug> --bank <id>` records Decision 1. It enforces the gates the skills only state in prose |
| `scripts/run_reviewer.py`, `scripts/review_copy.py` | Start a reviewer in a headless session with no MCP servers, with its fixed sentence; write the body-only copy it reads |
| `scripts/hooks/only_date.py` | The hook that limits `dot-runner`'s Bash to the `date` command |
| `pieces/<slug>.md`, `figures/<slug>-figures.csv`, `charts/`, `posts/<slug>-posts.md` | Each piece, its Figures rows, its chart and its posts, named by slug |
| `archive/` | The earlier trial's pieces, figures, charts and posts: superseded, kept for the record |

## Quick start

The scripts need a Python 3.10+ with the packages in `requirements.txt` (pandas, matplotlib, python-docx). Use whichever Python you like; install into it and check:

    python -m pip install -r requirements.txt
    python -c "import pandas, matplotlib, docx; print('ok')"

If the check prints `ok`, run the scripts with that same `python`:

    python scripts/check_piece.py pieces/ai-analyst-follow-up-questions.md

Expected: `17 pass, 0 fail, 1 partial, 7 for a human` (the partial is check 1: a claim title, which the headline test covers).

Then run `claude` in this folder and type `/mcp` to check that `ask_dot` is connected. `HANDOVER.md` section 1 has the set-up.

**Git Bash and slash commands.** Git Bash rewrites an argument that starts with `/` into a Windows path, so `claude -p "/outline <slug>"` arrives as `D:/…/Git/outline`. Set `MSYS_NO_PATHCONV=1` before invoking a skill from Git Bash, or from any script run there. `scripts/run_reviewer.py` sets it for the session it starts. Typing `/outline` at the Claude Code prompt is unaffected.

**Permissions.** `.claude/settings.json` pre-approves the eleven scripts the skills and workflow call (`bank.py`, `check_piece.py`, `export_docx.py`, `export_webflow.py`, `ground_truth_from_spec.py`, `mark_run.py`, `review_copy.py`, `run_reviewer.py`, `stage_gate.py`, `timing.py`, `verify_sources.py`), each by its exact path, for both the Bash and the PowerShell tool (a headless session on Windows runs commands through PowerShell, which has its own permission rules), so a stage never stops mid-way to ask about logging its time. Everything else still asks.

## Where the three pieces stand (1 November 2026)

- **What `check_piece.py` prints (1 November 2026):** A, 17 pass, 0 fail, 1 partial, 7 for a human; B, 18 pass, 0 fail, 1 partial, 6 for a human; F, 19 pass, 0 fail, 0 partial, 6 for a human. A's and B's partial is check 1, a claim title, by design (the headline test covers it). A's extra human check is 25: its outline predates the quotable line.
- **A and B** have each had the three blind reviewers, a second fact-check on other models, the headline test, the lift test and a phone read, recorded in `reviews/<slug>/human.md`.
- **F** is through Decision 3 and exported.
- **Before publishing:** the pre-publish sequence in `STATUS.md` section 3 (each publish note signed, then A, B and F in one session). Rick's open questions are in `DECISIONS-FOR-DOT.md`; none blocks publishing. Run scores are quoted item by item, never as a bare total (CLAUDE.md v1.8.10).
- The earlier pieces 1–3 of 28 October are archived in `archive/` and are not part of this submission.

## What has been tested, and what hasn't

- **check_piece.py** runs on all three pieces. On a deliberately broken copy of piece 1 it caught all six planted problems. Four bugs were found while using it on pieces 2 and 3 (dates, labels, a quoted-voice count, a named-thing heuristic) and fixed; all three pieces were re-run afterwards. The planted errors were planted by the author.
- **ground_truth.py** (retired 31 October 2026, replaced by `ground_truth_from_spec.py`) matched 21 hand-computed answers on a small test dataset, then reproduced all 20 expected answers on the real Olist files (largest gap 0.152%, rounding). Delivered-only average order value: 137.0416, matching Dot's 137.04.
- **verify_sources.py** works, but the build environment couldn't reach getdot.ai; the ten links were opened in a browser instead. Run it on a normal connection.
- **charts.py** produced all three charts.
- **Tested by an outside person, 29 October 2026,** on the earlier Claude Project set-up: a tester who had never seen the machine set it up from these files alone and ran RESEARCH on the rehearsal question. The rules loaded (she named the four human decisions correctly), and the verdict matched the author's run: PIECE, but NOT A PIECE if the test only reproduces piece 1.
- **The ask_dot MCP, 31 October 2026:** connected from Claude Code; one question asked and answered (BRL 137.04, basis stated); what it exposes recorded in `facts/dot-mcp.md`. Mode, credits, model, environment and active context notes are not observable via MCP.
- **The only_date.py hook** was tested on its own: it allows `date` and `date +FORMAT`, and blocks chained commands, substitutions and other commands.
- **Since tested (31 October–1 November 2026):** the `researcher` subagent on A, B and F; the `dot-runner` subagent on A's run; full pieces through the gate in Claude Code (A and B); the three blind reviewers through `run_reviewer.py`; time per stage, logged in `runs/<slug>-timing.csv` (costs in HANDOVER.md section 2).
- **Tested cold three times (1 November 2026),** each by a fresh Claude Code session given only the README, never by a person: to a research verdict (about 4 minutes), to a marked Dot run on a practice piece (about 10 minutes), and the teardown first test to "next outline" (about 6 minutes). Each logged the gaps it hit (`runs/coldstart/`; what was fixed and what is open: HANDOVER.md, "For a newcomer").
- **Not yet tested:** a full piece run by a person other than the author; the monthly loop (never run); any outcome (nothing is published).

---

# Runbook

One piece, end to end. One owner. `/piece <slug>` runs these steps in the order `scripts/stage_gate.py` allows and stops at every point a person owns (HANDOVER.md section 7). Times below are logged machine minutes where we have them; a person's time on top is not logged.

## The four human decisions

1. **The question.** From the question bank, calls first.
2. **The outline.** Approved before a word is drafted.
3. **The title.** Picked from three candidates.
4. **Publish.** Only when all 25 checks in CLAUDE.md pass.

## Eleven steps

| # | Step | How |
|---|---|---|
| 1 | Pick the question | Decision 1: `python scripts/stage_gate.py start <slug> --bank <id> --format research\|teardown\|guide` |
| 2 | Research | The `researcher` subagent writes `runs/<slug>-research.md` and its verdict |
| 3 | Evidence | Research: write the truth spec, a person reviews its rival definitions, record batch conditions in Dot's UI, the `dot-runner` subagent asks the questions, `mark_run.py` marks them (it prints correct-as-asked and correct-under-another-reading separately). Teardown or guide: build `figures/<slug>-figures.csv` from cited publications, each opened in a browser |
| 4 | Outline | `/outline <slug>`, then Decision 2: a person fills "Approved by" and "Date" |
| 5 | Draft | `/draft <slug>` |
| 6 | SEO and links | `/seo-geo <slug>` |
| 7 | Blind reviews | `python scripts/run_reviewer.py <reader\|fact-checker\|lift-tester> <slug>`, once each. It starts each reviewer in a headless session with no MCP servers and a body-only copy of the draft, so the reviewer never sees CLAUDE.md or what the writer meant |
| 8 | Revise | Fix every point or say why it stands, in `reviews/<slug>/revisions.md`; a second fact-check on another model |
| 9 | Edit | `check_piece.py` until no FAIL; `verify_sources.py`; the headline test, lift test and phone read, recorded in `reviews/<slug>/human.md`; Decision 3: `title_approved_by` and `reviewed_on` |
| 10 | Posts | `/linkedin <slug>`; a person writes every first line; `check_piece.py --post` |
| 11 | Export and publish | `/export <slug>` (refuses while any check FAILs); Decision 4, a person's; then `python scripts/bank.py status <id> published --basis "<URL>"` |

A rule 14 waiver (no screenshots) is recorded once: `python scripts/stage_gate.py waive <slug> --rule 14 --batch <n> --by "<name, date>"`, after the batch's conditions block states it (CLAUDE.md v1.8.9).

## The monthly loop: 20 minutes a week, one owner

| Week | Do |
|---|---|
| 1 | Take the baseline readings: Search Console click-through per piece, the Site Explorer AI-responses panel, Rank Tracker. Save them as new dated files in `data/ahrefs/`; never overwrite. Read the buyer queries in Google, Perplexity (signed in, same account) and ChatGPT and record them in a new `measure/baseline-YYYY-MM-DD.md` (CLAUDE.md, Measurement) |
| 2 | Add new questions from sales calls and from Search Console's non-brand queries to the question bank |
| 3 | Review the logged fixes (`reviews/<slug>/revisions.md`, the run files). Any mistake seen twice becomes a CLAUDE.md rule with a dated origin, and a check in `check_piece.py` if it can be automated |
| 4 | Re-run past pieces' evaluations to catch drift. Rewrite any title whose click-through is below the site average after 30 days. Pick the next question |

Ahrefs access ended on 31 October 2026. Weeks 1 and 4 need it back; until then, the Ahrefs readings are the frozen snapshot in `data/ahrefs/`. New readings go in new dated files there.

## Rank Tracker

Add these in Ahrefs Rank Tracker, US and Germany:

- best ai data analyst 2026
- how to evaluate ai data analyst accuracy
- ai data analyst accuracy
- text to sql accuracy
- semantic layer ai analyst
- ai data analyst
- reduce ad hoc data requests
- ai data analyst cost per question
- ai data analyst pricing
- conversational analytics
- self service analytics tools

## Running a piece with the workflow

1. **Decision 1.** Pick the question with `/bank top`, confirm its evidence score, then record it: `python scripts/stage_gate.py start <slug> --bank <id>`.
2. **Run `/piece <slug>`.** It starts every run from `stage_gate.py` and runs only the stage the gate names, then asks the gate again. The first run of a saved workflow asks you to approve it.
3. **It stops** when the gate says a person is needed or something is blocked, when a stage fails, when a stage runs and the gate's answer doesn't change, or after two `check_piece` fix rounds that leave a FAIL. It reports where and why.
4. **Do what it names** (check the truth spec and add `reviewed_by`; record a batch's conditions or credits in Dot's UI; approve the outline; set the title and tick the human checks; publish), then run `/piece <slug>` again. Where a piece stands is read from the files every time, so this works in any session.

