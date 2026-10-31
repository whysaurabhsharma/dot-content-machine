#!/usr/bin/env python3
"""export_webflow.py - prepare one piece as paste-ready files for Webflow and as clean Markdown.

Usage:
    python scripts/export_webflow.py pieces/<slug>.md
    python scripts/export_webflow.py pieces/<slug>.md --out exports/<slug>

Writes, in <out> (default exports/<slug>):
- <slug>.md: the piece without its front matter, title as H1.
- webflow.html: the body as HTML for Webflow's rich-text field. No H1: the title
  is its own field.
- webflow-fields.json: the CMS fields (name, slug, SEO title, meta description),
  the images to upload, and the FAQ file if /seo-geo wrote one.

This prepares files to paste. It does not create a draft in Webflow: there is no
Webflow connector or CMS token here. The piece file is only read.
"""
import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from export_docx import ROOT, front_matter, inline, load  # noqa: E402


def html_inline(text):
    out = []
    for t, bold, italic, url in inline(text):
        s = html.escape(t)
        if italic:
            s = f"<em>{s}</em>"
        if bold:
            s = f"<strong>{s}</strong>"
        if url:
            s = f'<a href="{html.escape(url, quote=True)}">{s}</a>'
        out.append(s)
    return "".join(out)


def to_html(parts):
    out = []
    for kind, data in parts:
        if kind in ("h2", "h3"):
            out.append(f"<{kind}>{html_inline(data)}</{kind}>")
        elif kind == "para":
            out.append(f"<p>{html_inline(data)}</p>")
        elif kind in ("ulist", "olist"):
            tag = "ul" if kind == "ulist" else "ol"
            out.append(f"<{tag}>" + "".join(f"<li>{html_inline(i)}</li>" for i in data) + f"</{tag}>")
        elif kind == "table":
            head = "".join(f"<th>{html_inline(c)}</th>" for c in data[0])
            rows = "".join("<tr>" + "".join(f"<td>{html_inline(c)}</td>" for c in r) + "</tr>" for r in data[1:])
            out.append(f"<table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table>")
        elif kind == "image":
            out.append(f'<figure><img src="{html.escape(Path(data["src"]).name, quote=True)}" '
                       f'alt="{html.escape(data["alt"], quote=True)}">')
        elif kind == "caption":
            if out and out[-1].startswith("<figure>") and not out[-1].endswith("</figure>"):
                out[-1] += f"<figcaption>{html_inline(data)}</figcaption></figure>"
            else:
                out.append(f"<p><em>{html_inline(data)}</em></p>")
    return "\n".join(o + ("</figure>" if o.startswith("<figure>") and not o.endswith("</figure>") else "")
                     for o in out)


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    piece = Path(argv[1])
    text = piece.read_text(encoding="utf-8")
    meta, body = front_matter(text)
    _, parts = load(piece)
    slug = meta.get("slug") or piece.stem
    out = Path(argv[argv.index("--out") + 1] if "--out" in argv else f"exports/{slug}")
    out.mkdir(parents=True, exist_ok=True)

    (out / f"{slug}.md").write_text(f"# {meta.get('title', slug)}\n\n{body.strip()}\n", encoding="utf-8")
    (out / "webflow.html").write_text(to_html(parts) + "\n", encoding="utf-8")
    images = [{"file": d["src"], "upload_as": Path(d["src"]).name, "alt": d["alt"],
               "exists": (ROOT / d["src"]).exists()} for k, d in parts if k == "image"]
    faq = ROOT / "pieces" / f"{piece.stem}-faq.json"
    fields = {
        "note": "Paste-ready files only. No draft was created in Webflow.",
        "name": meta.get("title", ""),
        "slug": slug,
        "seo_title": meta.get("seo_title", ""),
        "meta_description": meta.get("meta", ""),
        "post_body": "webflow.html",
        "images_to_upload": images,
        "faq_schema": faq.relative_to(ROOT).as_posix() if faq.exists() else None,
    }
    (out / "webflow-fields.json").write_text(json.dumps(fields, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    missing = [k for k in ("name", "seo_title", "meta_description") if not fields[k]]
    print(f"Wrote {out / (slug + '.md')}, {out / 'webflow.html'}, {out / 'webflow-fields.json'}"
          + (f"; empty fields: {missing}" if missing else ""))
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
