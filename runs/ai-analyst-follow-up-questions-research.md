# Research: AI analyst follow-up questions context

- **Question (bank #43, buyer's words):** "Does it keep context across follow-ups, and how do I test that?" Short form: "AI analyst follow-up questions context".
- **Piece slug:** ai-analyst-follow-up-questions
- **Date:** 31 October 2026

## 1. The gap chain

- **What the buyer asks:** "Does it keep context across follow-ups, and how do I test that?"
- **What they find today:** advice only. The three pages read are a vendor marketing page (ThoughtSpot, undated), an essay with hypothetical examples (Opinionated Intelligence, 18 March 2026) and a framework post where "context" means business metadata, not conversation memory (Context & Chaos / Metadata Weekly, 13 November 2025). None shows anyone running a follow-up sequence and reporting a result.
- **Who gets cited in AI answers:** not measured. `measure/citations.md` tracks three buyer questions (evaluating accuracy, what changes, cost and fit); this question is not one of them. Its latest reading is Day 0, 27 October 2026, Perplexity free app. Those counts are citation markers, not pages, and the file holds only marker counts, not the answers in full. No count is borrowed from another question.
- **The gap:** advice only. Nobody shows a follow-up chain run against a known dataset with the answers checked against the data.
- **What only Dot can show:** a scripted multi-turn chat in Dot on the Olist tables, where each follow-up leans on the previous turn ("those", "the same for 2018", "the first number"), and each answer is checked against the raw CSVs. Dot returns SQL with each answer (facts/dot-mcp.md), so we can show which filter it carried forward.

## 2. The words buyers type

| Phrase | Where it appears | volume_us | volume_global | difficulty |
|---|---|---|---|---|
| conversational analytics | keywords.csv; Search Console (384 impressions, position 25.8) | 1.2K | 3.5K | 15 |
| ai data analyst | keywords.csv | 700 | 2.0K | 22 |
| AI analyst follow-up questions context | bank row 43 | not measured | not measured | not measured |
| ai analyst data warehouse | keywords.csv | not indexed | not indexed | not measured |
| natural language query data | keywords.csv | not indexed | not indexed | not measured |

All volumes: Ahrefs, 27-28 October 2026 (rows read 27 October 2026). "not indexed" is what Ahrefs displayed, not a zero.

## 3. The run

- **Playbook stage:** Stage 3 · Prove (the playbook page lists Aim, Ground, Prove, Launch, Run). It runs a scripted follow-up test as part of the test set.
- **Data:** Olist orders and order items tables, loaded in the Dot account (`uploads.main.olist_orders_dataset`, 99.4K rows; `uploads.main.olist_order_items_dataset`, 112.7K rows, per facts/dot-mcp.md). Licence: CC BY-NC-SA 4.0 (facts A10, an Assumption: Rick accepted Olist as the trial dataset). Record dataset and licence in Sources before the first run (hard rule 9).
- **Mode:** one mode for the whole batch, recorded per batch. The mode selector (Economy or Balanced, O5) is not settable or readable through MCP, so a person screenshots it.
- **Numbers it must produce:** per test question below, one figure each, plus a pass/fail per follow-up against figures computed from the raw CSVs. Also the count of follow-ups that kept the earlier filter, and the credits per batch (readings from Billing, an Assumption-labelled conversion of 1 credit ≈ $1 per A2, with the docs caveat that the same question can take different paths).
- **Conditions screenshots (per runs/README.md#screenshots):** for each batch, `runs/screenshots/ai-analyst-follow-up-questions-batch-<n>-{mode,credits-before,credits-after,environment,notes}.png`, taken in Dot's UI (mode selector in the chat composer; Settings → Billing before and after; environment menu; Model → Notes showing which notes are on). Whether the "delivered orders" note (O3) is active must be recorded, since it changes revenue scoping.
- **Open definition:** "late" is delivered customer date later than estimated delivery date, compared at calendar-day grain (as O11 did for on-time). The truth spec must fix this before the run.

## 4. Sources rows

| source | url_or_tool | what_it_showed | date |
|---|---|---|---|
| Search Console rows | data/ahrefs/search-console-queries.csv | Related row: "conversational analytics", clicks 0, impressions 384, ctr 0%, position 25.8. Row "conversation analytics software" (338 impressions, position 4.1) is call analytics, not related, left out. No file date shown | 31 October 2026 (read) |
| Keywords Explorer | data/ahrefs/keywords.csv | "conversational analytics" 1.2K US / 3.5K global / difficulty 15; "ai data analyst" 700 / 2.0K / 22; "AI analyst follow-up questions context" not measured | Ahrefs, 27-28 October 2026 |
| AI answers | measure/citations.md | Question not tracked: not measured. Latest reading is Day 0, 27 October 2026, Perplexity free app, three other questions, marker counts only | 31 October 2026 (read) |
| Question bank | bank/questions.csv row 43 | Question, ai_form, persona Analytics Engineer, evidence score 3 (needs multi-turn chats run in Dot) | 31 October 2026 |
| Playbook | https://www.getdot.ai/blog/ai-data-analyst-playbook | Stages: Aim, Ground, Prove, Launch, Run; Stage 3 · Prove covers the test set and ~80% bar | 31 October 2026 |
| Dataset | facts/dot-facts.md A10; facts/dot-mcp.md | Olist, CC BY-NC-SA 4.0 (Assumption); two tables, row counts | 31 October 2026 |
| Top page 1 (WebSearch) | https://www.thoughtspot.com/data-trends/dashboard/ai-analyst-agents-vs-bi-tools | "What an AI Analyst Does That Your BI Tool Can't Answer". Opens: "Your BI tool can tell you that sales dropped in the Midwest last month." ThoughtSpot, vendor blog, Amani Undru; no date. Advice: asserts follow-ups carry context, no test shown | 31 October 2026 |
| Top page 2 (WebSearch) | https://opinionatedintelligence.substack.com/p/why-ai-analysis-gives-you-generic | "Why AI Analysis Gives You The Wrong Specific Answers". Opens: "When people evaluate a company or a product, they almost never rely on a single number." Chandra Narayanan and Julie Zhuo, Opinionated Intelligence; 18 March 2026. Advice, hypothetical examples, no multi-turn test | 31 October 2026 |
| Top page 3 (WebSearch) | https://metadataweekly.substack.com/p/context-engineering-for-ai-analysts (redirects to https://contextandchaos.substack.com/p/context-engineering-for-ai-analysts, read there) | "Context Engineering for AI Analysts". Opens: "What if your AI Analyst understood your business as well as your best human analyst?" Shubham Bhargav, guest post on Context & Chaos; 13 November 2025. Advice; context means metadata, no conversation test | 31 October 2026 |
| WebSearch order | WebSearch, query "AI analyst follow-up questions context test" | The order is WebSearch's, not Google's, on 31 October 2026. Results 1-3 were these distinct pages; all three fetched and read | 31 October 2026 |

Note: the query run was "AI analyst follow-up questions context test" (main phrasing plus "test").

## 5. Stop conditions

- Evidence already exists: no. None of the three pages ran a follow-up test.
- Only Dot's data could show it and Dot lacks that data: no for the core test, since Olist suffices and the MCP can ask multi-turn chats. Limit: mode, credits, environment and notes are not observable via MCP, so a person must take the screenshots.

## 6. Verdict

**PIECE IF** the Olist orders table has the delivered-customer and estimated-delivery date columns, so the "late" chain has a defined ground truth (check with get_catalog or the raw CSV before the truth spec is written).

## 7. Test questions

Chat plan: T1 to T5 are one chat (T1 fresh, each next one a follow-up in T1's chat). T6 is a fresh chat. T7 is fresh and T8 follows it.

**T1.** "How many orders were delivered in 2017?"
- Definition: olist_orders_dataset, order_status = 'delivered', year of purchase timestamp = 2017.
- Figure: count of orders (orders, whole year).

**T2.** Follow-up of T1: "And how many of those were delivered late?"
- Definition: the T1 set, where delivered customer date is later than estimated delivery date, calendar-day grain.
- Figure: count of orders (2017 delivered, late).

**T3.** Follow-up of T2: "What share of the delivered orders is that?"
- Definition: T2 count divided by T1 count.
- Figure: percentage of 2017 delivered orders that were late (one percentage).

**T4.** Follow-up of T3: "What is that share for 2018?"
- Definition: same late definition and delivered filter, purchase year 2018.
- Figure: percentage of 2018 delivered orders that were late (one percentage).

**T5.** Follow-up of T4: "Going back to my first question, how many orders was that?"
- Definition: T1's count, recalled after four later turns.
- Figure: count of orders (2017 delivered), which must equal T1's.

**T6.** (fresh chat, no history) "How many orders delivered in 2017 were delivered later than their estimated delivery date?"
- Definition: same as T2, written in full.
- Figure: count of orders (2017 delivered, late), the control against T2.

**T7.** (fresh chat) "What was the total item price of orders delivered in 2017?"
- Definition: sum of price in olist_order_items_dataset, joined to orders with status 'delivered' and purchase year 2017; freight excluded.
- Figure: revenue, currency units, whole year.

**T8.** Follow-up of T7: "How much of that came in November?"
- Definition: the T7 definition, restricted to purchase month November 2017.
- Figure: revenue, currency units, November 2017.

RESEARCH names figures only; values are computed later from the raw CSVs by `scripts/ground_truth_from_spec.py`.

## 8. Sources as CSV

```csv
source,url_or_tool,what_it_showed,date
Search Console rows,data/ahrefs/search-console-queries.csv,"conversational analytics: clicks 0, impressions 384, ctr 0%, position 25.8; no file date shown",31 October 2026 (read)
Keywords Explorer,data/ahrefs/keywords.csv,"conversational analytics 1.2K US / 3.5K global / difficulty 15; ai data analyst 700 / 2.0K / 22; AI analyst follow-up questions context not measured","Ahrefs, 27-28 October 2026"
AI answers,measure/citations.md,"Question not tracked: not measured; latest reading Day 0 27 Oct 2026 Perplexity free app, marker counts only for other questions",31 October 2026 (read)
Question bank,bank/questions.csv row 43,"Question, ai_form, persona, scores",31 October 2026
Playbook,https://www.getdot.ai/blog/ai-data-analyst-playbook,"Stages Aim, Ground, Prove, Launch, Run; Stage 3 Prove covers test set and ~80% bar",31 October 2026
Dataset,facts/dot-facts.md A10 and facts/dot-mcp.md,"Olist, CC BY-NC-SA 4.0 (Assumption); two tables with row counts",31 October 2026
Top page 1,https://www.thoughtspot.com/data-trends/dashboard/ai-analyst-agents-vs-bi-tools,"ThoughtSpot vendor blog, no date, advice; asserts follow-up context, no test",31 October 2026
Top page 2,https://opinionatedintelligence.substack.com/p/why-ai-analysis-gives-you-generic,"Opinionated Intelligence, 18 Mar 2026, advice, hypothetical examples, no multi-turn test",31 October 2026
Top page 3,https://contextandchaos.substack.com/p/context-engineering-for-ai-analysts,"Context & Chaos guest post (also Metadata Weekly), 13 Nov 2025, advice; context means metadata",31 October 2026
WebSearch order,WebSearch query "AI analyst follow-up questions context test","Order is WebSearch's not Google's; first three distinct pages read in full",31 October 2026
```
