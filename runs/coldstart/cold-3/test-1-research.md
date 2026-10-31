# Research: "How do I write down our metric definitions so everyone, including an AI, uses the same ones?"

Piece slug: `test-1` · Bank #30 ("metric definitions document template") · Format: teardown · Date: 1 November 2026
Census bar (from the caller): the organisation's own publication describes how it writes down or governs its metric definitions.

## 1. The gap chain

- **What the buyer asks:** "How do I write down our metric definitions so everyone, including an AI, uses the same ones?" (bank #30, persona Analytics Engineer; typed form "metric definitions document template").
- **What they find today (advice, not evidence):** the top three pages for the query are an Atlan template page (vendor-owned, advice, no result shown), an InnerSource Commons template page (documentation, bare template) and a ServiceNow product-docs page (documentation, about its own product's metric types). None shows anyone who ran or used a definitions document and reports what happened. Dot's own pages, per the bank row: docs train-dot/maintaining-dot has note-writing rules and the data-culture playbook has a two-page KPI glossary; "No template" (bank gap_basis).
- **Who gets cited in AI answers:** not measured. `measure/citations.md` tracks three other buyer questions (evaluating accuracy, what changes, cost and fit); this question is not among them. No counts are borrowed.
- **The gap:** advice only. Templates exist; accounts of how an organisation actually writes down and governs its definitions, from the organisation itself, are scattered and not gathered anywhere I found.
- **What only Dot can show:** nothing from a run (a teardown has no run of ours). What Dot adds is the gathering: a census of organisations that published their own practice, and the patterns across them. Bank evidence_basis for #30 says "a template anyone can write; batch 2 showed the note changed no figure" (score 1), which argues against a research piece and for a teardown.

## 2. The words buyers type

All values: Ahrefs, 27-28 October 2026 (frozen snapshot). Search Console had no row related to this question (the file's twelve rows are about Power BI, conversational analytics and similar).

| Phrase | volume_us | volume_global | difficulty |
|---|---|---|---|
| metric definitions | 20 | not measured | 13 |
| single source of truth metrics | not indexed | not indexed | not measured |
| metric definitions document template | not measured | not measured | not measured |
| semantic layer (flagged `is_buyer_query: no` in the file) | 2.4K | not measured | 24 |

"metric definitions" is the only phrase with volume. "metric definitions document template" is the bank's name for the topic but is not in `keywords.csv`: written "not measured", never estimated.

## 3. The run

None. A teardown has no run of ours and no Dot workspace check (skipped as instructed; no `get_catalog` call made, as the caller said). Playbook stage the topic belongs to: **Stage 2, "Ground"** (owner: the domain analyst), read at https://www.getdot.ai/blog/ai-data-analyst-playbook on 1 November 2026. It says: "Write atomic notes with owners. Add out-of-scope redirects" and "Rename what is unclear. Deactivate dead fields. Describe what remains"; the Aim section says "If nobody has agreed how a metric is calculated, no agent can be right about it." `facts/house-structure-and-links.md`, "Suggested links per piece", has rows only for pieces 1-3 (Stage 3, 5, 5); none names Ground, so link the Playbook and /context-agent and docs.getdot.ai, and verify each with `verify_sources.py`. Dataset and licence: none, since there is no run; the piece cites no Olist-derived figure.

## 4. Sources rows

See the CSV in section 8. Order of the ranking pages is WebSearch's, not Google's, on 1 November 2026.

## 5. Stop conditions

- Evidence already exists? Not found: no page among the top three shows anyone using a definitions document and reporting a result. Several organisations describe their practice (section 7), but no one has gathered them against this question.
- Only Dot's data could show it? No, the census is public.
- Neither stop condition applies. Two risks: the census count rests on thin margins (below), and the bank row scored evidence 1.

## 6. Verdict

**PIECE IF** the human accepts a census of 5 organisations as enough, two of them borderline (Wikimedia, Collibra: see section 7), or first adds one or more from Airbnb and Pinterest after a person opens their Medium posts in a browser (both returned HTTP 403 to WebFetch, so they are left out). If the bar is "five or more, no borderline", this is currently 3 clear plus 2 borderline.

## 7. Sources

Census of organisations whose own publication describes how it writes down or governs its metric definitions. Each opened with WebFetch on 1 November 2026. Quotes are from the WebFetch reading of the page, not from a browser; re-read in a browser before publishing.

### Meets the bar (5)

**1. Uber.** "The Journey Towards Metric Standardization", Uber Blog (Uber Engineering), 12 January 2021. Authors: Xiaodong Wang, Wenrui Meng, Will Yu. URL: https://www.uber.com/blog/umetric/. Clear.
- What it says: uMetric splits each metric into a *view definition*, a *metric definition* (SQL business logic plus author and use-case information) and *dimensions and filters* supplied by consumers at runtime. Goal: "Everyone can author a metric that is unambiguous and not duplicated with existing metrics." Uber formed Verification Committees at the organization level, staffed with domain experts, to resolve which definition and data source to use; it calls this "a time consuming process" and added tiering. Upstream source owners own quality alerts: "the hard work to uphold the quality falls on the source owner."
- Numbers: 30+ teams (teams Uber worked with to find duplicate or ambiguous metrics); 10K+ metrics (observed in that work); 10X or 100X (metric instances spun off for a popular metric); 18 months (lookback of an Operations team's daily "completed trips" metric); 6.53M and 6.20M ("Shopping Sessions" in two tools; the article states no city or period).

**2. GitLab.** "Metrics Dictionary Guide", GitLab Docs (GitLab). No date shown. URL: https://docs.gitlab.com/development/internal_analytics/metrics/metrics_dictionary. Clear, with a scope caveat: the metrics are product-usage (Service Ping) metrics, not finance or sales KPIs.
- What it says: metrics are defined in individual YAML files; the Metrics Dictionary is built from them; "Currently, the metrics dictionary is built automatically once an hour." Definitions are validated against a JSON Schema; every metric must have a unique `key_path` and an owner (`product_group`). "Do not add new schema exceptions."
- Numbers: once an hour (dictionary build); 1 hour (a metric change appears within 1 hour of deployment to production; an event change within 1 hour of merge to master); 18 fields in the definition table, 12 marked required; 3 statuses (`active`, `broken`, `removed`); 4 value types; 4 data categories; 3 tiers; 7d and 28d time frames; 8 performance-indicator types (WebFetch's counts of the page's lists; recount from the page before use, rule 16).
- Not used: GitLab's KPI handbook page (https://handbook.gitlab.com/handbook/company/kpis/) returned only navigation to WebFetch across 230,566 characters; its body was not read, so nothing is drawn from it.

**3. Langfuse.** "Analytics", Langfuse handbook (Langfuse). No date shown. URL: https://langfuse.com/handbook/product-engineering/analytics. Clear.
- What it says: goal is "If we discuss a metric, it is clearly understood and documented what it means and how it is calculated." Business logic lives in dbt, not in Metabase; documentation sits in the mart's YAML; each change adds schema tests (`unique`, `not_null`, `accepted_values`); changes go through a feature branch and PR ("never push to main"); dbt Cloud builds and tests only the PR's diff in a temporary BigQuery dataset.
- Numbers: none. The page names no owner per metric and no review cadence.

**4. Collibra (borderline).** "Customer zero: How Collibra built an org-wide AI analyst on its own governed context", Collibra blog, 30 July 2026; by Meredith Bailey, interviewing Dmytro Protsyk, Sr. Director of Strategy Operations. URL: https://www.collibra.com/blog/customer-zero-how-collibra-built-an-org-wide-ai-analyst-on-its-own-governed-context. Vendor marketing; its own AI analyst, Dwight.
- What it says: no separate definition-writing process. A "governed context compiler" pulls semantic models, governed measures, approved synonyms and ownership from Collibra's Knowledge Graph. "Every time we change what's in Dwight's brain, we run evals." "Nothing goes in just because it happens to exist." "whoever owns a piece of context should be the one to approve a change to it"; a human gives final approval.
- Numbers: no measured results. Round figures are illustrative (ten thousand files, a dozen locations for "Customer", two weeks, two months).
- Why borderline: it describes governing context for an AI analyst (owners approve, evals gate) more than how definitions are written down.

**5. Wikimedia Foundation (borderline).** "Research and Decision Science/Data glossary/Essential metrics", Meta-Wiki. Last edited 4 August 2024, 06:40; no named author. URL: https://meta.wikimedia.org/wiki/Research_and_Decision_Science/Data_glossary/Essential_metrics.
- What it says: essential metrics are judged on accessibility, relevance and trustability; a production metric must have "Defined business owners or data stewards who can make decision and answer questions about the metric"; essential metrics need "planned engineering resourced dedicated to enable standardized data pipelines, data quality checks, monitoring and alerts"; the Foundation "envisions" Metrics Cards, inspired by Machine Learning Model Cards.
- Numbers: none that are findings; "hundreds of metrics" defined by different Foundation teams and "a few" needed for core decisions (both approximate); fiscal years 2022-2023 and 2023-2024; working group met July and December 2023.
- Why borderline: partly a criteria and proposal document ("envisions"), not a description of a finished practice.

### Fell short of the bar (2 read, 2 not readable)

- **Photoroom** (https://www.photoroom.com/inside-photoroom/why-ai-for-bi-fails, 3 July 2026, Juliette Duizabo, Head of Data): says semantic discipline has three parts (Design, Protection, Validation) but "does not explain how metric definitions are written or enforced"; it defers that to a later article ("write definitions as code"), which I could not find or open. Numbers (20+ interpretations of "revenue last month"; 3 components) are claims, not results.
- **dbt Labs** (https://docs.getdbt.com/best-practices/how-we-build-our-metrics/semantic-layer-1-intro, last updated 11 March 2026): a best-practices guide for users; the body never says dbt Labs follows it internally, and it says nothing on ownership or review.
- **Airbnb (Minerva)** and **Pinterest ("Trusting Metrics at Pinterest")**: Medium posts, HTTP 403 to WebFetch. Not read, so left out. A web.archive.org copy was blocked by the permission system and was not worked around.
- Searches for Spotify, Netflix, LinkedIn, Lyft, Etsy, Shopify, Mozilla, Zalando, Monzo and Wise returned no own-publication posts on this topic. That is a search limit, not a finding that none exist.

**Count meeting the bar: 5 (3 clear, 2 borderline).**

Hard rule 4: every finding above is the publisher's, to be named as theirs, linked, copied exactly, with a Figures row (`published: <URL>, read 1 November 2026`), and never combined with figures from our runs.

## 8. Sources as CSV

```csv
source,url_or_tool,what_it_showed,date
bank row #30,bank/questions.csv,question "metric definitions document template"; Dot's pages: docs train-dot/maintaining-dot note-writing rules and data-culture playbook two-page KPI glossary; no template (gap_basis); evidence_score 1,read 1 November 2026
Search Console rows,data/ahrefs/search-console-queries.csv,12 rows; none related to metric definitions,read 1 November 2026
Keywords Explorer: metric definitions,data/ahrefs/keywords.csv,volume_us 20; volume_global not measured; difficulty 13,Ahrefs 28 October 2026
Keywords Explorer: single source of truth metrics,data/ahrefs/keywords.csv,volume_us not indexed; volume_global not indexed; difficulty not measured,Ahrefs 28 October 2026
Keywords Explorer: metric definitions document template,data/ahrefs/keywords.csv,not in file: not measured,Ahrefs 27-28 October 2026
Keywords Explorer: semantic layer,data/ahrefs/keywords.csv,volume_us 2.4K; volume_global not measured; difficulty 24; is_buyer_query no,Ahrefs 28 October 2026
AI answers,measure/citations.md,question not tracked: not measured (file holds marker counts only for three other questions),read 1 November 2026
Ranking page 1 (WebSearch order; vendor-owned template; advice),https://atlan.com/resources/readme-template-metric/,"Atlan 'Readme Template: Metrics'; opens 'Metrics often become confusing or inconsistent when not properly explained'; no date, no author; template fields only; no result shown",1 November 2026
Ranking page 2 (documentation; advice),https://innersourcecommons.gitbook.io/managing-innersource-projects/measuring/index/use_gqm/index-2/gqm_metric_template,InnerSource Commons 'GQM Metric Template'; fill-in sections (name; synopsis; unit; interpretation; measuring); no date; no result,1 November 2026
Ranking page 3 (documentation; neither evidence nor advice),https://www.servicenow.com/docs/r/washingtondc/environmental-social-governance/types-of-metric-definitions.html,ServiceNow 'Types of metric definitions' product docs; updated 10 September 2026; three types (automated; manual; calculated) of its own GRC product,1 November 2026
Playbook,https://www.getdot.ai/blog/ai-data-analyst-playbook,Five stages Aim Ground Prove Launch Run; metric definitions sit in Stage 2 Ground,1 November 2026
PLAN.md,PLAN.md,read; sections name pieces A B F only; neither slug test-1 nor bank #30 appears; no run needs bind this piece,1 November 2026
House links,facts/house-structure-and-links.md,suggested links table has rows for pieces 1-3 only (Stages 3 and 5),1 November 2026
Census: Uber,https://www.uber.com/blog/umetric/,Verification Committees; metric definition model; 30+ teams; 10K+ metrics; 12 January 2021,1 November 2026
Census: GitLab,https://docs.gitlab.com/development/internal_analytics/metrics/metrics_dictionary,YAML definitions; schema validation; owner required; dictionary built once an hour; no date shown,1 November 2026
Census: GitLab KPI handbook (not used),https://handbook.gitlab.com/handbook/company/kpis/,body not readable through WebFetch (navigation only),1 November 2026
Census: Langfuse,https://langfuse.com/handbook/product-engineering/analytics,definitions in dbt YAML; PR review; schema tests; no date; no numbers,1 November 2026
Census: Collibra (borderline),https://www.collibra.com/blog/customer-zero-how-collibra-built-an-org-wide-ai-analyst-on-its-own-governed-context,owners approve context changes; evals on every change; 30 July 2026,1 November 2026
Census: Wikimedia Foundation (borderline),https://meta.wikimedia.org/wiki/Research_and_Decision_Science/Data_glossary/Essential_metrics,criteria; data stewards required; Metrics Cards envisioned; last edited 4 August 2024,1 November 2026
Fell short: Photoroom,https://www.photoroom.com/inside-photoroom/why-ai-for-bi-fails,defers definition-writing to a later article; 3 July 2026,1 November 2026
Fell short: dbt Labs,https://docs.getdbt.com/best-practices/how-we-build-our-metrics/semantic-layer-1-intro,user best-practices guide; not own practice; updated 11 March 2026,1 November 2026
Not read: Airbnb Minerva,https://medium.com/airbnb-engineering/how-airbnb-achieved-metric-consistency-at-scale-f23cc53dea70,HTTP 403,1 November 2026
Not read: Pinterest,https://medium.com/pinterest-engineering/trusting-metrics-at-pinterest-ed76307e10a0,HTTP 403,1 November 2026
```
