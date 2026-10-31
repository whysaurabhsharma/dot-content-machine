# CLAUDE.md — Dot content machine

This file is the single source of every rule. Product statements live in `facts/dot-facts.md`, each marked Observed, Assumption or Confirmed. Claude Code reads it automatically from the repo; there is no copy to keep in step. To change a rule: edit here and add a dated line to the change log at the bottom.

## What this machine makes

Evidence-led pieces for getdot.ai, 900–1,300 words. Each piece is one stage of the AI Data Analyst Playbook, actually run. LinkedIn posts are cut from the pieces, never written separately.

## Hard rules

A piece that breaks any one of these does not ship.

1. **Questions come from sales calls first.** Search volume breaks ties; it never picks the topic.
2. **No finding is written before its run.** Titles come after the run, from the Figures tab only.
3. **Every number has a Figures row**: value, where it was computed, date.
4. **Nothing from the rehearsal (23–24 October), or from another account or dataset, appears in a piece unless it recurred in that piece's own run.** A piece's own run stays valid until its data, definitions or product version change; re-run then. This bars findings, not tools: prompts, scripts and rules may be ported.
5. **Every product claim has evidence in the piece, a yes from Dot, or an "Assumption" label in the text.** Unlabelled and unconfirmed means cut.
6. **"We" means Dot.** The subject is a team rolling out an AI analyst; Dot is the instrument, not the defendant. Every limitation is paired with what the product does about it, or cut.
7. **No bracket citations.** Sources are links on the words that need them.
8. **Human-supplied claims go through the same fact-check as model output.**
9. **Record the dataset and its licence in Sources** before the first run. For the trial, Dot asked for any realistic dataset, since the point is the method.
10. **Cost per answer is published as a credits range, with dollars alongside, labelled as an assumption.** The conversion is facts/dot-facts.md A2 (1 credit ≈ $1), and the docs caveat that the same question can take different paths stays in.

### Evidence rules

11. **Never state a setting for every row after opening one.** Open them all, or write "the rows I opened".
12. **Classify a gap before counting it**: display rounding, or a real disagreement. Only the second is a finding.
13. **Every product quote names its question.** If the quote came from a chat, don't use it to describe an evaluation run, or say plainly which it came from.
14. **Screenshot the mode selector at the start of every batch**, and log the mode per batch. A written reminder wasn't enough; the check has to leave evidence.
15. **Read the credit balance before and after every batch.** One reading across mixed modes can't be split.
16. **Count from the source text, never by eye, and recount before a number is used a second time.**
17. **Every run carries its conditions**: the account, the environment, the mode, and which context notes were active.
18. **Judge recurrence item by item, not only in total.** Matching totals with changed items is a different finding, and usually a stronger one.

## Style rules

1. 900–1,300 words. Cut a section, not sentences.
2. Bold lede with a number and a named thing.
3. Pocket guide after the lede: five to eight lines that are the whole piece.
4. H2s are claims. Never questions.
5. Method in plain words, then one table, then one chart.
6. One "Things to keep in mind" box, two to four caveats, said once.
7. Named companies and quotes with links. Use the canon: the Playbook, the drift essay, the semantic-layer essays, DABstep.
8. "Where Dot fits" is the last H2, under 80 words, with a docs link.
9. End on an instruction, then: *If this excites you, we'd love to hear from you. Get in touch.*
10. Sentences average under 18 words. No paragraph over four sentences.
11. Read every paragraph aloud, once on a phone screen.
12. **Quotable lines carry their own subject.** Models lift self-contained claims, not lines that lean on the sentence before.
13. SEO title contains the query. Meta under 155 characters. Slug four to six words.
14. Every image has alt text and a caption with the date and energy mode.
15. **Titles use the words buyers type and say what the reader gets.** Check the words against Search Console queries, Keywords Explorer and the pages that already rank. A clever title nobody searches for fails.
16. **The first 60 words say what the reader will have by the end.** The problem, the proof, then the promise: a test, a number, a fix.
17. **A post's first two lines give a reason to click:** the reader's stake, then the promise. The post ends by saying what the link delivers.

## Banned

Starter list. The EDIT stage adds to it; each addition gets a change-log line.

