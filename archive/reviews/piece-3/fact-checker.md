# fact-checker · piece-3

Started with: Fact-check reviews/piece-3/draft.md against figures/piece-3-figures.csv and runs/piece-3-run.md.

The run file `runs/piece-3-run.md` does not exist, so I could not check any Dot quote against it (see section 4). The memory folder was empty, so there were no earlier mistakes to look for.

**1. Numbers: internal consistency and figures file**

1. "5.8 credits", Economy batch (L3, L5, L25, L45, L50, alt text): 73.0 − 67.2 = 5.8 checks out. Figures C07 = 5.8.
2. "5.3", batch 1 (L5, L25, L45, L50): 67.2 − 61.9 = 5.3 checks out. Figures C06 = 5.3.
3. "61.9", "67.2", "73.0" (L25, L43–44): match C03, C04 and C05 (C05 is recorded as 73).
4. "10 of 10 correctly", "all correct" (L3, L5): match C18 and the table's "Yes" in every row.
5. "nine of ten in Balanced" (L5, L27): matches C10 = 9. "One Economy answer" in batch 1 (L81) matches C23 = 1.
6. "half a credit" (L7, L50): 5.8 − 5.3 = 0.5 checks out. Figures C22 = 0.5.
7. "Twenty answers cost 11.1 credits" (L25): 5.3 + 5.8 = 11.1 checks out. Figures C02 = 20 and C20 = 11.1.
8. "0.58" per answer (L46, L56): 5.8 / 10 = 0.58 checks out. Figures C08.
9. "off by up to 0.1" per total and "0.2" for the gap (L52): 2 × 0.05 and 4 × 0.05 check out. Figures C17 = 0.1 and C29 = 0.2. No separate ID for the 0.1-per-total bound.
10. "about 520 answers" (L56): 300 / 0.58 = 517.2, so "about 520" holds. Figures C27 = 520 (C12 = 517 is the exact value).
11. "300 credits" / "300 base credits" (L56, L87): match C11 and C26.
12. "$0.58 an answer" (L56): this is 0.58 × the assumed $1 per credit. No figures-file ID.
13. "1 credit is about $1" and "$300" (L56, L87): C26 records the $300 signup claim. The "$1 per credit" rate has no ID of its own; the draft labels it an assumption.
14. "BRL 5,962,902.01" (L68): matches C15. "BRL 6,155,806.98" (L68): matches C16.
15. "BRL 137.04" (L70): matches C25. "137.75" (L70): matches C28.
16. "Two answers in each batch" (L68): matches C14 = 2.
17. "All four of those answers" and "those four" (L72, L74): 2 × 2 = 4 is consistent, but there is no figures-file ID.
18. "two context notes active" (L23): no figures-file ID. It also doesn't match the rest of the draft, which only ever describes one context note ("the context note sets", L23; table column header).
19. "28 October 2026" (L23, L62): matches the date column for C01–C10 and C14–C25, C28–C29. There is no ID for the date itself.
20. "seven steps" (L9): the list has 7 items, so it is consistent. No ID; none needed.
21. "Ten questions" (L3, L23): matches C01 = 10.
22. "Row counts, sums and one average" (L80) **does not match the draft's own table**. There are two averages (Q3 "Average item price", Q9 "Average order value") and one percentage (Q10).
23. "four questions a month or four hundred" (L58): illustrative, with no ID.
24. "2017" (L40, L68): appears only in the descriptions of C15 and C16.
25. "each mode ran once" (L82) **is not consistent with the draft**. Balanced never ran as a batch: batch 1 was 1 Economy + 9 Balanced (L27, L81).

**2. Claims about what a product does**

1. "Ask an AI data analyst what one answer costs and you get a credit bundle, not a number" (L3): ASSERTED.
2. "Billing counts credits used, to one decimal place" (L25, L87): VERIFIABLE (the table shows the readings).
3. "the selector switched after question 1" / "Mine switched after the first" (L14, L27): ASSERTED. No screenshot or log is shown, and nothing shows the switch came from the product rather than the user.
4. "The mode selector sits in the chat composer" (L29): ASSERTED.
5. "Batch 2 was Economy for all ten, checked on screen before each question" (L27): ASSERTED.
6. Dot scoped Q8 to delivered orders and named the scope (L68): VERIFIABLE in the draft (it quotes the answer), but not checked against the run file because that file is missing.
7. Dot scoped Q9 to delivered orders (L70): VERIFIABLE in the draft (fragment quote only), with the same run-file caveat.
8. "All four of those answers named their scope in the reply, unprompted" (L72): ASSERTED for the two batch 1 answers and partly for Q9. Only batch 2 Q8 is quoted in full.
9. The context note sets the delivered-orders definition (L23, table column): ASSERTED. The quoted answer attributes the scope to "the default Olist revenue scope", not to a context note.
10. "The free tier includes 300 base credits" (L87): ASSERTED in the draft (C11 records a Billing page source).
11. "milestones such as connecting sources or inviting colleagues add more" (L87): ASSERTED.
12. "the $300 advertised at signup" (L87): ASSERTED.
13. "the chat timestamps are per minute and include typing" (L83): ASSERTED.
14. "A Power BI licence or a Tableau seat costs the same whether your team asks four questions a month or four hundred" (L58): ASSERTED (links only).
15. "Credit pricing moves with use" (L58): ASSERTED.
16. "both batches ran the same ten questions in the same order" (L50): ASSERTED. The figures file (C01) records the same questions but not the order.
17. "We found no Dot page that publishes a dollar price for a credit" (L56): ASSERTED, and it **contradicts L87**, where the signup page is cited as advertising $300 for 300 credits.

**3. Conclusions that go further than the evidence**

1. L3: "Economy didn't save credits over Balanced" has no qualifier. The evidence is one run against a mixed-mode batch, and the body itself limits the claim to "on these ten questions".
2. L7: "choosing Economy saved nothing; it used half a credit more" is drawn from one run per batch. The comparison batch was not all Balanced, and batch 2 always ran second (L82), so order is not controlled for.
3. L52: "A gap of half a credit is larger than that" only rules out display rounding. Saying "It shows Economy didn't save credits here" treats the gap as settled, even though run-to-run variance and batch order (L80, L82 admit both) are not excluded.
4. L72: "All four of those answers named their scope in the reply, unprompted" goes beyond what is shown, which is one full quote and one undated fragment.
5. L74: "those four would have scored wrong" depends on batch 1's Q8 and Q9 values, which are never shown.
6. L23 / table: says the context note set the scope, but the evidence quoted (L68) names "the default Olist revenue scope".
7. L87: "accurate to about a tenth" while L52 says the gap between batch totals can be off by up to 0.2.

**4. Quotes presented as Dot's words**

1. The run file `runs/piece-3-run.md` does not exist, so neither quote could be checked word for word against the answer it is said to come from. Both are unverified.
2. Q8 (L68): "This uses the default Olist revenue scope: delivered orders purchased from January 1 through December 31, 2017, excluding freight." It is presented as a full sentence from batch 2. Not checkable against the run file.
3. Q9 (L70): "using delivered orders and merchandise value only" is presented as a fragment with no batch named. That is inconsistent with the Q8 quote, which is a full sentence tied to batch 2. Not checkable against the run file.
4. Neither batch 1 answer to Q8 or Q9 is quoted, although L72 makes a claim about all four.

I created the memory file and added 11 lines for the problems above: `C:\Users\LENOVO\OneDrive\Documents\1Sauarbh\1Dot\dot-content-machine\dot-content-machine\.claude\agent-memory\fact-checker\MEMORY.md`
