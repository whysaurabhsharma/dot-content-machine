# fact-checker · how-companies-test-ai-data-analysts

Started with: Fact-check reviews/how-companies-test-ai-data-analysts/draft.md against figures/how-companies-test-ai-data-analysts-figures.csv and runs/how-companies-test-ai-data-analysts-run.md.

The run file runs/how-companies-test-ai-data-analysts-run.md does not exist.

1. **Numbers: internal consistency and figures-file match**
   - 13 companies (title, lede, lines 11, 22, table): consistent; there are 13 table rows. Matches C-1.
   - 5 strict (title, lede, lines 11, 22, 64): consistent; 5 rows are marked Strict. Matches C-2. The number holds up but the grouping doesn't:
     - Uber's row takes its test set and scoring from QueryGPT and its timing from Finch. Line 52 says "Uber's QueryGPT post … describe[s] testing, but no trigger". So no single Uber method states all three parts.
     - LinkedIn's "Runs when" is "Expert review every 3 months". Line 30 says that is when accepted answers are added, not when the test runs.
   - ~95% to ~65% over a month (lines 5, 54): matches ANT-5 and ANT-6.
   - Roughly 90% of PRs (line 7): matches ANT-7.
   - 8 of 13 (line 12, H2 line 20): matches C-4. The label changes from place to place: "real questions or expert-checked answers" (line 12), "real questions with known answers" (H2 and lede). The C-4 list includes WisdomAI, whose table row says "Public LiveSQLBench subset", and GitHub, whose question source isn't stated. "Most of the thirteen build the test from their own work" (line 24) doesn't fit WisdomAI.
   - About 60% (lines 13, 28): matches LIN-3 and LIN-12.
   - 7 of 13 LLM judge (line 14, H2, line 36): matches C-5. The body names 4 and the table adds Snowflake, WisdomAI and Grab, so the count is consistent.
   - 2.03% / 2.04% / 35% (lines 15, 40): match HEX-2, HEX-1 and HEX-3.
   - 5 re-run (lines 16, 50): the five are named and the count matches C-6. Line 16 says "on every change", but Salesforce re-runs on knowledge-base changes (line 52, table).
   - About 90% per domain (line 17): matches ANT-13 and C-8. The line states it in the present tense, but line 56 quotes "initially used ~90%".
   - 10 product areas, over 130 questions (line 24): match LIN-2 and LIN-1.
   - 201 questions (line 26, table): matches CLK-1.
   - 150 questions (line 26, table): matches SNO-1.
   - Three of the 13 (line 28): matches C-7. The draft names only LinkedIn and ClickHouse; Uber, the third, never appears in that section.
   - 10-15% (line 28): matches LIN-4.
   - 39 questions (line 30): matches CLK-4. "Models from different providers" has no support in the figures file.
   - Every 3 months (line 30, table): matches LIN-5.
   - 27 October 2026 (lines 32, 60): no figures ID, and there is no run file to back it.
   - Scale of 1 to 5 (line 36): no figures ID.
   - Within 1 point, 75% (line 40): match LIN-6 and LIN-7.
   - 84.9% (line 42): matches CLK-13.
   - ~90% initial, ~100% target (line 56): match ANT-13 and ANT-14.
   - ~5% (line 58, table): matches UBR-1.
   - "Seen twice" (line 60): no figures ID, and there is no run file.
   - Read on 31 October 2026 (line 64): matches the date column of the figures file. It has no ID of its own.
   - Publication dates in the table (3 June 2026, 9 December 2024, 19 September 2024, September 2026, 22 May 2026, 29 August 2024, 19 June 2026, 27 May 2025, 22 December 2025, 1 October 2024, 22 June 2026, 12 August 2026): no figures IDs for any of them.
   - Above 95% in aggregate (table): matches ANT-2.
   - 53% rated 4 or 5 (table): matches LIN-21.
   - 76.6% (table): matches CLK-5.
   - ~50% (table): matches SFC-1.
   - 5 queries (table): matches VER-1.
   - 20% to 85% (table): match WIS-1 and WIS-3.
   - 3 vendors (lines 64, 87): matches C-3, and the table marks the same three.
   - "Three different accuracy measures" for LinkedIn (line 84): no figures ID. The figures file has more than three LinkedIn measures (LIN-7, LIN-8/9, LIN-13 to LIN-17, LIN-21, LIN-22).
   - "Eight lines" (line 9): there are 8 items. That checks out.
   - "The five methods side by side" (lede): the table shows 13 rows. The five are never set out on their own.

