# The three-piece plan

Written 31 October 2026, after Saurabh chose the three pieces (A, B and F below). Rewritten 1 November 2026 as a record of that plan, now that the pieces are through it, and as the place to plan the next piece. Where each piece stands is read from the files by `python scripts/stage_gate.py <slug>`, not from here.

## How this file is used: shaping a new piece's research

**To shape a new piece's research, add a section here named by its slug** (for example `### C, metric-definitions-back-doors`). Put in it what the research must deliver: for a research piece, the questions, phrasings, repeats and chats the run needs; for a teardown, the census bar and the go/no-go count; for a guide, which runs or publications each step may rest on. The researcher reads this file as input 5 (`.claude/agents/researcher.md`), and `/piece` checks the research against it (`.claude/workflows/piece.js`): a section naming the slug binds the research's section 7, and a research file that doesn't meet it stops as blocked. A piece with no section here is researched from its bank row alone.

Write the section before Decision 1's research starts, and leave it once the research is done: the research file records which section it followed. The sections for B and F below are kept for that reason.

## The cluster

One buyer worry: **can I trust an AI analyst's answers before I roll it out?** Three formats, three kinds of evidence (CLAUDE.md, "What this machine makes", v1.7):

| # | Piece | Format | Bank | Evidence | What it gives the reader |
|---|---|---|---|---|---|
| A | `ai-analyst-follow-up-questions`, "Your AI Analyst Picked a Date. Only the SQL Said Which." | Research | #43 | Our own run (31 October 2026, 8 answers: all correct, 5 under the definition asked, 3 (Q6, Q7, Q8) only under the delivery-date reading) | The problem, proved on our data: a right answer to a question you didn't mean, and a six-step test that shows which date was used |
| B | `how-companies-test-ai-data-analysts`, "7 Companies Published Their AI Analysts' Accuracy. No Two Measured the Same Thing." (working title "How N Companies Test Their AI Data Analyst") | Teardown | #36 ("AI data analyst test questions"; swapped from #35, 31 October 2026) | Other organisations' published evaluation methods, primary sources only (hard rule 4's cited-publication exception) | What others actually do to test their analyst, in one census, and the patterns it shows |
| F | `test-ai-analyst-before-rollout`, "How to Test an AI Data Analyst Before Rollout: 8 Steps" (working title "How to Test an AI Analyst Before Rollout") | Guide | #35 ("how to evaluate AI data analyst accuracy", demand 3), **the hub** | B's census (cited publications) and our runs (A's, and piece 2's archived run) | How to do it: the steps, each backed by a run or a publication, or labelled untested (hard rule 19) |

**How they compound:** B shows what others do; F turns it into steps; A proves the core step on our own data. B and F needed no new Dot run, which kept the Olist licence question to A and to what F cites from our runs. Dot has since confirmed it may publish figures from the Olist dataset (`facts/dot-facts.md`, L-OLIST).

## What the plan bound for B's and F's research

A's run was done before this plan was written, so A has no section. The two below are what B's and F's research files followed (each cites "PLAN.md, section B" or "section F").

### B, `how-companies-test-ai-data-analysts`: teardown

