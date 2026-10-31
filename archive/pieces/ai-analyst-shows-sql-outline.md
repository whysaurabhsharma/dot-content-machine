# OUTLINE: "Why does it matter whether the AI shows its SQL, and would anyone on my team read it?"

Piece slug: `ai-analyst-shows-sql`. Bank #41. Outlined 31 October 2026, from `runs/ai-analyst-shows-sql-research.md`, `runs/ai-analyst-shows-sql-run.md` (batch 1, Q1 to Q12), `figures/ai-analyst-shows-sql-figures.csv` (MR-Q1 to MR-Q12) and `figures/ai-analyst-shows-sql-truth.csv`.

**Rule 14 waiver.** Batch 1's conditions were recorded by hand at about 17:00 IST, with no screenshots (waived by Saurabh, 31 October 2026). Under that waiver the piece may make no claim about mode, credits, environment or context notes from this run: not the mode, not the cost, not which notes were on, and not that a note caused any reading. This outline therefore carries no mode in the chart caption and no cost per answer. Both conflict with a standing rule (style rule 14, hard rule 10); both decided 31 October 2026 (Missing figures).

**Research verdict honoured.** PIECE IF the piece claims only what the run counts and makes no claim about whether teams read SQL. "Almost nobody opens it" (the Playbook) is not used.

