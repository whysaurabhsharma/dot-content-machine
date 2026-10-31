# Research: "How do I test whether an AI data analyst gives correct answers before rolling it out?"

Piece slug: `how-companies-test-ai-data-analysts` · Format: teardown (taken from the caller's message; the manifest is not written yet) · Bank #35 · Date: 31 October 2026 (section 7 re-run against the wider bar, same day)

## 1. The gap chain

- **What the buyer asks:** "How do I test whether an AI data analyst gives correct answers before rolling it out?"
- **What they find today:** advice. The top three pages for the main phrasing (WebSearch order, 31 October 2026) are a dbt Labs blog post that reports one consultancy's measured results (mostly evidence, self-reported, second-hand: dbt Labs writing about Data Culture's talk), a dbt Summit session abstract (advice, no numbers), and a Querio vendor guide (advice, no tests run).
- **Who gets cited in AI answers:** not measured. `measure/citations.md` tracks three buyer questions by topic label only; its question 1 is labelled "Evaluating accuracy" and the buyer's wording is not recorded, so it cannot be matched to this question and no count is borrowed. For the human's information, the file's latest reading (Day 0, 27 October 2026, Perplexity free app, citation markers, not pages) on that label: Dot 5 (the AI Data Analyst Playbook), datafact 8, bygravity 4, getbruin 1, aianalystlab 1. The file holds marker counts only, not the answers in full; nothing was recounted or reconstructed.
- **The gap:** advice only. The pages that rank say "build a golden set"; none of the three shows several organisations' real methods side by side.
- **What only Dot can show:** nothing from a Dot run is needed (PLAN.md: B needs no new Dot run). What the piece offers is a census of primary publications. A Dot-specific angle exists only through "Where Dot fits".

## 2. The words buyers type

All from the inputs; Ahrefs, 27-28 October 2026.

| Phrase | volume_us | volume_global | difficulty |
|---|---|---|---|
| text to sql accuracy | 10 | 10 | not measured |
| ai data analyst accuracy | not indexed | not indexed | not measured |
| how to evaluate ai data analyst accuracy | not indexed | not indexed | not measured |
| ai data analyst | 700 | 2.0K | 22 |

Search Console (file read, 31 October 2026): no row relates to testing or accuracy. The closest, "conversational analytics" (0 clicks, 384 impressions, position 25.8), is a topic neighbour, not this question. Page titles seen: "How to Eval an AI Data Analyst", "Don't ship what you can't measure: Evaluation-driven development for AI analytics agents".

## 3. The run

