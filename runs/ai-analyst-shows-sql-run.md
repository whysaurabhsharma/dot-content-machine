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
- Credits after: to be recorded by hand after the last answer
- Model: not observable via MCP

**Catalog check, read through the MCP before the first question** (`get_catalog`, query "delivered in year delivery date", 31 October 2026, about 17:05 IST). Definitions returned: two, "Olist revenue, order value, basket size, cancellation and shipping metrics" and "Olist dataset currency and monetary formatting". No definition named for "delivered in <year>" or for a delivery-date reading. The tool truncates definition text: the metrics note's returned text ends "Unless explicitly requested otherwise, report a pur…", so whether it already sets a default date basis is not observable via MCP. Whether `get_catalog` lists notes that are switched off is also not observable: the off note "About aiinterviewagents.com" was not returned, which fits either reading.