**Playbook stage:** Stage 3 · Prove (research section 3; https://www.getdot.ai/blog/ai-data-analyst-playbook).

## 1. Title candidates

**Working title for the draft, decided by Saurabh on 31 October 2026: "Your AI Analyst Counted Late Orders Two Ways".** House style from Dot's blog (short, flat claim, "Your X", no colon). The SEO title carries the buyer's words ("AI analyst shows SQL"). The candidates below stay open for Decision 3, after the reviews.

Buyer phrases from research section 2 only: "AI analyst shows SQL" (bank row 41, volume not measured), "ai data analyst" (700 US, 2.0K global), "text to sql accuracy" (10 US).

1. **Recommended.** AI data analyst shows SQL: 2,878 or 2,453 late orders, and how to tell which you got
2. AI analyst shows SQL: a test for whether the answer names its definition
3. Text to SQL accuracy: when every answer is correct and the two chats still disagree

Reason for 1: it carries the bank phrase inside the one measured phrase ("ai data analyst"), promises a check, and its proof is the run's real finding (MR-Q5 against MR-Q11), not the answers that matched.

Title 2 has no number from the run. Title 3's phrase has almost no volume (10 US).

## 2. The opening (57 words)

> **Ask an AI data analyst "How many orders were delivered late in 2017?" in two fresh chats, and you can get 2,878 and 2,453. That happened in Dot, on the Olist dataset. Both were correct, by different clocks. Each answer said which. By the end, you will have a test for whether your analyst shows its definition.**

Figures: MR-Q5 (2,878, timestamp grain, correct under its stated definition, T5b); MR-Q11 (2,453, calendar-day grain, T11); F03 (two fresh chats).

## 3. The surprising detail

> The same phrase, "delivered in 2017", meant two different years inside one batch. Asked for a count, Dot used the purchase date and returned 43,428 orders, saying "This uses purchase date, not delivery date." Asked for the total item price, it used the delivery date and returned BRL 5,612,818: "This uses delivery date, not purchase date." Both fresh-chat repeats chose the same way.

Figures: MR-Q1, MR-Q7 (43,428); MR-Q2, MR-Q8 (5,612,818, marked against T2d, the delivery-date reading, correct under its stated definition). Quotes name their questions (rule 13): Q1 "How many orders were delivered in 2017?" and Q2 "What was the total item price of orders delivered in 2017?", both from this run's chats.

## 4. Pocket guide

1. Showing the SQL matters when a question has two honest readings.
2. We asked Dot six ambiguous questions on the Olist dataset, each in two fresh chats.
3. Every answer checked out against figures computed from the raw CSVs, under the definition it stated.
4. One question split: "delivered late in 2017" gave 2,878 at timestamp grain and 2,453 by calendar day.
5. "Delivered in 2017" meant purchase year for a count and delivery year for a revenue total.
6. 11 of 12 answers' text named its date basis; on the twelfth, only the SQL showed it.
7. The SQL is the check when the text is silent and the reference when two chats disagree.
8. Ask your key question twice, fresh, and compare the stated definition and the date filter.

Figures: F01, F03 (line 2); MR-Q1 to MR-Q12 (line 3); MR-Q5, MR-Q11 (line 4); MR-Q1, MR-Q2, MR-Q7, MR-Q8 (line 5); F04, MR-Q4, F06 (line 6).

## 5. Three H2s

### H2 1: The same late-delivery question returned 2,878 and 2,453, and each answer named its clock

- Method in plain words: each question asked word for word in two fresh chats; rival readings computed from the raw CSVs before the run; each answer marked against the reading it stated. Judged item by item (hard rule 18).
- Finding: Q5, 2,878 (MR-Q5): "delivery occurred after the estimated delivery timestamp". Q11, 2,453 (MR-Q11): "they arrived after the estimated delivery day". Q11's SQL compares `CAST(... AS DATE)`; Q5's compares raw timestamps. Same words, different grain, both correct under their stated definitions.
- Limitation: two fresh chats chose different grains for "late".
- What the product does: the answer text named the grain both times, and the SQL showed the comparison line by line. A reader comparing the two sentences sees the difference without opening the SQL.
- What to do: pick one grain for "late" before you ask. No claim that writing it down fixes the split: this run didn't test that (piece 3 does). Say nothing about which note, if any, was active in this run (rule 14 waiver).

### H2 2: "Delivered in 2017" meant purchase year for a count and delivery year for a revenue total

- Method: Q1 and Q7 asked for a count; Q2 and Q8 asked for an item-price total. All four say "delivered in 2017".
- Finding: Q1 and Q7, 43,428 (MR-Q1, MR-Q7), purchase year, both chats. Q2 and Q8, BRL 5,612,818 (MR-Q2, MR-Q8), delivery year, both chats. Recurrence held item by item inside each question; the reading flipped between questions.
- Limitation: the phrase is ambiguous, and Dot did not resolve it the same way across question types.
- What the product does: every one of the four answers stated its date basis in the text ("This uses purchase date, not delivery date"; "This uses delivery date, not purchase date"), and each SQL filters on the matching column (`order_purchase_timestamp` or `order_delivered_customer_date`).
- Contrast: the purchase-year item price, BRL 5,962,902 (F09), and the delivery-year count, 40,930 (F10): the readings each answer did not use.

### H2 3: The SQL earns its place on the one answer whose text left the date out

- Method: for each answer, check whether the text names its date basis (the rule in F04's row), then whether the SQL's period filter names a date column (F06).
- Finding: Q4, "How many orders did we get in 2017?", answered 45,101 (MR-Q4) "including all order statuses", with no date basis in the text. Its SQL filters on `order_purchase_timestamp`. Q10, the same question in a fresh chat, returned 45,101 (MR-Q10) and said "based on purchase date".
- Limitation: on Q4, a reader who did not open the SQL could not tell which date was used.
- What the product does: the SQL is returned with every answer, so the date basis is one click away even when the text omits it.
- Counts: the text named its date basis in 11 of 12 answers (F04); every answer came back with SQL (F05: 12) whose period filter names a date column (F06: 12). Counted by script from the answer text, with the rule written in F04's row.
- No claim about whether anyone on a team reads the SQL (research verdict).

## 6. The table and the chart

**Table: six questions, two fresh chats each.** Columns: question (verbatim); chat A answer; chat B answer; reading stated in the text (A / B); what the SQL filters on; same reading in both chats? Rows: Q1/Q7 (MR-Q1, MR-Q7), Q2/Q8 (MR-Q2, MR-Q8), Q3/Q9 (MR-Q3, MR-Q9, BRL 6,921,535, purchase year, with shipping), Q4/Q10 (MR-Q4, MR-Q10), Q5/Q11 (MR-Q5, MR-Q11), Q6/Q12 (MR-Q6, MR-Q12, 7.7%). Only the values in the figures file; the "stated in text" column is yes/no per answer, read from the run file's Basis lines.

**Chart: one question, two fresh chats.** Two bars: 2,878 (Q5, timestamp grain) and 2,453 (Q11, calendar day), each labelled with the answer's own wording for "late".

- Alt text: "Bar chart. Asked 'How many orders were delivered late in 2017?' in two fresh chats, Dot returned 2,878 orders at timestamp grain and 2,453 by calendar day, on the Olist dataset."
- Caption: "Dot's answers to the same question in two fresh chats, Olist dataset, 31 October 2026." No mode: rule 14 was waived for this piece.

Figures: MR-Q5, MR-Q11.

## 7. Things to keep in mind

1. One dataset, one batch, each question asked in two fresh chats. This shows what can happen, not how often.
2. The run's settings were recorded by hand, not captured, so this piece says nothing about which settings or definitions shaped each reading.
3. The 2018 late share matched to display rounding: 7.7% in both chats against a reference of 7.725972% (MR-Q6, MR-Q12). The SQL left orders with missing dates out of the denominator; the reference did not. Rounding, not a disagreement (rule 12).
4. Whether a team reads the SQL was not measured.

## 8. Where Dot fits (draft wording, 43 words)

> In this run, every Dot answer came back with its SQL, 12 of 12, and the text named its date basis in 11. Where the text didn't, the SQL's period filter did. Dot's documentation is at https://docs.getdot.ai

Evidence: F04, F05, F06, from the run file. No Assumption used: A5 is not used (untested here; piece 3 tests whether writing a definition down settles a reading). No mode, credits, environment or note state from this run (rule 14 waiver).

## 9. The instruction

Ask your AI analyst "How many orders were delivered late last year?" in two fresh chats today. If the numbers differ, read each answer's definition sentence, then the date filter in its SQL.

Then the CTA: *If this excites you, we'd love to hear from you. Get in touch.*

## 10. Missing figures

Resolved 31 October 2026: every figure this outline wanted now has a row in `figures/ai-analyst-shows-sql-figures.csv`, counted by script from the run file and the truth file (rule 16):

- F01–F03: design counts (6 questions, 12 answers, 2 fresh chats per question).
- F04: 11 answers named their date basis in the text; F05: 12 came back with SQL; F06: 12 SQL filters name the date column.
- F07: 5 of 6 pairs agreed; F08: the 425 gap.
- F09, F10: the readings not used (BRL 5,962,902.01; 40,930).
- F11, F12: orders with no delivery date reported by Dot (2 in 2017; 6 in 2018).

Decided the same day, under the rule 14 waiver, as for piece 1: **no cost per answer** (credits after are recorded, 7.1 for the batch, but the waiver bars publishing them), and the chart caption gives the date and **no mode**. **Licence:** recorded as L2 in `facts/dot-facts.md`, a decision, not a resolution.

Approved by: Saurabh
Date: 2026-10-31
