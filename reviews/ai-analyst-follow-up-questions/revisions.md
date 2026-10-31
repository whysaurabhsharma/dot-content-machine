# revisions · ai-analyst-follow-up-questions

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

