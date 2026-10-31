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
| A | Read aloud A's closing paragraph (a link clause added after Decision 3, not yet read); then Decision 4 | **Saurabh** |
| B | Rick's sign-off on the context agent quote and on the DABstep concession (and his answer on the home page's 96% / 89%); three census corrections found by the browser re-read (Snowflake's scoring cell, Snowflake missing from "more than one right answer", Ramp's scoring and trigger: see `runs/test-ai-analyst-before-rollout-verification.md`); A live first | **Rick**, then Saurabh, then publishing order |
| F | Re-check facts O1 and O2 on the current account ("Where Dot fits" rests on them); A and B live first (F links both) | **Saurabh**, then publishing order |
| Posts | Each goes out after its piece is live, with the link in the first comment | Publishing order |
| Licence | L1, L2, L4 are decisions to proceed, not resolutions; the Olist label was never verified at source | **Dot** |
| Assumptions A1–A8, and "does Dot's evaluation hold a pass bar?" | A yes, no or change | **Rick** (HANDOVER.md section 8) |

## 3. Pre-publish sequence

**A**
1. Read aloud A's closing paragraph.
2. Decision 4: publish A at `/blog/ai-analyst-follow-up-questions`.
3. `python scripts/bank.py status 43 published --basis "<URL>"`.

**B**
4. Get Rick's two sign-offs (context agent quote; DABstep concession) and his answer on the home page's 96% / 89%. If a full-set run is published, update B's DABstep sentence.
5. Decide the three census corrections from the browser re-read of B's eight remaining sources (done 1 November; every number matched; three method findings). Ramp's could change B's five to six.
6. Re-check O1 and O2 in Dot's UI (B's "Where Dot fits" cites the evaluation).
7. `python scripts/verify_sources.py pieces/how-companies-test-ai-data-analysts.md`: the link to A must now return 200.
8. Decision 4: publish B; `bank.py status 36 published`.

**F**
9. `verify_sources.py` on F: the links to A and B must return 200.
10. Decision 4: publish F; `bank.py status 35 published`.
11. Re-export any piece edited after its export (`/export <slug>`).

**Posts**
12. Post in the order above, each after its piece is live; link and UTM in the first comment.

## 4. Not done, and why

- **Tier 3** (agreed for after the pieces): the citation reading of the 18 buyer queries, `bank/surfaces.csv`, `/distribute`, `check_posts.py`, a post queue. Not started; the pieces came first.
- **The 18-query baseline.** The 18 queries are defined (`data/ahrefs/keywords.csv`, `is_buyer_query=yes`), but none has been read in an answer engine. The baseline is 3 Perplexity readings on topic labels (27 October) plus 2 on another question, and the frozen Ahrefs snapshot of 27–28 October. Ahrefs access ended 31 October.
- **F's final text has not been lift-tested.** The re-run was on the rewrite (61dda1a), before Decision 3's eight small fixes.
- **Check 25 for a guide** should test whether the steps survive compression, not one quoted line. Recorded in `prompts/06-edit.md`, not built.
- **No check that pieces agree with each other**, and none that flags a bare "N of M correct". Both errors were caught by people this time.
- **No chart stage** in the workflow; a missing chart passes the checker.
- **The `/linkedin` skill** still lists the older five structures, not the cluster's six.
- **The machine has been run cold once, to a research verdict** (a fresh session from the README alone, 1 November; gaps in HANDOVER.md section 6), **but never end to end by anyone but the author.** The monthly measurement loop has never run, and nothing is published, so there is no outcome to measure yet.
