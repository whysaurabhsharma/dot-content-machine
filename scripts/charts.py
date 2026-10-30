#!/usr/bin/env python3
"""charts.py - one chart per piece, in house colours, with alt text and caption.

Usage:
    python scripts/charts.py charts/piece-1-band.json

The spec is JSON with "type" ("band" or "ranking"), "out", "title", "alt",
"caption", and the data. Writes the PNG and a .txt beside it holding the alt
text and caption to paste into the piece. Grey for context, one blue accent for
what the title is about.
"""
import json
import sys
import textwrap
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches
from matplotlib import font_manager as fm

INK, SOFT, GREY, ACCENT, BAND = "#1F1F1F", "#6B6B6B", "#C9C9C3", "#2F6FD6", "#E6E6E2"
for f in ("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
          "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"):
    if Path(f).exists():
        fm.fontManager.addfont(f)
        plt.rcParams["font.family"] = "Liberation Sans"


def style(ax):
    for s in ("left", "right", "top"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color("#BBBBBB")
    ax.tick_params(axis="x", colors=SOFT, labelsize=8.5)


def band(spec, ax):
    e, tol = spec["expected"], spec["tolerance_pct"] / 100
    lo, hi = round(e * (1 - tol), 2), round(e * (1 + tol), 2)
    ax.axvspan(lo, hi, ymin=0.08, ymax=0.92, color=BAND, zorder=0)
    ax.axvline(e, ymin=0.08, ymax=0.92, color=INK, lw=1.4)
    ax.text(e + 0.08, 0.86, f"{spec.get('expected_label', 'Expected')} {e:g}", fontsize=9.5, va="center", color=INK)
    spec.setdefault("subtitle", f"Shaded: the {spec['tolerance_pct']:g}% tolerance band, {lo:.2f} to {hi:.2f}")
    ys = [0.62 - i * 0.32 for i in range(len(spec["points"]))]
    for p, y in zip(spec["points"], ys):
        ax.plot(p["value"], y, "o", ms=8, color=ACCENT, zorder=3)
        ax.text(p["value"] - 0.25, y, f"{p['label']}: {p['value']:g}", fontsize=9.5, va="center", ha="right", color=INK)
    pad = (hi - lo) * 0.3
    ax.set_xlim(lo - 2 * pad, hi + pad)
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    ax.set_xlabel(spec.get("x_label", ""), color=SOFT, fontsize=8.5)


def ranking(spec, ax):
    rows = spec["rows"] if spec.get("keep_order") else sorted(spec["rows"], key=lambda r: -r["value"])
    for i, r in enumerate(rows):
        y = len(rows) - 1 - i
        ax.barh(y, r["value"], color=ACCENT if r.get("accent") else GREY, height=0.7,
                hatch="///" if r.get("hatch") else None, edgecolor="white" if r.get("hatch") else None)
        ax.text(r["value"] * 1.01, y, r.get("value_label", f"{r['value']:g}"), va="center", fontsize=8.5, color=INK)
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([r["label"] for r in reversed(rows)], fontsize=8.5)
    ax.tick_params(axis="y", length=0)
    ax.set_xticks([])


def stacked(spec, ax):
    cats, segs = spec["categories"], spec["segments"]
    colors = [GREY, ACCENT, "#9DBCEB", "#1F1F1F"]
    for i, cat in enumerate(cats):
        y, left = len(cats) - 1 - i, 0
        for j, seg in enumerate(segs):
            v = cat["values"][j]
            if v:
                ax.barh(y, v - 0.06, left=left + 0.03, color=colors[j], height=0.62)
                ax.text(left + v / 2, y, f"{v:g}", ha="center", va="center", fontsize=8.5,
                        color="white" if j in (1, 3) else INK)
            left += v
    ax.set_yticks(range(len(cats)))
    ax.set_yticklabels([c["label"] for c in reversed(cats)], fontsize=8.5)
    ax.tick_params(axis="y", length=0)
    ax.set_xticks([])
    handles = [matplotlib.patches.Patch(color=colors[j], label=seg) for j, seg in enumerate(segs)]
    ax.legend(handles=handles, loc="lower left", bbox_to_anchor=(0, 1.0), fontsize=7.8, frameon=False, ncol=len(segs), handlelength=1.2)


def main(spec_path):
    spec = json.load(open(spec_path))
    fig, ax = plt.subplots(figsize=tuple(spec.get("size", [7.2, 2.8])), dpi=220)
    {"band": band, "ranking": ranking, "stacked": stacked}[spec["type"]](spec, ax)
    style(ax)
    fig.tight_layout(rect=(0, 0, 1, 0.80))
    fig.text(0.02, 0.95, spec["title"], fontsize=10.5, fontweight="bold", color=INK)
    if spec.get("subtitle"):
        fig.text(0.02, 0.885, spec["subtitle"], fontsize=8.5, color=SOFT)
    out = Path(spec["out"])
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=220)
    out.with_suffix(".txt").write_text(f"ALT:\n{spec['alt']}\n\nCAPTION:\n{spec['caption']}\n")
    print(f"wrote {out} and {out.with_suffix('.txt')}")
    for need in ("alt", "caption"):
        if not spec.get(need):
            print(f"WARNING: no {need}; check 10 will fail")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    main(sys.argv[1])
