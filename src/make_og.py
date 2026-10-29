"""Social preview images (Open Graph, 1200x630) and the Apple touch icon. Called by build.py.

One card for the site and one per blog post, so a post shared on LinkedIn shows its own title.
Pure Pillow with the site font (assets/InterTight.woff), quantised to 16 colours (~15 KB per card).
The images in the repo are made by .github/workflows/og-images.yml (python src/make_og.py) on every push that touches
the posts, this script or the font; build.py only draws the ones that are missing, for local previews."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
INK, INK2, PAPER, MUTED, ACCENT = "#0e1a24", "#1b2b38", "#f2eee6", "#a9b3bb", "#c4672b"


def font(root, size, weight):
    f = ImageFont.truetype(str(root / "assets" / "InterTight.woff"), size)
    try:
        f.set_variation_by_axes([weight])
    except Exception:
        pass
    return f


def mark(d, x, y, s, stroke=PAPER, box=True):
    """The site logo (favicon.svg geometry, 34-unit grid) drawn at (x, y) with size s."""
    k = s / 34
    P = lambda a, b: (x + a * k, y + b * k)
    w = max(2, round(2.4 * k))
    if box:
        d.rectangle([P(1, 1), P(33, 33)], outline=stroke, width=max(1, round(1.5 * k)))
    for seg in [((10, 9), (10, 25)), ((17, 9), (17, 25)), ((17, 9), (24, 9)), ((17, 17), (22, 17)), ((24, 17), (24, 25)), ((24, 25), (17, 25))]:
        d.line([P(*seg[0]), P(*seg[1])], fill=stroke, width=w)
    r = 2.4 * k
    cx, cy = P(10, 9)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=ACCENT)


def wrap(d, text, f, maxw):
    lines, cur = [], ""
    for word in text.split():
        t = (cur + " " + word).strip()
        if d.textlength(t, font=f) <= maxw:
            cur = t
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def card(root, out, kicker, title, foot):
    im = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(im)
    d.rectangle([0, H - 10, W, H], fill=ACCENT)
    mark(d, 72, 64, 64)
    d.text((156, 70), "Iñigo González", font=font(root, 30, 700), fill=PAPER)
    d.text((156, 108), "IT Operations · Infrastructure", font=font(root, 22, 500), fill=MUTED)
    d.text((72, 210), kicker.upper(), font=font(root, 22, 700), fill=ACCENT, spacing=4)
    size = 64
    while True:
        ft = font(root, size, 700)
        lines = wrap(d, title, ft, W - 144)
        if len(lines) <= 3 or size <= 44:
            break
        size -= 4
    y = 252
    for ln in lines[:3]:
        d.text((72, y), ln, font=ft, fill=PAPER)
        y += int(size * 1.18)
    d.text((72, H - 76), foot, font=font(root, 22, 500), fill=MUTED)
    out.parent.mkdir(parents=True, exist_ok=True)
    im.quantize(colors=16, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(out, "PNG", optimize=True)


def touch_icon(root, out):
    im = Image.new("RGB", (180, 180), INK)
    mark(ImageDraw.Draw(im), 0, 0, 180, box=False)
    im.save(out, "PNG", optimize=True)


def build(site, posts, cats, only_missing=False):
    """site = repo root (fonts come from site/assets). Returns {post repo: image path relative to the site}."""
    todo = lambda f: not (only_missing and f.exists())
    f = site / "assets" / "og" / "site.png"
    if todo(f):
        card(site, f, "IT Site Leader · Madrid", "IT operations, Modern Workplace and infrastructure", "inigogonzalezgarcia.github.io")
    f = site / "assets" / "apple-touch-icon.png"
    if todo(f):
        touch_icon(site, f)
    out = {}
    for p in posts:
        rel = f"assets/og/{p['repo']}.png"
        if todo(site / rel):
            card(site, site / rel, "Blog · " + cats[p["cat"]][1], p["title_en"], f"inigogonzalezgarcia.github.io/blog · {p.get('label', p['n'])}")
        out[p["repo"]] = rel
    return out


if __name__ == "__main__":
    import sys
    src = Path(__file__).resolve().parent
    sys.path.insert(0, str(src))
    from posts import POSTS, CATS
    print(len(build(src.parent, POSTS, CATS)), "post cards + site card + touch icon")
