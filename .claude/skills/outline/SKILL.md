---
name: outline
description: Stage 2 OUTLINE. Writes pieces/<slug>-outline.md from the piece's research, run and figures, for a person to approve (Decision 2). Started by a person or by the piece workflow, in the order stage_gate.py allows.
argument-hint: <piece-slug> [--practice]
allowed-tools: Read, Write, Glob, Grep, Bash(python scripts/timing.py:*), Bash(python -I scripts/timing.py:*)
---

# Stage 2 · OUTLINE

**Why this skill has no `disable-model-invocation` flag (removed 31 October 2026).** It had the flag so that only a person could start a stage. A workflow's agents count as the model, so the flag also stopped `.claude/workflows/piece.js` from running this stage, and told its agents not to follow this file by any other route. The protection moved rather than vanished: `scripts/stage_gate.py` now enforces it. It refuses a stage out of order, never redoes a finished stage, and holds every decision gate (the question, the outline approval, the title and human checks, publishing) until a person has recorded it in the files. The workflow starts every run from the gate and obeys it.

Source: `prompts/02-outline.md`. Run after the evidence run, with its numbers already in the figures file.

**The piece:** the first word of `$ARGUMENTS` is the slug. `--practice` after it is the practice-only override (see "Refuse" below).

## Timing

First action: `python scripts/timing.py <slug> outline start`. Last action, after the output file is written: `python scripts/timing.py <slug> outline end`. Stage names: `runs/README.md#timing`.

## Inputs

Read all of these before writing. If one is missing, stop and say which.

- `CLAUDE.md`: every rule.
- `facts/house-structure-and-links.md`: the anatomy of a piece.
- `facts/dot-facts.md`: Observed, Assumption, Superseded, Confirmed.
- `runs/<slug>-research.md`: the gap chain, the words buyers type, the verdict.
- `runs/<slug>-run.md`: the conditions block of each batch, and the observed findings.
- `figures/<slug>-figures.csv`: every number the piece may use (ID, value, where computed, date).
- `figures/<slug>-truth.csv`: the ground truth those figures were marked against.

## Output

`pieces/<slug>-outline.md`, and nothing else. If it already exists, stop and ask before replacing it.

You are outlining one piece for Dot's blog. Follow CLAUDE.md and facts/house-structure-and-links.md.

**Write the outline in this order:**

1. **Three title candidates.** Formula: the words buyers type, plus what the reader gets, plus proof from the run. Mark one as recommended, with a one-line reason. Use only buyer phrases from the research file's section 2. The final title is Decision 3, a person's.
2. **The opening**, written out in full, 60 words or fewer: the reader's situation, the proof, then "By the end, you will have…".
3. **The surprising detail**, one short paragraph, with a number.
4. **Pocket guide**: five to eight numbered lines.
5. **Three H2s, each a claim.** Under each, the figures IDs that prove it. Pair each limitation with what the product does about it.
6. **The table and the chart**: what each shows, and the chart's alt text and caption (date and mode, from the run's conditions block).
7. **Things to keep in mind**: two to four caveats.
8. **Where Dot fits**: under 80 words. Use only Observed or Confirmed facts, and Assumptions labelled "Assumption", from facts/dot-facts.md, by ID. Never a Superseded one.
9. **The instruction** the reader can act on today.
10. **Missing figures**: every number the outline wanted but the figures file doesn't have. Empty if none.

End the file with these two lines, left blank for the person:

    Approved by:
    Date:

SEO title, meta, slug, internal links and reverse links are not part of the outline. `/seo-geo` sets them after the draft, against search data and the link inventory.

## Refuse

- **Any number that has no row in `figures/<slug>-figures.csv`.** List it under "Missing figures" instead.
- **The rehearsal (hard rule 4).** If the slug is `rehearsal`, or the run file says the run was a rehearsal, rehearsal findings can't appear in a piece. Stop and say so. With `--practice`, go ahead, but put `PRACTICE ONLY: not for publication (hard rule 4)` as the outline's first line.

## Must not

- Write prose beyond the opening and the surprising detail.
- Invent, round or recompute a number. Use the figures file's values; display rounding is stated as such.
- Fill in "Approved by" or "Date". Decision 2 is a person's.
- Edit the research, run, figures or truth files.