No Dot run. Teardown format; PLAN.md says B's figures are `published: <URL>, read <date>` rows and none is combined with Dot's own figures (hard rule 4, condition d). Dataset and licence (hard rule 9): none; no data is analysed. Mode, credits, environment and context-note screenshots (runs/README.md#screenshots): not applicable, no batch. Playbook stage: the evaluation stage ("evaluating accuracy", per the citations label); not confirmed against the Playbook text, which I did not read. The figures the piece may use are those copied in section 7.

## 4. Sources rows

See section 8 (CSV). Plan read: PLAN.md, section B (teardown). It names this slug. It sets: section 7 is a census of primary publications; go if five or more meet the bar. The bar was widened on 31 October 2026 by Saurabh (see section 7) and the go bar is now eight.

## 5. Stop conditions

None applies. Evidence in the form of one organisation's methods exists, but the buyer has no side-by-side view. Dot's own data is not needed.

## 6. Verdict

**PIECE.** Rule given by Saurabh (31 October 2026): PIECE if N is 8 or more, NOT A PIECE if N is under 8. N = 13 on the wider bar (12 if Grab, the softest entry, is dropped; 10 even if the three newest additions are all dropped); strict bar M = 5. Two judgment calls are the human's: whether Grab Bench counts, and whether customer-facing evaluation tooling (Databricks, Microsoft Fabric, Google Prism) counts; neither changes the verdict.

## 7. Sources

Census date: 31 October 2026. Every page below was opened with WebFetch. WebFetch returns a model-written reading of the page, not raw text, so verbatim quotes are only those the reading returned in quotation marks; re-open each URL before quoting. Primary sources only (organisation's own blog, paper or docs); no getdot.ai teardown, newsletter, news article or secondary summary was used for any entry.

**Bars.** Strict bar (first census): the publication states what they test against, how they score, and when they run it. Wider bar (Saurabh, 31 October 2026): the organisation's primary publication says something checkable about how it verifies its own AI data analyst / text-to-SQL / data agent's answers, with at least one of (a) a named method, (b) a measured accuracy figure for its own system, (c) a described test set. Customer-facing evaluation tooling (how customers should test their agents, not how the vendor tests its own) is not counted; it is listed separately below.

### Meets the wider bar (13)

Entries 1-5 also met the strict bar. Entries 6-13 meet the wider bar only.

**1. Anthropic** (strict: yes; wider: a, b, c)
- URL: https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude
- Publisher and date: Anthropic PBC (claude.com blog); authors Josh Cherry, Clement Peng, Johanne Jiao, Justin Leder, Chen Chang; 3 June 2026.
- What they tested: their own Claude-based analytics agent over their data warehouse.
- Against: "Offline evals are question-and-answer pairs." Dashboard-based evals are generated by Claude and validated by humans; long-tail evals are generated from business context (roadmaps, table docs); stakeholder corrections in threads are harvested as candidate evals. Ground truth is anchored to a snapshot date, a stable fact table, or grading of the query rather than the number.
- Scoring: grader can judge the agent's query, not only its number; per-assertion pass/fail per run; online, a provenance footer plus share of queries resolved through the semantic layer and share of responses with correction language.
- When: before launch (a domain owner cannot announce the agent until their eval slice clears a threshold, initially about 90%); per change (before/after run on the relevant slice; evals touching a changed dependency re-run in CI); continuously (results stored like telemetry, passive monitoring reviewed weekly, corrections harvested every few hours).
- Quotes (verbatim): "Design for null results." · "Treat skill maintenance as a first class citizen" · "Offline eval accuracy should be ~100%".
- Numbers: 21% (maximum accuracy on their evals without skills); above 95% aggregate with skills, ~99% in certain domains; 95% (share of business analytics queries automated via Claude); ~95% to ~65% (offline accuracy drop in one month without skill maintenance); ~90% (share of data-model PRs that include a skill change); +6% accuracy, +32% tokens, +72% latency (adversarial review); under 1 point (accuracy change from grep access to thousands of prior SQL files); ~80% (share of wrong answers where the correct answer was present in the corpus); ~90% (initial launch threshold per domain eval slice); ~100% (target offline eval accuracy); three (consecutive net-negative doc refinement iterations); a few dozen (evals per topic before diminishing returns); an hour (runtime per ablation run).

**2. LinkedIn (SQL Bot)** (strict: yes; wider: a, b, c)
- URLs: https://www.linkedin.com/blog/engineering/ai/practical-text-to-sql-for-data-analytics (blog); https://arxiv.org/html/2507.14372v1 (paper)
- Publisher and date: LinkedIn Engineering Blog, Albert Chen and 18 co-authors, 9 December 2024. Paper: "Text-to-SQL for Enterprise Data Analytics", arXiv:2507.14372v1, 18 July 2025, authors from LinkedIn (Sunnyvale), Workshop on Agentic AI for Enterprise at KDD '25, 4 August 2025.
- What they tested: their internal SQL Bot / data chatbot.
- Against: an internal benchmark. Blog: "We collaborated with domain experts across 10 product areas to define a set of over 130 benchmark questions." Paper: "We asked product area domain experts in our company to provide questions and ground truth queries"; 133 questions, 10 product areas, 167 ground-truth tables; 60% of questions have more than one valid response.
- Scoring: automated table and field recall, hallucination rate, syntax correctness, latency; query accuracy by human evaluation plus LLM-as-a-judge (gpt-4o-2024-05-13 in the paper) on a 1-5 rubric (5 perfect; 4 close with minor logic issues such as an incorrect date filter; 3 right tables and most columns; 2 right tables, mostly wrong columns; 1 wrong). Paper: execution accuracy "does not account for other valid output formats". Quotes (verbatim, blog): "it does not require data access, allows us to assess how close the query is to being correct" · "we've found that it returns a score within 1 point of the human score 75% of the time" · "Without these additional answers, we underreported recall by 10-15%."
- When: described as ongoing benchmarking; experts review the benchmark every 3 months; disagreements between judge and humans are investigated. No schedule for the automated metrics. Paper: each ablation run once at temperature 0.
- Numbers, blog: 130+ benchmark questions; 10 product areas; ~60% of questions with more than one accepted answer; 10-15% (recall underreported without them); every 3 months (expert review); 1 point and 75% (judge within 1 point of human, share of cases); ~95% of survey respondents rated query accuracy "Passes" or above and ~40% "Very Good" or "Excellent" (a user survey, not the benchmark); 5-10x (adoption increase from DARWIN integration); 80% of sessions (from "Fix with AI"); over 1 year building.
- Numbers, paper (benchmark, "Full" configuration, Table 2): table recall 78% of ground-truth tables; column recall 56% of ground-truth columns; score 4+ on 48% of answers; successful compilation 96% of queries; valid tables and columns 99% of queries; schemas-only baseline 9% scored 4+; per response 4.6 LLM calls, 3.0 EBR queries, 9.4 database queries; under 60 seconds per question. Expert review of the production version: 124 of 133 questions rated (~93%); 53% rated 4 or 5; 77% rated 3 or higher; incorrect filter the most common issue at 24% (denominator not stated); incorrect joins 4%. The paper's 53% (production, expert review) and 48% (Full ablation, benchmark) are different measures; do not set them against each other, or against the blog's ~95% survey.

**3. Uber (QueryGPT; Finch)** (strict: yes for QueryGPT; wider: a, c for both, b only partly)
- URLs: https://www.uber.com/blog/query-gpt ; https://www.uber.com/blog/unlocking-financial-insights-with-finch
- Publisher and date: Uber Engineering Blog. QueryGPT: Jeffrey Johnson, Callie Busch, Abhi Khune, 19 September 2024. Finch: Eddie Huang, Taya Yusuf, Tim Ross, 17 July 2025.
- What they tested: their own text-to-SQL tool (QueryGPT) and finance data agent (Finch).
- Against (QueryGPT): "identified a set of real questions from the QueryGPT logs, and manually verified the correct intent, schemas required to answer the question, and the golden SQL." Two flows: "Vanilla" (baseline, end to end) and "Decoupled" (supplies the actual intent and datasets so each component is evaluated alone).
- Scoring (QueryGPT): per question, intent accuracy; table overlap (0 to 1; example 0.5 when one of two required tables is chosen); successful run; run has output (more than 0 records); qualitative query similarity (an LLM scores 0 to 1 against the golden SQL).
- When (QueryGPT): "production and staging environments", results tracked over time to "identify regressions and patterns revealing areas for improvement"; no fixed schedule given.
- Finch: sub-agents checked against expected responses; the output of a generated query compared with a "golden" reference query's output; supervisor routing accuracy checked; simulated end-to-end queries; historical queries re-run before system prompt or model changes are deployed. Finch gives no scores or test-set sizes.
- Numbers (QueryGPT; as read): ~5% run-to-run variation the team does not over-index on; 0 to 1 (scale for table overlap and similarity); ~300 daily active users in the limited release; 78% of users reported generated queries cut their SQL-writing time; 1.2 million interactive queries per month on the platform; 10 minutes (estimated manual authoring time) vs 3 minutes (QueryGPT); 7 tier-1 tables and 20 SQL queries in the v1 sample set; 20+ algorithm iterations. Finch: none that measure accuracy.
- Stated limits: LLM non-determinism; the question set cannot cover every business question; more than one correct SQL may exist.

**4. ClickHouse (DWAINE)** (strict: yes; wider: a, b, c)
- URL: https://clickhouse.com/blog/agentic-analytics-benchmark-data-agent-mnist
- Publisher and date: ClickHouse blog; Eduardo Vellasques and Al Brown; page header 1 September 2026, metadata 10 September 2026 (the two disagree).
- What they tested: models inside "ClickHouse's internal analytics agent" (DWAINE), using its production traffic.
- Against: 201 questions from DWAINE production traffic, run on an anonymised synthetic reconstruction of ClickHouse's warehouse (18 tables, 865 columns, two dbt layers). Ground truth: three models from three providers solved each question; an answer became ground truth if at least two agreed; three-way disagreements were dropped (39 questions).
- Scoring: a candidate is correct when its result set matches ground truth under column-linked equivalence (column linking, row alignment, numeric tolerance). A three-seat LLM jury (Anthropic, OpenAI, Google; each seat excludes the candidate's own family) decides by majority.
- When: a benchmark run once per model round, with August 2026 public API pricing; not a recurring test. The harness is open source so others can run it on their own warehouse.
- Numbers (as read; model names are as the reading gave them): 76.6% pass rate for the top model across 201 questions; 65.7% for DeepSeek V4 Flash; 29 models; $1 vs $52 full-run cost, with the correctness gap given as 6.9% in one place and 11 points in another (the post disagrees with itself); 51.7% of ground-truth answers unanimous; 39 questions dropped; 501 to 475 to 243 to 204 to 201 candidate questions after each filtering stage; 84.9% of scored result sets matched only through column-linked mapping; 0 of 670 entity-recovery attempts gave an exact match (27 models). Caveat the authors give: ground truth is model agreement, not human audit.

**5. Hex** (strict: yes; wider: a, c; no accuracy figure for its own agents)
- URL: https://hex.tech/blog/evaluate-data-agents/
- Publisher and date: Hex; Izzy Miller (Engineering Research); 22 May 2026. Vendor describing evaluation of its own agents (Notebook Agent, Generative Apps), a method, not an accuracy claim.
- Against: a synthetic company, Shorelane Commerce, built from data generators, dbt models, documentation, events and stakeholder personas; small eval sets with preconfigured rubrics and ground truths.
- Scoring: rubrics that are deterministic, LLM-judged or hybrid (examples named: ToolEfficiency, SemanticLayerUsage, WorkspaceGuideAdherence); "hypothesis objective" rubrics compare a candidate run to a baseline side by side; locally run candidates compared with remotely run production baselines.
- When: "eval sets run daily to establish shared “production baselines”"; ad hoc and scheduled runs for experiments.
- Quote (verbatim): "We are biased towards being overly harsh" (about the LLM judge, which the post says is still not well calibrated).
- Numbers: 2.03% vs 2.04% (example values in one eval, 2.04% correct); 0.01 percentage points (difference the judge sometimes accepted); 35% (share of judgments in which it accepted that difference). Scene-setting numbers about the fictional company (about $129M yearly revenue, 30,000 handcrafted lines, six years of data) are not evaluation results. The post reports no accuracy scores for Hex's agents.

**6. Snowflake (Cortex Analyst)** (strict: no, no run timing; wider: a, b, c)
- URLs, all read in full: https://www.snowflake.com/en/engineering-blog/cortex-analyst-text-to-sql-accuracy-bi/ (Renee Huang, 29 August 2024); https://www.snowflake.com/en/engineering-blog/agentic-semantic-model-text-to-sql (Tom Zayats, 31 March 2025); https://snowflake.com/en/engineering-blog/snowflake-cortex-analyst-behind-the-scenes (Nipun Sehrawat, 14 August 2024).
- Publisher: Snowflake Inc. Engineering Blog. A vendor evaluating a product it sells.
- Published: a 150-question internal benchmark with human-selected gold queries; column precision and recall; in 2025, four BIRD dev subsets with a two-step LLM judge. The August 2024 "behind the scenes" post says "We have a comprehensive internal benchmark suite that is representative of real-world, business intelligence-style questions" (reading cut the quote at its length limit), gives no test-set size, no run timing, and says a future post will cover benchmark details.
- Numbers as read: 150 questions (internal benchmark); 90%+ SQL accuracy claimed ("achieves more than 90%+ SQL accuracy on real-world use cases"); 51% (GPT-4o on the internal set); 392 questions across four BIRD subsets; 57% vanilla vs 78% Cortex Analyst average (unweighted, 21 percentage points); "close to 2x more accurate than single-shot SQL generation" (GPT-4o) and roughly 14% higher accuracy than another text-to-SQL product (behind-the-scenes post; basis for comparison not stated in the reading).

**7. GitHub (Qubot)** (strict: no, scoring method not stated; wider: a, c partly)
- URL: https://github.blog/ai-and-ml/github-copilot/how-we-built-an-internal-data-analytics-agent/
- Publisher and date: GitHub Blog; Matteo Vasirani and Cynthia Joseph; 19 June 2026.
- Published: a test set where each case has a known correct answer, ground-truth SQL, and domain and difficulty metadata (the contents are described; size and trial count are not given); it is run on every change to context or agent configuration, before release (a named method: regression testing before release). How accuracy is judged against ground truth is not stated.
- Numbers: "3x" faster to the right answer, no baseline. No accuracy figure.

**8. Salesforce (Horizon Agent)** (strict: no; wider: a, b weak)
- URL: https://www.salesforce.com/blog/text-to-sql-agent/
- Publisher and date: Salesforce blog; Nick Gibson; 27 May 2025.
- Published: names "automated regression testing" as a safeguard, without a test set or pass rates. States "At launch we only had the correct response ~50% of the time" with no method for how that was measured. The agent returns the SQL, answer and context in Slack (the reading from this census describes no further verification).
- Numbers: ~50% (share of correct responses at launch, method not stated).

**9. Vercel (d0)** (strict: no; wider: b, c)
- URL: https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools
- Publisher and date: Vercel blog; Andrew Qu; 22 December 2025.
- Published: benchmarked the old and new d0 architecture on 5 representative queries. Success is not defined and no run timing is given, so the figures are thin.
- Numbers: 5 queries; 80% vs 100% success (old vs new architecture). Not counted from the second post (https://vercel.com/blog/testing-if-bash-is-all-you-need, 22 January 2026), which is not an evaluation of d0.

**10. Ramp (Ramp Research)** (strict: no; wider: a, c partly)
- **Corrected 1 November 2026 (browser re-read): strict: yes.** The post states scoring ("asserts not only on the final answer but also the intermediate steps, including expected tool calls, table references, and query shape") and a trigger ("update context, run tests, and confirm improvements"). The WebFetch reading above missed both.
- URL: https://engineering.ramp.com/post/meet-ramp-research
- Publisher and date: Ramp engineering blog; the page as read shows no author or date.
- Published: domain experts wrote end-to-end tests; a Python mini-framework in the dbt project checks final answer, expected tool calls, table references and query shape. No scoring method, schedule or test-set size. Usage numbers (1,800+ questions answered) are not evaluation results.

**11. Prosus (Toqan Data Analyst)** (strict: no; wider: a)
- URL: https://www.prosus.com/news-insights/2024/democratising-data-analysis-with-toqan (also read as a 404: https://toqan.ai/blog/democratising-data-analysis-with-toqan; a Medium copy returned 403).
- Publisher and date: Prosus; no author stated; 1 October 2024; title "Democratising data analysis with Toqan".
- Published: three safeguards in the agent: it "asks people to clarify requests if needed", "mentions any assumptions it has made in the process", and "indicates when it can't find an answer to minimise false positives". No evaluation set, no accuracy figure for Toqan, no test count.
- Numbers: "85 to 90% accuracy" for plain LLMs on text-to-SQL, which the team judged insufficient; this describes LLMs before the agent approach, not Toqan.

**12. WisdomAI** (strict: no; wider: a, b, c partly)
- URL: https://www.wisdom.ai/blog/how-wisdom-gets-text-to-sql-right
- Publisher and date: WisdomAI; Sharvanath Pathak (CTO); the page body says 22 June 2026 and the metadata says 31 October 2026 (the two disagree). A vendor describing its own product.
- Published: accuracy measured in three phases (schema only; after uploading a knowledge base and column descriptions; after the system learns SQL from evaluation queries with ground-truth SQL hidden). Scoring: "a combination of heuristics over data matches, accounting for factors such as extra columns and row ordering," plus LLM-as-judge. Test set: the public `livesqlbench-base-full-v1`, query-only cases, 5 datasets; counts of questions not given. Internal evals use "LLM- and human-validated ground truth" with details deferred to another article (paraphrase of the reading, not a verbatim quote).
- Numbers as read: about 20% baseline, about 50% after knowledge-base files, about 85% after context learning (LiveSQLBench query-only subset, aggregate over 5 datasets); above 95% production accuracy "typically" after human review (a claim, method not given); 80-92% on the BIRD dev set with the learning loop; 48% for the top LiveSQLBench leaderboard entry (all case types, not comparable); worked examples: 352 rows returned vs 336 correct (solar_panel_10); $4,850 returned vs $1,541 correct (solar_panel_8).

**13. Grab (Grab Bench)** (strict: no; wider: a, softest entry)
- URL: https://engineering.grab.com/grab-bench-evaluating-ai
- Publisher and date: Grab Tech Engineering Blog; Christian Coffrant; 12 August 2026.
- Published: an eval harness for AI systems on Grab work, with SQL generation as one task surface. Named methods: LLM judges "are useful for open-ended tasks such as SQL, where correctness can depend on business intent and query shape"; deterministic scorers where the task contract allows; baselines (empty, schema-only and others); canaries (simple or malformed cases with known expected results); hidden splits (unseen certification cases). "Query generation cares about preserving metric and schema intent." No test-set size and no accuracy figures. It is about benchmarking models on Grab work generally, not a data analyst's answers specifically; whether it counts is the human's call.
- Numbers: none. (Grab's 94.15% on Spider2-snow, 515 of 547, reached me only through a secondary summary; its primary post was not found and is not used.)

### Checked, does not meet the wider bar

- **Databricks (Genie), customer-facing tooling.** https://www.databricks.com/blog/building-confidence-your-genie-space-benchmarks-and-ask-review (Hanlin Sun and Richard Tomlinson, 16 October 2024) and https://docs.databricks.com/aws/en/genie/benchmarks, both read in full. Describe benchmark questions with gold SQL, Correct / Needs Review labels, up to 500 benchmark questions per space, two to four phrasings per question, a 5,000-row comparison limit, an LLM judge in agent mode, and a human Request Review. It is how Databricks tells customers to test their own Genie spaces, not how Databricks verifies its own analyst; no accuracy figure or test set of its own. Would count as (a) if the human admits customer tooling.
- **Microsoft (Fabric data agent).** https://learn.microsoft.com/en-us/fabric/data-science/evaluate-data-agent (docs, updated 1 September 2026), read in full. A Python SDK for customers: question and expected-answer pairs, an LLM critic prompt, summary of correct, incorrect and unclear counts. Customer tooling in preview; no results. Would count as (a) if customer tooling is admitted.
- **Google Cloud (Prism).** https://cloud.google.com/blog/products/ai-machine-learning/run-evals-for-conversational-analytics-agents-using-prism (Kate Grinevskaja and Phil Meyers, 11 April 2026), read in full. "an open-source evaluation tool" with assertions, data checks, an AI judge and delta analysis; "It does not describe how Google evaluates its own agent" (the reading's words). No test-set sizes or figures. Would count as (a) if customer tooling is admitted.
- **Adyen (DABstep).** https://www.adyen.com/knowledge-hub/data-agent-benchmark-for-multi-step-reasoning-dabstep (4 February 2025, with Hugging Face), read (page truncated). A public benchmark of 450+ tasks with binary scoring, not Adyen testing its own analyst.
- **Data Culture (via dbt Labs).** https://www.getdbt.com/blog/data-culture-ai-analytics-agent-trust-context (dbt Labs, 26 October 2026), read in full. Golden questions, a four-tier comparison, an LLM judge and accuracy from 0% to 94.7% on an e-commerce client, but it is dbt Labs reporting a talk, a secondary source. The talk page (https://www.getdbt.com/dbt-summit/sessions/dont-ship-what-you-cant-measure-evaluation-driven-development-for-ai-analytics-agents, 18 September 2026) is an abstract with no numbers. No primary Data Culture publication found.
- **Instacart (Ava).** https://company.instacart.com/tech-innovation/scaling-productivity-with-ava-instacarts-internal-ai-assistant (Zain Adil, Kevin Lei, Ada Cohen, 7 September 2023), read in full. No method, figure or test set for data or SQL answers; the one verification line concerns Slack summaries posted publicly so participants can check them. Knowledge retrieval and code execution described as future work. (The tech.instacart.com copy failed, 403; the SQL-interview post and the customer-support LACE post are not about verifying a data analyst.)
- **Pinterest.** https://medium.com/pinterest-engineering/how-we-built-text-to-sql-at-pinterest-30bad30dabff : FAILED, HTTP 403 again this run (also on pinterest-engineering.medium.com and the 2026 "unified-context-intent-embeddings" post, 403 in the earlier run). Pinterest's community post (https://community.pinterest.biz/t/pinterest-s-secret-sauce-for-fast-accurate-data-answers/43918.md, 24 March 2026) was read and has no evaluation detail. Not counted.
- **OpenAI (in-house data agent).** https://openai.com/index/inside-our-in-house-data-agent/ : FAILED, HTTP 403 (also the de-DE copy earlier, and the no-trailing-slash form this run). Only secondary summaries found. Not counted.
- **Netflix (LORE).** FAILED. The LORE post is part of Netflix's analytics-engineering survey series; https://netflixtechblog.com/part-1-a-survey-of-analytics-engineering-work-at-netflix-d761cfd551ee and the netflixtechblog.medium.com form both returned HTTP 403. (I did not confirm that URL is the LORE post; it came from a search result title.) Not counted.
- **Delivery Hero (QueryAnswerBird).** https://deliveryhero.jobs/?p=11367 : FAILED, HTTP 403. Not counted.
- **Swiggy (Hermes).** https://bytes.swiggy.com/hermes-v3-building-swiggys-conversational-ai-analyst-a41057a2279d and the V1 post: FAILED (fetch error, no output, both URL forms) in the earlier run; not retried. Not counted.
- **Fiverr (Simon).** https://medium.com/fiverr-engineering/democratize-data-and-information-with-text-to-code-models-text2sql-cb6beff6f820 : FAILED, HTTP 403 (earlier run). Not counted.
- **Stripe, Airbnb, DoorDash.** Searched on 31 October 2026 (site-restricted and plain queries); no primary publication about verifying an internal data analyst found. Stripe's docs pages found describe its MCP server and Sigma assistant, not an evaluation (not opened beyond search snippets). Not counted.
- **Lyft, Spotify, Gorgias, Wix, Booking, Zalando, Shopify, Mercari, Meta, Block, Atlassian, Notion, Cloudflare, Slack, Zomato, Meesho, Flipkart, Mercado Libre, Rappi, Gojek, AWS.** Searched (several searches, none exhaustive); no primary publication found. Not counted.
- **Ramp, other posts.** site:engineering.ramp.com search returned nothing from the domain.
- **Non-primary or non-own-system results seen and not opened or not counted:** deepset ("using generative AI to query large BI tables", an evaluation of approaches, not their own analyst; not opened), Lamini (vendor marketing; not opened), Querio, BlazeSQL and datalakehousehub guides (advice).

Organisations meeting the wider bar: 13 (strict bar: 5)

## 8. Sources as CSV

```csv
source,url_or_tool,what_it_showed,date
Search Console rows,data/ahrefs/search-console-queries.csv,No row relates to testing or accuracy; nearest topic neighbour conversational analytics 0 clicks 384 impressions position 25.8,read 31 October 2026
Keywords Explorer,data/ahrefs/keywords.csv,text to sql accuracy US 10 global 10 difficulty not measured; ai data analyst accuracy not indexed; how to evaluate ai data analyst accuracy not indexed; ai data analyst US 700 global 2.0K difficulty 22,"Ahrefs, 27-28 October 2026"
AI answers,measure/citations.md,Question not matched (file tracks "Evaluating accuracy" by label only); not measured for this question; nearest Day 0 reading Perplexity free app: Dot 5 datafact 8 bygravity 4 getbruin 1 aianalystlab 1 (markers not pages; no full answers held),read 31 October 2026
Ranking page 1,https://www.getdbt.com/blog/data-culture-ai-analytics-agent-trust-context,dbt Labs 26 Oct 2026; reports Data Culture golden-question results; mostly evidence but self-reported and second-hand,"WebSearch order as run 31 October 2026"
Ranking page 2,https://www.getdbt.com/dbt-summit/sessions/dont-ship-what-you-cant-measure-evaluation-driven-development-for-ai-analytics-agents,dbt Summit session abstract 18 Sep 2026; advice; no numbers,"WebSearch order as run 31 October 2026"
Ranking page 3,https://querio.ai/articles/evaluate-ai-data-analyst-framework-open-benchmarks,Querio vendor guide 9 Sep 2026; advice; thresholds such as 90% accuracy; no tests run,"WebSearch order as run 31 October 2026"
Plan,PLAN.md,Section B names this slug; section 7 is a census of primary publications; go bar later set to 8 on the wider criteria by Saurabh,read 31 October 2026
Census Anthropic,https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude,Meets strict and wider bar: Q&A eval pairs; per-assertion grading; gate ~90% before launch; per-change and continuous; 3 June 2026,read 31 October 2026
Census LinkedIn blog,https://www.linkedin.com/blog/engineering/ai/practical-text-to-sql-for-data-analytics,Meets strict and wider: 130+ expert-written benchmark questions; human plus LLM judge; reviewed every 3 months; 9 Dec 2024,read 31 October 2026
Census LinkedIn paper,https://arxiv.org/html/2507.14372v1,Meets strict and wider: 133 questions 167 tables; 1-5 rubric; 53% rated 4 or 5 in production review; 18 Jul 2025,read 31 October 2026
Census Uber QueryGPT,https://www.uber.com/blog/query-gpt,Meets strict and wider: golden question-to-SQL set from logs; five signals; staging and production; 19 Sep 2024,read 31 October 2026
Census Uber Finch,https://www.uber.com/blog/unlocking-financial-insights-with-finch,Method only (golden query output comparison; regression before deploy); no numbers; 17 Jul 2025,read 31 October 2026
Census ClickHouse,https://clickhouse.com/blog/agentic-analytics-benchmark-data-agent-mnist,Meets strict and wider: 201 production questions; two-of-three model ground truth; LLM jury; 76.6% top; Sep 2026,read 31 October 2026
Census Hex,https://hex.tech/blog/evaluate-data-agents/,Meets strict and wider (a and c): synthetic company eval sets; deterministic and LLM rubrics; run daily; 22 May 2026,read 31 October 2026
Wider Snowflake 2024,https://www.snowflake.com/en/engineering-blog/cortex-analyst-text-to-sql-accuracy-bi/,Wider bar a b c: 150-question internal benchmark; 51% GPT-4o; no run timing; 29 Aug 2024,read 31 October 2026
Wider Snowflake 2025,https://www.snowflake.com/en/engineering-blog/agentic-semantic-model-text-to-sql,Wider bar: BIRD subsets and LLM judge; 57% vs 78%; 31 Mar 2025,read 31 October 2026
Wider Snowflake behind the scenes,https://snowflake.com/en/engineering-blog/snowflake-cortex-analyst-behind-the-scenes,Wider bar b: internal benchmark suite; 90%+ SQL accuracy claimed; no test-set size; 14 Aug 2024,read 31 October 2026
Wider GitHub,https://github.blog/ai-and-ml/github-copilot/how-we-built-an-internal-data-analytics-agent/,Wider bar a c: test set with ground-truth SQL; run on every change before release; scoring not explained; 19 Jun 2026,read 31 October 2026
Wider Salesforce,https://www.salesforce.com/blog/text-to-sql-agent/,Wider bar a b weak: automated regression testing named; ~50% correct at launch with no method; 27 May 2025,read 31 October 2026
Wider Vercel,https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools,Wider bar b c: 5 queries; 80% vs 100% success; success undefined; 22 Dec 2025,read 31 October 2026
Not counted Vercel second post,https://vercel.com/blog/testing-if-bash-is-all-you-need,Not an evaluation of d0; 22 Jan 2026,read 31 October 2026
Wider Ramp,https://engineering.ramp.com/post/meet-ramp-research,Wider bar a c: expert-written end-to-end tests; mini-framework checks answer tool calls tables query shape; no date shown,read 31 October 2026
Wider Prosus Toqan,https://www.prosus.com/news-insights/2024/democratising-data-analysis-with-toqan,Wider bar a: clarifying questions; assumption disclosure; abstention when unsure; no figures; 1 Oct 2024,read 31 October 2026
Wider WisdomAI,https://www.wisdom.ai/blog/how-wisdom-gets-text-to-sql-right,Wider bar a b c: three-phase accuracy on LiveSQLBench; ~20% to ~85%; heuristics plus LLM judge; 22 Jun 2026 (metadata 31 Oct 2026),read 31 October 2026
Wider Grab Bench,https://engineering.grab.com/grab-bench-evaluating-ai,Wider bar a (softest): LLM judges for SQL; canaries; hidden splits; no sizes or figures; 12 Aug 2026,read 31 October 2026
Customer tooling Databricks blog,https://www.databricks.com/blog/building-confidence-your-genie-space-benchmarks-and-ask-review,Customer-facing benchmarks with gold SQL and Request Review; no figures; not counted; 16 Oct 2024,read 31 October 2026
Customer tooling Databricks docs,https://docs.databricks.com/aws/en/genie/benchmarks,Up to 500 benchmark questions; chat and agent modes; not counted,read 31 October 2026
Customer tooling Microsoft,https://learn.microsoft.com/en-us/fabric/data-science/evaluate-data-agent,Fabric SDK ground-truth evaluation with LLM critic; customer tool; not counted; updated 1 Sep 2026,read 31 October 2026
Customer tooling Google Prism,https://cloud.google.com/blog/products/ai-machine-learning/run-evals-for-conversational-analytics-agents-using-prism,Open-source tool for customers; not Google's own testing; 11 Apr 2026,read 31 October 2026
Not meeting Adyen,https://www.adyen.com/knowledge-hub/data-agent-benchmark-for-multi-step-reasoning-dabstep,Public benchmark; not Adyen's own analyst; 4 Feb 2025,read 31 October 2026
Not meeting Instacart,https://company.instacart.com/tech-innovation/scaling-productivity-with-ava-instacarts-internal-ai-assistant,No verification method or figures for data answers; 7 Sep 2023,read 31 October 2026
Not meeting Pinterest community,https://community.pinterest.biz/t/pinterest-s-secret-sauce-for-fast-accurate-data-answers/43918.md,No evaluation detail; 24 Mar 2026,read 31 October 2026
Failed to load Pinterest,https://medium.com/pinterest-engineering/how-we-built-text-to-sql-at-pinterest-30bad30dabff,HTTP 403 on both runs (also alternate host and 2026 post),attempted 31 October 2026
Failed to load OpenAI,https://openai.com/index/inside-our-in-house-data-agent/,HTTP 403 (also de-DE copy and no-slash form),attempted 31 October 2026
Failed to load Netflix,https://netflixtechblog.com/part-1-a-survey-of-analytics-engineering-work-at-netflix-d761cfd551ee,HTTP 403 (also netflixtechblog.medium.com form); LORE post not confirmed,attempted 31 October 2026
Failed to load Instacart tech blog,https://tech.instacart.com/scaling-productivity-with-ava-instacarts-internal-ai-assistant-ed7f02558d84,HTTP 403; company.instacart.com copy read instead,attempted 31 October 2026
Failed to load Delivery Hero,https://deliveryhero.jobs/?p=11367,HTTP 403,attempted 31 October 2026
Failed to load Prosus Medium copy,https://medium.com/prosus-ai-tech-blog/just-ask-data-insights-for-everyone-a21057d24263,HTTP 403; prosus.com copy read instead (toqan.ai copy 404),attempted 31 October 2026
Failed to load Swiggy,https://bytes.swiggy.com/hermes-v3-building-swiggys-conversational-ai-analyst-a41057a2279d,Fetch error on V3 and V1 (earlier run),attempted 31 October 2026
Failed to load Fiverr,https://medium.com/fiverr-engineering/democratize-data-and-information-with-text-to-code-models-text2sql-cb6beff6f820,HTTP 403 (earlier run),attempted 31 October 2026
```
