# The question bank

**Read this first.** The bank is the input layer: the machine picks its next piece from it. Its inputs are thinner than the scores make them look.

## The honest state of the inputs, 31 October 2026

- **Only 3 of the 102 questions have an Ahrefs row, and all 3 read `not indexed`.** They are #1 "reduce ad hoc data requests", #32 "single source of truth metrics" and #35 "how to evaluate AI data analyst accuracy". The other 99 are "not measured". Phrases are matched exactly, never approximately, so no volume is estimated.
- **No question in the bank has a Search Console row.**
- **No question yet comes from a sales call.** Hard rule 1 puts sales-call questions first, and the PDF asked Rick and Théo for ten. None has been added. Until some are, `bank.py top` ranks by score alone and says so every time it runs.
- **Ahrefs access ended on 31 October 2026.** Volume, difficulty, "People also ask", current top pages and new Search Console queries can't be read. The snapshot in `data/ahrefs/` is frozen at 27–28 October 2026.
- **The citation series covers three questions,** asked on Day 0. Every other question's AI citations are "not measured".

## How each question is scored

Four factors, each 1 to 3, maximum 12 (ICP question bank PDF, page 4). The PDF gave only each question's total, kept as `pdf_score`. The factors are scored afresh, so movement from `pdf_score` can be shown.

| Factor | 1 | 2 | 3 | Scored by |
|---|---|---|---|---|
| `demand` | No source named | One or two sources named | Three or more sources, or a vendor built a page for it | `bank.py`, counting the external sources each row's notes name. Rows that mention a page are flagged for a person, since "a vendor built a page" can't be read reliably from the notes. Ahrefs volume is a note (`ahrefs_volume_us`), not part of this score |
| `gap` | A Dot page answers it | Dot touches it in passing | Dot has nothing | The `/bank` skill, by a live site check of getdot.ai and docs.getdot.ai from their sitemaps (296 and 81 pages on 31 October 2026), opening every page cited; marked `model-unconfirmed` until a person confirms. `site:` web searches returned no Dot pages that day, so a 3 means no page in the sitemaps answered it |
| `incumbent` | A strong page with original evidence ranks | Decent pages, none with original evidence | Only generic, undated or vendor-pitch pages | The `/bank` skill, by reading the top three pages, **for a shortlist only**: the top 15 by the other three factors, with a tie at the cut kept whole (17 on 31 October 2026). Every other row says "not scored". Page order is WebSearch's, not Google's, and dated |
| `evidence` | Anyone could write it | Dot's customer proof helps | Only running Dot can produce the evidence | The model proposes with a reason; **a person confirms.** `bank.py top` refuses to recommend a question whose evidence score is unconfirmed |

Each factor has a `_basis` column (what the score rests on) and a `_by` column (`data`, `model-unconfirmed` or `human`). `total` is filled only when all four factors are scored.

## Known bias: evidence scores come out inflated

**Expect it, and apply the two tests from the start.** On 31 October 2026 the model's evidence proposals were systematically too high, at both 3 and 2, for the same two reasons:

1. **Assuming Dot features that aren't in `facts/`**: lineage, Auto-Review, Git sync, row-level security, audit logs, usage limits, feedback, CI evaluations, environment behaviour, embedding, alerts, Deep Analysis, scheduled reports.
2. **Assuming data or customer proof we don't hold**: warehouses and tools not connected (Snowflake, Databricks, Looker, dbt, a BI tool, more than one source), user or personal data, data that changes over time, real request logs, Dot's internal rollout or usage data, and customer stories that were only hypothetical.

Counted by script:

- **Threes: 33 of 51 came down.** 30 failed the two tests; a person lowered 3 more (#29, #30, #34).
- **Twos: 11 of the 20 original twos fail the same tests.** #4 was set to 1. The other 10 (#7, #10, #22, #63, #84, #85, #86, #89, #90, #96) are recorded as failing but not yet changed. A 2 passes only when the customer proof it names is published and linkable (an impact page, public docs).
- **The 30 threes the tests lowered were set to 2, which is itself too high.** Their reasons name no customer proof, so by the same test they belong at 1. Not yet changed.

**The two tests, for anyone re-scoring:** (1) is the feature Observed in `facts/dot-facts.md` or `facts/dot-mcp.md`? An Assumption doesn't count. (2) Does the data or proof the score rests on actually exist and is it ours, or published and citable? Fail either, and the score comes down. The `/bank` skill states test (1) and the data half of test (2); the published-proof half applies to every 2.

## Open question for Rick: sales-call priority is literal

`bank.py top` puts every sales-call question ahead of every other question, whatever its score (hard rule 1). Tested on a scratch copy, 31 October 2026: a confirmed sales-call question scoring **4/12** outranked #43 at 11/12. So a single weak sales-call question currently jumps the whole bank.

Whether that is right is a question for Rick, not something to fix silently, so it is left literal. The alternative, **not implemented**, is a score floor: sales-call questions go first only if their total reaches a minimum (say 8/12), and below it they rank on score like any other question.

## The monthly loop

Run with the `/bank` skill (`.claude/skills/bank/SKILL.md`), which calls `scripts/bank.py`:

1. `/bank add`: new questions from sales calls (marked `from_sales_call: yes`) and from a Search Console export.
2. `/bank rescore`: re-score, and write a dated copy, `bank/scores-YYYY-MM-DD.csv`.
3. A person confirms the evidence scores: `python scripts/bank.py confirm <id> evidence`.
4. `/bank top`: the next question to write. Sales-call questions come first; ties on total break on Ahrefs volume only where it was measured.

## As of 31 October 2026

**Evidence 3s were tested against facts and data.** The first `/bank rescore` proposed evidence 3 for 51 questions. A 3 now needs two tests passed: the feature it relies on is Observed in `facts/` (not an Assumption), and Dot's two Olist tables hold the data the test needs. **18 of the 51 survive**: 2 confirmed by a person (#43, #35) and 16 still model-unconfirmed. 33 came down: 3 set by a person (#29 to 2, #30 and #34 to 1) and 30 by the tests, each with the failed test in its basis. Features that failed: lineage, Auto-Review, Git sync, row-level security, audit logs, usage limits, downvotes and feedback, CI evaluations, environment behaviour, embedding, alerts, Deep Analysis, scheduled reports. Data that failed: Snowflake, Databricks, Looker, dbt, a semantic layer, a BI tool, more than one source, personal data, a second user, and data that changes over time.

**Already covered by an existing piece:** #35 (piece 1), #1 (piece 2) and #61 (piece 3) are marked `drafted`, with the piece named in each row's source column. #36, #37 (piece 1), #60 and #66 (piece 3) overlap an existing piece in part; they stay `unwritten`, and the overlap is noted in their source column.

**Evidence scores are confirmed one at a time,** when a question is picked, not in bulk. `bank.py top` refuses to recommend a question while an unconfirmed one ranks above it.


`bank.py rescore` scored demand for all 102 questions: 62 score 1, 34 score 2, 6 score 3, and 15 are flagged for a person to check for a vendor page. Gap and evidence are proposed for all 94 unwritten questions, and incumbent for a shortlist of 17 (15, plus a tie kept whole). `top` recommends nothing until a person confirms evidence scores.
