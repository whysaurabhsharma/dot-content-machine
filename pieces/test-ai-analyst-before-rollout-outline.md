# OUTLINE: "How do I test whether an AI data analyst gives correct answers before rolling it out?"

Piece: `test-ai-analyst-before-rollout` · Format: guide · Bank #35 · 1 November 2026. Evidence: `runs/test-ai-analyst-before-rollout-research.md` section 7; figures `figures/test-ai-analyst-before-rollout-figures.csv` (five census sources re-read in a browser, `runs/test-ai-analyst-before-rollout-verification.md`). Licence: decision L4.

**Ground rules this outline follows.**
- The guide answers the buyer's question for the buyer's own rollout. Our runs are evidence for a step, never the subject.
- Every step is tagged: **ours** (a run of ours), **cited** (a census publication; "done by X", not "shown to work"), or **untested**. Hard rule 19: no step claims a fix nothing tested.
- Rule 4(d): a cited number never sits beside, or confirms, one of ours. Steps that have both keep them in separate sentences, each with its own source.
- Our run scores are always split (v1.8.10): A, 5 correct as asked and 3 only under the delivery-date reading (RA-SPLIT); piece 2, 9 and 3 (RP2-SPLIT). Never "8 of 8" or "12 of 12" alone.
- Hub: links to A (`/blog/ai-analyst-follow-up-questions`) at steps 3–5 and to B (`/blog/how-companies-test-ai-data-analysts`) at steps 1, 6 and 8. Both link back once F is live (pre-publish).

## 1. Title candidates

Buyer phrases from research section 2 only: "ai data analyst" (700 US), "ai data analyst accuracy" and "how to evaluate ai data analyst accuracy" (not indexed), "text to sql accuracy" (10 US).

1. **"How to Test an AI Data Analyst Before Rollout: 8 Steps"**. **Recommended:** a guide title names what the reader gets (style rule 15); the head term carries the volume; "8 steps" is countable from the piece.
2. "How to Evaluate AI Data Analyst Accuracy Before You Roll It Out". The exact long-tail phrase, but Ahrefs shows it not indexed, and it promises no deliverable.
3. "Test Your AI Data Analyst Before Rollout. Each Step Comes From a Real Run." Says why to trust it; at 12 words it is long, and "Real Run" needs the opening to explain.

## 2. The opening (57 words)

**To test an AI data analyst before rollout, ask real questions with every right answer written down first. Ask each twice, in fresh chats, and read the SQL. In our run on Dot, one question returned 2,878 and 2,453. By the end, you'll have eight steps, each resting on a run of ours or a published method.**

(2,878 and 2,453: RP2-MR-Q5, RP2-MR-Q11. The answer to the question is in the first two sentences: hard rule 20. Count check at draft.)

## 3. The surprising detail

Both numbers were right. Piece 2 asked how many 2017 orders were delivered late, in two fresh chats, worded identically. One answer counted late by timestamp, the other by calendar day: 2,878 (RP2-MR-Q5) and 2,453 (RP2-MR-Q11), 425 apart (RP2-F08). A test with one expected answer would have failed one correct number and passed the other.

## 4. Pocket guide

1. Collect real questions your team already asked.
2. Write every answer you would accept before you ask.
3. Ask each question twice, each time in a fresh chat.
4. Open the SQL behind every answer, not only the text.
5. Test a follow-up chain, then ask its first question again in a fresh chat.
6. Mark by hand first; separate display rounding from real disagreement.
7. Decide the bar a result must clear before you see the results.
8. Re-run on a schedule, and whenever something the analyst depends on changes.

## 5. Three H2s

### H2 1: Eight steps test an AI data analyst before rollout, each resting on a run or a publication

Holds the numbered list (section 6). Figures: as listed per step.

### H2 2: A right answer to a question you didn't mean passes a one-answer test

Steps 2–5 explained. Ours: in A, the follow-up chain read "delivered in 2017" by purchase date and the fresh chat by delivery date, 691 apart (RA-F12); in A, 5 answers were correct as asked and 3 only under the delivery-date reading (RA-SPLIT); in A, every answer came back with SQL (RA-F16) but only 5 of 8 texts named their date (RA-F15). Cited, separate sentences: LinkedIn found about 60% of its benchmark questions have more than one valid answer (LIN-3) and underreported recall by 10-15% without them (LIN-4).
Limitation paired with what the product does: the answer text doesn't always name its date; Dot returned its SQL with every answer in both runs (RA-F16, RP2-F05), and the SQL named the date column.

### H2 3: A test passed at launch needs a bar and a schedule

Steps 7–8. Cited: Anthropic's offline accuracy drifted from about 95% at launch to about 65% over a month, "before we treated this as an engineering problem" (ANT-5, ANT-6; the clause is kept, see note). Anthropic "initially used ~90%" as a launch bar (ANT-13), the only numeric bar in B's census of 13 (C-8, C-1). Five of 13 re-run on a change, before each deploy, or daily (C-6). Uber does "not over-index decisions based on ~5% run-to-run changes in most metrics" (UBR-1). No run of ours re-ran after a change: the step is **cited** only, and the piece says so.

**Note on the drift sentence.** The browser re-read shows Anthropic's sentence continues "…over a month before we treated this as an engineering problem." F quotes the clause, so the drift reads as a condition Anthropic then addressed, which is what makes "re-run on a schedule" the lesson.

## 6. The body the format needs (guide)

