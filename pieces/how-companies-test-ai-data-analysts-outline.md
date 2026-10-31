# OUTLINE: "How do I test whether an AI data analyst gives correct answers before rolling it out?"

Piece slug: `how-companies-test-ai-data-analysts`. Format: teardown (`runs/how-companies-test-ai-data-analysts-piece.json`). Bank #35 per the manifest and the gate. Outlined 31 October 2026, from `runs/how-companies-test-ai-data-analysts-research.md` (section 7, the census), `runs/how-companies-test-ai-data-analysts-verification.md` (every source re-opened, 31 October 2026) and `figures/how-companies-test-ai-data-analysts-figures.csv`.

**Settled by Saurabh, 31 October 2026, before approval.** Bank #35 (the manifest is right; PLAN.md was corrected). Grab stays in the 13: it meets the stated bar, and dropping it afterwards would move the goalposts. Customer-facing testing tools (Databricks, Microsoft Fabric, Google Prism) stay out, and the piece says why in one sentence. "Companies" throughout: all 13 are companies. The Playbook stage name is still unconfirmed (research section 3); the draft links the Playbook without naming the stage unless it is checked.

No Dot run (teardown). Every number is a `published: <URL>, read 2026-10-31` row or a census count (C-1 to C-8). None is combined with Dot's own figures (hard rule 4). Each company's figure measures its own system on its own test set; the piece never ranks one against another.

## 1. Title candidates

**Working title, decided by Saurabh on 31 October 2026: "13 Companies Test Their AI Analyst. 5 Show How."** The two-sentence turn of Dot's house style, and it reports a result rather than a list. Decision 3 still comes after the reviews.

1. **Working title.** 13 Companies Test Their AI Analyst. 5 Show How.
2. How 13 Companies Test Their AI Data Analyst

The SEO title carries the buyer's phrase "how to evaluate AI data analyst accuracy" (the bank question; not indexed in Ahrefs, 27–28 October 2026). `/seo-geo` sets it.

Proof figures: C-1 (13) and C-2 (5).

## 2. The opening (56 words)

> **Thirteen companies published how they check their AI analyst's answers before trusting them. Only five published a method you could copy: what they test against, how they score, and when they run the test. Most of the thirteen test against real questions with known answers. By the end, you'll have the five methods side by side.**

Figures: C-1 (13), C-2 (5), C-4 ("most of the thirteen": 8 of 13). Hard rule 20: the question (how do companies test an AI analyst) is answered in the first 100 words; the promise sits beside the answer.

## 3. The surprising detail

> Anthropic watched its own analytics agent lose accuracy with nothing broken. Offline accuracy drifted "from ~95% at launch to ~65% over a month", because the skills the agent relied on were not kept up as the data model changed. Anthropic's fix was procedural: roughly 90% of its data-model PRs now include a skill change in the same diff.

Figures: ANT-5 (~95%), ANT-6 (~65%), ANT-7 (~90%). Quote verbatim from the page (verification, Anthropic, CONFIRMED). The draft must keep "~" or "about" on all three: the page gives them as approximate. "Because the skills were not kept up" is the research file's reading ("without skill maintenance"); the draft should link it to the page's own heading, "Treat skill maintenance as a first class citizen" (CONFIRMED), and not claim more cause than that.

## 4. Pocket guide

1. We read 13 companies' own publications on how they test their AI data analyst; 5 state what they test against, how they score, and when they run it.
2. 8 of the 13 test against real questions or expert-checked answers, not a public benchmark.
3. Real questions often have more than one right answer: LinkedIn found about 60% of its benchmark questions did.
4. 7 of the 13 score answers with an LLM judge, and the published judges miss things.
5. Hex's judge accepted a 0.01-point wrong answer 35% of the time.
6. 5 of the 13 re-run their tests on every change or daily, because accuracy drifts.
7. Only Anthropic publishes a number an analyst must clear before launch: about 90% per domain.
8. Start with your own team's real questions and the answers you would accept, then re-run them on every change.

Figures: C-1, C-2 (line 1); C-4 (line 2); LIN-3 (line 3); C-5 (line 4); HEX-1, HEX-2, HEX-3 (line 5: 2.04% right vs 2.03% wrong is the "0.01-point" difference, which the page writes ".01pp"); C-6 (line 6); C-8, ANT-13 (line 7). Line 8 is the instruction (item 9).

## 5. Three H2s

Each H2 reads standing alone (hard rule 21): it names the census and its count, with no "this" or "they" reaching outside the section.

### H2 1: Eight of 13 companies test their AI analyst against real questions with known answers

