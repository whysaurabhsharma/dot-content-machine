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
