# Cold-start log 2 — piece `cold-2`, bank #42, research, practice

Tester: a fresh Claude Code subagent, no prior context, starting from README.md. Run 2026-11-01.

## Timeline

- 03:17 Start. Read README.md, then SETUP.md.
- 03:18 Setup checks pass (14 of 14); workspace verified (43,428). Decision 1 recorded.
- 03:19-03:21 Research (researcher subagent): PIECE IF.
- 03:21 PIECE IF cleared (practice sign-off). 03:21-03:23 truth spec, ground truth, reviewed_by (practice sign-off).
- 03:23 Batch 1 conditions written as "not observed". 03:23-03:25 Dot run (dot-runner subagent), 4 questions.
- 03:26 Credits after recorded as "not observed"; marked with mark_run.py. Gate: next is outline. Stopped there, as asked.

## Gaps and confusions (in order hit)

### G1. README points to three different "first" files (minor)
- README.md line 7: "New here? Read `HANDOVER.md` first." Line 11: "New here? SETUP.md ... Start with STATUS.md". Three "start here" pointers in five lines. The task brief said SETUP.md first, so I followed that; a person with only the README would not know which wins.

### G2. SETUP steps 1-6 and 10: smooth (03:17-03:18)
- Python 3.14.6, Claude Code 2.1.316, packages installed, import check printed `ok`.
- Step 5 (Kaggle download) is clear: URL, the account requirement, the two file names; `data/README.md` repeats it. Stood in for the download by copying the two CSVs from the main checkout into `data/olist/`, as the person running the test instructed.
- Step 10 `python scripts/check_setup.py`: "14 of 14 passed" first time.
- Steps 7-9 not done by me: the Dot account, workspace and MCP were already set up by the person running the test.

### G3. SETUP step 11 (workspace verification): smooth (03:18)
- Asked Dot "How many orders were delivered in 2017?" in a fresh chat via MCP: "43,428 orders placed in 2017 have a recorded status of delivered . This uses purchase date, not delivery date." Matches. Chat: https://app.getdot.ai/?c=2b94f948-5d3d-4043-97a8-da8023021bc7
- facts/dot-workspace-setup.md section 3 step 3 ("Record the conditions in Dot's own UI") cannot be done by this tester: no UI access. See G8.
- SETUP step 12 (rules loaded): CLAUDE.md is in context; the four decisions are the question, the outline, the title, the publish. OK.

### G4. Decision 1 with `--practice` silently skips the gate's refusals (moderate)
- `python scripts/stage_gate.py start cold-2 --bank 42 --format research --practice` succeeded (03:18).
- Bank row 42 has `evidence_by = model-unconfirmed`. stage_gate.py's help says `start` "refuses unless ... its evidence score is confirmed by a person"; the code (scripts/stage_gate.py lines 349-353) skips that check, and the status check, when `--practice` is passed. Neither the help text nor SETUP.md line 22 says practice bypasses them. For a practice piece that is arguably right, but a tester never meets the "confirm the evidence score" step a real piece needs, and no message says it was skipped.
- HANDOVER.md section 3, first test, step 1: "If it isn't the top row, add `--why`". #42 is not the top row (`bank.py top` names #41); the script did not ask for `--why` and wrote `"why": ""`. The doc reads as a requirement; the script treats it as optional.
- The manifest stores `"question"` = the bank's `ai_form` (buyer wording) and `"topic"` = the bank's `question` column (short phrase). The previous cold-start's gap 5 looks fixed, but the names are now swapped relative to the bank CSV's columns, which confuses anyone reading both.

### G5. Research stage started (03:19)
- `python scripts/timing.py cold-2 research start` worked.
- The `researcher` subagent started fine with the Agent tool. Brief: bank #42, slug cold-2, format research, practice, at most 4 test questions (the person's credit limit).

### G6. Research done in 2.1 min (03:19-03:21); the researcher skipped two of its own "before you start" steps (moderate)
- Verdict PIECE IF; four test questions (T1 "Which month was our best month?", T2 repeat, T3 follow-up "What if I meant by number of orders? How many orders did the best month have?", T4 "What was our best month for sales in 2017?").
- `.claude/agents/researcher.md` "Before you start" says to name the Playbook stage *from the Playbook itself and `facts/house-structure-and-links.md`*. The researcher instead took "Stage 3, trusted numbers" from bank row #35 and says it read no Playbook document. The same section says to call `get_catalog` and record it in Sources; the Sources table has no get_catalog row. So the cold-start gaps (3) and (4) of the first test were addressed in the prompt but not reliably followed by the agent (model: sonnet).
- Its third top page failed (HTTP 429) and the fallback arXiv page was unreadable; it said so and used a page from a second search. Honest, and as instructed.

