# Dot's MCP: what it exposes

Observed 31 October 2026, about 03:45 IST. Source: check 4 of the [smoke test](../runs/smoke-test.md).

How it was observed: from Claude Code, through the `ask_dot` MCP server over HTTP (`https://app.getdot.ai/ai/mcp`, type `http` in the Claude Code config). `/mcp` reported "Authentication successful. Connected to ask_dot." The observations come from the tool schemas the server publishes, one `ask_dot` answer (chat `c3dfb706-90fe-40a7-8651-af37e09eb083`) and two `get_catalog` calls.

Observed facts only. Anything that couldn't be seen says "not observable via MCP".

## Tools

The server exposes 10 tools. "Reserved" means the tool's own description says it is only for Dot's widget.

| Tool | What it does, per its description | Who calls it |
|---|---|---|
| `ask_dot` | Submits a question, or a follow-up when given a `chat_id`. Returns a `chat_id` at once. Dot writes and runs the SQL in the background. | Callable by us |
| `get_result` | Waits up to `wait_seconds` (0–120, default 50), then returns the answer: text, SQL, data, follow-ups. | Callable by us |
| `get_catalog` | Reads Dot's catalog without running any analysis. With `query`, it searches apps, definitions, tables and past chats. Without one, it gives an overview. | Callable by us |
| `show_app` | Shows a published app live, optionally with filters set or on a tab. | Callable by us |
| `view_app` | Renders an app or a draft in a browser and returns screenshots, plus each card's values as text. | Callable by us |
| `build_app` | Has Dot's app builder make or change an app as a draft. The draft stays unpublished until the user publishes it. | Callable by us |
| `wait` | Pauses for 1–120 seconds. | Callable by us |
| `answer_progress` | Follows a question while Dot works on it. "Never call this to read an answer." | Reserved for Dot's widget |
| `export_table` | Backs the widget's Download buttons: one table, every row, as CSV or Excel. | Reserved for Dot's widget |
| `publish_app` | Backs the widget's Publish button, which supplies `confirm`. "Never call this yourself." | Reserved for Dot's widget |

## Mode

No tool has a parameter for mode, model or effort. `ask_dot` takes only `question`, `chat_id` and `asked_from`, and `asked_from` is described as set by the widget. So the Economy/Balanced selector seen in the Dot chat composer (dot-facts O5) can't be set through the MCP.

The mode the account was in for the 31 October answer: not observable via MCP.

## Model and credits

The `get_result` response contained:

- the answer text
- the SQL
- a data preview
- column statistics
- a CSV download link
- an "Open in Dot" link

It did not name a model or report credits used. No tool returns a credit balance.

- Model used: not observable via MCP.
- Credits used per answer: not observable via MCP.
- Credit balance: not observable via MCP.

## Workspace and context notes

`get_catalog` with no query, header: "Dot Data Catalog: aiinterviewagents.com". Its capabilities line reads "SQL queries, Visualizations, Scheduled reports".

| Item | Observed |
|---|---|
| Connection | `data/aiinterviewagents.com/uploads.db` (duckdb), 1 connection |
| Tables | `uploads.main.olist_orders_dataset`: 8 columns, 99.4K rows. `uploads.main.olist_order_items_dataset`: 7 columns, 112.7K rows. |
| Apps | 1: Sample Executive Dashboard (`_shared__welcome-to-dot-apps`) |
| Links | All answer and chat links point to `app.getdot.ai` |

`get_catalog` with the query "average order value" lists two definitions. The tool truncates their text.

- "Olist dataset currency and monetary formatting"
- "Olist revenue, order value, basket size, cancellation and shipping metrics"

These definitions are observable. Whether a note was active for a given answer is not observable via MCP, and neither is whether the answer used it. The 31 October answer cited no note. The tool also doesn't show which environment the account is in (Production or another): not observable via MCP.

## What this means for the pipeline

A run made only through the MCP can't meet three hard rules. The MCP can still ask the questions. The evidence for these rules has to come from the Dot UI, by a person, and be saved where it can be traced.

| Rule | Why the MCP can't meet it | Human step |
|---|---|---|
| 14. Screenshot the mode selector each batch | No mode parameter. The mode isn't reported. | Before each batch, screenshot the mode selector in Dot's chat composer. |
| 15. Read credits before and after each batch | No balance tool. No credits per answer. | Screenshot Settings → Billing before and after the batch. |
| 17. Every run carries its conditions | Account and connection are observable through `get_catalog`. Environment, mode and active context notes are not. | Screenshot the environment menu, and Model → Notes showing which notes are on. |

The screenshot naming scheme, and the rule that run files reference each path, are in [runs/README.md](../runs/README.md#screenshots). The account and the tables can come from `get_catalog`, so they need no screenshot.
