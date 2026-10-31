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
