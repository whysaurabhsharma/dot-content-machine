# Publish note · how-companies-test-ai-data-analysts (piece B)

**Read by:** 

Fill the line above with your name and the date once you have read this note. `scripts/stage_gate.py` holds Decision 4 (publishing) until it is filled. This note is copied into `exports/how-companies-test-ai-data-analysts/PUBLISH-NOTE.md`, next to the files you paste from.

## What this piece assumes

Two passages in "Where Dot fits", the last section, rest on something Dot has not confirmed. Each is labelled in the text.

### The context agent quote (labelled "Assumption": untested)

As it stands:

> Dot's context agent page says: "Merging re-checks accuracy first: Dot answers its 25 questions again and merges at 95% or more." Assumption: the page describes how merging works today; we haven't tested it.

Why it is there: the quote comes from Dot's own page (https://www.getdot.ai/context-agent), where it sits in a top panel that may be an illustration. Nobody has seen a merge re-checked in Dot.

Who answers: Rick (Dot). The question: does the page describe how merging works today?

- **If yes:** delete the sentence "Assumption: the page describes how merging works today; we haven't tested it." The quote then stands on Dot's word.
- **If no:** delete both sentences (the quote and its label). The first paragraph of "Where Dot fits" then reads, in full: "Dot answers data questions for your team." (that sentence keeps its link to https://www.getdot.ai/blog/conversational-analytics).

### Dot's evaluation (labelled "observed on 27 October 2026 and not re-checked since")

As it stands:

> In Dot's evaluation, each test question carries an expected answer, a unit and a tolerance in percent. That was observed on 27 October 2026 and not re-checked since.

Why it is there: it was seen on a trial account on 27 October (fact O1). It was recorded on 1 November as confirmed by Rick and its label removed; nobody at Dot had confirmed it, so the label is back (CLAUDE.md v1.8.28).

Who answers: Rick (Dot), or anyone with a Dot account, by looking.

- **If still true:** delete the sentence "That was observed on 27 October 2026 and not re-checked since."
- **If changed:** delete both sentences. The paragraph then reads, in full: "More in the AI Data Analyst Playbook and Dot's docs." (both links kept).

## Open with Dot (none blocks publishing)

**1. The context agent page.** Does the merging panel on https://www.getdot.ai/context-agent describe how Dot works today, or is it an illustration? B quotes it with an "Assumption" label. When Dot answers, apply the replacement text in "What this piece assumes" above.

**2. The DABstep figures.** Does a published Dot run cover all 450 tasks of Adyen's DABstep benchmark? Dot's DABstep post reports 90% on a 30-task slice; Dot's home page shows 96% on 72 easy tasks and 89% on 378 hard ones. B cites only the 30-task post, which is accurate as it stands. If a full-set run is published, replace B's sentence "Dot publishes an accuracy figure too: 90% on a 30-task slice of Adyen's public DABstep benchmark." with one that cites that run and its figure, add a figures row for the new number, and link the run's post.

## Decided by Saurabh, Dot sign-off pending

`scripts/stage_gate.py` refuses Decision 4 while any line below reads PENDING. When Dot signs, replace PENDING with who signed and the date. These were first recorded as Dot's approvals on 1 November 2026; nobody at Dot had given them (CLAUDE.md v1.8.28).

**Dot sign-off:** PENDING · the dataset licence. Saurabh decided on 1 November 2026 that the piece may publish figures computed from the Olist public e-commerce dataset (CC BY-NC-SA 4.0 label; facts L1, L4). If Dot says no, the runs need repeating on data Dot may publish (the questions and scripts carry over).

**Dot sign-off:** PENDING · the byline. Saurabh decided on 1 November 2026 that the author is Saurabh Sharma. If Dot says yes, set `author_approved_by` in the piece's front matter to who approved it and the date, and re-export. If no, delete the `author` and `author_approved_by` lines and re-export.

**Dot sign-off:** PENDING · naming partners. B's census table and post B3 say what each company's published testing post leaves out, by name, Snowflake (a Dot integration partner) among them. Saurabh decided yes on 1 November 2026, since Dot already publishes comparison pages at getdot.ai/compare. If Dot says no: post B3 drops the names, and Snowflake's row is reworded with Snowflake's sign-off or the table is reconsidered.

## Fix after publishing

**Links to A and F.** B links piece A ("our earlier piece on follow-up questions", https://www.getdot.ai/blog/ai-analyst-follow-up-questions) and guide F ("before rollout" in the closing paragraph, https://www.getdot.ai/blog/test-ai-analyst-before-rollout). Each returns 404 until that piece is live. Publish A first, and F in the same session, or remove the F link until F is live.

## Posts that depend on this piece

- **Post B1 (the number):** ready once B is live.
- **Post B3 (the failure taxonomy):** ready once B is live. It names what five companies' published testing posts leave out, Snowflake (a Dot integration partner) among them. Held until Dot signs off naming partners (above).
