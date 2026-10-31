# lift-tester · how-companies-test-ai-data-analysts

Started with: Read reviews/how-companies-test-ai-data-analysts/draft.md as an answer engine and report what you would and would not lift.

I read only `C:\Users\LENOVO\OneDrive\Documents\1Sauarbh\1Dot\dot-content-machine\dot-content-machine\reviews\how-companies-test-ai-data-analysts\draft.md`.

## Summary

- The draft looked at 13 companies' own write-ups on testing their AI analyst. Only some explained how they do it: "Only 5 published a method you could copy: what they test against, how they score, and when they run the test."
- Most build their tests from real questions, but real questions often have more than one right answer, and the LLM judges used to score answers miss things: "Hex's judge accepted a wrong 2.03% in place of the right 2.04%, 35% of the time."
- Accuracy drifts, so the careful companies re-run their tests on every change, before each deploy, or daily: "A test passed at launch says little about the same agent a month later."

## 1. Would lift (best first)

1. `[Anthropic's offline accuracy drifted](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude) "from ~95% at launch to ~65% over a month".`
   It's a direct quote from a named source with a big, concrete before-and-after number. It answers "why re-test?" by itself.
2. "Hex's judge accepted a wrong 2.03% in place of the right 2.04%, 35% of the time."
   It's specific and easy to picture, and it shows LLM judges are unreliable without needing any context.
3. "About 60% of LinkedIn's benchmark questions have more than one accepted answer."
   It has a clean subject, a number and a source, and it answers "why is building a test set hard?"
4. "Thirteen companies published how they check their [AI analyst](https://www.getdot.ai/blog/conversational-analytics-software)'s answers; only five published a method you could copy."
   This is the piece's own finding and stands alone. I'd quote it over the H1, which is a headline, not a sentence.
5. "Uber does "not over-index decisions based on ~5% run-to-run changes in most metrics"."
   It's a quoted primary source with a usable rule of thumb for noise between runs.
6. "LinkedIn's judge lands within 1 point of the human score 75% of the time."
   It's a measured agreement rate that pairs well with the Hex line.
7. "At ClickHouse, 84.9% of scored result sets matched only through column-linked mapping."
   It makes the case against plain exact-match scoring with a number, though it needs the next sentence to be clear to a general reader.
8. "Roughly 90% of its data-model PRs now include a skill change in the same diff."
   It's a concrete fix, but "its" needs Anthropic named, so I'd have to quote it with the sentence before it.
9. "A test passed at launch says little about the same agent a month later."
   It's a clean takeaway, but only usable right after the Anthropic number, because it has no evidence of its own.

## 2. Would not lift

- "Only Anthropic publishes a number an analyst must clear before launch: about 90% per domain."
  It reads as a ready-made answer but drops a caveat. The body says Anthropic "initially used ~90%" and that its target is about 100%. Quoted alone, it overstates ~90% as the current bar.
- "Anthropic, Uber, Hex, GitHub and Salesforce re-run their tests on every change, before each deploy, or daily."
  The sentence is accurate. But next to the title "5 Show How", a reader or answer engine will likely take these five to be the five strict companies. They aren't: LinkedIn and ClickHouse are strict, GitHub and Salesforce aren't. The eight-line summary still sets up that confusion.
- "Three of the 13 companies say so, or drop the questions where answers disagree."
  Only LinkedIn and ClickHouse are named, so the third is a mystery, and "say so" refers back to the previous sentence.
- "Testing once is not enough, and Anthropic has the numbers to show it."
  It's an opener that promises evidence without containing any. The next line is the one to quote.
- "The reason to re-run is drift."
  Too general, with nothing to attribute it to.
- "The published LLM judges miss things, and the companies say so."
  It's a summary claim, and the Hex and LinkedIn numbers do the job better.
- "Exact matching would miss things too."
  "Too" depends on the sentence before it, so it can't stand alone.
- "The companies answer this by leaning harsh and keeping people in the loop."
  It generalises to "the companies" from three examples, and "this" refers back.
- "So a re-run needs a line for what counts as a regression, set before the result comes in."
  This is the draft's own advice, not a sourced finding, and "So" ties it to the Uber line.
- "Start with your team's real questions and every answer you would accept, then re-run them on every change."
  Reasonable how-to advice, but it's the draft's recommendation with no source, so it's weaker than the evidence lines.
- "Dot's evaluation re-scored on save, without a re-run, when we tested it on 27 October 2026." / "Its score fell after a deliberate change and came back after reverting, seen twice."
  A vendor testing its own product, and "seen twice" is thin. The Dot section also says "Assumption: it always re-scores when a question is saved.", which weakens the claim further.

## 3. The one line

`[Anthropic's offline accuracy drifted](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude) "from ~95% at launch to ~65% over a month".`
