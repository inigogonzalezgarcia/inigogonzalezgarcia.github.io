"""Shared layout and page bodies. Imported by build.py."""
import html, re, datetime, json

SITE_URL = "https://inigogonzalezgarcia.github.io/"
MAIL = "inigogonzalezgarcia@outlook.es"
LINKEDIN = "https://www.linkedin.com/in/igonzalez93"
GITHUB = "https://github.com/inigogonzalezgarcia"
LINKTREE = "https://linktr.ee/inigogonzalezgarcia"

def bi(es, en):
    return f'<span class="es">{es}</span><span class="en">{en}</span>'

NAV = [  # key, href (relative to site root), es, en
    ("journey", "journey.html", "Viaje", "Journey"),
    ("about", "about.html", "Sobre mí", "About"),
    ("blog", "blog/", "Blog", "Blog"),
    ("guides", "guias.html", "Guías", "Guides"),
    ("store", "store.html", "Servicios", "Services"),
    ("resources", "recursos.html", "Recursos", "Resources"),
    ("links", "links.html", "Links", "Links"),
]

# Security headers that a static GitHub Pages site can set through <meta>. Shared by every page (pages.py, legal.py,
# build.py, and privacidad.html through its sec:start/sec:end markers). Every external origin below is used by the site:
# Google Analytics 4 (loaded by consent.js only after the visitor accepts), Cloudflare Turnstile (contact and newsletter
# forms), Formspree (contact form) and Brevo (newsletter form). GA4 needs the *.google-analytics.com wildcard because it
# sends hits to regional hosts (region1.google-analytics.com, ...), as Google documents for CSP.
CSP = "; ".join([
    "default-src 'self'",
    "script-src 'self' https://www.googletagmanager.com https://challenges.cloudflare.com",
    "style-src 'self'",
    "img-src 'self' https://*.google-analytics.com https://www.googletagmanager.com",
    "font-src 'self'",
    "connect-src 'self' https://formspree.io https://b6aad168.sibforms.com https://*.google-analytics.com https://*.analytics.google.com https://www.googletagmanager.com",
    "frame-src https://challenges.cloudflare.com",
    "form-action 'self' https://formspree.io https://b6aad168.sibforms.com",
    "object-src 'none'",
    "base-uri 'self'",
    "upgrade-insecure-requests",
])
SEC_HEAD = f'''<!-- Security: GitHub Pages cannot send custom HTTP headers, so only what works in <meta> is set here (CSP, referrer).
     Pending until the site moves behind Cloudflare (needs a custom domain), because they only work as real HTTP headers:
     CSP frame-ancestors / X-Frame-Options (clickjacking), X-Content-Type-Options, Permissions-Policy, HSTS,
     Cross-Origin-Opener-Policy, Cross-Origin-Embedder-Policy and Cross-Origin-Resource-Policy.
     No Subresource Integrity on gtag.js and Turnstile api.js: both are unversioned by design and change without notice
     (Cloudflare says not to pin Turnstile with SRI); the CSP limits them to their exact origins instead. -->
<meta http-equiv="Content-Security-Policy" content="{CSP}">
<meta name="referrer" content="strict-origin-when-cross-origin">'''

# Structured data (schema.org JSON-LD). One Person node, referenced by @id from every page, so search engines tie the
# blog posts, the site and the profiles (sameAs) to the same person. No employer names (GDPR choice for the site).
PERSON_ID = SITE_URL + "#person"
PERSON = {
    "@type": "Person", "@id": PERSON_ID, "name": "Iñigo González", "alternateName": "Iñigo González García",
    "jobTitle": "IT Site Leader, Senior Engineer", "url": SITE_URL, "image": SITE_URL + "assets/img/about.jpg",
    "description": "IT Site Leader in Madrid with 11+ years in IT operations, Modern Workplace and infrastructure.",
    "address": {"@type": "PostalAddress", "addressLocality": "Madrid", "addressCountry": "ES"},
    "knowsLanguage": ["es", "en"],
    "knowsAbout": ["IT operations", "Modern Workplace", "IT infrastructure", "Microsoft Intune", "Microsoft Entra ID",
                   "Active Directory", "Microsoft 365", "Jamf Pro", "Microsoft Teams Rooms", "Windows 11 migration",
                   "PowerShell", "Citrix", "VMware", "Microsoft Azure", "AWS", "Kubernetes"],
    "sameAs": [LINKEDIN, GITHUB, LINKTREE],
}
PERSON_REF = {"@type": "Person", "@id": PERSON_ID, "name": "Iñigo González", "url": SITE_URL}
WEBSITE = {"@type": "WebSite", "@id": SITE_URL + "#website", "url": SITE_URL, "name": "Iñigo González",
           "inLanguage": ["en", "es"], "publisher": PERSON_REF}

