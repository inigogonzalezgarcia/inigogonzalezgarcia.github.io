"""Language checks on the built site (one language per URL, with hreflang). Run by build.py after every build, or alone:
    python3 src/check_i18n.py          prints the counts, exits 1 on any problem
For every served HTML page: fixed <html lang> (es under /es/, en elsewhere); no element of the other language (class="es" on
English pages, class="en" on Spanish ones); canonical = its own URL, og:url and og:locale to match; the hreflang trio
(en, es, x-default = en) with absolute URLs, self-including and reciprocal (the other page exists and lists the same trio);
every internal href/src (relative or site-absolute) points to a file that exists; title and description present and in the
page's language (a simple word count), with a description that differs from the other language's; no SysAdmin Desks link
with the other language's ?lang=. Exempt: the 404 (one page, language from the URL) and redirect stubs (asesoria.html)."""
import json, pathlib, re, sys
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

SITE_URL = "https://inigogonzalezgarcia.github.io/"
SINGLE = {"404.html", "asesoria.html"}
SKIP_DIRS = ("src/", ".git/", ".github/", "node_modules/")

ES_W = {"de", "la", "el", "los", "las", "y", "en", "para", "con", "del", "que", "por", "una", "un", "tu", "tus", "sin", "cómo",
        "guías", "guía", "más", "años", "sobre", "qué", "mi", "mis", "lo", "se", "al", "esta", "página", "servicios", "política"}
EN_W = {"the", "and", "for", "with", "of", "to", "your", "how", "in", "on", "an", "guides", "guide", "without", "years", "about",
        "what", "my", "is", "it's", "this", "page", "services", "policy", "from", "by"}
NAME = re.compile(r"Iñigo González(?: García)?")

def lang_score(text):
    """(spanish, english) word hits; the owner's name does not count."""
    words = re.findall(r"[a-záéíóúüñ']+", NAME.sub(" ", text).lower())
    es = sum(w in ES_W for w in words) + len(re.findall(r"[áéíóúñ¿¡]", NAME.sub(" ", text).lower()))
    return es, sum(w in EN_W for w in words)

class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.html_attrs, self.title, self.in_title, self.meta, self.links, self.alts, self.urls, self.classes = {}, "", False, {}, {}, {}, [], {"es": 0, "en": 0}
        self.ld, self.in_ld = [], False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html": self.html_attrs = a
        if tag == "title": self.in_title = True
        if tag == "meta":
            k = a.get("name") or a.get("property")
            if k: self.meta[k] = a.get("content") or ""
        if tag == "link" and a.get("rel") == "canonical": self.links["canonical"] = a.get("href")
        if tag == "link" and a.get("rel") == "alternate" and a.get("hreflang"): self.alts[a["hreflang"]] = a.get("href")
        if tag == "script" and a.get("type") == "application/ld+json": self.in_ld = True
        for k in ("href", "src"):
            if a.get(k) is not None: self.urls.append((tag, k, a[k]))
        for c in (a.get("class") or "").split():
            if c in self.classes: self.classes[c] += 1
    def handle_startendtag(self, tag, attrs): self.handle_starttag(tag, attrs)
    def handle_endtag(self, tag):
        if tag == "title": self.in_title = False
        if tag == "script": self.in_ld = False
    def handle_data(self, d):
        if self.in_title: self.title += d
        if self.in_ld: self.ld.append(d)

def page_url(rel):
    """File path -> its public URL (index.html is served as its folder)."""
    return SITE_URL + (rel[:-len("index.html")] if rel.endswith("index.html") else rel)

def url_file(root, url):
    """Public URL of this site -> file path relative to the root, or None."""
    if not url.startswith(SITE_URL): return None
    p = url[len(SITE_URL):].split("#")[0].split("?")[0]
    return p + "index.html" if p == "" or p.endswith("/") else p

def resolves(root, rel, u):
    """Does an internal link from page `rel` point to an existing file? (None = not internal, not checked)"""
    if not u or u.startswith("#") or re.match(r"^(?:mailto|tel|data|javascript):", u, re.I): return None
    if re.match(r"^[a-z][a-z0-9+.-]*:|^//", u, re.I):
        if not u.startswith(SITE_URL): return None
        target = url_file(root, u)
    else:
        path = unquote(urlsplit(u).path)
        if path == "": return None
        base = "" if path.startswith("/") else rel.rsplit("/", 1)[0] + "/" if "/" in rel else ""
        parts = []
        for seg in (base + path.lstrip("/")).split("/"):
            if seg == "..":
                if not parts: return False  # above the site root
                parts.pop()
            elif seg not in ("", "."): parts.append(seg)
        target = "/".join(parts)
        if path.endswith("/") or path in (".", "..") or path.endswith("/.") or path.endswith("/..") or target == "": target = (target + "/" if target else "") + "index.html"
    f = root / target
    return f.is_file()

