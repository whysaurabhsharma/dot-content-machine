# Cold-start log 3: SETUP.md Part 1, then HANDOVER.md section 3 first test (teardown)

Tester: a fresh Claude Code subagent (Opus), given only README.md. Not a person. Date: 1 November 2026 (machine clock reads 2026-11-01, ~03:40 local).
Rules for the test: no Dot (no ask_dot call), no Olist CSVs, no edits to README/SETUP/HANDOVER/CLAUDE.md, scripts/ or .claude/.

## Timeline

| Time (local) | Step | Result |
|---|---|---|
| 03:40 | README.md read; points to SETUP.md | Smooth. "Start here: SETUP.md" is unambiguous. |
| 03:40 | SETUP Part 1 steps 1-4 (python 3.14.6, git 2.54, claude 2.1.316, ls, pip install) | All pass, under 1 minute (packages already installed on this machine). |
| 03:40 | SETUP step 5, `python scripts/check_setup.py` | 12 of 12 passed, 3 SKIP: "ready for teardowns and guides". Smooth. |
| 03:41 | SETUP step 6, rules check | Ran headless (`claude -p "What are the four human decisions?"`) instead of an interactive `claude`. Answered: question, outline, title, publish. 8 seconds. |
| 03:41 | HANDOVER s3 first test, step 1: `stage_gate.py start test-1 --bank 30 --format teardown --practice` | Wrote runs/test-1-piece.json. Gate: "next research". Smooth, 10 seconds. |
| 03:41 | Step 2: `timing.py test-1 research start`, then the researcher subagent started with HANDOVER's sentence verbatim | Started as the named subagent (`researcher`, model sonnet). I appended one parenthesis: the worktree path and "do not call any mcp__ask_dot__ tool" (test rule). |
| 03:45 | Researcher finished (3.8 min, 44 tool calls) and `timing.py test-1 research end` (4.0 min) | runs/test-1-research.md written, with `## 7. Sources` as the gate expects. **Verdict: PIECE IF**: accept a census of 5 (3 clear: Uber, GitLab, Langfuse; 2 borderline: Collibra, Wikimedia), or first add Airbnb/Pinterest after a person opens their Medium posts (403 to WebFetch). No ask_dot call made. Gate: "waiting research, the verdict is PIECE IF". |
| 03:45 | Step 3: cleared PIECE IF with `stage_gate.py clear test-1 --by "cold-start test (practice), not a person's review, 2026-11-01" --basis "..."` | Gate moved to "next figures". See G-1, G-2. |
| 03:45-03:46 | Step 4: figures | Re-opened Uber and GitLab with WebFetch (not a browser), asking for each number's exact sentence: all CONFIRMED. Wrote figures/test-1-figures.csv (12 rows: census count + 7 Uber + 4 GitLab) and runs/test-1-verification.md (modelled on B's). See G-3, G-b, G-4. |
| 03:46 | Step 5: `python scripts/stage_gate.py test-1` | **`next  outline   pieces/test-1-outline.md`**, "Next: outline (next)". End of the first test. |

Total: about 6 minutes wall clock from README to "next outline" (HANDOVER says about 30). Most of it was the researcher (4 min). A person doing a real browser check of every source would add most of the remaining 25.

Timing note: HANDOVER section 3 doesn't ask for the figures step to be timed. I logged `figures start/end` only after writing the file, so `runs/test-1-timing.csv`'s figures row (0.2 min) is not the real time (about 1 minute). timing.py only appends, so it stays; this line is the correction.

Files written: runs/test-1-piece.json, runs/test-1-research.md (by the researcher), runs/test-1-timing.csv, figures/test-1-figures.csv, runs/test-1-verification.md, this log.

## What worked smoothly

- README -> SETUP -> HANDOVER s3 pointers: unambiguous, no dead links.
- check_setup.py: clear PASS/SKIP lines, correct "ready for teardowns and guides" ending; it correctly needs no Olist CSVs and no Dot for Part 1.
- Nothing in Part 1 or the first test needed the Olist CSVs or a Dot account. No ask_dot call was made by me or the researcher.
- stage_gate.py: every call said exactly what came next, including the PIECE IF wait with the `clear` command to type, and "not used by format teardown" for truth/run/mark.
- The researcher subagent could be started by name and followed the teardown branch for section 7.

## Gaps and notes, as found (ranked list at the end)

