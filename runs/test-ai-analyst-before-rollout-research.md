# Research: "How do I test whether an AI data analyst gives correct answers before rolling it out?"

Piece slug: `test-ai-analyst-before-rollout` · Format: guide (`runs/test-ai-analyst-before-rollout-piece.json`) · Bank #35 (bank phrase "how to evaluate AI data analyst accuracy") · Date: 1 November 2026 · Role: cluster hub (links to A and B; both link back).

## 1. The gap chain

- **What the buyer asks:** "How do I test whether an AI data analyst gives correct answers before rolling it out?"
- **What they find today:** advice, mostly. Top three pages for the main phrasing (WebSearch order, 1 November 2026): a dbt Labs blog post reporting one consultancy's results (evidence, self-reported, second-hand: dbt Labs writing about a Data Culture talk); a dbt Summit session abstract (advice, no numbers); a Querio vendor guide (advice, no test run). None gives numbered steps backed by several organisations' published methods or by a run.
- **Who gets cited in AI answers:** not measured. `measure/citations.md` tracks three buyer questions by topic label only ("1 · Evaluating accuracy"); the buyer's wording is not recorded, so it cannot be matched to this question and no count is borrowed. For the human's information only: the file's latest reading is Day 0 (27 October 2026, Perplexity free app, citation markers, not pages); there is no later monthly reading in the file (the "Next check" heading is empty). On that label: Dot 5 (the AI Data Analyst Playbook), datafact 8, bygravity 4, getbruin 1, aianalystlab 1. The file holds marker counts only, not the answers in full; nothing was recounted or reconstructed.
- **The gap:** advice only. Nobody ranks with steps that cite what 13 organisations published (B) plus a run showing what the steps catch.
- **What only Dot can show:** from runs already done (no new run): answers that came back with SQL (A: 8 of 8, F16; piece 2: 12 of 12, F05), a right answer to an ambiguous question that only the SQL disambiguated (A: two answers whose date a person read from the SQL, A-3), and the same question in two fresh chats returning two different counts (piece 2: 2,878 and 2,453, F08). Our runs are evidence for steps, not the subject.

## 2. The words buyers type

Ahrefs, 27-28 October 2026 (frozen snapshot). I read `data/ahrefs/keywords.csv` today; B's research read the same rows on 31 October 2026, and its attribution is kept.

| Phrase | volume_us | volume_global | difficulty |
|---|---|---|---|
| ai data analyst | 700 | 2.0K | 22 |
| text to sql accuracy | 10 | 10 | not measured |
| how to evaluate ai data analyst accuracy | not indexed | not indexed | not measured |
| ai data analyst accuracy | not indexed | not indexed | not measured |

Search Console (`data/ahrefs/search-console-queries.csv`, read 1 November 2026): no row relates to testing or accuracy. The nearest topic neighbour is "conversational analytics" (0 clicks, 384 impressions, position 25.8); it is not this question. Titles seen on ranking pages: "How to Eval an AI Data Analyst: Framework + Open Benchmarks", "Don't ship what you can't measure: Evaluation-driven development for AI analytics agents". "Before rollout" and "correct answers" appear only in the buyer's question, not in any keyword row; "test" does not appear in any row either. Search volume is thin: the only measured head term is "ai data analyst".

## 3. The run

