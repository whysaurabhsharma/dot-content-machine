# Piece 2 · LinkedIn posts C and D

Made in the Claude Project (prompts/07-linkedin.md), 28 October 2026, then checked against the run log.

## Post C · caveat first · 134 words

Before anyone tells your data team an AI analyst can take the Slack queue, here are the conditions we ran under.

29 ad hoc questions, each in a fresh chat, no follow-up help. The outcomes: 25 answered, 3 asked a question back, 1 refused with an offer, 0 needed an analyst.

The questions were ours, not a real Slack queue, so this is an "after" with no "before". One public dataset, Brazilian e-commerce, 2016–2018, with two context notes active. The mode drifted from Economy to Balanced at request 22, noticed after the fact. We rebuilt all 25 numbers from the raw data by script, and they matched.

The piece gives you all 29 questions, the four outcomes, and the first check to run on any Dot answer. Does it say what it counted?

**First comment:** The run, question by question: https://getdot.ai/blog/ai-analyst-ad-hoc-requests?utm_source=linkedin&utm_medium=social&utm_campaign=content-machine&utm_content=post-c

**Image:** charts/piece-2-outcomes.png. Caption: "29 ad hoc requests, 27 October 2026. Economy for requests 1–21, Balanced for 22–29."

## Post D · one case in full

If ad hoc questions land on your data team, the risk isn't a wrong number. It's a zero that looks right.

We asked Dot what revenue was last year. It returned BRL 0, and in the same reply called it "a data-coverage limit, not evidence of zero business activity."

The dataset ends in October 2018, so there was nothing to find. Dot offered the latest twelve months instead. Across 29 fresh chats, 22 of the 26 replies that returned a result stated their basis without being asked.

A number without its basis is the one your team will quote in a meeting.

The piece gives you all 29 questions, the four outcomes, and the first check to run on any Dot answer. Does it say what it counted?

**First comment:** All 29 questions and what came back: https://getdot.ai/blog/ai-analyst-ad-hoc-requests?utm_source=linkedin&utm_medium=social&utm_campaign=content-machine&utm_content=post-d

**Image:** the chat reply to the revenue question, cropped to the BRL 0 line and the coverage-limit sentence. Caption: "Last-year revenue, fresh chat, 27 October 2026, Economy mode."

## Before posting

- The piece URL must be live and opened by `verify_sources.py`.
- Voice is Rick's: "we" means Dot (decision D1, 28 October 2026).
