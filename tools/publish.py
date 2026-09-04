#!/usr/bin/env python3
"""
publish.py - step 6 of the loop. One command from approved draft to live.

    python tools/publish.py <slug>

Reads the draft's own frontmatter for title, date, hoard and summary, registers
it in content/posts.json newest first, validates, commits, pushes, and verifies
the entry actually rendered on the live site.

Refuses to push if validation fails. Refuses to publish a draft whose summary
is still a placeholder, because the excerpt is the owner's under governance
section 2.4 and it is the most visible text on the site.

    --dry-run     do everything except commit and push
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS = os.path.join(ROOT, "content", "posts.json")
LIVE = "https://myrddhinmclean-hash.github.io/mAxAdrAgoN"
HOARDS = ("draega", "machine", "odd")


def run(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess:
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if check and p.returncode != 0:
        print("command failed: %s" % " ".join(cmd))
        print(p.stdout)
        print(p.stderr)
        sys.exit(1)
    return p


def frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    out = {}
    for line in text[3:end].splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def find_draft(slug: str) -> tuple[str, str]:
    for hoard in HOARDS:
        p = os.path.join(ROOT, "content", hoard, slug + ".md")
        if os.path.isfile(p):
            return hoard, p
    print("no draft found for slug %r in content/{%s}/" % (slug, ",".join(HOARDS)))
    sys.exit(1)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    slug = args.slug

    hoard, path = find_draft(slug)
    # utf-8-sig: PowerShell and several Windows editors write a BOM, which
    # would otherwise push the leading --- off position 0 and make the
    # frontmatter silently unparseable. Found by the guard test, 2026-08-31.
    with open(path, encoding="utf-8-sig") as fh:
        fm = frontmatter(fh.read())

    print("draft: %s" % os.path.relpath(path, ROOT))

    # --- guards -----------------------------------------------------------
    missing = [k for k in ("title", "date", "hoard", "summary") if not fm.get(k)]
    if missing:
        print("FAIL: frontmatter missing %s" % missing)
        return 1
    if fm["hoard"] != hoard:
        print("FAIL: frontmatter says hoard %r but file is in content/%s/"
              % (fm["hoard"], hoard))
        return 1
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", fm["date"]):
        print("FAIL: date %r is not YYYY-MM-DD" % fm["date"])
        return 1
    if "OWNER TO WRITE" in fm["summary"] or "[" in fm["summary"][:2]:
        print("FAIL: summary is still a placeholder.")
        print("The excerpt is the owner's under governance 2.4. Nothing publishes without it.")
        return 1

    posts = json.load(open(POSTS, encoding="utf-8"))
    if any(p.get("slug") == slug for p in posts):
        print("already registered in posts.json, re-validating and pushing any edits")
    else:
        entry = {
            "slug": slug,
            "hoard": hoard,
            "title": fm["title"],
            "date": fm["date"],
            "excerpt": fm["summary"],
            "path": "../content/%s/%s.md" % (hoard, slug),
        }
        # Optional. A machine entry can name the branch of the map it belongs
        # to, which is what the entry page links to and what map.html links
        # back from. Carried from frontmatter so the connection is declared in
        # the draft rather than patched into the index afterwards.
        if fm.get("branch") and fm.get("branch_n"):
            entry["branch"] = fm["branch"]
            entry["branch_n"] = fm["branch_n"]
        posts.insert(0, entry)   # newest first
        with open(POSTS, "w", encoding="utf-8") as fh:
            json.dump(posts, fh, indent=2)
            fh.write("\n")
        print("registered in posts.json, newest first")

    # --- validate ---------------------------------------------------------
    print("\nvalidating ...")
    v = run([sys.executable, os.path.join("tools", "validate_site.py")], check=False)
    print(v.stdout.strip().splitlines()[-1] if v.stdout else "")
    if v.returncode != 0:
        print(v.stdout)
        print("\nABORTED. Nothing committed, nothing pushed.")
        return 1

    if args.dry_run:
        print("\ndry run: stopping before commit")
        return 0

    # --- commit and push --------------------------------------------------
    notes = os.path.join("content", hoard, slug + ".editor-notes.md")
    run(["git", "add", os.path.relpath(path, ROOT), "content/posts.json"])
    if os.path.isfile(os.path.join(ROOT, notes)):
        run(["git", "add", notes])
    run(["git", "commit", "-m", "publish: %s" % fm["title"]])
    run(["git", "push", "origin", "main"])
    print("pushed")

    # --- verify live ------------------------------------------------------
    print("\nverifying live ...")
    url = "%s/content/posts.json" % LIVE
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            live_posts = json.loads(r.read().decode("utf-8"))
        if any(p.get("slug") == slug for p in live_posts):
            print("LIVE: %s appears in the published index" % slug)
            print("      %s/hoards/%s.html" % (LIVE, hoard))
        else:
            print("NOT YET LIVE: GitHub Pages can take a minute. Re-check the hoard page.")
    except Exception as exc:
        print("could not verify: %s" % exc)
        print("check manually: %s/hoards/%s.html" % (LIVE, hoard))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
