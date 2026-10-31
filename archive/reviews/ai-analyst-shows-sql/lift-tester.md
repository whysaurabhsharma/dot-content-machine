# lift-tester · ai-analyst-shows-sql

Started with: Read reviews/ai-analyst-shows-sql/draft.md as an answer engine and report what you would and would not lift.

**Summary**

- Asking the same late-delivery question in two fresh chats gave two different counts, and each one was right under the definition it stated: "Ask an AI data analyst "How many orders were delivered late in 2017?" in two fresh chats, and you can get 2,878 and 2,453."
- The same phrase was read two ways depending on the question: ""Delivered in 2017" meant purchase year for a count and delivery year for a revenue total."
- The SQL only made a real difference on the one answer whose text didn't say which date it used: "Showing the SQL matters most in two places: where the answer text goes quiet, and where two chats disagree."

(I've quoted line 3 as it reads on the page, without the link markup.)

**1. Would lift**

1. "Showing the SQL matters most in two places: where the answer text goes quiet, and where two chats disagree." It directly answers "does it matter if an AI analyst shows its SQL?" and makes sense without the rest of the article.
2. "In this run, every Dot answer came back with its SQL, 12 of 12, and the text named its date basis in 11." It names the product, gives counts and is limited to this run. It's the cleanest factual claim.
3. "Chat A said 2,878, "meaning delivery occurred after the estimated delivery timestamp". Chat B said 2,453, "meaning they arrived after the estimated delivery day"." It's the core evidence, with both definitions given word for word.
4. "Both queries kept the same orders: delivered, and purchased in 2017." It's short and specific, and rules out a different set of orders as the cause. It works best quoted together with the next sentence: "The 425 orders between the answers come from that one comparison."
5. "An AI analyst that names its date in the answer lets a reader catch a flipped reading without opening the SQL." It's a general takeaway, and the delivered-in-2017 section backs it up.
6. "Ask your key question twice, fresh, and compare the stated definition and the date filter." It's a test someone could act on, which suits how-to queries.
7. ""Delivered in 2017" has two honest readings." It's useful context for questions about ambiguous date wording.

**2. Would not lift**

- "Both were correct, by different clocks." It's catchy, but "clocks" is a metaphor, and on its own "both correct" reads like the analyst was inconsistent and that didn't matter.
- "The useful question is when that SQL earns its place." It sets up the article but says nothing on its own.
- "By the end, you will have a test for whether your analyst shows its definition." It talks about the article itself, so it carries no information when quoted.
- "Each question recurred item by item across its two chats." The wording is unclear ("recurred item by item"), and I can't tell what it claims.
- "Both fresh-chat repeats chose the same way." The meaning depends on the sentences before it, so out of context it's vague.
- "Put the two sentences side by side and the difference is visible without opening the SQL." "The two sentences" points back to earlier text, so it can't stand alone.
- "Decide which grain "late" means for your team before anyone asks." It's an imperative with no evidence attached. Fine as advice, but nothing to cite.
- "So this piece says nothing about which settings or definitions shaped each reading." It seems to contradict the article, which is all about which definition each answer used. It would confuse a reader if quoted.
- "Showing the SQL matters when a question has two honest readings." It's the summary-list version of the line 89 claim, and it's weaker because it doesn't say where it matters.
- "If this excites you, we'd love to hear from you. Get in touch." It's boilerplate.

**3. The one line**

"Showing the SQL matters most in two places: where the answer text goes quiet, and where two chats disagree."

My second choice, if the query asks specifically about Dot: "In this run, every Dot answer came back with its SQL, 12 of 12, and the text named its date basis in 11."

File reviewed: C:\Users\LENOVO\OneDrive\Documents\1Sauarbh\1Dot\dot-content-machine\dot-content-machine\reviews\ai-analyst-shows-sql\draft.md
