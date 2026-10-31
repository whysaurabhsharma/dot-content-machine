---
title: "7 Companies Published Their AI Analysts' Accuracy. No Two Measured the Same Thing."
format: teardown
seo_title: "How 13 Companies Test Their AI Data Analysts"
meta: "13 companies published how they test their AI analyst. Seven gave an accuracy figure; no two measured the same thing. The five methods worth copying."
slug: how-companies-test-ai-data-analysts
query_data: "how to evaluate ai data analyst accuracy: not indexed (not measured). Related: ai data analyst 700 US, 2.0K global, difficulty 22; text to sql accuracy 10 US, difficulty not measured. Ahrefs, 27–28 October 2026"
reverse_links:
  - The AI Data Analyst Playbook (https://www.getdot.ai/blog/ai-data-analyst-playbook), on the stage that covers testing before rollout, anchor "how 13 companies test their AI analyst"
  - The Context Agent page (https://www.getdot.ai/context-agent), beside "measures Dot's accuracy", anchor "AI data analyst test questions"
  - The conversational analytics software post (https://www.getdot.ai/blog/conversational-analytics-software), anchor "test an AI analyst before rollout"
queries:
  - ai data analyst test questions
  - ai data analyst
  - text to sql accuracy
playbook_url: https://www.getdot.ai/blog/ai-data-analyst-playbook
figures: figures/how-companies-test-ai-data-analysts-figures.csv
dataset: "None for the census: 13 companies' own publications, each re-opened 31 October 2026; no dataset analysed and no Dot batch of its own. The Dot section cites piece A's run (runs/ai-analyst-follow-up-questions-run.md): Olist, CC BY-NC-SA 4.0, licence decision L1."
---

**We read how 13 companies, including Anthropic, LinkedIn and Uber, test their AI analysts: the internal agents staff use to ask data questions. Seven of the 13 published an accuracy figure, each measured differently: ClickHouse compared result sets, LinkedIn's experts rated answers, and Vercel counted undefined successes. By the end, you'll have one table of what all 13 measured, with the five that published enough to copy marked. Those five are the most complete descriptions, not proof of better testing.**

**The whole piece in eight lines:**

1. Of 13 companies that published how they test their AI analyst, 7 published an accuracy figure.
2. Each figure came from its own test set, scored its own way.
3. Five companies published enough to copy: what they test against, how they score and when they run it.
4. Of the 13, 8 build their test set from real questions or ground-truth answers.
5. A real question can have more than one right answer. About 60% of LinkedIn's benchmark questions do.
6. Anthropic, Uber, Hex, GitHub and Salesforce re-run their tests on a change, before each deploy, or daily.
7. Of the 13 publications, only Anthropic's states a bar to clear before launch that we found: about 90%, initially.
8. Our earlier run on Dot used the method's core: every expected answer computed before asking.

## The seven accuracy figures can't be compared

Seven of the 13 companies published an accuracy figure, and no two measured the same thing. LinkedIn reports the share of answers its experts rated highly. ClickHouse reports a pass rate for the best model on its own production questions. [Snowflake reports](https://www.snowflake.com/en/engineering-blog/cortex-analyst-text-to-sql-accuracy-bi/) 51% for GPT-4o on its internal evaluation set.

WisdomAI reports a public benchmark subset. Salesforce gives a share correct at launch but not how it was counted. [Vercel reports](https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools) 80% to 100% success on 5 queries without defining success. [Anthropic reports](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude) above 95% in aggregate with skills, and around 99% in certain domains.

None of the seven figures can be ranked against another, or against a vendor's claim. What carries across is the method.

[Dot publishes an accuracy figure too](https://www.getdot.ai/blog/from-10-to-90-percent-on-adyens-dabstep): 90% on a 30-task slice of Adyen's public DABstep benchmark. That figure doesn't compare with the others here either. Two figures compare only when they come from the same tasks, scored the same way, on systems set up the same way.

## Eight of 13 test against real questions

Eight of the 13 build their [AI analyst](https://www.getdot.ai/blog/conversational-analytics-software)'s test set from real questions or ground-truth answers. They are Anthropic, LinkedIn, Uber, ClickHouse, Snowflake, GitHub, Ramp and WisdomAI. Hex isn't counted: its ground truths sit on a synthetic company.

[LinkedIn](https://www.linkedin.com/blog/engineering/ai/practical-text-to-sql-for-data-analytics) asked domain experts in 10 product areas for over 130 questions, each with a ground-truth query. [Uber](https://www.uber.com/blog/query-gpt) took real questions from QueryGPT's logs and verified the golden SQL by hand. [ClickHouse](https://clickhouse.com/blog/agentic-analytics-benchmark-data-agent-mnist) built its set from its internal agent's production traffic.

Three of the 13 companies deal in print with questions that have more than one right answer. [About 60% of LinkedIn's benchmark questions](https://www.linkedin.com/blog/engineering/ai/practical-text-to-sql-for-data-analytics) have more than one accepted answer. Without those extra answers, LinkedIn "[underreported recall by 10-15%](https://www.linkedin.com/blog/engineering/ai/practical-text-to-sql-for-data-analytics)". Uber notes that a question can have more than one correct SQL query.

[ClickHouse's](https://clickhouse.com/blog/agentic-analytics-benchmark-data-agent-mnist) model panel dropped 39 of 243 candidate questions where no two models agreed. [A legal review](https://clickhouse.com/blog/agentic-analytics-benchmark-data-agent-mnist) then took 204 down to the final 201. LinkedIn's remedy is a calendar: experts review its benchmark every 3 months and add accepted answers.

## More than half score answers with an LLM judge

LinkedIn, Uber, ClickHouse, Hex, Snowflake, WisdomAI and Grab use an LLM to judge their analyst's answers. [Hex](https://hex.tech/blog/evaluate-data-agents/) built one eval where the right answer is 2.04% and a common wrong one is 2.03%. Hex's judge accepted the wrong one [35% of the time](https://hex.tech/blog/evaluate-data-agents/).

LinkedIn and Hex each publish one check on their judge, and the two checks measure different things. [LinkedIn's judge](https://www.linkedin.com/blog/engineering/ai/practical-text-to-sql-for-data-analytics) lands within 1 point of the human score 75% of the time. Of its LLM judge, Hex writes: "[We are biased towards being overly harsh.](https://hex.tech/blog/evaluate-data-agents/)"

Anthropic's post doesn't say what kind of grader it uses, so the count leaves it out. ClickHouse doesn't require an exact match. Its scorer links each answer's columns to the ground truth's, aligns the rows and allows a numeric tolerance. ClickHouse writes that "[84.9% of scored result sets in our test match only through the linked mapping](https://clickhouse.com/blog/agentic-analytics-benchmark-data-agent-mnist)".

## Anthropic's accuracy drifted within a month

[Anthropic reports](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude) that its offline accuracy drifted from about 95% at launch to about 65% over a month. [Dot's essay on accuracy decay](https://www.getdot.ai/blog/your-ai-analyst-will-be-worse-next-month) starts from that figure. Anthropic's case shows that a test passed at launch can say little about the same agent a month later.

Anthropic, Uber, Hex, GitHub and Salesforce re-run their tests on a change, before each deploy, or daily. Anthropic re-runs the affected evals in CI when a PR touches a dependency. [Uber's Finch](https://www.uber.com/blog/unlocking-financial-insights-with-finch) re-runs historical queries before a prompt or model update deploys. Ramp describes testing but no trigger, so it isn't counted.

This group isn't the bold five in the table. GitHub and Salesforce re-run on a change but don't say how they score. LinkedIn and ClickHouse publish a full method but don't re-run on every change.

Re-runs vary on their own, which makes a small drop hard to read. Uber does "[not over-index decisions based on ~5% run-to-run changes in most metrics](https://www.uber.com/blog/query-gpt)".

Anthropic's is the only publication of the 13 in which we found a number to clear before launch. At Anthropic, a domain owner cannot announce the agent until their eval slice clears a threshold. Anthropic "[initially used ~90%](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude)", and its stated target for offline accuracy is about 100%.

## The method runs on Dot

This section reports the run from [our earlier piece on follow-up questions](https://www.getdot.ai/blog/ai-analyst-follow-up-questions), not a new run. There, we computed every expected answer from the raw data before asking, including the second reading a question allowed. Then we asked eight questions and marked each answer against the definition it stated.

Every answer matched a reading we had computed. Two answers didn't say which date they used, so we read their dates from their SQL. The phrase "delivered in 2017" had two right answers: one by purchase date, one by delivery date.

That is the census's more-than-one-right-answer problem, found in a run of our own. The run was small: each question asked once, scored without a judge. It shows the method can be run, though not all of it by script.

## All 13, side by side

A company entered this census when its own publication named a method, described a test set, or gave its own accuracy figure. Prosus entered on a named method: its agent asks people to clarify and says when it can't find an answer. Each row draws on the company's own publications, read on 31 October 2026.

The five names in bold state their test set, scoring and timing. "(vendor)" marks a company that sells what it evaluates. "Not stated" means the publication doesn't say.

| Company | Tests against | Scores with | Runs when | Accuracy figure |
|---|---|---|---|---|
| **[Anthropic](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude)** | Human-validated question-and-answer pairs | Pass/fail per assertion | In CI when a dependency changes | Above 95% in aggregate, with skills |
| **[LinkedIn](https://www.linkedin.com/blog/engineering/ai/practical-text-to-sql-for-data-analytics)** | Experts' questions and ground-truth queries | Human review plus LLM judge | Benchmark reviewed every 3 months | [53% rated 4 or 5](https://arxiv.org/html/2507.14372v1), production review |
| **[Uber](https://www.uber.com/blog/query-gpt)** | Logged questions, hand-checked golden SQL | LLM similarity plus table overlap | Over time; before Finch updates deploy | None published |
| **[ClickHouse](https://clickhouse.com/blog/agentic-analytics-benchmark-data-agent-mnist)** | 201 production questions | LLM jury, majority vote | Once per model round | 76.6% for the top model |
| **[Hex](https://hex.tech/blog/evaluate-data-agents/)** (vendor) | A synthetic company with ground truths | Deterministic, LLM-judged or hybrid rubrics | Daily | None published |
| [Snowflake](https://www.snowflake.com/en/engineering-blog/cortex-analyst-text-to-sql-accuracy-bi/) (vendor) | 150 questions, human-selected gold queries | LLM judge | Not stated | 51% for GPT-4o, internal set |
| [GitHub](https://github.blog/ai-and-ml/github-copilot/how-we-built-an-internal-data-analytics-agent/) | Known answers and ground-truth SQL | Not stated | Every context or configuration change | None published |
| [Salesforce](https://www.salesforce.com/blog/text-to-sql-agent/) | Not stated | Not stated | On knowledge-base changes | ~50% at launch, method not stated |
| [Vercel](https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools) | 5 representative queries | Success, not defined | Not stated | 80% to 100% success |
| [Ramp](https://engineering.ramp.com/post/meet-ramp-research) | Experts' end-to-end tests | Not stated | Not stated | None published |
| [Prosus](https://www.prosus.com/news-insights/2024/democratising-data-analysis-with-toqan) | Not stated | Not stated | Not stated | None published |
| [WisdomAI](https://www.wisdom.ai/blog/how-wisdom-gets-text-to-sql-right) (vendor) | Public LiveSQLBench subset | Heuristics plus LLM judge | Not stated | 20% to 85% across learning phases |
| [Grab](https://engineering.grab.com/grab-bench-evaluating-ai) | Canaries and hidden cases | LLM judges for SQL | Not stated | None published |

## Things to keep in mind

- **Every figure is self-reported.** Each company measures its own system on its own test set, and none says the result was audited. We read each publication but checked nothing beyond it.
- **The census counts what was published, and isn't exhaustive.** Posts from Pinterest, OpenAI, Netflix, Delivery Hero, Swiggy and Fiverr would not load. They may describe how those companies test; the census can't say, so 13 is a floor, not a full count.
- **Customer testing tools aren't counted.** Databricks, Microsoft and Google publish tools for customers to test with, not how they check their own analyst.
- **This census of 13 is not Dot's census of 14.** [Our census of how 14 companies built AI data analysts](https://www.getdot.ai/blog/how-companies-built-ai-data-analysts) counted what companies built; this one counts what they published about testing it.

## Where Dot fits

[Dot answers data questions for your team.](https://www.getdot.ai/blog/conversational-analytics) Dot's [context agent page](https://www.getdot.ai/context-agent) says a context change is re-checked before it merges. The page reads: "[Merging re-checks accuracy first: Dot answers its 25 questions again and merges at 95% or more.](https://www.getdot.ai/context-agent)" In this census, only Anthropic published a numeric bar, and it applies at launch, not to each change.

In [Dot's evaluation](https://docs.getdot.ai/train-dot/evaluation), each test question carries an expected answer, a unit and a tolerance in percent. More in the [AI Data Analyst Playbook](https://www.getdot.ai/blog/ai-data-analyst-playbook) and [Dot's docs](https://docs.getdot.ai).

---

Write down real questions your team asked last month, with every answer you would accept for each. Run them against your AI analyst before rollout, then again on a schedule or when something it depends on changes.

*If this excites you, we'd love to hear from you. Get in touch.*
