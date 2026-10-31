# Stage 3 · DRAFT

Runs in this repo as the `/draft` skill (`.claude/skills/draft/SKILL.md`), which refuses to start until the outline's "Approved by" line is filled.

Write the piece from the approved outline below. Follow CLAUDE.md's style rules exactly.

- 900–1,300 words. Sentences average under 18 words; none over 25. No paragraph over four sentences.
- Open with the outline's opening, in bold. Then the surprising detail, then the pocket guide.
- Every H2 is a claim. Method in plain words, then one table, then one chart.
- Every number comes from the Figures tab. Every product statement comes from facts/dot-facts.md: Observed and Confirmed facts stated plainly, Assumptions with the word "Assumption" in the same sentence.
- Quotable lines carry their own subject; they must make sense out of context.
- Product quotes name the question and chat they came from.
- Links on the words that need them; no bracket citations.
- Rick's voice: "we" means Dot (decision D1). Never "I". Quoted questions typed into Dot stay as typed.
- End with the instruction, then: *If this excites you, we'd love to hear from you. Get in touch.*

Return the piece as markdown, with the front matter fields from the outline (title, seo_title, meta, slug, queries, figures, reverse_links).

**Approved outline:** {paste}
