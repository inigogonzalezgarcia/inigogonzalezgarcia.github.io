/* Motion with GSAP (self-hosted in assets/vendor/gsap): the home title line by line, and the journey stages
   with one sticky photo panel that follows the stage you are reading. Everything is readable without it:
   nothing is hidden by CSS that only this file can show (the title has a CSS fallback after 1.5 s). */
(function () {
  "use strict";
  var root = document.documentElement;
  function ready() { root.classList.remove("motion-wait"); }
  if (!window.gsap) { ready(); return; }
  var mm = gsap.matchMedia();

  /* ---------- home: the title rises line by line, only the first time it is painted */
  var h1 = document.querySelector(".hero h1");
  if (h1 && window.SplitText) {
    gsap.registerPlugin(SplitText);
    mm.add("(prefers-reduced-motion: no-preference)", function () {
      var target = h1.querySelector(root.lang === "es" ? ".es" : ".en") || h1;
      var split = SplitText.create(target, { type: "lines", mask: "lines" });
      gsap.from(split.lines, {
        yPercent: 100, duration: 0.9, ease: "expo.out", stagger: 0.08,
        onComplete: function () { split.revert(); }
      });
      ready();
      return function () { split.revert(); };
    });
  }
  ready();

  /* ---------- journey: on wide screens, the photos sit in one sticky panel and change with the stage */
  var stages = document.querySelector(".stages");
  if (stages && window.ScrollTrigger) {
    gsap.registerPlugin(ScrollTrigger);
    mm.add("(min-width: 960px) and (prefers-reduced-motion: no-preference)", function () {
      var arts = gsap.utils.toArray(".stages > .stage");
      if (arts.length < 2) return;
      var panel = document.createElement("div");
      panel.className = "scrolly-media";
      panel.style.gridRow = "1 / span " + arts.length;
      var items = arts.map(function (a) {
        var v = a.querySelector(".stage-visual");
        return { a: a, v: v, next: v ? v.nextSibling : null };
      }).filter(function (x) { return x.v; });
      items.forEach(function (x) { panel.appendChild(x.v); });
      stages.classList.add("is-scrolly");
      stages.insertBefore(panel, stages.firstChild);
      function show(i) {
        items.forEach(function (x, j) { x.v.classList.toggle("on", j === i); x.a.classList.toggle("on", j === i); });
      }
      show(0);
      var triggers = items.map(function (x, i) {
        return ScrollTrigger.create({
          trigger: x.a, start: "top 60%", end: "bottom 60%",
          onToggle: function (self) { if (self.isActive) show(i); }
        });
      });
      return function () {
        triggers.forEach(function (t) { t.kill(); });
        items.forEach(function (x) { x.a.insertBefore(x.v, x.next); x.v.classList.remove("on"); x.a.classList.remove("on"); });
        panel.remove();
        stages.classList.remove("is-scrolly");
      };
    });
  }
})();