def crumbs(*items, lang="en"):
    """BreadcrumbList from (name, path) pairs, paths relative to SITE_URL. A name can be an (es, en) pair; on Spanish pages
    every path points to its /es/ mirror."""
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i, "name": (n if isinstance(n, str) else n[0] if lang == "es" else n[1]), "item": lurl(p, lang)}
        for i, (n, p) in enumerate(items, 1)]}

def ld_tag(nodes):
    if not nodes: return ""
    data = json.dumps({"@context": "https://schema.org", "@graph": nodes}, ensure_ascii=False, separators=(",", ":"))
    return '<script type="application/ld+json">' + data.replace("</", "<\\/") + "</script>"


# ---------------------------------------------------------------- languages: one language per URL
# Every indexable page exists twice: English at its historic URL and Spanish under /es/ with the same relative path.
# Pages are written in both languages at once (bi() and class="es"/"en" elements); write() in build.py renders one file
# per language, removing the other language's elements (only_lang) and, on Spanish pages, pointing shared files back to the
# root (es_links). Pages with no Spanish copy: the 404 (one page, language picked from the URL) and redirect stubs.
LANGS = ("en", "es")
NO_ES = {"404.html", "asesoria.html"}

def lpath(path, lang):
    """Site-relative path of a page in one language ("" is the home page)."""
    return ("es/" if lang == "es" else "") + path

def lurl(path, lang="en"):
    return SITE_URL + lpath(path, lang)

def pick(lang, es, en):
    return es if lang == "es" else en

def hreflang_tags(path):
    return "\n".join(f'<link rel="alternate" hreflang="{h}" href="{lurl(path, l)}">' for h, l in (("en", "en"), ("es", "es"), ("x-default", "en")))

def lang_btn(lang, R, path):
    """Language switch: a link to the same page in the other language (R: relative path to this language's root)."""
    other = "en" if lang == "es" else "es"
    href = R + ("../" if lang == "es" else "es/") + path
    on = lambda l: ' class="on"' if l == lang else ""
    label = "Read this page in English" if other == "en" else "Leer esta página en español"
    return (f'<a class="lang-btn" id="langBtn" href="{href}" hreflang="{other}" aria-label="{label}" lang="{other}">'
            f'<span data-l="es"{on("es")}>ES</span> · <span data-l="en"{on("en")}>EN</span></a>')

class Page(str):
    """A page in both languages. As a str it is the English page; .render(lang) gives either language."""

def page(render):
    p = Page(render("en"))
    p.render = render
    return p

from html.parser import HTMLParser as _HTMLParser
_VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}

class _LangStrip(_HTMLParser):
    """Finds the spans of every element whose class list contains `drop` (with all its children)."""
    def __init__(self, text, drop):
        super().__init__(convert_charrefs=False)
        self.text, self.drop, self.spans, self.tag, self.depth, self.start = text, drop, [], None, 0, 0
        self.lines = [0]
        for line in text.split("\n"): self.lines.append(self.lines[-1] + len(line) + 1)
    def _off(self):
        ln, col = self.getpos()
        return self.lines[ln - 1] + col
    def _hit(self, attrs):
        return self.drop in (dict(attrs).get("class") or "").split()
    def handle_starttag(self, tag, attrs):
        if self.tag:
            if tag == self.tag: self.depth += 1
            return
        if not self._hit(attrs): return
        o = self._off()
        if tag in _VOID: self.spans.append((o, o + len(self.get_starttag_text())))
        else: self.tag, self.depth, self.start = tag, 1, o
    def handle_startendtag(self, tag, attrs):
        if self.tag or not self._hit(attrs): return
        o = self._off()
        self.spans.append((o, o + len(self.get_starttag_text())))
    def handle_endtag(self, tag):
        if self.tag != tag: return
        self.depth -= 1
        if self.depth == 0:
            o = self._off()
            self.spans.append((self.start, self.text.index(">", o) + 1))
            self.tag = None

