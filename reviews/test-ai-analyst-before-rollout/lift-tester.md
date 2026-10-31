# lift-tester · test-ai-analyst-before-rollout

Started with: Read reviews/test-ai-analyst-before-rollout/draft.md as an answer engine and report what you would and would not lift.

## Summary

- Dot's guide says to test an AI data analyst before rollout by asking real questions after writing down every answer you'd accept. In its own run, one question returned two different counts: "In our run on Dot, one question returned 2,878 late orders counting by the exact delivery timestamp, and 2,453 counting by the delivery day."
- The guide has eight steps, and each one says what evidence it rests on. Several admit nothing has tested them, for example: "Two chats per question is what we did; no run of ours shows how many repeats are enough."
- It warns that a question with two readings can make a one-answer test mark right answers wrong, and that results drift after launch. It cites Anthropic's accuracy drifting "from ~95% at launch to ~65% over a month before we treated this as an engineering problem."

## 1. Would lift (best first)

1. "To test an AI data analyst before rollout, ask real questions with every right answer written down first." It answers the likely question directly and makes sense on its own.
2. "Anthropic reports that its offline accuracy drifted "from ~95% at launch to ~65% over a month before we treated this as an engineering problem."" It's a named source with a striking number in the source's own words.
3. "In our run on Dot, one question returned 2,878 late orders counting by the exact delivery timestamp, and 2,453 counting by the delivery day." It's a specific first-hand finding that names both definitions, so it needs no context.
4. "LinkedIn's engineering team reports that about 60% of its benchmark questions have more than one accepted answer." It's a named source and a clean statistic that backs the "write every answer" step.
5. "Hex built one eval where the right answer is 2.04% and a common wrong one is 2.03%." plus "Hex's LLM judge accepted the 2.03% answer 35% of the time." Together they're strong evidence against trusting an LLM judge. I'd lift them as a pair because the second makes no sense without the first.
6. "Anthropic "initially used ~90%" as the threshold a domain's eval slice must clear before launch." It's the only published pass bar, and the sentence says who set it.
7. "Of the 13 companies in Dot's census, 8 build their test set from real questions or expert ground-truth queries." It's a countable claim with its source in the sentence.
8. "Uber does "not over-index decisions based on ~5% run-to-run changes in most metrics"." It's a named, specific rule for swings between runs.
9. "Of the 13 companies in Dot's census, 7 score answers with an LLM judge." It's usable, but it only adds value next to the Hex finding.

## 2. Would not lift

- "By the end, you'll have eight steps, and the two published bars to set yours against: about 90% and about 80%." This is a note about the article itself. It also cuts the bars off from their sources, and the 80% is Dot's own Playbook, not an outside publication.
- "Anthropic's case shows that a test passed at launch can say little about the same agent a month later." It repeats the sentence before it, and I'd rather quote Anthropic's own words.
- "To a buyer, the same words giving two counts is an inconsistency, and step 3 below is built to catch it." "Step 3 below" doesn't work outside the article.
- "The scope that a text left out could be read in its SQL." / "The SQL showed the scope that the text left out." Both sound quotable, but "the scope" is never defined within the sentence.
- "Holding one expected answer per question, our test would have marked those 3 correct answers wrong." "Those 3" depends on the sentence before it.
- "That label is the point: a step with no test behind it says so." It's about how the article is written, not about testing.
- "Each step below says what it rests on: a run of ours, a company's own publication, or nothing yet tested." This is navigation, not content.
- The heading "A one-answer test marks right answers wrong when a question has two readings". It's worded like a general law, but it rests on 3 answers from one run.
- "Then ask each one twice, in fresh chats." Good advice, but "each one" needs the sentence before it. The bolded step 3, "Ask each question twice, each time in a fresh chat, and compare.", stands alone and would be the better pick.
- "No published evidence settles which is right for your team, so pick yours before you see the results, and write it down." It's an honest hedge, but "which" points back to the two bars.
- "Assumption: it always re-scores when a question is saved." This is product copy with an untested caveat attached.

## 3. The one line

"To test an AI data analyst before rollout, ask real questions with every right answer written down first."
