# reader · test-ai-analyst-before-rollout

Started with: Read reviews/test-ai-analyst-before-rollout/draft.md and give your report.

I read only `C:\Users\LENOVO\OneDrive\Documents\1Sauarbh\1Dot\dot-content-machine\dot-content-machine\reviews\test-ai-analyst-before-rollout\draft.md`.

**1. Three places I'd stop reading**

- **Line 33 onward ("A one-answer test marks right answers wrong..."): two separate "late orders in 2017" examples.** The opening example is 2,878 vs 2,453, a gap of 425 caused by timestamp vs. day. This section's example is a gap of 691 caused by purchase date vs. delivery date. Both are late orders in 2017 on the same dataset, so as a stranger I can't tell whether this is one finding or two. By the second I've lost track of which gap is which, and it feels like the numbers are being reused to look like more evidence.
- **Step 6 (line 29): the judge paragraph.** It goes Hex's 2.04% vs 2.03%, then a 35% figure, then LinkedIn's "within 1 point" (1 point on what scale?), then a hedge, then "Dot's census lists how all 13 companies score." That last clause doesn't tell me the result. I came for advice on whether an LLM judge is safe to use and got a pointer to another page.
- **Lines 43 to 49 ("A test passed at launch needs a bar...").** This repeats steps 7 and 8 almost word for word: the same Anthropic ~95% to ~65% quote, the same "5 of 13", the same "initially used ~90%", and the same "untested" disclaimer. This is where I'd skim to the end. The Dot section that follows ("We haven't tested it against the steps above", "Assumption: it always re-scores") then reads as internal notes, not a reason to look at the product.

Smaller snag: step 4 says "For two of the other three, a person read the date from the SQL." What happened with the third?

**2. The one sentence I'd quote to my CFO**

"We watched our offline accuracy drift from ~95% at launch to ~65% over a month before we treated this as an engineering problem." (Anthropic, quoted in step 8)

It's short, from a credible source, and makes the case for budget to re-test.

**3. The one claim I don't believe**

"Both numbers were right." The draft says two identically worded questions got 2,878 and 2,453, and calls both correct. Each may match the raw data under its own definition. But from where I sit, a tool that picks a different definition of "late" each time I ask the same question is giving inconsistent answers. The draft presents that as a problem with the test, when to a buyer it looks like a problem with the product. I'd trust the piece more if it said this outright.

**4. After the first 60 words, do I know what I'll have by the end?**

Yes. I'll have an eight-step checklist for testing an AI analyst before rollout: real questions, every acceptable answer written down first, each question asked twice in fresh chats, and the SQL read behind every answer. The title and the lede's last sentence both say so. That last sentence ("each resting on a run of ours or a published method") is about the article itself, though, and costs words in the most valuable spot.
