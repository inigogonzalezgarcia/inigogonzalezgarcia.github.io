"""Build every page (index, journey, blog, about, store, resources, links, legal) and assets/data.js from src/. Run: python3 src/build.py"""
import json, html, math, pathlib

ROOT = pathlib.Path(__file__).parent
SITE_ROOT = ROOT.parent
SITE = SITE_ROOT
CONF = json.loads((ROOT / "config.json").read_text())

def bi(es, en):
    return f'<span class="es">{es}</span><span class="en">{en}</span>'

# ---------------------------------------------------------------- stages
STAGES = [
    dict(n="01", key="s1", company=("Consultora tecnológica", "Technology consultancy"), years="2015 — 2016",
         where="Madrid", sector=("Consultoría", "Consulting"),
         role=("IT Support Engineer", "IT Support Engineer"),
         p=("Mi primera etapa: soporte a empresas y comercios de clientes, administración de sistemas Windows y redes LAN. También TPV, PMS hotelero e IPTV para clientes de hostelería, y algo de diseño web y desarrollo a medida.",
            "My first stage: support for client businesses and shops, Windows administration and LAN networking. Also POS, hotel PMS and IPTV for hospitality clients, plus some web design and custom development."),
         p2=("Aquí aprendí lo básico que no se olvida: documentar, escalar a tiempo y no dejar a un usuario sin respuesta.",
             "This is where I learned the basics you never forget: document, escalate in time and never leave a user without an answer."),
         chips=["Windows", "LAN / WiFi", "SQL Server", "Office 365", "POS · ICG · HIOPOS", "CashDro"]),
    dict(n="02", key="s2", company=("Grupo de lujo internacional", "International luxury group"), years="2016 — 2018",
         where="París · Madrid · Lisboa", where_en="Paris · Madrid · Lisbon",
         sector=("Lujo · retail", "Luxury retail"),
         role=("IT Support / Systems Engineer", "IT Support / Systems Engineer"),
         p=("Soporte IT para oficinas y tiendas de marcas del grupo en España y Portugal, con base en Madrid y trabajo en las oficinas de París y Lisboa. Altas de usuarios (red, correo, AS400), licencias de Office 365 con el service desk central de París, Mac y Adobe, impresoras de tienda y una app Android de notas de gastos.",
            "IT support for offices and stores of group brands in Spain and Portugal, based in Madrid with work at the Paris and Lisbon offices. User provisioning (network, email, AS400), Office 365 licensing with the central service desk in Paris, Mac and Adobe, store printers and an Android expenses app."),
         p2=("Aquí empecé con Microsoft Graph, Azure AD Connect, Veeam y SharePoint, y a trabajar con procesos ITIL.",
             "This is where I started with Microsoft Graph, Azure AD Connect, Veeam and SharePoint, and with ITIL processes."),
         chips=["Active Directory", "Office 365", "Azure AD Connect", "Microsoft Graph", "Veeam", "SharePoint", "Cisco AnyConnect", "Poly"]),
    dict(n="03", key="s3", company=("Multinacional de software sanitario", "Healthcare software multinational"), years="2018 — 2019",
         where="Kansas City · Madrid · Bruselas · Gante", where_en="Kansas City · Madrid · Brussels · Ghent",
         sector=("Salud", "Healthcare"),
         role=("IT Systems Engineer", "IT Systems Engineer"),
         p=("Servidores Windows y Red Hat para historia clínica electrónica en proyectos de EMEA y Norteamérica: performance tuning, actualizaciones de hardware y sistema operativo, despliegue de monitorización con respuesta a alarmas y entornos de prueba.",
            "Windows and Red Hat servers for electronic health records on EMEA and North America projects: performance tuning, hardware and OS upgrades, monitoring rollout with alarm response, and test environments."),
         p2=("Entornos regulados donde una caída afecta a un hospital. Ahí entendí de verdad qué significa disponibilidad.",
             "Regulated environments where an outage hits a hospital. That is where I really understood what availability means."),
         chips=["Windows Server", "Red Hat", "Citrix", "EHR", "PHP", "Monitoring"]),
    dict(n="04", key="s4", company=("Grupo industrial alimentario", "Food manufacturing group"), years="2019 — 2021",
         where="Madrid · Milán · Estambul", where_en="Madrid · Milan · Istanbul",
         sector=("Industria", "Manufacturing"),
         role=("IT Manager", "IT Manager"),
         p=("Responsable de IT con un equipo repartido entre Madrid, Milán y Estambul. Reportaba al COO y al CTO y gestionaba el presupuesto de IT de Madrid y Milán. Infraestructura, proveedores y proyectos en tres países.",
            "Head of IT with a team spread across Madrid, Milan and Istanbul. I reported to the COO and CTO and managed the IT budget for Madrid and Milan. Infrastructure, vendors and projects in three countries."),
         p2=("Mi primera vez decidiendo en qué se gasta y por qué, no solo cómo se arregla.",
             "My first time deciding what to spend on and why, not just how to fix things."),
         chips=["VMware", "Citrix", "Veeam", "SQL", "VPN · LAN/WAN/WiFi", "JAMF Pro", "SAP support", "IT budget"]),
    dict(n="05", key="s5", company=("Servicios financieros", "Financial services"), years=("2021 — hoy", "2021 — now"), live=True,
         where="Madrid · Londres · París · Ámsterdam · Copenhague · Fráncfort · Bergen · Ginebra · Dubái · Nueva York · Singapur · Tokio · Manila", where_en="Madrid · London · Paris · Amsterdam · Copenhagen · Frankfurt · Bergen · Geneva · Dubai · New York · Singapore · Tokyo · Manila",
         sector=("Finanzas", "Finance"),
         role=("IT Site Leader, Senior Engineer · Infra & EUC", "IT Site Leader, Senior Engineer · Infra & EUC"),
         p=("Llevo la sede de Madrid: operaciones IT para trading floor y usuarios corporativos en un entorno regulado. Intune, Autopilot, Defender y Entra ID con Conditional Access; SCCM con OSD y empaquetado; redes Cisco, salas de comunicaciones y racks; pruebas de DR/BCP y proveedores. Lideré la migración a Windows 11 de las oficinas de Madrid.",
            "I run the Madrid site: IT operations for trading floor and corporate users in a regulated environment. Intune, Autopilot, Defender and Entra ID with Conditional Access; SCCM with OSD and packaging; Cisco networks, comms rooms and racks; DR/BCP testing and vendors. I led the Windows 11 migration of the Madrid offices."),
         p2=("También construí mi propia consola de operaciones IT para automatizar el día a día, y desde 2023 formo a los becarios de IT y llevo el onboarding de nuevos empleados.",
             "I also built my own IT operations console to automate day-to-day work, and since 2023 I have trained IT interns and run new-joiner onboarding."),
         chips=["Intune", "Autopilot", "Entra ID", "SCCM / OSD", "BitLocker", "Cisco", "Teams Rooms", "PowerShell", "SolarWinds", "Grafana"]),
]

