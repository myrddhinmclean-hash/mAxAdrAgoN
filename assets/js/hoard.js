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

  filtered.sort((a, b) => new Date(b.date) - new Date(a.date));

  container.innerHTML = filtered
    .map(
      (entry) => `
      <a class="entry-item" href="entry.html?post=${encodeURIComponent(entry.slug)}">
        <div class="entry-meta">${entry.date} &middot; Hoard: ${entry.hoard.toUpperCase()}</div>
        <h3 class="entry-title">${entry.title}</h3>
        <p class="entry-excerpt">${entry.excerpt}</p>
      </a>
    `
    )
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
  if (metaEl) metaEl.textContent = `${post.date} · Hoard: ${post.hoard.toUpperCase()}`;
  if (backLinkEl) {
    backLinkEl.href = `${post.hoard}.html`;
    backLinkEl.textContent = `← Back to ${post.hoard.toUpperCase()} Hoard`;
  }
  document.title = `${post.title} — mAxAdrAgoN`;

  try {
    const res = await fetch(post.path);
    if (!res.ok) throw new Error("Fetch failed");
    const rawMd = await res.text();
    const parsed = parseMarkdown(rawMd);
    contentEl.innerHTML = parsed.html;
  } catch (err) {
    contentEl.innerHTML = `
      <p><em>${post.excerpt}</em></p>
      <div class="lair-intro" style="margin-top: 2rem;">
        <p><em>First hoard entry coming soon. Markdown source: <code>${post.path}</code></em></p>
      </div>
    `;
  }
}
