# ai-analyst-shows-sql run

## Batch 1: conditions

Observed in Dot's UI by a person at about 17:00 IST on 31 October 2026, before the first question, and recorded here as text. **No screenshots were taken.**

**Rule 14 waived for this piece** by Saurabh, 31 October 2026 (run with `stage_gate.py --no-screenshots`). The mode, environment, context notes and credits are a person's observation, not screenshotted evidence. **Therefore no claim about mode, credits, environment or context notes may appear in the published piece**: not the mode the answers ran in, not their cost, not which notes were on. Only claims resting on Dot's answers and their SQL, as recorded below, are supported. This reverses the plan's earlier "screenshots for both batches" (PLAN.md), on Saurabh's instruction.

**This batch is also piece 3's "without note" batch (PLAN.md).** Its notes state is hand-recorded text, with one machine-read check below.

- Date: 2026-10-31, about 17:00 IST (conditions); each entry's time is from `date`
- Workspace: aiinterviewagents.com
- Tables: uploads.main.olist_orders_dataset; uploads.main.olist_order_items_dataset
- Data sources on: olist_order_items_dataset, olist_orders_dataset
- Mode: Balanced. Recorded by hand; no screenshot (rule 14 waived)
- Environment: Production. Recorded by hand; no screenshot (rule 14 waived)
- Context notes: on: "Olist dataset currency and monetary formatting", "Olist revenue, order value, basket size, cancellation and shipping metrics". Off: "About aiinterviewagents.com". Recorded by hand; no screenshot (rule 14 waived)
- Credits before: 90.6 of 300 used. Recorded by hand; no screenshot (rule 14 waived)
- Credits after: 97.7 of 300 used. Recorded by hand after Q12; no screenshot (rule 14 waived). Batch 1 used 7.1 credits (97.7 − 90.6). Under the waiver this figure may not appear in the published piece
- Model: not observable via MCP

**Catalog check, read through the MCP before the first question** (`get_catalog`, query "delivered in year delivery date", 31 October 2026, about 17:05 IST). Definitions returned: two, "Olist revenue, order value, basket size, cancellation and shipping metrics" and "Olist dataset currency and monetary formatting". No definition named for "delivered in <year>" or for a delivery-date reading. The tool truncates definition text: the metrics note's returned text ends "Unless explicitly requested otherwise, report a pur…", so whether it already sets a default date basis is not observable via MCP. Whether `get_catalog` lists notes that are switched off is also not observable: the off note "About aiinterviewagents.com" was not returned, which fits either reading.

**The metrics note, verbatim.** Note "Olist revenue, order value, basket size, cancellation and shipping metrics", on for this batch. Copied from Model → Notes by Saurabh on 31 October 2026, after the run, and saved here as evidence; the get_catalog read above truncates it. Whether the text was the same at the time of the run is the person's record, not observable via MCP.

