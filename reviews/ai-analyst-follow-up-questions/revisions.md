# revisions · ai-analyst-follow-up-questions

## Round 7: after the phone read

31 October 2026. Saurabh's phone read passed on 52b3158. He also ran three model reads for a second opinion; he took four fixes and declined the rest. check_piece.py afterwards: 17 pass, 0 fail, 1 partial (check 1, claim title); verify_sources.py: 6 links, 0 failed.

### Fixed

- **Accuracy: Q2 did not name its date (all three model reads).** The table was right: Q2, the 2,453 answer, stated no date; only Q1 did, one turn earlier. The run supports that Q2 kept Q1's purchase-date filter (its SQL carries the same filter; its text doesn't restate it). Fixed in three places: the second H2 is now "The first answer named its date; the fresh-chat answer didn't"; the lede says "the first chat named purchase date"; the method paragraph now says Q2, Q6 and Q8 stated no date, Q2 matched the purchase-date reading its chat had named (MR-Q2, matched by question text), and a person read Q6's and Q8's dates from their SQL. The section also gains: "Q2, the 2,453 answer, kept that purchase-date filter without restating it."
- **Docs placeholder.** "Dot's documentation is at the docs" now links its own address: docs.getdot.ai.
- **Unclear antecedent.** "that chat named purchase date" is now "the first chat named purchase date".
- **ID list cut.** "5 of 8, Q1, Q3, Q4, Q5 and Q7" now ends at "5 of 8". The IDs remain in the table and in F15.

### Considered and declined

The model reads also suggested cutting or restructuring the table, the sections and the caveats. Declined by Saurabh: the models read a markdown file, not the rendered page; he read the rendered piece whole, aloud, on a phone, and it worked. The table, the sections and the caveats stay as they are.

## Round 6: headline test attempt 4

31 October 2026. Attempt 4 passed with one fault, found independently by all three readers: the title said "It Didn't Say Which" while the lede said "but its SQL did".

