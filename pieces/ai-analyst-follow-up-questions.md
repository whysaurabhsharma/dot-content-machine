---
title: "“Delivered in 2017” has two right answers. Test which one your AI analyst gives you"
title_approved_by: Saurabh, 2026-10-31 (third title, after two failed headline tests)
seo_title: "AI Analyst Follow-Up Questions: Check Which Date It Used"
meta: "“Delivered in 2017” gave Dot two correct late-order counts on Olist data. A six-step test shows which date your analyst used, and where its SQL says so."
slug: ai-analyst-follow-up-questions-test
queries:
  - AI analyst follow-up questions context
  - conversational analytics
  - ai data analyst
playbook_url: https://www.getdot.ai/blog/ai-data-analyst-playbook
figures: figures/ai-analyst-follow-up-questions-figures.csv
dataset: Olist public dataset (orders and order items tables), CC BY-NC-SA 4.0 (facts A10, an Assumption)
query_data: "AI analyst follow-up questions context: not measured (not in keywords.csv). Related: conversational analytics 1.2K US, difficulty 15; ai data analyst 700 US, difficulty 22. Ahrefs, 27–28 October 2026"
reverse_links:
  - The Playbook's Stage 3 · Prove card (https://www.getdot.ai/blog/ai-data-analyst-playbook), anchor "test follow-up questions"
  - The conversational analytics post (https://www.getdot.ai/blog/conversational-analytics), anchor "a context test you can copy"
  - The conversational analytics software post (https://www.getdot.ai/blog/conversational-analytics-software), anchor "AI analyst follow-up questions"
---

**Asked how many orders "delivered in 2017" were late, [Dot](https://www.getdot.ai/) gave 2,453 in a follow-up chain and 1,762 in a fresh chat. Both are correct: each matches the raw data for its date. The chain named purchase date; the fresh chat silently used delivery date. By the end, you'll have a six-step test that shows which date your analyst used.**

We ran this test on [Olist, a public e-commerce dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), so anyone can recompute it. Late means delivered on a later calendar day than the estimated delivery date. Dot's chain answer to "And how many of those were delivered late?" defined it the same way: "meaning delivery occurred after the estimated delivery day."

**The whole piece in seven lines:**

1. "Delivered in 2017" has two valid readings: bought in 2017, or delivered to the customer in 2017.
2. Dot counted 2,453 late orders by purchase date in a follow-up chain, and 1,762 by delivery date in a fresh chat.
3. Both counts match the raw Olist data for the date each used; they sit 691 orders apart.
4. Dot's first chain answer named purchase date, while the fresh-chat count never named its date.
5. Every Dot answer came back with its SQL, and the SQL's date filter showed the date even where the text was silent.
6. Asked four turns later to go back to the first question, Dot returned 43,428 again, with the same SQL as its first answer.
7. The test: run a chain, re-ask one question cold, check whether each answer names its date, and read its SQL if not.

## Both late-order counts were correct, each for a different date

We ran this as part of the Prove stage of [the Playbook](https://www.getdot.ai/blog/ai-data-analyst-playbook), where a team tests the analyst on known questions before launch. Buyers of [conversational analytics](https://www.getdot.ai/blog/conversational-analytics) ask whether an analyst keeps context across follow-up questions.

The method was three chats. Chat A was a chain of five questions, each leaning on the one before. Chat B asked the chain's second question again, written in full, with no history. Chat C asked about item price, with one follow-up.

Before the first question, we computed the expected answers from the raw Olist CSVs. "Delivered in 2017" was ambiguous on purpose, so we computed both readings: purchased in 2017, and delivered in 2017. After the run, a script checked each answer against the basis it stated. Q6 and Q8 stated no date, so a person read each one's date from its SQL.

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

Inside the chain, Dot counted 2,453 late orders among those purchased in 2017. That matches the raw data by purchase date exactly. In the fresh chat, Dot counted 1,762 late orders among those delivered in 2017. That matches the raw data by delivery date exactly.

Neither answer is wrong. "Delivered in 2017" can mean orders bought in 2017 that were later delivered. It can also mean orders that reached the customer in 2017. The two readings put 691 orders between Dot's answers.

![Bar chart of two Dot answers to how many orders delivered in 2017 were late, on the Olist dataset. Inside a follow-up chain, Dot used purchase date and returned 2,453. In a fresh chat, it used delivery date and returned 1,762.](charts/ai-analyst-follow-up-questions-late-orders.png)

*Late orders for "delivered in 2017", asked inside a follow-up chain and in a fresh chat. Olist dataset, Dot, 31 October 2026. The run's mode is not stated.*

Each answer's SQL shows its date filter. Here is Q2's, word for word. Asked about "those", it kept Q1's filter on the purchase date.

```sql
WHERE order_status = 'delivered'
  AND order_purchase_timestamp >= TIMESTAMP '2017-01-01 00:00:00'
  AND order_purchase_timestamp < TIMESTAMP '2018-01-01 00:00:00'
```

And here is Q6's, from the fresh chat, filtering on the delivery date.

```sql
WHERE order_status = 'delivered'
  AND order_delivered_customer_date >= TIMESTAMP '2017-01-01 00:00:00'
  AND order_delivered_customer_date < TIMESTAMP '2018-01-01 00:00:00'
```

The fresh reading covered 40,930 orders delivered in 2017, of which 4.3% arrived late. The chain's 5.6% was a share of a different set: 43,428 orders purchased in 2017 and delivered. The item-price chat read the phrase by delivery date too: BRL 5,612,818, against BRL 5,962,902 by purchase year.

Dot's 5.6% for 2017 and 7.7% for 2018, Q3 and Q4 in the table above, were display rounding, not gaps. Dot's answers left out orders with no delivery date. Q3 said "excluding the two orders with missing delivery dates", and Q4 said "excluding six orders with missing delivery dates". The ground truth kept them; with or without them in the denominator, the chain's shares round to 5.6% and 7.7%.

## The chain named its date; the fresh chat didn't

The risk isn't a wrong number. It is a right number for a date you didn't mean, with nothing in the text to say so.

Dot made the chain's choice visible at turn one. Asked "How many orders were delivered in 2017?", it answered: "This uses purchase date, not delivery date." The item-price chat was just as clear. Asked "What was the total item price of orders delivered in 2017?", Dot answered: "This uses the customer delivery date, not the purchase date."

The fresh-chat late count did not name its date. That was Q6, the chain's second question asked again in full. Dot's answer began: "1,762 orders delivered in 2017 arrived after their estimated delivery date". That reuses the ambiguous phrase, so the sentence alone doesn't say which date.

Where the text was silent, the SQL wasn't. Every answer in this run, 8 of 8, came back with its SQL, and its date filter named the column. Most answers also named their date unprompted: 5 of 8, Q1, Q3, Q4, Q5 and Q7.

An AI analyst's answer can be right and still not say which question it answered.

## Dot returned the first answer's figure and SQL four turns later

Asked four turns later to go back to the first question, Dot returned 43,428 again. Its SQL was the same as its first answer's, purchase-date filter included.

Scope held in the item-price chat too. Asked "How much of that came in November?", Dot returned BRL 651,458, with its SQL still filtering on the delivery date. The purchase-month reading would have been BRL 987,765.

## A follow-up test you can copy takes six steps and one fresh chat

1. Pick a phrase your team reads two ways, such as "delivered in", "active customer" or "revenue".
2. Compute the expected answer under each reading, from the raw tables, before you ask anything.
3. In one chat, ask five questions, each leaning on the last with "those", "that" or "go back to".
4. In a fresh chat, ask one of the chain's questions again, written in full.
5. Check whether the answer names its date. If it doesn't, read the date filter in its SQL.
6. Mark each answer against the reading it used, item by item.

Our run used two fresh chats; the test needs only one.

When you run this, a total that matches under a different date filter is still a different answer.

## Things to keep in mind

- **One run, one dataset, eight questions.** One run can't say why the fresh chat read the phrase differently: chat history, a default, or run-to-run variation. Assumption: the same question can take a different path on another day, so a re-run can differ.
- **"Delivered in 2017" was ambiguous on purpose.** The fresh late count and the November follow-up were marked correct under the delivery-date reading, which a person took from their SQL. Neither is an error.
- **This run's settings were noted by hand, without screenshots.** So this piece doesn't publish the run's mode or [cost](https://www.getdot.ai/pricing).

## Where Dot fits

In this test, Dot's text didn't always name its date, but its SQL always did: every answer came back with its query. Five of eight answers also named their date in plain words, and step 5 of the test reads the SQL for the rest. Dot's documentation is at [the docs](https://docs.getdot.ai).

---

Run the six steps this week, on one phrase your team argues about. Before you trust either number, check which date each answer used.

*If this excites you, we'd love to hear from you. Get in touch.*
