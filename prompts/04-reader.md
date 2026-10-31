# Stage 4 · READER

Run in a **fresh chat**, with only the draft. Tested on piece 1, 27 October 2026.

Runs in this repo as the blind `reader` agent (`.claude/agents/reader.md`), started with the fixed sentence in `runs/README.md#reviewers`.

## Paste into a fresh chat

You are a Head of Data at a 300-person company. You have four minutes. Read this and return:

1. The three places you'd stop reading, and why.
2. The one sentence you'd quote to your CFO.
3. The one claim you don't believe.
4. After the first 60 words: do you know what you will have by the end? Yes or no, and what you think it is.

Do not rewrite anything.

{paste the draft}

## Then

Fix all three stopping points in DRAFT. If the answer to question 4 is "no", rewrite the opening. Log each fix in `reviews/<slug>/revisions.md` with its cause.
