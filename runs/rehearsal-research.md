# RESEARCH: "How do we stop different teams getting different numbers for the same metric?"

Piece slug: `rehearsal`. Date: 31 October 2026.

Note on the slug: rule 4 bars findings from the rehearsal (23-24 October) from appearing in a piece. This file has no rehearsal findings in it. It uses only the five inputs fetched today.

## 1. The gap chain

- **What the buyer asks:** "How do we stop different teams getting different numbers for the same metric?"
- **What they find today:** mostly *advice*. Acceldata (3 Jan 2026) is advice only. Badang Labs (15 Apr 2026) is advice, plus an unsourced "3-5 hours per month" claim. OWOX (updated 14 Oct 2026) is mostly advice, with *some evidence*: SQL on its own synthetic B2B demo dataset showed one metric moving with the counting rule (webinar credit about $59k vs about $489k; MQL-to-SQL 21.7%, 19.3%, 24.1%). None of the three runs an AI analyst, and none shows whether an AI analyst gives different teams the same number.
- **Who gets cited in AI answers:** not measured. `measure/citations.md` tracks three Day 0 questions (27 Oct, Perplexity free app): evaluating accuracy, what changes, cost and fit. This question isn't one of them. The file holds citation-marker counts only, not the answers in full. I did not borrow counts from another question.
- **The gap:** advice only. One partial evidence page (OWOX) covers marketing attribution on synthetic data, not an AI analyst and not wording differences between teams.
- **What only Dot can show:** the same Olist metric asked in separate fresh chats, worded as different teams would word it, answered from one stored definition (the note "Olist revenue, order value, basket size, cancellation and shipping metrics", facts O3). Then each answer is compared with figures computed from the raw CSVs, and with the same metric under the other plausible definition (all orders vs delivered). This uses Dot's own feature (context notes) and data (Olist tables in the workspace).

## 2. The words buyers type

The inputs hold few buyer phrases for this question. Ahrefs, 27-28 October 2026:

| Phrase | volume_us | volume_global | difficulty |
|---|---|---|---|
| semantic layer | 2.4K | not measured | 24 |
| metric definitions | 20 | not measured | 13 |
| single source of truth metrics | not indexed | not indexed | not measured |
| semantic layer ai analyst | not indexed | not indexed | not measured |

Also in the inputs, from the ranking pages: "conflicting metrics across teams" (Acceldata title), "same metric" (OWOX title). Neither is in Keywords Explorer, so volume is not measured. "semantic layer" and "metric definitions" are marked `is_buyer_query = no` in the file. The exact buyer question is not in the file.

Search Console: no row in `search-console-queries.csv` relates to this question (the nearest, "decision intelligence platform", is not about it). Nothing is claimed from it. The file shows no date.

## 3. The run

- **Playbook stage:** the stage that fixes definitions and context for the analyst. The inputs I read don't name the Playbook's stages. The OUTLINE stage must confirm the exact stage name and link from the Playbook.
- **Data:** `uploads.main.olist_orders_dataset` (99.4K rows) and `uploads.main.olist_order_items_dataset` (112.7K rows), per facts/dot-mcp.md. Ground truth is computed from `data/olist/*.csv`.
- **Dataset and licence (rule 9):** Olist Brazilian E-Commerce, https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce. Licence CC BY-NC-SA 4.0 (data/README.md). Rick confirmed any realistic dataset is fine for the trial (facts A10). The licence matters again before commercial publication.
- **What to run:** for each of three metrics (item revenue, average order value, orders count), ask the same metric in a fresh chat three times, each worded as a different team would word it (finance, operations, marketing). Compare the answers with each other and with ground truth under both definitions (delivered only; all orders). Keep every chat fresh, so no answer can see another.
- **Two batches (decided 31 October 2026):** the piece claims that one stored definition causes the agreement, so the note must be tested off as well as on.
  - **Batch 1:** the Olist metrics note ("Olist revenue, order value, basket size, cancellation and shipping metrics") **on**. All eleven test questions, T01–T11.
  - **Batch 2:** the same note **off**. The same eleven questions, worded identically, in fresh chats.
  - The human switches the note in Dot's UI between batches. Each batch's `notes` screenshot must show the note's state.
  - Comparison is item by item across batches (rule 18): T01 in batch 1 against T01 in batch 2, and so on.
- **Mode:** the human sets and screenshots the mode. The MCP can't set or read mode, credits, environment or notes (facts/dot-mcp.md). Save each batch's five screenshots per `runs/README.md#screenshots`: `runs/screenshots/rehearsal-batch-<n>-{mode,credits-before,credits-after,environment,notes}.png`. The `notes` screenshot must show whether the Olist metrics note is on.
- **Numbers it must produce:** per question, Dot's value, ground truth under the delivered-only definition, ground truth under the all-orders definition, and which of the two (if either) Dot's value matches. Also, per metric, whether the three team phrasings agree with each other, judged item by item (rule 18). Cost per answer as a credits range with dollars alongside, labelled Assumption (A2), with the caveat that the same question can take different paths (rule 10). Credits come from the before and after Billing screenshots.
- **Conditions to record (rule 17):** account aiinterviewagents.com, environment, mode, active notes.