### G7. A PIECE IF condition that can only be met after the run blocks the gate before it (serious)
- The verdict's condition: "the run records the metrics note as active and the finding is stated as what Dot did under that note". The gate (stage_gate.py, PIECE IF branch) waits at research until a person runs `stage_gate.py clear`. But the condition is about the run, which hasn't happened, and "the note is active" is exactly what the MCP cannot see (facts/dot-mcp.md). Nothing tells a person how to clear a forward-looking condition: clear it now on a promise, or hold the piece at research forever.
- Worked around: `get_catalog` shows the note exists; cleared as "cold-start test (practice), not a person's review, 2026-11-01" with a basis stating it is a forward condition not checked before the run. **A real new team member would stop here** (sign-off required).
- Suggestion: the researcher prompt should say a PIECE IF condition must be checkable before the run, or the gate should carry forward conditions to the run stage.

### G8. Truth spec (03:21-03:23, 1.2 min): clear, but the spec language can't express the question (moderate)
- HANDOVER section 3 step 4 and the spec format in `scripts/ground_truth_from_spec.py`'s docstring were enough to write `specs/cold-2-truth.json`. 16 rows (4 asked, 12 rivals/reference), all computed.
- **"Which month" can't be marked.** A formula must return a number, and mark_run.py marks the first number in the answer. The heart of this question (which month Dot names, and which metric it picked) is not marked. Worked around by adding reference rows T1m/T4m that compute the best month as YYYYMM (201711), asked: false, for a person to compare by eye. No doc says how to handle a question whose answer is a label, not a number; the researcher's rule "one number per question" pushes the problem to the spec.
- **Formula builtins are only `len`.** `int(...)` failed with NameError; nothing documents the allowed names. Used `pd.to_numeric` instead.
- **A formula reads one table.** The rival "orders of any status in the month with the highest delivered revenue" needs both tables; computed only over orders with item rows (T3d), with the limit stated in its metric.
- **Repeats share question text.** mark_run.py matches a run entry to a truth row by id (Q1 vs T1, never equal: run entries are Q<k>, spec rows T<k> by precedent) and then by question text, through a dict, so T1 and T2 (identical wording) collapse to whichever comes last. Values are identical here, so it doesn't change a mark, but the row named will be T2 for Q1. Nothing in the docs says to use `--map` for repeats; I will use `--map Q1=T1 --map Q2=T2 --map Q3=T3 --map Q4=T4`.
- **Observed from the truth values (not a finding about Dot):** on this data the readings collide. The best month is 2017-11 under revenue and under delivered order count, and it falls in 2017, so T4 = T1 and T3 = T3c. A rival-readings test can't tell some readings apart from the number alone. The research step can't see this, because it never sees values (hard rule 2), so nobody checks whether the test discriminates.
- `reviewed_by` signed "cold-start test (practice), not a person's review, 2026-11-01". **A real new team member would stop here** (sign-off required).

### G9. Batch conditions: unobservable, and the gate accepts "not recorded" as recorded (serious)
- HANDOVER section 3 step 5 and stage_gate.py say a person writes `## Batch 1: conditions` from Dot's UI. This tester has no UI. Wrote the block with each of Mode, Environment, Context notes, Credits before as "not observable via MCP; not recorded". `stage_gate.py cold-2` then said `run (next)`.
- stage_gate.py `recorded()` only rejects "not yet recorded" or blank. The run-format template text ("Mode: not selectable via MCP. Screenshot: ...") or my "not recorded" passes as a recording. For a practice piece no screenshot is checked either. So the gate's rule 14/15/17 stop can be passed with text that admits nothing was observed.
- **Ownership of the block is contradictory.** HANDOVER section 3 step 5, runs/README.md and stage_gate.py: a person writes it before the run (the gate refuses the run until it exists). `.claude/agents/dot-runner.md` "Before the first question": the dot-runner writes the conditions block. Followed literally, the file gets two `## Batch 1: conditions` headings. Told the dot-runner not to write a second one.
- SETUP.md line 22 says practice pieces "record conditions as text instead of screenshots"; runs/README.md line 23 says only "a rehearsal may" do that. Different words for the same allowance.
- Whether the metrics note was on is the PIECE IF condition (G7); it remains unverified.

