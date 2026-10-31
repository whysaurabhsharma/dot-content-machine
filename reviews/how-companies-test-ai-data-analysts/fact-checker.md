# fact-checker · how-companies-test-ai-data-analysts

Started with: Fact-check reviews/how-companies-test-ai-data-analysts/draft.md against figures/how-companies-test-ai-data-analysts-figures.csv and runs/how-companies-test-ai-data-analysts-run.md.

The run file runs/how-companies-test-ai-data-analysts-run.md does not exist.

**1. Numbers**

1. Title, lede, line 1, line 3, line 4 and the C-section: 13 matches C-1, 5 matches C-2, 7 matches C-9 and 8 matches C-4. These agree with each other. The table has 13 rows, 5 marked Strict and 3 marked vendor, which matches C-1, C-2 and C-3.
2. Section 2 says "8 build their test set from real questions or ground-truth answers" (C-4). Under that wording Hex also fits, since its row says "A synthetic company with ground truths". That would make 9. C-4 leaves Hex out because the company is synthetic, but the draft's definition doesn't say that.
3. ClickHouse "took 201 questions" (CLK-1) and "dropped 39 questions where no two of them agreed" (CLK-4), but the 76.6% is "across 201 questions" (CLK-5). If 39 were dropped from 201, 162 would be left. The figures file also has 501 candidates going to 475 after curation (CLK-12), which doesn't match either number.
4. Snowflake: "measured on a 150-question internal benchmark" (SNO-1 for the 150). No figures-file row ties a Snowflake accuracy figure to that set. SNO-2 (51%) on the internal set is GPT-4o, and SNO-3 (90%+) is "on real-world use cases". The table's "One number" for Snowflake is "150 questions", which isn't an accuracy figure, although the draft counts Snowflake among the 7 that published one.
5. Vercel's "One number" is "5 queries" (VER-1). The table doesn't show the 80%/100% accuracy figure (VER-2/VER-3) that puts Vercel among the 7.
6. "About 60%" of LinkedIn's questions: matches LIN-3 and LIN-12. "10-15%": matches LIN-4. "10 product areas": LIN-2. "over 130": LIN-1 (the paper says 133, LIN-10). "every 3 months": LIN-5.
7. "Three of the 13 deal with that in print": matches C-7. "39": CLK-4.
8. "More than half" use an LLM judge: 7 of 13 is 53.8%, which is consistent. C-5 = 7, and the seven companies listed match C-5.
9. "1 point", "75%": LIN-6, LIN-7. "2.04%" and "2.03%": HEX-1 and HEX-2; the 0.01pp gap is consistent with HEX-3. "35%": HEX-3. "84.9%": CLK-13.
10. Five that re-run (lines 6 and 52): matches C-6.
11. "about 95% to about 65% in a month": ANT-5, ANT-6. "~90%": ANT-13 and C-8. "about 100%": ANT-14. "~5%": UBR-1. "Only one of the 13": C-8.
12. Table: "Above 95% in aggregate" is ANT-2. "53% rated 4 or 5" is LIN-21. "~5%" is UBR-1. "76.6%" is CLK-5. "~50%" is SFC-1. "20% to 85%" is WIS-1 and WIS-3.
13. All 13 publication dates in the table (3 June 2026, 9 December 2024, 19 September 2024, September 2026, 22 May 2026, 29 August 2024, 19 June 2026, 27 May 2025, 22 December 2025, 1 October 2024, 22 June 2026, 12 August 2026, and "No date shown"): none is in the figures file.
14. "Our census of how 14 companies built AI data analysts": 14 has no figures-file ID.
15. Dot section: "eight questions", "asked once", and the two answers to "delivered in 2017": none has an ID. A-1 records only the year 2017, not the two values or the question count.
16. "Pinterest, OpenAI, Netflix, Delivery Hero, Swiggy and Fiverr" (six posts that would not load): no ID.
17. "read on 31 October 2026" matches the figures-file dates. "checked it on 27 October" (Dot evaluation) has no ID.

**2. Product claims**

