# Handover: run the machine yourself

Written 28 October 2026 for Rick and Théo; rewritten 31 October 2026 for Claude Code. Everything here works from the files in this repo; nothing depends on the author's accounts.

## 1. Set it up in Claude Code (10 minutes)

`CLAUDE.md` is the rulebook. Claude Code reads it automatically whenever it starts in this folder, so there is nothing to copy or paste.

1. Clone the repo and open a terminal in it.
2. Install the scripts' packages into the Python you'll use: `python -m pip install -r requirements.txt`. Check with `python -c "import pandas, matplotlib, docx; print('ok')"`.
3. Connect Dot's MCP, once per machine: `claude mcp add --transport http ask_dot https://app.getdot.ai/ai/mcp`
4. Run `claude` in the folder. Type `/mcp`, choose `ask_dot` and sign in to your Dot workspace. It should report "Connected to ask_dot."
5. Check the rules loaded: ask *"What are the four human decisions?"* It should answer: the question, the outline, the title, the publish.
6. Check the subagents loaded: type `/agents`. You should see `researcher` and `dot-runner`.

You can also open the folder in VS Code with the Claude Code extension. The steps are the same.

## 2. A 15-minute first test

Pick a question in a buyer's words, from `bank/questions.csv` or your own. Then:

1. **Research.** In Claude Code: *"Use the researcher agent on this question, piece slug test-1: '…'"*. It reads the Ahrefs snapshot and the citation series, fetches the top three pages, and writes `runs/test-1-research.md`.
2. **Read the verdict:** PIECE, PIECE IF, or NOT A PIECE. Read the test questions it proposes. Each has its exact wording, the definition it depends on, and the figure it must produce.
3. **Screenshots, in Dot's own UI:** take the five for batch 1, named as in `runs/README.md#screenshots`. Mode, credits, environment and context notes can't be seen through the MCP.
4. **Run.** *"Use the dot-runner agent on test-1, batch 1, first question only."* It asks Dot the question word for word and appends the answer to `runs/test-1-run.md`.
5. **Check the entry** against `facts/run-format.md`: answer verbatim, the SQL, the chat link, the classification, and whether it stated population, period and definition.

What a good result looks like: on 28 October, the question "How do we stop different teams getting different numbers for the same metric?" returned "PIECE, if the test covers five metrics", and Dot's answer to the first test question stated the number, the population (delivered orders), merchandise value only, and the order count. The whole run took 13 minutes. That run used the earlier Claude Project set-up, by hand; the subagents haven't yet been timed.

## 3. Running a full piece

Follow the runbook in `README.md`: eleven steps, four decisions. The full step-by-step guide is `guides/Dot-Run-a-Full-Piece.pdf`. It was written for the earlier Claude Project set-up; its steps hold, but where it says to paste into the Project, use the subagent or prompt the runbook names.

Things to know:

- **READER and the first fact-check run outside this repo**, in a fresh chat with only the draft: READER (`04-reader.md`) and the first fact-check (`05-fact-check.md`). A Claude Code session here loads `CLAUDE.md` automatically, and the reviewer must not know what the writer meant. Use a fresh claude.ai chat, or Claude Code started in an empty folder. The second fact-check runs in a different model (ChatGPT).
- **The plan binds the run.** If `PLAN.md` has a section naming a piece's slug, the researcher reads it as input 5, and its test questions must meet that section's run needs; `/piece`'s truth stage stops, blocked, if they don't. To steer a future piece, write its section in `PLAN.md`, naming the slug, before Decision 1.
- **Every number needs a row** in the piece's `figures/` CSV before the checker will pass it. Add rows as you go, not at the end.
- **Log the run conditions before the first question of every batch.** Take the five screenshots in Dot's UI (`runs/README.md#screenshots`): mode, credits before, environment, context notes, then credits after the batch. `dot-runner` writes the paths into the run file; you record the values in the Run Log. The mode drifted twice during the trial; the screenshot is the fix.
- **Batches.** `dot-runner` fits about 13–14 questions in one call. Longer runs are split into numbered batches, each with its own five screenshots (`runs/README.md#batches`).

Gate: `python scripts/check_piece.py pieces/<piece>.md`. Fix every FAIL; do the six human checks; then Decision 4.

## 4. The monthly loop (one owner, about 20 minutes a week)

- **Week 1:** read the Baseline tab's measures and add a dated column: Search Console, Rank Tracker, the AI-responses panel, the three Perplexity prompts (recorded in `measure/citations.md`).
- **Week 2:** add new questions from sales calls and Search Console to the question bank.
- **Week 3:** turn any fix made twice into a rule in `CLAUDE.md`, with a dated line in its change log. Claude Code picks it up at the next session.
- **Week 4:** re-run past evaluations in Dot; pick the next question.

Ahrefs access ended on 31 October 2026, so weeks 1 and 4 can't read Ahrefs until it returns. `data/ahrefs/README.md` says how to reconnect it and where new readings go.

## 5. What's still open