def stage_html(s):
    yrs = bi(*s["years"]) if isinstance(s["years"], tuple) else s["years"]
    where = bi(s["where"], s.get("where_en", s["where"]))
    live = f'<span class="live label"><span class="dot"></span>{bi("En curso", "Current")}</span>' if s.get("live") else ""
    img = CONF["stage_photos"].get(s["key"])
    visual_img = (f'<img src="{img["src"]}" alt="{html.escape(img.get("alt",""))}" loading="lazy" width="600" height="450">'
                  f'<span class="photo-place label">{bi(html.escape(img["place_es"]), html.escape(img["place_en"]))}</span>') if img else ""
    chips = "".join(f"<li>{html.escape(c)}</li>" for c in s["chips"])
    return f'''      <article class="stage reveal" id="etapa-{s["key"]}">
        <div class="stage-visual{' photo' if img else ''}">
          {visual_img}
          <div class="years"><span>{yrs}</span><span class="tag">{bi(*s["sector"])}</span></div>
          {'' if img else f'<div class="stage-n" aria-hidden="true">{s["n"]}</div>'}
          {'' if img else f'<div class="years"><span>{where}</span></div>'}
        </div>
        <div class="stage-body">
          <p class="label">{bi("Etapa", "Stage")} {s["n"]} · {yrs}{live}</p>
          <h3>{bi(*s["company"])}</h3>
          <p class="role">{bi(*s["role"])}</p>
          <p>{bi(*s["p"])}</p>
          <p class="muted">{bi(*s["p2"])}</p>
          <ul class="chips">{chips}</ul>
          <a class="arrow-link" href="index.html?f={s["key"]}#mapa">{bi("Ver en el mapa", "See on the map")} →</a>
        </div>
      </article>'''


# ---------------------------------------------------------------- map
M = json.loads((ROOT / "map.json").read_text())
# countries per stage: WORKED = where I worked (dark), PRESENCE = where the company had clients or offices (light).
# Stage 3 presence: Cerner subsidiaries in its 2019 10-K (Exhibit 21) plus its Middle East clients (Saudi Arabia, Qatar).
WORKED = {
    "s1": {"ESP"},
    "s2": {"FRA", "ESP", "PRT"},
    "s3": {"USA", "ESP", "BEL"},
    "s4": {"ITA", "ESP", "TUR"},
    "s5": {"GBR", "ESP", "FRA", "NLD", "DNK", "DEU", "NOR", "CHE", "ARE", "USA", "SGP", "JPN", "PHL"},
}
PRESENCE = {
    "s3": {"AUS", "AUT", "BEL", "BRA", "CAN", "CHL", "EGY", "FIN", "FRA", "DEU", "IND", "IRL", "MYS", "MEX", "NLD",
           "NOR", "PRT", "ROU", "ESP", "SWE", "ARE", "GBR", "USA", "SAU", "QAT"},
}
def _stages(iso, table):
    return " ".join(k for k in sorted(table) if iso in table[k])
CITIES = json.loads((ROOT / "cities.json").read_text())
def rel(d):
    """Absolute M/L path -> relative path in tenths of a pixel (about half the size)."""
    out = []
    for ring in d.split("Z"):
        if not ring:
            continue
        pts = [tuple(round(float(v) * 10) for v in p.split(",")) for p in ring[1:].split("L")]
        x0, y0 = pts[0]
        s, px, py = [], x0, y0
        for x, y in pts[1:]:
            dx, dy = x - px, y - py
            if dx or dy:
                s.append(f"{dx/10:g}{'' if dy < 0 else ','}{dy/10:g}")
            px, py = x, y
        if s:
            out.append(f"M{x0/10:g},{y0/10:g}l" + " ".join(s) + "z")
    return "".join(out)


def _land(iso, d):
    w, pr = _stages(iso, WORKED), _stages(iso, PRESENCE)
    cls = "land" + (" hit" if w else " pres" if pr else "")
    attrs = (f' data-w="{w}"' if w else "") + (f' data-p="{pr}"' if pr else "")
    return f'<path class="{cls}"{attrs} d="{rel(d)}"/>'
paths = "".join(_land(iso, d) for iso, d in M["paths"])
mx, my = M["cities"]["madrid"]
routes, pins = [], []
for c in CITIES:
    x, y = M["cities"][c["id"]]
    if c["id"] != "madrid":
        # gentle arc from Madrid
        dx, dy = x - mx, y - my
        dist = math.hypot(dx, dy)
        cx, cy = (mx + x) / 2 - dy * 0.18, (my + y) / 2 - abs(dx) * 0.18 - dist * 0.05
        routes.append(f'<path class="route{" team" if c["kind"]=="team" else ""}" data-s="{" ".join(c["stages"])}" d="M{mx:.1f},{my:.1f}Q{cx:.1f},{cy:.1f} {x:.1f},{y:.1f}"/>')
    lx = 6 if c.get("label", "r") == "r" else -6
    anchor = "start" if lx > 0 else "end"
    ly = c.get("ly", 3)
    hq = f' data-hq="{" ".join(c["hq"])}"' if c.get("hq") else ""
    major = " major" if c["id"] in ("madrid", "kansas", "istanbul") else ""
    pins.append(f'<g class="pin {c["kind"]}{major}" data-id="{c["id"]}" data-s="{" ".join(c["stages"])}"{hq} data-x="{x:.1f}" data-y="{y:.1f}" transform="translate({x:.1f} {y:.1f})" tabindex="0" role="button" aria-label="{html.escape(c["name_es"])} / {html.escape(c["name_en"])}"><circle class="halo" r="7"/><circle class="core" r="3"/><text class="es" x="{lx}" y="{ly}" text-anchor="{anchor}">{html.escape(c["name_es"])}</text><text class="en" x="{lx}" y="{ly}" text-anchor="{anchor}">{html.escape(c["name_en"])}</text></g>')
MAP = f'''      <svg id="map" viewBox="0 0 1000 487" role="img" aria-label="Mapa / Map">
        <g id="mapLayer">{paths}<g id="routes">{"".join(routes)}</g><g id="pins">{"".join(pins)}</g></g>
      </svg>'''


# ---------------------------------------------------------------- pages
import sys
sys.path.insert(0, str(ROOT))
from pages import PERSON, PERSON_ID, PERSON_REF, WEBSITE, SITE_URL, crumbs, layout, page_hero, card, md, minutes, fdate, soon, bi as bi2, MAIL, LINKEDIN, GITHUB, LINKTREE, SEC_HEAD
from posts import POSTS, CATS
import make_og
OG = make_og.build(SITE, POSTS, CATS, only_missing=True)  # social preview cards, one per post (CI makes the real ones)

SEC = {p.stem: p.read_text() for p in (ROOT / "sections").glob("*.html")}
FORM = f'https://formspree.io/f/{CONF["formspree_id"]}' if CONF.get("formspree_id") else f"mailto:{MAIL}"
TS = CONF.get("turnstile_sitekey", "")
CAPTCHA = (f'<div class="cf-turnstile" data-sitekey="{TS}" data-theme="light" data-size="flexible" data-language="auto" '
           f'data-callback="tsOk" data-expired-callback="tsExpired" data-error-callback="tsExpired"></div>') if TS else ""
CAPTCHA_JS = '<script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>' if TS else ""
STAGES_HTML = "\n".join(stage_html(s) for s in STAGES)
POSTS_SORTED = sorted(POSTS, key=lambda p: (p["date"], p["n"]), reverse=True)
DESC = "Iñigo González: IT Site Leader in Madrid. 11+ years in IT operations, Modern Workplace and infrastructure across financial services, healthcare, manufacturing and luxury retail."

import re as _re
_BLANK = _re.compile(r'<a\b[^>]*\btarget="_blank"[^>]*>')

def safe_rel(s):
    """Every link that opens a new tab gets rel="noopener noreferrer" (other rel values such as "me" are kept)."""
    def fix(m):
        t = m.group(0)
        r = _re.search(r'\brel="([^"]*)"', t)
        vals = r.group(1).split() if r else []
        for v in ("noopener", "noreferrer"):
            if v not in vals: vals.append(v)
        rel = f'rel="{" ".join(vals)}"'
        return t.replace(r.group(0), rel) if r else t.replace("<a ", f"<a {rel} ", 1)
    return _BLANK.sub(fix, s)

