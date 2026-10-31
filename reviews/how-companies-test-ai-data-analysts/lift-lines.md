# Lift lines · how-companies-test-ai-data-analysts

Format and method: `prompts/06-edit.md`, section 3. Each line stands alone and is checkable (CLAUDE.md v1.8.2).

## Intended

Updated 31 October 2026 after the reframe and round 3 revision. Each line is word for word in the piece.

1. "Seven of the 13 companies published an accuracy figure, and no two measured the same thing." (ID: C-9) The outline's quotable line; the blind lift-tester lifted it word for word (check 25).
2. "About 60% of LinkedIn's benchmark questions have more than one accepted answer." (ID: LIN-3) Ties this piece to piece A's two right answers.
3. "Anthropic's case shows that a test passed at launch can say little about the same agent a month later." (supported by ANT-5, ANT-6) Saurabh chose the earlier wording, "A test passed at launch says little about the same agent a month later."; the round 3 revision scoped it to Anthropic's case because the fact-checker said it generalised from one company. **Approved as revised by Saurabh, 31 October 2026:** one company can't carry a general claim.

Added 31 October 2026, after the lift test:

4. **"Hex's judge accepted the wrong one 35% of the time."** (ID: HEX-3) Lifted by Claude without being targeted, which is the strongest evidence a line is liftable. It is also the line the blind reader said they would quote to a CFO. It outperformed line 3.

Replaced:
- "Thirteen companies published how they check their AI analyst's answers; only five published a method you could copy." No longer in the piece after the reframe.

## Lift test, 31 October 2026 (Saurabh): PASS

Prompt: "Summarise this article in exactly three bullet points. Each bullet must contain one direct quotation from the article, in quotation marks." Pasted above `reviews/how-companies-test-ai-data-analysts/draft.md`.

| Tool | Lifted | Intended? |
|---|---|---|
| Perplexity | "no two measured the same thing" | Yes, line 1 (its second half) |
| Perplexity | "Five companies published enough to copy: what they test against, how they score and when they run it" | No (pocket guide line 3) |
| Perplexity | "About 60% of LinkedIn's benchmark questions do" | Yes, line 2's figure, in the pocket guide's wording rather than line 2's sentence |
| Claude | "no two measured the same thing" | Yes, line 1 |
| Claude | "About 60% of LinkedIn's benchmark questions have more than one accepted answer" | Yes, line 2, word for word |
| Claude | Hex's judge accepting a wrong figure 35% of the time | No, now line 4 |
| Claude | "its offline accuracy drifted from about 95% to about 65%" | Line 3's substance, not its sentence |

- **Lines 1 and 2 were lifted by both engines.** Both independently found the piece's spine: no two of the published figures measured the same thing.
- **Line 3 was not lifted word for word by either.** Claude paraphrased its substance through the Anthropic drift sentence. A line that survives paraphrase but not quotation is weaker than one quoted word for word; the Hex sentence, not targeted, did better.
- The quotes above are as Saurabh reported them.