- **Quotable line goes here** (item 11), as the section's first or second sentence.
- Method in plain words: what each company tests against. LinkedIn asked domain experts in 10 product areas for over 130 questions with ground-truth queries. Uber took real questions from QueryGPT's logs and verified the golden SQL by hand. ClickHouse took 201 questions from its agent's production traffic. Snowflake built a 150-question internal benchmark with human-selected gold queries.
- Figures: C-1, C-4; LIN-1 (130), LIN-2 (10); LIN-10 (133), LIN-11 (167) if the paper is cited too; CLK-1 (201), CLK-2 (18), CLK-3 (865); SNO-1 (150). Uber has no size figure for its set; say so, or say nothing about size.
- Limitation: a real question often has more than one right answer. 3 companies say so, or drop the questions where answers disagree. About 60% of LinkedIn's benchmark questions have more than one accepted answer; without them, LinkedIn "underreported recall by 10-15%". ClickHouse dropped 39 questions where its three ground-truth models disagreed.
- Figures: C-7 (3); LIN-3 (~60%), LIN-4 (10-15%); CLK-4 (39).
- What is done about it (tested, hard rule 19): LinkedIn's remedy is in its own numbers. Experts review the benchmark every 3 months and add accepted answers (LIN-5); the 10–15% (LIN-4) is what the missing answers cost. Dot's side (rule 6): an evaluation question in Dot carries an expected answer, a unit and a tolerance in percent (facts O1, Observed 27 October 2026). O1 does not say a question can hold more than one accepted answer; the draft must not imply it.

### H2 2: Seven of 13 companies score answers with an LLM judge, and the published judges are imperfect

- Method: who scores how. LinkedIn: a human review plus an LLM judge on a 1–5 rubric. Uber: an LLM similarity score from 0 to 1 against the golden SQL, plus table overlap. ClickHouse: a three-seat LLM jury, each seat from a different provider, deciding by majority. Hex: deterministic, LLM-judged or hybrid rubrics. Anthropic is not counted: its page names a grader but not what it is (verification, discrepancy 10).
- Figures: C-5 (7); UBR-2 (0.5, the table-overlap example); LIN-15, LIN-21 only if the rubric's results are shown, and then never against each other (LIN-15 is a benchmark ablation, LIN-21 an expert review of production, LIN-8 a user survey).
- Limitation: the judges miss things. LinkedIn's judge lands within 1 point of the human score 75% of the time. Hex built an eval where the right answer is 2.04% and a common wrong one 2.03%; its judge accepted the wrong one 35% of the time. At ClickHouse, 84.9% of scored result sets matched only through column-linked mapping, so an exact-match scorer would have failed answers its method counts as correct.
- Figures: LIN-6 (1), LIN-7 (75%); HEX-1 (2.04%), HEX-2 (2.03%), HEX-3 (35%); CLK-13 (84.9%).
- What is done about it (from the publications): LinkedIn investigates where judge and humans disagree, and keeps the quarterly expert review (LIN-5). Hex: "We are biased towards being overly harsh" (verbatim; quote names its context, the LLM judge, rule 13). Anthropic has "the grader judge the agent's query rather than its number" (verification, method notes; no figure). Dot's side: Dot's evaluation scores a number against a tolerance and shows a verdict such as "0.52% off expected" (facts O1). That is a deterministic check, not an LLM judge; the draft says only what O1 says.

### H2 3: Five of 13 companies re-run their tests on every change or daily, because accuracy drifts

- Method: when they run. Anthropic re-runs affected evals in CI when a PR touches a dependency. Uber re-runs Finch's historical queries before a prompt or model update deploys. Hex runs eval sets daily. GitHub evaluates every change before it ships. Salesforce runs automated regression testing on knowledge-base changes.
- Figures: C-6 (5). Uber QueryGPT alone and Ramp are not counted (no trigger stated); say so in one clause if the census table shows them.
- The drift case: Anthropic's ~95% to ~65% in a month (ANT-5, ANT-6) belongs here if the surprising detail is moved; otherwise refer to it by name only, not by repeating the numbers (style rule 7, said once).
- Launch gates: only 1 company publishes a numeric gate. An Anthropic domain owner cannot announce the agent until their eval slice clears a threshold, "initially" about 90% (C-8, ANT-13); the target offline accuracy is "~100%" (ANT-14).
- Limitation: re-runs vary on their own. Uber does "not over-index decisions based on ~5% run-to-run changes in most metrics" (UBR-1).
- What is done about it: Uber treats a ~5% move as noise (UBR-1), so a re-run needs a threshold for what counts as a regression. Dot's side: Dot's evaluation re-scored on save without a re-run, 100% to 95% after a deliberate change and back after reverting, seen twice (facts O2, Observed 27 October 2026). That it always does so is Assumption A7, and is labelled "Assumption" if used.

## 6. The body the format needs (teardown)

PLAN.md, section B: 1,000–1,600 words; one census table, one row per publication, each row linking its primary source. `check_piece.py` check 10 for a teardown: at least 5 census rows, every row linked; a chart is optional, but complete if present.

**The census table.** 13 rows, in the order of research section 7 (strict-bar entries first). Columns:

