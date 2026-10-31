# Cold-start log: first test on bank #29, slug `cold-1`

1 November 2026. A new team member, starting from README.md only, ran the handover's "first test" as far as the research verdict. Decision 1 (bank #29) was made by the person running the test. Dot sign-in, screenshots and Dot runs were out of scope. Environment: Windows 11, Git Bash, Python 3.14.6, Claude Code (the test ran as an agent session, so `/mcp` and `/agents` could not be typed; the agent list it was given showed all five agents).

## Timeline

| Step | Clock (local) | Took | Result |
|---|---|---|---|
| Read README.md, HANDOVER.md | 01:59:55–02:00:08 | under 1 min (skim; longer for a person) | Found the first test in HANDOVER section 3, not section 2 as README says |
| Set-up: Python packages, sanity check | 02:00:08–02:00:22 | under 1 min | Packages already present; check printed `ok`; check_piece.py ran, one count differs from README |
| MCP connection (`/mcp`, sign-in) | — | skipped | Out of scope: no Dot sign-in |
| Decision 1 recorded | 02:00:22–02:00:46 | under 1 min | `stage_gate.py start cold-1 --bank 29 --format research` wrote `runs/cold-1-piece.json` |
| Research (researcher subagent) | 02:00:58–02:02:12 | 1.2 min logged by `timing.py` (agent: 64 s, 14 tool uses) | `runs/cold-1-research.md`, verdict **PIECE IF** |
| Read and check the research file | 02:02:12–02:04 | about 2 min | Quality issues noted below |
| Screenshots, dot-runner, check entry | — | stopped | Need Dot's UI and a Dot run |

Files the test created: `runs/cold-1-piece.json`, `runs/cold-1-timing.csv`, `runs/cold-1-research.md`, this log.

## What worked smoothly

- README points to HANDOVER and STATUS on its first screen; the quick start's two commands worked first time.
- `stage_gate.py start` accepted #29 (unwritten, evidence confirmed by a person) and the gate then named the next stage plainly (`research`, then `truth`).
- `timing.py` logged start and end with minutes; the stage name `research` and who logs it are defined in `runs/README.md#timing`.
- The researcher agent's instructions are complete enough to run cold: it found every input file, said "not measured" where it should, wrote section 7 in the required shape, and gave a verdict in the required form. `stage_gate.py` accepted the file.
- `bank/README.md` is candid about the bank's limits (no sales-call questions, thin Ahrefs data), which explained why #29 is not `bank.py top`'s pick.

## Gaps, most serious first

