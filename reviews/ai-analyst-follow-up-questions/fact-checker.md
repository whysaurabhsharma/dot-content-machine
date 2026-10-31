# fact-checker · ai-analyst-follow-up-questions

Started with: Fact-check reviews/ai-analyst-follow-up-questions/draft.md against figures/ai-analyst-follow-up-questions-figures.csv and runs/ai-analyst-follow-up-questions-run.md.

**1. Numbers**

1. All the arithmetic checks out. 2,453 − 1,762 = 691 (F12). 1,762 / 40,930 = 4.30% (F09). 2,453 / 43,428 rounds to 5.6% (MR-Q3), and 4,078 / 52,783 rounds to 7.7% (MR-Q4). 5 + 1 + 2 = 8 questions (F01, F03). The chats come to 3 (F02), and Q5 minus Q1 is 4 turns (F04). There are 8 summary lines and 5 test steps. Every other number has a matching ID: 43,428 (MR-Q1, MR-Q5), 2,453 (MR-Q2), 1,762 (MR-Q6), 40,930 (F08), BRL 5,612,818 (MR-Q7), BRL 5,962,902.01 (F06), BRL 651,458 (MR-Q8), BRL 987,765.37 (F07), two orders (F10), six orders (F11). The problems are below.
2. Line 41 says 5.6% and 7.7% "are the raw-data shares rounded to one decimal". The expected values (MR-Q3 5.64843, MR-Q4 7.725972) are 2,453/43,428 and 4,078/52,783, so they include the 2 and 6 orders with no delivery date. Dot's quoted answers exclude those orders, so Dot's shares are 2,453/43,426 and 4,078/52,777. Both still round to 5.6% and 7.7%, but the draft calls them the same share when they are not.
3. Line 55 compares BRL 5,612,818 (whole BRL) with BRL 5,962,902.01 (to the cent). The precision is mixed within one comparison.
4. Line 55 compares the 4.3% late share with the chain's 5.6%. The 4.3% has no exclusion in its denominator, but the 5.6% leaves out 2 orders. The draft doesn't say this.
5. The table column is headed "Date in the SQL's year filter", but Q8's SQL filters on a month (November 2017).
6. The 5 in "five-step test" has no figures ID. It is structural, so this is a note, not an error.
7. The caption date "31 October 2026" has no figures ID. The run file does support it.
8. In the figures file, MR-Q5's description says "T1 recalled after four turns". That conflicts with the draft (line 39) and the run file, which both say Q5 re-ran Q1's query.

**2. Product claims**

9. Q5 resolved "my first question" correctly and re-ran Q1's query: VERIFIABLE (the SQL is identical; the draft describes it but does not show the SQL).
10. Q8 kept the delivery-date filter: VERIFIABLE (described from the SQL).
11. Chain filters used `order_purchase_timestamp` and fresh-chat filters used `order_delivered_customer_date`: VERIFIABLE.
12. "Each answer in this run came back with its SQL": VERIFIABLE from the run file, but the draft shows no SQL.
13. Line 92, "Dot's context notes are where a team can define what 'delivered in' means": ASSERTED.
14. Line 92, "Dot's evaluation questions hold an expected answer and a percent tolerance": ASSERTED. The only support is a link to the docs.
15. Line 20, the Prove stage is "where a team tests the analyst on known questions before launch": ASSERTED.
16. Line 24, the expected answers for both readings were computed "Before the first question": ASSERTED. Nothing in the figures file shows when they were computed, and Q6 and Q8 were matched with `--decide` after the run.

**3. Conclusions that go further than the evidence**

17. Line 61, "Dot's fresh-chat control missed because of reading, not memory." "Missed" contradicts line 53 ("Neither answer is wrong") and the table's "Correct" for Q6.
18. Lines 5, 47 and 61 blame the different reading on whether the chat had history. That rests on one run, so a re-run could also explain the gap. The run file also shows two context notes switched on. The waiver bars the piece from mentioning them, so that possible cause can be neither ruled out nor disclosed.
19. Line 71, "that was a bigger risk in follow-up questions than forgetting." The 691-order gap came from Q6, which was a fresh chat, not a follow-up. "Bigger risk" is a comparative drawn from one run in which memory never failed.
20. Line 24 says a person chose the reading "Where an answer didn't state its reading". Line 69 says the SQL's delivery-date filter shows the reading. If the SQL settles it (line 63), the draft doesn't explain why a person had to choose.
21. Line 61, "Judge a control item by item, or you will blame the wrong thing." This turns one run into a general rule.
22. Line 20, "real questions rarely arrive alone." No evidence is given.
23. Line 69, "That repeats the question's own words." Only "delivered in 2017" repeats the question; "arrived after" does not.

**4. Quotes**

24. "This uses purchase date, not delivery date." (lines 45 and 67, attributed to Q1): word for word under Q1.
25. "excluding the two orders with missing delivery dates" (Q3) and "excluding six orders with missing delivery dates" (Q4): word for word under their questions.
26. "This uses the customer delivery date, not the purchase date." (Q7): word for word under Q7.
27. "1,762 orders delivered in 2017 arrived after their estimated delivery date" (Q6): word for word as the opening of the Q6 answer, and "began" correctly marks it as partial.
28. The chart caption is not a Dot quote, but its wording ("Mode not published: it was noted by hand, not screenshotted") differs from the caption the run file records as chosen ("Mode not recorded for publication (rule 14 waived)").

I added six new lines to `C:\Users\LENOVO\OneDrive\Documents\1Sauarbh\1Dot\dot-content-machine\dot-content-machine\.claude\agent-memory\fact-checker\MEMORY.md`.
