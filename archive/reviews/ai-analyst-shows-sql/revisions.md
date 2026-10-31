# revisions · ai-analyst-shows-sql

## Round 1: after the blind reviews

31 October 2026. No revise-notes.md this round. The closing instruction was not changed: it already ends at "then the date filter in its SQL." (outline Decision 2). Front matter and title not touched. check_piece.py afterwards: 17 pass, 0 fail, 1 partial (check 1, claim title), 1,153 words.

### Reader: three stopping points

- **"Prove stage" opening (line 22).** Fixed. The section now opens on the plain question "Does it matter whether an AI analyst shows its SQL?", then says what the Prove stage is in plain words; "The useful question is when that SQL earns its place" is cut. The vendor-page claim about buyers is gone.
- **"Each question recurred item by item" (line 71).** Fixed. Now: "Each question got the same reading in both its chats. The reading changed between questions: the count used purchase year, and the revenue total used delivery year."
- **Caveats (lines 94-95).** Fixed. The settings caveat now reads "This piece reports which reading each answer stated, not why it took it", so it no longer takes back the thesis. The 7.7% caveat now says plainly that it matched at one decimal place, with the denominator difference stated as a definition difference, and the pocket guide's line 3 says "at the precision shown".
- **Claim not believed ("11 of 12").** Fixed. The late-delivery answers are now quoted as full sentences, which show "orders placed in 2017". The matching rule is stated in the piece, not deferred to the figures file, and the spend and 2018 answers' date phrases are quoted.

### Fact-checker

- **7.7% reference uses a different denominator.** Fixed in the caveat: both answers dropped six orders, the reference kept them, both round to 7.7%. No new figure added.
- **"six orders with no delivery date".** Fixed: "six orders missing a delivery or estimated date", matching the SQL.
- **"Both queries kept the same orders" asserted.** Fixed: chat B's full WHERE clause is shown, word for word, and the piece says chat A's has the same three conditions.
- **"425 come from that one comparison" asserted.** Fixed by the WHERE clause above.
- **"Every answer checked out ... under the definition it stated".** Fixed: now "Every answer matched a figure computed from the raw CSVs, at the precision shown"; the stated-definition wording is kept only for the two late counts, which matched exactly (MR-Q5, MR-Q11).
- **"All 12 came back with their SQL ... named date column" asserted.** Stands, reworded: the method paragraph says a script made these counts (F05, F06); showing 12 SQL blocks would break the word limit.
- **Yes marks for Q3, Q6, Q9, Q12 without text.** Fixed: "on orders placed in 2017" and "placed in 2018" quoted from those answers.
- **Q1/Q2 "SQL filtered on the matching column" asserted.** Stands: the column names are given in the text for each question; the run file holds the SQL.
- **"Dot left the six orders out of the denominator" asserted.** Stands, reworded in the caveat; the run file's Q6 and Q12 answers say so ("Six orders with missing delivery dates were excluded").
- **"Dot's documentation is at docs.getdot.ai" asserted.** Stands: it is a link, checked by verify_sources.py.
- **"Buyers comparing ... ask whether an AI analyst shows its SQL" asserted.** Fixed: cut; the section now asks the question itself.
- **"each with two honest readings" and "Before the run, we computed every rival reading".** Fixed: "each worded so that a date or a definition is left open"; "before the run" and "every rival reading" cut.
- **"A script marked each answer against the reading it stated".** Fixed: "A script computed reference figures from the raw CSVs and compared each answer with them."
- **"Each answer named its clock in plain words".** Fixed: limited to the late pair ("timestamp" vs "day"), and the piece now says the 2018 answers said "estimated delivery date" while comparing calendar days.
- **"Recurred item by item".** Fixed (see reader point 2).
- **Readings credited to Dot's choice.** Fixed: "Dot used" / "chose different grains" / "Dot didn't resolve" are now "the answer used", "the reading changed between questions"; the caveat says the piece reports which reading each answer stated, not why. The context note is not named, because the run file bars any claim about context notes under the rule 14 waiver.
- **7.7% "display rounding, not a disagreement".** Fixed: now "matched at one decimal place", with the denominator difference stated.
- **"Showing the SQL matters most in two places" unmeasured ranking.** Fixed: "In this run, showing the SQL mattered in two places"; pocket line 7 likewise scoped to "In this run".
- **Lede generalises ("you can get").** Fixed: the lede now says "We asked Dot ... on the Olist dataset".
- **Late quotes are fragments called "the two sentences".** Fixed: both quoted as full sentences; "the two sentences" line cut.
- **Q4 quote drops " .".** Stands: the space-period is a capture artefact; the words are verbatim.
- **Chat A SQL omits NOT NULL guards.** Fixed: all three conditions shown.
- **Chat B SQL sits inside COUNT(*) FILTER.** Fixed: shown with its FILTER wrapper, and the text says "inside its count".
- **Q4 SQL upper bound cut.** Fixed: both bounds shown.
- **BRL 5,962,902 not in Figures (check 15).** Fixed: now BRL 5,962,902.01, F09's value.

### Lift tester (not required; noted)

- "Both were correct, by different clocks", "The useful question ...", "recurred item by item", "Put the two sentences side by side ..." and the self-contradicting caveat are cut. The preferred line is kept with its subject and scoped to the run.
