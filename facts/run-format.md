# Run file format

The format of `runs/<piece>-run.md`. The `dot-runner` subagent writes it. Check 16 ("Every finding comes from this dataset's run") and `mark_run.py` both read it, so it is fixed: same headings, same labels, same order. Change it here first, with a line in CLAUDE.md's change log, then change the writer and the readers.

## Structure

A run file is one H1, then for each batch a conditions block followed by one entry per question.

```
# <piece> run

## Batch <n>: conditions
...

### Q<k>: <question as asked>
...

### Q<k+1>: <question as asked>
...

## Batch <n+1>: conditions
...
```

- `<n>` numbers batches from 1 within the piece ([runs/README.md#batches](../runs/README.md#batches)).
- `<k>` numbers questions from 1 across the whole piece, in the research file's order. It doesn't restart with each batch.
- Entries are only ever appended. An earlier entry is never edited.
- Rival definitions go into the truth spec before the run, not after. If a question has a plausible second reading (all orders vs delivered; with or without shipping), its row is in `specs/<piece>-truth.json` before the first question is asked. A rival added after seeing Dot's answer must say so in the spec.

## Conditions block, once per batch

```
## Batch <n>: conditions

- Date: <output of date>
- Workspace: <as get_catalog reports it>
- Tables: <as get_catalog reports them>
- Mode: not selectable via MCP. Screenshot: runs/screenshots/<piece>-batch-<n>-mode.png
- Environment: not observable via MCP. Screenshot: runs/screenshots/<piece>-batch-<n>-environment.png
- Context notes: not observable via MCP. Screenshot: runs/screenshots/<piece>-batch-<n>-notes.png
- Credits before: not observable via MCP. Screenshot: runs/screenshots/<piece>-batch-<n>-credits-before.png
- Credits after: not observable via MCP. Screenshot: runs/screenshots/<piece>-batch-<n>-credits-after.png
- Model: not observable via MCP
```

All five screenshot paths are always listed, per [runs/README.md#screenshots](../runs/README.md#screenshots). The human records the values from Dot's UI; `dot-runner` never writes them.

## Entry, once per question

One H3 per question. The heading is `Q<k>:` followed by the question exactly as asked. Then these lines and blocks, in this order:

| Part | Format | Rule |
|---|---|---|
| Time | `- Time: <output of date +%Y-%m-%dT%H:%M:%S%z>` | Taken right after the answer returns |
| Chat | `- Chat: <Dot "Open in Dot" link>` | |
| Classification | `- Classification: <value>` | One of `answered`, `asked back`, `refused with offer`, `needed an analyst`. `call failed` if the call errored |
| Basis | Three lines: `- Basis, population: yes` or `no`, then the same for `period` and `definition` | After `yes`, a dash and the words quoted from the answer text. Only the text counts, not the SQL |
| Answer | `**Answer**` then a fenced `text` block | The full answer text, verbatim, character for character. On a failed call, the error text |
| Data | `**Data**` then a fenced `text` block | The data preview verbatim, if returned. Otherwise `**Data**: none returned` |
| SQL | `**SQL**` then a fenced `sql` block | Verbatim, if returned. Otherwise `**SQL**: none returned` |

A reader parses the labels before the colon and the first word after it. Nothing else goes in an entry: no interpretation, no expected value, no right or wrong. Marking is `mark_run.py`'s job.

## Worked example

This is the real question and answer from check 1 of the [smoke test](../runs/smoke-test.md), 31 October 2026, written in this format. Two things differ from a real run:

- **No screenshots were taken.** The smoke test predates the scheme, so the five paths are shown but the files don't exist.
- **The time is approximate.** The smoke test predates dot-runner's clock and recorded only "about 03:45 IST". A real run copies the output of `date`.

````
# smoke-test run

## Batch 1: conditions

- Date: 2026-10-31, about 03:45 IST
- Workspace: aiinterviewagents.com
- Tables: uploads.main.olist_orders_dataset; uploads.main.olist_order_items_dataset
- Mode: not selectable via MCP. Screenshot: runs/screenshots/smoke-test-batch-1-mode.png
- Environment: not observable via MCP. Screenshot: runs/screenshots/smoke-test-batch-1-environment.png
- Context notes: not observable via MCP. Screenshot: runs/screenshots/smoke-test-batch-1-notes.png
- Credits before: not observable via MCP. Screenshot: runs/screenshots/smoke-test-batch-1-credits-before.png
- Credits after: not observable via MCP. Screenshot: runs/screenshots/smoke-test-batch-1-credits-after.png
- Model: not observable via MCP

### Q1: what is our average order value?

- Time: 2026-10-31, about 03:45 IST
- Chat: https://app.getdot.ai/?c=c3dfb706-90fe-40a7-8651-af37e09eb083
- Classification: answered
- Basis, population: yes - "based on delivered orders"
- Basis, period: yes - "covering September 2016–October 2018"
- Basis, definition: yes - "excluding shipping"

**Answer**

```text
Our average order value is BRL 137.04, based on delivered orders and excluding shipping .

This uses the full uploaded dataset, covering September 2016–October 2018, not current sales .
```

**Data**

```text
average_order_value_brl, merchandise_revenue_brl, delivered_order_count, min_purchase_timestamp, max_purchase_timestamp, delivered_orders_missing_items_count, eligible_item_rows_null_price_count
137.04, 13221498.11, 96478, 2016-09-04 21:15:19, 2018-10-17 17:30:18, 0, 0
```

**SQL**

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
````

The answer text keeps Dot's stray space before each full stop. Verbatim means verbatim.
