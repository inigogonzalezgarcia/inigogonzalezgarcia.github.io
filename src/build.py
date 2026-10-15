"""Build every page (index, journey, blog, about, links, store) and assets/data.js from src/. Run: python3 src/build.py"""
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
         where="Madrid · París · Lisboa", where_en="Madrid · Paris · Lisbon",
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
         where="Madrid · Londres · París", where_en="Madrid · London · Paris",
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
HIT = {"ESP", "GBR", "FRA", "PRT", "USA", "BEL", "ITA", "TUR", "NLD"}
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


paths = "".join(f'<path class="land{" hit" if iso in HIT else ""}" d="{rel(d)}"/>' for iso, d in M["paths"])
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
    major = " major" if c["id"] in ("madrid", "kansas", "istanbul") else ""
    pins.append(f'<g class="pin {c["kind"]}{major}" data-id="{c["id"]}" data-s="{" ".join(c["stages"])}" data-x="{x:.1f}" data-y="{y:.1f}" transform="translate({x:.1f} {y:.1f})" tabindex="0" role="button" aria-label="{html.escape(c["name_es"])} / {html.escape(c["name_en"])}"><circle class="halo" r="7"/><circle class="core" r="3"/><text class="es" x="{lx}" y="{ly}" text-anchor="{anchor}">{html.escape(c["name_es"])}</text><text class="en" x="{lx}" y="{ly}" text-anchor="{anchor}">{html.escape(c["name_en"])}</text></g>')
MAP = f'''      <svg id="map" viewBox="0 0 1000 487" role="img" aria-label="Mapa / Map">
        <g id="mapLayer">{paths}<g id="routes">{"".join(routes)}</g><g id="pins">{"".join(pins)}</g></g>
      </svg>'''


# ---------------------------------------------------------------- pages
import sys
sys.path.insert(0, str(ROOT))
from pages import layout, page_hero, card, md, minutes, fdate, soon, bi as bi2, MAIL, LINKEDIN, GITHUB, LINKTREE
from posts import POSTS, CATS

SEC = {p.stem: p.read_text() for p in (ROOT / "sections").glob("*.html")}
FORM = f'https://formspree.io/f/{CONF["formspree_id"]}' if CONF.get("formspree_id") else f"mailto:{MAIL}"
TS = CONF.get("turnstile_sitekey", "")
CAPTCHA = (f'<div class="cf-turnstile" data-sitekey="{TS}" data-theme="light" data-size="flexible" data-language="auto" '
           f'data-callback="tsOk" data-expired-callback="tsExpired" data-error-callback="tsExpired"></div>') if TS else ""
CAPTCHA_JS = '<script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>' if TS else ""
STAGES_HTML = "\n".join(stage_html(s) for s in STAGES)
POSTS_SORTED = sorted(POSTS, key=lambda p: (p["date"], p["n"]), reverse=True)
DESC = "Iñigo González: IT Site Leader in Madrid. 11+ years in IT operations, Modern Workplace and infrastructure across financial services, healthcare, manufacturing and luxury retail."

def write(path, s):
    assert "{{" not in s, path
    f = SITE / path
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(s)
    return len(s)

sizes = {}

