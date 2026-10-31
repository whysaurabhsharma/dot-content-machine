# fact-checker · ai-analyst-shows-sql

Started with: Fact-check reviews/ai-analyst-shows-sql/draft.md against figures/ai-analyst-shows-sql-figures.csv and runs/ai-analyst-shows-sql-run.md.

1. **Numbers**
   - 2,878 (A) and 2,453 (B): consistent everywhere they appear. They match MR-Q5 and MR-Q11.
   - 425: 2,878 − 2,453 = 425, which is correct. It matches F08.
   - 43,428: matches MR-Q1 and MR-Q7.
   - BRL 5,612,818: matches MR-Q2 and MR-Q8, where the figures file has 5,612,817.85, rounded.
   - BRL 6,921,535: matches MR-Q3 and MR-Q9.
   - 45,101: matches MR-Q4 and MR-Q10.
   - 7.7%: matches MR-Q6 and MR-Q12.
     - The "figure computed from the raw CSVs" is 7.725972 in the MR-Q6 description. 4,078 / 52,783 = 7.726%, so that checks out.
     - Problem: that reference keeps the 6 missing-date orders in the denominator. Dot's two answers drop them (4,078 / 52,777 = 7.727%). So the figures file has no reference value under the definition Dot stated.
   - "six questions": matches F01. "two fresh chats": matches F03. "12 answers": matches F02. 6 × 2 = 12, which is correct.
   - "11 of 12": matches F04.
   - "12 of 12" / "All 12 came back with their SQL": matches F05.
   - "all 12 filtered the period on a named date column": matches F06.
   - "Five of the six questions returned the same value": matches F07, and the table agrees.
   - 40,930: matches F10.
   - BRL 5,962,902: matches F09 (5,962,902.01, rounded). Whole-BRL rounding is used consistently with 5,612,818.
   - "six orders with no delivery date": matches F12.
     - Problem: Dot's SQL counts orders missing *either* the delivered date or the estimated date, not just the delivery date.
   - "eight lines": the list has 8 items. This is structural, so it has no ID.
   - "31 October 2026": matches the run file's date. It has no figures-file ID.
   - "One question split": consistent with F07.

2. **Product claims**
   - Dot used the purchase date for the count and the delivery date for the revenue total, for both chats: VERIFIABLE. The SQL and quotes are shown.
   - Chat A compared timestamps and chat B compared calendar days: VERIFIABLE. The snippets are shown.
   - "Both queries kept the same orders: delivered, and purchased in 2017": ASSERTED. The draft doesn't show the WHERE clauses of either query, only the comparison lines.
   - "The 425 orders between the answers come from that one comparison": ASSERTED. It depends on the WHERE clauses that aren't shown.
   - "Every answer checked out against figures computed from the raw CSVs": ASSERTED. Only 2,878 and 2,453 are said to "match the raw data exactly", and no reference values are shown for Q1–Q4 or Q6.
   - "All 12 came back with their SQL, and all 12 filtered the period on a named date column": ASSERTED. The draft shows only three SQL fragments, from Q5, Q11 and Q4.
   - "The text named its date basis in 11 of 12 answers": partly VERIFIABLE. Only 7 answers are quoted (Q1, Q2, Q4, Q5, Q7, Q8, Q10, Q11). The table's Yes marks for Q3, Q6, Q9 and Q12 have no text shown.
   - "Each answer's ... SQL filtered on the matching column" for the four "delivered in 2017" answers: ASSERTED. Only column names are given in prose, with no snippet.
   - "Chat B, the fresh repeat, returned 45,101 again": VERIFIABLE through the quote.
   - "Dot left the six orders with no delivery date out of the denominator": ASSERTED. No answer text or SQL for Q6 or Q12 is shown.
   - "Dot's documentation is at docs.getdot.ai": ASSERTED.
   - "Buyers comparing conversational analytics tools ask whether an AI analyst shows its SQL": ASSERTED.

