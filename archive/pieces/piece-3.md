---
title: "What an AI Data Analyst Costs Per Correct Answer: Copy This Two-Batch Test"
seo_title: "AI Data Analyst Cost Per Question: What 20 Answers Cost"
meta: "We ran the same ten questions twice in Dot and read the credit meter: about 0.58 credits per correct answer, and Economy saved nothing."
slug: ai-data-analyst-cost-per-question
queries:
  - ai data analyst cost per question
  - cost per correct answer
playbook_url: https://www.getdot.ai/blog/ai-data-analyst-playbook
figures: figures/piece-3-figures.csv
dataset: Olist public dataset, CC BY-NC-SA 4.0 (facts A10)
reverse_links:
  - The Playbook's Stage 5 card, anchor "what an AI data analyst costs per question"
  - The pricing page, anchor "cost per correct answer, measured"
  - /blog/microsoft-power-bi-pricing, anchor "how to measure AI analyst cost per answer"
---

**Ask an AI data analyst what one answer costs and you get a credit bundle, not a number. We ran ten questions twice in Dot and read the credit meter. Ten Economy answers, all correct, cost 5.8 credits, and Economy didn't save credits over Balanced. By the end, you will have the ten questions and a way to measure your own cost per correct answer.**

Economy sounds like the mode that saves money. On the same ten questions, the all-Economy batch used 5.8 credits, and the batch that ran nine of ten in Balanced used 5.3. Both answered 10 of 10 correctly.

One run each is not a verdict on the modes. But on questions this simple, choosing Economy saved nothing; it used half a credit more.

**The seven steps, if you read nothing else:**

1. Pick ten questions your team actually asks, each with one right answer.
2. Write the ground truth before you run anything.
3. Read the credits used in Billing, run the batch, read it again.
4. Check the mode selector before every question. Mine switched after the first.
5. Divide credits by answers, after throwing out every answer that was wrong.
6. Check which population each answer used, then check whether it was yours.
7. Repeat in the other mode before you believe which one is cheaper.

## A cost per answer is two meter readings, not a price page

