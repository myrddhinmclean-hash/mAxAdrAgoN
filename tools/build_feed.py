#!/usr/bin/env python3
"""
build_feed.py - generate the feeds. Pure addition: writes new files, touches
nothing that exists, changes no URL.

    py -3 tools/build_feed.py            write the feeds
    py -3 tools/build_feed.py --check    write nothing, report what would change

THE SHAPE IS BRIEF, SUMMARY, ARCHIVE
That is how the work has been organised from the start, so the feeds follow it
rather than inventing a structure of their own.

    archive   the entry itself, on this site, canonical
    summary   the excerpt, which is what a feed item and a social card carry
    brief     one line that earns a click, which is what a note or a post is

Two feeds, because the first two layers are different objects and anything
consuming them wants one or the other, not both mixed:

    feed.xml    the entries. Long form. This is the one an importer wants.
    notes.xml   the log. Dated shop notes, the brief layer of the record.
    feed.json   the entries again as JSON Feed, for anything that prefers it.

WHY EVERY ITEM, ALWAYS
Importers take what the feed gives them. A feed capped at the most recent ten or
twenty silently truncates an archive on import, and the missing entries are not
obvious afterwards. This emits all of them.
"""

from __future__ import annotations

import json
import os
import re
import sys
from email.utils import formatdate
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://myrddhinmclean-hash.github.io/mAxAdrAgoN"
TITLE = "mAxAdrAgoN"
DESC = ("A running record of what Mac McLean is building: tabletop tools, agent "
        "systems, a world called Draega, and the mistakes kept in place.")


def read(path: str) -> str:
    with open(path, encoding="utf-8-sig", errors="replace") as fh:
        return fh.read()


def esc(s) -> str:
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def rfc822(date_str: str) -> str:
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    except ValueError:
        dt = datetime.now(timezone.utc)
    return formatdate(dt.timestamp(), usegmt=True)


def entry_url(slug: str) -> str:
    return "%s/hoards/entry.html?post=%s" % (SITE, slug)


def rss(items, path_name: str, feed_title: str, feed_desc: str) -> str:
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">',
           "<channel>",
           "<title>%s</title>" % esc(feed_title),
           "<link>%s/</link>" % SITE,
           "<description>%s</description>" % esc(feed_desc),
           "<language>en</language>",
           '<atom:link href="%s/%s" rel="self" type="application/rss+xml"/>' % (SITE, path_name),
           "<lastBuildDate>%s</lastBuildDate>" % formatdate(usegmt=True)]
    for it in items:
        out += ["<item>",
                "<title>%s</title>" % esc(it["title"]),
                "<link>%s</link>" % esc(it["url"]),
                '<guid isPermaLink="false">%s</guid>' % esc(it["guid"]),
                "<pubDate>%s</pubDate>" % rfc822(it["date"]),
                "<description>%s</description>" % esc(it["summary"])]
        for c in it.get("categories", []):
            out.append("<category>%s</category>" % esc(c))
        out.append("</item>")
    out += ["</channel>", "</rss>", ""]
    return "\n".join(out)


def main() -> int:
    check = "--check" in sys.argv
    posts = json.loads(read(os.path.join(ROOT, "content", "posts.json")))
    log = json.loads(read(os.path.join(ROOT, "content", "log.json")))

    entries = [{
        "title": p["title"],
        "url": entry_url(p["slug"]),
        "guid": "maxadragon-entry-%s" % p["slug"],
        "date": p.get("date", ""),
        "summary": p.get("excerpt", ""),
        "categories": [c for c in [p.get("hoard"), p.get("branch")] if c],
    } for p in sorted(posts, key=lambda p: p.get("date", ""), reverse=True)]

    notes = [{
        "title": e["title"],
        "url": "%s/index.html" % SITE,
        "guid": "maxadragon-note-%s-%s" % (e.get("date", ""), re.sub(r"[^a-z0-9]+", "-", e["title"].lower())[:48]),
        "date": e.get("date", ""),
        # The first paragraph is the summary layer. The rest is archive and
        # lives on the site, which is where a reader should end up.
        "summary": e.get("body", "").split("\n\n")[0],
        "categories": e.get("tags", []),
    } for e in log.get("entries", [])]

    files = {
        "feed.xml": rss(entries, "feed.xml", TITLE, DESC),
        "notes.xml": rss(notes, "notes.xml", "%s - the log" % TITLE,
                         "Dated notes on what was worked on, newest first."),
        "feed.json": json.dumps({
            "version": "https://jsonfeed.org/version/1.1",
            "title": TITLE,
            "home_page_url": SITE + "/",
            "feed_url": "%s/feed.json" % SITE,
            "description": DESC,
            "items": [{
                "id": e["guid"], "url": e["url"], "title": e["title"],
                "summary": e["summary"], "date_published": e["date"] + "T00:00:00Z",
                "tags": e["categories"],
            } for e in entries],
        }, indent=2) + "\n",
    }

    changed = []
    for name, body in files.items():
        path = os.path.join(ROOT, name)
        old = read(path) if os.path.isfile(path) else None
        # lastBuildDate moves every run; ignore it when deciding if anything changed.
        strip = lambda s: re.sub(r"<lastBuildDate>.*?</lastBuildDate>", "", s or "")
        if strip(old) != strip(body):
            changed.append(name)
            if not check:
                with open(path, "w", encoding="utf-8", newline="\n") as fh:
                    fh.write(body)

    print("entries in feed.xml : %d" % len(entries))
    print("notes in notes.xml  : %d" % len(notes))
    print("changed             : %s" % (", ".join(changed) if changed else "nothing"))
    if check:
        print("--check: nothing written")
        return 1 if changed else 0

    # Prove the XML parses rather than trusting that it was built correctly.
    import xml.etree.ElementTree as ET
    for name in ("feed.xml", "notes.xml"):
        tree = ET.parse(os.path.join(ROOT, name))
        n = len(tree.getroot().findall("./channel/item"))
        print("%-11s parses, %d items" % (name, n))
    json.loads(read(os.path.join(ROOT, "feed.json")))
    print("feed.json   parses")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
