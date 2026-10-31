# The three-piece plan

Written 31 October 2026, from Saurabh's decisions that day. Time available: 48 hours. This file is the plan; where each piece actually stands is read from the files by `python scripts/stage_gate.py <slug>`.

## The cluster

One buyer worry: **can you trust an AI analyst's answer before you rely on it?** Three pieces, one story:

| # | Piece | Bank | Role in the story | What it proves |
|---|---|---|---|---|
| 1 | `ai-analyst-follow-up-questions` | #43 | **The problem** | The same phrase, "delivered in 2017", got two correct answers for two different dates (2,453 and 1,762), and the answer that used delivery date never said so. Only its SQL did. |
| 2 | `ai-analyst-shows-sql` | #41, "AI analyst shows SQL" (score 10, highest in the bank) | **How to see it** | When an answer's text states the definition it used, and when only the SQL reveals it, counted answer by answer across ambiguous definitions (date, freight, order status, how "late" is measured). |
| 3 | `ai-analyst-how-much-context` (proposed) | #47, "how much context does AI analyst need" | **What to write down** | **What the note defined held. The phrase it left open was read two ways, and the term it never defined varied from chat to chat.** Piece 3's own run tests whether writing those two down ("late", and how to read "delivered in <year>") settles them. Either outcome is publishable. |

Six LinkedIn posts, two per piece. Post 1 of 6 is written (piece 1, Post A).

**Fit to the bank wording.** #47's long form asks "Can I start with ten definitions, or do I need everything?" Piece 3 tests one definition, so it answers the first step of that question, not the whole of it. Say so in the piece.

## What each run needs

All runs: workspace aiinterviewagents.com, the two Olist tables (`olist_orders_dataset`, `olist_order_items_dataset`), Balanced mode unless decided otherwise. **Rule 14:** the plan first required all five screenshots for every batch of pieces 2 and 3. **Changed 31 October 2026 (Saurabh): piece 2's batch 1 is waived too**, conditions recorded as text (`runs/ai-analyst-shows-sql-run.md`). Piece 2 may claim nothing about mode, credits, environment or notes. Piece 3's requirement is open: see its section.

### Piece 1: done

- Run: batch 1, 31 October 2026, 8 questions in three chats (a five-question chain, two fresh chats). 8 of 8 correct. Conditions recorded by hand (rule 14 waived): no claim about mode, credits, environment or context notes.
- State: through the gate. Decision 4 (publish) open. The licence decision (facts L1) is recorded as a decision, not a resolution.

### Piece 2, `ai-analyst-shows-sql`: one batch, done

- **Questions:** about 6, each with rival readings computed **before** the run (`specs/<slug>-truth.json`, `"asked": false` rows):
  - At least two on **"delivered in <year>"** (for example a count and an item-price total), so piece 3 has date questions to compare.
  - One on **"how much did customers spend"** (freight in or out).
  - The rest on order status (all or delivered) and on "late" (calendar day or timestamp).
  - Piece 1's spec already holds several of these rivals (T2b timestamp grain, T7b with freight, T7c all statuses); reuse their definitions.
- **Each question asked in at least two fresh chats.** About 12 asks.
- **What only Dot can show:** each answer's text and SQL. The SQL comes back with every answer through the `ask_dot` MCP (`facts/dot-mcp.md`). The count is per answer: stated in the text, shown only in the SQL, or neither.
- **Conditions:** recorded by hand, rule 14 waived (31 October 2026). Notes on: the metrics note and the currency note; off: "About aiinterviewagents.com". The metrics note's full text is saved verbatim in the run file.
- **Result, 31 October 2026:** 12 of 12 correct. Against the metrics note: 10 of 12 followed its purchase-cohort rule; the two that didn't were the same question (item price of orders "delivered in 2017"), in both chats, each stating its delivery-date basis. "Late" (not defined in the note) was read at timestamp grain in one chat and calendar day in the other. Piece 2's run is now context for piece 3, not its "without" batch.
- Credits: about 4–5, at piece 1's rate of 3.0 for 8 answers.

### Piece 3, `ai-analyst-how-much-context` (proposed), bank #47: its own before and after batches

Redesigned 31 October 2026, after piece 2's run. The metrics note already states the date rule ("Unless explicitly requested otherwise, report a purchase cohort using order_purchase_timestamp"), so piece 3 no longer adds a first definition. It tests whether writing down what the note leaves open settles it.

