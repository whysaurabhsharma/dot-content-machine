# Stage 5 · FACT-CHECK

Two passes, then the link check. Tested on piece 1, 27 October 2026: the first pass returned 60 items, 51 of them problems.

## Pass 1: a fresh chat, the draft only

Runs in this repo as the blind `fact-checker` agent (`.claude/agents/fact-checker.md`), which also gets the figures file and the run file, started with the fixed sentence in `runs/README.md#reviewers`. Pass 2 stays on a different model.

You are fact-checking a draft blog post before publication. You have no other context. Return only a numbered list:

1. Every number in the draft, and whether it is internally consistent with the other numbers in the draft. Check all arithmetic yourself.
2. Every claim about what a product does, marked VERIFIABLE (the draft shows evidence) or ASSERTED (the draft states it without evidence).
3. Any sentence where the conclusion goes further than the evidence shown.
4. Any quote presented as something the product said: is it presented consistently?

Do not rewrite anything. Do not praise anything. Only list problems.

{paste the draft}

## Pass 2: a different model

Paste the same prompt and draft into a different model (ChatGPT or Gemini). The same model family can share blind spots.

## Pass 3: the links

    python scripts/verify_sources.py pieces/<piece>.md

## Then

Triage every item: fix it, or write one line on why it stands. Log every fix in the Run Log with its cause. When the same kind of mistake appears in two pieces, add a rule to CLAUDE.md with a dated origin.
