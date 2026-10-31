# The three-piece plan

Written 31 October 2026, from Saurabh's decisions that day. Time available: 48 hours. This file is the plan; where each piece actually stands is read from the files by `python scripts/stage_gate.py <slug>`.

## The cluster

One buyer worry: **can you trust an AI analyst's answer before you rely on it?** Three pieces, one story:

| # | Piece | Bank | Role in the story | What it proves |
|---|---|---|---|---|
| 1 | `ai-analyst-follow-up-questions` | #43 | **The problem** | The same phrase, "delivered in 2017", got two correct answers for two different dates (2,453 and 1,762), and the answer that used delivery date never said so. Only its SQL did. |
| 2 | `ai-analyst-shows-sql` | #41, "AI analyst shows SQL" (score 10, highest in the bank) | **How to see it** | When an answer's text states the definition it used, and when only the SQL reveals it, counted answer by answer across ambiguous definitions (date, freight, order status, how "late" is measured). |
| 3 | not yet named | #47, "how much context does AI analyst need" | **How to fix it** | What changes when a team writes the ambiguous term down: the same questions with and without a context note that fixes the date reading. A null result ("we wrote it down and it still didn't hold") is a finding and is publishable. |

Six LinkedIn posts, two per piece. Post 1 of 6 is written (piece 1, Post A).

**Fit to the bank wording.** #47's long form asks "Can I start with ten definitions, or do I need everything?" Piece 3 tests one definition, so it answers the first step of that question, not the whole of it. Say so in the piece.

## What each run needs

All runs: workspace aiinterviewagents.com, the two Olist tables (`olist_orders_dataset`, `olist_order_items_dataset`), Balanced mode unless decided otherwise. **Rule 14 is not waived for pieces 2 and 3:** all five conditions screenshots for every batch (mode, credits before, credits after, environment, notes), named as in `runs/README.md#screenshots`. Piece 1 used the only waiver.

### Piece 1: done

- Run: batch 1, 31 October 2026, 8 questions in three chats (a five-question chain, two fresh chats). 8 of 8 correct. Conditions recorded by hand (rule 14 waived): no claim about mode, credits, environment or context notes.
- State: through the gate. Decision 4 (publish) open. The licence decision (facts L1) is recorded as a decision, not a resolution.

### Piece 2, `ai-analyst-shows-sql`: one batch, which also serves as piece 3's "without" batch

- **Questions:** about 6, each with rival readings computed **before** the run (`specs/<slug>-truth.json`, `"asked": false` rows):
  - At least two on **"delivered in <year>"** (for example a count and an item-price total), so piece 3 has date questions to compare.
  - One on **"how much did customers spend"** (freight in or out).
  - The rest on order status (all or delivered) and on "late" (calendar day or timestamp).
  - Piece 1's spec already holds several of these rivals (T2b timestamp grain, T7b with freight, T7c all statuses); reuse their definitions.
- **Each question asked in at least two fresh chats.** About 12 asks.
- **What only Dot can show:** each answer's text and SQL. The SQL comes back with every answer through the `ask_dot` MCP (`facts/dot-mcp.md`). The count is per answer: stated in the text, shown only in the SQL, or neither.
- **Conditions:** the active context notes must be screenshotted and listed (rule 17), because piece 3 compares against exactly this state.
- Credits: about 4–5, at piece 1's rate of 3.0 for 8 answers.

### Piece 3, bank #47 (slug not yet chosen): one new batch, after piece 2's run is complete

- **Order matters.** Under rule 4 a run stays valid until its definitions change, and adding the note is that change. Piece 2's run must be finished, marked and screenshotted before the note is created; after that, it is the "before" record, not a current run.
- **Steps:**
  1. Create a **new** context note fixing the reading of "delivered in <year>". Not a toggle-off of an existing note: the rehearsal could not tell "the note had no effect" from "switching it off didn't take".
  2. Create it **before** the credits-before screenshot. Facts O7 lists "a note with the context agent +20" as a credits milestone, so making the note can move the balance.
  3. Confirm the note exists with `get_catalog` (query: the term). Record the result in the run file. Whether a given answer used the note stays not observable via MCP; the evidence is the answers and their SQL.
  4. Ask the same questions as piece 2, worded identically, each in at least two fresh chats. About 12 asks.
- **Comparison:** item by item (rule 18), piece 2's answers against piece 3's, per question and per chat, so the note's effect can be told apart from chat-to-chat variation.
- **Decision point before step 1 (human): which reading the note fixes.** The natural team definition is the delivery date (`order_delivered_customer_date`). If piece 2's run shows Dot already reading every date question by delivery date, a delivery-date note can't show a change, and the note's reading has to be reconsidered then. Piece 1's run read the phrase both ways: purchase date in Q1, delivery date in Q6 and Q7.
- **What only Dot can show:** whether one written definition changes how Dot reads a term it otherwise reads inconsistently, on the same questions, on the same data.
- **What the rehearsal does and doesn't support (design only; rule 4 keeps its findings out of the pieces):** its note set "delivered orders", a scope Dot used anyway, and switching it off changed no figure, only whether Dot asked about the period. Piece 3's note is different in kind: it targets a reading Dot has made both ways.
- Credits: about 4–5.

## Which runs feed which

```
piece 1 run (31 Oct) ── evidence that "delivered in <year>" is read both ways ──► piece 3's design
piece 2 run ───────────── its own findings ───────────────────────────────────► piece 2
            └──────────── the "without note" batch (same questions, same notes) ─► piece 3
piece 3 run (note added) ── the "with note" batch ─────────────────────────────► piece 3
```

Piece 1's run is the same account and dataset, so rule 4 allows piece 2 and 3 to cite it; each piece's own findings still come from its own run.

## Time

About 11 hours of work across the 48 hours, screenshots included:

| Work | Estimate |
|---|---|
| Piece 2: research, truth spec, run with screenshots, marking | 1.5 h |
| Piece 2: outline (Decision 2), draft, reviews, revise | 1.5 h |
| Piece 2: human checks (headline, lift, second fact-check, phone read) | 1.5–2 h |
| Piece 3: note, catalog check, run with screenshots, marking, comparison | 1.5 h |
| Piece 3: outline, draft, reviews, revise | 1.5 h |
| Piece 3: human checks | 1.5–2 h |
| Five posts (one more for piece 1, two each for pieces 2 and 3) | 45 min |
| Handover | 1 h |

Order: piece 2's run, then piece 3's run, can happen back to back once piece 2's batch is marked; the writing of both can then proceed in parallel. Batch the human checks for both pieces into one sitting each.

## Decisions that stay human

The question (Decision 1), the outline (Decision 2), the title and human checks (Decision 3), the publish (Decision 4); plus, for piece 3, which reading the note fixes. The licence question (facts L1) stands for all three pieces.
