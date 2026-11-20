"""Short links for LinkedIn comments and posts.

Writes small redirect pages so a comment can say
  inigogonzalezgarcia.github.io/b/39      -> /blog/39-<slug>.html
  inigogonzalezgarcia.github.io/es/b/39   -> /es/blog/39-<slug>.html
  inigogonzalezgarcia.github.io/g/<short> -> /guias/<slug>.html
  inigogonzalezgarcia.github.io/es/g/<short> -> /es/guias/<slug>.html

Each redirect page copies the target's title, description and og:image, so
LinkedIn still shows the preview card, is noindex, and forwards with
utm_source=linkedin so the visit is attributed in Analytics. It carries the site's CSP and
referrer policy and forwards with <meta http-equiv="refresh"> only (no inline script), so build.py's security
check passes on it like on any other page.

The guide short names are kept in src/shortlinks.json and never change once
assigned (new guides are appended). Run after build.py:  python src/shortlinks.py
"""
import html
import json
import pathlib
import re

from pages import SEC_HEAD   # the same CSP and referrer policy as every other page

ROOT = pathlib.Path(__file__).parent
SITE = ROOT.parent
BASE = "https://inigogonzalezgarcia.github.io"
MAP_FILE = ROOT / "shortlinks.json"
UTM = "utm_source=linkedin&utm_medium=social&utm_campaign=shortlink"
STOP = {"de", "del", "y", "la", "el", "los", "las", "en", "un", "una", "a", "al",
        "con", "para", "por", "que", "se", "no", "su", "sus", "o", "e", "lo"}


def meta(page: str, prop: str) -> str:
    m = re.search(rf'<meta (?:property|name)="{re.escape(prop)}" content="([^"]*)"', page)
    return m.group(1) if m else ""


def title_of(page: str) -> str:
    m = re.search(r"<title>(.*?)</title>", page, re.S)
    return m.group(1).strip() if m else ""


def redirect_page(target: str, src_html: str, lang: str) -> str:
    url = f"{target}?{UTM}"
    t = meta(src_html, "og:title") or title_of(src_html)
    d = meta(src_html, "og:description") or meta(src_html, "description")
    img = meta(src_html, "og:image")
    esc = lambda s: html.escape(html.unescape(s), quote=True)
    img_tags = (f'<meta property="og:image" content="{esc(img)}">\n'
                '<meta property="og:image:width" content="1200">\n'
                '<meta property="og:image:height" content="630">\n'
                '<meta name="twitter:card" content="summary_large_image">\n') if img else ""
    label = "Ir a la página" if lang == "es" else "Go to the page"
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
{SEC_HEAD}
<title>{esc(t)}</title>
<meta name="robots" content="noindex,follow">
<link rel="canonical" href="{esc(target)}">
<meta name="description" content="{esc(d)}">
<meta property="og:type" content="article">
<meta property="og:url" content="{esc(target)}">
<meta property="og:title" content="{esc(t)}">
<meta property="og:description" content="{esc(d)}">
{img_tags}<meta http-equiv="refresh" content="0; url={esc(url)}">
</head>
<body><p><a href="{esc(url)}">{label}: {esc(t)}</a></p></body>
</html>
"""


def guide_short(slug: str, taken: set) -> str:
    words = [w for w in slug.split("-") if w and w not in STOP]
    for n in range(2, len(words) + 1):
        cand = "-".join(words[:n])
        if cand not in taken:
            return cand
    i = 2
    while f"{slug}-{i}" in taken:
        i += 1
    return f"{slug}-{i}"


def main():
    data = json.loads(MAP_FILE.read_text()) if MAP_FILE.exists() else {"guides": {}}
    guides = data.setdefault("guides", {})          # slug -> short
    taken = set(guides.values())
    written = 0

    # Blog: /b/NN and /es/b/NN
    for lang, src_dir, out_dir in (("en", "blog", "b"), ("es", "es/blog", "es/b")):
        for f in sorted((SITE / src_dir).glob("[0-9][0-9]-*.html")):
            num = f.name[:2]
            target = f"{BASE}/{src_dir}/{f.name}"
            out = SITE / out_dir / num / "index.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(redirect_page(target, f.read_text(encoding="utf-8"), lang), encoding="utf-8")
            written += 1

    # Guides: /g/<short> and /es/g/<short>
    for f in sorted((SITE / "guias").glob("*.html")):
        slug = f.stem
        if re.match(r"^(nivel|sector)-\d$", slug):
            continue
        if slug not in guides:
            guides[slug] = guide_short(slug, taken)
            taken.add(guides[slug])
        short = guides[slug]
        for lang, src_dir, out_dir in (("en", "guias", "g"), ("es", "es/guias", "es/g")):
            src = SITE / src_dir / f.name
            if not src.exists():
                continue
            out = SITE / out_dir / short / "index.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(redirect_page(f"{BASE}/{src_dir}/{f.name}", src.read_text(encoding="utf-8"), lang),
                           encoding="utf-8")
            written += 1

    MAP_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    print(f"{written} redirect pages, {len(guides)} guide short names")


if __name__ == "__main__":
    main()
