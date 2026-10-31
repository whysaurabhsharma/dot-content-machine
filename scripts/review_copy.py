#!/usr/bin/env python3
"""review_copy.py - write the body-only copy the blind reviewers read.

Usage:
    python scripts/review_copy.py <slug>

Reads pieces/<slug>.md and writes reviews/<slug>/draft.md: the title as an H1,
then the body, with the front matter stripped. The front matter (queries, figures
file, Playbook URL, reverse links, dataset) says what the writer intended, which a
stranger reading the page wouldn't know. The piece file is only read; the copy is
replaced each time, so make it again after every edit.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from export_docx import front_matter  # noqa: E402


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    slug = argv[1]
    piece = Path("pieces") / f"{slug}.md"
    if not piece.exists():
        print(f"No piece at {piece}")
        return 1
    meta, body = front_matter(piece.read_text(encoding="utf-8"))
    out = Path("reviews") / slug / "draft.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    title = meta.get("title", "")
    out.write_text((f"# {title}\n\n" if title else "") + body.strip() + "\n", encoding="utf-8")
    print(f"Wrote {out} ({len(body.split())} words, front matter stripped)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