- unlock, leverage (as a verb), seamless, robust, game-changer, revolutionary, delve
- "in today's fast-paced world", "it's important to note", "at the end of the day"
- "our" for anything that isn't Dot's
- a question as an H2
- any figure without a Figures row

## Measurement

The monthly AI baseline is Site Explorer's AI-responses panel — all platforms, Perplexity and AI Overviews — read on the same day each month. Brand Radar isn't in Dot's plan. Manual buyer prompts supplement the panel; they don't replace it. Citation markers are counted as markers and never called sources.

## The seven stages

RESEARCH → OUTLINE → DRAFT → READER → FACT-CHECK → EDIT → LINKEDIN

Each stage has a prompt in `prompts/`. Four decisions stay human: the question, the outline, the title, the publish.

1. **RESEARCH.** The gap chain: the buyer's question, what they find today, the gap type, what only Dot can show. Output: Sources rows, dated.
2. **OUTLINE.** The Playbook template. Gate: no number that isn't already in Figures. A human approves before drafting.
3. **DRAFT.** 900–1,300 words against the style rules.
4. **READER.** A Head of Data at a 300-person company, four minutes. Returns three places they'd stop reading, the one sentence they'd quote to their CFO, and the one claim they don't believe. Rewrites nothing. The writer then fixes all three stopping points.
5. **FACT-CHECK.** Two passes. First, a fresh chat with the draft only and no other context. Second, a different model. Each returns every number checked for internal consistency, every product claim marked VERIFIABLE or ASSERTED, every conclusion that outruns its evidence, and every quote checked for attribution. Then `verify_sources.py` on every URL.
6. **EDIT.** `check_piece.py` clean. A headline test: would a buyer know in three seconds what they get? Then the lift test: paste the piece into Perplexity and Claude, ask each for three bullets with one quotation each. Rewrite until the intended lines are lifted, or until the lifted lines are better than the intended ones.
7. **LINKEDIN.** Under 150 words. Three first lines tried; the most specific kept. A number within three lines. No hashtags, no emoji. Ends on an action. The link goes in the first comment with a UTM.

## The gate: 24 checks

A "no" on any line means the piece isn't done. Who checks each line is in brackets: script, model, or human.

**Headline and opening**
1. The title uses the words buyers type and says what the reader gets. (human, against search data)
2. The first 60 words say what the reader will have by the end. (human)
3. The SEO title contains the query; meta under 155 characters; slug of four to six words. (check_piece.py)
4. A bold lede with a number and a named thing. (check_piece.py)
5. A pocket guide of five to eight lines. (check_piece.py)

**Structure and style**
6. 900–1,300 words. (check_piece.py)
7. Sentences average under 18 words; none over 25. (check_piece.py)
8. No paragraph over four sentences. (check_piece.py)
9. Every H2 is a claim, not a question. (check_piece.py)
10. One table; one chart with alt text and a dated caption. (check_piece.py)
11. One "Things to keep in mind" box with two to four caveats. (check_piece.py)
12. "Where Dot fits" is last, under 80 words, with a docs link. (check_piece.py)
13. Ends on an instruction, then the italic CTA. (check_piece.py)
14. "We" means Dot. (human)

**Evidence**
15. Every number has a Figures row; check_piece.py and verify_sources.py are clean. (scripts)
16. Every finding comes from this dataset's run. (human, against the Run Log)
17. Every product claim is evidenced, confirmed, or labelled "Assumption". (check_piece.py flags unlabelled claims; human confirms)
18. The dataset and its licence are recorded in Sources. (human)
19. No brackets, placeholders, or byline nobody approved. (check_piece.py)

**Links**
20. Five or more internal links, including the Playbook stage, each opened to confirm it. (verify_sources.py)
21. Three reverse links listed, with anchor text. (human)

**Review**
22. READER pass done and its three stopping points fixed. (model, then human)
23. Lift test in Perplexity and Claude; the intended lines are the ones quoted. (model)
24. Read aloud once, on a phone, today. (human)

## Change log

**27 October 2026 — v1.** Written after the first live run. Added hard rules 11–15 and style rule 12; tightened hard rule 5. Origins:

