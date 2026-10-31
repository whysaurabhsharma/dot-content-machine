# Does your AI analyst remember what you asked? We tested Dot: one phrase, two readings

**Does your AI analyst remember what you asked? We asked [Dot](https://www.getdot.ai/) eight questions on Olist data, and one phrase, "delivered in 2017", gave late-order counts 691 apart. The follow-up chain read it as purchase date and a fresh chat as delivery date, and both matched the raw data. By the end, you'll have a five-step test.**

Dot also kept the thread: asked four turns later to go back to the first question, it returned the same 43,428 orders. In this run, the readings differed between the chain and the fresh chats. Each answer's SQL showed which date it used.

**The whole piece in eight lines:**

1. "Does it keep context?" has two halves: does it remember, and does it read your words the same way.
2. We asked Dot eight questions across three chats: a five-question chain, a fresh-chat control and an item-price chat.
3. Asked to go "back to my first question", Dot re-ran the first query and returned 43,428 again.
4. Dot kept scope in the item-price chat: "How much of that came in November?" kept the delivery-date filter.
5. Dot read "delivered in 2017" as purchase year inside the chain and as delivery date in a fresh chat.
6. Those two readings gave 2,453 late orders in the chain and 1,762 in a fresh chat, 691 apart.
7. Dot's answer text didn't always name the date; the date filter in each answer's SQL always did.
8. Test a chain, re-ask one of its questions cold, and compare the date column in both answers' SQL.

## Dot kept context through a five-question follow-up chain

We ran this as part of the Prove stage of [the Playbook](https://www.getdot.ai/blog/ai-data-analyst-playbook), where a team tests the analyst on known questions before launch. Buyers of [conversational analytics](https://www.getdot.ai/blog/conversational-analytics) ask whether an analyst keeps context across follow-up questions.

The method was one chat and five questions. Each question leaned on the one before: "those", "that share", "for 2018", "my first question". Then we opened a fresh chat and asked the chain's second question again, written in full. A third chat asked about item price, with one follow-up.

Before the first question, we computed the expected answers from the raw Olist CSVs. "Delivered in 2017" was ambiguous on purpose, so we computed both readings: purchased in 2017, and delivered in 2017.

After the run, a script checked each answer against them, reading only the basis the answer stated. Q6 and Q8 didn't name a date in their text. So a person read each one's reading from its SQL, which filters on the delivery date.

| # | Chat | Question as asked | Dot's figure | Date in the SQL's date filter | Answer text named that date | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| Q1 | A, chain | How many orders were delivered in 2017? | 43,428 | Purchase date | Yes | Correct, exact |
| Q2 | A, chain | And how many of those were delivered late? | 2,453 | Purchase date | No | Correct, exact |
| Q3 | A, chain | What share of the delivered orders is that? | 5.6% | Purchase date | Yes | Correct, display rounding |
| Q4 | A, chain | What is that share for 2018? | 7.7% | Purchase date | Yes | Correct, display rounding |
| Q5 | A, chain | Going back to my first question, how many orders was that? | 43,428 | Purchase date | Yes | Correct, exact |
| Q6 | B, fresh | How many orders delivered in 2017 were delivered later than their estimated delivery date? | 1,762 | Delivery date | No | Correct, reading taken from the SQL by a person |
| Q7 | C, fresh | What was the total item price of orders delivered in 2017? | BRL 5,612,818 | Delivery date | Yes | Correct under its stated definition |
| Q8 | C, follow-up | How much of that came in November? | BRL 651,458 | Delivery date | No | Correct, reading taken from the SQL by a person |

Every figure Dot gave matched the raw data under the reading its own SQL used. The five chain answers matched the purchase-year reading. The item-price answer matched the definition it stated. The fresh late count and the November follow-up matched the delivery-date reading their SQL used.

Dot returned 43,428 at the first question and 43,428 again four turns later, when asked to go back to it. Its SQL for the later answer repeated the first query's purchase-year filter. Dot re-ran the query rather than repeating a stored figure, and it resolved "my first question" correctly.

Dot's 5.6% and 7.7% were display rounding, not gaps. Dot excluded the orders with no delivery date, two in 2017 and six in 2018; the ground truth kept them. Both ways, each share rounds to the same one-decimal figure. Dot said so: "excluding the two orders with missing delivery dates" for 2017, "excluding six orders with missing delivery dates" for 2018.

Dot kept scope in the item-price chat too. Asked "How much of that came in November?", it returned BRL 651,458, and its SQL filtered on the delivery date, as the question before had. The purchase-month reading would have been BRL 987,765.

The chain fixed its reading of "delivered in 2017" at the first answer, and every follow-up inherited it. Dot made the choice visible at turn one, in its first answer: "This uses purchase date, not delivery date."

## The same words got a different date in a fresh chat

The control was simple: the chain's second question again, written in full, in a chat with no history. We asked: "How many orders delivered in 2017 were delivered later than their estimated delivery date?"

Inside the chain, Dot counted 2,453 late orders among those purchased in 2017. In the fresh chat, Dot counted 1,762 late orders among those delivered in 2017. Two readings of one phrase, "delivered in 2017", put 691 orders between Dot's answers.

Neither answer is wrong. "Delivered in 2017" can mean orders bought in 2017 that were later delivered. It can also mean orders that reached the customer in 2017.

Dot's fresh-chat reading covered 40,930 orders delivered in 2017, of which 4.3% arrived late. That is a different set of orders from the chain's, whose 5.6% was a share of orders purchased in 2017. The item-price chat also read the phrase by delivery date: BRL 5,612,818, against BRL 5,962,902 by purchase year.

![Bar chart of two Dot answers to how many orders delivered in 2017 were late, on the Olist dataset. Inside a follow-up chain, Dot used purchase date and returned 2,453. In a fresh chat, it used delivery date and returned 1,762.](charts/ai-analyst-follow-up-questions-late-orders.png)

*Late orders for "delivered in 2017", asked inside a follow-up chain and in a fresh chat. Olist dataset, Dot, 31 October 2026. The run's mode is not stated.*

Each answer in this run came back with its SQL, and the SQL shows which date each one used. In the chain, Dot's date filter sat on `order_purchase_timestamp`, the purchase date. In both fresh chats, it sat on `order_delivered_customer_date`, the delivery date.

## Basis statements were inconsistent, so read the SQL as well as the sentence

Some of Dot's answers named the date they used. The first chain answer did, as quoted above. The item-price answer did too: "This uses the customer delivery date, not the purchase date."

The fresh-chat late count did not. Its answer began: "1,762 orders delivered in 2017 arrived after their estimated delivery date". That reuses the question's phrase "delivered in 2017", which is the ambiguous part. The sentence alone doesn't say which date; the SQL's filter on the delivery date does.

An AI analyst's answer can be right and still not say which question it answered.

## A follow-up test you can copy takes five questions and one fresh chat

1. Pick a phrase your team reads two ways, such as "delivered in", "active customer" or "revenue".
2. Compute the expected answer under each reading, from the raw tables, before you ask anything.
3. In one chat, ask five questions, each leaning on the last with "those", "that" or "go back to".
4. In a fresh chat, ask one of the chain's questions again, written in full.
5. Compare the filter in both answers' SQL, then mark each answer against the reading it used.

Score item by item. A matching total with a different filter is a different answer.

## Things to keep in mind

- **One run, one dataset, eight questions.** One run can't say whether chat history or run-to-run variation produced the different readings. Assumption: the same question can take a different path on another day, so a re-run can differ.
- **"Delivered in 2017" was ambiguous on purpose.** The fresh late count and the November follow-up were marked correct under the delivery-date reading, which a person took from their SQL. Neither is an error.
- **This run's settings were noted by hand, without screenshots.** So this piece doesn't publish the run's mode or [cost](https://www.getdot.ai/pricing).

## Where Dot fits

Every answer in this test came with its SQL, so the date filter was visible even when the text skipped it. Dot's [context notes](https://www.getdot.ai/context-agent) are where a team can define what "delivered in" means. Dot's evaluation questions hold an expected answer and a percent tolerance, for step 2's answers; details are in [the docs](https://docs.getdot.ai).

---

Run the five steps this week, on one phrase your team argues about. Before you trust either number, compare the filter in both answers' SQL.

*If this excites you, we'd love to hear from you. Get in touch.*
