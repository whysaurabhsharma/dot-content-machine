# Publish note · how-companies-test-ai-data-analysts (piece B)

**Read by:** 

Fill the line above with your name and the date once you have read this note. `scripts/stage_gate.py` holds Decision 4 (publishing) until it is filled. This note is copied into `exports/how-companies-test-ai-data-analysts/PUBLISH-NOTE.md`, next to the files you paste from.

## What this piece assumes

One passage in "Where Dot fits", the last section, rests on something Dot has not confirmed. It is labelled in the text as untested.

### The context agent quote (labelled "Assumption": untested)

As published:

> Dot's context agent page says: "Merging re-checks accuracy first: Dot answers its 25 questions again and merges at 95% or more." Assumption: the page describes how merging works today; we haven't tested it.

Why it is there: the quote comes from Dot's own page (https://www.getdot.ai/context-agent), where it sits in a top panel that may be an illustration. Nobody has seen a merge re-checked in Dot.

Who answers: Rick (Dot). The question: does the page describe how merging works today?

- **If yes:** delete the sentence "Assumption: the page describes how merging works today; we haven't tested it." The quote then stands on Dot's word.
- **If no:** delete both sentences (the quote and its label). The first paragraph of "Where Dot fits" then reads, in full: "Dot answers data questions for your team." (that sentence keeps its link to https://www.getdot.ai/blog/conversational-analytics).

(The evaluation sentence that also carried a label was confirmed by Dot on 1 November 2026, and its label removed.)

## Open with Dot (none blocks publishing)

**1. The context agent page.** Does the merging panel on https://www.getdot.ai/context-agent describe how Dot works today, or is it an illustration? B quotes it with an "Assumption" label. When Dot answers, apply the replacement text in "What this piece assumes" above.

**2. The DABstep figures.** Does a published Dot run cover all 450 tasks of Adyen's DABstep benchmark? Dot's DABstep post reports 90% on a 30-task slice; Dot's home page shows 96% on 72 easy tasks and 89% on 378 hard ones. B cites only the 30-task post, which is accurate as it stands. If a full-set run is published, replace B's sentence "Dot publishes an accuracy figure too: 90% on a 30-task slice of Adyen's public DABstep benchmark." with one that cites that run and its figure, add a figures row for the new number, and link the run's post.

## Confirmed by Dot

**The dataset licence: confirmed.** The figures come from the Olist public e-commerce dataset (CC BY-NC-SA 4.0 label). Dot confirmed on 1 November 2026 (Rick and Théo) that it may publish figures from it. Nothing to do.

**The byline: confirmed.** Author: Saurabh Sharma, approved by Dot (Rick) on 1 November 2026. Set it in the CMS item's author field (it is in `webflow-fields.json` as `author`).

## Fix after publishing

**Links to A and F.** B links piece A ("our earlier piece on follow-up questions", https://www.getdot.ai/blog/ai-analyst-follow-up-questions) and guide F ("before rollout" in the closing paragraph, https://www.getdot.ai/blog/test-ai-analyst-before-rollout). Each returns 404 until that piece is live. Publish A first, and F in the same session, or remove the F link until F is live.

## Posts that depend on this piece

- **Post B1 (the number):** ready once B is live.
- **Post B3 (the failure taxonomy):** ready once B is live. It names what five companies' published testing posts leave out, Snowflake (a Dot integration partner) among them; Dot approved this on 1 November 2026, since it already publishes comparison pages at getdot.ai/compare.
