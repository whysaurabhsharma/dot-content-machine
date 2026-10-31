# Research: AI analyst shows SQL

- **Question (bank #41, buyer's words):** "Why does it matter whether the AI shows its SQL, and would anyone on my team read it?" Short form: "AI analyst shows SQL".
- **Piece slug:** ai-analyst-shows-sql
- **Date:** 31 October 2026

## 1. The gap chain

- **What the buyer asks:** "Why does it matter whether the AI shows its SQL, and would anyone on my team read it?"
- **What they find today:** advice only. The three pages read are LeadDesk product docs (undated; says the tool generates SQL, users can copy it, validate results), a Querio vendor article (19 June 2026; argues hidden SQL hides bad joins and missing filters, cites other people's figures, no own test) and an AI2sql promo page (undated; never displays a generated query). None shows an answer set where the SQL changed what a reader would conclude. Evidence: none of the three.
- **Who gets cited in AI answers:** not measured. `measure/citations.md` tracks three other buyer questions (evaluating accuracy, what changes, cost and fit); this one is not tracked, so no count is borrowed. Latest reading is Day 0, 27 October 2026, Perplexity free app (two later readings, 28 and 29 October, are on a different question). Counts there are citation markers, not pages, and the file holds only marker counts, not the answers in full.
- **The gap:** advice only. Everyone says "check the SQL"; nobody counts how often the answer text already states its definition versus how often only the SQL reveals it.
- **What only Dot can show:** each answer's text and SQL come back together through `ask_dot`/`get_result` (facts/dot-mcp.md). Asking the same ambiguous questions in fresh chats on the Olist tables, we can count per answer whether the definition was stated in the text, shown only in the SQL, or neither, and check each figure against the raw CSVs. Whether anyone on a team reads the SQL is not something a run can show.

## 2. The words buyers type

| Phrase | Where it appears | volume_us | volume_global | difficulty |
|---|---|---|---|---|
| AI analyst shows SQL | bank row 41 | not measured | not measured | not measured |
| ai data analyst | keywords.csv | 700 | 2.0K | 22 |
| conversational analytics | keywords.csv | 1.2K | 3.5K | 15 |
| text to sql accuracy | keywords.csv | 10 | 10 | not measured |
| ai analyst data warehouse | keywords.csv | not indexed | not indexed | not measured |

All volumes: Ahrefs, 27-28 October 2026 (rows read 27 October 2026). "not indexed" is what Ahrefs displayed, not a zero. Search Console: no row relates to this question (the nearest, "conversational analytics", 384 impressions, 0 clicks, position 25.8, is a different topic); none used.

## 3. The run

- **Playbook stage:** Stage 3 · Prove (Aim, Ground, Prove, Launch, Run). The Playbook line "We ship that too, and almost nobody opens it" sits under "Train against numbers people already trust" in Stage 3, and refers to "show our work" generally, not SQL specifically.
- **Data:** Olist orders and order items, loaded in the aiinterviewagents.com workspace (`uploads.main.olist_orders_dataset`, 99.4K rows; `uploads.main.olist_order_items_dataset`, 112.7K rows). Licence: CC BY-NC-SA 4.0 (facts A10, an Assumption; the label was never verified at source and facts L1 records that publishing proceeds as a decision, not a resolution).
- **Mode:** Balanced unless decided otherwise (PLAN.md). The mode is not settable or readable through MCP, so a person screenshots it each batch.
- **What to run:** about 6 ambiguous questions, each asked in two fresh chats (12 asks), worded identically. Rival readings are computed before the run in the truth spec (`"asked": false` rows). Reuse piece 1's definitions (T1b delivery date, T2b timestamp grain, T7b with freight, T7c all statuses).
- **Numbers it must produce:** per ask, one figure marked against the raw CSVs. From the answers and SQL, for each ask: whether the text states the reading used (date, freight, status, late grain), or only the SQL does, or neither; the count per category across the 12 asks; and, per question, whether the two chats agreed on a reading. Also credits per batch, as a range with dollars alongside, labelled Assumption (A2: 1 credit about $1), with the docs caveat that the same question can take different paths. Counts of answers are counts of answers, recounted from the run text (rule 16).
- **Conditions:** screenshots per runs/README.md#screenshots: `runs/screenshots/ai-analyst-shows-sql-batch-<n>-{mode,credits-before,credits-after,environment,notes}.png`. Active context notes must be listed (rule 17): `get_catalog` shows the notes "Olist dataset currency and monetary formatting" and "Olist revenue, order value, basket size, cancellation and shipping metrics" exist, but whether either is active is not observable via MCP. Piece 3 compares against exactly this state.
- **Fixed before the run:** "late" = calendar-day grain (date part of delivered customer date later than date part of estimated date), as piece 1.

## 4. Sources rows

| source | url_or_tool | what_it_showed | date |
|---|---|---|---|
| Search Console rows | data/ahrefs/search-console-queries.csv | No related rows; "conversational analytics" (0 clicks, 384 impressions, position 25.8) is adjacent, not used | 31 October 2026 (read) |
| Keywords Explorer | data/ahrefs/keywords.csv | "AI analyst shows SQL" not measured; ai data analyst 700 / 2.0K / 22; text to sql accuracy 10 / 10 / not measured; conversational analytics 1.2K / 3.5K / 15; ai analyst data warehouse not indexed | Ahrefs, 27-28 October 2026 |
| AI answers | measure/citations.md | Question not tracked: not measured. Latest reading Day 0, 27 Oct 2026, Perplexity free app; marker counts only, answers not held in full | 31 October 2026 (read) |
| Question bank | bank/questions.csv row 41 | Question, ai_form, persona Head of Data, evidence score 3 (SQL returned with every answer; per-number lineage not relied on) | 31 October 2026 |
| Top page 1 | https://onboard.leaddesk.com/what-is-the-ai-analyst | "What is the AI Analyst?" Opens: "Analyst AI is an AI tool to accelerate the creation of SQL queries to interrogate LeadDesk call data." LeadDesk Plc; no date. Advice (product docs); says validate, results vary between runs | 31 October 2026 |
| Top page 2 | https://docs.patterns.app/basics/generating-analyses | Failed to load: "Page Not Found". Not described; next distinct result taken | 31 October 2026 |
| Top page 2 (next) | https://querio.ai/articles/what-is-an-ai-data-analyst-capabilities-limitations | "What Is an AI Data Analyst? Capabilities & Limitations". Opens: "An AI data analyst can answer plain-English questions, write SQL on live warehouse data, and return a fast first draft." Querio, vendor; 19 June 2026. Advice; secondhand figures, no own test | 31 October 2026 |
| Top page 3 | https://ai2sql.io/ai2sql-data-analysts-no-code-sql | "AI2SQL for Data Analysts: No-Code SQL Generation Made Easy". Opens: "Data analysts and business professionals often need to pull insights from databases, but not everyone is fluent in SQL." AI2sql, vendor; no date. Advice; never shows a generated query | 31 October 2026 |
| WebSearch order | WebSearch, query "AI analyst shows SQL" | Order is WebSearch's, not Google's, on 31 October 2026. Distinct results in order: LeadDesk, Patterns (failed), Querio, AI2sql (a second AI2sql URL dropped as the same publisher's sibling page) | 31 October 2026 |
| Playbook | https://www.getdot.ai/blog/ai-data-analyst-playbook | Stages 1 Aim to 5 Run; Stage 3 · Prove; "We ship that too, and almost nobody opens it" under "Train against numbers people already trust" | 31 October 2026 |
| Plan | PLAN.md | Read. Section names this slug (piece 2, bank #41). Needs set: about 6 questions with rivals computed before the run; at least two on "delivered in <year>" (a count and an item-price total); one on "how much did customers spend"; rest on order status and "late"; each question in at least two fresh chats (about 12 asks); all five screenshots per batch; active notes listed | 31 October 2026 |
| Dataset | facts/dot-facts.md A10, L1; facts/dot-mcp.md | Olist, CC BY-NC-SA 4.0 (Assumption, unverified at source); two tables with row counts | 31 October 2026 |

## 5. Stop conditions

- Evidence already exists: no. None of the three pages counts where a definition is stated.
- Only Dot's data could show it and Dot lacks it: no. Olist suffices and SQL returns with every answer. Limits: mode, credits, environment and notes need person-taken screenshots; whether a reader would open the SQL cannot be shown by this run.

## 6. Verdict

**PIECE IF** the piece claims only what the run counts (where each definition appears: text, SQL only, or neither) and makes no claim about whether teams read SQL; "almost nobody opens it" is not used without its own source.

## 7. Test questions

Chat plan: every test question is its own fresh chat. T1 to T6 are the first ask; T7 to T12 repeat them in new fresh chats. Each asks for one number. The text/SQL classification is read from each answer afterwards, not asked.

**T1.** "How many orders were delivered in 2017?"
- Definition: olist_orders_dataset, order_status = 'delivered', year of purchase timestamp = 2017. Rivals: delivered customer date in 2017 (piece 1 T1b).
- Figure: count of orders, delivered, whole year.

**T2.** "What was the total item price of orders delivered in 2017?"
- Definition: sum of price in olist_order_items_dataset joined to delivered orders purchased in 2017; freight excluded. Rivals: delivery year (T7d), with freight, all statuses (T7c).
- Figure: item price total, BRL, whole year.

**T3.** "How much did customers spend in 2017?"
- Definition: sum of price plus freight_value on items of delivered orders purchased in 2017 (what customers paid). Rivals: price only, all statuses, delivery year. The spec fixes the primary before the run.
- Figure: customer spend, BRL, whole year.

**T4.** "How many orders did we get in 2017?"
- Definition: orders table, all statuses, purchase year 2017. Rival: delivered only.
- Figure: count of orders, all statuses, whole year.

**T5.** "How many orders were delivered late in 2017?"
- Definition: delivered orders purchased in 2017 where the date part of the delivered customer date is later than the date part of the estimated date (calendar day). Rivals: timestamp grain (T2b), delivery year (T2c).
- Figure: count of late orders, delivered, whole year.

**T6.** "What percentage of delivered orders were late in 2018?"
- Definition: late delivered orders purchased in 2018 (calendar day) divided by delivered orders purchased in 2018. Rivals: timestamp grain, delivery year.
- Figure: percentage of delivered orders, purchase year 2018.

**T7.** Repeat of T1: "How many orders were delivered in 2017?" (fresh chat). Same definition and figure as T1.

**T8.** Repeat of T2: "What was the total item price of orders delivered in 2017?" (fresh chat). Same as T2.

**T9.** Repeat of T3: "How much did customers spend in 2017?" (fresh chat). Same as T3.

**T10.** Repeat of T4: "How many orders did we get in 2017?" (fresh chat). Same as T4.

**T11.** Repeat of T5: "How many orders were delivered late in 2017?" (fresh chat). Same as T5.

**T12.** Repeat of T6: "What percentage of delivered orders were late in 2018?" (fresh chat). Same as T6.

RESEARCH names figures only; values are computed later from the raw CSVs by `scripts/ground_truth_from_spec.py`. PLAN.md needs met: at least two "delivered in <year>" questions (T1, T2), one spend question (T3), status (T4) and late (T5, T6), every question in two fresh chats.

## 8. Sources as CSV

```csv
source,url_or_tool,what_it_showed,date
Search Console rows,data/ahrefs/search-console-queries.csv,"No related rows; conversational analytics (0 clicks, 384 impressions, position 25.8) adjacent, not used",31 October 2026 (read)
Keywords Explorer,data/ahrefs/keywords.csv,"AI analyst shows SQL not measured; ai data analyst 700 / 2.0K / 22; text to sql accuracy 10 / 10 / not measured; conversational analytics 1.2K / 3.5K / 15; ai analyst data warehouse not indexed","Ahrefs, 27-28 October 2026"
AI answers,measure/citations.md,"Question not tracked: not measured; latest reading Day 0 27 Oct 2026 Perplexity free app; marker counts only",31 October 2026 (read)
Question bank,bank/questions.csv row 41,"Question, ai_form, persona, evidence score 3",31 October 2026
Top page 1,https://onboard.leaddesk.com/what-is-the-ai-analyst,"LeadDesk Plc product docs, no date, advice",31 October 2026
Top page 2 (failed),https://docs.patterns.app/basics/generating-analyses,"Page Not Found; not described",31 October 2026
Top page 2 (next),https://querio.ai/articles/what-is-an-ai-data-analyst-capabilities-limitations,"Querio vendor, 19 Jun 2026, advice, secondhand figures",31 October 2026
Top page 3,https://ai2sql.io/ai2sql-data-analysts-no-code-sql,"AI2sql vendor, no date, advice, no generated query shown",31 October 2026
WebSearch order,"WebSearch, query AI analyst shows SQL","Order is WebSearch's not Google's; first three distinct readable pages read in full",31 October 2026
Playbook,https://www.getdot.ai/blog/ai-data-analyst-playbook,"Stage 3 Prove; 'We ship that too, and almost nobody opens it'",31 October 2026
Plan,PLAN.md,"Read; section names piece 2 slug; needs: ~6 questions, rivals before run, two delivered-in-year, one spend, status and late, two fresh chats each, five screenshots per batch",31 October 2026
Dataset,facts/dot-facts.md A10 L1 and facts/dot-mcp.md,"Olist, CC BY-NC-SA 4.0 (Assumption, unverified at source); two tables with row counts",31 October 2026
```