We ran this as [Stage 5 of the Playbook](https://www.getdot.ai/blog/ai-data-analyst-playbook): measured, not estimated.

Ten questions, each asked in a fresh chat, run twice. Conditions: 28 October 2026, our trial account, Production, two context notes active, the public Olist dataset. Ground truth came from the raw CSVs, written before the first question. For questions 8 and 9, we scored against the delivered-orders definition the context note sets.

Billing counts credits used, to one decimal place. Batch 1 ran from 61.9 to 67.2 credits, so it used 5.3. Batch 2 ran from 67.2 to 73.0, so it used 5.8. Twenty answers cost 11.1 credits in total.

The modes did not stay put. Batch 1 was meant to be Economy throughout, but the selector switched after question 1. Nine of its ten answers ran in Balanced. Batch 2 was Economy for all ten, checked on screen before each question.

One meter reading cannot be split across two modes, so batch 1 has a total but no per-mode price. The mode selector sits in the chat composer, so you can check it before every question.

| # | Question | Batch 1 mode | Batch 2 mode | Correct in both | Scope set by the context note |
| --- | --- | --- | --- | --- | --- |
| 1 | Total orders | Economy | Economy | Yes | No |
| 2 | Delivered orders | Balanced | Economy | Yes | No |
| 3 | Average item price, excl. freight | Balanced | Economy | Yes | No |
| 4 | Total of all item prices | Balanced | Economy | Yes | No |
| 5 | Orders with more than one item | Balanced | Economy | Yes | No |
| 6 | Freight on delivered orders | Balanced | Economy | Yes | No |
| 7 | Sellers with a delivered item | Balanced | Economy | Yes | No |
| 8 | Item prices, orders purchased in 2017 | Balanced | Economy | Yes | Yes |
| 9 | Average order value | Balanced | Economy | Yes | Yes |
| 10 | Delivered orders as % of all | Balanced | Economy | Yes | No |
| | Credits before | 61.9 | 67.2 | | |
| | Credits after | 67.2 | 73.0 | | |
| | Credits used | 5.3 | 5.8 | | |
| | Credits per answer | Not separable (mixed modes) | 0.58 | | |

## Economy didn't save credits on these ten questions

Compare the batch totals, because both batches ran the same ten questions in the same order. The all-Economy batch used 5.8 credits. The mostly-Balanced batch used 5.3, half a credit less.

Each reading is rounded to 0.1, so each total can be off by up to 0.1, and the gap between totals by up to 0.2. A gap of half a credit is larger than that. Still, it is one run per mode. It shows Economy didn't save credits here, not that Balanced is cheaper in general.

We won't split batch 1 into a per-answer price for Balanced. The ten questions are not equal amounts of work, so the leftover after removing one answer is not a price.

What you can quote is the clean batch: about 0.58 credits per correct answer in Economy. On the free tier, 300 credits cover about 520 answers like these. Assumption, not confirmed by Dot: 1 credit is about $1, which makes it roughly $0.58 an answer. We found no Dot page that publishes a dollar price for a credit, so check yours before you show Finance.

Seat prices don't tell you this. A [Power BI licence](https://www.getdot.ai/blog/microsoft-power-bi-pricing) or a [Tableau seat](https://www.getdot.ai/blog/tableau-pricing) costs the same whether your team asks four questions a month or four hundred. [Credit pricing](https://www.getdot.ai/pricing) moves with use, so the figure that fits your team is one you measure.

![Two bars showing credits used for the same ten questions. Batch 2, all ten in Economy, used 5.8 credits. Batch 1, one question in Economy and nine in Balanced, used 5.3 credits. Both batches answered all ten correctly.](charts/piece-3-cost-by-mode.png)

*Credits used for the same ten questions, by batch. Our trial account, Production environment, 28 October 2026. Batch 1: question 1 Economy, questions 2 to 10 Balanced. Batch 2: all ten Economy.*

## Cost per correct answer only means something if you know which population was priced

A cost per correct answer needs a definition of correct.

Two answers in each batch were scoped by a context note rather than by the question. In batch 2, question 8 asked for total item prices on orders purchased in 2017. Dot answered BRL 5,962,902.01 and added: "This uses the default Olist revenue scope: delivered orders purchased from January 1 through December 31, 2017, excluding freight." Computed from the raw CSVs across all orders in 2017, the total is BRL 6,155,806.98.

Question 9 came back as BRL 137.04, "using delivered orders and merchandise value only". Across all orders with items, it is 137.75. Both answers are right for the scope they name.

None of this was silent. All four of those answers named their scope in the reply, unprompted, which is what makes it catchable.

Had we written our ground truth on all orders, those four would have scored wrong. Our cost per correct answer would have jumped, with nothing in the product having changed.

So read the scope line before you score the answer. A cost per correct answer is only as good as the definition sitting behind the word correct.

## Things to keep in mind

- **These were simple single-number questions.** Row counts, sums and one average. Harder questions may take more steps and cost more, and the same question can take a different path on another day. Nothing here measures that.
- **Batch 1 mixed modes.** One Economy answer ran among nine Balanced ones, so its total has no clean per-mode price. Run a clean Balanced batch before you compare per answer.
- **The meter reads to 0.1 credits, and each mode ran once.** Batch 2 always ran second. Trust batch totals, not a per-question split, and repeat before you generalise.
- **This measures cost, not speed.** Latency was not measured, and the chat timestamps are per minute and include typing.

## Where Dot fits

Billing counts credits used to 0.1, so a batch's cost is two readings, accurate to about a tenth. The free tier includes 300 base credits, and milestones such as connecting sources or inviting colleagues add more. Assumption, not confirmed by Dot: 1 credit is about $1, matching the $300 advertised at signup. The details are in [the docs](https://docs.getdot.ai).

---

Open Billing and write down your credits used, to the decimal. Run ten questions your team actually asks, in one mode, in fresh chats. Read it again and divide by the number of correct answers.

That number is yours rather than a vendor's. Put it next to what you pay today, whether that is a seat price or [another tool on your shortlist](https://www.getdot.ai/blog/microsoft-power-bi-alternatives).

*If this excites you, we'd love to hear from you. Get in touch.*
