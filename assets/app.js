(function () {
  "use strict";
  var S = window.SITE || { cities: {}, hero: [] };
  var root = document.documentElement;
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var lang = function () { return root.lang === "en" ? "en" : "es"; };

  /* ---------- language ---------- */
  var T = {
    es: { title: "Iñigo González · Operaciones IT e Infraestructura", sending: "Enviando…", ok: "Gracias. Te responderé lo antes posible.", err: "No se ha podido enviar. Escríbeme a inigogonzalezgarcia@yahoo.es.", missing: "Rellena nombre, un email válido y el mensaje." },
    en: { title: "Iñigo González · IT Operations & Infrastructure", sending: "Sending…", ok: "Thank you. I'll get back to you soon.", err: "It couldn't be sent. Email me at inigogonzalezgarcia@yahoo.es.", missing: "Please fill in your name, a valid email and a message." }
  };
  function applyLang(l) {
    root.lang = l;
    document.title = root.getAttribute("data-title-" + l) || T[l].title;
    $$(".lang-btn [data-l]").forEach(function (s) { s.classList.toggle("on", s.getAttribute("data-l") === l); });
    try { localStorage.setItem("lang", l); } catch (e) {}
    renderCity(currentCity);
    setCaption();
  }
  $("#langBtn").addEventListener("click", function () { applyLang(lang() === "es" ? "en" : "es"); });

  /* ---------- header + menu ---------- */
  var header = $(".site-header");
  function onScroll() { header.classList.toggle("solid", window.scrollY > window.innerHeight * 0.6); }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
  var menu = $("#menu"), openBtn = $("#menuOpen");
  function setMenu(open) {
    menu.classList.toggle("open", open);
    menu.setAttribute("aria-hidden", open ? "false" : "true");
    openBtn.setAttribute("aria-expanded", open ? "true" : "false");
    document.body.style.overflow = open ? "hidden" : "";
    if (open) $("nav a", menu).focus(); else openBtn.focus();
  }
  openBtn.addEventListener("click", function () { setMenu(true); });
  $("#menuClose").addEventListener("click", function () { setMenu(false); });
  $$("a", menu).forEach(function (a) { a.addEventListener("click", function () { setMenu(false); }); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && menu.classList.contains("open")) setMenu(false); });

  /* ---------- hero slider ---------- */
  var slides = S.hero || [], idx = 0, timer;
  var media = $("#heroMedia"), hero = $(".hero");
  if (media) slides.forEach(function (s, i) {
    var img = new Image();
    img.src = s.src; img.alt = s.alt || ""; if (i === 0) img.className = "on";
    if (s.pos) img.style.objectPosition = s.pos;
    media.appendChild(img);
  });
  if (media && slides.length) hero.classList.add("has-photos");
  if (media && slides.length > 1) hero.classList.add("multi");
  function pad(n) { return (n < 10 ? "0" : "") + n; }
  function setCaption() {
    if (!media) return;
    var s = slides[idx];
    $("#heroCaption").textContent = s ? (s["caption_" + lang()] || "") : "";
    $("#slideCount").textContent = pad(idx + 1) + " / " + pad(Math.max(slides.length, 1));
  }
  function go(d) {
    if (slides.length < 2) return;
    var imgs = $$("img", media);
    imgs[idx].classList.remove("on");
    idx = (idx + d + slides.length) % slides.length;
    imgs[idx].classList.add("on");
    setCaption();
  }
  function auto() { clearInterval(timer); if (slides.length > 1 && !matchMedia("(prefers-reduced-motion: reduce)").matches) timer = setInterval(function () { go(1); }, 7000); }
  if (media) {
    $("#prevSlide").addEventListener("click", function () { go(-1); auto(); });
    $("#nextSlide").addEventListener("click", function () { go(1); auto(); });
    auto();
  }

  /* ---------- about photo ---------- */
  if (S.about && $("#aboutPhoto")) {
    var ap = $("#aboutPhoto"), im = new Image();
    im.src = S.about.src; im.alt = S.about.alt || "Iñigo González"; im.loading = "lazy";
    if (S.about.pos) im.style.objectPosition = S.about.pos;
    ap.insertBefore(im, ap.firstChild);
    var ini = $(".initials", ap); if (ini) ini.remove();
    var cap = $(".cap", ap);
    if (cap && S.about.caption_es) cap.innerHTML = '<span class="es"></span><span class="en"></span>', cap.firstChild.textContent = S.about.caption_es, cap.lastChild.textContent = S.about.caption_en || S.about.caption_es;
  }

  /* ---------- reveal + counters ---------- */
  function countUp(el) {
    var to = +el.getAttribute("data-count"), suf = el.getAttribute("data-suffix") || "";
    if (el.hasAttribute("data-plain") || matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    var t0 = null, dur = 1100;
    function step(t) {
      if (!t0) t0 = t;
      var p = Math.min((t - t0) / dur, 1), e = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(to * e) + suf;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add("in");
        var big = $(".big[data-count]", e.target); if (big) countUp(big);
        io.unobserve(e.target);
      });
    }, { rootMargin: "0px 0px -8% 0px" });
    $$(".reveal").forEach(function (el) { io.observe(el); });
  } else { $$(".reveal").forEach(function (el) { el.classList.add("in"); }); }

  function finish() {
  /* ---------- contact form ---------- */
  var form = $("#contactForm"), status = $("#formStatus");
  if (form) form.addEventListener("submit", function (e) {
    e.preventDefault();
    var l = lang(), d = new FormData(form);
    var name = (d.get("name") || "").trim(), email = (d.get("email") || "").trim(), msg = (d.get("message") || "").trim();
    if (!name || !msg || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) { status.className = "form-status err"; status.textContent = T[l].missing; return; }
    if (!S.formspree) {
      location.href = "mailto:inigogonzalezgarcia@yahoo.es?subject=" + encodeURIComponent("Web · " + name) + "&body=" + encodeURIComponent(msg + "\n\n" + name + " · " + email);
      return;
    }
    status.className = "form-status"; status.textContent = T[l].sending;
    fetch(form.action, { method: "POST", body: d, headers: { Accept: "application/json" } })
      .then(function (r) { if (!r.ok) throw 0; form.reset(); status.className = "form-status ok"; status.textContent = T[l].ok; })
      .catch(function () { status.className = "form-status err"; status.textContent = T[l].err; });
  });

  var y = $("#year"); if (y) y.textContent = new Date().getFullYear();
  applyLang(lang());
  }

  /* ---------- map ---------- */
  var svg = $("#map"), FULL = [0, 0, 1000, 487], HOME = [180, 20, 460, 259];
  var vb = HOME.slice(), currentCity = "madrid", filter = "all";
  if (!svg) { finish(); return; }
  function ratio() { var b = svg.getBoundingClientRect(); return b.width ? b.height / b.width : HOME[3] / HOME[2]; }
  function setVB(v) {
    var R = ratio(), w = Math.min(Math.max(v[2], 60), FULL[2], FULL[3] / R), h = w * R;
    var x = Math.min(Math.max(v[0], FULL[0]), FULL[2] - w), y = Math.min(Math.max(v[1], FULL[1]), Math.max(FULL[3] - h, 0));
    vb = [x, y, w, h];
    svg.setAttribute("viewBox", vb.map(function (n) { return n.toFixed(1); }).join(" "));
    var cw = svg.clientWidth || 900, px = Math.max(10, Math.min(13, cw / 70)) / 7 * (w / cw);
    $$("#pins .pin", svg).forEach(function (g) {
      var t = g.getAttribute("transform").replace(/ scale\([^)]*\)/, "");
      g.setAttribute("transform", t + " scale(" + px.toFixed(3) + ")");
    });
    svg.classList.toggle("zoomed", w < 300);
  }
  function zoom(f, cx, cy) {
    if (cx == null) { cx = vb[0] + vb[2] / 2; cy = vb[1] + vb[3] / 2; }
    var w = vb[2] * f, h = vb[3] * f;
    setVB([cx - (cx - vb[0]) * f, cy - (cy - vb[1]) * f, w, h]);
  }
  $("#zIn").addEventListener("click", function () { zoom(0.7); });
  $("#zOut").addEventListener("click", function () { zoom(1 / 0.7); });
  function home() { if (svg.getBoundingClientRect().width < 640) setVB([225, 20, 370, 278]); else setVB(HOME); }
  $("#zReset").addEventListener("click", home);
  $("#zEu").addEventListener("click", function () { fitTo(["madrid", "lisbon", "london", "amsterdam", "istanbul", "milan"]); });
  function fitTo(ids) {
    var xs = [], ys = [];
    ids.forEach(function (id) { var g = $('#pins .pin[data-id="' + id + '"]', svg); if (g) { xs.push(+g.getAttribute("data-x")); ys.push(+g.getAttribute("data-y")); } });
    if (!xs.length) return;
    var x0 = Math.min.apply(null, xs), x1 = Math.max.apply(null, xs), y0 = Math.min.apply(null, ys), y1 = Math.max.apply(null, ys);
    var r = ratio(), w = Math.max(x1 - x0 + 90, (y1 - y0 + 50) / r, 90), h = w * r;
    setVB([(x0 + x1) / 2 - w / 2, (y0 + y1) / 2 - h / 2, w, h]);
  }
  function toSvg(e) {
    var r = svg.getBoundingClientRect();
    return [vb[0] + (e.clientX - r.left) / r.width * vb[2], vb[1] + (e.clientY - r.top) / r.height * vb[3]];
  }
  var drag = null, moved = false;
  svg.addEventListener("pointerdown", function (e) {
    drag = { x: e.clientX, y: e.clientY, vb: vb.slice() }; moved = false;
  });
  window.addEventListener("pointermove", function (e) {
    if (!drag) return;
    var r = svg.getBoundingClientRect(), dx = e.clientX - drag.x, dy = e.clientY - drag.y;
    if (!moved && Math.abs(dx) + Math.abs(dy) < 5) return;
    if (!moved) { moved = true; svg.classList.add("dragging"); try { svg.setPointerCapture(e.pointerId); } catch (x) {} }
    setVB([drag.vb[0] - dx / r.width * drag.vb[2], drag.vb[1] - dy / r.height * drag.vb[3], drag.vb[2], drag.vb[3]]);
  });
  window.addEventListener("pointerup", function () { drag = null; svg.classList.remove("dragging"); });
  svg.addEventListener("wheel", function (e) {
    if (!e.ctrlKey && !e.metaKey) return; // keep normal page scroll
    e.preventDefault(); var p = toSvg(e); zoom(e.deltaY > 0 ? 1.15 : 0.87, p[0], p[1]);
  }, { passive: false });

  function renderCity(id) {
    var c = S.cities[id]; if (!c || !svg) return;
    currentCity = id;
    var l = lang();
    var kind = { base: { es: "Base", en: "Base" }, onsite: { es: "En persona", en: "In person" }, team: { es: "Equipo coordinado", en: "Team coordinated" } }[c.kind][l];
    $("#cityCard").innerHTML = '<p class="label muted"></p><h3></h3><p></p>';
    $("#cityCard .label").textContent = kind;
    $("#cityCard h3").textContent = c["name_" + l];
    $("#cityCard p:last-child").textContent = c[l];
    $$("#pins .pin", svg).forEach(function (g) { g.classList.toggle("sel", g.getAttribute("data-id") === id); });
  }
  $$("#pins .pin", svg).forEach(function (g) {
    var pick = function () { if (!moved) renderCity(g.getAttribute("data-id")); };
    g.addEventListener("click", pick);
    g.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); renderCity(g.getAttribute("data-id")); } });
  });
  function setFilter(f) {
    filter = f;
    $$(".map-tabs button").forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-f") === f ? "true" : "false"); });
    $$("#pins .pin, #routes .route", svg).forEach(function (g) {
      var on = f === "all" || (" " + g.getAttribute("data-s") + " ").indexOf(" " + f + " ") >= 0;
      g.style.opacity = on ? "" : "0.12";
    });
    if (f === "all") home();
    else fitTo($$("#pins .pin", svg).filter(function (g) { return (" " + g.getAttribute("data-s") + " ").indexOf(" " + f + " ") >= 0; }).map(function (g) { return g.getAttribute("data-id"); }));
    if (f !== "all") {
      var first = $$("#pins .pin", svg).filter(function (g) { return g.getAttribute("data-id") !== "madrid" && (" " + g.getAttribute("data-s") + " ").indexOf(" " + f + " ") >= 0; })[0];
      renderCity(first ? first.getAttribute("data-id") : "madrid");
    }
  }
  $$(".map-tabs button").forEach(function (b) { b.addEventListener("click", function () { setFilter(b.getAttribute("data-f")); }); });
  $$("[data-filter]").forEach(function (a) { a.addEventListener("click", function () { setFilter(a.getAttribute("data-filter")); }); });
  home();
  window.addEventListener("resize", function () { setVB(vb); });
  var f0 = null; try { f0 = new URLSearchParams(location.search).get("f"); } catch (e) {}
  if (f0 && /^s[1-5]$/.test(f0)) setFilter(f0);

  finish();
})();
