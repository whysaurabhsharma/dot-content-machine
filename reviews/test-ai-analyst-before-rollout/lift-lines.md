# Lift lines · test-ai-analyst-before-rollout

Format and method: `prompts/06-edit.md`, section 3.

## Intended

1. "Ask each test question twice, in fresh chats: in our run on Dot, one question returned 2,878 and 2,453, each correct under its own definition." (IDs: RP2-MR-Q5, RP2-MR-Q11) The outline's quotable line; the blind lift-tester lifted it word for word (check 25). Now in step 3.

Replaced 1 November 2026: line 1 is now **"In our run on Dot, one question returned 2,878 late orders counting by the exact delivery timestamp, and 2,453 counting by the delivery day."** (IDs: RP2-MR-Q5, RP2-MR-Q11). The blind lift-tester chose it from the opening over the targeted line, because it names both definitions and needs no context, which is what the headline readers asked for. **An engine chose a better line than we targeted, in all three pieces:** A (see its lift-lines), B (the Hex line, added as line 4), and F (this line). Write the intended lines, but read the engine's choice as the stronger evidence.

## Lift test, 1 November 2026 (Saurabh): PASS

| Tool | Lifted | Intended? |
|---|---|---|
| Perplexity | "Collect real questions your team already asked. Write every answer you would accept before you ask" | No: pocket lines 1 and 2 |
| Perplexity | "Ask each question twice, each time in a fresh chat, and compare" | No: step 3's instruction, the step the quotable line sits in |
| Perplexity | "Re-run the test on a schedule, and whenever something it depends on changes: a definition, a table, a model" | No: step 8 |
| Claude | "Hold access until the tests pass your bar (~80%)" | No: the Playbook, quoted in step 7 |
| Claude | "underreported recall by 10-15%" | No: LinkedIn, step 2 |
| Claude | the 2,878 / 2,453 split with both definitions | The quotable line's substance, not its sentence |
| Claude | "3 matched only the delivery-date reading" | No; checked against A's figures (RA-SPLIT) |

**Finding about the format, not a failure.** Neither engine lifted the quotable line; both lifted the steps, accurately and in order. A guide's citable unit is its instructions, not a sentence. Carrying the method intact through compression is the real test for a guide, and both engines passed it.

**For next time (not changed now, on Saurabh's instruction):** for a guide, the intended lift lines should be the steps themselves, and check 25 should test whether the steps survive compression (how many of the step instructions an engine's summary reproduces, and in order), not whether one line is quoted.
