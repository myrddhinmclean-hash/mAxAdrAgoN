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

HOARDS = ("draega", "machine")  # Odd removed 2026-09-04: never Mac's, AI scaffold; GOVERNANCE A8

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
skipped_stubs = []
for page in site_pages:
    body = read(page)
    # Redirect stubs carry no content of their own - only a meta refresh pointing
    # somewhere else. Requiring a legal notice on a page nobody reads for half a
    # second is noise, and it trains people to ignore this check.
    if re.search(r'http-equiv\s*=\s*["\']refresh', body, re.I):
        skipped_stubs.append(os.path.relpath(page, ROOT))
        continue
    if not re.search(r"Fan Content Policy|Wizards of the Coast", body, re.I):
        no_disclaimer.append(os.path.relpath(page, ROOT))
if skipped_stubs:
    print("  INFO  redirect stubs exempt: %s" % ", ".join(sorted(skipped_stubs)))
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
print("CHECK 7  entry title is rendered exactly once")
# Every entry page printed its title twice for the whole life of the site: once
# from the frontmatter, once from the markdown body's own H1. Six checks passed
# green the entire time, because none of them looked at what a reader sees.
#
# This cannot execute JavaScript, so it does not pretend to render the page. It
# guards the two static facts the fix depends on: hoard.js still lifts a leading
# body H1 out of the content, and the page still reads it back.
hoard_js = os.path.join(ROOT, "assets", "js", "hoard.js")
if not os.path.exists(hoard_js):
    bad("hoard.js is missing")
else:
    js = read(hoard_js)
    if "bodyTitle" not in js:
        bad("hoard.js no longer lifts the leading body H1 out of the markdown "
            "(bodyTitle is gone). Every entry would print its title twice.")
    elif "parsed.metadata" not in js:
        bad("hoard.js extracts bodyTitle but the entry page never reads it back.")
    else:
        ok("hoard.js still lifts the leading body H1; titles render once")

    mismatches = []
    for p in posts:
        md_path = os.path.normpath(os.path.join(ROOT, "hoards", p["path"]))
        if not os.path.exists(md_path):
            continue
        m = re.search(r"^#\s+(.+?)\s*$", read(md_path), re.M)
        if m and m.group(1).strip() != str(p.get("title", "")).strip():
            mismatches.append((p["slug"], p.get("title", ""), m.group(1).strip()))
    if mismatches:
        print("  INFO  %d entry heading(s) differ from the index title; the "
              "longer one is shown:" % len(mismatches))
        for slug, t, h in mismatches:
            print("          %s: %r vs %r" % (slug, t, h))

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

print()
print("CHECK 8  sitemap.xml lists every registered entry and every content page")
sitemap_path = os.path.join(ROOT, "sitemap.xml")
if not os.path.exists(sitemap_path):
    bad("sitemap.xml is missing; run tools/build_sitemap.py")
else:
    sm = read(sitemap_path)
    missing_slugs = [p["slug"] for p in posts if ("post=" + p["slug"] + "<") not in sm]
    if missing_slugs:
        bad("sitemap.xml is stale, %d registered slug(s) absent: %s. Run tools/build_sitemap.py"
            % (len(missing_slugs), ", ".join(missing_slugs[:6])))
    else:
        ok("sitemap.xml covers all %d registered entries" % len(posts))
    missing_pages = []
    for name in sorted(os.listdir(ROOT)):
        if not name.endswith(".html") or name in ("404.html", "log.html", "lore.html"):
            continue
        if 'http-equiv="refresh"' in read(os.path.join(ROOT, name))[:600]:
            continue
        loc = "/" if name == "index.html" else "/" + name
        if (loc + "</loc>") not in sm:
            missing_pages.append(name)
    if missing_pages:
        bad("sitemap.xml missing page(s): %s" % ", ".join(missing_pages))
    else:
        ok("sitemap.xml covers every content page")
    if not os.path.exists(os.path.join(ROOT, "robots.txt")):
        warn("robots.txt is missing")

print()
print("CHECK 9  voice debt in registered entries (informational, see VOICE.md 2026-09-04)")
# The hard vetoes gate0 enforces on drafts, checked here on what is already
# live so the debt is visible on every run. Never fails the build: these
# entries were approved before the rule and only the owner retires them.
_fence = re.compile(r"```.*?```", re.S)
_inline = re.compile(r"`[^`\n]*`")
_rule = re.compile(r"^\s*\|?\s*:?-{3,}.*$", re.M)
debt = []
for entry in posts:
    md_path = os.path.normpath(os.path.join(ROOT, "hoards", entry["path"]))
    if not os.path.exists(md_path):
        continue
    text = read(md_path)
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4:]
    body = _rule.sub(" ", _inline.sub(" ", _fence.sub(" ", text)))
    dashes = len(re.findall(r"—|–|--", body))
    bangs = body.count("!")
    semis = body.count(";")
    if dashes or bangs or semis:
        debt.append("%s: %d dash, %d exclamation, %d semicolon" % (entry["slug"], dashes, bangs, semis))
if debt:
    warn("%d entr%s carry voice debt under the 2026-09-04 rules:" % (len(debt), "y" if len(debt) == 1 else "ies"))
    for d in debt:
        print("          %s" % d)
else:
    ok("no registered entry carries an em dash, exclamation mark or semicolon")

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
