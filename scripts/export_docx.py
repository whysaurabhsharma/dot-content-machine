#!/usr/bin/env python3
"""export_docx.py - export one piece to .docx.

Usage:
    python scripts/export_docx.py pieces/<slug>.md
    python scripts/export_docx.py pieces/<slug>.md --out exports/<slug>

Writes <out>/<slug>.docx (default out: exports/<slug>). The title comes from the
front matter; the body keeps headings, paragraphs, bold, italics, links, lists,
tables and the chart image with its caption. The piece file is only read.

Also holds the small Markdown parser that export_webflow.py reuses, so both
exports read a piece the same way.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INLINE = re.compile(r"\*\*(.+?)\*\*|(?<![\w*])\*(?!\s)(.+?)\*(?!\w)|\[([^\]]+)\]\(([^)\s]+)\)|`([^`]+)`")


# ---------- parsing, shared with export_webflow.py ----------
def unquote(s):
    """Strip one matching pair of surrounding double quotes, not a quote that ends a value
    ('anchor "x"' kept its closing quote stripped until 1 November 2026)."""
    return s[1:-1] if len(s) >= 2 and s[0] == s[-1] == '"' else s


def front_matter(text):
    """(meta, body). Lists in the front matter become Python lists."""
    if not text.startswith("---"):
        return {}, text
    _, fm, body = text.split("---", 2)
    meta, key = {}, None
    for line in fm.strip().splitlines():
        if re.match(r"^\s+-\s+", line) and key:
            meta.setdefault(key, []).append(unquote(line.split("-", 1)[1].strip()))
        elif ":" in line:
            key, val = line.split(":", 1)
            key, val = key.strip(), unquote(val.strip())
            meta[key] = val if val else []
    return meta, body


def blocks(body):
    """List of (kind, data): h2, h3, para, ulist, olist, table, image, caption."""
    out, prev = [], None
    for raw in re.split(r"\n\s*\n", body.strip()):
        b = raw.strip()
        if not b:
            continue
        if b.startswith("### "):
            out.append(("h3", b[4:].strip()))
        elif b.startswith("## "):
            out.append(("h2", b[3:].strip()))
        elif b.startswith("|"):
            rows = [[c.strip() for c in line.strip().strip("|").split("|")] for line in b.splitlines()]
            out.append(("table", [r for i, r in enumerate(rows) if i != 1]))
        elif b.startswith("!["):
            m = re.match(r"!\[([^\]]*)\]\(([^)]+)\)", b)
            out.append(("image", {"alt": m.group(1), "src": m.group(2)}))
        elif re.match(r"^\d+\.\s", b):
            out.append(("olist", [re.sub(r"^\d+\.\s+", "", l) for l in b.splitlines()]))
        elif b.startswith("- "):
            out.append(("ulist", [l[2:] for l in b.splitlines()]))
        elif prev == "image" and b.startswith("*") and b.endswith("*") and not b.startswith("**"):
            out.append(("caption", b.strip("*")))
        else:
            out.append(("para", " ".join(l.strip() for l in b.splitlines())))
        prev = out[-1][0]
    return out


def inline(text):
    """Split inline Markdown into runs: (text, bold, italic, url)."""
    runs, pos = [], 0
    for m in INLINE.finditer(text):
        if m.start() > pos:
            runs.append((text[pos:m.start()], False, False, None))
        if m.group(1) is not None:
            runs += [(t, True, i, u) for t, _, i, u in inline(m.group(1))]
        elif m.group(2) is not None:
            runs += [(t, b, True, u) for t, b, _, u in inline(m.group(2))]
        elif m.group(3) is not None:
            runs.append((m.group(3), False, False, m.group(4)))
        else:
            runs.append((m.group(5), False, False, None))
        pos = m.end()
    if pos < len(text):
        runs.append((text[pos:], False, False, None))
    return runs


def load(path):
    text = Path(path).read_text(encoding="utf-8")
    meta, body = front_matter(text)
    return meta, blocks(body)


# ---------- docx ----------
def add_runs(par, text):
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    for t, bold, italic, url in inline(text):
        if url is None:
            r = par.add_run(t)
            r.bold, r.italic = bold, italic
            continue
        rel = par.part.relate_to(url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
                                 is_external=True)
        link = OxmlElement("w:hyperlink")
        link.set(qn("r:id"), rel)
        run = OxmlElement("w:r")
        props = OxmlElement("w:rPr")
        style = OxmlElement("w:rStyle")
        style.set(qn("w:val"), "Hyperlink")
        props.append(style)
        underline = OxmlElement("w:u")
        underline.set(qn("w:val"), "single")
        props.append(underline)
        run.append(props)
        txt = OxmlElement("w:t")
        txt.text = t
        txt.set(qn("xml:space"), "preserve")
        run.append(txt)
        link.append(run)
        par._p.append(link)


def export_docx(piece_path, out_dir):
    from docx import Document
    from docx.shared import Inches
    meta, parts = load(piece_path)
    slug = meta.get("slug") or Path(piece_path).stem
    doc = Document()
    doc.add_heading(meta.get("title", slug), level=0)
    missing = []
    for kind, data in parts:
        if kind in ("h2", "h3"):
            doc.add_heading(data, level=1 if kind == "h2" else 2)
        elif kind == "para":
            add_runs(doc.add_paragraph(), data)
        elif kind in ("ulist", "olist"):
            for item in data:
                add_runs(doc.add_paragraph(style="List Bullet" if kind == "ulist" else "List Number"), item)
        elif kind == "table":
            table = doc.add_table(rows=len(data), cols=len(data[0]))
            table.style = "Table Grid"
            for i, row in enumerate(data):
                for j, cell in enumerate(row[:len(data[0])]):
                    p = table.cell(i, j).paragraphs[0]
                    add_runs(p, f"**{cell}**" if i == 0 else cell)
        elif kind == "image":
            img = ROOT / data["src"]
            if img.exists():
                doc.add_picture(str(img), width=Inches(6))
            else:
                missing.append(data["src"])
                doc.add_paragraph(f"Image not found: {data['src']}")
            doc.add_paragraph(f"Alt text: {data['alt']}").runs[0].italic = True
        elif kind == "caption":
            add_runs(doc.add_paragraph(), f"*{data}*")
    out = Path(out_dir) / f"{slug}.docx"
    out.parent.mkdir(parents=True, exist_ok=True)
    doc.save(out)
    return out, missing


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    piece = argv[1]
    meta, _ = load(piece)
    slug = meta.get("slug") or Path(piece).stem
    out_dir = argv[argv.index("--out") + 1] if "--out" in argv else f"exports/{slug}"
    out, missing = export_docx(piece, out_dir)
    print(f"Wrote {out}" + (f"; images not found: {missing}" if missing else ""))
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