- **Rule 11.** The piece 1 draft claimed 3% tolerance on all twenty rows. One row had been opened.
- **Rule 12.** Two of the three "gaps" the draft counted were display rounding (97 vs 97.02; 1.14 vs 1.14).
- **Rule 13.** The fact-check found three unattributed product quotes, taken from chats and used to describe an evaluation run.
- **Rule 14.** The mode drifted from Economy to Balanced at request 22 of 29, unnoticed.
- **Rule 15.** 18.3 credits were spent across mixed modes; the cost per mode couldn't be recovered from one reading.
- **Style rule 12.** The lift test skipped both of the draft's aphorisms and quoted self-contained claims instead.
- **Rule 5, tightened.** Three claims in "Where Dot fits" had neither evidence nor a yes.

**27 October 2026, 19:30 — v1.1.** Added rule 16. Origin: the Perplexity citation counts were tallied by eye in chat and carried into the Run Log; recounted from each answer's text, eight of the sixteen figures were wrong, and the correction revealed getbruin.com as the most-cited domain across all three buyer prompts.

**27 October 2026, 19:50 — v1.2.** From review of the Day 1 report by the dry-run and roadmap chats. Amended rules 4 and 14; added rules 17 and 18 and the Measurement section. Origins:

- **Rule 4, amended.** Building the machine needs the dry run's tested prompts and scripts; the rule was written to bar findings, and now says so.
- **Rule 14, made mechanical.** The mode drifted to Balanced despite the written rule.
- **Rule 17.** Piece 2's run didn't record that the metric definitions note was active, though eight answers were scoped to delivered orders because of it.
- **Rule 18.** The report said piece 2 "reproduced the dry run exactly". The totals matched; four requests had changed outcome.
- **Measurement.** Site Explorer's AI-responses panel was on screen all afternoon and unused.
- **For check_piece.py when it's ported:** a closing quote after a question mark must end a sentence. Without that, today's measurement reported a 37-word sentence that is really two.

**27 October 2026, 21:30 — v1.3.** From Rick's feedback at the Day 1 check-in. Amended rules 5 and 9; added style rules 15–17; numbered the gate as 24 checks with who checks each; added a headline test to EDIT. Origins:

- **Rule 5.** Rick asked for product features to be taken as assumptions and labelled as such, rather than blocking on confirmation.
- **Rule 9.** Rick confirmed any realistic dataset is fine for the trial, because Dot wants to see the thought process.
- **Style rules 15–17 and the headline test.** Rick couldn't tell from piece 1's title what it would deliver, and the post gave no reason to click. Buyers search phrases like "best AI data analyst 2026"; the pages that rank for it are numbered lists of tools, several leading with accuracy scores.
- **The numbered gate.** "22 checks" was quoted without the list behind it. The gate is now 24 numbered checks: the original 22 plus the two headline checks.

**27 October 2026, 22:15 — v1.4.** Saurabh answered the product-claim list as assumptions, on Rick's instruction to assume and say so. Amended rule 10. Origins:

- **Rule 10.** Saurabh: cost per answer may be published in dollars, as an assumption. The conversion (1 credit ≈ $1) rests on the signup page's “$300 in free credits” and Saurabh's answer that 300 is the full credit total: 100 at signup, the rest earned by connecting. No Dot pricing page states a price per credit.
- **Facts file.** All seven claim-list answers recorded in `facts/dot-facts.md` as assumptions A1–A8, each with its basis. Line 6 (re-scoring on save) was also observed twice.

**28 October 2026 — v1.5.** From the machine's first run in the Claude Project (piece 2, RESEARCH). Clarified rule 4. Origins:

- **Rule 4.** The RESEARCH stage, run on 28 October, read "today's data" as excluding the piece's own run from 27 October and asked for a re-run. The rule was written to bar rehearsal findings, not the trial's own runs. It now says so, and says when a run expires.
- **Facts O4 and O11.** RESEARCH flagged "25 answered" and "26 returned a result" as a conflict. They aren't: 26 is 25 answered plus one refusal that returned a coverage statement. O4 now says that. RESEARCH also flagged that "answered" isn't "correct", so the 25 checkable answers were recomputed from the raw CSVs (O11): all 25 correct.

