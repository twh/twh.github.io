#!/usr/bin/env python3
"""Validate every link in the built site.

Internal links are resolved against the build output on disk; a miss is a hard
failure, because it means the site shipped a dead link. External links are
fetched over the network and reported, but a failure there is advisory: remote
hosts rate-limit CI runners and go down for reasons that have nothing to do
with this site.

Usage: check_links.py <public_dir> [--external] [--strict-external]
"""
import concurrent.futures
import html
import os
import re
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from urllib.parse import urlsplit, urljoin

HREF = re.compile(r'(?:href|src)\s*=\s*(?:"([^"]*)"|\'([^\']*)\'|([^\s>]+))', re.I)
# preconnect/dns-prefetch point at an origin, not a document; fetching them
# returns 404 from hosts that only serve paths (fonts.googleapis.com does).
PRECONNECT = re.compile(
    r'<link\b[^>]*\brel\s*=\s*["\']?(?:preconnect|dns-prefetch)\b[^>]*>', re.I
)
SKIP_SCHEMES = ("mailto:", "tel:", "javascript:", "data:", "#")
UA = "Mozilla/5.0 (compatible; waynehendricks.com link checker)"
TIMEOUT = 20


def pages(root):
    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            if name.endswith(".html"):
                yield os.path.join(dirpath, name)


def collect(root):
    """Return {url: [source pages]} for every href/src in the build."""
    found = defaultdict(list)
    for path in pages(root):
        rel = os.path.relpath(path, root)
        with open(path, encoding="utf-8", errors="replace") as fh:
            source = PRECONNECT.sub("", fh.read())
        for match in HREF.finditer(source):
            url = html.unescape(next(g for g in match.groups() if g is not None)).strip()
            if not url or url.lower().startswith(SKIP_SCHEMES):
                continue
            found[url].append(rel)
    return found


def resolve_internal(root, url, source_page):
    """Map an internal URL to a file on disk, or None if it does not exist."""
    path = urlsplit(url).path
    if not path:
        return True  # bare fragment or query against the current page
    if path.startswith("/"):
        target = os.path.join(root, path.lstrip("/"))
    else:
        base = os.path.dirname(os.path.join(root, source_page))
        target = os.path.normpath(os.path.join(base, path))
    if os.path.isfile(target):
        return True
    if os.path.isdir(target) and os.path.isfile(os.path.join(target, "index.html")):
        return True
    return False


def check_external(url):
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            return url, response.status, ""
    except urllib.error.HTTPError as exc:
        if exc.code in (403, 405, 501):  # host dislikes HEAD; retry with GET
            try:
                request = urllib.request.Request(url, headers={"User-Agent": UA})
                with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
                    return url, response.status, ""
            except Exception as inner:  # noqa: BLE001 - reported, not raised
                return url, getattr(inner, "code", 0), str(inner)
        return url, exc.code, str(exc)
    except Exception as exc:  # noqa: BLE001 - reported, not raised
        return url, 0, str(exc)


def main() -> int:
    root = sys.argv[1]
    do_external = "--external" in sys.argv
    strict_external = "--strict-external" in sys.argv

    found = collect(root)
    internal, external = {}, {}
    for url, sources in found.items():
        if urlsplit(url).scheme in ("http", "https"):
            external[url] = sources
        else:
            internal[url] = sources

    broken_internal = []
    for url, sources in sorted(internal.items()):
        for source in sources:
            if not resolve_internal(root, url, source):
                broken_internal.append((url, source))

    print(f"internal links: {len(internal)} unique, {len(broken_internal)} broken")
    for url, source in broken_internal:
        print(f"  BROKEN  {url}   (in {source})")

    broken_external = []
    if do_external:
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
            results = list(pool.map(check_external, sorted(external)))
        for url, status, detail in results:
            if status and 200 <= status < 400:
                continue
            broken_external.append((url, status, detail))
        print(f"external links: {len(external)} unique, {len(broken_external)} failing")
        for url, status, detail in broken_external:
            where = ", ".join(external[url][:3])
            print(f"  {status or 'ERR'}  {url}   (in {where}) {detail}")

    if broken_internal:
        return 1
    if strict_external and broken_external:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
