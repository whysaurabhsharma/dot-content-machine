# Dot facts

Every statement about Dot's product that a piece may use. Nothing else about the product may appear in a piece.

Three kinds:

- **Observed**: seen in the product, with the date and where. May be stated as fact, in the past tense if seen once.
- **Assumption**: not confirmed by Dot. Must carry the word "Assumption" in the text where it appears.
- **Confirmed**: a yes from Dot, with who and when. Empty so far.

When Dot confirms or corrects an assumption, move it to Confirmed with the date, and remove the label from every piece that uses it.

`check_piece.py` reads the **Keywords** column: any sentence in a piece that mentions an Assumption keyword without the word "Assumption" fails check 17.

## Observed

27 October 2026, the dry-run work account, Production environment.

| ID | Observation | Where |
|---|---|---|
| O1 | Each evaluation question has an expected answer, a unit dropdown that includes "No unit", and a tolerance in percent. The details panel shows a verdict ("Exact match", "0.52% off expected") and the time taken. | Evaluation, question details |
| O2 | The evaluation re-scored on save without a re-run: 100% → 95% after a deliberate change, back to 100% after reverting. Seen twice. | Evaluation |
| O3 | Context notes have a title, access groups, a Foundational toggle and a description. The note "Olist revenue, order value, basket size, cancellation and shipping metrics" sets eligible orders to `order_status = 'delivered'` for revenue, average order value, basket size and shipping revenue. | Model → Notes |
| O4 | Chat answers stated their population, period or definition unprompted in 22 of the 26 answers that returned a result. The 26 are the 25 answered plus one refusal that returned a coverage statement (D6); the other 3 of the 29 asked back. | 29 ad hoc requests, fresh chats, 27 Oct |
| O5 | The chat composer has a mode selector with Economy and Balanced. | Chat |
| O6 | Chats raise proposals and data-gap items for an admin; duplicates of earlier proposals are marked "Duplicate". | Chat |
| O7 | Billing shows 100 base credits included (27 October 2026). **31 October 2026:** Settings → Billing showed "300 base credits included. Milestones add more.", Credit Usage 73.9 / 300, "Free credits don't reset." and 0 bonus credits earned (screenshot `runs/screenshots/rehearsal-batch-1-credits-before.png`). This supersedes the 100 recorded on 27 October; both readings are kept as observations. Milestones add credits: a live data source +50 for each unique type, Slack or Teams +50, scheduling a call +50, inviting colleagues +10 each (up to 5), scheduling a report +20, a note with the context agent +20. "Spread the word" unlocks after 220+ credits are used. | Settings → Billing |
| O8 | The signup page advertises "$300 in free credits, no credit card required". Signup requires a work email; a Gmail address was rejected. US region, with a switch to EU. | app.getdot.ai/register |
| O9 | The environment menu shows Production, "New environment…" and "Manage environments". | Sidebar |
| O10 | Apps holds dashboards; the account has a "Sample Executive Dashboard" with 37 cards. | Apps |
| O11 | Of the 26 answers that returned a result, 25 contain numbers that were recomputed from the raw Olist CSVs on 28 October; all 25 were correct. Q4 (missing product data) has no number to check. Seller on-time rates (N2) match when "on time" is counted by calendar day: top ten 92.2%, all sellers 93.2%. | Recomputed with pandas on olist_orders_dataset.csv and olist_order_items_dataset.csv |

## Assumptions

Made by Saurabh Sharma, 27 October 2026, answering the product-claim list. Rick asked for assumptions to be made and stated rather than waiting for confirmation.

| ID | Assumption | Basis | Keywords | Claim-list line |
|---|---|---|---|---|
| A1 | Cost per answer may be published, in dollars as well as credits. | Saurabh's answer | — | 1 |
| A2 | 1 credit ≈ $1. | O8's "$300 in free credits" together with O7's 31 October 2026 reading: 300 base credits included, 0 bonus credits earned. Basis corrected 31 October 2026; it cited A3 until then. No Dot page states a price per credit. | per credit | — |
| A4 | A "cheaper than an analyst" comparison may be published if the analyst's cost and its source are stated in the text. | Saurabh's answer: assume, and say so | cheaper than an analyst, analyst cost | 2 |
| A5 | The context agent stores a definition once, and every chat answer uses it. | O3 and O4: eight answers scoped themselves to delivered orders, matching the note | context agent | 4 |
| A6 | Environments let a team test a definition change before it reaches everyone. | O9 only; the behaviour was not tested | environments let | 5 |
| A7 | The evaluation always re-scores when a question is saved. | O2, seen twice; Saurabh: yes | always re-scores | 6 |
| A8 | Dot is comfortable publishing a piece where its evaluation passes a 0.52% definition disagreement. | Saurabh's answer: assume | — | 7 |

| A10 | Olist is acceptable as the trial dataset. Licence: CC BY-NC-SA 4.0. | Rick: pick a realistic dataset; Dot wants to see the thought process | — | — |

## Superseded

Assumptions that a later observation contradicted. Kept as they were stated, with the date and the observation that ended them. A piece may not rely on them.

- **A3, superseded 31 October 2026.** Stated 27 October 2026: "The 300 free credits are 100 at signup plus the rest earned by connecting data sources and connectors." Basis then: Saurabh's answer; consistent with the milestones in O7. Keywords then: free credits. Claim-list line 3. **Contradicted** by O7's 31 October 2026 reading: Settings → Billing showed "300 base credits included. Milestones add more." with 0 bonus credits earned, so the 300 is the base allowance, not 100 plus earned credits (screenshot `runs/screenshots/rehearsal-batch-1-credits-before.png`).

## Confirmed

| ID | Decision | Who and when |
|---|---|---|
| D1 | Voice: pieces and posts publish in Rick's voice. "We" means Dot; no "I", because Rick did not run the tests personally. | Saurabh, 28 October 2026, on Rick's direction (was assumption A9) |
