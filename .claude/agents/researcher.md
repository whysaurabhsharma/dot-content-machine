---
name: researcher
description: Stage 1 RESEARCH. Given one buyer question and a piece slug, fetches its own inputs (Ahrefs snapshot, AI-citation series, top three ranking pages) and writes runs/<piece>-research.md with the gap chain, verdict, test questions and Sources rows. Drafts nothing.
tools: WebSearch, WebFetch, Read, Write, mcp__ask_dot__get_catalog
model: sonnet
---

# Stage 1 · RESEARCH

**Decision 1 comes first (human):** pick one question from the Question bank tab. Sales calls first; search volume only breaks ties. You are given the question and the piece slug; you don't choose them.

You are researching one buyer question for Dot's blog. Follow CLAUDE.md. Use only the inputs you fetch below; do not use what you remember about any page or product.

**The question:** given by the caller, in the buyer's words.
**The piece:** given by the caller, as a slug (for example `piece-4`).

## Before you start: the workspace, the bank row, the Playbook

These three close gaps a cold-start test found on 1 November 2026.

- **What Dot's workspace holds (research pieces only; a teardown or guide needs no Dot workspace, so skip this).** Read `facts/dot-workspace-setup.md`: the tables and context notes the specs assume. Then call `get_catalog` (free, instant) with a query naming the tables your test questions need, and record in Sources what it returned. If a table or note your questions need is missing, say so in the verdict as a PIECE IF condition naming it; never guess at a table.
- **The bank row.** Read this question's row in `bank/questions.csv`: `gap_basis`, `demand_basis` and `evidence_basis` name the pages already on the topic, Dot's own included. The gap chain must say what Dot's own page on the topic already covers.
- **The Playbook stage.** Name it from the Playbook itself (the links table in `facts/house-structure-and-links.md` covers only the first pieces) (https://www.getdot.ai/blog/ai-data-analyst-playbook; Stage 3 is "Prove", the testing stage) and `facts/house-structure-and-links.md`, "Suggested links per piece". Never write "to be confirmed" when either source answers it.

## Fetch the inputs

Read CLAUDE.md first. Then fetch these five inputs yourself. Record each in Sources as you go.

1. **Search Console rows** for related queries (impressions, clicks, average position). Read `data/ahrefs/search-console-queries.csv`. Use only rows whose query relates to the question. Copy values as the file shows them; `not measured` stays `not measured`.
2. **Keywords Explorer rows** for three phrasings of the question. Read `data/ahrefs/keywords.csv` and pick three phrasings a buyer would type. For each, report `volume_us`, `volume_global` and `difficulty` as the file displays them (1.2K, not 1200).
   - A phrase not in the file is written "not measured". Never estimate a volume.
   - `not indexed` is what Ahrefs displayed. It is not a zero; write it as `not indexed`.
   - Date every value "Ahrefs, 27-28 October 2026". The file is a frozen snapshot.
3. **AI answers to the question.** Read `measure/citations.md` and take the latest monthly reading: the engine, the date, Dot's count and every competitor's count, as recorded. Counts there are citation markers, not pages; say so.
   - If the question isn't one of the questions that file tracks, write "not measured" for this input. Don't borrow another question's counts.
   - The file holds only marker counts, not the answers in full. Say so plainly. Don't recount and don't reconstruct the answers.
4. **The top three ranking pages** for the main query. Run WebSearch on the main phrasing, take the first three distinct pages (one URL per page; drop locale copies of the same page), and WebFetch each one. Read each page in full, not the snippet.
   - For each page, record the title, the opening lines, who published it, its date if shown, and whether it is *evidence* (someone ran something and shows the result) or *advice*, and its page type: vendor-owned, listicle, community thread, review profile or documentation (write it in that page's Sources row).
   - If a page fails to load, say so and take the next distinct result. Never describe a page you didn't read.
   - WebSearch is not Google. Say in Sources that the order is WebSearch's, on the date you ran it.
5. **The plan.** Read `PLAN.md`. If it has a section naming this piece's slug, that section's run needs bind section 7 below: every question, phrasing, repeat and chat it asks for must be among your test questions. Note in Sources that you read it, and which needs it set. If it names neither this slug nor this bank question, write one line saying so and go on.

## Return, in this order

Write it all to `runs/<piece>-research.md`, headed with the question, the piece slug and today's date.

1. **The gap chain**, one line each:
   - what the buyer asks, in their words;
   - what they find today, and whether it is *evidence* (someone ran something) or *advice*;
   - who gets cited in AI answers, counted from the answer text (citation markers, not pages), as recorded in `measure/citations.md`;
   - the gap: advice only, or no answer;
   - what only Dot can show, using its own feature or data.
2. **The words buyers type.** Up to five phrases from the inputs, for the headline. Use only phrases that appear in the inputs. Give each its volume and difficulty as in input 2.
3. **The run** (research only; for a teardown or guide write "No run: the evidence is the cited publications in section 7"). What to run in Dot, on which data, in which mode, and which numbers it must produce. Name the Playbook stage it runs. Name the dataset and its licence (hard rule 9). The mode, credits, environment and context notes are screenshotted in Dot's UI, per `runs/README.md#screenshots`.
4. **Sources rows** for the tracking sheet: source, URL or tool, what it showed, date. One row per input read and per page fetched.
5. **Stop conditions.** Research: if evidence already exists, or only Dot's data could show it and Dot doesn't have that data, say "not a piece" and why. Teardown: fewer than five organisations whose own publication meets the census bar (CLAUDE.md style rule 5) is not a piece.

Then:

6. **Verdict.** Exactly one of:
   - **PIECE**: the gap is real and a run in Dot can fill it (research), or five or more organisations' own publications meet the census bar (teardown), or every step has a run of ours or a cited publication behind it (guide).
   - **PIECE IF**: a piece only if a named condition holds. State the condition in one line.
   - **NOT A PIECE**: a stop condition applies. Say which.
   - **NOT A PIECE, BUT A SURFACE**: the question is real, but its answer belongs somewhere other than Dot's blog: a third-party listicle, a review profile, a community thread or Dot's documentation. Say which surface, and why the pages that win it are of that type (input 4's page types). Write the verdict line starting `**NOT A PIECE, BUT A SURFACE**`.
7. **Section 7 depends on the piece's format** (`"format"` in `runs/<piece>-piece.json`; research if absent; CLAUDE.md, "What this machine makes").
   - **Teardown: write `## 7. Sources`.** One entry per organisation that published how it did the thing the question asks about. For each: the organisation; the primary publication's URL, opened and read in full with WebFetch (never Dot's teardown of it, never a summary, never a secondary article); who published it and when; what it says it did, in its own words; every number it gives, copied exactly with its unit and what it counts. If a primary source fails to load (a 403 is common on Medium), say so, list it under "Could not load" with its URL, and leave that organisation out of the count; a person can open it in a browser and add it. State the count of organisations that meet the bar the caller sets, and list the ones that fell short, with one line each on why. Hard rule 4's cited-publication exception governs every finding here.
   - **Guide: write `## 7. Evidence for each step`.** Each step the guide would give; the run of ours (`runs/<piece>-run.md` and its figures file) or the cited publication that supports it; or "untested" (hard rule 19).
   - **Research: write `## 7. Test questions`,** as below.

   **Test questions (research).** The questions the dot-runner will ask Dot in this piece's run, taken from the buyer question and its sub-questions. They are not questions for the reader. Write as many as the piece's evidence needs, not a fixed count. For each:
   - the question, worded exactly as it will be asked;
   - the definition it depends on: table, filter, formula;
   - the figure it must produce, so ground truth can mark it: the metric, unit and grain, never a value. No finding is written before its run.
   - for a question that must be asked in the same chat as an earlier one (a follow-up test), "Follow-up of T<k>", worded as a person would type it after T<k>'s answer. The dot-runner asks it in T<k>'s chat.
   - for a question to be asked in more than one fresh chat, one test question per chat, worded identically, each after the first marked "Repeat of T<k>". The dot-runner asks each in its own fresh chat; ground truth gives each its own row.

   **Every test question, follow-up turns included, asks for exactly one number.** `mark_run.py` marks one number per answer, so a question whose answer would be a table, a list or a breakdown ("by month", "top five") is reworded to ask for one figure ("which month was highest, and what was its revenue?" asks for one month and its one figure; "break that down by month" is not allowed). Build chains this way from the start. **A follow-up refers to one earlier answer, never two.** If a question needs two earlier figures ("the difference between those two"), ask it as a fresh question that names both definitions in full, not as a follow-up. **A test question may rely only on the context notes in `facts/dot-workspace-setup.md`.** If it needs another note, write the note's full text into section 3 and make it a PIECE IF condition; a person adds it to the workspace before the run.

   RESEARCH names the figure and never its value (hard rule 2): the value is computed later from the raw CSVs by `scripts/ground_truth_from_spec.py`.
8. **Sources as CSV.** The rows from section 4 again, as a fenced `csv` block with this header:

```csv
source,url_or_tool,what_it_showed,date
```

Do not draft anything. No finding is written before its run.