def write(path, s):
    assert "{{" not in s, path
    s = safe_rel(s)
    f = SITE / path
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(s)
    return len(s)

sizes = {}

# home
latest = "\n".join(card(p, CATS, "") for p in POSTS_SORTED[:3])
home_body = "\n\n".join([
    SEC["hero"], SEC["welcome"],
    f'''<section class="section u-paper2" id="historias">
  <div class="wrap">
    <div class="numbers-head reveal">
      <div>
        <p class="label kicker">Blog</p>
        <h2 class="h2">{bi("Últimas<br>historias.", "Latest<br>stories.")}</h2>
      </div>
      <a class="arrow-link" href="blog/">{bi("Todas las historias", "All stories")} →</a>
    </div>
    <div class="cards">
{latest}
    </div>
  </div>
</section>''',
    f'''<section class="section news-band">
  <div class="wrap welcome reveal">
    <div>
      <p class="label kicker">Tech Career Lab · newsletter</p>
      <h2 class="h2 sm">{bi("33 ideas gratis.", "33 free ideas.")}</h2>
    </div>
    <div>
      <p class="lede">{bi("33 ideas para que te encuentren si trabajas en IT y, después, una idea práctica cada dos semanas en tu email. Sin spam y te das de baja cuando quieras.", "33 ideas to get found if you work in IT, then one practical idea in your inbox every two weeks. No spam, unsubscribe any time.")}</p>
      <a class="btn" href="recursos.html">{bi("Quiero las 33 ideas", "Send me the 33 ideas")} →</a>
    </div>
  </div>
</section>''',
    SEC["map"].replace("{{MAP}}", MAP),
    f'''<section class="section">
  <div class="wrap welcome reveal">
    <div>
      <p class="label kicker">IGG-ICS · IT · Tech Career, Lab &amp; Strategy</p>
      <h2 class="h2 sm">{bi("Estrategia profesional IT.", "IT career strategy.")}</h2>
    </div>
    <div>
      <p class="lede">{bi("Servicios para perfiles IT: genera oportunidades con visibilidad, posicionamiento y networking, y no solo enviando currículums.", "Services for IT professionals: create opportunities through visibility, positioning and networking, not just by sending CVs.")}</p>
      <a class="arrow-link" href="store.html">{bi("Ver los servicios", "See the services")} →</a>
    </div>
  </div>
</section>''',
    f'''<section class="section dark cta-band">
  <div class="wrap welcome reveal">
    <div>
      <p class="label kicker">{bi("Contacto", "Contact")}</p>
      <h2 class="h2 sm">{bi("Hablemos.", "Let's talk.")}</h2>
    </div>
    <div>
      <p class="lede">{bi("Proyectos, ideas o una de mis herramientas adaptada a tu entorno.", "Projects, ideas, or one of my tools adapted to your environment.")}</p>
      <a class="btn" href="about.html#contacto">{bi("Escríbeme", "Get in touch")} →</a>
    </div>
  </div>
</section>'''])
sizes["index.html"] = write("index.html", layout(R="", path="", active="", home=True,
    title_en="Iñigo González · IT Operations & Infrastructure", title_es="Iñigo González · Operaciones IT e Infraestructura",
    desc=DESC, body=home_body, ld=[PERSON, WEBSITE]))

# journey
JP = CONF.get("journey_photo")
def credit(ph):
    return (f'<li>{bi(html.escape(ph["place_es"]), html.escape(ph["place_en"]))}: <a href="{ph["source"]}" target="_blank" rel="noopener">'
            f'{html.escape(ph["author"])}</a>, <a href="{ph["license_url"]}" target="_blank" rel="noopener">{ph["license"]}</a></li>')
CREDITS = "".join(credit(p) for p in ([JP] if JP else []) + [CONF["stage_photos"][k] for k in sorted(CONF["stage_photos"])])
journey_body = page_hero(bi("El viaje · 2015 — 2026", "The journey · 2015 — 2026"),
    bi("Once años.<br>Cinco etapas.", "Eleven years.<br>Five stages."),
    bi("De una consultora tecnológica a la sede de Madrid de una firma de servicios financieros, con la misma idea: que la tecnología funcione y no se note.",
       "From a technology consultancy to the Madrid site of a financial services firm, with the same idea throughout: technology that works and that people don't have to think about.")) \
    + "\n\n" + SEC["numbers"].replace(' u-pt0"', '"') + "\n\n" + SEC["stages"].replace("{{STAGES}}", STAGES_HTML) + "\n\n" + SEC["toolkit"] \
    + f'''

<section class="credits">
  <div class="wrap">
    <p class="label muted">{bi("Fotografías", "Photo credits")}</p>
    <ul>{CREDITS}</ul>
    <p class="muted">{bi("Imágenes de Wikimedia Commons, recortadas y comprimidas para la web.", "Images from Wikimedia Commons, cropped and compressed for the web.")}</p>
  </div>
</section>'''
if JP:
    journey_body = journey_body.replace('<section class="page-hero">', '<section class="page-hero has-bg bg-journey">', 1)
sizes["journey.html"] = write("journey.html", layout(R="", path="journey.html", active="journey",
    title_en="Journey · Iñigo González", title_es="Viaje · Iñigo González",
    desc="Eleven years in IT operations in five stages: consulting, luxury retail, healthcare software, manufacturing and financial services.", body=journey_body,
    ld=[crumbs(("Home", ""), ("Journey", "journey.html"))]))

# blog index
cards = "\n".join(card(p, CATS, "../") for p in POSTS_SORTED)
blog_body = page_hero("Blog · " + bi("Labs y herramientas", "Labs & tools"),
    bi("Cómo lo<br>construí.", "How I<br>built it."),
    bi("Una historia por cada proyecto de GitHub: el problema, lo que hice, lo que aprendí y los siguientes pasos. Todo con datos ficticios.",
       "One story per GitHub project: the problem, what I built, what I learned and the next steps. All with synthetic data.")) + f'''

<section class="section">
  <div class="wrap">
    <div class="cards">
{cards}
    </div>
    <p class="note reveal">{bi("Los laboratorios 06–16 llevan a la nube y a las flotas de GPU lo que hago en operaciones IT: validar hardware, monitorizar y gestionar releases y capacidad. Todos se reproducen en un portátil con datos simulados, y cada artículo termina con los siguientes pasos para llevarlo a un entorno real.", "Labs 06–16 take what I do in IT operations (hardware validation, monitoring, release and capacity management) to the cloud and to GPU fleets. Each one runs on a laptop with simulated data, and every story ends with the next steps to take it to a real environment.")}</p>
  </div>
</section>'''
sizes["blog/index.html"] = write("blog/index.html", layout(R="../", path="blog/", active="blog",
    title_en="Blog · Iñigo González", title_es="Blog · Iñigo González",
    desc="How I built each of my GitHub projects: IT Ops tools and cloud, SRE and GPU labs.", body=blog_body,
    ld=[{"@type": "Blog", "@id": SITE_URL + "blog/#blog", "url": SITE_URL + "blog/", "name": "Labs & tools · Iñigo González",
         "inLanguage": "en", "author": PERSON_REF,
         "blogPost": [{"@type": "BlogPosting", "headline": q["title_en"], "url": f'{SITE_URL}blog/{q["repo"]}.html', "datePublished": q["date"]} for q in POSTS_SORTED]},
        crumbs(("Home", ""), ("Blog", "blog/"))]))

