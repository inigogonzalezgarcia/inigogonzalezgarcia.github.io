/* Legal pages (privacy, legal notice, terms): the contact email, built here so the address is not in the HTML.
   The language button is a plain link to the page in the other language (boot.js remembers the choice). */
(function () {
  "use strict";
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
