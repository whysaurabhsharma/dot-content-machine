# Stage 1 · RESEARCH

**Decision 1 comes first (human):** pick one question from the Question bank tab. Sales calls first; search volume only breaks ties.

Runs in this repo as the `researcher` subagent (`.claude/agents/researcher.md`).

You are researching one buyer question for Dot's blog. Follow CLAUDE.md. Use only the inputs below; do not use what you remember about any page or product.

**The question:** {paste the question, in the buyer's words}

**Inputs:**
1. Search Console rows for related queries (impressions, clicks, average position): {paste}
2. Keywords Explorer rows (query, volume, difficulty, or "not indexed"): {paste}
3. AI answers to the question, pasted in full, with the engine and date: {paste Perplexity / Claude / ChatGPT answers}
4. The titles and opening lines of the top pages for the main query: {paste}

**Return, in this order:**

1. **The gap chain**, one line each:
   - what the buyer asks, in their words;
   - what they find today, and whether it is *evidence* (someone ran something) or *advice*;
   - who gets cited in AI answers, counted from the answer text (citation markers, not pages);
   - the gap: advice only, or no answer;
   - what only Dot can show, using its own feature or data.
2. **The words buyers type.** Up to five phrases from the inputs, for the headline. Use only phrases that appear in the inputs.
3. **The run.** What to run in Dot, on which data, in which mode, and which numbers it must produce. Name the Playbook stage it runs.
4. **Sources rows** for the tracking sheet: source, URL or tool, what it showed, date.
5. **Stop conditions.** If evidence already exists, or only Dot's data could show it and Dot doesn't have that data, say "not a piece" and why.

Do not draft anything. No finding is written before its run.