# posts
from urllib.parse import quote as _q

def share_html(p):
    """Share links for a post: plain URLs to each network (no third-party scripts, nothing loads until clicked),
    copy-link, and the device share sheet where the browser offers one (app.js shows that button)."""
    url = f'{SITE_URL}blog/{p["repo"]}.html'
    U = _q(url, safe="")
    def row(l, title, copy, copied, more):
        T = _q(title + " · Iñigo González", safe="")
        aria = {"es": "Compartir en", "en": "Share on"}[l]
        links = [("LinkedIn", f"https://www.linkedin.com/sharing/share-offsite/?url={U}"),
                 ("X", f"https://x.com/intent/post?url={U}&amp;text={T}"),
                 ("WhatsApp", f"https://wa.me/?text={T}%20{U}"),
                 ("Email", f"mailto:?subject={T}&amp;body={U}")]
        ext = ' target="_blank" rel="noopener"'
        a = "".join(f'<a class="share-btn" href="{h}"{"" if n == "Email" else ext} aria-label="{aria} {n}">{n}</a>' for n, h in links)
        return (f'<div class="share-row {l}" lang="{l}">{a}'
                f'<button class="share-btn" type="button" data-copy="{url}" data-copied="{copied}">{copy}</button>'
                f'<button class="share-btn" type="button" data-share="{url}" data-title="{html.escape(title)}" hidden>{more}</button></div>')
    return ('<div class="share">\n'
            f'        <p class="label muted">{bi("Compartir", "Share")}</p>\n'
            f'        {row("es", p["title_es"], "Copiar enlace", "Enlace copiado", "Más…")}\n'
            f'        {row("en", p["title_en"], "Copy link", "Link copied", "More…")}\n'
            '        <p class="share-msg small muted" role="status" aria-live="polite"></p>\n'
            '      </div>')

order = sorted(POSTS, key=lambda p: p["n"])
for i, p in enumerate(order):
    c = CATS[p["cat"]]
    prev = order[i - 1] if i > 0 else None
    nxt = order[i + 1] if i + 1 < len(order) else None
    def nav_link(q, label_es, label_en, cls):
        if not q: return "<span></span>"
        return f'<a class="post-nav-link {cls}" href="{q["repo"]}.html"><span class="label muted">{bi(label_es, label_en)}</span><span>{bi(html.escape(q["title_es"]), html.escape(q["title_en"]))}</span></a>'
    meta = f'{bi(*c)} · {fdate(p["date"])} · {bi(str(minutes(p["es"])) + " min", str(minutes(p["en"])) + " min read")}'
    body = page_hero(f'<a href="./">Blog</a> · {p["n"]}', bi(html.escape(p["title_es"]), html.escape(p["title_en"])),
                     bi(html.escape(p["dek_es"]), html.escape(p["dek_en"])), f'<p class="label post-meta">{meta}</p>').replace('class="page-hero"', 'class="page-hero post-hero"', 1) + f'''

<section class="section post">
  <div class="wrap post-grid">
    <article class="prose">
      <div class="es" lang="es">
{md(p["es"])}
<p>¿Quieres llevarlo a tu entorno o adaptarlo a tu caso? <a href="../about.html#contacto">Escríbeme</a> y lo vemos.</p>
      </div>
      <div class="en" lang="en">
{md(p["en"])}
<p>Want to bring it to your environment or adapt it to your case? <a href="../about.html#contacto">Get in touch</a> and we can look at it together.</p>
      </div>
      <div class="news-box">
        <p class="label kicker">Tech Career Lab · newsletter</p>
        <p class="news-box-t">{bi("¿Te ha servido? Cada dos semanas envío una idea práctica para perfiles IT: LinkedIn, proyectos, networking y procesos de selección.", "Found this useful? Every two weeks I send one practical idea for IT professionals: LinkedIn, projects, networking and hiring processes.")}</p>
        <a class="btn" href="../recursos.html">{bi("Apúntate y llévate las 33 ideas", "Sign up and get the 33 ideas")} →</a>
      </div>
    </article>
    <aside class="post-aside">
      <p class="label muted">{bi("El repositorio", "The repository")}</p>
      <p class="repo-name">{p["repo"]}</p>
      <a class="btn" href="{GITHUB}/{p["repo"]}" target="_blank" rel="noopener">{bi("Ver en GitHub", "View on GitHub")} ↗</a>
      <p class="muted small">{bi("Datos ficticios. Nada de código, datos ni sistemas de ninguna empresa.", "Synthetic data. No employer code, data or systems.")}</p>
      {share_html(p)}
    </aside>
  </div>
  <div class="wrap post-nav">
    {nav_link(prev, "Anterior", "Previous", "prev")}
    {nav_link(nxt, "Siguiente", "Next", "next")}
  </div>
</section>'''
    sizes[f"blog/{p['repo']}.html"] = write(f"blog/{p['repo']}.html", layout(R="../", path=f"blog/{p['repo']}.html", active="blog",
        title_en=f'{p["title_en"]} · Iñigo González', title_es=f'{p["title_es"]} · Iñigo González',
        desc=p["dek_en"], body=body, og_type="article", og_image=OG[p["repo"]],
        ld=[{"@type": "BlogPosting", "headline": p["title_en"], "alternativeHeadline": p["title_es"], "description": p["dek_en"],
             "datePublished": p["date"], "dateModified": p["date"], "inLanguage": "en", "image": SITE_URL + OG[p["repo"]],
             "url": f'{SITE_URL}blog/{p["repo"]}.html', "mainEntityOfPage": f'{SITE_URL}blog/{p["repo"]}.html',
             "author": PERSON_REF, "publisher": PERSON_REF, "isPartOf": {"@id": SITE_URL + "blog/#blog"},
             "articleSection": c[1]},
            crumbs(("Home", ""), ("Blog", "blog/"), (p["title_en"], f'blog/{p["repo"]}.html'))]))

# about
now = f'''<section class="section">
  <div class="wrap now-grid">
    <div class="reveal">
      <p class="label kicker">{bi("Ahora · octubre 2026", "Now · October 2026")}</p>
      <h2 class="h2 sm">{bi("En qué estoy.", "What I'm up to.")}</h2>
    </div>
    <dl class="spec reveal">
      <div class="spec-row"><dt class="label">{bi("Trabajo", "Work")}</dt><dd>{bi("IT Site Leader en Madrid, en servicios financieros.", "IT Site Leader in Madrid, in financial services.")}</dd></div>
      <div class="spec-row"><dt class="label">{bi("Construyendo", "Building")}</dt><dd>{bi("Nuevos repos sobre operaciones IT: contratos y proveedores, pre-aperturas de hoteles y evidencias de seguridad.", "New repos on IT operations: contracts and vendors, hotel pre-openings and security evidence.")}</dd></div>
      <div class="spec-row"><dt class="label">{bi("Labs", "Labs")}</dt><dd>{bi("Kubernetes, SRE y operación de clústeres GPU, en laboratorios abiertos.", "Kubernetes, SRE and GPU cluster operations, in open labs.")}</dd></div>
      <div class="spec-row"><dt class="label">{bi("Idiomas", "Languages")}</dt><dd>{bi("Español nativo, inglés a diario y francés en progreso.", "Native Spanish, English every day and French in progress.")}</dd></div>
    </dl>
  </div>
</section>'''
about_body = SEC["about"].replace('class="section dark" id="sobre-mi"', 'class="section dark about-top" id="sobre-mi"') \
    + "\n\n" + now + "\n\n" + SEC["contact"].replace("{{FORM_ACTION}}", FORM).replace("{{CAPTCHA}}", CAPTCHA).replace("{{CAPTCHA_JS}}", CAPTCHA_JS)
