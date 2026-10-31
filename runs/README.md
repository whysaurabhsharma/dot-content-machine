# runs

One file per piece, holding every Dot answer word for word under its question, with the time: runs/piece-4-run.md, and so on. Quotes in a piece come from here, never from memory.

The format of a run file is defined in [facts/run-format.md](../facts/run-format.md). The `dot-runner` subagent writes it; check 16 and `mark_run.py` read it.

## Screenshots

Mode, credits, environment and active context notes are not observable via MCP ([facts/dot-mcp.md](../facts/dot-mcp.md)), so each is screenshotted in Dot's own UI and saved as:

    runs/screenshots/<piece>-batch-<n>-{mode,credits-before,credits-after,environment,notes}.png

| Suffix | Taken when | Where in Dot | Rule |
|---|---|---|---|
| `mode` | Start of the batch, before the first question | Chat composer, mode selector | 14 |
| `credits-before` | Start of the batch, before the first question | Settings → Billing | 15 |
| `credits-after` | End of the batch, after the last answer | Settings → Billing | 15 |
| `environment` | Start of the batch | Sidebar, environment menu | 17 |
| `notes` | Start of the batch | Model → Notes, showing which are on | 17 |

Every run file references the path of each screenshot it depends on, next to the batch it belongs to. A batch without its five paths has no recorded conditions.

A rehearsal may record a batch's conditions as text, by hand, instead of screenshots, and must say so in its conditions block. A piece intended for publication must have all five screenshots for every batch.

Screenshots show the account holder's name and email. That is fine for internal evidence. A screenshot used in a published piece must have personal details removed first.

## Batches

`dot-runner` has a limit of 60 turns, and each question takes about four. So a run is split into batches.

- A batch is as many questions as fit in one `dot-runner` call, in the order of the research file's test questions.
- Batches are numbered from 1 within a piece and never renumbered. The next call picks up at the first question not yet recorded.
- Each batch gets its own five screenshots, named per the scheme above with its own `<n>`. The `credits-after` of batch 1 doesn't stand in for the `credits-before` of batch 2: take both.

## Timing

Every step logs its start and end with `scripts/timing.py` to `runs/<piece>-timing.csv`, using exactly these stage names. `timing.py` rejects any other name; add a new one here and in its `STAGES` list together.

| Stage | Covers | Who logs it |
|---|---|---|
| `research` | The researcher: inputs fetched to `runs/<piece>-research.md` written | The caller of the `researcher` agent, or its skill |
| `truth` | Writing `specs/<piece>-truth.json` and running `ground_truth_from_spec.py` | The person or skill doing it |
| `run` | One batch of Dot questions: just before the first question to the moment the last answer returns | The `dot-runner` itself, once per batch. Its writing time after the last answer is not counted |
| `mark` | `mark_run.py` on the run, including any fix needed before it marks correctly | The person or skill doing it |
| `findings` | Recording the observed findings in the run file | The person or skill doing it |
| `outline` | `/outline`: the outline written to `pieces/<slug>-outline.md` | The `/outline` skill |
| `draft` | `/draft`: the piece written to `pieces/<slug>.md` | The `/draft` skill |
| `seo-geo` | `/seo-geo`: SEO fields, links and FAQ schema | The `/seo-geo` skill |
| `linkedin` | `/linkedin`: one post appended to `posts/<slug>-posts.md` | The `/linkedin` skill |
| `export` | `/export`: the files in `exports/<slug>/` | The `/export` skill |

The `note` column says how each row was made: `logged` (written by `timing.py` at the time), `backfilled` (added later from a timestamp in the record, with its source named), or `not logged` (no evidence; no time is estimated).

## Reviewers

The three blind reviewers (`.claude/agents/reader.md`, `fact-checker.md`, `lift-tester.md`) start without CLAUDE.md, can read only their allowlist (`scripts/hooks/read_allowlist.py`), and read a body-only copy of the piece. Make the copy first, and again after every edit:

    python scripts/review_copy.py <slug>

Start a reviewer only with the launcher, which makes the copy, starts a headless session with no MCP servers, passes the fixed sentence and saves the report:

    python scripts/run_reviewer.py <reader|fact-checker|lift-tester> <slug>

Don't start a reviewer with the Agent tool from an interactive session: every connected MCP server's instructions, including ask_dot's description of Dot, would reach it (`facts/reviewer-blindness.md`, B4). The launcher passes exactly the sentence below, with the slug filled in and nothing else: no rules, no context, no hints about what to look for.

| Reviewer | The fixed sentence |
|---|---|
| `reader` | Read reviews/<slug>/draft.md and give your report. |
| `fact-checker` | Fact-check reviews/<slug>/draft.md against figures/<slug>-figures.csv and runs/<slug>-run.md. |
| `lift-tester` | Read reviews/<slug>/draft.md as an answer engine and report what you would and would not lift. |

Save each report as `reviews/<slug>/<reviewer>.md`. What still reaches a reviewer despite all this is recorded in `facts/reviewer-blindness.md`.