| Item | Why it matters | What closes it |
|---|---|---|
| Phone read of each piece (check 24) | The last human check | Read each aloud once on a phone |
| Piece 1's evaluation on Dot's data | The trial used Olist, licensed non-commercial | Re-create the 20 rows in a Dot workspace |
| Assumptions A1–A8 | Each is labelled in the text | A yes, no or change from Dot |
| A clean Balanced batch for piece 3 | The Balanced figure is from a mixed batch | Ten questions, all Balanced, credits read before and after |
| Time per piece | Never logged | Time the next piece, stage by stage |
| The question bank | `bank/questions.csv` holds all 102 questions; they haven't been re-ranked with sales-call questions | Re-rank it with ten sales-call questions |
| `scripts/mark_run.py` and `scripts/ground_truth_from_spec.py` | Named by `dot-runner` and `researcher`, but not yet written | Write both against `facts/run-format.md` |
| Stages 2–7 in Claude Code | Only RESEARCH and the run are subagents | Decide skill or subagent for each |
| The subagents on a real question | Neither has run yet | Section 2 |
| No chart stage in the workflow | The draft references a chart, but no stage makes it; `check_piece.py` checks the markdown, not the image file, so a missing chart passes. Found on ai-analyst-follow-up-questions, 31 October 2026, and made by hand with `scripts/charts.py` | Add a chart stage after seo-geo, and have `stage_gate.py` require every referenced image to exist |
| Ahrefs access | Ended 31 October 2026 | Reconnect, per `data/ahrefs/README.md` |
| The Python on a new machine | The scripts need a Python with `requirements.txt` installed. On the author's machine they run because `C:\Python314` has them in the user site-packages and the skills don't use `-I`, which would hide that folder | Install the requirements into whichever `python` comes first on PATH, and check with `python -c "import pandas, matplotlib, docx"` |
| Pieces older than run files | Pieces 1–3 have no `runs/<piece>-run.md`, so the fact-checker can't check their Dot quotes word for word. It is told to say so plainly, not treat them as checked | Re-run their questions with `dot-runner` if a piece is to be republished |
| Nobody but the author has run it | The core claim about the machine | Section 2, then one full piece |

## Found while writing: Dot's own accuracy claim

Found on 31 October 2026 while writing the teardown `how-companies-test-ai-data-analysts`, whose finding is that published accuracy figures can't be compared unless they were measured on the same tasks. Recorded so Dot can decide what, if anything, to change; nothing on Dot's site was changed.

- **Dot's home page and its impact page** (https://www.getdot.ai/ and https://www.getdot.ai/impact) carry a section headed "Benchmarked on 450+ financial analysis tasks from Adyen". Its chart sets Dot beside "Google Data Science Agent · ~52% weighted overall (Nov 2025)" and a "Human baseline from DABStep: 62% accuracy with 3+ hrs of work on easy tasks." The section doesn't state Dot's own percentage or which tasks Dot ran.
- **Dot's DABstep post** (https://www.getdot.ai/blog/from-10-to-90-percent-on-adyens-dabstep) gives the figure: "90% accuracy, reproduced on the public Hugging Face leaderboard", on "The assigned slice … 30 representative tasks drawn from the public DABstep benchmark". Its chart reads "14 versions · 30 tasks each" and "90%: assigned slice peak"; the post doesn't mention a held-out set. The headline's 10% isn't explained in the text, whose nearby figures are "about 30%" and "~15% Original SOTA DABstep paper".
- **Why it matters:** a heading that reads as 450+ tasks, a Dot figure from 30 tasks, a competitor's figure from the full benchmark, and a human figure from easy tasks only are four different test sets on one chart. That is the comparison the teardown says can't be made. A reader who checks will find it.
- **What would make the claim hold:** state the slice on the home page ("90% on a 30-task slice of DABstep"), or run Dot on the full public set and publish that figure beside Google's.
- All three pages were read through WebFetch, which returns a model's reading of the page; check the quotes against the live pages before acting on them.

## Recommendations for Dot, and roadmap items not adopted

From the roadmap update of 31 October 2026, decided by Saurabh.

- **Byline, a recommendation for Dot.** The roadmap cites evidence that content with a named author is cited about 2.3x more than anonymous content. The pieces carry a reviewed-on date (hard rule 22) but no named author: Rick did not run these tests, and who bylines a piece is Dot's decision. Check 19 forbids a byline nobody approved. If Dot names an author, add the field and drop that sentence from rule 22.
- **Not adopted: the roadmap's skill names** (`/make-piece-plan`, `make-piece-write.js`, `/gate`). The machine already does the same jobs as `/piece`, `.claude/workflows/piece.js` and `scripts/stage_gate.py`; renaming would cost time and risk breaking references without changing what they do.
- **A future piece: example test questions.** Readers of the teardown expected a bank of test questions they could copy. The census names where published examples are likely (LinkedIn's paper, ClickHouse's open-source test harness); about an hour of reading, with every question checked word for word, would produce them. Kept out of the teardown, which promises a census, not a question bank (Saurabh, 31 October 2026).
- **FAQ schema kept, not demoted (Saurabh, 31 October 2026).** The roadmap demotes FAQ schema because it shows no measurable lift for pages already visible in AI answers. These pieces aren't visible yet, and an FAQ file costs nothing, so `/seo-geo` still writes one where it is earned. Revisit once a piece shows up in AI answers: then the roadmap's reason applies.
- **Not adopted: the fact-checker's confirmed-claims list.** `facts/dot-facts.md` already has Confirmed and Observed tables; a second list in the fact-checker's memory would duplicate them. Confirmed product claims go in `facts/dot-facts.md`.

## 6. Accounts and tools you need

Claude Code · Dot (a workspace with the Olist tables or your own data, connected through the `ask_dot` MCP) · Ahrefs (the Getdot project; Rank Tracker already holds 18 keywords; access ended 31 October 2026) · Perplexity and ChatGPT (free plans are enough) · Google Sheets (the tracking sheet) · Python 3.10+ for the scripts.
