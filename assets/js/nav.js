/**
 * mAxAdrAgoN — Projects navigation panel.
 *
 * The five nav links are static HTML so crawlers see them without running JS.
 * This adds a click-opened panel under Projects: branches on the left, the
 * projects inside the focused branch on the right.
 *
 * Click, not hover. A hover menu closes when the pointer crosses a gap on the
 * way to the item it is aimed at, and it never opens at all on a touch screen.
 * If this file fails to load, the Projects link still works on its own.
 */
(function () {
  function slug(prefix, s) {
    return prefix + String(s).toLowerCase()
      .replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
  }

  // "Branch 24 and 2: Multi-agent systems" reads as "Multi-agent systems" in a
  // menu. The branch numbering is FutureMap bookkeeping, not a label.
  function label(branch) {
    const s = String(branch).replace(/^Branch[^:]*:\s*/i, "");
    return s.charAt(0).toUpperCase() + s.slice(1);
  }

  const esc = s => String(s == null ? "" : s)
    .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

  /**
   * The phone menu button.
   *
   * Built here rather than in the twelve page templates, so there is one copy
   * of it. The CSS hides .site-nav under 600px ONLY when this button exists,
   * which means a failure to load this file leaves the links visible and
   * wrapping, exactly as they were before. That is the safe direction to fail.
   */
  function mountNavToggle() {
    const nav = document.querySelector(".site-nav");
    const header = document.querySelector(".site-header");
    if (!nav || !header || document.querySelector(".nav-toggle")) return;

    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "nav-toggle";
    btn.setAttribute("aria-label", "Menu");
    btn.setAttribute("aria-expanded", "false");
    btn.setAttribute("aria-controls", "site-nav");
    btn.innerHTML = '<span class="nt-bars" aria-hidden="true"></span><span>Menu</span>';
    if (!nav.id) nav.id = "site-nav";

    function setOpen(open) {
      nav.classList.toggle("open", open);
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    }
    btn.addEventListener("click", function () {
      setOpen(!nav.classList.contains("open"));
    });
    // Following a link should not leave the menu hanging open behind the
    // next page in browsers that restore the DOM from bfcache.
    nav.addEventListener("click", function (e) {
      if (e.target.closest("a")) setOpen(false);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") setOpen(false);
    });
    // Rotating a phone to landscape can cross the 600px line with the menu
    // open, which would leave .open set on a nav that is now horizontal.
    window.addEventListener("resize", function () {
      if (window.innerWidth >= 600) setOpen(false);
    });

    header.insertBefore(btn, nav);
  }

  document.addEventListener("DOMContentLoaded", function () {
    mountNavToggle();

    const panel = document.getElementById("nav-projects-menu");
    if (!panel) return;
    const drop = panel.closest(".nav-drop");
    const nav = document.querySelector(".site-nav");
    const root = (nav && nav.getAttribute("data-root")) || "";

    fetch(root + "content/projects.json", { cache: "no-store" })
      .then(r => (r.ok ? r.json() : null))
      .then(function (data) {
        if (!data || !data.branches || !data.branches.length) return;

        // Parked work is not shown, matching projects.html. The exception is
        // anything flagged "perpetual": carrying the parked status because it
        // runs on its own lifecycle beside this one, not because it stopped.
        // A branch left with nothing in it drops out rather than showing an
        // empty column.
        const branches = data.branches.map(function (b) {
          const copy = {};
          for (const k in b) copy[k] = b[k];
          copy.projects = (b.projects || []).filter(function (p) {
            return p.status !== "parked" || p.perpetual;
          });
          return copy;
        }).filter(function (b) { return b.projects.length; });
        if (!branches.length) return;

        panel.innerHTML =
          '<div class="np-cols">' +
            '<div class="np-branches" role="tablist"></div>' +
            '<div class="np-projects"></div>' +
          "</div>" +
          '<a class="np-all" href="' + root + 'projects.html">See the whole register &rarr;</a>';

        const bCol = panel.querySelector(".np-branches");
        const pCol = panel.querySelector(".np-projects");

        bCol.innerHTML = branches.map(function (b, i) {
          return '<button type="button" class="np-branch" role="tab" data-i="' + i + '">' +
                 '<span>' + esc(label(b.branch)) + "</span>" +
                 '<span class="np-count">' + (b.projects || []).length + "</span></button>";
        }).join("");

        function show(i) {
          const b = branches[i];
          bCol.querySelectorAll(".np-branch").forEach(function (el) {
            el.classList.toggle("on", Number(el.dataset.i) === i);
          });
          const items = (b.projects || []).map(function (p) {
            return '<a class="np-proj" href="' + root + "projects.html#" + slug("p-", p.name) + '">' +
                   '<span class="np-dot s-' + esc(p.status) + '"></span>' +
                   '<span class="np-pname">' + esc(p.name) + "</span>" +
                   '<span class="np-status">' + esc(p.status) + "</span></a>";
          }).join("");
          pCol.innerHTML =
            '<a class="np-branchlink" href="' + root + "projects.html#" + slug("b-", b.branch) + '">' +
            esc(label(b.branch)) + "</a>" + items;
        }

        bCol.addEventListener("click", function (e) {
          const btn = e.target.closest(".np-branch");
          if (btn) show(Number(btn.dataset.i));
        });
        bCol.addEventListener("mouseover", function (e) {
          const btn = e.target.closest(".np-branch");
          if (btn) show(Number(btn.dataset.i));
        });
        show(0);

        // --- open / close -------------------------------------------------
        const toggle = document.createElement("button");
        toggle.type = "button";
        toggle.className = "np-toggle";
        toggle.setAttribute("aria-label", "Show project branches");
        toggle.setAttribute("aria-expanded", "false");
        toggle.innerHTML = "&#9662;";
        drop.insertBefore(toggle, panel);
        drop.classList.add("has-menu");

        function setOpen(open) {
          drop.classList.toggle("open", open);
          toggle.setAttribute("aria-expanded", open ? "true" : "false");
        }
        toggle.addEventListener("click", function (e) {
          e.preventDefault();
          e.stopPropagation();
          setOpen(!drop.classList.contains("open"));
        });
        document.addEventListener("click", function (e) {
          if (!drop.contains(e.target)) setOpen(false);
        });
        document.addEventListener("keydown", function (e) {
          if (e.key === "Escape") setOpen(false);
        });
        panel.addEventListener("click", function (e) {
          if (e.target.closest("a")) setOpen(false);
        });
      })
      .catch(function () {});
  });
})();
