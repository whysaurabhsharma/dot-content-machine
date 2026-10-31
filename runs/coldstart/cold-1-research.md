# Research: cold-1

**Question (caller's words):** "Finance and sales report different revenue. How do I find out why and stop it recurring?"
**Piece slug:** cold-1 (bank #29, format research, `practice: false`)
**Date:** 1 November 2026

Note: `runs/cold-1-piece.json` records bank #29 as "two dashboards show different numbers". The caller's wording is used here.

## 1. The gap chain

- **Buyer asks:** "Finance and sales report different revenue. How do I find out why and stop it recurring?"
- **What they find today:** advice only. The three pages read (monday.com, OWOX, MerchantSpring) list causes: gross versus net, recognition timing, income outside sales, what counts as a deal, pull time. None shows a reader's own two numbers being reconciled. OWOX has a worked example on its own demo dataset with SQL, but it is a vendor demo about pipeline more than revenue, and is mainly advice.
- **Cited in AI answers:** not measured. `measure/citations.md` tracks three other buyer questions (evaluating accuracy, what changes, cost and fit) and its latest reading is 27 October 2026, Perplexity free app. This question is not among them. The file holds citation-marker counts only, not the answers in full.
- **The gap:** advice only.
- **What only Dot can show:** Dot's answer to "why do these two numbers differ" on a dataset, with the SQL that reveals each definition, and whether a stored definition makes the next answer use the same one (A5, an assumption). Facts O3/O4 show one such note on Olist.

## 2. The words buyers type

Ahrefs, 27-28 October 2026. No phrasing of the question is in the file, so none is offered as a headline phrase with a volume. Nearest rows:

| Phrase | volume_us | volume_global | difficulty |
|---|---|---|---|
| single source of truth metrics | not indexed | not indexed | not measured |
| metric definitions | 20 | not measured | 13 |
| semantic layer | 2.4K | not measured | 24 |

Not in the file, so "not measured": "finance and sales report different revenue", "why do sales and finance numbers not match", "reconcile sales and finance revenue". Search Console has no related row (rows are Power BI, conversational analytics and similar; nothing on revenue mismatch). Tie-breaking on volume is weak here: all nearby phrases are small or not indexed.

## 3. The run

- **Stage:** Playbook stage covering definitions and the semantic layer (name to be confirmed against the Playbook; I did not read it in this task).
- **Data:** Olist Brazilian e-commerce dataset (orders, order_items, order_payments), as used in earlier runs. Licence recorded as CC BY-NC-SA 4.0 (A10), never verified at source; L1-L4 are decisions, not resolutions, and L4 covers only piece F. A new decision is needed for cold-1.
- **Method:** model "sales" as price on all orders by purchase date, and "finance" as delivered orders by delivery date. Ask Dot for each, the gap, and what drives it, then ask the headline question in fresh chats to test recurrence under a stored definition note.
- **Conditions to screenshot per batch** (runs/README.md#screenshots): mode, credits before and after, environment, notes. Cost per answer, if given, as a credits range with dollars (A2, assumption).
- **Needs:** order_payments loaded into Dot's workspace; unverified.

## 4. Sources rows

See the CSV in section 8.

## 5. Stop conditions

Evidence partly exists (OWOX worked example) but is a pipeline demo on a vendor dataset. Not stopped. Dot's data must hold order_items and delivery dates; if the workspace lacks them, stop.

## 6. Verdict

**PIECE IF** the Dot workspace holds Olist orders, order_items and delivery timestamps, and the licence decision for cold-1 is made.

## 7. Test questions

Definitions: SALES = sum of order_items.price, all order statuses, grouped by order_purchase_timestamp. FINANCE = sum of order_items.price, order_status = 'delivered', grouped by order_delivered_customer_date. Year 2017.

- **T1.** "What was total revenue in 2017, counting the item price of every order by the date it was purchased?" Table: orders joined to order_items; filter purchase year 2017, no status filter; formula sum(price). Figure: SALES, BRL, one year.
- **T2.** "What was total revenue in 2017, counting only delivered orders by the date they were delivered?" Filter status delivered, delivery year 2017; sum(price). Figure: FINANCE, BRL, one year.
- **T3.** "What is the difference between those two 2017 revenue figures?" Follow-up of T2 in the same chat as T1 and T2 is not possible with one number each, so ask it as a fresh question carrying both definitions. Figure: SALES minus FINANCE, BRL, 2017.
- **T4.** "How much item value was on orders purchased in 2017 that were cancelled or never delivered?" Filter purchase year 2017, status not delivered; sum(price). Figure: BRL.
- **T5.** "How much item value was on orders purchased in 2017 but delivered in 2018?" Filter purchase 2017, delivery 2018; sum(price). Figure: BRL.
- **T6.** Follow-up of T5: "And how much of that was freight rather than item price?" Sum freight_value on the T5 population. Figure: BRL.
- **T7.** "In which 2017 month was the gap between purchase-date revenue and delivery-date revenue largest, and what was the gap?" Monthly SALES minus monthly FINANCE; one month and its one gap in BRL.
- **T8.** "What was our revenue in 2017?" Run after a context note defining revenue as delivered orders is active. Figure: revenue 2017, BRL, under the note's definition. Asked in a fresh chat.
- **T9.** Repeat of T8 (fresh chat, worded identically).
- **T10.** Repeat of T8 (fresh chat, worded identically).

T8-T10 test recurrence only; no remedy claim beyond what they show (rule 19). Figures are named, not valued (rule 2).

## 8. Sources as CSV

```csv
source,url_or_tool,what_it_showed,date
Search Console rows,data/ahrefs/search-console-queries.csv,"11 rows; none relates to revenue mismatch (nearest: conversational analytics, 384 impressions, position 25.8)",1 Nov 2026 (file read)
Keywords Explorer rows,data/ahrefs/keywords.csv,"semantic layer 2.4K US difficulty 24; metric definitions 20 US difficulty 13; single source of truth metrics not indexed; question phrasings not in file = not measured (Ahrefs, 27-28 October 2026)",1 Nov 2026 (file read)
AI answers,measure/citations.md,"Question not tracked: not measured. File holds marker counts only; latest reading 27 Oct 2026 Perplexity free app on three other questions",1 Nov 2026
Plan,PLAN.md,"Read; no section names cold-1 or bank #29; no run needs set",1 Nov 2026
Search order,WebSearch query 'finance and sales report different revenue numbers why',"Order is WebSearch's, not Google's. Results 1-3 distinct pages used: monday.com, OWOX, MerchantSpring (a Harvard-domain clone of the monday.com title skipped as a duplicate)",1 Nov 2026
Ranking page 1,https://monday.com/blog/crm-and-sales/revenue-vs-sales/,"'Revenue vs sales: how to track both metrics accurately in 2026'; opens 'Your sales team just closed a $100K deal. Finance says revenue for the quarter is only up $8K.'; monday.com, 13 April 2026; advice; vendor-owned",1 Nov 2026
Ranking page 2,https://www.owox.com/blog/articles/single-source-of-truth-pipeline/,"'Why Sales, Marketing and Finance Report Different Pipeline Numbers'; opens 'Sales, marketing and finance rarely report the same pipeline or revenue number, and usually none of them is wrong.'; OWOX, updated 10 Oct 2026; mainly advice with a vendor demo example; vendor-owned",1 Nov 2026
Ranking page 3,https://help.merchantspring.io/en/why-do-sales-and-profitability-reports-show-different-numbers,"'Why do Sales and Profitability reports show different numbers?'; opens by saying the reports serve different purposes and use different data sources; MerchantSpring; no date; advice; documentation",1 Nov 2026
Facts and dataset,facts/dot-facts.md,"A5, A10 (Olist, CC BY-NC-SA 4.0, unverified at source), O3, L1-L4",1 Nov 2026
```
