(function () {
  "use strict";
  var S = window.SITE || { cities: {}, hero: [] };
  var root = document.documentElement;
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var lang = function () { return root.lang === "en" ? "en" : "es"; };

  /* ---------- language ---------- */
  var T = {
    es: { title: "Iñigo González · Operaciones IT e Infraestructura", sending: "Enviando…", ok: "Gracias. Te responderé lo antes posible.", err: "No se ha podido enviar. Vuelve a intentarlo en unos minutos o escríbeme por LinkedIn.", missing: "Rellena nombre, un email válido y el mensaje.", captcha: "Completa la verificación antes de enviar.", nmissing: "Rellena tu nombre, un email válido y marca la casilla.", nok: "¡Hecho! Te enviaré las 33 ideas por email en las próximas 24 horas. Si no las ves, revisa Promociones y Spam.", nbrevo: "¡Casi está! Te he enviado un email para confirmar tu suscripción. En cuanto confirmes, te llegan las 33 ideas. Si no lo ves, revisa Promociones y Spam.", nconf: "¡Suscripción confirmada! Las 33 ideas van de camino a tu email.", bmissing: "Para reservar, elige una hora y marca las dos casillas.", bok: "¡Recibido! Te escribiré en menos de 24 horas laborables con el precio y el enlace de pago. La cita queda confirmada al recibir el pago.", week: "Semana del", none: "No quedan horas esta semana." },
    en: { title: "Iñigo González · IT Operations & Infrastructure", sending: "Sending…", ok: "Thank you. I'll get back to you soon.", err: "It couldn't be sent. Please try again in a few minutes or message me on LinkedIn.", missing: "Please fill in your name, a valid email and a message.", captcha: "Please complete the check before sending.", nmissing: "Please fill in your name and a valid email, and tick the box.", nok: "Done! I’ll email you the 33 ideas within 24 hours. If you can’t see them, check your Promotions and Spam folders.", nbrevo: "Almost there! I’ve sent you an email to confirm your subscription. Once you confirm, the 33 ideas will arrive. If you can’t see it, check Promotions and Spam.", nconf: "Subscription confirmed! The 33 ideas are on their way to your inbox.", bmissing: "To book, pick a time and tick both boxes.", bok: "Got it! I'll email you within 24 working hours with the price and the payment link. The appointment is confirmed once payment arrives.", week: "Week of", none: "No times left this week." }
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

  /* ---------- share (blog posts) ---------- */
  var shareMsg = $(".share-msg");
  function say(t) { if (!shareMsg) return; shareMsg.textContent = t; setTimeout(function () { if (shareMsg.textContent === t) shareMsg.textContent = ""; }, 3000); }
  $$("[data-copy]").forEach(function (b) {
    b.addEventListener("click", function () {
      var u = b.getAttribute("data-copy");
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(u).then(function () { say(b.getAttribute("data-copied")); }, function () { say(u); });
      } else say(u);
    });
  });
  if (navigator.share) $$("[data-share]").forEach(function (b) {
    b.hidden = false;
    b.addEventListener("click", function () {
      navigator.share({ title: b.getAttribute("data-title"), url: b.getAttribute("data-share") }).catch(function () {});
    });
  });

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

  /* ---------- about photos: one, or several that take turns ---------- */
  var AB = S.about ? [].concat(S.about) : [];
  if (AB.length && $("#aboutPhoto")) {
    var ap = $("#aboutPhoto"), cap = $(".cap", ap), ini = $(".initials", ap), abImgs = [], abDots = [], abI = 0, abTimer;
    if (ini) ini.remove();
    AB.forEach(function (p, i) {
      var im = new Image();
      im.src = p.src; im.alt = p.alt || "Iñigo González"; im.loading = i ? "lazy" : "eager"; im.decoding = "async";
      if (p.pos) im.style.objectPosition = p.pos;
      if (!i) im.className = "on"; else im.setAttribute("aria-hidden", "true");
      ap.insertBefore(im, cap); abImgs.push(im);
    });
    function abCap(p) {
      if (!cap) return;
      if (!p.caption_es) { cap.replaceChildren(); return; }
      var ce = document.createElement("span"), cn = document.createElement("span");
      ce.className = "es"; ce.textContent = p.caption_es;
      cn.className = "en"; cn.textContent = p.caption_en || p.caption_es;
      cap.replaceChildren(ce, cn);
    }
    function abShow(i) {
      abI = (i + abImgs.length) % abImgs.length;
      abImgs.forEach(function (im, j) { im.classList.toggle("on", j === abI); if (j === abI) im.removeAttribute("aria-hidden"); else im.setAttribute("aria-hidden", "true"); });
      abDots.forEach(function (d, j) { d.setAttribute("aria-current", j === abI ? "true" : "false"); });
      abCap(AB[abI]);
    }
    abCap(AB[0]);
    if (AB.length > 1) {
      var dots = document.createElement("div"); dots.className = "about-dots";
      AB.forEach(function (p, i) {
        var b = document.createElement("button"); b.type = "button";
        b.setAttribute("aria-label", (root.lang === "es" ? "Foto " : "Photo ") + (i + 1));
        b.addEventListener("click", function () { abShow(i); abAuto(); });
        dots.appendChild(b); abDots.push(b);
      });
      ap.appendChild(dots); abShow(0);
      var abAuto = function () {
        clearInterval(abTimer);
        if (!matchMedia("(prefers-reduced-motion: reduce)").matches) abTimer = setInterval(function () { abShow(abI + 1); }, 6000);
      };
      abAuto();
    }
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
  /* ---------- booking slots: Mon-Fri 10:30-18:00 Madrid, one week, from tomorrow; weekend/Friday -> next week ---------- */
  var slotsReset = function () {};
  (function () {
    var box = $("#slots"), chk = $("#f-book"), grid = $("#slotGrid"), hid = $("#f-slot"), wk = $("#slotWeek");
    if (!box || !chk || !grid) return;
    var TZ = "Europe/Madrid", MAD = (function () {
      var p = {}; new Intl.DateTimeFormat("en-GB", { timeZone: TZ, year: "numeric", month: "2-digit", day: "2-digit" }).formatToParts(new Date()).forEach(function (x) { p[x.type] = x.value; });
      return new Date(Date.UTC(+p.year, +p.month - 1, +p.day));
    })();
    function days() {
      var dow = MAD.getUTCDay(), out = [], start, i;
      // tomorrow onwards within this week (Mon..Fri); if none left, next Monday..Friday
      var tomorrow = new Date(MAD.getTime() + 864e5), td = tomorrow.getUTCDay();
      if (td >= 1 && td <= 5 && dow !== 0) { for (i = td; i <= 5; i++) out.push(new Date(MAD.getTime() + (i - dow) * 864e5)); }
      if (!out.length) { var add = ((8 - dow) % 7) || 7; start = new Date(MAD.getTime() + add * 864e5); for (i = 0; i < 5; i++) out.push(new Date(start.getTime() + i * 864e5)); }
      return out;
    }
    var TIMES = []; for (var m = 10 * 60 + 30; m <= 17 * 60 + 30; m += 30) TIMES.push(("0" + Math.floor(m / 60)).slice(-2) + ":" + ("0" + m % 60).slice(-2));
    function render() {
      var l = lang(), loc = l === "es" ? "es-ES" : "en-GB", ds = days();
      var fmtD = new Intl.DateTimeFormat(loc, { timeZone: "UTC", weekday: "long", day: "numeric", month: "long" });
      var monday = new Date(ds[0].getTime() - ((ds[0].getUTCDay() + 6) % 7) * 864e5);
      wk.textContent = T[l].week + " " + new Intl.DateTimeFormat(loc, { timeZone: "UTC", day: "numeric", month: "long", year: "numeric" }).format(monday);
      grid.innerHTML = "";
      ds.forEach(function (d) {
        var iso = d.toISOString().slice(0, 10), col = document.createElement("div"); col.className = "slot-day";
        var h = document.createElement("h4"); h.textContent = fmtD.format(d); col.appendChild(h);
        var row = document.createElement("div"); row.className = "slot-times";
        TIMES.forEach(function (tm) {
          var b = document.createElement("button"); b.type = "button"; b.className = "slot-btn"; b.setAttribute("role", "radio");
          var val = iso + " " + tm + " (Madrid)";
          b.setAttribute("aria-checked", hid.value === val ? "true" : "false"); b.textContent = tm; b.dataset.v = val;
          b.addEventListener("click", function () { hid.value = val; $$(".slot-btn", grid).forEach(function (x) { x.setAttribute("aria-checked", x === b ? "true" : "false"); }); });
          row.appendChild(b);
        });
        col.appendChild(row); grid.appendChild(col);
      });
    }
    function toggle() { box.hidden = !chk.checked; if (chk.checked) render(); }
    chk.addEventListener("change", toggle);
    var lb = $("#langBtn"); if (lb) lb.addEventListener("click", function () { if (!box.hidden) setTimeout(render, 0); });
    slotsReset = function () { hid.value = ""; box.hidden = true; };
    if (/[?&]reserva=1/.test(location.search) || location.hash === "#reservar") { chk.checked = true; toggle(); }
  })();

  /* ---------- contact form: "Report a problem" in SysAdmin Desks opens about.html?tema=sysadmindesks with the message started */
  (function () {
    var m = $("#f-msg");
    if (!m || m.value || !/[?&]tema=sysadmindesks(&|$)/.test(location.search)) return;
    m.value = document.documentElement.lang === "es"
      ? "SysAdmin Desks · Ticket: \nQué escribí o hice: \nQué esperaba que pasara: \n"
      : "SysAdmin Desks · Ticket: \nWhat I typed or did: \nWhat I expected to happen: \n";
  })();

  /* ---------- forms (contact + newsletter) ---------- */
  var tsBtns = [];
  window.tsOk = function () { tsBtns.forEach(function (b) { b.disabled = false; }); };
  window.tsExpired = function () { tsBtns.forEach(function (b) { b.disabled = true; }); };
  var emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  [["#contactForm", "#formStatus"], ["#newsForm", "#newsStatus"]].forEach(function (pair) {
    var form = $(pair[0]), status = $(pair[1]);
    if (!form) return;
    var news = form.getAttribute("data-kind") === "news";
    var brevo = form.getAttribute("data-provider") === "brevo";
    var ts = $(".cf-turnstile", form), sendBtn = $('button[type="submit"]', form);
    if (ts && sendBtn) { sendBtn.disabled = true; tsBtns.push(sendBtn); }
    if (news && /[?&]confirmado=1/.test(location.search)) {
      status.className = "form-status ok"; status.textContent = T[lang()].nconf;
      setTimeout(function () { form.scrollIntoView({ behavior: "smooth", block: "center" }); }, 300);
    }
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var l = lang(), d = new FormData(form), t = T[l];
      var done = function () { form.reset(); status.className = "form-status ok"; status.textContent = news ? (brevo ? t.nbrevo : t.nok) : t.ok; };
      var fail = function () { status.className = "form-status err"; status.textContent = t.err; };
      var reset = function () { if (ts && window.turnstile) { window.turnstile.reset(ts); sendBtn.disabled = true; } };
      if (news) {
        var nm = (d.get("NOMBRE") || "").trim(), em = (d.get("EMAIL") || "").trim(), ok = $("#n-consent", form);
        if (!nm || !emailRe.test(em) || !(ok && ok.checked)) { status.className = "form-status err"; status.textContent = t.nmissing; return; }
        if (ts && !d.get("cf-turnstile-response")) { status.className = "form-status err"; status.textContent = t.captcha; return; }
        if ((d.get("email_address_check") || "") !== "") { done(); return; }
        status.className = "form-status"; status.textContent = t.sending;
        if (brevo) {
          var body = new URLSearchParams();
          body.set("NOMBRE", nm); body.set("EMAIL", em); body.set("IDIOMA", l);
          body.set("email_address_check", ""); body.set("locale", l); body.set("html_type", "simple");
          fetch(form.action, { method: "POST", mode: "no-cors", body: body }).then(done, fail).then(reset);
        } else {
          d.set("lang", l);
          fetch(form.action, { method: "POST", body: d, headers: { Accept: "application/json" } })
            .then(function (r) { if (!r.ok) throw 0; done(); }).catch(fail).then(reset);
        }
        return;
      }
      var name = (d.get("name") || "").trim(), email = (d.get("email") || "").trim(), msg = (d.get("message") || "").trim();
      var booking = !!(d.get("reserva"));
      if (booking && !msg) { msg = "Reserva de la sesión inicial"; d.set("message", msg); }
      if (!name || !msg || !emailRe.test(email)) { status.className = "form-status err"; status.textContent = t.missing; return; }
      if (booking && (!d.get("hora_preferida") || !d.get("acepta_condiciones") || !d.get("ejecucion_anticipada"))) { status.className = "form-status err"; status.textContent = t.bmissing; return; }
      if (booking) { d.set("_subject", "Reserva sesión inicial · " + d.get("hora_preferida")); done = function () { form.reset(); slotsReset(); status.className = "form-status ok"; status.textContent = t.bok; }; }
      if (!S.formspree) { fail(); return; }
      if (ts && !d.get("cf-turnstile-response")) { status.className = "form-status err"; status.textContent = t.captcha; return; }
      status.className = "form-status"; status.textContent = t.sending;
      fetch(form.action, { method: "POST", body: d, headers: { Accept: "application/json" } })
        .then(function (r) { if (!r.ok) throw 0; done(); }).catch(fail).then(reset);
    });
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
  function home() { fitTo($$("#pins .pin", svg).map(function (g) { return g.getAttribute("data-id"); })); }
  $("#zReset").addEventListener("click", home);
  $("#zEu").addEventListener("click", function () { fitTo(["madrid", "lisbon", "london", "amsterdam", "istanbul", "milan", "bergen", "copenhagen", "frankfurt", "geneva"]); });
  function fitTo(ids, extra) {
    var xs = [], ys = [];
    ids.forEach(function (id) { var g = $('#pins .pin[data-id="' + id + '"]', svg); if (g) { xs.push(+g.getAttribute("data-x")); ys.push(+g.getAttribute("data-y")); } });
    (extra || []).forEach(function (p) { xs.push(p[0]); ys.push(p[1]); });
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
    var k = document.createElement("p"), h = document.createElement("h3"), d = document.createElement("p");
    k.className = "label muted"; k.textContent = kind;
    h.textContent = c["name_" + l];
    d.textContent = c[l];
    $("#cityCard").replaceChildren(k, h, d);
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
    var has = function (el, a) { return (" " + (el.getAttribute(a) || "") + " ").indexOf(" " + f + " ") >= 0; };
    $$("#pins .pin, #routes .route", svg).forEach(function (g) {
      var on = f === "all" || has(g, "data-s");
      g.style.opacity = on ? "" : "0.12";
      if (g.classList.contains("pin")) g.classList.toggle("hq", f !== "all" && has(g, "data-hq"));
    });
    // countries: dark where I worked, light where the company had clients or offices
    $$("path.land", svg).forEach(function (l) {
      var w = f === "all" ? l.hasAttribute("data-w") : has(l, "data-w");
      var p = !w && (f === "all" ? l.hasAttribute("data-p") : has(l, "data-p"));
      l.classList.toggle("hit", w);
      l.classList.toggle("pres", p);
    });
    if (f === "all") home();
    else {
      // a stage with company presence worldwide opens on the whole map, so every shaded country is in view
      var wide = $$("path.land", svg).some(function (l) { return has(l, "data-p"); }) ? [[60, 70], [960, 430]] : [];
      fitTo($$("#pins .pin", svg).filter(function (g) { return has(g, "data-s"); }).map(function (g) { return g.getAttribute("data-id"); }), wide);
    }
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