def only_lang(text, lang):
    """Remove every element marked with the other language's class (class="es" / class="en"), children included."""
    p = _LangStrip(text, "en" if lang == "es" else "es")
    p.feed(text); p.close()
    assert p.tag is None, f"unclosed <{p.tag}> with class {p.drop}"
    out, last = [], 0
    for a, b in p.spans:
        out.append(text[last:a]); last = b
    out.append(text[last:])
    return "".join(out)

_TAG = re.compile(r"<[a-zA-Z][^<>]*>")
_URL_ATTR = re.compile(r'(\s(?:href|src|action)=")([^"]*)(")')

def _es_url(u):
    if not u or re.match(r"^(?:[a-z][a-z0-9+.-]*:|/|#)", u, re.I): return u  # external, mailto:, data:, site-absolute, anchor
    path = re.split(r"[?#]", u, 1)[0]
    name = path.rsplit("/", 1)[-1]
    page_link = path == "" or path.endswith("/") or name in (".", "..") or (name.endswith(".html") and name not in NO_ES)
    return u if page_link else "../" + u

def es_links(text):
    """Spanish pages sit one folder deeper (/es/...). Links to pages stay inside the /es/ tree (same relative paths);
    links to shared files (assets, images, fonts, downloads) and to pages with no Spanish copy go back to the root."""
    head, sep, rest = text.partition("<body")
    fix = lambda m: _URL_ATTR.sub(lambda a: a.group(1) + _es_url(a.group(2)) + a.group(3), m.group(0))
    return _TAG.sub(fix, head) + sep + _TAG.sub(fix, rest)

_ATTR_PAIR = re.compile(r'="\[es\]([^"\[]*)\[en\]([^"]*)"')

def attr_pair(text, lang):
    """Attributes written as "[es]texto[en]text" (aria-labels in the sections) keep only the page's language."""
    return _ATTR_PAIR.sub(lambda m: '="' + (m.group(1) if lang == "es" else m.group(2)) + '"', text)

def localize(text, lang):
    """One language of a bilingual page: other-language elements and attribute halves removed; on Spanish pages,
    shared files at the root."""
    text = attr_pair(only_lang(text, lang), lang)
    return es_links(text) if lang == "es" else text

_TITLE_ATTRS = re.compile(r'<html lang="[a-z]+" data-title-es="([^"]*)" data-title-en="([^"]*)">')

def bilingual_static(text, path, desc_es, desc_en):
    """Pages with a hand-written head (legal shell, privacidad): fix the head for each language
    (<html lang>, title, description, self canonical, hreflang) and turn the language button into a link."""
    m = _TITLE_ATTRS.search(text)
    assert m, path
    t_es, t_en = m.group(1), m.group(2)
    def render(lang):
        s = text.replace(m.group(0), f'<html lang="{lang}">', 1)
        s = re.sub(r"<title>[^<]*</title>", f"<title>{pick(lang, t_es, t_en)}</title>", s, count=1)
        s = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{html.escape(pick(lang, desc_es, desc_en))}">', s, count=1)
        s = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{lurl(path, lang)}">\n' + hreflang_tags(path), s, count=1)
        s, n = re.subn(r'<button class="lang-btn" id="langBtn"[^>]*>.*?</button>', lang_btn(lang, "", path), s, count=1)
        assert n == 1, path
        return s
    return page(render)

_DANGLING = {"a", "al", "con", "de", "del", "el", "en", "la", "las", "lo", "los", "o", "para", "por", "que", "se", "sin", "su", "sus", "tu", "tus", "un", "una", "y", "e", "u", "the", "and", "of", "to"}

