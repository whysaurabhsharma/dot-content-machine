# Publish note · test-ai-analyst-before-rollout (guide F)

**Read by:** 

Fill the line above with your name and the date once you have read this note. `scripts/stage_gate.py` holds Decision 4 (publishing) until it is filled. This note is copied into `exports/test-ai-analyst-before-rollout/PUBLISH-NOTE.md`, next to the files you paste from.

## What this piece assumes

One sentence in "Where Dot fits" rests on something Dot has not confirmed. It is labelled in the text.

### Dot's evaluation (labelled "observed on 27 October 2026 and not re-checked since")

As it stands:

> Dot's evaluation holds each test question's expected answer, a unit and a tolerance in percent, so steps 2 and 6 live in one place. That was observed on 27 October 2026 and not re-checked since.

Why it is there: it was seen on a trial account on 27 October (fact O1). It was recorded on 1 November as confirmed by Rick and its label removed; nobody at Dot had confirmed it, so the label is back (CLAUDE.md v1.8.28).

Who answers: Rick (Dot), or anyone with a Dot account, by looking.

- **If still true:** delete the sentence "That was observed on 27 October 2026 and not re-checked since."
- **If changed:** delete both sentences. The paragraph then reads, in full: "More in the AI Data Analyst Playbook." (link kept).

## Open with Dot (none blocks publishing)

**1. A pass bar in Dot's evaluation.** Does Dot's evaluation let a team set a pass bar? Step 7 tells readers to decide one before testing; F makes no claim that Dot's evaluation holds one. If Dot confirms it does, replace "so steps 2 and 6 live in one place." in "Where Dot fits" with "so steps 2, 6 and 7 live in one place.", then re-read that paragraph aloud.

## Decided by Saurabh, Dot sign-off pending

`scripts/stage_gate.py` refuses Decision 4 while any line below reads PENDING. When Dot signs, replace PENDING with who signed and the date. These were first recorded as Dot's approvals on 1 November 2026; nobody at Dot had given them (CLAUDE.md v1.8.28).

**Dot sign-off:** PENDING · the dataset licence. Saurabh decided on 1 November 2026 that the piece may publish figures computed from the Olist public e-commerce dataset (CC BY-NC-SA 4.0 label; facts L1, L4). If Dot says no, the runs need repeating on data Dot may publish (the questions and scripts carry over).

**Dot sign-off:** PENDING · the byline. Saurabh decided on 1 November 2026 that the author is Saurabh Sharma. If Dot says yes, set `author_approved_by` in the piece's front matter to who approved it and the date, and re-export. If no, delete the `author` and `author_approved_by` lines and re-export.

## Fix after publishing

**Links to A and B.** F links piece A (https://www.getdot.ai/blog/ai-analyst-follow-up-questions) and piece B (https://www.getdot.ai/blog/how-companies-test-ai-data-analysts) in several steps. Each returns 404 until that piece is live. Publish F last, after A and B, or in the same session.

## Posts that depend on this piece

Post F5 (the checklist) and post F4 (the contrarian read), in `posts/test-ai-analyst-before-rollout-posts.md`. Each goes out only after F is live.
