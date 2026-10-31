# OUTLINE: "Does it keep context across follow-ups, and how do I test that?"

Piece slug: `ai-analyst-follow-up-questions`. Bank #43. Outlined 31 October 2026, from `runs/ai-analyst-follow-up-questions-research.md`, `runs/ai-analyst-follow-up-questions-run.md` (batch 1), `figures/ai-analyst-follow-up-questions-figures.csv` and `figures/ai-analyst-follow-up-questions-truth.csv`.

**Rule 14 waiver.** Batch 1's conditions were recorded by hand, with no screenshots (waived by Saurabh, 31 October 2026). Under that waiver, the piece may make no claim about mode, credits, environment or context notes from this run. This outline therefore carries no mode in the chart caption and no cost per answer. Both conflict with a standing rule (style rule 14, hard rule 10); see Missing figures, items 7 and 8, for the decision a person must make.

**Playbook stage:** Stage 3 · Prove (research section 3; https://www.getdot.ai/blog/ai-data-analyst-playbook).

## 1. Title candidates

**Working title for the draft, decided by Saurabh on 31 October 2026: "AI analyst follow-up questions: a context test you can copy".** /draft uses this as the front-matter title, not the recommended candidate below: candidate 3's shape (the buyer's phrase and a clear promise), with the numbers carried in the lede rather than the title. All three candidates below stay open for Decision 3, after the reviews.

Buyer phrases used are from research section 2 only: "AI analyst follow-up questions context" (bank row 43, volume not measured), "ai data analyst" (700 US), "conversational analytics" (1.2K US).

1. **Recommended.** AI analyst follow-up questions: a context test, and why "delivered in 2017" gave 2,453 and 1,762
2. AI data analyst follow-up questions: it recalled 43,428 four turns later, and read the same words two ways
3. Conversational analytics follow-ups: how to test context with one chain and one fresh chat

Reason for 1: it carries the bank's own phrasing, promises the reader a test, and its proof is the run's real finding (MR-Q2 against MR-Q6), not the clean recall.

Title 2's "four turns" now has a Figures row (F04). Title 3 has no number from the run.

## 2. The opening (59 words)

> **Buyers ask whether an AI analyst keeps context across follow-up questions. We tested Dot on the Olist dataset with a chain of follow-ups. It recalled 43,428 orders four turns later. But "delivered in 2017" meant 2,453 late orders inside the chain and 1,762 in a fresh chat. By the end, you will have a follow-up test to run yourself.**

Figures: MR-Q1, MR-Q5 (43,428); MR-Q2 (2,453); MR-Q6 (1,762). "Four turns" is a design count (Missing figures, item 2).

## 3. The surprising detail

> The fresh chat that returned 1,762 never said which date it used. Its answer to "How many orders delivered in 2017 were delivered later than their estimated delivery date?" read: "1,762 orders delivered in 2017 arrived after their estimated delivery date." Only the figure gave the date away: it matches the count by delivery date, not purchase date. A second fresh chat, asked for total item price, did say: "This uses the customer delivery date, not the purchase date."

Figures: MR-Q6 (marked against T2c, the delivery-date reading, decided by a person); MR-Q7 (correct under its stated definition, T7d). Quotes name their questions (rule 13): Q6 and Q7, both from this run's chats.

## 4. Pocket guide

1. "Does it keep context?" has two halves: does it remember, and does it read your words the same way.
2. We asked Dot eight questions on the Olist dataset: a five-question follow-up chain, then two fresh chats.
3. Memory held: asked "going back to my first question", Dot returned 43,428 again.
4. Scope held: "How much of that came in November?" kept the delivery-date reading of the question before it.
5. Interpretation moved: "delivered in 2017" meant purchase year inside the chain, delivery date in a fresh chat.
6. So the same words gave 2,453 late orders in the chain and 1,762 in a fresh chat.
7. Each answer's SQL showed which date it filtered on, even where the answer text didn't say.
8. Test a chain, then re-ask its key question cold, and compare the date filter in the SQL.

Figures: MR-Q5 (line 3); MR-Q7, MR-Q8 (line 4); MR-Q1, MR-Q6, MR-Q7 (line 5); MR-Q2, MR-Q6 (line 6). "Eight", "five-question" and "two fresh chats" are design counts (Missing figures, item 2).

## 5. Three H2s

### H2 1: Dot kept context through a five-question follow-up chain

- Method in plain words: one chat, five questions, each leaning on the one before ("those", "that share", "for 2018", "my first question"). Then a fresh chat with one follow-up. Every answer checked against figures computed from the raw Olist CSVs.
- Finding: MR-Q1 43,428 and MR-Q5 43,428, the recall exact. MR-Q2 2,453 late among "those". MR-Q3 5.6% and MR-Q4 7.7%, display rounding of 5.648% and 7.726% (rule 12: rounding, not a gap). MR-Q8 BRL 651,458 kept MR-Q7's delivery-date scope.
- Limitation: the chain fixed its reading of "delivered in 2017" at the first answer, and every follow-up inherited it.
- What the product does: Q1's answer named its date unprompted: "This uses purchase date, not delivery date." The reader could catch the choice at turn one.

