# Verification of section 7: test-1 (practice)

Re-read 1 November 2026 by the cold-start test (practice), not a person's review. HANDOVER.md section 3 step 4 asks for each source to be opened **in a browser**; this was done instead with WebFetch, asking for the exact sentence holding each number, as `runs/how-companies-test-ai-data-analysts-verification.md` did. A person still owes the browser check.

Status: CONFIRMED (same value, unit and meaning on the page), NOT FOUND.

## Uber

URL: https://www.uber.com/blog/umetric/ (12 January 2021; Xiaodong Wang, Wenrui Meng, Will Yu)

| Item | Status | Exact text |
|---|---|---|
| 30+ teams, 10K+ metrics | CONFIRMED | "working with 30+ teams and 10K+ metrics" |
| 10X or 100X instances | CONFIRMED | "there can be 10X or 100X instances spinned off for a popular metric" |
| 18 months | CONFIRMED | "defines the “completed trips” metric as a Presto/Hive SQL in the last 18 months" |
| 6.53M | CONFIRMED | "Figure 3. iHub – Shopping Sessions: 6.53M" |
| 6.20M | CONFIRMED | "Figure 4 . Summary – Shopping Sessions: 6.20M" |
| Quote "Everyone can author a metric that is unambiguous and not duplicated with existing metrics." | CONFIRMED | exact |
| "Verification Committees" | CONFIRMED | "we formed Verification Committees at the organization level." |

## GitLab

URL: https://docs.gitlab.com/development/internal_analytics/metrics/metrics_dictionary (no date shown)

| Item | Status | Exact text |
|---|---|---|
| once an hour | CONFIRMED | "Currently, the metrics dictionary is built automatically once an hour." |
| within 1 hour | CONFIRMED | "When a change to a metric is made in a YAML file, you can see the change in the dictionary within 1 hour" (excerpt) |
| JSON Schema | CONFIRMED | "We are using JSON Schema to validate the metrics definition." |
| owner required | CONFIRMED | "Have an owner." under "All metrics must:" |
| 18 attributes, 12 required | CONFIRMED (WebFetch count) | required: key_path, description, product_group, product_categories, value_type, status, time_frame, data_source, data_category, tiers, milestone, introduced_by_url |
| 3 statuses | CONFIRMED | active, broken, removed |

## Not re-read

Langfuse, Collibra and Wikimedia carry no numbers used as figures; their quotes in section 7 were not re-read. Airbnb and Pinterest were not read at all (403).