```text
Shared reporting rules

These definitions apply to uploads.main.olist_orders_dataset (one row per order_id) and uploads.main.olist_order_items_dataset (one row per (order_id, order_item_id)). Monetary metrics are in BRL, as defined in the Olist currency note.

Unless explicitly requested otherwise, report a purchase cohort using order_purchase_timestamp: include timestamps at or after the period start and strictly before the period end. Use timestamps as stored; do not invent a timezone conversion. Status means the recorded order_status in the uploaded snapshot, not status at purchase time. Results describe that cohort's recorded outcomes, not accounting revenue recognized on delivery dates; recent cohorts can still have incomplete outcomes.

For revenue, average order value, average basket size and shipping revenue, eligible orders have order_status = 'delivered'. Do not additionally require an approval or delivery timestamp. This default measures fulfilled sales rather than a pipeline that can still fail. It excludes canceled, unavailable, created, approved, processing, invoiced, shipped, and any other non-delivered status. Non-canceled booked sales are a reasonable alternative, but must be explicitly named and given their own status scope; they are not the default revenue here.

Aggregate item rows to order_id before joining to orders on order_id. Set:

merchandise_brl = SUM(price) per order;

shipping_brl = SUM(freight_value) per order;

item_units = COUNT(*) per order.

An item row counts as one purchased unit; order_item_id is a sequence within the order, not a quantity to sum. The same product appearing twice counts as two units. Do not deduplicate on product_id, or use SUM(DISTINCT price) or SUM(DISTINCT freight_value): identical amounts on different item rows are legitimate. Use the orders table without an item join for cancellation rate so orders without items remain in the denominator.

If delivered orders lack items, or required item amounts are null, report the data-quality gap rather than silently treating them as zero or excluding their orders from an average. The formulas assume complete eligible item records. Return null/undefined for averages or rates with zero eligible orders; monetary totals for an empty eligible cohort are zero.

Metric definitions

Revenue

Formula: SUM(merchandise_brl) over eligible orders, equivalent to summing item price after filtering orders to delivered.

Grain: Item amounts aggregated to one order, then summed across the reporting cohort; unit BRL.

Status filter: Delivered only.

Excludes: Freight, non-delivered orders, and any unrepresented taxes, fees, commissions or other charges. There is no refund/return adjustment in these two tables, so do not label this net revenue or infer that delivered sales were never refunded.

Chosen interpretation: Delivered merchandise sales (a merchandise GMV proxy), not Olist's own corporate revenue. Merchandise plus shipping is also a reasonable customer-facing sales total, but keeping freight separate makes product sales and shipping performance independently interpretable. These tables cannot establish accounting recognition, marketplace commissions, or net receipts.

Average order value (AOV)

Formula: Revenue / COUNT(delivered orders) within the same purchase cohort; equivalently AVG(merchandise_brl) at order grain with complete item coverage.

Grain: One delivered order contributes one basket total and one denominator count; unit BRL per order.

Status filter: Delivered only, matching revenue exactly.

Excludes: Freight and all non-delivered orders; no additional refund adjustment is available. Do not average individual item prices or average subgroup AOVs without order-count weighting.

Chosen interpretation: Merchandise-only AOV keeps AOV × delivered order count = revenue. A freight-inclusive average is valid when explicitly called average order value including shipping: (Revenue + Shipping revenue) / delivered order count.

Average basket size

Formula: SUM(item_units) / COUNT(delivered orders) in the same purchase cohort; equivalently AVG(item_units) at order grain with complete item coverage. Use non-integer division.

Grain: Purchased item units per delivered order.

Status filter: Delivered only.

Excludes: Non-delivered orders; not a count of distinct products, sellers or customers, and not a monetary basket value.

Chosen interpretation: Units per order measures how many items customers purchase. Distinct products per order is a reasonable assortment/diversity metric but would count repeated units as one; explicitly name that alternative average distinct products per order. Monetary basket value is AOV, not basket size.

Cancellation rate

Formula: 100.0 × COUNT(orders WHERE order_status = 'canceled') / COUNT(all orders) for the same purchase cohort.

Grain: One order, regardless of how many items it contains or whether it has any item rows; unit percent.

Status filter: Numerator is exactly canceled; denominator includes every recorded status, including canceled, unavailable, delivered and in-progress orders. No delivered-only restriction applies.

Excludes: unavailable and other non-canceled statuses from the numerator, but not the denominator. Cannot count historical cancellation events, item-level cancellations, returns, or refunds from this status snapshot.

Chosen interpretation: Explicit cancellations divided by all placed orders is directly auditable and does not collapse unavailable inventory into cancellation. If requested, canceled-or-unavailable rate uses both statuses in the numerator and the same denominator; it is a broader unsuccessful-order measure, not cancellation rate. A terminal-outcome-only denominator is another distinct metric and must not be substituted silently.

Shipping revenue

Formula: SUM(shipping_brl) over eligible orders, equivalent to summing item freight_value after filtering orders to delivered.

Grain: Item freight amounts aggregated to order, then summed across the reporting cohort; unit BRL.

Status filter: Delivered only, matching revenue and AOV.

Excludes: Merchandise price, non-delivered orders, carrier operating costs, and any unrecorded shipping refunds or adjustments. Zero-freight delivered items remain eligible.

Chosen interpretation: Recorded freight charges associated with delivered sales, not profit, carrier cost or proven Olist-retained revenue. The name shipping revenue refers to this dataset proxy. Freight on all placed orders is a reasonable booked-charge measure but includes unsuccessful and unfinished orders; delivered freight is consistent with fulfilled merchandise revenue.

Reference SQL

This produces the five metrics at cohort level without order fanout. To select a period, add WHERE order_purchase_timestamp >= <start timestamp> AND order_purchase_timestamp < <end timestamp> inside cohort. For no period filter, it uses the full uploaded cohort. Check item completeness before using the result.

WITH cohort AS (
  SELECT order_id, order_status
  FROM uploads.main.olist_orders_dataset
), items_by_order AS (
  SELECT order_id,
         SUM(price) AS merchandise_brl,
         SUM(freight_value) AS shipping_brl,
         COUNT(*) AS item_units
  FROM uploads.main.olist_order_items_dataset
  GROUP BY order_id
), fulfilled AS (
  SELECT c.order_id, i.merchandise_brl, i.shipping_brl, i.item_units
  FROM cohort c
  LEFT JOIN items_by_order i ON c.order_id = i.order_id
  WHERE c.order_status = 'delivered'
), sales AS (
  SELECT COUNT(*) AS delivered_orders,
         COALESCE(SUM(merchandise_brl), 0) AS revenue_brl,
         COALESCE(SUM(shipping_brl), 0) AS shipping_revenue_brl,
         SUM(item_units) AS units
  FROM fulfilled
), cancellations AS (
  SELECT COUNT(*) AS placed_orders,
         COUNT(*) FILTER (WHERE order_status = 'canceled') AS canceled_orders
  FROM cohort
)
SELECT s.revenue_brl,
       s.revenue_brl / NULLIF(s.delivered_orders, 0) AS average_order_value_brl,
       1.0 * s.units / NULLIF(s.delivered_orders, 0) AS average_basket_size,
       100.0 * c.canceled_orders / NULLIF(c.placed_orders, 0) AS cancellation_rate_pct,
       s.shipping_revenue_brl
FROM sales s CROSS JOIN cancellations c;
```