| Column | Content |
|---|---|
| Company | Name, linked to the primary publication (section 7 URL; LinkedIn's row links the blog, and the paper may be linked in the text) |
| Published | Date as section 7 gives it (Ramp: "no date shown"; ClickHouse: September 2026, header and metadata disagree) |
| Tests against | A few words from section 7 |
| Scores with | A few words; "LLM judge" only for the 7 in C-5 |
| Runs when | A few words; "on every change or daily" only for the 5 in C-6 |
| Bar | Strict or wider (C-2) |
| One number | At most one figure per row, by ID, or "none published" |

Numbers per row, one each, all from the figures file: Anthropic ANT-2 (above 95% with skills); LinkedIn LIN-21 (53% rated 4 or 5, expert review of production); Uber none on accuracy (UBR-1, ~5% run-to-run, if a number is wanted); ClickHouse CLK-5 (76.6%, top model on 201 questions); Hex none (HEX-3 belongs in H2 2, not here); Snowflake SNO-1 (150 questions); GitHub none; Salesforce SFC-1 (~50% at launch, method not stated); Vercel VER-1 (5 queries); Ramp none; Prosus none (PRO-1 is plain LLMs, not Toqan, so it does not go in Toqan's row); WisdomAI WIS-1 to WIS-3 as "20% to 85%" (exact, no "about": verification discrepancy 7); Grab none.

Three are vendors evaluating a product they sell: Hex, Snowflake, WisdomAI (C-3). Mark them in the table (a note or a symbol) rather than in a separate column.

**The chart (optional; recommended).** A horizontal bar chart: of the 13, how many do each practice. Bars: real questions or expert-checked answers 8 (C-4); LLM judge 7 (C-5); re-run on every change or daily 5 (C-6); more than one right answer acknowledged 3 (C-7); numeric launch gate 1 (C-8). Axis to 13 (C-1).

- Alt text: "Bar chart of 13 companies' published AI analyst tests: 8 use real questions or expert-checked answers, 7 an LLM judge, 5 re-run on every change or daily, 3 allow more than one right answer, 1 publishes a launch gate."
- Caption: *Census of 13 companies' own publications, read 31 October 2026.*
- No mode line: style rule 14's mode requirement is research-only since v1.8.1 (Saurabh, 31 October 2026).

## 7. Things to keep in mind

1. Every figure is a company reporting on its own system, on its own test set. None is audited, and no two are comparable; the piece does not rank them. LinkedIn alone publishes three different accuracy measures (LIN-8, LIN-15, LIN-21).
2. The census counts what each company published, not what it does. A missing practice in the table means the publication does not mention it.
3. The census is not exhaustive. Primary sources only; several known posts (Pinterest, OpenAI, Netflix, Delivery Hero, Swiggy, Fiverr) would not load and are not counted. Databricks, Microsoft and Google publish testing tools for their customers; those are left out, because they describe how customers should test, not how each company checks its own analyst.
4. Three of the 13 sell the product they evaluate (C-3).

## 8. Where Dot fits (under 80 words)

- Open with Dot's own words, whole (hard rule 23, `facts/dot-entity.md`): "Dot answers data questions for your team."
- O1 (Observed, 27 October 2026): each evaluation question in Dot has an expected answer, a unit and a tolerance in percent, and shows a verdict such as "0.52% off expected".
- O2 (Observed, seen twice): the evaluation re-scored on save without a re-run. If the draft says it always does, that is A7 and carries "Assumption".
- Docs link: https://docs.getdot.ai (verified, house file).
- Nothing Superseded. No credit or cost figure: the piece has no run of its own (hard rule 10 is research only).

O1 and O2 were observed on the dry-run work account on 27 October 2026. They are product observations from the facts file, not findings, so hard rule 4 does not bar them; a person may still prefer to re-observe them on the current account before publishing.

## 9. The instruction

Write down real questions your team asked last month, with every answer you would accept for each, and run them against your AI analyst before rollout and again after every change.

Grounded in C-4 (real questions), C-7 and LIN-3 (more than one accepted answer), C-6 (re-run on change). No count of questions is given: no figure supports one, and research section 7 gives Anthropic's "a few dozen per topic" without a figures row (see item 10).

## 10. Missing figures

1. **12**: the census count without Grab. Research section 6 gives it; no figures row. Needed only if the draft states the count without Grab.
2. **"A few dozen" evals per topic before diminishing returns** (Anthropic). Verified on the page (verification, Anthropic, CONFIRMED) but no figures row. Needed if the instruction gives the reader a size for the test set.
3. **The number of publications that failed to load.** Caveat 3 names them instead of counting them. A count needs a census row.
4. **392**, Snowflake's BIRD total: not stated on the page (verification, discrepancy 2). Not to be used; listed so the draft does not reintroduce it.

## 11. Quotable line

Quotable line: Thirteen companies published how they check their AI analyst's answers; only five published a method you could copy. (ID: C-1, C-2)

18 words. Saurabh's wording, with "companies" for "companies" (item 3 of his decisions). Placed in the opening, as its first two sentences in substance, and again as the first sentence of H2 1. It carries its own subject (style rule 12).

## 12. Freshness

Freshness: census measured 31 October 2026 (C-1 to C-8, every source re-opened that day); re-measure in April 2027, or sooner if any of the 13 publishes a new evaluation post. The sources are public, so it is re-measurable. The buyer-phrase volumes behind the titles are not re-measurable, source closed: the Ahrefs snapshot of 27–28 October 2026, whose access ended 31 October 2026.

Approved by:
Date:
