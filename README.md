# Dot content machine

Turns a buyer's question into an evidence-led piece for getdot.ai, checks it harder than a reader would, and measures whether Dot gets chosen.

It runs in Claude Code, in this repo. Claude Code reads `CLAUDE.md` automatically, runs the stage subagents in `.claude/agents/`, and talks to Dot through the `ask_dot` MCP.

**New here? Read `HANDOVER.md` first.** It gets you from a fresh clone to a connected Claude Code session in ten minutes, and through a 15-minute test run.

## This submission

Three pieces, one topic cluster, three formats (research, teardown, guide): can you trust an AI analyst's answers before you roll it out? Six LinkedIn posts, two per piece.

| # | Piece | Posts | State |
|---|---|---|---|
| 1 of 3 | `pieces/ai-analyst-follow-up-questions.md` | Post 1 of 6: Post A in `posts/ai-analyst-follow-up-questions-posts.md` | Through the gate; Decision 4 (publish) open |
| 2 of 3 | Teardown, `how-companies-test-ai-data-analysts` (bank #36) | Posts 2–3 | Research |
| 3 of 3 | Guide, `test-ai-analyst-before-rollout` (bank #35) | Posts 4–6 | After B |

The plan, what each piece proves and which runs feed which: `PLAN.md`.

The earlier Claude Project trial's pieces and posts are in `archive/` and are not part of this submission.

## What's here

| Path | What it is |
|---|---|
| `HANDOVER.md` | Set-up in Claude Code, a 15-minute first test, how to run a full piece, the monthly loop, what's still open |
| `CLAUDE.md` | Every rule: 23 hard rules, 17 style rules, the seven stages, the 25-check gate, a dated change log (v1.6.5). Claude Code reads it automatically |
| `.claude/agents/researcher.md` | Stage 1 RESEARCH as a subagent. Reads the Ahrefs snapshot and the citation series, fetches the top three pages, writes `runs/<piece>-research.md` |
| `.claude/agents/dot-runner.md` | The evidence run as a subagent. Asks Dot each test question verbatim through `ask_dot` and appends every answer to `runs/<piece>-run.md` |
| `prompts/01-research.md` … `07-linkedin.md` | The seven stage prompts. 01 runs as the `researcher` subagent; 02, 03 and 07 as the `/outline`, `/draft` and `/linkedin` skills; 04–06 are not yet built |
| `.claude/skills/` | The five writing skills: `/outline`, `/draft`, `/seo-geo`, `/linkedin`, `/export`. Each takes the piece slug, times itself with `timing.py`, and is started only by a person or the workflow |
| `scripts/export_docx.py`, `scripts/export_webflow.py` | `/export`'s scripts: the piece as .docx, clean Markdown, and paste-ready Webflow files. They create no draft in Webflow |
| `runs/` | Every Dot answer, word for word, one file per piece. The screenshot scheme and batching rules are in `runs/README.md` |
| `runs/screenshots/` | The five conditions screenshots per batch, taken in Dot's UI |
| `runs/smoke-test.md` | The 31 October 2026 smoke test of the `ask_dot` MCP |
| `facts/dot-facts.md` | Observed in Dot (O1–O11), assumed (A1–A10, with basis), confirmed (D1: Rick's voice, "we" = Dot) |
| `facts/dot-mcp.md` | What the `ask_dot` MCP exposes, observed 31 October 2026, and what it can't show |
| `facts/run-format.md` | The run-file format that `dot-runner` writes and check 16 and `mark_run.py` read, with a worked example |
| `facts/house-structure-and-links.md` | The anatomy of a piece; ten internal links verified 28 October 2026 |
| `bank/questions.csv` | The question bank, from the ICP question bank PDF, scored on its four factors. **Read `bank/README.md` first**: only 3 of 102 phrases have an Ahrefs row, none has a Search Console row, and none yet comes from a sales call |
| `scripts/bank.py`, `.claude/skills/bank/` | The monthly entry point: `/bank add`, `/bank rescore`, `/bank top` |
| `ICP_question_bank_what_Dot_s_buyers_ask__October_2026.pdf` | The source of the question bank |
| `data/ahrefs/` | The Ahrefs snapshot, 27–28 October 2026: keywords, Search Console, Site Explorer, Rank Tracker. Frozen; access ended 31 October 2026 |
| `data/` | A note on the Olist dataset (CC BY-NC-SA 4.0) and where to download it. The CSVs are not included |
| `measure/citations.md` | The monthly AI-citation series: citation markers per domain, Perplexity, from Day 0 |
| `scripts/check_piece.py` | Runs the 25-check gate on a piece: 15 checks decided alone, 3 with a person, 6 flagged for a human. With `--post`, checks each LinkedIn post in a `posts/` file against stage 7 and checks 15, 17 and 19 |
| `scripts/verify_sources.py` | Opens every link in a piece |
| `scripts/ground_truth_from_spec.py` | Computes every expected value in a JSON spec from the raw CSVs and writes `figures/<piece>-truth.csv`, with each definition, row count and CSV date. A row that can't be computed carries its reason |
| `scripts/mark_run.py` | Marks each answer in `runs/<piece>-run.md` against `figures/<piece>-truth.csv`, under the definition the answer stated; gaps under 0.1% are rounding. Appends to `figures/<piece>-figures.csv` and prints "N of M correct" |
| `scripts/timing.py` | Logs a stage's start and end to `runs/<piece>-timing.csv`, with minutes, for time per piece |
| `scripts/charts.py` | One chart per piece from a JSON spec, with alt text and caption |
| `.claude/agents/reader.md`, `fact-checker.md`, `lift-tester.md` | The three blind reviewers: no CLAUDE.md, a Read allowlist enforced by `scripts/hooks/read_allowlist.py`, a body-only review copy. Start them only with `scripts/run_reviewer.py`; what still reaches them is in `facts/reviewer-blindness.md` |
| `.claude/workflows/piece.js` | The piece workflow, `/piece <slug>`: runs the stages in the order `stage_gate.py` allows and stops at every human decision. Re-run it after each decision |
| `scripts/stage_gate.py` | Where a piece stands, read only from files: the checkpoint the workflow starts from. `start <slug> --bank <id>` records Decision 1. It enforces the gates the skills only state in prose |
| `scripts/run_reviewer.py`, `scripts/review_copy.py` | Start a reviewer in a headless session with no MCP servers, with its fixed sentence; write the body-only copy it reads |
| `scripts/hooks/only_date.py` | The hook that limits `dot-runner`'s Bash to the `date` command |
| `pieces/<slug>.md`, `figures/<slug>-figures.csv`, `charts/`, `posts/<slug>-posts.md` | Each piece, its Figures rows, its chart and its posts, named by slug |
| `archive/` | The earlier trial's pieces, figures, charts and posts: superseded, kept for the record |
| `tracking/` | A note on the tracking sheet, a Google Sheet sent with this folder as a link: Question bank, Coverage, Sources, Figures, Baseline, Run Log |
| `guides/Dot-Run-a-Full-Piece.pdf` | Step-by-step guide to one complete piece, written for the earlier Claude Project set-up. The steps hold; where it says to paste into the Project, use the subagent or prompt named below instead |
| `guides/Dot-Machine-Tester-Guide.pdf` | A 30-minute first test, written for the earlier Claude Project set-up. Superseded by `HANDOVER.md` section 2 |

## Quick start

The scripts need a Python 3.10+ with the packages in `requirements.txt` (pandas, matplotlib, python-docx). Use whichever Python you like; install into it and check:

    python -m pip install -r requirements.txt
    python -c "import pandas, matplotlib, docx; print('ok')"

If the check prints `ok`, run the scripts with that same `python`:

    python scripts/check_piece.py pieces/ai-analyst-follow-up-questions.md

Expected: `17 pass, 0 fail, 1 partial, 6 for a human` (the partial is check 1: a claim title, which the headline test covers).

Then run `claude` in this folder and type `/mcp` to check that `ask_dot` is connected. `HANDOVER.md` section 1 has the set-up.

**Git Bash and slash commands.** Git Bash rewrites an argument that starts with `/` into a Windows path, so `claude -p "/outline <slug>"` arrives as `D:/…/Git/outline`. Set `MSYS_NO_PATHCONV=1` before invoking a skill from Git Bash, or from any script run there. `scripts/run_reviewer.py` sets it for the session it starts. Typing `/outline` at the Claude Code prompt is unaffected.

**Permissions.** `.claude/settings.json` pre-approves only the five scripts the skills call (`timing.py`, `check_piece.py`, `verify_sources.py`, `export_docx.py`, `export_webflow.py`), each by its exact path, for both the Bash and the PowerShell tool (a headless session on Windows runs commands through PowerShell, which has its own permission rules), so a stage never stops mid-way to ask about logging its time. Everything else still asks.

## Where the three pieces stand (28 October 2026)

- All three pass every automated check: 18 pass, 0 fail.
- Done on each: READER, two fact-checks (Claude and ChatGPT), the lift test in Perplexity and Claude.
- Open: the phone read (check 24) on all three; the lift test re-run on piece 1's new opening.
- Before publishing: re-run piece 1's evaluation in a Dot workspace (the trial ran on Olist, licensed non-commercial), and get a yes, no or change on assumptions A1–A8.

## What has been tested, and what hasn't

- **check_piece.py** runs on all three pieces. On a deliberately broken copy of piece 1 it caught all six planted problems. Four bugs were found while using it on pieces 2 and 3 (dates, labels, a quoted-voice count, a named-thing heuristic) and fixed; all three pieces were re-run afterwards. The planted errors were planted by the author.
- **ground_truth.py** (retired 31 October 2026, replaced by `ground_truth_from_spec.py`) matched 21 hand-computed answers on a small test dataset, then reproduced all 20 expected answers on the real Olist files (largest gap 0.152%, rounding). Delivered-only average order value: 137.0416, matching Dot's 137.04.
- **verify_sources.py** works, but the build environment couldn't reach getdot.ai; the ten links were opened in a browser instead. Run it on a normal connection.
- **charts.py** produced all three charts.
- **Tested by an outside person, 29 October 2026,** on the earlier Claude Project set-up: a tester who had never seen the machine set it up from these files alone and ran RESEARCH on the rehearsal question. The rules loaded (she named the four human decisions correctly), and the verdict matched the author's run: PIECE, but NOT A PIECE if the test only reproduces piece 1.
- **The ask_dot MCP, 31 October 2026:** connected from Claude Code; one question asked and answered (BRL 137.04, basis stated); what it exposes recorded in `facts/dot-mcp.md`. Mode, credits, model, environment and active context notes are not observable via MCP.
- **The only_date.py hook** was tested on its own: it allows `date` and `date +FORMAT`, and blocks chained commands, substitutions and other commands.
- **Not yet tested:** the `researcher` and `dot-runner` subagents on a real question; a full piece run in Claude Code; a full piece run by anyone other than the author; time per piece (never logged); the monthly loop (never run); any outcome (nothing is published).

---

# Runbook

One piece, end to end. One owner. Times are estimates from piece 1, which was run by hand; log the real times in the Run Log from piece 2 on.

## The four human decisions

1. **The question.** From the question bank, calls first.
2. **The outline.** Approved before a word is drafted.
3. **The title.** Picked from three candidates.
4. **Publish.** Only when all 25 checks in CLAUDE.md pass.

## Eleven steps

| # | Step | How | Time |
|---|---|---|---|
| 1 | Pick the question | Decision 1. `bank/questions.csv` and the Question bank tab | 5 min |
| 2 | Research | The `researcher` subagent, given the question and a piece slug. It writes `runs/<piece>-research.md`. Add its Sources rows to the Sources tab | 30 min |
| 3 | Run the evidence in Dot | Take the five screenshots for batch 1 in Dot's UI (`runs/README.md#screenshots`). Then the `dot-runner` subagent, given the piece and batch number. Repeat per batch. Record credits from the screenshots in the Run Log | 30–75 min |
| 4 | Recompute ground truth | Write `specs/<piece>-truth.json` from the research file's test questions, then `python scripts/ground_truth_from_spec.py specs/<piece>-truth.json`. Every number into the piece's figures CSV | 10 min |
| 5 | Outline | `prompts/02-outline.md`, then Decision 2 | 20 min |
| 6 | Draft | `prompts/03-draft.md` | 30 min |
| 7 | READER | `prompts/04-reader.md`, in a fresh chat outside this repo, with only the draft. Fix the three stopping points | 15 min |
| 8 | Fact-check | `prompts/05-fact-check.md`: a fresh chat outside this repo, then a second model, then `verify_sources.py`. Log every fix | 30 min |
| 9 | Edit | `check_piece.py` until no FAIL; the headline test; the lift test in Perplexity and Claude. Decision 3 | 30 min |
| 10 | Chart and posts | `charts.py`; `prompts/07-linkedin.md` for each post, each with a different opening structure | 30 min |
| 11 | Gate and publish | The 25 checks; Decision 4; Webflow optional (Dot's team publishes); UTM links; request three reverse links; add the target queries to Rank Tracker | 20 min |

Steps 5, 6 and 10 run as skills: `/outline <slug>`, then a person fills "Approved by" (Decision 2), then `/draft <slug>` and `/seo-geo <slug>`; `/linkedin <slug>` per post; `/export <slug>` last, which refuses while any check FAILs. The skills haven't yet run on a real piece.

READER and the first fact-check must not run in a Claude Code session in this repo: it loads `CLAUDE.md` automatically, and the reviewer must not know what the writer meant. Use a fresh claude.ai chat, or Claude Code started in an empty folder.

## The monthly loop: 20 minutes a week, one owner

| Week | Do |
|---|---|
| 1 | Read the Baseline tab: Search Console click-through per piece, the Site Explorer AI-responses panel, Rank Tracker. Add a new dated column; never overwrite. Ask the three Perplexity buyer questions and record them in `measure/citations.md` |
| 2 | Add new questions from sales calls and from Search Console's non-brand queries to the question bank |
| 3 | Review the Run Log's fixes. Any mistake seen twice becomes a CLAUDE.md rule with a dated origin, and a check in `check_piece.py` if it can be automated |
| 4 | Re-run past pieces' evaluations to catch drift. Rewrite any title whose click-through is below the site average after 30 days. Pick the next question |

Ahrefs access ended on 31 October 2026. Weeks 1 and 4 need it back; until then, the Ahrefs readings are the frozen snapshot in `data/ahrefs/`. New readings go in new dated files there.

## Rank Tracker

Add these in Ahrefs Rank Tracker, US and Germany:

- best ai data analyst 2026
- how to evaluate ai data analyst accuracy
- ai data analyst accuracy
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

