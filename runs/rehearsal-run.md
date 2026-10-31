# rehearsal run

## Batch 1: conditions

Three of the five screenshots were taken: credits-before, notes and mode. Environment and credits-after were recorded by hand. This is a rehearsal and nothing will be published from it, so a partial set was allowed (runs/README.md#screenshots). Observed in Dot's UI at about 04:50 IST on 31 October 2026, before the first question; the three screenshots were saved at 05:02–05:04.

- Date: 2026-10-31, about 04:50 IST (conditions); each entry's time is from `date`
- Workspace: aiinterviewagents.com
- Tables: uploads.main.olist_orders_dataset; uploads.main.olist_order_items_dataset
- Data sources on: olist_order_items_dataset, olist_orders_dataset
- Mode: Balanced. Screenshot: runs/screenshots/rehearsal-batch-1-mode.png (the chat composer's mode selector, shown in the smoke-test chat)
- Environment: Production. Recorded by hand; no environment screenshot. "Production" is also visible in the sidebar of all three screenshots
- Context notes: on: "Olist dataset currency and monetary formatting", "Olist revenue, order value, basket size, cancellation and shipping metrics". Off: "About aiinterviewagents.com". Screenshot: runs/screenshots/rehearsal-batch-1-notes.png (Model → Notes, which also shows both data sources on)
- Credits before: 73.9 of 300 used. Screenshot: runs/screenshots/rehearsal-batch-1-credits-before.png (Settings → Billing)
- Credits after: 76.6 of 300 used. Recorded by hand after Q11; no credits-after screenshot. Batch 1 used 2.7 credits (76.6 − 73.9), all in Balanced mode
- Model: not observable via MCP

### Q1: Finance here: what was our total revenue?

- Time: 2026-10-31T05:07:33+0530
- Chat: https://app.getdot.ai/?c=ebf474c1-ddbd-4039-a554-5ef0b3c38594
- Classification: answered
- Basis, population: yes - "This is delivered merchandise sales, excluding shipping and non-delivered orders"
- Basis, period: yes - "across the full uploaded dataset, covering purchases from September 2016 to October 2018"
- Basis, definition: yes - "delivered merchandise sales, excluding shipping and non-delivered orders—not Olist’s corporate accounting revenue"

**Answer**

```text
Total revenue was BRL 13,221,498 across the full uploaded dataset, covering purchases from September 2016 to October 2018 .

This is delivered merchandise sales, excluding shipping and non-delivered orders—not Olist’s corporate accounting revenue. Refund adjustments are unavailable.
```

**Data**

```text
revenue_brl, delivered_order_count, min_purchase_timestamp, max_purchase_timestamp, count_delivered_orders_lacking_items, count_delivered_items_with_null_price
13221498.11, 96478, 2016-09-04 21:15:19, 2018-10-17 17:30:18, 0, 0
```

**SQL**

```sql
WITH cohort AS (
  SELECT
    order_id,
    order_status,
    order_purchase_timestamp
  FROM uploads.main.olist_orders_dataset
),
items_by_order AS (
  SELECT
    order_id,
    SUM(price) AS merchandise_brl,
    COUNT(*) AS item_units,
    COUNT(*) FILTER (WHERE price IS NULL) AS null_price_items_count
  FROM uploads.main.olist_order_items_dataset
  GROUP BY order_id
),
delivered_orders AS (
  SELECT
    c.order_id,
    c.order_purchase_timestamp,
    i.merchandise_brl,
    i.item_units,
    i.null_price_items_count,
    CASE WHEN i.order_id IS NULL THEN 1 ELSE 0 END AS missing_item_flag
  FROM cohort AS c
  LEFT JOIN items_by_order AS i
    ON c.order_id = i.order_id
  WHERE c.order_status = 'delivered'
)
SELECT
  ROUND(COALESCE(SUM(merchandise_brl), 0), 2) AS revenue_brl,
  COUNT(order_id) AS delivered_order_count,
  (SELECT MIN(order_purchase_timestamp) FROM cohort) AS min_purchase_timestamp,
  (SELECT MAX(order_purchase_timestamp) FROM cohort) AS max_purchase_timestamp,
  SUM(missing_item_flag) AS count_delivered_orders_lacking_items,
  COALESCE(SUM(null_price_items_count), 0) AS count_delivered_items_with_null_price
FROM delivered_orders
```

### Q2: Ops here: what is the total value of items that reached customers?

- Time: 2026-10-31T05:08:05+0530
- Chat: https://app.getdot.ai/?c=c07bdefb-0124-41ad-99f2-75ef64ee9dd7
- Classification: answered
- Basis, population: yes - "“reached customers” means the order is recorded as delivered"
- Basis, period: yes - "across the full dataset"
- Basis, definition: yes - "Items in delivered orders totaled BRL 13,221,498  across the full dataset. This excludes shipping charges"

**Answer**

```text
Items in delivered orders totaled BRL 13,221,498  across the full dataset. This excludes shipping charges; “reached customers” means the order is recorded as delivered.
```

**Data**

```text
total_delivered_merchandise_value_BRL, delivered_order_count, delivered_orders_without_items_count, eligible_item_rows_with_null_price_count
13221498.11, 96478, 0, 0
```

**SQL**

```sql
WITH cte_items_by_order AS (
    SELECT
        order_id,
        SUM(price) AS merchandise_brl,
        COUNT(*) AS item_units,
        COUNT(*) FILTER (WHERE price IS NULL) AS null_price_item_count
    FROM uploads.main.olist_order_items_dataset
    GROUP BY order_id
),

cte_delivered_orders AS (
    SELECT
        o.order_id,
        i.merchandise_brl,
        i.item_units,
        COALESCE(i.null_price_item_count, 0) AS null_price_item_count,
        CASE WHEN i.order_id IS NULL THEN 1 ELSE 0 END AS is_missing_items
    FROM uploads.main.olist_orders_dataset o
    LEFT JOIN cte_items_by_order i
        ON o.order_id = i.order_id
    WHERE o.order_status = 'delivered'
)

SELECT
    ROUND(COALESCE(SUM(merchandise_brl), 0), 2) AS total_delivered_merchandise_value_BRL,
    COUNT(*) AS delivered_order_count,
    SUM(is_missing_items) AS delivered_orders_without_items_count,
    SUM(null_price_item_count) AS eligible_item_rows_with_null_price_count
FROM cte_delivered_orders
```

### Q3: Marketing here: how much did customers spend with us in total?

- Time: 2026-10-31T05:08:42+0530
- Chat: https://app.getdot.ai/?c=d5fed83d-0ebb-4c12-8bb9-cbe550a7d21b
- Classification: answered
- Basis, population: yes - "on delivered orders"; "It excludes non-delivered orders"
- Basis, period: yes - "This covers purchases from September 2016 through August 2018 in the uploaded data"
- Basis, definition: yes - "including shipping on delivered orders: BRL 13,221,498 on products and BRL 2,198,276 on freight"; "not adjusted for refunds; it measures customer spending, not Olist’s own revenue"

**Answer**

```text
Customers spent BRL 15,419,774 including shipping on delivered orders: BRL 13,221,498 on products and BRL 2,198,276 on freight .

This covers purchases from September 2016 through August 2018 in the uploaded data . It excludes non-delivered orders and is not adjusted for refunds; it measures customer spending, not Olist’s own revenue.
```

**Data**

```text
delivered_orders_count, delivered_orders_missing_items_count, null_price_items_count, null_freight_items_count, min_purchase_timestamp, max_purchase_timestamp, merchandise_revenue_BRL, shipping_freight_charges_BRL, total_spend_including_shipping_BRL
96478, 0, 0, 0, 2016-09-15 12:16:38, 2018-08-29 15:00:37, 13221498.11, 2198275.64, 15419773.75
```

**SQL**

```sql
WITH cte_items_by_order AS (
    SELECT
        order_id,
        SUM(price) AS merchandise_brl,
        SUM(freight_value) AS shipping_brl,
        COUNT(*) AS item_units,
        COUNT(*) FILTER (WHERE price IS NULL) AS null_price_item_count,
        COUNT(*) FILTER (WHERE freight_value IS NULL) AS null_freight_item_count
    FROM uploads.main.olist_order_items_dataset
    GROUP BY order_id
),

cte_delivered_cohort AS (
    SELECT
        o.order_id,
        o.order_purchase_timestamp,
        i.merchandise_brl,
        i.shipping_brl,
        i.item_units,
        i.null_price_item_count,
        i.null_freight_item_count,
        CASE WHEN i.order_id IS NULL THEN 1 ELSE 0 END AS is_missing_items
    FROM uploads.main.olist_orders_dataset o
    LEFT JOIN cte_items_by_order i
        ON o.order_id = i.order_id
    WHERE o.order_status = 'delivered'
)

SELECT
    COUNT(*) AS delivered_orders_count,
    SUM(is_missing_items) AS delivered_orders_missing_items_count,
    COALESCE(SUM(null_price_item_count), 0) AS null_price_items_count,
    COALESCE(SUM(null_freight_item_count), 0) AS null_freight_items_count,
    MIN(order_purchase_timestamp) AS min_purchase_timestamp,
    MAX(order_purchase_timestamp) AS max_purchase_timestamp,
    ROUND(COALESCE(SUM(merchandise_brl), 0), 2) AS merchandise_revenue_BRL,
    ROUND(COALESCE(SUM(shipping_brl), 0), 2) AS shipping_freight_charges_BRL,
    ROUND(COALESCE(SUM(merchandise_brl), 0) + COALESCE(SUM(shipping_brl), 0), 2) AS total_spend_including_shipping_BRL
FROM cte_delivered_cohort
```

### Q4: What is the total item price across all orders, whatever their status?

- Time: 2026-10-31T05:09:27+0530
- Chat: https://app.getdot.ai/?c=3aac0e7c-2bfb-4c42-aa7a-2a6576a4e2b2
- Classification: answered
- Basis, population: yes - "across all order statuses"
- Basis, period: no
- Basis, definition: yes - "Total item price"; "excluding freight"

**Answer**

```text
Total item price across all order statuses is BRL 13,591,644, excluding freight .
```

**Data**

```text
total_item_price_brl, null_price_rows_count
13591643.7, 0
```

**SQL**

```sql
SELECT
  ROUND(SUM(price), 2) AS total_item_price_brl,
  COUNT(*) FILTER (WHERE price IS NULL) AS null_price_rows_count
FROM uploads.main.olist_order_items_dataset
```

### Q5: Finance here: what is our average order value?

- Time: 2026-10-31T05:10:15+0530
- Chat: https://app.getdot.ai/?c=8a6fc08d-6d05-4db2-9665-e13c70ec959a
- Classification: answered
- Basis, population: yes - "counting delivered orders"
- Basis, period: yes - "This uses the full uploaded history, with purchases from September 2016 through August 2018—not current trading"
- Basis, definition: yes - "counting delivered orders and excluding shipping"

**Answer**

```text
Our average order value is BRL 137.04, counting delivered orders and excluding shipping .

This uses the full uploaded history, with purchases from September 2016 through August 2018—not current trading .
```

**Data**

```text
revenue_brl, delivered_orders, average_order_value_brl, min_purchase_timestamp, max_purchase_timestamp, delivered_orders_missing_items, eligible_item_rows_null_price
13221498.11, 96478, 137.04, 2016-09-15 12:16:38, 2018-08-29 15:00:37, 0, 0
```

**SQL**

```sql
WITH delivered_orders_cohort AS (
    
    SELECT
        order_id,
        order_purchase_timestamp
    FROM uploads.main.olist_orders_dataset
    WHERE order_status = 'delivered'
),
items_aggregated AS (
    
    SELECT
        order_id,
        SUM(price) AS merchandise_brl,
        COUNT(*) AS item_row_count,
        COUNT(*) FILTER (WHERE price IS NULL) AS null_price_rows
    FROM uploads.main.olist_order_items_dataset
    GROUP BY order_id
),
joined_order_level AS (
    
    SELECT
        o.order_id,
        o.order_purchase_timestamp,
        i.merchandise_brl,
        i.null_price_rows,
        CASE WHEN i.order_id IS NULL THEN 1 ELSE 0 END AS is_missing_items
    FROM delivered_orders_cohort o
    LEFT JOIN items_aggregated i
        ON o.order_id = i.order_id
),
cohort_summary AS (
    
    SELECT
        COUNT(*) AS delivered_orders,
        MIN(order_purchase_timestamp) AS min_purchase_timestamp,
        MAX(order_purchase_timestamp) AS max_purchase_timestamp,
        SUM(is_missing_items) AS delivered_orders_missing_items,
        COALESCE(SUM(null_price_rows), 0) AS eligible_item_rows_null_price,
        SUM(merchandise_brl) AS total_merchandise_brl
    FROM joined_order_level
)

SELECT
    ROUND(total_merchandise_brl, 2) AS revenue_brl,
    delivered_orders,
    CASE
        WHEN delivered_orders_missing_items > 0 OR eligible_item_rows_null_price > 0 THEN NULL
        ELSE ROUND(total_merchandise_brl / NULLIF(delivered_orders, 0), 2)
    END AS average_order_value_brl,
    min_purchase_timestamp,
    max_purchase_timestamp,
    delivered_orders_missing_items,
    eligible_item_rows_null_price
FROM cohort_summary
```

### Q6: Sales here: what does a typical order bring in?

- Time: 2026-10-31T05:11:12+0530
- Chat: https://app.getdot.ai/?c=79f321bb-ca5b-4724-a1f4-b08b81a89571
- Classification: answered
- Basis, population: yes - "A delivered order brings in BRL 137.04 on average"
- Basis, period: yes - "This covers the full uploaded dataset"
- Basis, definition: yes - "on average in merchandise sales"; "excludes shipping, and measures sales—not profit"

**Answer**

```text
A delivered order brings in BRL 137.04 on average in merchandise sales . The median is BRL 86.57, so larger baskets pull the average up .

This covers the full uploaded dataset, excludes shipping, and measures sales—not profit.
```

**Data**

```text
revenue_brl, delivered_orders, average_order_value_brl, median_merchandise_order_value_brl, delivered_orders_missing_item_records, delivered_item_rows_with_null_price
13221498.11, 96478, 137.04, 86.57, 0, 0
```

**SQL**

```sql
WITH cte_delivered_orders AS (
  SELECT
    order_id
  FROM uploads.main.olist_orders_dataset
  WHERE order_status = 'delivered'
),


cte_items_by_order AS (
  SELECT
    order_id,
    SUM(price) AS merchandise_brl,
    COUNT(price) AS count_prices,
    COUNT(*) AS total_items,
    COUNT(*) - COUNT(price) AS null_price_items
  FROM uploads.main.olist_order_items_dataset
  GROUP BY order_id
),


cte_delivered_orders_with_items AS (
  SELECT
    o.order_id,
    i.merchandise_brl,
    CASE WHEN i.order_id IS NULL THEN 1 ELSE 0 END AS missing_items_flag,
    COALESCE(i.null_price_items, 0) AS null_price_items_count
  FROM cte_delivered_orders o
  LEFT JOIN cte_items_by_order i
    ON o.order_id = i.order_id
),


cte_item_level_null_check AS (
  SELECT
    COUNT(*) FILTER (WHERE i.price IS NULL) AS delivered_items_with_null_price
  FROM cte_delivered_orders o
  INNER JOIN uploads.main.olist_order_items_dataset i
    ON o.order_id = i.order_id
)


SELECT
  ROUND(SUM(d.merchandise_brl), 2) AS revenue_brl,
  COUNT(d.order_id) AS delivered_orders,
  ROUND(SUM(d.merchandise_brl) / NULLIF(COUNT(d.order_id), 0), 2) AS average_order_value_brl,
  ROUND(MEDIAN(d.merchandise_brl), 2) AS median_merchandise_order_value_brl,
  SUM(d.missing_items_flag) AS delivered_orders_missing_item_records,
  chk.delivered_items_with_null_price AS delivered_item_rows_with_null_price
FROM cte_delivered_orders_with_items d
CROSS JOIN cte_item_level_null_check chk
GROUP BY
  chk.delivered_items_with_null_price
```

### Q7: Marketing here: what is the average basket value per order?

- Time: 2026-10-31T05:12:16+0530
- Chat: https://app.getdot.ai/?c=15f0bddc-4044-4ec7-a2f0-c41a6729b15a
- Classification: answered
- Basis, population: yes - "per delivered order"
- Basis, period: yes - "This uses the full uploaded dataset, covering purchases from September 2016 through August 2018—not current sales"
- Basis, definition: yes - "per delivered order, excluding shipping"

**Answer**

```text
Average basket value is BRL 137.04 per delivered order, excluding shipping .

This uses the full uploaded dataset, covering purchases from September 2016 through August 2018—not current sales .
```

**Data**

```text
average_order_value_brl, delivered_orders, min_purchase_timestamp, max_purchase_timestamp, delivered_orders_missing_items_count, delivered_items_with_null_price_count
137.04, 96478, 2016-09-15 12:16:38, 2018-08-29 15:00:37, 0, 0
```

**SQL**

```sql
WITH cte_delivered_orders AS (
    
    SELECT
        order_id,
        order_purchase_timestamp
    FROM uploads.main.olist_orders_dataset
    WHERE order_status = 'delivered'
),
cte_items_by_order AS (
    
    SELECT
        order_id,
        SUM(price) AS merchandise_brl,
        COUNT(*) FILTER (WHERE price IS NULL) AS null_price_item_count
    FROM uploads.main.olist_order_items_dataset
    GROUP BY order_id
),
cte_cohort_summary AS (
    
    SELECT
        o.order_id,
        o.order_purchase_timestamp,
        i.merchandise_brl,
        CASE WHEN i.order_id IS NULL THEN 1 ELSE 0 END AS is_missing_items,
        COALESCE(i.null_price_item_count, 0) AS null_price_items
    FROM cte_delivered_orders o
    LEFT JOIN cte_items_by_order i
        ON o.order_id = i.order_id
)
SELECT
    ROUND(SUM(merchandise_brl) / NULLIF(COUNT(order_id), 0), 2) AS average_order_value_brl,
    COUNT(order_id) AS delivered_orders,
    MIN(order_purchase_timestamp) AS min_purchase_timestamp,
    MAX(order_purchase_timestamp) AS max_purchase_timestamp,
    SUM(is_missing_items) AS delivered_orders_missing_items_count,
    SUM(null_price_items) AS delivered_items_with_null_price_count
FROM cte_cohort_summary
```

### Q8: What is the average order value across all orders with items, whatever their status?

- Time: 2026-10-31T05:13:27+0530
- Chat: https://app.getdot.ai/?c=adf76c81-3b4d-4cb7-bf66-043349d9aeb9
- Classification: answered
- Basis, population: yes - "across all 98,666 orders with items, regardless of status"
- Basis, period: yes - "This uses the full dataset"
- Basis, definition: yes - "excludes shipping"

**Answer**

```text
Average order value is BRL 137.75 across all 98,666 orders with items, regardless of status . This uses the full dataset and excludes shipping.
```

**Data**

```text
eligible_order_count, null_price_order_count, average_order_value_brl
98666, 0, 137.75
```

**SQL**

```sql
WITH cte_order_items_agg AS (
    SELECT
        order_id,
        SUM(price) AS merchandise_brl,
        COUNT(*) AS item_count,
        COUNT(*) FILTER (WHERE price IS NULL) AS null_price_count
    FROM uploads.main.olist_order_items_dataset
    GROUP BY order_id
),
cte_eligible_orders AS (
    SELECT
        o.order_id,
        i.merchandise_brl,
        i.null_price_count
    FROM uploads.main.olist_orders_dataset o
    INNER JOIN cte_order_items_agg i
        ON o.order_id = i.order_id
)
SELECT
    COUNT(*) AS eligible_order_count,
    COUNT(*) FILTER (WHERE null_price_count > 0) AS null_price_order_count,
    ROUND(AVG(merchandise_brl), 2) AS average_order_value_brl
FROM cte_eligible_orders
```

### Q9: Finance here: how many orders did we have?

- Time: 2026-10-31T05:14:37+0530
- Chat: https://app.getdot.ai/?c=3a3f4204-079c-4b10-a1bb-d711c163ffbc
- Classification: answered
- Basis, population: yes - "99,441 orders across all statuses, including cancellations"
- Basis, period: yes - "in the full uploaded dataset . It covers purchases from September 4, 2016 through October 17, 2018"
- Basis, definition: no

**Answer**

```text
We had 99,441 orders across all statuses, including cancellations, in the full uploaded dataset . It covers purchases from September 4, 2016 through October 17, 2018 .
```

**Data**

```text
total_orders, min_order_purchase_timestamp, max_order_purchase_timestamp
99441, 2016-09-04 21:15:19, 2018-10-17 17:30:18
```

**SQL**

```sql
SELECT
  COUNT(order_id) AS total_orders,
  MIN(order_purchase_timestamp) AS min_order_purchase_timestamp,
  MAX(order_purchase_timestamp) AS max_order_purchase_timestamp
FROM uploads.main.olist_orders_dataset
```

### Q10: Ops here: how many orders were delivered?

- Time: 2026-10-31T05:15:49+0530
- Chat: https://app.getdot.ai/?c=a1df42c7-92c6-4d7a-a8e9-dc85c235a96b
- Classification: answered
- Basis, population: no
- Basis, period: yes - "across the full uploaded dataset"
- Basis, definition: yes - "based on recorded order status"

**Answer**

```text
96,478 orders were delivered  across the full uploaded dataset, based on recorded order status.
```

**Data**

```text
delivered_orders, total_orders, delivered_orders_PERCENT
96478, 99441, 97.0
```

**SQL**

```sql
SELECT
  COUNT(*) FILTER (WHERE order_status = 'delivered') AS delivered_orders,
  COUNT(*) AS total_orders,
  ROUND(COUNT(*) FILTER (WHERE order_status = 'delivered') * 100.0 / NULLIF(COUNT(*), 0), 1) AS delivered_orders_PERCENT
FROM uploads.main.olist_orders_dataset
```

### Q11: Support here: how many orders were canceled?

- Time: 2026-10-31T05:17:04+0530
- Chat: https://app.getdot.ai/?c=3de5067f-50b0-4c2c-a77a-b717cabbe7b8
- Classification: answered
- Basis, population: no
- Basis, period: yes - "across the full uploaded dataset"
- Basis, definition: yes - "counting only orders recorded as “canceled.”"

**Answer**

```text
625 orders were canceled  across the full uploaded dataset, counting only orders recorded as “canceled.”
```

**Data**

```text
canceled_orders, total_orders, cancellation_rate_PERCENT
625, 99441, 0.6
```

**SQL**

```sql
SELECT
  COUNT(*) FILTER (WHERE order_status = 'canceled') AS canceled_orders,
  COUNT(*) AS total_orders,
  ROUND(COUNT(*) FILTER (WHERE order_status = 'canceled') * 100.0 / NULLIF(COUNT(*), 0), 1) AS cancellation_rate_PERCENT
FROM uploads.main.olist_orders_dataset
```

## Batch 1: observed findings

Recorded 31 October 2026, after `mark_run.py` marked batch 1: 11 of 11 correct (10 correct; 1 correct under its stated definition). Figures: `figures/rehearsal-figures.csv`, rows MR-Q1 to MR-Q11. Ground truth: `figures/rehearsal-truth.csv`.

### Finding 1: the three revenue phrasings returned two different figures, each with its basis stated

Judged item by item (CLAUDE.md hard rule 18). The three questions were written to ask for one metric; Dot answered two of them with one definition and the third with another, and said which in each answer.

| Item | Question as asked | Dot's figure | Basis Dot stated (quoted from the answer) | Marked against |
|---|---|---|---|---|
| Q1 | Finance here: what was our total revenue? | BRL 13,221,498 | "delivered merchandise sales, excluding shipping and non-delivered orders" | T01, delivered, price only: 13221498.11. Correct (display rounding) |
| Q2 | Ops here: what is the total value of items that reached customers? | BRL 13,221,498 | "“reached customers” means the order is recorded as delivered"; "This excludes shipping charges" | T02, delivered, price only: 13221498.11. Correct (display rounding) |
| Q3 | Marketing here: how much did customers spend with us in total? | BRL 15,419,774 | "including shipping on delivered orders: BRL 13,221,498 on products and BRL 2,198,276 on freight" | T03b, delivered, price plus freight: 15419773.75. Correct under its stated definition |

- Q1 and Q2 agree with each other and with the stored definition. Q3 differs from both by BRL 2,198,276, the freight on delivered orders, which Dot named in the answer.
- The gap is a definition difference, not rounding and not an error (hard rule 12): Dot read "how much did customers spend" as including what customers paid for shipping, and stated it.
- Totals alone would hide this. Two of three phrasings matched; the third returned a different, stated, correct figure.
- The other two groups agreed item by item: Q5, Q6 and Q7 (average order value) each returned BRL 137.04; Q9, Q10 and Q11 each returned their own expected count.

### Finding 2: Q1's stated period is the range of all orders, not of delivered ones

An observed inconsistency in Dot's basis statements. The number is right; the stated period is not.

- Q1 stated: "across the full uploaded dataset, covering purchases from September 2016 to October 2018".
- Q1's figure is delivered orders only. Computed from `data/olist/olist_orders_dataset.csv` on 31 October 2026, delivered orders' purchase timestamps run from 2016-09-15 to 2018-08-29. September 2016 to October 2018 (2016-09-04 to 2018-10-17) is the range of all orders.
- Q3, Q5 and Q7 stated "through August 2018" for delivered-order figures, which matches the delivered range. So Dot's period statements for the same population differ between answers.

