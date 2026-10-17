/* Legal pages (privacy, legal notice, terms): language button and the contact email, built here so the address is not in the HTML. */
(function () {
  "use strict";
  var r = document.documentElement, b = document.getElementById("langBtn");
  function set(l) {
    if (l !== "es" && l !== "en") l = "en";
    r.lang = l;
    var t = r.getAttribute("data-title-" + l); if (t) document.title = t;
    [].forEach.call(b.querySelectorAll("[data-l]"), function (s) { s.classList.toggle("on", s.getAttribute("data-l") === l); });
    try { localStorage.setItem("lang", l); } catch (e) {}
  }
  if (b) {
    b.addEventListener("click", function () { set(r.lang === "en" ? "es" : "en"); });
    set(r.lang === "en" ? "en" : "es");
  }
  // <span class="eml" data-e="base64 of the reversed address"> -> <a href="mailto:...">address</a> (or plain text with data-plain)
  [].forEach.call(document.querySelectorAll(".eml[data-e]"), function (el) {
    var m;
    try { m = atob(el.getAttribute("data-e")).split("").reverse().join(""); } catch (e) { return; }
    if (!/^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/.test(m)) return;
    if (el.hasAttribute("data-plain")) { el.replaceWith(document.createTextNode(m)); return; }
    var a = document.createElement("a");
    a.href = "mailto:" + m;
    a.textContent = m;
    el.replaceWith(a);
  });
})();
