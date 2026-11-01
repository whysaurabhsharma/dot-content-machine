# Archive: the earlier Claude Project trial

Everything here came from the earlier trial, run 27–29 October 2026 in a Claude Project, before the machine moved to Claude Code. It is **superseded** and is **not part of this submission**. It is kept, not deleted, so the change log in `CLAUDE.md` can still point at what happened.

| Path | What it was |
|---|---|
| `pieces/piece-1.md`, `piece-2.md`, `piece-3.md` | The trial's three pieces (slugs `test-ai-data-analyst-accuracy`, `ai-analyst-ad-hoc-requests`, `ai-data-analyst-cost-per-question`) |
| `figures/piece-1-figures.csv` … `piece-3-figures.csv`, `piece-1-truth.csv`, `ground-truth.csv` | Their Figures rows and ground truth |
| `specs/piece-1-truth.json` | Piece 1's evaluation questions as a truth spec |
| `charts/piece-1-*`, `piece-2-*`, `piece-3-*` | Their charts, specs and alt text |
| `posts/post-A.md`, `piece-2-posts.md`, `posts-B-E-F.md` | Their six LinkedIn posts |
| `reviews/piece-3/` | Piece 3's blind reviews |
| `exports/ai-data-analyst-cost-per-question/` | Piece 3's export (local only: `archive/exports/` is gitignored; the three current exports in `exports/` are committed) |

The paths inside these files still point to their old locations (`figures/piece-1-figures.csv` and so on), so `check_piece.py` will not find their figures from here. Hard rule 4 still applies: no finding from these files may appear in a current piece unless it recurs in that piece's own run.

Moved here 31 October 2026, on Saurabh's instruction.

## Archived 31 October 2026: this submission's first piece 2 and piece 3

Not part of the submission. Saurabh chose a different set of three pieces (see `PLAN.md`).

| Path | What it was |
|---|---|
| `pieces/ai-analyst-shows-sql.md`, `ai-analyst-shows-sql-outline.md` | Piece 2 as research, working title "Your AI Analyst Counted Late Orders Two Ways" (bank #41): outline approved, drafted, reviewed and revised, then dropped for being a second test-result piece |
| `reviews/ai-analyst-shows-sql/` | Its blind reviews, revisions, lift lines and human-checks file |
| `charts/ai-analyst-shows-sql-late-orders.*` | Its chart |
| `runs/ai-analyst-how-much-context-*`, `specs/ai-analyst-how-much-context-truth.json`, `figures/ai-analyst-how-much-context-truth.csv` | Piece 3 as planned (bank #47): Decision 1, research and a truth spec; never run |

**Kept outside the archive, as evidence:** piece 2's run, `runs/ai-analyst-shows-sql-run.md`, with its figures, truth file, spec, research, manifest and timing. The guide `test-ai-analyst-before-rollout` may cite it.
