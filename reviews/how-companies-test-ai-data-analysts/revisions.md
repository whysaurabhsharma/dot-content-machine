# Revisions · how-companies-test-ai-data-analysts

## Round 3: after the blind reviews of the reframed draft (31 October 2026)

revise-notes.md (round 3) applied in full. Title and title_approved_by untouched. check_piece.py after revision: 18 pass, 0 fail, 1 partial (check 1, the title: for the headline test), 6 for a human; 1,442 words (teardown cap 1,600). No run file exists for this teardown; the Dot lines rest on piece A's run and figures, the company quotes on the verification file.

### Revise notes

1. **Table carries the seven figures.** Done: Snowflake "51% for GPT-4o on its internal set" (SNO-2); Vercel "80% to 100% success, before and after a rebuild" (VER-2, VER-3; "Success, not defined" stays in its scoring cell). Test-set sizes stay in the body.
2. **Headline once in the opening, once in its section.** Done: the H2 is now "The seven accuracy figures can't be compared"; its first sentence keeps the quotable line; pocket line 2 now reads "Each figure came from its own test set, scored its own way."
3. **Anthropic's drift links Anthropic.** Done: the sentence links Anthropic's own post first; Dot's essay is the second link.
4. **The two fives.** Done: the opening already read "the five that published enough to copy"; "five" doesn't appear in the re-run section or pocket line 6.
5. **13 against 14 moved out.** Done: now its own caveat, with the link; the entry rule is one shorter sentence after the LinkedIn, Uber, ClickHouse and Snowflake paragraphs.
6. **Always-re-scores claim cut.** Done: "Where Dot fits" keeps only "When we checked it on 27 October, the score updated on save without a re-run."
7. **Dot section.** Done: "Two answers didn't say which date they used, so a person read it from their SQL before marking them" sits beside "Every answer matched" (Q6 and Q8, marked with --decide); "Its core needs no special tooling"; figures rows A-2 (8, from piece A's F01) and A-3 (2, from MR-Q6 and MR-Q8) added; A-1 kept.
8. **Claims that outran the figures.** Done, item by item:
   - Hex: "Hex has ground truths too, but they sit on a synthetic company, so it isn't counted."
   - ClickHouse: "built its final set of 201 questions", and the 39 were dropped "before settling on the final 201".
   - Anthropic: "reports an aggregate figure, and around 99% in certain domains" (ANT-2, ANT-3).
   - LinkedIn and Hex "publish how far their judge can be trusted"; the H2 now ends "two publish how far to trust it".
   - Uber threshold: now "Our reading, not Uber's: decide what counts as a regression before the re-run's result comes in."
   - Heading: "Anthropic's accuracy drifted, and the companies that re-run do it on a change or a schedule"; the paragraph separating the re-run group from the strict group stays.
   - Anthropic's row: "Pass/fail per assertion; grader type not stated" (research section 7, Anthropic entry).
   - Prosus's row: "counted for a named method: the agent asks people to clarify and says when it can't find an answer" (verification file, Prosus quotes).
   - "Anthropic's grader can judge the agent's query" cut from the judge section.
9. **Caveats stay at four.** Done: "self-reported" and the three vendors merged; "counts what was published" and "isn't exhaustive" merged; customer tools and 13 against 14 are the other two.
10. **Saurabh's two.**
    - Drift reads as Anthropic's finding: "Anthropic reports that its offline accuracy drifted from about 95% at launch to about 65% over a month", close to the post's own words; Anthropic's post linked first, Dot's essay second.
    - Hex's 2.03% line: moved into the first paragraph of the judge section, right after the list of judges; "Hex's judge accepted the wrong one 35% of the time." stands whole as its own sentence.

### Reader: three stopping points

1. **Headline four times; Snowflake and Vercel's numbers aren't accuracy figures.** Fixed by notes 1 and 2.
2. **Method before anything useful; 13 against 14; the two fives.** Fixed by notes 4 and 5.
3. **"Assumption: it always re-scores…" reads as an internal note.** Fixed by note 6.
- **Claim not believed (95% to 65%).** Fixed by notes 3 and 10: Anthropic is the sentence's subject and its post the first link.
- **The CFO line (Hex 2.03%).** Kept whole and moved up (note 10).

### Fact-checker

- **Numbers 2, 3, 4, 5.** Fixed by notes 8 (Hex, ClickHouse) and 1 (Snowflake, Vercel).
- **Number 13, publication dates.** Stand: publication metadata from research section 7, not findings; check 15 passes.
- **Number 14, "14 companies".** Stands, in the caveat: it is in the title of Dot's own linked census; check 15 passes.
- **Number 15, Dot run counts.** Fixed: A-2 and A-3 added (note 7).
- **Numbers 16, 17 (unloaded posts; 27 October).** Stand: no number in the first; the date is facts/dot-facts.md O2.
- **Product claims 1, 2 (evaluation fields, re-score on save).** Stand: facts O1 and O2, observed; the generalised "always" is cut (note 6).
- **Product claims 3, 4, 5 (every answer matched; computed before asking; no judge).** Stand, now with the two-answers sentence beside them: piece A's run records 8 of 8 correct (F05), and its truth file holds both readings (T2c, T7d, T8c).
- **Product claim 7, practices without a figures row.** Stand where research section 7 or the verification file holds them: ClickHouse's seats from different providers, row alignment and tolerance (research, ClickHouse scoring); Uber's hand-verified golden SQL and LinkedIn's ground-truth queries (verification); LinkedIn investigating judge-human disagreements (research, LinkedIn); Databricks, Microsoft and Google tools (research, customer tooling). Changed: Uber's "gives no size" cut; Grab's "certification" cut ("Canaries and hidden cases", verification); Anthropic's grader sentence cut; "LinkedIn alone publishes…" cut in the caveat merge.
- **Conclusion 1.** Fixed (note 8).
- **Conclusions 2, 3 (heading; "a test passed at launch").** Fixed: heading changed (note 8); the line is now "Anthropic's case shows that a test passed at launch can say little about the same agent a month later." This changes lift-lines.md intended line 3, for a person to update.
- **Conclusions 4, 5, 6.** Fixed (notes 8 and 7).
- **Conclusion 7 ("often more than one right answer").** Fixed: "can have" in pocket line 5 and the body.
- **Conclusion 8 (strict definition).** Anthropic's scoring now stated (note 8). LinkedIn's timing stands: C-2 counts it strict, and its row says the 3 months is the benchmark review.
- **Conclusion 9 (Prosus).** Fixed (note 8).
- **Conclusion 10.** Fixed (note 8).
- **Conclusions 11, 12.** Fixed by notes 6 and 7.
- **Quotes.** "We are biased towards being overly harsh" stands: verbatim in the verification file (Hex). "Exact match" stands: facts O1. "delivered in 2017" stands: piece A's run file, Q1, Q6 and Q7.

### Lift-tester (applied where it overlapped)

- Snowflake and Vercel table cells fixed (note 1); the "Assumption:" line cut (note 6); the re-run group no longer called "five" (note 4). The 53% arXiv link stands: the table intro says each row draws on a company's own publications, plural.

### Knock-on

- pieces/how-companies-test-ai-data-analysts-faq.json: the drift answer replaced with the two revised sentences, word for word.
- lift-lines.md not edited: intended line 1 is stale from round 2, and line 3's wording changed here; both for Saurabh.

## Round 2: reframe after the first headline test failed (Saurabh, 31 October 2026)

- **New finding leads:** "Seven of the 13 companies published an accuracy figure, and no two measured the same thing" (C-9, new row). New first H2 and pocket guide; the opening now carries it.
- **Checked and rejected as the lead:** "none of the 13 published a result" (false: 7 did); Anthropic's drift (Dot already published it, in Rick's essay). The drift paragraph at the top is cut; one sentence remains in the re-run section, linked to the essay.
- **Dot section added** ("The method runs on Dot, and the same problem showed up"), from piece A's run; no number of ours beside the census's.
- **Fixes:** "most" is gone from the opening; "five that published enough to copy"; AI analyst defined as the internal text-to-SQL and analytics agents staff ask for numbers; one line placing the 13 beside Rick's census of 14 builds.
- **No second "seven":** the LLM-judge section names its seven companies instead of counting them.
- **Bank and query:** B is #36, "AI data analyst test questions"; seo_title, meta and queries changed to match. F takes #35 and is the hub.
- **Outline:** quotable line changed after Decision 2 (recorded there).
- **FAQ:** one answer updated to match the piece word for word.
- **Reviews are stale:** the reframe changed most of the piece, so the three blind reviews are re-run on it.


