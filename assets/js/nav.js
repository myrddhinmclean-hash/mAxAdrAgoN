/**
 * mAxAdrAgoN — navigation dropdown.
 * The five nav links are static HTML so crawlers see them without running JS.
 * This file only adds the branch list under Projects as an enhancement; if it
 * never runs, the Projects link still works and the register still has everything.
 */
(function () {
  function slug(s) {
    return "b-" + String(s).toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
  }

  document.addEventListener("DOMContentLoaded", function () {
    const menu = document.getElementById("nav-projects-menu");
    if (!menu) return;
    const nav = document.querySelector(".site-nav");
    const root = (nav && nav.getAttribute("data-root")) || "";

    fetch(root + "content/projects.json", { cache: "no-store" })
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (data) {
        if (!data || !data.branches) return;
        menu.innerHTML = data.branches.map(function (b) {
          const n = (b.projects || []).length;
          return '<a href="' + root + "projects.html#" + slug(b.branch) + '">' +
                 b.branch.replace(/&/g, "&amp;").replace(/</g, "&lt;") +
                 '<span class="nav-count">' + n + "</span></a>";
        }).join("");
        const drop = menu.closest(".nav-drop");
        if (drop) drop.classList.add("has-menu");
      })
      .catch(function () {});
  });
})();
