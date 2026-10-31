---
title: "How to Test an AI Data Analyst Before Rollout: 8 Steps"
format: guide
seo_title: "How to Evaluate AI Data Analyst Accuracy Before Rollout"
meta: "Eight steps to test an AI data analyst before rollout: real questions, every accepted answer written first, two fresh chats each, and the SQL read."
slug: test-ai-analyst-before-rollout
query_data: "how to evaluate ai data analyst accuracy: not indexed (not measured). Related: ai data analyst 700 US, 2.0K global, difficulty 22; text to sql accuracy 10 US, difficulty not measured. Ahrefs, 27–28 October 2026"
reverse_links:
  - The AI Data Analyst Playbook (https://www.getdot.ai/blog/ai-data-analyst-playbook), on the stage that covers testing before rollout, anchor "how to test an AI data analyst before rollout"
  - The teardown of how 13 companies test their AI analysts (https://www.getdot.ai/blog/how-companies-test-ai-data-analysts), in its closing instruction, anchor "eight steps to test your AI analyst"
  - The accuracy decay essay (https://www.getdot.ai/blog/your-ai-analyst-will-be-worse-next-month), beside its re-test routine, anchor "how to evaluate AI data analyst accuracy"
queries:
  - ai data analyst
  - how to evaluate ai data analyst accuracy
  - ai data analyst accuracy
  - text to sql accuracy
playbook_url: https://www.getdot.ai/blog/ai-data-analyst-playbook
figures: figures/test-ai-analyst-before-rollout-figures.csv
dataset: "No new run. The steps cite two earlier runs of ours on the Olist public e-commerce dataset (orders and order items tables): piece A's run (runs/ai-analyst-follow-up-questions-run.md) and piece 2's archived run (runs/ai-analyst-shows-sql-run.md). Licence CC BY-NC-SA 4.0 (facts A10, an Assumption, unverified at source); publication decision L4, a decision and not a resolution. Census figures come from the publications in piece B's census, re-read 1 November 2026."
---

**To test an AI data analyst before rollout, ask real questions with every right answer written down first. Ask each test question twice, in fresh chats: in our run on Dot, one question returned 2,878 and 2,453, each correct under its own definition. Then read the SQL behind every answer. By the end, you'll have eight steps, and the one thing no evidence settles yet: the bar to pass.**

On 31 October 2026, in our repeat-question run, we asked Dot "How many orders were delivered late in 2017?" in two fresh chats, worded identically. One answer counted late as "meaning delivery occurred after the estimated delivery timestamp". The other counted late as "meaning they arrived after the estimated delivery day".

The two counts sit 425 orders apart. Each matches the raw data under the definition its answer stated, and the calendar-day reading was the one we had planned. To a buyer, the same words giving two counts is an inconsistency, and step 3 below is built to catch it. Each answer named its definition in its text, so the gap could be seen.

**The whole guide in eight lines:**

1. Collect real questions your team already asked.
2. Write every answer you would accept before you ask.
3. Ask each question twice, each time in a fresh chat.
4. Open the SQL behind every answer, not only the text.
5. Test a follow-up chain, then ask its first question again in a fresh chat.
6. Mark against your written answers; separate display rounding from real disagreement.
7. Decide the bar a result must clear before you see the results.
8. Re-run on a schedule, and whenever something the analyst depends on changes.

## Eight steps test an AI data analyst before rollout, and each says what it rests on

Each step below says what it rests on: a run of ours, a company's own publication, or nothing yet tested. The company practices come from [Dot's census of how 13 companies test their AI analysts](https://www.getdot.ai/blog/how-companies-test-ai-data-analysts).

Both runs of ours used Olist, a public e-commerce dataset, on 31 October 2026. The repeat-question run asked 6 questions, each in 2 fresh chats. The follow-up run asked 8 questions, 5 of them in one follow-up chain.

1. **Collect the questions your team already asked**, from chat threads, tickets and dashboards. Of the 13 companies in [Dot's census](https://www.getdot.ai/blog/how-companies-test-ai-data-analysts), 8 build their test set from real questions or expert ground-truth queries. [LinkedIn collected 133 questions](https://arxiv.org/html/2507.14372v1) across 10 product areas, and [its engineering blog](https://www.linkedin.com/blog/engineering/ai/practical-text-to-sql-for-data-analytics) says domain experts helped define them. That is what these companies do; no publication shows real questions catch more errors than invented ones.
2. **Write down every answer you would accept before you ask**, with its definition: the table, the filter and the date. In both our runs, every expected answer was computed from raw data before the first question, including the second reading an ambiguous phrase allowed. In [our follow-up run](https://www.getdot.ai/blog/ai-analyst-follow-up-questions), 5 answers matched the reading we had planned, and 3 matched only the second reading, by delivery date. Without that reading written down, a test would have marked those 3 correct answers wrong.
3. **Ask each question twice, each time in a fresh chat, and compare.** In our repeat-question run, 5 of 6 questions returned the same value in both chats. The sixth, on late orders, returned 2,878 and 2,453, because each chat defined "late" differently. Two chats per question is what we did; no run of ours shows how many repeats are enough.
4. **Open the SQL behind every answer, not only the text.** In [our follow-up run](https://www.getdot.ai/blog/ai-analyst-follow-up-questions), all 8 answers came back with their SQL. Only 5 of 8 answer texts named the date that set their scope. The SQL of all 8 filtered on a named date column, purchase or delivery. The scope that a text left out could be read in its SQL.
5. **Test a follow-up chain, then ask its first question again in a fresh chat.** In [our follow-up run](https://www.getdot.ai/blog/ai-analyst-follow-up-questions), Dot read the chain's first question, "How many orders were delivered in 2017?", by purchase date. Dot kept that reading across 4 turns, and returned 43,428 again, from the same SQL, when asked for the first figure. A fresh chat, asked in other words about late orders "delivered in 2017", read the phrase by delivery date. Its count sat 691 orders below the chain's: one chain on one dataset, evidence the shift can happen, not why or how often.
6. **Mark each answer against your written answers before trusting an LLM judge, and sort each gap into display rounding or real disagreement.** In our follow-up run, two shares came back as 5.6% and 7.7%: display rounding of exact values, not errors. [Hex built one eval](https://hex.tech/blog/evaluate-data-agents/) where the right answer is 2.04% and a common wrong one is 2.03%. [Hex's LLM judge](https://hex.tech/blog/evaluate-data-agents/) accepted the 2.03% answer 35% of the time. Of the 13 companies in [Dot's census](https://www.getdot.ai/blog/how-companies-test-ai-data-analysts), 7 score answers with an LLM judge.
7. **Decide the bar a result must clear before you see the results.** Deciding it in advance rests on one company's practice, not on a run of ours. [Anthropic](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude) "initially used ~90%" as the threshold a domain's eval slice must clear before launch. Anthropic is the only one of the 13 companies in [Dot's census](https://www.getdot.ai/blog/how-companies-test-ai-data-analysts) to publish a number to clear. The right bar for your team is untested: no run of ours or publication shows what it should be, so this guide sets none.
8. **Re-run the test on a schedule, and whenever something it depends on changes**: a definition, a table, a model. Of the 13 companies in [Dot's census](https://www.getdot.ai/blog/how-companies-test-ai-data-analysts), 5 re-run on a change, before each deploy, or daily. No run of ours re-ran after a change, so this step rests on published practice alone.

## A one-answer test marks right answers wrong when a question has two readings

"Delivered in 2017" can mean bought in 2017, or delivered to the customer in 2017. In [our follow-up run](https://www.getdot.ai/blog/ai-analyst-follow-up-questions), Dot read the phrase by purchase date inside a follow-up chain, and by delivery date in a fresh chat. The two late-order counts sat 691 apart, and each matched the raw data for its own date. That gap is separate from the 425-order gap in our repeat-question run, which came from timestamp against calendar day.

Item by item, 5 of the follow-up run's answers matched the reading we had planned, and 3 matched only the delivery-date reading. A test holding one expected answer per question would have marked those 3 correct answers wrong. A test holding both readings marks them correct, then shows a person which reading each answer took.

[LinkedIn's engineering team reports](https://www.linkedin.com/blog/engineering/ai/practical-text-to-sql-for-data-analytics) that about 60% of its benchmark questions have more than one accepted answer. Without those extra answers, [LinkedIn says](https://www.linkedin.com/blog/engineering/ai/practical-text-to-sql-for-data-analytics) it "underreported recall by 10-15%".

An AI analyst's answer text doesn't always say which reading it took. In our follow-up run, only 5 of 8 answer texts named their date. Every answer in both our runs came back with its SQL, and every query filtered on a named date column. The SQL showed the scope that the text left out.

## A test passed at launch can say little about the same agent a month later

[Anthropic reports](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude) that its offline accuracy drifted from about 95% at launch to about 65% over a month. That was before Anthropic treated drift as an engineering problem. Anthropic's case shows that a test passed at launch can say little about the same agent a month later. [Dot's essay on accuracy decay](https://www.getdot.ai/blog/your-ai-analyst-will-be-worse-next-month) starts from that figure.

A re-run also needs a rule for small swings between runs. [Uber](https://www.uber.com/blog/query-gpt) does "not over-index decisions based on ~5% run-to-run changes in most metrics". No run of ours re-ran after a change, so how often to re-run, and which swing matters, stay untested.

## Things to keep in mind

- **Our runs are small and on one dataset.** Two runs on Olist's public e-commerce data, with conditions recorded by hand, not screenshotted. They show steps 2 to 6 catching something, not how often.
- **The census practices are self-reported.** "8 of 13 do it" means they say they do it; no publication shows its method beats another.
- **Two things this guide doesn't set: how many questions, and what bar.** No run of ours tested either, and only one of the 13 companies published a bar.

## Where Dot fits

[Dot answers data questions for your team.](https://www.getdot.ai/blog/conversational-analytics) In [Dot's evaluation](https://docs.getdot.ai/train-dot/evaluation), each test question holds an expected answer, a unit and a tolerance in percent. On 27 October 2026, its details panel showed a verdict such as "Exact match", and the evaluation re-scored on save without a re-run. Assumption: it always re-scores when a question is saved.

More in the [AI Data Analyst Playbook](https://www.getdot.ai/blog/ai-data-analyst-playbook).

---

Pick the questions your team asked last month, and write down every answer you would accept for each, before you ask your AI analyst anything.

*If this excites you, we'd love to hear from you. Get in touch.*
