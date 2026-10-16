"""Shared layout and page bodies. Imported by build.py."""
import html, re, datetime

SITE_URL = "https://inigogonzalezgarcia.github.io/"
MAIL = "inigogonzalezgarcia@yahoo.es"
LINKEDIN = "https://www.linkedin.com/in/igonzalez93"
GITHUB = "https://github.com/inigogonzalezgarcia"
LINKTREE = "https://linktr.ee/inigogonzalezgarcia"

def bi(es, en):
    return f'<span class="es">{es}</span><span class="en">{en}</span>'

NAV = [  # key, href (relative to site root), es, en
    ("journey", "journey.html", "Viaje", "Journey"),
    ("map", "index.html#mapa", "Mapa", "Map"),
    ("blog", "blog/", "Blog", "Blog"),
    ("about", "about.html", "Sobre mí", "About"),
    ("store", "store.html", "Store", "Store"),
    ("resources", "recursos.html", "Recursos", "Resources"),
    ("links", "links.html", "Links", "Links"),
]

LANG_JS = ("document.documentElement.classList.remove('no-js');(function(){var l;try{l=new URLSearchParams(location.search).get('lang')"
           "||localStorage.getItem('lang')}catch(e){}if(l!=='es'&&l!=='en'){l='en'}document.documentElement.lang=l})();")

LDJSON = ('{"@context":"https://schema.org","@type":"Person","name":"Iñigo González","jobTitle":"IT Site Leader, Senior Engineer",'
          '"address":{"@type":"PostalAddress","addressLocality":"Madrid","addressCountry":"ES"},"url":"https://inigogonzalezgarcia.github.io/",'
          '"sameAs":["https://www.linkedin.com/in/igonzalez93","https://github.com/inigogonzalezgarcia","https://linktr.ee/inigogonzalezgarcia"]}')

CUR = ' aria-current="page"'

def layout(*, R, path, active, title_en, title_es, desc, body, home=False, og_type="website"):
    t_en = html.escape(title_en); t_es = html.escape(title_es)
    nav_top = "".join(
        f'<a href="{R}{h}"{CUR if k == active else ""}>{bi(es, en)}</a>'
        for k, h, es, en in NAV)
    nav_menu = "".join(
        f'<a href="{R}{h}"><span class="label">{i:02d}</span>{bi(es, en)}</a>' for i, (k, h, es, en) in enumerate(NAV, 1))
    return f'''<!doctype html>
<html lang="en" class="no-js{' inner' if not home else ''}" data-title-en="{t_en}" data-title-es="{t_es}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t_en}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="author" content="Iñigo González">
<meta name="theme-color" content="#0e1a24">
<link rel="canonical" href="{SITE_URL}{path}">
<link rel="icon" href="{R}assets/favicon.svg" type="image/svg+xml">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{t_en}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{SITE_URL}{path}">
<link rel="preload" href="{R}assets/InterTight.woff" as="font" type="font/woff" crossorigin>
<link rel="stylesheet" href="{R}assets/style.css">
<script>{LANG_JS}</script>
{f'<script type="application/ld+json">{LDJSON}</script>' if home else ''}
</head>
<body>
<a class="skip" href="#main">{bi("Saltar al contenido", "Skip to content")}</a>

<header class="site-header" id="top">
  <div class="wrap">
    <a class="brand" href="{R}index.html" aria-label="Iñigo González">
      <svg class="brand-mark" viewBox="0 0 34 34" aria-hidden="true"><rect x="1" y="1" width="32" height="32" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 9v16M17 9v16M17 9h7M17 17h5M24 17v8h-7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="square"/><circle cx="10" cy="9" r="2.2" fill="#c4672b"/></svg>
      <span class="brand-name">Iñigo González<small>IT Operations · Infra</small></span>
    </a>
    <nav class="top-nav label" aria-label="Main">{nav_top}</nav>
    <div class="head-actions">
      <button class="menu-btn" id="menuOpen" aria-expanded="false" aria-controls="menu">{bi("Menú", "Menu")}</button>
      <span class="sep" aria-hidden="true"></span>
      <button class="lang-btn" id="langBtn" aria-label="Cambiar idioma / Change language"><span data-l="es">ES</span> · <span data-l="en">EN</span></button>
    </div>
  </div>
</header>

<div class="menu" id="menu" aria-hidden="true">
  <div class="menu-top">
    <span class="label">Iñigo González</span>
    <button class="menu-btn" id="menuClose">{bi("Cerrar ×", "Close ×")}</button>
  </div>
  <nav aria-label="Menu">{nav_menu}</nav>
  <div class="menu-foot label">
    <a href="{LINKEDIN}" rel="me noopener" target="_blank">LinkedIn ↗</a>
    <a href="{GITHUB}" rel="me noopener" target="_blank">GitHub ↗</a>
    <a href="{R}about.html#contacto">{bi("Contacto", "Contact")} →</a>
  </div>
</div>

<main id="main">
{body}
</main>

<footer>
  <div class="wrap">
    <span>© <span id="year">2026</span> Iñigo González · Madrid</span>
    <span>{bi("Hecha a mano y publicada con GitHub Pages ·", "Hand-built and published with GitHub Pages ·")} <a href="{GITHUB}/inigogonzalezgarcia.github.io">{bi("código", "source")}</a></span>
    <span><a href="{R}aviso-legal.html">{bi("Aviso legal", "Legal notice")}</a> · <a href="{R}privacidad.html">{bi("Privacidad y cookies", "Privacy and cookies")}</a> · <a href="{R}condiciones.html">{bi("Condiciones", "Terms")}</a> · <a href="{R}recursos.html">Newsletter</a> · <button class="linkbtn" type="button" data-cookie-settings>{bi("Preferencias de cookies", "Cookie settings")}</button></span>
    <a href="#top">{bi("Volver arriba ↑", "Back to top ↑")}</a>
  </div>
</footer>

<script src="{R}assets/data.js"></script>
<script src="{R}assets/app.js"></script>
<script src="{R}assets/consent.js"></script>
</body>
</html>
'''