One numbered list of eight steps, each starting with a verb (style rule 5). For each: the step, one to three sentences, and its evidence tag in plain words.

1. **Collect the questions your team already asked**, from chat threads, tickets and dashboards. *Cited:* 8 of the 13 companies in Dot's census build their test set from real questions or ground-truth answers (C-4, link B); LinkedIn's experts wrote 133 questions across 10 product areas (LIN-10, LIN-2). Done by them, not shown to work better than invented questions.
2. **Write every answer you would accept before you ask**, with its definition (table, filter, date). *Both:* our runs computed every expected answer, both readings of an ambiguous phrase, before the first question (A, link). LinkedIn: about 60% (LIN-3), 10-15% (LIN-4), in its own sentence.
3. **Ask each question twice, each time in a fresh chat.** *Ours:* piece 2, 5 of 6 pairs matched (RP2-F07); the sixth returned 2,878 and 2,453 (RP2-MR-Q5, RP2-MR-Q11), two definitions of late.
4. **Open the SQL behind every answer.** *Ours:* in A, all 8 answers came back with SQL (RA-F16); the text named the date in 5 (RA-F15); for two of the other three, a person read the date from the SQL.
5. **Test a follow-up chain, then ask its first question again in a fresh chat.** *Ours, one chain:* in A, the chain kept its reading across 4 turns (RA-F04; Q5 returned Q1's 43,428, RA-MR-Q5), and the fresh chat read the phrase another way (691, RA-F12). One chain is evidence the drift can happen, not how often.
6. **Mark the answers by hand first, and sort each gap**: display rounding or a real disagreement. *Both:* ours, A's two shares, 5.6% and 7.7%, were display rounding of exact values (RA-MR-Q3, RA-MR-Q4). Cited, separate sentences: Hex's LLM judge accepted 2.03% for a right answer of 2.04% 35% of the time (HEX-2, HEX-1, HEX-3); LinkedIn's judge lands within 1 point of the human score 75% of the time (LIN-7, LIN-6). No claim that a judge can replace hand-marking.
7. **Decide the bar a result must clear before you see the results.** *Cited, one company:* Anthropic "initially used ~90%" (ANT-13), 1 of 13 in the census (C-8). The right bar for your team is **untested**, and the step says so. **Saurabh at approval (1 November 2026):** the step must say plainly that it rests on one company, and the right bar stays labelled untested. The draft gives no threshold of its own: a guide that invents one is the untested remedy hard rule 19 bars.
8. **Re-run on a schedule, and whenever something it depends on changes**: a definition, a table, a model. *Cited:* Anthropic's drift (ANT-5, ANT-6, with the clause); 5 of 13 re-run (C-6, link B); Uber's ~5% noise (UBR-1) as the reason to set a threshold for "changed". No run of ours re-ran after a change.

No table or chart required for a guide (style rule 5). None proposed.

**Cut, per research section 7:** "include a question the data can't answer" (thin, untested); any count of how many test questions you need (the census runs from a handful of queries to 201 questions, so PLAN's post 4 angle is unsupported); any claim that a context note or definition fixes ambiguity (notes were on in both runs and answers still diverged); any cost per answer (rule 14 waived).

## 7. Things to keep in mind

- **Our runs are small and on one dataset.** Two runs, on Olist's public e-commerce data, with conditions recorded by hand (rule 14 waived). They show the steps catch something, not how often.
- **The census practices are self-reported.** "8 of 13 do it" means they say they do it; no publication shows its method beats another.
- **Two things this guide doesn't set: how many questions, and what bar.** No run of ours tested either; the census ranges too widely to suggest one.
- **A written definition didn't stop two readings.** Context notes were on in both runs; answers still read "delivered in 2017" two ways. The steps catch it; nothing here shows a note prevents it.

## 8. Where Dot fits (under 80 words; draft must count)

"Dot answers data questions for your team." (facts/dot-entity.md, hard rule 23). Dot's evaluation holds each test question with an expected answer, a unit and a tolerance, and shows a verdict such as "Exact match" (O1). It re-scored on save, without a re-run (O2); Assumption: it always does (A7). We haven't tested it against the steps above. Docs link: docs.getdot.ai evaluation page (verify_sources at draft).

Pre-publish (same as B): re-check O1 and O2 on the current account; both were observed on 27 October 2026.

## 9. The instruction

Pick the questions your team asked last month, and write down every answer you would accept for each, before you ask your AI analyst anything.

Then the CTA: *If this excites you, we'd love to hear from you. Get in touch.* (Kept pending Rick's answer on the closing line, HANDOVER.md.)

## 10. Missing figures

- None in the outline. Two links must be opened before the draft cites them: Dot's essay "Your AI Analyst Will Be Worse Next Month" (if F links it at step 8), and the Playbook (stage name unconfirmed; link without naming the stage unless checked).

## 11. Quotable line

Quotable line: Ask each test question twice, in fresh chats: in our run on Dot, one question returned 2,878 and 2,453, both correct.

(19 words. Numbers RP2-MR-Q5, RP2-MR-Q11; "both correct" rests on each matching a computed definition. Placed in the opening; it carries its own subject.)

## 12. Freshness

Freshness: measured 31 October 2026 (piece 2's run, Olist, Dot's product as of that day); re-run at Dot's next product release that touches chat answers or evaluation, and by 1 February 2027 at the latest. Census figures: re-read when any of the five publications is updated.

Approved by: Saurabh
Date: 2026-11-01
