# Research: "how much context does AI analyst need"

Piece slug: `ai-analyst-how-much-context`. Bank #47. Date: 31 October 2026.

Long form (bank `ai_form`): "How much documentation is enough? Can I start with ten definitions, or do I need everything?"

Decision 1 (human) recorded: bank #47, slug `ai-analyst-how-much-context`, `practice: false` (`runs/ai-analyst-how-much-context-piece.json`). Bank row: persona Analytics Engineer, type evaluation, `from_sales_call` = no, `ahrefs_volume_us` = not measured, pdf_score 10 (the highest in the bank is #41 at 10, a tie; the row says inferred, not observed).

## 1. The gap chain

- **What the buyer asks:** "how much context does AI analyst need", long form "How much documentation is enough? Can I start with ten definitions, or do I need everything?"
- **What they find today:** *advice*. The three pages that rank (WebSearch order, 31 October 2026) are an essay with invented numbers (Opinionated Intelligence, 18 Mar 2026), a vendor interview with no accuracy numbers (Collibra, 30 Jul 2026) and a vendor thought-leadership post with a hypothetical example (Mixpanel, 22 Apr 2026). None shows anyone running an analyst with and without a written definition.
- **Who gets cited in AI answers:** not measured. `measure/citations.md` tracks three other buyer questions (evaluating accuracy, what changes, cost and fit); this question is not one of them. No counts are borrowed. The file holds only marker counts, not the answers in full.
- **The gap:** advice only, no measured answer.
- **What only Dot can show:** whether one written note settles what an AI analyst otherwise reads two ways. Piece 2's run (same account and dataset, context only) showed "late" read at timestamp grain in one chat (2,878) and calendar-day in another (2,453), and "delivered in 2017" read as delivery date for item price in both chats but purchase date for a count in both chats. Piece 3's own two batches (before and after a new note, three fresh chats per question) test whether writing those two things down changes the answers. Evidence is Dot's answer text and the SQL returned with each answer, plus `get_catalog` to confirm the note exists.

The bank wording asks about "ten definitions or everything". The run tests one note holding two definitions, so it answers the first step of that question, not the whole of it (PLAN.md). The piece must say so.

## 2. The words buyers type

Search Console: no row in `data/ahrefs/search-console-queries.csv` relates to this question (the twelve rows are about conversational analytics, Power BI, dotmovies and similar). Nothing is copied from it.

Keywords Explorer (Ahrefs, 27-28 October 2026). The exact question is not in the file: "how much context does AI analyst need", volume not measured.

| Phrase | volume_us | volume_global | difficulty | Read |
|---|---|---|---|---|
| ai data analyst | 700 | 2.0K | 22 | Ahrefs, 27 October 2026 |
| metric definitions | 20 | not measured | 13 | Ahrefs, 28 October 2026 (file marks it is_buyer_query = no) |
| semantic layer ai analyst | not indexed | not indexed | not measured | Ahrefs, 27 October 2026 |
| how much context does AI analyst need | not measured | not measured | not measured | not in the file |

Phrases for the headline, from the inputs only: "ai data analyst" (700 US, 2.0K global, difficulty 22), "metric definitions" (20 US, difficulty 13), "how much context does AI analyst need" (bank wording, not measured). "semantic layer ai analyst" is not indexed. The pages that rank use "context", "minimum viable context" and "governed context" in their titles. Those are phrases from the pages read, not Ahrefs-measured.

## 3. The run

