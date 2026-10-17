/* Cookie consent + Google Analytics 4 (loaded only after the visitor accepts). */
(function () {
  "use strict";
  var GA_ID = (window.SITE && window.SITE.ga4) || "";
  var KEY = "consent-v1";
  var MAX_AGE = 1000 * 60 * 60 * 24 * 180; // ask again after 6 months
  var root = document.documentElement;
  var L = function () { return root.lang === "en" ? "en" : "es"; };
  var T = {
    es: {
      kicker: "Iñigo González · Privacidad",
      title: "Tu privacidad, tu elección.",
      text: "Uso cookies de Google Analytics para saber cuánta gente visita la web y desde dónde, solo si las aceptas. Las necesarias para que la web funcione no requieren tu permiso. Puedes cambiar tu elección cuando quieras.",
      policy: "Política de cookies y privacidad ↗",
      reject: "Rechazar opcionales", config: "Configurar", accept: "Aceptar todo", save: "Guardar elección",
      necTitle: "Necesarias", necText: "Recuerdan tu idioma y tu elección sobre cookies. Siempre activas.",
      anTitle: "Analítica (Google Analytics)", anText: "Visitas, páginas vistas, país y de dónde llegas, de forma agregada. Cookies _ga y _ga_*, hasta 2 años.",
      always: "Siempre activas"
    },
    en: {
      kicker: "Iñigo González · Privacy",
      title: "Your privacy, your choice.",
      text: "I use Google Analytics cookies to know how many people visit this site and from where, only if you accept them. The ones needed for the site to work don't need your permission. You can change your choice at any time.",
      policy: "Cookie and privacy policy ↗",
      reject: "Reject optional", config: "Settings", accept: "Accept all", save: "Save choice",
      necTitle: "Necessary", necText: "They remember your language and your cookie choice. Always on.",
      anTitle: "Analytics (Google Analytics)", anText: "Visits, page views, country and where you came from, in aggregate. Cookies _ga and _ga_*, up to 2 years.",
      always: "Always on"
    }
  };

  function read() {
    try {
      var c = JSON.parse(localStorage.getItem(KEY) || "null");
      // only trust a well-formed record: { analytics: boolean, ts: number }
      if (c && typeof c === "object" && typeof c.analytics === "boolean" && typeof c.ts === "number" && Date.now() - c.ts < MAX_AGE) return { analytics: c.analytics, ts: c.ts };
    } catch (e) {}
    return null;
  }
  function write(analytics) {
    var c = { analytics: !!analytics, ts: Date.now() };
    try { localStorage.setItem(KEY, JSON.stringify(c)); } catch (e) {}
    return c;
  }

  /* ---- Google Analytics ---- */
  var gaLoaded = false;
  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = gtag;
  gtag("consent", "default", { ad_storage: "denied", ad_user_data: "denied", ad_personalization: "denied", analytics_storage: "denied" });
  function loadGA() {
    if (!GA_ID || gaLoaded) return;
    gaLoaded = true;
    gtag("consent", "update", { analytics_storage: "granted" });
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(GA_ID);
    document.head.appendChild(s);
    gtag("js", new Date());
    gtag("config", GA_ID, { allow_google_signals: false, allow_ad_personalization_signals: false });
  }
  function clearGA() {
    // remove _ga cookies set on this host if the visitor withdraws consent
    document.cookie.split(";").forEach(function (c) {
      var n = c.split("=")[0].trim();
      if (n.indexOf("_ga") === 0) {
        ["", location.hostname, "." + location.hostname].forEach(function (d) {
          document.cookie = n + "=; Max-Age=0; path=/" + (d ? "; domain=" + d : "");
        });
      }
    });
  }
  function apply(c) {
    if (c && c.analytics) loadGA();
    else { clearGA(); if (gaLoaded) location.reload(); }
  }

  /* ---- Banner ---- */
  var box;
  function render(showSettings) {
    var t = T[L()], c = read();
    if (!box) {
      box = document.createElement("div");
      box.className = "cc";
      box.setAttribute("role", "dialog");
      box.setAttribute("aria-live", "polite");
      document.body.appendChild(box);
    }
    var checked = c ? c.analytics : false;
    box.setAttribute("aria-label", t.title);
    // build the banner with DOM nodes (no innerHTML)
    var el = function (tag, cls, attrs) {
      var n = document.createElement(tag);
      if (cls) n.className = cls;
      if (attrs) Object.keys(attrs).forEach(function (k) { n.setAttribute(k, attrs[k]); });
      for (var i = 3; i < arguments.length; i++) n.appendChild(arguments[i]);
      return n;
    };
    var kids = [el("p", "label cc-k"), el("h2", "cc-t"), el("p", "cc-x"), el("a", "cc-p", { href: "privacidad.html" })];
    if (showSettings) {
      var cb = el("input", null, { type: "checkbox", id: "ccA" }); cb.checked = !!checked;
      kids.push(el("div", "cc-s", null,
        el("div", "cc-row", null, el("div", null, null, el("strong", "n1"), el("p", "d1")), el("span", "label cc-on a1")),
        el("div", "cc-row", null, el("div", null, null, el("strong", "n2"), el("p", "d2")), el("label", "cc-sw", null, cb, el("span")))));
      kids.push(el("div", "cc-b", null, el("button", "cc-btn", { "data-a": "save" })));
    } else {
      kids.push(el("div", "cc-b", null, el("button", "cc-btn", { "data-a": "reject" }), el("button", "cc-btn", { "data-a": "config" }), el("button", "cc-btn full", { "data-a": "accept" })));
    }
    box.replaceChildren.apply(box, kids);
    box.querySelector(".cc-k").textContent = t.kicker;
    box.querySelector(".cc-t").textContent = t.title;
    box.querySelector(".cc-x").textContent = t.text;
    box.querySelector(".cc-p").textContent = t.policy;
    if (showSettings) {
      box.querySelector(".n1").textContent = t.necTitle; box.querySelector(".d1").textContent = t.necText; box.querySelector(".a1").textContent = t.always;
      box.querySelector(".n2").textContent = t.anTitle; box.querySelector(".d2").textContent = t.anText;
      box.querySelector('[data-a="save"]').textContent = t.save;
    } else {
      box.querySelector('[data-a="reject"]').textContent = t.reject;
      box.querySelector('[data-a="config"]').textContent = t.config;
      box.querySelector('[data-a="accept"]').textContent = t.accept;
    }
    box.hidden = false;
    var first = box.querySelector("button"); if (first) setTimeout(function () { first.focus({ preventScroll: true }); }, 50);
  }
  function close() { if (box) box.hidden = true; }
  document.addEventListener("click", function (e) {
    var b = e.target.closest && e.target.closest(".cc [data-a]");
    if (b) {
      var a = b.getAttribute("data-a");
      if (a === "config") return render(true);
      var c = write(a === "accept" ? true : a === "save" ? box.querySelector("#ccA").checked : false);
      close(); apply(c);
      return;
    }
    var o = e.target.closest && e.target.closest("[data-cookie-settings]");
    if (o) { e.preventDefault(); render(true); }
  });
  // re-render in the new language if the visitor switches while the banner is open
  new MutationObserver(function () { if (box && !box.hidden) render(!!box.querySelector(".cc-s")); })
    .observe(root, { attributes: true, attributeFilter: ["lang"] });

  if (!GA_ID) return; // nothing optional to consent to yet
  var saved = read();
  if (saved) apply(saved);
  else if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", function () { render(false); });
  else render(false);
})();
