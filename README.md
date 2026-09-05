# mAxAdrAgoN

The lair. A static site on GitHub Pages for Mac McLean's projects, products, a world called Draega, and a dated record of what got built and what went wrong. No framework, no build step, no external dependency. Live at https://myrddhinmclean-hash.github.io/mAxAdrAgoN

Rewritten 2026-09-04 to match the repository as it is.

## Layout

    index.html              home, with the newest entries
    projects.html           every project, started or not, from content/projects.json
    products.html           the two things on sale, the one page allowed to sell
    radpodcast.html         Rivals and Destiny, recorded, unreleased
    map.html                the map of the future, from the moonshots corpus
    privacy.html terms.html refunds.html   required by the products page
    404.html                not found
    hoards/draega.html      the Draega archive list
    hoards/machine.html     the Machine archive list
    hoards/entry.html       renders one entry from content/ by ?post=<slug>
    hoards/odd.html         redirect stub only; Odd was removed 2026-09-04
    log.html lore.html      redirect stubs for old links
    content/posts.json      the entry index, newest first
    content/projects.json   the project register, grouped by branch
    content/draega/         Draega entries, one markdown file each
    content/machine/        Machine entries, one markdown file each
    content/*/*.editor-notes.md   sources and omissions for each entry; never rendered
    campaign/draega-canon/  mirror of the World Anvil canon, owner authored
    campaign/golden-sea/    the 24 module campaign kit, working material
    assets/css/style.css    dark ground, gold, emerald, electric blue
    assets/js/hoard.js      fetches markdown and renders it; lifts the leading H1
    tools/publish.py        step six of the loop: register, validate, commit, push, verify live
    tools/validate_site.py  nine checks; the last two were added 2026-09-04
    tools/build_sitemap.py  writes sitemap.xml from the pages and posts.json
    robots.txt sitemap.xml  added 2026-09-04
    feed.xml feed.json notes.xml   feeds, in progress
    GOVERNANCE.md           a pointer. The constitution lives in D:\mAxAdrAgoN-Brand\governance\GOVERNANCE.md
    CONTENT.md              the beginner guide to editing text and adding entries

`Storyline GG/` exists locally and is gitignored. It never publishes.

## Adding an entry

Mac names the subject. Find the real source or stop. Read `D:\mAxAdrAgoN-Brand\VOICE-PACK.md`, write the body once, put it in `content/<hoard>/<slug>.md` with `title`, `date`, `hoard` and `summary` in the frontmatter, and the editor notes beside it. Run the gate (`py -3 D:\mAxAdrAgoN-Brand\editor\src\gate0.py <file>`). Mac reads it and writes or approves the summary. Then, from this directory:

    py -3 tools\publish.py <slug>

It registers the entry, runs the validator, commits only the entry and the index, pushes, and checks the live index. `--dry-run` stops before the commit. Never `git add -A` in this repository.

## Validating without publishing

    py -3 tools\validate_site.py
    py -3 tools\build_sitemap.py

The validator refuses to push on a broken index, a missing file, editor material in a body, a missing legal notice, bad frontmatter, or a stale sitemap. It warns, and does not block, on entries that carry an em dash, exclamation mark or semicolon, which are banned for new writing under VOICE.md as of 2026-09-04.

## Rules that live here

Two hoards, Draega and Machine. No posting cadence, ever. Writing about a product outside the Products page is a teardown, never a pitch. The narrator was never in Draega. Anything countable is counted by code.

Dungeons & Dragons content on this site is unofficial fan content permitted under the Fan Content Policy and is not approved or endorsed by Wizards of the Coast.
