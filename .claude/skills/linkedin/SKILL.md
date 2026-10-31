---
name: linkedin
description: Stage 7 LINKEDIN. Appends one post cut from the piece to posts/<slug>-posts.md, using an opening structure not yet used for that piece, then checks it. Never posts to LinkedIn. Started by a person or by the piece workflow, in the order stage_gate.py allows.
argument-hint: <piece-slug>
allowed-tools: Read, Edit, Write, Glob, Grep, Bash(python scripts/timing.py:*), Bash(python -I scripts/timing.py:*), Bash(python scripts/check_piece.py:*), Bash(python -I scripts/check_piece.py:*)
---

# Stage 7 · LINKEDIN

**Why this skill has no `disable-model-invocation` flag (removed 31 October 2026).** It had the flag so that only a person could start a stage. A workflow's agents count as the model, so the flag also stopped `.claude/workflows/piece.js` from running this stage, and told its agents not to follow this file by any other route. The protection moved rather than vanished: `scripts/stage_gate.py` now enforces it. It refuses a stage out of order, never redoes a finished stage, and holds every decision gate (the question, the outline approval, the title and human checks, publishing) until a person has recorded it in the files. The workflow starts every run from the gate and obeys it.

Source: `prompts/07-linkedin.md`.

**The piece:** the first word of `$ARGUMENTS` is the slug.

## Timing

First action: `python scripts/timing.py <slug> linkedin start`. Last action, after the check: `python scripts/timing.py <slug> linkedin end`. Stage names: `runs/README.md#timing`.

## Inputs

- `pieces/<slug>.md`: the piece. Its front matter gives the slug for the link.
- `figures/<slug>-figures.csv`: every number in the post must also be here.
- `posts/<slug>-posts.md`, if it exists: the posts already cut from this piece.
- `CLAUDE.md`: style rule 17 and stage 7.

## Output

One post appended to `posts/<slug>-posts.md` (create the file with `# <slug> · LinkedIn posts` if it doesn't exist). Earlier posts are never edited.

Heading: `## Post <ID> · <slug> · <structure>`. The ID is the next letter not yet used in the file. The structure is the first of these not yet used for this piece: the checklist · caveat first · one case in full · arithmetic first · the list. If all five are used, stop and say so.

Write one LinkedIn post from the piece. Follow CLAUDE.md style rule 17.

- **Line 1, the stake:** who this is for and what is at risk for them.
- **Line 2, the surprising result**, with a number from the piece.
- **The middle:** three or four short lines of proof, one point only.
- **The close:** exactly what the link gives the reader. The link goes in the first comment, with `?utm_source=linkedin&utm_medium=social&utm_campaign=content-machine&utm_content=<post-id>`.
- Under 150 words. No hashtags, no emoji. Name Dot at least once.
- Try three first lines; keep the most specific.

Under the heading, write in this order: `**First lines tried:**` (the three), the post, `**First comment:**` (the link), `**Image:**` (the chart or crop to use, with its caption's date and mode).

## Check

Run `python scripts/check_piece.py --post posts/<slug>-posts.md` and report the new post's result. Fix any FAIL in the new post (only the new post), then run it again.

## Must not

- Use a number that isn't in the piece and the figures file.
- Use a hashtag or an emoji, or put the link in the post body.
- Edit an earlier post, or the piece.
- Post to LinkedIn, or to anywhere else. Publishing is a person's.