### 1. The first test skips the gate's own order
- **Where:** HANDOVER.md lines 98–104 ("A 15-minute first test") against README.md "Eleven steps", rows 1–3, and `scripts/stage_gate.py` docstring ("the run waits for the truth spec's reviewed_by").
- **Expected:** one sequence. **Found:** the first test goes research → screenshots → dot-runner. It never records Decision 1 and never writes or reviews the truth spec. After research, `stage_gate.py cold-1` says `next truth`, not screenshots. So the first test is a side path the gate does not recognise; someone following the gate would hit a different step 3 from the one HANDOVER names.
- **Workaround:** recorded Decision 1 with `stage_gate.py start` (the runbook's step 1) so the gate could track the piece; stopped at the research verdict as instructed.

### 2. A PIECE IF verdict passes the gate with its condition unrecorded
- **Where:** `scripts/stage_gate.py` (handles `NOT A PIECE` and `NOT A PIECE, BUT A SURFACE`; no `PIECE IF` branch); researcher.md section 6.
- **Expected:** a PIECE IF condition to be a stop a person must clear. **Found:** the gate marks research `done` and moves to `truth`. Both conditions here (the Dot workspace holds the needed Olist tables; a licence decision for cold-1) are unchecked and recorded nowhere but in prose. Licence decisions L1–L4 in `facts/dot-facts.md` each name a piece; none covers a new piece, and nothing says who makes the next one or where.
- **Workaround:** none; noted for whoever continues.

### 3. Nobody tells the researcher what data Dot's workspace holds
- **Where:** `.claude/agents/researcher.md`, "Return", item 3 ("What to run in Dot, on which data"); HANDOVER section 10 ("a workspace with the Olist tables or your own data").
- **Found:** the researcher had to guess that the workspace holds Olist `order_items` and `order_payments` and wrote it as a condition. No file lists the tables connected in the current workspace (`facts/dot-mcp.md` says `get_catalog` can read them, but the researcher has no MCP access).
- **Workaround:** the verdict carries it as a condition. A file of connected tables, refreshed by the dot-runner's `get_catalog` call, would close it.

### 4. The research output has quality problems the instructions didn't prevent
- **Where:** `runs/cold-1-research.md` section 7.
- T3 contradicts itself: it says it will carry both definitions in a fresh question, but its wording ("the difference between those two 2017 revenue figures") only makes sense as a follow-up. The one-number rule and the follow-up rule (researcher.md section 7) don't say what to do when a follow-up needs two earlier numbers.
- T8–T10 depend on a context note that defines revenue, which is assumption A5 and the run's own setup, not something the research justifies; the run section never says who writes the note or what it says.
- The Playbook stage is "to be confirmed": the agent wasn't told where the stage names live. `facts/house-structure-and-links.md` line 80–82 maps topics to Playbook stages, but researcher.md never points to it.
- The research ignores Dot's own page on the topic. The bank row's gap basis cites `/blog/the-semantic-layer-solves-the-wrong-half` (gap 2, "touches it in passing"); researcher.md never asks the agent to read the bank row, so the gap chain says nothing about Dot's existing page.
- **Workaround:** none made; a person reviewing the research (or the truth spec review) should fix these before any run.

### 5. Two names for bank #29
- **Where:** `runs/cold-1-piece.json` (written by `stage_gate.py start`) stores the bank's `question` column, "two dashboards show different numbers"; the buyer's wording is the `ai_form` column. HANDOVER section 4 and the task use the `ai_form`.
- **Effect:** the gate and manifest show a different question from the one the researcher is given. Harmless here (the researcher noted it and used the buyer's words), but a later stage reading the manifest would get the short form.

### 6. Cross-references and versions disagree
- README.md line 66: the first test is "HANDOVER.md section 2"; it is section 3 (HANDOVER line 98). Section 2 is costs.
- CLAUDE.md version: README.md "What's here" says v1.6.5; HANDOVER.md line 7 says v1.8.10; STATUS.md says v1.8.13; the file's change log ends at v1.8.13.
- Piece status: HANDOVER.md lines 13–17 say F is at "Outline next", A has 1 post and "Three of six posts exist"; README.md and STATUS.md say F is exported and all six posts exist. HANDOVER's own section 2 table also says "F (guide, so far)".
- README.md quick start: expected `17 pass, 0 fail, 1 partial, 6 for a human`; got `17 pass, 0 fail, 1 partial, 7 for a human` (check 25 is HUMAN because A's outline predates v1.8). README lists "6 flagged for a human" in the What's-here table too.
- README.md "Permissions" says `.claude/settings.json` pre-approves "only the five scripts the skills call"; it also pre-approves `bank.py`, `stage_gate.py`, `mark_run.py`, `ground_truth_from_spec.py`, `review_copy.py` and more.
- `.claude/skills/bank/SKILL.md` calls itself "Stage 3 BANK"; stage 3 in CLAUDE.md is DRAFT.

### 7. Small tool behaviours
- `python scripts/stage_gate.py --help` treats `--help` as a slug and prints "a person runs `stage_gate.py start --help --bank <id>`". No help; read the docstring instead.
- The researcher agent has no Bash, so it can't call `timing.py` itself; README says each stage "times itself". `runs/README.md#timing` does say the caller logs research, so this is consistent once found; the handover's first test doesn't mention it.
- HANDOVER section 3 set-up step 2 installs packages; on this machine they were already present, and the check alone was enough.
- `bank.py top` recommends #41 (10/12), not #29 (9/12). The person's Decision 1 overrides it; nothing in the files says whether choosing below the top needs a reason recorded.

### 8. Things a newcomer could not do from the files
- `/mcp` and `/agents` checks (HANDOVER section 3, steps 4–6) need an interactive Claude Code prompt; untestable here.
- The "four human decisions" check (step 5) passed by reading CLAUDE.md: the question, the outline, the title, the publish.

## Where the test stopped

At the research verdict. The next step by HANDOVER is screenshots in Dot's UI for batch 1; by the gate it is the truth spec (`specs/cold-1-truth.json`) and its `reviewed_by`.
