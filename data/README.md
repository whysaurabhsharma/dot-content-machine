# Data

Put the two Olist CSVs in `data/olist/`. That folder is in `.gitignore`, so the CSVs are never committed:

- `olist_orders_dataset.csv`
- `olist_order_items_dataset.csv`

`specs/ai-analyst-follow-up-questions-truth.json` reads them from those paths, run from the repo root.

Source: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce. Licence: CC BY-NC-SA 4.0, recorded in the Sources tab. Rick confirmed that any realistic dataset is fine for the trial, and on 1 November 2026 Dot (Rick and Théo) confirmed it may publish figures from this dataset (CLAUDE.md v1.8.17). A different dataset needs its own licence check before anything is published.
