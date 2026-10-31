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

**Each intended line stands alone and is checkable** (CLAUDE.md v1.8.2): it carries a number, or a claim that a figure cited in the piece supports directly; give that figure's ID beside the line.

**Record the lines in `reviews/<slug>/lift-lines.md`** (example: `reviews/ai-analyst-follow-up-questions/lift-lines.md`). Before the test, write the three intended lines under "Intended". After it, add a table of what each tool lifted, verbatim, marked intended or not, and the verdict. A line an engine lifts without being targeted is the strongest evidence a line is liftable: if it is better than an intended line, add it to the list, with that note.

**Known limit of the method (31 October 2026):** Claude may decline to give three verbatim quotes, citing its own limits on verbatim reproduction, and paraphrase the rest. Record how many quotes each tool actually gave; a tool that gave fewer than three hasn't failed the piece, but its partial result counts for less.

**Decision 3 (human):** pick the title from the three candidates.
