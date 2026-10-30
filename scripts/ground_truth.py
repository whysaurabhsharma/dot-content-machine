#!/usr/bin/env python3
"""ground_truth.py - recompute every expected answer in the evaluation from the raw data.

Usage:
    python scripts/ground_truth.py data/olist_orders_dataset.csv data/olist_order_items_dataset.csv
    python scripts/ground_truth.py <orders.csv> <items.csv> --write figures/ground-truth.csv

Prints each of the 20 evaluation questions with the answer computed from the CSVs,
the expected answer stored in the evaluation, and the gap. Re-running this on the
day of a piece makes every expected answer a result from that day, not one carried
over (CLAUDE.md rule 4). Also computes average order value under the context note's
definition (delivered orders only), which is piece 1's central comparison.
"""
import csv
import sys

import pandas as pd

# Expected answers as stored in Dot's evaluation "Olist Orders and Items Accuracy", read 27 October 2026.
EXPECTED = {
    1: 99441, 2: 96478, 3: 8, 4: 112650, 5: 98666, 6: 6735, 7: 3095, 8: 625, 9: 120.65, 10: 140.64,
    11: 13591643.7, 12: 13221498.11, 13: 137.75, 14: 9803, 15: 1.14, 16: 97.02, 17: 2198275.64,
    18: 96478, 19: 6155806.98, 20: 2970,
}
QUESTIONS = {
    1: "Rows in olist_orders_dataset",
    2: "Orders with order_status = delivered",
    3: "Distinct values of order_status",
    4: "Rows in olist_order_items_dataset",
    5: "Distinct order_id values in the items table",
    6: "Highest single item price",
    7: "Distinct seller_id values in the items table",
    8: "Orders with order_status = canceled",
    9: "Average item price, excluding freight",
    10: "Average of price plus freight_value per item",
    11: "Sum of price across all item rows",
    12: "Sum of price on items of delivered orders",
    13: "Average order value: per-order sum of item prices, all orders with items",
    14: "Orders with more than one item row",
    15: "Average item rows per order_id",
    16: "Delivered orders as a percentage of all orders",
    17: "Total freight_value on items of delivered orders",
    18: "Distinct delivered orders that appear in the items table",
    19: "Sum of price on items of orders purchased in calendar 2017",
    20: "Distinct sellers with at least one item on a delivered order",
}


def compute(orders, items):
    delivered_ids = set(orders.loc[orders.order_status == "delivered", "order_id"])
    items_delivered = items[items.order_id.isin(delivered_ids)]
    per_order = items.groupby("order_id")["price"].sum()
    purchased_2017 = set(orders.loc[pd.to_datetime(orders.order_purchase_timestamp).dt.year == 2017, "order_id"])
    r = {
        1: len(orders),
        2: int((orders.order_status == "delivered").sum()),
        3: orders.order_status.nunique(),
        4: len(items),
        5: items.order_id.nunique(),
        6: float(items.price.max()),
        7: items.seller_id.nunique(),
        8: int((orders.order_status == "canceled").sum()),
        9: float(items.price.mean()),
        10: float((items.price + items.freight_value).mean()),
        11: float(items.price.sum()),
        12: float(items_delivered.price.sum()),
        13: float(per_order.mean()),
        14: int((items.groupby("order_id").size() > 1).sum()),
        15: float(items.groupby("order_id").size().mean()),
        16: 100 * (orders.order_status == "delivered").sum() / len(orders),
        17: float(items_delivered.freight_value.sum()),
        18: items_delivered.order_id.nunique(),
        19: float(items[items.order_id.isin(purchased_2017)].price.sum()),
        20: items_delivered.seller_id.nunique(),
    }
    # The context note's definition: delivered orders only.
    r["13b"] = float(items_delivered.groupby("order_id")["price"].sum().mean())
    return r


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    orders = pd.read_csv(argv[1])
    items = pd.read_csv(argv[2])
    r = compute(orders, items)
    rows, worst = [], 0.0
    print(f"\nground_truth.py  {argv[1]}  {argv[2]}\n")
    print(f"{'#':>3}  {'computed':>16}  {'expected':>16}  {'gap':>8}  question")
    for q in range(1, 21):
        c, e = r[q], EXPECTED[q]
        gap = abs(c - e) / abs(e) * 100 if e else 0.0
        worst = max(worst, gap)
        print(f"{q:>3}  {c:>16,.4f}  {e:>16,}  {gap:>7.3f}%  {QUESTIONS[q]}")
        rows.append({"id": f"GT{q:02d}", "value": round(c, 4), "description": QUESTIONS[q],
                     "where_computed": "ground_truth.py on the Olist CSVs", "date": pd.Timestamp.today().date().isoformat()})
    print(f"\n13b  {r['13b']:>16,.4f}  average order value under the context note's definition (delivered only)")
    rows.append({"id": "GT13b", "value": round(r["13b"], 4),
                 "description": "Average order value, delivered orders only (the context note's definition)",
                 "where_computed": "ground_truth.py on the Olist CSVs", "date": pd.Timestamp.today().date().isoformat()})
    print(f"\nLargest gap between computed and expected: {worst:.3f}%")
    if "--write" in argv:
        out = argv[argv.index("--write") + 1]
        with open(out, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
        print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