sizes["about.html"] = write("about.html", layout(R="", path="about.html", active="about",
    title_en="About · Iñigo González", title_es="Sobre mí · Iñigo González",
    desc="About Iñigo González, IT Site Leader in Madrid, and how to get in touch.", body=about_body,
    ld=[{"@type": "ProfilePage", "url": SITE_URL + "about.html", "mainEntity": PERSON}, crumbs(("Home", ""), ("About", "about.html"))]))

# store (IGG-ICS · IT · Tech Career, Lab & Strategy): service catalogue, no prices or checkout yet
BOOK = CONF.get("booking_url", "")  # Calendly: only sent by email for follow-up sessions, not shown on the site
RESERVA = "about.html?reserva=1#reservar"
book_btn = f'<a class="btn" href="{RESERVA}">{bi("Reserva la sesión inicial · 39 €", "Book the initial session · €39")} →</a>'
book_link = lambda es, en: f'<a class="arrow-link" href="about.html#contacto">{bi(es, en)} →</a>'
session_link = lambda es, en: f'<a class="arrow-link" href="{RESERVA}">{bi(es, en)} →</a>'

PROBLEMS = [
    ("Tu CV no pasa el primer filtro", "Your CV doesn't get past the first filter",
     "Los ATS y los reclutadores deciden en segundos. Si tu CV no explica tu stack y tus resultados, ni llega a un técnico.",
     "ATS software and recruiters decide in seconds. If your CV doesn't explain your stack and your results, it never reaches an engineer."),
    ("Tu LinkedIn no te trae oportunidades", "LinkedIn isn't bringing you opportunities",
     "Un perfil genérico no aparece en las búsquedas de los reclutadores tech, y nadie te escribe.",
     "A generic profile doesn't show up in tech recruiters' searches, so nobody gets in touch."),
    ("Envías candidaturas y no pasa nada", "You apply and nothing happens",
     "Sin una estrategia, sin networking y sin el mercado oculto, todo depende de las ofertas publicadas y de la suerte.",
     "Without a strategy, networking or the hidden job market, everything depends on advertised roles and luck."),
]
problem_cards = "\n".join(
    f'      <div class="etm-item reveal"><p class="label muted">{i:02d}</p><h3>{bi(es, en)}</h3><p>{bi(des, den)}</p></div>'
    for i, (es, en, des, den) in enumerate(PROBLEMS, 1))

SERVICES = [
    {"id": "revision", "tag": ("Para empezar", "To get started"),
     "name": ("Revisión exprés · CV + LinkedIn IT", "Express review · CV + LinkedIn for IT"),
     "fmt": ("Por escrito, sin llamada · entrega en 5 días laborables", "Written, no call · delivered in 5 working days"),
     "items": [("Revisión de tu CV pensando en los filtros ATS y en reclutadores de IT", "A review of your CV with ATS filters and IT recruiters in mind"),
               ("Revisión de tu perfil de LinkedIn: titular, extracto, experiencia y aptitudes", "A review of your LinkedIn profile: headline, about, experience and skills"),
               ("Informe con los cambios ordenados por prioridad", "A report with the changes in order of priority"),
               ("Una ronda de dudas por email", "One round of questions by email")],
     "for": ("Si tienes poco tiempo y quieres un CV y un perfil que funcionen ya.", "If you're short on time and want a CV and a profile that work now.")},
    {"id": "diagnostico", "tag": ("El más pedido", "Most popular"),
     "name": ("Diagnóstico 360º IT", "IT 360º diagnosis"),
     "fmt": ("Videollamada de 60 min · resumen por escrito en 48 h", "60-min video call · written summary within 48 h"),
     "items": [("Análisis de tu perfil, tu CV, tu LinkedIn y tu objetivo", "A look at your profile, CV, LinkedIn and goal"),
               ("Hacia dónde ir: operaciones, cloud, ciberseguridad, gestión…", "Where to go next: operations, cloud, security, management…"),
               ("Qué pide hoy el mercado para ese paso", "What the market asks for that step today"),
               ("Plan de acción de 30 días por escrito", "A written 30-day action plan")],
     "for": ("Si no tienes claro el siguiente paso o llevas tiempo sin respuestas.", "If your next step isn't clear or you've had no replies for a while.")},
    {"id": "plan", "tag": ("Más completo", "Most complete"),
     "name": ("Plan Acción IT · 4 semanas", "IT Action Plan · 4 weeks"),
     "fmt": ("4 videollamadas de 45 min · dudas por email", "4 × 45-min video calls · questions by email"),
     "items": [("El Diagnóstico 360º IT", "The IT 360º diagnosis"),
               ("La Revisión exprés de CV + LinkedIn completa", "The full CV + LinkedIn express review"),
               ("Estrategia de búsqueda, networking y mercado oculto", "Job search strategy, networking and the hidden job market"),
               ("Preparación de entrevistas con una simulación, en español o en inglés", "Interview preparation with a mock interview, in Spanish or English")],
     "for": ("Si buscas activamente y quieres hacerlo con método y acompañamiento.", "If you're actively looking and want a method and someone alongside you.")},
]
def svc_card(s):
    lis = "".join(f"<li>{bi(es, en)}</li>" for es, en in s["items"])
    return f'''      <article class="svc reveal" id="{s["id"]}">
        <p class="label svc-tag">{bi(*s["tag"])}</p>
        <h3>{bi(*s["name"])}</h3>
        <p class="label muted svc-fmt">{bi(*s["fmt"])}</p>
        <ul>{lis}</ul>
        <p class="svc-for">{bi(*s["for"])}</p>
        <div class="svc-foot">
          <span class="label svc-price">{bi("Precio: muy pronto", "Price: coming soon")}</span>
          {book_link("Pregunta por este servicio", "Ask about this service")}
        </div>
      </article>'''
svc_cards = "\n".join(svc_card(s) for s in SERVICES)

ETM_AREAS = [
    ("Estrategia profesional", "Career strategy",
     "Dónde estás y hacia dónde ir (operaciones, cloud, ciberseguridad, gestión…) y qué pasos tienen sentido con el mercado actual y la IA.",
     "Where you are and where to go next (operations, cloud, security, management…) and which steps make sense in today's market and with AI."),
    ("LinkedIn y visibilidad", "LinkedIn and visibility",
     "Un perfil que explica tu stack y tus resultados, y contenido técnico que hace que te encuentren.",
     "A profile that explains your stack and your results, and technical content that gets you found."),
    ("Marca personal", "Personal brand",
     "Demostrar con proyectos y no solo con el CV: GitHub, portfolio y aprender en público.",
     "Show it with projects, not just a CV: GitHub, a portfolio and learning in public."),
    ("Networking y mercado oculto", "Networking and the hidden job market",
     "Cómo llegar a hiring managers, reclutadores tech y equipos antes de que la oferta se publique.",
     "How to reach hiring managers, tech recruiters and teams before the role is advertised."),
    ("CV, entrevistas y procesos", "CV, interviews and hiring processes",
     "Un CV que pasa los ATS y convence a un técnico, y entrevistas técnicas y de comportamiento, en español e inglés.",
     "A CV that gets through the ATS and convinces an engineer, plus technical and behavioural interviews, in Spanish and English."),
    ("Posicionamiento a largo plazo", "Long-term positioning",
     "Un plan para seguir creciendo en tu especialidad y generar oportunidades, también en remoto o en otros países.",
     "A plan to keep growing in your field and creating opportunities, including remote roles and other countries."),
]
etm_cards = "\n".join(
    f'      <div class="etm-item reveal"><p class="label muted">{i:02d}</p><h3>{bi(es, en)}</h3><p>{bi(des, den)}</p></div>'
    for i, (es, en, des, den) in enumerate(ETM_AREAS, 1))

