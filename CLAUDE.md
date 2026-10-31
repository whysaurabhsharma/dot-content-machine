# CLAUDE.md — Dot content machine

This file is the single source of every rule. Product statements live in `facts/dot-facts.md`, each marked Observed, Assumption or Confirmed. Claude Code reads it automatically from the repo; there is no copy to keep in step. To change a rule: edit here and add a dated line to the change log at the bottom.

## What this machine makes

Evidence-led pieces for getdot.ai, in one of three formats, named in the piece's front matter as `format:` (research if absent):

- **Research:** our own run is the subject. One stage of the AI Data Analyst Playbook, actually run.
- **Teardown:** what other organisations published about how they did something, gathered into a census and the patterns it shows. No run of ours.
- **Guide:** steps a reader follows. Every step rests on a run of ours or on a cited publication (hard rule 4), or is labelled untested.

An essay format (one named idea, carried by argument) is not defined yet: our shape rules would fail Rick's essays, which run 440–560 words with no pocket guide, table or "Where Dot fits". Define it when one is written.

LinkedIn posts are cut from the pieces, never written separately.

## Hard rules

A piece that breaks any one of these does not ship.

1. **Questions come from sales calls first.** Search volume breaks ties; it never picks the topic.
2. **No finding is written before its evidence.** A research title comes after the run, from the Figures tab only. A teardown or guide title names what the reader gets; any number in it has a Figures row.
3. **Every number has a Figures row**: value, where it was computed, date. For a number from a cited publication (rule 4), where it was computed reads `published: <URL>, read <date>`.
4. **Nothing from the rehearsal (23–24 October), or from another account or dataset, appears in a piece unless it recurred in that piece's own run.** A piece's own run stays valid until its data, definitions or product version change; re-run then. This bars findings, not tools: prompts, scripts and rules may be ported.
   **One exception, cited publications.** A finding that another organisation published, or that Dot published in a post on getdot.ai, may appear as that publisher's finding, never as ours, only if all four hold: (a) the sentence names who published it; (b) it links the primary publication, opened and read for this piece, not a summary of it (Dot's own teardowns included); (c) every number in it is copied exactly and has a Figures row as rule 3 says; (d) it is not combined in arithmetic with, or offered as confirmation of, a figure from our own runs. The rehearsal, other accounts and unpublished runs stay barred: the exception covers what a reader can open and check, not what we ran and didn't publish. **Our own runs are a separate case:** a run of ours, on the same account and dataset, may be cited by a later piece; its run file is the evidence.
5. **Every product claim has evidence in the piece, a yes from Dot, or an "Assumption" label in the text.** Unlabelled and unconfirmed means cut.
6. **"We" means Dot.** The subject is a team rolling out an AI analyst; Dot is the instrument, not the defendant. Every limitation is paired with what the product does about it, or cut.
7. **No bracket citations.** Sources are links on the words that need them.
8. **Human-supplied claims go through the same fact-check as model output.**
9. **Record the dataset and its licence in Sources** before the first run. For the trial, Dot asked for any realistic dataset, since the point is the method. A piece with no run of its own records the licence of any run it cites.
10. **When a piece gives a cost per answer, it is published as a credits range, with dollars alongside, labelled as an assumption.** Research only; a teardown or guide that cites another organisation's cost uses rule 4. The conversion is facts/dot-facts.md A2 (1 credit ≈ $1), and the docs caveat that the same question can take different paths stays in.

### Evidence rules

