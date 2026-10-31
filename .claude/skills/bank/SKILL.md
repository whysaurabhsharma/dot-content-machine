---
name: bank
description: Stage 3 BANK. The monthly entry point to the question bank. `add` puts new questions in (sales calls first), `rescore` re-scores the four factors, `top` names the next question to write. Started only by a person or the workflow.
disable-model-invocation: true
argument-hint: <add|rescore|top>
allowed-tools: Read, WebSearch, WebFetch, Bash(python scripts/bank.py:*), Bash(python -I scripts/bank.py:*), Bash(python scripts/timing.py:*), Bash(python -I scripts/timing.py:*)
---

# Stage 3 · BANK

Read `bank/README.md` first: it records what the bank's inputs can and can't measure. Source of the method: the ICP question bank PDF, page 4.

**The command:** the first word of `$ARGUMENTS` is `add`, `rescore` or `top`. Anything else: stop and say so.

## Timing

First action: `python scripts/timing.py bank bank start`. Last action: `python scripts/timing.py bank bank end`. Stage names: `runs/README.md#timing`.

## Inputs and output

- Reads: `bank/questions.csv`, `data/ahrefs/keywords.csv` (frozen snapshot, 27–28 October 2026), `measure/citations.md`, and getdot.ai and docs.getdot.ai, live.
- Writes: `bank/questions.csv`, only through `scripts/bank.py`. `rescore` also writes the dated copy `bank/scores-YYYY-MM-DD.csv`. Never edit the CSV by hand, and never change the bank's text columns (question, ai_form, demand, gap, weak_competition, evidence, source).

## add

The person gives the new questions, each with its source. For each, run:

    python scripts/bank.py add --question "<short Google form>" --ai-form "<long form>" --persona "<persona>" --type <problem|evaluation|comparison|implementation> --source "<source, who, date>" [--sales-call]

Use `--sales-call` only when the source is a sales call. Search Console questions can be added only from a CSV the person exports into `data/`; access through Ahrefs ended on 31 October 2026. Then do `rescore` for the new rows.

## rescore

1. `python scripts/bank.py rescore`. It scores **demand** by counting the external sources each row names, writes Ahrefs volume as a note ("not measured" where there is no row), and keeps every judgement score already set.
2. **Gap at Dot**, for every unwritten row: fetch the sitemaps of www.getdot.ai and docs.getdot.ai, pick the candidate pages, and open them before scoring 1 or 2. (On 31 October 2026, `site:getdot.ai` and `site:docs.getdot.ai` searches returned no Dot pages at all, so the sitemaps are the method; searches are only a supplement.) 1 = a Dot page answers it; 2 = Dot touches it in passing (an essay, a docs page); 3 = Dot has nothing. Record with `bank.py set <id> gap <n> --basis "<URLs opened, or 'none found', and the date>" --by model`.
3. **Evidence advantage**, for every unwritten row: 1 = anyone could write it; 2 = Dot's customer proof helps; 3 = only running Dot (an eval, a walkthrough, a deep analysis) can produce the evidence. The test: could the piece hold a screenshot nobody else can take? A 3 must pass two more tests, and the basis says which: **(1)** the feature it relies on is Observed in `facts/dot-facts.md` or `facts/dot-mcp.md` (an Assumption doesn't count); **(2)** Dot's connected data actually holds what the test needs (on 31 October 2026, only the Olist orders and items tables). If either fails, score 2 or 1 and say which test failed. Record with `--by model` and a one-line reason. It stays "model-unconfirmed" until a person runs `bank.py confirm <id> evidence`.
4. **Weak incumbent, for the shortlist only:** `python scripts/bank.py shortlist --n 15`. It keeps a tie at the cut whole, so it can return more than 15. For each one, run WebSearch on the question, read the first three distinct pages in full with WebFetch, and score 1 = a strong page with original evidence ranks; 2 = decent pages, none with original evidence; 3 = only generic, undated or vendor-pitch pages. The basis names the three URLs, says the order is WebSearch's, not Google's, and gives the date. Every other row stays "not scored: outside the shortlist".
5. Report: how many rows have each factor scored, the shortlist, and the list of evidence scores waiting for a person to confirm.

## top

Run `python scripts/bank.py top` and report its output word for word. It puts sales-call questions first (hard rule 1), and refuses to recommend a question whose evidence score is unconfirmed. Don't override it, and don't pick a question yourself.

## Must not

- Estimate a search volume, or treat Ahrefs volume as part of the demand score.
- Match a phrase to an Ahrefs row that isn't the same phrase.
- Confirm an evidence score. Only a person confirms.
- Score weak incumbent outside the shortlist, or describe the whole bank as assessed.
- Present WebSearch order as Google ranking.
- Change a question's status. Writing a piece changes it.
