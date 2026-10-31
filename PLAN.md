# The three-piece plan

Rewritten 31 October 2026, after Saurabh chose the three pieces (A, B and F below). Where each piece actually stands is read from the files by `python scripts/stage_gate.py <slug>`. A section here that names a piece's slug binds its research (`.claude/agents/researcher.md`, input 5).

## The cluster

One buyer worry: **can I trust an AI analyst's answers before I roll it out?** Three formats, three kinds of evidence (CLAUDE.md, "What this machine makes", v1.7):

| # | Piece | Format | Bank | Evidence | What it gives the reader |
|---|---|---|---|---|---|
| A | `ai-analyst-follow-up-questions`, "Your AI Analyst Picked a Date. Only the SQL Said Which." | Research | #43 | Our own run (31 October 2026, 8 answers) | The problem, proved on our data: a right answer to a question you didn't mean, and a six-step test that shows which date was used |
| B | `how-companies-test-ai-data-analysts`, working title "How N Companies Test Their AI Data Analyst" | Teardown | #36 (#35 is marked drafted by the archived trial) | Other organisations' published evaluation methods, primary sources only (hard rule 4's cited-publication exception) | What others actually do to test their analyst, in one census, and the patterns it shows |
| F | `test-ai-analyst-before-rollout`, working title "How to Test an AI Analyst Before Rollout" | Guide | #35, the only demand-3 question in the bank | B's census (cited publications) and our runs (A's, and piece 2's archived run) | How to do it: the steps, each backed by a run or a publication, or labelled untested (hard rule 19) |

**How they compound:** B shows what others do; F turns it into steps; A proves the core step on our own data. B and F need no new Dot run, which also keeps the Olist licence question (facts L1) to A and to whatever F cites from our runs.

## What each piece needs

### A, `ai-analyst-follow-up-questions`: done

Through the gate. Decision 4 (publish) is open. Licence: decision L1, not a resolution.

### B, `how-companies-test-ai-data-analysts`: teardown

- **Section 7 of the research: a census of organisations that published how they test their AI analyst.** For each: the primary publication, opened and read in full (never Dot's teardown of it, never a summary); who published it and when; the method in their words; every number copied exactly.
- **The bar for an entry:** a real published evaluation method, meaning what they test against, how they score, and when they run it, not a passing mention of accuracy.
- **Go or no-go:** five or more organisations meet the bar, or B is not a piece and a different third piece is chosen (Saurabh, 31 October 2026).
- **Shape (style rules 1 and 5):** 1,000–1,600 words; one census table, one row per publication, each row linking its primary source; pocket guide, "Things to keep in mind", "Where Dot fits", CTA.
- **Figures:** every number a `published: <URL>, read <date>` row (hard rule 3). None combined with our own figures (rule 4, condition d).

### F, `test-ai-analyst-before-rollout`: guide

- **Section 7 of the research: evidence for each step.** Each step, and the publication from B's census or the run of ours behind it, or "untested".
- **Our runs it may cite:** A's run, and piece 2's archived run (`runs/ai-analyst-shows-sql-run.md`: 6 questions in two fresh chats each, 12 of 12 correct; the late-delivery question returned 2,878 and 2,453). Piece 2's conditions were recorded by hand with rule 14 waived, so no claim about mode, credits, environment or notes may rest on it.
- **Shape:** 1,000–1,900 words; five to nine numbered steps, each starting with a verb; pocket guide, caveats, "Where Dot fits", CTA.
- **Depends on B:** F's steps cite B's census, so B's research comes first.
- **Bank:** #35 is marked "drafted" by the archived trial piece, so `stage_gate.py start` will refuse it until a person decides its status.

## Not chosen, and why (for the handover)

| Candidate | Format | Why not |
|---|---|---|
| C, "Your Metric Definitions Have Back Doors" | Essay | Its idea overlaps A. Kept as one of the five future topics. |
| D, "The Definition Is in the SQL" | Essay | Overlaps A ("only the SQL said which"). |
| E, "What to Write Down Before Your AI Analyst Answers" | Guide | Needs piece 3's two Dot batches; the same run as G. |
| G, "Does Writing It Down Change the Answer?" | Research | The same run as E, published as findings. |
| H, "Text-to-SQL Benchmarks Don't Measure Your Questions" | Explainer | Not chosen; overlaps the DABstep post. |
| Piece 2 as research, "Your AI Analyst Counted Late Orders Two Ways" (#41) | Research | A second test-result piece: one format twice. Archived; its run is kept as evidence for F. |
| Piece 3 as planned, "how much context" (#47) | Research | Replaced by the format plan; never run. Archived. |

## Order

1. B: Decision 1, research (the census and its count), then go or no-go.
2. If go: B's figures, outline (Decision 2), draft, reviews, Decision 3.
3. F: Decision 1 (after #35's status is settled), research citing B, then the same stages.
4. Five more LinkedIn posts: one for A, two each for B and F.
5. Handover.

## Decisions that stay human

The question (Decision 1), the outline (Decision 2), the title and human checks (Decision 3), the publish (Decision 4); B's go or no-go; #35's bank status; a licence decision for F if it cites Olist-derived figures.
