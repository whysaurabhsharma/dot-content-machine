# House structure and links

## The anatomy of a piece

Extracted from the pieces that already work on getdot.ai: Rick's essays, Anand's Cafe Bench and the AI Data Analyst Playbook.

1. **Title** in the words buyers type, saying what the reader gets (style rule 15).
2. **Bold opening**, up to 60 words: the reader's situation, the proof, then "By the end, you will have…" (style rule 16).
3. **The detail that makes it real**: the surprising number, in one short paragraph.
4. **Pocket guide**: five to eight numbered lines that are the whole piece.
5. **Three H2s, each a claim.** Method in plain words, then the finding, then what to do about it. Each limitation is paired with what the product does about it.
6. **One table, one chart.** The chart has alt text and a caption with the date and mode.
7. **Things to keep in mind**: two to four caveats, said once.
8. **Where Dot fits**: last H2, under 80 words, a docs link, and assumptions labelled.
9. **An instruction** the reader can act on today.
10. **CTA**, in italics: *If this excites you, we'd love to hear from you. Get in touch.*

## Internal-link inventory

Five or more internal links per piece, including the Playbook stage it runs (check 20). `verify_sources.py` must open every one before a piece ships.

### Verified

| URL | How it was verified |
|---|---|
| https://www.getdot.ai/blog/ai-data-analyst-playbook | Live; cited five times by Perplexity on 27 October 2026 |
| https://www.getdot.ai/context-agent | Opened in a browser by Saurabh, 28 October 2026 |
| https://www.getdot.ai/pricing | Opened 28 October 2026 |
| https://www.getdot.ai/blog/conversational-analytics | Opened 28 October 2026 |
| https://www.getdot.ai/blog/conversational-analytics-software | Opened 28 October 2026 |
| https://www.getdot.ai/blog/self-service-analytics-tools | Opened 28 October 2026 |
| https://www.getdot.ai/blog/microsoft-power-bi-pricing | Opened 28 October 2026 |
| https://www.getdot.ai/blog/tableau-pricing | Opened 28 October 2026 |
| https://www.getdot.ai/blog/microsoft-power-bi-alternatives | Opened 28 October 2026. The singular "alternative" returns 404 |
| https://docs.getdot.ai | Opened 28 October 2026 |
| https://www.getdot.ai/blog/your-ai-analyst-will-be-worse-next-month | Rick's drift essay. Opened by `verify_sources.py` (200), 1 November 2026; linked from B and F |
| https://www.getdot.ai/blog/from-10-to-90-percent-on-adyens-dabstep | The DABstep post. Opened by `verify_sources.py` (200), 1 November 2026; linked from B |
| https://www.getdot.ai/blog/how-companies-built-ai-data-analysts | Dot's census of 14. Opened by `verify_sources.py` (200), 1 November 2026; linked from B |

`check_piece.py` check 20 fails a `getdot.ai/blog/` link that names neither a piece's own slug (`pieces/<slug>.md`) nor a URL in this file (v1.8.27). To link a Dot page not listed here, open it first, then add it to this table.

### Seen in Ahrefs or Search Console, 27 October 2026

These pages rank or receive traffic, so they exist. Open each with `verify_sources.py` before linking to it.

| URL | Seen in |
|---|---|
| https://www.getdot.ai/ | Top pages |
| https://www.getdot.ai/pricing | Top pages |
| https://www.getdot.ai/context-agent | Top pages |
| https://www.getdot.ai/blog | Top pages |
| https://docs.getdot.ai | Top pages |
| https://www.getdot.ai/blog/microsoft-power-bi-pricing | Top pages; Search Console |
| https://www.getdot.ai/blog/microsoft-power-bi-alternatives | Top pages |
| https://www.getdot.ai/blog/tableau-pricing | Top pages |
| https://www.getdot.ai/blog/tableau-alternatives | Top pages |
| https://www.getdot.ai/blog/qlik-sense-alternatives | Top pages |
| https://www.getdot.ai/blog/decision-intelligence-software | Top pages; Search Console |
| https://www.getdot.ai/blog/self-service-analytics-tools | Top pages |
| https://www.getdot.ai/blog/self-service-bi-tools | Top pages |
| https://www.getdot.ai/blog/sisense-alternatives | Top pages |
| https://www.getdot.ai/blog/domo-pricing | Top pages |
| https://www.getdot.ai/blog/domo-ai-alternatives | Top pages |
| https://www.getdot.ai/blog/bi-tools-for-data-visualization | Top pages |
| https://www.getdot.ai/blog/ai-data-integration-tools | Top pages; Search Console |
| https://www.getdot.ai/blog/ai-dashboard-software | Top pages (web analytics) |
| https://www.getdot.ai/blog/conversational-analytics | Top pages; Search Console |
| https://www.getdot.ai/blog/conversational-analytics-software | Top pages; Search Console |
| https://www.getdot.ai/blog/marketing-analytics-tools | Search Console |
| https://www.getdot.ai/blog/thoughtspot-alternatives | Search Console |
| https://blog.getdot.ai/root-cause-analysis-how-to-uncover-key-drivers-behind-your-metrics-b52827c7e3d3 | Search Console |

**Do not link:** `/blog/looker-alternatives`, which Ahrefs marked "Lost" on 27 October.

### Named in the canon, URL still to find

- The semantic-layer essays

(Rick's drift essay and the DABstep post were found and moved to Verified, 1 November 2026.)

## Suggested links per piece

| Piece | Links to try first |
|---|---|
| 1 · Trust | The Playbook (Stage 3) · /context-agent · docs.getdot.ai (for "Where Dot fits") · /pricing · the drift essay |
| 2 · What changes | The Playbook (Stage 5) · /blog/self-service-analytics-tools · /blog/conversational-analytics · /blog/self-service-bi-tools · the root-cause analysis post |
| 3 · Cost and fit | The Playbook (Stage 5) · /pricing · /blog/microsoft-power-bi-pricing · /blog/tableau-pricing · /blog/microsoft-power-bi-alternatives |

## Reverse links to request at handover

Three existing pages per piece should link to it, with anchor text. Start with the Playbook's stage cards, the DABstep post, and the pricing pages above.