### H2 2: The same words got a different date with no prior turns

- Method: Q6 is Q2 written in full, asked in a fresh chat as the control. Q7 is a fresh chat on item price with the same phrase. Judged item by item (hard rule 18).
- Finding: Q2 in the chain, 2,453 (MR-Q2, purchase year). Q6 in a fresh chat, 1,762 (MR-Q6, delivery date). Q7, BRL 5,612,818 (MR-Q7, delivery date, stated).
- Not lost context: the control did not reproduce Q2 because, without history, Dot read the phrase the other defensible way. Both readings are correct under their own date.
- Limitation: a fresh-chat control that "fails" can be an interpretation change, not a memory failure.
- What the product does: every answer came with its SQL, and the SQL shows which date set the year: the year filter is on the purchase date (`order_purchase_timestamp`) in Q1–Q5, and on the delivery date (`order_delivered_customer_date`) in Q6–Q8. Q2–Q4 also read the delivery date, to measure lateness (run file, SQL blocks).

### H2 3: Basis statements were inconsistent, so read the SQL as well as the sentence

- Method: read each answer's text for the date it used.
- Finding: Q7 named its date; Q6 did not (quotes as in section 3). MR-Q6 was marked correct only after a person decided the delivery-date reading (`--decide`), since the answer gave no basis to infer it from.
- Limitation: an answer can be right and still not tell you which question it answered.
- What the product does: the SQL shows the date filter on every answer, so a reader can check which date was used even when the answer text doesn't say.

## 6. The table and the chart

**Table.** One row per question, Q1–Q8: chat (A chain, B fresh, C fresh plus follow-up); the question as asked; Dot's figure (MR row); the date Dot filtered on, from its SQL; whether the answer text named that date; verdict (correct exact, correct with display rounding, correct under stated definition, correct as decided by a person). Lets the reader judge item by item.

**Chart.** Two horizontal bars, late orders for "delivered in 2017": inside the chain, 2,453 (MR-Q2); fresh chat, 1,762 (MR-Q6). Bars labelled by the date each answer used: purchase date, delivery date.

- Alt text: "Bar chart of two Dot answers to how many orders delivered in 2017 were late, on the Olist dataset. Inside a follow-up chain, Dot used purchase date and returned 2,453. In a fresh chat, it used delivery date and returned 1,762."
- Caption: "Late orders for 'delivered in 2017', asked inside a follow-up chain and in a fresh chat. Olist dataset, Dot, 31 October 2026. Mode not recorded for publication (rule 14 waived)." Decided 31 October 2026 (option a): the caption says why the mode is missing rather than naming it.

## 7. Things to keep in mind

1. One run, one dataset, eight questions. The same question can take different paths, so a re-run can differ.
2. "Delivered in 2017" was ambiguous on purpose. Q6 and Q8 were marked correct under the delivery-date reading, decided by a person; neither is an error.
3. The late shares left out orders with no delivery date, and Dot said so in its answers to Q3 and Q4.
4. This run's conditions were recorded by hand, without screenshots, so its mode and cost aren't published.

## 8. Where Dot fits (59 words)

> Every answer in this test came with its SQL, so the date filter was visible even when the text skipped it. In Dot, a definition such as what "delivered in" means can live in a context note, with a title, access groups and a Foundational toggle. Each evaluation question holds an expected answer and a percent tolerance. Docs: docs.getdot.ai.

Facts: run file SQL blocks (evidence in the piece); O3; O1. No Assumption, and no Superseded fact. A5 was cut on 31 October 2026: rehearsal batch 2 found that switching the metrics note off changed no figure, so the line couldn't be vouched for (the rehearsal finding itself stays out of the piece, hard rule 4).

## 9. The instruction

Write five follow-ups on your own data, each leaning on the last. Then ask the first one again, in full, in a fresh chat. Compare the date filter in both answers' SQL before you trust either number.

## 10. Missing figures

None. On 31 October 2026 every figure this outline wanted was added to `figures/ai-analyst-follow-up-questions-figures.csv` by script, from the run file, the truth file and the raw orders CSV:

- F01–F04: design counts (8 questions, 3 chats, a 5-question chain, recall 4 turns later).
- F05: 8 of 8 correct.
- F06, F07: purchase-year contrasts for Q7 and Q8 (BRL 5,962,902.01; BRL 987,765.37).
- F08, F09: Q6's delivery-date reading (40,930 orders; 4.3% late).
- F10, F11: delivered orders with no delivery date (2 in 2017; 6 in 2018).
- F12: the gap between the two readings, 691.

Decided the same day, under the rule 14 waiver: **no cost per answer** in this piece (hard rule 10 governs how cost is published, not whether every piece gives it), and the chart caption says **"Mode not recorded for publication (rule 14 waived)"** rather than naming the mode. Both are recorded in the run file.

Approved by: Saurabh
Date: 2026-10-31