No new Dot run. The guide cites runs already done and B's census (PLAN.md section F).
- **Playbook stage:** the evaluation stage ("evaluating accuracy", per the citations label); not confirmed against the Playbook text, which I did not read.
- **Dataset and licence (hard rule 9):** Olist Brazilian e-commerce dataset (orders and order items), used in A's run and piece 2's run. Licence recorded in the repo as CC BY-NC-SA 4.0, an Assumption (facts A10), never verified at source; Saurabh decided publication may proceed (facts L1 for A, L2 for piece 2), a decision and not a resolution. The guide inherits the same open question wherever it cites an Olist-derived figure.
- **Conditions screenshots (runs/README.md#screenshots):** none exist. Rule 14 was waived for A's run and piece 2's run (hand-recorded). No step may rest on mode, credits, environment or context notes from either run, and the guide gives no cost per answer (hard rule 10). Also: both runs had the metrics note on (hand-recorded); that can't be used to say the note changes or fixes anything, and no run of ours tested that.

## 4. Sources rows

See section 8 (CSV). Plan: PLAN.md read 1 November 2026; section "F, test-ai-analyst-before-rollout" names this slug. It sets: section 7 is evidence per step; may cite A's run and piece 2's archived run only; no claim from the waived conditions; 1,000-1,900 words; 5-9 numbered steps starting with a verb; depends on B.

**How the top three pages were read.** WebFetch returns a model-written reading, not raw text. Quotes below that came back in quotation marks are marked as such; every one must be re-opened before it is quoted.
1. dbt Labs blog (https://www.getdbt.com/blog/data-culture-ai-analytics-agent-trust-context): title "How Data Culture measured its way from zero trust to a shippable AI analytics agent"; opening (quoted by the reading): "At a dbt Summit 2026 breakout session titled" "Don't ship what you can't measure: Evaluation-driven development for AI analytics agents," "Opeyemi Fabiyi, director of analytics engineering at Data Culture, laid out a three-step framework"; publisher dbt Labs; dated 2026-10-26; vendor blog post and conference recap with a case study; evidence of self-reported results (reading: 0% to 94.7% on one e-commerce deployment; those numbers are not in B's figures and are not used here).
2. dbt Summit session (https://www.getdbt.com/dbt-summit/sessions/dont-ship-what-you-cant-measure-evaluation-driven-development-for-ai-analytics-agents): opening (quoted by the reading): "Building AI analytics agents is becoming democratised; tools like Snowflake Cortex Analyst make it easier than ever..."; publisher dbt Labs; session on 18 September 2026; conference session description; advice, no results. The `/agenda/` URL in the results is the same page and was dropped.
3. Querio (https://querio.ai/articles/evaluate-ai-data-analyst-framework-open-benchmarks): title "How to Eval an AI Data Analyst: Framework + Open Benchmarks"; opening (quoted by the reading): "If I were buying or testing an AI data analyst, I'd judge it on five things: correct SQL results,"; publisher Querio (AI analytics vendor); Sep 9, 2026; vendor blog article; advice (50-100 versioned questions, 0-3 scoring, thresholds such as 90%), no test of its own.

## 5. Stop conditions

None applies. Evidence in the sense of "someone ran it" exists at the company level (B's census), and our runs exist, so the piece is not "no answer"; but no ranking page turns them into steps. Dot does hold the data the run-based steps need (Olist runs in A and piece 2). Two limits the guide must carry: several steps are practice "done by" a named company, not shown to work; and the strongest "works" evidence in our runs is detection (the test surfaced a difference), not a fix.

## 6. Verdict

**PIECE IF** each census publication a step leans on (Anthropic, LinkedIn, Uber, ClickHouse, Hex) is opened and read again for this piece (hard rule 4b; B read them via WebFetch, a model-written reading) and Saurabh's licence decision (L1, L2) is accepted to cover citing Olist-derived figures.

Enough steps have evidence for a five-step guide without leaning on "untested": steps 2, 3, 4, 6 and 8 below each rest on a run of ours, a cited publication with a number, or both. Steps 1 and 5 and 7 are thinner (a practice done by named companies, or one chain of our own). Steps 9 and the questions-count claim must be cut or labelled untested; see the end of section 7.

## 7. Evidence for each step

Reading conventions. IDs are rows of `figures/how-companies-test-ai-data-analysts-figures.csv` (B) or `figures/ai-analyst-follow-up-questions-figures.csv` (A) and `figures/ai-analyst-shows-sql-figures.csv` (piece 2, "P2"). "Done by X" means the publication says they do it; it is not "shown to work". Hard rule 4(d): a cited number never sits beside, or confirms, a figure of ours. Piece 2's "12 of 12 correct" needs care: by the question's primary definition 9 of 12 matched exactly; Q2, Q5 and Q8 (P2 MR-Q2, MR-Q5, MR-Q8) were marked correct only under the definition the answer stated (rival readings T2d, T5b, T2d). A's "8 of 8" likewise: Q6 and Q8 were decided by a person, Q7 correct under its stated definition (A MR-Q6, MR-Q7, MR-Q8). Rule 18: item by item, not in total.

**Step 1. Collect real questions from your own people and logs to test with.** Status: cited publication (practice, not shown to work).
- Anthropic, https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude (3 June 2026): evals from dashboards (human-validated), business context, and stakeholder corrections harvested from threads.
- LinkedIn, https://www.linkedin.com/blog/engineering/ai/practical-text-to-sql-for-data-analytics (9 Dec 2024), paper https://arxiv.org/html/2507.14372v1: domain experts wrote 130+ questions (LIN-1, LIN-2) / 133 questions, 167 ground-truth tables (LIN-10, LIN-11).
- Uber QueryGPT, https://www.uber.com/blog/query-gpt (19 Sep 2024): real questions from logs, manually verified intent, schemas and golden SQL (a quote the B reading returned in quotation marks; re-open).
- ClickHouse, https://clickhouse.com/blog/agentic-analytics-benchmark-data-agent-mnist: 201 questions from production traffic (CLK-1).
- Census count: 8 of 13 build the set from real questions or expert/ground-truth queries (C-4).
- Not shown: that real questions find more errors than invented ones. No run of ours (A's and P2's questions were written by us).

**Step 2. Write the expected answer and its definition before you ask, and accept more than one valid reading where the question allows.** Status: both.
- Ours: the truth specs list rival readings per question (`figures/ai-analyst-shows-sql-truth.csv` T2d, T5b, T11; `figures/ai-analyst-follow-up-questions-truth.csv` T2c, T7d, T8c). P2: 3 of 12 answers matched a rival definition rather than the primary one (MR-Q2, MR-Q5, MR-Q8); A: 3 of 8 (MR-Q6, MR-Q7, MR-Q8). Without the listed rivals those would have been marked wrong; whether they were errors was a person's call (A). The test shows the practice classifies; it doesn't show the answers should be accepted.
- Cited: LinkedIn: ~60% of benchmark questions have more than one valid answer (LIN-3, LIN-12); without the extra accepted answers recall was underreported by 10-15% (LIN-4). ClickHouse dropped 39 questions where its three ground-truth models disagreed (CLK-4). Anthropic anchors ground truth to a snapshot date or a stable table (reading's paraphrase; re-open).
- Do not say: that stating a definition in the data tool fixes the ambiguity. Untested.

**Step 3. Ask each question more than once, each time in a fresh chat, and compare.** Status: run of ours (one dataset, two chats per question).
- P2 (`runs/ai-analyst-shows-sql-run.md`, Q1-Q6 vs Q7-Q12): 6 questions in 2 fresh chats (F01-F03); 5 of 6 pairs returned the same value (F07); the late-orders pair returned 2,878 (Q5) and 2,453 (Q11), a gap of 425 (F08), each answer stating its own definition (timestamp vs estimated delivery day).
- A: Q6 (fresh chat) did not reproduce Q2 (chain): 1,762 vs 2,453 (MR-Q6, MR-Q2, F12: 691), because the same words got a different date reading without context.
- Cited, not combinable with the above (rule 4d): Uber says it does not over-index on ~5% run-to-run change (UBR-1, a number from its own system).
- Not shown: how many repeats are enough. Two is what we did.

**Step 4. Open the SQL, or the stated basis, behind every answer, and check which date, status and unit it used.** Status: both.
- Ours: A: 8 of 8 answers came back with SQL (F16); 5 of 8 answer texts named the date that set their scope (F15), 3 did not (A-4); for Q6 and Q8 a person read the date from the SQL (A-3, MR-Q6, MR-Q8). P2: 12 of 12 answers had SQL (F05), 11 of 12 named the date basis in the text (F04), all 12 SQL filter on a named date column (F06). This shows the SQL let a person classify an ambiguous answer; it doesn't show a tool that hides SQL fails.
- Cited: Anthropic's grader can judge the agent's query, not only its number, plus a provenance footer (reading; re-open). Uber scores query similarity to golden SQL (reading). LinkedIn scores table recall and column recall (LIN-13, LIN-14).
- Product claim "Dot returns SQL with its answers": evidenced by A and P2 as above (rule 5).

**Step 5. Ask your follow-ups inside the same chat, then ask the first question again in a fresh one.** Status: run of ours (one chain, one dataset); no census publication read for it.
- A: Q5 ("Going back to my first question") returned 43,428, matching Q1 four turns earlier (MR-Q1, MR-Q5, F04). Q8 kept Q7's delivery-date scope (A Finding 1). A fresh-chat control did not reproduce the chain (step 3). Do not say Dot re-ran the query or stored the figure: not observable (A, v1.6.6).
- Nothing in B's section 7 describes testing follow-up questions. Not claimed as common practice.

**Step 6. Mark by hand first, and classify each gap as display rounding or a real disagreement before counting it.** Status: both.
- Ours: A MR-Q3 (5.6 vs 5.64843, 0.8574%) and MR-Q4 (7.7 vs 7.725972, 0.3362%) were display rounding, recorded as such (hard rule 12); P2 MR-Q6 and MR-Q12 the same.
- Cited: ClickHouse: 84.9% of scored result sets matched only through a column-linked mapping (CLK-13), so strict matching would have marked most as wrong. Hex: its LLM judge accepted a 0.01 percentage-point difference 35% of the time (HEX-3). LinkedIn: LLM judge within 1 point of the human score 75% of the time (LIN-6, LIN-7), with expert review every 3 months (LIN-5). Census: 7 of 13 use an LLM judge (C-5).
- Do not say: that an LLM judge can replace the hand-marking. Evidence shows it disagrees with humans on a quarter of cases (LinkedIn) or sometimes too leniently (Hex).

**Step 7. Set a pass bar before you test, and decide what happens below it.** Status: cited publication, one publisher (practice, not shown to work).
- Anthropic: a domain owner cannot announce the agent until its eval slice clears a threshold, initially ~90% (ANT-13); census: only 1 of 13 publishes a numeric launch gate (C-8). Anthropic reports above 95% aggregate accuracy with skills (ANT-2); that is an outcome, not evidence the bar caused it.
- Querio's 90% (reading, advice) is not a test. The value is untested: no publication shows 90% is the right bar.
- Dot's own stated behaviour (merge re-checks 25 questions at 95% or more, DOT-4, DOT-5) is Dot's page, an illustration, pending Rick's sign-off (PLAN.md section B). Quote as stated behaviour only.

**Step 8. Re-run the same set after every change to your data model or context, and on a schedule.** Status: cited publication (practice by named companies; one reported detection).
- Anthropic: offline accuracy drifted from ~95% at launch to ~65% over a month without skill maintenance (ANT-5, ANT-6); evals touching a changed dependency re-run in CI (reading; re-open). Dot's own essay "Your AI Analyst Will Be Worse Next Month" covers the drift (named in PLAN.md; not opened here, must be opened before citing).
- Census: 5 of 13 re-run on every change, before each deploy or daily (C-6): Anthropic, Uber (Finch), Hex (daily), GitHub, Salesforce.
- No run of ours re-ran after a change. Nothing from our runs supports this step.
- Do not say: that re-running prevents drift. Anthropic reports the drift and its fix (skill maintenance, ANT-7: ~90% of data-model PRs include a skill change); re-running only detected it.

**Step 9. Include a question your data cannot answer and check the analyst says so.** Status: cited, thin, untested by us.
- Anthropic, verbatim quote in B: "Design for null results." Prosus describes a safeguard (indicates when it can't find an answer; no evaluation, no figures).
- No run of ours asked an unanswerable question (all 8 and all 12 were answered; the rehearsal's refusal is barred, rule 4). **Cut, or label untested.**

### Which steps must be cut or labelled

- **Cut or label untested:** step 9 (one quoted line, no test); any claim that a stated definition, context note or semantic layer fixes ambiguity or drift (no run of ours tested it; A's and P2's notes were on throughout and answers still diverged); any number for "how many questions" (the census sizes range from 5 queries, VER-1, to 201 questions, CLK-1; no source shows a small set suffices, so PLAN.md's LinkedIn post 4, "you don't need 50-100 questions", is not supported); any "right" pass threshold (90% is one company's initial choice); any cost per answer (conditions waived).
- **Thin, keep with "done by" wording:** steps 1, 7 and 8 (practice by named organisations; nothing shows it works). Step 5 rests on one chain of 5 questions and one fresh control; keep with the sample stated.
- **Strongest:** steps 2, 3, 4, 6 (a run of ours plus at least one published number).
- **Not combinable (rule 4d):** step 3's ours with UBR-1; step 6's ours with CLK-13, HEX-3, LIN-6.
- **Re-open before quoting:** every quotation in this section came through WebFetch's model-written reading (B's section 7); only the ones B returned in quotation marks may be quoted, after re-opening.
- **Hand-recorded conditions:** nothing above rests on mode, credits, environment or notes.

## 8. Sources as CSV

```csv
source,url_or_tool,what_it_showed,date
Search Console rows,data/ahrefs/search-console-queries.csv,No row relates to testing or accuracy; nearest topic neighbour conversational analytics 0 clicks 384 impressions position 25.8,read 1 November 2026
Keywords Explorer,data/ahrefs/keywords.csv,ai data analyst US 700 global 2.0K difficulty 22; text to sql accuracy US 10 global 10 difficulty not measured; how to evaluate ai data analyst accuracy not indexed; ai data analyst accuracy not indexed (same rows B read 31 October 2026),"Ahrefs, 27-28 October 2026"
AI answers,measure/citations.md,Question not matched (file tracks Evaluating accuracy by label only); not measured for this question; latest reading is Day 0 Perplexity free app: Dot 5 datafact 8 bygravity 4 getbruin 1 aianalystlab 1 (markers not pages; no full answers held),read 1 November 2026
Ranking page 1,https://www.getdbt.com/blog/data-culture-ai-analytics-agent-trust-context,dbt Labs 2026-10-26; vendor blog and conference recap; reports Data Culture results (self-reported; second-hand); evidence; read via WebFetch (model reading),WebSearch order as run 1 November 2026
Ranking page 2,https://www.getdbt.com/dbt-summit/sessions/dont-ship-what-you-cant-measure-evaluation-driven-development-for-ai-analytics-agents,dbt Summit session description 18 Sep 2026; advice; no results,WebSearch order as run 1 November 2026
Ranking page 3,https://querio.ai/articles/evaluate-ai-data-analyst-framework-open-benchmarks,Querio vendor blog 9 Sep 2026; advice; 50-100 questions 0-3 scoring 90% thresholds; no test run,WebSearch order as run 1 November 2026
Plan,PLAN.md,Section F names this slug; may cite A's run and piece 2's archived run; no claim from waived conditions; 5-9 steps,read 1 November 2026
Census (B),runs/how-companies-test-ai-data-analysts-research.md section 7; figures/how-companies-test-ai-data-analysts-figures.csv,13 organisations on the wider bar and 5 on the strict bar; IDs ANT LIN UBR CLK HEX CLK C-4 C-5 C-6 C-8 used per step (read via WebFetch by B 31 October 2026; re-open before quoting),read 1 November 2026
Piece A run,runs/ai-analyst-follow-up-questions-run.md; figures/ai-analyst-follow-up-questions-figures.csv,8 questions 3 chats; Q5 repeated Q1 figure 43428; Q6 fresh chat gave 1762 vs chain 2453; 8 answers with SQL; conditions hand-recorded rule 14 waived,31 October 2026 run; read 1 November 2026
Piece 2 run,runs/ai-analyst-shows-sql-run.md; figures/ai-analyst-shows-sql-figures.csv; figures/ai-analyst-shows-sql-truth.csv,6 questions x 2 fresh chats; 5 of 6 pairs same; late orders 2878 vs 2453; 12 of 12 SQL; 3 of 12 correct only under stated rival definition; conditions hand-recorded rule 14 waived,31 October 2026 run; read 1 November 2026
Dataset and licence,facts/dot-facts.md A10 L1 L2 (as cited in the run files),Olist CC BY-NC-SA 4.0 an Assumption never verified at source; publication decision L1 L2 by Saurabh,as recorded in the run files read 1 November 2026
```
