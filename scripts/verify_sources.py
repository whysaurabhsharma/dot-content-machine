#!/usr/bin/env python3
"""verify_sources.py - open every link in a piece and report what came back.

Usage:
    python scripts/verify_sources.py pieces/piece-1.md

Checks 15 and 20 in CLAUDE.md need every link opened, not assumed. Prints the
status of each URL and exits 1 if any link fails or the piece has fewer than
five internal (getdot.ai) links.
"""
import re
import sys
import urllib.request
import urllib.error

UA = {"User-Agent": "Mozilla/5.0 (Dot content machine link check)"}


def check(url, timeout=15):
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.geturl()
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (403, 405):
                continue
            return e.code, url
        except Exception as e:
            if method == "HEAD":
                continue
            return f"error: {type(e).__name__}: {str(e)[:80]}", url
    return "error", url


def main(path):
    text = open(path, encoding="utf-8").read()
    urls = sorted(set(re.findall(r"\]\((https?://[^)\s]+)\)", text)))
    if not urls:
        print("No links found.")
        return 1
    bad, internal = 0, 0
    print(f"\nverify_sources.py  {path}\n")
    for u in urls:
        status, final = check(u)
        ok = isinstance(status, int) and 200 <= status < 400
        bad += 0 if ok else 1
        internal += 1 if "getdot.ai" in u else 0
        moved = f"  -> {final}" if final != u else ""
        print(f"  {'OK  ' if ok else 'FAIL'}  {status}  {u}{moved}")
    print(f"\n{len(urls)} links, {internal} internal, {bad} failed")
    if internal < 5:
        print("Fewer than five internal links: check 20 fails. See facts/house-structure-and-links.md.")
    return 1 if bad or internal < 5 else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