def check(root):
    root = pathlib.Path(root)
    problems, n = [], {"en": 0, "es": 0, "single": 0, "links": 0, "hreflang": 0}
    pages = {}
    for f in sorted(root.rglob("*.html")):
        rel = f.relative_to(root).as_posix()
        if rel.startswith(SKIP_DIRS) or "/vendor/" in rel: continue
        text = f.read_text()
        p = Page(); p.feed(text); p.close()
        p.raw_pair = '="[es]' in text  # an "[es]…[en]…" attribute that localize() did not resolve
        pages[rel] = p
    for rel, p in pages.items():
        bad = lambda m: problems.append(f"{rel}: {m}")
        # internal links, on every page
        for tag, k, u in p.urls:
            r = resolves(root, rel, u)
            if r is None: continue
            n["links"] += 1
            if not r: bad(f'<{tag} {k}="{u}"> does not resolve')
        if p.raw_pair: bad('unresolved "[es]…[en]…" attribute')
        if rel in SINGLE:
            n["single"] += 1; continue
        lang = "es" if rel.startswith("es/") else "en"
        other = "en" if lang == "es" else "es"
        n[lang] += 1
        if p.html_attrs.get("lang") != lang: bad(f'<html lang="{p.html_attrs.get("lang")}">, expected {lang}')
        if "data-i18n" in p.html_attrs: bad("data-i18n on a one-language page")
        if p.classes[other]: bad(f'{p.classes[other]} element(s) with class="{other}"')
        me = page_url(rel)
        if p.links.get("canonical") != me: bad(f"canonical {p.links.get('canonical')} != {me}")
        if p.meta.get("og:url", me) != me: bad(f"og:url {p.meta.get('og:url')} != {me}")
        if "og:locale" in p.meta and p.meta["og:locale"] != {"es": "es_ES", "en": "en_GB"}[lang]: bad(f"og:locale {p.meta['og:locale']}")
        # hreflang trio, self-including and reciprocal
        if set(p.alts) != {"en", "es", "x-default"}: bad(f"hreflang set {sorted(p.alts)}")
        else:
            n["hreflang"] += 1
            if p.alts[lang] != me: bad(f"hreflang {lang} {p.alts[lang]} is not this page")
            if p.alts["x-default"] != p.alts["en"]: bad("x-default != en")
            twin = url_file(root, p.alts[other])
            if twin not in pages: bad(f"hreflang {other} -> {p.alts[other]}: no such page")
            elif pages[twin].alts != p.alts: bad(f"hreflang not reciprocal with {twin}")
            elif (p.meta.get("description") or "") == (pages[twin].meta.get("description") or ""): bad("same description as the other language")
        # title and description in the page's language
        for what, text in (("title", p.title.strip()), ("description", (p.meta.get("description") or "").strip())):
            if not text: bad(f"empty {what}"); continue
            es, en = lang_score(text)
            if (lang == "es" and en > es) or (lang == "en" and es > en): bad(f"{what} looks {other}: {text[:80]}")
        for k in ("og:title", "og:image:alt"):
            if k in p.meta and p.meta[k] != p.title.strip(): bad(f"{k} differs from <title>")
        if "og:description" in p.meta and p.meta["og:description"] != p.meta.get("description"): bad("og:description differs from description")
        # JSON-LD: page language and own-language URLs
        for blob in p.ld:
            try: data = json.loads(blob)
            except ValueError: bad("JSON-LD does not parse"); continue
            for node in data.get("@graph", []):
                if "inLanguage" in node and isinstance(node["inLanguage"], str) and node["inLanguage"] != lang: bad(f"JSON-LD inLanguage {node['inLanguage']}")
                for k in ("url", "mainEntityOfPage"):
                    v = node.get(k)
                    if node.get("@type") not in ("Person", "WebSite") and isinstance(v, str) and v.startswith(SITE_URL) and (v.startswith(SITE_URL + "es/") != (lang == "es")):
                        bad(f"JSON-LD {k} {v} is in the other language")
                if node.get("@type") == "BreadcrumbList":
                    for it in node["itemListElement"]:
                        if it["item"].startswith(SITE_URL + "es/") != (lang == "es"): bad(f"breadcrumb {it['item']} is in the other language")
        # SysAdmin Desks links carry the page's language
        for tag, k, u in p.urls:
            if "sysadmindesksbyigg.pages.dev" in u and f"lang={other}" in u: bad(f"SysAdmin Desks link in the other language: {u}")
    summary = (f"i18n: {n['en']} en + {n['es']} es pages ({n['single']} single), {n['hreflang']} hreflang trios, "
               f"{n['links']} internal links resolved, {len(problems)} problem(s)")
    return {"problems": problems, "summary": summary, "counts": n}

if __name__ == "__main__":
    r = check(pathlib.Path(__file__).resolve().parent.parent)
    for pr in r["problems"]: print(" ", pr)
    print(r["summary"])
    sys.exit(1 if r["problems"] else 0)
