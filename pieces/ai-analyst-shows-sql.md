---
title: "Your AI Analyst Counted Late Orders Two Ways"
seo_title: "AI Analyst Shows SQL: A Two-Chat Test for Its Definitions"
meta: "Asked twice, Dot counted 2,878 and 2,453 late orders on Olist data, each by a stated clock. A two-chat test shows if your analyst names its definition."
slug: ai-analyst-shows-sql
queries:
  - AI analyst shows SQL
  - ai data analyst
  - conversational analytics
  - text to sql accuracy
  - ai analyst data warehouse
playbook_url: https://www.getdot.ai/blog/ai-data-analyst-playbook
figures: figures/ai-analyst-shows-sql-figures.csv
dataset: Olist public dataset (orders and order items tables), CC BY-NC-SA 4.0 (facts A10, an Assumption; publication proceeds under decision L2)
query_data: "AI analyst shows SQL: not measured (not in keywords.csv). Related: conversational analytics 1.2K US, difficulty 15; ai data analyst 700 US, difficulty 22. Ahrefs, 27–28 October 2026"
reverse_links:
  - The Playbook's Stage 3 · Prove card (https://www.getdot.ai/blog/ai-data-analyst-playbook), anchor "check whether your analyst names its definition"
  - The conversational analytics software post (https://www.getdot.ai/blog/conversational-analytics-software), anchor "AI analyst shows SQL"
  - The conversational analytics post (https://www.getdot.ai/blog/conversational-analytics), anchor "ask the same question in two fresh chats"
---

**We asked [Dot](https://www.getdot.ai/), an [AI data analyst](https://www.getdot.ai/blog/conversational-analytics), "How many orders were delivered late in 2017?" in two fresh chats on the Olist dataset. One answer said 2,878 and the other 2,453. Both matched the raw data under the definition of "late" each answer stated. By the end, you'll have a two-chat test of whether your analyst states its definition.**

The same phrase, "delivered in 2017", got two readings inside one batch. Asked "How many orders were delivered in 2017?", the answer used the purchase date and returned 43,428 orders. It said: "This uses purchase date, not delivery date."

Asked "What was the total item price of orders delivered in 2017?", the answer used the delivery date and returned BRL 5,612,818. It said: "This uses delivery date, not purchase date." Each question got the same reading again in its fresh-chat repeat.

**The whole piece in eight lines:**

1. We asked Dot six questions on the Olist dataset, each in two fresh chats, 12 answers in all.
2. Each question's wording left a date or a definition open.
3. Every answer matched a figure computed from the raw CSVs, at the precision shown.
4. One question split: "delivered late in 2017" gave 2,878 at timestamp grain and 2,453 by calendar day.
5. "Delivered in 2017" meant purchase year for a count and delivery year for a revenue total.
6. In 11 of 12 answers, the text named its date basis; on the twelfth, only the SQL showed it.
7. In this run, the SQL was the check where the text was silent, and the reference where two chats disagreed.
8. Ask your key question twice, fresh, and compare the stated definition and the date filter.

## The same late-delivery question returned 2,878 and 2,453, and each answer named its definition of late

Does it matter whether an AI analyst shows its SQL? We tested that on one public dataset. The test belongs to the Prove stage of [the Playbook](https://www.getdot.ai/blog/ai-data-analyst-playbook): a team checks its analyst on questions with known answers. Run it before rollout, and before choosing among [conversational analytics tools](https://www.getdot.ai/blog/conversational-analytics-software).

We picked six questions on [Olist, a public e-commerce dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), each worded so that a date or a definition is left open. We asked each one word for word in two fresh chats, 12 answers in all. Chat A is the first ask; chat B is the fresh repeat. A script computed reference figures from the raw CSVs and compared each answer with them.

| Question as asked | Chat A | Chat B | Text named its date (A / B) | SQL's period filter | Same reading in both chats |
| --- | --- | --- | --- | --- | --- |
| How many orders were delivered in 2017? | 43,428 | 43,428 | Yes / Yes | Purchase date | Yes |
| What was the total item price of orders delivered in 2017? | BRL 5,612,818 | BRL 5,612,818 | Yes / Yes | Delivery date | Yes |
| How much did customers spend in 2017? | BRL 6,921,535 | BRL 6,921,535 | Yes / Yes | Purchase date | Yes |
| How many orders did we get in 2017? | 45,101 | 45,101 | No / Yes | Purchase date | Yes |
| How many orders were delivered late in 2017? | 2,878 | 2,453 | Yes / Yes | Purchase date | No: timestamp against calendar day |
| What percentage of delivered orders were late in 2018? | 7.7% | 7.7% | Yes / Yes | Purchase date | Yes |

Five of the six questions returned the same value in both chats. The late-delivery question split. Chat A said: "2,878 orders placed in 2017 were delivered late, meaning delivery occurred after the estimated delivery timestamp". Chat B said: "2,453 orders placed in 2017 were delivered late, meaning they arrived after the estimated delivery day".

![Bar chart. Asked 'How many orders were delivered late in 2017?' in two fresh chats, Dot returned 2,878 orders at timestamp grain and 2,453 by calendar day, on the Olist dataset.](charts/ai-analyst-shows-sql-late-orders.png)

*Dot's answers to the same question in two fresh chats, Olist dataset, 31 October 2026.*

The SQL shows where the counts part. Chat A counted an order late when its delivery timestamp passed the estimated one.

```sql
    WHERE order_delivered_customer_date IS NOT NULL
      AND order_estimated_delivery_date IS NOT NULL
      AND order_delivered_customer_date > order_estimated_delivery_date
```

Chat B compared calendar days, inside its count.

```sql
  COUNT(*) FILTER (
    WHERE CAST(order_delivered_customer_date AS DATE) > CAST(order_estimated_delivery_date AS DATE)
  ) AS late_delivered_order_count,
```

Both queries counted from the same orders. Chat B's filter is below; chat A's has the same three conditions in a different order.

```sql
WHERE order_status = 'delivered'
  AND order_purchase_timestamp >= TIMESTAMP '2017-01-01 00:00:00'
  AND order_purchase_timestamp < TIMESTAMP '2018-01-01 00:00:00'
```

So the 425 orders between the answers come from the late comparison alone. Both counts match the raw data exactly, each under the definition its answer stated.

Chat A's answer said "timestamp"; chat B's said "day". Each word matched its SQL, so the difference shows in the answer text alone. The wording isn't always that exact: the 2018 answers said "estimated delivery date" and compared calendar days.

Decide which grain "late" means for your team before anyone asks.

## "Delivered in 2017" meant purchase year for a count and delivery year for a revenue total

"Delivered in 2017" has two honest readings. It can mean bought in 2017 and since delivered. It can also mean delivered to the customer in 2017.

Asked "How many orders were delivered in 2017?", both chats returned 43,428 and filtered on `order_purchase_timestamp`. Chat A said: "This uses purchase date, not delivery date." Chat B said: "This uses purchase dates, not delivery dates."

Asked "What was the total item price of orders delivered in 2017?", both chats returned BRL 5,612,818. Both filtered on `order_delivered_customer_date`. Chat A said: "This uses delivery date, not purchase date." Chat B said: "This uses the actual delivery date, not the purchase date."

The readings the answers didn't use give different numbers. By delivery date, 40,930 orders reached customers in 2017. By purchase year, the item price of delivered orders was BRL 5,962,902.01.

Each question got the same reading in both its chats. The reading changed between questions: the count used purchase year, and the revenue total used delivery year. All four answers said which date they used, and each SQL filtered on that column.

An AI analyst that names its date in the answer lets a reader catch a flipped reading without opening the SQL.

## The SQL earns its place on the one answer whose text left the date out

For each answer, a script checked two things. Did the text name its date basis? Did the SQL's period filter name a date column? The text counted if it named a purchase or delivery date, or said orders were "placed in" or delivered "in calendar year".

The text named its date basis in 11 of 12 answers. The spend answers said "on orders placed in 2017"; the 2018 answers said "placed in 2018". All 12 came back with their SQL, and in all 12 the period filter named a date column.

The exception was "How many orders did we get in 2017?" Chat A answered: "We received 45,101 orders in 2017, including all order statuses". Nothing in that sentence says which date put an order in 2017. Its SQL does.

```sql
WHERE order_purchase_timestamp >= '2017-01-01'
  AND order_purchase_timestamp < '2018-01-01'
```

Chat B, the fresh repeat, returned 45,101 again and added "based on purchase date". On chat A's answer, a reader who skipped the SQL could not tell which date was used. Because the SQL came back with every answer, the date basis was still there to read.

In this run, showing the SQL mattered in two places: where the answer text went quiet, and where two chats disagreed.

## Things to keep in mind

- **One dataset, one batch, two fresh chats per question.** This shows what can happen, not how often it happens.
- **This piece reports which reading each answer stated, not why it took it.** The run's settings were recorded by hand, without screenshots, so they aren't used here as evidence.
- **The 2018 late share matched at one decimal place.** Both answers left out six orders missing a delivery or estimated date. The reference figure kept them in its denominator, and both versions round to 7.7%.
- **Whether a team reads the SQL was not measured.** This run counted what the answers and their SQL said.

## Where Dot fits

In this run, every Dot answer came back with its SQL, 12 of 12, and the text named its date basis in 11. Where the text didn't, the SQL's period filter did. Dot's documentation is at [docs.getdot.ai](https://docs.getdot.ai).

---

Ask your AI analyst "How many orders were delivered late last year?" in two fresh chats today. If the numbers differ, read each answer's definition sentence, then the date filter in its SQL.

*If this excites you, we'd love to hear from you. Get in touch.*