STEPS = [
    ("Empieza gratis", "Start for free", "Apúntate a la newsletter y llévate las <a href='recursos.html'>33 ideas</a> para que te encuentren si trabajas en IT.", "Join the newsletter and get the <a href='recursos.html'>33 ideas</a> to get found if you work in IT."),
    ("Reserva la sesión inicial", "Book the initial session", "En el <a href='about.html?reserva=1#reservar'>formulario de contacto</a> marcas la sesión inicial (30 min · 39 €) y eliges una hora de lunes a viernes, de 10:30 a 18:00 (hora de Madrid).", "In the <a href='about.html?reserva=1#reservar'>contact form</a>, tick the initial session (30 min · €39) and pick a time, Monday to Friday, 10:30 to 18:00 (Madrid time)."),
    ("Pago y confirmación", "Payment and confirmation", "Te envío por email el enlace de pago de Revolut. Al recibir el pago te confirmo la cita y te mando el enlace de la videollamada.", "I email you the Revolut payment link. Once payment arrives, I confirm the appointment and send you the video call link."),
    ("Sesión y siguientes pasos", "Session and next steps", "30 minutos sobre tu situación y tu objetivo, con siguientes pasos concretos. Si quieres seguir, te paso el enlace para reservar más sesiones.", "30 minutes on where you are and your goal, with concrete next steps. If you want to continue, I'll send you the link to book more sessions."),
]
steps_html = "\n".join(
    f'      <div class="spec-row"><dt class="label">{i:02d} · {bi(es, en)}</dt><dd>{bi(des, den)}</dd></div>'
    for i, (es, en, des, den) in enumerate(STEPS, 1))

FAQ = [
    ("¿Cuánto cuesta la sesión inicial?", "How much is the initial session?",
     "39 €, impuestos incluidos, por 30 minutos de videollamada. No tienes que contratar nada después.",
     "€39, taxes included, for a 30-minute video call. You don't have to buy anything afterwards."),
    ("¿Cómo se paga?", "How do I pay?",
     "Por adelantado, con el enlace de pago de Revolut que te envío por email cuando reservas. Puedes pagar con tarjeta o desde tu cuenta Revolut. Yo no veo los datos de tu tarjeta.",
     "In advance, through the Revolut payment link I email you when you book. You can pay by card or from your Revolut account. I never see your card details."),
    ("¿Y el resto de servicios?", "What about the other services?",
     "Publicaré sus precios cuando abra su contratación. Si te interesa alguno, lo hablamos en la sesión inicial.",
     "I'll publish their prices when booking for them opens. If one interests you, we can talk about it in the initial session."),
    ("¿Para quién es?", "Who is it for?",
     "Para perfiles IT: soporte, sistemas, operaciones, workplace, infraestructura, cloud, ciberseguridad o gestión de equipos y servicios, desde junior hasta senior.",
     "For IT professionals: support, systems, operations, workplace, infrastructure, cloud, security or team and service management, from junior to senior."),
    ("¿Es online? ¿En qué idioma?", "Is it online? In which language?",
     "Todo es online, por videollamada o por escrito, en español o en inglés.",
     "Everything is online, by video call or in writing, in Spanish or English."),
    ("¿Me garantizas un trabajo?", "Can you guarantee me a job?",
     "No. Nadie puede garantizarlo. Trabajamos todo lo que depende de ti para que lleguen más y mejores oportunidades.",
     "No. Nobody can. We work on everything that depends on you, so that more and better opportunities come your way."),
    ("¿Qué pasa con mi CV y lo que te cuente?", "What happens to my CV and what I tell you?",
     "Es confidencial y solo lo uso para prestarte el servicio. Más detalles en la política de privacidad.",
     "It's confidential and I only use it to provide the service. More details in the privacy policy."),
]
faq_html = "\n".join(
    f'      <details class="faq-item"><summary>{bi(q_es, q_en)}</summary><p>{bi(a_es, a_en)}</p></details>'
    for q_es, q_en, a_es, a_en in FAQ)

store_body = page_hero("Store · IGG-ICS · IT · Tech Career, Lab &amp; Strategy",
    bi("Tu carrera en IT,<br>con estrategia.", "Your IT career,<br>with a strategy."),
    bi("Servicios de estrategia profesional para perfiles IT y tecnológicos: te ayudo a generar oportunidades con visibilidad, posicionamiento y networking, y no solo enviando currículums.",
       "Career strategy services for IT and tech professionals: I help you create opportunities through visibility, positioning and networking, not just by sending CVs."),
    f'''<div class="hero-ctas u-mt34">
      <a class="btn" href="#servicios">{bi("Ver servicios", "See services")} ↓</a>
      {session_link("Sesión inicial · 30 min · 39 €", "Initial session · 30 min · €39")}
    </div>''') + f'''

<section class="section">
  <div class="wrap">
    <div class="numbers-head reveal">
      <div>
        <p class="label kicker">{bi("¿Te suena?", "Sound familiar?")}</p>
        <h2 class="h2 sm">{bi("Lo que frena a muchos perfiles IT.", "What holds many IT professionals back.")}</h2>
      </div>
    </div>
    <div class="etm-grid">
{problem_cards}
    </div>
  </div>
</section>

<section class="section u-paper2" id="servicios">
  <div class="wrap">
    <div class="numbers-head reveal">
      <div>
        <p class="label kicker">{bi("Servicios", "Services")}</p>
        <h2 class="h2 sm">{bi("Elige por dónde empezar.", "Choose where to start.")}</h2>
      </div>
    </div>
    <p class="notice reveal">{bi("Estos servicios se contratarán más adelante. Para empezar, <a href='recursos.html'>llévate las 33 ideas gratis</a> o <a href='about.html?reserva=1#reservar'>reserva la sesión inicial</a> (30 min · 39 €).",
                                 "These services will open for booking later. To start, <a href='recursos.html'>get the 33 ideas for free</a> or <a href='about.html?reserva=1#reservar'>book the initial session</a> (30 min · €39).")}</p>
    <div class="svc-grid">
{svc_cards}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="numbers-head reveal">
      <div>
        <p class="label kicker">{bi("Qué trabajamos", "What we work on")}</p>
        <h2 class="h2 sm">{bi("Más que buscar empleo.", "More than a job search.")}</h2>
      </div>
    </div>
    <div class="etm-grid">
{etm_cards}
    </div>
  </div>
</section>

<section class="section u-paper2">
  <div class="wrap now-grid">
    <div class="reveal">
      <p class="label kicker">{bi("Cómo funciona", "How it works")}</p>
      <h2 class="h2 sm">{bi("Paso a paso.", "Step by step.")}</h2>
    </div>
    <dl class="spec etm-spec reveal">
{steps_html}
    </dl>
  </div>
</section>

<section class="section">
  <div class="wrap welcome reveal">
    <div>
      <p class="label kicker">{bi("Próximamente", "Coming soon")}</p>
      <h2 class="h2 sm">{bi("Taller en grupo.", "Group workshop.")}</h2>
    </div>
    <div>
      <p class="lede">{bi("Un taller corto y práctico para perfiles IT, en directo y en grupo reducido. Si te apuntas a la newsletter <em>Tech Career Lab</em>, serás de los primeros en saber la fecha.",
                          "A short, hands-on workshop for IT professionals, live and in a small group. Join the <em>Tech Career Lab</em> newsletter and you'll be among the first to hear the date.")}</p>
      <a class="arrow-link" href="recursos.html">{bi("Apúntate y te aviso", "Sign up and I'll let you know")} →</a>
    </div>
  </div>
</section>

<section class="section u-paper2">
  <div class="wrap now-grid">
    <div class="reveal">
      <p class="label kicker">FAQ</p>
      <h2 class="h2 sm">{bi("Preguntas frecuentes.", "Questions.")}</h2>
    </div>
    <div class="faq reveal">
{faq_html}
    </div>
  </div>
</section>

<section class="section dark cta-band">
  <div class="wrap welcome reveal">
    <div>
      <p class="label kicker">IGG-ICS</p>
      <h2 class="h2 sm">{bi("¿Hablamos?", "Shall we talk?")}</h2>
    </div>
    <div>
      <p class="lede">{bi("Más que buscar empleo, trabajamos en construir carreras profesionales en IT con estrategia.", "More than looking for a job, we build IT careers with a strategy.")}</p>
      {book_btn}
      <p class="muted small u-mt22">{bi("Ningún servicio puede garantizar una oferta de trabajo. Lo que sí trabajamos es todo lo que depende de ti para que lleguen más y mejores oportunidades. Consulta las <a href='condiciones.html'>condiciones</a>.", "No service can guarantee a job offer. What we do work on is everything that depends on you, so that more and better opportunities come your way. See the <a href='condiciones.html'>terms</a>.")}</p>
    </div>
  </div>
</section>'''
sizes["store.html"] = write("store.html", layout(R="", path="store.html", active="store",
    title_en="Store · IGG-ICS IT career services · Iñigo González", title_es="Store · Servicios IGG-ICS para perfiles IT · Iñigo González",
    desc="IGG-ICS career services for IT professionals: CV and LinkedIn review, IT 360º diagnosis and a 4-week action plan. Online, in Spanish or English.", body=store_body,
    ld=[crumbs(("Home", ""), ("Store", "store.html"))]))

