# Handover: the Dot content machine

Written 28 October 2026 for Rick and Théo. Rewritten 31 October 2026 for Claude Code. Rewritten again 1 November 2026 around what was delivered. Everything here works from the files in this repo; nothing depends on the author's accounts.

## 0. In one page

**What this is.** A repo that turns a buyer's question into an evidence-led blog piece for getdot.ai, with every number checked against a file and every rule enforced by a script. It runs in Claude Code. `CLAUDE.md` is the rulebook (v1.8.10, every change dated in its change log).

**What was delivered.** One cluster of three pieces on one buyer worry: *can I trust an AI analyst's answers before I roll it out?*

| Piece | Format | Where it stands |
|---|---|---|
| A · `ai-analyst-follow-up-questions` | Research: our own run in Dot | Through Decision 3 and exported. Waits on Decision 4. 2 posts |
| B · `how-companies-test-ai-data-analysts` | Teardown: a census of 13 companies | Through Decision 3 and exported. Waits on Rick's sign-offs, three census corrections, then Decision 4. 2 posts |
| F · `test-ai-analyst-before-rollout` | Guide: the cluster's hub | Through Decision 3 and exported. Waits on A and B going live. 2 posts |

All six LinkedIn posts exist, first lines by Saurabh. Exports are in `exports/<slug>/` (a .docx and clean Markdown each; the folder is not in git). Current state, in two minutes: `STATUS.md`.

**What Rick needs to do:** answer the seven questions in `DECISIONS-FOR-DOT.md`, ordered by what blocks publication. Section 8 has the detail.

**SEO and answer-engine choices, and the LinkedIn adaptation:** section 11. **A five-minute demo script:** `DEMO-SCRIPT.md`.

**Where to start reading:** this file, then `CLAUDE.md`, then `PLAN.md` (the cluster), then any piece in `pieces/` beside its `figures/` file and its `reviews/` folder.

## 1. The three pieces, and why these three

**One worry, three kinds of evidence.** A buyer asks whether an AI analyst's answers can be trusted before rollout. Each piece answers it with a different kind of evidence (`CLAUDE.md`, "What this machine makes"):

- **A, research.** Our own run in Dot on the Olist dataset, 31 October 2026, 8 questions. Finding: the phrase "delivered in 2017" got two correct answers, 2,453 and 1,762, because one chat read it as purchase date and the other as delivery date. Only the SQL said which. Score, item by item: all 8 correct, 5 under the definition asked and 3 (Q6, Q7, Q8) only under the delivery-date reading. Bank #43.
- **B, teardown.** What 13 companies published about how they test their own AI analyst, one table, every row linked to the company's own post. Finding: 7 published an accuracy figure, and no two measured the same thing. 5 published enough to copy (test set, scoring and timing). Bank #36.
- **F, guide.** Steps a reader follows to test before rollout. Each step rests on B's census, on our runs (A, and archived piece 2), or is labelled untested (hard rule 19). F links to A and B; both link back. Bank #35.

The bank rows for all three now read `drafted` (`bank/questions.csv`).

**Rejected candidates** (from `PLAN.md`):

