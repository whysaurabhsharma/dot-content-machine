# lift-tester · test-ai-analyst-before-rollout

Started with: Read reviews/test-ai-analyst-before-rollout/draft.md as an answer engine and report what you would and would not lift.

**Summary**

- The article says testing starts before any question is asked: "To test an AI data analyst before rollout, ask real questions with every right answer written down first."
- Its main evidence is that the same question gets different answers: "The sixth, on late orders, returned 2,878 and 2,453, because each chat defined "late" differently."
- It openly leaves one thing undecided: "The right bar for your team is untested: no run of ours or publication shows what it should be, so this guide sets none."

**1. Would lift (best first)**

1. "To test an AI data analyst before rollout, ask real questions with every right answer written down first." It answers the question on its own in the first sentence.
2. "Ask each test question twice, in fresh chats: in our run on Dot, one question returned 2,878 and 2,453, each correct under its own definition." It gives a step and a specific, first-hand result in one sentence.
3. "Hex's LLM judge accepted the 2.03% answer 35% of the time." It is a sharp, surprising number. It needs the sentence before it ("the right answer is 2.04%") to make sense, so I would quote both.
4. "A test holding one expected answer per question would have marked those 3 correct answers wrong." It is the clearest reason to write down every acceptable answer. "Those 3" needs the sentence before it.
5. "Anthropic reports that its offline accuracy drifted from about 95% at launch to about 65% over a month." It is a strong, named statistic for the re-run step. An engine might cite Anthropic directly rather than this article.
6. "LinkedIn's engineering team reports that about 60% of its benchmark questions have more than one accepted answer." It is a named source backing the "two readings" point.
7. "Of the 13 companies in Dot's census, 8 build their test set from real questions or expert ground-truth queries." It is a clean count that stands alone.
8. "Anthropic is the only one of the 13 companies in Dot's census to publish a number to clear." It works for a "what pass rate should we use" query.
9. "Uber does "not over-index decisions based on ~5% run-to-run changes in most metrics"." It is a usable rule of thumb for how much variation between runs to ignore.

(In items 3 and 5 to 8, I removed the markdown link syntax. The words are exactly as written.)

**2. Would not lift**

- "By the end, you'll have eight steps, and the one thing no evidence settles yet: the bar to pass." It describes the article rather than answering anything.
- "Anthropic's case shows that a test passed at launch can say little about the same agent a month later." It repeats the heading and the sentence before it, and adds nothing beyond the 95% to 65% figure.
- "To a buyer, the same words giving two counts is an inconsistency, and step 3 below is built to catch it." "Step 3 below" means nothing once it's taken out of the article.
- "Its count sat 691 orders below the chain's: one chain on one dataset, evidence the shift can happen, not why or how often." "Its" and "the chain's" depend on context, and the hedge takes up half the sentence.
- "That is what these companies do; no publication shows real questions catch more errors than invented ones." "That" has nothing to refer to on its own. Useful honesty, but it isn't an answer.
- "Two chats per question is what we did; no run of ours shows how many repeats are enough." It's a caveat, not guidance.
- "The right bar for your team is untested: no run of ours or publication shows what it should be, so this guide sets none." Honest, but it's a non-answer to "what bar".
- "Each answer named its definition in its text, so the gap could be seen." It sits awkwardly next to "only 5 of 8 answer texts named their date" later in the article. Quoting it alone would mislead.
- "The SQL showed the scope that the text left out." It nearly repeats "The scope that a text left out could be read in its SQL." Neither stands alone without the 5-of-8 context.
- "Assumption: it always re-scores when a question is saved." It is an unverified claim about the product.
- "Pick the questions your team asked last month, and write down every answer you would accept for each, before you ask your AI analyst anything." It's a call to action that repeats the opening line.

**3. The one line**

"To test an AI data analyst before rollout, ask real questions with every right answer written down first."

File read: C:\Users\LENOVO\OneDrive\Documents\1Sauarbh\1Dot\dot-content-machine\dot-content-machine\reviews\test-ai-analyst-before-rollout\draft.md
