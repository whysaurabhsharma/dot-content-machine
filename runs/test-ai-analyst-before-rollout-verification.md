# Browser re-read of the census sources · test-ai-analyst-before-rollout (and piece B)

1 November 2026. Each page opened in Chrome (Claude in Chrome), and every quote in the figures rows checked against the page's own text by script in the page (`document.body.innerText`, whitespace and curly quotes normalised). This is the page's text, not a model's reading of it. It clears F's research condition (hard rule 4b: opened and read for this piece) and B's pre-publish item "re-read in a browser the numbers the draft uses" for these five companies.

| Company | URL as opened (after redirects) | Quotes checked | Result |
|---|---|---|---|
| Anthropic | https://claude.com/resources/articles/how-anthropic-enables-self-service-data-analytics-with-claude (redirected from claude.com/blog/…) | 13 | 11 verbatim. 2 were truncated in our rows, numbers exact: the drift sentence continues "…over a month before we treated this as an engineering problem."; "three consecutive net-negative iterations" is followed by a colon, not a full stop |
| LinkedIn (blog) | https://www.linkedin.com/blog/engineering/ai/practical-text-to-sql-for-data-analytics | 7 | 7 verbatim |
| LinkedIn (paper) | https://arxiv.org/html/2507.14372v1 | 9, plus Table 2 | 9 verbatim; Table 2 "Full" row reads 78% · 56% · 48% · 96% · 99% (LIN-13, LIN-14 and the rest match) |
| Uber (QueryGPT) | https://www.uber.com/in/en/blog/query-gpt/ (locale redirect) | 7 | 7 verbatim, including "In general, we do not over-index decisions based on ~5% run-to-run changes in most metrics." |
| Uber (Finch) | https://www.uber.com/in/en/blog/unlocking-financial-insights-with-finch/ | 2 passages | "Historical queries are re-run to detect accuracy drifts before updates are deployed for system prompts or model changes." and the "golden" query comparison: both present |
| ClickHouse | https://clickhouse.com/blog/agentic-analytics-benchmark-data-agent-mnist | 13 | 13 verbatim. The chain reads: 501 candidates, 475 after curation, a schema-compatibility gate "brings this down to 243", the ground-truth committee "cuts it to 204", a legal review removed three, 201. The 39 dropped are questions where all three models (from three providers) gave different answers |
| Hex | https://hex.tech/blog/evaluate-data-agents/ | 6 | 6 verbatim. "calibrated" and "on purpose" do not appear (confirms piece B's round 8 correction). The sentence after the calibration line is "We are biased towards being overly harsh, …" |

Not re-opened in the browser: Snowflake, GitHub, Salesforce, Vercel, Ramp, Prosus, WisdomAI, Grab, and Dot's own pages (DABstep post, census of 14, context agent page). F's figures file therefore carries no row from them; B's pre-publish browser re-read is done for the five above only.

**Added 1 November 2026, later the same day.** Also opened in Chrome: the Playbook (https://www.getdot.ai/blog/ai-data-analyst-playbook): Stage 3, "Prove": "Hold access until the tests pass your bar (~80%)" and "Move on when: the tests clear the bar and stay there through a week of changes." Dot's essay (https://www.getdot.ai/blog/your-ai-analyst-will-be-worse-next-month, Rick Radewagen, 31 August 2026): opens "Anthropic got their internal data agent to 95% accuracy. One month later it was at 65%." Both verbatim in the page text.

**Added 1 November 2026, at Decision 3.** Re-opened in Chrome: Dot's essay, section "Twenty minutes a week keeps it alive": "The version that costs almost nothing and gets you most of the way is twenty minutes a week with one named owner." ... "Then re-run your test questions and see whether the number moved." Uber QueryGPT, "Evaluation Set": "We identified a set of real questions from the QueryGPT logs, and manually verified the correct intent, schemas required to answer the question, and the golden SQL."

## B's eight remaining sources, re-read in Chrome, 1 November 2026

Each page opened in Chrome; quotes and claims checked against the page's own text by script.

| Company | Result |
|---|---|
| Snowflake (main post, the table row's link) | Numbers verbatim: 150 questions, GPT-4o "plummeted to 51%", "90%+ SQL accuracy", "about 14% more accurate". **Two findings.** (1) **Scoring:** this post tried LLM judges and set them aside ("Given the limitations of strict execution accuracy and the challenges of using LLMs as judges, our team adopted a more iterative approach"): human evaluators select all correct SQL as gold queries, and scoring uses "precision and recall for column matching, setting a more lenient threshold". B's table cell says "LLM judge". (2) **More than one right answer:** the post has a section headed "One question can have multiple correct answers". B's C-7 (3 companies deal in print with more than one right answer) leaves Snowflake out. |
| Snowflake (second post, BIRD study) | Table verbatim (52/83, 63/80, 45/70, 69/79; average 57%, 78%, 21%; "approximately 20%"). "The LLM_JUDGE was Mistral Large 2": this is where C-5's Snowflake judge comes from, a research study, not the internal evaluation the table row links. |
| GitHub | Verbatim: "A curated dataset of prompts with known correct answers, ground-truth SQL"; "Every change to the context layer or agent configuration gets evaluated before it ships"; "three times faster". Also: it runs "Qubot N times per case" (repeat trials), not used by B; relevant to F's step 3. |
| Salesforce | Verbatim: "At launch we only had the correct response ~50% of the time."; knowledge base "updated in ~15 minutes with automated regression testing". Also: "if you ask a question 10 times, you might get 8 correct answers and 2 wrong" (not used; relevant to F's step 3). |
| Vercel | Verbatim: "across 5 representative queries"; "Success rate 4/5 (80%) 5/5 (100%) +20%". The page never defines success. |
| Ramp | Verbatim: domain experts "wrote end-to-end tests". **Finding:** the post states a scoring method and a trigger, which B marks "Not stated": "a Python mini-framework in our dbt project. It asserts not only on the final answer but also the intermediate steps, including expected tool calls, table references, and query shape", and "update context, run tests, and confirm improvements". If those count, Ramp meets the strict bar (6, not 5) and the re-run count (6, not 5), on the same reading that counts Salesforce. |
| Prosus | Verbatim: the three safeguards and "85 to 90% accuracy" (plain LLMs, not Toqan). |
| WisdomAI | Verbatim: "Accuracy improves from 20% to 50% … and from 50% to 85% through context learning"; "5 datasets"; "80-92% accuracy on the Bird dev set"; "a combination of heuristics over data matches … and LLM-as-judge"; 48% leaderboard. |
| Grab | Verbatim: teaching vs certification artifacts, canaries, hidden cases; "LLM judges are useful for open-ended tasks such as SQL". |

Not re-opened: Snowflake's third post (SNO-12, not used in B's text).
