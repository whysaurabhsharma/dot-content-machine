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

Dot's instruction of 1 November: where there is doubt, the piece takes a labelled assumption and a publish note says what to fix. Rick's answers no longer block the pieces.

| Item | Waiting on | Who |
|---|---|---|
| A, B, F | Each piece's publish note read and signed ("**Read by:**"), then Decision 4 | **Whoever publishes** |
| Post B3 (failure taxonomy) | **Held** until Rick answers question 7 (naming partners' gaps) | **Rick** |
| Other five posts | Their piece live | Publishing order |
| Licence | Saurabh's decisions to proceed (L1, L2, L4); the question stays Dot's | **Dot** |

| Piece | Publish note | Assumptions it carries |
|---|---|---|
| A | [reviews/ai-analyst-follow-up-questions/publish-note.md](reviews/ai-analyst-follow-up-questions/publish-note.md) | None pending |
| B | [reviews/how-companies-test-ai-data-analysts/publish-note.md](reviews/how-companies-test-ai-data-analysts/publish-note.md) | P-1 context agent quote (untested); P-2 evaluation (observed 27 October, not re-checked) |
| F | [reviews/test-ai-analyst-before-rollout/publish-note.md](reviews/test-ai-analyst-before-rollout/publish-note.md) | P-2 evaluation |

Rick's questions, which now confirm or reverse assumptions rather than block: [DECISIONS-FOR-DOT.md](DECISIONS-FOR-DOT.md).

## 3. Pre-publish sequence

All three pieces are exported (1 November 2026), each folder with its PUBLISH-NOTE.md: A 17 pass, B 18 pass, F 19 pass, 0 fail each.

**One session, in this order:**
1. Read A's publish note; fill its "Read by:" line. Publish A at `/blog/ai-analyst-follow-up-questions`.
2. Read B's publish note; fill "Read by:". Publish B at `/blog/how-companies-test-ai-data-analysts`.
3. Read F's publish note; fill "Read by:". Publish F at `/blog/test-ai-analyst-before-rollout`.
4. Run `python scripts/verify_sources.py pieces/<slug>.md` for all three: every cross-link (A to F, B to A and F, F to A and B) must now return 200.
5. `python scripts/bank.py status 43 published --basis "<URL>"`, then 36, then 35.
6. Posts, in order, each after its piece is live: B1, A2, F5, A6, F4. **B3 waits for Rick's question 7.**

**When Rick answers:** apply each publish note's replacement text, re-read the changed paragraph aloud, republish, and move P-1 or P-2 to Confirmed (or retire it) in `facts/dot-facts.md` with a change-log line.

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