11. **Never state a setting for every row after opening one.** Open them all, or write "the rows I opened".
12. **Classify a gap before counting it**: display rounding, or a real disagreement. Only the second is a finding.
13. **Every product quote names its question.** If the quote came from a chat, don't use it to describe an evaluation run, or say plainly which it came from.
14. **Screenshot the mode selector at the start of every batch**, and log the mode per batch. A written reminder wasn't enough; the check has to leave evidence.
15. **Read the credit balance before and after every batch.** One reading across mixed modes can't be split.
16. **Count from the source text, never by eye, and recount before a number is used a second time.**
17. **Every run carries its conditions**: the account, the environment, the mode, and which context notes were active.
18. **Judge recurrence item by item, not only in total.** Matching totals with changed items is a different finding, and usually a stronger one.
19. **No remedy the evidence didn't test.** Advice that says doing X fixes Y needs a run of ours, or a cited publication, that shows it. Otherwise cut it, or, in a guide, label the step untested. A limitation is still paired with what the product does (rule 6), from evidence.
20. **The question is answered completely in the first 100 words**, with no reference to anything above it. The promise of style rule 16 may sit beside the answer, not instead of it. Origin: about 44% of citations come from the first third of a page (roadmap update, 31 October 2026).
21. **Every H2 section reads standing alone**, with no pronoun or "this" pointing outside it. Engines retrieve passages, not pages.
22. **Every piece carries a reviewed-on date** (`reviewed_on:` in the front matter): the day a person last read it in full, set at Decision 3. No named author: who bylines a piece is Dot's decision, and check 19 forbids a byline nobody approved. (The roadmap's evidence that authored content is cited about 2.3x more than anonymous is a recommendation for Dot, recorded in HANDOVER.md.)
23. **Dot is described only in the exact words of `facts/dot-entity.md`**, never paraphrased. How this sits with rule 5: those words are Dot's own description of itself, quoted from its own pages, so a piece may use them as how Dot describes Dot without further evidence. Rule 5 still applies to any product claim a piece makes beyond that wording, or relies on as tested.

## Style rules

1. Research 900–1,300 words; teardown 1,000–1,600; guide 1,000–1,900. Cut a section, not sentences.
2. Bold lede with a number and a named thing.
3. Pocket guide after the lede: five to eight lines that are the whole piece.
4. H2s are claims. Never questions.
5. By format. Research: method in plain words, then one table, then one chart. Teardown: one census table with a row per publication (five or more), each linking its primary source; no chart required. Guide: one numbered list of five to nine steps, each starting with a verb; no table required. Any chart has alt text and a dated caption.
6. One "Things to keep in mind" box, two to four caveats, said once.
7. Named companies and quotes with links. Use the canon: the Playbook, the drift essay, the semantic-layer essays, DABstep.
8. "Where Dot fits" is the last H2, under 80 words, with a docs link.
9. End on an instruction, then: *If this excites you, we'd love to hear from you. Get in touch.*
10. Sentences average under 18 words. No paragraph over four sentences.
11. Read every paragraph aloud, once on a phone screen. After a later edit, re-read aloud the paragraphs that changed, not the whole piece.
12. **Quotable lines carry their own subject.** Models lift self-contained claims, not lines that lean on the sentence before.
13. SEO title contains the query. Meta under 155 characters. Slug four to six words.
14. Every image has alt text and a caption with the date; in research, the energy mode too. A teardown or guide has no batch of its own, and its caption doesn't explain the missing mode.
15. **Titles use the words buyers type and say what the reader gets.** Check the words against Search Console queries, Keywords Explorer and the pages that already rank. A clever title nobody searches for fails. A flat claim that states the finding counts as saying what the reader gets, provided the lede carries the promise (style rule 16) and the headline test passes on that title. **The title's shape depends on the format** (Dot's own blog, 31 October 2026): a research title names the finding or what the reader gets, from the Figures tab; a teardown title is 8–13 words, colons allowed, the subject plus a number plus the finding ("How 14 Companies Built AI Data Analysts", "Ramp Research: The Analyst Agent That Answered 1,800+ Questions in 6 Weeks"); a guide title names what the reader gets; an essay title, when the format is defined, is 4–9 words, no colon, a claim that corrects or warns the reader ("Your Data Model Is the Prompt").
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

1. **RESEARCH.** The gap chain: the buyer's question, what they find today, the gap type, what only Dot can show. Output: Sources rows, dated. The verdict is one of four: PIECE, PIECE IF, NOT A PIECE, or NOT A PIECE, BUT A SURFACE (the question is real, but its answer belongs on another surface: a third-party listicle, a review profile, a community thread or Dot's documentation, recorded in the bank's `surface` column).
2. **OUTLINE.** The Playbook template. Gate: no number that isn't already in Figures. A human approves before drafting. The outline carries a quotable line (one sentence under 25 words that stands alone and is checkable: it carries a number, or a claim that a cited figure in the piece supports directly, with that figure's ID given; built to be lifted word for word) and a freshness line (when the central number was measured, and when to re-measure it, or "not re-measurable, source closed"); `stage_gate.py` refuses an outline without them.
3. **DRAFT.** 900–1,300 words against the style rules.
4. **READER.** A Head of Data at a 300-person company, four minutes. Returns three places they'd stop reading, the one sentence they'd quote to their CFO, and the one claim they don't believe. Rewrites nothing. The writer then fixes all three stopping points.
5. **FACT-CHECK.** Two passes. First, a fresh chat with the draft only and no other context. Second, a different model. Each returns every number checked for internal consistency, every product claim marked VERIFIABLE or ASSERTED, every conclusion that outruns its evidence, and every quote checked for attribution. Then `verify_sources.py` on every URL.
6. **EDIT.** `check_piece.py` clean. A headline test: would a buyer know in three seconds what they get? Then the lift test: paste the piece into Perplexity and Claude, ask each for three bullets with one quotation each. Rewrite until the intended lines are lifted, or until the lifted lines are better than the intended ones.
7. **LINKEDIN.** Under 150 words. Three first lines tried; the most specific kept. A number within three lines. No hashtags, no emoji. Ends on an action. The link goes in the first comment with a UTM.

