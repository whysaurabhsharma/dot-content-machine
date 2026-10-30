# Handover: run the machine yourself

Written 28 October 2026 for Rick and Théo. Everything here works from the files in this folder; nothing depends on the author's accounts.

## 1. Set it up in your own Claude account (10 minutes)

**First, two names that are easy to mix up.** `CLAUDE.md` is a file in this folder: the rulebook. "Instructions" is not a file; it's the name of a box inside your Claude Project. You copy the text of `CLAUDE.md` into that box.

1. In Claude, create a Project named **Dot Content Machine**.
2. Open `CLAUDE.md` in a text editor (Notepad on Windows, TextEdit on Mac) and copy all of its text.
3. In the Project, open the box called **Instructions** ("Set project instructions"), paste the text, and save.
4. In the Project's files area (labelled **Project knowledge** or **Files**, depending on your version of Claude), upload twelve files: the seven in `prompts/`, the two in `facts/`, and the three in `pieces/`.
5. Check it loaded: start a chat in the Project and ask *"What are the four human decisions?"* It should answer: the question, the outline, the title, publish.

**Or use Claude Code.** Open this folder in VS Code with Claude Code, or run `claude` in it from a terminal. It reads `CLAUDE.md` automatically and runs the scripts for you. Install the two libraries first: `pip install pandas matplotlib`.

## 2. A 15-minute first test

Pick a question in a buyer's words. Then:

1. **Perplexity:** paste the question. Copy the whole answer. Note who is cited and whether Dot is.
2. **Google:** search a short form of it. Copy the titles of the top three results.
3. **Ahrefs → Keywords Explorer (US):** check two or three phrases. Note volume or "not indexed".
4. **The Project, new chat:** paste the template below with the blanks filled. In Claude Code, replace the first line with *"Run the prompt in prompts/01-research.md for this question."*
5. **Read the verdict:** PIECE, NOT A PIECE, or PIECE IF. Read the three test questions it proposes.
6. **Dot, Economy mode, new chat:** ask the first test question. Check whether the answer states its basis (population, period, definition), as the verdict said a correct answer must.

What a good result looks like: on 28 October, the question "How do we stop different teams getting different numbers for the same metric?" returned "PIECE, if the test covers five metrics", and Dot's answer to the first test question stated the number, the population (delivered orders), merchandise value only, and the order count. The whole run took 13 minutes.

```
Run prompts/01-research.md (from project knowledge) for this question. This is a live run, so some inputs are partial: say what's missing rather than guessing, and don't use anything you remember about any page or product.

The question, in the buyer's words: "…"

Inputs:
1. Perplexity's answer to the question, pasted in full (today):
…
2. Top three Google results for "…": 
- … · - … · - …
3. Ahrefs Keywords Explorer, US: …: SV …, KD … · …: not indexed
4. Search Console: not pulled for this run.

Return the five sections as usual, and end with:
- A one-line verdict: PIECE or NOT A PIECE, and why.
- The first three test questions I should ask Dot, in a buyer's words, with what a correct answer would need to state.
```

## 3. Running a full piece

**The full step-by-step guide is `guides/Dot-Run-a-Full-Piece.pdf`**: every step with what to paste, what you get, where to save it, and how it went in the trial.

Follow `runbook.md`: eleven steps, four decisions. Three things to know:

- **Two stages run outside the Project**, in a fresh chat with no instructions: READER (`04-reader.md`) and the first fact-check (`05-fact-check.md`). The reviewer must not know what the writer meant. The second fact-check runs in a different model (ChatGPT).
- **Every number needs a row** in the piece's `figures/` CSV before the checker will pass it. Add rows as you go, not at the end.
- **Log the run conditions** in the Run Log before the first question: account, environment, mode (screenshot it), active context notes, credits before and after. The mode drifted twice during the trial; checking it before every question is the fix.

Gate: `python scripts/check_piece.py pieces/<piece>.md`. Fix every FAIL; do the six human checks; then Decision 4.

## 4. The monthly loop (one owner, about 20 minutes a week)

- **Week 1:** read the Baseline tab's measures and add a dated column: Search Console, Rank Tracker, the AI-responses panel, the three Perplexity prompts.
- **Week 2:** add new questions from sales calls and Search Console to the Question bank.
- **Week 3:** turn any fix made twice into a rule in `CLAUDE.md`, dated, and re-paste the instructions.
- **Week 4:** re-run past evaluations in Dot; pick the next question.

## 5. What's still open

| Item | Why it matters | What closes it |
|---|---|---|
| Phone read of each piece (check 24) | The last human check | Read each aloud once on a phone |
| Piece 1's evaluation on Dot's data | The trial used Olist, licensed non-commercial | Re-create the 20 rows in a Dot workspace |
| Assumptions A1–A8 | Each is labelled in the text | A yes, no or change from Dot |
| A clean Balanced batch for piece 3 | The Balanced figure is from a mixed batch | Ten questions, all Balanced, credits read before and after |
| Time per piece | Never logged | Time the next piece, stage by stage |
| The question bank of 102 | Only 10 rows are in the sheet | Load the bank and re-rank it with ten sales-call questions |
| Nobody but the author has run it | The core claim about the machine | Section 2, then one full piece |

## 6. Accounts and tools you need

Claude (a Project, or Claude Code) · Dot (a workspace with the Olist tables or your own data) · Ahrefs (the Getdot project; Rank Tracker already holds 18 keywords) · Perplexity and ChatGPT (free plans are enough) · Google Sheets (the tracking sheet) · Python 3.10+ for the scripts.
