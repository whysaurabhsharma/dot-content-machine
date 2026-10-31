---
name: export
description: Exports a finished piece to exports/<slug>/ as .docx, clean Markdown and paste-ready Webflow files. Refuses while any check_piece.py check FAILs. Prepares files only; creates no draft in Webflow. Started only by a person or the workflow.
disable-model-invocation: true
argument-hint: <piece-slug>
allowed-tools: Read, Glob, Bash(python scripts/timing.py:*), Bash(python -I scripts/timing.py:*), Bash(python scripts/check_piece.py:*), Bash(python -I scripts/check_piece.py:*), Bash(python scripts/export_docx.py:*), Bash(python -I scripts/export_docx.py:*), Bash(python scripts/export_webflow.py:*), Bash(python -I scripts/export_webflow.py:*)
---

# Export

No source prompt. The last step before Decision 4 (publish), which stays a person's.

**The piece:** the first word of `$ARGUMENTS` is the slug. Run the commands with the Python that has `requirements.txt` installed (README, Quick start); python-docx is needed.

**This skill prepares files. It does not create a draft in Webflow.** There is no Webflow connector here; a real one is Stage 4's export step and needs a token with CMS:write. Say this in the report.

## Timing

First action: `python -I scripts/timing.py <slug> export start`. Last action: `python -I scripts/timing.py <slug> export end`. Stage names: `runs/README.md#timing`.

## Gate

Run `python -I scripts/check_piece.py pieces/<slug>.md`. If any check is FAIL, stop: report the FAILs, export nothing, and log `export end`. HUMAN checks don't block the export, but list them in the report as still open before Decision 4.

If the piece's first body line is `PRACTICE ONLY`, export into `exports/<slug>-practice/` instead, and say it is not for publication (hard rule 4).

## Inputs

- `pieces/<slug>.md`: the piece. Read only.
- The chart image its body references (in `charts/`).
- `pieces/<slug>-faq.json`, if `/seo-geo` wrote one.

## Output

All in `exports/<slug>/`:

- `<front-matter slug>.docx`: from `python -I scripts/export_docx.py pieces/<slug>.md --out exports/<slug>`.
- `<front-matter slug>.md`, `webflow.html` and `webflow-fields.json`: from `python -I scripts/export_webflow.py pieces/<slug>.md --out exports/<slug>`. The JSON maps the Webflow CMS fields (name, slug, SEO title, meta description), lists the images to upload with their alt text, and points to the FAQ file if there is one.

Report each file written, any image not found, any empty CMS field, and the HUMAN checks still open.

## Must not

- Export while any check FAILs. Decision 4 is enforced by the checker, not by trust.
- Change the piece, its figures or its chart.
- Publish, or create anything in Webflow or anywhere else. Publishing is Decision 4, a person's.
- Write outside `exports/<slug>/` (or `exports/<slug>-practice/`).
