---
title: "Can an AI Analyst Take Your Ad Hoc Data Requests? We Tested 29"
seo_title: "AI Analyst for Ad Hoc Data Requests: 29 Questions Tested"
meta: "Can an AI analyst take over your ad hoc data requests? We ran 29 Slack-style questions through Dot: 25 answered, 3 sent back, and what to check first."
slug: ai-analyst-ad-hoc-requests
queries:
  - reduce ad hoc data requests
  - ad hoc data request process
  - conversational analytics
playbook_url: https://www.getdot.ai/blog/ai-data-analyst-playbook
figures: figures/piece-2-figures.csv
dataset: Olist public dataset, CC BY-NC-SA 4.0 (facts A10)
reverse_links:
  - The Playbook's Stage 5 card, anchor "29 ad hoc questions, tested"
  - The DABstep post, anchor "what an AI analyst actually answers"
  - /blog/conversational-analytics, anchor "how many ad hoc requests an AI analyst absorbs"
---

**If your data team spends its week answering ad hoc Slack questions, you need a number, not advice. We put 29 of them to Dot, each in a fresh chat. Twenty-five came back answered, and the numbers we rebuilt from the raw data all matched. By the end, you will have the 29 questions, the four outcomes, and the first check to run: does each answer say what it counted?**

One answer shows why that check matters. When we asked how much revenue we did last year, there was nothing to find: the dataset ends in October 2018. Dot reported BRL 0 and called it "a data-coverage limit, not evidence of zero business activity." Then it offered the latest twelve months instead.

**The seven steps, if you read nothing else:**

1. Write down your recent ad hoc questions in the words people actually asked them.
2. Ask each in a fresh chat, one question per chat, and don't help it.
3. Count four outcomes only: answered, asked back, refused with an offer, needed a person.
4. Read each answer for its basis: the population, the period, the definition.
5. Recompute the numbers yourself against the raw table. Agreement is the test, not confidence.
6. Treat "asked back" as a pass. All three of ours had two reasonable readings.
7. Log what the chat escalated to an admin. Mine raised three items, two of them duplicates.

## Twenty-five of twenty-nine came back answered, and none needed a person

The set-up was deliberately ordinary. The data was a public Brazilian e-commerce dataset: two tables, 99,441 orders, September 2016 to October 2018. Two context notes were active: one sets eligible orders to delivered, the other covers currency.