### Q1: How many orders were delivered in 2017?

- Time: 2026-10-31T17:14:30+0530
- Chat: https://app.getdot.ai/?c=9d395282-f9e2-48fd-baff-998376c1a8ac
- Classification: answered
- Basis, population: yes - "have a recorded status of delivered"
- Basis, period: yes - "orders placed in 2017"
- Basis, definition: yes - "This uses purchase date, not delivery date."

**Answer**

```text
43,428 orders placed in 2017 have a recorded status of delivered . This uses purchase date, not delivery date.
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

### Q2: What was the total item price of orders delivered in 2017?

- Time: 2026-10-31T17:15:01+0530
- Chat: https://app.getdot.ai/?c=d318f093-128e-449c-b95b-1647ad2726fa
- Classification: answered
- Basis, population: yes - "for orders delivered during calendar 2017"
- Basis, period: yes - "during calendar 2017"
- Basis, definition: yes - "excluding freight . This uses delivery date, not purchase date."

**Answer**

```text
Total item price was BRL 5,612,818 for orders delivered during calendar 2017, excluding freight . This uses delivery date, not purchase date.
```

**Data**

```text
total_item_price_BRL, delivered_order_count, missing_item_orders_count, null_item_prices_count
5612817.85, 40930, 0, 0
```

**SQL**

```sql
WITH cte_delivered_2017_orders AS (
  SELECT
    order_id
  FROM uploads.main.olist_orders_dataset
  WHERE order_status = 'delivered'
    AND order_delivered_customer_date >= '2017-01-01'
    AND order_delivered_customer_date < '2018-01-01'
),


