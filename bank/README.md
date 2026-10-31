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
| `gap` | A Dot page answers it | Dot touches it in passing | Dot has nothing | The `/bank` skill, by a live site check of getdot.ai and docs.getdot.ai; marked `model-unconfirmed` until a person confirms |
| `incumbent` | A strong page with original evidence ranks | Decent pages, none with original evidence | Only generic, undated or vendor-pitch pages | The `/bank` skill, by reading the top three pages, **for a shortlist of 15 only**. Every other row says "not scored". Page order is WebSearch's, not Google's, and dated |
| `evidence` | Anyone could write it | Dot's customer proof helps | Only running Dot can produce the evidence | The model proposes with a reason; **a person confirms.** `bank.py top` refuses to recommend a question whose evidence score is unconfirmed |

Each factor has a `_basis` column (what the score rests on) and a `_by` column (`data`, `model-unconfirmed` or `human`). `total` is filled only when all four factors are scored.

## The monthly loop

Run with the `/bank` skill (`.claude/skills/bank/SKILL.md`), which calls `scripts/bank.py`:

1. `/bank add`: new questions from sales calls (marked `from_sales_call: yes`) and from a Search Console export.
2. `/bank rescore`: re-score, and write a dated copy, `bank/scores-YYYY-MM-DD.csv`.
3. A person confirms the evidence scores: `python scripts/bank.py confirm <id> evidence`.
4. `/bank top`: the next question to write. Sales-call questions come first; ties on total break on Ahrefs volume only where it was measured.

## As of 31 October 2026

`bank.py rescore` has scored demand for all 102 questions: 62 score 1, 34 score 2, 6 score 3, and 15 are flagged for a person to check for a vendor page. Gap, incumbent and evidence are not yet scored, so no question has a total and `top` recommends nothing.
