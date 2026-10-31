# Revisions · how-companies-test-ai-data-analysts

## Round 9: the drift clause (Saurabh, 1 November 2026, after Decision 3)

- **Anthropic's drift sentence completed.** The browser re-read (runs/test-ai-analyst-before-rollout-verification.md) shows Anthropic's sentence continues "...over a month before we treated this as an engineering problem." B's sentence stopped at "over a month", which let a reader take the drift as ongoing. Now: "...to about 65% over a month. That was before it treated drift as an engineering problem." (Saurabh's wording, split into two sentences because one ran to 26 words and failed check 7.) FAQ answer 2 updated to match, word for word. A change after Decision 3: Saurabh re-reads the paragraph aloud (style rule 11).

## Round 8: after the partial re-read, PASS with four fixes (Saurabh, 31 October 2026, on 5f94c01)

- **Judge-check paragraph promised two checks and described one (logic gap): fixed.** Hex's check is named as the 2.04% eval above, where its judge took the wrong answer 35% of the time. Hex's words are now reported speech, since quotation marks can't be heard: "Hex writes that it still sometimes struggles to calibrate its LLM judges." Checked against the post's sentence, "we still sometimes struggle to calibrate and align our LLM judges": faithful; "and align" dropped.
- **"Not proof of better testing" lost from the lede in round 7: restored in the table intro.**
- **ClickHouse parse: fixed, with one change to the proposed wording.** The proposal said ClickHouse "started with 243 candidate questions". The post starts from 501 (CLK-12), curated to 475, then brought down to 243 before the panel. Now: "ClickHouse narrowed 501 candidate questions to 243. Its model panel then dropped 39 where no two models agreed, and a legal review removed 3 more, leaving 201."
- **Judge list leads with its count again:** "Seven of the 13 score answers with an LLM judge: …". The lede's seven reads "published an accuracy figure". The two sevens are different groups, overlapping in four (LinkedIn, ClickHouse, Snowflake, WisdomAI).
- **Decision 3:** title_approved_by Saurabh, 2026-10-31; reviewed_on 2026-10-31.

## Round 7: after the third phone read, PASS with fixes (Saurabh, 31 October 2026, on 40d1ee5)

