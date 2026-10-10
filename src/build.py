"""Build index.html and assets/data.js from src/. Run: python3 src/build.py"""
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
    visual_img = f'<img src="{img["src"]}" alt="{html.escape(img.get("alt",""))}" loading="lazy">' if img else ""
    chips = "".join(f"<li>{html.escape(c)}</li>" for c in s["chips"])
    return f'''      <article class="stage reveal" id="etapa-{s["key"]}">
        <div class="stage-visual{' photo' if img else ''}">
          {visual_img}
          <div class="years"><span>{yrs}</span><span class="tag">{bi(*s["sector"])}</span></div>
          <div class="stage-n" aria-hidden="true">{s["n"]}</div>
          <div class="years"><span>{where}</span></div>
        </div>
        <div class="stage-body">
          <p class="label">{bi("Etapa", "Stage")} {s["n"]} · {yrs}{live}</p>
          <h3>{bi(*s["company"])}</h3>
          <p class="role">{bi(*s["role"])}</p>
          <p>{bi(*s["p"])}</p>
          <p class="muted">{bi(*s["p2"])}</p>
          <ul class="chips">{chips}</ul>
          <a class="arrow-link" href="#mapa" data-filter="{s["key"]}">{bi("Ver en el mapa", "See on the map")} →</a>
        </div>
      </article>'''

# ---------------------------------------------------------------- projects
GH = "https://github.com/inigogonzalezgarcia/"
TOOLS = [
    ("01", "01-finops-cloud-cost-dashboard", "FinOps Cloud Cost Dashboard", "Desviaciones y anomalías de coste en AWS y Azure", "Cloud cost drift and anomalies across AWS and Azure"),
    ("02", "02-intune-compliance-report", "Intune Device Compliance Report", "Cumplimiento de dispositivos visible para IT y dirección", "Endpoint compliance visibility for IT and management"),
    ("03", "03-entra-id-hygiene-audit", "Entra ID Identity Hygiene Audit", "Cuentas inactivas, invitados antiguos y usuarios sin MFA", "Inactive accounts, stale guests and users without MFA"),
    ("04", "04-itsm-kpi-dashboard", "ITSM Service Desk KPI Dashboard", "MTTR, SLA y backlog del service desk", "MTTR, SLA and backlog tracking for service desks"),
    ("05", "05-it-ops-console", "IT Ops Console", "Una vista para las operaciones IT de una sede, con MFA", "One view for on-site IT operations, with MFA"),
]
LABS = [
    ("06", "06-kubernetes-ingress-lab", "Kubernetes Ingress Lab", "Cilium, Envoy Gateway y external-dns", "Cilium, Envoy Gateway and external-dns"),
    ("07", "07-aws-private-connectivity", "AWS Private Connectivity", "PrivateLink y DNS privado con Terraform", "PrivateLink and private DNS with Terraform"),
    ("08", "08-edge-health-slo-monitor", "Edge Health & SLO Monitor", "SLO, presupuesto de error y alertas por burn rate", "SLOs, error budgets and burn-rate alerts"),
    ("09", "09-gpu-node-remediation", "GPU Node Remediation", "Controlador de Kubernetes que drena, repara o pone en cuarentena nodos GPU", "Kubernetes controller that drains, repairs or quarantines GPU nodes"),
    ("10", "10-gpu-fleet-observability", "GPU Fleet Observability", "Métricas DCGM, alertas con runbook y Grafana", "DCGM metrics, alerts with runbooks and Grafana"),
    ("11", "11-gpu-fleet-lifecycle", "GPU Fleet Lifecycle", "Rollouts de drivers con canary, aprobación y rollback", "Driver rollouts with canary, approval and rollback"),
    ("12", "12-gpu-goodput-mtbi", "GPU Goodput & MTBI", "Simulador de fiabilidad de un entrenamiento de 1.024 GPU", "Reliability simulator for a 1,024-GPU training job"),
    ("13", "13-cluster-acceptance-burnin", "Cluster Acceptance & Burn-in", "Del handover a la firma del cliente de un clúster GPU", "From handover to customer sign-off of a GPU cluster"),
    ("14", "14-slurm-gpu-ops", "Slurm GPU Operations", "Health checks, drain y requeue en un clúster Slurm", "Health checks, drain and requeue on a Slurm cluster"),
    ("15", "15-multi-tenant-gpu-scheduling", "Multi-tenant GPU Scheduling", "Cuotas entre equipos con Kueue y KAI Scheduler", "Team quotas with Kueue and KAI Scheduler"),
    ("16", "16-gitops-gpu-fleet", "GitOps GPU Fleet", "GPU Operator promocionado con Flux de staging a prod", "GPU Operator promoted with Flux from staging to prod"),
]

def plist(items):
    out = []
    for n, slug, t, es, en in items:
        out.append(f'<li><a href="{GH}{slug}" target="_blank" rel="noopener"><span class="n">{n}</span><span class="t">{html.escape(t)}<span class="d">{bi(html.escape(es), html.escape(en))}</span></span><span class="go">↗</span></a></li>')
    return "\n".join(out)

PROJECTS = f'''      <div class="proj-group reveal">
        <p class="label muted">01 — 05</p>
        <h3>{bi("Herramientas de IT Ops", "IT Ops tools")}</h3>
        <p class="muted">{bi("Python, PowerShell y Microsoft Graph para problemas del día a día: cumplimiento, identidad, costes y service desk.", "Python, PowerShell and Microsoft Graph for everyday problems: compliance, identity, cost and service desk.")}</p>
        <ul class="proj-list">{plist(TOOLS)}</ul>
      </div>
      <div class="proj-group reveal">
        <p class="label muted">06 — 16</p>
        <h3>{bi("Laboratorios: cloud, SRE y GPU", "Labs: cloud, SRE and GPU")}</h3>
        <p class="muted">{bi("Kubernetes, Terraform, SLO y operación de clústeres GPU, con CI que lo prueba todo de punta a punta.", "Kubernetes, Terraform, SLOs and GPU cluster operations, with CI that tests everything end to end.")}</p>
        <ul class="proj-list">{plist(LABS)}</ul>
      </div>'''

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

# ---------------------------------------------------------------- assemble
tpl = (ROOT / "index.template.html").read_text()
out = (tpl.replace("{{STAGES}}", "\n".join(stage_html(s) for s in STAGES))
          .replace("{{PROJECTS}}", PROJECTS)
          .replace("{{MAP}}", MAP)
          .replace("{{FORM_ACTION}}", f'https://formspree.io/f/{CONF["formspree_id"]}' if CONF.get("formspree_id") else "mailto:inigogonzalezgarcia@yahoo.es"))
assert "{{" not in out
(SITE / "index.html").write_text(out)
data = {"cities": {c["id"]: c for c in CITIES}, "hero": CONF["hero_photos"], "about": CONF.get("about_photo"),
        "formspree": bool(CONF.get("formspree_id")), "ga4": CONF.get("ga4_id", "")}
(SITE / "assets" / "data.js").write_text("window.SITE=" + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n")
print("ok", len(out) // 1024, "KB")
