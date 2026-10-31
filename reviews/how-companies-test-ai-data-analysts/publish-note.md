# Publish note · how-companies-test-ai-data-analysts (piece B)

**Read by:** 

Fill the line above with your name and the date once you have read this note. `scripts/stage_gate.py` holds Decision 4 (publishing) until it is filled. This note is copied into `exports/how-companies-test-ai-data-analysts/PUBLISH-NOTE.md`, next to the files you paste from.

## What this piece assumes

Two passages in "Where Dot fits", the last section, rest on things Dot has not confirmed. Each is labelled in the text, so a reader can tell which kind it is.

### 1. The context agent quote (labelled "Assumption": untested)

As published:

> Dot's context agent page says: "Merging re-checks accuracy first: Dot answers its 25 questions again and merges at 95% or more." Assumption: the page describes how merging works today; we haven't tested it.

Why it is there: the quote comes from Dot's own page (https://www.getdot.ai/context-agent), where it sits in a top panel that may be an illustration. Nobody has seen a merge re-checked in Dot.

Who answers: Rick (Dot). The question: does the page describe how merging works today?

- **If yes:** delete the sentence "Assumption: the page describes how merging works today; we haven't tested it." The quote then stands on Dot's word.
- **If no:** delete both sentences (the quote and its label). The first paragraph of "Where Dot fits" then reads, in full: "Dot answers data questions for your team." (that sentence keeps its link to https://www.getdot.ai/blog/conversational-analytics).

### 2. The evaluation sentence (labelled "observed … not re-checked since")

As published:

> In Dot's evaluation, each test question carries an expected answer, a unit and a tolerance in percent. That was observed on 27 October 2026 and not re-checked since.

Why it is there: this was seen once, on a trial Dot account, on 27 October 2026.

Who answers: Rick, or anyone with a Dot account, by opening an evaluation and looking.

- **If it still works this way:** delete "That was observed on 27 October 2026 and not re-checked since."
- **If it has changed:** replace the first sentence with what the evaluation now holds, and delete the second.
- **If evaluation no longer exists:** delete both sentences. The paragraph keeps "More in the AI Data Analyst Playbook and Dot's docs." with its two links.

## Decided, not assumed

**The dataset licence.** The section on our own run reports figures from piece A's run on the Olist dataset (CC BY-NC-SA 4.0 label, unverified at source). Saurabh recorded a decision to proceed (L1). If Dot says it may not publish figures from Olist, do not publish.

## Fix after publishing

**Links to A and F.** B links piece A ("our earlier piece on follow-up questions", https://www.getdot.ai/blog/ai-analyst-follow-up-questions) and guide F ("before rollout" in the closing paragraph, https://www.getdot.ai/blog/test-ai-analyst-before-rollout). Each returns 404 until that piece is live. Publish A first, and F in the same session, or remove the F link until F is live.

## Posts that depend on this piece

- **Post B1 (the number):** ready once B is live.
- **Post B3 (the failure taxonomy): HOLD.** It names, in public, what five companies' published testing posts leave out, Snowflake (a Dot integration partner) among them. Whether Dot is comfortable with that is Rick's call (DECISIONS-FOR-DOT.md, question 7). Do not queue it until he answers.
