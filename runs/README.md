# runs

One file per piece, holding every Dot answer word for word under its question, with the time: runs/piece-4-run.md, and so on. Quotes in a piece come from here, never from memory.

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
