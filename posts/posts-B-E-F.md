# Posts B, E and F

Made in the Claude Project (prompts/07-linkedin.md), 28 October 2026, then checked against the run logs.

## Post B · piece 1 · the checklist

Four things decide what an AI analyst's accuracy score means: the number, the unit, the population, the date range. If you are picking a tool on that score, it may have checked only one.

We ran a 20-question accuracy evaluation in Dot. It scored 100%, and passed an answer that didn't match its own expected value.

Average order value came back 137.04 against an expected 137.75. That is 0.52% off, inside a 3% tolerance, on a row with no unit set.

Both numbers were right. A context note counted delivered orders only; the expected answer counted every order with items.

Then we changed one row's expected currency from BRL to USD. The score dropped to 95% on save.

The piece gives you the twenty questions, the row that passed, and the one-row fix. Link in the first comment.

**First comment:** https://www.getdot.ai/blog/test-ai-data-analyst-accuracy?utm_source=linkedin&utm_medium=social&utm_campaign=content-machine&utm_content=post-b

**Image:** charts/piece-1-tolerance-band.png. Caption: "Evaluation run and a chat answer, 27 October 2026." The evaluation run's mode was not recorded, so no mode is stated.

## Post E · piece 3 · arithmetic first

5.8 credits, ten correct answers: about 0.58 credits per correct answer. A seat costs the same at four questions a month or four hundred.

Economy mode saved nothing here. The mostly-Balanced batch used 5.3 credits; the all-Economy batch used 5.8.

Same ten questions, each in a fresh chat, run twice in Dot. Credits read in Billing before and after each batch. Ten of ten correct, both times.

One run per mode, so that is a reading, not a verdict.

Assumption, not confirmed by Dot: 1 credit ≈ $1, so roughly $0.58 an answer. On the free tier, 100 credits covers about 170 answers like these.

The piece gives you the ten questions, both batch readings, and the method to meter your own. Link in the first comment.

**First comment:** https://www.getdot.ai/blog/ai-data-analyst-cost-per-question?utm_source=linkedin&utm_medium=social&utm_campaign=content-machine&utm_content=post-e

**Image:** charts/piece-3-cost-by-mode.png (credits per batch). Caption carries the date and the mode per batch.

## Post F · piece 3 · the list

Before you compare two AI analysts on price, check four things.

On ten simple questions in Dot, Economy used 5.8 credits; a mostly-Balanced batch used 5.3.

1. The mode. Economy didn't use fewer credits than Balanced here.
2. The definition of correct. Four of twenty answers were scoped to delivered orders by a context note. Each said so in its reply. Scored against all orders, they would read as wrong.
3. The meter. Billing reads to 0.1 credits, so compare batch totals, not single questions.
4. The questions. These were simple single-number asks; harder ones may cost more, and we didn't measure that.

The piece gives you both batches, the ten questions, and what to check before you compare two tools on price. Link in the first comment.

**First comment:** https://www.getdot.ai/blog/ai-data-analyst-cost-per-question?utm_source=linkedin&utm_medium=social&utm_campaign=content-machine&utm_content=post-f

**Image:** a crop of piece 3's ten-question table, so it differs from post E's chart.

## Before posting

- Both piece URLs must be live and opened by `verify_sources.py`.
- Post A (piece 1) is in the Day 1 file; posts C and D are in posts/piece-2-posts.md.
