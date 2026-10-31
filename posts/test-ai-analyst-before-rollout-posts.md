# test-ai-analyst-before-rollout · LinkedIn posts

Structures from PLAN.md's cluster table: structure 5, the checklist (Post A); structure 4, the contrarian read (Post B). Line 1 of each post is Saurabh's.

## Post A · test-ai-analyst-before-rollout · the checklist (cluster structure 5)

**First lines tried:** (Saurabh, 1 November 2026)
- Most advice on testing an AI analyst stops at 'build a golden set'. Here's what the companies that published theirs actually do.
- Eight steps, each with the evidence behind it.
- Nobody can tell you what accuracy score is good enough. Thirteen companies published how they test anyway. (kept)

Nobody can tell you what accuracy score is good enough. Thirteen companies published how they test anyway.

Eight steps to test an AI data analyst before rollout, each with its evidence:

1. Collect real questions your team already asked.
2. Write every answer you would accept before you ask.
3. Ask each question twice, in fresh chats. In our run on Dot, one returned 2,878 and 2,453.
4. Open the SQL behind every answer.
5. Test a follow-up chain, then ask one of its questions again, in full, in a fresh chat.
6. Mark against your written answers before trusting an LLM judge.
7. Decide the bar first. Anthropic started at ~90%; our Playbook suggests ~80%.
8. Re-run on a schedule. Dot's guidance: twenty minutes a week, one named owner.

The piece gives the evidence behind each step: a run of ours on Dot, or companies' own publications.

**First comment:** The eight steps, with the evidence behind each: https://www.getdot.ai/blog/test-ai-analyst-before-rollout?utm_source=linkedin&utm_medium=social&utm_campaign=content-machine&utm_content=f-post-a

**Image:** none from the piece. Optional: the eight steps as a card, captioned "How to test an AI data analyst before rollout. Dot, 1 November 2026."

## Post B · test-ai-analyst-before-rollout · the contrarian read (cluster structure 4)

**Source:** F's step 2 and its second section: our follow-up run (RA-OTHER, RA-F01) and LinkedIn (LIN-3, LIN-4). Angle chosen by Saurabh, 1 November 2026: "One expected answer per question marks right answers wrong."

**First lines tried:** (Saurabh, 1 November 2026)
- If your test holds one right answer per question, it will mark correct answers wrong. Ours would have.
- The standard advice on testing AI analysts is wrong, and our own run proves it.
- Your golden set is marking correct answers wrong. (kept)

Your golden set is marking correct answers wrong.

The standard advice for testing an AI analyst: build a golden set, one right answer per question.

In our run on Dot, that would have marked 3 of 8 correct answers wrong.

"Delivered in 2017" has two readings: bought in 2017, or delivered in 2017. Dot used each in a different chat, and both matched the raw data.

LinkedIn found the same at scale. About 60% of its benchmark questions have more than one accepted answer, and without them it underreported recall by 10-15%.

So write down every answer you would accept, with its definition, before you ask.

The piece has all eight steps of the test, with the evidence behind each.

**First comment:** The eight-step test, with the evidence behind each step: https://www.getdot.ai/blog/test-ai-analyst-before-rollout?utm_source=linkedin&utm_medium=social&utm_campaign=content-machine&utm_content=f-post-b

**Image:** none from the piece.