def desc_cut(text, n=158):
    """Description from a longer text: whole words up to n characters plus "…", never cutting inside parentheses
    or between two numbers. Texts that already fit (160 characters) are kept as they are."""
    text = " ".join(text.split())
    if len(text) <= 160: return text
    i = n + 1
    while True:
        i = text.rfind(" ", 0, i)
        if i <= 40: return text[:n].rstrip() + "…"
        head = text[:i]
        if head.count("(") > head.count(")") or (head[-1].isdigit() and text[i + 1:i + 2].isdigit()): continue
        if head.rsplit(" ", 1)[-1].lower() in _DANGLING: continue  # no "… de las…"
        head = head.rstrip(" ,;:·—–-")
        if head: return head + "…"

OG_DEFAULT = "assets/og/site.png"
# Google Search Console ownership (URL-prefix property). Public by design; must stay on the home page to stay verified.
GSC_VERIFY = "BPFmgcy9AT3FRIMzeQDYNz7wj-FolbKvJYaCzrT8nus"

CUR = ' aria-current="page"'

def gsap_tags(R, plugins):
    """GSAP only on the pages that use it (self-hosted, CSP script-src 'self'), then assets/motion.js."""
    if not plugins: return ""
    tags = [f'<script src="{R}assets/vendor/gsap/gsap.min.js"></script>'] + [f'<script src="{R}assets/vendor/gsap/{p}.min.js"></script>' for p in plugins]
    return "\n" + "\n".join(tags + [f'<script src="{R}assets/motion.js"></script>'])

def layout(*, single=False, **kw):
    """A page in both languages (see Page). single=True: one bilingual page whose language is picked from the URL
    (only the 404, which GitHub Pages serves at any missing URL)."""
    if single: return _layout(None, **kw)
    return page(lambda lang: _layout(lang, **kw))

