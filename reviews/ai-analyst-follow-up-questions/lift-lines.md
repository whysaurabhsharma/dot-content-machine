# Lift lines · ai-analyst-follow-up-questions

The lines this piece intends answer engines to quote, and what the lift test actually lifted. Format and method: `prompts/06-edit.md`, section 3.

## Intended

Set 31 October 2026, before the lift test, by proposal; Saurabh ran the test against them.

1. "An AI analyst's answer can be right and still not say which question it answered."
2. "A matching total with a different filter is a different answer." **Changed 31 October 2026, after the second fact-check.** Gemini and ChatGPT both flagged it: this run produced no matching totals under different filters (the late counts were 2,453 and 1,762), so it read as a finding it wasn't. Relabelled as an instruction for the reader's own test: "When you run this, a total that matches under a different date filter is still a different answer." Cost of the fix: Perplexity lifted the old line verbatim in the lift test, and that line no longer exists in the piece. The new wording has not been lift-tested.
3. "Every answer in this run, 8 of 8, came back with its SQL, and its date filter named the column."

Added 31 October 2026, after the lift test:

4. **"The risk isn't a wrong number. It is a right number for a date you didn't mean, with nothing in the text to say so."** Recorded by Saurabh as the best line in the piece. Perplexity lifted it without it being targeted, which is the strongest evidence a line is liftable. It is two sentences, and the second leans on the first; the engine took them as a pair.

## Lift test, 31 October 2026 (Saurabh)

Prompt: "Summarise this article in exactly three bullet points. Each bullet must contain one direct quotation from the article, in quotation marks." Pasted above `reviews/ai-analyst-follow-up-questions/draft.md`, the round 3 copy.

| Tool | Lifted verbatim | Intended? |
|---|---|---|
| Perplexity | "A matching total with a different filter is a different answer" | Yes, line 2 |
| Perplexity | "The risk isn't a wrong number. It is a right number for a date you didn't mean, with nothing in the text to say so." | No, now line 4 |
| Claude | "An AI analyst's answer can be right and still not say which question it answered" | Yes, line 1 |

Claude declined to give three quotes, citing its own limits on verbatim reproduction, and paraphrased the rest. Intended line 3 was not lifted by either tool.

Verdict: **pass** (Saurabh).
