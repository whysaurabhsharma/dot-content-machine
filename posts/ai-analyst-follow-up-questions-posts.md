# ai-analyst-follow-up-questions · LinkedIn posts

## Post A · ai-analyst-follow-up-questions · the checklist

**Relabelled:** 1 November 2026, to the cluster table (PLAN.md, "LinkedIn: six posts, six structures"). This post's shape is the checklist, structure 5, which the table gives to F. A's two posts in the table are structure 2 (Post B below) and structure 6 (Post C below). So this is a seventh post, outside the six: keep it as an extra, or retire it (Saurabh's call). It is not rewritten.

**First lines tried:**
- Before you trust an AI analyst's follow-up answers, check which date it used.
- "Delivered in 2017" gave Dot two correct late-order counts, 691 orders apart.
- If you're rolling out an AI analyst, the risk isn't a wrong number. It's a right number for a date you didn't mean. (kept: it names the reader and the stake; the number follows on line 2)

If you're rolling out an AI analyst, the risk isn't a wrong number. It's a right number for a date you didn't mean.

We asked Dot how many "delivered in 2017" orders were late. After earlier questions in the same chat, it said 2,453. In a fresh chat, 1,762.

Both match the raw Olist data. The first chat used purchase date; the fresh chat used delivery date. They sit 691 orders apart.

The first four of the test's six steps:
1. Pick a phrase your team reads two ways.
2. Compute both readings from the raw tables first.
3. In one chat, ask five chained questions.
4. Ask one again, in full, in a fresh chat.

Then check whether each answer names its date; if not, read its SQL. Dot returned its SQL with all 8 answers here.

The piece has all six steps and the SQL line that showed the date.

**First comment:** The six-step follow-up test and the SQL behind both counts: https://www.getdot.ai/blog/ai-analyst-follow-up-questions?utm_source=linkedin&utm_medium=social&utm_campaign=content-machine&utm_content=post-a

**Image:** charts/ai-analyst-follow-up-questions-late-orders.png, the piece's bar chart of the two late-order counts. Caption: "Late orders for "delivered in 2017", asked inside a follow-up chain and in a fresh chat. Olist dataset, Dot, 31 October 2026. The run's mode is not stated."

## Post B · ai-analyst-follow-up-questions · the transcript (cluster structure 2)

**Source:** `runs/ai-analyst-follow-up-questions-run.md`, Q2 and Q6. Dot's answer is quoted word for word; the run file shows a space before its comma and full stop (the export's spacing), removed here.

**First lines tried:** left for Saurabh.

**Line 1:** _to be written by Saurabh: who this is for and what is at risk for them._

We asked Dot a follow-up in one chat, "And how many of those were delivered late?" Its answer, word for word:

"2,453 orders were delivered late (5.6%), meaning delivery occurred after the estimated delivery day. Two orders lack delivery dates and could not be assessed."

Nothing in it is wrong; the number matches the raw data. But it doesn't say which 2017: orders bought then, or delivered then.

Its SQL said purchase date. Asked in full in a fresh chat, Dot read delivery date and returned 1,762.

Two right answers, 691 apart, and only the SQL said which.

The piece shows the SQL line that settled it, and a six-step test for your own team.

**First comment:** The six-step follow-up test and the SQL behind both counts: https://www.getdot.ai/blog/ai-analyst-follow-up-questions?utm_source=linkedin&utm_medium=social&utm_campaign=content-machine&utm_content=a-post-b

**Image:** charts/ai-analyst-follow-up-questions-late-orders.png, the piece's bar chart of the two counts.

## Post C · ai-analyst-follow-up-questions · the build log (cluster structure 6)

**Source:** `runs/ai-analyst-follow-up-questions-timing.csv` (figures TIM-1, TIM-2). No credits figure: the screenshot rule was waived for A's run.

**First lines tried:** left for Saurabh.

**Line 1:** _to be written by Saurabh: who this is for and what is at risk for them._

We ran a content piece through a machine that logs every stage. Asking Dot the 8 test questions took 5.1 minutes.

What changed: before the first question, we computed every expected answer from the raw data, including both readings of "delivered in 2017".

What happened: a follow-up chain read the phrase by purchase date. A fresh chat read it by delivery date. The counts sat 691 apart, and both matched the data.

The number: 26.9 logged minutes, research to export.

What that number leaves out is a person's time. The decisions, the headline tests and the phone reads were people's, and they were where the piece got better.

The piece has the six-step test and the SQL behind both counts.

**First comment:** The six-step follow-up test, and how the run was set up: https://www.getdot.ai/blog/ai-analyst-follow-up-questions?utm_source=linkedin&utm_medium=social&utm_campaign=content-machine&utm_content=a-post-c

**Image:** none from the piece. Optional: a table of the logged stages, captioned "Logged machine minutes per stage, piece A, 31 October 2026."
