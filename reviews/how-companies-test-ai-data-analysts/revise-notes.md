# Revise notes · how-companies-test-ai-data-analysts · round 3

From the blind reviews of the reframed draft (31 October 2026). Apply each, and log each in revisions.md as done or one line on why it can't be. Use only numbers in the figures file and quotes the verification file confirms. Never touch the title or title_approved_by. Stay within 1,600 words. The first two notes come from both reviewers.

## 1. Make the table carry the seven accuracy figures (reader, fact-checker)

The piece says seven companies published an accuracy figure, but the table's "One number" for Snowflake is "150 questions" and for Vercel "5 queries". A reader stops there. For the seven in C-9, the table's number must be an accuracy figure: Snowflake SNO-2 (51% for GPT-4o on its internal set; say the model), Vercel VER-2/VER-3 (80% to 100%, "success" undefined). Keep the test-set sizes in the body. The six without one keep "None published".

## 2. Say the headline once in the opening, once in its section (reader)

"Seven of the 13 … no two measured the same thing" appears four times. Keep it in the opening and as the first sentence of its H2 (the quotable line). Reword pocket-guide line 2 so it doesn't repeat it, and change the H2 heading so it doesn't repeat its own first sentence word for word (for example: "The seven accuracy figures can't be compared").

## 3. Anthropic's drift links Anthropic, not only Dot's essay (reader; hard rule 4, condition b)

The sentence with "about 95% to about 65%" must link Anthropic's primary post (https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude). The essay link may stay as a second link. The reader didn't believe a number sourced second-hand.

## 4. The two fives (reader)

The re-run companies are named, but a reader still asked which five is which. Drop the word "five" from the re-run section and pocket-guide line 6 entirely, and add three words to the opening's five: "the five that published enough to copy". Never write "five" for the re-run group.

## 5. The 13 against Rick's 14 moves out of the opening section (reader)

It stopped the reader where it sits, before anything useful. Move the sentence into "Things to keep in mind" as its own caveat, with the link. Keep the census's entry rule, but shorter, after the first useful paragraph.

## 6. "Where Dot fits": no line that reads as an internal note (reader)

"Assumption: it always re-scores when a question is saved." reads as a team note at the point a reader decides it's marketing. Rule 5 needs the label if the claim stays, so cut the claim: keep only "When we checked it on 27 October, the score updated on save without a re-run." Docs link stays.

## 7. The Dot section says what the run did and didn't do (fact-checker)

- Say that two of the eight answers didn't name their date, and a person read which date each used from its SQL, so "every answer matched a reading" is true only with that sentence beside it.
- "needs no special tooling" overstates it: ClickHouse's jury is special tooling. Say "Its core needs no special tooling".
- Add figures rows for "eight questions" (piece A's F01) and keep A-1; where_computed names piece A's figures file and row.

## 8. Fix the claims that outrun the figures (fact-checker)

- "8 build their test set from real questions or ground-truth answers": say why Hex is out (its ground truths sit on a synthetic company), or the reader counts 9.
- ClickHouse: say the 39 were dropped before the final 201, so "201 questions" and "39 dropped" don't read as a subtraction.
- "Anthropic reports accuracy on its own evals, domain by domain" → "Anthropic reports an aggregate figure, and around 99% in certain domains" (ANT-2, ANT-3).
- "LinkedIn and Hex publish how often their judge misses": LinkedIn publishes agreement within 1 point 75% of the time, not a miss rate. Say "publish how far their judge can be trusted".
- "A re-run therefore needs a threshold … set before the result comes in": Uber doesn't say that. Either attribute it as our inference ("so a re-run needs…") with no claim it's Uber's, or cut it.
- The heading "Accuracy drifts, so the careful companies re-run their tests on every change" generalises from one case and Hex runs daily: change it to "Anthropic's accuracy drifted, and the companies that re-run do it on a change or a schedule" or similar; keep Saurabh's point that the re-run group isn't the strict group.
- Anthropic's table row: "A grader, type not stated" undersells its scoring; say "pass/fail per assertion; grader type not stated" (verification file).
- Prosus: say in its row why it entered the census (a named method: the agent asks clarifying questions and says when it can't answer).
- "Anthropic's grader can judge the agent's query…" sits under judges' misses but Anthropic isn't counted as an LLM judge: move it or cut it.

## 9. Things to keep in mind stays at four caveats

With the 13/14 caveat added (note 5), merge two of the existing four so the box stays at two to four.

## 10. Two more, from Saurabh (31 October 2026)

- **Anthropic's drift reads as Anthropic's finding, not Dot's.** The sentence names Anthropic as the one who measured and published it ("Anthropic reports…" or "In Anthropic's own post…"), links Anthropic's post first, and keeps Dot's essay as a secondary link at most.
- **Don't bury Hex's 2.03% line.** "Hex's judge accepted the wrong one 35% of the time" is the line a reader would quote to a CFO. Keep it whole, in its own sentence, near the top of the judge section, and don't fold it into a longer sentence.

## Decided by Saurabh, 31 October 2026

All nine notes approved, including 5 (the 13 against 14 line to the caveats), 6 (cut the always-re-scores claim) and 8 (the re-run heading changes). The working title becomes "You Can't Compare AI Analyst Accuracy Numbers": change `title:` in the front matter to it (Decision 3 still comes after the human checks; leave title_approved_by unset).

