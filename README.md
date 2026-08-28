# Maxadragon (mAxAdrAgoN) — The Lair

> A static personal brand website for **Maxadragon (mAxAdrAgoN)** — a dragon who hoards knowledge and interesting problems instead of gold, and translates complex things for people who are intimidated by them.

Zero build steps. Zero external dependencies. Zero frameworks. Deploys instantly to **GitHub Pages**.

---

## 🎨 Color Palette & Aesthetic

- **Base Theme**: Deep Charcoal / Obsidian (`#0c1110`, `#131a18`, `#1b2522`)
- **Dragon Gold**: `#d4a017` / `#f5c230`
- **Emerald Green**: `#10b981` / `#34d399` (Used for tags, borders, and Draega Hoard accents)
- **Electric Blue**: `#00d2ff` / `#38bdf8` (Used for interactive links, code highlights, and Machine Hoard accents)

---

## 📁 Repository Structure

```text
.
├── index.html              # "The Lair" (Intro & portals to the 3 Hoards)
├── lore.html               # "The Lore" (Worldbuilding & character lore)
├── CONTENT.md              # Beginner guide for editing text and adding posts
├── README.md               # Deployment and repository instructions
├── hoards/
│   ├── draega.html         # Draega Hoard archive list
│   ├── machine.html        # Machine Hoard archive list
│   ├── odd.html            # Odd Hoard archive list
│   └── entry.html          # Dynamic reader for Markdown posts
├── content/
│   ├── posts.json          # Index of all hoard entries
│   ├── draega/
│   │   └── the-scale-and-the-anvil.md # Sample post
│   ├── machine/
│   │   └── on-the-nature-of-cogs.md   # Sample post
│   └── odd/
│       └── a-collection-of-pebbles.md # Sample post
└── assets/
    ├── css/
    │   └── style.css       # Emerald, Electric Blue, & Dragon Gold theme
    └── js/
        └── hoard.js        # Minimal zero-dependency markdown fetcher & reader
```

---

## 🚀 How to Deploy to GitHub Pages (Beginner Guide)

Because this site uses pure static HTML/CSS/JS, there is **zero build setup** needed (no Node, no npm, no command-line build steps).

### Step 1: Create a GitHub Repository
1. Go to [github.com/new](https://github.com/new) and log into your GitHub account.
2. Under **Repository name**, enter a name (e.g. `maxadragon` or `maxadragon.github.io`).
3. Set the repository to **Public**.
4. Click **Create repository**.

### Step 2: Upload or Push the Files
#### Option A: Using the GitHub Website (Easiest)
1. On your new repository page, click **uploading an existing file**.
2. Drag and drop all the files and folders from this folder (`index.html`, `lore.html`, `CONTENT.md`, `hoards/`, `content/`, `assets/`, etc.).
3. Click **Commit changes**.

#### Option B: Using Git in Terminal
```bash
git init
git add .
git commit -m "Initial commit of mAxAdrAgoN lair"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

### Step 3: Turn On GitHub Pages
1. In your GitHub repository, click on **Settings** (tab near the top right).
2. On the left sidebar under *Code and automation*, click **Pages**.
3. Under **Build and deployment** > **Source**, select **Deploy from a branch**.
4. Under **Branch**:
   - Select `main` (or `master`)
   - Keep folder set to `/(root)`
5. Click **Save**.

### Step 4: Visit Your Live Site
In about 1 minute, refresh the **Settings > Pages** screen. GitHub will give you a live URL, like:
`https://your-username.github.io/your-repo-name/`

---

## ✏️ Editing Content
See [CONTENT.md](CONTENT.md) for a simple, non-coder guide on how to edit text and add new posts to the hoards.
