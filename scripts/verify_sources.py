#!/usr/bin/env python3
"""verify_sources.py - open every link in a piece and report what came back.

Usage:
    python scripts/verify_sources.py pieces/ai-analyst-follow-up-questions.md

Checks 15 and 20 in CLAUDE.md need every link opened, not assumed. Prints the
status of each URL and exits 1 if any link fails or the piece has fewer than
five internal (getdot.ai) links.
"""
import re
import sys
import urllib.request
import urllib.error

UA = {"User-Agent": "Mozilla/5.0 (Dot content machine link check)"}
# Some sites refuse a named bot (Uber answered 406, Salesforce 500, 31 October 2026) but serve a browser.
BROWSER = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/124.0 Safari/537.36",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Accept-Language": "en-US,en;q=0.9"}


def fetch(url, method, headers, timeout):
    req = urllib.request.Request(url, method=method, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.geturl()


def check(url, timeout=15):
    result = ("error", url)
    for method in ("HEAD", "GET"):
        try:
            return fetch(url, method, UA, timeout)
        except urllib.error.HTTPError as e:
            # Some sites refuse or mishandle HEAD; Kaggle answers HEAD with 404 and GET with 200.
            if method == "HEAD" and e.code in (403, 404, 405):
                continue
            result = (e.code, url)
            break
        except Exception as e:
            if method == "HEAD":
                continue
            result = (f"error: {type(e).__name__}: {str(e)[:80]}", url)
            break
    # Before reporting a refusal or a server error, retry once as a browser would ask.
    # A "not found" (404, 410) is reported as it is: some sites answer a browser with 200
    # even for a page that doesn't exist (Kaggle did, 31 October 2026).
    if result[0] in (404, 410):
        return result
    try:
        status, final = fetch(url, "GET", BROWSER, timeout)
        return status, final
    except urllib.error.HTTPError as e:
        return result if result[0] != "error" else (e.code, url)
    except Exception:
        return result


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