- **Title.** "Your AI Analyst Picked a Date. Only the SQL Said Which." (the readers' fix).
- **Lede, sentence 3.** "That chat named purchase date. The fresh chat used delivery date without saying so. Only its SQL did." The readers proposed "The chain named…"; "That chat" is used because the lede's first sentence no longer says "chain".
- **Lede, sentence 1.** "in a follow-up chain" is now "after earlier questions in the same chat": our term replaced at its first use. Later uses of "chain" stand; the method paragraph defines it ("Chat A was a chain of five questions").
- **Lede to four sentences (check 8).** The readers' split made six. Saurabh chose version A: "Both are correct for their own date: that chat named purchase date, and the fresh chat used delivery date without saying so. Only its SQL did." It keeps "Only its SQL did." as its own sentence and drops "each matches the raw data"; the next paragraph links the dataset and invites recomputation.
- **Step count.** Checked: the lede, the meta, the test's H2 and the closing instruction say six; the pocket guide and seo_title give no count; no posts or exports exist yet for this piece.

## Round 5: house-style title and phone fixes

31 October 2026, Saurabh's instructions. check_piece.py afterwards: 17 pass, 1 fail (check 1: no promise word in the title; held for a decision on check 1), 1,182 words.

- **Title.** Now "Your AI Analyst Picked a Date. It Didn't Say Which.", matching Dot's blog: short flat claims, often "Your X", no colons or how-to promise. title_approved_by updated by Saurabh's instruction; not headline-tested (human.md).
- **F04.** Description no longer says "recall": "Turns between Q1 and Q5, which asked for Q1's figure again".
- **Fresh chats.** "Our run used two fresh chats; the test needs only one" is now "You need one fresh chat. We used two."
- **Lede, sentence 3 (hard rule 6).** "the fresh chat silently used delivery date" is now "the fresh chat used delivery date without saying so, but its SQL did": the claim title accuses "your AI analyst" and Dot is the first analyst named, so the pairing goes in the lede. Lede 66 words; the promise still falls inside the first 60. check_piece.py afterwards: 17 pass, 0 fail, 1 partial (check 1, claim title, until headline test attempt 4).
- **SQL.** Q2's block cut; the chain's filter is named inline (`order_purchase_timestamp`). One block remains: Q6's delivery-date line alone, verbatim, since that line is the finding. Check 15 confirms it appears whole in the run file.

## Round 4: second fact-check

31 October 2026. Gemini and ChatGPT, each given the round 3 draft only (prompts/05-fact-check.md, pass 2). Triage approved by Saurabh: 10 fixed, 11 stand. check_piece.py afterwards: 18 pass, 0 fail, 6 for a human (1,187 words). Title, title_approved_by, chart caption and alt text untouched.

### Fixed

- **F1. SQL not reproduced (both).** Q2's and Q6's date filters added inline, word for word from the run file; check 15 now fails any code line not verbatim in the run file (scripts/check_piece.py).
- **F2. "A matching total with a different filter is a different answer" (both).** Not something this run produced; relabelled as an instruction for the reader's own test: "When you run this, a total that matches under a different date filter is still a different answer." Lift record updated.
- **F3. "Re-ran rather than repeating a stored figure" (both).** Cut: identical SQL doesn't prove re-execution, and execution is not observable via MCP. Pocket guide line 6, the memory H2 and its paragraph now say Dot returned 43,428 again with the same SQL; the run file's Finding 1 corrected, dated.
- **F4. Missing delivery dates asserted (both).** Now quoted from Dot's Q3 and Q4 answers.
- **F5. "Both ways, each share rounds…" ambiguous (ChatGPT).** Now: "with or without them in the denominator, the chain's shares round to 5.6% and 7.7%."
- **F6. One fresh chat in the test, two in the run (ChatGPT).** Added: "Our run used two fresh chats; the test needs only one."
- **F7. 43,428 against 40,930 unexplained (ChatGPT).** The chain's set is now named: 43,428 orders purchased in 2017 and delivered.
- **F8. Cause not isolated (ChatGPT; Gemini similar).** Caveat now: "One run can't say why the fresh chat read the phrase differently: chat history, a default, or run-to-run variation."
- **F9. "Both are correct" reported, not demonstrated (ChatGPT, central).** "Olist, a public e-commerce dataset" now links to the Kaggle page recorded in data/README.md, "so anyone can recompute it".
- **F10. "day" vs "date" (ChatGPT).** Not a misquote: Q2's answer says "day", and the SQL compares calendar days. The definition now reads "delivered on a later calendar day than the estimated delivery date".

### Stand

- **S1.** Arithmetic confirmed by both; nothing to fix.
- **S2. 7.7% (both).** A chain step, not a finding; the sentence now points to the table: "Q3 and Q4 in the table above". Numerator and denominator stay in the run file.
- **S3. SQL with every answer, 8 of 8.** Observed for all eight in the run file; two are now shown.
- **S4. Q8's delivery-date scope.** In the run file's Q8 SQL; the excerpt is kept to the spine pair.
- **S5. Lede attributes a cause (Gemini).** It describes; F8's caveat says the cause isn't known.
- **S6. Quotes unauthenticated (both).** Chats are in a private workspace; every quote is verbatim from the run file and names its question.
- **S7. Quotes "read blunt" (Gemini).** Dot's exact words.
- **S8. 5 of 8 not auditable (ChatGPT).** The table carries it answer by answer; full texts in the run file.
- **S9. BRL differences unstated (ChatGPT).** Not used by the piece.
- **S10. Docs link (ChatGPT).** The piece claims nothing about the docs' contents.
- **S11. User questions presented as questions (ChatGPT).** Confirmed correct.

## Round 3

31 October 2026, from revise-notes.md round 3 (Saurabh). check_piece.py afterwards: 18 pass, 0 fail, 6 for a human (1,116 words; lede 60 words). Title and title_approved_by untouched. Chart caption and alt text unchanged.

### 1. Restructure: visible-vs-hidden is the spine

- **H2 1 first.** Done: "Both late-order counts were correct, each for a different date" opens the body: method, table, 2,453 by purchase date (MR-Q2) and 1,762 by delivery date (MR-Q6), each matching the raw data for its date, the chart, and the SQL's date-filter columns; 691 (F12), 40,930 (F08), 4.3% (F09) and the rounding note stay here.
- **H2 2, the spine.** Done: "The chain named its date; the fresh chat didn't". Q1's quote ("This uses purchase date, not delivery date."), Q6's unnamed date (quote under Q6, named as Q6), Q7's quote as the visible version, each under its question; then "Where the text was silent, the SQL wasn't."
- **H2 3, memory, demoted.** Done: "Dot re-ran the first question four turns later", two short paragraphs: Q5 returned 43,428 again by re-running the query; Q8 kept Q7's delivery-date scope (BRL 651,458 against 987,765, F14).
- **The test gains a step.** Done: step 5 is now "Check whether the answer names its date. If it doesn't, read the date filter in its SQL." The test is six steps; the lede, the test's H2 and the closing instruction all say six.
- **Pocket guide.** Done: seven lines in the new order: two readings, both correct (with 691); named vs unnamed date and the SQL; memory; the test.
- **SEO fields.** Done: seo_title "AI Analyst Follow-Up Questions: Check Which Date It Used" (56 characters, query words 83%); meta opens with the two correct counts, not a memory question, and has no "context test" (152 characters). Slug unchanged.

### 2. Lede fixes

- **"Both are correct": how we know.** Done in the lede: "Both are correct: each matches the raw data for its date."
- **The fresh chat's date.** Done in the lede: "the fresh chat silently used delivery date."
- **Define "late".** Done in the paragraph after the lede: "Late means delivered after the estimated delivery date", with Q2's own definition quoted under its question.
- **Name the data as a public e-commerce dataset (Olist).** Done in the paragraph after the lede, because the lede was already at 60 words: "We ran this test on Olist, a public e-commerce dataset."
- **"which you got".** Done: the lede now ends "a six-step test that shows which date your analyst used." 60 words, four sentences; 2,453, 1,762 and the named-vs-unnamed contrast kept.

### 3. Hard rule 6: limitation paired with what the run supports

- Done: in H2 2, Q6's unnamed date is followed by "Every answer in this run, 8 of 8, came back with its SQL" (F16) and "Most answers also named their date unprompted: 5 of 8, Q1, Q3, Q4, Q5 and Q7" (F15). "Where Dot fits" now says the same and nothing more.
- No remedy claimed: the context-notes and evaluation-questions lines are cut from "Where Dot fits" (the context-agent link with them), so no feature is said to prevent or catch the unnamed date. Internal links: 5, the Playbook included.

### Still holding

- **Title.** Unchanged, with title_approved_by.
- **Rule 14 waiver.** Nothing on mode, credits, environment or context notes; the caveat on hand-noted settings and the caption's "The run's mode is not stated" stay.
- **Numbers.** Every number has a figures row (check 15: none missing); no new figure was needed.
- **Chart.** Caption and alt text unchanged; charts/ai-analyst-follow-up-questions-late-orders.json needs no sync.

## Round 2, 31 October 2026: after the second reader and fact-checker reviews, with revise-notes.md

check_piece.py afterwards: 18 pass, 0 fail, 6 for a human (1,211 words; longest sentence 25 words). Title and title_approved_by untouched.

### revise-notes.md (Saurabh)

1. **691 in the lede.** Done: the lede now says "delivered in 2017" gave late-order counts 691 apart (F12), that the chain read purchase date and a fresh chat delivery date, and that both matched the raw data; the 43,428 repeat moved to the second paragraph. 4 sentences, 56 words, buyer's question kept, ends on the five-step promise.
2. **No causal claim about chat history.** Done: second paragraph says "In this run, the readings differed between the chain and the fresh chats"; "missed because of reading" is cut; the first caveat says one run can't tell chat history from run-to-run variation. Context notes from the run are not mentioned.
3. **5.6% / 7.7% and 4.3%.** Done: the piece says Dot excluded the orders with no delivery date (two in 2017, F10; six in 2018, F11), the ground truth kept them, and each share rounds to the same figure both ways. The 4.3% (F09) is now said to be a share of 40,930 orders delivered in 2017 (F08), a different set from the chain's purchase-year orders.
4. **"Missed" vs "neither answer is wrong".** Done: "Neither answer is wrong" kept; "missed" and "Judge a control item by item, or you will blame the wrong thing" cut. Nothing now says the control failed.
5. **"A person chose".** Done: the method now says once that a script checked each answer reading only its stated basis, Q6 and Q8 didn't name a date in their text, so a person read each reading from its SQL, which filters on the delivery date. "The SQL settles the question" became "the SQL shows which date each one used"; the table verdicts and caveat now say "reading taken from the SQL by a person". Q8 is included because it was also marked by --decide (MR-Q8).
6. **"Bigger risk than forgetting".** Done: cut; the line now ends at "...still not say which question it answered."
7. **Mixed precision and table header.** Done: BRL 5,962,902.01 is now BRL 5,962,902 (F13) and BRL 987,765.37 is now BRL 987,765 (F14), matching Dot's whole-BRL answers. Table header and pocket-guide line 7 say "date filter"; the SQL paragraph says "date filter" too.
8. **Caption.** Done: "Late orders for "delivered in 2017", asked inside a follow-up chain and in a fresh chat. Olist dataset, Dot, 31 October 2026. The run's mode is not stated." Date kept; no mode, credits or workflow note.

### Reader: three stopping points

- **Stop 1, the lede leads with the dullest result.** Fixed by note 1: the 691 gap leads and is resolved in the same lede.
- **Stop 2, the finding told three times before the first H2.** Fixed: the second paragraph no longer restates 2,453 vs 1,762 or the purchase/delivery split; it adds the 43,428 memory result instead. The third caveat, which repeated the body's exclusion point, is cut.
- **Stop 3, "missed" vs "Neither answer is wrong", and the team-note caption.** Fixed by notes 4 and 8.
- **Claim not believed ("bigger risk ... than forgetting").** Cut (note 6).
- **"If the SQL settles it, why did a person choose?"** Fixed by note 5.
- **Promise arrives late (word 56).** "By the end" now begins at word 47 of a 56-word lede.

### Fact-checker

- **2, 5.6% and 7.7% called the raw-data shares.** Fixed (note 3).
- **3, mixed precision.** Fixed (note 7, F13, F14).
- **4, 4.3% denominator not said.** Fixed (note 3, F08).
- **5, "year filter" header with Q8 on a month.** Fixed (note 7).
- **6, "five-step" has no figures ID.** Stands: structural count of the numbered list, not a finding.
- **7, caption date has no figures ID.** Stands: style rule 14 requires the date; the run file records batch 1 on 31 October 2026.
- **8, MR-Q5 description says "recalled".** Fixed before this round in the figures file (now "Q1's query re-run four turns later").
- **9-12, SQL-based claims VERIFIABLE but SQL not shown.** Stand: the piece names the filtered columns from the run file's SQL; no claim beyond them.
- **13, context notes "where a team can define" ASSERTED.** Stands: observed in Dot's Model → Notes screen (facts O3), a note setting order eligibility.
- **14, evaluation questions with expected answer and percent tolerance ASSERTED.** Stands: observed in Dot's evaluation screen (facts O1), linked to the docs.
- **15, Prove stage description ASSERTED.** Stands: describes the linked Playbook stage.
- **16, "Before the first question" ASSERTED.** Stands: the truth spec and figures/ai-analyst-follow-up-questions-truth.csv were committed at 12:41 (9a7c65d), before the batch 1 run commit at 13:46 (93d3c49); the --decide matching after the run is now stated separately (note 5).
- **17, "missed".** Fixed (note 4).
- **18, history blamed for the different reading.** Fixed (note 2).
- **19, "bigger risk" ranking.** Fixed (note 6).
- **20, person chose vs SQL settles.** Fixed (note 5).
- **21, "Judge a control item by item, or you will blame the wrong thing".** Cut.
- **22, "real questions rarely arrive alone" unevidenced.** Fixed: now "Buyers ... ask whether an analyst keeps context across follow-up questions."
- **23, "That repeats the question's own words".** Fixed: "That reuses the question's phrase "delivered in 2017", which is the ambiguous part."
- **24-27, quotes.** Stand: word for word under their questions.
- **28, caption wording.** Fixed (note 8).

### Lift-tester

- **"More than forgetting" line generalises and leans on "That".** Fixed: the second sentence is cut; the first stands alone.
- **"Judge it item by item, or you will blame the wrong thing" has no fact.** Cut.
- **Other would-not-lift lines ("Only the figure gave the date away", "It recalled", "But"/"So" openers, "The fix is already on the screen", "Two lines of a WHERE clause").** Not in the current piece; nothing to change.

## Round 1

Revised 31 October 2026 after the reader, fact-checker and lift-tester reviews. check_piece.py afterwards: 18 pass, 0 fail, 6 for a human (it had 2 fails before: a 28-word sentence and two five-sentence paragraphs, both fixed).

## Reader: three stopping points

- **Stop 1, the opening (numbers before the problem; "fresh chat" before the chain was explained).** Fixed: the lede now states the question, then the method (a chain of linked questions, then one asked again in a new chat), then the two numbers, then the promise. The second paragraph explains why the two numbers differ, so the pocket guide is no longer needed to decode the opening.
- **Stop 2, internal process in the caption and caveats ("rule 14 waived").** Fixed: the caption now says "Mode not published: it was noted by hand, not screenshotted"; the caveat says the settings were noted by hand, so the piece doesn't publish mode or cost. No internal rule numbers remain.
- **Stop 3, "Where Dot fits" reads as a feature list and buries the takeaway.** Fixed: each feature is now tied to the test (context notes to define "delivered in", labelled Assumption since it wasn't tested; evaluation questions to hold step 2's expected answers). The takeaway now has its own H2, a five-step copyable test, and the closing instruction points to it.

## Reader: other points

- **Claim not believed, "All 8 answers were correct".** Fixed: replaced with what each group matched: the five chain answers the purchase-year reading, the item-price answer its stated definition, and Q6 and Q8 only once a person chose the reading. The method paragraph now says a person chose the reading after the run.
- **Memory test is weak (Q5 re-ran the query).** Fixed: the piece now says Dot re-ran the first query rather than repeating a stored figure, and claims only that it resolved "my first question" correctly.
- **Both exclusions claimed, one quoted.** Fixed: the Q3 and Q4 wording are both quoted and tied to the 2017 and 2018 shares.
- **The copyable test is thin.** Fixed: new H2 with five numbered steps; the closing instruction refers to them.

## Fact-checker: numbers

- **F06 description says "the chain's purchase-year reading of Q7".** Stands in the piece: the piece says "by purchase year", which is correct. The description error is in the figures file, which this stage does not edit; flagged here for whoever owns figures.
- **"two fresh chats" has no row; "second chain" clashes.** Fixed: the piece says "three chats" (F02) and names them; "second chain" is gone.
- **"The raw figures round to 5.6% and 7.7%".** Fixed: reworded to "both are the raw-data shares rounded to one decimal", which states no new number; the values rest on MR-Q3 and MR-Q4.
- **"Two lines of a WHERE clause".** Fixed: cut.
- **"Stage 3 of the Playbook".** Fixed: now "the Prove stage of the Playbook", linked; no number.
- **"31 October 2026" in the caption.** Stands: style rule 14 requires the date in the caption, and it matches the run file.
- **"Most answers named the date they used".** Fixed: now "Some of Dot's answers named the date they used", followed by the two quoted examples.
- **"The late shares left out orders with no delivery date" covers the 4.3% too.** Fixed: the caveat now says "the chain's late shares", tied to the quoted 2017 and 2018 share answers.

## Fact-checker: product claims

- **"It recalled 43,428 orders".** Fixed: "returned", and the piece says Q5's SQL repeated Q1's filter.
- **"Scope held" for Q8 asserted.** Fixed: now rests on Q8's SQL filtering on the delivery date (run file); the table and caveat keep that the reading was chosen by a person for marking.
- **"meant purchase year inside the chain" only a summary column.** Fixed: the SQL section names the filtered column per chat (`order_purchase_timestamp`, `order_delivered_customer_date`), from the run file's SQL.
- **"Each answer's SQL showed..." / "Every answer came with its SQL" asserted.** Fixed: now "Each answer in this run came back with its SQL", which the run file records for all eight.
- **"Dot shows the SQL behind each answer ... on the screen".** Fixed: cut; nothing about the UI is claimed.
- **"The same question can take a different path on another day".** Fixed: labelled Assumption.
- **Context note title, access groups, Foundational toggle.** Fixed: the feature list is cut; context notes are named as where a definition lives (facts O3, observed), and the effect on this test is labelled Assumption.
- **Evaluation question with expected answer and percent tolerance.** Stands: observed in Dot's evaluation screen (facts O1).
- **"Stage 3 ... where a team proves the analyst on a test set".** Stands as a description of the linked Playbook stage, reworded to "tests the analyst on known questions before launch".

## Fact-checker: conclusions that outrun the evidence

- **"Only the figure gave the date away" vs the SQL claims.** Fixed: cut; the piece now says the sentence alone doesn't name the date and the SQL's filter does.
- **"The answer itself gave no basis to infer it".** Fixed: cut; replaced as above.
- **"the same words" / "from the same phrase" when the chain question was worded differently.** Fixed: the piece says every chain follow-up inherited the first answer's reading of "delivered in 2017", and the gap line reads "Two readings of one phrase, 'delivered in 2017', put 691 orders between Dot's answers". The H2 "The same words got a different date in a fresh chat" stands: the fresh chat asked the chain's question written in full.
- **"That is the real risk in follow-up questions, more than forgetting".** Fixed: scoped to "In Dot's run on Olist".
- **"Memory held exactly" rests on one re-run query.** Fixed: cut; see the memory point above.
- **"Before the first question, we wrote the expected answers ... checked".** Fixed: the method now says both readings were computed beforehand and a person chose the reading for unstated answers after the run.
- **"A fresh-chat control that misses can be an interpretation change".** Fixed: scoped to "In this run, Dot's fresh-chat control missed because of reading, not memory."
- **"Scope held" vs "decided by a person" for Q8.** Fixed: scope claim rests on the SQL; the person's choice is stated as a marking decision.

## Fact-checker: quotes

- **Q6 quote cut without ellipsis, introduced as "Dot answered:".** Fixed: now "Its answer began:", naming it as the opening of the answer, in the Q6 paragraph.
- **Q3 fragment with no question named.** Fixed: tied to "The 2017 share"; Q4's wording now quoted for "The 2018 share".
- **Q7 and Q1 quotes.** Stand: word for word and tied to their questions.

## Lift-tester

- **"It recalled ..." has no referent.** Fixed: sentences now name Dot.
- **Lines starting "But"/"So".** Fixed: the lede and pocket-guide line 6 no longer lean on the sentence before.
- **"The fix is already on the screen", "Two lines of a WHERE clause".** Fixed: cut.
- **"All 8 answers were correct" overstates when quoted alone.** Fixed: replaced, see the reader's disbelieved claim.

## After the headline test, 31 October 2026

The headline test failed (reviews/ai-analyst-follow-up-questions/human.md, attempt 1): three readers couldn't tell whether the piece showed Dot working or broken, because the opening gave the gap (2,453 in the chain, 1,762 in a fresh chat) without resolving it. That broke hard rule 6. These revisions came after the three blind reviews, so the reviews describe the old opening, not this one.

- **Lede rewritten** to address the reader, open with the buyer's question, and resolve the gap within 60 words: Dot returned the same 43,428 orders four turns after the first, and "delivered in 2017" meant purchase date in the chain and delivery date in fresh chats, each matching the raw data for its date. Sources: F01, F04, MR-Q1, MR-Q5; MR-Q2 against T2 and MR-Q6 against T2c. 58 words, four sentences.
- **Second paragraph** now carries the two figures the lede dropped: "The two readings gave 2,453 late orders in the chain and 1,762 in the fresh chat, and that gap is not a memory failure."
- **Title** changes from "AI analyst follow-up questions: a context test you can copy" to "Does your AI analyst remember what you asked? We tested Dot: one phrase, two readings" (title A, approved by Saurabh): the buyer's question, the finding, and "tested" as the promise check 1 needs.


## Round (cluster), 1 November 2026

- After Decision 3: the closing instruction links the hub guide F (link only, plus the clause "then the rest of the pre-rollout test"), and "ai data analyst" moved out of this piece's queries to F, so the three pieces target distinct queries (Saurabh's cluster check). Re-read aloud the changed paragraph.

- Read-aloud fix to the closing (1 November): "Run the six steps this week on one phrase your team argues about. Before you trust either number, check which date each answer used. Then run the full eight-step test before rollout." The link is on the last sentence.

- Closing read aloud: PASS, 1 November (Saurabh). PIECE IF clearance confirmed by Saurabh.
