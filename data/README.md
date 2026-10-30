# Data

Put the two Olist CSVs in `data/olist/`. That folder is in `.gitignore`, so the CSVs are never committed:

- `olist_orders_dataset.csv`
- `olist_order_items_dataset.csv`

`specs/piece-1-truth.json` reads them from those paths, run from the repo root.

Source: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce. Licence: CC BY-NC-SA 4.0, recorded in the Sources tab. Rick confirmed that any realistic dataset is fine for the trial; the licence matters again before anything is published commercially.