- **Playbook stage:** Stage 3 · Prove, as piece 2's outline names it. I did not fetch the Playbook page here, so a human should confirm whether writing a note belongs to a different stage.
- **Account and data:** workspace aiinterviewagents.com; tables `uploads.main.olist_orders_dataset` and `uploads.main.olist_order_items_dataset` (PLAN.md).
- **Dataset and licence (hard rule 9):** Olist Brazilian e-commerce public dataset, licence CC BY-NC-SA 4.0 per `facts/dot-facts.md` A10. The label was never verified at source. Publication proceeds under decision L3 (Saurabh, 31 October 2026, before the run), which is a decision, not a resolution. Copy this section into the run file when it is created.
- **Mode:** Balanced unless decided otherwise (PLAN.md). Mode, credits and environment recorded by hand for this piece (rule 14 waived for those three, PLAN.md); the notes screenshot (Model → Notes) is required for both batches, with `get_catalog` read recorded. Screenshots under `runs/screenshots/ai-analyst-how-much-context-batch-<n>-notes.png` per `runs/README.md#screenshots`. Mode, credits, environment and notes screenshots are not observable via MCP. The piece may state which notes were on and what they said. It may not claim mode, credits or environment.
- **Batch 1, before:** the notes exactly as in piece 2 (metrics note and currency note on; "About aiinterviewagents.com" off). 12 asks: 4 questions, 3 fresh chats each.
- **Between batches:** create a new note, not an edit of the metrics note, with the text Saurabh approved on 31 October 2026 (PLAN.md section "Piece 3"). Read credits after creating it (facts O7: a note made with the context agent can add 20 credits). Confirm with `get_catalog`. Screenshot the notes.
- **Batch 2, after:** the same 4 questions, 3 fresh chats each. 12 asks. 24 in all.
- **Numbers it must produce (a metric, unit and grain per question, no values):** see section 7. Compared item by item and chat by chat (rule 18): does "late" settle on calendar day in all three chats; does item price follow the purchase cohort; does the control stay put.
- **Predictions, stated before the run, from PLAN.md:** item price moves from the delivery-date reading to the purchase cohort; "late" settles on calendar day in all three chats; the control stays put. If they don't, the run records which answers kept the old reading, and that is the finding. Either outcome is publishable.
- **Cost:** credits range with dollars alongside, labelled Assumption (A2, 1 credit ≈ $1), with the docs caveat that the same question can take different paths (rule 10). Waived for publication under the hand-recorded rule 14 waiver: the PLAN says no claim about credits. Decide before the outline whether the piece carries any cost line.
- **Truth spec follows the note, not piece 2's spec, on missing delivery dates (Saurabh, 31 October 2026):** delivered orders with no `order_delivered_customer_date` are left out of both the late count and the denominator. The spec must record why in its notes. The difference from piece 2's spec is display rounding at one decimal (rule 12).

## 4. Sources rows

| Source | URL or tool | What it showed | Date |
|---|---|---|---|
| Question and slug | `runs/ai-analyst-how-much-context-piece.json` | Bank id 47, question "how much context does AI analyst need", practice false | 2026-10-31 |
| Question bank | `bank/questions.csv`, row 47 (page 1 of the file, lines 1-63, read) | ai_form "How much documentation is enough? Can I start with ten definitions, or do I need everything?"; Analytics Engineer; ahrefs_volume_us not measured; existing gap note: three advice pages, none with original evidence | 2026-10-31 |
| Search Console | `data/ahrefs/search-console-queries.csv` | 12 rows; none relates to the question; none used | 2026-10-31 |
| Keywords Explorer | `data/ahrefs/keywords.csv` | "ai data analyst" US 700, global 2.0K, difficulty 22; "metric definitions" US 20, global not measured, difficulty 13; "semantic layer ai analyst" not indexed; the question phrase not in file. Ahrefs, 27-28 October 2026 | 2026-10-31 |
| AI answers | `measure/citations.md` | Latest monthly reading is Day 0, 27 October 2026, Perplexity free app, three other questions. This question is not tracked: not measured. The file holds marker counts only, not the answers | 2026-10-31 |
| Ranking page 1 | https://opinionatedintelligence.substack.com/p/why-ai-analysis-gives-you-generic | "Why AI Analysis Gives You The Wrong Specific Answers", Chandra Narayanan and Julie Zhuo, Opinionated Intelligence (Substack), 18 Mar 2026. Opens "When people evaluate a company or a product, they almost never rely on a single number." Advice; examples hypothetical | 2026-10-31 |
| Ranking page 2 | https://www.collibra.com/blog/customer-zero-how-collibra-built-an-org-wide-ai-analyst-on-its-own-governed-context | "Customer zero: How Collibra built an org-wide AI analyst on its own governed context", Collibra blog, interview by Meredith Bailey with Dmytro Protsyk, 30 Jul 2026. Opens "We built our own internal AI analyst, named it Dwight, and pointed it at our internal data." Advice; says accuracy, cost and speed "all improved at once" with better context, gives no figures | 2026-10-31 |
| Ranking page 3 | https://mixpanel.com/blog/why-ai-analytics-needs-behavioral-context/ | "Why AI analytics needs behavioral context", Mixpanel, Scott Cohen, 22 Apr 2026 (page shows "last edited" 1 Oct 2026). Opens "Context engineering is a relatively new discipline, but the baseline playbook is already forming." Advice; hypothetical A/B example, no results | 2026-10-31 |
| WebSearch order | WebSearch, query "how much context does an AI data analyst need" | Order is WebSearch's, not Google's, on 31 October 2026. First three distinct pages are the three above. The query run was "how much context does an AI data analyst need", a slight rewording of the bank phrase. All three loaded in full via WebFetch (read through a summarising fetch tool, not raw text) | 2026-10-31 |
| Plan | `PLAN.md` | Has a section naming `ai-analyst-how-much-context` and bank #47. Sets: 4 questions worded as in piece 2, 3 fresh chats each, 2 batches, 24 asks; new note between batches; spec follows the note on missing delivery dates; notes screenshot both batches; rule 14 waived for mode, credits, environment | 2026-10-31 |
| Prior run (context only) | `runs/ai-analyst-shows-sql-run.md` | Metrics note verbatim; piece 2 answers: "late" 2,878 (timestamp) vs 2,453 (calendar day); 2018 late share 7.7% both chats; item price delivered in 2017 BRL 5,612,818 both chats; count delivered in 2017 43,428 both chats; purchase-cohort item price BRL 5,962,902 (Q3/Q9 data). Context for piece 3 only (rule 4) | 2026-10-31 |
| Facts | `facts/dot-facts.md` | A10 and L3 (Olist licence, decision to proceed); A2 (1 credit ≈ $1); O7 (a context-agent note can add 20 credits) | 2026-10-31 |