Revised 31 October 2026 after the blind reviews. No revise-notes.md existed for this round. Title and title_approved_by untouched. check_piece.py after revision: 19 pass, 0 fail, 6 for a human.

## Inputs

- **Run file missing.** runs/how-companies-test-ai-data-analysts-run.md does not exist: the piece is a teardown with no Dot run (front matter, outline). Every number is from the figures file; company quotes match the figures file or research section 7 word for word; the Dot lines rest on facts/dot-facts.md O1, O2 and A7 only.
- **H2 3 wording ("Accuracy drifts, so the careful companies re-run their tests on every change") and the named five** were set by Saurabh at Decision 2 and are kept as written.

## Reader: three stopping points

1. **"13 companies, 5 show how" four times; the counting rule vague.** H2 1 now opens on its own finding (8 of 13) instead of the 13/5 line, and the rule is concrete: a company counted when its own publication named a method, gave an accuracy figure for its own system, or described a test set. Pocket-guide line 1 shortened.
2. **Dot as an ad mid-evidence, with a lab-notebook "we observed on 27 October".** All three Dot paragraphs left the evidence sections (H2 1, H2 2, H2 3); Dot now appears only in "Where Dot fits". The dates, "as we observed" and "seen twice" are gone; the re-score line keeps its Assumption label (A7).
3. **The two fives conflated; Uber and LinkedIn's "Strict" rows inconsistent.** H2 3 adds three sentences saying the re-running companies are a different group from the strict methods (GitHub and Salesforce don't say how they score; LinkedIn and ClickHouse don't re-run on every change), without putting a count beside it. Uber's table row now shows QueryGPT's own timing (staging and production, tracked over time) as well as Finch's; the body no longer says QueryGPT has "no trigger". LinkedIn's "Runs when" now reads "Ongoing; experts review the benchmark every 3 months". The table intro says Uber's row draws on two publications.