3. **Conclusions that go further than the evidence**
   - Line 13, "Every answer checked out ... under the definition it stated": Q4 chat A stated no date basis, as the draft itself says at line 81. Q6 and Q12 were checked against a reference whose denominator differs from the one the answers stated.
   - Line 24, "six questions ... each with two honest readings" and "Before the run, we computed every rival reading":
     - The figures file holds rival-reading values only for the Q1, Q2 and Q5 wordings (F10, F09, MR-Q5/T5b). None exist for Q3, Q4 or Q6.
     - Nothing in the figures file shows anything was computed before the run. Every row is dated 2026-10-31 with no time.
   - Line 26, "A script marked each answer against the reading it stated": the MR rows say "matched by question text". Q4 chat A stated no reading.
   - Line 57, "Each answer named its clock in plain words": the 2018 answers also used calendar-day SQL, but their text says "estimated delivery date", not "day". So the wording is not a reliable signal of grain. Only the Q5/Q11 pair supports this sentence.
   - Line 71, "Each question recurred item by item across its two chats": only totals and order counts are compared. Nothing item by item is shown.
   - Lines 5, 57 and 71 credit the reading choices to Dot ("Dot used", "chose different grains", "Dot didn't resolve the phrase the same way").
     - The run file records a context note that was on during the run. It says: "Unless explicitly requested otherwise, report a purchase cohort using order_purchase_timestamp".
     - Line 94 says the piece "says nothing about which settings or definitions shaped each reading", but the body attributes the readings to Dot anyway.
   - Line 95, "The 2018 late share was display rounding, not a disagreement": the same bullet says Dot and the reference used different denominators. So the gap is a definition difference as well as rounding.
   - Line 89, "Showing the SQL matters most in two places": this ranking was not measured. Line 96 says reading the SQL was not measured.
   - Line 3, "Ask an AI data analyst ... and you can get 2,878 and 2,453": this generalises from one product and one batch. The caveat at line 93 limits it, but the lede doesn't.

4. **Quotes**
   - Line 5, "This uses purchase date, not delivery date.": found word for word under Q1, "How many orders were delivered in 2017?" Line 65 repeats it consistently.
   - Line 7, "This uses delivery date, not purchase date.": found word for word under Q2. Line 67 repeats it consistently.
   - Line 65, "This uses purchase dates, not delivery dates.": found word for word under Q7.
   - Line 67, "This uses the actual delivery date, not the purchase date.": found word for word under Q8.
   - Line 37, "meaning delivery occurred after the estimated delivery timestamp": found word for word under Q5. It is a mid-sentence fragment, not a full sentence.
   - Line 37, "meaning they arrived after the estimated delivery day": found word for word under Q11. It is also a fragment.
     - Line 57 calls these two quotes "the two sentences".
   - Line 81, "We received 45,101 orders in 2017, including all order statuses": found word for word under Q4. The run file has " ." before the end, which is dropped.
   - Line 87, "based on purchase date": found word for word under Q10.
   - SQL at line 46: found word for word under Q5. It is one of three ANDed conditions, and the NOT NULL guards are omitted.
   - SQL at line 52: found word for word under Q11. Problem: this `WHERE` sits inside a `COUNT(*) FILTER (...)`, not in the query's WHERE clause, and the draft doesn't say so.
   - SQL at line 84: found word for word under Q4. Problem: the upper bound `AND order_purchase_timestamp < '2018-01-01'` is cut, with no ellipsis.

I added five new lines for the ai-analyst-shows-sql piece to `C:\Users\LENOVO\OneDrive\Documents\1Sauarbh\1Dot\dot-content-machine\dot-content-machine\.claude\agent-memory\fact-checker\MEMORY.md`.

Files checked:
- `C:\Users\LENOVO\OneDrive\Documents\1Sauarbh\1Dot\dot-content-machine\dot-content-machine\reviews\ai-analyst-shows-sql\draft.md`
- `C:\Users\LENOVO\OneDrive\Documents\1Sauarbh\1Dot\dot-content-machine\dot-content-machine\figures\ai-analyst-shows-sql-figures.csv`
- `C:\Users\LENOVO\OneDrive\Documents\1Sauarbh\1Dot\dot-content-machine\dot-content-machine\runs\ai-analyst-shows-sql-run.md`