## The gate: 25 checks

A "no" on any line means the piece isn't done. Who checks each line is in brackets: script, model, or human.

**Headline and opening**
1. The title uses the words buyers type and says what the reader gets. A claim title may leave the buyers' words to the SEO title, which is what search shows. (human, against search data; check_piece.py marks a claim title PARTIAL until the headline test passes on it)
2. The first 60 words say what the reader will have by the end. (human)
3. The SEO title contains the query; meta under 155 characters; slug of four to six words. (check_piece.py)
4. A bold lede with a number and a named thing. (check_piece.py)
5. A pocket guide of five to eight lines. (check_piece.py)

**Structure and style**
6. The format's word range (style rule 1). (check_piece.py)
7. Sentences average under 18 words; none over 25. (check_piece.py)
8. No paragraph over four sentences. (check_piece.py)
9. Every H2 is a claim, not a question. (check_piece.py)
10. The format's body (style rule 5). (check_piece.py)
11. One "Things to keep in mind" box with two to four caveats. (check_piece.py)
12. "Where Dot fits" is last, under 80 words, with a docs link. (check_piece.py)
13. Ends on an instruction, then the italic CTA. (check_piece.py)
14. "We" means Dot. (human)

**Evidence**
15. Every number has a Figures row; a published number's source is linked in the piece; check_piece.py and verify_sources.py are clean. (scripts)
16. Every finding comes from this piece's run, a cited run of ours, or a cited publication meeting rule 4's four conditions; no untested remedy (rule 19). (human, against the Run Log and the sources)
17. Every product claim is evidenced, confirmed, or labelled "Assumption"; Dot is described only in the words of facts/dot-entity.md (hard rule 23). (check_piece.py flags unlabelled claims and paraphrased definitions of Dot; human confirms)
18. The dataset and its licence are recorded in Sources. (human)
19. No brackets, placeholders, or byline nobody approved; a reviewed-on date (hard rule 22) by Decision 3. (check_piece.py)

**Links**
20. Five or more internal links, including the Playbook stage, each opened to confirm it. (verify_sources.py)
21. Three reverse links listed, with anchor text. (human)

**Review**
22. READER pass done and its three stopping points fixed. (model, then human)
23. Lift test in Perplexity and Claude; the intended lines are the ones quoted. (model)
24. Read aloud once, on a phone, today; after a later edit, the changed paragraphs re-read aloud. (human)
25. The blind lift-tester's lifted lines reproduce the outline's quotable line in substance: its number, and most of its words. (check_piece.py, against reviews/<slug>/lift-tester.md)

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

**31 October 2026 — v1.6.7.** Style rule 11 and check 24 relaxed, on Saurabh's instruction: an edit after the phone read needs only the changed paragraphs re-read aloud, not the whole piece. The first read is still the whole piece. Origin: `ai-analyst-follow-up-questions` went through several fix rounds in one day, and each edit would otherwise have reset the whole read.

**31 October 2026 — v1.6.8.** Style rule 15 and check 1 allow a claim title. Origin: Saurabh read Dot's blog. Rick's titles are 4–9 words, flat claims, often "Your X", with no colons, no quoted jargon and no how-to promise. Check 1 demanded a promise word that no Rick title has. The search-word test stays a FAIL. A claim title is PARTIAL, and the headline test and the lede's promise (check 2) carry what the promise word did.

