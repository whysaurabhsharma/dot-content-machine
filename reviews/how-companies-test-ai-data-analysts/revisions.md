# Revisions · how-companies-test-ai-data-analysts

Revised 31 October 2026 after the blind reviews. No revise-notes.md existed for this round. Title and title_approved_by untouched. check_piece.py after revision: 19 pass, 0 fail, 6 for a human.

## Inputs

- **Run file missing.** runs/how-companies-test-ai-data-analysts-run.md does not exist: the piece is a teardown with no Dot run (front matter, outline). Every number is from the figures file; company quotes match the figures file or research section 7 word for word; the Dot lines rest on facts/dot-facts.md O1, O2 and A7 only.
- **H2 3 wording ("Accuracy drifts, so the careful companies re-run their tests on every change") and the named five** were set by Saurabh at Decision 2 and are kept as written.

## Reader: three stopping points

1. **"13 companies, 5 show how" four times; the counting rule vague.** H2 1 now opens on its own finding (8 of 13) instead of the 13/5 line, and the rule is concrete: a company counted when its own publication named a method, gave an accuracy figure for its own system, or described a test set. Pocket-guide line 1 shortened.
2. **Dot as an ad mid-evidence, with a lab-notebook "we observed on 27 October".** All three Dot paragraphs left the evidence sections (H2 1, H2 2, H2 3); Dot now appears only in "Where Dot fits". The dates, "as we observed" and "seen twice" are gone; the re-score line keeps its Assumption label (A7).
3. **The two fives conflated; Uber and LinkedIn's "Strict" rows inconsistent.** H2 3 adds three sentences saying the re-running companies are a different group from the strict methods (GitHub and Salesforce don't say how they score; LinkedIn and ClickHouse don't re-run on every change), without putting a count beside it. Uber's table row now shows QueryGPT's own timing (staging and production, tracked over time) as well as Finch's; the body no longer says QueryGPT has "no trigger". LinkedIn's "Runs when" now reads "Ongoing; experts review the benchmark every 3 months". The table intro says Uber's row draws on two publications.

Also from the reader: the 84.9% claim is now ClickHouse's own sentence quoted whole, with how its column-linked scorer works; "three of the 13" now names all three (Uber added); the lede's promise is now "all 13 methods in one table, with the 5 copyable ones marked", which the piece delivers.

## Fact-checker

1. **"Real questions with known answers" label drifting; WisdomAI uses a public benchmark.** One label throughout, matching C-4: "real questions or ground-truth answers" (lede, pocket guide, H2 1). "Most of the thirteen build the test from their own work" cut. WisdomAI's row adds its validated ground truth.
2. **Uber's strict status assembled from two systems.** Table row now shows QueryGPT's own timing (C-2 counts Uber on QueryGPT, research section 7); Finch kept as the re-run trigger (C-6).
3. **LinkedIn's "when" is a review cadence.** Row reworded (see reader 3).
4. **"On every change" too wide for Salesforce.** Pocket guide and H2 3 body now say "on a change, before each deploy, or daily". The H2 keeps "on every change": Saurabh's wording.
5. **~90% launch bar stated as current.** Pocket guide now says Anthropic "initially used about 90%"; the body already quoted "initially used ~90%".
6. **"Three of the 13" names two.** Uber added: it notes a question can have more than one correct SQL query (C-7, research section 7).
7. **"Models from different providers" unsupported (H2 1).** Now "a panel of models", and "where no two of them agreed" for the 39 dropped questions (CLK-4).
8. **27 October 2026 and "seen twice" without a figures row or run file.** Both cut.
9. **"Scale of 1 to 5" without a figures row.** Cut: "scoring against a rubric".
10. **Publication dates in the table without figures IDs.** Stand: they are publication metadata from research section 7, not findings; check 15 passes.
11. **"Three different accuracy measures" for LinkedIn.** Now names the three kinds (user survey, benchmark ablation, expert review) with no count.
12. **"The five methods side by side" not delivered.** Lede promise changed (see reader).
13. **Dot product claims ASSERTED.** Dot's own sentence (facts/dot-entity.md) opens "Where Dot fits"; the expected answer, unit, tolerance and "Exact match" verdict are O1; the re-score on save is O2 in the past tense; "always" carries the Assumption label (A7). "Show how" and "the kind of test set this piece describes" cut.
14. **Anthropic drift cause asserted.** "The data model moving while the agent's skills stood still" cut in both places; the piece now gives only the post's own heading for the drop.
15. **"Anthropic's fix was procedural".** Cut; the 90% PR figure is now reported as "the same post says", with no causal link.
16. **"Testing once is not enough, and Anthropic has the numbers".** Cut; the opening goes straight to the quoted drift.
17. **Table broader than the body for Anthropic and GitHub.** Anthropic: "When a PR touches a dependency, in CI". GitHub: "On every context or configuration change, before release".
18. **"The published judges are imperfect" rests on 2 of 7.** H2 2 now says "two publish where the judge falls short", and the body names LinkedIn and Hex; Snowflake, WisdomAI and Grab now named as the other judges.
19. **"Leaning harsh and keeping people in the loop" leaned on Anthropic, not counted as a judge.** Now "Hex and LinkedIn respond to their judges' misses in different ways"; Anthropic's query grading is a separate sentence about its grader.
20. **ClickHouse exact-match inference.** Cut; replaced by ClickHouse's own sentence on the 84.9% (CLK-13, verbatim) and its words "proved vital".
21. **"Careful" in the H2 3 heading.** Stands: Saurabh's chosen wording at Decision 2.
22. **"Each row is one company's own publication".** Now "draws on one company's own publications", with Uber's two named.
23. **"None is audited, and no two are comparable".** Now "none says the result was audited" and "the figures can't be compared", each company using its own test set.
24. **Dot's test set "has the same shape" though it holds one expected answer.** Claim cut.
25. **"Exact match" quotes not checked against a run file.** Stands, once: the verdict is quoted from facts/dot-facts.md O1 (Observed); the second use was cut. No run file exists for a teardown.
26. **"Treat skill maintenance as a first class citizen" and "We are biased towards being overly harsh" have no figures row.** Stand: neither contains a number; both are verbatim in research section 7 (Anthropic and Hex entries).
27. **Link-only company claims (LinkedIn judge, Uber, ClickHouse jury, Hex, GitHub, Salesforce, table cells, unloaded posts, customer tools).** Stand: each is a cited publication, linked and read 31 October 2026 (research section 7 and the verification file).

## Lift-tester (not required, applied where it overlapped)

- The ~90% line now says "initially". The "re-run" line no longer says "on every change" and is followed in H2 3 by the sentence separating it from the strict methods. "Exact matching would miss things too" and "The companies answer this by…" replaced with self-contained sentences. "So a re-run needs…" now starts "A re-run therefore needs…".

## Knock-on

- pieces/how-companies-test-ai-data-analysts-faq.json: two answers updated so they stay word for word with the changed sentences.
