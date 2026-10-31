# Research: What does a good AI analyst do when the question is ambiguous, like 'best month'?

Piece slug: `cold-2` (format: research, practice piece, never published). Bank #42 (`ambiguous business questions AI`, bank row 42). Date: 1 November 2026.

## 1. The gap chain

- **What the buyer asks:** "What does a good AI analyst do when the question is ambiguous, like 'best month'?" (bank #42, persona Analytics Engineer).
- **What they find today:** advice only. The three pages read (Databricks, BytePlus docs, a Barking Iguana essay) say to ask a clarifying question or state an assumption. None shows a run with a result. The bank's own scan (31 October 2026) found no "best month" handling anywhere.
- **Who gets cited in AI answers:** not measured. `measure/citations.md` tracks three other questions (day 0, 27 October 2026, Perplexity free app); this question is not among them, so no counts are borrowed.
- **The gap:** advice only. No page shows what an analyst actually returned for "best month", or whether the same question gets the same reading twice.
- **What only Dot can show:** Dot's own answers to "best month" on the Olist tables: whether it asks back or states a basis, which reading it picks (revenue, order count, other), and whether a fresh chat picks the same one. Bank #42's gap basis: O4 (answers state basis; 3 of 29 asked back, 27 October, other account). That is rehearsal, so it is not a finding here (hard rule 4).

## 2. The words buyers type

No input phrase for this question has a measured volume. Phrases that appear in the inputs:

| Phrase | Source | volume_us | volume_global | difficulty |
|---|---|---|---|---|
| ambiguous business questions AI | bank #42 topic | not measured | not measured | not measured |
| best month | the question's own words | not measured | not measured | not measured |
| ambiguous questions | page titles read (Databricks, Barking Iguana) | not measured | not measured | not measured |
| ai data analyst | keywords.csv | 700 | 2.0K | 22 |
| natural language query data | keywords.csv | not indexed | not indexed | not measured |

(Ahrefs, 27-28 October 2026. "ai data analyst" is a head term, not a phrasing of this question.) The honest headline words are the question's own: "ambiguous", "best month", "AI analyst". Volume is unknown, so this question is a sales-call pick, not a search pick (hard rule 1).

## 3. The run

- **Playbook stage:** Stage 3, trusted numbers (the bank's row for #35 names it as the stage that covers testing answers against known figures). This run asks ambiguous questions and marks what Dot returns, so it sits within that stage.
- **Data:** Olist Brazilian e-commerce, `uploads.main.olist_orders_dataset` (99,441 rows) and `uploads.main.olist_order_items_dataset` (112,650 rows), uploaded per `facts/dot-workspace-setup.md`. Licence: CC BY-NC-SA 4.0 (facts A10; the label was never verified at source, L1). Dot (Rick and Théo, 1 November 2026) confirmed Dot may publish figures from Olist (facts L-OLIST).
- **Mode:** the human sets and screenshots it; Economy is the usual choice. Not decided here.
- **Conditions to screenshot in Dot's UI** (`runs/README.md#screenshots`): mode, credits-before, credits-after, environment and notes, all five for batch 1. Both Olist notes must be on, and the metrics note is the "Olist revenue, order value, basket size, cancellation and shipping metrics" note. It defines revenue as delivered orders by purchase timestamp, which will shape what "best" resolves to. Record that as a condition (hard rule 17).
- **Budget:** batch 1 holds at most 4 questions (section 7). Cost per answer, if given, is a credits range with dollars as an assumption (hard rule 10, facts A2).
- **Numbers it must produce:** per question, one figure: the value Dot reports for the month it names, plus (from the answer text, recorded for classification, not asked as a second number) which metric it said it used. Ground truth computes, from the raw CSVs, month-level values under each reading Dot could take, so each answer is marked against the reading it stated (hard rule 18, item by item). Whether Dot asks back instead of answering is recorded; an ask-back is a result, not a failure.

## 4. Sources rows

| Source | URL or tool | What it showed | Date |
|---|---|---|---|
| Search Console rows | `data/ahrefs/search-console-queries.csv` | 11 rows read; none relates to ambiguous questions or "best month". Nothing used. | 1 Nov 2026 (file read) |
| Keywords Explorer | `data/ahrefs/keywords.csv` | Three buyer phrasings ("ambiguous business questions AI", "best month ai analyst", "ai analyst clarifying questions") are absent from the file: not measured. Nearest rows: ai data analyst 700 / 2.0K / difficulty 22; natural language query data not indexed. | Ahrefs, 27-28 October 2026 |
| AI answers | `measure/citations.md` | Question not tracked. Latest reading: 29 Oct 2026 (outside tester), a different question. Not measured for this question. The file holds marker counts only, not full answers. | 1 Nov 2026 (file read) |
| Page 1: Databricks, "Which AI tools handle ambiguity without making things up?" | https://answers.databricks.com/ai-tools-handle-ambiguity-without-hallucinating | WebSearch rank 1 (order is WebSearch's, not Google's, run 1 Nov 2026). Opens: "When you ask an AI assistant a vague or open-ended question, the response may sound confident but be completely wrong." Publisher: Databricks. Date: none shown (a "© Databricks 2026" footer only). **Advice.** Page type: vendor-owned. Cites McKinsey's 51% survey figure; no tests, no Genie accuracy figures. | 1 Nov 2026 |
| Page 2: BytePlus, "Intent Clarification Configuration (in limited release)" | https://docs.byteplus.com/docs/dataagent/Intent_Clarification_Configuration_in_limited_release | WebSearch rank 2 (locale copies at /pt, /id, /es, /de, /vi, /fr, /ko dropped as the same page). Opens: "This article provides configuration guidance related to intent clarification." Publisher: BytePlus. Last updated 5 June 2026. **Advice.** Page type: documentation. Up to three clarifying questions per conversation, configurable; "time and metrics" named as the ambiguity dimensions. | 1 Nov 2026 |
| Page 3 candidate failed: awesomepapers.io paper 2605.25284 | https://awesomepapers.io/speech-audio/papers/2605.25284 | WebSearch rank 3. WebFetch returned HTTP 429 twice. Not read, not described. | 1 Nov 2026 |
| Fallback candidate not readable: arXiv 2607.05762 | https://arxiv.org/pdf/2607.05762 | Came from a second search (the first had no further distinct pages: the rest were BytePlus locale copies). Fetched, but only the title ("Articulating Assumptions in AI-Generated Scientific Analyses through Task Decomposition"), authors (Hammad, Nojiri) and a 2026-07-08 metadata timestamp were recoverable; the body was unreadable. Not described further. | 1 Nov 2026 |
| Page 3: Barking Iguana, "Handling Ambiguous Questions With Clarification" | https://barkingiguana.com/writing/handling-ambiguous-questions-with-clarification/ | From the second search ("AI analyst ambiguous question \"best month\" clarify or state assumption"), rank 2, first readable. Opens: "A retail company runs a customer-service assistant on Amazon Bedrock..." Publisher: Barking Iguana ("Exam Room" series); author Craig R Webster; 4 Aug 2026; posts are LLM-aided per its footer. **Advice.** Page type: practitioner blog (none of the five types fits exactly; nearest is a vendor-neutral listicle-style essay). Illustrative "wrong two times in three" in a hypothetical, not measured. | 1 Nov 2026 |
| The plan | `PLAN.md` | Read. No section names slug `cold-2` or bank #42 (it names A #43, B #36, F #35). No run needs set. | 1 Nov 2026 |
| Workspace setup | `facts/dot-workspace-setup.md` | Olist tables, two notes, and the metrics note's full text (revenue = delivered, purchase timestamp). Used for the run's definitions. | 1 Nov 2026 |
| Dataset and licence | `facts/dot-facts.md` A10, L1, L-OLIST | Olist, CC BY-NC-SA 4.0 (unverified at source); Dot confirmed publishing figures 1 Nov 2026. | 1 Nov 2026 |

WebSearch's order is not Google's. The question's phrasing wasn't searched verbatim for pages 1 and 2 (first search: "what does a good AI analyst do when the question is ambiguous best month"); page 3 came from a second query because the first returned too few distinct pages.

## 5. Stop conditions

Evidence already exists? No: the three pages read are advice; none ran a "best month" question. Only Dot's data could show it, and Dot has the Olist tables (orders by purchase timestamp), so the run is possible. No stop condition applies. One caution: the answer depends on Dot's metrics note (delivered-only revenue), so any finding is about Dot with that note on.

## 6. Verdict

**PIECE IF**: a piece only if the run records the metrics note as active and the finding is stated as what Dot did under that note, since the note may itself settle "best" and leave nothing ambiguous.

## 7. Test questions

All four are asked in batch 1. Each asks for one number. Definitions: month = calendar month of `order_purchase_timestamp` (as stored, no timezone conversion, per the metrics note). "Delivered revenue" = SUM(price) over orders with `order_status = 'delivered'`, aggregated to order then summed by month, BRL. "Delivered orders" = COUNT of delivered orders by month. Ground truth computes the alternative readings too (all-status orders, AOV, revenue including freight) and marks each answer against the reading it states. No values here.

- **T1.** "Which month was our best month?"
  - Depends on: delivered revenue by purchase month (default under the metrics note); alternatives: delivered or all-status order count by month.
  - Figure: the value Dot reports for the month it names; unit and grain as Dot states them (BRL or orders, per purchase month). If Dot asks back, record the ask-back and no number.
- **T2.** Repeat of T1. "Which month was our best month?" (a fresh chat)
  - Same definitions as T1.
  - Figure: the same: the value Dot reports for the month it names, per purchase month. Marked as its own row; compared with T1's reading item by item.
- **T3.** Follow-up of T1. "What if I meant by number of orders? How many orders did the best month have?"
  - Depends on: order count by purchase month, delivered-only and all-status (the answer states which).
  - Figure: orders, in the month Dot names, per purchase month, under the status scope Dot states.
- **T4.** "What was our best month for sales in 2017?"
  - Depends on: delivered revenue by purchase month filtered to purchase timestamps in 2017 (>= 2017-01-01, < 2018-01-01); alternatives as in T1.
  - Figure: the value Dot reports for the month it names, per purchase month, in 2017 (BRL or orders as Dot states).

## 8. Sources as CSV

```csv
source,url_or_tool,what_it_showed,date
Search Console rows,data/ahrefs/search-console-queries.csv,11 rows read; none relates to ambiguous questions or best month; nothing used,1 Nov 2026 (file read)
Keywords Explorer,data/ahrefs/keywords.csv,Three buyer phrasings absent from file: not measured. Nearest: ai data analyst 700 / 2.0K / difficulty 22; natural language query data not indexed,Ahrefs 27-28 October 2026
AI answers,measure/citations.md,Question not tracked; not measured. File holds marker counts only not full answers,1 Nov 2026 (file read)
Page 1 Databricks (vendor-owned; advice),https://answers.databricks.com/ai-tools-handle-ambiguity-without-hallucinating,WebSearch rank 1 (order is WebSearch's not Google's); undated; advice; cites McKinsey 51%; no tests,1 Nov 2026
Page 2 BytePlus docs (documentation; advice),https://docs.byteplus.com/docs/dataagent/Intent_Clarification_Configuration_in_limited_release,WebSearch rank 2; locale copies dropped; updated 5 June 2026; up to 3 clarification attempts; advice,1 Nov 2026
Page 3 candidate awesomepapers.io,https://awesomepapers.io/speech-audio/papers/2605.25284,HTTP 429 twice; not read,1 Nov 2026
Fallback candidate arXiv 2607.05762,https://arxiv.org/pdf/2607.05762,Body unreadable; only title and authors recovered; not described,1 Nov 2026
Page 3 Barking Iguana (practitioner blog; advice),https://barkingiguana.com/writing/handling-ambiguous-questions-with-clarification/,From a second search; 4 Aug 2026; Craig R Webster; design essay; no measured results,1 Nov 2026
The plan,PLAN.md,Read; no section for cold-2 or bank #42; no run needs,1 Nov 2026
Workspace setup,facts/dot-workspace-setup.md,Olist tables and metrics note text (revenue = delivered by purchase timestamp),1 Nov 2026
Dataset and licence,facts/dot-facts.md A10 L1 L-OLIST,Olist CC BY-NC-SA 4.0 (unverified at source); Dot confirmed publishing figures 1 Nov 2026,1 Nov 2026
```
