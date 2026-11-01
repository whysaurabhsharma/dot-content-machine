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
| A5 | The context agent stores a definition once, and every chat answer uses it. | O3 and O4: eight answers scoped themselves to delivered orders, matching the note | stores a definition once, every chat answer uses it, every answer uses it | 4 |
| A6 | Environments let a team test a definition change before it reaches everyone. | O9 only; the behaviour was not tested | environments let | 5 |
| A7 | The evaluation always re-scores when a question is saved. | O2, seen twice; Saurabh: yes | always re-scores | 6 |
| A8 | Dot is comfortable publishing a piece where its evaluation passes a 0.52% definition disagreement. | Saurabh's answer: assume | — | 7 |
| A10 | Olist is acceptable as the trial dataset. Licence: CC BY-NC-SA 4.0. | Rick: pick a realistic dataset; Dot wants to see the thought process | — | — |

## Pending Dot's confirmation

**1 November 2026, corrected the same day (CLAUDE.md v1.8.28):** P-2 was recorded as confirmed by Rick and moved to Confirmed, and its label was removed from B and F. Nobody at Dot had confirmed it. P-2 is back here and its label is restored in both pieces. P-1 stays pending (question 1). A1–A8 stay unresolved: the note "add assumption there" was Saurabh's, not Dot's; none of A1–A8 appears in the three pieces.

Added 1 November 2026, under Dot's instruction: where there is doubt, take an assumption, label it in the piece, and write a publish note saying what needs fixing. These differ from A1–A8 in kind, and the piece labels them differently so a reader can tell (CLAUDE.md v1.8.16):

- **Untested ("Assumption: … not tested")**: we don't know whether it is true.
- **Observed, not re-checked ("as observed on <date> and not re-checked since")**: it was true when we looked, and may have changed.

Each P has a publish note (`reviews/<slug>/publish-note.md`) with the exact replacement text if Dot says no. When Dot answers, the P moves to Confirmed, or the replacement goes in and the P is retired, with a change-log line. `check_piece.py` fails a sentence that uses a P keyword without its label ("assumption", or "not re-checked since").

| ID | Assumption | Label kind | Keywords | Pieces | Who confirms |
|---|---|---|---|---|---|
| P-1 | Dot's context agent page describes how merging works today: "Merging re-checks accuracy first: Dot answers its 25 questions again and merges at 95% or more." | Untested | merges at 95% or more | B | Rick (DECISIONS-FOR-DOT.md, question 1) |
| P-2 | Dot's evaluation still holds each test question's expected answer, a unit and a tolerance in percent, as observed on 27 October 2026 (O1). | Observed, not re-checked | a unit and a tolerance in percent | B, F | Rick (question 3), or anyone with a Dot account, by looking |

## Superseded

Assumptions that a later observation contradicted. Kept as they were stated, with the date and the observation that ended them. A piece may not rely on them: `check_piece.py` fails a piece that uses any keyword in this table's Keywords column, labelled or not. Those keywords name the superseded claim itself, so they can be narrower than the keywords the assumption had while it stood.

| ID | Stated 27 October 2026 | Basis then | Superseded | Contradicted by | Keywords |
|---|---|---|---|---|---|
| A3 | The 300 free credits are 100 at signup plus the rest earned by connecting data sources and connectors. (Keywords then: free credits. Claim-list line 3.) | Saurabh's answer; consistent with the milestones in O7 | 31 October 2026 | O7's 31 October 2026 reading: Settings → Billing showed "300 base credits included. Milestones add more." with 0 bonus credits earned, so the 300 is the base allowance, not 100 plus earned credits (screenshot `runs/screenshots/rehearsal-batch-1-credits-before.png`) | 100 base credits, 100 credits, 100 at signup, the 100 plus |

## Confirmed

| ID | Decision | Who and when |
|---|---|---|
| D1 | Voice: pieces and posts publish in Dot's voice. "We" means Dot; no "I", whoever the byline names. (Was "in Rick's voice" until 1 November 2026; changed when Saurabh Sharma's byline exposed the conflict, CLAUDE.md v1.8.18.) | Saurabh, 28 October 2026, on Rick's direction (was assumption A9) |

## Decisions that leave a question open

A decision to proceed, made by a person, where the underlying question stays unresolved. Not a confirmation from Dot, so not in the Confirmed table. The records that list the question as open stay as they are.

| ID | Decision | Who and when | What stays open |
|---|---|---|---|
| L1 | Publication may proceed for `ai-analyst-follow-up-questions`, whose figures are computed from the Olist dataset. | Saurabh, 31 October 2026 | This is a decision, not a resolution. The CC BY-NC-SA 4.0 label (A10) was never verified at source: the Kaggle page loaded without its licence label. README.md ("Before publishing: re-run piece 1's evaluation in a Dot workspace (the trial ran on Olist, licensed non-commercial)") and HANDOVER.md ("The trial used Olist, licensed non-commercial") both still list it as a blocker. Whether publishing Olist-derived figures on getdot.ai is NonCommercial use is Dot's question as publisher, and Dot has not answered it. The gate does not record this decision. **1 November 2026: still Saurabh's decision, Dot sign-off pending (DECISIONS-FOR-DOT.md question 4).** An earlier record said Dot confirmed it; nobody at Dot had (CLAUDE.md v1.8.28). |
| L2 | Publication may proceed for `ai-analyst-shows-sql`, whose figures are computed from the Olist dataset. | Saurabh, 31 October 2026 | The same as L1: a decision, not a resolution. The CC BY-NC-SA 4.0 label (A10) is still unverified at source; README.md and HANDOVER.md still list it as a blocker; Dot, as publisher, owns the question and has not answered it. The gate does not record this decision. **1 November 2026: still Saurabh's decision, Dot sign-off pending (DECISIONS-FOR-DOT.md question 4).** An earlier record said Dot confirmed it; nobody at Dot had (CLAUDE.md v1.8.28). |
| L3 | Publication may proceed for `ai-analyst-how-much-context`, whose figures will be computed from the Olist dataset. | Saurabh, 31 October 2026, before its run | The same as L1. Recorded before the piece's run because all three pieces run on Olist; it covers that piece only as far as it uses Olist. |
| L4 | Publication may proceed for `test-ai-analyst-before-rollout` (guide F), which cites figures derived from the Olist dataset through our own runs (piece A's run, and piece 2's archived run). | Saurabh, 1 November 2026 | L1 and L2 extended to F, on the same terms: a decision, not a resolution. The CC BY-NC-SA 4.0 label (A10) is still unverified at source, and the licence question stays Dot's to own. **1 November 2026: still Saurabh's decision, Dot sign-off pending (DECISIONS-FOR-DOT.md question 4).** An earlier record said Dot confirmed it; nobody at Dot had (CLAUDE.md v1.8.28). |

**31 October 2026:** the pieces L2 and L3 named were not chosen and are archived. L2 still covers piece 2's run, which the guide `test-ai-analyst-before-rollout` may cite; that guide needs its own decision before it publishes Olist-derived figures. L3 no longer applies to anything.
