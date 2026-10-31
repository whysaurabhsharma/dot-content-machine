# ai-analyst-follow-up-questions run

## Batch 1: conditions

Observed in Dot's UI by a person at about 12:15 IST on 31 October 2026, before the first question, and recorded here as text. **No screenshots were saved**: the four were reported taken, but none reached runs/screenshots/, and the conditions were accepted as hand-recorded text instead.

**Rule 14 waived for this piece** by Saurabh, 31 October 2026 (run with `stage_gate.py --no-screenshots`). The mode, environment, context notes and credits are a person's observation, not screenshotted evidence. **Therefore no claim about mode, credits, environment or context notes may appear in the published piece**: not the mode the answers ran in, not their cost, not which notes were on. Only claims resting on Dot's answers and their SQL, as recorded below, are supported.

**Credits baseline.** The reading moved from 79.4 (the rehearsal's closing figure) to 87.6 because of unrelated chats between the rehearsal and this piece. This batch's cost is measured from 87.6, not from 79.4.

- Date: 2026-10-31, about 12:15 IST (conditions); each entry's time is from `date`
- Workspace: aiinterviewagents.com
- Tables: uploads.main.olist_orders_dataset; uploads.main.olist_order_items_dataset
- Data sources on: olist_order_items_dataset, olist_orders_dataset
- Mode: Balanced. Recorded by hand; no screenshot (rule 14 waived)
- Environment: Production. Recorded by hand; no screenshot (rule 14 waived)
- Context notes: on: "Olist dataset currency and monetary formatting", "Olist revenue, order value, basket size, cancellation and shipping metrics". Off: "About aiinterviewagents.com". Recorded by hand; no screenshot (rule 14 waived)
- Credits before: 87.6 of 300 used. Recorded by hand; no screenshot (rule 14 waived)
- Credits after: not yet recorded. The human reads it in Dot's UI after the batch; no screenshot (rule 14 waived)
- Model: not observable via MCP

### Q1: How many orders were delivered in 2017?

- Time: 2026-10-31T13:37:59+0530
- Chat: https://app.getdot.ai/?c=a6360504-44c8-47dd-80f1-8e55bbbeba9e
- Classification: answered
- Basis, population: yes - "have a recorded status of delivered"
- Basis, period: yes - "orders purchased in 2017"
- Basis, definition: yes - "This uses purchase date, not delivery date."

**Answer**

```text
43,428 orders purchased in 2017 have a recorded status of delivered . This uses purchase date, not delivery date.
```

**Data**

```text
delivered_orders, total_placed_orders, delivered_orders_PERCENT
43428, 45101, 96.3
```

**SQL**

```sql
SELECT
  COUNT(*) FILTER (WHERE order_status = 'delivered') AS delivered_orders,
  COUNT(*) AS total_placed_orders,
  ROUND(COUNT(*) FILTER (WHERE order_status = 'delivered') * 100.0 / NULLIF(COUNT(*), 0), 1) AS delivered_orders_PERCENT
FROM uploads.main.olist_orders_dataset
WHERE order_purchase_timestamp >= TIMESTAMP '2017-01-01 00:00:00'
  AND order_purchase_timestamp < TIMESTAMP '2018-01-01 00:00:00'
```

### Q2: And how many of those were delivered late?

- Time: 2026-10-31T13:38:29+0530
- Chat: https://app.getdot.ai/?c=a6360504-44c8-47dd-80f1-8e55bbbeba9e
- Follow-up of: Q1
- Classification: answered
- Basis, population: no
- Basis, period: no
- Basis, definition: yes - "meaning delivery occurred after the estimated delivery day"

**Answer**

```text
2,453 orders were delivered late (5.6%) , meaning delivery occurred after the estimated delivery day. Two orders lack delivery dates and could not be assessed .
```

**Data**

```text
delivered_order_count, late_order_count, late_rate_PERCENT, missing_timestamps_count
43428, 2453, 5.6, 2
```

**SQL**

```sql
SELECT
  COUNT(*) AS delivered_order_count,
  COUNT(*) FILTER (
    WHERE order_delivered_customer_date IS NOT NULL
      AND order_estimated_delivery_date IS NOT NULL
      AND CAST(order_delivered_customer_date AS DATE) > CAST(order_estimated_delivery_date AS DATE)
  ) AS late_order_count,
  ROUND(
    COUNT(*) FILTER (
      WHERE order_delivered_customer_date IS NOT NULL
        AND order_estimated_delivery_date IS NOT NULL
        AND CAST(order_delivered_customer_date AS DATE) > CAST(order_estimated_delivery_date AS DATE)
    ) * 100.0 / NULLIF(
      COUNT(*) FILTER (
        WHERE order_delivered_customer_date IS NOT NULL
          AND order_estimated_delivery_date IS NOT NULL
      ),
      0
    ),
    1
  ) AS late_rate_PERCENT,
  COUNT(*) FILTER (
    WHERE order_delivered_customer_date IS NULL
       OR order_estimated_delivery_date IS NULL
  ) AS missing_timestamps_count
FROM uploads.main.olist_orders_dataset
WHERE order_status = 'delivered'
  AND order_purchase_timestamp >= TIMESTAMP '2017-01-01 00:00:00'
  AND order_purchase_timestamp < TIMESTAMP '2018-01-01 00:00:00'
```

### Q3: What share of the delivered orders is that?

- Time: 2026-10-31T13:38:54+0530
- Chat: https://app.getdot.ai/?c=a6360504-44c8-47dd-80f1-8e55bbbeba9e
- Follow-up of: Q2
- Classification: answered
- Basis, population: yes - "delivered orders purchased in 2017"
- Basis, period: yes - "purchased in 2017"
- Basis, definition: yes - "excluding the two orders with missing delivery dates"

**Answer**

```text
5.6% of delivered orders purchased in 2017 were late, excluding the two orders with missing delivery dates .
```

**Data**

```text
delivered_order_count, late_order_count, late_rate_PERCENT, missing_timestamps_count
43428, 2453, 5.6, 2
```

**SQL**

```sql
SELECT
  COUNT(*) AS delivered_order_count,
  COUNT(*) FILTER (
    WHERE order_delivered_customer_date IS NOT NULL
      AND order_estimated_delivery_date IS NOT NULL
      AND CAST(order_delivered_customer_date AS DATE) > CAST(order_estimated_delivery_date AS DATE)
  ) AS late_order_count,
  ROUND(
    COUNT(*) FILTER (
      WHERE order_delivered_customer_date IS NOT NULL
        AND order_estimated_delivery_date IS NOT NULL
        AND CAST(order_delivered_customer_date AS DATE) > CAST(order_estimated_delivery_date AS DATE)
    ) * 100.0 / NULLIF(
      COUNT(*) FILTER (
        WHERE order_delivered_customer_date IS NOT NULL
          AND order_estimated_delivery_date IS NOT NULL
      ),
      0
    ),
    1
  ) AS late_rate_PERCENT,
  COUNT(*) FILTER (
    WHERE order_delivered_customer_date IS NULL
       OR order_estimated_delivery_date IS NULL
  ) AS missing_timestamps_count
FROM uploads.main.olist_orders_dataset
WHERE order_status = 'delivered'
  AND order_purchase_timestamp >= TIMESTAMP '2017-01-01 00:00:00'
  AND order_purchase_timestamp < TIMESTAMP '2018-01-01 00:00:00'
```

### Q4: What is that share for 2018?

- Time: 2026-10-31T13:39:31+0530
- Chat: https://app.getdot.ai/?c=a6360504-44c8-47dd-80f1-8e55bbbeba9e
- Follow-up of: Q3
- Classification: answered
- Basis, population: yes - "delivered orders purchased in 2018"
- Basis, period: yes - "purchased in 2018"
- Basis, definition: yes - "excluding six orders with missing delivery dates"

**Answer**

```text
7.7% of delivered orders purchased in 2018 were late, excluding six orders with missing delivery dates .
```

**Data**

```text
delivered_order_count, late_order_count, late_rate_PERCENT, missing_timestamps_count
52783, 4078, 7.7, 6
```

**SQL**

```sql
SELECT
  COUNT(*) AS delivered_order_count,
  COUNT(*) FILTER (
    WHERE order_delivered_customer_date IS NOT NULL
      AND order_estimated_delivery_date IS NOT NULL
      AND CAST(order_delivered_customer_date AS DATE) > CAST(order_estimated_delivery_date AS DATE)
  ) AS late_order_count,
  ROUND(
    COUNT(*) FILTER (
      WHERE order_delivered_customer_date IS NOT NULL
        AND order_estimated_delivery_date IS NOT NULL
        AND CAST(order_delivered_customer_date AS DATE) > CAST(order_estimated_delivery_date AS DATE)
    ) * 100.0 / NULLIF(
      COUNT(*) FILTER (
        WHERE order_delivered_customer_date IS NOT NULL
          AND order_estimated_delivery_date IS NOT NULL
      ),
      0
    ),
    1
  ) AS late_rate_PERCENT,
  COUNT(*) FILTER (
    WHERE order_delivered_customer_date IS NULL
       OR order_estimated_delivery_date IS NULL
  ) AS missing_timestamps_count
FROM uploads.main.olist_orders_dataset
WHERE order_status = 'delivered'
  AND order_purchase_timestamp >= TIMESTAMP '2018-01-01 00:00:00'
  AND order_purchase_timestamp < TIMESTAMP '2019-01-01 00:00:00'
```

### Q5: Going back to my first question, how many orders was that?

- Time: 2026-10-31T13:40:06+0530
- Chat: https://app.getdot.ai/?c=a6360504-44c8-47dd-80f1-8e55bbbeba9e
- Follow-up of: Q4
- Classification: answered
- Basis, population: yes - "had a recorded status of delivered"
- Basis, period: yes - "orders purchased in 2017"
- Basis, definition: no

**Answer**

```text
43,428 orders purchased in 2017 had a recorded status of delivered .
```

**Data**

```text
delivered_orders, total_placed_orders, delivered_orders_PERCENT
43428, 45101, 96.3
```

**SQL**

```sql
SELECT
  COUNT(*) FILTER (WHERE order_status = 'delivered') AS delivered_orders,
  COUNT(*) AS total_placed_orders,
  ROUND(COUNT(*) FILTER (WHERE order_status = 'delivered') * 100.0 / NULLIF(COUNT(*), 0), 1) AS delivered_orders_PERCENT
FROM uploads.main.olist_orders_dataset
WHERE order_purchase_timestamp >= TIMESTAMP '2017-01-01 00:00:00'
  AND order_purchase_timestamp < TIMESTAMP '2018-01-01 00:00:00'
```

### Q6: How many orders delivered in 2017 were delivered later than their estimated delivery date?

- Time: 2026-10-31T13:40:52+0530
- Chat: https://app.getdot.ai/?c=eb241702-5983-4d9e-875b-3af3a8fe567f
- Classification: answered
- Basis, population: yes - "orders delivered in 2017"
- Basis, period: yes - "delivered in 2017"
- Basis, definition: yes - "Deliveries on the estimated date are not counted as late."

**Answer**

```text
1,762 orders delivered in 2017 arrived after their estimated delivery date . Deliveries on the estimated date are not counted as late.
```

**Data**

```text
late_delivered_orders, total_delivered_orders, late_delivery_rate_PERCENT
1762, 40930, 4.3
```

**SQL**

```sql
SELECT
  COUNT(*) FILTER (
    WHERE CAST(order_delivered_customer_date AS DATE) > CAST(order_estimated_delivery_date AS DATE)
  ) AS late_delivered_orders,
  COUNT(*) AS total_delivered_orders,
  ROUND(
    COUNT(*) FILTER (
      WHERE CAST(order_delivered_customer_date AS DATE) > CAST(order_estimated_delivery_date AS DATE)
    ) * 100.0 / NULLIF(COUNT(*), 0),
    1
  ) AS late_delivery_rate_PERCENT
FROM uploads.main.olist_orders_dataset
WHERE order_status = 'delivered'
  AND order_delivered_customer_date >= TIMESTAMP '2017-01-01 00:00:00'
  AND order_delivered_customer_date < TIMESTAMP '2018-01-01 00:00:00'
```

### Q7: What was the total item price of orders delivered in 2017?

- Time: 2026-10-31T13:41:48+0530
- Chat: https://app.getdot.ai/?c=b84f3b12-eeea-4b68-9c66-ad66a771d590
- Classification: answered
- Basis, population: yes - "for orders delivered in calendar 2017"
- Basis, period: yes - "calendar 2017"
- Basis, definition: yes - "excluding freight . This uses the customer delivery date, not the purchase date."

**Answer**

```text
The total item price was BRL 5,612,818 for orders delivered in calendar 2017, excluding freight . This uses the customer delivery date, not the purchase date.
```

**Data**

```text
total_item_price_BRL, delivered_orders_missing_items_count, null_price_item_rows_count
5612817.85, 0, 0
```

**SQL**

```sql
WITH cte_delivered_orders_2017 AS (
    
    SELECT
        order_id
    FROM uploads.main.olist_orders_dataset
    WHERE order_status = 'delivered'
      AND order_delivered_customer_date >= TIMESTAMP '2017-01-01 00:00:00'
      AND order_delivered_customer_date < TIMESTAMP '2018-01-01 00:00:00'
),
cte_items_by_order AS (
    
    SELECT
        order_id,
        SUM(price) AS merchandise_brl,
        COUNT(CASE WHEN price IS NULL THEN 1 END) AS null_price_item_count
    FROM uploads.main.olist_order_items_dataset
    GROUP BY order_id
)
SELECT
    ROUND(COALESCE(SUM(i.merchandise_brl), 0.0), 2) AS total_item_price_BRL,
    COUNT(CASE WHEN i.order_id IS NULL THEN 1 END) AS delivered_orders_missing_items_count,
    COALESCE(SUM(i.null_price_item_count), 0) AS null_price_item_rows_count
FROM cte_delivered_orders_2017 o
LEFT JOIN cte_items_by_order i
    ON o.order_id = i.order_id
```

### Q8: How much of that came in November?

- Time: 2026-10-31T13:42:47+0530
- Chat: https://app.getdot.ai/?c=b84f3b12-eeea-4b68-9c66-ad66a771d590
- Follow-up of: Q7
- Classification: answered
- Basis, population: yes - "from orders delivered in November 2017"
- Basis, period: yes - "November 2017"
- Basis, definition: yes - "excluding freight"

**Answer**

```text
BRL 651,458 came from orders delivered in November 2017, excluding freight .
```

**Data**

```text
total_item_price_BRL, delivered_orders_missing_items_count, null_price_item_rows_count
651457.52, 0, 0
```

**SQL**

```sql
WITH cte_delivered_orders_nov_2017 AS (
    
    SELECT
        order_id
    FROM uploads.main.olist_orders_dataset
    WHERE order_status = 'delivered'
      AND order_delivered_customer_date >= TIMESTAMP '2017-11-01 00:00:00'
      AND order_delivered_customer_date < TIMESTAMP '2017-12-01 00:00:00'
),
cte_items_by_order AS (
    
    SELECT
        order_id,
        SUM(price) AS merchandise_brl,
        COUNT(CASE WHEN price IS NULL THEN 1 END) AS null_price_item_count
    FROM uploads.main.olist_order_items_dataset
    GROUP BY order_id
)
SELECT
    ROUND(COALESCE(SUM(i.merchandise_brl), 0.0), 2) AS total_item_price_BRL,
    COUNT(CASE WHEN i.order_id IS NULL THEN 1 END) AS delivered_orders_missing_items_count,
    COALESCE(SUM(i.null_price_item_count), 0) AS null_price_item_rows_count
FROM cte_delivered_orders_nov_2017 o
LEFT JOIN cte_items_by_order i
    ON o.order_id = i.order_id
```
