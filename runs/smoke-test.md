# Smoke test — 31 October 2026

Run from Claude Code with the ask_dot MCP connected (`/mcp`: "Authentication successful. Connected to ask_dot."). Saved as each check ran. Rule: nothing guessed; where something can't be observed, it says "not observable via MCP".

## Check 1 — ask_dot: "what is our average order value?"

- Tool: `mcp__ask_dot__ask_dot`, question sent exactly: `what is our average order value?`
- Chat ID: `c3dfb706-90fe-40a7-8651-af37e09eb083` — [Open in Dot](https://app.getdot.ai/?c=c3dfb706-90fe-40a7-8651-af37e09eb083)
- Read with `get_result` (wait_seconds 90); answer returned on the first call.

**Answer, verbatim (text part):**

> Our average order value is BRL 137.04, based on delivered orders and excluding shipping .
>
> This uses the full uploaded dataset, covering September 2016–October 2018, not current sales .

(The stray space before each full stop is in Dot's output.)

**Data row returned, verbatim:**

```
average_order_value_brl, merchandise_revenue_brl, delivered_order_count, min_purchase_timestamp, max_purchase_timestamp, delivered_orders_missing_items_count, eligible_item_rows_null_price_count
137.04, 13221498.11, 96478, 2016-09-04 21:15:19, 2018-10-17 17:30:18, 0, 0
```

**SQL returned, verbatim:**

```sql
WITH dataset_coverage AS (
  SELECT
    MIN(order_purchase_timestamp) AS min_purchase_timestamp,
    MAX(order_purchase_timestamp) AS max_purchase_timestamp
  FROM uploads.main.olist_orders_dataset
),

items_by_order AS (
  SELECT
    order_id,
    SUM(price) AS merchandise_brl,
    COUNT(price) AS count_non_null_price_items,
    COUNT(*) AS total_items,
    COUNT(*) - COUNT(price) AS count_null_price_items
  FROM uploads.main.olist_order_items_dataset
  GROUP BY order_id
),

delivered_orders_summary AS (
  SELECT
    o.order_id,
    i.merchandise_brl,
    i.count_null_price_items,
    CASE WHEN i.order_id IS NULL THEN 1 ELSE 0 END AS is_missing_items
  FROM uploads.main.olist_orders_dataset o
  LEFT JOIN items_by_order i ON o.order_id = i.order_id
  WHERE o.order_status = 'delivered'
)

SELECT
  ROUND(SUM(COALESCE(d.merchandise_brl, 0)) / NULLIF(COUNT(d.order_id), 0), 2) AS average_order_value_brl,
  ROUND(SUM(COALESCE(d.merchandise_brl, 0)), 2) AS merchandise_revenue_brl,
  COUNT(d.order_id) AS delivered_order_count,
  c.min_purchase_timestamp,
  c.max_purchase_timestamp,
  SUM(d.is_missing_items) AS delivered_orders_missing_items_count,
  COALESCE(SUM(d.count_null_price_items), 0) AS eligible_item_rows_null_price_count
FROM delivered_orders_summary d
CROSS JOIN dataset_coverage c
GROUP BY
  c.min_purchase_timestamp,
  c.max_purchase_timestamp
```

**Did it state its basis?** Yes. The text names three: delivered orders only; shipping excluded; full uploaded dataset, September 2016–October 2018, "not current sales". The SQL matches: `order_status = 'delivered'`, `SUM(price)` from order items (no `freight_value`), whole table. It also returned the denominator (96,478 delivered orders) and two data-quality counts (0 orders missing items, 0 null prices).

Not stated in the text: that the date range shown is the range of *all* orders' purchase timestamps (the `dataset_coverage` CTE has no status filter), not of delivered orders. Whether a metric-definitions context note drove the "delivered, excluding shipping" scoping: not observable via MCP (the answer doesn't cite a note).

## Check 2 — data/ahrefs/keywords.csv

File read in full (21 data rows). Counted by script (`csv.DictReader`, filter `is_buyer_query == 'yes'`), not by eye.

- **US volume for "ai data analyst": 700** (global 2.0K, KD 22, read 2026-10-27).
- Buyer rows: 18. US volumes across them: `not indexed` ×13, `10` ×2, `1.2K` ×1, `700` ×1, `150` ×1.
- **13 of the 18 buyer queries have no volume.** All 13 read `not indexed` in both US and global. Per `data/ahrefs/README.md`, `not indexed` is what Ahrefs displayed and is not a recorded zero.

The 13: how to evaluate ai data analyst accuracy; ai data analyst accuracy; reduce ad hoc data requests; ad hoc data request process; ai data analyst cost per question; ai data analyst vs bi tool; semantic layer ai analyst; replace data analyst with ai; how to measure data team productivity; data team slack requests; ai analyst data warehouse; natural language query data; ai bi tool comparison.

Source date: Ahrefs, 27–28 October 2026 (frozen snapshot; Ahrefs access ended 31 October 2026).

## Check 3 — web search: "how do I evaluate an AI data analyst's accuracy?"

Tool: Claude Code `WebSearch` (standard mode, US-only). This is not Google; its order is not a Google ranking, and Ahrefs/SERP position is not observable from it.

Results in the order returned (10 links). The top five, as returned:

1. How to Eval an AI Data Analyst: Framework + Open Benchmarks — https://querio.ai/articles/evaluate-ai-data-analyst-framework-open-benchmarks
2. ai analytics databench (Hex) — https://hex.tech/resources/ai-analytics-databench/
3. Tableau blog, 5 August 2025 (Italian locale) — https://www.tableau.com/it-it/blog/agentic-accuracy-technical-strategies-validation-methods
4. Same Tableau post (fr-ca locale) — https://www.tableau.com/fr-ca/blog/agentic-accuracy-technical-strategies-validation-methods
5. Same Tableau post (pt-br locale) — https://www.tableau.com/pt-br/blog/agentic-accuracy-technical-strategies-validation-methods

Results 3–8 are six locale copies of one Tableau post. De-duplicated, the 10 links are **four distinct pages**:

1. querio.ai — https://querio.ai/articles/evaluate-ai-data-analyst-framework-open-benchmarks
2. Hex — https://hex.tech/resources/ai-analytics-databench/
3. Tableau — https://www.tableau.com/blog/agentic-accuracy-technical-strategies-validation-methods
4. InfiniSynapse, "How to Evaluate AI Data Analyst Tools: Buyer Scorecard" — https://infinisynapse.com/en/blog/how-to-evaluate-ai-data-analyst (also a zh copy)

A fifth distinct page did not appear in this result set. Pages were not opened; titles are as the search tool returned them.

## Check 4 — what the ask_dot MCP exposes

**Tools (10):** `ask_dot`, `get_result`, `get_catalog`, `show_app`, `view_app`, `build_app`, `wait`, plus three the server marks widget-only: `answer_progress`, `export_table`, `publish_app` ("Never call this yourself").

| Question | Observed |
|---|---|
| Can a mode (Economy / Balanced) be set? | **No.** No tool's parameter schema has a mode, model or effort field. `ask_dot` takes only `question`, `chat_id`, `asked_from`. Which mode the account is in: not observable via MCP. |
| Does the response name the model? | **No.** The check 1 response has text, SQL, data, stats, CSV link, chat link. No model named. Not observable via MCP. |
| Does the response name credits used? | **No.** No credit count in the response; no tool returns a balance. Not observable via MCP. Rule 15 readings must be taken in the Dot UI. |
| Workspace | `get_catalog` header: "Dot Data Catalog: aiinterviewagents.com". One connection: `data/aiinterviewagents.com/uploads.db` (duckdb), 2 tables: `uploads.main.olist_orders_dataset` (8 cols, 99.4K rows), `uploads.main.olist_order_items_dataset` (7 cols, 112.7K rows). One app: Sample Executive Dashboard. Environment: links point to app.getdot.ai. |
| Context notes | `get_catalog("average order value")` lists two definitions in the workspace: "Olist dataset currency and monetary formatting" and "Olist revenue, order value, basket size, cancellation and shipping metrics" (text truncated by the tool). Their existence is observable. **Whether they were active for, or used by, the check 1 answer: not observable via MCP.** The answer doesn't cite them. Its BRL label and delivered-only/no-shipping scope are consistent with them, but that's inference, not observation. |

Other observations:
- `get_catalog` also lists five earlier "Average Order Value" chats (23 and 27 October 2026), so this question has prior runs in the same workspace to compare against.
- Prior chat IDs: 37b5a886…, e863ec21…, 126f5e3b…, 99f86fcb…, 3a6b9a04….

## Conditions (rule 17)

- Account/workspace: aiinterviewagents.com (as `get_catalog` reports it)
- Environment: app.getdot.ai via ask_dot MCP, from Claude Code
- Mode: not observable via MCP
- Context notes active: not observable via MCP (two exist; see check 4)
- Credits before/after: not read (not observable via MCP; needs the Dot UI)
- Date: 31 October 2026, ~03:45 IST