cte_items_per_order AS (
  SELECT
    order_id,
    SUM(price) AS merchandise_price,
    COUNT(CASE WHEN price IS NULL THEN 1 END) AS null_price_count,
    COUNT(*) AS item_row_count
  FROM uploads.main.olist_order_items_dataset
  GROUP BY order_id
)


SELECT
  ROUND(COALESCE(SUM(i.merchandise_price), 0), 2) AS total_item_price_BRL,
  COUNT(o.order_id) AS delivered_order_count,
  COUNT(CASE WHEN i.order_id IS NULL THEN 1 END) AS missing_item_orders_count,
  COALESCE(SUM(i.null_price_count), 0) AS null_item_prices_count
FROM cte_delivered_2017_orders o
LEFT JOIN cte_items_per_order i
  ON o.order_id = i.order_id
```

### Q3: How much did customers spend in 2017?

- Time: 2026-10-31T17:15:38+0530
- Chat: https://app.getdot.ai/?c=685aef3f-8a95-45cb-b5cf-c25cd34c21c0
- Classification: answered
- Basis, population: yes - "that were delivered"
- Basis, period: yes - "on orders placed in 2017"
- Basis, definition: yes - "including shipping"

**Answer**

```text
Customers spent BRL 6,921,535 on orders placed in 2017 that were delivered, including shipping .

That comprises BRL 5,962,902 in merchandise and BRL 958,633 in shipping . Refunds are not accounted for in these tables.
```

**Data**

```text
delivered_orders_count, delivered_orders_missing_items_count, null_price_items_count, null_freight_items_count, merchandise_revenue_brl, recorded_freight_brl, total_spending_brl
43428, 0, 0, 0, 5962902.01, 958633.23, 6921535.24
```

**SQL**

```sql
WITH cte_delivered_cohort AS (
  SELECT
    order_id
  FROM uploads.main.olist_orders_dataset
  WHERE order_purchase_timestamp >= '2017-01-01'
    AND order_purchase_timestamp < '2018-01-01'
    AND order_status = 'delivered'
),
cte_items_aggregated AS (
  SELECT
    order_id,
    SUM(price) AS merchandise_brl,
    SUM(freight_value) AS shipping_brl,
    COUNT(*) FILTER (WHERE price IS NULL) AS null_price_item_count,
    COUNT(*) FILTER (WHERE freight_value IS NULL) AS null_freight_item_count
  FROM uploads.main.olist_order_items_dataset
  GROUP BY order_id
)
SELECT
  COUNT(c.order_id) AS delivered_orders_count,
  COUNT(c.order_id) FILTER (WHERE i.order_id IS NULL) AS delivered_orders_missing_items_count,
  COALESCE(SUM(i.null_price_item_count), 0) AS null_price_items_count,
  COALESCE(SUM(i.null_freight_item_count), 0) AS null_freight_items_count,
  ROUND(COALESCE(SUM(i.merchandise_brl), 0), 2) AS merchandise_revenue_brl,
  ROUND(COALESCE(SUM(i.shipping_brl), 0), 2) AS recorded_freight_brl,
  ROUND(COALESCE(SUM(i.merchandise_brl), 0) + COALESCE(SUM(i.shipping_brl), 0), 2) AS total_spending_brl
FROM cte_delivered_cohort c
LEFT JOIN cte_items_aggregated i
  ON c.order_id = i.order_id
```

### Q4: How many orders did we get in 2017?

- Time: 2026-10-31T17:16:24+0530
- Chat: https://app.getdot.ai/?c=161fb7c0-f2a8-4aac-a4c5-fe88b0bac317
- Classification: answered
- Basis, population: yes - "including all order statuses"
- Basis, period: yes - "45,101 orders in 2017"
- Basis, definition: no

**Answer**

```text
We received 45,101 orders in 2017, including all order statuses .
```

**Data**

```text
total_orders
45101
```

**SQL**

```sql
SELECT
  COUNT(order_id) AS total_orders