**28 October 2026 — v1.6.** Voice decided: Rick's voice, "we" meaning Dot (facts D1, was A9). All three pieces and six posts converted; quoted inputs left as asked. Rule 6 unchanged; check 14 now has a decided standard.

**29 October 2026 — v1.6.1.** Voice conversion completed outside the article bodies: piece 2's title and meta, piece 3's meta and chart caption, and a stale note in posts/piece-2-posts.md still said "I". Prompt 03 still told DRAFT to write as "I"; it now states Rick's voice. Cause: the D1 conversion was checked on the article text only. Check 14 now needs the front matter and chart captions read too.

**31 October 2026 — v1.6.2.** Screenshot scheme added; rule 14's text unchanged. The scheme for the conditions screenshots now lives in [runs/README.md#screenshots](runs/README.md#screenshots): `runs/screenshots/<piece>-batch-<n>-{mode,credits-before,credits-after,environment,notes}.png`, taken in Dot's own UI, with each path referenced in the run file. Origin: the 31 October smoke test found that mode, credits, environment and active context notes are not observable via MCP ([facts/dot-mcp.md](facts/dot-mcp.md)).

**31 October 2026 — v1.6.3.** Header updated: the Claude Project is gone, and CLAUDE.md is now read automatically by Claude Code from the repo. The re-paste step is removed; a rule change is an edit here plus a change-log line. Earlier entries that mention the Project are left as written, since they record what happened then.

**31 October 2026 — v1.6.4.** Created [facts/run-format.md](facts/run-format.md): the run-file format that `dot-runner` writes and that check 16 and `scripts/mark_run.py` both read. Its worked example is the real question and answer from check 1 of the smoke test (`runs/smoke-test.md`). Question numbers run continuously across batches. A change to the format is made there first, with a line here.

**31 October 2026 — v1.6.5.** Check 17 tightened; posts checked. Origin: the A3 correction. Facts O7 read 300 base credits on 31 October, superseding the 100 recorded on 27 October, and A3 ("100 at signup plus the rest earned") was superseded. Piece 3 and post E still said "100 credits covers about 170 answers", and both passed every check because each sentence was labelled "Assumption"; only a hand search found them.

- **Check 17.** A piece now fails if it uses a keyword of an assumption that `facts/dot-facts.md` marks superseded, even when the sentence is labelled. Labelling covers an open assumption, not a contradicted one.
- **Posts.** `check_piece.py --post <file>` runs each post against stage 7 and style rule 17, plus checks 15, 17 and 19 against its piece's figures. On post E as it stood before the fix, it fails 15 (100 and 170 not in Figures) and 17 (superseded keyword).


**31 October 2026 — v1.6.6.** From the second fact-check of `ai-analyst-follow-up-questions` (Gemini and ChatGPT). Check 15 widened to code; the link check and the lift test tightened. Origins:

- **Check 15, code blocks.** Both models called the piece's central claims unverifiable because no SQL was shown. Dot's SQL may now appear in a piece as fenced code. `check_piece.py` leaves code out of every prose check: words, sentences, Figures rows and banned words. In return, each code block must appear whole in the piece's run file, word for word, as consecutive lines, or check 15 fails. A first version compared line by line; a test showed a line borrowed from a different query in the same run file passed, so it now compares whole blocks.
- **verify_sources.py.** A HEAD request answered with 404 now falls back to GET, as 403 and 405 already did. Kaggle answers HEAD with 404 and GET with 200, so the Olist link failed falsely.
- **Lift test record.** Each piece now keeps `reviews/<slug>/lift-lines.md`: the intended lines before the test, what each tool lifted after it, verbatim. An unintended lift that is better is added to the list. Claude may decline to give three verbatim quotes; record how many each tool gave ([prompts/06-edit.md](prompts/06-edit.md), section 3).
- **Records that overclaim are corrected too.** The piece said Dot "re-ran the query rather than repeating a stored figure"; identical SQL doesn't show that, and execution is not observable via MCP. The run file's Finding 1 and the truth spec's T5 wording made the same claim and were corrected, though neither is published.