## 5. Stop conditions

Evidence does not exist: all three ranking pages are advice, and none reports a run. Dot has the data (the two Olist tables, already loaded) and the feature (notes, `get_catalog`). No stop condition applies.

Two cautions, neither a stop. First, the test covers one note on two definitions, not "ten definitions or everything", and the piece must not claim to answer the whole question. Second, rule 4: piece 2's run is context only; the piece's finding must come from piece 3's own batches.

## 6. Verdict

**PIECE IF** the notes screenshot for both batches and the `get_catalog` reads are captured, so the piece may state which notes were on. Without them the piece cannot say what was written down when.

## 7. Test questions

Each chat takes one question and returns one number. Four questions, each in three fresh chats per batch: 12 asks per batch, 24 across both batches. Questions are worded exactly as in piece 2. Truth spec: rivals computed before the run; the spec follows the approved note (calendar-day grain, purchase cohort, missing delivery dates left out of count and denominator).

Definitions used by the four questions:
- Purchase cohort 2017 = `order_purchase_timestamp` from 2017-01-01 to before 2018-01-01 on `uploads.main.olist_orders_dataset`; delivered = `order_status = 'delivered'`.
- Late (calendar day) = `CAST(order_delivered_customer_date AS DATE) > CAST(order_estimated_delivery_date AS DATE)`. Rival: timestamp grain (`order_delivered_customer_date > order_estimated_delivery_date`).
- Item price = SUM(`price`) in `olist_order_items_dataset`, aggregated to order then summed. Rival reading for T3: orders filtered on delivery date, `order_delivered_customer_date` in 2017.
- 2018 late share = 100.0 × late orders / delivered orders with a delivery date, 2018 purchase cohort, one decimal.

**The 12 test questions. Batch 1 (before the new note) asks all 12; batch 2 (after the note is created and confirmed with `get_catalog`) asks the same 12 again, in new fresh chats.**

