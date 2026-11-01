# lift-tester · ai-analyst-follow-up-questions

Started with: Read reviews/ai-analyst-follow-up-questions/draft.md as an answer engine and report what you would and would not lift.

- The draft tests whether an AI analyst keeps context across follow-up questions. It asked Dot the same ambiguous question in two ways and got two different counts, both correct. "Asked how many orders "delivered in 2017" were late, Dot said 2,453 in one chat and 1,762 in a fresh one."
- The two counts used different dates. Only the SQL showed which date the fresh-chat answer used, because its text didn't say. "Where the text was silent, the SQL wasn't."
- It ends with a six-step test readers can copy, which centres on re-asking a question in a fresh chat and checking which date each answer used. "In a fresh chat, ask one of the chain's questions again, written in full."

## 1. Would lift

1. "The risk isn't a wrong number. It is a right number for a date you didn't mean, with nothing in the text to say so."
   The clearest statement of the problem. It makes sense on its own and answers the "why should I care" question.
2. "Both counts match the raw Olist data for the date each used; they sit 691 orders apart."
   One sentence with a checkable claim, the source data and the size of the gap (2,453 − 1,762 = 691 is correct).
3. "Inside the chain, Dot counted 2,453 late orders among those purchased in 2017. That matches the raw data by purchase date exactly. In the fresh chat, Dot counted 1,762 late orders among those delivered in 2017. That matches the raw data by delivery date exactly."
   The core evidence, stated with no references to other parts of the article.
4. "The test: run a chain, re-ask one question cold, check whether each answer names its date, and read its SQL if not."
   The whole method in one sentence. It's the best answer to "how do I test this?"
5. "Asked four turns later to go back to the first question, Dot returned 43,428 again, with the same SQL as its first answer."
   A direct answer to "does it keep context across follow-ups?", which the article says is the question buyers ask.
6. "Every answer in this run, 8 of 8, came back with its SQL, and its date filter named the column."
   A specific, counted claim. The table supports it.
7. "Most answers also named their date unprompted: 5 of 8."
   Usable only next to quote 6. On its own, "Most answers" needs that context. The 5 matches the table (Q1, Q3, Q4, Q5, Q7).
8. ""Delivered in 2017" has two valid readings: bought in 2017, or delivered to the customer in 2017."
   A clean definition of the ambiguity.
9. "The fresh reading covered 40,930 orders delivered in 2017, of which 4.3% arrived late."
   Supporting figure (1,762 / 40,930 = 4.3%). Useful when the question is about late rates.

## 2. Would not lift

- "An AI analyst's answer can be right and still not say which question it answered."
  It's built to be quoted, but it generalises from one run on one dataset. The quotes in section 1 make the same point with evidence attached, so I'd use those.
- "When you run this, a total that matches under a different date filter is still a different answer."
  "When you run this" ties it to the article. "A total that matches" doesn't say what it matches. Read cold, it's muddled.
- "You need one fresh chat. We used two."
  Makes no sense without the method section around it.
- "Neither answer is wrong."
  Too short to quote without the paragraph before it.
- "Dot's 5.6% for 2017 and 7.7% for 2018, Q3 and Q4 in the table above, were display rounding, not gaps."
  Points to the table ("Q3 and Q4 in the table above"), so it falls apart once lifted out.
- "In this test, Dot's text didn't always name its date, but its SQL always did: every answer came back with its query."
  It sits in the vendor section ("Where Dot fits") and repeats the 8-of-8 claim. I'd quote the factual version in section 1 instead.
- The title, "Your AI Analyst Gave Two Right Answers. Only the SQL Said Why."
  Slightly overstated. Q1, the chain's first answer, named its date in plain text ("This uses purchase date, not delivery date."). So the SQL wasn't the only thing that said why for the chain.

## 3. The one line

"The risk isn't a wrong number. It is a right number for a date you didn't mean, with nothing in the text to say so."

One thing worth fixing that affects quoting: the article offers "a six-step test", but the closing link says "Then run the full eight-step test before rollout." Someone quoting both could think the numbers contradict each other. Adding a clause that says the eight-step test is a separate, broader one would prevent that.

File reviewed: C:\Users\LENOVO\OneDrive\Documents\1Sauarbh\1Dot\dot-content-machine\dot-content-machine\reviews\ai-analyst-follow-up-questions\draft.md