# home
latest = "\n".join(card(p, CATS, "") for p in POSTS_SORTED[:3])
home_body = "\n\n".join([
    SEC["hero"], SEC["welcome"],
    f'''<section class="section" id="historias" style="background:var(--paper-2)">
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
    SEC["map"].replace("{{MAP}}", MAP),
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
    desc=DESC, body=home_body))

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
    + "\n\n" + SEC["numbers"].replace(' style="padding-top:0"', '') + "\n\n" + SEC["stages"].replace("{{STAGES}}", STAGES_HTML) + "\n\n" + SEC["toolkit"] \
    + f'''

<section class="credits">
  <div class="wrap">
    <p class="label muted">{bi("Fotografías", "Photo credits")}</p>
    <ul>{CREDITS}</ul>
    <p class="muted">{bi("Imágenes de Wikimedia Commons, recortadas y comprimidas para la web.", "Images from Wikimedia Commons, cropped and compressed for the web.")}</p>
  </div>
</section>'''
if JP:
    journey_body = journey_body.replace('<section class="page-hero">', f'<section class="page-hero has-bg" style="background-image:url({JP["src"]})">', 1)
sizes["journey.html"] = write("journey.html", layout(R="", path="journey.html", active="journey",
    title_en="Journey · Iñigo González", title_es="Viaje · Iñigo González",
    desc="Eleven years in IT operations in five stages: consulting, luxury retail, healthcare software, manufacturing and financial services.", body=journey_body))

# blog index
cards = "\n".join(card(p, CATS, "../") for p in POSTS_SORTED)
blog_body = page_hero("Blog · " + bi("Aprendiendo en público", "Learning in public"),
    bi("Cómo lo<br>construí.", "How I<br>built it."),
    bi("Una historia por cada proyecto de GitHub: el problema, lo que hice, lo que aprendí y lo que falta por probar. Todo con datos ficticios.",
       "One story per GitHub project: the problem, what I built, what I learned and what is still untested. All with synthetic data.")) + f'''

<section class="section">
  <div class="wrap">
    <div class="cards">
{cards}
    </div>
    <p class="note reveal">{bi("Los laboratorios 06–16 son eso: laboratorios. No tengo experiencia en producción con flotas de GPU; los hago para aprender el problema y lo digo en cada artículo.", "Labs 06–16 are just that: labs. I don't have production GPU fleet experience; I build them to learn the problem, and every story says so.")}</p>
  </div>
</section>'''
sizes["blog/index.html"] = write("blog/index.html", layout(R="../", path="blog/", active="blog",
    title_en="Blog · Iñigo González", title_es="Blog · Iñigo González",
    desc="How I built each of my GitHub projects: IT Ops tools and cloud, SRE and GPU labs.", body=blog_body))

# posts
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
      </div>
      <div class="en" lang="en">
{md(p["en"])}
      </div>
    </article>
    <aside class="post-aside">
      <p class="label muted">{bi("El repositorio", "The repository")}</p>
      <p class="repo-name">{p["repo"]}</p>
      <a class="btn" href="{GITHUB}/{p["repo"]}" target="_blank" rel="noopener">{bi("Ver en GitHub", "View on GitHub")} ↗</a>
      <p class="muted small">{bi("Datos ficticios. Nada de código, datos ni sistemas de ninguna empresa.", "Synthetic data. No employer code, data or systems.")}</p>
    </aside>
  </div>
  <div class="wrap post-nav">
    {nav_link(prev, "Anterior", "Previous", "prev")}
    {nav_link(nxt, "Siguiente", "Next", "next")}
  </div>
</section>'''
    sizes[f"blog/{p['repo']}.html"] = write(f"blog/{p['repo']}.html", layout(R="../", path=f"blog/{p['repo']}.html", active="blog",
        title_en=f'{p["title_en"]} · Iñigo González', title_es=f'{p["title_es"]} · Iñigo González',
        desc=p["dek_en"], body=body, og_type="article"))

# about
now = f'''<section class="section">
  <div class="wrap now-grid">
    <div class="reveal">
      <p class="label kicker">{bi("Ahora · octubre 2026", "Now · October 2026")}</p>
      <h2 class="h2 sm">{bi("En qué estoy.", "What I'm up to.")}</h2>
    </div>
    <dl class="spec reveal">
      <div class="spec-row"><dt class="label">{bi("Trabajo", "Work")}</dt><dd>{bi("IT Site Leader en Madrid, en servicios financieros.", "IT Site Leader in Madrid, in financial services.")}</dd></div>
      <div class="spec-row"><dt class="label">{bi("Construyendo", "Building")}</dt><dd>{bi("Nuevos repos sobre Modern Workplace e infraestructura: Teams Rooms, co-management MECM + Intune, Active Directory.", "New repos on Modern Workplace and infrastructure: Teams Rooms, MECM + Intune co-management, Active Directory.")}</dd></div>
      <div class="spec-row"><dt class="label">{bi("Aprendiendo", "Learning")}</dt><dd>{bi("Kubernetes, SRE y operación de clústeres GPU, en laboratorios abiertos.", "Kubernetes, SRE and GPU cluster operations, in open labs.")}</dd></div>
      <div class="spec-row"><dt class="label">{bi("Idiomas", "Languages")}</dt><dd>{bi("Español nativo, inglés a diario y francés en progreso.", "Native Spanish, English every day and French in progress.")}</dd></div>
    </dl>
  </div>
</section>'''
about_body = SEC["about"].replace('class="section dark" id="sobre-mi"', 'class="section dark about-top" id="sobre-mi"') \
    + "\n\n" + now + "\n\n" + SEC["contact"].replace("{{FORM_ACTION}}", FORM).replace("{{CAPTCHA}}", CAPTCHA).replace("{{CAPTCHA_JS}}", CAPTCHA_JS)
sizes["about.html"] = write("about.html", layout(R="", path="about.html", active="about",
    title_en="About · Iñigo González", title_es="Sobre mí · Iñigo González",
    desc="About Iñigo González, IT Site Leader in Madrid, and how to get in touch.", body=about_body))

# links
LINKS = [
    ("blog/", bi("Blog: cómo construí cada proyecto", "Blog: how I built each project"), ""),
    ("journey.html", bi("El viaje: once años en cinco etapas", "The journey: eleven years in five stages"), ""),
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
    desc="Blog, journey, LinkedIn, GitHub and contact for Iñigo González.", body=links_body))

# store (under construction)
sizes["store.html"] = write("store.html", layout(R="", path="store.html", active="store",
    title_en="Store · Iñigo González", title_es="Store · Iñigo González",
    desc="Coming soon.", body=soon("Store", "Store", "")))

data = {"cities": {c["id"]: c for c in CITIES}, "hero": CONF["hero_photos"], "about": CONF.get("about_photo"),
        "formspree": bool(CONF.get("formspree_id")), "ga4": CONF.get("ga4_id", "")}
(SITE / "assets" / "data.js").write_text("window.SITE=" + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n")
print("ok", len(sizes), "pages,", sum(sizes.values()) // 1024, "KB")
