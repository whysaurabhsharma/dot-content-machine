# 7 Companies Published Their AI Analysts' Accuracy. No Two Measured the Same Thing.

**We read how 13 companies, including Anthropic, LinkedIn and Uber, test their AI analysts: the internal agents their staff use to ask data questions. Seven of the 13 published an accuracy figure, each measured differently: ClickHouse compared result sets, LinkedIn's experts rated answers, Vercel counted successes without defining them. By the end, you'll have one table of what all 13 measured, and the six that published enough to copy are marked. Start from those six.**

**The whole piece in eight lines:**

1. Of 13 companies that published how they test their AI analyst, 7 published an accuracy figure.
2. Each figure came from its own test set, scored its own way.
3. Six companies published enough to copy: what they test against, how they score and when they run it.
4. Of the 13, 8 build their test set from real questions or ground-truth answers.
5. A real question can have more than one right answer. About 60% of LinkedIn's benchmark questions do.
6. Tests are re-run on a change, before each deploy, or daily: Anthropic, Uber, Hex, Ramp, GitHub and Salesforce. GitHub and Salesforce don't say how they score.
7. Only Anthropic's publication sets a bar to clear before launch: about 90%, at first.
8. Our earlier run on Dot used the method's core: every expected answer computed before asking.

## The seven accuracy figures can't be compared

