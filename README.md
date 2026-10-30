# Dot content machine

Turns a buyer's question into an evidence-led piece for getdot.ai, checks it harder than a reader would, and measures whether Dot gets chosen.

**New here? Read `HANDOVER.md` first.** It gets you from this folder to a working Claude Project in ten minutes, and through a 15-minute test run.

## What's here

| Path | What it is |
|---|---|
| `guides/Dot-Run-a-Full-Piece.pdf` | Step-by-step guide to one complete piece: 14 steps, 4 decisions, about 4½–5½ hours, with the trial's real example at each step |
| `guides/Dot-Machine-Tester-Guide.pdf` | A 30-minute first test: set up the Project and run RESEARCH once |
| `runs/` | Every Dot answer, word for word, one file per piece |
| `HANDOVER.md` | Set-up in your own Claude account, a 15-minute first test, how to run a full piece, the monthly loop, what's still open |
| `CLAUDE.md` | Every rule: 18 hard rules, 17 style rules, the seven stages, the 24-check gate, a dated change log (v1.6). The Claude Project's instructions are pasted from it. Claude Code reads it automatically |
| `PROJECT.md` | How to set up the Claude Project and run a stage |
| `runbook.md` | One piece in eleven steps, the four human decisions, the monthly loop |
| `prompts/01-research.md` … `07-linkedin.md` | The seven stage prompts |
| `scripts/check_piece.py` | Runs the 24-check gate on a piece: 15 checks decided alone, 3 with a person, 6 flagged for a human |
| `scripts/verify_sources.py` | Opens every link in a piece |
| `scripts/ground_truth.py` | Recomputes the 20 evaluation answers from the raw Olist CSVs |
| `scripts/charts.py` | One chart per piece from a JSON spec, with alt text and caption |
| `facts/dot-facts.md` | Observed in Dot (O1–O11), assumed (A1–A10, with basis), confirmed (D1: Rick's voice, "we" = Dot) |
| `facts/house-structure-and-links.md` | The anatomy of a piece; ten internal links verified 28 October 2026 |
| `pieces/piece-1.md`, `piece-2.md`, `piece-3.md` | The three pieces, in Rick's voice |
| `figures/piece-N-figures.csv` | Every number in each piece, with where it was computed |
| `figures/ground-truth.csv` | The 20 evaluation answers recomputed from the raw data |
| `charts/` | Each piece's chart, its spec, and its alt text |
| `posts/` | Six LinkedIn posts: A and B (piece 1), C and D (piece 2), E and F (piece 3) |
| `tracking/` | A note on the tracking sheet, a Google Sheet sent with this folder as a link: Question bank, Coverage, Sources, Figures, Baseline, Run Log |
| `data/` | A note on the Olist dataset (CC BY-NC-SA 4.0) and where to download it. The CSVs are not included |

## Quick start

    pip install pandas matplotlib
    python scripts/check_piece.py pieces/piece-1.md

Expected: `18 pass, 0 fail, 0 partial, 6 for a human`.

## Where the three pieces stand (28 October 2026)

- All three pass every automated check: 18 pass, 0 fail.
- Done on each: READER, two fact-checks (Claude and ChatGPT), the lift test in Perplexity and Claude.
- Open: the phone read (check 24) on all three; the lift test re-run on piece 1's new opening.
- Before publishing: re-run piece 1's evaluation in a Dot workspace (the trial ran on Olist, licensed non-commercial), and get a yes, no or change on assumptions A1–A8.

## What has been tested, and what hasn't

- **check_piece.py** runs on all three pieces. On a deliberately broken copy of piece 1 it caught all six planted problems. Four bugs were found while using it on pieces 2 and 3 (dates, labels, a quoted-voice count, a named-thing heuristic) and fixed; all three pieces were re-run afterwards. The planted errors were planted by the author.
- **ground_truth.py** matched 21 hand-computed answers on a small test dataset, then reproduced all 20 expected answers on the real Olist files (largest gap 0.152%, rounding). Delivered-only average order value: 137.0416, matching Dot's 137.04.
- **verify_sources.py** works, but the build environment couldn't reach getdot.ai; the ten links were opened in a browser instead. Run it on a normal connection.
- **charts.py** produced all three charts.
- **Tested by an outside person, 29 October 2026:** a tester who had never seen the machine set up the Claude Project from these files alone and ran RESEARCH on the rehearsal question. The rules loaded (she named the four human decisions correctly), and the verdict matched the author's run: PIECE, but NOT A PIECE if the test only reproduces piece 1. Her feedback: the tester's guide made "Instructions" sound like a file; it now says it's a box in Claude.
- **Not yet tested:** a full piece run by anyone other than the author; time per piece (never logged); the monthly loop (never run); any outcome (nothing is published).


---

# Runbook (merged from runbook.md)

# Runbook

One piece, end to end. One owner. Times are estimates from piece 1, which was run by hand; log the real times in the Run Log from piece 2 on.

## The four human decisions

1. **The question.** From the Question bank tab, calls first.
2. **The outline.** Approved before a word is drafted.
3. **The title.** Picked from three candidates.
4. **Publish.** Only when all 24 checks in CLAUDE.md pass.

## Eleven steps

| # | Step | How | Time |
|---|---|---|---|
| 1 | Pick the question | Decision 1. Question bank tab | 5 min |
| 2 | Research | `prompts/01-research.md` with Search Console, Keywords Explorer and AI-answer inputs. Add Sources rows | 30 min |
| 3 | Run the evidence in Dot | Screenshot the mode selector first. Read credits before and after. Log the conditions in the Run Log | 30–75 min |
| 4 | Recompute ground truth | `scripts/ground_truth.py`. Every number into the piece's figures CSV | 10 min |
| 5 | Outline | `prompts/02-outline.md`, then Decision 2 | 20 min |
| 6 | Draft | `prompts/03-draft.md` | 30 min |
| 7 | READER | `prompts/04-reader.md`, in a fresh chat. Fix the three stopping points | 15 min |
| 8 | Fact-check | `prompts/05-fact-check.md`: fresh chat, then a second model, then `verify_sources.py`. Log every fix | 30 min |
| 9 | Edit | `check_piece.py` until no FAIL; the headline test; the lift test in Perplexity and Claude. Decision 3 | 30 min |
| 10 | Chart and posts | `charts.py`; `prompts/07-linkedin.md` for each post, each with a different opening structure | 30 min |
| 11 | Gate and publish | The 24 checks; Decision 4; Webflow with UTM links; request three reverse links; add the target queries to Rank Tracker | 20 min |

## The monthly loop: 20 minutes a week, one owner

| Week | Do |
|---|---|
| 1 | Read the Baseline tab: Search Console click-through per piece, the Site Explorer AI-responses panel, Rank Tracker. Add a new dated column; never overwrite |
| 2 | Add new questions from sales calls and from Search Console's non-brand queries to the Question bank |
| 3 | Review the Run Log's fixes. Any mistake seen twice becomes a CLAUDE.md rule with a dated origin, and a check in `check_piece.py` if it can be automated |
| 4 | Re-run past pieces' evaluations to catch drift. Rewrite any title whose click-through is below the site average after 30 days. Pick the next question |

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
