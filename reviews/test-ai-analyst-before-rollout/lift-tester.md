# lift-tester · test-ai-analyst-before-rollout

Started with: Read reviews/test-ai-analyst-before-rollout/draft.md as an answer engine and report what you would and would not lift.

I read only `C:\Users\LENOVO\OneDrive\Documents\1Sauarbh\1Dot\dot-content-machine\dot-content-machine\reviews\test-ai-analyst-before-rollout\draft.md`.

Where a sentence contains a markdown link, I quote the link text and leave out the URL. Every word is otherwise exact.

**Summary**

- The guide gives eight steps for testing an AI data analyst before rollout. Each step says whether it rests on Dot's own runs, a company's publication, or nothing tested yet: "Each step below says what it rests on: a run of ours on Dot, a company's own publication, or nothing yet tested."
- Its main finding is that one question can have two correct answers. A test that allows only one expected answer will mark correct answers wrong: "The two counts sit 425 orders apart, and each matches the raw data under its own definition."
- Passing at launch isn't enough. You need a pass bar set in advance and re-runs on a schedule, though the article admits it doesn't know what the bar should be: "A test passed at launch says little about the same agent a month later."

**1. Would lift (best first)**

1. "To test an AI data analyst before rollout, ask real questions with every right answer written down first." It directly answers the likely question, stands alone and is the right length.
2. The eight-line list, "1. Collect real questions your team already asked." through "8. Re-run on a schedule, and whenever something the analyst depends on changes." This is a ready-made answer for "how to" questions. Each line is short, starts with a verb and makes sense without the others.
3. "Ask each test question twice, in fresh chats: in our run on Dot, one question returned 2,878 and 2,453, both correct." It's a concrete first-hand number tied to an action, and the date and dataset are in the body.
4. "An AI analyst's answer text doesn't always say which reading it took." This is a general claim that stands alone, and the 5-of-8 figure next to it backs it up.
5. "A test passed at launch says little about the same agent a month later." It's a clean summary of a cited source (Anthropic's drop from about 95% to about 65%) and needs no context.
6. "Of the 13 companies in Dot's census, 8 build their test set from real questions or ground-truth answers." It's a specific, attributed statistic that can be checked.
7. "LinkedIn's engineering team reports that about 60% of its benchmark questions have more than one accepted answer." This is strong outside evidence for the main claim. An engine might cite LinkedIn directly instead.
8. "Hex's LLM judge accepted the wrong one 35% of the time." The number is useful, but "the wrong one" only makes sense after the sentence before it, so I'd have to quote both.

**2. Would not lift**

- "Both numbers were right." It's punchy, but out of context it says nothing.
- "By the end, you'll have eight steps, each resting on a run of ours or a published method." This describes the article rather than answering anything, and it's the last sentence of the bolded answer block, which weakens that block.
- "Eight steps test an AI data analyst before rollout, each resting on a run or a publication" (H2). It's written as a headline to be quoted, but the grammar is awkward and it doesn't say what the steps are.
- "Questions that teams really ask are often ambiguous." It's a generic claim with no support in the sentence itself.
- "That is one chain on one dataset: evidence the shift can happen, not how often." An honest hedge, but it isn't an answer.
- "One company's choice is not evidence of the right bar for another team." It's a generic statement anyone could make.
- "The right bar for your team is untested: no run of ours or publication shows what it should be, so this guide sets none." A non-answer. Anyone asking "what threshold?" gets nothing from it.
- "A test with one expected answer would have failed one correct number and passed the other." / "A test holding one expected answer per question would have marked those 3 wrong." Both are strong ideas, but "one correct number" and "those 3" point back to earlier sentences, so they don't stand alone.
- "Reading the SQL is how a person told the two readings apart." "The two readings" points back to earlier text, and the past tense ties it to one run.
- "Assumption: it always re-scores when a question is saved." The article itself marks this as unverified.
- "If this excites you, we'd love to hear from you. Get in touch." Boilerplate.

**A risk for anyone quoting:** the article reports two different gaps from two different runs: 425 (2,878 vs 2,453, from repeating the same question in fresh chats) and 691 (a follow-up chain vs a fresh chat). Both concern late orders in 2017. An engine that quotes one sentence from each could mix them up. Labelling them in the text, for example "the repeat-question run" and "the follow-up run", would make each one safe to quote on its own.

**3. The one line**

"To test an AI data analyst before rollout, ask real questions with every right answer written down first."