FROM uploads.main.olist_orders_dataset
WHERE order_purchase_timestamp >= '2017-01-01'
  AND order_purchase_timestamp < '2018-01-01'
```

### Q5: How many orders were delivered late in 2017?

- Time: 2026-10-31T17:17:08+0530
- Chat: https://app.getdot.ai/?c=a50b9777-ac9b-4fc8-85ac-f9cd1560f961
- Classification: answered
- Basis, population: yes - "orders placed in 2017 were delivered late"
- Basis, period: yes - "orders placed in 2017"
- Basis, definition: yes - "meaning delivery occurred after the estimated delivery timestamp"

**Answer**

```text
2,878 orders placed in 2017 were delivered late, meaning delivery occurred after the estimated delivery timestamp .

Two delivered orders had missing timestamps and could not be assessed .
```

**Data**

```text
late_delivered_orders, unassessable_delivered_orders, total_delivered_orders, late_delivered_orders_PERCENT
2878, 2, 43428, 6.6
```

**SQL**

```sql
SELECT
  COUNT(*) FILTER (
    WHERE order_delivered_customer_date IS NOT NULL
      AND order_estimated_delivery_date IS NOT NULL
      AND order_delivered_customer_date > order_estimated_delivery_date
  ) AS late_delivered_orders,
  COUNT(*) FILTER (
    WHERE order_delivered_customer_date IS NULL
      OR order_estimated_delivery_date IS NULL
  ) AS unassessable_delivered_orders,
  COUNT(*) AS total_delivered_orders,
  ROUND(
    COUNT(*) FILTER (
      WHERE order_delivered_customer_date IS NOT NULL
        AND order_estimated_delivery_date IS NOT NULL
        AND order_delivered_customer_date > order_estimated_delivery_date
    ) * 100.0 / NULLIF(COUNT(*), 0),
    1
  ) AS late_delivered_orders_PERCENT
FROM uploads.main.olist_orders_dataset
WHERE order_purchase_timestamp >= TIMESTAMP '2017-01-01 00:00:00'
  AND order_purchase_timestamp < TIMESTAMP '2018-01-01 00:00:00'
  AND order_status = 'delivered'
```

### Q6: What percentage of delivered orders were late in 2018?

- Time: 2026-10-31T17:17:56+0530
- Chat: https://app.getdot.ai/?c=c0d3b369-676e-48ad-b4b4-9fdf34f7efe4
- Classification: answered
- Basis, population: yes - "of delivered orders placed in 2018"
- Basis, period: yes - "placed in 2018"
- Basis, definition: yes - "meaning they arrived after the estimated delivery date"

**Answer**

```text
7.7% of delivered orders placed in 2018 were late , meaning they arrived after the estimated delivery date.

Six orders with missing delivery dates were excluded from the calculation .
```

**Data**

```text
total_delivered_orders, missing_timestamps_orders, late_orders, late_delivered_orders_PERCENT
52783, 6, 4078, 7.7
```

**SQL**

```sql
WITH delivered_cohort AS (
    SELECT
        order_id,
        order_delivered_customer_date,
        order_estimated_delivery_date,
        
        CASE
            WHEN order_delivered_customer_date IS NULL OR order_estimated_delivery_date IS NULL THEN 1
            ELSE 0
        END AS is_missing_timestamp,
        
        CASE
            WHEN order_delivered_customer_date IS NOT NULL
                 AND order_estimated_delivery_date IS NOT NULL
                 AND CAST(order_delivered_customer_date AS DATE) > CAST(order_estimated_delivery_date AS DATE) THEN 1
            ELSE 0
        END AS is_late
    FROM uploads.main.olist_orders_dataset
    WHERE order_purchase_timestamp >= TIMESTAMP '2018-01-01 00:00:00'
      AND order_purchase_timestamp < TIMESTAMP '2019-01-01 00:00:00'
      AND order_status = 'delivered'
)
SELECT
    COUNT(*) AS total_delivered_orders,
    SUM(is_missing_timestamp) AS missing_timestamps_orders,
    SUM(is_late) AS late_orders,
    ROUND(SUM(is_late) * 100.0 / NULLIF(COUNT(*) - SUM(is_missing_timestamp), 0), 1) AS late_delivered_orders_PERCENT
