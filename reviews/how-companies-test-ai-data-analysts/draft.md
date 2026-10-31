# 7 Companies Published Their AI Analysts' Accuracy. No Two Measured the Same Thing.

**We read how 13 companies, including Anthropic, LinkedIn and Uber, test their AI analysts: the internal agents staff use to ask data questions. Seven of the 13 published an accuracy figure, each measured differently: ClickHouse compared result sets, LinkedIn's experts rated answers, and Vercel counted undefined successes. By the end, you'll have one table of what all 13 measured, with the five that published enough to copy marked. Those five are the most complete descriptions, not proof of better testing.**

**The whole piece in eight lines:**

1. Of 13 companies that published how they test their AI analyst, 7 published an accuracy figure.
2. Each figure came from its own test set, scored its own way.
3. Five companies published enough to copy: what they test against, how they score and when they run it.
4. Of the 13, 8 build their test set from real questions or ground-truth answers.
5. A real question can have more than one right answer. About 60% of LinkedIn's benchmark questions do.
6. Anthropic, Uber, Hex, GitHub and Salesforce re-run their tests on a change, before each deploy, or daily.
7. Of the 13 publications, only Anthropic's states a bar to clear before launch that we found: about 90%, initially.
8. We ran the method's core on Dot: real questions, answers computed before asking, and a rule for a match.

## The seven accuracy figures can't be compared

