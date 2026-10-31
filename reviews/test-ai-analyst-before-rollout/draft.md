# How to Test an AI Data Analyst Before Rollout: 8 Steps

**To test an AI data analyst before rollout, ask real questions with every right answer written down first. Then ask each one twice, in fresh chats, worded identically. In our run on Dot, one question returned 2,878 late orders counting by the exact delivery timestamp, and 2,453 counting by the delivery day. By the end, you'll have eight steps, and the two published bars to set yours against: about 90% and about 80%.**

**The whole guide in eight lines:**

1. Collect real questions your team already asked.
2. Write every answer you would accept before you ask.
3. Ask each question twice, each time in a fresh chat.
4. Open the SQL behind every answer, not only the text.
5. Test a follow-up chain, then ask one of its questions again, in full, in a fresh chat.
6. Mark against your written answers; separate display rounding from real disagreement.
7. Decide the bar a result must clear before you see the results.
8. Re-run on a schedule, and whenever something the analyst depends on changes.

## Eight steps test an AI data analyst before rollout, and each names its evidence

Each step ends with its evidence: a run of ours, a count from [Dot's census of 13 companies](https://www.getdot.ai/blog/how-companies-test-ai-data-analysts), or none yet. Both runs of ours used Olist, a public e-commerce dataset, on 31 October 2026. The repeat-question run asked 6 questions, each in 2 fresh chats; the follow-up run asked 8, 5 of them in one chain.

1. **Collect the questions your team already asked**, from chat threads, tickets and dashboards. [LinkedIn](https://www.linkedin.com/blog/engineering/ai/practical-text-to-sql-for-data-analytics) asked domain experts in 10 product areas for over 130 questions, each with a ground-truth query. Of the 13 companies in Dot's census, 8 build their test set from real questions or expert ground-truth queries. *Evidence: 8 of 13 companies.*
2. **Write down every answer you would accept before you ask**, with its definition: the table, the filter and the date. In [our follow-up run](https://www.getdot.ai/blog/ai-analyst-follow-up-questions), "delivered in 2017" allowed two readings, and we computed both before the first question. Of 8 answers, 5 matched the reading we had planned and 3 matched only the delivery-date reading. One expected answer per question would have marked those 3 correct answers wrong. *Evidence: our run.*
3. **Ask each question twice, each time in a fresh chat, worded identically, and compare.** In our repeat-question run, 5 of 6 questions matched across chats, but "How many orders were delivered late in 2017?" did not. Both answers counted orders placed in 2017. One counted late as "delivery occurred after the estimated delivery timestamp" and the other as "they arrived after the estimated delivery day". *Evidence: our run.*
4. **Open the SQL behind every answer, not only the text.** In our follow-up run, all 8 answers came back with their SQL. Only 5 of 8 answer texts named the date that set their scope. Every query filtered on a named date column, so the SQL showed what the text left out. *Evidence: our run.*
5. **Test a follow-up chain, then ask one of its questions again, in full, in a fresh chat.** In our follow-up run, Dot read the chain's first question by purchase date and kept that reading for 4 turns. Asked about late orders "delivered in 2017" in full in a fresh chat, it read the phrase by delivery date. Its count sat 691 below the chain's. *Evidence: our run, one chain.*
6. **Mark each answer against your written answers before trusting an LLM judge, and sort each gap into display rounding or real disagreement.** In our follow-up run, Dot gave the late share as 5.6% for 2017 and 7.7% for 2018, each our computed share rounded for display. [Hex](https://hex.tech/blog/evaluate-data-agents/) built one eval where the right answer is 2.04% and a common wrong one is 2.03%. Its LLM judge accepted the wrong one 35% of the time. *Evidence: our run; Hex's published eval; 7 of 13 companies in Dot's census use an LLM judge.*
7. **Decide the bar a result must clear before you see the results.** [Anthropic](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude) "initially used ~90%" as the threshold a domain's eval slice must clear before launch. [Our Playbook](https://www.getdot.ai/blog/ai-data-analyst-playbook) suggests about 80%: "Hold access until the tests pass your bar (~80%)". No published evidence settles which is right for your team, so write yours down before the first run. *Evidence: one company, and our Playbook.*
8. **Re-run the test on a schedule, and whenever something it depends on changes**: a definition, a table, a model. Of the 13 companies in Dot's census, 5 re-run on a change, before each deploy, or daily. *Evidence: 5 of 13 companies.*

## A one-answer test marks right answers wrong when a question has two readings

A buyer can mean one thing by a question and an AI analyst can read another, with both answers matching the data. [LinkedIn's engineering team reports](https://www.linkedin.com/blog/engineering/ai/practical-text-to-sql-for-data-analytics) that about 60% of its benchmark questions have more than one accepted answer. Without those extra answers, LinkedIn says it "underreported recall by 10-15%".

## Accuracy measured at launch drifted within a month at Anthropic

[Anthropic reports](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude) that its offline accuracy drifted from about 95% at launch to about 65% over a month. That was before Anthropic treated it as an engineering problem. [Dot's essay on accuracy decay](https://www.getdot.ai/blog/your-ai-analyst-will-be-worse-next-month) starts from that figure.

A re-run also needs a rule for small swings between runs. [Uber](https://www.uber.com/blog/query-gpt) does "not over-index decisions based on ~5% run-to-run changes in most metrics".

## Things to keep in mind

- **Our runs are small and on one dataset.** Two runs on Olist's public e-commerce data. They show steps 2 to 6 catching something, not how often.
- **The census practices are self-reported.** "8 of 13 do it" means they say they do it; no publication shows its method beats another.
- **Two things this guide doesn't set: how many questions, and what bar.** No run of ours tested either. Anthropic and our Playbook each name a bar, and no published evidence settles which.

## Where Dot fits

[Dot answers data questions for your team.](https://www.getdot.ai/blog/conversational-analytics) In both our runs, every answer came back with its SQL. [Dot's evaluation](https://docs.getdot.ai/train-dot/evaluation) holds each test question's expected answer, a unit and a tolerance in percent, so steps 2 and 6 live in one place. More in the [AI Data Analyst Playbook](https://www.getdot.ai/blog/ai-data-analyst-playbook).

---

Pick the questions your team asked last month. This week, ask one of them twice, in two fresh chats, and compare.

*If this excites you, we'd love to hear from you. Get in touch.*
