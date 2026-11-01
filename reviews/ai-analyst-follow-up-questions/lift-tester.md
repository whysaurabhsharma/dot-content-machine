# lift-tester · ai-analyst-follow-up-questions

Started with: Read reviews/ai-analyst-follow-up-questions/draft.md as an answer engine and report what you would and would not lift.

**Summary**

- Dot gave two different late-order counts for one ambiguous phrase, and both were right: "Dot counted 2,453 late orders by purchase date in a follow-up chat, and 1,762 by delivery date in a fresh chat."
- The answer text didn't always say which date was used, but the SQL always did: "Every answer in this run, 8 of 8, came back with its SQL, and its date filter named the column."
- The article ends with a test anyone can repeat: "The test: run a follow-up chat, re-ask one question in a fresh chat, and read the SQL of any answer that doesn't name its date."

**1. Would lift (best first)**

1. "Dot counted 2,453 late orders by purchase date in a follow-up chat, and 1,762 by delivery date in a fresh chat." It stands on its own and gives both numbers, both dates and both chat types. It's the main finding in one sentence.
2. "Every answer in this run, 8 of 8, came back with its SQL, and its date filter named the column." It's a clear, checkable number that answers "how would I know which date it used?"
3. "Asked four turns later to go back to the first question, Dot returned 43,428 again, with the same SQL as its first answer." It directly answers the buyer's question about whether the analyst keeps context.
4. "The test: run a follow-up chat, re-ask one question in a fresh chat, and read the SQL of any answer that doesn't name its date." It's a whole method in one line, good for "how do I test this?" questions.
5. "Both counts match the raw Olist data for the date each used; they sit 691 orders apart." It verifies both counts and sizes the gap. It needs item 1 before it ("Both counts" depends on it), so I'd quote them together.
6. "It is a right number for a date you didn't mean, with nothing in the text to say so." This is the general warning. I'd only use it next to the sentence before it (see below).
7. "Late means delivered on a later calendar day than the estimated delivery date." A definition worth citing as support when explaining the numbers.
8. "This uses purchase date, not delivery date." Dot's own words. It's good evidence that the first answer named its date.

**2. Would not lift**

- "An AI analyst's answer can be right and still not say which question it answered." It's written as a pull quote, but it's general and only repeats line 56, which is more specific. An answer engine would take the concrete version.
- "The risk isn't a wrong number." Taken alone it's a teaser with nothing in it. It only works as a setup for the next sentence.
- "When you run this, a total that matches under a different date filter is still a different answer." The opening clause depends on what came before, and "a total that matches" doesn't say what it matches. It's hard to read on its own.
- "You need one fresh chat. We used two." It's catchy but means nothing out of context. It also counts the item-price chat as a "fresh chat", while the method section calls it "A third chat".
- "Neither answer is wrong." This needs the paragraph before it to make sense.
- "Where the text was silent, the SQL wasn't." It's a rhetorical lead-in. The 8 of 8 sentence after it carries the actual fact.
- "In this test, Dot's text didn't always name its date, but its SQL always did: every answer came back with its query." It repeats the 8 of 8 line in a section that reads like a sales pitch, so I'd quote the neutral version.
- "Before you trust either number, check which date each answer used." "Either number" depends on context, and the line is part of a call to action.
- "Dot's 5.6% for 2017 and 7.7% for 2018, both in the follow-up chat, were display rounding, not gaps." It's accurate but too detailed for most answers.

**3. The one line**

"Dot counted 2,453 late orders by purchase date in a follow-up chat, and 1,762 by delivery date in a fresh chat."

**Notes**

- I checked the figures against each other and they agree: 2,453 − 1,762 = 691; 2,453 / 43,428 = 5.6%; 1,762 / 40,930 = 4.3%. The table shows 5 answers that named their date and 3 that didn't, matching the "5 of 8" and "three answers stated no date" claims.
- In the lede, "Dot" is a markdown link (`[Dot](https://www.getdot.ai/)`), so anyone quoting it would quote the displayed text.

File reviewed: C:\Users\LENOVO\OneDrive\Documents\1Sauarbh\1Dot\dot-content-machine\dot-content-machine\reviews\ai-analyst-follow-up-questions\draft.md