Seven of the 13 companies published an accuracy figure, and no two measured the same thing. LinkedIn reports the share of answers its experts rated highly. ClickHouse reports a pass rate for the best model on its own production questions. [Snowflake reports](https://www.snowflake.com/en/engineering-blog/cortex-analyst-text-to-sql-accuracy-bi/) 51% for GPT-4o on its internal evaluation set.

WisdomAI reports a public benchmark subset. Salesforce gives a share correct at launch but not how it was counted. [Vercel reports](https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools) 80% to 100% success on 5 queries without defining success. [Anthropic reports](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude) an aggregate figure, and around 99% in certain domains.

Each figure answers a different question, on a different test set, scored a different way. So none of the figures can be ranked against another, and a vendor's accuracy claim can't be ranked against them either. What carries across is the method. The five companies that published enough to copy say what they test against, how they score and when they run the test.

[Dot publishes an accuracy figure too](https://www.getdot.ai/blog/from-10-to-90-percent-on-adyens-dabstep): 90% on a 30-task slice of Adyen's public DABstep benchmark. That figure doesn't compare with the others here either. Two figures compare only when they come from the same tasks, scored the same way, on systems set up the same way.

## Eight of 13 companies test their AI analyst against real questions or ground-truth answers

Eight of the 13 companies build their [AI analyst](https://www.getdot.ai/blog/conversational-analytics-software)'s test set from real questions or ground-truth answers. Hex has ground truths too, but they sit on a synthetic company, so it isn't counted.

[LinkedIn](https://www.linkedin.com/blog/engineering/ai/practical-text-to-sql-for-data-analytics) asked domain experts in 10 product areas for over 130 questions, each with a ground-truth query. [Uber](https://www.uber.com/blog/query-gpt) took real questions from QueryGPT's logs and verified the golden SQL by hand.

[ClickHouse](https://clickhouse.com/blog/agentic-analytics-benchmark-data-agent-mnist) built its final set of 201 questions from its internal agent's production traffic. [Snowflake](https://www.snowflake.com/en/engineering-blog/cortex-analyst-text-to-sql-accuracy-bi/) built a 150-question internal benchmark with gold queries chosen by people.

A company entered this census when its own publication named a method, described a test set, or gave its own accuracy figure.

A real question can have more than one right answer, and three of the 13 companies deal with that in print. [About 60% of LinkedIn's benchmark questions](https://www.linkedin.com/blog/engineering/ai/practical-text-to-sql-for-data-analytics) have more than one accepted answer. Without those extra answers, LinkedIn "[underreported recall by 10-15%](https://www.linkedin.com/blog/engineering/ai/practical-text-to-sql-for-data-analytics)". Uber notes that a question can have more than one correct SQL query.

[ClickHouse's](https://clickhouse.com/blog/agentic-analytics-benchmark-data-agent-mnist) model panel dropped 39 of 243 candidate questions where no two models agreed. [A legal review](https://clickhouse.com/blog/agentic-analytics-benchmark-data-agent-mnist) then took 204 down to the final 201. LinkedIn's remedy is a calendar: experts review its benchmark every 3 months and add accepted answers.

## More than half of the 13 companies score answers with an LLM judge, and two publish a check on it

LinkedIn, Uber, ClickHouse, Hex, Snowflake, WisdomAI and Grab use an LLM to judge their analyst's answers. [Hex](https://hex.tech/blog/evaluate-data-agents/) built one eval where the right answer is 2.04% and a common wrong one is 2.03%. Hex's judge accepted the wrong one [35% of the time](https://hex.tech/blog/evaluate-data-agents/).

LinkedIn and Hex each publish one check on their judge, and the two checks measure different things. [LinkedIn's judge](https://www.linkedin.com/blog/engineering/ai/practical-text-to-sql-for-data-analytics) lands within 1 point of the human score 75% of the time. Of its LLM judge, Hex writes: "[We are biased towards being overly harsh.](https://hex.tech/blog/evaluate-data-agents/)" LinkedIn investigates where its judge and its human reviewers disagree.

LinkedIn pairs human review with an LLM judge scoring against a rubric. Uber has an LLM score each query's similarity to the golden SQL, alongside table overlap. ClickHouse uses an LLM jury, each seat from a different provider, deciding by majority. Hex mixes deterministic, LLM-judged and hybrid rubrics.

Anthropic's post doesn't say what kind of grader it uses, so the count leaves it out; that says nothing about how Anthropic grades. ClickHouse doesn't require an exact match. Its scorer links each answer's columns to the ground truth's, aligns the rows and allows a numeric tolerance. ClickHouse writes that "[84.9% of scored result sets in our test match only through the linked mapping](https://clickhouse.com/blog/agentic-analytics-benchmark-data-agent-mnist)".

## Anthropic's accuracy drifted, and the companies that re-run do it on a change or a schedule

[Anthropic reports](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude) that its offline accuracy drifted from about 95% at launch to about 65% over a month. [Dot's essay on accuracy decay](https://www.getdot.ai/blog/your-ai-analyst-will-be-worse-next-month) starts from that figure. Anthropic's case shows that a test passed at launch can say little about the same agent a month later.

Anthropic, Uber, Hex, GitHub and Salesforce re-run their tests on a change, before each deploy, or daily. Anthropic re-runs the affected evals in CI when a PR touches a dependency. [Uber's Finch](https://www.uber.com/blog/unlocking-financial-insights-with-finch) re-runs historical queries before a prompt or model update deploys. Hex runs its eval sets daily.

[GitHub](https://github.blog/ai-and-ml/github-copilot/how-we-built-an-internal-data-analytics-agent/) evaluates every change to context or agent configuration before it ships. [Salesforce](https://www.salesforce.com/blog/text-to-sql-agent/) runs automated regression testing when its knowledge base changes. Ramp describes testing but no trigger, so it sits outside the companies that re-run.

The companies that re-run are not the same group as the strict methods in the census table. GitHub and Salesforce re-run on a change but don't say how they score. LinkedIn and ClickHouse publish a full method but don't re-run on every change.

Anthropic's is the only publication of the 13 in which we found a number to clear before launch. At Anthropic, a domain owner cannot announce the agent until their eval slice clears a threshold. Anthropic "[initially used ~90%](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude)", and its stated target for offline accuracy is about 100%. [Its other figures](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude) sit at other stages: above 95% with skills, about 99% in some domains, about 65% after a month without upkeep.

Re-runs vary on their own, which makes a small drop hard to read. Uber does "[not over-index decisions based on ~5% run-to-run changes in most metrics](https://www.uber.com/blog/query-gpt)".

## The method runs on Dot, and the same problem showed up

Its core needs no special tooling, so we ran it on Dot. For [our test of follow-up questions](https://www.getdot.ai/blog/ai-analyst-follow-up-questions), we computed every expected answer from the raw data before asking, including the second reading a question allowed. Then we asked eight questions and marked each answer against the definition it stated.

Every answer matched a reading we had computed. Two answers didn't say which date they used, so a person read it from their SQL before marking them. The phrase "delivered in 2017" had two right answers: one by purchase date, one by delivery date.

That is the census's more-than-one-right-answer problem, found in a run of our own. The run was small: eight questions, asked once, scored without a judge. It shows the method can be run, though not all of it by script. For two answers that didn't name their date, a person decided which reading each matched.

## All 13 publications, side by side, each linked to its source

Each row draws on one company's own publications, read on 31 October 2026. Uber's row draws on two: QueryGPT and Finch. "Strict" marks the five that state their test set, scoring and timing; "vendor" marks the three that sell what they evaluate. "Not stated" means the publication doesn't say.

| Company | Published | Tests against | Scores with | Runs when | Bar | Accuracy figure |
|---|---|---|---|---|---|---|
| [Anthropic](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude) | 3 June 2026 | Question-and-answer pairs, human-validated | Pass/fail per assertion; grader type not stated | When a PR touches a dependency, in CI | Strict | Above 95% in aggregate, with skills |
| [LinkedIn](https://www.linkedin.com/blog/engineering/ai/practical-text-to-sql-for-data-analytics) | 9 December 2024 | Experts' questions and ground-truth queries | Human review plus LLM judge | Ongoing; experts review the benchmark every 3 months | Strict | [53% rated 4 or 5](https://arxiv.org/html/2507.14372v1) in expert review of production |
| [Uber](https://www.uber.com/blog/query-gpt) | 19 September 2024 | Real questions from logs, golden SQL checked by hand | LLM judge (similarity) plus table overlap | QueryGPT: staging and production, tracked over time. Finch: before prompt or model updates deploy; re-runs vary ~5%, treated as noise | Strict | None published |
| [ClickHouse](https://clickhouse.com/blog/agentic-analytics-benchmark-data-agent-mnist) | September 2026 | 201 production questions | LLM jury, majority vote | Once per model round | Strict | 76.6% for the top model |
| [Hex](https://hex.tech/blog/evaluate-data-agents/) (vendor) | 22 May 2026 | A synthetic company with ground truths | Deterministic, LLM-judged or hybrid rubrics | Daily | Strict | None published |
| [Snowflake](https://www.snowflake.com/en/engineering-blog/cortex-analyst-text-to-sql-accuracy-bi/) (vendor) | 29 August 2024 | Internal benchmark, human-selected gold queries | LLM judge | Not stated | Wider | 51% for GPT-4o on its internal set |
| [GitHub](https://github.blog/ai-and-ml/github-copilot/how-we-built-an-internal-data-analytics-agent/) | 19 June 2026 | Known answers and ground-truth SQL | Not stated | On every context or configuration change, before release | Wider | None published |
| [Salesforce](https://www.salesforce.com/blog/text-to-sql-agent/) | 27 May 2025 | Not stated | Not stated | On knowledge-base changes | Wider | ~50% correct at launch, method not stated |
| [Vercel](https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools) | 22 December 2025 | Representative queries | Success, not defined | Not stated | Wider | 80% to 100% success, before and after a rebuild |
| [Ramp](https://engineering.ramp.com/post/meet-ramp-research) | No date shown | End-to-end tests written with domain experts | Not stated | Not stated | Wider | None published |
| [Prosus](https://www.prosus.com/news-insights/2024/democratising-data-analysis-with-toqan) | 1 October 2024 | Not stated; counted for a named method: the agent asks people to clarify and says when it can't find an answer | Not stated | Not stated | Wider | None published |
| [WisdomAI](https://www.wisdom.ai/blog/how-wisdom-gets-text-to-sql-right) (vendor) | 22 June 2026 | Public LiveSQLBench subset; LLM- and human-validated ground truth | Heuristics plus LLM judge | Not stated | Wider | 20% to 85% across the learning phases |
| [Grab](https://engineering.grab.com/grab-bench-evaluating-ai) | 12 August 2026 | Canaries and hidden cases | LLM judges for SQL | Not stated | Wider | None published |

## Things to keep in mind

- **Every figure is self-reported.** Each company measures its own system on its own test set, and none says the result was audited. Every description of a company's method is what that company published, linked at its name; we read each publication but checked nothing beyond it. Three of the 13 sell the product they evaluate: Hex, Snowflake and WisdomAI.
- **The census counts what was published, and isn't exhaustive.** A "Not stated" means the publication doesn't mention the practice. Posts from Pinterest, OpenAI, Netflix, Delivery Hero, Swiggy and Fiverr would not load. They may describe how those companies test; the census can't say, so 13 is a floor, not a full count.
- **Customer testing tools aren't counted.** Databricks, Microsoft and Google publish testing tools for customers; those show how customers should test, not how each company checks its own analyst.
- **This census of 13 is not Dot's census of 14.** [Our census of how 14 companies built AI data analysts](https://www.getdot.ai/blog/how-companies-built-ai-data-analysts) counted what companies built. This one counts what companies published about testing what they built, so some names appear in both and some in only one.

## Where Dot fits

[Dot answers data questions for your team.](https://www.getdot.ai/blog/conversational-analytics) In [Dot's evaluation](https://docs.getdot.ai/train-dot/evaluation), each test question carries an expected answer, a unit and a tolerance in percent, and gets a verdict such as "Exact match". When we checked it on 27 October, the score updated on save without a re-run. More in the [AI Data Analyst Playbook](https://www.getdot.ai/blog/ai-data-analyst-playbook) and [Dot's docs](https://docs.getdot.ai).

---

Write down real questions your team asked last month, with every answer you would accept for each. Run them against your AI analyst before rollout, then again on a schedule or when something it depends on changes.

*If this excites you, we'd love to hear from you. Get in touch.*