| # | Question, as it will be asked | Depends on | Figure it must produce | Chat |
|---|---|---|---|---|
| T1 | How many orders were delivered late in 2017? | Purchase cohort 2017, delivered, late at calendar day, missing delivery dates left out; rival: timestamp grain | Count of orders, one 2017 cohort | Fresh chat 1 |
| T2 | What percentage of delivered orders were late in 2018? | 2018 cohort, delivered, late at calendar day, denominator delivered with a delivery date; rivals: timestamp grain, missing dates kept in the denominator | Percentage of delivered orders, one 2018 cohort, one decimal | Fresh chat 1 |
| T3 | What was the total item price of orders delivered in 2017? | Item price definition; purchase cohort (truth) vs delivery-date filter (rival) | BRL total, one 2017 period | Fresh chat 1 |
| T4 | How many orders were delivered in 2017? | Purchase cohort 2017, status delivered (control); rival: delivery-date filter | Count of orders, one 2017 period | Fresh chat 1 |
| T5 | How many orders were delivered late in 2017? | As T1 | As T1 | Repeat of T1, fresh chat 2 |
| T6 | What percentage of delivered orders were late in 2018? | As T2 | As T2 | Repeat of T2, fresh chat 2 |
| T7 | What was the total item price of orders delivered in 2017? | As T3 | As T3 | Repeat of T3, fresh chat 2 |
| T8 | How many orders were delivered in 2017? | As T4 | As T4 | Repeat of T4, fresh chat 2 |
| T9 | How many orders were delivered late in 2017? | As T1 | As T1 | Repeat of T1, fresh chat 3 |
| T10 | What percentage of delivered orders were late in 2018? | As T2 | As T2 | Repeat of T2, fresh chat 3 |
| T11 | What was the total item price of orders delivered in 2017? | As T3 | As T3 | Repeat of T3, fresh chat 3 |
| T12 | How many orders were delivered in 2017? | As T4 | As T4 | Repeat of T4, fresh chat 3 |


*Changed 31 October 2026, before review and before the run:* this section first listed batch 2 as T13–T24. `stage_gate.py` counts a batch as complete only when it has an entry for every asked question in the spec, so each batch must ask the same set. Batch 2 now re-asks T1–T12; its answers are told apart by batch, not by question id. No wording, definition or value changed.

No follow-up questions: PLAN.md asks for fresh chats only. Each question asks for exactly one number. No question contains the words "delivery date" or "reached the customer", which keeps the note's let-out test intact (PLAN.md). The marker for each answer is the number against the stated definition (rule 18, item by item).

## 8. Sources as CSV

```csv
source,url_or_tool,what_it_showed,date
Question and slug,runs/ai-analyst-how-much-context-piece.json,"Bank id 47, question 'how much context does AI analyst need', practice false",2026-10-31
Question bank,bank/questions.csv row 47,"ai_form 'How much documentation is enough? Can I start with ten definitions, or do I need everything?'; ahrefs_volume_us not measured; existing gap note: advice pages with no original evidence",2026-10-31
Search Console,data/ahrefs/search-console-queries.csv,"12 rows; none relates to the question; none used",2026-10-31
Keywords Explorer,data/ahrefs/keywords.csv,"ai data analyst US 700 global 2.0K difficulty 22; metric definitions US 20 global not measured difficulty 13; semantic layer ai analyst not indexed; question phrase not in file (Ahrefs 27-28 October 2026)",2026-10-31
AI answers,measure/citations.md,"Latest reading Day 0 27 October 2026 Perplexity free app; this question not tracked so not measured; file holds marker counts only not the answers",2026-10-31
Ranking page 1,https://opinionatedintelligence.substack.com/p/why-ai-analysis-gives-you-generic,"Opinionated Intelligence (Narayanan and Zhuo) 18 Mar 2026; advice; hypothetical numbers",2026-10-31
Ranking page 2,https://www.collibra.com/blog/customer-zero-how-collibra-built-an-org-wide-ai-analyst-on-its-own-governed-context,"Collibra blog 30 Jul 2026; vendor interview; advice; no accuracy figures",2026-10-31
Ranking page 3,https://mixpanel.com/blog/why-ai-analytics-needs-behavioral-context/,"Mixpanel (Scott Cohen) 22 Apr 2026; advice; hypothetical example",2026-10-31
WebSearch order,WebSearch query 'how much context does an AI data analyst need',"Order is WebSearch's not Google's on 31 October 2026; first three distinct pages as above",2026-10-31
Plan,PLAN.md,"Section for ai-analyst-how-much-context names 4 questions x 3 fresh chats x 2 batches; new note between batches; spec follows note on missing delivery dates; notes screenshot both batches",2026-10-31
Prior run (context only),runs/ai-analyst-shows-sql-run.md,"Metrics note verbatim; piece 2 answers for late grain and delivered-in-2017 readings; context for piece 3 only (rule 4)",2026-10-31
Facts,facts/dot-facts.md,"A10 and L3 Olist licence decision; A2 1 credit ~ $1; O7 context-agent note can add 20 credits",2026-10-31
```