- **What the existing note leaves open (from piece 2's run, read against the note's verbatim text in `runs/ai-analyst-shows-sql-run.md`):**
  - **The let-out clause.** "Unless explicitly requested otherwise" was applied to "orders delivered in 2017" for item price (delivery date, both chats) but not for the order count (purchase date, both chats).
  - **"Late".** The note never defines it, or the estimated delivery date. One chat compared timestamps (2,878), the other calendar days (2,453).
- **Questions:** 4, worded exactly as in piece 2, each in **three** fresh chats per batch (two can't tell a settled reading from variance). 12 asks per batch, 24 in all.
  1. "How many orders were delivered late in 2017?" (late grain)
  2. "What percentage of delivered orders were late in 2018?" (late grain)
  3. "What was the total item price of orders delivered in 2017?" (the let-out)
  4. "How many orders were delivered in 2017?" (control: followed the note in piece 2)
- **Truth spec before the run:** each question's rivals (calendar day and timestamp; purchase and delivery date; their combinations), as in piece 2's spec.
- **Batch 1, before:** notes exactly as in piece 2. **Notes screenshot** (Model → Notes); `get_catalog` read recorded.
- **Between the batches, in this order:**
  1. Create a **new** note (not an edit of the metrics note, so the before text stays as recorded). Draft text, for a person to approve: *"Late: an order is late when the date part of order_delivered_customer_date is later than the date part of order_estimated_delivery_date (calendar day). Orders with no delivery date are reported as a gap, not counted as on time or late. 'Delivered in <year>' means delivered orders in that year's purchase cohort, as the shared reporting rules state; use the delivery date only when a question asks when orders reached customers, for example 'by delivery date'."*
  2. Take credits before **after** creating it (facts O7: a note made with the context agent can add 20 credits).
  3. Confirm the note with `get_catalog`; record the result.
  4. **Notes screenshot** showing the new note on and the others as before.
- **Batch 2, after:** the same 4 questions, 3 fresh chats each.
- **Comparison:** item by item and chat by chat (rule 18): does "late" settle on calendar day in all three chats? Does item price follow the purchase cohort? Does the control stay put?
- **Evidence and claims:** the notes screenshot for both batches; mode, credits and environment recorded by hand (rule 14 waived for those three). So the piece may say which notes were on and what they said, and may not claim mode, credits or environment.
- **Rule 4:** piece 2's run is the same account and dataset and stays citable as context, but piece 3's finding comes from its own two batches.
- **Decision point before the note is created (human):** approve the note's text.
- Credits: about 14 for 24 asks, at piece 2's rate (7.1 for 12). About 202 remain.

## Which runs feed which

```
piece 1 run (31 Oct) ── "delivered in <year>" read both ways ───────────────► piece 3's design
piece 2 run (31 Oct) ── its own findings ────────────────────────────────────► piece 2
            └────────── what the note leaves open (let-out, "late") ────────► piece 3's design
piece 3 batch 1 ──────── before: existing notes ────────────────────────────► piece 3
piece 3 batch 2 ──────── after: plus one note on "late" and the let-out ────► piece 3
```

Piece 1's run is the same account and dataset, so rule 4 allows piece 2 and 3 to cite it; each piece's own findings still come from its own run.

## Time

About 11 hours of work across the 48 hours, screenshots included:

| Work | Estimate |
|---|---|
| Piece 2: research, truth spec, run with screenshots, marking | 1.5 h |
| Piece 2: outline (Decision 2), draft, reviews, revise | 1.5 h |
| Piece 2: human checks (headline, lift, second fact-check, phone read) | 1.5–2 h |
| Piece 3: truth spec, two batches with notes screenshots, the note, catalog checks, marking, comparison | 2.5 h |
| Piece 3: outline, draft, reviews, revise | 1.5 h |
| Piece 3: human checks | 1.5–2 h |
| Five posts (one more for piece 1, two each for pieces 2 and 3) | 45 min |
| Handover | 1 h |

Order: piece 2's run, then piece 3's run, can happen back to back once piece 2's batch is marked; the writing of both can then proceed in parallel. Batch the human checks for both pieces into one sitting each.

## Decisions that stay human

The question (Decision 1), the outline (Decision 2), the title and human checks (Decision 3), the publish (Decision 4); plus, for piece 3, the new note's text. The licence question (facts L1) stands for all three pieces.
