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
    f'''<section class="section">
  <div class="wrap welcome reveal">
    <div>
      <p class="label kicker">IGG-ICS · IT · Tech Career, Lab &amp; Strategy</p>
      <h2 class="h2 sm">{bi("Estrategia profesional IT.", "IT career strategy.")}</h2>
    </div>
    <div>
      <p class="lede">{bi("Un programa de pago para perfiles IT: genera oportunidades con visibilidad, posicionamiento y networking, y no solo enviando currículums.", "A paid programme for IT professionals: create opportunities through visibility, positioning and networking, not just by sending CVs.")}</p>
      <a class="arrow-link" href="asesoria.html">{bi("Ver el programa", "See the programme")} →</a>
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

# advisory (IGG-ICS · IT · Tech Career, Lab & Strategy)
BOOK = CONF.get("booking_url", "")
if BOOK:
    book_btn = f'<a class="btn" href="{BOOK}" target="_blank" rel="noopener">{bi("Reserva una llamada", "Book a call")} ↗</a>'
else:
    book_btn = f'<a class="btn" href="about.html#contacto">{bi("Pide información", "Ask for details")} →</a>'
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
advisory_body = page_hero("IGG-ICS · IT · Tech Career, Lab &amp; Strategy",
    bi("Tu carrera en IT,<br>con estrategia.", "Your IT career,<br>with a strategy."),
    bi("Un programa de estrategia profesional para perfiles IT y tecnológicos, donde te ayudo a generar oportunidades laborales a través de visibilidad, posicionamiento y networking.",
       "A career strategy programme for IT and tech professionals, where I help you create job opportunities through visibility, positioning and networking."),
    f'<p style="margin-top:30px">{book_btn}</p>') + f'''

<section class="section">
  <div class="wrap welcome reveal">
    <div>
      <p class="label kicker">{bi("Por qué", "Why")}</p>
      <h2 class="h2 sm">{bi("Dejar de enviar currículums.", "Stop just sending CVs.")}</h2>
    </div>
    <div>
      <p class="lede">{bi("IGG-ICS nace con el objetivo de enseñar a profesionales IT a dejar de depender únicamente de enviar currículums y empezar a construir una estrategia profesional que genere oportunidades.",
                          "IGG-ICS was created to help IT professionals stop relying only on sending CVs and start building a career strategy that creates opportunities.")}</p>
    </div>
  </div>
</section>

<section class="section" style="background:var(--paper-2)">
  <div class="wrap">
    <p class="label kicker">{bi("Qué trabajamos", "What we work on")}</p>
    <div class="etm-grid">
{etm_cards}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap now-grid">
    <div class="reveal">
      <p class="label kicker">{bi("Cómo funciona", "How it works")}</p>
      <h2 class="h2 sm">{bi("Paso a paso.", "Step by step.")}</h2>
    </div>
    <dl class="spec etm-spec reveal">
      <div class="spec-row"><dt class="label">01 · {bi("Primera llamada", "First call")}</dt><dd>{bi("Hablamos de tu situación, tus objetivos y si el programa encaja contigo.", "We talk about where you are, your goals and whether the programme is a good fit.")}</dd></div>
      <div class="spec-row"><dt class="label">02 · {bi("Plan", "Plan")}</dt><dd>{bi("Te propongo un plan a medida con las áreas que más te van a ayudar.", "I propose a tailored plan with the areas that will help you most.")}</dd></div>
      <div class="spec-row"><dt class="label">03 · {bi("Sesiones y seguimiento", "Sessions and follow-up")}</dt><dd>{bi("Sesiones online con tareas entre una y otra, y seguimiento de los avances.", "Online sessions with work in between, and follow-up on your progress.")}</dd></div>
      <div class="spec-row"><dt class="label">{bi("Formato", "Format")}</dt><dd>{bi("Online, en español o en inglés. Servicio de pago; el precio depende del plan y te lo indico en la primera llamada.", "Online, in Spanish or English. Paid service; the price depends on the plan and I share it on the first call.")}</dd></div>
    </dl>
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
      <p class="muted small" style="margin-top:22px">{bi("Ningún programa puede garantizar una oferta de trabajo. Lo que sí trabajamos es todo lo que depende de ti para que lleguen más y mejores oportunidades.", "No programme can guarantee a job offer. What we do work on is everything that depends on you, so that more and better opportunities come your way.")}</p>
    </div>
  </div>
</section>'''
sizes["asesoria.html"] = write("asesoria.html", layout(R="", path="asesoria.html", active="advisory",
    title_en="IGG-ICS · IT career strategy · Iñigo González", title_es="IGG-ICS · Estrategia profesional IT · Iñigo González",
    desc="IGG-ICS (IT · Tech Career, Lab & Strategy): a paid career strategy programme for IT professionals on visibility, LinkedIn, personal brand, networking, CVs and interviews.", body=advisory_body))

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

<section class="section" style="background:var(--paper-2)">
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
      <p class="lede">{bi("Si prefieres trabajarlo conmigo, paso a paso y con un plan a tu medida, échale un vistazo al programa.", "If you'd rather work on it with me, step by step and with a plan built for you, take a look at the programme.")}</p>
      <a class="btn" href="asesoria.html">{bi("Ver el programa", "See the programme")} →</a>
    </div>
  </div>
</section>
{CAPTCHA_JS}'''
sizes["recursos.html"] = write("recursos.html", layout(R="", path="recursos.html", active="resources",
    title_en="33 ideas to get found in IT · Iñigo González", title_es="33 ideas para que te encuentren en IT · Iñigo González",
    desc="Free resource: 33 ideas for IT professionals to get found on LinkedIn, show their work with projects, network and get through hiring processes. Plus the Tech Career Lab newsletter.", body=resources_body))

# links
LINKS = [
    ("blog/", bi("Blog: cómo construí cada proyecto", "Blog: how I built each project"), ""),
    ("journey.html", bi("El viaje: once años en cinco etapas", "The journey: eleven years in five stages"), ""),
    ("asesoria.html", bi("IGG-ICS: estrategia profesional para perfiles IT", "IGG-ICS: career strategy for IT professionals"), ""),
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
    desc="Blog, journey, LinkedIn, GitHub and contact for Iñigo González.", body=links_body))

# store (under construction)
sizes["store.html"] = write("store.html", layout(R="", path="store.html", active="store",
    title_en="Store · Iñigo González", title_es="Store · Iñigo González",
    desc="Coming soon.", body=soon("Store", "Store", "")))

data = {"cities": {c["id"]: c for c in CITIES}, "hero": CONF["hero_photos"], "about": CONF.get("about_photo"),
        "formspree": bool(CONF.get("formspree_id")), "ga4": CONF.get("ga4_id", "")}
(SITE / "assets" / "data.js").write_text("window.SITE=" + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n")
print("ok", len(sizes), "pages,", sum(sizes.values()) // 1024, "KB")
