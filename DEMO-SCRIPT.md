# Demo script: five minutes, the machine running

A screen recording of the repo in Claude Code and a terminal. Everything shown runs live; the only prepared thing is a broken copy of piece B, made on camera. Times are targets.

**Before recording:** open the repo in a terminal (Git Bash) and in Claude Code; `python -c "import pandas, docx; print('ok')"` prints ok; close any window showing an email address.

---

## 0:00–0:30 · What this is

**Show:** `README.md`, the top table of three pieces.

**Say:** "This repo turns a buyer's question into an evidence-led piece for Dot's blog. Three pieces went through it this week: a research piece from our own run in Dot, a census of 13 companies, and a guide that sits between them. I'll show where a piece stands, what happens when something is wrong, and where a person still decides."

## 0:30–1:15 · Where a piece stands, read from the files

**Run:**
```
python scripts/stage_gate.py test-ai-analyst-before-rollout
```

**Say:** "The gate reads only the files, so it gives the same answer in any session. Every stage is done: research, figures, outline, draft, three blind reviewers, revision, the human checks, export. It's waiting on one thing: a person reading the publish note. That note lists what the piece still assumes and the text to paste if Dot says no. Until someone signs it, the gate holds publishing."

**Show:** `reviews/how-companies-test-ai-data-analysts/publish-note.md`, scrolled to "What this piece assumes" and "Open with Dot".

## 1:15–2:45 · A check catches something (the part that matters)

**Run**, saying what each line does:
```
mkdir -p demo && cp pieces/how-companies-test-ai-data-analysts.md demo/broken-b.md
sed -i 's/underreported recall by 10-15%/underreported recall by 10-16%/' demo/broken-b.md
sed -i "s/ Assumption: the page describes how merging works today; we haven't tested it\.//" demo/broken-b.md
python scripts/check_piece.py demo/broken-b.md
```

**Say, while the two edits run:** "I'm making two mistakes a tired writer makes. One: I change LinkedIn's '10 to 15 percent' to '10 to 16'. Two: I delete the label on a claim about Dot's product that nobody has confirmed."

**Point at:** `15 FAIL … not in Figures: ['16']` and `17 FAIL … unlabelled: P-1 "merges at 95% or more"`.

**Say:** "Both caught. Every number in a piece needs a row in its figures file, with where it came from and the date; 16 has none. And the claim about Dot's context agent is on a list of things Dot hasn't confirmed, so it can't appear without its label. A prompt can ask a model to be careful. This refuses the piece until it is."

**Say, briefly:** "Building this demo, the first version of that range check missed the 16, because it only read the start of a range. That's fixed now and logged in the rulebook's change log. The checks have bugs too; the change log is where they get found and recorded."

**Run:** `rm -rf demo`

## 2:45–3:30 · A number, traced to its source

**Show:** `figures/ai-analyst-follow-up-questions-figures.csv`, the row `MR-Q2,2453`.

**Then show:** `runs/ai-analyst-follow-up-questions-run.md`, search `### Q2:`, the answer and its SQL.

**Say:** "Piece A says Dot counted 2,453 late orders. Here is the figures row, and here is Dot's answer, word for word, with the SQL it ran. The expected answer was computed from the raw data before the first question was asked. A second reading of the same phrase gave 1,762, and both were right. The SQL is the only place that says which date each one used."

## 3:30–4:15 · Blind reviewers, and what they changed

**Show:** `reviews/test-ai-analyst-before-rollout/lift-tester.md`, section 1, then `reviews/test-ai-analyst-before-rollout/revisions.md`, the line "Quotable line, third change".

**Say:** "Three reviewers read each draft with no rulebook and no context, started only through a script that strips everything else away. This one reads like an answer engine and says what it would quote. On the guide it picked a better line than the one we'd targeted, and we took it; in all three pieces, the real answer engines did the same. The fact-checker caught us claiming 'both correct' where one answer was only correct under its own definition."

## 4:15–5:00 · Where it stops

**Show:** `HANDOVER.md`, section 7, "Where the machine stops, and why".

**Say:** "It stops at seven points. Four are decisions that need judgement: which question to write, the outline, the title, publishing. One is the rival definitions a person reads before any run. Two are in Dot's own interface, because mode, credits and active notes can't be seen through the connector. What it can't do is decide what the finding is, or whether a title earns a click: every real improvement this week came from a person reading. What it does is check every number, source every claim and enforce every rule, so the four decisions that need judgement are the four you keep."
