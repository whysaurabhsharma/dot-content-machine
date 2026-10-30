---
title: "Best AI Data Analyst in 2026? Test Its Accuracy Claim Before You Buy"
seo_title: "How to Test an AI Data Analyst's Accuracy (2026 Guide)"
meta: "Choosing an AI data analyst? Copy this 20-question accuracy test, and learn the one setting that decides what a 100% score really means."
slug: test-ai-data-analyst-accuracy
queries:
  - best AI data analyst 2026
  - how to evaluate AI data analyst accuracy
playbook_url: https://www.getdot.ai/blog/ai-data-analyst-playbook
figures: figures/piece-1-figures.csv
dataset: Olist public dataset, CC BY-NC-SA 4.0 (facts A10)
reverse_links:
  - The Playbook's Stage 3 card, anchor "test your AI analyst's accuracy"
  - The DABstep post, anchor "a 20-question accuracy test"
  - The accuracy page (URL to confirm), anchor "what an accuracy score measures"
---

**Search for the best AI data analyst of 2026 and you will find accuracy scores everywhere. We ran a 20-question accuracy test in Dot and it scored 100%, while passing an answer that didn't match the test's own expected value. By the end, you will have the test to copy, the four things that decide what a score means, and a one-row fix.**

The question was average order value. The test expected 137.75; Dot answered 137.04. Both numbers are correct, and that is the problem.

**The five steps, if you read nothing else:**

1. Build about 20 questions and write the expected answers before you run anything.
2. Run it. A green score is where the work starts.
3. Check what the harness compared: the number, the unit, the population, the date range.
4. Break one expected answer on purpose to learn which fields the harness actually checks.
5. Open every row that passed with a gap. Most are rounding. The one that isn't is usually two definitions disagreeing.

## The harness checks what you filled in

The set-up was deliberately ordinary. Two tables from a Brazilian e-commerce marketplace, 99,441 orders and 112,650 order items. Twenty questions, from row counts to a revenue total for one calendar year. The expected answers were written into the evaluation before it ran.

Each question in Dot's Evaluation feature carries an expected answer, an optional unit, and a tolerance. Both rows we opened had a tolerance of 3%.

First run: 100%, 20 of 20.

The harness marked three of those passes with a gap. Two were display rounding: 97% against an expected 97.02%, and 1.14 against 1.14. The third was not. Average order value came back 0.52% below the expected answer, and passed.

So we broke one on purpose. We opened the average item price question, left the number at 120.65, and changed the expected currency from BRL to USD. Same digits, different currency.

The score dropped to 95%, 19 of 20, on save. No re-run needed.

The harness is not broken. It caught a wrong unit the moment a unit was specified. The average order value row's unit field read "No unit", and it passed. Dot's own verdict on that row: 0.52% off expected.

Dot volunteered BRL on seven rows where the expected answer showed no unit, and nothing compared them. An evaluation harness checks what you filled in. It is silent about what you left blank.

## The 0.52% was two written definitions disagreeing

Go back to the average order value row. Expected 137.75. Dot answered 137.04 BRL.