FROM delivered_cohort
```

### Q7: How many orders were delivered in 2017?

- Time: 2026-10-31T17:18:46+0530
- Chat: https://app.getdot.ai/?c=b7f8ad8f-2cbb-4bf2-a182-4720d23ef04b
- Classification: answered
- Basis, population: yes - "were delivered"
- Basis, period: yes - "orders placed in 2017"
- Basis, definition: yes - "This uses purchase dates, not delivery dates."

**Answer**

```text
43,428 orders placed in 2017 were delivered . This uses purchase dates, not delivery dates.
```

**Data**

```text
delivered_orders, total_orders, delivered_rate_PERCENT
43428, 45101, 96.3
```

**SQL**

```sql
SELECT
  COUNT(*) FILTER (WHERE order_status = 'delivered') AS delivered_orders,
  COUNT(*) AS total_orders,
  ROUND(COUNT(*) FILTER (WHERE order_status = 'delivered') * 100.0 / NULLIF(COUNT(*), 0), 1) AS delivered_rate_PERCENT
FROM uploads.main.olist_orders_dataset
WHERE order_purchase_timestamp >= TIMESTAMP '2017-01-01 00:00:00'
  AND order_purchase_timestamp < TIMESTAMP '2018-01-01 00:00:00'
```

### Q8: What was the total item price of orders delivered in 2017?

- Time: 2026-10-31T17:19:44+0530
- Chat: https://app.getdot.ai/?c=3da97565-a6e7-44a4-9d45-8a93c3a44849
- Classification: answered
- Basis, population: yes - "for orders delivered in calendar year 2017"
- Basis, period: yes - "in calendar year 2017"
- Basis, definition: yes - "excluding freight . This uses the actual delivery date, not the purchase date."

**Answer**

```text
The total item price was BRL 5,612,818 for orders delivered in calendar year 2017, excluding freight . This uses the actual delivery date, not the purchase date.
```

**Data**

```text
total_item_price_brl, delivered_order_count, eligible_orders_without_items_count, eligible_item_rows_with_null_price_count
5612817.85, 40930, 0, 0
```

**SQL**

```sql
WITH cte_eligible_orders AS (
    
    SELECT
        order_id
    FROM uploads.main.olist_orders_dataset
    WHERE order_status = 'delivered'
      AND order_delivered_customer_date >= TIMESTAMP '2017-01-01 00:00:00'
      AND order_delivered_customer_date < TIMESTAMP '2018-01-01 00:00:00'
),
cte_order_items_agg AS (
    
    SELECT
        order_id,
        SUM(price) AS merchandise_brl,
        COUNT(*) AS total_item_rows,
        COUNT(*) FILTER (WHERE price IS NULL) AS null_price_rows
    FROM uploads.main.olist_order_items_dataset
    WHERE order_id IN (SELECT order_id FROM cte_eligible_orders)
    GROUP BY order_id
)
SELECT
    ROUND(COALESCE(SUM(i.merchandise_brl), 0.0), 2) AS total_item_price_brl,
    COUNT(o.order_id) AS delivered_order_count,
    COUNT(o.order_id) FILTER (WHERE i.order_id IS NULL) AS eligible_orders_without_items_count,
    COALESCE(SUM(i.null_price_rows), 0) AS eligible_item_rows_with_null_price_count
FROM cte_eligible_orders o
LEFT JOIN cte_order_items_agg i
    ON o.order_id = i.order_id
```

### Q9: How much did customers spend in 2017?

- Time: 2026-10-31T17:20:47+0530
- Chat: https://app.getdot.ai/?c=f34b4cc9-afc5-46a9-a27a-82617209f605
- Classification: answered
- Basis, population: yes - "that were delivered . ... Canceled and other non-delivered orders are excluded"
- Basis, period: yes - "on orders placed in 2017"
- Basis, definition: yes - "including shipping"

**Answer**

```text
Customers spent BRL 6,921,535 including shipping on orders placed in 2017 that were delivered .