## 4. Sources rows

| Source | URL or tool | What it showed | Date |
|---|---|---|---|
| Search Console rows | data/ahrefs/search-console-queries.csv | 12 rows (counted by script); none related to the question; file shows no date | read 31 Oct 2026 |
| Keywords Explorer | data/ahrefs/keywords.csv | semantic layer 2.4K US, difficulty 24; metric definitions 20 US, difficulty 13; single source of truth metrics and semantic layer ai analyst not indexed | Ahrefs, 27-28 October 2026 |
| AI answers | measure/citations.md | Question not tracked; "not measured". File holds marker counts only | read 31 Oct 2026 |
| Dataset | data/README.md | Olist, CC BY-NC-SA 4.0 | read 31 Oct 2026 |
| Workspace | facts/dot-mcp.md, facts/dot-facts.md | Two Olist tables; note in O3; mode, credits, environment, notes not observable via MCP | read 31 Oct 2026 |
| WebSearch (order is WebSearch's, not Google's) | query "how to stop different teams getting different numbers for the same metric" | 17 results; 1st Acceldata, then four fitgap pages, fog.zeo.org, StoryPointLab, Notion page, Badang Labs, ... OWOX 15th, Hänninen 16th | run 31 Oct 2026 |
| Page 1 | https://acceldata.io/blog/how-to-fix-conflicting-metrics-across-teams-a-practical-guide | "How to Fix Conflicting Metrics Across Teams: A Practical Guide", Acceldata (vendor), by Aryan Sharma, 3 Jan 2026. Opens "Many organizations struggle with conflicting analytics reports". Advice only | fetched 31 Oct 2026 |
| Failed fetches | us.fitgap.com (standardizing order fields; establish governance; quality targets) all HTTP 410; fog.zeo.org HTTP 404; datamasterclass Notion page returned only "Notion" | Not read, not described | 31 Oct 2026 |
| Page 2 | https://website-2b5.pages.dev/blog/why-team-gets-different-answers/ | "Why Your Team Gets 3 Different Answers to the Same Question", Badang Labs, 15 Apr 2026. Opens "Ask your finance team 'what was revenue last month?'". Advice; "3-5 hours per month" is anecdotal | fetched 31 Oct 2026 |
| Page 3 | https://www.owox.com/blog/articles/analytics-sales-marketing-alignment.md | "How to align marketing, sales and analytics teams on the same metrics", OWOX blog (vendor), by Ievgen Krasovytskyi, updated 14 Oct 2026. Opens "Marketing, sales and analytics agree on the same metrics when each metric has one written definition and one owner." Mostly advice, some evidence (SQL on synthetic demo data) | fetched 31 Oct 2026 |

Limits of the page input:

- WebSearch is not Google; the order is WebSearch's, on 31 October 2026.
- Of WebSearch's top six results, four failed to load: three fitgap pages returned HTTP 410 and fog.zeo.org returned HTTP 404. The fourth fitgap page in the top six was not tried. Result 7 (StoryPointLab) was not tried, and result 8 (a Notion page) came back empty.
- So the three pages read are WebSearch's 1st (Acceldata), 9th (Badang Labs) and 15th (OWOX). They are not the top three ranking pages, and nothing in this file should describe them as such.
- Racklify was not tried. Hänninen (16th, Feb 2022, anecdote plus advice) was read but not used as a ranked page.
- The fetch tool summarises pages, so "read in full" holds only to that extent.

## 5. Stop conditions

- Evidence already exists? Partly (OWOX), but on marketing attribution with synthetic data and no AI analyst. Not the same claim. No stop.
- Only Dot's data could show it and Dot doesn't have it? Dot has the Olist tables and the note. No stop.
- Limit: whether the note is on for a chat is not observable via MCP, so a human screenshot is required. Comparing "note on" with "note off" needs the human to switch the note and screenshot it.

## 6. Verdict

**PIECE IF: a human screenshots the five conditions per batch (including that the Olist metrics note is on, and toggles it off for a comparison batch if the piece is to claim the note causes the agreement).**

**Contradicted by evidence, 31 October 2026.** Batch 2, with the note off, returned the same figure as batch 1 on every question it answered. The claim that one stored definition causes the agreement is not supported. See runs/rehearsal-run.md, "Batch 2: observed findings".