- **G-1. The first test's census bar sets no count, so PIECE IF is likely on every run, and clearing it is a judgement a newcomer can't make.** HANDOVER.md line 112 gives the census bar ("the organisation's own publication describes how it writes down or governs its metric definitions") but not how many organisations meet it, nor what "borderline" counts as. The researcher therefore hedged with PIECE IF on a borderline count. The only floor I found is CLAUDE.md style rule 5 ("five or more"), which a newcomer has to know to look for. HANDOVER line 113 says "check the condition yourself", but this condition ("the human accepts...") is acceptance, not a check. Workaround: accepted 5 as meeting style rule 5, signed as practice.
- **G-2. A "practice" clearance is indistinguishable from a person's in the manifest.** `clear` takes any string for `--by`; runs/test-1-piece.json now says cleared by "cold-start test (practice)...". Nothing stops a model from clearing a PIECE IF on a real piece the same way. (Related open item, HANDOVER line 41: `--practice` skips refusals silently.)
- **G-3. Step 4's browser check can't be done by a session without a browser, and the gate doesn't know whether it was done.** HANDOVER.md line 114: "Open each source in a browser and check the number and any quote". I used WebFetch instead (the same model-reading route the step warns about) and wrote runs/test-1-verification.md, copying B's precedent. stage_gate.py lines 149-154 mark figures "done" as soon as the CSV has one data row: no verification file, no "checked by", nothing. The first test's step 5 therefore passes whether or not step 4's check happened. Also undefined: step 4 says "every number you would use" before any outline exists, so which numbers to copy is a guess (I took every number Uber and GitLab give, skipped the approximate Wikimedia/Collibra ones), and HANDOVER doesn't mention a verification file at all.
- **G-4. How to write a published value like "10K+", "6.53M" or "10X" as a figures `value` is undocumented.** check_piece.py `norm_number` (line 115) needs a plain float, so "10K+" can't be copied exactly as hard rule 4(c) asks. I wrote 10000 / 6.53 / 10 with the page's exact text in `description`. Whether check 15 will then match "10K+" in prose is untested.

- **G-a (minor, tooling).** Appending to this log with a bash heredoc was refused by the worktree guard ("too complex to verify"). Not a repo gap; logged with Edit instead.
- **G-b. The figures CSV's columns are not documented anywhere a newcomer reads.** HANDOVER.md line 114 says "one row each, its source as `published: <URL>, read <date>`" but names no header. No .md file contains `id,value,description,where_computed,date`; I found it only by opening B's `figures/how-companies-test-ai-data-analysts-figures.csv`, and the column name `where_computed` only in scripts/check_piece.py line 191. Workaround: copy B's header and ID style (ORG-n).
- **G-c. researcher.md is written for research pieces in places a teardown hits.** `.claude/agents/researcher.md` line 54 (section 3 "The run": what to run in Dot, mode, screenshots), line 56 (stop condition "only Dot's data could show it") and line 61 (PIECE = "a run in Dot can fill it") have no teardown wording, while line 21 and line 65 do split by format. A teardown has no run (CLAUDE.md "What this machine makes"), so the PIECE verdict as defined can't strictly apply. Effect seen: see the research output below.
- **G-d (small).** HANDOVER.md line 108 calls the first test "about 30 minutes"; SETUP.md line 16 gives no time. The researcher subagent was given `mcp__ask_dot__get_catalog` in its tool list (researcher.md line 4) even for a teardown; it is told to skip it (line 21), but nothing enforces that for a no-Dot test. I added an explicit "do not call ask_dot" line to its prompt.
- **G-e. Two sources the researcher wanted (Airbnb Minerva, Pinterest) are Medium posts that 403 to WebFetch**, and its web.archive.org fallback was blocked by permissions. The best-known public accounts of metric governance are unreachable to the subagent, so the census leans on borderline entries. Nothing in researcher.md says what to do with a 403 beyond "take the next result".
- **G-f. The house links table doesn't cover a new piece.** facts/house-structure-and-links.md "Suggested links per piece" has rows only for pieces 1-3; the researcher had to pick the Playbook stage (Stage 2 "Ground") from the Playbook page alone. Worked, but researcher.md line 23 points at a table that can't answer for any new piece.
- **G-g (unclear order, minor).** HANDOVER.md line 115 says `/piece test-1` continues to the outline; README "Running a piece with the workflow" step 2 says its first run asks you to approve the workflow. Not exercised (out of scope).

## Ranked gaps (most serious first)

1. G-3: figures marked done with no check that step 4's browser verification happened (stage_gate.py lines 149-154; HANDOVER.md line 114). Also no browser available to a model session.
2. G-1: no census count in the first test's bar; PIECE IF clearance is a judgement (HANDOVER.md lines 112-113).
3. G-2: a practice/model signature clears PIECE IF exactly like a person's (stage_gate.py `clear`).
4. G-c: researcher.md lines 54, 56, 61 still research-only for a teardown (section 3 "The run", stop condition, PIECE definition).
5. G-b: figures CSV header undocumented (HANDOVER.md line 114).
6. G-4: no way to record "10K+"/"6.53M" exactly as a numeric value (check_piece.py line 115).
7. G-e: Medium 403s, archive blocked: key census sources unreachable.
8. G-f: house links table covers only pieces 1-3 (facts/house-structure-and-links.md; researcher.md line 23).
9. G-d, G-g, G-a: small.