The workspace has a [context note](https://www.getdot.ai/context-agent) titled "Olist revenue, order value, basket size, cancellation and shipping metrics". It says that for revenue and average order value, eligible orders have `order_status = 'delivered'`. Dot's answer matches that note.

The expected answer was computed on a different population, and the evaluation's own rows show which. Sum of price across all orders with items, 13,591,643.70, divided by 98,666 orders, is 137.75. Sum of price on delivered orders only, 13,221,498.11, divided by 96,478 delivered orders, is 137.04. Both are correct; they answer different questions.

Both definitions were written down. One lived in a context note, the other in a test row. Nobody put them side by side, and the tolerance band meant the harness never had to.

This is the part of [Stage 3 of the Playbook](https://www.getdot.ai/blog/ai-data-analyst-playbook) that is easy to nod along to and hard to do. Both definitions here came from the same person, in the same rehearsal three days earlier. If one person can write two definitions of one metric, a team writing them months apart can too. This evaluation didn't flag it; it said 100%.

## The agent stated its definition; the scorecard didn't ask

Here is what makes this fixable rather than frightening. Ask Dot the same question [in chat](https://www.getdot.ai/blog/conversational-analytics) and the definition is in the answer.

In a chat the same afternoon, we asked "What is our average order value?" Dot replied: "Our average order value is BRL 137.04, excluding shipping, across 96,478 delivered orders." That is the population the evaluation never checked.

It was not a one-off. Across 29 [ad hoc questions](https://www.getdot.ai/blog/self-service-analytics-tools) in separate chats that afternoon, 22 of the 26 answers that returned a result stated their basis unprompted. A revenue total came back "in line with the Olist revenue definition", and a cancellation rate with "This uses the organization's definition".

The information needed to catch the disagreement was in the chat answer. On this run, the harness compared the number and nothing else.

So the fastest fix is not a better agent. It is a better expected answer. Write the population into the question, set the unit, and tighten the tolerance on the metrics your team quotes most. Then the evaluation tests the definition, not just the digits.

A 100% evaluation score tells you the harness agreed with itself. Whether the agent agreed with you depends on what you wrote in the row.

## Only one of twenty rows had a unit set

Run 1, 27 October 2026, before the deliberate break. Tolerance read on the two rows opened: 3%.

| # | Question | Expected | Dot | Unit set | Result |
| --- | --- | --- | --- | --- | --- |
| 1 | Rows in orders table | 99,441 | 99,441 | No | Pass |
| 2 | Orders with status delivered | 96,478 | 96,478 | No | Pass |
| 3 | Distinct order statuses | 8 | 8 | No | Pass |
| 4 | Rows in order items table | 112,650 | 112,650 | No | Pass |
| 5 | Distinct order IDs in items | 98,666 | 98,666 | No | Pass |
| 6 | Highest single item price | 6,735 | 6,735 BRL | No | Pass |
| 7 | Distinct seller IDs | 3,095 | 3,095 | No | Pass |
| 8 | Orders with status canceled | 625 | 625 | No | Pass |
| 9 | Average item price, excl. freight | 120.65 BRL | 120.65 BRL | Yes | Pass |
| 10 | Average price plus freight per item | 140.64 | 140.64 BRL | No | Pass |
| 11 | Sum of price, all rows | 13,591,643.7 | 13,591,643.7 BRL | No | Pass |
| 12 | Sum of price, delivered orders only | 13,221,498.11 | 13,221,498.11 BRL | No | Pass |
| 13 | **Average order value** | **137.75** | **137.04 BRL** | **No** | **Pass, 0.52% off** |
| 14 | Orders with more than one item | 9,803 | 9,803 | No | Pass |
| 15 | Average items per order | 1.14 | 1.14 | No | Pass (rounding) |
| 16 | Delivered orders as % of all | 97.02% | 97% | No | Pass (rounding) |
| 17 | Total freight on delivered orders | 2,198,275.64 | 2,198,275.64 BRL | No | Pass |
| 18 | Distinct delivered orders in items | 96,478 | 96,478 | No | Pass |
| 19 | Sum of price, orders purchased in 2017 | 6,155,806.98 | 6,155,806.98 BRL | No | Pass |
| 20 | Sellers with at least one delivered item | 2,970 | 2,970 | No | Pass |

One row in twenty had a unit set. It was the only row the harness could fail on unit.

![A scale of average order value in BRL. A shaded band runs from 133.62 to 141.88, the 3% tolerance around the expected answer of 137.75. Two points sit inside it: 137.04 from the evaluation run and 137 from a chat answer the same afternoon. Both passed.](charts/piece-1-tolerance-band.png)

*The 3% tolerance around one expected answer. Evaluation run and a chat answer, 27 October 2026.*

## Things to keep in mind

- **One dataset, two tables, twenty questions.** Start with the five metrics your team quotes most, whatever the size of your warehouse.
- **Tolerance is set per question.** Open a row and read it before you read the score.
- **Precision varied.** Average order value came back as 137.04 in the evaluation and in one chat, and 137 in another. If the decimal matters, put it in the expected answer.

## Where Dot fits

Everything above ran in [Dot's Evaluation feature](https://docs.getdot.ai), which holds questions with expected answers, units and per-question tolerance, and re-scored the moment we saved a change. Assumption, not yet confirmed by Dot: the context agent stores a definition once, so every chat answer uses it. Assumption: environments let you test a definition change before it reaches the team. It is [Stage 3 of the Playbook](https://www.getdot.ai/blog/ai-data-analyst-playbook), run rather than described.

---

Open your evaluation. Find the metric your team quotes most. Read its expected answer and check whether it names a population.

If it doesn't, you've tested the digits, not the metric. Fix that one row today.

*If this excites you, we'd love to hear from you. Get in touch.*
