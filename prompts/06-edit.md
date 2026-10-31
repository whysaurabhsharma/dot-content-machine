# Stage 6 · EDIT

## 1. The checker

    python scripts/check_piece.py pieces/<piece>.md

Fix every FAIL. HUMAN lines are checked by a person, using the gate list in CLAUDE.md.

## 2. The headline test (human, three seconds)

Show the title and the first 60 words to someone who hasn't seen the piece. Can they say who it is for, what they get, and why to trust it? If not, rewrite the title or the opening.

## 3. The lift test

A first pass runs in this repo as the blind `lift-tester` agent (`.claude/agents/lift-tester.md`). It is the same model family as the writer, so the real lift test in Perplexity and Claude below still runs.

Paste the piece into Perplexity, and separately into Claude, with this line above it:

    Summarise this article in exactly three bullet points. Each bullet must contain one direct quotation from the article, in quotation marks.

Compare the quoted lines with the three you intended to be quoted. Rewrite until the intended lines are lifted, or until the lifted lines are better than the intended ones. Lines that lean on the sentence before them are rarely quoted; give each its own subject.

**Decision 3 (human):** pick the title from the three candidates.
