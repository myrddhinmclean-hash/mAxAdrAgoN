/**
 * mAxAdrAgoN — Hoard Content Engine
 * Minimal vanilla JS helper to render Hoard lists and Markdown entries.
 * Zero external libraries or frameworks.
 */

// Simple lightweight markdown-to-HTML parser
function parseMarkdown(md) {
  if (!md) return "";

  let text = md.replace(/\r\n/g, "\n");

  // Frontmatter
  let metadata = {};
  if (text.startsWith("---")) {
    const endIdx = text.indexOf("---", 3);
    if (endIdx !== -1) {
      const front = text.substring(3, endIdx).trim();
      front.split("\n").forEach((line) => {
        const parts = line.split(":");
        if (parts.length >= 2) {
          const key = parts[0].trim();
          const val = parts.slice(1).join(":").trim().replace(/^["']|["']$/g, "");
          metadata[key] = val;
        }
      });
      text = text.substring(endIdx + 3).trim();
    }
  }

  // Permanent pipeline rule: strip trailing editor notes and preceding divider
  text = text.replace(/(?:\n\s*---\s*)?\n\s*\*?Tempted to invent but didn't:[\s\S]*$/i, "").trim();

  // The page already prints a title above the body. A leading H1 in the body
  // printed it a second time on every entry. Lift it out and hand it back, so
  // the page can use the fuller of the two headings and show it once.
  const leadH1 = text.match(/^#\s+(.+?)\s*$/m);
  if (leadH1 && text.trimStart().startsWith("#") && !text.trimStart().startsWith("##")) {
    metadata.bodyTitle = leadH1[1].trim();
    text = text.replace(/^#\s+.+?\s*$/m, "").trim();
  }

  // Code blocks
  const codeBlocks = [];
  text = text.replace(/```([a-z0-9_-]*)\n([\s\S]*?)```/g, (match, lang, code) => {
    const id = `___CODE_BLOCK_${codeBlocks.length}___`;
    const escaped = code
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
    codeBlocks.push(`<pre><code class="language-${lang}">${escaped}</code></pre>`);
    return id;
  });

  // Inline code
  text = text.replace(/`([^`]+)`/g, (match, code) => {
    const escaped = code
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
    return `<code>${escaped}</code>`;
  });

  // Headers
  text = text.replace(/^### (.*$)/gim, "<h3>$1</h3>");
  text = text.replace(/^## (.*$)/gim, "<h2>$1</h2>");
  text = text.replace(/^# (.*$)/gim, "<h1>$1</h1>");

  // Blockquotes
  text = text.replace(/^\> (.*$)/gim, "<blockquote><p>$1</p></blockquote>");

  // Bold & Italic
  text = text.replace(/\*\*\*(.*?)\*\*\*/g, "<strong><em>$1</em></strong>");
  text = text.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
  text = text.replace(/\*(.*?)\*/g, "<em>$1</em>");
  text = text.replace(/___(.*?)___/g, "<strong><em>$1</em></strong>");
  text = text.replace(/__(.*?)__/g, "<strong>$1</strong>");
  text = text.replace(/_(.*?)_/g, "<em>$1</em>");

  // Links
  text = text.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');

  // Unordered lists
  text = text.replace(/^\s*[\-\*]\s+(.*)$/gim, "<li>$1</li>");
  text = text.replace(/(<li>.*<\/li>(\n<li>.*<\/li>)*)/g, "<ul>$1</ul>");

  // Paragraphs
  const blocks = text.split(/\n\n+/);
  const htmlBlocks = blocks.map((block) => {
    block = block.trim();
    if (!block) return "";
    if (
      block.startsWith("<h") ||
      block.startsWith("<blockquote") ||
      block.startsWith("<ul") ||
      block.startsWith("<pre") ||
      block.startsWith("___CODE_BLOCK_")
    ) {
      return block;
    }
    return `<p>${block.replace(/\n/g, "<br>")}</p>`;
  });

  let html = htmlBlocks.join("\n\n");

  codeBlocks.forEach((block, idx) => {
    html = html.replace(`___CODE_BLOCK_${idx}___`, block);
    html = html.replace(`<p>___CODE_BLOCK_${idx}___</p>`, block);
  });

  return { html, metadata };
}

// Fallback posts
const FALLBACK_POSTS = [
  {
    slug: "the-scale-and-the-anvil",
    hoard: "draega",
    title: "The Draega Chronicle [Under Excavation]",
    date: "2026-08-28",
    excerpt: "The initial lore conversion for the Druid Temple and the world of Draega is currently being transcribed.",
    path: "../content/draega/the-scale-and-the-anvil.md"
  },
  {
    slug: "on-the-nature-of-cogs",
    hoard: "machine",
    title: "First Machine Teardown [Pending]",
    date: "2026-08-28",
    excerpt: "First system teardown and translation coming soon.",
    path: "../content/machine/on-the-nature-of-cogs.md"
  },
  {
    slug: "a-collection-of-pebbles",
    hoard: "odd",
    title: "First Curiosity [Pending]",
    date: "2026-08-28",
    excerpt: "First collection of contradictions and edge cases coming soon.",
    path: "../content/odd/a-collection-of-pebbles.md"
  }
];

// Load and list entries
async function loadHoardEntries(hoardName) {
  const container = document.getElementById("entries-container");
  if (!container) return;

  let posts = FALLBACK_POSTS;

  try {
    const res = await fetch("../content/posts.json");
    if (res.ok) {
      posts = await res.json();
    }
  } catch (err) {}

  const filtered = posts.filter((p) => p.hoard.toLowerCase() === hoardName.toLowerCase());

  if (filtered.length === 0) {
    container.innerHTML = `
      <div class="lair-intro">
        <p>This shelf of the hoard is currently quiet. No entries cataloged yet.</p>
      </div>
    `;
    return;
  }

  const byDate = (a, b) => new Date(b.date) - new Date(a.date);

  // Children nest under a parent slug. A place inside a place is not a
  // sibling of the place that contains it.
  const childrenOf = {};
  filtered.forEach((p) => {
    if (p.parent) {
      (childrenOf[p.parent] = childrenOf[p.parent] || []).push(p);
    }
  });

  const tops = filtered.filter((p) => !p.parent).sort(byDate);

  // Campaigns are separate bodies of work inside one hoard. Entries with no
  // campaign fall into a single unlabelled group rendered first.
  const groups = [];
  const seen = {};
  tops.forEach((p) => {
    const key = p.campaign || "";
    if (!(key in seen)) {
      seen[key] = groups.length;
      groups.push({ campaign: key, entries: [] });
    }
    groups[seen[key]].entries.push(p);
  });
  groups.sort((a, b) => (a.campaign === "" ? -1 : b.campaign === "" ? 1 : 0));

  const card = (entry, isChild) => `
      <a class="entry-item${isChild ? " entry-child" : ""}" href="entry.html?post=${encodeURIComponent(entry.slug)}">
        <div class="entry-meta">${entry.date} &middot; ${
          isChild ? "Within " + (entry.within || "this place") : entry.hoard.toUpperCase()
        }</div>
        <h3 class="entry-title">${entry.title}</h3>
        <p class="entry-excerpt">${entry.excerpt}</p>
      </a>`;

  container.innerHTML = groups
    .map((g) => {
      const head = g.campaign
        ? `<h2 class="campaign-head">${g.campaign}</h2>`
        : "";
      const body = g.entries
        .map((entry) => {
          const kids = (childrenOf[entry.slug] || []).sort(byDate);
          const nested = kids.length
            ? `<div class="entry-nest">${kids.map((k) => card(k, true)).join("")}</div>`
            : "";
          return card(entry, false) + nested;
        })
        .join("");
      return head + body;
    })
    .join("");
}

// Load individual entry
async function loadSingleEntry() {
  const titleEl = document.getElementById("entry-title");
  const metaEl = document.getElementById("entry-meta");
  const contentEl = document.getElementById("entry-content");
  const backLinkEl = document.getElementById("back-link");

  if (!contentEl) return;

  const urlParams = new URLSearchParams(window.location.search);
  const postSlug = urlParams.get("post");

  let posts = FALLBACK_POSTS;
  try {
    const res = await fetch("../content/posts.json");
    if (res.ok) {
      posts = await res.json();
    }
  } catch (e) {}

  const post = posts.find((p) => p.slug === postSlug) || posts[0];

  if (!post) {
    contentEl.innerHTML = "<p>Entry not found in the hoard.</p>";
    return;
  }

  if (titleEl) titleEl.textContent = post.title;
  if (metaEl) {
    let meta = `${post.date} · ${post.hoard.toUpperCase()}`;
    if (post.campaign) meta += ` · ${post.campaign}`;
    metaEl.textContent = meta;
  }
  if (backLinkEl) {
    // A nested entry goes back to the place that contains it, not to the archive.
    const parent = post.parent ? posts.find((p) => p.slug === post.parent) : null;
    if (parent) {
      backLinkEl.href = `entry.html?post=${encodeURIComponent(parent.slug)}`;
      backLinkEl.textContent = `← Back to ${parent.title}`;
    } else {
      backLinkEl.href = `${post.hoard}.html`;
      // The reader-facing name of each collection. The key stays "hoard" in
      // posts.json and in this file, because renaming it would break the live
      // /hoards/ URLs and three scripts; only the wording changed.
      const ARCHIVE_NAME = { draega: "The Draega Archive", machine: "The Machine Archive" };
      const label = ARCHIVE_NAME[post.hoard] || post.hoard.toUpperCase();
      backLinkEl.textContent = `← Back to ${label}`;
    }
  }
  document.title = `${post.title} — mAxAdrAgoN`;

  try {
    const res = await fetch(post.path);
    if (!res.ok) throw new Error("Fetch failed");
    const rawMd = await res.text();
    const parsed = parseMarkdown(rawMd);
    contentEl.innerHTML = parsed.html;

    // Prefer the body's own heading when it carries more than the index does
    // ("Shell Valley" in the index, "Shell Valley: The Heartwood Descent" in
    // the file). Either way it appears once.
    const bt = parsed.metadata && parsed.metadata.bodyTitle;
    if (bt && titleEl && bt.length > String(post.title).length) {
      titleEl.textContent = bt;
      document.title = bt + " — mAxAdrAgoN";
    }
  } catch (err) {
    contentEl.innerHTML = `
      <p><em>${post.excerpt}</em></p>
      <div class="lair-intro" style="margin-top: 2rem;">
        <p><em>First hoard entry coming soon. Markdown source: <code>${post.path}</code></em></p>
      </div>
    `;
  }
}
