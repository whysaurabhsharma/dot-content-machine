# The three-piece plan

Rewritten 31 October 2026, after Saurabh chose the three pieces (A, B and F below). Where each piece actually stands is read from the files by `python scripts/stage_gate.py <slug>`. A section here that names a piece's slug binds its research (`.claude/agents/researcher.md`, input 5).

## The cluster

One buyer worry: **can I trust an AI analyst's answers before I roll it out?** Three formats, three kinds of evidence (CLAUDE.md, "What this machine makes", v1.7):

| # | Piece | Format | Bank | Evidence | What it gives the reader |
|---|---|---|---|---|---|
| A | `ai-analyst-follow-up-questions`, "Your AI Analyst Picked a Date. Only the SQL Said Which." | Research | #43 | Our own run (31 October 2026, 8 answers) | The problem, proved on our data: a right answer to a question you didn't mean, and a six-step test that shows which date was used |
| B | `how-companies-test-ai-data-analysts`, working title "How N Companies Test Their AI Data Analyst" | Teardown | #36 ("AI data analyst test questions"; swapped from #35, 31 October 2026) | Other organisations' published evaluation methods, primary sources only (hard rule 4's cited-publication exception) | What others actually do to test their analyst, in one census, and the patterns it shows |
| F | `test-ai-analyst-before-rollout`, working title "How to Test an AI Analyst Before Rollout" | Guide | #35 ("how to evaluate AI data analyst accuracy", demand 3), **the hub** | B's census (cited publications) and our runs (A's, and piece 2's archived run) | How to do it: the steps, each backed by a run or a publication, or labelled untested (hard rule 19) |

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
- **When F exists:** B's opening ends by pointing at F as where the method lives (link the five "methods to start from" to F), and F links back to B's census. B makes no promise about the reader's own questions; that is F's job (Saurabh, 31 October 2026).
- **Before publishing: Rick signs off the context agent claim** in "Where Dot fits": Dot's context agent page (https://www.getdot.ai/context-agent) says "Merging re-checks accuracy first: Dot answers its 25 questions again and merges at 95% or more." It sits in the page's top product panel, an illustration, and the page doesn't describe the process further or say what happens below 95%. The piece quotes it as Dot's stated behaviour, not as something we observed (hard rule 5).
- **Before publishing: Rick signs off the DABstep concession** in the first section ("Dot publishes an accuracy figure too: 90% on a 30-task slice of Adyen's public DABstep benchmark…"); it is a product claim (hard rule 5). See also HANDOVER.md, "Found while writing".
- **Before publishing:** re-check facts O1 and O2 (Dot's evaluation: expected answer, unit, tolerance, verdict; re-scoring on save) on the current account, since both were observed on the dry-run account on 27 October 2026; and re-read in a browser the numbers the draft uses, since every source was read through WebFetch.

### F, `test-ai-analyst-before-rollout`: guide

- **Section 7 of the research: evidence for each step.** Each step, and the publication from B's census or the run of ours behind it, or "untested".
- **Our runs it may cite:** A's run, and piece 2's archived run (`runs/ai-analyst-shows-sql-run.md`: 6 questions in two fresh chats each, 12 of 12 correct; the late-delivery question returned 2,878 and 2,453). Piece 2's conditions were recorded by hand with rule 14 waived, so no claim about mode, credits, environment or notes may rest on it.
- **Shape:** 1,000–1,900 words; five to nine numbered steps, each starting with a verb; pocket guide, caveats, "Where Dot fits", CTA.
- **Depends on B:** F's steps cite B's census, so B's research comes first.
- **Bank:** #35, the how-to query (swapped from #36 on 31 October 2026). F is the cluster's hub: it links to A and B as its evidence, and both link back to it once it exists.

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
| 3 | The failure taxonomy | B | The 8 that don't clear the strict bar, and what each is missing |
| 4 | The contrarian read | F | You don't need 50–100 test questions (only if F's evidence supports it) |
| 5 | The checklist | F | The guide's own steps |
| 6 | The build log | A | `runs/ai-analyst-follow-up-questions-timing.csv` and what the run took (no credits figure: rule 14 was waived for A's run) |

Post 1 of 6 already exists (A, "the checklist", in `posts/ai-analyst-follow-up-questions-posts.md`); it is rewritten or relabelled to fit this table when `/linkedin` is updated (tier 3, with `check_posts.py` and `posts/queue.csv`). A person writes every first line.

## Order

1. B: Decision 1, research (the census and its count), then go or no-go.
2. If go: B's figures, outline (Decision 2), draft, reviews, Decision 3.
3. F: Decision 1 on #35, research citing B, then the same stages.
4. Five more LinkedIn posts: one for A, two each for B and F.
5. Handover.

## Decisions that stay human

The question (Decision 1), the outline (Decision 2), the title and human checks (Decision 3), the publish (Decision 4); B's go or no-go (go: 13 on the wider bar); a licence decision for F if it cites Olist-derived figures.
