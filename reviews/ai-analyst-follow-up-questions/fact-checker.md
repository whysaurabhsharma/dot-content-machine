# fact-checker · ai-analyst-follow-up-questions

Started with: Fact-check reviews/ai-analyst-follow-up-questions/draft.md against figures/ai-analyst-follow-up-questions-figures.csv and runs/ai-analyst-follow-up-questions-run.md.

I read all three files. The run file exists.

**1. Numbers**

All the arithmetic I checked is correct:
- 2,453 − 1,762 = 691
- 1,762 / 40,930 = 4.30%
- 5.64843 rounds to 5.6; 7.725972 rounds to 7.7
- 5 chain questions + 1 in chat B + 2 in chat C = 8

These match the figures file:
- 43,428 (MR-Q1, MR-Q5)
- 2,453 (MR-Q2)
- 1,762 (MR-Q6)
- 5.6% (MR-Q3)
- 7.7% (MR-Q4)
- BRL 5,612,818 (MR-Q7)
- BRL 651,458 (MR-Q8)
- 8 questions (F01)
- five-question chain (F03)
- "four turns later" (F04)
- "All 8 answers were correct" (F05)
- BRL 987,765.37 (F07)
- 40,930 (F08)
- 4.3% (F09)
- "two orders" with missing delivery dates (F10)
- 691 (F12)
- BRL 5,962,902.01 (F06)

Problems:
- **BRL 5,962,902.01:** F06's description calls it "the chain's purchase-year reading of Q7". Q7 was in fresh chat C, not the chain. The value matches; the description in the figures file is wrong.
- **"two fresh chats" (lines 12 and 24):** no figures-file row. It can only be worked out from F02 (3 chats). Line 43 then calls chat C "the second chain", which clashes with "two fresh chats".
- **"The raw figures round to 5.6% and 7.7%" (line 41):** the raw values (5.64843, 7.725972) appear only inside the MR-Q3 and MR-Q4 descriptions. No row of their own.
- **"Two lines of a WHERE clause" (line 73):** no figures-file ID.
- **"Stage 3 of the Playbook" (line 22):** no figures-file ID.
- **"31 October 2026" in the caption:** no figures-file ID. The date does match the run file.
- **"Most answers named the date they used" (line 67):** this rests on the table's 5 of 8 "Yes". No figures-file ID.
- **"The late shares left out orders with no delivery date" (line 79):** this is true of 5.6% and 7.7%. The draft also gives a third late share, 4.3% (line 55), and Dot's Q6 answer text says nothing about exclusions.

**2. Product claims**

- "It recalled 43,428 orders four turns later": VERIFIABLE, from the table's Q1 and Q5. But Q5's SQL in the run file is identical to Q1's, so Dot re-ran the query; it didn't recall the figure.
- "Scope held: 'How much of that came in November?' kept the delivery-date reading": ASSERTED in the draft. The only evidence is the table's SQL column, and the table marks Q8 "reading decided by a person".
- "'delivered in 2017' meant purchase year inside the chain, delivery date in a fresh chat": VERIFIABLE only as a summary column. No SQL is shown except two column names.
- "Each answer's SQL showed which date it filtered on" and "Every answer came with its SQL": ASSERTED. The draft shows no SQL.
- "Dot shows the SQL behind each answer, so the date filter is visible" / "The fix is already on the screen": ASSERTED. No screenshots were saved, the run file says "Model: not observable via MCP", and nothing shows what the UI displays.
- "Dot also said it had excluded orders with no delivery date": VERIFIABLE (quoted).
- "Dot made the choice visible at turn one": VERIFIABLE (quoted).
- "The same question can take a different path on another day": ASSERTED.
- "a definition ... can live in a context note, with a title, access groups and a Foundational toggle": ASSERTED.
- "Each evaluation question holds an expected answer and a percent tolerance": ASSERTED.
- "Stage 3 of the Playbook, where a team proves the analyst on a test set before launch": ASSERTED.

**3. Conclusions that go further than the evidence**

- **Line 5:** "Only the figure gave the date away." This contradicts line 17 ("Each answer's SQL showed which date it filtered on") and line 63 ("In both fresh chats, it sat on the delivery date").
- **Line 69:** "The answer itself gave no basis to infer it." This contradicts line 5 (the figure gave it away) and the SQL claims. The figures file only says the reading was "not inferred from the stated basis".
- **Line 16:** "the same words gave 2,453 late orders in the chain and 1,762 in a fresh chat". The chain question was "And how many of those were delivered late?", not the Q6 wording. Line 51's "from the same phrase" has the same problem.
- **Line 71:** "That is the real risk in follow-up questions, more than forgetting." The unstated-basis case (Q6) was a fresh chat, not a follow-up. The claim also generalises from one run.
- **Line 39:** "Memory held exactly." This rests on one recall, and that recall re-ran Q1's query.
- **Line 26:** "Before the first question, we wrote the expected answers ... Then we checked each of Dot's answers against them." Q6 and Q8 were matched to rival scopes with `--decide` after the run. Q7 was compared under T7d because of the definition its answer stated.
- **Line 61:** "A fresh-chat control that misses can be an interpretation change, not a memory failure." This is a general rule drawn from one control in one run.
- **Line 14 vs the table:** "Scope held" is presented as something Dot did. Yet the table says Q8's reading was "decided by a person".

**4. Quotes**

- **Line 5, "1,762 orders delivered in 2017 arrived after their estimated delivery date":** it appears under Q6 in the run file. But it is introduced with "Dot answered:" and cut before the second sentence, "Deliveries on the estimated date are not counted as late.", with no ellipsis.
- **Line 7, "This uses the customer delivery date, not the purchase date.":** word for word under Q7. Presented as something Dot "added", consistent with the source.
- **Line 41, "excluding the two orders with missing delivery dates":** word for word under Q3. The draft doesn't say which question it answered; line 79 attributes it loosely to "the 2017 and 2018 shares". Q4's wording is different ("excluding six orders...") and isn't quoted.
- **Line 45, "This uses purchase date, not delivery date.":** word for word under Q1. Correctly tied to the first answer.
- **Line 69, "delivered in 2017":** it appears under Q6.
- **Presentation is inconsistent:** Q6 is a cut fragment presented as the full answer; Q7 is a full sentence labelled "added"; the Q3 fragment has no question named.

I added seven lines to `C:\Users\LENOVO\OneDrive\Documents\1Sauarbh\1Dot\dot-content-machine\dot-content-machine\.claude\agent-memory\fact-checker\MEMORY.md`, one for each new kind of problem.
