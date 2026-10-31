# ai-analyst-follow-up-questions · LinkedIn posts

## Post A · ai-analyst-follow-up-questions · the checklist

**First lines tried:**
- Before you trust an AI analyst's follow-up answers, check which date it used.
- "Delivered in 2017" gave Dot two correct late-order counts, 691 orders apart.
- If you're rolling out an AI analyst, the risk isn't a wrong number. It's a right number for a date you didn't mean. (kept: it names the reader and the stake; the number follows on line 2)

If you're rolling out an AI analyst, the risk isn't a wrong number. It's a right number for a date you didn't mean.

We asked Dot how many "delivered in 2017" orders were late. Asked after earlier questions in the same chat, it said 2,453. In a fresh chat, 1,762.

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