Seven of the 13 companies published an accuracy figure, and no two measured the same thing. LinkedIn reports the share of answers its experts rated highly. ClickHouse reports a pass rate for the best model on its own production questions. [Snowflake reports](https://www.snowflake.com/en/engineering-blog/cortex-analyst-text-to-sql-accuracy-bi/) 51% for GPT-4o on its internal evaluation set.

WisdomAI reports a public benchmark subset. Salesforce gives a share correct at launch but not how it was counted. [Vercel reports](https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools) 80% to 100% success on 5 queries without defining success. [Anthropic reports](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude) above 95% in aggregate with skills, and around 99% in certain domains.

None of the seven figures can be ranked against another, or against a vendor's claim. What carries across is the method.

[Dot publishes an accuracy figure too](https://www.getdot.ai/blog/from-10-to-90-percent-on-adyens-dabstep): 90% on a 30-task slice of Adyen's public DABstep benchmark. That figure doesn't compare with the others here either. Two figures compare only when they come from the same tasks, scored the same way, on systems set up the same way.

## Eight of 13 test against real questions

Eight of the 13 build their [AI analyst](https://www.getdot.ai/blog/conversational-analytics-software)'s test set from real questions or ground-truth answers. They are Anthropic, LinkedIn, Uber, ClickHouse, Snowflake, GitHub, Ramp and WisdomAI. Hex isn't counted: its ground truths sit on a synthetic company.

[LinkedIn](https://www.linkedin.com/blog/engineering/ai/practical-text-to-sql-for-data-analytics) asked domain experts in 10 product areas for over 130 questions, each with a ground-truth query. [Uber](https://www.uber.com/blog/query-gpt) took real questions from QueryGPT's logs and verified the golden SQL by hand. [ClickHouse](https://clickhouse.com/blog/agentic-analytics-benchmark-data-agent-mnist) built its set from its internal agent's production traffic.

Four of the 13 companies deal in print with questions that have more than one right answer: LinkedIn, Uber, ClickHouse and Snowflake. About 60% of LinkedIn's benchmark questions have more than one accepted answer. Without those extra answers, LinkedIn "underreported recall by 10-15%".

Uber notes that a question can have more than one correct SQL query. Snowflake's human evaluators manually select all the correct SQL queries as acceptable gold queries.

ClickHouse narrowed 501 candidate questions to 243. Its model panel then dropped 39 where no two models agreed, and a legal review removed 3 more, leaving 201. LinkedIn's remedy is a calendar: experts review its benchmark every 3 months and add accepted answers.

## More than half score answers with an LLM judge

Seven of the 13 score answers with an LLM judge: LinkedIn, Uber, ClickHouse, Hex, Snowflake, WisdomAI and Grab. [Hex](https://hex.tech/blog/evaluate-data-agents/) built one eval where the right answer is 2.04% and a common wrong one is 2.03%. Hex's judge accepted the wrong one 35% of the time.

LinkedIn and Hex each publish one check on their judge. LinkedIn's lands within 1 point of the human score 75% of the time. Hex's is the eval above, where its judge took the wrong answer 35% of the time. Hex writes that it still sometimes struggles to calibrate its LLM judges.

Anthropic's post doesn't say what kind of grader it uses, so the count leaves it out. ClickHouse doesn't require an exact match. Its scorer links each answer's columns to the ground truth's, aligns the rows and allows a numeric tolerance. ClickHouse reports that 84.9% of its scored answers matched only through that mapping.

## Anthropic's accuracy drifted within a month

Anthropic reports that its offline accuracy drifted from about 95% at launch to about 65% over a month. That was before Anthropic treated it as an engineering problem. [Dot's essay on accuracy decay](https://www.getdot.ai/blog/your-ai-analyst-will-be-worse-next-month) starts from that figure. Anthropic's case shows that a test passed at launch can say little about the same agent a month later.

Six re-run their tests on a change, before each deploy, or daily: Anthropic, Uber, Hex, GitHub, Salesforce and Ramp. Anthropic re-runs the affected evals in CI when a PR touches a dependency. [Uber's Finch](https://www.uber.com/blog/unlocking-financial-insights-with-finch) re-runs historical queries before a prompt or model update deploys. [Ramp](https://engineering.ramp.com/post/meet-ramp-research) runs its tests when its context changes: "update context, run tests, and confirm improvements".

This group isn't the same as the six full methods in the table below. GitHub and Salesforce re-run on a change but don't say how they score. LinkedIn and ClickHouse publish a full method but don't re-run on every change.

Re-runs vary on their own, which makes a small drop hard to read. Uber does "not over-index decisions based on ~5% run-to-run changes in most metrics".

Anthropic's is the only publication of the 13 in which we found a number to clear before launch. At Anthropic, a domain owner cannot announce the agent until their eval slice clears a threshold. Anthropic "initially used ~90%", and its stated target for offline accuracy is about 100%.

## The method runs on Dot

This section reports the run from [our earlier piece on follow-up questions](https://www.getdot.ai/blog/ai-analyst-follow-up-questions), not a new run. There, we computed every expected answer from the raw data before asking, including the second reading a question allowed. Then we asked eight questions and marked each answer against the definition it stated.

Every answer matched a reading we had computed. Three answers didn't say which date they used. For two, we read the date from their SQL; the third matched the date its chat had already named. The phrase "delivered in 2017" had two right answers: one by purchase date, one by delivery date.

That is the census's more-than-one-right-answer problem, found in a run of our own. The run was small: each question asked once, scored without a judge. It shows the method can be run, though not all of it by script.

## All 13, side by side

A company entered this census when its own publication named a method, described a test set, or gave its own accuracy figure. Prosus entered on a named method: its agent asks people to clarify and says when it can't find an answer. Each row draws on the company's own publications, read on 31 October 2026.

The six names in bold state their test set, scoring and timing; that makes them the most complete descriptions, not proof of better testing. "(vendor)" marks a company that sells what it evaluates. "Not stated" means the publication doesn't say.

| Company | Accuracy figure | Tests against | Scores with | Runs when |
|---|---|---|---|---|
| **[Anthropic](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude)** | Above 95% in aggregate, with skills | Human-checked Q&A pairs | Pass/fail per assertion | In CI when a dependency changes |
| **[LinkedIn](https://www.linkedin.com/blog/engineering/ai/practical-text-to-sql-for-data-analytics)** | [53% rated 4 or 5](https://arxiv.org/html/2507.14372v1), production review | Experts' questions and ground-truth queries | Human review plus LLM judge | Benchmark reviewed every 3 months |
| **[Uber](https://www.uber.com/blog/query-gpt)** | None published | Logged questions, hand-checked golden SQL | LLM similarity plus table overlap | Over time; before Finch updates deploy |
| **[ClickHouse](https://clickhouse.com/blog/agentic-analytics-benchmark-data-agent-mnist)** | 76.6% for the top model | 201 production questions | LLM jury, majority vote | Once per model round |
| **[Hex](https://hex.tech/blog/evaluate-data-agents/)** (vendor) | None published | A synthetic company with ground truths | Rubrics: code, LLM or both | Daily |
| **[Ramp](https://engineering.ramp.com/post/meet-ramp-research)** | None published | Experts' end-to-end tests | Assertions on answer and steps | When its context changes |
| [Snowflake](https://www.snowflake.com/en/engineering-blog/cortex-analyst-text-to-sql-accuracy-bi/) (vendor) | 51% for GPT-4o, internal set | 150 questions, human-selected gold queries | Human-selected gold queries, column match | Not stated |
| [GitHub](https://github.blog/ai-and-ml/github-copilot/how-we-built-an-internal-data-analytics-agent/) | None published | Known answers and ground-truth SQL | Not stated | Every config change |
| [Salesforce](https://www.salesforce.com/blog/text-to-sql-agent/) | ~50% at launch, method not stated | Not stated | Not stated | On knowledge-base changes |
| [Vercel](https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools) | 80% to 100% success | 5 representative queries | Success, not defined | Not stated |
| [Prosus](https://www.prosus.com/news-insights/2024/democratising-data-analysis-with-toqan) | None published | Not stated | Not stated | Not stated |
| [WisdomAI](https://www.wisdom.ai/blog/how-wisdom-gets-text-to-sql-right) (vendor) | 20% to 85% across learning phases | Public LiveSQLBench subset | Heuristics plus LLM judge | Not stated |
| [Grab](https://engineering.grab.com/grab-bench-evaluating-ai) | None published | Canaries and hidden cases | LLM judges for SQL | Not stated |

## Things to keep in mind

- **Every figure is self-reported.** Each company measures its own system on its own test set, and none says the result was audited. We read each publication but checked nothing beyond it.
- **The census counts what was published, and isn't exhaustive.** Posts from Pinterest, OpenAI, Netflix, Delivery Hero, Swiggy and Fiverr would not load. They may describe how those companies test; the census can't say, so 13 is a floor, not a full count.
- **Customer testing tools aren't counted.** Databricks, Microsoft and Google publish tools for customers to test with, not how they check their own analyst.
- **This census of 13 is not Dot's census of 14.** [Our census of how 14 companies built AI data analysts](https://www.getdot.ai/blog/how-companies-built-ai-data-analysts) counted what companies built; this one counts what they published about testing it.

## Where Dot fits

[Dot answers data questions for your team.](https://www.getdot.ai/blog/conversational-analytics) Dot's [context agent page](https://www.getdot.ai/context-agent) says: "Merging re-checks accuracy first: Dot answers its 25 questions again and merges at 95% or more." Assumption: the page describes how merging works today; we haven't tested it.

In [Dot's evaluation](https://docs.getdot.ai/train-dot/evaluation), each test question carries an expected answer, a unit and a tolerance in percent. More in the [AI Data Analyst Playbook](https://www.getdot.ai/blog/ai-data-analyst-playbook) and [Dot's docs](https://docs.getdot.ai).

---

Write down real questions your team asked last month, with every answer you would accept for each. Run them against your AI analyst [before rollout](https://www.getdot.ai/blog/test-ai-analyst-before-rollout), then again on a schedule or when something it depends on changes.

*If this excites you, we'd love to hear from you. Get in touch.*
