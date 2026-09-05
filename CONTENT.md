# CONTENT GUIDE — How to Edit Your Site

This website is designed so that you can update any text without knowing how to code and without breaking the design.

---

## 1. Quick Map: Where is Everything?

| What You Want to Edit | File to Open | Notes |
|---|---|---|
| **Lair Home Page Intro** | `index.html` | Look for `<section class="lair-intro">` |
| **The Lore & Worldbuilding** | `lore.html` | Look for text inside the `<p>` and `<h2>` tags |
| **Hoard Descriptions** | `hoards/draega.html`<br>`hoards/machine.html` | Look for `<p class="hoard-desc">` |
| **Draega Hoard Entries** | `content/draega/` | Markdown files (`.md`) |
| **Machine Hoard Entries** | `content/machine/` | Markdown files (`.md`) |
| **List of All Entries** | `content/posts.json` | The directory index that lists all entries |

---

## 2. How to Edit Page Text (e.g. `index.html` or `lore.html`)

1. Open the file in any text editor (VS Code, Notepad, etc.).
2. Find the sentences you want to change between the tags like `<p>Your words here</p>`.
3. Type your new text.
4. Save the file.

> **Tip:** Do not delete the angle brackets `< >` around HTML tags. Just edit the text inside them.

---

## 3. How to Add a New Post / Hoard Entry

To add a new article or entry to any Hoard:

### Step 1: Create a Markdown file in `content/<hoard-name>/`
For example, inside `content/machine/`, create a file named `my-new-post.md`:

```markdown
---
title: "My New Post Title"
date: "2026-08-28"
hoard: "machine"
summary: "A short 1-2 sentence description that appears in the archive list."
---

# My New Post Title

Your main article text goes here. You can use standard Markdown:

- Use `## Subheadings` for sections
- Use `**bold**` or `*italic*`
- Use `> quotes` for callouts
- Use `- bullet points` for lists
```

### Step 2: Register it in `content/posts.json`
Open `content/posts.json` and add an entry for your post (newest at the top):

```json
[
  {
    "slug": "my-new-post",
    "hoard": "machine",
    "title": "My New Post Title",
    "date": "2026-08-28",
    "excerpt": "A short 1-2 sentence description that appears in the archive list.",
    "path": "../content/machine/my-new-post.md"
  },
  ...
]
```

That's it! The site will automatically display it in the archive list and render your markdown.

---

## 4. How to Add Images in the Future

In `lore.html` and other pages, you will see marked image slots:
```html
<div class="image-slot">
  ...
</div>
```

When you have an image ready:
1. Put the image file (e.g. `my-map.png`) into an `assets/images/` folder.
2. Replace the `<div class="image-slot">...</div>` block with:
```html
<img src="assets/images/my-map.png" alt="Map of Draega" style="width: 100%; border-radius: 6px; margin: 2rem 0;">
```