### G10. Dot run (03:23-03:25, 2.1 min, logged by the dot-runner): smooth
- The `dot-runner` subagent started with the Agent tool, asked all 4 questions verbatim, kept the conditions block, put Q3 in Q1's chat, and timed itself. Classifications: Q1 asked back; Q2, Q3, Q4 answered.
- Q1 (fresh chat, "Which month was our best month?") asked back: "Do you mean the month with the highest revenue, the most orders, or the best delivery performance?" Q2 (the identical question, another fresh chat) answered with revenue. Same wording, two behaviours: an item-by-item difference (hard rule 18).
- Q3 was written as a follow-up to an *answer* ("How many orders did the best month have?"), but Q1 asked back instead, so the follow-up landed after a clarifying question. The research step can't foresee that; nothing tells the runner or the spec what a follow-up means when its parent asked back. It still worked here (Dot read Q3 as answering its own question).
- Credits after: recorded as "not observable via MCP; not recorded". The gate then moved to mark (same weakness as G9).

### G11. mark_run.py marked a correct answer as a "real gap": year parsed as the answer (serious)
- `python scripts/mark_run.py cold-2 --batch 1` (the gate's exact command), 03:26, printed:

```
   Q1  not marked                        Classification is 'asked back'; no answer to mark
   Q2  correct                           Q2 vs T2 (...), matched by question text: answer 987,765, expected 987765.37 BRL; gap 0.0000% (rounding); correct
   Q3  matches rival                     Answer gave 7,544, under a stated basis ('counting all statuses, including cancellations across the available history orders placed') that matches no truth row by its words; the figure equals T3b (...: 7544); a person decides
   Q4  real gap                          Q4 vs T4 (...), matched by question text: answer 2017, expected 987765.37 BRL; gap 99.7958% (real); real gap

1 of 4 correct: 1 under the definition asked, 0 only under another reading (...). Quote both numbers, never the total alone.
  correct: 1; matches rival: 1; not marked: 1; real gap: 1
```

- **Q4 is a false "real gap".** Dot's answer: "November was our best sales month in 2017, with BRL 987,765 in sales ." The expected value is 987,765.37: Dot was right. mark_run.py takes "the first number in the answer text, skipping dates and years in dates"; its year skip only covers "<Month> <YYYY>" (YEAR_IN_DATE) and "YYYY-MM", so "in 2017" is read as the answer. Any answer that names a year before its figure ("in 2017, ...") is marked wrong. The figures file now holds `MR-Q4,2017`, a Figures row for a number that isn't Dot's answer, and the gate reports mark "done": no step makes a person look at a "real gap" before the outline.
- **Q3's "matches no truth row by its words" is misleading.** The basis matched the signal "all statuses" in two rows, T3b and my T3d (both unfiltered, different formulas), so the definition was ambiguous, not unmatched. Partly my spec's fault (a shared signal); the message pointed me the wrong way.
- **The repeat collapse (G8) happened:** Q2 matched T2 "by question text". Q1 would have matched T2 too had it answered.
- A person's view (to a scratch file, not the repo's figures): `--map Q1=T1 --decide Q3=T3b` gives "2 of 4 correct: 1 under the definition asked, 1 only under another reading"; Q4 is still "real gap", because neither `--map` nor `--decide` can correct the extracted number. There is no documented way to mark Q4 correctly short of editing the run file (forbidden) or the figures row by hand. Left the repo's `figures/cold-2-figures.csv` as mark_run.py wrote it.
- Read by hand: Dot named November 2017 in Q2, Q3 and Q4 (truth T1m/T4m: 201711), and Q2/Q4's values match T1/T4 to display rounding; Q3's 7,544 equals T3b. None of this is visible in mark_run.py's output, which marks no month.

### G12. Stage times (all `logged` in runs/cold-2-timing.csv)
- Setup (steps 1-6, 10, 11): about 1 minute of commands, 03:17-03:18.
- Decision 1: under a minute. Research 2.1 min. Truth 1.2 min (plus reading the spec format). Conditions under a minute. Run 2.1 min. Mark 0.3 min.
- Wall clock, README to marked run: 03:17 to 03:27, about 10 minutes.

## What worked smoothly
- SETUP.md's table: every step had a check, and check_setup.py's 14/14 matched reality.
- The workspace verification question (43,428) gave an unambiguous yes.
- `stage_gate.py <slug>` always named the next step and the exact command; I never had to guess the order.
- Both named subagents (`researcher`, `dot-runner`) could be started, and the dot-runner's output parsed cleanly in mark_run.py.
- mark_run.py's split line ("1 under the definition asked, 0 only under another reading") and its refusal to re-mark existing rows.

## Sign-offs made by this test (a real new team member would stop at each)
1. PIECE IF clearance: `stage_gate.py clear cold-2 --by "cold-start test (practice), not a person's review, 2026-11-01"` (G7).
2. Truth spec `reviewed_by`: same wording (G8).
3. Batch 1 conditions and credits after: written as "not observable via MCP; not recorded", which the gate accepted (G9, G10).

