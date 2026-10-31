# Publish note · test-ai-analyst-before-rollout (guide F)

**Read by:** 

Fill the line above with your name and the date once you have read this note. `scripts/stage_gate.py` holds Decision 4 (publishing) until it is filled. This note is copied into `exports/test-ai-analyst-before-rollout/PUBLISH-NOTE.md`, next to the files you paste from.

## What this piece assumes

One passage in "Where Dot fits", the last section, rests on something Dot has not re-confirmed.

### The evaluation sentence (labelled "observed … not re-checked since")

As published:

> Dot's evaluation holds each test question's expected answer, a unit and a tolerance in percent, so steps 2 and 6 live in one place. That was observed on 27 October 2026 and not re-checked since.

Why it is there: this was seen once, on a trial Dot account, on 27 October 2026.

Who answers: Rick, or anyone with a Dot account, by opening an evaluation and looking.

- **If it still works this way:** delete "That was observed on 27 October 2026 and not re-checked since."
- **If it has changed:** rewrite the first sentence to say what the evaluation now holds; keep "so steps 2 and 6 live in one place" only if both still apply; delete the second sentence.
- **If evaluation no longer exists:** delete both sentences. The paragraph keeps "More in the AI Data Analyst Playbook." with its link.

## Decided, not assumed

**The dataset licence.** Steps 2 to 6 cite figures from two of our runs on the Olist dataset (CC BY-NC-SA 4.0 label, unverified at source). Saurabh recorded a decision to proceed (L4). If Dot says it may not publish figures from Olist, do not publish.

## Fix after publishing

**Links to A and B.** F links piece A (https://www.getdot.ai/blog/ai-analyst-follow-up-questions) and piece B (https://www.getdot.ai/blog/how-companies-test-ai-data-analysts) in several steps. Each returns 404 until that piece is live. Publish F last, after A and B, or in the same session.

## Posts that depend on this piece

Post F5 (the checklist) and post F4 (the contrarian read), in `posts/test-ai-analyst-before-rollout-posts.md`. Each goes out only after F is live.
