# lift-tester · how-companies-test-ai-data-analysts

Started with: Read reviews/how-companies-test-ai-data-analysts/draft.md as an answer engine and report what you would and would not lift.

**Summary**

- The piece looked at 13 companies' published methods and found the accuracy figures can't be compared: "Seven of the 13 companies published an accuracy figure, and no two measured the same thing."
- Only five published a method complete enough to copy, and a real question often has more than one right answer: "About 60% of LinkedIn's benchmark questions have more than one accepted answer."
- Accuracy drifts after launch, so the careful companies re-run their tests, and the article ran the core method on Dot: "A test passed at launch says little about the same agent a month later."

**1. Would lift**

1. "Anthropic's offline accuracy fell from about 95% to about 65% in a month, the case [our essay on accuracy decay](https://www.getdot.ai/blog/your-ai-analyst-will-be-worse-next-month) starts from." The most striking number in the piece, with a named source. I would quote only the clause before the comma.
2. "Hex's judge accepted the wrong one 35% of the time." A specific, checkable figure on how often an LLM judge fails. It needs the sentence before it (2.04% vs 2.03%) to make sense.
3. "Seven of the 13 companies published an accuracy figure, and no two measured the same thing." This is the central finding. It is self-contained and carries a count.
4. "About 60% of LinkedIn's benchmark questions have more than one accepted answer." A sourced number for a point most readers won't know.
5. "Without those extra answers, LinkedIn "underreported recall by 10-15%"." It is a direct quote from the source and shows what the 60% costs.
6. "LinkedIn's judge lands within 1 point of the human score 75% of the time." A clean measure of judge reliability.
7. "Only one of the 13 companies publishes a number to clear before launch." A rare-practice finding. I'd pair it with "Anthropic "initially used ~90%", and its stated target for offline accuracy is about 100%."
8. "Uber does "not over-index decisions based on ~5% run-to-run changes in most metrics"." Useful practical guidance on noise, quoted from the source.
9. "ClickHouse writes that "84.9% of scored result sets in our test match only through the linked mapping"." A strong case against exact-match scoring.

**2. Would not lift**

- "So none of the figures can be ranked against another, and a vendor's accuracy claim can't be ranked against them either." Reads like a takeaway, but it's an inference and has no number of its own. Line 3 says the same thing more tightly.
- "What carries across is the method." Has the shape of a slogan but says nothing without the surrounding context.
- "A test passed at launch says little about the same agent a month later." Quotable but generic. The 95%-to-65% sentence is the evidence and is what I'd use. (I used this line only for the summary.)
- "A re-run therefore needs a threshold for what counts as a regression, set before the result comes in." Advice with no figure or source behind it.
- "That is the census's more-than-one-right-answer problem, found in a run of our own." Self-referential, and based on an eight-question run the piece itself calls small.
- "A list of real questions, answers computed before you ask, and a rule for what counts as a match are enough to start." A how-to line, but untested beyond that small run.
- "Five companies published enough to copy: what they test against, how they score and when they run it." It's in a numbered list right next to item 6, which names a *different* five (Anthropic, Uber, Hex, GitHub, Salesforce). Quoted alone, a reader would likely confuse the two groups.
- "When we checked it on 27 October, the score updated on save without a re-run; Assumption: it always re-scores when a question is saved." Not quotable. The "Assumption:" text looks like a leftover drafting note that went live.
- "*If this excites you, we'd love to hear from you. Get in touch.*" Boilerplate.

**3. The one line**

"Seven of the 13 companies published an accuracy figure, and no two measured the same thing."

**Things I noticed while reading (not fixed)**

- The table's "One number" column doesn't show an accuracy figure for Snowflake ("150 questions") or Vercel ("5 queries"). Yet the body counts both among the seven that published one. An engine checking the table against that claim would find only five accuracy figures there.
- LinkedIn's "53% rated 4 or 5" links to an arXiv paper, not the LinkedIn blog post given as the row's source. That doesn't fit the claim that "Each row draws on one company's own publications".

File read: C:\Users\LENOVO\OneDrive\Documents\1Sauarbh\1Dot\dot-content-machine\dot-content-machine\reviews\how-companies-test-ai-data-analysts\draft.md