- **Section 7 of the research: a census of organisations that published how they test their AI analyst.** For each: the primary publication, opened and read in full (never Dot's teardown of it, never a summary); who published it and when; the method in their words; every number copied exactly.
- **The bar for an entry:** a real published evaluation method, meaning what they test against, how they score, and when they run it, not a passing mention of accuracy.
- **Go or no-go:** five or more organisations meet the bar, or B is not a piece and a different third piece is chosen (Saurabh, 31 October 2026). Result: go, 13 on the wider bar.
- **Shape (style rules 1 and 5):** 1,000–1,600 words; one census table, one row per publication, each row linking its primary source; pocket guide, "Things to keep in mind", "Where Dot fits", CTA.
- **Figures:** every number a `published: <URL>, read <date>` row (hard rule 3). None combined with our own figures (rule 4, condition d).
- **Links with F:** B's opening ends by pointing at F as where the method lives, and F links back to B's census. B makes no promise about the reader's own questions; that is F's job (Saurabh, 31 October 2026).

The pre-publish checks this section once listed are now recorded elsewhere: the context agent quote is DECISIONS-FOR-DOT.md question 1 (fact P-1), the DABstep concession is question 2, and Dot's evaluation (fact O1) was confirmed as current by Rick on 1 November (question 3, fact P-2). Every number B uses was re-read in a browser (`runs/how-companies-test-ai-data-analysts-verification.md`).

### F, `test-ai-analyst-before-rollout`: guide

- **Section 7 of the research: evidence for each step.** Each step, and the publication from B's census or the run of ours behind it, or "untested".
- **Our runs it may cite:** A's run, and piece 2's archived run (`runs/ai-analyst-shows-sql-run.md`: 6 questions in two fresh chats each, 12 of 12 correct, but only 9 under the definition asked: 3 (Q2, Q5, Q8) were correct only under the answer's own stated rival definition; the late-delivery question returned 2,878 and 2,453). Piece 2's conditions were recorded by hand with rule 14 waived, so no claim about mode, credits, environment or notes may rest on it.
- **Shape:** 1,000–1,900 words; five to nine numbered steps, each starting with a verb; pocket guide, caveats, "Where Dot fits", CTA.
- **Depends on B:** F's steps cite B's census, so B's research came first.
- **Bank:** #35, the how-to query (swapped from #36 on 31 October 2026). F is the cluster's hub: it links to A and B as its evidence, and both link back to it.

## Not chosen, and why

| Candidate | Format | Why not |
|---|---|---|
| C, "Your Metric Definitions Have Back Doors" | Essay | Its idea overlaps A. Kept as one of the five future topics. |
| D, "The Definition Is in the SQL" | Essay | Overlaps A ("only the SQL said which"). |
| E, "What to Write Down Before Your AI Analyst Answers" | Guide | Needs piece 3's two Dot batches; the same run as G. |
| G, "Does Writing It Down Change the Answer?" | Research | The same run as E, published as findings. |
| H, "Text-to-SQL Benchmarks Don't Measure Your Questions" | Explainer | Not chosen; overlaps the DABstep post. |
| Piece 2 as research, "Your AI Analyst Counted Late Orders Two Ways" (#41) | Research | A second test-result piece: one format twice. Archived; its run is kept as evidence for F. |
| Piece 3 as planned, "how much context" (#47) | Research | Replaced by the format plan; never run. Archived. |

## B's reframe, 31 October 2026 (after its first headline test failed)

- **The finding:** "Seven of the 13 companies published an accuracy figure, and no two measured the same thing." A correction, not an inventory: a reader comparing vendor accuracy claims can't, and the five copyable methods are what she does instead. It also gives F, the guide, its reason to exist.
- **Checked and rejected as the lead:**
  - "None of the 13 published a result": false. 7 did (C-9).
  - Anthropic's ~95% to ~65% drift in a month: true, but Dot already published it in Rick's essay "Your AI Analyst Will Be Worse Next Month" (bank #39 is covered). Leading with it would republish his finding. B keeps one sentence on it, linked to his essay, as support for its third lift line.
- **Kept:** only Anthropic publishes a launch bar (C-8), in the pocket guide and the re-run section.
- **Added:** a section where Dot ran the method's core, from piece A's run. Its point is that the method is runnable, not that our result confirms anyone's; our numbers never sit beside the census's (rule 4, condition d).
- **Publish order:** A before B. B links to A's URL, which fails the link check until A is live.

## LinkedIn: six posts, six structures, rotated across the cluster

A deliberate change from the roadmap update (31 October 2026). Its post model draws every post from a piece's run files and assumes every piece is research. This cluster is deliberately three formats, and only A has a run file, so the six structures are assigned across the cluster rather than per piece:

| # | Structure | Piece | Drawn from |
|---|---|---|---|
| 1 | The number | B | 13 organisations clear the wider bar, 5 the strict one (figures C-1, C-2) |
| 2 | The transcript | A | A verbatim Dot answer from `runs/ai-analyst-follow-up-questions-run.md` |
| 3 | The failure taxonomy | B | The 7 that don't clear the strict bar (8 until Ramp was added, 1 November), and what each is missing |
| 4 | The contrarian read | F | You don't need 50–100 test questions (only if F's evidence supports it) |
| 5 | The checklist | F | The guide's own steps |
| 6 | The build log | A | `runs/ai-analyst-follow-up-questions-timing.csv` and what the run took (no credits figure: rule 14 was waived for A's run) |

All six posts were written to this table (`posts/<slug>-posts.md`); the publishing order is in STATUS.md. The `/linkedin` skill still lists its older five structures, so a new piece's posts take their structure from a table like this one until the skill is updated. A person writes every first line.

## Decisions that stay human

The question (Decision 1), the outline (Decision 2), the title and human checks (Decision 3), the publish (Decision 4), and, for a teardown, the go or no-go on the census count (CLAUDE.md, "The seven stages").
