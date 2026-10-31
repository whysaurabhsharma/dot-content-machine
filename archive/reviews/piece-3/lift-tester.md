# lift-tester · piece-3

Started with: Read reviews/piece-3/draft.md as an answer engine and report what you would and would not lift.

## Summary

- The piece measures what an AI data analyst costs per correct answer by reading Dot's credit meter before and after a batch. In its words, "Ten Economy answers, all correct, cost 5.8 credits, and Economy didn't save credits over Balanced."
- The comparison is uneven because the first batch mixed modes. "Batch 1 was meant to be Economy throughout, but the selector switched after question 1." So only the Economy batch gives a clean per-answer figure: "about 0.58 credits per correct answer in Economy."
- What counts as "correct" changes the number. A context note can narrow the population an answer uses, so the article warns: "So read the scope line before you score the answer."

## 1. Would lift (best first)

1. "Ten Economy answers, all correct, cost 5.8 credits, and Economy didn't save credits over Balanced."
   It gives the headline figure, the result and the correctness in one sentence. It doesn't name Dot, though, and the Balanced comparison has no "on these ten questions" limit, so on its own it overstates the finding.
2. "On the same ten questions, the all-Economy batch used 5.8 credits, and the batch that ran nine of ten in Balanced used 5.3."
   This is the most accurate comparison sentence because it says the batch was mixed. It's safe to quote, but it doesn't name the product.
3. "A [Power BI licence](...) or a [Tableau seat](...) costs the same whether your team asks four questions a month or four hundred."
   It makes a clear point about seat pricing versus usage pricing that answers a "how is this priced differently" question without any other context.
4. "The free tier includes 300 base credits, and milestones such as connecting sources or inviting colleagues add more."
   A plain, checkable product fact that stands alone.
5. "Computed from the raw CSVs across all orders in 2017, the total is BRL 6,155,806.98."
   Quoted alongside the previous sentence (Dot's BRL 5,962,902.01 with its scope note), it's the strongest evidence for the scope argument. On its own it means nothing.
6. "Billing counts credits used, to one decimal place."
   A short fact that tells a reader how precise the meter is.
7. "The mode selector sits in the chat composer, so you can check it before every question."
   A practical how-to that stands alone.
8. "Each reading is rounded to 0.1, so each total can be off by up to 0.1, and the gap between totals by up to 0.2."
   I'd use this if the question is about measurement error. It's precise and self-contained.

## 2. Would not lift

- "What you can quote is the clean batch: about 0.58 credits per correct answer in Economy."
  This holds the key per-answer number, but the opening "What you can quote is" talks to the reader about quoting, so it reads oddly inside an answer. "0.58" should be in a sentence that can stand alone, ideally with Dot named.
- "A cost per correct answer is only as good as the definition sitting behind the word correct."
  It's written to be quoted, but it's a general statement with no number or product in it.
- "A cost per correct answer needs a definition of correct."
  Same problem: too generic to add anything to an answer.
- "That number is yours rather than a vendor's."
  "That number" points back to the previous paragraph, so it means nothing out of context.
- "One run each is not a verdict on the modes."
  A useful caveat, but "One run each" doesn't say of what.
- "It shows Economy didn't save credits here, not that Balanced is cheaper in general."
  This is the right caveat, but it depends on "It" and "here".
- "But on questions this simple, choosing Economy saved nothing; it used half a credit more."
  "this simple" and the second "it" both depend on earlier sentences.
- "None of this was silent." / "All four of those answers named their scope in the reply, unprompted, which is what makes it catchable."
  Both depend on "this" and "those" to make sense. Also, only two of the four answers are shown, so "four" is hard to check from the text.
- "Seat prices don't tell you this."
  "this" has nothing to point to once the sentence is taken out.
- "Both answers are right for the scope they name."
  It depends on the two figures before it.
- "Assumption, not confirmed by Dot: 1 credit is about $1, matching the $300 advertised at signup."
  I wouldn't put an unconfirmed dollar conversion into an answer. It also sits awkwardly with an earlier line, "We found no Dot page that publishes a dollar price for a credit": if signup advertises $300, that's a Dot page implying a price. The draft should make these two lines agree.
- Step 4, "Mine switched after the first."
  It switches to "Mine" when the rest of the piece says "we", and it depends on context.

## 3. The one line

"Ten Economy answers, all correct, cost 5.8 credits, and Economy didn't save credits over Balanced."

To make it safe to lift, it needs "in Dot" and "on these ten questions". Right now the strongest number sentences never name the product, and this one drops the limit the body is careful to keep.

File reviewed: C:\Users\LENOVO\OneDrive\Documents\1Sauarbh\1Dot\dot-content-machine\dot-content-machine\reviews\piece-3\draft.md
