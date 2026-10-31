# fact-checker · test-ai-analyst-before-rollout

Started with: Fact-check reviews/test-ai-analyst-before-rollout/draft.md against figures/test-ai-analyst-before-rollout-figures.csv and runs/test-ai-analyst-before-rollout-run.md.

**The run file runs/test-ai-analyst-before-rollout-run.md does not exist.**

Files checked:
- C:\Users\LENOVO\OneDrive\Documents\1Sauarbh\1Dot\dot-content-machine\dot-content-machine\reviews\test-ai-analyst-before-rollout\draft.md
- C:\Users\LENOVO\OneDrive\Documents\1Sauarbh\1Dot\dot-content-machine\dot-content-machine\figures\test-ai-analyst-before-rollout-figures.csv
- runs/test-ai-analyst-before-rollout-run.md: missing

1. **Numbers**
   1. "8 Steps" / "eight steps" / "eight lines" (title, lede, line 9, H2): matches the 8 listed. There is no figures ID, which is fine for a structural count.
   2. "2,878 and 2,453" (lede, step 3): match RP2-MR-Q5 and RP2-MR-Q11. Lede and line 5 say "both correct" and "Both numbers were right". RP2-MR-Q5 marks 2,878 only "correct under stated definition", and says that definition differs "from the one asked (T11)". Under the definition asked, 2,878 does not match.
   3. "31 October 2026" (lines 5 and 22): matches the run dates in the RA-* and RP2-* descriptions. Line 5's date for the "delivered late in 2017" pair has no ID of its own.
   4. "425 orders apart": 2,878 − 2,453 = 425. Correct. Matches RP2-F08.
   5. "13 companies" (several places): C-1.
   6. "8 build their test set from real questions or ground-truth answers" / "8 of 13": the count matches C-4. C-4 says "real questions or expert/ground-truth queries", and it leaves out Hex, which has "ground truths on a synthetic company". Under the draft's wording ("or ground-truth answers"), Hex would qualify.
   7. "133 questions across 10 product areas, written with domain experts": 133 is LIN-10 and 10 is LIN-2/LIN-10. Domain experts appear only in the blog quote (LIN-1, "over 130"). The draft cites the arXiv paper, whose quote (LIN-10) doesn't mention domain experts.
   8. "5 answers were correct as asked and 3 only under that second reading" (step 2, line 37): 5 matches RA-SPLIT, and 3 = 8 − 5. RA-F05 in the same figures file splits it as "7 correct, 1 correct under stated definition", and RA-MR-Q6 and RA-MR-Q8 are marked plain "correct". The figures file contradicts itself.
   9. "5 of 6 questions returned the same value in both chats": RP2-F07. 6 = RP2-F01. "Two chats per question": RP2-F03.
   10. "all 8 answers came back with their SQL": RA-F16.
   11. "Only 5 of 8 answer texts named the date" (step 4, line 41): RA-F15. That leaves Q2, Q6 and Q8.
   12. "For two of the other three, a person read the date from the SQL": no figures ID. RA-MR-Q6 and Q8 say "decided by a person (--decide)" and don't mention SQL. The third answer (Q2) is never explained.
   13. "across 4 turns": RA-F04.
   14. "returned 43,428 again": RA-MR-Q5. RA-MR-Q5 says "same SQL", so the query was re-run, not the figure remembered.
   15. "691 orders below" (step 5, line 35): 2,453 − 1,762 = 691. Correct. Matches RA-F12, RA-MR-Q2 and RA-MR-Q6.
   16. "5.6% and 7.7%": match RA-MR-Q3 (5.64843) and RA-MR-Q4 (7.725972). Both round correctly to one decimal.
   17. "2.04%" / "2.03%" / "35% of the time": HEX-1, HEX-2, HEX-3.
   18. "within 1 point ... 75% of the time": LIN-6, LIN-7.
   19. "~90%" (step 7, line 49): ANT-13.
   20. "1 of 13 to publish a number to clear": C-8.
   21. "~95% ... ~65% over a month" (step 8, line 45): ANT-5 and ANT-6. The draft's quote continues "before we treated this as an engineering problem". The verbatim quote recorded in ANT-5/ANT-6 ends at "over a month." The extra words have no figures record.
   22. "5 re-run on a change, before each deploy, or daily" (step 8, line 47): C-6.
   23. "about 60%": LIN-3. "10-15%": LIN-4, and the quote matches.
   24. "~5% run-to-run": UBR-1, and the quote is a substring of the recorded quote.
   25. "Two runs": consistent with the RA-* and RP2-* runs. No ID.
   26. "27 October 2026" (Dot details panel): no figures ID. It is also a different date from both runs.
   27. "Dot's census lists how all 13 companies score": there is no figures ID for "all 13 score". C-5 covers only the 7 companies that use LLM judges.