**31 October 2026 — v1.7.** Formats: research, teardown, guide. Origin: Saurabh chose A (research, done), B (teardown, "How N Companies Test Their AI Data Analyst", #35/#36) and F (guide, "How to Test an AI Analyst Before Rollout", #35) for three formats and three kinds of evidence. Rule 4 gains a narrow cited-publication exception; rules 2, 3, 9 and 10 and style rules 1 and 5 depend on the format; hard rule 19 writes down a practice applied all session. Our shape was built from the Playbook plus Cafe Bench. Length and table rules now follow each format; the pocket guide, the caveats box, "Where Dot fits" and the CTA stay. Rick's essays use none of these, so no essay format is defined until one is written.

**31 October 2026 — v1.8.** From the roadmap update ("the version to deliver"), as decided by Saurabh. Its rules 19–22 become 20–23, since 19 is taken.
- **/outline** carries a quotable line and a freshness line; the gate refuses an outline without them.
- **Hard rules 20–23:** answer in the first 100 words; standalone H2 sections; a reviewed-on date and no named author (Dot's decision; the 2.3x byline evidence goes to the handover as a recommendation); Dot described only in `facts/dot-entity.md`'s words, which rule 5 accepts as Dot's own self-description.
- **A fourth research verdict:** NOT A PIECE, BUT A SURFACE, with a `surface` column in the bank.
- **Check 25:** the blind lift-tester must reproduce the outline's quotable line in substance; a script compares the two, so the lift-tester stays blind.
- **Export no longer requires Webflow files.** `export_webflow.py` stays; the gate needs the .docx and the clean Markdown only. Dot's team publishes.
- **LinkedIn:** the roadmap's six structures are assigned across the cluster, not per piece (PLAN.md), because its post model assumes every piece is research.
- **Not adopted:** the roadmap's skill names (`/make-piece-*`, `/gate`) and the fact-checker's confirmed-claims list; reasons in HANDOVER.md.

**31 October 2026 — v1.8.1.** Style rule 14's mode requirement is research-only. Origin: piece B's outline proposed the caption "No Dot run, so no energy mode applies"; Saurabh cut it, because a caption explaining why a rule doesn't apply is a team note in public, which the readers caught in piece 1.

**31 October 2026 — v1.8.2.** A quotable or lift line must stand alone and be checkable: it carries a number, or a claim that a cited figure in the piece supports directly (its figures ID given). Was: it must carry a number. Origin: the rule rejected the most quotable sentence in piece B, "A test passed at launch says little about the same agent a month later." That sentence is checkable: it rests on Anthropic's published drift from about 95% to about 65% in a month (ANT-5, ANT-6), cited two paragraphs earlier. A number is the usual way to be checkable, not the only one. The change came from the line being better than the rule (Saurabh).

**31 October 2026 — v1.8.3.** Check 1: a claim title may leave the buyers' words to the SEO title. Origin: piece B's title "Their Accuracy Numbers Don't Compare. Your Questions Do." is the two-sentence turn Saurabh chose, and its SEO title "How 13 Companies Test Their AI Data Analyst" carries the search words. A title with neither the words nor an SEO title that has them still fails.

**31 October 2026 — v1.8.4.** Style rule 15: title shape depends on the format, and check 1 holds a teardown title to 8–13 words. Origin: piece B's titles were judged against the essay shape (4–9 words, no colon), which produced three failed headline tests' worth of argument. Dot's own teardown titles are longer, number-led and often use a colon; its essays are short claims. A rule that treats both the same keeps producing the argument (Saurabh). B's title is now "13 Companies Test Their AI Analyst. No Two Measure Accuracy the Same Way.", and its SEO title nearly repeats it, as Rick's 14-company post does.

**31 October 2026 — v1.8.5.** Check 1's v1.8.3 allowance (a claim title may leave the search words to the SEO title) no longer requires the title to lack a promise word. Origin: B's narrowed title "7 Companies Published Their AI Analysts' Accuracy. No Two Measured the Same Thing." contains "Measured", which the checker reads as a promise word, so the allowance didn't apply and the title failed although its SEO title carries the search words.

**31 October 2026 — v1.8.6.** Check 15: a published number's source is linked in the same sentence, or the same table row, as the number, not just somewhere in the piece. The pocket guide is exempt, since it restates numbers the body links; a value that also has a row from our own census or runs isn't held to a link. Origin: piece B's second fact-check found five company quotes linked elsewhere in the piece; the stricter check then found ten sentences more, and one number (Dot's census of 14) with no Figures row of its own, passing only because another row shared its value.

**31 October 2026 — v1.8.7.** Assumption A5's keywords in `facts/dot-facts.md` narrowed from "context agent" to the claim itself ("stores a definition once", "every chat answer uses it"). Origin: check 17 was flagging a phrase rather than the claim. Piece B quotes Dot's context agent page on a different matter (the merge check), and the writer got past the check by hyphenating the link text to "context-agent page". A check that a hyphen can dodge is checking the wrong thing. **The workaround was caught and reverted: gaming a check is a reportable event**, recorded here so the next person treats it that way, and the wording is back to "context agent page".

**31 October 2026 — v1.8.8.** Check 15 relaxed from v1.8.6, on Saurabh's instruction after the third phone read of piece B. A published number's source must be linked in the piece, not in the same sentence. Links go on each company's first substantive mention and on every company name in the table; none in the pocket guide, none inside a list of five or more names. Origin: the same-sentence rule linked the same company four or five times, and on a phone the piece read as a wall of blue. Every claim stays one tap from its source, through the first mention or the table row.


**1 November 2026 — v1.8.9.** A rule 14 waiver is a recorded state the gate reads, not a flag. Origin: piece A was exported, but `stage_gate.py` reported it stuck at its run, because the waiver Saurabh made on 31 October was honoured only when `--no-screenshots` was passed on that call. A decision a person made that the machine can't see is the class of problem the machine exists to prevent (Saurabh). Now a person states the waiver in the batch's conditions block (`**Rule 14 waived`, who and the cost) and runs `stage_gate.py waive <slug> --rule 14 --batch <n> --by "<name, date>"` once; it writes the waiver into `runs/<slug>-piece.json` and refuses if the run file doesn't state it. The gate reads both on every call; the flag is ignored. A's waiver migrated from its run file, line 7.

**1 November 2026 — v1.8.10.** `mark_run.py` no longer prints "N of M correct" alone. It prints how many were correct under the definition asked and how many only under another reading (the answer's stated definition, a rival reading, or a person's `--decide`), and says to quote both. Origin: F's research found that piece 2's "12 of 12 correct" included 3 correct only under the answer's own rival definition, and A's "8 of 8" included 3 correct only under the delivery-date reading. Both totals were true and both misled. It is the third time in this cluster that one number meant two things (B's two fives, B's two sevens), so it is recorded in HANDOVER.md as a pattern: our own scores need the item-by-item discipline rule 18 demands of Dot's answers. Checked: neither published piece uses the bare total; A's table gives each answer's reading. PLAN.md, A's run file and outline, and B's revisions now carry the split.

**1 November 2026 — v1.8.11.** Check 25 fixed twice, from F's first `/piece` run. (1) It paired quote marks with one regex over the whole lift-tester report, with the 15-character floor inside the regex; a short quote ("how to") threw the pairing out of step, and a verbatim lift of F's quotable line scored 18%. Quotes are now paired line by line, then filtered by length. The workflow's edit agent found it and stopped rather than change the piece to dodge it, as v1.8.7 asks. (2) With that fixed, check 25 passed on a lift of a sentence F's revision had removed ("both correct"). The lifted line must now still be in the piece; otherwise check 25 fails and asks for the lift-tester to be re-run. A and B unchanged (A: HUMAN, no quotable line; B: PASS).

**1 November 2026 — v1.8.12.** Hard rule 4: a run of ours, on the same account and dataset, may be cited by a later piece; its run file is the evidence (Saurabh). Origin: F's revise stage asked whether F may cite piece 2's archived run, since the exception's last sentence reads "unpublished runs stay barred". That clause was written for cited publications, where a reader has no other way to check, and should never have been read as covering our own runs. Our runs are more checkable than a published post, not less: the run file is in the repo, every answer is verbatim, and the figures are computed from raw data a reader can download. The rule was ambiguous because it conflated the two cases. The rehearsal and other accounts stay barred.

**1 November 2026 — v1.8.13.** Check 15 for posts: a published number's source is looked for in the piece the post links to, since a post carries no links of its own (its link is in the first comment). Origin: F's checklist post failed check 15 on Anthropic's ~90% and the Playbook's ~80%, both linked in F. B's posts were unaffected because their numbers have rows from our own census.

**1 November 2026 — v1.8.14.** The gate has a PIECE IF branch. Origin: the cold-start test found that a PIECE IF verdict passed research unchecked, its condition recorded only in the research file's prose. Now research waits until a person checks the condition and records it with `stage_gate.py clear <slug> --by --basis`. F's condition is recorded as Saurabh's (decision L4 and the browser re-read); A's was met before its run (the truth file computes late from the two date columns) and was recorded from the files, for Saurabh to confirm. `stage_gate.py --help` now prints the usage instead of treating `--help` as a slug. The handover's first test now follows the gate's order.
