#!/usr/bin/env python3
"""
validate_site.py - the mechanical half of GOVERNANCE.md section 7 step 5.

Run from the repo root before every push:

    python tools/validate_site.py

Exit code 0 means safe to push. Non-zero means do not push.

This exists because "Antigravity validates before commit" was a rule enforced by
an agent remembering to do it. The rule is now a script, so it is enforced by
running. Agent identity is not the gate; this is.

Checks:
  1  content/posts.json parses as JSON
  2  every registered slug resolves to a real file
  3  no editor notes or source-ledger material leaked into any entry body
  4  the WotC Fan Content Policy disclaimer is present on every SITE page
  5  frontmatter sanity: title, date, hoard present; hoard matches the index
  6  informational: entries per hoard, and which hoards will render empty

Checks 1-5 fail the build. Check 6 never fails - hoard.js has a graceful empty
state ("This shelf of the hoard is currently quiet"), so an empty hoard is a
content decision, not a defect.
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Directories that are not the published site. Anything under these is ignored
# by the disclaimer check - they are working material, not pages readers reach.
NON_SITE_DIRS = {".git", "campaign", "tools", "Storyline GG", "node_modules"}

# Markers that mean editor-only material has leaked into a reader-facing file.
LEAK_MARKERS = (
    "SOURCE LEDGER",
    "VETO SWEEP",
    "PRESENCE CHECK",
    "DASH COUNT",
    "EDITOR NOTE",
    "REQUIRES VERIFICATION",
    "INVENTIONS:",
    "WEAKEST PASSAGE",
)

HOARDS = ("draega", "machine", "odd")

failures = []
warnings = []


def ok(msg):
    print("  PASS  " + msg)


def bad(msg):
    print("  FAIL  " + msg)
    failures.append(msg)


def warn(msg):
    print("  WARN  " + msg)
    warnings.append(msg)


def info(msg):
    print("  INFO  " + msg)


def read(path):
    # utf-8-sig strips a BOM if present. Windows tools write them, and a BOM
    # pushes the leading --- off position 0, silently breaking frontmatter.
    with open(path, encoding="utf-8-sig", errors="replace") as fh:
        return fh.read()


def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end]
    out = {}
    for line in block.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip().strip('"').strip("'")
    return out


print("validate_site.py - repo root: %s" % ROOT)
print()

# ---------------------------------------------------------------- check 1
print("CHECK 1  posts.json parses")
posts_path = os.path.join(ROOT, "content", "posts.json")
posts = None
try:
    posts = json.loads(read(posts_path))
    ok("posts.json parses, %d entries registered" % len(posts))
except Exception as exc:
    bad("posts.json does not parse: %s" % exc)
    print()
    print("ABORT: nothing else can be checked while the index is broken.")
    sys.exit(1)

# ---------------------------------------------------------------- check 2
print()
print("CHECK 2  every slug resolves to a file")
missing = []
for entry in posts:
    rel = entry.get("path", "").replace("../", "")
    if not rel or not os.path.isfile(os.path.join(ROOT, rel)):
        missing.append("%s -> %s" % (entry.get("slug"), entry.get("path")))
if missing:
    for m in missing:
        bad("no file for %s" % m)
else:
    ok("all %d registered slugs resolve" % len(posts))

# ---------------------------------------------------------------- check 3
print()
print("CHECK 3  no editor material in entry bodies")
leaks = []
for entry in posts:
    rel = entry.get("path", "").replace("../", "")
    full = os.path.join(ROOT, rel)
    if not os.path.isfile(full):
        continue
    body = read(full)
    for marker in LEAK_MARKERS:
        if marker in body:
            leaks.append("%s contains %r" % (entry.get("slug"), marker))
if leaks:
    for lk in leaks:
        bad(lk)
else:
    ok("no ledger or editor-note markers in any registered entry")

# ---------------------------------------------------------------- check 4
print()
print("CHECK 4  WotC disclaimer on every site page")
site_pages = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in NON_SITE_DIRS]
    for fn in filenames:
        if fn.endswith(".html"):
            site_pages.append(os.path.join(dirpath, fn))

no_disclaimer = []
for page in site_pages:
    if not re.search(r"Fan Content Policy|Wizards of the Coast", read(page), re.I):
        no_disclaimer.append(os.path.relpath(page, ROOT))
if no_disclaimer:
    for pg in no_disclaimer:
        bad("no WotC disclaimer: %s" % pg)
else:
    ok("disclaimer present on all %d site pages" % len(site_pages))

# ---------------------------------------------------------------- check 5
print()
print("CHECK 5  frontmatter sanity")
fm_problems = []
for entry in posts:
    rel = entry.get("path", "").replace("../", "")
    full = os.path.join(ROOT, rel)
    if not os.path.isfile(full):
        continue
    fm = parse_frontmatter(read(full))
    slug = entry.get("slug")
    for field in ("title", "date", "hoard"):
        if not fm.get(field):
            fm_problems.append("%s: frontmatter missing %s" % (slug, field))
    if fm.get("hoard") and fm["hoard"] != entry.get("hoard"):
        fm_problems.append(
            "%s: hoard mismatch, file says %r but index says %r"
            % (slug, fm["hoard"], entry.get("hoard"))
        )
    if fm.get("date") and not re.match(r"^\d{4}-\d{2}-\d{2}$", fm["date"]):
        fm_problems.append("%s: date %r is not YYYY-MM-DD" % (slug, fm["date"]))
if fm_problems:
    for p in fm_problems:
        bad(p)
else:
    ok("frontmatter complete and consistent with the index")

# ---------------------------------------------------------------- check 6
print()
print("CHECK 6  hoard occupancy (informational)")
counts = {h: 0 for h in HOARDS}
for entry in posts:
    h = entry.get("hoard")
    counts[h] = counts.get(h, 0) + 1
info("entries per hoard: %s" % counts)
for h in HOARDS:
    if counts.get(h, 0) == 0:
        info("hoard '%s' renders its empty state - by design, not a defect" % h)

# ---------------------------------------------------------------- verdict
print()
print("=" * 60)
if failures:
    print("RESULT: DO NOT PUSH - %d failure(s)" % len(failures))
    for f in failures:
        print("  - %s" % f)
    sys.exit(1)

print("RESULT: SAFE TO PUSH")
if warnings:
    print("(%d warning(s), none blocking)" % len(warnings))
sys.exit(0)