2. **Claims about what a product does**
   - Dot "answers data questions for your team" (line 91): ASSERTED.
   - Each Dot test-set question carries an expected answer, a unit and a tolerance in percent (lines 32, 91): ASSERTED. Line 32 says "as we observed", but no screenshot or log is shown.
   - The tolerance decides how close counts as right (line 32): ASSERTED.
   - Dot compares each answer with its expected answer within the tolerance (line 46): ASSERTED.
   - Dot shows a verdict such as "Exact match" for every question (lines 46, 91): ASSERTED.
   - Dot re-scored on save without a re-run (lines 60, 91): ASSERTED.
   - The score fell after a deliberate change and came back after reverting, seen twice (line 60): ASSERTED.
   - "Assumption: it always re-scores when a question is saved" (line 91): ASSERTED. The draft itself labels it an assumption.
   - The Playbook and docs "show how" (line 91): ASSERTED.
   - Anthropic's accuracy drift: VERIFIABLE (quoted and linked). Its cause, "the data model moving while the agent's skills stood still" (lines 5, 54), is ASSERTED.
   - Anthropic's grader judges the query, not the number (line 44): ASSERTED.
   - Anthropic re-runs affected evals in CI (line 50): ASSERTED (link only). The table's "On every change, in CI" is wider than the body's "when a PR touches a dependency".
   - LinkedIn's judge with a 1 to 5 rubric, plus human review, and its investigation of disagreements (lines 36, 44): ASSERTED (link only).
   - Uber's LLM similarity score plus table overlap (line 36), golden SQL verified by hand (line 24), and Finch re-running before deploys (line 50): ASSERTED (links only).
   - ClickHouse's LLM jury with seats from different providers, deciding by majority (line 36): ASSERTED.
   - Hex's mixed rubrics and daily runs (lines 38, 50): ASSERTED. Hex's "overly harsh" (line 44): VERIFIABLE (quoted).
   - GitHub evaluates every change before it ships (line 52): ASSERTED. The table broadens it to "On every change".
   - Salesforce's regression testing on knowledge-base changes (line 52): ASSERTED.
   - Every table cell for Snowflake, Vercel, Ramp, Prosus, WisdomAI and Grab: ASSERTED (link only).
   - Pinterest, OpenAI, Netflix, Delivery Hero, Swiggy and Fiverr posts "would not load" (line 86): ASSERTED.
   - Databricks, Microsoft and Google publish testing tools for customers (line 86): ASSERTED.

3. **Conclusions that go further than the evidence**
   - Line 3, "Only 5 published a method you could copy": Uber's "method" is assembled from two systems, and LinkedIn's timing is a review cadence (see item 1).
   - Line 3 and the H2 on line 20, "Most test against real questions with known answers": WisdomAI uses a public benchmark, and Snowflake, GitHub and Anthropic aren't shown to use real questions.
   - Line 5, "Testing once is not enough, and Anthropic has the numbers to show it": the numbers show drift. They don't show that re-testing caught or prevented it.
   - Lines 5 and 54: drift is attributed to the data model moving while skills stood still. The quoted sentence gives no cause.
   - Line 7, "Anthropic's fix was procedural": the 90% PR figure is presented as the fix for the drift without evidence linking the two.
   - Line 17: the ~90% bar is stated as current, but the source says "initially".
   - The H2 on line 34 and line 40, "the published judges are imperfect" / "The published LLM judges miss things, and the companies say so": only 2 of the 7 judges (LinkedIn, Hex) are shown.
   - Line 44, "The companies answer this by leaning harsh and keeping people in the loop": this rests on Hex, LinkedIn and Anthropic. The draft has already excluded Anthropic from the LLM-judge count (line 38).
   - Line 42, "A plain exact-match scorer would have failed answers that ClickHouse counts as correct": this is an inference. The draft doesn't quote ClickHouse saying it.
   - The H2 on line 48, "the careful companies re-run": "careful" is a judgement the evidence doesn't support.
   - Line 64, "Each row is one company's own publication": the LinkedIn row cites a blog and an arXiv paper, and the Uber row draws on QueryGPT and Finch.
   - Line 84, "None is audited, and no two are comparable": stated with no support.
   - Lines 32 and 91: Dot's test set "has the same shape" / is "the kind of test set this piece describes". Dot holds one expected answer per question, while the piece asks for "every answer you would accept".
   - Line 60: Dot's re-score-on-save behaviour rests on one dated test, "seen twice", with no evidence shown and no run file.

4. **Product quotes**
   - "Exact match" (line 46), given as a Dot verdict: not checked: no run file.
   - "Exact match" (line 91), given as a Dot verdict: not checked: no run file.
   - The other quoted lines in the draft are company statements, not product output. These match quotes in the figures file: "from ~95% at launch to ~65% over a month" (ANT-5/ANT-6), "underreported recall by 10-15%" (LIN-4), "initially used ~90%" (ANT-13) and "not over-index decisions based on ~5% run-to-run changes in most metrics" (UBR-1). Two have no record in the figures file: "Treat skill maintenance as a first class citizen" and "We are biased towards being overly harsh".

I added 9 new mistake lines to C:\Users\LENOVO\OneDrive\Documents\1Sauarbh\1Dot\dot-content-machine\dot-content-machine\.claude\agent-memory\fact-checker\MEMORY.md. The missing run file was already recorded there from piece-3, so I didn't add it again.
