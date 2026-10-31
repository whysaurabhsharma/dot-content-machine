# Revise notes · ai-analyst-follow-up-questions

A person's instructions for the revise round after the second reader and fact-checker reviews. Saurabh, 31 October 2026. Apply every one, and log each in revisions.md as done, or one line on why it can't be.

1. **Put the 691 in the lede** (F12: 2,453 in the chain minus 1,762 in the fresh chat). A repeated answer to a repeated question (43,428 at Q1 and Q5) is the dullest result and must not lead.
2. **No causal claim about chat history.** Write "in this run, the readings differed between the chain and the fresh chats", not that the history caused it. The same context notes were on throughout, so they can't explain the difference, but one run can't rule out run-to-run variation either. Don't mention the notes (the rule 14 waiver bars it).
3. **5.6% and 7.7%:** say plainly that Dot excluded the orders with no delivery date (two in 2017, F10; six in 2018, F11) and the ground truth didn't, and that the shares round the same. **4.3%:** say plainly that its denominator (40,930 orders by delivery date, F08) is a different set from the chain's.
4. **Resolve "missed" against "neither answer is wrong".** Neither answer is wrong: both match the raw data for the date each used. Remove "missed" and anything else that says the control failed.
5. **Explain "a person chose" properly:** mark_run.py reads only an answer's stated basis; Q6's text didn't name its date; so a person read the reading from Q6's SQL, whose year filter is on the delivery date. Say that once, instead of two claims side by side.
6. **Cut the "bigger risk than forgetting" ranking.** One run can't rank two risks.
7. **Fix the mixed precision** (BRL 5,612,818 beside BRL 5,962,902.01: use the same precision for both, with a figures row for any new rounding) **and the "year filter" table header** (Q8 filters on a month: say "date filter").
8. **Rewrite the caption so it doesn't read like a team note.** It still gives the date (style rule 14) and must not name the mode or the credits (rule 14 waiver). For example: "… Olist dataset, Dot, 31 October 2026. The run's mode is not stated."

Constraints that still hold: the title is Decision 3 and stays as approved; the lede stays within 60 words and four sentences, ends on what the reader will have, and keeps the buyer's question; every number needs a row in figures/ai-analyst-follow-up-questions-figures.csv, so if a fix needs a number that has no row, stop and report blocked rather than inventing one.
