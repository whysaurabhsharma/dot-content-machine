# Claude Code workflows: what was tested

Observed 31 October 2026, Claude Code 2.1.314, in this repo. Each finding names how it was tested.

## Saved-workflow format

| Question | Observed | How |
|---|---|---|
| File format and place | A JavaScript file with a `.js` extension in `.claude/workflows/`, starting with `export const meta = { name, description }` as a plain literal | A probe file `.claude/workflows/format-probe.js` was found and loaded by a fresh headless session, and later run from the interactive session |
| `.md` workflows | Not documented; not tested. The docs (code.claude.com/docs/en/workflows.md) show only `.js` | Docs |
| Invocation | As `/<meta.name>`, or with the Workflow tool's `name` | Both tried |
| Picked up mid-session? | Not at first: the Workflow tool answered "not found" in the session that created the file. A later turn of the same session listed it and ran it. A new session picks it up at start | Observed |
| First run of a saved workflow | Needs a person's approval ("Review dynamic workflow before running"). A headless `claude -p` session could not approve it and refused to run it | Fresh headless session |

## Skills with `disable-model-invocation: true`

**A workflow agent can't start one.** A probe workflow's agent called the Skill tool on a probe skill with the flag set, and got:

> "Skill probe-gated cannot be used with Skill tool due to disable-model-invocation. Ask the user to run /probe-gated themselves — it cannot be invoked via the Skill tool. Do not replicate this skill's workflow by other means — it is reserved for explicit user invocation."

So a workflow can't run `/outline`, `/draft`, `/seo-geo`, `/linkedin`, `/export` or `/bank` while they carry the flag, and its agents must not follow those skills' instructions by another route either.