That includes BRL 5,962,902 in merchandise and BRL 958,633 in shipping . Canceled and other non-delivered orders are excluded; refunds are not reflected in these tables.
```

**Data**

```text
delivered_orders_count, delivered_orders_missing_items_count, total_merchandise_price_brl, total_freight_value_brl, total_customer_spend_brl, null_price_item_rows_count, null_freight_item_rows_count
43428, 0, 5962902.01, 958633.23, 6921535.24, 0, 0
```

**SQL**

```sql
WITH cte_orders_2017 AS (
    
    SELECT
        order_id
    FROM uploads.main.olist_orders_dataset
    WHERE order_purchase_timestamp >= '2017-01-01'
      AND order_purchase_timestamp < '2018-01-01'
      AND order_status = 'delivered'
),
cte_items_by_order AS (
    
    SELECT
        order_id,
        SUM(price) AS merchandise_brl,
        SUM(freight_value) AS shipping_brl,
        COUNT(*) AS item_units,
        COUNT(*) FILTER (WHERE price IS NULL) AS null_price_items_count,
        COUNT(*) FILTER (WHERE freight_value IS NULL) AS null_freight_items_count
    FROM uploads.main.olist_order_items_dataset
    GROUP BY order_id
),
cte_order_level_joined AS (
    
    SELECT
        o.order_id,
        i.merchandise_brl,
        i.shipping_brl,
        i.null_price_items_count,
        i.null_freight_items_count,
        CASE WHEN i.order_id IS NULL THEN 1 ELSE 0 END AS is_missing_items
    FROM cte_orders_2017 o
    LEFT JOIN cte_items_by_order i
        ON o.order_id = i.order_id
)
SELECT
    COUNT(*) AS delivered_orders_count,
    SUM(is_missing_items) AS delivered_orders_missing_items_count,
    ROUND(COALESCE(SUM(merchandise_brl), 0), 2) AS total_merchandise_price_brl,
    ROUND(COALESCE(SUM(shipping_brl), 0), 2) AS total_freight_value_brl,
    ROUND(COALESCE(SUM(merchandise_brl), 0) + COALESCE(SUM(shipping_brl), 0), 2) AS total_customer_spend_brl,
    COALESCE(SUM(null_price_items_count), 0) AS null_price_item_rows_count,
    COALESCE(SUM(null_freight_items_count), 0) AS null_freight_item_rows_count
FROM cte_order_level_joined
```

### Q10: How many orders did we get in 2017?

- Time: 2026-10-31T17:21:54+0530
- Chat: https://app.getdot.ai/?c=e18802c4-7fb3-4d79-b85e-5785edf8c189
- Classification: answered
- Basis, population: yes - "including all order statuses"
- Basis, period: yes - "45,101 orders in 2017"
- Basis, definition: yes - "based on purchase date"

**Answer**

```text
We received 45,101 orders in 2017, including all order statuses, based on purchase date .
```

**Data**

```text
total_orders
45101
```

**SQL**

```sql
SELECT
  COUNT(order_id) AS total_orders
FROM uploads.main.olist_orders_dataset
WHERE order_purchase_timestamp >= '2017-01-01 00:00:00'
  AND order_purchase_timestamp < '2018-01-01 00:00:00'
```

### Q11: How many orders were delivered late in 2017?

- Time: 2026-10-31T17:23:04+0530
- Chat: https://app.getdot.ai/?c=ae3884e7-7dd4-46a3-9667-fdcaac054f83
- Classification: answered
- Basis, population: yes - "orders placed in 2017 were delivered late"
- Basis, period: yes - "orders placed in 2017"
- Basis, definition: yes - "meaning they arrived after the estimated delivery day"

**Answer**

```text
2,453 orders placed in 2017 were delivered late, meaning they arrived after the estimated delivery day .

