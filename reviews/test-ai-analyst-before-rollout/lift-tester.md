# lift-tester · test-ai-analyst-before-rollout

Started with: Read reviews/test-ai-analyst-before-rollout/draft.md as an answer engine and report what you would and would not lift.

I read only `C:\Users\LENOVO\OneDrive\Documents\1Sauarbh\1Dot\dot-content-machine\dot-content-machine\reviews\test-ai-analyst-before-rollout\draft.md`.

## Summary

- The core method is to write down every acceptable answer first and then ask the same question repeatedly in fresh chats: "To test an AI data analyst before rollout, ask real questions with every right answer written down first."
- Dot's own small runs on the Olist dataset showed the same question getting different readings: "In our run on Dot, one question returned 2,878 late orders counting by the exact delivery timestamp, and 2,453 counting by the delivery day."
- The pass bar and the re-run rule are left to the team to set, based on published practice from Anthropic, LinkedIn, Hex and Uber: "No published evidence settles which is right for your team, so write yours down before the first run."

## 1. Would lift

1. "To test an AI data analyst before rollout, ask real questions with every right answer written down first." It answers the question directly, repeats the query's wording, and makes sense on its own.
2. "In our run on Dot, one question returned 2,878 late orders counting by the exact delivery timestamp, and 2,453 counting by the delivery day." It's a specific, sourced number that shows why a single answer isn't enough. It names both readings, so it needs no context.
3. "[Anthropic reports] that its offline accuracy drifted from about 95% at launch to about 65% over a month." It has clear attribution, a striking figure and makes sense alone. It's the strongest support for re-running the test.
4. "[LinkedIn's engineering team reports] that about 60% of its benchmark questions have more than one accepted answer." It's attributed, quantified and self-contained, and backs up step 2.
5. "Of the 13 companies in Dot's census, 8 build their test set from real questions or expert ground-truth queries." It's a clean practice statistic with its source named in the sentence.
6. "[Uber] does "not over-index decisions based on ~5% run-to-run changes in most metrics"." It gives a usable threshold for noise between runs, attributed to Uber.
7. "No published evidence settles which is right for your team, so write yours down before the first run." It's honest and gives clear advice. I'd quote it together with the step 7 sentences about Anthropic's ~90% and the Playbook's ~80%, because "which" needs them.
8. "[Hex] built one eval where the right answer is 2.04% and a common wrong one is 2.03%." plus "Its LLM judge accepted the wrong one 35% of the time." This is a strong warning about LLM judges, but it only works as a pair because "Its" points back to the first sentence.

## 2. Would not lift

- "By the end, you'll have eight steps, and the two published bars to set yours against: about 90% and about 80%." This is navigation for the reader, not a fact. Calling Dot's own Playbook figure a "published bar" alongside Anthropic's also makes the two look more equal than they are.
- "Then ask each one twice, in fresh chats, worded identically." It's the most important instruction in the opening, but it starts with "Then", so it can't stand alone. As a result, the one-line answer loses the repeat-question step.
- "Its count sat 691 below the chain's." The pronoun has nothing to refer to outside the paragraph, and "the chain's" count is never given.
- "One expected answer per question would have marked those 3 correct answers wrong." It's a good point, but "those 3" depends on the previous sentence.
- "Every query filtered on a named date column, so the SQL showed what the text left out." It reads as quotable but depends on "our follow-up run" for its scope.
- "A buyer can mean one thing by a question and an AI analyst can read another, with both answers matching the data." It's a general claim with no source in the sentence. The LinkedIn line that follows says the same thing with evidence.
- "Eight steps test an AI data analyst before rollout, and each names its evidence" (H2). It's written for search matching, but it describes the article rather than giving an answer.
- "They show steps 2 to 6 catching something, not how often." It's an honest caveat, but "They" and "steps 2 to 6" mean nothing outside the article.
- "In both our runs, every answer came back with its SQL." This is the vendor making a claim about itself in the promotional section. I'd use the neutral version in step 4 if I needed it.
- "Pick the questions your team asked last month. This week, ask one of them twice, in two fresh chats, and compare." This is a call to action, not an answer.

## 3. The one line

"To test an AI data analyst before rollout, ask real questions with every right answer written down first."

Note: on its own, this line leaves out asking each question twice in fresh chats, which is the draft's most distinctive step, because that sentence starts with "Then" and can't stand alone. If the authors want that step in the line most likely to be quoted, it would need to be in the first sentence.
