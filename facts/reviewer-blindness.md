# What still reaches a blind reviewer

The blind reviewers (`reader`, `fact-checker`, `lift-tester`) are meant to judge a draft as a stranger would. Five measures keep the rulebook out:

- **`scripts/run_reviewer.py`**, the only way to start a reviewer: a headless session with `--strict-mcp-config` and an empty MCP config, so no MCP server instructions reach it (B4);
- `omitClaudeMd: true`, so no CLAUDE.md loads;
- a PreToolUse hook (`scripts/hooks/read_allowlist.py`) that blocks any file outside each reviewer's allowlist;
- a body-only review copy (`scripts/review_copy.py`), with no front matter;
- one fixed invocation sentence each (`runs/README.md#reviewers`).

This file records what still gets through. Each item is Observed: seen on 31 October 2026, Claude Code 2.1.314, by a probe agent configured like the reviewers (`tools: Read`, `omitClaudeMd: true`). The probe was asked to quote its whole context.

## Observed: leaks the agent definition can't close

| ID | What reaches every subagent | Content or names? | Source |
|---|---|---|---|
| B1 | **The environment block:** working directory, platform, shell, OS version, scratchpad path, model name and ID, today's date. | Names. The folder path names the project (`dot-content-machine`). | Probe, 31 Oct 2026. The subagents docs list "environment details" in what a subagent receives and give no way to switch them off. |
| B2 | **A git status snapshot:** branch, git user, the names of changed and untracked files, and the five most recent commit subjects. | File names, not file contents. **But commit subjects are content:** on 31 Oct they included "A2 basis corrected, A3 superseded", which describes a rule change. | Probe, 31 Oct 2026. The docs list the git status snapshot and give no way to switch it off. |
| B3 | **The user's email address.** | Identity, not rules. | Probe, 31 Oct 2026. Not mentioned in the docs. |
| B4 | **MCP server instructions** for every connected server (ask_dot, Claude Docs, Clay, Google Sheets, HubSpot, rea), even though the reviewer has none of their tools. | **Content.** The ask_dot instructions describe what Dot does ("writes SQL, runs queries, generates charts, and explains results"), which is product information a reviewer judging product claims shouldn't have. | Probe, 31 Oct 2026: they arrived as a system message after its first tool call. **Closed only by `run_reviewer.py`** (below). |

The docs give no setting in an agent definition that removes B1, B2 or B3. They leak file names and identity rather than rules, apart from the commit subjects in B2.

## B4: what closes it and what doesn't

Tested 31 October 2026 with two probe agents (`tools: Read`, `omitClaudeMd: true`), each started from a fresh headless `claude -p` session:

| Setup | MCP server instructions reached the probe? |
|---|---|
| Agent definition with `mcpServers: []` | **Yes**: all six servers, ask_dot's first sentence quoted. An empty list in the agent definition does not withhold them. |
| No `mcpServers` field (control) | **Yes**: the same six servers. |
| Parent session started with `--strict-mcp-config` and an empty MCP config | **No**: none at any point, before or after its tool call. |

So B4 is closed only when the session that starts the reviewer has no MCP servers connected. `scripts/run_reviewer.py` does that, and is the only way to start a reviewer. **Started any other way, such as from an interactive session with the Agent tool, a reviewer would receive ask_dot's description of Dot.** So that route fails closed: the launcher sets `DOT_REVIEWER_LAUNCH=<reviewer>` in the session it starts, and the reviewers' hook blocks every file call without it, so a directly launched reviewer can't read the draft and stops. The guard can be defeated only on purpose, by setting that variable in the shell before starting an interactive session. If that happens, or the guard fails, the reviewer's judgements divide like this:

| Judgement | Trustworthy if B4 is open? |
|---|---|
| Arithmetic and internal consistency of the draft's numbers | Yes: they don't depend on knowing the product |
| Numbers against the figures file; quotes against the run file | Yes: checked against files, not knowledge |
| Conclusions that go further than the draft's own evidence | Yes, mostly: the test is the draft's reasoning |
| Product claims marked VERIFIABLE or ASSERTED | **No**: it may treat a claim as known because ask_dot's instructions say it, not because the draft shows it |
| Reader's "claim I don't believe" about a product feature | **No**, for the same reason |

Even with B4 closed, product claims still need the second fact-check on a different model, outside this repo, because the reviewers share a model family with the writer (below).

## Observed: hooks and the shell

- In a headless session started from `run_reviewer.py`, hooks ran in PowerShell, not Git Bash, so `$CLAUDE_PROJECT_DIR` in a hook command was not expanded. A path relative to the repo root works in both shells, but only when the session starts in the repo root.
- The hook commands are now a short `python -c` shim that reads `CLAUDE_PROJECT_DIR` from its own environment and runs the hook script by absolute path. It works in Git Bash and PowerShell from any working directory (tested from the home directory). If the variable is missing or wrong, it blocks with "Hook script not found, CLAUDE_PROJECT_DIR is …" rather than failing silently.
- When the hook couldn't run, every read was blocked: the reviewer reported it couldn't open the draft and wrote no review. The allowlist fails closed.

## Observed: what did not reach the probe

- No CLAUDE.md content, project or user.
- No hook-injected text: the caveman plugin's SessionStart and UserPromptSubmit output did not appear.
- No skills list, and no agents list.
- No main-session memory.
- No output style.

## Observed: the reviewers share a model family with the writer

The writer and the three reviewers all run on the same model family (Claude; the probe reported Opus 5.5). Their blind spots may overlap: a reviewer may miss the mistake the writer made for the same reason the writer made it. So the second fact-check stays on a different model (ChatGPT or Gemini), as `prompts/05-fact-check.md` pass 2 says. The lift test still runs in Perplexity and Claude (`prompts/06-edit.md`), and the `lift-tester` agent is only a first pass.

## Closed by the measures above

- **CLAUDE.md read by hand.** The probe could Read CLAUDE.md with `tools: Read`. The allowlist hook now blocks that.
- **Intent in the front matter.** Queries, figures file, Playbook URL, reverse links and dataset are stripped from the review copy.
- **Rules passed in the request.** The fixed sentences carry only file paths, and `run_reviewer.py` passes them with nothing added.
- **MCP server instructions (B4).** Closed by `run_reviewer.py`, as above.

Live test, 31 October 2026: each reviewer tried to read files outside its allowlist from a real agent call, and the hook blocked every one (CLAUDE.md, facts/dot-facts.md, pieces/piece-3.md, figures/piece-3-figures.csv for the lift-tester, prompts/06-edit.md, figures/piece-3-truth.csv for the fact-checker), as well as the fact-checker's Write to pieces/. Each could read its own files.
