PRACTICE ONLY: not for publication (hard rule 4)

# OUTLINE: "How do we stop different teams getting different numbers for the same metric?"

Piece slug: `rehearsal`. Outlined 31 October 2026, from `runs/rehearsal-research.md`, `runs/rehearsal-run.md` (batch 1 only), `figures/rehearsal-figures.csv` and `figures/rehearsal-truth.csv`.

**Scope warning.** The research verdict says the piece claims one stored definition *causes* the agreement, so it needs batch 2 (note off). Batch 2 has not run. This outline claims only what batch 1 shows: what happened with the note on. Every causal line waits for batch 2 (see Missing figures).

## 1. Title candidates

Buyer phrases used are from research section 2 only: "conflicting metrics across teams", "same metric", "metric definitions", "semantic layer". None has a measured buyer volume; "semantic layer" (2.4K US) and "metric definitions" (20 US) are marked `is_buyer_query = no`.

1. **Recommended.** Conflicting metrics across teams: we asked an AI analyst for revenue three ways and got two numbers
2. Metric definitions for an AI analyst: finance, sales and marketing all got BRL 137.04
3. Same metric, three teams: what an AI analyst does with one stored definition

Reason for 1: it uses the phrase from the page WebSearch ranked first for this question, and its proof is the run's real surprise (MR-Q1, MR-Q2, MR-Q3), not the clean result.

Title 2 overclaims "all got" as agreement caused by the definition until batch 2 runs; usable only as "with the definition on".

## 2. The opening (59 words)

> **Finance, ops and marketing each ask an AI analyst for revenue. We ran that test in Dot on the Olist dataset, in fresh chats, with one stored definition on. Two phrasings returned BRL 13,221,498. The third returned BRL 15,419,774 and said why: it added freight. By the end, you will have a test to run on your own metrics.**

Figures: MR-Q1, MR-Q2 (13,221,498); MR-Q3 (15,419,774).

## 3. The surprising detail

> "How much did customers spend with us in total?" is a revenue question to marketing. Dot read it as what customers paid, shipping included, and returned BRL 15,419,774 instead of BRL 13,221,498. It was not wrong. It named the freight in the answer, and the figure matches the raw CSVs under that reading. The disagreement was in the question, not the arithmetic.

Figures: MR-Q3 (correct under stated definition, against T03b); MR-Q1.

## 4. Pocket guide

1. Teams disagree on a number because they ask with different words, not different maths.
2. We asked Dot eleven questions on Olist, each in a fresh chat, with one stored revenue definition on.
3. Three phrasings of average order value all returned BRL 137.04.
4. Three phrasings of revenue returned two numbers: BRL 13,221,498 twice, BRL 15,419,774 once.
5. The odd one out added freight, and said so in the answer.
6. The all-orders definition sits close behind: BRL 13,591,644 and BRL 137.75.
7. So test your metric with each team's words, and read the definition every answer states.

Figures: MR-Q5–Q7; MR-Q1–Q3; MR-Q4, MR-Q8. "Eleven" is the question count from research section 7 (design, not a finding); see Missing figures for a count row.

## 5. Three H2s

### H2 1: One stored definition held across three team phrasings of average order value

- Method in plain words: three phrasings of AOV (finance, sales, marketing), fresh chats, note on; then the three order counts.
- Finding: MR-Q5, MR-Q6, MR-Q7 each BRL 137.04 (display rounding of 137.041586; gap classified as rounding, rule 12). Orders: MR-Q9 99,441; MR-Q10 96,478; MR-Q11 625, each exact.
- Limitation: batch 1 shows agreement with the note on; it can't show the note caused it.
- What the product does: the note sets eligible orders to `order_status = 'delivered'` for revenue, AOV and basket size (O3), and every AOV answer named "delivered orders" (run file, Q5–Q7 basis lines). Assumption A5, labelled: the context agent stores a definition once and every chat answer uses it.

### H2 2: A different phrasing can change the definition, and Dot said when it did