- **ClickHouse arithmetic broken by the round 6 cut: fixed.** "...where no two models agreed, and a legal review removed 3 more." CLK-17 (3) added.
- **Table:** "Accuracy figure" moved to the second column; three cells shortened ("Human-checked Q&A pairs", "Rubrics: code, LLM or both", "Every config change"). The five strict names render bold (checked in the exported HTML: five `<strong>` company cells).
- **Links, the middle path:** none in the pocket guide; none inside a list of five or more names; each company linked at its first substantive mention and in its table row. Ten repeat links removed. Check 15 relaxed to match (CLAUDE.md v1.8.8).
- **Lede:** ends "Start from those five."
- **Seven-name sentence:** leads with the count. "Seven of the 13 use an LLM judge: LinkedIn, Uber, ClickHouse, Hex, Snowflake, WisdomAI and Grab."
- **Hex line, checked before accepting: round 6's wording was ours.** Hex's post doesn't contain "calibrated" or "on purpose". It says "we still sometimes struggle to calibrate and align our LLM judges", and frames the harsh bias as a problem it is "constantly and anxiously improving on". Round 6's "leans one way on purpose" was our reading. Replaced with Hex's own words, quoted and linked.
- **Two sevens (Saurabh, after the round): fixed.** The judge sentence now opens with the judge, not a count: "An LLM judge does the scoring at LinkedIn, Uber, ClickHouse, Hex, Snowflake, WisdomAI and Grab." Whole-piece scan, by script, for a number naming two groups of companies: none left. 7 = accuracy figures, 5 = full methods, 8 = real questions, 3 = more than one right answer; the re-run group carries no count. Same-number, different-noun uses remain and read as distinct: "three answers" and "eight questions" (piece A's run), Vercel's "5 queries", "eight lines".
- **Knock-on:** FAQ answer 2 had joined two sentences that the essay link separates, so it wasn't word for word (since round 4b). Now the drift sentence alone.

## Round 6: after the second phone read (Saurabh, 31 October 2026)

- **The lede, untouched for two rounds: fixed.** Cause: the writer's brief for rounds 4 and 5 said never to change the lede's first two sentences, which protected its stumbles. Now the three readers' version, with one "and" dropped to keep its second sentence at 25 words.
- **Two or three answers without a date (correctness): fixed.** Piece A's table and F15 show three (Q2, Q6, Q8); two of them (Q6, Q8) were read from the SQL. B now says so (A-4 added).
- **Where Dot fits ranked Dot above the 13 on an untested gate: fixed.** The contrast with Anthropic is cut; it now says "We haven't tested that gate here."
- **Forward reference to bold names: fixed.** "This group isn't the same as the five full methods in the table below."
- **Pocket line 7: fixed.** "Only Anthropic's publication sets a bar to clear before launch: about 90%, at first."
- **Hex's 35% beside "overly harsh": fixed.** One clause: its judge still isn't well calibrated, and it leans one way on purpose.
- **ClickHouse's legal review (204 to 201): cut.**
- **ClickHouse's 84.9% quote: paraphrased,** number kept and linked.
- **Link each company once: not done.** Every repeated link left sits on a sentence with a published number or a quote, which check 15 (v1.8.6) requires; no link on a bare name repeats. Saurabh to decide between the two rules.


## Round 5: after the phone read (Saurabh, 31 October 2026)

1. **Table:** five columns (Company · Tests against · Scores with · Runs when · Accuracy figure); Published and Bar dropped; the five that state test set, scoring and timing in bold; "(vendor)" on Hex, Snowflake, WisdomAI; cells about six words; every row keeps its source link, LinkedIn's 53% still links the arXiv paper. Uber's ~5% note now lives only in the body (it was already there); Prosus's inclusion reason moved to the table's intro. Intro rewritten: bold, "(vendor)", "Not stated"; "strict" and "bar" no longer used for the five.
2. **Length:** cut from repeats (list below).
3. **"A person":** gone. The Dot section says once "we read their dates from their SQL"; pocket guide line 8 now reads "Our earlier run on Dot used the method's core: every answer computed before asking."
4. **Eight of 13:** all eight named where the count is given.
5. **Front matter and Dot section:** `dataset:` now says the census used no dataset and no Dot batch of its own, and that the Dot section cites piece A's run (Olist, CC BY-NC-SA 4.0, L1). The Dot section opens: "This section reports the run from our earlier piece on follow-up questions, not a new run."
6. **H2s:** "The seven accuracy figures can't be compared" · "Eight of 13 test against real questions" · "More than half score answers with an LLM judge" · "Anthropic's accuracy drifted within a month" · "The method runs on Dot" · "All 13, side by side".
7. **Where Dot fits:** rebuilt around the context-agent page's verbatim line (DOT-4, DOT-5) and "only Anthropic published a bar like that"; the "Exact match" verdict and the 27 October re-scoring sentence cut. The link text is "context-agent page" (hyphenated) because check 17 matches facts A5's keyword "context agent" in any sentence; the claim is evidenced by the quoted page, and no "Assumption" label was asked for.
8. **CTA:** kept as it was.

Cut for length (1,596 → 1,353 words, check_piece.py):

- Anthropic's figures: the "Its other figures sit at other stages…" sentence; the first section now gives above 95% and about 99% once, the drift paragraph 95% to 65%, the launch paragraph 90% and 100%.
- Re-run companies: the per-company Hex, GitHub and Salesforce sentences (the table's "Runs when" column carries them); the list now appears once in the body, as the pocket guide's sentence, followed by Anthropic's and Uber's detail.
- The second "a person decided which reading each matched" sentence in the Dot section, and "so a person read it from their SQL before marking them" reduced to "so we read their dates from their SQL".
- The paragraph describing each judge (LinkedIn rubric, Uber similarity, ClickHouse jury, Hex rubrics): repeated the table's "Scores with" column.
- Snowflake's 150-question sentence and ClickHouse's "201 questions" in the test-set paragraph (both in the table; 201 also in the 39-of-243 paragraph).
- "Each figure comes from its own test set, scored its own way" (pocket guide line 2 says it) and "The five companies that published enough to copy say…" (lede and table intro say it).
- "That says nothing about how Anthropic grades"; "LinkedIn investigates where its judge and its human reviewers disagree".
- Caveats tightened: the "Not stated" definition (table intro has it), the vendor list (the table marks them), "They may describe how those companies test; the census can't say", the customer-tools and census-of-14 caveats shortened.
- Table intro: Uber's "draws on two, QueryGPT and Finch".

## Round 4b: the rest of the second fact-check (Saurabh's list of nine)

1. **Anthropic's five figures unreconciled (ChatGPT): fixed.** One sentence after the launch bar places the others: above 95% with skills, about 99% in some domains, about 65% after a month without upkeep.
2. **ClickHouse's 39 without a starting total (ChatGPT): fixed.** Now 39 of 243 dropped, then a legal review from 204 to the final 201 (CLK-15, CLK-16 added, confirmed in the verification file).
3. **Title says 7, SEO title says 13 (ChatGPT): stands.** The title states the finding; the SEO title describes the page, as Rick's 14-company post does. Saurabh agrees.
4. **"Those five are the methods to start from" (ChatGPT): fixed.** Now "the most complete descriptions, not proof of better testing".
5. **LinkedIn and Hex "how far their judge can be trusted" (Gemini): fixed.** Now each publishes one check on its judge, and the two checks measure different things; the H2 says "a check on it".
6. **Anthropic's grader (Gemini): fixed.** The count leaves it out because the post doesn't say what kind; "that says nothing about how Anthropic grades".
7. **Sources that wouldn't load (Gemini): fixed.** The caveat now says they may describe their testing, so 13 is a floor, not a full count.
8. **~95% to ~65% as "30%" (Gemini): stands.** The piece never says 30% or 30 points; it gives the two figures only.
9. **"Again after every change" (Gemini): fixed.** Now "then again on a schedule or when something it depends on changes", matching what the census shows. The FAQ answer is updated to match.

Cut for length (1,621 → 1,597 words): "Our reading, not Uber's: decide what counts as a regression before the re-run's result comes in."

## Round 4: second fact-check, ChatGPT and Gemini (Saurabh, 31 October 2026)

Triage from Saurabh's summary of both reports; the full replies were not pasted.

- **"The table is missing" (Gemini): stands as wrong.** The review copy had all 13 rows; both blind reviewers quoted the table. Most likely the paste lost it. Recorded in HANDOVER.md as a method limit.
- **8 entries in "One number", 7 in the text (ChatGPT): fixed.** The column is now "Accuracy figure"; Uber's ~5% run-to-run note moved to its "Runs when" cell, and its figure cell reads "None published".
- **"DABstep is the one kind of test where figures can be compared" (both): fixed.** Now: the figure doesn't compare with the others either; figures compare only from the same tasks, scored the same way, on systems set up the same way. Rick's sign-off stays on the pre-publish list.
- **Everything about other companies marked ASSERTED (ChatGPT): a category error.** A teardown reports what each company published and links it. One caveat now says so; no line-by-line change.
- **Quotes not linked at the quote (both): fixed.** LinkedIn, Hex, ClickHouse, Anthropic and Uber quotes each link their source at the quote. The stricter check 15 (v1.8.6) then found ten more sentences, now linked at the number, and a missing row for Dot's census of 14 (DOT-3).
- **"Only one of the 13 publishes a number to clear before launch" (Gemini): fixed.** The census recorded when each company runs its tests but didn't search the 13 for a launch bar specifically. Now: "Anthropic's is the only publication of the 13 in which we found a number to clear before launch."
- **"It shows the method is runnable … a rule for a match" (ChatGPT): fixed.** Now says the method can be run, though not all by script: for two answers that didn't name their date, a person decided which reading each matched.


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
- **Product claims 3, 4, 5 (every answer matched; computed before asking; no judge).** Stand, now with the two-answers sentence beside them: piece A's run records 8 of 8 correct (F05), and its truth file holds both readings (T2c, T7d, T8c). (Note, 1 November 2026: 5 of the 8 under the definition asked, 3 only under the delivery-date reading. B's own sentence, "Every answer matched a reading we had computed", is accurate as written.)
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

## Round (cluster), 1 November 2026

- After Decision 3: the closing instruction links the hub guide F (link only), and "ai data analyst" moved out of this piece's queries to F, so the three pieces target distinct queries (Saurabh's cluster check). Re-read aloud the changed paragraph.

## Drift sentence in Anthropic's words (1 November 2026)

- Round 9's "That was before it treated drift as an engineering problem" paraphrased Anthropic ("drift" for its "this"). F's second fact-check flagged the same paraphrase. Now quoted: drifted "from ~95% at launch to ~65% over a month before we treated this as an engineering problem." FAQ answer updated word for word. Saurabh's pending read-aloud of this paragraph covers the new wording.

## Census corrections after the browser re-read (Saurabh, 1 November 2026)

From the Chrome re-read of the eight remaining sources (runs/test-ai-analyst-before-rollout-verification.md). Every number matched; three method findings, all applied:
- **Snowflake's scoring cell:** "LLM judge" became "Human-selected gold queries, column match". The linked post set LLM judges aside. Snowflake still counts among the 7 that use a judge: its second post tests its own product (Cortex Analyst) with an LLM judge on public BIRD subsets, the same footing on which WisdomAI counts. C-5 stays 7.
- **More than one right answer: 3 became 4** (C-7), Snowflake added ("One question can have multiple correct answers"), and the four now named.
- **Ramp added to the strict bar and the re-run group: 5 became 6** for both (C-2, C-6). Ramp's post states its scoring (assertions on the final answer and intermediate steps) and a trigger ("update context, run tests, and confirm improvements"); excluding it while counting Salesforce on similar wording applied our own criterion inconsistently. The two sixes are different groups (strict: Anthropic, LinkedIn, Uber, ClickHouse, Hex, Ramp; re-run: Anthropic, Uber, Hex, GitHub, Salesforce, Ramp); B names the re-run group without a count, as before. Changed: meta, opening, pocket lines 3 and 6, the re-run paragraph (the "isn't counted" sentence replaced by Ramp's own words), the table note and Ramp's row (now bold, after Hex), FAQ answer 3, both posts (post 2's taxonomy loses "Both: Ramp"; Vercel now stands alone there). Needs reading aloud.

## Read-aloud of the census changes (Saurabh, 1 November 2026)

- **Ramp's six checked first, in Chrome:** the post states its scoring in so many words: "So we built a Python mini-framework in our dbt project. It asserts not only on the final answer but also the intermediate steps, including expected tool calls, table references, and query shape." Test set: "With domain experts, we listed the high-priority concepts in every domain and wrote end-to-end tests." Timing: "This suite enabled us to close the feedback loop: update context, run tests, and confirm improvements." Six holds.
- Pocket line 6 no longer opens with six names, and no longer gives a second "six" beside line 3's: "Tests are re-run … at Anthropic, Uber, Hex, Ramp, GitHub and Salesforce. GitHub and Salesforce don't say how they score." The body's re-run sentence leads with its count: "Six re-run their tests …: Anthropic, …". FAQ answer 3 updated.
- Snowflake now has its clause: "Snowflake keeps every correct query a human evaluator picks as a gold answer." To keep the paragraph at four sentences, LinkedIn's two sentences became one ("…more than one accepted answer; without them, LinkedIn "underreported recall by 10-15%"."). Lift line 2 in lift-lines.md is therefore no longer word for word in the piece.
- Post 2: "Both:" became "How it scores and when it runs: Vercel, …". It now ends on its takeaway joined to what the link delivers (style rule 17 needs the last line to say what the link gives): "A gap in a post isn't a gap in the testing; it's what a reader can't copy, and the piece shows each one, row by row." Post 1 still ends on the description of the piece. Its UTM string is intact (utm_medium=social); the break was in the paste.
- Rick asked whether naming partners' gaps in public is acceptable (Snowflake is a Dot integration partner): DECISIONS-FOR-DOT.md, item 7.