Also from the reader: the 84.9% claim is now ClickHouse's own sentence quoted whole, with how its column-linked scorer works; "three of the 13" now names all three (Uber added); the lede's promise is now "all 13 methods in one table, with the 5 copyable ones marked", which the piece delivers.

## Fact-checker

1. **"Real questions with known answers" label drifting; WisdomAI uses a public benchmark.** One label throughout, matching C-4: "real questions or ground-truth answers" (lede, pocket guide, H2 1). "Most of the thirteen build the test from their own work" cut. WisdomAI's row adds its validated ground truth.
2. **Uber's strict status assembled from two systems.** Table row now shows QueryGPT's own timing (C-2 counts Uber on QueryGPT, research section 7); Finch kept as the re-run trigger (C-6).
3. **LinkedIn's "when" is a review cadence.** Row reworded (see reader 3).
4. **"On every change" too wide for Salesforce.** Pocket guide and H2 3 body now say "on a change, before each deploy, or daily". The H2 keeps "on every change": Saurabh's wording.
5. **~90% launch bar stated as current.** Pocket guide now says Anthropic "initially used about 90%"; the body already quoted "initially used ~90%".
6. **"Three of the 13" names two.** Uber added: it notes a question can have more than one correct SQL query (C-7, research section 7).
7. **"Models from different providers" unsupported (H2 1).** Now "a panel of models", and "where no two of them agreed" for the 39 dropped questions (CLK-4).
8. **27 October 2026 and "seen twice" without a figures row or run file.** Both cut.
9. **"Scale of 1 to 5" without a figures row.** Cut: "scoring against a rubric".
10. **Publication dates in the table without figures IDs.** Stand: they are publication metadata from research section 7, not findings; check 15 passes.
11. **"Three different accuracy measures" for LinkedIn.** Now names the three kinds (user survey, benchmark ablation, expert review) with no count.
12. **"The five methods side by side" not delivered.** Lede promise changed (see reader).
13. **Dot product claims ASSERTED.** Dot's own sentence (facts/dot-entity.md) opens "Where Dot fits"; the expected answer, unit, tolerance and "Exact match" verdict are O1; the re-score on save is O2 in the past tense; "always" carries the Assumption label (A7). "Show how" and "the kind of test set this piece describes" cut.
14. **Anthropic drift cause asserted.** "The data model moving while the agent's skills stood still" cut in both places; the piece now gives only the post's own heading for the drop.
15. **"Anthropic's fix was procedural".** Cut; the 90% PR figure is now reported as "the same post says", with no causal link.
16. **"Testing once is not enough, and Anthropic has the numbers".** Cut; the opening goes straight to the quoted drift.
17. **Table broader than the body for Anthropic and GitHub.** Anthropic: "When a PR touches a dependency, in CI". GitHub: "On every context or configuration change, before release".
18. **"The published judges are imperfect" rests on 2 of 7.** H2 2 now says "two publish where the judge falls short", and the body names LinkedIn and Hex; Snowflake, WisdomAI and Grab now named as the other judges.
19. **"Leaning harsh and keeping people in the loop" leaned on Anthropic, not counted as a judge.** Now "Hex and LinkedIn respond to their judges' misses in different ways"; Anthropic's query grading is a separate sentence about its grader.
20. **ClickHouse exact-match inference.** Cut; replaced by ClickHouse's own sentence on the 84.9% (CLK-13, verbatim) and its words "proved vital".
21. **"Careful" in the H2 3 heading.** Stands: Saurabh's chosen wording at Decision 2.
22. **"Each row is one company's own publication".** Now "draws on one company's own publications", with Uber's two named.
23. **"None is audited, and no two are comparable".** Now "none says the result was audited" and "the figures can't be compared", each company using its own test set.
24. **Dot's test set "has the same shape" though it holds one expected answer.** Claim cut.
25. **"Exact match" quotes not checked against a run file.** Stands, once: the verdict is quoted from facts/dot-facts.md O1 (Observed); the second use was cut. No run file exists for a teardown.
26. **"Treat skill maintenance as a first class citizen" and "We are biased towards being overly harsh" have no figures row.** Stand: neither contains a number; both are verbatim in research section 7 (Anthropic and Hex entries).
27. **Link-only company claims (LinkedIn judge, Uber, ClickHouse jury, Hex, GitHub, Salesforce, table cells, unloaded posts, customer tools).** Stand: each is a cited publication, linked and read 31 October 2026 (research section 7 and the verification file).

## Lift-tester (not required, applied where it overlapped)

- The ~90% line now says "initially". The "re-run" line no longer says "on every change" and is followed in H2 3 by the sentence separating it from the strict methods. "Exact matching would miss things too" and "The companies answer this by…" replaced with self-contained sentences. "So a re-run needs…" now starts "A re-run therefore needs…".

## Knock-on

- pieces/how-companies-test-ai-data-analysts-faq.json: two answers updated so they stay word for word with the changed sentences.