# old advisory URL: keep it working (newsletters link to it) and send visitors to the store
sizes["asesoria.html"] = write("asesoria.html", '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<!--SEC-->
<title>IGG-ICS · Store · Iñigo González</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="https://inigogonzalezgarcia.github.io/store.html">
<meta http-equiv="refresh" content="0; url=store.html">
<script src="assets/redirect.js"></script>
</head>
<body>
<p><a href="store.html">IGG-ICS → Store</a></p>
</body>
</html>
'''.replace("<!--SEC-->", SEC_HEAD))

# resources: lead magnet "33 ideas" + newsletter signup (Formspree for now; full text goes by email, not on the site)
RES_BLOCKS = [
    ("Tu perfil de LinkedIn", "Your LinkedIn profile", 7),
    ("Contenido y visibilidad", "Content and visibility", 5),
    ("Demuéstralo con proyectos", "Show it with projects", 6),
    ("Networking y mercado oculto", "Networking and the hidden job market", 5),
    ("CV, entrevistas y procesos", "CV, interviews and hiring processes", 6),
    ("A largo plazo", "The long game", 4),
]
res_cards = "\n".join(
    f'      <div class="etm-item reveal"><p class="label muted">{n} {bi("ideas", "ideas")}</p><h3>{bi(es, en)}</h3></div>'
    for es, en, n in RES_BLOCKS)
NEWS_ACTION = CONF.get("brevo_form") or FORM
news_form = f'''<form class="reveal" id="newsForm" action="{NEWS_ACTION}" method="POST" novalidate data-kind="news" data-provider="{'brevo' if CONF.get('brevo_form') else 'formspree'}">
      <div class="field"><label class="label" for="n-name">{bi("Nombre", "Name")}</label><input id="n-name" name="NOMBRE" autocomplete="given-name" required></div>
      <div class="field"><label class="label" for="n-email">Email</label><input id="n-email" name="EMAIL" type="email" autocomplete="email" required></div>
      <label class="check"><input type="checkbox" id="n-consent" required> <span>{bi("Quiero recibir las 33 ideas y la newsletter <em>Tech Career Lab</em> (cada dos semanas) con consejos para perfiles IT. Puedo darme de baja cuando quiera.", "I want to receive the 33 ideas and the <em>Tech Career Lab</em> newsletter (every two weeks) with tips for IT professionals. I can unsubscribe at any time.")}</span></label>
      <input class="hp" type="text" name="email_address_check" value="" tabindex="-1" autocomplete="off" aria-hidden="true">
      {CAPTCHA}
      <div><button class="btn" type="submit">{bi("Quiero mis 33 ideas", "Send me the 33 ideas")} ↗</button></div>
      <p class="form-status" id="newsStatus" role="status"></p>
      <p class="privacy">{bi("Te enviaré un email para confirmar tu suscripción (doble confirmación). La newsletter se gestiona con Brevo y solo uso tus datos para enviarte las ideas y la newsletter. Más información en la <a href='privacidad.html'>política de privacidad</a>.", "I'll email you to confirm your subscription (double opt-in). The newsletter runs on Brevo and I only use your details to send you the ideas and the newsletter. More in the <a href='privacidad.html'>privacy policy</a>.")}</p>
    </form>'''
resources_body = page_hero(bi("Recursos gratuitos · Tech Career Lab", "Free resources · Tech Career Lab"),
    bi("33 ideas para que te encuentren<br>si trabajas en IT.", "33 ideas to get found<br>if you work in IT."),
    bi("Si buscas trabajo en IT o quieres empezar a construir tu marca profesional, estas 33 ideas te ayudan a ganar visibilidad, demostrar lo que sabes hacer y que más empresas te tengan en su radar.",
       "If you are looking for an IT job or want to start building your professional brand, these 33 ideas help you get seen, show what you can do and get on more companies' radar.")) + f'''

<section class="section">
  <div class="wrap contact">
    <div class="reveal">
      <p class="label kicker">{bi("Te las envío por email", "Delivered by email")}</p>
      <h2 class="h2 sm">{bi("Recíbelas gratis.", "Get them free.")}</h2>
      <p class="lede muted">{bi("Déjame tu nombre y tu email y te mando las 33 ideas, con enlaces a ejemplos reales en esta web. Después recibirás la newsletter <em>Tech Career Lab</em>: LinkedIn, proyectos, networking y procesos de selección para perfiles IT.",
                                "Leave your name and email and I'll send you the 33 ideas, with links to real examples on this site. After that you'll get the <em>Tech Career Lab</em> newsletter: LinkedIn, projects, networking and hiring processes for IT professionals.")}</p>
    </div>
    {news_form}
  </div>
</section>

<section class="section u-paper2">
  <div class="wrap">
    <p class="label kicker">{bi("Qué incluye", "What's inside")}</p>
    <div class="etm-grid">
{res_cards}
    </div>
  </div>
</section>

<section class="section dark cta-band">
  <div class="wrap welcome reveal">
    <div>
      <p class="label kicker">IGG-ICS</p>
      <h2 class="h2 sm">{bi("¿Quieres ir más rápido?", "Want to move faster?")}</h2>
    </div>
    <div>
      <p class="lede">{bi("Si prefieres trabajarlo conmigo, paso a paso y con un plan a tu medida, échale un vistazo a los servicios.", "If you'd rather work on it with me, step by step and with a plan built for you, take a look at the services.")}</p>
      <a class="btn" href="store.html">{bi("Ver los servicios", "See the services")} →</a>
    </div>
  </div>
</section>
{CAPTCHA_JS}'''
sizes["recursos.html"] = write("recursos.html", layout(R="", path="recursos.html", active="resources",
    title_en="33 ideas to get found in IT · Iñigo González", title_es="33 ideas para que te encuentren en IT · Iñigo González",
    desc="Free resource: 33 ideas for IT professionals to get found on LinkedIn, show their work with projects, network and get through hiring processes. Plus the Tech Career Lab newsletter.", body=resources_body,
    ld=[crumbs(("Home", ""), ("Resources", "recursos.html"))]))

# links
LINKS = [
    ("blog/", bi("Blog: cómo construí cada proyecto", "Blog: how I built each project"), ""),
    ("journey.html", bi("El viaje: once años en cinco etapas", "The journey: eleven years in five stages"), ""),
    ("store.html", bi("Store · IGG-ICS: servicios para perfiles IT", "Store · IGG-ICS: services for IT professionals"), ""),
    ("recursos.html", bi("Gratis: 33 ideas para que te encuentren si trabajas en IT", "Free: 33 ideas to get found if you work in IT"), ""),
    (LINKEDIN, "LinkedIn", "ext"),
    (GITHUB, "GitHub", "ext"),
    ("about.html#contacto", bi("Formulario de contacto", "Contact form"), ""),
    (LINKTREE, "Linktree", "ext"),
]
TGT = ' target="_blank" rel="me noopener"'
links_html = "\n".join(
    f'      <a class="link-btn reveal" href="{h}"{TGT if x == "ext" and h.startswith("http") else ""}><span>{t}</span><span aria-hidden="true">{"↗" if x else "→"}</span></a>'
    for h, t, x in LINKS)
links_body = page_hero("Links", bi("Todo, en un sitio.", "Everything, in one place."), "") + f'''

<section class="section links-section">
  <div class="wrap links-list">
{links_html}
  </div>
</section>'''
sizes["links.html"] = write("links.html", layout(R="", path="links.html", active="links",
    title_en="Links · Iñigo González", title_es="Links · Iñigo González",
    desc="Blog, journey, LinkedIn, GitHub and contact for Iñigo González.", body=links_body,
    ld=[crumbs(("Home", ""), ("Links", "links.html"))]))

# legal pages (legal notice, terms); privacidad.html stays hand-written
import legal
for path, kw in legal.PAGES.items():
    sizes[path] = write(path, legal.shell(path=path, **kw))

# 404: GitHub Pages serves /404.html for any missing URL, at that URL, so every link is root-absolute (R="/")
nf_latest = "\n".join(f'      <a class="link-btn" href="/blog/{q["repo"]}.html"><span>{html.escape(q["title_en"])}</span><span aria-hidden="true">→</span></a>' for q in POSTS_SORTED[:3])
nf_body = page_hero("404", bi("Esta página<br>no existe.", "This page<br>doesn't exist."),
    bi("Puede que el enlace sea antiguo o tenga una errata. Estos caminos sí funcionan:", "The link may be old or have a typo. These ones work:")) + f'''

<section class="section links-section">
  <div class="wrap links-list">
      <a class="link-btn" href="/"><span>{bi("Inicio", "Home")}</span><span aria-hidden="true">→</span></a>
      <a class="link-btn" href="/blog/"><span>{bi("Blog: labs y herramientas", "Blog: labs & tools")}</span><span aria-hidden="true">→</span></a>
{nf_latest}
      <a class="link-btn" href="/about.html#contacto"><span>{bi("Contacto", "Contact")}</span><span aria-hidden="true">→</span></a>
  </div>
</section>'''
sizes["404.html"] = write("404.html", layout(R="/", path="404.html", active="", title_en="Page not found · Iñigo González",
    title_es="Página no encontrada · Iñigo González", desc="This page doesn't exist.", body=nf_body, robots="noindex"))

# sitemap.xml + robots.txt: every indexable page (not noindex, not redirects); lastmod = post date, or the newest
# post date for pages that list posts, so the file only changes when content does
NOINDEX = {"404.html", "asesoria.html", "privacidad.html"} | set(legal.PAGES)
newest = max(q["date"] for q in POSTS)
post_date = {f'blog/{q["repo"]}.html': q["date"] for q in POSTS}
urls = []
for rel in sorted(sizes, key=lambda r: (r != "index.html", r.startswith("blog/"), r)):
    if rel in NOINDEX: continue
    loc = SITE_URL + ("" if rel == "index.html" else rel.replace("index.html", ""))
    urls.append(f"  <url><loc>{loc}</loc><lastmod>{post_date.get(rel, newest)}</lastmod></url>")
(SITE / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                  + "\n".join(urls) + "\n</urlset>\n")
(SITE / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /src/\n\nSitemap: {SITE_URL}sitemap.xml\n")

data = {"cities": {c["id"]: c for c in CITIES}, "hero": CONF["hero_photos"], "about": CONF.get("about_photo"),
        "formspree": bool(CONF.get("formspree_id")), "ga4": CONF.get("ga4_id", "")}
(SITE / "assets" / "data.js").write_text("window.SITE=" + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n")

# privacidad.html is hand-written: keep its security <meta> block and new-tab links in sync with the rest of the site
pv = SITE / "privacidad.html"
pt = pv.read_text()
pt = _re.sub(r"(<!-- sec:start[^>]*-->\n).*?(<!-- sec:end -->)", lambda m: m.group(1) + SEC_HEAD + "\n" + m.group(2), pt, count=1, flags=_re.S)
pv.write_text(safe_rel(pt))

# security checks on everything that is served
problems = []
for f in sorted(SITE.rglob("*.html")):
    rel = f.relative_to(SITE).as_posix()
    if rel.startswith("src/"): continue
    t = f.read_text()
    head = t.split("</head>")[0]
    if 'http-equiv="Content-Security-Policy"' not in head: problems.append(f"{rel}: no CSP")
    elif head.find("<script") != -1 and head.find("<script") < head.find("Content-Security-Policy"): problems.append(f"{rel}: script before CSP")
    if 'name="referrer"' not in head: problems.append(f"{rel}: no referrer policy")
    for sc in _re.findall(r"<script(?![^>]*\bsrc=)([^>]*)>", t):
        if 'type="application/ld+json"' not in sc: problems.append(f"{rel}: inline script")
    if _re.search(r'<[a-zA-Z][^>]*\sstyle="', t): problems.append(f"{rel}: inline style attribute")
    if _re.search(r"<style\b", t): problems.append(f"{rel}: <style> block")
    if _re.search(r'<[a-zA-Z][^>]*\son[a-z]+="', t): problems.append(f"{rel}: inline event handler")
    if "javascript:" in t: problems.append(f"{rel}: javascript: URL")
    for a in _BLANK.findall(t):
        if not ("noopener" in a and "noreferrer" in a): problems.append(f"{rel}: target=_blank without noopener noreferrer")
    if MAIL in t: problems.append(f"{rel}: email address in plain text")
for f in list(SITE.rglob("*.html")) + list((SITE / "assets").glob("*.js")) + list((SITE / "assets").glob("*.css")):
    if "xkeysib-" in f.read_text(errors="ignore"): problems.append(f"{f.relative_to(SITE)}: Brevo API key")
if problems:
    raise SystemExit("security check failed:\n  " + "\n  ".join(problems))
print("ok", len(sizes), "pages,", sum(sizes.values()) // 1024, "KB · security checks passed")