1. Dot's evaluation gives each test question "an expected answer, a unit and a tolerance in percent", with a verdict such as "Exact match". ASSERTED: no screenshot or log is shown.
2. "the score updated on save without a re-run": ASSERTED.
3. "Every answer matched a reading we had computed": ASSERTED. The run file is missing and no answers are shown.
4. "we computed every expected answer from the raw data before asking, including the second reading": ASSERTED. Nothing in the three files shows the order. My memory of the earlier piece-A check records that some readings were matched after the run.
5. "scored without a judge", "real questions": ASSERTED.
6. Company practices with figures-file support: the judge counts and listed companies (C-5), the re-run triggers (C-6), Anthropic's gate (ANT-13), LinkedIn's review cycle (LIN-5), ClickHouse's dropped questions (CLK-4) and the 84.9% mapping (CLK-13). VERIFIABLE: each is quoted in the figures file.
7. Company practices with no figures-file support, all ASSERTED:
   - ClickHouse "each seat from a different provider"
   - ClickHouse "allows a numeric tolerance"
   - Uber "verified the golden SQL by hand" and "gives no size for that set"
   - LinkedIn "each with a ground-truth query"
   - LinkedIn "investigates where its judge and its human reviewers disagree"
   - "Anthropic's grader can judge the agent's query rather than its number"
   - Grab "Canaries and hidden certification cases"
   - Databricks, Microsoft and Google "publish testing tools for customers"
   - "LinkedIn alone publishes a user survey, a benchmark ablation and an expert review"

**3. Conclusions that go further than the evidence**

1. "Anthropic reports accuracy on its own evals, domain by domain": ANT-2 and ANT-3 give an aggregate figure and "around 99% in certain domains".
2. Heading "Accuracy drifts, so the careful companies re-run their tests on every change": the body's five include Hex (daily) and Uber Finch (before deploy). The heading also generalises drift from one company (ANT-5/ANT-6).
3. "A test passed at launch says little about the same agent a month later": this rests on Anthropic's single drift case.
4. "LinkedIn and Hex publish how often their judge misses": LinkedIn publishes agreement within 1 point 75% of the time, which is not a miss rate.
5. "A re-run therefore needs a threshold ... set before the result comes in": UBR-1 doesn't say that.
6. "The method these companies publish needs no special tooling": the draft itself describes ClickHouse's multi-provider LLM jury and its column-linking scorer.
7. "Real questions often have more than one right answer" (line 5): this rests on LinkedIn's 60% figure.
8. Strict is defined as stating "test set, scoring and timing" / "enough to copy", but:
   - Anthropic's scoring is "A grader, type not stated".
   - LinkedIn's timing is its 3-monthly benchmark review, which is when answers are added, not when the test runs.
9. The entry rule is "a named method, an accuracy figure for its own system, or a described test set", but Prosus's row shows "Not stated" for test set and scoring, and has no accuracy figure (C-9 excludes it).
10. "Anthropic's grader can judge the agent's query..." is placed under how companies "respond to their judges' misses", but the draft says Anthropic's grader isn't counted as an LLM judge.
11. "Assumption: it always re-scores when a question is saved" is generalised from one check on 27 October.
12. "Every answer matched a reading we had computed" and "That is the census's more-than-one-right-answer problem, found in a run of our own" have no run evidence shown.

**4. Product quotes**

1. "Exact match" (presented as a Dot evaluation verdict): not checked, because there is no run file.
2. "delivered in 2017" (the question phrase from the Dot run): not checked, because there is no run file. The figures file points A-1 to runs/ai-analyst-follow-up-questions-run.md, which is outside the three files I was given.
3. The company quotes are not product quotes, but checked against the figures file:
   - "underreported recall by 10-15%" (LIN-4), "84.9% of scored result sets..." and "proved vital" (CLK-13), "initially used ~90%" (ANT-13), and "not over-index decisions based on ~5% run-to-run changes in most metrics" (UBR-1) match word for word.
   - "We are biased towards being overly harsh." (Hex) is not in the figures file, so it isn't checked.

Files:
- C:\Users\LENOVO\OneDrive\Documents\1Sauarbh\1Dot\dot-content-machine\dot-content-machine\reviews\how-companies-test-ai-data-analysts\draft.md
- C:\Users\LENOVO\OneDrive\Documents\1Sauarbh\1Dot\dot-content-machine\dot-content-machine\figures\how-companies-test-ai-data-analysts-figures.csv
- C:\Users\LENOVO\OneDrive\Documents\1Sauarbh\1Dot\dot-content-machine\dot-content-machine\.claude\agent-memory\fact-checker\MEMORY.md (9 new lines added)
