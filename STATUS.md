# Status · Dot content machine

1 November 2026. Where the submission stands, in two minutes. Rick's questions, in the order they block publication: [DECISIONS-FOR-DOT.md](DECISIONS-FOR-DOT.md). Detail and reasons: `HANDOVER.md`. Where each piece stands is always read from the files: `python scripts/stage_gate.py <slug>`.

## 1. Delivered

| What | One line |
|---|---|
| **A**, research: `ai-analyst-follow-up-questions` | "Your AI Analyst Picked a Date. Only the SQL Said Which." Our run on Dot: two right answers to one phrase, 691 apart, and a six-step test. 17 pass, 0 fail. Exported |
| **B**, teardown: `how-companies-test-ai-data-analysts` | "7 Companies Published Their AI Analysts' Accuracy. No Two Measured the Same Thing." A census of 13 companies' published testing methods. 18 pass, 0 fail. Exported |
| **F**, guide (the hub): `test-ai-analyst-before-rollout` | "How to Test an AI Data Analyst Before Rollout: 8 Steps", each step tagged with its evidence. 19 pass, 0 fail. Exported |
| **Six LinkedIn posts** | Two per piece, six different structures, first lines by Saurabh. All pass the post checks. Order: B1, A2, B3, F5, A6, F4 (the cluster numbers in `PLAN.md`) |
| **The baseline** | `measure/baseline-2026-11-01.md`: 5 of the 18 buyer queries, read in Google, Perplexity and ChatGPT (15 readings) on 1 November 2026, before any piece went live. Dot cited 0 times in 15. This completes the brief's deliverable 4 (Saurabh, 1 November 2026). The other 13 queries are unread (HANDOVER.md section 5) |
| **The machine** | `/piece <slug>` runs research to export in Claude Code, stopping at seven points a person owns; 25-check gate (`check_piece.py`); rulebook `CLAUDE.md` v1.8.26 |

Exports: `exports/<slug>/` (a .docx, clean Markdown, Webflow HTML and fields; not in git).

## 2. What each item waits on

Dot answered five of the eight questions on 1 November 2026 (Rick and Théo): the evaluation is current, the Olist licence is fine, the byline is Saurabh Sharma, naming partners is approved, and A1–A8 stays unresolved (none is in the pieces). Nothing blocks publishing.

| Item | Waiting on | Who |
|---|---|---|
| A, B, F | Each piece's publish note read and signed ("**Read by:**"), then Decision 4 | **Whoever publishes** |
| All six posts | Their piece live (post B3 released from hold) | Publishing order |

| Piece | Publish note | Still labelled in the text |
|---|---|---|
| A | [reviews/ai-analyst-follow-up-questions/publish-note.md](reviews/ai-analyst-follow-up-questions/publish-note.md) | Nothing |
| B | [reviews/how-companies-test-ai-data-analysts/publish-note.md](reviews/how-companies-test-ai-data-analysts/publish-note.md) | P-1, the context agent quote ("Assumption: … we haven't tested it") |
| F | [reviews/test-ai-analyst-before-rollout/publish-note.md](reviews/test-ai-analyst-before-rollout/publish-note.md) | Nothing |

Still open with Dot, none blocking: question 1 (context agent page, labelled in B), question 2 (the DABstep figures; B's sentence is accurate as written), question 5 (a pass bar in Dot's evaluation; F makes no such claim). See [DECISIONS-FOR-DOT.md](DECISIONS-FOR-DOT.md).

## 3. Pre-publish sequence

All three pieces are exported (1 November 2026), each folder with its PUBLISH-NOTE.md and the byline in `webflow-fields.json`: A 17 pass, B 18 pass, F 19 pass, 0 fail each.

**One session, in this order:**
1. Read A's publish note; fill its "Read by:" line. Publish A at `/blog/ai-analyst-follow-up-questions`, author Saurabh Sharma.
2. The same for B, at `/blog/how-companies-test-ai-data-analysts`.
3. The same for F, at `/blog/test-ai-analyst-before-rollout`.
4. Run `python scripts/verify_sources.py pieces/<slug>.md` for all three: every cross-link (A to F, B to A and F, F to A and B) must now return 200.
5. `python scripts/bank.py status 43 published --basis "<URL>"`, then 36, then 35.
6. Posts, in order, each after its piece is live: B1, A2, B3, F5, A6, F4.

**Publish order considered and kept: A, B, F (Saurabh, 1 November 2026).** The baseline suggested F first, because its target query has the weakest page one of the five read. Kept A, B, F because F is the hub and both others link to it. **The one-session requirement, not the order, is what prevents dead links**: any order puts at least one dead link live until the last piece is up (A first links to F). Correction: the first version of this note gave the reason as "F first would put two dead links on a live page", which implied A first puts none; Claude corrected it on 1 November 2026.

**A link from A to B considered and rejected (Saurabh, 1 November 2026).** A links to F only; F links to A and B; B links to A and F. That is the hub shape by design: F, the hub, is one click from both others, and every piece reaches every other within two clicks (A reaches B through F). Adding A to B would cost a re-read aloud, `check_piece.py` and a re-export on a piece past Decision 3, for little a reader gains. Not a gap.

**When Rick answers question 1:** apply B's publish note's replacement text, re-read that paragraph aloud, republish, and move P-1 to Confirmed (or retire it) in `facts/dot-facts.md`.

## 4. Not done, and why

- **Tier 3** (agreed for after the pieces): the citation reading of the other 13 buyer queries, `bank/surfaces.csv`, `/distribute`, `check_posts.py`, a post queue. Not started; the pieces came first.
- **13 of the 18 buyer queries are unread.** The baseline read 5 (above). The rest are named in HANDOVER.md section 5. Repeat readings need a Perplexity account (the same one each time) and the same location for Google.
- **F's final text has not been lift-tested.** The re-run was on the rewrite (61dda1a), before Decision 3's eight small fixes.
- **Check 25 for a guide** should test whether the steps survive compression, not one quoted line. Recorded in `prompts/06-edit.md`, not built.
- **No check that pieces agree with each other**, and none that flags a bare "N of M correct". Both errors were caught by people this time.
- **No chart stage** in the workflow; a missing chart passes the checker.
- **The `/linkedin` skill** still lists the older five structures, not the cluster's six.
- **Cold-start gaps 1 and 2: fixed 1 November.** The handover's first test now follows the gate (Decision 1, research, PIECE IF check, truth spec reviewed, then the run). The gate has a PIECE IF branch: it waits until a person records how the condition was met (`stage_gate.py clear`). F's condition is recorded as Saurabh's (L4 and the browser re-read); A's was recorded from the files and confirmed by Saurabh the same day (commit b8528c7). Gaps 3 to 7 were fixed the same day (CLAUDE.md v1.8.21).
- **The machine has been run cold three times** (fresh sessions from the README alone, 1 November: a research verdict, a marked Dot run, the teardown first test; what was fixed and what is open in HANDOVER.md, "For a newcomer"), **but never end to end by anyone but the author.** The monthly measurement loop has never run, and nothing is published, so there is no outcome to measure yet.