**Decision, 31 October 2026 (human):** the comparison batch is run. The piece's claim is that one stored definition causes the agreement, so there are two batches: batch 1 with the note on, batch 2 with it off, the same eleven questions (section 3).

## 7. Test questions

Each question is asked in a fresh chat, in both batches.

**T02 reworded, 31 October 2026 (human):** the agent's wording was "Ops here: what is the total value of items we shipped?". `shipped` is a real Olist order status, so a literal reading by Dot would be correct, and the test would measure our wording, not Dot. It now reads "Ops here: what is the total value of items that reached customers?": an ops phrasing for the same delivered-orders figure, naming no status. Ground truth for each is computed later from the raw CSVs by `scripts/ground_truth_from_spec.py`; no values here. Definitions follow specs/piece-1-truth.json (orders table `o`, items table `i`, join on order_id).

| ID | Question, as asked | Definition it depends on | Figure it must produce |
|---|---|---|---|
| T01 | "Finance here: what was our total revenue?" | `i` joined to `o`; sum of `price`; filter `order_status == 'delivered'` (the note's definition) | Revenue, BRL, one value, delivered item rows |
| T02 | "Ops here: what is the total value of items that reached customers?" | Same table, formula, filter as T01 | Revenue, BRL, one value, delivered item rows |
| T03 | "Marketing here: how much did customers spend with us in total?" | Same table, formula, filter as T01 | Revenue, BRL, one value, delivered item rows |
| T04 | "What is the total item price across all orders, whatever their status?" | `i` only; sum of `price`; no filter | Sum of price, BRL, all item rows (the competing definition) |
| T05 | "Finance here: what is our average order value?" | `i` joined to `o`; per-`order_id` sum of `price`, then mean; filter `order_status == 'delivered'` | Average order value, BRL, per order, delivered orders with items |
| T06 | "Sales here: what does a typical order bring in?" | Same as T05 | Average order value, BRL, per order, delivered orders with items |
| T07 | "Marketing here: what is the average basket value per order?" | Same as T05 | Average order value, BRL, per order, delivered orders with items |
| T08 | "What is the average order value across all orders with items, whatever their status?" | `i` only; per-`order_id` sum of `price`, then mean; no filter | Average order value, BRL, per order, all orders with items (the competing definition) |
| T09 | "Finance here: how many orders did we have?" | `o`; count rows; no filter (note's scope for "orders" is not stated in facts O3; both counts needed) | Orders, count, all order rows |
| T10 | "Ops here: how many orders were delivered?" | `o`; count rows; `order_status == 'delivered'` | Orders, count, delivered order rows |
| T11 | "Support here: how many orders were canceled?" | `o`; count rows; `order_status == 'canceled'` | Orders, count, canceled order rows |

Agreement judged item by item: T01-T03 agree if all three match each other and ground truth; likewise T05-T07. T04 and T08 are the contrast: they show how far the all-orders figure sits from the delivered-only figure (the gap between the two is classified as definition, not rounding, per rule 12). Display rounding is classified before any difference is counted.

## 8. Sources as CSV

```csv
source,url_or_tool,what_it_showed,date
Search Console rows,data/ahrefs/search-console-queries.csv,11 rows; none related to the question; file shows no date,read 31 Oct 2026
Keywords Explorer,data/ahrefs/keywords.csv,"semantic layer 2.4K US difficulty 24; metric definitions 20 US difficulty 13; single source of truth metrics and semantic layer ai analyst not indexed","Ahrefs, 27-28 October 2026"
AI answers,measure/citations.md,Question not tracked so not measured; file holds marker counts only,read 31 Oct 2026
Dataset,data/README.md,Olist Brazilian E-Commerce; CC BY-NC-SA 4.0,read 31 Oct 2026
Workspace,facts/dot-mcp.md and facts/dot-facts.md,Two Olist tables; note in O3; mode credits environment notes not observable via MCP,read 31 Oct 2026
WebSearch (order is WebSearch's not Google's),query: how to stop different teams getting different numbers for the same metric,17 results; Acceldata first; four fitgap pages then others,31 Oct 2026
Page 1,https://acceldata.io/blog/how-to-fix-conflicting-metrics-across-teams-a-practical-guide,"Acceldata vendor blog 3 Jan 2026; advice only",31 Oct 2026
Failed fetches,us.fitgap.com x3 (HTTP 410); fog.zeo.org (404); datamasterclass Notion (empty),Not read,31 Oct 2026
Page 2,https://website-2b5.pages.dev/blog/why-team-gets-different-answers/,"Badang Labs 15 Apr 2026; advice; anecdotal 3-5 hours claim",31 Oct 2026
Page 3,https://www.owox.com/blog/articles/analytics-sales-marketing-alignment.md,"OWOX vendor blog updated 14 Oct 2026; mostly advice with SQL on synthetic demo data",31 Oct 2026
```
