---
name: seo-geo
description: Sets a drafted piece's SEO title, meta, slug, internal and reverse links, and FAQ schema where earned, against the Ahrefs snapshot and the link inventory. Edits only front matter and link markup. Started by a person or by the piece workflow, in the order stage_gate.py allows.
argument-hint: <piece-slug>
allowed-tools: Read, Edit, Write, Glob, Grep, Bash(python scripts/timing.py:*), Bash(python -I scripts/timing.py:*), Bash(python scripts/verify_sources.py:*), Bash(python -I scripts/verify_sources.py:*), Bash(python scripts/check_piece.py:*), Bash(python -I scripts/check_piece.py:*)
---

# SEO and GEO

**Why this skill has no `disable-model-invocation` flag (removed 31 October 2026).** It had the flag so that only a person could start a stage. A workflow's agents count as the model, so the flag also stopped `.claude/workflows/piece.js` from running this stage, and told its agents not to follow this file by any other route. The protection moved rather than vanished: `scripts/stage_gate.py` now enforces it. It refuses a stage out of order, never redoes a finished stage, and holds every decision gate (the question, the outline approval, the title and human checks, publishing) until a person has recorded it in the files. The workflow starts every run from the gate and obeys it.

No source prompt. Built from CLAUDE.md style rules 13 and 15, gate checks 3, 20 and 21, and `facts/house-structure-and-links.md`. Runs after `/draft`, before the blind reviewers.

**The piece:** the first word of `$ARGUMENTS` is the slug.

## Timing

First action: `python scripts/timing.py <slug> seo-geo start`. Last action: `python scripts/timing.py <slug> seo-geo end`. Stage names: `runs/README.md#timing`.

## Inputs

- `pieces/<slug>.md`: the drafted piece.
- `runs/<slug>-research.md`: section 2 (the words buyers type) and section 4 (Sources).
- `data/ahrefs/keywords.csv` and `data/ahrefs/search-console-queries.csv`: the frozen Ahrefs snapshot.
- `facts/house-structure-and-links.md`: the internal-link inventory.
- `bank/questions.csv`: buyer questions, for the FAQ test.

## Output

1. **Front matter of `pieces/<slug>.md`:**
   - `seo_title`: contains the query, 60 characters or fewer.
   - `meta`: 155 characters or fewer.
   - `slug`: four to six words.
   - `reverse_links`: three, each with its anchor text.
   The query is the buyer phrase from the research file that best matches what the piece delivers. Give its volume and difficulty as `keywords.csv` displays them (1.2K, not 1200), dated "Ahrefs, 27–28 October 2026". A phrase not in the file is "not measured"; `not indexed` is not zero. Never estimate a volume.
2. **Internal links in the body:** five or more, including the Playbook stage (`playbook_url`). Each goes on words already in the piece: wrap them in a link, and change no other character.
3. **`pieces/<slug>-faq.json`, only where earned.** It is earned when the piece itself answers two or more distinct buyer questions from the research file or `bank/questions.csv`. Each answer is a sentence or two copied word for word from the piece. If not earned, write no file and say why.

## Check

Run `python scripts/verify_sources.py pieces/<slug>.md`. Remove any link it can't open, and say which. Then run `python scripts/check_piece.py pieces/<slug>.md` and report checks 3, 20 and 21.

## Must not

- Change a claim, a number, a quote or any sentence's wording. Only front matter and link markup change.
- Change the H1 `title`. That is Decision 3, a person's.
- Link to a URL that `verify_sources.py` hasn't opened, or that isn't in the link inventory, without saying so.
- Write an FAQ answer in new words.
- Estimate a search volume, or present Ahrefs figures as current.
