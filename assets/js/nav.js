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

  document.addEventListener("DOMContentLoaded", function () {
    const panel = document.getElementById("nav-projects-menu");
    if (!panel) return;
    const drop = panel.closest(".nav-drop");
    const nav = document.querySelector(".site-nav");
    const root = (nav && nav.getAttribute("data-root")) || "";

    fetch(root + "content/projects.json", { cache: "no-store" })
      .then(r => (r.ok ? r.json() : null))
      .then(function (data) {
        if (!data || !data.branches || !data.branches.length) return;
        const branches = data.branches;

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
