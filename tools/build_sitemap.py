#!/usr/bin/env python3
"""build_sitemap.py - write sitemap.xml from the pages on disk and posts.json.

    python tools/build_sitemap.py

One URL per top-level page that is not a redirect stub, plus one per registered
entry. validate_site.py CHECK 8 fails the build if the sitemap is missing a
registered slug, so a publish that forgets this step cannot go out quiet.
Added 2026-09-04; the site had no sitemap or robots.txt before.
"""
from __future__ import annotations

import json
import os
import re
import sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIVE = "https://myrddhinmclean-hash.github.io/mAxAdrAgoN"
POSTS = os.path.join(ROOT, "content", "posts.json")
OUT = os.path.join(ROOT, "sitemap.xml")

# Pages that redirect or exist only as error targets carry no content to index.
SKIP = {"404.html", "log.html", "lore.html"}


def is_redirect(path: str) -> bool:
    try:
        head = open(path, encoding="utf-8").read(600)
    except OSError:
        return True
    return 'http-equiv="refresh"' in head


def page_urls() -> list[str]:
    urls = []
    for name in sorted(os.listdir(ROOT)):
        if not name.endswith(".html") or name in SKIP:
            continue
        if is_redirect(os.path.join(ROOT, name)):
            continue
        urls.append(f"{LIVE}/{name}" if name != "index.html" else f"{LIVE}/")
    hoards = os.path.join(ROOT, "hoards")
    for name in sorted(os.listdir(hoards)):
        if not name.endswith(".html") or name == "entry.html":
            continue
        if is_redirect(os.path.join(hoards, name)):
            continue
        urls.append(f"{LIVE}/hoards/{name}")
    return urls


def entry_urls(posts: list[dict]) -> list[tuple[str, str]]:
    return [(f"{LIVE}/hoards/entry.html?post={p['slug']}", p.get("date", "")) for p in posts]


def build() -> str:
    posts = json.load(open(POSTS, encoding="utf-8"))
    today = date.today().isoformat()
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in page_urls():
        lines += ["  <url>", f"    <loc>{u}</loc>", f"    <lastmod>{today}</lastmod>", "  </url>"]
    for u, d in entry_urls(posts):
        lastmod = d if re.match(r"^\d{4}-\d{2}-\d{2}$", d or "") else today
        lines += ["  <url>", f"    <loc>{u.replace('&', '&amp;')}</loc>", f"    <lastmod>{lastmod}</lastmod>", "  </url>"]
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def main() -> int:
    xml = build()
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(xml)
    n = xml.count("<url>")
    print(f"wrote sitemap.xml with {n} urls")
    return 0


if __name__ == "__main__":
    sys.exit(main())