| Candidate | Format | Why not |
|---|---|---|
| C, "Your Metric Definitions Have Back Doors" | Essay | Overlaps A. Its idea is folded into future topic #44 (section 4) |
| D, "The Definition Is in the SQL" | Essay | Overlaps A ("only the SQL said which") |
| E, "What to Write Down Before Your AI Analyst Answers" | Guide | Needs piece 3's two Dot batches, never run |
| G, "Does Writing It Down Change the Answer?" | Research | The same run as E |
| H, "Text-to-SQL Benchmarks Don't Measure Your Questions" | Explainer | Overlaps Dot's DABstep post |
| Piece 2, "Your AI Analyst Counted Late Orders Two Ways" (#41) | Research | A second test-result piece: one format twice. Archived; its run is kept as evidence for F. Its score, item by item: 12 of 12 correct, 9 under the definition asked and 3 (Q2, Q5, Q8) only under the answer's stated rival definition |
| Piece 3, "how much context" (#47) | Research | Replaced by the three-format plan; never run. Archived |

**B's reframe.** B's first title, "13 Companies Test Their AI Analyst. 5 Show How.", failed the headline test: an inventory, not a finding. Rejected leads: "none of the 13 published a result" (false, 7 did) and Anthropic's drift from about 95% to about 65% (true, but Dot's own essay already leads with it). The kept finding is the comparison problem.

## 2. What each piece cost

**Logged stage minutes**, summed by script from each `runs/<slug>-timing.csv`. These are the minutes a stage's skill or agent was running, not the elapsed day.

| Piece | Logged minutes | Wall clock (first to last log) | Largest stages |
|---|---|---|---|
| Bank build (102 questions scored) | 19.9 | 31 Oct, 11:08–11:28 | — |
| A (research) | 26.9 | 31 Oct, 12:36–16:36 (4.0 h) | revise 8.1, reviews 5.4, run 5.1 |
| Piece 2 (archived research) | 25.6 | 31 Oct, 17:00–17:59 | run 10.2, reviews 3.7 |
| B (teardown) | 47.0 | 31 Oct 18:47 – 1 Nov 00:04 (5.3 h) | revise 13.7, research 10.9, reviews 7.7, figures 6.7 |
| F (guide, so far) | 10.5 | 1 Nov, 00:08–00:24 | figures 6.1 (backfilled), research 2.9, outline 1.5 |

**What the logs don't cover, plainly:**

- **A person's time is not logged:** the four decisions, the headline tests, the phone reads, the fact-check triage. That is most of the elapsed time.
- **B's revision rounds 4 to 8 are not logged.** Only two revise stages are in its timing file; rounds 4–8 are in `reviews/how-companies-test-ai-data-analysts/revisions.md` with no times.
- **A's posts, phone reads and later fixes after 16:36** are not logged.
- **F's figures stage was not logged.** It is backfilled from two commit times and marked so in the file. It is an upper bound: the interval also holds reading the roadmap document for this handover.

So these figures are a floor, not the cost.

**Credits** (Dot usage), from readings taken by hand because rule 14's screenshots were waived for both runs. Internal only: under the waiver these may not appear in a published piece.

| Piece | Credits | Basis |
|---|---|---|
| A | 3.0 | 87.6 → 90.6 of 300 used (`runs/ai-analyst-follow-up-questions-run.md`) |
| Piece 2 | 7.1 | 90.6 → 97.7 of 300 used (`runs/ai-analyst-shows-sql-run.md`) |
| B | 0 | No Dot run |
| F | 0 so far | No Dot run; it cites A's and piece 2's runs |

In dollars, **assumption A2** (1 credit ≈ $1, not stated on any Dot pricing page) gives about $3.00 for A and $7.10 for piece 2.

## 3. Running the machine

### Set it up in Claude Code (10 minutes)

`CLAUDE.md` is the rulebook. Claude Code reads it automatically whenever it starts in this folder.

1. Clone the repo and open a terminal in it.
2. Install the scripts' packages: `python -m pip install -r requirements.txt`. Check with `python -c "import pandas, matplotlib, docx; print('ok')"`.
3. Connect Dot's MCP, once per machine: `claude mcp add --transport http ask_dot https://app.getdot.ai/ai/mcp`
4. Run `claude` in the folder. Type `/mcp`, choose `ask_dot`, and sign in to your Dot workspace.
5. Check the rules loaded: ask *"What are the four human decisions?"* It should answer: the question, the outline, the title, the publish.
6. Check the agents loaded: type `/agents`. You should see `researcher`, `dot-runner`, `reader`, `fact-checker` and `lift-tester`.

### A 30-minute first test

It follows the gate's order. At any point, `python scripts/stage_gate.py test-1` says what comes next. (Rewritten 1 November 2026: the earlier version skipped Decision 1 and the truth spec, which the gate requires before a run; a cold-start test found it.)

1. **Decision 1.** Pick a question (`python scripts/bank.py top`, or any unwritten row whose evidence a person has confirmed), then record it: `python scripts/stage_gate.py start test-1 --bank <id> --format research`. If it isn't the top row, add `--why "<reason>"`; the reason is kept in the manifest.
2. **Research.** First `python scripts/timing.py test-1 research start`. Then *"Use the researcher agent on bank #<id>, piece slug test-1."* It checks the workspace against `facts/dot-workspace-setup.md` with `get_catalog` and writes `runs/test-1-research.md`. Then `python scripts/timing.py test-1 research end` (the researcher can't time itself).
3. **Read the verdict:** PIECE, PIECE IF, NOT A PIECE, or NOT A PIECE, BUT A SURFACE. For **PIECE IF**, check the condition yourself, then record it: `python scripts/stage_gate.py clear test-1 --by "<name, date>" --basis "<how it was met>"`. The gate waits until you do.
4. **Truth spec.** Write `specs/test-1-truth.json` from the research's test questions, including every rival reading of an ambiguous phrase, then `python scripts/ground_truth_from_spec.py specs/test-1-truth.json`. A person reads the rival definitions and adds `"reviewed_by": "<name, date>"`. No run starts before this.
5. **Batch conditions in Dot's own UI:** mode, environment, context notes, credits before, as `## Batch 1: conditions` in `runs/test-1-run.md`, with the screenshots named as in `runs/README.md#screenshots`. Mode, credits, environment and context notes can't be seen through the MCP.
6. **Run.** *"Use the dot-runner agent on test-1, batch 1, first question only."* It asks Dot word for word and appends the answer to `runs/test-1-run.md`.
7. **Check the entry** against `facts/run-format.md`.

### A full piece, on one command

1. **Decision 1.** Pick the question (`/bank top`), confirm its evidence score, then record it: `python scripts/stage_gate.py start <slug> --bank <id> --format research|teardown|guide`.
2. **Run `/piece <slug>`.** It asks `scripts/stage_gate.py` where the piece stands, runs that one stage, and asks again.
3. **It stops** when the gate needs a person (section 7 lists the stops), when something is blocked, or after two fix rounds that leave a FAIL.
4. **Do what it names**, then run `/piece <slug>` again. Where a piece stands is read from the files, so a new session picks up where the last one stopped.

Things to know:

- **The three formats.** A teardown or guide has no run of its own: the gate skips truth, run and mark, and asks for a figures stage instead.
- **Blind reviewers.** READER, the first fact-check and the lift test are subagents started only through `scripts/run_reviewer.py`, which gives them the draft and nothing else. The second fact-check runs in a different model (ChatGPT, Gemini) outside this repo.
- **Every number needs a row** in the piece's `figures/` CSV before `check_piece.py` passes it.
- **Waiving the screenshots (v1.8.9, 1 November 2026).** A waiver is a recorded state, not a flag. A person states it in the batch's conditions block in a line starting `**Rule 14 waived`, then runs `python scripts/stage_gate.py waive <slug> --rule 14 --batch <n> --by "<name, date>"` once. The gate reads it on every call. The cost: no claim about mode, credits, environment or context notes in that piece.
- **Scores are split (v1.8.10).** `scripts/mark_run.py` prints how many answers were correct under the definition asked and how many only under another reading. Quote both, never the total alone.
- **Gate:** `python scripts/check_piece.py pieces/<slug>.md` runs the 25 checks. `python scripts/verify_sources.py pieces/<slug>.md` opens every link.

### The monthly loop (one owner, about 20 minutes a week)

- **Week 1:** take the month's readings (section 5).
- **Week 2:** add new questions from sales calls and Search Console to the bank.
- **Week 3:** turn any fix made twice into a rule in `CLAUDE.md`, with a dated change-log line.
- **Week 4:** re-run past evaluations in Dot; pick the next question.

## 4. Five future topics, from the bank

One per bank row, from `bank/questions.csv` (scores: demand · gap · incumbent · evidence, each 1–3).

| # | Buyer question | Total | Evidence | What it would need |
|---|---|---|---|---|
| #29 | Finance and sales report different revenue. How do I find out why and stop it recurring? | 9 | 2, confirmed by a person | A Dot run tracing two revenue definitions through their SQL |
| #37 | What accuracy should I expect on real business questions, not academic benchmarks? | 9 | 3, not yet confirmed | A person confirms the score; then an evaluation run on Olist business questions (fact O1) |
| #42 | What does a good AI analyst do when the question is ambiguous, like "best month"? | 9 | 3, not yet confirmed | A person confirms the score; builds on fact O4 (answers state their basis; 3 of 29 asked back) |
| #47 | How much documentation is enough? Can I start with ten definitions? | 8 | 3, confirmed by a person | Archived piece 3's two-batch design, ready to run (`archive/runs/ai-analyst-how-much-context-research.md`). Essay C's idea, that metric definitions have back doors, belongs here or with #44 ("What metric definitions do I need to write before an AI analyst answers anyone?", total 8, evidence 1), which needs customer proof we don't hold |
| #4 | What share of a typical data team's requests are repeat lookups versus real analysis? | 9 | 1 | Real request logs, which we don't have. Listed to show what blocks a high-scoring question |

## 5. Measurement plan

**What to measure, and whether we can now.**

| Measure | Tool | How often | Who | Can we measure it now? |
|---|---|---|---|---|
| Google visibility: rank for the target queries | Ahrefs Rank Tracker (18 keywords loaded 28 Oct, no positions recorded) | Weekly | Content owner | **No.** Ahrefs access ended 31 October 2026 |
| Google visibility: impressions and clicks | Search Console | Monthly | Content owner | Only the snapshot in `data/ahrefs/search-console*.csv` |
| AI answers mentioning Dot | Ahrefs Site Explorer, AI-responses panel | Monthly, same day | Content owner | **No**, until Ahrefs returns |
| Perplexity citations | Free Perplexity app, by hand, counted from the answer text (`measure/citations.md`) | Monthly | Content owner | Yes |
| ChatGPT citations | Free ChatGPT, by hand, same method | Monthly | Content owner | Yes, but **never read so far** |
| LinkedIn engagement | LinkedIn page analytics | Per post, at 7 days | Whoever posts | Needs Dot's LinkedIn account; never accessed |
| Qualified traffic | Dot's web analytics, filtered on `utm_campaign=content-machine` | Monthly | Dot | Needs Dot's analytics; never accessed |
| Conversions | Dot's signups or CRM, by the same UTM | Monthly | Dot | Needs Dot's CRM; never accessed |

Citation markers are counted as markers and never called sources (`CLAUDE.md`, Measurement).

**The dated baseline.**

What we have:

- **Perplexity, 27 October 2026:** three buyer questions, recorded by topic label ("Evaluating accuracy", "What changes", "Cost and fit"). Dot was cited on 1 of 3: 5 markers, all to the AI Data Analyst Playbook, on "Evaluating accuracy".
- **Two later readings on a different question** (28 and 29 October): Dot 0 both times.
- **The Ahrefs snapshot, 27–28 October 2026** (`data/ahrefs/`): domain rating 43; 223 organic keywords; an estimated 1.3K organic visits a month; 380 AI responses mentioning Dot in the last month (224 in AI Overviews, 49 in Perplexity).

What's missing:

- **The 18 buyer queries.** They are the 18 rows of `data/ahrefs/keywords.csv` marked `is_buyer_query=yes`; 5 of the 18 have search volume. **None of the 18 has a citation reading.** The three readings above used topic labels, not these phrases, so all 18 are missing. Reading them by hand in Perplexity and ChatGPT, and recording the winning page type for each, is tier 3 work (`bank/surfaces.csv`, not yet built).
- Any reading after Ahrefs access ended.

## 6. What's still open

| Item | Why it matters | What closes it |
|---|---|---|
| Decision 4 for A, B and F | Publishing | `STATUS.md`, section 3: A, then B, then F; each later piece links the earlier ones, which return 404 until live |
| Re-check facts O1 and O2 on the current account | Both were observed on the dry-run account on 27 October | Look in Dot's UI and record the date |
| Census corrections from B's re-read (done 1 November: all eight sources re-opened, every number matched; three corrections applied the same day: Snowflake's scoring cell, Snowflake added to "more than one right answer" (3 to 4), Ramp added to the strict bar and the re-run count (5 to 6)) | Five (Anthropic, LinkedIn, Uber, ClickHouse, Hex) were re-read in Chrome on 1 November, quotes checked verbatim (`runs/test-ai-analyst-before-rollout-verification.md`). Snowflake, GitHub, Salesforce, Vercel, Ramp, Prosus, WisdomAI, Grab and Dot's own pages were read only through WebFetch | Re-open each in a browser before B publishes |
| The Olist licence | **Resolved 1 November 2026: Dot confirmed it may publish figures from the Olist dataset** (Rick and Théo). L1, L2 and L4 are confirmed, not only decisions | Nothing |
| Assumptions A1–A8 | Each needs Dot's yes, no or change | Section 8 |
| A number meaning two things, three times in one cluster | B's two fives and two sevens (different groups under one count), then "12 of 12 correct" and "8 of 8 correct", where 3 of 12 and 3 of 8 were correct only under the answer's own stated or a person-decided reading. Our own scores need the same item-by-item discipline rule 18 demands of Dot's answers | `mark_run.py` now prints the split (1 November 2026). A check that flags a bare "N of M correct" in a piece is not written |
| No check that pieces agree with each other | B said two of A's answers didn't name their date; A's own table says three. Caught by a phone read, fixed in B | A script that compares a cited figure with the cited piece's Figures row |
| No chart stage in the workflow | `check_piece.py` checks the Markdown, not the image file, so a missing chart passes | A chart stage after seo-geo, and the gate checking every referenced image exists |
| Ahrefs access | Ended 31 October 2026 | Reconnect, per `data/ahrefs/README.md` |
| Python on a new machine | The scripts need `requirements.txt` installed in whichever `python` comes first on PATH | Install, then `python -c "import pandas, matplotlib, docx"` |
| The question bank | 102 questions, not re-ranked with sales-call questions | Re-rank with ten sales-call questions |
| The incumbent shortlist | Stale (`bank/README.md`) | Re-check the pages that rank |
| Tier 3 | Agreed for after the pieces | The 18-query citation reading, `bank/surfaces.csv`, `/distribute`, `check_posts.py`, a post queue |
| Cold-start gaps (tested once, 1 November 2026) | A fresh session given only the README reached a research verdict on bank #29 (PIECE IF) in about 4 minutes. Full log: `runs/coldstart/COLDSTART-LOG-2026-11-01.md`. Gaps, most serious first: (1) section 3's first test skips Decision 1 and the truth spec, which the gate requires before a run; (2) the gate has no branch for a PIECE IF verdict, and nothing says who records a licence decision for a new piece; (3) the researcher isn't told which tables Dot's workspace holds; (4) the researcher isn't pointed to the bank row's gap basis or to `facts/house-structure-and-links.md` for the Playbook stage, and its test questions had a fresh-chat question worded as a follow-up; (5) the manifest stores the bank's short question, not the buyer's wording; (6) docs contradicted each other (fixed the same day: section numbers, the CLAUDE.md version, this section's state); (7) `stage_gate.py --help` treats --help as a slug; `bank.py top` picks #41 with no rule for choosing another | (1) and (2) fixed 1 November (CLAUDE.md v1.8.14): the first test follows the gate, and the gate waits on a recorded PIECE IF check. (3) to (7) open |
| Nobody but the author has run it end to end | Tested once cold, to the research verdict (above); never by a person other than the author, never to a published piece | One full piece by Dot's team |

**Why the browser step exists: the Anthropic record (1 November 2026).** Three errors were found in how the cluster used Anthropic's post. (1) The drift quote in our figures stopped at "over a month."; the page continues "before we treated this as an engineering problem", so B let a reader take the drift as ongoing. (2) The "three consecutive net-negative iterations" quote was also cut short (not used in a piece). (3) When the missing clause was added, we wrote "drift" where Anthropic wrote "this", and the paraphrase spread to B, F and both FAQ files before Gemini caught it. The first two came from reading the page through a model's fetch, which returns a model's reading, not the text; the third was ours. The Hex quote ("on purpose") was the same kind of fetch error. Open every source in a browser, and check quotes against the page's own text by script (`runs/test-ai-analyst-before-rollout-verification.md` shows how); when adding words from a source, quote them rather than paraphrase.

**A citation risk in answer engines (1 November 2026, from F's lift test).** An engine can credit a source we cite for a claim we made. Perplexity attributed all three of its bullets on F to LinkedIn, including lines that are our own steps, and for LinkedIn's figure it quoted LinkedIn's own page ("~60% of our benchmark questions now have multiple answers") rather than the piece's sentence: it reached through our link to the source. Spread the citations, keep each source to the step it supports, and give our own instructions their own sentences with no source beside them. F's step 1 example was moved from LinkedIn to Uber for a separate reason; LinkedIn is now F's least-cited named source.

**A limit of the second fact-check method (1 November 2026, from F).** A model scoring a guide reads hard rule 19's honesty labels ("rests on one company's practice", "no run of ours tested this") as weaknesses, and reports them as defects. They aren't: a step that says what it rests on is the rule working. Don't "fix" them by removing the labels or strengthening the claim; triage each against the evidence, and stand the label.

## 7. Where the machine stops, and why

**What runs on one command.** `/piece <slug>` runs research, the truth spec, the Dot run, marking, the outline, the draft, SEO, three blind reviewers, the revise step, the check loop, LinkedIn and export, in the order `scripts/stage_gate.py` allows.

**Where it stops, by design: seven points.** An honest count; each exists for a reason.

- **The question (Decision 1).** Which buyer question gets a piece is a sales judgement; search volume only breaks ties (hard rule 1).
- **The rival definitions (truth review).** Before a run, a person reads the truth spec's rival readings and adds `reviewed_by`. The machine can compute both readings; only a person knows which ones a buyer might mean, and they must be in before the run, or a right answer to another reading is marked wrong.
- **Batch conditions (Dot UI).** Mode, environment, context notes and credits before are recorded in Dot's UI before a run, because MCP can't see them.
- **Credits after (Dot UI).** The same limit, after the run: no cost per answer without it.
- **The outline (Decision 2).** What the finding is, and which evidence carries it.
- **The title and human checks (Decision 3).** Whether a title earns a click, the phone read, the headline test.
- **The publish (Decision 4).** Publishing is Dot's act, after its sign-offs.

**Why it stops at the Dot UI.** Mode, credits, environment and the active context notes are not observable via MCP (`facts/dot-mcp.md`, observed 31 October 2026). No MCP tool has a parameter or a field for any of them. That is a product limit, not a design choice. If Dot exposed them, those two stops would go.

**What it cannot do.** It cannot decide what the finding is, or whether a title earns a click. Every real improvement in this build came from a human read: B's reframe, both pieces' titles, the ledes. The machine's contribution was catching the errors a human read misses:

- **The date count.** B said two of A's answers didn't name their date. A's own table says three. The figures discipline made the mismatch findable.
- **ClickHouse's question count.** A proposed rewording said ClickHouse "started with 243 candidate questions". The source chain checked against the page says 501, then 475, then 243, then 204, then 201.
- **The score split.** "12 of 12 correct" was true. Checked item by item, 3 of the 12 were correct only under the answer's own rival definition.
- **The Hex quote.** A model's reading of Hex's post had Hex saying its judge "isn't well calibrated" and leans harsh "on purpose". Neither phrase is on the page.

**The pitch, plainly.** Not "type a topic, get a piece". Every number checked, every claim sourced, every rule enforced, and the four decisions that need judgement are the four you keep.

## 8. Findings for Rick

**The one-page version, with a line for each answer, ordered by what blocks publication: [DECISIONS-FOR-DOT.md](DECISIONS-FOR-DOT.md).**

### The context agent: a positioning line Dot isn't using

Dot's context agent page (https://www.getdot.ai/context-agent), in its top product panel, says: "Merging re-checks accuracy first: Dot answers its 25 questions again and merges at 95% or more." Set against B's census of 13:

- 6 of the 13 re-run their tests on a change, before each deploy, or daily (5 until Ramp was added on 1 November).
- 1 of the 13 states a numeric bar: Anthropic, which "initially used ~90%" as a launch threshold.
- None states a bar that a change must clear before it merges. Dot's page states exactly that.

It is the strongest positioning line in the cluster. Caveats: the panel is an illustration, and the page doesn't say what happens below 95%. B quotes it as Dot's stated behaviour, not as something we tested ("We haven't tested that gate here."). **Needs Rick's sign-off before B publishes.**

### Dot's home page accuracy claim

**Read in a browser, 1 November 2026** (Chrome; page text checked by script, the charts read from screenshots saved as `runs/screenshots/getdot-home-benchmark-easy-2026-11-01.jpg` and `-hard-2026-11-01.png`). The section is headed "Benchmarked on 450+ financial analysis tasks from Adyen" and holds two charts:

- **"You can train Dot to get better."** A line from 67% to 90% against "time invested" (0h to 8h), with a dashed line at 52% labelled "Google Data Science Agent". Footnote: "Google Data Science Agent · ~52% weighted overall (Nov 2025)."
- **"Hours of analysis in seconds."** Tabs "Easy 72" and "Hard 378". Easy: Dot 96%, "Humans · easy only" 62%. Hard: Dot 89%, "No human baseline · requires multi-file domain expertise". Footnote: "Human baseline from DABStep: 62% accuracy with 3+ hrs of work on easy tasks."

**What this changes.** The earlier handover (read through WebFetch) named only the 90% figure, from Dot's DABstep post ("30 representative tasks"). The live page also shows 96% on the 72 easy tasks and 89% on the 378 hard ones. 72 plus 378 is 450, so the page implies a run on the full public set, which no Dot post we read documents. Either way, the page sets Dot beside a Google figure that is a weighted overall score and a human figure on easy tasks only: different tasks, scored differently. That is the comparison B says can't be made.

**For Rick:** (1) Is there a full-set run behind 96% and 89%, and is it published? If so, B's sentence "Dot publishes an accuracy figure too … 90% on a 30-task slice" is incomplete and should cite it. (2) B's DABstep concession still needs his sign-off. (3) What would make the page hold: state each figure's task set and scoring beside it, or drop the Google and human comparisons.

### The byline

The roadmap cites evidence that a named author is cited about 2.3x more than anonymous content. The pieces carry a reviewed-on date (hard rule 22) but no author, because who bylines a piece is Dot's decision. If Dot names one, add the field and drop that sentence from rule 22.

### The closing line

Three independent readers of B flagged "If this excites you, we'd love to hear from you. Get in touch." as off-voice. It matches the last line of every Rick post we checked, so it stays (style rule 9). Keep or change: Dot's call.

### Assumptions A1–A8

Each is labelled "Assumption" wherever a piece uses it (`facts/dot-facts.md`). A3 is superseded and may not be used. None of the open ones is used in A or B; they were used in the archived trial pieces and will be needed by future pieces on cost or the context agent.

| ID | Assumption | Basis now | Used in | Rick's answer |
|---|---|---|---|---|
| A1 | Cost per answer may be published, in dollars as well as credits | Saurabh's answer | Archived piece 3 | |
| A2 | 1 credit ≈ $1 | The signup page's "$300 in free credits" and the 300 base credits read on 31 October; no Dot page states a price per credit | Archived piece 3; section 2 here | |
| A3 | Superseded: the 300 credits are 100 at signup plus the rest earned | Contradicted 31 October: 300 base credits, 0 bonus | Nowhere (barred) | — |
| A4 | A "cheaper than an analyst" comparison may be published if the analyst's cost and source are stated | Saurabh's answer | Not used | |
| A5 | The context agent stores a definition once, and every chat answer uses it | Facts O3 and O4: eight answers scoped to delivered orders, matching the note | Archived pieces 1 and 2 | |
| A6 | Environments let a team test a definition change before it reaches everyone | Fact O9 only; never tested | Archived piece 1 | |
| A7 | The evaluation always re-scores when a question is saved | Fact O2, seen twice | Not used | |
| A8 | Dot is comfortable publishing a piece where its evaluation passes a 0.52% definition disagreement | Saurabh's answer | Archived piece 1 | |

### Pending: Anthropic's drift sentence

On 1 November the Anthropic post was re-read in a browser. The drift sentence B relies on continues: "…over a month before we treated this as an engineering problem." B gives the drift (about 95% to about 65% in a month) without that clause. Whether B needs the clause, and whether adding it counts as a correction after Decision 3, is with Saurabh.

### Recommendations from the roadmap, and what wasn't adopted

- **Not adopted: the roadmap's skill names** (`/make-piece-plan`, `/gate`). `/piece`, `.claude/workflows/piece.js` and `scripts/stage_gate.py` already do those jobs.
- **Not adopted: the fact-checker's confirmed-claims list.** `facts/dot-facts.md` already holds Confirmed and Observed tables.
- **FAQ schema kept.** The roadmap demotes it because it shows no lift for pages already visible in AI answers. These pieces aren't visible yet, and an FAQ file costs nothing.
- **Links: one per company, at its first mention and in the table** (v1.8.8). The earlier rule linked every number, which read as a wall of links on a phone.
- **Method limit: pasted tables.** Gemini, given B as pasted text, said the census table was missing. Give a second model the rendered page, or check its row count.
- **A future piece: example test questions.** Readers of B expected a bank of questions to copy. LinkedIn's paper and ClickHouse's harness are where to look.

### Does Dot's evaluation hold a pass bar?

Guide F's step 7 says to decide the bar a result must clear before testing (Anthropic started at about 90%; Dot's Playbook suggests about 80%). Dot's evaluation was observed holding each question's expected answer, unit and tolerance (fact O1), and re-scoring on save (O2), but nobody observed a pass bar in it. So F's "Where Dot fits" says "steps 2 and 6 live in one place", not 2, 6 and 7 (hard rule 5). **If Dot's evaluation does hold a bar, the sentence gets stronger:** confirm it, and F can add step 7.

## 9. What I'd do differently

- **Fix the title shape before the first headline test.** A and B each took four headline-test rounds. B's titles were judged against the essay shape (4–9 words, no colon) until v1.8.4 tied title shape to format. That rule should have existed on day one.
- **Give every "don't change" instruction an expiry.** My brief to the writer said never to change B's first two sentences, to protect approved wording. It protected three known stumbles through two rounds instead. An instruction that protects wording must say what it protects and when it lapses.
- **Apply the evidence tests at scoring, not as an audit.** The model's first evidence scores were too high: 33 of 51 threes came down, and 11 of the original 20 twos failed the same two tests (`bank/README.md`). The tests were right; they came late.
- **Check numbers across pieces from the start.** B cited A's run and got the count of undated answers wrong (two, not three). Nothing compared the two pieces. Then our own scores, "12 of 12" and "8 of 8", were each true and each misleading. Our numbers needed the same item-by-item rule we hold Dot's answers to.
- **Never treat a model's reading of a page as a quote.** WebFetch returns a model's reading, not the page. That is how Hex's "on purpose" got into B. Every quote should have been checked in a browser before drafting, as F's were.
- **Treat a check that can be dodged as a broken check.** The writer got past check 17 by hyphenating "context agent" to "context-agent". It was caught and reverted (v1.8.7), and the check now looks for the claim, not the phrase. Gaming a check is a reportable event.

## 10. Accounts and tools you need

Claude Code · Dot (a workspace with the Olist tables or your own data, connected through the `ask_dot` MCP) · Ahrefs (the Getdot project; Rank Tracker holds 18 keywords; access ended 31 October 2026) · Perplexity and ChatGPT (free plans are enough) · Chrome with Claude in Chrome, for browser re-reads · Python 3.10+ with `requirements.txt`.

## 11. SEO and answer-engine choices, and how the research was adapted for LinkedIn

Each choice below was made on this cluster, with the change-log entry that records it.

**Titles carry the claim; the SEO title carries the search words.** Rick's own titles are flat claims ("Your Data Model Is the Prompt"), with no promise word and often no search phrase. Check 1 first failed them. It now marks a claim title PARTIAL and passes it when the SEO title carries the buyers' words and the headline test passes (CLAUDE.md v1.6.8, v1.8.3, v1.8.5), and title shape depends on the format (v1.8.4: a teardown title is 8–13 words, a guide title names what the reader gets). So B is "7 Companies Published Their AI Analysts' Accuracy. No Two Measured the Same Thing." with the SEO title "How 13 Companies Test Their AI Data Analyst" (80% of its target query's words); A's SEO title is "AI Analyst Follow-Up Questions: Check Which Date It Used"; F's title carries its query whole, "How to Test an AI Data Analyst Before Rollout: 8 Steps". Every title passed a three-reader headline test; A and B took four rounds each, F one.

**Answer engines quote passages, so pieces are built in quotable units.** From the roadmap's figure that about 44% of citations come from a page's first third: the question is answered in the first 100 words (hard rule 20), every H2 reads standing alone (hard rule 21), and every outline must carry one quotable line, under 25 words, standing alone and checkable (v1.8, v1.8.2). Check 25 then tests whether a blind lift-tester, reading the draft with nothing else, lifts that line; the line is compared by script so the tester stays blind.

**What the lift tests actually found** (Perplexity and Claude, by hand; records in each piece's `reviews/<slug>/lift-lines.md`):
- **An engine chose a better line than the one we targeted, in all three pieces.** In A, Perplexity lifted "The risk isn't a wrong number. It is a right number for a date you didn't mean, with nothing in the text to say so.", which wasn't targeted. In B, Claude lifted the Hex line ("Hex's judge accepted the wrong one 35% of the time."). In F, the blind tester lifted the opening's version of the number line, which we then made the quotable line.
- **From a guide, engines lift the steps, not a sentence.** Neither engine quoted F's quotable line; both carried the eight steps accurately and in order. A guide's citable unit is its instructions. Check 25 should test, for a guide, whether the steps survive compression (recorded in `prompts/06-edit.md`; not built).
- **Engines credit our claims to the sources we cite.** Perplexity attributed all three of its bullets on F to LinkedIn, including our own steps, and for LinkedIn's figure quoted LinkedIn's page rather than our sentence. Each source is now kept to the step it supports, and our instructions stand in sentences with no source beside them.

**FAQ schema kept, against the roadmap.** The roadmap demotes FAQ schema because it shows no lift for pages already visible in AI answers. These pages aren't visible yet, and the file costs nothing. B and F carry `pieces/<slug>-faq.json`; every answer is copied word for word from the piece, re-checked by script after every edit, so the schema can't drift from the text.

**The cluster de-conflicted, so three pieces stopped competing for one query.** All three had targeted "ai data analyst". Now F, the hub, owns it with "how to evaluate ai data analyst accuracy" and "ai data analyst accuracy"; B owns "ai data analyst test questions" and "text to sql accuracy"; A owns "AI analyst follow-up questions context" and "conversational analytics". A and B link to F from their closing instruction; F links to both from the steps they support.

**Posts drawn from the evidence, not the finished piece.** The six posts were cut from the run files, the census and the figures file: A's transcript post quotes Dot's answer from the run file; A's build log comes from the timing file; B's two posts from the census table and its counts. Two reasons. Every number in a post then traces to a figures row (the post check holds each post to its piece's figures, and finds a published number's source in the piece it links). And a post can carry what the piece cut: the build log's 27 minutes appears nowhere in A. The six use six different structures across the cluster rather than per piece (PLAN.md), because the roadmap's post model assumed every piece is research; a person wrote every first line; the link sits in the first comment with a UTM; and a post may end on its strongest line, with what the link delivers said in that comment (v1.8.15).

**What we couldn't do.** Ahrefs access ended on 31 October 2026, so search data is a frozen snapshot of 27–28 October: 18 buyer queries, 5 with any US volume, 13 "not indexed"; Rank Tracker held the queries but recorded no positions. Demand in the question bank is therefore scored by how many independent sources name a question (`bank/README.md`), not by search volume, and search volume only breaks ties (hard rule 1). No citation reading exists for any of the 18 queries (section 5).