We wrote 29 requests in the voice people use in a data channel: lowercase, short, unspecific, the kind [self-service analytics tools](https://www.getdot.ai/blog/self-service-analytics-tools) aim to absorb. Each went into its own fresh chat, with no follow-up from us. Nothing was rephrased to help it along.

Thirty were written. One, a follow-up ("same thing but only 2017"), was dropped: in a fresh chat, "same thing" has nothing to refer to. That is why the table skips R2.

Then we counted four outcomes, one per request. Twenty-five came back answered. Three asked a question back. One declined and offered something else.

"Needed a person" means the requester could not get an answer or a clear next question without an analyst stepping in, and none did. The three that asked back needed one reply from the requester; we sent none, so they stay unresolved here.

Zero escalations is not zero work. Four requests ended without a final number, but each ended with a clear next step: a question back, or an alternative. That is what [conversational analytics](https://www.getdot.ai/blog/conversational-analytics) promises, measured once.

## Most answers said what they counted, which is what makes them checkable

Twenty-six requests returned a result: the 25 answers, plus the refusal's zero. Twenty-two of those 26 replies stated their basis without being asked. They named the population, the period, or the definition they had used.

Eight of the 22 scoped themselves to delivered orders unasked. That matches the context note, which sets eligible orders to delivered for revenue, order value, basket size and shipping. Assumption, not yet confirmed by Dot: the context agent stores a definition once, so every chat answer uses it.

Four of the 26 did not state a basis. For answers like those, the safeguard is a written expected answer with the population in it, as in [Stage 3 of the Playbook](https://www.getdot.ai/blog/ai-data-analyst-playbook).

## Every number we could check matched the raw data, including the one that said no

Twenty-five of the 26 results carried a number: 24 answers and the refusal's zero. The exception was Q4, an answer that listed missing product data. A script rebuilt each of the 25 numbers from the two raw CSVs on 28 October, the day after the run, and all 25 matched. The script used the definition each answer stated, so this checks the arithmetic, not the choice of definition.

One of the matches was a no. When we asked "are our biggest sellers also our most reliable on delivery", Dot said no. The top ten sellers delivered on time 92.2% of the time, against 93.2% across all sellers. Half of the top ten sat below the overall rate.

Those figures count "on time" by calendar day. By the hour, they come out at 91.0% and 91.9%, and the answer is still no.

When we asked whether to push customers to buy more than one item, Dot called it worth testing, not pushing indiscriminately. It also raised the missing margin and conversion data for an admin. Three admin items came out of the run: two proposals marked as duplicates of earlier ones, and one new data gap. These were notes for later, raised alongside answers already given, not requests left waiting.

This is agreement with the source tables, not with a second analyst, and it was checked once, by script. Dot's Evaluation feature is the repeatable version. In a separate test, it held questions with expected answers, a unit and a tolerance per question, and re-scored the moment we saved a row.

## The three pauses were questions with two right answers

Asking back was the right move, not a weakness: each of the three questions had two right answers. Busiest, worried about, wrong: each request contained one of those words. To "whats our busiest month", Dot replied: "Do you mean busiest by number of orders or by delivered merchandise sales (BRL)?"

The other two split the same way. For "worried about", Dot asked whether we meant fulfilment problems or declining sales. For "anything wrong with this data", it asked which table, or a specific chart. Each reply asked which.

| ID | Request, as asked | Outcome |
| --- | --- | --- |
| L1 | how many orders did we get in total | Answered |
| L2 | how many of those actually got delivered | Answered |
| L3 | whats our busiest month | Asked back |
| L4 | how many orders got cancelled | Answered |
| L5 | how many sellers do we have | Answered |
| L6 | whats the most expensive single item anyone bought | Answered |
| L7 | when does the data start and end | Answered |
| L8 | how many orders have more than one item in them | Answered |
| L9 | how many different order statuses are there | Answered |
| L10 | roughly how many items per order | Answered |
| D1 | whats our revenue | Answered |
| D2 | whats the average order value | Answered |
| D3 | how much have we made from shipping | Answered |
| D4 | whats our cancellation rate | Answered |
| D5 | whats our average basket size | Answered |
| D6 | how much revenue did we do last year | Refused with an offer |
| R1 | of the delivered orders, how much did they come to in total | Answered |
| R3 | split the orders by status and give me a count for each | Answered |
| R4 | which month in 2018 was worst for cancellations | Answered |
| R5 | how much of our total value is shipping vs the actual goods | Answered |
| R6 | are multi-item orders worth more than single-item ones, on average | Answered |
| N1 | why did orders drop off after September 2018 | Answered |
| N2 | are our biggest sellers also our most reliable on delivery | Answered |
| N3 | is it worth us pushing customers to buy more than one item at a time | Answered |
| N4 | which sellers should we be worried about | Asked back |
| Q1 | is there anything wrong with this data that I should know about | Asked back |
| Q2 | are there any orders missing a delivery date that say they're delivered | Answered |
| Q3 | do any orders appear twice | Answered |
| Q4 | what's missing from this dataset that I'd need to answer questions about products | Answered |

By question type: lookup 10, with 9 answered and L3 asked back. Definition 6, with 5 answered and D6 refused with an offer; drill-down 5, all answered. Novel analysis and data quality 4 each, with 3 answered; N4 and Q1 asked back. Types describe the question, not why it paused.

![Five stacked horizontal bars, one per question type, showing 29 ad hoc requests by outcome. Lookup: 9 answered, 1 asked back. Definition: 5 answered, 1 refused with an alternative offered. Drill-down: 5 answered. Novel analysis: 3 answered, 1 asked back. Data quality: 3 answered, 1 asked back. No bar has a segment for needing an analyst.](charts/piece-2-outcomes.png)

*29 ad hoc requests by question type and outcome. Our trial account, Production environment, 27 October 2026. Mode: Economy for requests 1–21, Balanced for 22–29.*

## Things to keep in mind

- **The 29 questions were written by us, not lifted from a real Slack queue.** They use the voice of a data channel, but no real backlog was cleared here.
- **This is an "after" with no "before".** Nobody measured the team's ad hoc load first. Your own queue is your baseline.
- **One dataset, two tables, two context notes active.** A warehouse with twenty definitions may behave differently, whichever of [the tools that promise this](https://www.getdot.ai/blog/conversational-analytics-software) you put in front of it.
- **The mode drifted.** Economy ran requests 1–21 and Balanced ran 22–29, noticed after the fact. Outcomes are reported across both, not split by mode.

## Where Dot fits

Everything above ran in [Dot's chat](https://docs.getdot.ai), one fresh chat per request, with two context notes active; one sets eligible orders to delivered. Dot's chats also raise proposals and data-gap items for an admin, and mark repeats as duplicates. Assumption, not yet confirmed by Dot: the context agent stores a definition once, so every chat answer uses it. It is [Stage 5 of the Playbook](https://www.getdot.ai/blog/ai-data-analyst-playbook), run rather than described.

---

Take the last ten ad hoc questions from your data channel, in the words they were asked, and put each one in a fresh chat.

Then run the first check: does each answer say what it counted? An answer that names its population is easy to check; one that doesn't leaves you guessing what it counted.

*If this excites you, we'd love to hear from you. Get in touch.*