- Method: three phrasings of revenue (finance, ops, marketing), judged item by item (hard rule 18).
- Finding: MR-Q1 and MR-Q2 BRL 13,221,498 (delivered, price only). MR-Q3 BRL 15,419,774 (delivered, price plus freight; correct under its stated definition, T03b).
- Matching two of three hides the third; totals would call this agreement.
- Limitation: a stored definition did not stop a phrasing from pulling in a different measure.
- What the product does: the answer states its definition unprompted. Quote Q3's own words, naming the question (rule 13): "including shipping on delivered orders".

### H2 3: The competing definition sits close enough to pass for the right one

- Method: the same metrics asked explicitly across all statuses, as the contrast.
- Finding: MR-Q4 BRL 13,591,644 against MR-Q1 BRL 13,221,498; MR-Q8 BRL 137.75 against MR-Q5 BRL 137.04. Both are definition differences, not rounding (rule 12).
- Limitation: a reader without the definition can't tell which number is meant.
- What the product does: asked for all statuses, Dot dropped the delivered filter and said so: Q4 "across all order statuses"; Q8 "regardless of status".

## 6. The table and the chart

**Table.** One row per question Q1–Q11: team and phrasing as asked; Dot's figure (MR row); the definition Dot stated, quoted from that answer; the truth row it was marked against; verdict (correct, rounding, or correct under stated definition). Shows the three groups side by side so the reader judges item by item.

**Chart.** Horizontal bars, four revenue answers: Q1 and Q2 (BRL 13,221,498), Q3 (BRL 15,419,774), Q4 (BRL 13,591,644). Colour by definition: delivered price only, delivered plus freight, all statuses price only.

- Alt text: "Bar chart of four Dot answers to revenue questions on the Olist dataset. Finance and ops phrasings return BRL 13,221,498. Marketing's returns BRL 15,419,774, with freight. The all-statuses question returns BRL 13,591,644."
- Caption: "Dot's answers to four revenue questions, each in a fresh chat. Olist dataset, 31 October 2026, Balanced mode, Olist metrics note on."

## 7. Things to keep in mind

1. The note-off batch hasn't run, so this shows what happened with the definition on, not that the definition caused it.
2. Q1 ("Finance here: what was our total revenue?") stated the period of all orders, while its figure covers delivered orders only. The number was right; the stated period was not.
3. One run, one dataset, one mode. The docs caveat that the same question can take different paths.
4. Two of five condition screenshots were recorded by hand (environment, credits after), so cost per answer isn't published here.

## 8. Where Dot fits (69 words)

> In Dot, a metric definition lives in a context note, with a title, access groups and a Foundational toggle. Assumption: the context agent stores a definition once, and every chat answer uses it. Each evaluation question holds an expected answer and a percent tolerance, so every team's phrasing can be kept as a test. Assumption: environments let a team test a definition change before it reaches everyone. Docs: docs.getdot.ai.

Facts: O3, A5 (labelled), O1, A6 (labelled). No Superseded fact used.

## 9. The instruction

Pick the metric your teams argue about most. Write it the way finance, ops and marketing each would say it. Ask each in a fresh chat, and check that every answer names the definition it used.

## 10. Missing figures

1. **Batch 2, note off: all eleven answers and their MR rows.** Needed for any claim that the note causes the agreement (research verdict). Without it, H2 1 and the title stay observational.
2. **Freight on delivered orders, BRL 2,198,276.** Appears in Q3's answer text and inside MR-Q3's description, not as its own row. Wanted for the surprising detail.
3. **Gap, all statuses vs delivered:** revenue (MR-Q4 − MR-Q1) and AOV (MR-Q8 − MR-Q5). Not recomputed here; needs rows from a script.
4. **Score: 11 of 11 correct (10 correct, 1 correct under stated definition).** In the run file's findings from `mark_run.py`; no Figures row.
5. **Count of answers that stated their definition** (from the run file's basis lines). Count by script, not by eye (rule 16).
6. **Cost per answer as a credits range, with dollars (A2, labelled), rule 10.** Only a batch total exists (73.9 → 76.6 used, credits-after recorded by hand, no screenshot), and no per-answer credits. No Figures row.
7. **Playbook stage name and link.** Research section 3 leaves it unconfirmed. Not a number, but the piece can't name its stage until it is.

Approved by:
Date:
