# lift-tester · ai-analyst-follow-up-questions

Started with: Read reviews/ai-analyst-follow-up-questions/draft.md as an answer engine and report what you would and would not lift.

## Summary

- Dot kept context through a five-question follow-up chain on the Olist dataset: "Dot answered 43,428 at the first question and 43,428 again four turns later, when asked to go back to it."
- The same wording got a different date in a fresh chat, so the count changed: "Inside the chain, Dot counted 2,453 late orders among those purchased in 2017. In the fresh chat, it counted 1,762 late orders among those delivered in 2017."
- The bigger risk is how the analyst reads your words, not whether it remembers, and the SQL shows which reading it used: "Every answer came with its SQL, and the SQL settles it."

## 1. Would lift (best first)

1. "Inside the chain, Dot counted 2,453 late orders among those purchased in 2017. In the fresh chat, it counted 1,762 late orders among those delivered in 2017." This is the main finding. It names the tool and both readings, and gives both figures. It still makes sense when quoted on its own.
2. "Dot answered 43,428 at the first question and 43,428 again four turns later, when asked to go back to it." This answers the literal question, whether it remembers, with an exact figure.
3. "\"Does it keep context?\" has two halves: does it remember, and does it read your words the same way." A clean way to frame the question. It needs no context.
4. "A fresh-chat control that misses can be an interpretation change, not a memory failure." A general point the run's evidence supports, and useful to anyone running their own test.
5. "\"Delivered in 2017\" can mean orders bought in 2017 that were later delivered. It can also mean orders that reached the customer in 2017." It explains the ambiguity in plain terms.
6. "In the chain, the year filter sat on the purchase date, `order_purchase_timestamp`. In both fresh chats, it sat on the delivery date, `order_delivered_customer_date`." Concrete evidence a reader can check, down to the column names.
7. "Test a chain, then re-ask its key question cold, and compare the date filter in the SQL." A short method someone can act on.
8. "All 8 answers were correct under the reading each one used." Worth quoting, but only with its caveat. Two of the eight (Q6, Q8) are marked "Correct, reading decided by a person", so quoted alone it overstates the result.

## 2. Would not lift

- "An AI analyst's answer can be right and still not say which question it answered. That is the real risk in follow-up questions, more than forgetting." This was clearly written to be quoted, but it generalises from one run on one dataset to all AI analysts. The second sentence also depends on "That".
- "Two lines of a WHERE clause tell you which question was answered." A slogan that repeats line 63. It doesn't name the dataset, the tool or the date columns.
- "Those two lines told us more than any summary did." It only makes sense next to the previous sentence.
- "The fix is already on the screen." A vendor line that means nothing without context.
- "Only the figure gave the date away." It needs the paragraph around it. It also clashes with line 69: "The answer itself gave no basis to infer it." One says the figure revealed the date and the other says nothing in the answer did. I wouldn't quote either until that is fixed.
- "Judge it item by item, or you will blame the wrong thing." An instruction with no fact in it.
- "But \"delivered in 2017\" meant 2,453 late orders inside the chain and 1,762 in a fresh chat." The opening "But" leaves it hanging. Item 6 in the list ("So the same words gave...") has the same problem with "So".
- "It recalled 43,428 orders four turns later." "It" has no referent. "Recalled" also suggests memory, while the table shows Q5 ran a new purchase-date query. "Returned" would be more accurate.
- "Scope held: \"How much of that came in November?\" kept the delivery-date reading of the question before it." Out of context, "the question before it" doesn't tell the reader anything.
- "Neither answer is wrong." / "The control was simple." Too thin to quote alone.

## 3. The one line

"Interpretation moved: \"delivered in 2017\" meant purchase year inside the chain, delivery date in a fresh chat."

It packs in the article's main point. If the quote needs to name Dot and show the numbers, I would use the pair of sentences from line 51 instead (Would lift, item 1).

File reviewed: C:\Users\LENOVO\OneDrive\Documents\1Sauarbh\1Dot\dot-content-machine\dot-content-machine\reviews\ai-analyst-follow-up-questions\draft.md