def page_hero(kicker, h1, lede="", extra=""):
    lede_html = f'<p class="lede">{lede}</p>' if lede else ""
    return f'''<section class="page-hero">
  <div class="wrap">
    <p class="label kicker">{kicker}</p>
    <h1>{h1}</h1>
    {lede_html}{extra}
  </div>
</section>'''

# ---------------------------------------------------------------- blog helpers
MONTHS = {"es": ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sept", "oct", "nov", "dic"],
          "en": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]}

def fdate(iso):
    d = datetime.date.fromisoformat(iso)
    return bi(f"{d.day} {MONTHS['es'][d.month-1]} {d.year}", f"{d.day} {MONTHS['en'][d.month-1]} {d.year}")

def inline(s):
    s = html.escape(s)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", s)

def md(text):
    out, para, items = [], [], []
    def flush():
        if para: out.append("<p>" + inline(" ".join(para)) + "</p>"); para.clear()
        if items: out.append("<ul>" + "".join(f"<li>{inline(i)}</li>" for i in items) + "</ul>"); items.clear()
    for line in text.strip().split("\n"):
        line = line.rstrip()
        if not line: flush(); continue
        if line.startswith("## "): flush(); out.append(f"<h2>{inline(line[3:])}</h2>"); continue
        if line.startswith("- "):
            if para: flush()
            items.append(line[2:]); continue
        if items: flush()
        para.append(line)
    flush()
    return "\n".join(out)

def minutes(text):
    return max(2, round(len(text.split()) / 200))

def card(p, cats, R):
    c = cats[p["cat"]]
    return f'''      <article class="card reveal cat-{p["cat"]}">
        <a class="card-thumb" href="{R}blog/{p["repo"]}.html" tabindex="-1" aria-hidden="true"><span class="card-n">{p["n"]}</span><span class="card-cat label">{bi(*c)}</span></a>
        <p class="label card-meta">{bi(*c)} · {fdate(p["date"])}</p>
        <h3><a href="{R}blog/{p["repo"]}.html">{bi(html.escape(p["title_es"]), html.escape(p["title_en"]))}</a></h3>
        <p class="muted">{bi(html.escape(p["dek_es"]), html.escape(p["dek_en"]))}</p>
        <a class="arrow-link" href="{R}blog/{p["repo"]}.html">{bi("Leer el artículo", "Read the story")} →</a>
      </article>'''

def soon(kicker_es, kicker_en, R):
    return page_hero(bi(kicker_es, kicker_en),
                     bi("Aún lo estoy construyendo.", "Still building this."),
                     bi("Esta sección puede tardar unos días. Mientras tanto, el blog y el viaje ya están abiertos.",
                        "This section may take a few days. In the meantime, the blog and the journey are already open."),
                     f'''<div class="hero-ctas" style="margin-top:34px">
      <a class="btn" href="{R}blog/">{bi("Ir al blog", "Go to the blog")} →</a>
      <a class="arrow-link" href="{R}journey.html">{bi("Ver el viaje", "See the journey")}</a>
    </div>''').replace('class="page-hero"', 'class="page-hero soon"')
