# Revise notes · ai-analyst-follow-up-questions · round 3

A person's instructions, Saurabh, 31 October 2026, after the headline test passed on attempt 3. (Round 2's notes are in git history and logged in revisions.md.) Apply every one, and log each in revisions.md under "Round 3" as done, or one line on why it can't be.

## 1. Restructure: visible-vs-hidden is the spine

The finding is ambiguity, not memory: one phrase has two valid readings, both correct, and the risk is whether the answer tells you which one it used.

- **H2 1, first:** both late-order counts were correct, each for a different date. 2,453 by purchase date (MR-Q2), 1,762 by delivery date (MR-Q6); each matches the raw data for its date; each answer's SQL shows its date filter.
- **H2 2, the spine:** the chain named its date, the fresh chat didn't. Q1 named purchase date ("This uses purchase date, not delivery date."); Q6 never named its date (the hidden risk); Q7 named the delivery date ("This uses the customer delivery date, not the purchase date.", the visible version). Where the text is silent, the SQL shows the date.
- **H2 3, memory, demoted and short:** asked four turns later to go back to the first question, Dot re-ran the first query and returned 43,428 again; Q8 kept Q7's delivery-date scope. A few sentences, no more.
- **The test gains a step:** "Check whether the answer names its date. If it doesn't, read the date filter in its SQL." Keep the test's step count in step with the lede's "five-step" claim, or change both together.
- **Pocket guide:** reorder to match (two readings and both correct; visible vs hidden; memory; the test). Five to eight lines.
- **SEO fields:** `seo_title` and `meta` follow the new frame; no "context test", and the meta doesn't open with a memory question. `seo_title` must still contain the piece's query for check 3; meta under 155 characters. Leave `slug` as it is.

## 2. Lede fixes, from the readers

The lede stays within 60 words and four sentences, ends with "By the end, you'll have…", and keeps 2,453, 1,762 and the named-vs-unnamed contrast. If a fix doesn't fit, put it in the paragraph right after the lede and log where it went.

- "Both are correct": say how we know (each matches the raw data for the date it used).
- Say the fresh chat used delivery date without saying so; don't leave the reader guessing which date.
- Define "late" as delivered after the estimated delivery date: in the piece, if not the lede.
- Name the data once as a public e-commerce dataset (Olist).
- Replace "which you got" with "which date your analyst used".

## 3. Hard rule 6: pair the limitation with what Dot does, using only what the run supports

The limitation: in a fresh chat, Dot didn't state which date it used (Q6). Pair it with what this run actually shows:

- **Every answer came back with its SQL (F16: 8 of 8), and the SQL shows the date filter even where the text is silent.**
- **Most answers named their date unprompted (F15: 5 of 8: Q1, Q3, Q4, Q5, Q7).**

Do **not** claim that a context note, an evaluation, or any other feature would prevent or catch it: none of that was tested in this run (and the A5-style claim was cut at the outline). No new remedy.

## Still holding

- The title is Decision 3, approved: “Delivered in 2017” has two right answers. Test which one your AI analyst gives you. Don't change it.
- The rule 14 waiver: no claim about mode, credits, environment or context notes from this run.
- Every number needs a row in figures/ai-analyst-follow-up-questions-figures.csv. If a fix needs a number with no row, stop and report blocked.
- If the chart caption or alt text changes, say so, so charts/ai-analyst-follow-up-questions-late-orders.json can be synced.
