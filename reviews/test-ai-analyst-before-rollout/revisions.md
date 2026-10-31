# Revisions · test-ai-analyst-before-rollout

## Round 1: after the blind reviews (1 November 2026)

No revise-notes.md existed for this round. The fact-checker reported runs/test-ai-analyst-before-rollout-run.md missing: that is by design (a guide with no run of its own; front matter `dataset:` names the two cited runs). Quotes were checked against those two run files instead: runs/ai-analyst-shows-sql-run.md (the "repeat-question run") and runs/ai-analyst-follow-up-questions-run.md (the "follow-up run").

### Reader: three stopping points

- **Two late-order gaps blurred together (425 and 691): fixed.** The two runs are now named everywhere as "our repeat-question run" (425: timestamp against calendar day, both purchase-year) and "our follow-up run" (691: purchase date against delivery date). The step-list H2 opens with what each run asked (6 questions × 2 fresh chats, RP2-F01/F03; 8 questions, 5 in a chain, RA-F01/F03), and the two-readings H2 says outright that the 691 gap is separate from the 425 one.
- **Step 6 judge paragraph ended on a pointer, not a result: fixed.** The step now gives its advice in the bold line (mark against written answers before trusting an LLM judge), the evidence (Hex's judge accepted the 2.03% answer 35% of the time), and the census count (7 of 13 use an LLM judge, C-5). "Dot's census lists how all 13 score" is cut. LinkedIn's "within 1 point" is cut from the step: the reader asked "1 point on what scale?" and the figures record doesn't say.
- **Last section repeated steps 7 and 8: fixed.** The bar (~90%, 1 of 13) now appears only in step 7, and the re-run count (5 of 13) only in step 8. The last H2 now carries only what the steps don't: Anthropic's drift, the accuracy-decay essay and Uber's run-to-run rule. "Where Dot fits" lost its internal-note line ("We haven't tested it against the steps above").
- **Smaller snag, step 4's third answer: fixed.** The step no longer says a person read two dates from the SQL. It says the SQL of all 8 filtered on a named date column (opened all 8 in the run file: Q1-Q5 `order_purchase_timestamp`, Q6-Q8 `order_delivered_customer_date`), so the scope a text left out could be read there.
- **Claim not believed, "Both numbers were right": fixed.** Cut. The opening now says each count matches the raw data under the definition its answer stated, that the calendar-day reading was the one we planned, and, outright, that to a buyer the same words giving two counts is an inconsistency, which step 3 is built to catch. Paired (rule 6) with what the product did, from the run file: each answer named its definition in its text.
- **Lede's last sentence described the article: fixed.** Now "By the end, you'll have eight steps, and the one thing no evidence settles yet: the bar to pass."

### Fact-checker: numbers

- 1.2 / 1.3 / 3.2, "both correct" for 2,878: fixed in the lede and opening ("each correct under its own definition"; RP2-MR-Q5 says correct under stated definition, not the one asked).
- 1.6, "real questions or ground-truth answers" would admit Hex: fixed to C-4's wording, "real questions or expert ground-truth queries".
- 1.7, domain experts attributed to the arXiv paper: fixed. 133 and 10 stay on the arXiv link (LIN-10); domain experts now attributed to LinkedIn's engineering blog (LIN-1), linked.
- 1.8, RA-F05 (7 + 1) against RA-SPLIT (5 + 3): stands. Not a contradiction: F05 records mark_run's labels, where the two `--decide` answers (Q6, Q8) read "correct"; RA-SPLIT and the run file's item-by-item line count them against the reading planned. The piece uses RA-SPLIT, as the outline requires.
- 1.12, "two of the other three ... read the date from the SQL": fixed (see step 4 above).
- 1.14, 43,428 "again": fixed to "returned 43,428 again, from the same SQL" (RA-MR-Q5).
- 1.21, the drift quote ran past ANT-5's recorded text: fixed. The direct quote is gone; the piece now uses the two sentences Saurabh set for B and FAQ answer 2 ("...over a month. That was before Anthropic treated drift as an engineering problem."). The clause rests on the browser re-read in runs/test-ai-analyst-before-rollout-verification.md; ANT-5/ANT-6's quote column still ends at "over a month." and could be extended by a person.
- 1.26, "27 October 2026" with no figures ID: stands. A date, not a figure; the observation is facts O1 and O2.
- 1.27 / 3.11, "all 13 companies score": fixed to 7 of 13 with an LLM judge (C-5).
- 1.3, 1.25, other unlabelled structural counts: stand; check 15 passes, 56 numbers, none missing.

### Fact-checker: product claims marked ASSERTED

- 2.1-2.9: stand as evidenced. Each rests on a recorded answer, SQL or figure in the two cited run files (Q5/Q11 question text identical, run file lines 327 and 629; answers verbatim at lines 339 and 641; SQL for all 20 answers). The piece links piece A's published post for the follow-up run.
- 2.8, the fresh chat "read the phrase by delivery date": stands. Q6's SQL filters on `order_delivered_customer_date`; the text didn't say so, which is the step 4 finding.
- 2.10-2.12, Dot's evaluation: stand on facts O1 and O2 (observed) with the docs link; A7 stays labelled "Assumption".
- 2.13, "Dot answers data questions for your team.": stands; facts/dot-entity.md, hard rule 23.
- 2.14, essay "starts from that figure": stands; same sentence B carries after its fact-checks.

### Fact-checker: conclusions that outran the evidence

- 3.1, "A test passed at launch says little...": fixed to "Anthropic's case shows that a test passed at launch can say little about the same agent a month later", with the engineering-problem clause before it.
- 3.3, "computed every expected answer first": stands, reworded to "before the first question". Git shows each truth spec committed before its run: follow-up run truth 9a7c65d (12:41) before the first question (13:37); repeat-question run truth, T5b included, 364d043 (17:04) before batch 1 (6a8978d, 17:13).
- 3.4, "correct as asked / only under that second reading": fixed to "matched the reading we had planned / matched only the second reading, by delivery date", since "delivered in 2017" allows both.
- 3.5, "Mark the answers by hand first" when our runs were marked by script: fixed. Step 6 and pocket line 6 now say mark against your written answers before trusting an LLM judge.
- 3.6, "Reading the SQL is how a person told the two readings apart": fixed to "The SQL showed the scope that the text left out." The run file records `--decide`, not how the person decided.
- 3.7, the chain may never have been given the phrase, and other conditions weren't ruled out: fixed. Step 5 quotes the chain's first question ("How many orders were delivered in 2017?"), says the fresh chat asked "in other words", and ends "evidence the shift can happen, not why or how often".
- 3.8, "They show the steps catch something": fixed to "They show steps 2 to 6 catching something".
- 3.9, "the census ranges too widely": fixed to "only one of the 13 companies published a bar" (C-8).
- 3.10, the lede's "each resting on a run of ours or a published method": fixed (lede sentence replaced).
- 3.12, "Re-runs also vary on their own": fixed. Uber's line is now presented as a rule for small swings, not a measured variance.

### Fact-checker: quotes

- 4.1, 4.2: checked word for word against runs/ai-analyst-shows-sql-run.md lines 334/339 (Q5) and 636/641 (Q11). Both exact. The paragraph names the question asked.
- 4.3, "Exact match": stands as a UI label from facts O1, introduced with "such as"; not an answer quote.

### Lift-tester

- Its quote risk (425 and 691 mixed up): fixed by the run names above.
- "Both numbers were right" and the lede's last sentence: cut. The step-list H2 reworded ("...and each says what it rests on"). "Questions that teams really ask are often ambiguous" cut.

### Knock-ons and open points for a person

- **FAQ JSON:** answer 4 updated to step 5's new wording; all four answers re-checked by script as word-for-word substrings of the piece (markup removed).
- **Check 25 still FAILs** against the existing lift-tester report, which predates this round. Also, **the approved outline's quotable line says "both correct"**, which the fact-check found overclaims for 2,878. The piece now says "each correct under its own definition". The outline is approved and not edited here; a person should decide whether to amend its quotable line to match before the lift test is re-run.
- **Rule 4 question, not resolved here:** the repeat-question run is piece 2's archived run, which is unpublished; hard rule 4 bars unpublished runs outside the piece's own run. Saurabh approved the outline with it (Decision 2) and L4 covers its licence, but the rule 4 point itself is not recorded as decided.
- check_piece.py: 18 pass, 1 fail (check 25, above), 6 for a human. Style rule 11: the changed paragraphs (most of the body) need reading aloud.

## After revise: two decisions (Saurabh, 1 November 2026)

- **Piece 2's archived run may be cited.** Hard rule 4 amended (CLAUDE.md v1.8.12): a run of ours, on the same account and dataset, may be cited by a later piece; its run file is the evidence.
- **Quotable line changed after approval:** "both correct" became "each correct under its own definition" (24 words), as the fact-checker asked. Lift-tester re-run on the current draft: check 25 PASS, 100% match. check_piece: 19 pass, 0 fail.
- **Headline test capped at two rounds** (Saurabh): if round 2 fails, ship the better title and record that it was capped for time.

## After the headline test (Saurabh, 1 November 2026)

- **The bar.** The Playbook (opened in Chrome, 1 November 2026) says at Stage 3, "Prove": "Hold access until the tests pass your bar (~80%)", and "Move on when: the tests clear the bar and stay there through a week of changes." Step 7 now reads: Anthropic started at about 90%; our Playbook suggests about 80%; no published evidence settles which; pick yours before you see the results, and write it down. Saurabh's proposed "so step 8 shows how to set yours" was not used: step 8 is the re-run step, and no run of ours or publication shows a way to set a bar, so saying a step shows how would be an untested remedy (hard rule 19). PB-1 added.
- **Lede:** second sentence split; definitions named ("by the exact delivery timestamp", "by the delivery day"); the last clause is now the two published bars. The quotable line moved verbatim into step 3 (still in the first H2, so check 25 holds).
- **2,453 across A and F:** the same definition in both runs (late, by calendar day, among delivered orders purchased in 2017). F's step 3 now uses A's words: "2,453 late orders among those purchased in 2017".
- **Cluster:** target queries de-duplicated: F (hub) owns "ai data analyst", "how to evaluate ai data analyst accuracy", "ai data analyst accuracy"; B keeps "ai data analyst test questions", "text to sql accuracy"; A keeps "AI analyst follow-up questions context", "conversational analytics". A and B now link to F from their closing instruction; F links to both in the steps.

## Second fact-check: ChatGPT and Gemini (Saurabh, 1 November 2026)

- **5.6% and 7.7% (Gemini): fixed.** "Display rounding of exact values" can't explain a 2.1-point difference; they are different years. Now: "Dot gave the late share as 5.6% for 2017 and 7.7% for 2018. Each matched our computed share for its own year once rounded for display, so neither was a disagreement." (A's MR-Q3: expected 5.64843%; MR-Q4: 7.725972%.)
- **Steps flagged as weakly evidenced (both): stand.** Each is already labelled with its evidence. A caveat added: every step names the evidence behind it, and several say openly that nothing tests whether the step works. This is hard rule 19 working; recorded as a limit of the second fact-check method (HANDOVER.md).
- **"Without that reading written down, a test would have marked those 3 correct answers wrong" (both): fixed,** scoped to our test, here and in the second H2.
- **"That was before Anthropic treated drift as an engineering problem" (Gemini): fixed.** Our clause paraphrased Anthropic's "before we treated this as an engineering problem"; "drift" for "this" was our word. Now Anthropic's own words in quotation marks: drifted "from ~95% at launch to ~65% over a month before we treated this as an engineering problem." Same fix in B (its round 9 sentence had the same paraphrase), and both FAQ files, re-checked word for word.
- **"Anthropic is the only one of the 13 to publish a numerical threshold" (ASSERTED): fixed by scoping, and the link stands as the evidence.** Dot's census is a post on getdot.ai, which hard rule 4's exception names ("or that Dot published in a post on getdot.ai"), and the census is the primary publication of that count (C-8), not a summary of it. F carries C-8 as a figures row. The sentence now matches B's own wording: "Anthropic's is the only publication in which the census found a number to clear." Condition: B must be live before F, or the link 404s (publish order A, B, F).

## Step 3 echo and the quotable line (Saurabh, 1 November 2026)

- Quotable line changed to "In our run on Dot, one question asked in two fresh chats returned 2,878 and 2,453, each correct under its own definition."; step 3 no longer repeats its own instruction. B's SEO title made singular: "How 13 Companies Test Their AI Data Analyst" (query words 80%).
- **Lift-tester re-run: check 25 FAIL, 47%.** The blind tester didn't lift the new line; it lifted the opening's version instead: "In our run on Dot, one question returned 2,878 late orders counting by the exact delivery timestamp, and 2,453 counting by the delivery day." Not a checker fault. Open for Saurabh: adopt the lifted line as the quotable line (EDIT: "until the lifted lines are better than the intended ones").