2. **Product claims**
   1. Dot returned 2,878 and 2,453 in two fresh chats, each with its own definition of "late": VERIFIABLE (definition quotes shown, but unchecked; see item 4).
   2. "worded identically": ASSERTED. The draft doesn't show the second chat's question.
   3. "5 of 6 questions returned the same value in both chats": ASSERTED. No values are shown.
   4. "all 8 answers came back with their SQL" / "Dot returned its SQL with every answer in both our runs, and the SQL named the date column": ASSERTED. No SQL is shown.
   5. "Only 5 of 8 answer texts named the date": ASSERTED. No answer texts are shown.
   6. "Dot kept the chain's purchase-date reading across 4 turns": ASSERTED.
   7. "returned 43,428 again when asked for the first figure": ASSERTED.
   8. The fresh chat "read the phrase by delivery date": ASSERTED. Q6's text didn't name its date (RA-F15), and RA-MR-Q6 says a person decided the definition.
   9. 5.6% and 7.7% "came back": ASSERTED.
   10. Dot evaluation "holds an expected answer, a unit and a tolerance in percent": ASSERTED (docs link only).
   11. The details panel "showed a verdict such as 'Exact match'" on 27 October 2026: ASSERTED. No screenshot and no figures ID.
   12. "The evaluation re-scored on save, without a re-run": ASSERTED.
   13. "Dot answers data questions for your team": ASSERTED.
   14. "Dot's essay on accuracy decay starts from that figure": ASSERTED.
   15. Hex's judge "accepted the wrong one 35% of the time": VERIFIABLE (cited; HEX-3).
   16. LinkedIn's judge within 1 point 75% of the time: VERIFIABLE (cited; LIN-7).
   17. Anthropic's drift from ~95% to ~65%: VERIFIABLE up to "over a month". The rest of the quote is not in the figures record.

3. **Conclusions that go further than the evidence**
   1. Line 45, "A test passed at launch says little about the same agent a month later": this generalises from one company. It also drops the "without skill maintenance" condition in ANT-5/ANT-6, and ANT-2 reports "consistently above 95%" with skills.
   2. Line 7 and the lede, "Both numbers were right": the figures file marks 2,878 correct only under a definition other than the one asked.
   3. Step 2, "we computed every expected answer from the raw data first": nothing shows when this was done. RP2-MR-Q5 was matched to T5b because of the answer's stated definition. RA-MR-Q6 and Q8 were matched by --decide.
   4. Step 2 and line 37 say Q6 was correct "only under that second reading". Line 35 says both readings "were correct for their own date", and Q6 was asked as "delivered in 2017", which allows the delivery-date reading as asked.
   5. Step 6, "Mark the answers by hand first": the draft's own runs were marked by script (RA-F05 "mark_run"; RA-SPLIT "counted by script"), with a person deciding only Q6 and Q8.
   6. Line 41, "Reading the SQL is how a person told the two readings apart": the figures file records --decide, not reading the SQL. Step 4 also says this applied to only two of the three answers.
   7. Step 5 and line 35: they say the chain and the fresh chat each "read the phrase" differently. No chain question text is shown, so there's no evidence the chain was given the phrase "delivered in 2017". The draft also puts the difference down to fresh chat versus chain without ruling out other conditions, and with no run file that can't be checked.
   8. Line 53, "They show the steps catch something": the runs bear only on steps 2–6. Steps 1, 7 and 8 rest on publications alone, as step 8 itself says.
   9. Line 55, "the census ranges too widely to suggest one" (the bar): only 1 of 13 published a bar (C-8), so there is no range. No figures ID is given for a range in the number of questions either.
   10. Lede, "each resting on a run of ours or a published method": line 22 offers a third category, "nothing yet tested", and step 7 says the right bar "is untested".
   11. Step 6, "Dot's census lists how all 13 companies score": the only scoring figure (C-5) covers 7.
   12. Line 47, "Re-runs also vary on their own": Uber's quote states a decision rule, not a measured variance.

4. **Quotes presented as product output**
   1. "meaning delivery occurred after the estimated delivery timestamp" (line 5, Dot, under "How many orders were delivered late in 2017?"): not checked: no run file. A normalised version of this text appears in RP2-MR-Q5, but that isn't the run file.
   2. "meaning they arrived after the estimated delivery day" (line 5, Dot, same question): not checked: no run file. The figures file has no record of this text at all.
   3. "Exact match" (line 59, Dot details panel, 27 October 2026): not checked: no run file.
   4. Consistency: quotes 1 and 2 are both clause fragments introduced the same way ("counted late as"), with no chat or question number. Quote 3 is introduced with "such as", so it is presented as an example and not as a recorded output.

I added 11 new lines to MEMORY.md, one for each kind of mistake not already recorded there.
