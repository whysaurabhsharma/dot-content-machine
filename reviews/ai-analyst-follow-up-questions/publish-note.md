# Publish note · ai-analyst-follow-up-questions (piece A)

**Read by:** 

Fill the line above with your name and the date once you have read this note. `scripts/stage_gate.py` holds Decision 4 (publishing) until it is filled. This note is copied into `exports/ai-analyst-follow-up-questions/PUBLISH-NOTE.md`, next to the files you paste from.

## What this piece assumes

Nothing pending. It makes no product claim beyond what its own run showed (every answer came back with its SQL). Its one condition, that the Olist data has the two date columns the test needs, was checked before the run and confirmed by Saurabh on 1 November 2026.

## Decided by Saurabh, Dot sign-off pending

`scripts/stage_gate.py` refuses Decision 4 while any line below reads PENDING. When Dot signs, replace PENDING with who signed and the date. These were first recorded as Dot's approvals on 1 November 2026; nobody at Dot had given them (CLAUDE.md v1.8.28).

**Dot sign-off:** PENDING · the dataset licence. Saurabh decided on 1 November 2026 that the piece may publish figures computed from the Olist public e-commerce dataset (CC BY-NC-SA 4.0 label; facts L1, L4). If Dot says no, the runs need repeating on data Dot may publish (the questions and scripts carry over).

**Dot sign-off:** PENDING · the byline. Saurabh decided on 1 November 2026 that the author is Saurabh Sharma. If Dot says yes, set `author_approved_by` in the piece's front matter to who approved it and the date, and re-export. If no, delete the `author` and `author_approved_by` lines and re-export.

## Fix after publishing

**The link to guide F.** The closing paragraph links F: "Before rollout, run the full eight-step test." (to https://www.getdot.ai/blog/test-ai-analyst-before-rollout). Until F is live, that link returns 404. Either publish F in the same session, or remove the link for now (keep the sentence as plain text) and add it when F is live.

## Posts that depend on this piece

Post A2 (the transcript) and post A6 (the build log), in `posts/ai-analyst-follow-up-questions-posts.md`. Each goes out only after A is live.