Two delivered orders lacked dates and could not be assessed .
```

**Data**

```text
total_delivered_orders, late_delivered_order_count, late_delivered_order_rate_PERCENT, missing_delivery_dates_count
43428, 2453, 5.6, 2
```

**SQL**

```sql
SELECT
  COUNT(*) AS total_delivered_orders,
  COUNT(*) FILTER (
    WHERE CAST(order_delivered_customer_date AS DATE) > CAST(order_estimated_delivery_date AS DATE)
  ) AS late_delivered_order_count,
  ROUND(
    COUNT(*) FILTER (
      WHERE CAST(order_delivered_customer_date AS DATE) > CAST(order_estimated_delivery_date AS DATE)
    ) * 100.0 / NULLIF(COUNT(*), 0),
    1
  ) AS late_delivered_order_rate_PERCENT,
  COUNT(*) FILTER (
    WHERE order_delivered_customer_date IS NULL
       OR order_estimated_delivery_date IS NULL
  ) AS missing_delivery_dates_count
FROM uploads.main.olist_orders_dataset
WHERE order_status = 'delivered'
  AND order_purchase_timestamp >= TIMESTAMP '2017-01-01 00:00:00'
  AND order_purchase_timestamp < TIMESTAMP '2018-01-01 00:00:00'
```

### Q12: What percentage of delivered orders were late in 2018?

- Time: 2026-10-31T17:24:26+0530
- Chat: https://app.getdot.ai/?c=fd57050c-812b-461f-8bb4-4490d4001cf4
- Classification: answered
- Basis, population: yes - "of delivered orders placed in 2018"
- Basis, period: yes - "placed in 2018"
- Basis, definition: yes - "meaning they arrived after the estimated delivery date . ... arrivals on the estimated date count as on time"

**Answer**

```text
7.7% of delivered orders placed in 2018 were late, meaning they arrived after the estimated delivery date .

This excludes 6 orders with missing delivery timestamps ; arrivals on the estimated date count as on time.
```

**Data**

```text
total_delivered_orders, delivered_orders_with_missing_timestamps, late_delivered_orders, late_rate_known_timestamps_PERCENT, late_rate_all_delivered_PERCENT
52783, 6, 4078, 7.7, None
```

**SQL**

```sql
WITH cte_delivered_cohort AS (
    SELECT
        order_id,
        order_delivered_customer_date,
        order_estimated_delivery_date,
        
        CASE 
            WHEN order_delivered_customer_date IS NULL OR order_estimated_delivery_date IS NULL THEN 1 
            ELSE 0 
        END AS is_missing_timestamp,
        
        CASE 
            WHEN order_delivered_customer_date IS NOT NULL 
                 AND order_estimated_delivery_date IS NOT NULL 
                 AND CAST(order_delivered_customer_date AS DATE) > CAST(order_estimated_delivery_date AS DATE) 
            THEN 1 
            ELSE 0 
        END AS is_late
    FROM uploads.main.olist_orders_dataset
    WHERE order_status = 'delivered'
      AND order_purchase_timestamp >= TIMESTAMP '2018-01-01 00:00:00'
      AND order_purchase_timestamp < TIMESTAMP '2019-01-01 00:00:00'
)
SELECT
    COUNT(*) AS total_delivered_orders,
    SUM(is_missing_timestamp) AS delivered_orders_with_missing_timestamps,
    SUM(is_late) AS late_delivered_orders,
    
    ROUND(
        SUM(is_late) * 100.0 / NULLIF(COUNT(*) - SUM(is_missing_timestamp), 0),
        1
    ) AS late_rate_known_timestamps_PERCENT,
    
    CASE 
        WHEN SUM(is_missing_timestamp) = 0 THEN
            ROUND(SUM(is_late) * 100.0 / NULLIF(COUNT(*), 0), 1)
        ELSE NULL 
    END AS late_rate_all_delivered_PERCENT
FROM cte_delivered_cohort
```
