---
name: draft
description: Stage 3 DRAFT. Writes pieces/<slug>.md from the approved outline, against CLAUDE.md's style rules. Refuses unless the outline's "Approved by" line is filled. Started by a person or by the piece workflow, in the order stage_gate.py allows.
argument-hint: <piece-slug>
allowed-tools: Read, Write, Glob, Grep, Bash(python scripts/timing.py:*), Bash(python -I scripts/timing.py:*), Bash(python scripts/check_piece.py:*), Bash(python -I scripts/check_piece.py:*)
---

# Stage 3 · DRAFT

**Why this skill has no `disable-model-invocation` flag (removed 31 October 2026).** It had the flag so that only a person could start a stage. A workflow's agents count as the model, so the flag also stopped `.claude/workflows/piece.js` from running this stage, and told its agents not to follow this file by any other route. The protection moved rather than vanished: `scripts/stage_gate.py` now enforces it. It refuses a stage out of order, never redoes a finished stage, and holds every decision gate (the question, the outline approval, the title and human checks, publishing) until a person has recorded it in the files. The workflow starts every run from the gate and obeys it.

Source: `prompts/03-draft.md`.

**The piece:** the first word of `$ARGUMENTS` is the slug.

## Timing

First action: `python scripts/timing.py <slug> draft start`. Last action, after the check below: `python scripts/timing.py <slug> draft end`. Stage names: `runs/README.md#timing`.

## Gate: Decision 2

Read `pieces/<slug>-outline.md` first. If its `Approved by:` line or its `Date:` line is empty, stop. Say that the outline needs a person's approval (Decision 2), and write nothing. Log `draft end` anyway, so the attempt shows in the timing file.

If the outline's first line is `PRACTICE ONLY`, keep that line as the first line of the piece's body.

## Inputs

- `pieces/<slug>-outline.md`: the approved outline.
- `CLAUDE.md`: the style rules.
- `figures/<slug>-figures.csv`: the only source of numbers.
- `facts/dot-facts.md`: the only source of product statements.
- `runs/<slug>-run.md`: the only source of Dot quotes, each with its question and chat link.

## Output

`pieces/<slug>.md`, and nothing else. If it already exists, stop and ask before replacing it.

Write the piece from the approved outline. Follow CLAUDE.md's style rules exactly.

- 900–1,300 words. Sentences average under 18 words; none over 25. No paragraph over four sentences.
- Open with the outline's opening, in bold. Then the surprising detail, then the pocket guide.
- Every H2 is a claim. Follow the shape CLAUDE.md gives the piece's format (style rules 1 and 5): research, method then one table then one chart; teardown, one census table linking each primary source; guide, five to nine numbered steps, each starting with a verb. Put `format:` in the front matter, from `runs/<slug>-piece.json`.
- Every number comes from `figures/<slug>-figures.csv`. Every product statement comes from facts/dot-facts.md: Observed and Confirmed facts stated plainly, Assumptions with the word "Assumption" in the same sentence. Never a Superseded assumption.
- Quotable lines carry their own subject; they must make sense out of context.
- Product quotes are copied word for word from `runs/<slug>-run.md` and name the question and chat they came from (hard rule 13).
- Links on the words that need them; no bracket citations.
- Rick's voice: "we" means Dot (decision D1). Never "I". Quoted questions typed into Dot stay as typed.
- End with the instruction, then: *If this excites you, we'd love to hear from you. Get in touch.*

**Front matter:** `title` (the outline's recommended candidate, until Decision 3), `queries` (from the research file's section 2), `playbook_url`, `figures: figures/<slug>-figures.csv`, `dataset` (from the research file's section 3). Leave `seo_title`, `meta`, `slug` and `reverse_links` out: `/seo-geo` sets them.

## Check

Run `python scripts/check_piece.py pieces/<slug>.md` once and report its summary line and every FAIL. Don't loop to fix them; fixing is EDIT's job. Checks 3, 20 and 21 will fail until `/seo-geo` has run; say so.

## Must not

- Start without a filled "Approved by" and "Date" in the outline.
- Use a number that isn't in the figures file, or a product statement that isn't in facts/dot-facts.md.
- Paraphrase a Dot quote.
- Edit the outline, the figures file, the run file or facts/.
- Set the final title. Decision 3 is a person's.