def _layout(lang, *, R, path, active, title_en, title_es, desc, desc_es, body, home=False, og_type="website", og_image=OG_DEFAULT, ld=None, robots=None, gsap=()):
    """lang: "en" or "es" (one language per URL), or None for the single bilingual 404."""
    l = lang or "en"
    t_en = html.escape(title_en); t_es = html.escape(title_es)
    title = pick(l, t_es, t_en)
    d = html.escape(pick(l, desc_es, desc))
    if callable(ld): ld = ld(l)
    nav_top = "".join(
        f'<a href="{R}{h}"{CUR if k == active else ""}>{bi(es, en)}</a>'
        for k, h, es, en in NAV)
    nav_menu = "".join(
        f'<a href="{R}{h}"><span class="label">{i:02d}</span>{bi(es, en)}</a>' for i, (k, h, es, en) in enumerate(NAV, 1))
    cls = f'no-js{" inner" if not home else ""}{" motion-wait" if "SplitText" in gsap else ""}'
    html_tag = (f'<html lang="{lang}" class="{cls}">' if lang else
                f'<html lang="en" class="{cls}" data-i18n="auto" data-title-en="{t_en}" data-title-es="{t_es}">')
    canon = (f'<meta name="robots" content="{robots}">' if robots else
             f'<link rel="canonical" href="{lurl(path, l)}">\n{hreflang_tags(path)}')
    btn = lang_btn(lang, R, path) if lang else (f'<a class="lang-btn" id="langBtn" href="/es/" hreflang="es">'
                                                f'<span data-l="es">ES</span> · <span data-l="en" class="on">EN</span></a>')
    return f'''<!doctype html>
{html_tag}
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
{SEC_HEAD}
<title>{title}</title>
<meta name="description" content="{d}">
<meta name="author" content="Iñigo González">
{f'<meta name="google-site-verification" content="{GSC_VERIFY}">' + chr(10) if home else ''}<meta name="theme-color" content="#0e1a24">
{canon}
<link rel="icon" href="{R}assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{R}assets/apple-touch-icon.png">
<meta property="og:site_name" content="Iñigo González">
<meta property="og:locale" content="{pick(l, "es_ES", "en_GB")}">
<meta property="og:locale:alternate" content="{pick(l, "en_GB", "es_ES")}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{lurl(path, l)}">
<meta property="og:image" content="{SITE_URL}{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{title}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="{R}assets/InterTight.woff" as="font" type="font/woff" crossorigin>
<link rel="stylesheet" href="{R}assets/style.css">
<script src="{R}assets/boot.js"></script>
{ld_tag(ld)}
</head>
<body id="top">
<a class="skip" href="#main">{bi("Saltar al contenido", "Skip to content")}</a>

<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{R}index.html" aria-label="Iñigo González">
      <svg class="brand-mark" viewBox="0 0 34 34" aria-hidden="true"><rect x="1" y="1" width="32" height="32" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 9v16M17 9v16M17 9h7M17 17h5M24 17v8h-7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="square"/><circle cx="10" cy="9" r="2.2" fill="#c4672b"/></svg>
      <span class="brand-name">Iñigo González<small>IT Operations · Infra</small></span>
    </a>
    <nav class="top-nav label" aria-label="{pick(l, "Principal", "Main")}">{nav_top}</nav>
    <div class="head-actions">
      <button class="menu-btn" id="menuOpen" aria-expanded="false" aria-controls="menu">{bi("Menú", "Menu")}</button>
      <span class="sep" aria-hidden="true"></span>
      {btn}
    </div>
  </div>
</header>

<div class="menu" id="menu" aria-hidden="true">
  <div class="menu-top">
    <span class="label">Iñigo González</span>
    <button class="menu-btn" id="menuClose">{bi("Cerrar ×", "Close ×")}</button>
  </div>
  <nav aria-label="{pick(l, "Menú", "Menu")}">{nav_menu}</nav>
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
    <span><a href="{R}aviso-legal.html">{bi("Aviso legal", "Legal notice")}</a> · <a href="{R}privacidad.html">{bi("Privacidad y cookies", "Privacy and cookies")}</a> · <a href="{R}condiciones.html">{bi("Condiciones", "Terms")}</a> · <a href="{R}recursos.html">Newsletter</a> · {bi('SysAdmin Desks: <a href="https://sysadmindesksbyigg.pages.dev/about" target="_blank" rel="noopener noreferrer">qué es</a> · <a href="https://sysadmindesksbyigg.pages.dev/faq" target="_blank" rel="noopener noreferrer">preguntas frecuentes</a>', 'SysAdmin Desks: <a href="https://sysadmindesksbyigg.pages.dev/about#en" target="_blank" rel="noopener noreferrer">about</a> · <a href="https://sysadmindesksbyigg.pages.dev/faq#en" target="_blank" rel="noopener noreferrer">FAQ</a>')} · <button class="linkbtn" type="button" data-cookie-settings>{bi("Preferencias de cookies", "Cookie settings")}</button></span>
    <a href="#top">{bi("Volver arriba ↑", "Back to top ↑")}</a>
  </div>
</footer>

<script src="{R}assets/data.js"></script>
<script src="{R}assets/app.js"></script>
<script src="{R}assets/consent.js"></script>{gsap_tags(R, gsap)}
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
        <a class="card-thumb" href="{R}blog/{p["repo"]}.html" tabindex="-1" aria-hidden="true"><span class="card-n">{p.get("label", p["n"])}</span><span class="card-cat label">{bi(*c)}</span></a>
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
                     f'''<div class="hero-ctas u-mt34">
      <a class="btn" href="{R}blog/">{bi("Ir al blog", "Go to the blog")} →</a>
      <a class="arrow-link" href="{R}journey.html">{bi("Ver el viaje", "See the journey")}</a>
    </div>''').replace('class="page-hero"', 'class="page-hero soon"')

# ---------------------------------------------------------------- hand-written meta descriptions
# seo_overrides.py fills seo_desc / seo_desc_es for the pages with the most Search Console impressions. It runs here
# because build.py imports pages before it renders any post or guide (posts.py and guides.py import nothing).
import seo_overrides
seo_overrides.apply()
