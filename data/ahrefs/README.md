# Ahrefs snapshot, 27–28 October 2026

Every Ahrefs reading recorded during the trial, taken in Dot's Getdot workspace on
27 and 28 October 2026. Ahrefs access ended on 31 October 2026, so this is a frozen
snapshot, not a live source.

**Do not edit these files.** A later reading goes in a new dated file
(for example `keywords-2026-12-01.csv`), never over the top of these.

## Files

| File | What it holds | Source |
|---|---|---|
| `keywords.csv` | 21 phrases from Keywords Explorer, US. 18 buyer queries plus 3 rehearsal phrases. | Keywords Explorer, 27–28 Oct 2026 |
| `site-overview.csv` | Site Explorer for getdot.ai: DR, organic keywords, traffic, AI responses, top-page movement. | Site Explorer, 27 Oct 2026 |
| `search-console.csv` | Search Console totals through Ahrefs GSC Insights, last 90 days to 27 Oct. | GSC Insights, 27 Oct 2026 |
| `search-console-queries.csv` | The 12 per-query rows recorded from the same report. Split from `search-console.csv` so each file holds one table. | GSC Insights, 27 Oct 2026 |
| `rank-tracker-queries.csv` | The 18 Rank Tracker keywords (9 queries × US/English and Germany/German), added 28 Oct. Positions are empty: none was ever recorded. | Rank Tracker setup, 28 Oct 2026 |

## Rules for using this snapshot

- A phrase not in `keywords.csv` is written as **"not measured"**. Never estimate a volume.
- `not indexed` is what Ahrefs displayed for those phrases. It is **not** a recorded zero.
- Volumes are as Ahrefs displayed them (1.2K, 2.0K, 2.4K). The exact integers were never recorded, so do not convert them to whole numbers.
- Any piece citing these numbers must date them: "Ahrefs, 27–28 October 2026."

## What was never recorded, and is therefore absent

- Rank Tracker positions. The tracker showed 0 while waiting for its first read.
- Keyword difficulty for 15 of the 21 phrases.
- Global volume for `semantic layer` and `metric definitions`. The trial tracking sheet shows 7.9K and 40, but only from a screenshot that was never logged, so both are marked "not measured".
- Per-query clicks for 10 of the 12 Search Console rows; those rows record CTR only.
- The period for the 81.2K impressions / 561 clicks / 0.7% / position 9 reading. It comes from the Day 1 plan, which never states its period.
- The platform split for the other 107 of the 380 AI responses. Only AI Overviews (224) and Perplexity (49) were recorded.
- Any Ahrefs reading after 28 October 2026.

## If Ahrefs access returns

    claude mcp add ahrefs --transport http https://api.ahrefs.com/mcp/mcp

Lite plan or higher. Refreshed readings go in new dated files; these stay as they are.
