# Setting up a Dot workspace to match the specs

The pieces' test questions and truth specs assume a Dot workspace with two Olist tables and two context notes. A new workspace has neither. Set it up as below before any run, then verify it. If your workspace differs, the run measures something else, and the specs' expected answers no longer apply.

## 1. Upload the two tables

From the Olist dataset (https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce; the same files go in `data/olist/` in this repo, see `SETUP.md`), upload to Dot as CSV data sources:

| File | Table name the specs and notes use | Rows | Columns |
|---|---|---|---|
| `olist_orders_dataset.csv` | `uploads.main.olist_orders_dataset` | 99,441 | order_id, customer_id, order_status, order_purchase_timestamp, order_approved_at, order_delivered_carrier_date, order_delivered_customer_date, order_estimated_delivery_date |
| `olist_order_items_dataset.csv` | `uploads.main.olist_order_items_dataset` | 112,650 | order_id, order_item_id, product_id, seller_id, shipping_limit_date, price, freight_value |

The table names matter: the metrics note below names them. If Dot names your uploads differently, edit the note's first paragraph to match, and record the change in your run file's conditions.

## 2. Add the two context notes (Model → Notes)

Turn both **on**. Turn off any other note, or record it as on in each batch's conditions block (rule 17): another active note can change answers.

### Note 1: "Olist revenue, order value, basket size, cancellation and shipping metrics"

Full text, copied from Model → Notes in the original workspace on 31 October 2026 (`runs/ai-analyst-shows-sql-run.md`, "The metrics note, verbatim"):

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

### Note 2: "Olist dataset currency and monetary formatting"

**Its full text is not recorded in this repo.** The note existed and was on in every run (it appears in `get_catalog` results and every conditions block), but nobody copied its text. What the pieces rely on: monetary values are BRL (the metrics note says so too). Until the text is recovered from the original workspace, write a one-line note: "All monetary values in the Olist tables are Brazilian reais (BRL). Report amounts as BRL with thousands separators." and record in each batch's conditions that this note is a reconstruction.

## 3. Verify the workspace (before the first run)

1. **Tables and notes exist.** Ask Claude Code to call `get_catalog` with the query "olist orders items delivered". Expected: both tables listed, and both notes as definitions. The tool truncates note text, so it shows the notes exist, not their content.
2. **A known answer.** Ask Dot, in a fresh chat: "How many orders were delivered in 2017?" Expected: **43,428**, using purchase date (piece A's run, Q1, and figures row MR-Q1). Any other number means a table, a note or the date basis differs; find out why before going on.
3. **Record the conditions** in Dot's own UI, as `runs/README.md#screenshots` says: mode, environment, which notes are on, credits before. None of these is visible through the MCP.

## 4. What not to change

- Don't add a note that defines "delivered in <year>": pieces A and F rest on Dot choosing a date basis without one.
- Don't rename columns. The truth specs (`specs/*-truth.json`) compute expected answers from the raw CSVs by these column names.
