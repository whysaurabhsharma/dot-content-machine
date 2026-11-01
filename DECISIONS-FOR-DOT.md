# Decisions for Dot

1 November 2026. Eight questions for Rick. **Dot has answered none of them.** On 1 November Saurabh decided 4, 6 and 7 himself, and wrote the notes on 3 and 8; all five were first recorded here as Dot's answers, and corrected the same day (CLAUDE.md v1.8.28). The pieces are finished, not approved, and none is published: `stage_gate.py` refuses Decision 4 while the byline, the licence or (for B) partner naming waits on Dot's sign-off. Each says what it releases. Write the answer on the line; the evidence behind each is in `HANDOVER.md` section 8.

## Blocks piece B

**1. The context agent quote.** B's "Where Dot fits" quotes Dot's context agent page: "Merging re-checks accuracy first: Dot answers its 25 questions again and merges at 95% or more." We didn't test it, and the piece says so ("We haven't tested that gate here."). The line sits in the page's top panel, which looks like an illustration; the page doesn't say what happens below 95%. In B's census of 13 companies, none gates each change on a re-test, so this is the strongest product line in the cluster. **Yes:** B publishes as written. **No, or "illustration only":** we cut the quote, and "Where Dot fits" falls back to the evaluation (expected answer, unit, tolerance). **Releases:** B.

Answer: ____________________

**2. The DABstep figures.** B concedes: "Dot publishes an accuracy figure too: 90% on a 30-task slice of Adyen's public DABstep benchmark. That figure doesn't compare with the others here either." Dot's home page, read in a browser on 1 November, also shows 96% on the 72 easy tasks and 89% on the 378 hard ones (450 in all), beside Google's "~52% weighted overall" and a human 62% on easy tasks only. No Dot post we read documents a run on all 450. **Supporting evidence, 1 November 2026 baseline:** for the buyer query "ai data analyst accuracy", Perplexity's answer drew on count.co, which cites DABstep at 14.55% on its hardest tasks. Dot's own post reports 90% on a 30-task slice. Two DABstep numbers, measured on different task sets, reached the same buyer in one answer, and Dot itself wasn't cited (`measure/baseline-2026-11-01.md`, query 3). The comparison B says can't be made is already being made for buyers. **Is there one, and is it published?** **Yes, published:** B cites it instead of the 30-task slice. **Yes, unpublished:** B keeps the slice; Dot may want to publish the run. **No:** B stands; separately, the home page sets different task sets side by side, which is the comparison B says can't be made (labelling each figure's task set would fix that). **Releases:** B.

Answer: ____________________

## Blocks pieces B and F

**3. Dot's evaluation, as observed on 27 October.** B and F say each test question in Dot's evaluation "carries an expected answer, a unit and a tolerance in percent" (fact O1). That was seen on a trial account on 27 October. **Is it still how evaluation works?** **Yes:** both publish as written. **Changed:** we update the sentence. **Releases:** B and F ("Where Dot fits").

Answer: **Not answered by Dot.** First recorded as Rick's "yes, still current" on 1 November 2026; nobody at Dot had said so (corrected the same day). P-2 is pending again, and the label "observed on 27 October 2026 and not re-checked since" is restored in B and F.

## Blocks all three pieces, if the answer is no

**4. The Olist licence.** All three pieces cite figures computed from the Olist public dataset, labelled CC BY-NC-SA 4.0 on Kaggle; the label was never verified at source. Saurabh recorded decisions to proceed (L1, L2, L4); they are decisions, not resolutions, and the question is Dot's. **Can Dot publish figures from a non-commercial dataset on its blog?** **Yes:** nothing changes. **No:** the runs need repeating on data Dot may publish (the questions and scripts carry over). **Releases:** A, B and F.

Answer: **Decided by Saurabh, 1 November 2026: proceed. Dot sign-off pending.** First recorded as Rick and Théo's answer; corrected the same day. L1, L2 and L4 remain Saurabh's decisions.

## Strengthens a piece; blocks nothing

**5. A pass bar in Dot's evaluation.** F's step 7 says to decide the bar before testing (Anthropic started at about 90%; Dot's Playbook suggests about 80%). Nobody has seen a pass bar in Dot's evaluation, so F says only that steps 2 and 6 "live in one place". **Does the evaluation let a team set one?** **Yes:** F adds step 7 to that sentence. **No:** F stands.

Answer: ____________________

**6. A byline.** The pieces carry a reviewed-on date and no author (hard rule 22), because who bylines a piece is Dot's call. The roadmap cites evidence that a named author is cited about 2.3x more often. **Name an author?** **Yes:** add the field to each piece. **No:** nothing changes.

Answer: **Decided by Saurabh, 1 November 2026: byline Saurabh Sharma. Dot sign-off pending.** First recorded as Rick's answer; corrected the same day. Each piece's `author_approved_by` reads "Decided by Saurabh, 2026-11-01; Dot sign-off pending".

**7. Naming partners' gaps in public.** B's census table and its second LinkedIn post say what each company's published testing method leaves out, by name: Snowflake, GitHub, Salesforce, Vercel and Prosus among them. Snowflake is a Dot integration partner. Every statement is about what the company's own post says, linked and read in a browser, not about how it tests. **Is Dot comfortable naming partners this way?** **Yes:** nothing changes. **No:** post 2 drops the names (the table stays, since the piece's method is the census), or Snowflake's row is reworded with Snowflake's sign-off. **Releases:** B's post 2; B itself only if the answer is no for the table too.

Answer: **Decided by Saurabh, 1 November 2026: yes, since Dot already publishes comparison pages at getdot.ai/compare. Dot sign-off pending.** First recorded as Rick and Théo's answer; corrected the same day. B and post B3 wait on Dot's sign-off.

**8. Assumptions A1–A8.** None is used in the three pieces as they stand. Each needs a yes, no or change before a future piece relies on it; the list, with what each would allow, is in `HANDOVER.md` section 8 and `facts/dot-facts.md`.

Answer: **Not answered by Dot.** The note "add assumption there" was Saurabh's, first recorded as Dot's; corrected the same day. None of A1–A8 is in the pieces; unresolved.
