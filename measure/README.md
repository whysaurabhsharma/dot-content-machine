# Measurement: how to take a reading

The baseline is the manual reading of the buyer queries: each query in Google's top ten, Perplexity and ChatGPT (CLAUDE.md, Measurement, v1.8.26). Each reading goes in a new file, `measure/baseline-YYYY-MM-DD.md`. Once committed, a reading file is **never edited**. A correction goes in the next dated file, with a line saying what was wrong. This is the same convention as `data/ahrefs/`.

| File | What it is |
|---|---|
| `baseline-2026-11-01.md` | The first baseline: 5 of the 18 buyer queries, 15 readings, before any piece was live. Dot cited 0 times |
| `citations.md` | The earlier Perplexity series on three topic labels, 27–29 October 2026. Closed; not comparable with the baseline files |

## Conditions (rules, CLAUDE.md Measurement)

- **Perplexity: signed in, to the same account every time.** An anonymous session allows one query, and a signed-out reading isn't comparable with a signed-in one.
- **Google: a private window, signed out, from the same location as the last reading.** If the location differs, record the difference. The first baseline was read in Gurugram, India, and Google's footer still said "Based on your past activity".
- **ChatGPT:** record the plan and whether you were signed in. The first baseline was read on the free tier, signed out.
- Record the date, location, sign-in state and plan for each engine before the first query.

## Two corrections to the first baseline's method

The 1 November 2026 reading left two things out. Do them from the next reading on:

1. **Paste each answer's full text,** for Perplexity and ChatGPT alike. The first baseline recorded counts and summaries but not the answers, so its counts can't be recounted. Hard rule 16 says to count from the source text and recount before a number is used again; that needs the text.
2. **Name inline citation markers and source-panel entries separately.** Perplexity shows both: numbered markers in the answer, and a list of pages beside it. The first baseline called both "sources". CLAUDE.md says markers are counted as markers and never called sources. Record two lists per answer, "markers by domain" and "panel entries by domain", and never call either one sources.

## Each reading

1. Copy the previous baseline's list of queries, so readings stay comparable. Add queries only at the end, and say which are new.
2. Fill in the conditions table.
3. For each query, record:
   - **Google:** the top ten (domain, title, page type), whether getdot.ai appears, and whether there's an AI Overview.
   - **Perplexity and ChatGPT:** the answer in full, markers by domain, panel entries by domain (Perplexity), and whether Dot appears.
4. Report results per query and per engine, with the kind of source. Never give a single "AI citations" total: the first baseline found the kind of source changes with the question type (HANDOVER.md section 5).
5. Name the queries left unread.
