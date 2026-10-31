# Status · Dot content machine

1 November 2026. Where the submission stands, in two minutes. Rick's questions, in the order they block publication: [DECISIONS-FOR-DOT.md](DECISIONS-FOR-DOT.md). Detail and reasons: `HANDOVER.md`. Where each piece stands is always read from the files: `python scripts/stage_gate.py <slug>`.

## 1. Delivered

| What | One line |
|---|---|
| **A**, research: `ai-analyst-follow-up-questions` | "Your AI Analyst Picked a Date. Only the SQL Said Which." Our run on Dot: two right answers to one phrase, 691 apart, and a six-step test. 17 pass, 0 fail. Exported |
| **B**, teardown: `how-companies-test-ai-data-analysts` | "7 Companies Published Their AI Analysts' Accuracy. No Two Measured the Same Thing." A census of 13 companies' published testing methods. 18 pass, 0 fail. Exported |
| **F**, guide (the hub): `test-ai-analyst-before-rollout` | "How to Test an AI Data Analyst Before Rollout: 8 Steps", each step tagged with its evidence. 19 pass, 0 fail. Exported |
| **Six LinkedIn posts** | Two per piece, six different structures, first lines by Saurabh. All pass the post checks. Order: B1, A2, B3, F5, A6, F4 (the cluster numbers in `PLAN.md`) |
| **The machine** | `/piece <slug>` runs research to export in Claude Code, stopping at seven points a person owns; 25-check gate (`check_piece.py`); rulebook `CLAUDE.md` v1.8.13 |

Exports: `exports/<slug>/` (a .docx, clean Markdown, Webflow HTML and fields; not in git).

## 2. What each item waits on

| Item | Waiting on | Who |
|---|---|---|
| A | Decision 4 (all checks and read-alouds done; PIECE IF confirmed) | **Saurabh** |
| B | Rick's answers to questions 1, 2 and 7 (context agent quote, DABstep figures, naming partners); then O1 and O2 re-checked (question 3); A live first | **Rick**, then Saurabh, then publishing order |
| F | Question 3 (O1 and O2, which its "Where Dot fits" rests on); A and B live first (F links both) | **Rick or Saurabh**, then publishing order |
| Posts | Each goes out after its piece is live, link and UTM in the first comment | Publishing order |
| Licence | Question 4: L1, L2, L4 are decisions to proceed, not resolutions | **Dot** |

Rick's questions: [DECISIONS-FOR-DOT.md](DECISIONS-FOR-DOT.md), eight, ordered by what blocks publication.

## 3. Pre-publish sequence

All three pieces are exported as they stand (1 November 2026): A 17 pass, B 18 pass, F 19 pass, 0 fail each. Every piece's human checks are recorded in `reviews/<slug>/human.md`.

**A**
1. Decision 4: publish at `/blog/ai-analyst-follow-up-questions`.
2. `python scripts/bank.py status 43 published --basis "<URL>"`.
3. Post A2 (the transcript), link in the first comment.

**B**
4. Rick answers questions 1, 2 and 7. If any answer changes B, edit, re-read the changed paragraphs aloud, re-export.
5. Re-check facts O1 and O2 in Dot's UI (question 3).
6. `python scripts/verify_sources.py pieces/how-companies-test-ai-data-analysts.md`: the link to A must now return 200.
7. Decision 4: publish B; `bank.py status 36 published`.
8. Posts B1 (the number) and B3 (the failure taxonomy), spaced apart.

**F**
9. `verify_sources.py` on F: the links to A and B must return 200.
10. Decision 4: publish F; `bank.py status 35 published`.
11. Posts F5 (the checklist) and F4 (the contrarian read).

**Post order across the cluster:** B1, A2, B3, F5, A6, F4. A6 (the build log) can go any time after A is live.

## 4. Not done, and why

- **Tier 3** (agreed for after the pieces): the citation reading of the 18 buyer queries, `bank/surfaces.csv`, `/distribute`, `check_posts.py`, a post queue. Not started; the pieces came first.
- **The 18-query baseline.** The 18 queries are defined (`data/ahrefs/keywords.csv`, `is_buyer_query=yes`), but none has been read in an answer engine. The baseline is 3 Perplexity readings on topic labels (27 October) plus 2 on another question, and the frozen Ahrefs snapshot of 27–28 October. Ahrefs access ended 31 October.
- **F's final text has not been lift-tested.** The re-run was on the rewrite (61dda1a), before Decision 3's eight small fixes.
- **Check 25 for a guide** should test whether the steps survive compression, not one quoted line. Recorded in `prompts/06-edit.md`, not built.
- **No check that pieces agree with each other**, and none that flags a bare "N of M correct". Both errors were caught by people this time.
- **No chart stage** in the workflow; a missing chart passes the checker.
- **The `/linkedin` skill** still lists the older five structures, not the cluster's six.
- **Cold-start gaps 1 and 2: fixed 1 November.** The handover's first test now follows the gate (Decision 1, research, PIECE IF check, truth spec reviewed, then the run). The gate has a PIECE IF branch: it waits until a person records how the condition was met (`stage_gate.py clear`). F's condition is recorded as Saurabh's (L4 and the browser re-read); A's was recorded from the files for Saurabh to confirm. Gaps 3 to 7 stay open (HANDOVER.md section 6).
- **The machine has been run cold once, to a research verdict** (a fresh session from the README alone, 1 November; gaps in HANDOVER.md section 6), **but never end to end by anyone but the author.** The monthly measurement loop has never run, and nothing is published, so there is no outcome to measure yet.
