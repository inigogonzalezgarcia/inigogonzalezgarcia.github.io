# Blog posts: one per GitHub repo. Mini-markup: "## " heading, "- " bullet, blank line = new paragraph, `code`.
# Only facts that are in each repo's README. Labs 06-16 are labs: say so.

CATS = {
    "tools": ("Herramientas de IT Ops", "IT Ops tools"),
    "cloud": ("Laboratorio cloud y SRE", "Cloud & SRE lab"),
    "gpu": ("Laboratorio GPU", "GPU lab"),
    "sim": ("Simulador de soporte IT", "IT support simulator"),
}

POSTS = [
dict(n="01", repo="01-finops-cloud-cost-dashboard", date="2026-09-03", cat="tools",
 title_en="A cloud cost dashboard flags a last-week spike in development EC2 spend in 90 days of synthetic billing",
 title_es="Un panel detecta un pico de gasto en EC2 de desarrollo en la última semana de 90 días de facturación ficticia",
 seo_title_en="Cloud cost anomalies in AWS and Azure · Iñigo González",
 seo_title_es="Desvíos de coste cloud en AWS y Azure · Iñigo González",
 seo_desc="A small Streamlit dashboard for AWS and Azure spend that flags the week that looks wrong.",
 seo_desc_es="Un panel pequeño en Streamlit para el gasto de AWS y Azure que señala la semana que no cuadra.",
 dek_en="The Streamlit dashboard, published with synthetic billing data, puts AWS and Azure spend in one view, compares each week with the one before and flags the week that looks wrong.",
 dek_es="El panel en Streamlit, publicado con datos de facturación ficticios, reúne el gasto de AWS y Azure en una vista, compara cada semana con la anterior y señala la que no cuadra.",
 en="""
In the last week of a 90-day billing history, spend on EC2 in the development environment spikes, and the dashboard flags it with a probable cause and a suggested action: automatic shutdown of idle development instances. That is what the cloud cost dashboard published with this post finds. The billing data is synthetic, and the spike is injected on purpose so the detection has something to find.

Cloud costs rarely explode overnight. They drift: a test environment left running over a weekend, a service scaled up and never scaled down. By the time the monthly invoice arrives, the money is already spent.

## The last 7 days against the previous 7

The dashboard consolidates daily spend across AWS and Azure, with filters by provider, environment and department. Its weekly indicator compares the last 7 days with the previous 7. The demo covers 10 services, 4 departments and 3 environments, built with Python, pandas, Plotly and Streamlit.

## How to use it with real data

The next step is to import the CSV exports from AWS Cost Explorer and Azure Cost Management instead of the synthetic data, add a statistical baseline so each service is compared with its own history, and set budget thresholds per department.

## Where it comes from

I wanted a view that answers three questions fast: how much we spend and where, whether this week is different from last week, and whether anything is clearly out of line.""",
 es="""
En la última semana de un histórico de 90 días de facturación, el gasto en EC2 del entorno de desarrollo se dispara, y el panel lo señala con una causa probable y una acción sugerida: el apagado automático de las instancias de desarrollo ociosas. Así lo detecta el panel de costes cloud que acompaña a este post. Los datos de facturación son ficticios, y el pico se inyecta a propósito para que la detección tenga algo que encontrar.

El gasto cloud casi nunca se dispara de un día para otro. Se desvía poco a poco: un entorno de pruebas encendido todo el fin de semana, un servicio que se escala y nunca se vuelve a bajar. Cuando llega la factura mensual, el dinero ya se ha gastado.

## Los últimos 7 días frente a los 7 anteriores

El panel reúne el gasto diario en AWS y Azure, con filtros por proveedor, entorno y departamento. Su indicador semanal compara los últimos 7 días con los 7 anteriores. La demo cubre 10 servicios, 4 departamentos y 3 entornos, y está hecha con Python, pandas, Plotly y Streamlit.

## Cómo usarlo con datos reales

El siguiente paso es importar las exportaciones CSV de AWS Cost Explorer y Azure Cost Management en lugar de los datos ficticios, añadir una línea base estadística para comparar cada servicio con su propio histórico y fijar umbrales de presupuesto por departamento.

## De dónde sale

Quería una vista que respondiera rápido a tres preguntas: cuánto gastamos y dónde, si esta semana es distinta de la anterior y si hay algo claramente fuera de lugar."""),

dict(n="02", repo="02-intune-compliance-report", date="2026-09-30", updated="2026-11-14", cat="tools",
 title_en="An Intune report turns non-compliant devices into a one-page summary and a list of machines to fix",
 title_es="Un informe de Intune resume en una página los equipos que no cumplen y lista los que hay que arreglar",
 seo_title_en="Intune compliance report with Microsoft Graph · Iñigo González",
 seo_title_es="Informe de cumplimiento de Intune con Graph · Iñigo González",
 seo_desc="PowerShell pulls the devices from Microsoft Graph, Python turns them into a report and an action list.",
 seo_desc_es="PowerShell saca los dispositivos de Microsoft Graph y Python los convierte en un informe y una lista de acciones.",
 dek_en="PowerShell exports the managed devices from Microsoft Graph with read-only access and Python builds the report; the repo ships with a fictional fleet so it runs without a tenant.",
 dek_es="PowerShell exporta los dispositivos gestionados de Microsoft Graph con acceso de solo lectura y Python genera el informe; el repo trae una flota ficticia para funcionar sin tenant.",
 en="""
The Intune portal says a device is non-compliant, but it does not answer in one page how the fleet is doing by operating system and which machines need chasing this week. The compliance report published with this post does: it produces KPIs, compliance by OS, devices to review and OS versions, plus a list of the devices someone actually has to go and fix. The repository runs on a fictional fleet created by a sample-data script, so it works without a tenant, the organisation's own Microsoft cloud environment.

## A read-only export and a separate analysis

A PowerShell script, `Export-IntuneDevices.ps1`, exports the managed devices through Microsoft Graph, Microsoft's programming interface for its cloud services, with a read-only permission. A Python report using only the standard library turns that export into `report.html` and `action_list.csv`. Seven tests cover the logic.

## How to use it with real data

The steps are to create an app registration with read-only Intune permissions in Microsoft Graph, run the export script, point the report at the result, schedule it weekly and send the action list to the team that chases devices.

## Where it comes from

Python plus PowerShell is the split I use for anything Microsoft. Keeping export and analysis apart pays off: the PowerShell side only needs read access, and the Python side can be tested with fake data.""",
 es="""
El portal de Intune dice que un equipo no cumple, pero no responde en una página cómo va la flota por sistema operativo ni a qué equipos hay que perseguir esta semana. El informe de cumplimiento que acompaña a este post sí lo hace: genera KPIs, cumplimiento por sistema operativo, dispositivos a revisar y versiones de SO, además de la lista de equipos que alguien tiene que ir a arreglar. El repositorio funciona con una flota ficticia creada por un script de datos de ejemplo, así que no necesita tenant, el entorno de nube de Microsoft de la organización.

## Una exportación de solo lectura y un análisis aparte

Un script de PowerShell, `Export-IntuneDevices.ps1`, exporta los dispositivos gestionados por Microsoft Graph, la interfaz de programación de los servicios en la nube de Microsoft, con un permiso de solo lectura. Un informe en Python, solo con la librería estándar, convierte esa exportación en `report.html` y `action_list.csv`. Siete tests cubren la lógica.

## Cómo usarlo con datos reales

Los pasos son crear un registro de aplicación con permisos de solo lectura de Intune en Microsoft Graph, ejecutar el script de exportación, generar el informe a partir del resultado, programarlo cada semana y enviar la lista de acciones al equipo que persigue los equipos.

## De dónde sale

Python y PowerShell es el reparto que uso para todo lo de Microsoft. Separar la exportación del análisis compensa: la parte de PowerShell solo necesita permisos de lectura y la de Python se prueba con datos falsos."""),

dict(n="03", repo="03-entra-id-hygiene-audit", date="2026-09-30", cat="tools",
 title_en="An Entra ID audit finds admins without MFA, accounts idle for over 90 days and forgotten guests in one pass",
 title_es="Una auditoría de Entra ID encuentra administradores sin MFA, cuentas inactivas más de 90 días e invitados olvidados",
 seo_title_en="Entra ID audit: MFA gaps and stale accounts · Iñigo González",
 seo_title_es="Auditoría de Entra ID: MFA y cuentas olvidadas · Iñigo González",
 seo_desc="Admins without MFA, inactive members and stale guests, found in one pass.",
 seo_desc_es="Administradores sin MFA, miembros inactivos e invitados obsoletos, en una sola pasada.",
 dek_en="The audit reads users, sign-in activity and MFA registration through Microsoft Graph with read-only permissions and flags four kinds of identity debt.",
 dek_es="La auditoría lee los usuarios, su actividad de inicio de sesión y el registro de MFA por Microsoft Graph con permisos de solo lectura, y señala cuatro tipos de deuda de identidad.",
 en="""
Identity debt builds up quietly: an admin who never registered MFA, the second sign-in step, a leaver whose account is still enabled, guests invited for a project that ended a year ago. The Entra ID audit published with this post finds four of these in one pass: admins without MFA, members without MFA, members inactive for more than 90 days and stale guest accounts.

## Two read-only permissions and a P1 or P2 licence

A PowerShell script, `Export-EntraUsers.ps1`, reads the users, their `signInActivity` and the MFA registration report through Microsoft Graph, using `User.Read.All` and `AuditLog.Read.All`. Sign-in activity needs Entra ID P1 or P2, and the README says so. Python does the analysis and the report, with seven tests.

## How to use it with real data

It needs those two read-only Graph permissions on a tenant with Entra ID P1 or P2. Security should then agree what "inactive" and "stale" mean in the organisation and set the thresholds. Run monthly, each report can be kept as evidence for access reviews.

## Where it comes from

Most of the work was deciding what "inactive" and "stale" mean and writing it down, so the report can be defended when someone asks why their account is on it.""",
 es="""
La deuda de identidad crece sin hacer ruido: un administrador que nunca registró MFA, el segundo paso del inicio de sesión, una baja cuya cuenta sigue activa, invitados de un proyecto que acabó hace un año. La auditoría de Entra ID que acompaña a este post encuentra cuatro de estos casos en una sola pasada: administradores sin MFA, miembros sin MFA, miembros sin actividad en más de 90 días y cuentas de invitado obsoletas.

## Dos permisos de lectura y una licencia P1 o P2

Un script de PowerShell, `Export-EntraUsers.ps1`, lee los usuarios, su `signInActivity` y el informe de registro de MFA por Microsoft Graph, con `User.Read.All` y `AuditLog.Read.All`. La actividad de inicio de sesión requiere Entra ID P1 o P2, y el README lo dice. Python hace el análisis y el informe, con siete tests.

## Cómo usarlo con datos reales

Necesita esos dos permisos de solo lectura en Graph en un tenant con Entra ID P1 o P2. Después, seguridad debe acordar qué significan «inactivo» y «obsoleto» en la organización y fijar los umbrales. Ejecutada cada mes, cada informe puede guardarse como evidencia para las revisiones de acceso.

## De dónde sale

Casi todo el trabajo estuvo en decidir qué significan «inactivo» y «obsoleto» y dejarlo escrito, para poder defender el informe cuando alguien pregunte por qué sale su cuenta."""),

dict(n="04", repo="04-itsm-kpi-dashboard", date="2026-09-30", updated="2026-11-18", cat="tools",
 title_en="A service desk report pulls SLA by priority and the open tickets already out of SLA from a CSV export",
 title_es="Un informe de service desk saca el SLA por prioridad y los tickets abiertos ya fuera de SLA de una exportación CSV",
 seo_title_en="Service desk KPIs: SLA, MTTR and backlog · Iñigo González",
 seo_title_es="KPIs del service desk: SLA, MTTR y backlog · Iñigo González",
 seo_desc="SLA by priority and team, time to resolve, weekly trend and the open tickets already out of SLA.",
 seo_desc_es="SLA por prioridad y por equipo, tiempo de resolución, tendencia semanal y los tickets abiertos ya fuera de SLA.",
 dek_en="The report reads a ServiceNow-style ticket export and produces the same monthly numbers every time: SLA by priority and team, time to resolve, weekly trend and breaches.",
 dek_es="El informe lee una exportación de tickets tipo ServiceNow y genera cada mes las mismas cifras: SLA por prioridad y por equipo, tiempo de resolución, tendencia semanal e incumplimientos.",
 en="""
Every service desk tool has dashboards, but the monthly review usually starts from a CSV export and a spreadsheet. The KPI report published with this post starts from that same export and produces the same numbers every time: SLA compliance by priority and by team, median and mean time to resolve, the weekly trend, and the open tickets already out of SLA, the agreed time to resolve, which it also writes to `sla_breaches.csv`.

## Four hours for a P1, 72 for a P4

The report reads a ServiceNow-style CSV with number, opened, resolved, priority, category, assignment group and state. The default SLA targets are P1 4 h, P2 8 h, P3 24 h and P4 72 h, and the `--sla` option changes them. It runs on Python with the standard library only, and six tests cover it.

## How to use it with real data

Tickets can be exported to CSV from ServiceNow or any other tool, with the columns mapped to the report. Each team sets its own targets per priority with `--sla`, and using the same report every month keeps the numbers comparable.

## Where it comes from

Building it showed me that the median tells a different story from the mean: a few very long tickets move the mean a lot, and the median shows what most users actually live with.""",
 es="""
Todas las herramientas de service desk tienen paneles, pero la revisión mensual suele empezar con una exportación CSV y una hoja de cálculo. El informe de KPIs que acompaña a este post parte de esa misma exportación y genera siempre las mismas cifras: cumplimiento de SLA por prioridad y por equipo, tiempo de resolución mediano y medio, la tendencia semanal y los tickets abiertos que ya superan el SLA, el plazo acordado para resolverlos, que además escribe en `sla_breaches.csv`.

## Cuatro horas para un P1, 72 para un P4

El informe lee un CSV tipo ServiceNow con número, apertura, resolución, prioridad, categoría, grupo asignado y estado. Los objetivos de SLA por defecto son P1 4 h, P2 8 h, P3 24 h y P4 72 h, y la opción `--sla` los cambia. Funciona con Python, solo con la librería estándar, y seis tests lo cubren.

## Cómo usarlo con datos reales

Los tickets se pueden exportar a CSV desde ServiceNow o cualquier otra herramienta, mapeando las columnas al informe. Cada equipo fija sus objetivos por prioridad con `--sla`, y usar el mismo informe cada mes permite comparar las cifras.

## De dónde sale

Al hacerlo comprobé que la mediana cuenta otra historia que la media: unos pocos tickets muy largos mueven mucho la media, y la mediana enseña lo que vive la mayoría de usuarios."""),

dict(n="05", repo="05-it-ops-console", date="2026-09-30", updated="2026-11-17", cat="tools",
 title_en="An on-site IT console brings offline machines, expiring warranties, room checks and joiners into one app",
 title_es="Una consola de IT de sede reúne equipos offline, garantías que caducan, revisión de salas y altas en una sola app",
 seo_title_en="On-site IT ops console: Flask + PowerShell · Iñigo González",
 seo_title_es="Consola de operaciones IT: Flask + PowerShell · Iñigo González",
 seo_desc="Assets, warranties, room checklists, joiners and leavers, shifts and service health in one Flask app.",
 seo_desc_es="Activos, garantías, checklists de salas, altas y bajas, turnos y salud de servicios en una app Flask.",
 dek_en="The Flask app, built from scratch and anonymised, covers assets, warranties, room checklists, joiners and leavers, shifts and service health, with invite-only access and TOTP.",
 dek_es="La app en Flask, hecha desde cero y anonimizada, cubre activos, garantías, checklists de salas, altas y bajas, turnos y salud de servicios, con acceso por invitación y TOTP.",
 en="""
Running a site means keeping a lot of small things in mind at once: which machines are offline, which warranties expire, which rooms were checked this morning, who starts on Monday. The IT operations console published with this post puts all of it in one place. It was built from scratch and anonymised.

## Assets, rooms, people and shifts in one app

The console covers a dashboard, assets (offline, non-compliant, duplicate serials, remote queries), warranties and software. It adds people, floor maps, meeting-room checklists, joiners and leavers, visitors and shifts, plus service health, role-based admin and an audit log.

## Flask for the app, PowerShell for remote queries and an authenticator app to sign in

Access is invite-only. The first admin is created with `bootstrap-admin`, accounts are activated with a 6-character code sent by email, and every sign-in after that needs an authenticator app (TOTP, a one-time code that changes over time). It runs on Flask and SQLite, with PowerShell over CIM/WinRM, Windows remote management, for remote queries. Sixteen tests cover it.

## How to use it with real data

A site needs to connect LDAP for sign-in and SMTP for activation emails, enable WinRM for live device queries, load its asset inventory and floor plans, and adapt the room checklists.

## Where it comes from

I wanted all of a site's small tasks in one place. ARCHITECTURE.md, docs/decisions.md, with my PowerShell and WMI lessons, and docs/security.md explain the choices.""",
 es="""
Llevar una sede es tener muchas cosas pequeñas en la cabeza a la vez: qué equipos están offline, qué garantías caducan, qué salas se han revisado esta mañana, quién empieza el lunes. La consola de operaciones IT que acompaña a este post lo reúne todo en un sitio. Está hecha desde cero y anonimizada.

## Activos, salas, personas y turnos en una sola app

La consola incluye panel, activos (offline, no conformes, seriales duplicados, consultas remotas), garantías y software. Suma personas, planos de planta, checklists de salas, altas y bajas, visitas y turnos, además de salud de servicios, administración por roles y log de auditoría.

## Flask para la app, PowerShell para las consultas remotas y una app autenticadora para entrar

El acceso es solo por invitación. El primer administrador se crea con `bootstrap-admin`, las cuentas se activan con un código de 6 caracteres por email y desde entonces cada inicio de sesión pide app autenticadora (TOTP, un código de un solo uso que cambia con el tiempo). Funciona con Flask y SQLite, con PowerShell por CIM/WinRM, la administración remota de Windows, para las consultas remotas. Dieciséis tests la cubren.

## Cómo usarlo con datos reales

Una sede necesita conectar LDAP para el inicio de sesión y SMTP para los emails de activación, activar WinRM para las consultas en vivo, cargar su inventario de activos y sus planos, y adaptar los checklists de salas.

## De dónde sale

Quería todas las tareas pequeñas de una sede en un solo sitio. ARCHITECTURE.md, docs/decisions.md, con mis lecciones de PowerShell y WMI, y docs/security.md explican las decisiones."""),

dict(n="06", repo="06-kubernetes-ingress-lab", date="2026-10-01", updated="2026-11-11", cat="cloud",
 title_en="A Kubernetes ingress lab is rebuilt from zero in every CI run and passes nine end-to-end tests",
 title_es="Un laboratorio de ingress en Kubernetes se reconstruye desde cero en cada ejecución de CI y pasa nueve pruebas",
 seo_title_en="Kubernetes ingress lab: Cilium and Envoy · Iñigo González",
 seo_title_es="Laboratorio de ingress en Kubernetes: Cilium y Envoy · Iñigo González",
 seo_desc="Cilium, Envoy Gateway, cert-manager and external-dns on kind, with nine end-to-end checks.",
 seo_desc_es="Cilium, Envoy Gateway, cert-manager y external-dns sobre kind, con nueve pruebas de punta a punta.",
 dek_en="The lab runs Cilium, Envoy Gateway, cert-manager and external-dns on kind to show how traffic gets into a cluster today, and GitHub Actions rebuilds and tests it on every run.",
 dek_es="El laboratorio monta Cilium, Envoy Gateway, cert-manager y external-dns sobre kind para mostrar cómo entra hoy el tráfico en un clúster, y GitHub Actions lo reconstruye y prueba en cada ejecución.",
 en="""
A GitHub Actions workflow builds the cluster from scratch and runs nine end-to-end tests, and it has been green in the last four runs. That is the result of the Kubernetes ingress lab published with this post, a lab on how traffic gets into a cluster today: Gateway API instead of the classic Ingress, networking based on eBPF, which runs inside the Linux kernel, and certificates and DNS handled by controllers.

## Cilium replaces kube-proxy and Envoy Gateway takes the traffic

The lab runs on kind with no CNI, the cluster's network plugin, and no kube-proxy; Cilium replaces both, with LB IPAM, L2 announcements, an L7 policy and Hubble. Envoy Gateway handles redirect, TLS and rate limiting through Gateway API.

## A 403 on /env and no way around the gateway

cert-manager issues a wildcard certificate from a lab CA, and external-dns writes to BIND over RFC 2136 with TSIG, using TXT ownership records. The apps namespace denies by default, and an L7 allow-list makes `/env` return 403, with no way around the gateway.

## How to use it with real data

Kind can be replaced with a real cluster, BIND with the DNS provider in external-dns, and the lab CA with ACME or an internal PKI in cert-manager.

## Where it comes from

The lab comes from working with container platforms such as Red Hat OpenShift and Kubernetes on premises. My next step is contributing back: docs or a good first issue in one of these projects.""",
 es="""
Un workflow de GitHub Actions construye el clúster desde cero y pasa nueve pruebas de punta a punta, y ha salido en verde en las cuatro últimas ejecuciones. Es el resultado del laboratorio de ingress en Kubernetes que acompaña a este post, un laboratorio sobre cómo entra hoy el tráfico en un clúster: Gateway API en lugar del Ingress clásico, red con eBPF, que funciona dentro del núcleo de Linux, y certificados y DNS gestionados por controladores.

## Cilium sustituye a kube-proxy y Envoy Gateway recibe el tráfico

El laboratorio corre sobre kind sin CNI, el plugin de red del clúster, y sin kube-proxy; Cilium sustituye a ambos, con LB IPAM, anuncios L2, una política L7 y Hubble. Envoy Gateway se encarga de la redirección, TLS y la limitación de peticiones mediante Gateway API.

## Un 403 en /env y ninguna forma de saltarse el gateway

cert-manager emite un certificado wildcard desde una CA del laboratorio, y external-dns escribe en BIND por RFC 2136 con TSIG y registros TXT de propiedad. El namespace de las apps deniega por defecto, y una lista blanca L7 hace que `/env` devuelva 403, sin forma de saltarse el gateway.

## Cómo usarlo con datos reales

Se puede cambiar kind por un clúster real, BIND por el proveedor de DNS en external-dns, y la CA del laboratorio por ACME o una PKI interna en cert-manager.

## De dónde sale

El laboratorio viene de trabajar con plataformas de contenedores como Red Hat OpenShift y Kubernetes en local. Mi siguiente paso es contribuir de vuelta: documentación o una good first issue en alguno de estos proyectos."""),

dict(n="07", repo="07-aws-private-connectivity", date="2026-10-01", cat="cloud",
 title_en="The pipeline of a private AWS connectivity lab caught a Terraform bug that OpenTofu did not flag",
 title_es="La CI de un laboratorio de conectividad privada en AWS pilló un fallo de Terraform que OpenTofu no marcó",
 seo_title_en="AWS PrivateLink and private DNS with Terraform · Iñigo González",
 seo_title_es="AWS PrivateLink y DNS privado con Terraform · Iñigo González",
 seo_desc="PrivateLink, private DNS and SSM endpoints in five modules, tested without an AWS account.",
 seo_desc_es="PrivateLink, DNS privado y endpoints de SSM en cinco módulos, probados sin cuenta de AWS.",
 dek_en="A lab, tested without an AWS account, builds private access to a service with PrivateLink, private DNS and SSM endpoints in five Terraform modules, and runs them through format, validation, test and security checks.",
 dek_es="Un laboratorio, probado sin cuenta de AWS, monta el acceso privado a un servicio con PrivateLink, DNS privado y endpoints de SSM en cinco módulos de Terraform, y los pasa por comprobaciones de formato, validación, tests y seguridad.",
 en="""
Running the pipeline with Terraform caught a real bug that OpenTofu had not flagged: a `for_each`, the loop that creates one resource per item, over IDs that are still unknown when the plan is calculated. That is what happened in the private connectivity lab for AWS published with this post, a set of five Terraform modules tested without an AWS account. It is a lab, not a production deployment, and the fix is written up in docs/decisions.md.

The pattern the lab builds end to end is a common one: reaching a service privately, with no internet gateway and no NAT, the address translation that lets private machines go out to the internet. The first module creates a private VPC with flow logs, the records of the traffic that crosses it. The second puts an internal NLB, a network load balancer, behind an endpoint service that requires acceptance and explicit principals, so only the listed accounts can connect and each connection has to be approved.

## Five modules, from the endpoint to private DNS

The third module adds an interface endpoint with a narrow security group, the firewall rules attached to it. The fourth creates a private Route 53 zone with an alias and query logs, so the service is reached by name inside the network. The fifth adds SSM and S3 endpoints, plus a lab with two test instances that use IMDSv2, have no public IP and are reached through Session Manager.

## Five tests with a mocked provider and a cost of $0.11 an hour

The modules are tested with `terraform test` against a mocked AWS provider, 5 tests that need no account. A GitHub Actions pipeline runs fmt, validate, test and tfsec, a security scanner for Terraform code, and all of them are green. The estimated cost of running the lab is about $0.11 an hour.

## How to use it with real data

The next step is `terraform apply` in a sandbox AWS account, plugging in your own VPCs, allowed principals and private DNS zone. The CI checks, fmt, validate, test and tfsec, are meant to stay in the pipeline.

## Where it comes from

I built the lab from operating a hybrid AWS and Azure environment, where reaching a service privately, with no internet gateway and no NAT, is a common need.""",
 es="""
La CI con Terraform encontró un fallo real que OpenTofu no había marcado: un `for_each`, el bucle que crea un recurso por cada elemento, sobre IDs que todavía no se conocen cuando se calcula el plan. Es lo que pasó en el laboratorio de conectividad privada en AWS que acompaña a este post, un conjunto de cinco módulos de Terraform probados sin cuenta de AWS. Es un laboratorio, no un despliegue en producción, y la corrección está explicada en docs/decisions.md.

El patrón que monta el laboratorio de principio a fin es habitual: llegar a un servicio de forma privada, sin internet gateway y sin NAT, la traducción de direcciones que deja salir a internet a las máquinas privadas. El primer módulo crea una VPC privada con flow logs, los registros del tráfico que la cruza. El segundo coloca un NLB interno, un balanceador de red, detrás de un endpoint service que exige aceptación y principals explícitos, de modo que solo se conectan las cuentas de la lista y cada conexión hay que aprobarla.

## Cinco módulos, del endpoint al DNS privado

El tercer módulo añade un interface endpoint con un security group estrecho, las reglas de cortafuegos asociadas. El cuarto crea una zona privada de Route 53 con alias y logs de consultas, para llegar al servicio por nombre dentro de la red. El quinto añade endpoints de SSM y S3, más un laboratorio con dos instancias de prueba que usan IMDSv2, no tienen IP pública y se manejan con Session Manager.

## Cinco tests con el proveedor simulado y un coste de 0,11 $ la hora

Los módulos se prueban con `terraform test` sobre el proveedor de AWS simulado, 5 tests que no necesitan cuenta. Un pipeline de GitHub Actions pasa fmt, validate, test y tfsec, un analizador de seguridad para código de Terraform, y todo está en verde. Tener el laboratorio encendido cuesta unos 0,11 $ la hora.

## Cómo usarlo con datos reales

El siguiente paso es ejecutar `terraform apply` en una cuenta de AWS de pruebas y conectar tus VPC, los principals permitidos y tu zona DNS privada. Las comprobaciones de CI, fmt, validate, test y tfsec, están pensadas para quedarse en el pipeline.

## De dónde sale

Monté el laboratorio a partir de operar un entorno híbrido con AWS y Azure, donde llegar a un servicio de forma privada, sin internet gateway y sin NAT, es una necesidad habitual."""),

dict(n="08", repo="08-edge-health-slo-monitor", date="2026-10-01", cat="cloud",
 title_en="An edge monitoring lab wakes someone only when the error budget burns too fast, not on every failed check",
 title_es="Un laboratorio de monitorización del edge solo despierta a alguien cuando el presupuesto de error se quema rápido",
 seo_title_en="SLOs and burn-rate alerts in Python · Iñigo González",
 seo_title_es="SLO y alertas por burn rate en Python · Iñigo González",
 seo_desc="DNS, TLS, HTTP and TCP probes, an error budget and a fictional postmortem.",
 seo_desc_es="Sondas DNS, TLS, HTTP y TCP, un presupuesto de error y un postmortem ficticio.",
 dek_en="A lab in plain Python probes DNS, TLS, HTTP and TCP, tracks an SLO with an error budget and alerts on burn rate; it comes with a fictional postmortem of a DNS record lost in a zone migration.",
 dek_es="Un laboratorio en Python sin dependencias lanza sondas DNS, TLS, HTTP y TCP, sigue un SLO con presupuesto de error y avisa por burn rate; incluye un postmortem ficticio de un registro DNS perdido en una migración de zona.",
 en="""
A failed check at the edge, the part of a service closest to its users, does not have to wake anyone up. The edge health monitor published with this post only alerts when the error budget, the amount of failure an SLO (service level objective) allows, is being spent too fast. It is a lab written in Python, and its example incident is fictional: a DNS record lost during a zone migration, written up as a postmortem.

The approach is the one SRE teams use, applied to the edge. The tool runs DNS, TLS, HTTP and TCP probes and measures them against an SLO with an error budget. The alerts look at the burn rate, the speed at which that budget is consumed, over several time windows at once, and they wait for a minimum number of bad probes before firing.

## Results to Elasticsearch, Prometheus and a signed webhook

The results go out in several formats. The tool exports them to Elasticsearch in ECS, the Elastic Common Schema, and to Prometheus, sends a signed webhook so the receiver can check where it comes from, and builds an HTML report. The repository also includes a postmortem template next to the fictional one about the lost DNS record.

## Python 3.11, no dependencies and 14 tests

The lab runs on Python 3.11 with the standard library only, so there is nothing else to install. It has 14 tests.

## How to use it with real data

The results can be sent to an existing Elasticsearch or Prometheus. The systemd units are meant to be installed on a small VM close to the users, and the signed webhook can be connected to n8n, Teams or Slack. The SLOs have to be agreed with the service owners.

## Where it comes from

The lab comes from my years of monitoring and alert response with tools such as Grafana, SolarWinds and the Elastic stack.""",
 es="""
Una comprobación fallida en el edge, la parte de un servicio más cercana a sus usuarios, no tiene por qué despertar a nadie. El monitor de salud del edge que acompaña a este post solo avisa cuando el presupuesto de error, la cantidad de fallo que permite un SLO (objetivo de nivel de servicio), se está consumiendo demasiado rápido. Es un laboratorio escrito en Python, y su incidente de ejemplo es ficticio: un registro DNS perdido en una migración de zona, contado como postmortem.

El enfoque es el de los equipos SRE, aplicado al edge. La herramienta lanza sondas DNS, TLS, HTTP y TCP y las mide frente a un SLO con presupuesto de error. Las alertas miran el burn rate, la velocidad a la que se gasta ese presupuesto, en varias ventanas de tiempo a la vez, y esperan a un mínimo de sondas malas antes de avisar.

## Resultados a Elasticsearch, Prometheus y un webhook firmado

Los resultados salen en varios formatos. La herramienta los exporta a Elasticsearch en ECS, el esquema común de Elastic, y a Prometheus, envía un webhook firmado para que quien lo recibe pueda comprobar su origen y genera un informe HTML. El repositorio incluye además una plantilla de postmortem junto al ficticio del registro DNS perdido.

## Python 3.11, sin dependencias y 14 tests

El laboratorio funciona con Python 3.11 y solo la librería estándar, así que no hay nada más que instalar. Tiene 14 tests.

## Cómo usarlo con datos reales

Los resultados pueden enviarse a un Elasticsearch o un Prometheus existentes. Las units de systemd están pensadas para instalarse en una VM pequeña cerca de los usuarios, y el webhook firmado se puede conectar a n8n, Teams o Slack. Los SLO hay que acordarlos con los responsables del servicio.

## De dónde sale

El laboratorio viene de mis años de monitorización y respuesta a alertas con herramientas como Grafana, SolarWinds y el stack de Elastic."""),

dict(n="09", repo="09-gpu-node-remediation", date="2026-10-01", cat="gpu",
 title_en="A Kubernetes lab drains, repairs or quarantines GPU nodes on their own, and passed 28 checks first time",
 title_es="Un laboratorio de Kubernetes drena, repara o aísla nodos GPU por sí solo y pasa 28 pruebas a la primera",
 seo_title_en="Kubernetes GPU node remediation controller · Iñigo González",
 seo_title_es="Controlador de remediación de nodos GPU · Iñigo González",
 seo_desc="First GPU lab: XID errors, ECC and temperature drive each node through a state machine.",
 seo_desc_es="Primer laboratorio de GPU: los XID, el ECC y la temperatura llevan cada nodo por una máquina de estados.",
 dek_en="The first of a series of GPU labs, run on simulated GPUs: a Kubernetes controller reads XID errors, ECC and temperature and moves each node through a state machine, from draining to repair, validation or quarantine.",
 dek_es="Primero de una serie de laboratorios de GPU, con GPU simuladas: un controlador de Kubernetes lee los errores XID, el ECC y la temperatura y lleva cada nodo por una máquina de estados, del drenado a la reparación, la validación o la cuarentena.",
 en="""
A Kubernetes controller that decides on its own whether a GPU node should be drained, repaired, cordoned or quarantined passed an end-to-end test of 8 scenarios and 28 checks on its first run. It is the first of a series of GPU labs published with this post, and it runs on simulated GPUs, so anyone can reproduce it on a laptop.

The controller reads DCGM metrics, the health data NVIDIA exposes for its GPUs: XID errors, the error codes the driver reports, double-bit ECC memory errors, row remapping and temperature. With them it moves each node through Healthy, Draining, Repairing, Validating and back to Healthy, or to Cordoned for thermal issues, or to Quarantined. It is written in Go with the standard library only, without client-go, the usual Kubernetes library.

## A budget of nodes in repair and evictions that respect the workloads

The state is kept in annotations on each node, and a budget, max-unavailable, limits how many nodes can be in remediation at once. Evictions respect PodDisruptionBudgets, the limits that stop too many copies of an application going down together. Validation runs as a Job pinned to the node and using all its GPUs. The controller adds a repeat-offender rule, a dry-run mode, events and Prometheus metrics, and its XID policy is based on NVIDIA's documentation, summarised in docs/xid-policy.md.

## A simulator in place of the real GPUs

A simulator called `gpu-sim` stands in for dcgm-exporter, the component that publishes the GPU metrics. The CI runs unit tests, shellcheck and the end-to-end test on kind, a Kubernetes cluster that runs in containers. A `gpuremediate check` mode uses nvidia-smi on a real GPU.

## How to use it with real data

On a cluster with GPUs, dcgm-exporter replaces the simulator. The recommended start is dry-run mode with the max-unavailable budget set. `gpuremediate check` runs on any machine with `nvidia-smi`, including a Windows workstation.

## Where it comes from

The lab comes from my work in hardware operations: validating and certifying servers, and automating the detection and remediation of hardware failures. This series applies that to GPU fleets.""",
 es="""
Un controlador de Kubernetes que decide por sí solo si un nodo GPU hay que drenarlo, repararlo, acordonarlo o ponerlo en cuarentena pasó a la primera una prueba de punta a punta con 8 escenarios y 28 comprobaciones. Es el primero de una serie de laboratorios de GPU que acompaña a este post, y funciona con GPU simuladas, así que cualquiera puede reproducirlo en un portátil.

El controlador lee las métricas DCGM, los datos de salud que NVIDIA expone de sus GPU: los errores XID, los códigos de error que comunica el driver, los errores ECC de doble bit en memoria, el row remapping y la temperatura. Con ellos lleva cada nodo por Healthy, Draining, Repairing, Validating y de vuelta a Healthy, o a Cordoned por temperatura, o a Quarantined. Está escrito en Go solo con la librería estándar, sin client-go, la librería habitual de Kubernetes.

## Un presupuesto de nodos en reparación y evicciones que respetan las cargas

El estado vive en anotaciones de cada nodo, y un presupuesto, max-unavailable, limita cuántos nodos pueden estar en remediación a la vez. Las evicciones respetan los PodDisruptionBudget, los límites que impiden que caigan a la vez demasiadas copias de una aplicación. La validación es un Job fijado al nodo que usa todas sus GPU. El controlador añade una regla de reincidencia, un modo dry-run, eventos y métricas de Prometheus, y su política de XID se basa en la documentación de NVIDIA, resumida en docs/xid-policy.md.

## Un simulador en lugar de las GPU reales

Un simulador llamado `gpu-sim` hace de dcgm-exporter, el componente que publica las métricas de las GPU. La CI pasa tests unitarios, shellcheck y la prueba de punta a punta en kind, un clúster de Kubernetes que corre en contenedores. Un modo `gpuremediate check` usa nvidia-smi en una GPU real.

## Cómo usarlo con datos reales

En un clúster con GPU, dcgm-exporter sustituye al simulador. Lo recomendable es empezar en modo dry-run y con el presupuesto max-unavailable fijado. `gpuremediate check` funciona en cualquier máquina con `nvidia-smi`, también en un puesto Windows.

## De dónde sale

El laboratorio viene de mi trabajo en operación de hardware: validar y certificar servidores, y automatizar la detección y la reparación de fallos de hardware. Esta serie lo lleva a las flotas de GPU."""),

dict(n="10", repo="10-gpu-fleet-observability", date="2026-10-01", cat="gpu",
 title_en="A GPU fleet monitoring lab gives each of its 10 alerts a runbook and an action: drain, quarantine or cordon",
 title_es="Un laboratorio de monitorización de GPU da a cada una de sus 10 alertas un runbook y una acción a seguir",
 seo_title_en="GPU fleet observability with dcgm-exporter · Iñigo González",
 seo_title_es="Observabilidad de una flota GPU con dcgm-exporter · Iñigo González",
 seo_desc="Recording rules, alerts with runbooks, Alertmanager routing and a Grafana dashboard on DCGM metrics.",
 seo_desc_es="Recording rules, alertas con runbook, rutas de Alertmanager y un dashboard de Grafana sobre métricas DCGM.",
 dek_en="A lab on a simulated fleet of 4 nodes with 8 GPUs each turns DCGM metrics into recording rules, alerts with runbooks, Alertmanager routes and a Grafana dashboard, and passed 32 checks on its first run.",
 dek_es="Un laboratorio sobre una flota simulada de 4 nodos con 8 GPU cada uno convierte las métricas DCGM en recording rules, alertas con runbook, rutas de Alertmanager y un dashboard de Grafana, y pasó 32 comprobaciones a la primera.",
 en="""
Each of the 10 alerts in the GPU fleet monitoring lab published with this post says what to do: it comes with a runbook, the written procedure to follow, and an `action` label that reads drain, quarantine or cordon. The lab runs on a simulated fleet, and the question it answers is which NVIDIA DCGM metrics deserve an alert and who should get it.

The simulator, written in Go, models 4 nodes with 8 GPUs each. It uses the same metric names and labels as dcgm-exporter, the component that publishes GPU metrics, pod and namespace included, and it can inject faults. On top of those metrics sit 17 recording rules, queries that Prometheus calculates in advance, and the 10 alerts, documented in docs/alerts.md.

## A broken GPU does not also report itself as idle

Alertmanager sends each alert down one of three routes: the pager, a ticket or the team. Inhibitions, rules that silence one alert when another is firing, stop a broken GPU from also telling the team it is an idle GPU. A script generates the Grafana dashboard, and a tool called `fleetreport` adds up GPU-hours and idle GPU-hours per namespace.

## 32 checks green on the first run

The tests combine 7 `promtool test rules` cases, Go tests, configuration checks, shellcheck and an end-to-end run with Docker Compose that brings up Prometheus, Alertmanager and Grafana: 32 checks, green on the first run. One check needed a fix: comparing energy with power gave false failures with a single sample because of scrape jitter, the small variation in when metrics are collected. It now uses 1 minute of rate over 2 minutes of data.

## How to use it with real data

The simulator is replaced by dcgm-exporter on real nodes. The Grafana dashboard and the recording rules can be imported, and the Alertmanager alerts routed to the on-call and ticketing tools already in use.

## Where it comes from

The lab builds on my years of monitoring and building Grafana dashboards.""",
 es="""
Cada una de las 10 alertas del laboratorio de monitorización de una flota de GPU que acompaña a este post dice qué hacer: lleva un runbook, el procedimiento escrito que hay que seguir, y una etiqueta `action` que indica drain, quarantine o cordon. El laboratorio funciona sobre una flota simulada, y la pregunta que responde es qué métricas de NVIDIA DCGM merecen una alerta y quién debe recibirla.

El simulador, escrito en Go, reproduce 4 nodos con 8 GPU cada uno. Usa los mismos nombres y etiquetas de métricas que dcgm-exporter, el componente que publica las métricas de las GPU, pod y namespace incluidos, y permite inyectar fallos. Sobre esas métricas hay 17 recording rules, consultas que Prometheus calcula por adelantado, y las 10 alertas, documentadas en docs/alerts.md.

## Una GPU rota no avisa además de que está ociosa

Alertmanager manda cada alerta por una de tres rutas: la guardia, un ticket o el equipo. Las inhibiciones, reglas que silencian una alerta cuando salta otra, evitan que una GPU rota avise además al equipo de «GPU ociosa». Un script genera el dashboard de Grafana, y una herramienta llamada `fleetreport` suma las GPU-horas y las GPU-horas ociosas por namespace.

## 32 comprobaciones en verde a la primera

Las pruebas combinan 7 casos de `promtool test rules`, tests en Go, comprobaciones de configuración, shellcheck y una prueba de punta a punta con Docker Compose que levanta Prometheus, Alertmanager y Grafana: 32 comprobaciones, en verde a la primera. Una comprobación necesitó un arreglo: comparar energía con potencia daba falsos fallos con una sola muestra por el jitter del scrape, la pequeña variación en el momento en que se recogen las métricas. Ahora usa 1 minuto sobre 2 minutos de datos.

## Cómo usarlo con datos reales

El simulador se sustituye por dcgm-exporter en los nodos reales. El dashboard de Grafana y las recording rules se pueden importar, y las alertas de Alertmanager se enrutan a las herramientas de guardia y de tickets que ya se usen.

## De dónde sale

El laboratorio se apoya en mis años de monitorización y de cuadros de Grafana."""),

dict(n="11", repo="11-gpu-fleet-lifecycle", date="2026-10-02", cat="gpu",
 title_en="A driver rollout lab for GPU fleets stops a bad driver at the canary and rolls back on its own after an XID",
 title_es="Un laboratorio de despliegue de drivers de GPU frena un driver malo en el canary y da marcha atrás solo",
 seo_title_en="GPU driver rollout: canary and rollback · Iñigo González",
 seo_title_es="Despliegue de drivers GPU: canary y rollback · Iñigo González",
 seo_desc="A Go controller that upgrades nodes in batches and backs out on its own when something breaks.",
 seo_desc_es="Un controlador en Go que actualiza nodos por lotes y da marcha atrás solo cuando algo falla.",
 dek_en="A lab with a Go controller that upgrades the GPU driver across a fleet in batches, with a canary, human approval and a failure budget, and rolls back or quarantines a node when something breaks.",
 dek_es="Un laboratorio con un controlador en Go que actualiza el driver de GPU de la flota por lotes, con canary, aprobación humana y presupuesto de fallos, y vuelve atrás o aísla el nodo cuando algo falla.",
 en="""
A bad GPU driver stopped at the canary, the first small group of nodes to get a new version, and a hardware XID error during the soak that ended in an automatic rollback: both are among the 26 checks the driver rollout lab published with this post passed on its first run. It is a lab. In production the GPU Operator's own upgrade controller does this job; the lab shows what that controller has to get right.

The controller, written in Go with the standard library only, rolls a driver version across the fleet. Each node goes through Draining, Installing, Validating, Soaking and Done. During the soak, the period of watching the node after the upgrade, a hardware XID error or an ECC memory error counts as a failure. The node then goes back to the previous version, and if that also fails, it is quarantined with the label from lab 09.

## A canary, human approval and a budget for failures

The rollout needs human approval, given by rollout name, and advances in batches, inside a maintenance window, with pause and abort and a failure budget. The maxUnavailable limit also counts nodes that are out for other reasons, such as the quarantine and remediation from lab 09.

## A plan where unknown fields are errors

The plan lives in a ConfigMap, a Kubernetes configuration object, that is validated before use and where unknown fields are errors. The CI runs 12 controller unit tests, shellcheck and an end-to-end test on kind, a Kubernetes cluster in containers, with 4 workers. Besides the bad driver and the XID with rollback, the 26 checks cover a closed maintenance window.

## How to use it with real data

The lab is a place to rehearse a rollout policy: canary, approval, batches and rollback. The same policy is then applied with the GPU Operator's upgrade controller on real clusters, reusing the quarantine label from lab 09 so a node that fails twice is taken out of service.

## Where it comes from

The lab builds on my experience in release management: planning, testing, rollback and validation after each release.""",
 es="""
Un driver de GPU defectuoso frenado en el canary, el primer grupo pequeño de nodos que recibe una versión nueva, y un error XID de hardware durante el soak que acabó en una vuelta atrás automática: las dos cosas están entre las 26 comprobaciones que pasó a la primera el laboratorio de despliegue de drivers que acompaña a este post. Es un laboratorio. En producción lo hace el controlador de actualización del propio GPU Operator; el laboratorio enseña lo que ese controlador tiene que hacer bien.

El controlador, escrito en Go solo con la librería estándar, despliega una versión de driver por la flota. Cada nodo pasa por Draining, Installing, Validating, Soaking y Done. Durante el soak, el periodo en que se vigila el nodo tras la actualización, un XID de hardware o un error ECC de memoria cuenta como fallo. Entonces el nodo vuelve a la versión anterior y, si eso también falla, queda en cuarentena con la etiqueta del laboratorio 09.

## Canary, aprobación humana y un presupuesto de fallos

El despliegue necesita aprobación humana, que se da por nombre de rollout, y avanza por lotes, dentro de una ventana de mantenimiento, con pausa y aborto y un presupuesto de fallos. El límite maxUnavailable cuenta también los nodos que están fuera por otros motivos, como la cuarentena y la remediación del laboratorio 09.

## Un plan donde los campos desconocidos son error

El plan vive en un ConfigMap, un objeto de configuración de Kubernetes, que se valida antes de usarlo y donde los campos desconocidos son error. La CI pasa 12 tests unitarios del controlador, shellcheck y una prueba de punta a punta en kind, un clúster de Kubernetes en contenedores, con 4 workers. Además del driver malo y del XID con rollback, las 26 comprobaciones cubren una ventana de mantenimiento cerrada.

## Cómo usarlo con datos reales

El laboratorio sirve para ensayar una política de despliegue: canary, aprobación, lotes y vuelta atrás. Esa misma política se aplica luego con el controlador de actualización del GPU Operator en los clústeres reales, reutilizando la etiqueta de cuarentena del laboratorio 09 para que un nodo que falla dos veces salga de servicio.

## De dónde sale

El laboratorio se apoya en mi experiencia en gestión de releases: planificación, pruebas, vuelta atrás y validación después de cada despliegue."""),

dict(n="12", repo="12-gpu-goodput-mtbi", date="2026-10-02", cat="gpu",
 title_en="Without spare nodes, a simulated 1,024-GPU training job keeps only 36.1 % of its GPU-hours doing useful work",
 title_es="Sin nodos de repuesto, un entrenamiento simulado de 1.024 GPU solo aprovecha el 36,1 % de sus GPU-horas",
 seo_title_en="GPU goodput and MTBI simulator · Iñigo González",
 seo_title_es="Simulador de goodput y MTBI en GPU · Iñigo González",
 seo_desc="A 1,024-GPU training job, simulated with failures, to see what checkpoints, spares and fast detection are worth.",
 seo_desc_es="Un entrenamiento de 1.024 GPU simulado con fallos, para ver cuánto valen los checkpoints, los spares y la detección rápida.",
 dek_en="A lab simulates a 1,024-GPU training job with failures to measure what checkpoints, spare nodes and fast detection are worth, and splits every GPU-hour by where it goes.",
 dek_es="Un laboratorio simula un entrenamiento de 1.024 GPU con fallos para medir cuánto valen los checkpoints, los nodos de repuesto y la detección rápida, y reparte cada GPU-hora según adónde va.",
 en="""
A training job on 1,024 GPUs without spare nodes keeps only 36.1 % goodput, the share of its GPU-hours that goes into useful work, against 79.6 % in the baseline and 94.0 % when every improvement is combined. That is what the goodput simulator published with this post finds. It is a lab: the job and its failures are simulated, with assumptions placed between two public references, Llama 3's interruption count and Meta's paper on cluster reliability.

In a large training job failures are normal; what matters is how much useful work survives them. The simulator is discrete-event, meaning it jumps from one event to the next, and models a job of 1,024 GPUs on 128 nodes with spares, failure causes that each have their own detection time, and repairs.

## Seven scenarios, 20 seeds each

Each scenario runs with 20 seeds, different random starting points. The baseline reaches 79.6 %. Checkpointing at Daly's interval raises it to 85.1 %, and asynchronous checkpoints, saved without stopping the job, to 91.7 %. A firmware regression drops it to 73.5 %, removing the spares sinks it to 36.1 %, and everything combined reaches 94.0 %.

## Every GPU-hour, charged to a cause

An analyser reads a JSONL event log and splits every GPU-hour into productive time, checkpoints, lost work, detection, waiting for nodes and restart, charging the cost to each failure cause. It also calculates MTBI, the mean time between interruptions, and MTBF per node, applies the Young and Daly formulas for the checkpoint interval, tracks a goodput SLO with an error budget and produces an HTML report with SVG charts. It has 34 unit tests on Python 3.11 to 3.13, and a CI job regenerates docs/results.md and fails if it changes.

## How to use it with real data

Job events exported in the documented JSONL format show where the GPU-hours of a real job go. The Young and Daly formulas help tune the checkpoint interval, and goodput can be tracked as an SLO with an error budget.

## Where it comes from

The lab builds on my work in availability and capacity management and on post-incident reviews.""",
 es="""
Un entrenamiento con 1.024 GPU y sin nodos de repuesto se queda en un 36,1 % de goodput, la parte de sus GPU-horas que se dedica a trabajo útil, frente al 79,6 % del escenario base y el 94,0 % cuando se combinan todas las mejoras. Así lo calcula el simulador de goodput que acompaña a este post. Es un laboratorio: el trabajo y sus fallos son simulados, con supuestos situados entre dos referencias públicas, las interrupciones de Llama 3 y el paper de Meta sobre fiabilidad de clústeres.

En un entrenamiento grande los fallos son normales; lo que importa es cuánto trabajo útil sobrevive a ellos. El simulador es de eventos discretos, es decir, salta de un suceso al siguiente, y reproduce un trabajo de 1.024 GPU en 128 nodos con spares, causas de fallo con su propio tiempo de detección y reparaciones.

## Siete escenarios con 20 semillas cada uno

Cada escenario se ejecuta con 20 semillas, puntos de partida aleatorios distintos. El escenario base llega al 79,6 %. Hacer checkpoints con el intervalo de Daly lo sube al 85,1 %, y los checkpoints asíncronos, guardados sin parar el trabajo, al 91,7 %. Una regresión de firmware lo baja al 73,5 %, quitar los spares lo hunde al 36,1 % y todo combinado llega al 94,0 %.

## Cada GPU-hora, cargada a una causa

Un analizador lee un log de eventos JSONL y reparte cada GPU-hora en tiempo productivo, checkpoint, trabajo perdido, detección, espera de nodos y reinicio, y carga el coste a cada causa de fallo. Calcula además el MTBI, el tiempo medio entre interrupciones, y el MTBF por nodo, aplica las fórmulas de Young y Daly para el intervalo de checkpoint, sigue un SLO de goodput con presupuesto de error y genera un informe HTML con gráficos SVG. Tiene 34 tests unitarios en Python 3.11 a 3.13, y un job de CI regenera docs/results.md y falla si cambia.

## Cómo usarlo con datos reales

Los eventos de un trabajo exportados en el formato JSONL documentado muestran adónde van sus GPU-horas reales. Las fórmulas de Young y Daly ayudan a ajustar el intervalo de checkpoints, y el goodput se puede seguir como un SLO con presupuesto de error.

## De dónde sale

El laboratorio se apoya en mi trabajo en gestión de disponibilidad y capacidad y en las revisiones post-incidente."""),

dict(n="13", repo="13-cluster-acceptance-burnin", date="2026-10-04", cat="gpu",
 title_en="A fictional GPU cluster fails acceptance with 144 of 256 GPUs and passes with 248 after a second round",
 title_es="Un clúster de GPU ficticio no supera la aceptación con 144 de 256 GPU y la pasa con 248 en una segunda ronda",
 seo_title_en="GPU cluster acceptance and burn-in tests · Iñigo González",
 seo_title_es="Aceptación y burn-in de un clúster GPU · Iñigo González",
 seo_desc="Inventory, diagnostics, NCCL tests and a 72-hour burn-in, ending in a report a customer can sign.",
 seo_desc_es="Inventario, diagnósticos, pruebas NCCL y un burn-in de 72 horas, con un informe que el cliente puede firmar.",
 dek_en="A lab that takes a new GPU cluster from handover to sign-off: inventory, diagnostics, NCCL tests and a 72-hour burn-in, run on a fictional cluster and ending in a report the customer can sign.",
 dek_es="Un laboratorio que lleva un clúster de GPU nuevo de la entrega a la firma: inventario, diagnósticos, pruebas NCCL y un burn-in de 72 horas, ejecutado sobre un clúster ficticio y con un informe que el cliente puede firmar.",
 en="""
A new 256-GPU cluster fails its first acceptance round with only 144 GPUs ready and passes the second with 248, with one node still waiting on an RMA, the return of a faulty part to the manufacturer. That is the result of the acceptance lab published with this post. It runs on a fictional cluster of 4 racks, 8 nodes per rack and 8 GPUs per node, with 8 defects.

The pipeline checks each node in order: an inventory of GPUs, driver, VBIOS (the GPU firmware) and InfiniBand ports, the network that links the nodes; the `dcgmi diag -r 3` diagnostic; nccl-tests, which measure communication between GPUs, per node and then per rack; a 72-hour burn-in, a sustained load test; and a burn-in job across the whole cluster, scored with the rules of lab 12.

## Every failure gets a disposition, an owner and a next step

A node stops at its first failure. Each failure is classed as RMA, firmware, fabric, facility, investigate or collect evidence, and gets an owner and a next step. The criteria live in criteria.toml, where any unknown key is an error, and a second round replaces the evidence of the first.

## A report with a signature table

The customer gets report.md and report.html with the verdict, a rack-by-node grid, the punch list of pending items, the criteria and a signature table, plus punch-list.csv and result.json. The lab has 25 tests and a CI job that runs both rounds and requires NOT READY first and READY after.

## How to use it with real data

Write the acceptance criteria in `criteria.toml`, collect the real `dcgmi diag` and nccl-tests output with the commands that `accept plan` prints, and hand the HTML report and the punch list to the customer for sign-off.

## Where it comes from

Accepting new hardware and running go-live and service-acceptance reviews are part of my IT operations work. This lab applies the same discipline to a GPU cluster, from handover to the customer's signature.""",
 es="""
Un clúster nuevo de 256 GPU no supera la primera ronda de aceptación, con solo 144 GPU listas, y pasa la segunda con 248, con un nodo aún pendiente de un RMA, la devolución de una pieza defectuosa al fabricante. Es el resultado del laboratorio de aceptación que acompaña a este post. Se ejecuta sobre un clúster ficticio de 4 racks, 8 nodos por rack y 8 GPU por nodo, con 8 defectos.

El proceso revisa cada nodo por orden: un inventario de GPU, driver, VBIOS (el firmware de la GPU) y puertos InfiniBand, la red que une los nodos; el diagnóstico `dcgmi diag -r 3`; nccl-tests, que miden la comunicación entre GPU, primero por nodo y después por rack; un burn-in de 72 horas, una prueba de carga sostenida; y un trabajo de burn-in de todo el clúster, medido con las reglas del laboratorio 12.

## Cada fallo tiene disposición, responsable y siguiente paso

Un nodo se para en su primer fallo. Cada fallo se clasifica como RMA, firmware, fabric, instalaciones, investigar o recoger evidencia, y recibe un responsable y un siguiente paso. Los criterios están en criteria.toml, donde cualquier clave desconocida es un error, y una segunda ronda sustituye la evidencia de la primera.

## Un informe con tabla de firmas

El cliente recibe report.md y report.html con el veredicto, una rejilla rack × nodo, la lista de pendientes, los criterios y una tabla de firmas, además de punch-list.csv y result.json. El laboratorio tiene 25 tests y un job de CI que corre las dos rondas y exige primero NO LISTO y después LISTO.

## Cómo usarlo con datos reales

Hay que escribir los criterios de aceptación en `criteria.toml`, recoger la salida real de `dcgmi diag` y de nccl-tests con los comandos que imprime `accept plan`, y entregar al cliente el informe HTML y la lista de pendientes para la firma.

## De dónde sale

Aceptar hardware nuevo y llevar revisiones de puesta en producción y de aceptación del servicio forman parte de mi trabajo en operaciones IT. Este laboratorio aplica la misma disciplina a un clúster de GPU, de la entrega a la firma del cliente."""),

dict(n="14", repo="14-slurm-gpu-ops", date="2026-10-04", cat="gpu",
 title_en="In a Slurm lab, a GPU hardware error drains the node in 2 seconds and the requeued job still finishes",
 title_es="En un laboratorio de Slurm, un error de hardware de GPU drena el nodo en 2 segundos y el trabajo reencolado termina",
 seo_title_en="Slurm GPU cluster in Docker with health checks · Iñigo González",
 seo_title_es="Clúster Slurm con GPU en Docker y health checks · Iñigo González",
 seo_desc="Drain, requeue and validate, and four CI iterations to get cgroups v2 working.",
 seo_desc_es="Drain, requeue y validate, y cuatro iteraciones de CI para que funcionen los cgroups v2.",
 dek_en="A lab that runs a real Slurm 23.11 cluster in Docker Compose with simulated GPUs, where a health check drains faulty nodes, requeues their jobs and validates them before they return.",
 dek_es="Un laboratorio que monta un clúster Slurm 23.11 real en Docker Compose con GPU simuladas, donde un chequeo de salud drena los nodos con fallos, reencola sus trabajos y los valida antes de que vuelvan.",
 en="""
When a simulated GPU reports XID 79, an error code for a hardware fault, the node is drained in 2 seconds and the training job on it is requeued and completes its 150 steps. That is what the Slurm lab published with this post shows in CI, where sacct, Slurm's accounting tool, records the job as REQUEUED, REQUEUED, COMPLETED. The cluster is real Slurm 23.11 from Ubuntu 24.04 packages, but it runs in Docker Compose and its GPUs are simulated.

Many GPU clusters run Slurm rather than Kubernetes, so the lab brings lab 09's XID policy to Slurm. The setup has MariaDB, slurmdbd, slurmctld and 4 nodes with 4 simulated GPUs each.

## A health check every 10 seconds that never brings a node back

`gpuops health` runs as the HealthCheckProgram every 10 seconds and chooses cordon, which drains the node and lets jobs finish, drain, which also requeues them, or quarantine. It never resumes a node and respects a drain reason set by a person. Returning a node is the job of `gpuops validate`: a maintenance reservation, resume, a burn-in on every GPU, then release or drain again.

The test job trains on two nodes with checkpoints on shared storage, and on a hardware XID it hangs rather than fails. `gpuops events` joins sacct, the job log and the health-check log into lab 12's event format.

## 36 checks in seven minutes, after four CI iterations

CI runs 36 checks in about 7 minutes, and the real files from that run are kept as test fixtures. Getting cgroups v2, the Linux mechanism that limits each job's resources, to work without systemd took four CI iterations, and the requeue delay was 60 to 80 seconds; both are written up in docs/design.md.

## How to use it with real data

On real nodes, the health source should switch to `nvidia-smi` and the kernel log, cgroup isolation should be enabled for the GPUs, and NHC (Node Health Check) should run alongside the GPU health check.

## Where it comes from

This lab builds on my experience running Linux (Red Hat) servers.""",
 es="""
Cuando una GPU simulada informa del XID 79, un código de error de fallo de hardware, el nodo se drena en 2 segundos y el entrenamiento que corría en él se reencola y completa sus 150 pasos. Así lo muestra en la CI el laboratorio de Slurm que acompaña a este post, donde sacct, la herramienta de contabilidad de Slurm, registra el trabajo como REQUEUED, REQUEUED, COMPLETED. El clúster es un Slurm 23.11 real con paquetes de Ubuntu 24.04, pero corre en Docker Compose y sus GPU son simuladas.

Muchos clústeres de GPU usan Slurm en lugar de Kubernetes, así que el laboratorio lleva a Slurm la política XID del laboratorio 09. El montaje tiene MariaDB, slurmdbd, slurmctld y 4 nodos con 4 GPU simuladas cada uno.

## Un chequeo cada 10 segundos que nunca reactiva un nodo

`gpuops health` funciona como HealthCheckProgram cada 10 segundos y elige entre cordon, que drena el nodo y deja que acaben los trabajos, drain, que además los reencola, o cuarentena. Nunca reactiva un nodo y respeta el motivo de un drain puesto por una persona. Devolverlo al servicio es tarea de `gpuops validate`: reserva de mantenimiento, resume, burn-in en todas las GPU y después libera o vuelve a drenar.

El trabajo de prueba entrena en dos nodos con checkpoints en almacenamiento compartido y, ante un XID de hardware, se cuelga en lugar de fallar. `gpuops events` une sacct, el log del trabajo y el del chequeo de salud en el formato de eventos del laboratorio 12.

## 36 comprobaciones en siete minutos, tras cuatro iteraciones de CI

La CI ejecuta 36 comprobaciones en unos 7 minutos, y los ficheros reales de esa ejecución se guardan como fixtures de los tests. Hicieron falta cuatro iteraciones para que los cgroups v2, el mecanismo de Linux que limita los recursos de cada trabajo, funcionaran sin systemd, y el reencolado tardaba entre 60 y 80 segundos; las dos cosas están en docs/design.md.

## Cómo usarlo con datos reales

En nodos reales, la fuente de salud debe pasar a `nvidia-smi` y al log del kernel, hay que activar el aislamiento por cgroups de las GPU y conviene ejecutar NHC (Node Health Check) junto al chequeo de salud de GPU.

## De dónde sale

Este laboratorio se apoya en mi experiencia administrando servidores Linux (Red Hat)."""),

dict(n="15", repo="15-multi-tenant-gpu-scheduling", date="2026-10-05", cat="gpu",
 title_en="A lab turns one GPU quota agreement between three teams into Kueue and KAI rules, and CI fails if they drift",
 title_es="Un laboratorio traduce el reparto de GPU entre tres equipos a reglas de Kueue y KAI, y la CI falla si se desvían",
 seo_title_en="Multi-tenant GPU scheduling: Kueue and KAI · Iñigo González",
 seo_title_es="GPU compartidas entre equipos: Kueue y KAI · Iñigo González",
 seo_desc="One quota agreement in a TOML file, rendered into both schedulers and tested on kind.",
 seo_desc_es="Un acuerdo de cuotas en un fichero TOML, traducido a los dos planificadores y probado en kind.",
 dek_en="A lab that writes who gets which GPUs in one TOML file, renders it into both schedulers and tests borrowing, reclaim and GPU sharing on a kind cluster with simulated GPUs.",
 dek_es="Un laboratorio que escribe en un fichero TOML quién tiene qué GPU, lo traduce a los dos planificadores y prueba el préstamo, la recuperación y el uso compartido en un clúster kind con GPU simuladas.",
 en="""
The inference team keeps its 8 guaranteed GPUs and never lends them, while training and research each have GPUs that can be borrowed, and the owner can take capacity back when it needs it. That agreement, written in one file, tenancy.toml, is the starting point of the multi-tenant GPU lab published with this post. It runs on a kind cluster, Kubernetes inside Docker, with 4 workers and 8 GPUs each simulated by Run:ai's fake-gpu-operator, plus KubeVirt.

Training has 16 guaranteed GPUs and 8 that can be borrowed; research has 8 guaranteed and 8 more that can be borrowed. `python -m tenancy render` turns the file into Kueue ClusterQueues grouped in a cohort, a set of queues that lend to each other, and into KAI Scheduler Queues. CI fails if the manifests drift from the file.

## Two pods share one GPU at 0.5 each

Kueue gets 22 checks: borrowing, reclaim, priority within a team and all-or-nothing admission, which starts a job only if all of it fits. KAI Scheduler gets 19: two pods sharing one GPU at 0.5 each, over-quota, reclaim and gang scheduling, which launches a group of pods together or not at all. KubeVirt, which runs virtual machines on Kubernetes, gets 5: a VM boots with QEMU emulation and the team's ResourceQuota rejects a second one.

## Three rounds of fixes after the first CI run

docs/decisions.md records why: queue usage is reported with a delay, the preemption reason, why a job was evicted, is in a condition, and fractional GPUs are passed as text.

## How to use it with real data

Teams and quotas go in `tenancy.toml`, from which the manifests for Kueue or KAI Scheduler are rendered. As the cluster grows, fair sharing and topology-aware scheduling can be added, and the agreement should be reviewed with the teams every quarter.

## Where it comes from

This lab builds on capacity management and on SLA and OLA agreements between teams that share the same infrastructure. When several teams share a GPU cluster, the key is the agreement: who is guaranteed what, who can borrow and what happens when the owner wants it back.""",
 es="""
El equipo de inferencia conserva sus 8 GPU garantizadas y nunca las presta, mientras que entrenamiento e investigación tienen GPU prestables, y el dueño puede recuperar la capacidad cuando la necesita. Ese acuerdo, escrito en un solo fichero, tenancy.toml, es el punto de partida del laboratorio de GPU compartidas que acompaña a este post. Se ejecuta en un clúster kind, Kubernetes dentro de Docker, con 4 workers y 8 GPU cada uno simuladas por el fake-gpu-operator de Run:ai, más KubeVirt.

Training tiene 16 GPU garantizadas y 8 prestables; research tiene 8 garantizadas y otras 8 prestables. `python -m tenancy render` convierte el fichero en ClusterQueues de Kueue agrupadas en una cohort, un conjunto de colas que se prestan capacidad, y en Queues de KAI Scheduler. La CI falla si los manifiestos no coinciden con el fichero.

## Dos pods comparten una GPU a 0,5 cada uno

Kueue pasa por 22 comprobaciones: préstamo, recuperación, prioridad dentro del equipo y admisión todo o nada, que solo arranca un trabajo si cabe entero. KAI Scheduler, por 19: dos pods compartiendo una GPU a 0,5 cada uno, exceso de cuota, recuperación y gang scheduling, que lanza un grupo de pods a la vez o ninguno. KubeVirt, que ejecuta máquinas virtuales en Kubernetes, por 5: una VM arranca con emulación QEMU y la ResourceQuota del equipo rechaza una segunda.

## Tres rondas de arreglos tras la primera CI

docs/decisions.md explica por qué: el uso de las colas se informa con retraso, el motivo de la preemption, por qué se expulsó un trabajo, está en una condición, y las GPU fraccionarias se pasan como texto.

## Cómo usarlo con datos reales

Los equipos y sus cuotas se describen en `tenancy.toml`, desde donde se generan los manifiestos para Kueue o KAI Scheduler. A medida que crece el clúster se pueden añadir fair sharing y planificación según topología, y conviene revisar el acuerdo con los equipos cada trimestre.

## De dónde sale

Este laboratorio se apoya en la gestión de capacidad y en los acuerdos de SLA y OLA entre equipos que comparten la misma infraestructura. Cuando varios equipos comparten un clúster de GPU, la clave es el acuerdo: quién tiene qué garantizado, quién puede pedir prestado y qué pasa cuando el dueño lo quiere de vuelta."""),

dict(n="16", repo="16-gitops-gpu-fleet", date="2026-10-09", cat="gpu",
 title_en="A GPU fleet lab stops a bad GPU Operator release in staging before it reaches the production clusters",
 title_es="Un laboratorio de flota GPU para en staging una versión mala del GPU Operator antes de que llegue a producción",
 seo_title_en="GitOps GPU fleet: GPU Operator with Flux · Iñigo González",
 seo_title_es="Flota GPU con GitOps: GPU Operator y Flux · Iñigo González",
 seo_desc="One file defines releases and clusters; Git and Flux do the rest, with a gate before production.",
 seo_desc_es="Un fichero define versiones y clústeres; Git y Flux hacen el resto, con una puerta antes de producción.",
 dek_en="A lab that upgrades the GPU software stack across a fleet of clusters from Git with Flux, in waves from staging to production with a gate before prod, tested on two kind clusters.",
 dek_es="Un laboratorio que actualiza el software de GPU de una flota de clústeres desde Git con Flux, en olas de staging a producción y con una puerta antes de prod, probado en dos clústeres kind.",
 en="""
A release built to fail on purpose is stopped in staging and never reaches production. That is one of the 29 checks in the 20-minute end-to-end test of the GPU fleet lab published with this post, which runs Gitea, a self-hosted Git server, and two kind clusters, Kubernetes inside Docker. The same test shows Flux, the tool that applies what is in Git to each cluster, correcting drift.

Everything starts in one file, fleet.toml. It defines releases, each with GPU Operator, Network Operator and driver versions, and clusters with their GPU pools. Waves go from staging to prod H100 and then prod A100, with a pause after the canary, the first group to get the change.

## Approving production is a commit

`python -m fleet render` writes each cluster's folder, and Flux applies it in three steps: operators, config and lifecycle. The lifecycle step is lab 11's controller, with its rollout plan generated from the same file. `fleet start`, `fleet promote` and `fleet approve` each edit one line, and `fleet gate` checks the live clusters before promoting.

## A validate step catches a misspelt nodeSelecter

Besides 21 unit tests, CI renders the real NGC Helm charts at every version and checks them against the CRD schemas, the definitions of custom Kubernetes objects, of that exact version; it catches a misspelt `nodeSelecter`. One CI iteration was needed: the rollout plan was applied before the NVIDIADriver objects, so lifecycle now depends on config. The lab also found a difference in the NVIDIADriver CRD between two GPU Operator versions.

## How to use it with real data

Clusters and releases go in `fleet.toml`. Flux is bootstrapped on each cluster, or Argo CD, since the same structure works, and the gate before production stays as a required check in the repository.

## Where it comes from

This lab builds on Git, CI/CD pipelines and release management, and ties several of my earlier labs together.""",
 es="""
Una versión hecha para fallar a propósito se queda parada en staging y nunca llega a producción. Es una de las 29 comprobaciones de la prueba de punta a punta de 20 minutos del laboratorio de flota GPU que acompaña a este post, que usa Gitea, un servidor Git propio, y dos clústeres kind, Kubernetes dentro de Docker. La misma prueba muestra a Flux, la herramienta que aplica en cada clúster lo que hay en Git, corrigiendo la deriva.

Todo parte de un fichero, fleet.toml. Define versiones, cada una con su GPU Operator, Network Operator y driver, y clústeres con sus pools de GPU. Las olas van de staging a prod H100 y después a prod A100, con una pausa tras el canary, el primer grupo que recibe el cambio.

## Aprobar producción es un commit

`python -m fleet render` escribe la carpeta de cada clúster y Flux la aplica en tres pasos: operators, config y lifecycle. El paso lifecycle es el controlador del laboratorio 11, con su plan generado desde el mismo fichero. `fleet start`, `fleet promote` y `fleet approve` editan una línea cada uno, y `fleet gate` revisa los clústeres vivos antes de promocionar.

## La validación detecta un nodeSelecter mal escrito

Además de 21 tests unitarios, la CI renderiza los charts de Helm reales de NGC en cada versión y los comprueba contra los esquemas de CRD, las definiciones de objetos propios de Kubernetes, de esa versión exacta; detecta un `nodeSelecter` mal escrito. Hizo falta una iteración de CI: el plan de rollout se aplicaba antes que los objetos NVIDIADriver, así que lifecycle ahora depende de config. El laboratorio también encontró una diferencia en el CRD NVIDIADriver entre dos versiones del GPU Operator.

## Cómo usarlo con datos reales

Los clústeres y las versiones se describen en `fleet.toml`. Flux se instala en cada clúster, o Argo CD, porque la misma estructura sirve, y la puerta antes de producción se mantiene como comprobación obligatoria del repositorio.

## De dónde sale

Este laboratorio se apoya en Git, pipelines de CI/CD y gestión de releases, y une varios de mis laboratorios anteriores."""),

dict(n="17", repo="17-teams-rooms-fleet-health", date="2026-10-15", cat="tools",
 title_en="A morning check ranks 25 Teams Rooms devices so the boardroom with the next meeting is fixed first",
 title_es="Una revisión matinal ordena 25 dispositivos de Teams Rooms para arreglar antes la sala con la próxima reunión",
 seo_title_en="Teams Rooms health check with Microsoft Graph · Iñigo González",
 seo_title_es="Salud de Teams Rooms con Microsoft Graph · Iñigo González",
 seo_desc="Teams Rooms health from Microsoft Graph, a room register and today's bookings, turned into a morning walk-round.",
 seo_desc_es="La salud de Teams Rooms desde Microsoft Graph, un registro de salas y las reservas del día, convertidos en la ronda de primera hora.",
 dek_en="The tool, published with a made-up company with 25 devices in three offices, combines Teams Rooms health from Microsoft Graph, a room register and today's bookings into a morning walk-round list.",
 dek_es="La herramienta, publicada con una empresa inventada con 25 dispositivos en tres oficinas, cruza la salud de Teams Rooms desde Microsoft Graph, un registro de salas y las reservas del día en la lista de la ronda de primera hora.",
 en="""
The boardroom with a meeting in 30 minutes goes to the top of the list, the small room that is free all day goes to the bottom, and each problem comes with the first thing to try. That is the order the Teams Rooms morning check published with this post gives the on-site engineer at 08:00. Its demo is a made-up company with 25 devices in three offices and faults placed on purpose.

The Teams admin center shows the health of every room, one device at a time. The tool instead reads all devices and their health from Microsoft Graph, Microsoft's API for its cloud services, with a read-only PowerShell script that queries `/teamwork/devices`.

## Three states: not ready, at risk or ready

A room is Not ready when it is offline, Teams sign-in has failed, or the camera, microphone, speaker or main display is down. It is At risk with no calendar on the console, a stale heartbeat, outdated software, or a second display or HDMI ingest down. Otherwise it is Ready.

## Firmware drift and devices missing from the register

morning_check.md sorts rooms by state, priority and next meeting. The tool also writes report.html, actions.csv with serial numbers for the ticket, a daily trend, and a housekeeping list of firmware that drifted from the rest of the model and devices nobody added to the room register. It runs on Python's standard library, with 14 tests and a short runbook.

## How to use it with real data

Run the PowerShell export against the tenant (the `/teamwork/devices` API is in Graph beta), fill in the room register with the rooms and their priority, and run it every morning before the first meetings.

## Where it comes from

What I learned building it: most of the value is in the order of the list, not in the detection. And an offline console should show one issue, not five, because everything else about it is noise until it is back.""",
 es="""
La sala de Consejo con una reunión en 30 minutos va arriba de la lista, la sala pequeña que está libre todo el día va al final, y cada problema llega con lo primero que hay que probar. Ese es el orden que da al técnico a las 8:00 la revisión de primera hora de Teams Rooms que acompaña a este post. Su demo es una empresa inventada con 25 dispositivos en tres oficinas y fallos puestos a propósito.

El Teams admin center enseña la salud de cada sala, de dispositivo en dispositivo. La herramienta, en cambio, lee todos los dispositivos y su salud desde Microsoft Graph, la API de Microsoft para sus servicios en la nube, con un script de PowerShell de solo lectura que consulta `/teamwork/devices`.

## Tres estados: no lista, en riesgo o lista

Una sala está No lista si no tiene conexión, ha fallado el inicio de sesión en Teams o la cámara, el micrófono, el altavoz o la pantalla principal están caídos. Está En riesgo si la consola no tiene calendario, no hay latido reciente, el software está desactualizado o fallan la segunda pantalla o la entrada HDMI. Si no, está Lista.

## Firmware desalineado y equipos fuera del registro

morning_check.md ordena las salas por estado, prioridad y próxima reunión. La herramienta genera además report.html, actions.csv con números de serie para el ticket, una tendencia diaria y una lista de mantenimiento con el firmware que se ha quedado distinto al resto del modelo y los dispositivos que nadie dio de alta en el registro de salas. Funciona con la librería estándar de Python, con 14 tests y un runbook corto.

## Cómo usarlo con datos reales

Hay que ejecutar la exportación de PowerShell contra el tenant (la API `/teamwork/devices` está en la beta de Graph), completar el registro con las salas y su prioridad, y lanzarlo cada mañana antes de las primeras reuniones.

## De dónde sale

Lo que aprendí al construirla: casi todo el valor está en el orden de la lista, no en la detección. Y una consola sin conexión debe mostrar un problema, no cinco, porque lo demás es ruido hasta que vuelva."""),

dict(n="18", repo="18-mecm-intune-comanagement-tracker", date="2026-10-15", cat="tools",
 title_en="A co-management review says NO-GO to the next workload move: only 91.9% of 260 devices are co-managed",
 title_es="Una revisión de co-management dice NO-GO al siguiente workload: solo el 91,9 % de 260 equipos está co-gestionado",
 seo_title_en="MECM + Intune co-management tracker · Iñigo González",
 seo_title_es="Seguimiento de co-management MECM + Intune · Iñigo González",
 seo_desc="MECM and Intune joined in one report: real co-management state, workload authority against the plan and Windows 11 waves.",
 seo_desc_es="MECM e Intune en un solo informe: estado real de co-management, autoridad por workload frente al plan y olas de Windows 11.",
 dek_en="The tracker, published with a made-up company with 260 devices halfway through a Windows 11 migration, joins MECM and Intune to show real co-management state, workload authority against the plan and progress per wave.",
 dek_es="El seguimiento, publicado con una empresa inventada con 260 equipos a mitad de una migración a Windows 11, cruza MECM e Intune para mostrar el estado real de co-management, la autoridad por workload frente al plan y el avance por ola.",
 en="""
The next move of the co-management slider, the setting that hands each workload from MECM to Intune, gets a NO-GO: only 91.9% of devices are co-managed and one pilot device has not picked up the change. That is what the tracker published with this post finds in its demo, a made-up company with 260 devices halfway through its migration.

In a co-management and Windows 11 migration, every status meeting asks how many devices are really co-managed, what breaks if a workload moves to Intune for everyone, and whether the next wave will finish on time. The answers sit in two consoles that do not share a report.

## Five states for every device

A read-only SQL query reads the MECM reporting views for client health, OS build and collections, and a PowerShell export pulls `managedDevices` with `configurationManagerClientEnabledFeatures` from Intune. The tool joins them by device name into five states: co-managed, MECM only (not enrolled), enrolled outside co-management, in MECM without client, and Intune only. For each co-managed device it compares the workload authority the plan expects with what Intune reports, and it tracks each Windows 11 wave and the hardware that blocks the upgrade.

## A go/no-go ready for the change request

gates.md gives GO or NO-GO for every workload on Pilot against limits agreed in `plan.json`, ready to paste into the change request. It runs on Python's standard library, with 14 tests and a playbook for using it alongside a change board.

## How to use it with real data

Run the SQL query against the MECM site database and the Intune export from Graph, write the workloads, waves and gates in `plan.json`, and bring `gates.md` to each change advisory board (CAB) before moving the slider.

## Where it comes from

It comes from the Windows 11 migration I led: most of the effort is not the upgrade, it is finding the devices that are not where the plan says they are. Agreeing the gates before the CAB, not during it, saves the longest discussions.""",
 es="""
El siguiente paso del slider de co-management, el ajuste que pasa cada workload de MECM a Intune, recibe un NO-GO: solo el 91,9 % de los equipos está co-gestionado y un equipo del piloto no ha recogido el cambio. Así lo detecta en su demo el seguimiento que acompaña a este post, con una empresa inventada de 260 equipos a mitad de migración.

En una migración a co-management y Windows 11, cada reunión de seguimiento pregunta cuántos equipos están de verdad co-gestionados, qué se rompe si un workload pasa a Intune para todos y si la siguiente ola acabará a tiempo. Las respuestas están en dos consolas que no comparten informe.

## Cinco estados para cada equipo

Una consulta SQL de solo lectura lee las vistas de informes de MECM sobre salud del cliente, build del SO y colecciones, y una exportación en PowerShell saca de Intune `managedDevices` con `configurationManagerClientEnabledFeatures`. La herramienta los cruza por nombre de equipo en cinco estados: co-gestionado, solo MECM (sin inscribir), inscrito fuera de co-management, en MECM sin cliente y solo Intune. Para cada equipo co-gestionado compara la autoridad por workload que espera el plan con la que informa Intune, y sigue cada ola de Windows 11 y el hardware que impide la actualización.

## Un go/no-go listo para la petición de cambio

gates.md da GO o NO-GO para cada workload en Pilot frente a límites acordados en `plan.json`, listo para pegar en la petición de cambio. Funciona con la librería estándar de Python, con 14 tests y un playbook para usarlo junto al comité de cambios.

## Cómo usarlo con datos reales

Hay que ejecutar la consulta SQL contra la base de datos del sitio MECM y la exportación de Intune desde Graph, escribir los workloads, olas y gates en `plan.json`, y llevar `gates.md` a cada comité de cambios (CAB) antes de mover el slider.

## De dónde sale

Nace de la migración a Windows 11 que lideré: casi todo el esfuerzo no está en la actualización, sino en encontrar los equipos que no están donde dice el plan. Acordar los gates antes del CAB, y no durante, ahorra las discusiones más largas."""),

dict(n="19", repo="19-ad-infra-health-check", date="2026-10-16", updated="2026-11-15", cat="tools",
 title_en="A read-only Active Directory check puts on one Monday page what has to be fixed before 09:00",
 title_es="Un chequeo de Active Directory reúne en una página del lunes lo que hay que arreglar antes de las 9:00",
 seo_title_en="Active Directory health check with PowerShell · Iñigo González",
 seo_title_es="Chequeo de salud de Active Directory con PowerShell · Iñigo González",
 seo_desc_es="Controladores de dominio, replicación, DHCP, directivas de grupo y cuentas de administrador desde una exportación de solo lectura, ordenados por lo que hay…",
 dek_en="The weekly health check, published with a made-up domain of six domain controllers in four sites and faults placed on purpose, reviews controllers, replication, DHCP, Group Policy and admin accounts from one read-only export.",
 dek_es="El chequeo semanal, publicado con un dominio inventado de seis controladores en cuatro sedes y fallos puestos a propósito, revisa controladores, replicación, DHCP, directivas de grupo y cuentas de administrador desde una exportación de solo lectura.",
 seo_desc="Active Directory health check with PowerShell: one read-only export for domain controllers, replication, DHCP, Group Policy and admin accounts, by priority.",
 en="""
Most Active Directory problems warn first: a clock drifting, DFSR stopped after patching, a replication link failing quietly for weeks, a DHCP scope full the week new joiners arrive. The health check published with this post gathers those signals into one page with what to fix today. Its demo runs on a made-up domain with six domain controllers in four sites and faults placed on purpose.

`dcdiag` and `repadmin` already tell everything, but one domain controller at a time. The check starts instead from one read-only export, `Export-ADHealth.ps1`, built on the standard RSAT modules, the remote server administration tools.

## Six areas, from replication to the krbtgt password

The checks cover domain controllers, replication, DHCP, Group Policy, privileged access and directory hygiene. Replication includes the tombstone risk, the point after which a controller that stopped replicating cannot rejoin safely. Privileged access includes the age of the krbtgt password, the account behind the domain's Kerberos tickets.

Results go into `health_check.md` under Fix today, Plan this week and Housekeeping, plus `findings.csv` with the first step for each finding. Each run is compared with last week's to show what is new and what was resolved.

## How to use it with real data

The export runs with RSAT from an admin workstation joined to the domain. It is meant to be scheduled for Monday morning, keeping last week's run.

## Where it comes from

Two lessons shaped it: an unreachable domain controller should give one finding, not ten, and most of the value is in the order of the list, what must be fixed before 09:00 and what can go to a change.""",
 es="""
La mayoría de problemas de Active Directory avisan antes: un reloj que se desvía, DFSR parado después de parchear, un enlace de replicación fallando en silencio durante semanas, un ámbito de DHCP lleno la semana que llegan las incorporaciones. El chequeo que acompaña a este post reúne esas señales en una página con lo que hay que arreglar hoy. Su demo usa un dominio inventado de seis controladores en cuatro sedes con fallos puestos a propósito.

`dcdiag` y `repadmin` ya lo cuentan todo, pero de controlador en controlador. El chequeo parte en cambio de una sola exportación de solo lectura, `Export-ADHealth.ps1`, con los módulos estándar de RSAT, las herramientas de administración remota de servidores.

## Seis áreas, de la replicación a la contraseña de krbtgt

Las comprobaciones cubren controladores, replicación, DHCP, directivas de grupo, acceso privilegiado e higiene del directorio. La replicación incluye el riesgo de tombstone, el límite tras el cual un controlador que dejó de replicar no puede volver sin riesgo. El acceso privilegiado incluye la antigüedad de la contraseña de krbtgt, la cuenta que respalda los tickets Kerberos.

Los resultados van a `health_check.md` en Arreglar hoy, Planificar esta semana y Limpieza, más `findings.csv` con el primer paso de cada hallazgo. Cada ejecución se compara con la de la semana anterior para mostrar qué es nuevo y qué se ha resuelto.

## Cómo usarlo con datos reales

La exportación se ejecuta con RSAT desde un puesto de administración unido al dominio. Está pensado para programarse el lunes a primera hora, guardando la ejecución anterior.

## De dónde sale

Dos lecciones le dieron forma: un controlador que no responde debe dar un hallazgo, no diez, y casi todo el valor está en el orden de la lista, qué hay que arreglar antes de las 9:00 y qué puede ir a un cambio."""),

dict(n="20", repo="20-entra-sso-app-audit", date="2026-10-16", cat="tools",
 title_en="An Entra ID audit flags the SAML certificates and secrets that expire before a SaaS app stops at 09:00",
 title_es="Una auditoría de Entra ID detecta los certificados SAML que caducan antes de que una app SaaS se pare a las 9:00",
 seo_title_en="Entra ID SSO audit: SAML certificate expiry · Iñigo González",
 seo_title_es="Auditoría SSO de Entra ID: caducidad de certificados SAML · Iñigo González",
 seo_desc="Enterprise apps and app registrations in Entra ID: certificates and secrets about to expire, owners, MFA coverage, risky permissions and SCIM.",
 seo_desc_es="Aplicaciones empresariales y registros de aplicaciones en Entra ID: certificados y secretos a punto de caducar, propietarios, cobertura de MFA, permisos…",
 dek_en="The audit, published with a made-up tenant of 21 enterprise apps and faults placed on purpose, reviews certificates and secrets, owners, MFA coverage, risky permissions and SCIM provisioning from a read-only export.",
 dek_es="La auditoría, publicada con un tenant inventado de 21 aplicaciones empresariales y fallos puestos a propósito, revisa certificados y secretos, propietarios, cobertura de MFA, permisos de riesgo y aprovisionamiento SCIM desde una exportación de solo lectura.",
 en="""
When the SAML signing certificate of a SaaS app expires, the app stops accepting logons at 09:00; when a client secret expires, a nightly job fails. The single sign-on audit published with this post looks for those dates before they arrive. Its demo runs on a made-up tenant with 21 enterprise apps and faults placed on purpose.

The audit starts from `Export-EntraAppInventory.ps1`, a read-only Microsoft Graph export of service principals, app registrations and Conditional Access policies. For secrets and certificates it reads only the dates, never the values.

## Six areas, from expired secrets to leavers who keep their account

The checks cover credentials, ownership, access, permissions, SCIM provisioning and unused apps. Access covers whether assignment is required and MFA coverage. Permissions cover tenant-wide consent, unverified publishers, redirect URIs and daemons, unattended processes, that can write to the whole directory. SCIM, the standard that creates and removes accounts in the app, is flagged when provisioning is in quarantine and leavers keep their account.

A secret expired while the app still signs in is urgent; one already replaced by a newer secret is clean-up.

## How to use it with real data

The export needs read-only Graph permissions. The output is `review.md` for the monthly access review, `renewals.csv` as a renewal calendar with owners, `findings.csv` and `report.html`; every app in that calendar should get an owner. A runbook explains how to renew a SAML certificate without an outage.

## Where it comes from

It comes from integrating SaaS apps in Entra ID, where the hard part is not the SSO setup but who renews the certificate two years later.""",
 es="""
Cuando caduca el certificado de firma SAML de una aplicación SaaS, deja de aceptar inicios de sesión a las 9:00; cuando caduca un secreto, falla un proceso nocturno. La auditoría de inicio de sesión único que acompaña a este post busca esas fechas antes de que lleguen. Su demo usa un tenant inventado con 21 aplicaciones empresariales y fallos puestos a propósito.

La auditoría parte de `Export-EntraAppInventory.ps1`, una exportación de solo lectura con Microsoft Graph de entidades de servicio, registros de aplicaciones y políticas de acceso condicional. De secretos y certificados solo lee las fechas, nunca su valor.

## Seis áreas, de los secretos caducados a las bajas que siguen con cuenta

Las comprobaciones cubren credenciales, propietarios, acceso, permisos, aprovisionamiento SCIM y aplicaciones sin uso. El acceso incluye si la asignación es obligatoria y la cobertura de MFA. Los permisos incluyen el consentimiento para toda la organización, editores sin verificar, URI de redirección y procesos desatendidos que pueden escribir en todo el directorio. SCIM, el estándar que crea y elimina cuentas en la aplicación, se marca cuando el aprovisionamiento está en cuarentena y las bajas siguen con cuenta.

Un secreto caducado mientras la aplicación sigue iniciando sesión es urgente; uno ya sustituido por otro nuevo es limpieza.

## Cómo usarlo con datos reales

La exportación necesita permisos de solo lectura de Graph. El resultado es `review.md` para la revisión mensual de accesos, `renewals.csv` como calendario de renovaciones con propietarios, `findings.csv` y `report.html`; cada aplicación del calendario debe tener propietario. Un runbook explica cómo renovar un certificado SAML sin corte.

## De dónde sale

Nace de integrar aplicaciones SaaS en Entra ID, donde lo difícil no es configurar el SSO, sino quién renueva el certificado dos años después."""),

dict(n="21", repo="21-apple-fleet-audit", date="2026-10-17", updated="2026-11-19", cat="tools",
 title_en="A weekly Jamf Pro review puts first the push certificate and tokens that can stop a whole Apple fleet",
 title_es="Una revisión semanal de Jamf Pro pone primero el certificado y los tokens que pueden parar una flota Apple",
 seo_title_en="Jamf Pro weekly audit for an Apple fleet · Iñigo González",
 seo_title_es="Auditoría semanal de Jamf Pro (flota Apple) · Iñigo González",
 seo_desc="Push certificate and tokens, OS currency, FileVault, SIP, bootstrap token, passcodes, stale devices and full disks, with the executives' devices first.",
 seo_desc_es="Certificado push y tokens, versiones de sistema, FileVault, SIP, bootstrap token, códigos de acceso, equipos que no se conectan y discos llenos…",
 dek_en="The review, published with a made-up fleet of 40 Macs, iPhones and iPads with three VIP users and faults placed on purpose, checks tokens, OS versions, encryption, passcodes, stale devices and full disks, with executives' devices first.",
 dek_es="La revisión, publicada con una flota inventada de 40 Mac, iPhone e iPad con tres usuarios VIP y fallos puestos a propósito, comprueba tokens, versiones, cifrado, códigos, equipos sin conectar y discos llenos, con los de dirección primero.",
 en="""
The most expensive mistakes in an Apple fleet are not on one device but in the certificate or token that stops all of them. If the APNs push certificate expires, no device gets a command; if someone creates a new one instead of renewing it, every device has to re-enroll. The weekly Jamf Pro review published with this post puts those dates first. Its demo runs on a made-up fleet of 40 devices, 18 Macs, 14 iPhones and 8 iPads, with three VIP users and faults placed on purpose.

The review reads Jamf Pro through a read-only API client whose secret comes from an environment variable.

## From the ADE token to the CEO's full iPad

An expired ADE token, the one behind automated enrollment, means new laptops come out of the box unmanaged. On Macs the review looks for FileVault, Apple's disk encryption, with no recovery key in Jamf Pro, and Apple silicon Macs with no bootstrap token, so updates never install. It also flags iPhones with no passcode and laptops silent for two months.

VIP findings go up one level and get their own section, so the CEO's full iPad shows up well before the evening ahead of the board meeting. A value Jamf Pro did not collect skips the check instead of raising a false alarm.

## How to use it with real data

It needs a Jamf Pro API role with read privileges only and an API client. After the export, the APNs expiry date from Settings > Global > Push certificates and the VIP list are added. The output includes a token calendar and a work list per device.

## Where it comes from

It comes from managing MacBooks, iPhones and iPads with Jamf Pro and supporting VIP users and board meetings.""",
 es="""
Los errores más caros en una flota Apple no están en un dispositivo, sino en el certificado o el token que los para todos. Si caduca el certificado push de APNs, ningún dispositivo recibe órdenes; si alguien crea uno nuevo en lugar de renovarlo, toca volver a inscribirlos todos. La revisión semanal de Jamf Pro que acompaña a este post pone esas fechas primero. Su demo usa una flota inventada de 40 dispositivos, 18 Mac, 14 iPhone y 8 iPad, con tres usuarios VIP y fallos puestos a propósito.

La revisión lee Jamf Pro con un cliente de API de solo lectura cuyo secreto se lee de una variable de entorno.

## Del token de ADE al iPad lleno del CEO

Un token de ADE caducado, el de la inscripción automática, hace que los portátiles nuevos salgan de la caja sin gestionar. En los Mac busca FileVault, el cifrado de disco de Apple, sin clave de recuperación en Jamf Pro, y equipos Apple silicon sin bootstrap token, con lo que las actualizaciones nunca se instalan. También marca iPhone sin código y portátiles que llevan dos meses sin conectarse.

Los hallazgos VIP suben un nivel y tienen su propia sección, para que el iPad lleno del CEO no aparezca la tarde antes del consejo. Un dato que Jamf Pro no ha recogido se salta la comprobación en lugar de dar una falsa alarma.

## Cómo usarlo con datos reales

Hace falta un rol de API en Jamf Pro solo de lectura y un cliente de API. Tras la exportación se añaden la caducidad de APNs, desde Settings > Global > Push certificates, y la lista de VIP. El resultado incluye un calendario de tokens y una lista de trabajo por dispositivo.

## De dónde sale

Nace de gestionar MacBooks, iPhones e iPads con Jamf Pro y de dar soporte a usuarios VIP y reuniones de consejo."""),

dict(n="22", repo="22-dex-experience-score", date="2026-10-17", updated="2026-11-18", cat="tools",
 title_en="A lab scores every laptop from 0 to 10 and traces the top problem to blue screens after a driver update",
 title_es="Un laboratorio pone nota de 0 a 10 a cada portátil y sitúa el primer problema en pantallazos azules tras un driver",
 seo_title_en="DEX score: a 0-10 experience per laptop · Iñigo González",
 seo_title_es="Puntuación DEX de 0 a 10 por portátil · Iñigo González",
 seo_desc_es="Un laboratorio que convierte la telemetría de los equipos en una nota por dispositivo, sede y departamento, y ordena los cinco arreglos que más la subirían.",
 dek_en="A lab, run on a made-up company with 120 devices in three cities and six weeks of data, that turns endpoint telemetry into a score per device, site and department and ranks the fixes that would raise it most.",
 dek_es="Un laboratorio, con una empresa inventada de 120 equipos en tres ciudades y seis semanas de datos, que convierte la telemetría de los equipos en una nota por dispositivo, sede y departamento y ordena los arreglos que más la subirían.",
 seo_desc="DEX score lab: turns endpoint telemetry into a 0-10 digital experience score per device, site and department, and ranks the fixes that raise it most.",
 en="""
In a made-up company with 120 devices in three cities, the top problem is blue screens on one laptop model after a driver update. It is the first of five problems placed on purpose that the lab published with this post finds in six weeks of fictional data. The lab turns endpoint telemetry, the data each device records about itself, into a 0 to 10 score per device, site and department.

Tickets show only a fraction of the problems. People live with a slow laptop for weeks and just say "IT is slow". A monthly update adds 40 seconds to every logon or an Outlook add-in crashes on twenty laptops, and telemetry sees it.

## What lowers a device's DEX score: five categories, blue screens cap it and missing data never counts as zero

A read-only PowerShell collector gathers boot and logon times, app crashes, blue screens, Wi-Fi, latency, VPN failures, battery and disk. The score combines performance, stability, network and collaboration, hardware and an optional survey. Blue screens and very poor categories cap it, and missing data is left out, never scored as zero.

The lab ranks fixes by how much the fleet score would rise if each problem were gone and shows a 6-week trend by site. Every point lost has to lead to a cause and a fix.

## How to use it with real data

The collector can go out through an Intune remediation script or an RMM tool, with thresholds tuned after a few weeks. Telemetry linked to a person is personal data, so the first step is talking to the data protection officer and reporting by site and department.

## Where it comes from

It is a lab built on years of supporting Windows users and executives on site, inspired by public descriptions of digital employee experience (DEX) tools such as Nexthink. The model, thresholds and weights are my own and are explained in the repository.""",
 es="""
En una empresa inventada con 120 equipos en tres ciudades, el primer problema son los pantallazos azules en un modelo de portátil tras actualizar un driver. Es el primero de los cinco problemas puestos a propósito que encuentra, en seis semanas de datos ficticios, el laboratorio que acompaña a este post. El laboratorio convierte la telemetría, los datos que cada equipo registra sobre sí mismo, en una nota de 0 a 10 por dispositivo, sede y departamento.

Los tickets solo muestran una parte de los problemas. La gente convive semanas con un portátil lento y solo dice «IT va lento». Una actualización mensual añade 40 segundos a cada inicio de sesión o un complemento de Outlook falla en veinte portátiles, y la telemetría lo ve.

## Qué baja la puntuación DEX de un equipo: cinco categorías, los pantallazos azules le ponen tope y lo que falta nunca cuenta como cero

Un recolector de solo lectura en PowerShell recoge tiempos de arranque e inicio de sesión, cierres de aplicaciones, pantallazos azules, wifi, latencia, fallos de VPN, batería y disco. La nota combina rendimiento, estabilidad, red y colaboración, hardware y una encuesta opcional. Los pantallazos azules y las categorías muy malas le ponen tope, y los datos que faltan se dejan fuera, nunca cuentan como cero.

El laboratorio ordena los arreglos por cuánto subiría la nota de la flota si cada problema desapareciera y muestra la tendencia de 6 semanas por sede. Cada punto perdido tiene que llevar a una causa y a un arreglo.

## Cómo usarlo con datos reales

El recolector se puede desplegar con un script de corrección de Intune o una herramienta RMM, ajustando los umbrales tras unas semanas. La telemetría ligada a una persona es un dato personal, así que el primer paso es hablar con el delegado de protección de datos e informar por sede y departamento.

## De dónde sale

Es un laboratorio que parte de años dando soporte presencial a usuarios de Windows y a dirección, inspirado en las descripciones públicas de herramientas de experiencia digital del empleado (DEX) como Nexthink. El modelo, los umbrales y los pesos son míos y están explicados en el repositorio."""),
dict(n="23", repo="23-it-vendor-contract-tracker", date="2026-10-18", updated="2026-11-13", cat="tools",
 title_en="The costliest date in an IT contract is the notice deadline; a monthly review puts each one in the calendar",
 title_es="La fecha más cara de un contrato de IT es la del preaviso; una revisión mensual la lleva al calendario",
 seo_title_en="IT vendor contract and renewal tracker · Iñigo González",
 seo_title_es="Contratos y renovaciones de IT en una revisión · Iñigo González",
 seo_desc="A tracker that reads the contract register and finds the notice deadlines, unused licences, budget overruns and missed SLAs before they cost money.",
 seo_desc_es="Un tracker que lee el registro de contratos y encuentra los preavisos, licencias sin usar, desviaciones de presupuesto y SLA incumplidos antes de que cuesten…",
 dek_en="The tracker, published with a made-up company of 21 contracts from 17 vendors and faults placed on purpose, reads the contract register to find notice deadlines, unused licences, budget overruns and missed SLAs before they cost money.",
 dek_es="El tracker, publicado con una empresa inventada de 21 contratos de 17 proveedores y fallos puestos a propósito, lee el registro de contratos para encontrar preavisos, licencias sin usar, desviaciones de presupuesto y SLA incumplidos antes de que cuesten dinero.",
 en="""
A contract with 60 days' notice renews by itself for another year because nobody looked at the date in time. The tracker published with this post reads the register a team already keeps in a spreadsheet and finds those deadlines, including contracts that already renewed by themselves. Its demo runs on a made-up company with 21 contracts from 17 vendors, with faults placed on purpose.

## Licences, budget and service credits nobody claims

Firewall support ends and nobody notices until a replacement is needed. An add-on has 60 licences and 34 users while the main suite is 12 seats over what was bought. A budget line is on pace to end 14% over. A vendor misses its SLA, the service level it signed, two months running, and the service credit is never claimed.

The checks cover renewals and notice deadlines, licences, budget forecast, SLA and service credits, supplier risk and data quality. Usage data turns a renewal into a negotiation.

## A renewal calendar with a 14-day reminder

The output is `review.md` for the monthly vendor meeting, `actions.csv` with owners, dates and the money at stake, and `report.html` with a 12-month renewal calendar. `renewals.ics` puts every notice deadline in the team calendar with a reminder 14 days before.

## How to use it with real data

The register is exported to CSV and its columns mapped. Before each review, the spend to date from finance and last month's SLA figures are added.

## Where it comes from

It comes from managing IT suppliers, renewals and budgets, where the most expensive date in a contract is not the end date but the notice deadline.""",
 es="""
Un contrato con 60 días de preaviso se renueva solo otro año porque nadie miró la fecha a tiempo. El tracker que acompaña a este post lee el registro que el equipo ya tiene en una hoja de cálculo y encuentra esas fechas, también las de los contratos que ya se renovaron solos. Su demo usa una empresa inventada con 21 contratos de 17 proveedores, con fallos puestos a propósito.

## Licencias, presupuesto y penalizaciones que nadie reclama

Se acaba el soporte de un firewall y nadie se entera hasta que hace falta un repuesto. Un complemento tiene 60 licencias y 34 usuarios mientras la suite principal tiene 12 puestos más de los comprados. Una partida va camino de acabar un 14% por encima. Un proveedor incumple su SLA, el nivel de servicio que firmó, dos meses seguidos, y nadie reclama la penalización.

Las comprobaciones cubren renovaciones y preavisos, licencias, previsión del presupuesto, SLA y penalizaciones, riesgo de proveedor y calidad de los datos. Los datos de uso convierten una renovación en una negociación.

## Un calendario de renovaciones con aviso 14 días antes

El resultado es `review.md` para la reunión mensual de proveedores, `actions.csv` con responsable, fecha y el dinero en juego, y `report.html` con un calendario de renovaciones a 12 meses. `renewals.ics` lleva cada fecha límite de preaviso al calendario del equipo con aviso 14 días antes.

## Cómo usarlo con datos reales

El registro se exporta a CSV y se adaptan sus columnas. Antes de cada revisión se añaden el gasto acumulado de finanzas y las cifras de SLA del mes.

## De dónde sale

Nace de gestionar proveedores, renovaciones y presupuesto de IT, donde la fecha más cara de un contrato no es la de fin, sino la del preaviso."""),
dict(n="24", repo="24-hospitality-it-preopening", date="2026-10-18", cat="tools",
 title_en="A hotel pre-opening tracker shows which IT delay moves the opening, starting with a 75-day internet line",
 title_es="Un tracker de pre-apertura de hotel muestra qué retraso de IT mueve la apertura, empezando por la línea de 75 días",
 seo_title_en="Hotel IT pre-opening tracker and checklist · Iñigo González",
 seo_title_es="Pre-apertura de hotel: plan y checklist de IT · Iñigo González",
 seo_desc="A plan with lead times and dependencies that calculates the critical path, the gates at risk and the work that must start this week.",
 seo_desc_es="Un plan con plazos de entrega y dependencias que calcula el camino crítico, los hitos en riesgo y lo que tiene que empezar esta semana.",
 dek_en="The tracker, published with a made-up 120-room resort hotel opening in January, with 30 tasks and delays placed on purpose, calculates the critical path, the gates at risk and the work that must start this week.",
 dek_es="El tracker, publicado con un hotel vacacional inventado de 120 habitaciones que abre en enero, con 30 tareas y retrasos puestos a propósito, calcula el camino crítico, los hitos en riesgo y lo que tiene que empezar esta semana.",
 en="""
In a hotel pre-opening the internet circuits have a 75-day lead time, and almost every other IT system waits for them. The tracker published with this post turns the task list into a schedule that shows which delay moves the opening. Its demo runs on a made-up 120-room resort hotel opening in January, with 30 tasks in nine workstreams and delays placed on purpose.

The cloud PMS, the hotel management system, slides with the line, as do the room-charge interface, call charges and interface tests. Training starts only when the interfaces are tested, and the dress rehearsal needs everything.

## Critical path and gates from T-90 to T-1

From durations, dependencies and progress, the tool calculates forecast dates, float, the slack a task has before it delays others, and the critical path to the day IT is ready. Gates run from T-90, design frozen, to T-1, ready to open. It flags gates passed with open tasks, tasks forecast late, blocked work, tasks that must start this week and a risk register.

The output is `report.html` with a Gantt chart, `review.md` for the weekly meeting, `actions.csv` and a go-live checklist for T-7, T-1, opening day and the first week.

## How to use it with real data

The plan is exported with real vendor lead times and dependencies. It runs before each weekly meeting, daily from T-7, with the checklist printed for the dress rehearsal.

## Where it comes from

It comes from years supporting POS, hotel PMS and IPTV at a technology consultancy, where integrations and lead times, not the installation of each system, decide the opening.""",
 es="""
En la pre-apertura de un hotel los circuitos de internet tardan 75 días en llegar, y casi todos los demás sistemas de IT dependen de ellos. El tracker que acompaña a este post convierte la lista de tareas en un calendario que muestra qué retraso mueve la apertura. Su demo usa un hotel vacacional inventado de 120 habitaciones que abre en enero, con 30 tareas en nueve áreas y retrasos puestos a propósito.

El PMS en la nube, el sistema de gestión del hotel, se retrasa con la línea, igual que el interfaz de cargos a habitación, los cargos de llamadas y las pruebas de interfaces. La formación solo empieza cuando los interfaces están probados, y el ensayo general lo necesita todo.

## Camino crítico e hitos de T-90 a T-1

Con duraciones, dependencias y avance, la herramienta calcula fechas previstas, holgura, el margen de una tarea antes de retrasar a otras, y el camino crítico hasta el día en que IT está lista. Los hitos van de T-90, diseño cerrado, a T-1, listos para abrir. Marca hitos pasados con tareas abiertas, tareas que llegan tarde, trabajo bloqueado, tareas que tienen que empezar esta semana y un registro de riesgos.

El resultado es `report.html` con un diagrama de Gantt, `review.md` para la reunión semanal, `actions.csv` y una lista de puesta en marcha para T-7, T-1, el día de apertura y la primera semana.

## Cómo usarlo con datos reales

El plan se exporta con los plazos reales de los proveedores y las dependencias. Se ejecuta antes de cada reunión semanal, a diario desde T-7, con la lista impresa para el ensayo general.

## De dónde sale

Nace de años dando soporte a TPV, PMS hotelero e IPTV en una consultora tecnológica, donde lo que decide una apertura son los interfaces y los plazos de entrega, no la instalación de cada sistema."""),
dict(n="25", repo="25-security-controls-evidence", date="2026-10-19", updated="2026-11-19", cat="tools",
 title_en="A control register for ISO 27001, NIS2 and GDPR finds the evidence an auditor will ask for and nobody kept",
 title_es="Un registro de controles para ISO 27001, NIS2 y RGPD encuentra las evidencias que pedirá el auditor y nadie guardó",
 seo_title_en="ISO 27001, NIS2 and GDPR evidence tracker · Iñigo González",
 seo_title_es="Evidencias para ISO 27001, NIS2 y RGPD · Iñigo González",
 seo_desc="One control register mapped to three frameworks that finds missing, late or failing evidence, expired exceptions and how ready each framework is for the audit date.",
 seo_desc_es="Un registro de controles mapeado a tres marcos que encuentra evidencias que faltan, llegan tarde o fallan, excepciones caducadas y cómo de listo está cada…",
 dek_en="A register, published with a made-up company five weeks before an ISO 27001 audit, maps 23 controls to three frameworks and finds missing, late or failing evidence and expired exceptions.",
 dek_es="Un registro, publicado con una empresa inventada a cinco semanas de una auditoría ISO 27001, mapea 23 controles a tres marcos y encuentra evidencias que faltan, llegan tarde o fallan, y excepciones caducadas.",
 en="""
Most audit findings are not about missing security but about missing proof: a quarterly restore test done in June but not in September, a control marked implemented with nothing behind it, a DLP exception that expired last month. That is the gap the control and evidence register published with this post is built to find. Its demo is a made-up company with 23 controls, 33 evidence items and 3 exceptions against 48 requirements, five weeks before an ISO 27001 surveillance audit, with gaps placed on purpose.

The register maps each control and its evidence to ISO/IEC 27001:2022, NIS2 and GDPR at once. The same restore test answers all three frameworks, yet it is often collected three times by three people, or not at all. Its checks cover evidence, controls, exceptions, coverage per requirement and data quality.

## Every requirement covered, excluded, at risk or a gap

For the audit date, each requirement gets one of four states, with what stands in its way. That gives the readiness of each framework. A failing immutable backup copy, unlinked to any control, is the kind of problem the cross-check brings to the surface.

The output is a web report with a nine-week collection plan, a summary for the security review, a list of actions, an `audit-pack.csv` index for the auditor, a `soa.csv` in Statement-of-Applicability form and `evidence-calendar.ics` with every due date.

## How to use it with real data

It runs on Python with the standard library only and comes with 14 tests. The control register and evidence index are exported to CSV with the columns mapped, the requirements of each audit are added to the catalogue, and the calendar file goes into the team calendar before each security review.

## Where it comes from

It comes from applying ISO 27001, NIS2 and GDPR in IT operations, preparing evidence and answering audits. I learned that one piece of evidence well kept serves several frameworks, and that the calendar of what to collect matters as much as the controls themselves.""",
 es="""
La mayoría de hallazgos de auditoría no son por falta de seguridad, sino por falta de pruebas: una prueba de restauración trimestral hecha en junio pero no en septiembre, un control marcado como implantado sin nada detrás, una excepción de DLP que caducó el mes pasado. Ese es el hueco que busca el registro de controles y evidencias que acompaña a este post. Su demo es una empresa inventada con 23 controles, 33 evidencias y 3 excepciones frente a 48 requisitos, a cinco semanas de una auditoría de seguimiento de ISO 27001, con brechas puestas a propósito.

El registro mapea cada control y su evidencia a ISO/IEC 27001:2022, NIS2 y RGPD a la vez. La misma prueba de restauración responde a los tres marcos, pero muchas veces la recogen tres personas tres veces, o nadie. Sus comprobaciones cubren evidencias, controles, excepciones, cobertura por requisito y calidad de los datos.

## Cada requisito, cubierto, excluido, en riesgo o como brecha

Para la fecha de auditoría, cada requisito recibe uno de esos cuatro estados, con lo que lo impide. De ahí sale el grado de preparación de cada marco. Una copia inmutable del backup que falla sin estar relacionada con ningún control es el tipo de problema que el cruce saca a la luz.

La salida es un informe web con un plan de recogida a nueve semanas, un resumen para la revisión de seguridad, una lista de acciones, un índice `audit-pack.csv` para el auditor, un `soa.csv` en formato de Declaración de Aplicabilidad y `evidence-calendar.ics` con cada fecha de vencimiento.

## Cómo usarlo con datos reales

Funciona con Python y solo la librería estándar, y trae 14 tests. El registro de controles y el índice de evidencias se exportan a CSV adaptando las columnas, los requisitos de cada auditoría se añaden al catálogo y el calendario se importa en el del equipo antes de cada revisión de seguridad.

## De dónde sale

Nace de aplicar ISO 27001, NIS2 y RGPD en operaciones de IT, preparando evidencias y respondiendo auditorías. Aprendí que una evidencia bien guardada sirve para varios marcos, y que el calendario de lo que hay que recoger importa tanto como los propios controles."""),
dict(n="26", repo="26-ot-segmentation-lab", date="2026-10-20", cat="tools",
 title_en="A plant network lab finds old commissioning rules and vendor RDP to an HMI that bypass the segmentation",
 title_es="Un laboratorio de planta halla reglas antiguas y accesos RDP de proveedor a un HMI que se saltan la segmentación",
 seo_title_en="OT segmentation lab: Purdue and IEC 62443 · Iñigo González",
 seo_title_es="Segmentación OT: Purdue e IEC 62443 · Iñigo González",
 seo_desc="Zones, assets, firewall rules and observed traffic side by side: risky paths into OT, remote access that skips the jump host, and a tighter rule set built from what the plant really uses.",
 seo_desc_es="Zonas, activos, reglas de firewall y tráfico observado juntos: caminos de riesgo hacia OT, accesos remotos que se saltan el jump host y un conjunto de reglas…",
 dek_en="A lab built on a made-up bottling plant puts zones, assets, firewall rules and a week of traffic side by side against the Purdue model and IEC 62443, and proposes a tighter rule set from what the plant really uses.",
 dek_es="Un laboratorio sobre una planta embotelladora inventada pone juntos zonas, activos, reglas de firewall y una semana de tráfico frente al modelo Purdue e IEC 62443, y propone reglas más ajustadas a lo que la planta usa de verdad.",
 en="""
On a plant network the risky paths are rarely the ones in the diagram: a commissioning rule that still allows anything from the office to the plant servers years later, a finance PC reading a PLC with Modbus for a report, a vendor connecting with RDP straight to an HMI. That is what the segmentation lab published with this post looks for. It is a lab, not a real site: a made-up bottling plant with 8 zones, 25 assets, 16 conduits and a week of flows, with the problems placed on purpose.

The cause is that the rule set, the inventory and the real traffic each tell a different story; a temporary upgrade rule that expired a month ago can still carry traffic. The lab puts the three side by side and checks them against the Purdue model, which stacks plant systems in levels from the machines up to the office, and the zones and conduits idea of IEC 62443, which groups systems in zones and controls every link between them.

## Controller protocols from L3 and above and a safety system reachable from control

The checks flag rules that bypass the DMZ or skip a level, controller protocols coming from L3 or above, cleartext admin protocols, OT devices talking to the internet, remote access that does not start on the jump host (the single entry server for remote sessions) and the safety system reachable from control.

Asset and data checks add devices missing from the inventory, assets outside their zone's subnet, end-of-life Windows in OT and zones without an owner. The report draws a Purdue diagram coloured by status, a zone-to-zone matrix and `firewall-proposal.csv`, which says allow, review, re-route via DMZ or block for each observed service.

## How to use it with real data

It runs on Python with the standard library only, with 16 tests and a runbook for the segmentation review. It takes zones, inventory and firewall rules in CSV, plus a week of flows from the firewall or NetFlow. The proposal is reviewed with the plant before blocking anything, and each change goes through CAB with a rollback.

## Where it comes from

It builds on years supporting data centre and IT-OT integration work: Cisco switches and routers, comms rooms and racks, FortiGate firewalls, connectivity providers, DR/BCP tests and CAB changes with a rollback plan. That work taught me a plant firewall change is only safe when you know what traffic really crosses it. I am now studying IEC 62443 zones and conduits, and this lab is how I practise it.""",
 es="""
En una red de planta los caminos de riesgo casi nunca son los del diagrama: una regla de la puesta en marcha que años después sigue permitiendo todo desde la oficina hacia los servidores de planta, un PC de finanzas que lee un PLC con Modbus para un informe, un proveedor que entra por RDP directamente a un HMI. Eso es lo que busca el laboratorio de segmentación que acompaña a este post. Es un laboratorio, no una instalación real: una planta embotelladora inventada con 8 zonas, 25 activos, 16 conductos y una semana de flujos, con los problemas puestos a propósito.

La causa es que las reglas, el inventario y el tráfico real cuentan cada uno una historia distinta; una regla temporal de una actualización caducada hace un mes puede seguir pasando tráfico. El laboratorio los pone juntos y los compara con el modelo Purdue, que ordena los sistemas de planta en niveles desde las máquinas hasta la oficina, y con la idea de zonas y conductos de IEC 62443, que agrupa los sistemas en zonas y controla cada enlace entre ellas.

## Protocolos de controlador desde L3 o superior y un sistema de seguridad alcanzable desde control

Las comprobaciones señalan reglas que se saltan la DMZ o un nivel, protocolos de controlador desde L3 o superior, protocolos de administración en claro, equipos OT hablando con internet, accesos remotos que no empiezan en el jump host (el único servidor de entrada para las sesiones remotas) y el sistema de seguridad alcanzable desde control.

Las comprobaciones de activos y datos añaden equipos que no están en el inventario, activos fuera de la subred de su zona, Windows sin soporte en OT y zonas sin responsable. El informe dibuja un diagrama Purdue coloreado por estado, una matriz zona a zona y `firewall-proposal.csv`, que dice permitir, revisar, redirigir por la DMZ o bloquear para cada servicio observado.

## Cómo usarlo con datos reales

Funciona con Python y solo la librería estándar, con 16 tests y un runbook para la revisión de segmentación. Las zonas, el inventario y las reglas de firewall se exportan a CSV, junto con una semana de flujos del firewall o de NetFlow. La propuesta se revisa con la planta antes de bloquear nada, y cada cambio pasa por CAB con vuelta atrás.

## De dónde sale

Se apoya en años dando soporte a centro de datos e integración IT-OT: switches y routers Cisco, salas de comunicaciones y racks, firewalls FortiGate, proveedores de conectividad, pruebas de DR/BCP y cambios por CAB con plan de vuelta atrás. Ese trabajo me enseñó que un cambio de firewall en planta solo es seguro cuando sabes qué tráfico pasa de verdad. Ahora estudio zonas y conductos de IEC 62443, y este laboratorio es mi forma de practicarlo."""),
dict(n="27", repo="27-m365-tenant-governance-review", date="2026-10-21", cat="tools",
 title_en="A Global Admin left on for two years and a rejected change made anyway show how a Microsoft 365 tenant drifts",
 title_es="Un Global Admin activo dos años y un cambio rechazado hecho igualmente: así deriva un tenant de Microsoft 365",
 seo_title_en="Microsoft 365 tenant governance review · Iñigo González",
 seo_title_es="Revisión de gobierno del tenant Microsoft 365 · Iñigo González",
 seo_desc="Admin roles and PIM, emergency accounts, Conditional Access basics, settings drift, licences to reclaim, and admin changes matched to change tickets, including the provider's.",
 seo_desc_es="Roles de administración y PIM, cuentas de emergencia, lo básico de Acceso condicional, desviaciones de configuración, licencias a recuperar y cambios…",
 dek_en="A monthly review, published with a made-up retailer of 395 accounts run by a fictional provider, checks admin roles, emergency accounts, Conditional Access, settings drift and licences, and matches admin changes to change tickets.",
 dek_es="Una revisión mensual, publicada con un comercio inventado de 395 cuentas que opera un proveedor ficticio, comprueba roles de administración, cuentas de emergencia, Acceso condicional, desviaciones y licencias, y cruza los cambios con sus tickets.",
 en="""
A Microsoft 365 tenant drifts one reasonable change at a time: a Global Administrator given for a migration is still always-on two years later, and a change to allow automatic mail forwarding is rejected by the change board and made anyway. That is the kind of drift the monthly governance review published with this post is built to catch. It runs on a read-only export of a made-up retailer with 395 accounts, operated by a fictional provider, with the problems placed on purpose.

When a provider runs the platform, its engineers may hold permanent admin roles with no end date, while the risk stays with the internal team, which needs a short list for its monthly review.

## Every admin change matched to a ticket

The review covers six areas: privileged access, emergency accounts, the four Conditional Access basics, ten tenant settings against a baseline, licences, and sensitive admin changes. Conditional Access is the set of rules that decides who can sign in, from where and how.

Each change to roles, Conditional Access, tenant or mail-flow settings is matched to a change ticket by implementer and window, and comes out as approved, emergency, rejected, no ticket or made with an emergency account. A legacy authentication block left in report-only mode since July is the kind of setting that shows up as drift.

The output is a web report, a summary with a section for the service review with the provider, a list of actions, `privileged-access.csv` for the quarterly access review, `licence-reclaim.csv` and `admin-changes.csv`.

## How to use it with real data

The analysis runs on Python with the standard library only, with 16 tests and a runbook. A read-only PowerShell exporter reads Microsoft Graph and, optionally, Exchange Online, using a Global Reader account. Role names and the Conditional Access mapping are checked on the first run, and the baseline is agreed with security beforehand.

## Where it comes from

It comes from running Microsoft 365 as Global Administrator: PIM and just-in-time access, admin rights granted only for a limited time, Conditional Access, Exchange Online, Purview, tenant-to-tenant migrations and changes through CAB with providers. Governance is not a one-off hardening project but a monthly habit, and the change ticket keeps the provider and the internal team on the same page.""",
 es="""
Un tenant de Microsoft 365 se desvía cambio razonable a cambio razonable: un Global Administrator dado para una migración sigue activo dos años después, y un cambio para permitir el reenvío automático del correo se rechaza en el comité de cambios y se hace igualmente. Ese es el tipo de desviación que busca la revisión mensual de gobierno que acompaña a este post. Trabaja sobre una exportación de solo lectura de un comercio inventado con 395 cuentas, operado por un proveedor ficticio, con los problemas puestos a propósito.

Cuando la plataforma la opera un proveedor, sus ingenieros pueden tener roles de administración permanentes sin fecha de fin, mientras el riesgo sigue siendo del equipo interno, que necesita una lista corta para su revisión mensual.

## Cada cambio de administración, cruzado con un ticket

La revisión cubre seis áreas: acceso privilegiado, cuentas de emergencia, lo básico de Acceso condicional, diez ajustes del tenant frente a una línea base, licencias y cambios de administración sensibles. El Acceso condicional es el conjunto de reglas que decide quién puede iniciar sesión, desde dónde y cómo.

Cada cambio en roles, Acceso condicional, ajustes del tenant o del flujo de correo se cruza con un ticket de cambio por implementador y ventana, y sale como aprobado, de emergencia, rechazado, sin ticket o hecho con una cuenta de emergencia. Un bloqueo de la autenticación heredada que lleva en modo solo informe desde julio es el tipo de ajuste que aparece como desviación.

La salida es un informe web, un resumen con una sección para la revisión de servicio con el proveedor, una lista de acciones, `privileged-access.csv` para la revisión trimestral de accesos, `licence-reclaim.csv` y `admin-changes.csv`.

## Cómo usarlo con datos reales

El análisis funciona con Python y solo la librería estándar, con 16 tests y un runbook. Un exportador de solo lectura en PowerShell lee Microsoft Graph y, si se quiere, Exchange Online, con una cuenta Global Reader. En la primera ejecución se revisan los nombres de roles y el mapeo de Acceso condicional, y la línea base se acuerda antes con seguridad.

## De dónde sale

Nace de administrar Microsoft 365 como Global Administrator: PIM y acceso just-in-time, con permisos de administración solo por un tiempo limitado, Acceso condicional, Exchange Online, Purview, migraciones de tenant a tenant y cambios por CAB con proveedores. El gobierno de un tenant no es un proyecto de bastionado puntual sino un hábito mensual, y el ticket de cambio mantiene alineados al proveedor y al equipo interno."""),
dict(n="28", repo="28-euc-provider-service-review", date="2026-10-22", cat="tools",
 title_en="The provider reports 96% and users say it is slow: both are right, and the raw tickets show why",
 title_es="El proveedor dice 96% y los usuarios, que va lento: los dos tienen razón y los tickets en bruto explican por qué",
 seo_title_en="EUC provider service review: SLA and OLA · Iñigo González",
 seo_title_es="Revisión del servicio EUC del proveedor: SLA y OLA · Iñigo González",
 seo_desc="SLA scorecard with the breach list, backlog and ageing, escalations and the OLAs we owe the provider, out-of-hours coverage, the quality signals a compliance figure hides, and the service credits nobody has claimed.",
 seo_desc_es="Cuadro de SLA con la lista de incumplimientos, backlog y antigüedad, escalados y las OLAs que le debemos al proveedor, cobertura fuera de horario, las señales…",
 dek_en="A monthly service review, published with 1,454 fictional tickets from a made-up trading company and its fictional provider, recomputes the SLAs from the raw tickets, adds the internal teams' OLAs and works out the service credits nobody claimed.",
 dek_es="Una revisión mensual del servicio, publicada con 1.454 tickets ficticios de una empresa de trading inventada y su proveedor ficticio, recalcula los SLA desde los tickets en bruto, suma las OLAs de los equipos internos y calcula los créditos que nadie reclamó.",
 en="""
The provider's monthly pack says 96% and the users say the end-user service is slow, and both are usually right. The P2 figure leaves out tickets that spent a week in "waiting for customer", and a fifth of the compliant tickets were closed in the last 10% of the window. That is the gap the monthly service review published with this post is built to explain. Its demo is a made-up trading company with offices in four cities, run by a fictional provider with an offshore desk and onsite teams, and 1,454 tickets with the problems placed on purpose.

The cause is in how the figure is computed. Out-of-hours P2s wait for the follow-the-sun hand-over between time zones, and the average hides them. The tool recomputes the SLA, the service levels agreed in the contract, from the raw tickets with the rules written down, so both sides accept one set of numbers.

## A 19% escalation rate and twelve tickets stuck on the internal side

In the scenario, the provider escalated 19% of its tickets to the internal teams, and the network team has been sitting on twelve of them since July, so that breach belongs to the internal side. The tool measures those escalations against OLAs, the targets the internal teams owe the provider, with the clock starting at the hand-over.

The review covers six areas: SLA per type and priority with business-hours or 24x7 clocks and pending time subtracted; backlog and ageing by team; escalations; coverage in and out of hours; quality, from reopens and first-contact resolution to satisfaction, last-minute closes, parked tickets and instant closes; and the contract. For the contract it computes the service credits per missed metric, up to the monthly cap, which nobody had claimed because nobody had computed them.

## An agenda with two sides

The output includes a web report and `service-review.md`, an agenda with what to raise with the provider and what is owed to it, plus `actions.csv` with owners, a scorecard, `breaches.csv` with a `cause` column for the provider, `ageing.csv` with a `decision` column, escalations and findings.

## How to use it with real data

It runs on Python with the standard library only, with 16 tests and a runbook for before, during and after the meeting. A read-only PowerShell exporter covers Jira Cloud, and ServiceNow list exports load as they are. The first run goes next to the provider's own pack, and the difference between the two, the exclusions, is the first thing to agree.

## Where it comes from

It comes from managing end-user services with providers: SLAs and OLAs, provider and contract negotiation, backlog follow-up, escalations with offshore teams and process ownership for incidents, requests, changes and problems. The review goes better when the internal OLAs sit next to the provider's SLAs; half of the "provider problems" turn out to be queues on our side.""",
 es="""
El informe mensual del proveedor dice 96% y los usuarios dicen que el servicio de puesto de trabajo va lento, y normalmente los dos tienen razón. El dato de P2 deja fuera los tickets que pasaron una semana en «esperando al usuario», y una quinta parte de los tickets cumplidos se cerraron en el último 10% de la ventana. Ese es el hueco que explica la revisión mensual del servicio que acompaña a este post. Su demo es una empresa de trading inventada con oficinas en cuatro ciudades, operada por un proveedor ficticio con un service desk offshore y equipos presenciales, y 1.454 tickets con los problemas puestos a propósito.

La causa está en cómo se calcula el dato. Los P2 fuera de horario esperan al relevo del follow-the-sun entre husos horarios, y la media los esconde. La herramienta recalcula el SLA, los niveles de servicio acordados en el contrato, desde los tickets en bruto y con las reglas escritas, para que las dos partes acepten un único conjunto de números.

## Un 19% de escalados y doce tickets parados en el lado interno

En el escenario, el proveedor escaló el 19% de sus tickets a los equipos internos, y el equipo de red tiene doce desde julio, así que ese incumplimiento es del lado interno. La herramienta mide esos escalados frente a las OLAs, los objetivos que los equipos internos le deben al proveedor, con el reloj arrancando en el traspaso.

La revisión cubre seis áreas: SLA por tipo y prioridad con reloj de horario laboral o 24x7 y el tiempo en pendiente descontado; backlog y antigüedad por equipo; escalados; cobertura dentro y fuera de horario; calidad, desde reaperturas y resolución al primer contacto hasta satisfacción, cierres de último minuto, tickets aparcados y cierres instantáneos; y el contrato. Para el contrato calcula los créditos de servicio por métrica incumplida, hasta el tope mensual, que nadie había reclamado porque nadie los había calculado.

## Un orden del día con dos lados

La salida incluye un informe web y `service-review.md`, un orden del día con qué plantear al proveedor y qué se le debe, además de `actions.csv` con responsables, un cuadro de mando, `breaches.csv` con una columna `cause` para el proveedor, `ageing.csv` con una columna `decision`, escalados y hallazgos.

## Cómo usarlo con datos reales

Funciona con Python y solo la librería estándar, con 16 tests y un runbook para antes, durante y después de la reunión. Un exportador de solo lectura en PowerShell cubre Jira Cloud, y las exportaciones de lista de ServiceNow cargan tal cual. La primera ejecución se hace junto al informe del proveedor, y la diferencia entre los dos, las exclusiones, es lo primero que hay que acordar.

## De dónde sale

Nace de gestionar servicios de puesto de trabajo con proveedores: SLAs y OLAs, negociación de proveedores y contratos, seguimiento del backlog, escalados con equipos offshore y ser process owner de incidencias, peticiones, cambios y problemas. La revisión va mejor cuando las OLAs internas están junto a los SLAs del proveedor; la mitad de los «problemas del proveedor» resultan ser colas de nuestro lado."""),
dict(n="29", repo="29-tenant-separation-cutover-planner", date="2026-10-23", cat="tools",
 title_en="Wave 3 is on the 30th and the inventory says no: a third of the plant's devices have no TPM",
 title_es="La ola 3 es el día 30 y el inventario dice que no: un tercio de los equipos de la planta no tiene TPM",
 seo_title_en="Microsoft 365 tenant separation planner · Iñigo González",
 seo_title_es="Separación de tenant Microsoft 365: plan de olas · Iñigo González",
 seo_desc="Devices that cannot be reset into the target, users who will fail on day 1, applications without a decision, and a go or no-go per wave with the reason, from the source tenant's own exports.",
 seo_desc_es="Equipos que no se pueden resetear al tenant destino, usuarios que van a fallar el primer día, aplicaciones sin decisión y un go o no-go por ola con su motivo…",
 dek_en="A readiness planner for splitting a Microsoft 365 tenant, published with a made-up carve-out of 1,208 devices and 1,182 users, reads the source tenant's own exports and gives each wave a go or no-go with the reason.",
 dek_es="Un planificador de preparación para separar un tenant de Microsoft 365, publicado con una segregación inventada de 1.208 equipos y 1.182 usuarios, lee las exportaciones del propio tenant origen y da a cada ola un go o no-go con su motivo.",
 en="""
The programme plan says "wave 3, the plant, 30 November", but the inventory says a third of the plant's devices have no TPM, the security chip Windows 11 needs, fourteen kiosks have no primary user and ninety devices run an HMI application nobody has catalogued. On top of that, the wave has two more devices than the technicians can reset in four days. That is the scenario the tenant separation planner published with this post is built around. Its demo is a made-up carve-out of an automotive dealer group from its parent, with four sites and six waves.

None of that shows in the project tracker, and all of it is in the Intune, Entra and Exchange exports. A tenant separation is a thousand small resets that all have to work on the same weekend, so the planner starts the readiness review from those exports, not from the plan.

## Four blockers that stop a wave

On devices, four findings block a wave: no Autopilot hardware hash in the target, the fingerprint that lets a reset device join the new tenant; a BitLocker key not escrowed; hardware not Windows 11 capable; and devices not seen for weeks. Other findings become actions for the day itself, such as an OS below the baseline, low disk, domain-only joins, non-compliant devices, local admins the reset will remove, and kiosks and applications without a decision.

On users, the planner flags those with no MFA method, whom Conditional Access in the target will stop on day 1, mailboxes too big for the window, licences with no SKU bought in the target, shared mailboxes split across waves, dormant users and leavers.

## Six waves, each failing for a different reason

Each wave gets a go, a go with actions or a no-go, with the reason: technician capacity in devices per day, the blocked share, mailbox hours against the migration window, freeze windows, or a pilot that waits for the target tenant to be finished. In the demo, with 1,208 devices and 1,182 users, the problems are placed so each wave fails for a different reason.

The output is a web report, `cutover-plan.md` for the change board with the prerequisites checklist and the order of the cutover day, `blockers.csv` with owner and cleared columns, and CSVs per wave, device, user and application.

## How to use it with real data

It runs on Python with the standard library only, with 22 tests and a runbook with the weekly cadence, how to read the verdicts and the usual fix per finding. A read-only PowerShell exporter covers Microsoft Graph and Exchange Online. It is meant to run every week of the programme, after the wave rules and freeze calendar are agreed with the change board.

## Where it comes from

It comes from tenant-to-tenant migrations and the Microsoft 365 administration behind them, Windows Autopilot and Intune with ConfigMgr co-management, a Windows 11 migration across sites, and CAB changes with freeze windows. A wave rarely fails on the day; it fails weeks before, when nobody counts the devices without a hardware hash or the users without MFA.""",
 es="""
El plan del programa dice «ola 3, la planta, 30 de noviembre», pero el inventario dice que un tercio de los equipos de la planta no tiene TPM, el chip de seguridad que exige Windows 11, que catorce kioscos no tienen usuario principal y que noventa equipos llevan una aplicación HMI que nadie ha catalogado. Además, la ola tiene dos equipos más de los que los técnicos pueden resetear en cuatro días. Ese es el escenario sobre el que se construye el planificador de separación de tenant que acompaña a este post. Su demo es una segregación inventada de un grupo de concesionarios de automoción respecto a su matriz, con cuatro sedes y seis olas.

Nada de eso aparece en el seguimiento del proyecto, y todo está en las exportaciones de Intune, Entra y Exchange. Una separación de tenant son mil reseteos pequeños que tienen que salir bien el mismo fin de semana, así que el planificador empieza la revisión de preparación por esas exportaciones, no por el plan.

## Cuatro bloqueos que paran una ola

En los equipos, cuatro hallazgos bloquean una ola: no tener el hardware hash de Autopilot en el destino, la huella que permite que un equipo reseteado entre en el nuevo tenant; una clave de BitLocker sin custodiar; hardware no apto para Windows 11, y equipos que no se conectan desde hace semanas. Otros hallazgos pasan a ser acciones para el propio día, como un sistema por debajo de la línea base, poco disco, equipos solo unidos al dominio, equipos no conformes, administradores locales que el reseteo va a quitar, y kioscos y aplicaciones sin decisión.

En los usuarios, el planificador señala a los que no tienen método de MFA, a quienes el acceso condicional del destino parará el primer día, buzones demasiado grandes para la ventana, licencias sin SKU comprado en el destino, buzones compartidos repartidos entre olas, usuarios inactivos y bajas.

## Seis olas, cada una falla por un motivo distinto

Cada ola recibe un go, un go con acciones o un no-go, con su motivo: la capacidad de los técnicos en equipos por día, el porcentaje de bloqueados, las horas de migración de buzones frente a la ventana, los periodos de congelación o un piloto que espera a que el tenant destino esté terminado. En la demo, con 1.208 equipos y 1.182 usuarios, los problemas están puestos para que cada ola falle por un motivo distinto.

La salida es un informe web, `cutover-plan.md` para el comité de cambios con el checklist de prerrequisitos y el orden del día del corte, `blockers.csv` con columnas de responsable y resuelto, y los CSV por ola, equipo, usuario y aplicación.

## Cómo usarlo con datos reales

Funciona con Python y solo la librería estándar, con 22 tests y un runbook con la cadencia semanal, cómo leer los veredictos y la corrección habitual de cada hallazgo. Un exportador de solo lectura en PowerShell cubre Microsoft Graph y Exchange Online. Está pensado para ejecutarse cada semana del programa, después de acordar con el comité de cambios las reglas de las olas y el calendario de congelación.

## De dónde sale

Nace de migraciones tenant a tenant y de la administración de Microsoft 365 que hay detrás, de Windows Autopilot e Intune con co-gestión de ConfigMgr, de una migración a Windows 11 en varias sedes y de cambios por el CAB con periodos de congelación. Una ola rara vez falla el día del corte; falla semanas antes, cuando nadie cuenta los equipos sin hardware hash o los usuarios sin MFA."""),
dict(n="30", repo="30-jira-confluence-admin-kit", date="2026-10-24", cat="tools",
 title_en="A monthly Jira and Confluence review finds 128 unused licences and a sprint still open nine days late",
 title_es="Una revisión mensual de Jira y Confluence halla 128 licencias sin uso y un sprint abierto nueve días tarde",
 seo_title_en="Jira and Confluence admin review · Iñigo González",
 seo_title_es="Revisión de admin de Jira y Confluence · Iñigo González",
 seo_desc="Licences to reclaim with the saving, admins who should not be admins, external users and service accounts without an owner, projects, spaces and custom fields to clean up, and the agile health of every Scrum board, from the site's own exports.",
 seo_desc_es="Licencias a recuperar con el ahorro, administradores que no deberían serlo, usuarios externos y cuentas de servicio sin responsable, proyectos, espacios…",
 dek_en="A monthly admin review, published with a made-up warehouse-robotics company on Atlassian Cloud, finds licences to reclaim, admins who should not be admins, clutter to clean up and the agile health of every Scrum board, including a sprint nine days late.",
 dek_es="Una revisión mensual de administración, publicada con una empresa inventada de robótica de almacenes en Atlassian Cloud, encuentra licencias a recuperar, administradores que sobran, restos que limpiar y la salud ágil de cada tablero Scrum, con un sprint nueve días tarde.",
 en="""
The monthly Jira and Confluence review published with this post finds 128 unused licences in its demo. One of the causes it flags is the default group: everybody who joins gets Jira through it, whether they will use it or not. The same run finds a sprint still open nine days past its end date. The demo is a made-up warehouse-robotics company on Jira, Jira Service Management and Confluence Cloud, with 437 user accounts, 61 projects, 77 spaces, 460 custom fields and 12 Scrum boards, and the problems placed on purpose.

An Atlassian site grows by itself. Contractors keep access after the project ends, a demo project still lets Anyone browse it, and a third of the 460 custom fields have not been used in a year. None of this is hard to fix; it is hard to see.

## Licences, admins and the accounts nobody owns

The licence check flags product access not used for 90 days, never used after the grace period or kept by suspended accounts, with the cost per year and the seats against what was bought. The access check looks for more admins than the target, admins who are deactivated or idle or use personal domains, external users by domain and service accounts without a named owner. A colleague added to `jira-admins` "for a day" two years ago is the kind of case it surfaces.

The hygiene check covers projects open to Anyone, projects without a lead or with a lead who has left, idle projects and spaces to archive, one-off permission and workflow schemes, spaces with anonymous access or no active admin, personal spaces of leavers, and custom fields to remove.

## Two boards carrying a third of every sprint

For each Scrum board, the review reads the last six sprints: sprints still open past their end date, carry-over, scope added after the start, say/do, the share of planned work actually delivered, and idle boards. Two boards carry over a third of every sprint, which nobody notices because the board still looks busy.

The output is a web report, `admin-review.md` as the agenda with the decisions as a checklist, `licences.csv` with `manager_ok` and `removed` columns, `access-review.csv` with a `decision` column, and CSVs per project, space, field and board. The licence renewal, the access review and the retrospective all get the same thing: a list, the rule behind each item and a column for the decision.

## How to use it with real data

It runs on Python with the standard library only, with 17 tests and a 45-minute runbook that explains how to read the agile numbers. A read-only PowerShell exporter covers the Jira, Agile and Confluence Cloud REST APIs, and the user export from admin.atlassian.com loads as it is. Managers get a week to object before any licence is removed.

## Where it comes from

It comes from administering Jira and Confluence and managing the relationship with Atlassian, working as Scrum Master and Product Owner, running release management through the CAB, and managing licences and vendors. The licence saving pays for the review, but the agile numbers are what teams come for: conversation starters for the retrospective, not targets.""",
 es="""
La revisión mensual de Jira y Confluence que acompaña a este post encuentra 128 licencias sin uso en su demo. Una de las causas que señala es el grupo por defecto: todo el que entra recibe Jira por él, lo vaya a usar o no. La misma ejecución detecta un sprint abierto nueve días después de su fecha de fin. La demo es una empresa inventada de robótica de almacenes con Jira, Jira Service Management y Confluence Cloud, con 437 cuentas de usuario, 61 proyectos, 77 espacios, 460 campos personalizados y 12 tableros Scrum, y los problemas puestos a propósito.

Un sitio de Atlassian crece solo. Los externos siguen con acceso cuando termina el proyecto, un proyecto de demo sigue abierto a Anyone y un tercio de los 460 campos personalizados no se ha usado en un año. Nada de esto es difícil de arreglar; es difícil de ver.

## Licencias, administradores y cuentas sin dueño

La comprobación de licencias señala el acceso a producto sin usar en 90 días, nunca usado pasado el periodo de gracia o en manos de cuentas suspendidas, con el coste anual y las licencias frente a las compradas. La de accesos busca más administradores que el objetivo, administradores desactivados, inactivos o con dominios personales, usuarios externos por dominio y cuentas de servicio sin responsable con nombre. Un compañero metido en `jira-admins` «por un día» hace dos años es el tipo de caso que saca a la luz.

La comprobación de higiene cubre proyectos abiertos a Anyone, proyectos sin responsable o con un responsable que ya no está, proyectos y espacios inactivos para archivar, esquemas de permisos y de flujo usados por un solo proyecto, espacios con acceso anónimo o sin administrador activo, espacios personales de bajas y campos personalizados que eliminar.

## Dos tableros que arrastran un tercio de cada sprint

Para cada tablero Scrum, la revisión lee los últimos seis sprints: sprints abiertos después de su fecha de fin, trabajo arrastrado, alcance añadido después del inicio, say/do, la parte del trabajo comprometido que de verdad se entrega, y tableros parados. Dos tableros arrastran un tercio de cada sprint al siguiente, cosa que nadie nota porque el tablero sigue pareciendo activo.

La salida es un informe web, `admin-review.md` como orden del día con las decisiones en forma de checklist, `licences.csv` con columnas `manager_ok` y `removed`, `access-review.csv` con una columna `decision`, y los CSV por proyecto, espacio, campo y tablero. La renovación de licencias, la revisión de accesos y la retrospectiva reciben lo mismo: una lista, la regla detrás de cada elemento y una columna para la decisión.

## Cómo usarlo con datos reales

Funciona con Python y solo la librería estándar, con 17 tests y un runbook de 45 minutos que explica cómo leer los números ágiles. Un exportador de solo lectura en PowerShell cubre las API REST de Jira, Agile y Confluence Cloud, y la exportación de usuarios de admin.atlassian.com carga tal cual. Los responsables tienen una semana para objetar antes de quitar ninguna licencia.

## De dónde sale

Nace de administrar Jira y Confluence y llevar la relación con Atlassian, de trabajar como Scrum Master y Product Owner, de llevar la gestión de releases por el CAB y de gestionar licencias y proveedores. El ahorro en licencias paga la revisión, pero los números ágiles son lo que interesa a los equipos: sirven para abrir la conversación en la retrospectiva, no son objetivos."""),
dict(n="31", repo="31-dealer-systems-health", date="2026-10-25", cat="tools",
 title_en="A warranty feed that stops on Thursday night goes unseen until the dealer asks on Tuesday",
 title_es="Un feed de garantías parado el jueves por la noche no se detecta hasta que el concesionario pregunta el martes",
 seo_title_en="Dealer network systems: weekly health review · Iñigo González",
 seo_title_es="Sistemas de una red de concesionarios: revisión semanal · Iñigo González",
 seo_desc="Weekly review of a dealer network: stopped DMS feeds, warranty claims near the deadline, parts and price files per dealer, in red, amber or green.",
 seo_desc_es="Feeds del DMS parados o vacíos, garantías a punto de caducar y por qué se rechazan, el catálogo de recambios y la tarifa que usa de verdad cada concesionario…",
 dek_en="The weekly review, published with fictional data from an importer with 53 dealers in Spain and Portugal, puts DMS feeds, warranty claims, parts catalogues and price files side by side per dealer, in red, amber or green.",
 dek_es="La revisión semanal, publicada con datos ficticios de un importador con 53 concesionarios en España y Portugal, pone juntos por concesionario los feeds del DMS, las garantías, los catálogos de recambios y las tarifas, en rojo, ámbar o verde.",
 en="""
A dealer's warranty feed that stops on a Thursday night goes unnoticed until the dealer asks on Tuesday why its claims have no answer, and a DMS job that finishes as a success with zero records alerts nobody. Those are the failures the weekly dealer network review published with this post is built to catch. It is an open-source tool that runs on demo data from a made-up importer with 53 dealers in Spain and Portugal, two weeks of interface runs and about 4,600 warranty claims, with the problems placed on purpose.

The DMS, the dealer management system each dealer runs, sends repair orders and warranty claims to the brand through feeds. The review flags feeds without a successful run within their limit, and for those two one failed night is already red.

## An old parts catalogue behind a rising rejection rate

A dealer still on last month's parts catalogue sends labour operations the warranty system no longer accepts, so its rejection rate climbs and the talk turns to bad claims. The review sets the catalogue and price file each dealer has actually applied against the current ones and their grace periods; a price file that did not apply means a week of parts sold at the wrong price.

On warranty, it lists drafts near or past the submission limit, claims waiting for the brand's own decision, possible duplicates with the same VIN, the vehicle identification number, and labour operation, and accepted claims never paid.

## A closed dealer with working credentials

The tool also flags DMS versions not certified for the brand interfaces, dealers opening with checklist items still open and terminated dealers still sending data: a dealer that closed in September can still have working interface credentials. The output is a red, amber and green grid of the network, an agenda for the weekly call and CSV files per topic.

## How to use it with real data

A read-only PowerShell exporter with example SQL queries refuses anything but a single SELECT. The tool runs on Python with the standard library only, with 15 tests and a runbook. The suggested start is one region's real exports, with each red dealer's line sent to its area manager before the call.

## Where it comes from

The tool comes from working with dealer management systems and dealer networks, warranty claim management and aftersales parts catalogues, together with integrations, vendors, SLAs and OLAs. The lesson behind it is that most dealer problems have a systems cause one step upstream: a rejection rate that is really an old catalogue.""",
 es="""
El feed de garantías de un concesionario que se para un jueves por la noche pasa inadvertido hasta que el concesionario pregunta el martes por qué sus reclamaciones no tienen respuesta, y un trabajo del DMS que termina bien con cero registros no avisa a nadie. Esos son los fallos que busca la revisión semanal de la red de concesionarios que acompaña a este post, una herramienta de código abierto que se ejecuta con datos de ejemplo de un importador inventado con 53 concesionarios en España y Portugal, dos semanas de ejecuciones de interfaces y unas 4.600 reclamaciones de garantía, con los problemas puestos a propósito.

El DMS, el sistema de gestión que usa cada concesionario, envía a la marca las órdenes de reparación y las garantías mediante feeds. La revisión marca los feeds sin una ejecución correcta dentro de su límite, y en esos dos una sola noche fallida ya es rojo.

## Un catálogo de recambios viejo detrás de una tasa de rechazo que sube

Un concesionario que sigue con el catálogo del mes pasado envía operaciones de mano de obra que el sistema de garantías ya no acepta, así que su tasa de rechazo sube y se acaba hablando de reclamaciones mal hechas. La revisión compara el catálogo y la tarifa que cada concesionario ha aplicado de verdad con los vigentes y sus periodos de gracia; una tarifa que no se aplicó significa una semana de recambios vendidos al precio equivocado.

En garantías, lista los borradores cerca o fuera del límite de envío, las reclamaciones que esperan la decisión de la propia marca, los posibles duplicados con el mismo VIN, el número de bastidor, y la misma operación, y las reclamaciones aceptadas nunca pagadas.

## Un concesionario cerrado con credenciales que funcionan

La herramienta señala además versiones de DMS no certificadas para las interfaces de la marca, concesionarios que abren con tareas del checklist sin cerrar y concesionarios dados de baja que siguen enviando datos: uno que cerró en septiembre puede seguir teniendo credenciales de interfaz que funcionan. El resultado es una cuadrícula roja, ámbar y verde de la red, un orden del día para la reunión semanal y ficheros CSV por tema.

## Cómo usarlo con datos reales

Un exportador de solo lectura en PowerShell con consultas SQL de ejemplo rechaza cualquier cosa que no sea un único SELECT. La herramienta funciona con Python y solo la librería estándar, con 15 tests y un runbook. Lo propuesto es empezar con las exportaciones reales de una región y enviar la línea de cada concesionario en rojo a su jefe de zona antes de la reunión.

## De dónde sale

La herramienta nace de trabajar con sistemas de gestión de concesionarios y redes de concesionarios, gestión de garantías y catálogos de recambios de posventa, junto con integraciones, proveedores, SLAs y OLAs. La lección que hay detrás es que la mayoría de los problemas del concesionario tienen una causa de sistemas un paso antes: una tasa de rechazo que en realidad es un catálogo viejo."""),
dict(n="32", repo="32-backup-restore-test-tracker", date="2026-10-25", updated="2026-11-19", cat="tools",
 title_en="A nightly backup that fails three nights in a row leaves a system three days outside its RPO",
 title_es="Un backup nocturno que falla tres noches seguidas deja un sistema tres días fuera de su RPO",
 seo_title_en="Backup restore tests and DR review · Iñigo González",
 seo_title_es="Pruebas de restauración de backups y DR · Iñigo González",
 seo_desc="The last good backup of each system against its RPO, offsite and immutable copies that actually ran, restore tests against the plan and the RTO, and the DR exercises and their actions, per system and tier, in red, amber or green.",
 seo_desc_es="El último backup bueno de cada sistema frente a su RPO, las copias offsite e inmutables que de verdad se hicieron, las pruebas de restauración frente al plan…",
 dek_en="The monthly review, published with fictional data from a manufacturer with 76 systems, cross-checks backup jobs, offsite copies, restore tests and DR exercises to show which systems have proven they can be brought back, and with what evidence.",
 dek_es="La revisión mensual, publicada con datos ficticios de un fabricante con 76 sistemas, cruza los trabajos de backup, las copias offsite, las pruebas de restauración y los ejercicios de DR para mostrar qué sistemas han demostrado que se pueden recuperar, y con qué evidencia.",
 en="""
A green backup dashboard says the jobs ran, not that a system can be brought back in the time promised to the business. A nightly job that failed three nights in a row is three days outside a 24-hour RPO, the recovery point objective, or how much data the business accepts losing. That is the gap the monthly backup and restore review published with this post is built to expose. It is an open-source tool that runs on demo data from a made-up manufacturer with 76 systems in three tiers, a year of restore tests and its DR exercises, with the problems placed on purpose.

The review measures the RPO from each system's last good backup and counts failure streaks. It also lists systems with no backup job and missing offsite or immutable copies. A copy job that has failed for a week leaves a system with one copy, in one place.

## Restoring a file does not prove the ERP comes back in four hours

On restore tests, the tool lists systems never restored, last tests that failed or half worked, and tests overdue for their tier. It compares restore times with the RTO, the recovery time objective, only on full restores: restoring a file proves the backup is readable, not that the ERP comes back in four hours.

## An auditor counts the evidence, not the tests

Tests with no evidence are flagged too. For DR exercises, the review shows the last one, those planned and not done, and overdue actions. The output is a web report with tier 1 at a glance and a 12-month calendar of tests due, an agenda for the meeting, and CSV files with tests due, failing backups and an evidence pack for the auditor.

## How to use it with real data

A read-only PowerShell exporter reads Veeam job sessions; other tools' job reports work as CSV. It runs on Python with the standard library only, with 13 tests and a runbook. The suggested start is the tier 1 systems with one month of real exports and next month's restore tests booked in the change calendar.

## Where it comes from

The tool comes from my work with Veeam Backup and Commvault, and tape backups earlier on, designing and testing backup and DR plans, and supervising DR and business continuity tests aligned with ISO 22301. The question that shaped it is not whether the job ran, but when we last proved a system can come back, how long it took and where the evidence is.""",
 es="""
Un panel de backups en verde dice que los trabajos se ejecutaron, no que un sistema se pueda recuperar en el tiempo prometido al negocio. Un trabajo nocturno que ha fallado tres noches seguidas está tres días fuera de un RPO de 24 horas, el objetivo de punto de recuperación, es decir, cuántos datos acepta perder el negocio. Ese es el hueco que saca a la luz la revisión mensual de backups y restauraciones que acompaña a este post, una herramienta de código abierto que se ejecuta con datos de ejemplo de un fabricante inventado con 76 sistemas en tres niveles, un año de pruebas de restauración y sus ejercicios de DR, con los problemas puestos a propósito.

La revisión mide el RPO desde el último backup bueno de cada sistema y cuenta las rachas de fallos. También lista los sistemas sin trabajo de backup y las copias offsite o inmutables que faltan. Una copia que lleva una semana fallando deja el sistema con una sola copia, en un solo sitio.

## Restaurar un fichero no demuestra que el ERP vuelva en cuatro horas

En las pruebas de restauración, la herramienta lista los sistemas nunca restaurados, las últimas pruebas fallidas o a medias y las vencidas para su nivel. Compara los tiempos con el RTO, el objetivo de tiempo de recuperación, solo en restauraciones completas: restaurar un fichero demuestra que el backup se puede leer, no que el ERP vuelva en cuatro horas.

## Un auditor cuenta las evidencias, no las pruebas

Las pruebas sin evidencia también se señalan. En los ejercicios de DR, la revisión muestra el último, los planificados y no hechos, y las acciones vencidas. El resultado es un informe web con el nivel 1 de un vistazo y un calendario de 12 meses de pruebas pendientes, un orden del día para la reunión y ficheros CSV con las pruebas pendientes, los backups que fallan y un paquete de evidencias para el auditor.

## Cómo usarlo con datos reales

Un exportador de solo lectura en PowerShell lee las sesiones de Veeam; los informes de otras herramientas sirven en CSV. Funciona con Python y solo la librería estándar, con 13 tests y un runbook. Lo propuesto es empezar con los sistemas de nivel 1 y un mes de exportaciones reales y reservar las pruebas del mes siguiente en el calendario de cambios.

## De dónde sale

La herramienta nace de mi trabajo con Veeam Backup y Commvault, y antes con backups en cinta, diseñando y probando planes de backup y DR, y supervisando pruebas de DR y continuidad de negocio alineadas con ISO 22301. La pregunta que le da forma no es si se ejecutó el trabajo, sino cuándo demostramos por última vez que un sistema se puede recuperar, cuánto tardó y dónde está la evidencia."""),
dict(n="33", repo="33-executive-meeting-readiness", date="2026-10-25", cat="tools",
 title_en="Board meeting failures show days ahead, like a chair's iPad that had not checked in for twelve days",
 title_es="Los fallos de un consejo se ven días antes, como el iPad del presidente que llevaba doce días sin conectar",
 seo_title_en="Board meeting IT readiness: Teams Rooms, VIP · Iñigo González",
 seo_title_es="Preparación IT de consejos: Teams Rooms y VIP · Iñigo González",
 seo_desc="For every board, committee and executive meeting in the next two weeks: the tech check, the Teams Room and its peripherals, updates inside the freeze, the VIP devices and the support engineer, with a verdict per meeting.",
 seo_desc_es="Para cada consejo, comité y reunión de dirección de las próximas dos semanas: la prueba técnica, la sala Teams Rooms y sus periféricos, actualizaciones dentro…",
 dek_en="The readiness check, published with fictional data from an insurer with eleven meeting rooms, joins Teams Rooms health, device management, room calendars and the service desk to give each board and executive meeting of the next two weeks a verdict.",
 dek_es="La revisión de preparación, publicada con datos ficticios de una aseguradora con once salas, junta la salud de Teams Rooms, la gestión de dispositivos, los calendarios de las salas y la herramienta de soporte para dar un veredicto a cada consejo y comité de las próximas dos semanas.",
 en="""
When a board meeting goes wrong, the causes were usually visible days earlier: the microphone array showed as disconnected in the Teams Rooms health, the chair's iPad had not checked in to the MDM, the mobile device management system, for twelve days, a room update was scheduled for the night before, and last week's rehearsal never happened. That is what the meeting readiness check published with this post is built to catch. It is an open-source tool that runs on demo data from a made-up insurer with eleven rooms in three offices, 13 meetings in the next two weeks, 20 VIP devices and 90 days of room incidents, with the problems placed on purpose.

The signals live in the Teams admin center, Intune or Jamf, the room calendars and the service desk. The check joins them per meeting and gives each a verdict: ready, attention or at risk. Readiness belongs to the meeting, not the room: the same degraded display is a note for a workshop and a decision for the board.

## Meetings without a tech check and rooms that do not fit

For board, committee and investor meetings, the tool flags those without a tech check in the last week, rooms that are too small or have no Teams Room for a hybrid meeting, overlapping bookings or no setup time, and no support engineer. In the rooms, it flags Teams Rooms offline, faulty peripherals, updates inside the freeze and repeated incidents.

## VIP devices below the minimum version

For the attendees, the check lists devices not compliant or not checked in, the OS or board app below the minimum, worn batteries and attendees with no registered device. The output is a day-by-day web report, a readiness pack with a checklist per meeting and attendee, and CSV files.

## How to use it with real data

A read-only PowerShell exporter for Microsoft Graph reads Teams Rooms health, room calendars and Intune devices. It runs on Python with the standard library only, with 13 tests and a runbook. The suggested start is next month's board and committee meetings with the pack sent to the company secretary's team the day before each board meeting.

## Where it comes from

The tool comes from supporting board and executive committee meetings: Teams Rooms on Crestron with Logitech and Poly systems, iPads, MacBooks and iPhones managed with Jamf Pro and Intune, and VIP support for executives and board members.""",
 es="""
Cuando un consejo sale mal, las causas solían verse días antes: el array de micrófonos aparecía desconectado en la salud de Teams Rooms, el iPad del presidente llevaba doce días sin conectar con el MDM, el sistema de gestión de dispositivos móviles, había una actualización de la sala programada para la noche anterior y la prueba técnica de la semana pasada nunca se hizo. Eso es lo que busca la revisión de preparación de reuniones que acompaña a este post, una herramienta de código abierto que se ejecuta con datos de ejemplo de una aseguradora inventada con once salas en tres oficinas, 13 reuniones en las próximas dos semanas, 20 dispositivos VIP y 90 días de incidencias de salas, con los problemas puestos a propósito.

Las señales están en el centro de administración de Teams, Intune o Jamf, los calendarios de las salas y la herramienta de soporte. La revisión las junta por reunión y da a cada una un veredicto: lista, atención o en riesgo. La preparación es de la reunión, no de la sala: la misma pantalla degradada es una nota para un taller y una decisión para el consejo.

## Reuniones sin prueba técnica y salas que no encajan

En consejos, comités y reuniones con inversores, la herramienta señala los que no tienen prueba técnica en la última semana, las salas pequeñas o sin Teams Rooms para una reunión híbrida, las reservas solapadas o sin tiempo de preparación y la falta de técnico asignado. En las salas, marca las Teams Rooms desconectadas, los periféricos con fallos, las actualizaciones dentro de la congelación y las incidencias repetidas.

## Dispositivos VIP por debajo de la versión mínima

En los asistentes, la revisión lista los dispositivos que no cumplen la política o no se han conectado, el sistema operativo o la app del consejo por debajo del mínimo, las baterías gastadas y los asistentes sin dispositivo registrado. El resultado es un informe web día a día, un pack de preparación con una lista de comprobación por reunión y asistente, y ficheros CSV.

## Cómo usarlo con datos reales

Un exportador de solo lectura en PowerShell para Microsoft Graph lee la salud de Teams Rooms, los calendarios de las salas y los dispositivos de Intune. Funciona con Python y solo la librería estándar, con 13 tests y un runbook. Lo propuesto es empezar con los consejos y comités del próximo mes y enviar el pack a la secretaría del consejo el día antes de cada consejo.

## De dónde sale

La herramienta nace de dar soporte a consejos y comités de dirección: Teams Rooms sobre Crestron con sistemas Logitech y Poly, iPads, MacBooks e iPhones gestionados con Jamf Pro e Intune, y soporte VIP a directivos y consejeros."""),
dict(n="34", repo="34-venue-service-readiness", date="2026-10-26", updated="2026-11-15", cat="tools",
 title_en="A beach kitchen printer in error since the afternoon before was visible hours before the pool club filled up",
 title_es="La impresora de la cocina de playa, en error desde la tarde anterior, se veía horas antes de llenarse el pool club",
 seo_title_en="Hospitality IT opening check: POS and Wi-Fi · Iñigo González",
 seo_title_es="Revisión IT de apertura en hostelería: TPV y Wi-Fi · Iñigo González",
 seo_desc="For every service in the next week, in a restaurant, a pool club, a bar and a hotel: the opening check, enough working tills and handhelds, kitchen printers, card terminals and cash machines, the network and the failover, the PMS and IPTV, and the vendor who would fix each of them, with a verdict per service.",
 seo_desc_es="Para cada servicio de la próxima semana, en un restaurante, un pool club, un bar y un hotel: la prueba de apertura, suficientes TPV y comanderos funcionando…",
 dek_en="The morning check, published with fictional data from a beach club and boutique hotel, joins the POS, the network, the cash machines, the PMS and the vendors' portals to give every service of the next week a verdict.",
 dek_es="La revisión de cada mañana, publicada con datos ficticios de un beach club con hotel boutique, junta el TPV, la red, los cajones de efectivo, el PMS y los portales de los proveedores para dar un veredicto a cada servicio de la próxima semana.",
 en="""
When a pool club fills up at one o'clock, the failures that hurt are orders that never reach the kitchen, a queue at the only working card terminal and room charges that never reach the guest's bill. In the example the post starts from, all of it was visible that morning: the beach kitchen printer had been in error since the afternoon before, two of the four handhelds were dead or in a drawer, the backup internet line had been down for five days and the PMS interface had 37 charges waiting. That is what the morning service check published with this post is built to catch. It is an open-source tool that runs on demo data from a made-up beach club and boutique hotel with a restaurant, a pool club, a sunset bar and 24 rooms, with the problems placed on purpose.

The demo covers 16 services in a week, including a 900-guest Halloween night, 74 devices and five vendors. The PMS is the hotel's property management system, where room charges land. The check joins the POS, network, cash machine, PMS and vendor data per service, because a service is only as ready as its weakest device.

## Fewer working tills and handhelds than the guests need

The tool flags services with fewer working tills and handhelds than the guests need, kitchen printers or the KDS, the kitchen display screens, down where food is served, card terminals down and cash machines in error or short of change. It also checks both internet lines, Wi-Fi, the PMS interface, IPTV and the key card encoders, and flags big events with nobody from IT on duty.

## A vendor who answers until seven for a bar that closes at one

In the same example, the POS vendor answers until seven in the evening and the bar closes at one. The review flags open tickets past each vendor's SLA, contracts ending and services outside the vendor's support hours. The output is a day-by-day web report, an opening checklist for the outlet managers and CSV files.

## How to use it with real data

A read-only PowerShell probe pings every device on the venue network and keeps the last time each one answered. It runs on Python with the standard library only, with 15 tests and a runbook. The suggested start is two weeks of mornings with the real device register and service plan, tuning the guests per till with the outlet managers.

## Where it comes from

The tool comes from my first years in IT supporting hospitality clients, with POS systems such as ICG and HIOPOS, CashDro cash machines, hotel PMS and IPTV, and later from around 200 pre-openings of luxury brand corners in department stores. At one of them the connection failed two hours before opening; I solved it with a temporary USB router while I checked the line and the floor's comms room with the store's technicians.""",
 es="""
Cuando el pool club se llena a la una, los fallos que duelen son las comandas que nunca llegan a cocina, la cola en el único datáfono que funciona y los cargos a habitación que no llegan a la factura del cliente. En el ejemplo del que parte el post, todo se veía esa misma mañana: la impresora de la cocina de playa llevaba en error desde la tarde anterior, dos de los cuatro comanderos estaban sin batería o en un cajón, la línea de internet de respaldo llevaba cinco días caída y el interfaz del PMS tenía 37 cargos pendientes. Eso es lo que busca la revisión de servicio de cada mañana que acompaña a este post, una herramienta de código abierto que se ejecuta con datos de ejemplo de un beach club con hotel boutique inventado, con restaurante, pool club, bar de atardecer y 24 habitaciones, con los problemas puestos a propósito.

La demo cubre 16 servicios en una semana, con una noche de Halloween para 900 personas, 74 equipos y cinco proveedores. El PMS es el sistema de gestión del hotel, donde llegan los cargos a habitación. La revisión junta por servicio los datos del TPV, la red, los cajones, el PMS y los proveedores, porque un servicio está tan preparado como su equipo más débil.

## Menos TPV y comanderos funcionando de los que necesitan los clientes

La herramienta señala los servicios con menos TPV y comanderos funcionando de los que necesitan los clientes, las impresoras de cocina o el KDS, las pantallas de cocina, caídos donde hay comida, los datáfonos caídos y los cajones de efectivo en error o sin cambio. También revisa las dos líneas de internet, el Wi-Fi, el interfaz del PMS, la IPTV y los codificadores de tarjetas, y marca los eventos grandes sin nadie de IT de guardia.

## Un proveedor que atiende hasta las siete para un bar que cierra a la una

En el mismo ejemplo, el proveedor del TPV atiende hasta las siete de la tarde y el bar cierra a la una. La revisión señala los tickets fuera del SLA de cada proveedor, los contratos que vencen y los servicios fuera del horario de soporte. El resultado es un informe web día a día, un checklist de apertura para los responsables de cada zona y ficheros CSV.

## Cómo usarlo con datos reales

Una prueba de solo lectura en PowerShell hace ping a cada equipo de la red del local y guarda la última vez que respondió. Funciona con Python y solo la librería estándar, con 15 tests y un runbook. Lo propuesto es empezar con dos semanas de mañanas con el inventario real y el plan de servicios y ajustar los clientes por TPV con los responsables de cada zona.

## De dónde sale

La herramienta nace de mis primeros años en IT dando soporte a clientes de hostelería, con TPV como ICG y HIOPOS, cajones CashDro, PMS hotelero e IPTV, y después de unas 200 preaperturas de corners de marcas de lujo en grandes almacenes. En una de ellas la conexión falló a dos horas de abrir; lo resolví con un router USB temporal mientras revisaba la línea y la sala de comunicaciones de la planta con los técnicos de los grandes almacenes."""),
dict(n="35", repo="35-private-cloud-capacity-review", date="2026-10-27", cat="tools",
 title_en="A private cloud cluster at 74% of its RAM crosses its N+1 limit in January once projects are counted",
 title_es="Un clúster de nube privada al 74% de su RAM cruza su límite N+1 en enero al contar los proyectos aprobados",
 seo_title_en="Private cloud capacity: vSphere and Nutanix · Iñigo González",
 seo_title_es="Capacidad de nube privada: vSphere y Nutanix · Iñigo González",
 seo_desc="For every vSphere and Nutanix cluster: the CPU and RAM left after a host failure, the vCPU ratio, a 12-month trend with the approved projects and the reclaim list, the month it crosses its N+1 limit against the purchase lead time, datastores, and the month's availability.",
 seo_desc_es="Para cada clúster vSphere y Nutanix: la CPU y la RAM que quedan tras caer un host, el ratio de vCPU, una tendencia de 12 meses con los proyectos aprobados…",
 dek_en="The monthly capacity review, published with fictional data from an engineering company's private cloud, turns vSphere and Nutanix utilisation, approved projects and the reclaim list into the month each cluster runs out of room and the date to order hosts.",
 dek_es="La revisión mensual de capacidad, publicada con datos ficticios de la nube privada de una empresa de ingeniería, convierte el uso de vSphere y Nutanix, los proyectos aprobados y la lista de recuperación en el mes en que cada clúster se queda sin margen y la fecha para pedir hosts.",
 en="""
A cluster at 74% of its RAM looks healthy on the dashboard, but without the host that HA, the high-availability feature, keeps as a spare it is at 85% of what is left. It grows half a point a month and two approved projects land in January and March, so it crosses its N+1 limit, the level at which it can still lose a host, in January. New hosts take four months to order, deliver and add, so the decision was due in September. That is the reasoning behind the monthly capacity review published with this post, an open-source tool that runs on demo data from a made-up engineering company with a private cloud in Madrid and Guadalajara.

In the demo, with the problems placed on purpose, the Madrid production cluster crosses its N+1 limit in January once the approved projects are counted. The reclaim list moves that date to March, enough to order the hosts in November. The demo has two vSphere production clusters, a Nutanix AHV cluster, a management cluster, 23 hosts and 458 VMs.

## Capacity measured as a date, not a percentage

For each cluster, the review calculates the CPU and RAM left when the largest host fails, the vCPU:pCPU ratio against the policy and hosts in maintenance. The runway takes the latest p95, the level usage stays under 95% of the time, adds a 12-month linear trend and the approved projects at their go-live month, and takes away the reclaim list. The result is the month each cluster crosses its limit, the month to order by and the hosts to add.

## Powered-off VMs and old snapshots that move the date

The reclaim list covers VMs powered off for 30 or 90 days, idle or oversized VMs, old snapshots and VMs without an owner, with the RAM and storage each gives back. It only counts when it moves the date. The review also flags datastores low on free space, cluster outages against the availability target and hosts out of vendor support. The output is a web report with a runway chart per cluster, a decisions table for the meeting and CSV files.

## How to use it with real data

A read-only PowerShell exporter reads vCenter through PowerCLI and Nutanix Prism Central through its REST API. It runs on Python with the standard library only, with 15 tests and a runbook. The suggested start is the last 12 months of data and keeping each month's output so the next review compares the forecast with what happened.

## Where it comes from

The tool comes from running private cloud infrastructure on vCenter and vSphere, VMware VCF with vSAN and NSX-T, Nutanix, OpenShift and HPE GreenLake, on Dell, HP and Supermicro servers with SAN, NAS and NetApp storage, and from formal capacity and availability management. The lesson behind it is that the capacity meeting should end with dates and owners, not percentages.""",
 es="""
Un clúster al 74% de su RAM parece sano en el panel, pero sin el host que HA, la función de alta disponibilidad, guarda de reserva está al 85% de lo que queda. Crece medio punto al mes y hay dos proyectos aprobados que llegan en enero y en marzo, así que cruza su límite N+1, el nivel en el que aún puede perder un host, en enero. Pedir, recibir y añadir hosts nuevos lleva cuatro meses, de modo que la decisión había que tomarla en septiembre. Ese es el razonamiento de la revisión mensual de capacidad que acompaña a este post, una herramienta de código abierto que se ejecuta con datos de ejemplo de una empresa de ingeniería inventada con una nube privada en Madrid y Guadalajara.

En la demo, con los problemas puestos a propósito, el clúster de producción de Madrid cruza su límite N+1 en enero al contar los proyectos aprobados. La lista de recuperación mueve esa fecha a marzo, lo justo para pedir los hosts en noviembre. La demo tiene dos clústeres vSphere de producción, un clúster Nutanix AHV, un clúster de gestión, 23 hosts y 458 máquinas virtuales.

## La capacidad medida como una fecha, no como un porcentaje

Para cada clúster, la revisión calcula la CPU y la RAM que quedan si cae el host más grande, el ratio vCPU:pCPU frente a la política y los hosts en mantenimiento. La autonomía parte del último p95, el nivel por debajo del cual está el uso el 95% del tiempo, le suma una tendencia lineal de 12 meses y los proyectos aprobados en su mes de puesta en marcha, y resta la lista de recuperación. El resultado es el mes en que cada clúster cruza su límite, el mes límite para pedir y los hosts a añadir.

## Máquinas apagadas y snapshots antiguos que mueven la fecha

La lista de recuperación incluye máquinas apagadas desde hace 30 o 90 días, máquinas ociosas o sobredimensionadas, snapshots antiguos y máquinas sin responsable, con la RAM y el almacenamiento que devuelve cada una. Solo cuenta si mueve la fecha. La revisión también señala datastores con poco espacio libre, caídas de clúster frente al objetivo de disponibilidad y hosts sin soporte del fabricante. El resultado es un informe web con una gráfica de autonomía por clúster, una tabla de decisiones para la reunión y ficheros CSV.

## Cómo usarlo con datos reales

Un exportador de solo lectura en PowerShell lee vCenter con PowerCLI y Nutanix Prism Central con su API REST. Funciona con Python y solo la librería estándar, con 15 tests y un runbook. Lo propuesto es empezar con los últimos 12 meses de datos y guardar la salida de cada mes para que la siguiente revisión compare la previsión con lo que pasó.

## De dónde sale

La herramienta nace de gestionar infraestructura de nube privada con vCenter y vSphere, VMware VCF con vSAN y NSX-T, Nutanix, OpenShift y HPE GreenLake, sobre servidores Dell, HP y Supermicro con almacenamiento SAN, NAS y NetApp, y de la gestión formal de capacidad y disponibilidad. La lección que hay detrás es que la reunión de capacidad tiene que acabar con fechas y responsables, no con porcentajes."""),
dict(n="36", repo="36-major-incident-command-kit", date="2026-10-28", cat="tools",
 title_en="Users reported an outage 40 minutes before monitoring did, the kind of gap a major incident kit measures",
 title_es="Los usuarios avisaron 40 minutos antes que la monitorización: el hueco que mide un kit de incidentes mayores",
 seo_title_en="Major incident review kit: MTTA, MTTR, PIR · Iñigo González",
 seo_title_es="Kit de incidentes graves: MTTA, MTTR y revisión · Iñigo González",
 seo_desc="For every P1 and P2 of the quarter: the first alert against the first user report, time to acknowledge, mitigate and resolve against target, who ran it, the gaps in stakeholder updates, the change the night before, the review, the root cause and the overdue actions, with a timeline and a draft post-incident review per incident.",
 seo_desc_es="Para cada P1 y P2 del trimestre: la primera alerta frente al primer aviso de los usuarios, el tiempo de respuesta, mitigación y resolución frente al objetivo…",
 dek_en="The kit, published with fictional data from a bank's IT operations team over one quarter, measures each P1 and P2 from the first signal to resolution, checks updates and recent changes, and drafts a post-incident review with a timeline per incident.",
 dek_es="El kit, publicado con datos ficticios del equipo de operaciones IT de un banco durante un trimestre, mide cada P1 y P2 desde la primera señal hasta la resolución, revisa las comunicaciones y los cambios previos, y redacta un borrador de revisión post-incidente con su línea de tiempo.",
 en="""
In the example the post starts from, the service desk had dozens of calls about logins before anyone in IT knew, and no alert fired until well after detection. An alert on the payments queue fired at ten past two and nobody acted until three. Those are the gaps the major incident kit published with this post is built to measure. It is an open-source tool that runs on demo data from the IT operations team of a made-up bank over one quarter: 54 incidents, six of them major, on card payments, online banking, trader voice, the mobile API, the payments hub and market data, with the problems placed on purpose.

The post-incident review is usually written a week later, from memory, by the person busiest on the bridge, and by then the timeline is a guess. The kit rebuilds it from the ITSM tool, the monitoring consoles, the bridge chat and the sent folder. It compares the first alert on the service or CI, the configuration item affected, with the first user report and the ticket, and marks blind spots and alerts nobody acted on.

## An hour and a half without an update for the trading desk

In the same example, the trading desk went an hour and a half without an update and never got the resolution notice. The kit checks for an update every N minutes as the policy says, and flags a late first update, the gaps and a missing resolution notice. It also measures time to acknowledge, mitigate and resolve against each priority's targets.

## The change the night before, missing from the ticket

The change the night before was the cause, and the ticket does not say so. The kit lists changes on the service in the 72 hours before the impact, late reviews, the root cause in the problem record, overdue actions and incidents back on the same CI within 30 days. The action that would have caught the login outage is a month overdue.

The output is a web report with a timeline per incident, a draft review per major incident with the parts only people can write clearly marked, and CSV files with MTTD, MTTA, MTTM and MTTR, the mean times to detect, acknowledge, mitigate and resolve. A `start` command prints the role card and the first-fifteen-minutes checklist.

## How to use it with real data

A read-only PowerShell exporter reads ServiceNow and Jira Service Management. It runs on Python with the standard library only, with 15 tests and a runbook. The suggested start is last quarter's real exports, tuning the targets with the major incident managers.

## Where it comes from

The tool comes from leading the technical response in major incidents and the post-mortems that followed, and from owning the incident, change and problem processes. One was the outage of a voice line used by a trading desk at a financial services firm: the fix was technical, but what the desk remembered was how often they heard from us. An update with nothing new is still an update.""",
 es="""
En el ejemplo del que parte el post, el service desk había recibido decenas de llamadas por el login antes de que nadie en IT lo supiera, y ninguna alerta saltó hasta mucho después de la detección. Una alerta de la cola de pagos saltó a las dos y diez y nadie actuó hasta las tres. Esos son los huecos que mide el kit de incidentes mayores que acompaña a este post, una herramienta de código abierto que se ejecuta con datos de ejemplo del equipo de operaciones IT de un banco inventado durante un trimestre: 54 incidentes, seis de ellos mayores, en pagos con tarjeta, banca online, voz de trading, la API móvil, el hub de pagos y datos de mercado, con los problemas puestos a propósito.

La revisión post-incidente se suele escribir una semana después, de memoria, por quien más trabajo tuvo en el puente, y para entonces la línea de tiempo es una suposición. El kit la reconstruye a partir de la herramienta ITSM, las consolas de monitorización, el chat del puente y la bandeja de enviados. Compara la primera alerta sobre el servicio o el CI, el elemento de configuración afectado, con el primer aviso de los usuarios y el ticket, y marca los puntos ciegos y las alertas que nadie atendió.

## Hora y media sin noticias para la mesa de trading

En el mismo ejemplo, la mesa de trading pasó hora y media sin una actualización y nunca recibió el aviso de resolución. El kit comprueba que haya una comunicación cada N minutos según la política, y señala una primera comunicación tardía, los huecos y el aviso de resolución que falta. También mide el tiempo hasta la asignación, la mitigación y la resolución frente a los objetivos de cada prioridad.

## El cambio de la noche anterior, ausente del ticket

El cambio de la noche anterior fue la causa, y el ticket no lo dice. El kit lista los cambios en el servicio en las 72 horas previas al impacto, las revisiones tardías, la causa raíz en el registro de problema, las acciones vencidas y los incidentes que vuelven en el mismo CI en 30 días. La acción que habría detectado la caída del login lleva un mes vencida.

El resultado es un informe web con una línea de tiempo por incidente, un borrador de revisión por cada incidente mayor con las partes que solo pueden escribir las personas bien marcadas, y ficheros CSV con MTTD, MTTA, MTTM y MTTR, los tiempos medios de detección, asignación, mitigación y resolución. Un comando `start` imprime la tarjeta de roles y el checklist de los primeros quince minutos.

## Cómo usarlo con datos reales

Un exportador de solo lectura en PowerShell lee ServiceNow y Jira Service Management. Funciona con Python y solo la librería estándar, con 15 tests y un runbook. Lo propuesto es empezar con las exportaciones reales del último trimestre y ajustar los objetivos con los responsables de incidentes mayores.

## De dónde sale

La herramienta nace de liderar la respuesta técnica en incidentes mayores y los post-mortems que vinieron después, y de ser responsable de los procesos de incidencias, cambios y problemas. Uno de ellos fue la caída de una línea de voz que usaba una mesa de trading en una empresa de servicios financieros: la solución fue técnica, pero lo que la mesa recordaba era cada cuánto tenía noticias nuestras. Una actualización sin novedades sigue siendo una actualización."""),
dict(n="37", repo="37-iam-access-review", date="2026-10-29", updated="2026-11-20", cat="tools",
 title_en="An administrator who left three weeks ago is still in Domain Admins and a trader signed in after his last day",
 title_es="Un administrador que se fue hace tres semanas sigue en Domain Admins y un trader entró después de su último día",
 seo_title_en="IAM access review: joiners, movers, leavers · Iñigo González",
 seo_title_es="Revisión de accesos IAM: altas, cambios y bajas · Iñigo González",
 seo_desc="Monthly IAM review from HR, AD and Entra ID exports: leavers still enabled, movers keeping access, orphan accounts, standing admin roles and recertification.",
 seo_desc_es="A partir de la plantilla de RR. HH. y de las exportaciones de Active Directory, Entra ID, la bóveda PAM y la recertificación: bajas todavía habilitadas…",
 dek_en="The monthly access review, published with fictional data from a clearing house of 600 people, joins the HR roster with the Active Directory, Entra ID, PAM vault and recertification exports to find leavers still enabled, movers who kept their access and approvals nobody really made.",
 dek_es="La revisión mensual de accesos, publicada con datos ficticios de una cámara de compensación de 600 personas, cruza la plantilla de RR. HH. con Active Directory, Entra ID, la bóveda PAM y la recertificación para encontrar bajas habilitadas, cambios de puesto con acceso antiguo y aprobaciones que nadie revisó.",
 en="""
A systems administrator who left three weeks ago still has his admin account enabled and in Domain Admins, the group with full control of the Windows domain. That is what the monthly access review published with this post finds. It is an open-source tool that runs on demo data from a made-up clearing house of 600 people, reviewed over one month, with the problems placed on purpose.

The account survives because nobody joins the sources. HR knows who left and who moved, the directories know who can still sign in, the vault knows which passwords were rotated and the recertification campaign knows who approved what. The tool joins those exports per person and per account, every month.

## A trader signed in four days after his last day

The same review finds a trader who signed in four days after leaving, and lists every account still enabled past the end date and its grace period. It also follows movers: someone who moved from trading to finance in August kept the trading platform, and the platform owner approved it in the campaign.

## A permanent Global Administrator and a password unchanged for 200 days

In privileged access, a Global Administrator role was assigned permanently, outside PIM, the Entra ID feature that grants admin roles only when they are needed. A service account password kept in the vault has not changed in 200 days, and a batch account belongs to someone who left and is still used interactively, by a person signing in rather than by a process. The review also checks members of Tier 0, the most sensitive admin level, beyond the approved list.

## One reviewer approved 140 items in three minutes

The recertification campaign, in which owners confirm or remove each access, has 446 items. One reviewer approved 140 of them in three minutes, and three revokes were never actioned. The tool measures how the campaign was done, not only whether it was finished: items not reviewed on time, revokes pending, rubber-stamping and entitlements overdue for review by sensitivity tier.

The outputs are a web report with a status per area and an overall status, a pack for the monthly IAM service review with 13 controls written the way an auditor tests them, and CSV files for leavers, movers, orphan accounts, privileged access, service accounts and the campaign.

## How to use it with real data

The repository includes a read-only PowerShell exporter for Active Directory and Microsoft Graph. The tool runs on Python with only the standard library and comes with 18 tests and a runbook. The planned next step is to run it on last month's real exports and tune the grace periods, the thresholds, the PIM roles and the approved Tier 0 list with the IAM and infrastructure leads. The company, people and accounts of the demo are fictional.

## Where it comes from

The tool comes from administering Active Directory and Entra ID with PIM and just-in-time access, managing privileged accounts in CyberArk and ManageEngine Password Manager Pro, owning the joiner process and answering audits under ISO 27001. Two lessons shaped it: a leaver's account is a finding even if nobody used it, and a move is the moment access goes wrong, not the next campaign.""",
 es="""
Un administrador de sistemas que se fue hace tres semanas sigue teniendo su cuenta de administración habilitada y en Domain Admins, el grupo con control total del dominio de Windows. Así lo detecta la revisión mensual de accesos que acompaña a este post, una herramienta de código abierto que se ejecuta con datos de ejemplo de una cámara de compensación inventada de 600 personas, revisada durante un mes y con los problemas puestos a propósito.

La cuenta sobrevive porque nadie junta las fuentes. RR. HH. sabe quién se fue y quién cambió de puesto, los directorios saben quién puede seguir entrando, la bóveda sabe qué contraseñas se rotaron y la campaña de recertificación sabe quién aprobó qué. La herramienta cruza esas exportaciones por persona y por cuenta, todos los meses.

## Un trader entró cuatro días después de su último día

La misma revisión encuentra a un trader que inició sesión cuatro días después de irse, y enumera cada cuenta todavía habilitada pasada la fecha de baja y su margen. También sigue los cambios de puesto: alguien que pasó de trading a finanzas en agosto conservó la plataforma de trading, y el responsable de la plataforma lo aprobó en la campaña.

## Un Global Administrator permanente y una contraseña sin cambiar en 200 días

En accesos privilegiados, un rol de Global Administrator se asignó de forma permanente, fuera de PIM, la función de Entra ID que concede los roles de administración solo cuando hacen falta. La contraseña de una cuenta de servicio guardada en la bóveda lleva 200 días sin cambiar, y una cuenta del batch es de alguien que se fue y se sigue usando de forma interactiva, con una persona iniciando sesión en lugar de un proceso. La revisión comprueba además los miembros de Tier 0, el nivel de administración más sensible, fuera de la lista aprobada.

## Un revisor aprobó 140 elementos en tres minutos

La campaña de recertificación, en la que los responsables confirman o retiran cada acceso, tiene 446 elementos. Un revisor aprobó 140 de ellos en tres minutos y tres revocaciones no se llegaron a ejecutar. La herramienta mide cómo se hizo la campaña, no solo si se terminó: elementos sin revisar a tiempo, revocaciones pendientes, aprobaciones en bloque y derechos con la revisión vencida según su nivel de sensibilidad.

El resultado es un informe web con un estado por área y un estado global, un informe para la revisión mensual del servicio de IAM con 13 controles redactados como los prueba un auditor, y ficheros CSV de bajas, cambios de puesto, cuentas huérfanas, accesos privilegiados, cuentas de servicio y la campaña.

## Cómo usarlo con datos reales

El repositorio incluye un exportador de solo lectura en PowerShell para Active Directory y Microsoft Graph. La herramienta funciona con Python y solo la librería estándar, e incluye 18 tests y un runbook. El siguiente paso previsto es ejecutarla con las exportaciones reales del último mes y ajustar los márgenes, los umbrales, los roles de PIM y la lista aprobada de Tier 0 con los responsables de IAM e infraestructura. La empresa, las personas y las cuentas de la demo son ficticias.

## De dónde sale

La herramienta nace de administrar Active Directory y Entra ID con PIM y acceso just-in-time, de gestionar cuentas privilegiadas en CyberArk y ManageEngine Password Manager Pro, de ser responsable del proceso de altas y de responder a auditorías bajo ISO 27001. Dos lecciones le dan forma: la cuenta de una baja es un hallazgo aunque nadie la haya usado, y el cambio de puesto es el momento en que el acceso se tuerce, no la siguiente campaña."""),
dict(n="37b", label="SD", repo="sysadmindesksbyigg", app="https://sysadmindesksbyigg.pages.dev/", date="2026-10-29", cat="sim",
 title_en="The fix that looks right and does not close the ticket: SysAdmin Desks, a free simulator to practise IT support",
 title_es="El arreglo que parece bueno y no cierra el ticket: SysAdmin Desks, un simulador gratuito para practicar soporte IT",
 seo_title_en="SysAdmin Desks: free IT support simulator · Iñigo González",
 seo_title_es="SysAdmin Desks: practica soporte IT gratis · Iñigo González",
 seo_desc="Free IT support simulator in English and Spanish: 24 tickets with SLA, a console, Active Directory, a network room, RMA, labs and a work note that gets marked.",
 dek_en="A support desk in the browser: a ticket queue with SLA, the requester and the device, a console where the commands do something, a simulated Active Directory, a desktop to fix things on the user's machine, a network room with switch and firewall CLIs, shipments and RMA, 24 tickets from first line to second line, a tempting fix that does not solve the cause, and a work note that gets marked. Free, in English and Spanish.",
 dek_es="Una mesa de soporte en el navegador: cola de tickets con SLA, el solicitante y su equipo, una consola donde los comandos hacen algo, un Active Directory simulado, un escritorio para arreglar en la máquina del usuario, una sala de red con la CLI de switches y cortafuegos, envíos y RMA, 24 tickets de primer y segundo nivel, un arreglo tentador que no resuelve la causa y una nota de trabajo que se corrige. Gratis, en español e inglés.",
 en="""
## The problem
Most people learn support on the job, with real users waiting. Labs teach the commands, but not the ticket: reading what the user really says, finding the cause instead of the symptom, checking that it works before closing, and leaving a note the next engineer can use. The classic mistake is the fix that looks right. You unlock the account that locks every morning, the user is happy for an hour, and the ticket comes back because the old password is still saved on the phone. I wanted a place to practise that loop without a real company behind it.

## What I built
- A ticket queue with priority, SLA (20, 30 or 45 minutes) and status. Assigning a ticket starts the clock and opens the console.
- A ticket page with the requester and the device, cards that change as the scenario changes, and actions from the page that do the same as the command, traps included.
- 24 tickets across Active Directory, DNS, Windows, printers, Exchange Online, Intune and BitLocker, VPN, Microsoft 365 licences, Azure AD Connect, Veeam, MECM, Red Hat, Citrix, Conditional Access, SAML single sign-on, Linux joined to AD, SQL Server, Cisco, HP and FortiGate networking, warranty RMAs and leavers' equipment. Each one has a root cause, a tempting fix that does not close it and a check to prove it works.
- Closing a ticket asks for a resolution code and a work note. The note is marked on cause, change, verification and follow-up, and the result is Resolved, Resolved with remarks or Not resolved, with what is missing.
- A simulated Active Directory with OUs, users, groups and computers, where every button runs a visible PowerShell command; a desktop for the tickets that are fixed on the user's machine, with an event viewer; and an inventory of servers and printers linked to the open tickets.
- A knowledge base built from your own approved notes, downloadable as Markdown, progress with a streak, a weekly goal and badges, and an internal mailbox with real requests and phishing to tell apart from them.
- Ticket states (pending user, pending vendor) with the SLA paused, scripted questions to the requester where some clues only come out by asking, and a note to the user that is marked apart from the work note.
- A network room with Cisco, Aruba and FortiGate devices, their health and a CLI on each one, and shipments and RMA linked to tickets.
- A library per area, five labs to practise without the clock, and a profile with progress by area and a career path from first-line support to infrastructure.
- A "Practise it" box in the guides on this website, which opens the matching ticket in the right language.

## How it is built
A static site with plain JavaScript and a small database for accounts and results. Every ticket has automated tests, so the tempting fix can never close it. Everything is fictional: a made-up company, no real systems. It is practice, not work experience.

## What I learned
From working tickets and teaching others to work them: the work note is part of the fix, a ticket is not closed until the user confirms it works, and the fix that looks right is the most common way to reopen one.

## Next steps
- A fuller internal mailbox: folders, replying to the requester and writing new messages.
- Levels by points, weekly goals with a reward and badges by area in the profile, and a full shift of four tickets at the end of each lab.
- Keep the network room, a ticket's shipments and the labs as they were after reloading the page.
""",
 es="""
## El problema
Casi todo el mundo aprende soporte trabajando, con usuarios reales esperando. Los laboratorios enseñan los comandos, pero no el ticket: leer lo que el usuario dice de verdad, encontrar la causa y no el síntoma, comprobar que funciona antes de cerrar y dejar una nota que le sirva al siguiente técnico. El error clásico es el arreglo que parece bueno. Desbloqueas la cuenta que se bloquea cada mañana, el usuario está contento una hora y el ticket vuelve, porque la contraseña antigua sigue guardada en el móvil. Quería un sitio para practicar ese ciclo sin una empresa real detrás.

## Qué he hecho
- Una cola de tickets con prioridad, SLA (20, 30 o 45 minutos) y estado. Al asignarte un ticket empieza a correr el reloj y se abre la consola.
- Una ficha del ticket con el solicitante y su equipo, tarjetas que cambian según avanza el caso y acciones desde la ficha que hacen lo mismo que el comando, trampas incluidas.
- 24 tickets de Active Directory, DNS, Windows, impresoras, Exchange Online, Intune y BitLocker, VPN, licencias de Microsoft 365, Azure AD Connect, Veeam, MECM, Red Hat, Citrix, acceso condicional, inicio de sesión único con SAML, Linux unido a AD, SQL Server, redes Cisco, HP y FortiGate, RMA en garantía y equipos de bajas. Cada uno tiene una causa raíz, un arreglo tentador que no lo cierra y una comprobación para demostrar que funciona.
- Para cerrar un ticket hay que elegir un código de resolución y escribir una nota de trabajo. La nota se corrige por causa, cambio, verificación y seguimiento, y el resultado es Resuelto, Resuelto con observaciones o No resuelto, con lo que falta.
- Un Active Directory simulado con OU, usuarios, grupos y equipos, donde cada botón ejecuta un comando de PowerShell visible; un escritorio para los tickets que se arreglan en la máquina del usuario, con visor de eventos; y un inventario de servidores e impresoras ligado a los tickets abiertos.
- Una base de conocimiento que se crea con tus propias notas aprobadas y se descarga en Markdown, progreso con racha, objetivo semanal e insignias, y un buzón interno con peticiones reales y phishing que hay que saber distinguir.
- Estados del ticket (pendiente del usuario, pendiente del proveedor) con el SLA en pausa, preguntas guionizadas al solicitante donde algunas pistas solo salen preguntando, y una nota al usuario que se corrige aparte de la nota de trabajo.
- Una sala de red con equipos Cisco, Aruba y FortiGate, su estado de salud y una CLI en cada uno, y envíos y RMA ligados a los tickets.
- Una biblioteca por área, cinco laboratorios para practicar sin reloj y un perfil con el progreso por área y un itinerario desde el soporte de primera línea hasta infraestructura.
- Un bloque «Practícalo» en las guías de esta web, que abre el ticket correspondiente en el idioma de la guía.

## Cómo está hecho
Un sitio estático con JavaScript sin frameworks y una pequeña base de datos para las cuentas y los resultados. Cada ticket tiene tests automáticos, para que el arreglo tentador nunca pueda cerrarlo. Todo es ficticio: una empresa inventada y ningún sistema real. Es práctica, no experiencia laboral.

## Qué aprendí
De trabajar tickets y enseñar a otros a trabajarlos: la nota de trabajo es parte del arreglo, un ticket no está cerrado hasta que el usuario confirma que funciona, y el arreglo que parece bueno es la forma más habitual de reabrirlo.

## Siguientes pasos
- Un buzón interno más completo: carpetas, responder al solicitante y redactar mensajes.
- Niveles por puntos, objetivos semanales con recompensa e insignias por área en el perfil, y un turno completo de cuatro tickets al final de cada laboratorio.
- Que la sala de red, los envíos de un ticket y los laboratorios se conserven al recargar la página.
"""),
dict(n="38", repo="38-it-asset-lifecycle-planner", date="2026-10-30", updated="2026-11-19", cat="tools",
 title_en="An office inventory finds nine laptops nobody registered and half the budget due in one quarter",
 title_es="Un inventario de oficina encuentra nueve portátiles sin registrar y medio presupuesto en un solo trimestre",
 seo_title_en="IT asset inventory and refresh forecast · Iñigo González",
 seo_title_es="Inventario de hardware y plan de renovación · Iñigo González",
 seo_desc="Monthly IT asset review from Device42, Intune, Jamf and purchases: one inventory by serial, leavers' devices, stock and a refresh forecast by quarter.",
 seo_desc_es="A partir de la exportación de Device42 de las salas de comunicaciones, Intune y Jamf Pro, las compras al fabricante, el registro de la oficina, RR. HH.…",
 dek_en="The monthly asset review, published with fictional data from a broker with three offices, joins Device42, Intune, Jamf Pro, the purchases, the office register, HR and the stock by serial number to find unregistered devices, leavers' laptops and the replacements due each quarter.",
 dek_es="La revisión mensual de equipos, publicada con datos ficticios de un bróker con tres oficinas, cruza por número de serie Device42, Intune, Jamf Pro, las compras, el registro de la oficina, RR. HH. y el almacén para encontrar equipos sin registrar, portátiles de bajas y las renovaciones de cada trimestre.",
 en="""
Nine laptops that appear in Intune have no record in the office inventory, because they were bought outside the usual channel, and the laptops of a large refresh fall due in the same quarter as the trading floor desktops, half the budget at once. That is what the monthly IT asset review published with this post finds. It is an open-source tool that runs on demo data from a made-up broker with offices in Madrid, Paris and Amsterdam and two comms rooms, with the problems placed on purpose.

The gaps exist because the inventory is split by who looks after it. The comms rooms are in Device42, the laptops and phones in Intune and Jamf, the device management tools that control them remotely, the monitors and docks in a spreadsheet and the warranties in the vendor's portal. Each list looks complete on its own. The tool joins them by serial number, the only key every system shares, into one inventory.

## A leaver's laptop still checking in weeks after the last day

Put together, the lists show a laptop that has not synced for months, and a leaver's laptop still checking in weeks after the last day. The review flags devices not seen for 30 days, duplicate or mismatched serials, items without owner or site, and devices assigned to leavers and not returned after 14 days. It also checks the stock of each site against a minimum.

## Access switches past end of support and a core switch warranty ending in six weeks

In the comms rooms, access switches are past end of support from the manufacturer and the core switch's warranty ends in six weeks. The review lists devices out of support or warranty, warranties ending in the next 90 days, devices without rack position or owner, and firmware not recorded.

Every item gets one state, in stock, deployed, in repair, to be retired or retired, and one replacement date from the refresh policy. From those dates the tool builds the forecast for the next four quarters by category and site, with units and cost, and keeps the overdue backlog apart.

## How to use it with real data

The repository includes a read-only PowerShell exporter for Device42, Intune through Microsoft Graph, and Jamf Pro. It runs on Python with only the standard library and produces a web report with a status per area, a pack for the monthly review with the forecast ready for the budget, and CSV files for every area. The demo has 51 devices in Device42, about 300 in Intune and Jamf, 740 purchase lines, 457 register lines and 198 people, all fictional. The next step planned is to write user devices back to Device42 so it becomes the single inventory.

## Where it comes from

The tool comes from running an office IT site with Device42 for the comms rooms and a PowerShell operations console for asset control, managing macOS, iOS, Android and Windows with Intune and Jamf Pro, working with Dell on hardware and renewals, and preparing the annual IT budget of a multi-site company. The lesson behind it: a budget built from purchase dates shows the waves before they arrive.""",
 es="""
Nueve portátiles que aparecen en Intune no tienen registro en el inventario de la oficina, porque se compraron fuera del canal habitual, y los portátiles de una renovación grande vencen en el mismo trimestre que los equipos de sobremesa de la sala de trading, medio presupuesto de golpe. Así lo detecta la revisión mensual de equipos que acompaña a este post, una herramienta de código abierto que se ejecuta con datos de ejemplo de un bróker inventado con oficinas en Madrid, París y Ámsterdam y dos salas de comunicaciones, con los problemas puestos a propósito.

Los huecos existen porque el inventario está repartido según quién lo cuida. Las salas de comunicaciones están en Device42, los portátiles y los móviles en Intune y Jamf, las herramientas que los gestionan en remoto, los monitores y las bases en una hoja de cálculo y las garantías en el portal del fabricante. Cada lista parece completa por separado. La herramienta las une por número de serie, la única clave que comparten todos los sistemas, en un solo inventario.

## El portátil de una baja sigue conectándose semanas después de su último día

Juntas, las listas enseñan un portátil que no sincroniza desde hace meses y el portátil de una baja que sigue conectándose semanas después de su último día. La revisión señala los equipos que no se ven desde hace 30 días, los números de serie duplicados o que no cuadran, los equipos sin responsable o sin sede y los asignados a bajas y no devueltos a los 14 días. También compara el almacén de cada sede con un mínimo.

## Switches sin soporte y la garantía del switch de núcleo a seis semanas de vencer

En las salas de comunicaciones, los switches de acceso ya no tienen soporte del fabricante y la garantía del switch de núcleo vence en seis semanas. La revisión lista los equipos sin soporte o fuera de garantía, las garantías que vencen en los próximos 90 días, los equipos sin posición en el rack o sin responsable y el firmware sin registrar.

Cada equipo recibe un estado, en almacén, desplegado, en reparación, para retirar o retirado, y una fecha de renovación según la política. Con esas fechas la herramienta construye la previsión de los cuatro próximos trimestres por categoría y sede, con unidades y coste, y deja aparte lo atrasado.

## Cómo usarlo con datos reales

El repositorio incluye un exportador de solo lectura en PowerShell para Device42, Intune a través de Microsoft Graph y Jamf Pro. Funciona con Python y solo la librería estándar, y genera un informe web con un estado por área, un informe para la revisión mensual con la previsión lista para el presupuesto y ficheros CSV de cada área. La demo tiene 51 equipos en Device42, unos 300 en Intune y Jamf, 740 líneas de compra, 457 del registro y 198 personas, todos ficticios. El siguiente paso previsto es volcar los equipos de usuario en Device42 para que sea el inventario único.

## De dónde sale

La herramienta nace de llevar la IT de una sede con Device42 para las salas de comunicaciones y una consola de operaciones en PowerShell para el control de activos, de gestionar macOS, iOS, Android y Windows con Intune y Jamf Pro, de trabajar con Dell en el hardware y las renovaciones y de preparar el presupuesto anual de IT de una empresa con varias sedes. La lección que hay detrás: un presupuesto hecho con las fechas de compra enseña las olas antes de que lleguen."""),
dict(n="39", repo="39-vulnerability-remediation-sla", date="2026-10-31", updated="2026-11-13", cat="tools",
 title_en="A VPN back on old firmware with a known exploit and thirty servers still vulnerable while they wait for a reboot",
 title_es="Una VPN con firmware antiguo y un exploit conocido, y treinta servidores vulnerables a la espera de un reinicio",
 seo_title_en="Vulnerability remediation SLA review · Iñigo González",
 seo_title_es="Revisión del SLA de vulnerabilidades · Iñigo González",
 seo_desc="Weekly and monthly vulnerability SLA review from Qualys, CISA KEV, EPSS, the asset register and Tanium or Intune: what is late, why it is stuck, what to fix.",
 seo_desc_es="A partir de las detecciones de Qualys, el catálogo KEV de CISA, EPSS, el inventario de activos, el estado de parcheo y el registro de excepciones: cada…",
 dek_en="The vulnerability review, published with fictional data from a broker with about 400 servers and 1,200 endpoints, checks every open Qualys detection against its deadline and cross-checks CISA KEV, EPSS, the asset register, the patch status and the exceptions to show what is late and why.",
 dek_es="La revisión de vulnerabilidades, publicada con datos ficticios de un bróker con unos 400 servidores y 1.200 equipos, mide cada detección abierta de Qualys frente a su plazo y la cruza con el catálogo KEV de CISA, EPSS, el inventario, el parcheo y las excepciones para mostrar qué va tarde y por qué.",
 en="""
A VPN appliance came back from a warranty swap on old firmware with a vulnerability that has been exploited for two years, and thirty servers that installed their patch a week ago are still vulnerable because nobody agreed the reboot. That is what the vulnerability remediation review published with this post finds. It is an open-source tool that runs on demo data from a made-up broker with about 400 servers and 1,200 Windows 11 endpoints owned by six teams, with the problems placed on purpose.

The scanner says how many vulnerabilities there are, but not whether the remediation deadlines promised by severity are being kept. Those deadlines are usually tracked in a spreadsheet updated by hand, and the totals hide the reasons. The tool gives every open Qualys detection its deadline: 15, 30, 90 or 180 days by severity, and 7 days if it is in the CISA KEV catalog of vulnerabilities known to be exploited, has a high EPSS score, an estimate of how likely it is to be exploited, or is critical on an internet-facing host.

## Trading desktops vulnerable again after an old image

Each detection is then marked on time, due in 7 days, overdue, or overdue by more than twice the deadline. The review explains why fixes do not close. Trading desktops are vulnerable again after being rebuilt from an old golden image, the master copy used to install them. Servers on an operating system that can no longer be patched are covered by an exception that expired a month ago.

The review also checks coverage, because the clock starts when the scanner finds the vulnerability: hosts Qualys does not scan or has not scanned for two weeks, hosts nobody owns and patch agents failing.

## One browser update is 40% of the critical and high findings on laptops

One browser update, held back by a pinned version, accounts for 40% of all critical and high findings on the laptops. The tool ranks the ten updates or packages that remove most risk. By team, one closes half of its fixes on time while the rest are above 90%.

The trend shows the share closed inside the deadline in each of the last three months and the mean time to remediate by severity.

## How to use it with real data

The repository includes a read-only PowerShell exporter for the Qualys API, the CISA KEV feed, the EPSS API and Intune. It runs on Python with only the standard library and produces a web report with a status per area, a weekly critical list, a monthly pack and CSV files for every area. The demo has almost 7,000 Qualys detections, the asset register, patch status from Tanium and Intune and seven exceptions, all fictional, plus 15 tests and a runbook.

## Where it comes from

The tool comes from using Qualys and Tanium for vulnerability and patch management at an office IT site, Microsoft Defender, and Intune and MECM in co-management, including the Windows 11 migration of an office with a trading floor; from cybersecurity risk management and remediation tracking; from ISO 27001, NIS2 and NIST CSF and their audits; and from the CAB as change process owner. The lesson behind it: installed is not fixed until the host reboots, and an exception is a time-boxed decision, not a way to turn the report green.""",
 es="""
Un equipo de VPN volvió de un cambio por garantía con un firmware antiguo y una vulnerabilidad explotada desde hace dos años, y treinta servidores que instalaron su parche hace una semana siguen siendo vulnerables porque nadie acordó el reinicio. Así lo detecta la revisión de corrección de vulnerabilidades que acompaña a este post, una herramienta de código abierto que se ejecuta con datos de ejemplo de un bróker inventado con unos 400 servidores y 1.200 equipos con Windows 11 repartidos entre seis equipos responsables, con los problemas puestos a propósito.

El escáner dice cuántas vulnerabilidades hay, pero no si se cumplen los plazos de corrección prometidos por severidad. Esos plazos se suelen seguir en una hoja de cálculo actualizada a mano, y las cifras esconden los motivos. La herramienta da a cada detección abierta de Qualys su plazo: 15, 30, 90 o 180 días según la severidad, y 7 días si está en el catálogo KEV de CISA de vulnerabilidades que se sabe que se explotan, tiene un EPSS alto, una estimación de la probabilidad de que se explote, o es crítica en un equipo expuesto a internet.

## Puestos de trading vulnerables otra vez por una imagen antigua

Después, cada detección queda en plazo, a punto de vencer en 7 días, vencida o vencida más del doble del plazo. La revisión explica por qué no se cierran las correcciones. Los equipos de la sala de trading vuelven a ser vulnerables tras reinstalarse desde una imagen maestra antigua, la copia base con la que se instalan. Unos servidores con un sistema operativo que ya no se puede parchear están cubiertos por una excepción que caducó hace un mes.

La revisión comprueba también la cobertura, porque el reloj empieza cuando el escáner encuentra la vulnerabilidad: equipos que Qualys no analiza o no analiza desde hace dos semanas, equipos sin responsable y agentes de parcheo que fallan.

## Una actualización del navegador es el 40 % de las vulnerabilidades críticas y altas de los portátiles

Una actualización del navegador, retenida por una versión fijada, supone el 40 % de todas las vulnerabilidades críticas y altas de los portátiles. La herramienta ordena las diez actualizaciones o paquetes que más riesgo eliminan. Por equipos, uno cierra la mitad de sus correcciones a tiempo mientras el resto supera el 90 %.

La tendencia muestra el porcentaje cerrado dentro del plazo en cada uno de los tres últimos meses y el tiempo medio de corrección por severidad.

## Cómo usarlo con datos reales

El repositorio incluye un exportador de solo lectura en PowerShell para la API de Qualys, el catálogo KEV de CISA, la API de EPSS e Intune. Funciona con Python y solo la librería estándar, y genera un informe web con un estado por área, una lista semanal de críticas, un informe mensual y ficheros CSV de cada área. La demo tiene casi 7.000 detecciones de Qualys, el inventario de activos, el estado de parcheo de Tanium e Intune y siete excepciones, todo ficticio, además de 15 tests y un runbook.

## De dónde sale

La herramienta nace de usar Qualys y Tanium para la gestión de vulnerabilidades y parches en una sede, Microsoft Defender, e Intune y MECM en cogestión, incluida la migración a Windows 11 de una oficina con sala de trading; de la gestión de riesgos de ciberseguridad y el seguimiento de la corrección; de ISO 27001, NIS2 y NIST CSF y sus auditorías; y del CAB como responsable del proceso de cambios. La lección que hay detrás: instalado no es corregido hasta que el equipo se reinicia, y una excepción es una decisión con fecha de caducidad, no una forma de poner el informe en verde."""),

dict(n="40", repo="40-change-calendar-risk-review", date="2026-11-02", updated="2026-11-19", cat="tools",
 title_en="Two teams booked changes on the trading platform's path the same night and a patch inside the month-end freeze",
 title_es="Dos equipos programan cambios en la ruta de la plataforma de trading la misma noche y un parche en el cierre de mes",
 seo_title_en="Change calendar and CAB risk review · Iñigo González",
 seo_title_es="Calendario de cambios y revisión del CAB · Iñigo González",
 seo_desc="Weekly CAB pack from ServiceNow changes, the service map, freezes and incidents: what is not ready, what collides, and how last month's changes went.",
 seo_desc_es="A partir de las peticiones de cambio, el mapa de servicios, el registro de congelaciones, los incidentes y las aprobaciones: las dos próximas semanas por día…",
 dek_en="The weekly change review, published with fictional data from a bank with a trading floor, cross-checks the change requests with the service map, the freezes, the incidents and the approvals to show what is not ready for the CAB, what collides and how last month's changes went.",
 dek_es="La revisión semanal de cambios, publicada con datos ficticios de un banco con sala de trading, cruza las peticiones de cambio con el mapa de servicios, las congelaciones, los incidentes y las aprobaciones para mostrar qué no está listo para el CAB, qué coincide y cómo fueron los cambios del mes pasado.",
 en="""
The data centre firewalls and the core switches are due to be upgraded the same night by two different teams, both in the path of the trading platform, and a database patch on that platform is booked inside the month-end close freeze. That is what the change calendar review published with this post finds. It is an open-source tool that runs on demo data from a made-up bank with a trading floor, reviewed on a Monday morning before the CAB, the change advisory board that approves changes, with the problems placed on purpose.

The change calendar in the ITSM tool is a list, and the CAB approves each change on its own merits. The list does not show how the changes relate to each other or to the rest of the month. The tool works out the impact of each change through the dependency map of 16 business services in three tiers, so a change on the core network collides with anything on the services that depend on it.

## A high-risk change with no backout plan, raised two days before its window

The readiness checks find a high-risk change raised two days before its window with no backout plan, the steps to undo it if it goes wrong. The review flags changes without a backout, test or implementation plan, with the risk not assessed or below what the impact and the tier of the service suggest, raised inside the lead time, not approved when they start before the CAB, without an owner or outside the maintenance window of their tier.

A firmware upgrade on the storage of critical services is booked as a standard change, the pre-approved kind meant for routine work, so it never reaches the CAB. One team raises more emergency changes every month for the same reasons, and the tool shows the emergency share by month, its reasons and emergencies never approved afterwards.

## A change closed as successful two hours before a P1 at the market open

The other half of the review looks back. One change was closed as successful two hours before a P1, a top-priority incident, at the market open, and no post-implementation review was booked. The tool measures last month's success rate and trend, unsuccessful changes, incidents linked to a change or opened on the same service within hours of one, overruns, unauthorised work, overdue reviews and the teams with a low success rate or rising emergencies.

## How to use it with real data

The repository includes a read-only PowerShell exporter for the ServiceNow Table API, covering changes, incidents, approvals and the service map. It runs on Python with only the standard library and produces a web report with a two-week calendar by day and service where collisions, freezes and gaps stand out, a CAB agenda with the monthly review, and CSV files for every area. The demo holds 263 change requests from nine teams, three months of history and the next two weeks, and a freeze register with the month-end close and an index rebalance, all fictional. It comes with 15 tests and a runbook.

## Where it comes from

The tool comes from being process owner for incidents, changes and problems, taking part in CABs and go-live reviews, release management, writing runbooks and training others, leading the technical response in major incidents, and working with ServiceNow, EasyVista, HaloITSM, Jira and Confluence. The lesson behind it: two changes on the same path the same night mean two backout plans for one symptom, and a change followed by a P1 is not a success, however it was closed.""",
 es="""
Los cortafuegos del centro de datos y los switches del núcleo se van a actualizar la misma noche por dos equipos distintos, ambos en el camino de la plataforma de trading, y un parche de base de datos de esa plataforma está programado dentro de la congelación del cierre de mes. Así lo detecta la revisión del calendario de cambios que acompaña a este post, una herramienta de código abierto que se ejecuta con datos de ejemplo de un banco inventado con sala de trading, revisado un lunes por la mañana antes del CAB, el comité que aprueba los cambios, con los problemas puestos a propósito.

El calendario de cambios de la herramienta de ITSM es una lista, y el CAB aprueba cada cambio por separado. La lista no enseña cómo se relacionan los cambios entre sí ni con el resto del mes. La herramienta calcula el impacto de cada cambio a través del mapa de dependencias de 16 servicios de negocio en tres niveles, así que un cambio en la red troncal coincide con cualquier otro en los servicios que dependen de ella.

## Un cambio de riesgo alto sin plan de marcha atrás, dado de alta dos días antes

Las comprobaciones de preparación encuentran un cambio de riesgo alto dado de alta dos días antes de su ventana y sin plan de marcha atrás, los pasos para deshacerlo si sale mal. La revisión señala los cambios sin plan de marcha atrás, de pruebas o de implementación, con el riesgo sin evaluar o por debajo de lo que indican el impacto y el nivel del servicio, dados de alta dentro del plazo mínimo, sin aprobar cuando empiezan antes del CAB, sin responsable o fuera de la ventana de mantenimiento de su nivel.

Una actualización de firmware del almacenamiento de servicios críticos está registrada como cambio estándar, el tipo preaprobado pensado para trabajos rutinarios, así que nunca llega al CAB. Un equipo abre cada mes más cambios de emergencia por los mismos motivos, y la herramienta muestra el porcentaje de emergencias por mes, sus motivos y las que nunca se aprobaron después.

## Un cambio cerrado con éxito dos horas antes de un P1 en la apertura del mercado

La otra mitad de la revisión mira hacia atrás. Un cambio se cerró con éxito dos horas antes de un P1, un incidente de máxima prioridad, en la apertura del mercado, y no tenía revisión posterior programada. La herramienta mide la tasa de éxito del mes pasado y su evolución, los cambios fallidos, los incidentes vinculados a un cambio o abiertos en el mismo servicio pocas horas después, los cambios que se pasaron de su ventana, los trabajos sin autorizar, las revisiones pendientes y los equipos con poca tasa de éxito o con emergencias en aumento.

## Cómo usarlo con datos reales

El repositorio incluye un exportador de solo lectura en PowerShell para la Table API de ServiceNow, con cambios, incidentes, aprobaciones y el mapa de servicios. Funciona con Python y solo la librería estándar, y genera un informe web con un calendario de dos semanas por día y servicio donde destacan las coincidencias, las congelaciones y los huecos, el orden del día del CAB con la revisión mensual y ficheros CSV de cada área. La demo tiene 263 peticiones de cambio de nueve equipos, tres meses de histórico y las dos próximas semanas, y un registro de congelaciones con el cierre de mes y un rebalanceo de índices, todo ficticio. Incluye 15 tests y un runbook.

## De dónde sale

La herramienta nace de ser responsable de los procesos de incidentes, cambios y problemas, de participar en CAB y en revisiones de puesta en producción, de la gestión de versiones, de escribir runbooks y formar a otros, de dirigir la respuesta técnica en incidentes mayores y de trabajar con ServiceNow, EasyVista, HaloITSM, Jira y Confluence. La lección que hay detrás: dos cambios en el mismo camino la misma noche suponen dos planes de marcha atrás para un solo síntoma, y un cambio seguido de un P1 no es un éxito, se cierre como se cierre."""),

dict(n="41", repo="41-windows-update-ring-tracker", date="2026-11-02", cat="tools",
 title_en="A paused and forgotten update ring left the trading floor two months behind on Windows updates",
 title_es="Un anillo de actualización pausado y olvidado dejó a la sala de trading dos meses por detrás en Windows Update",
 seo_title_en="Windows update rings: gates and go/no-go · Iñigo González",
 seo_title_es="Anillos de Windows Update y go/no-go · Iñigo González",
 seo_desc="Patch Tuesday through the Intune update rings: each ring against its deadline, the go/no-go gates, devices behind and why, failures by model and the trend.",
 seo_desc_es="A partir de los dispositivos y los anillos de actualización de Intune, los despliegues de Configuration Manager de los equipos en cogestión, los informes…",
 dek_en="The update ring review, published with fictional data from a firm with 1,500 Windows 11 devices, follows each month's update through the Intune and Configuration Manager rings against their deadlines and gates, and shows devices behind and why, failures by model and the trend.",
 dek_es="La revisión de anillos, publicada con datos ficticios de una empresa con 1.500 equipos con Windows 11, sigue la actualización de cada mes por los anillos de Intune y Configuration Manager frente a sus plazos y puertas, y muestra los equipos con retraso y por qué, los fallos por modelo y la tendencia.",
 en="""
The late update ring for the trading floor was paused after a bad update and nobody remembered it, so five weeks later it is two months behind and the pause expires with nobody having decided what happens next. That is what the Windows update rollout review published with this post finds. It is an open-source tool that runs on demo data from a made-up firm with a trading floor and 1,500 Windows 11 devices in four European cities, reviewed twenty days after the October Patch Tuesday, with the problems placed on purpose.

Update rings are groups of devices that receive the monthly update after a set delay, and they work as timers. The broad ring is offered the update ten days after Patch Tuesday whether the pilot went well or not, and in this demo it starts with the pilot still at 77%. A report that counts installs does not say whether the rollout is under control. The tool adds a gate between rings, built on the previous ring's share on the build, its failure rate, the days since it was offered, open P1 or P2 incidents about the update and known issues, and gives a go or no-go for the next promotion.

## Sixty trading desktops in the wrong ring and a pilot of IT engineers

Sixty trading desktops sit in the broad ring instead of the late one, and lose their headset audio at the market open. The pilot, meant to catch problems first, is nine IT engineers out of ten. The review checks whether the pilot misses the departments, models and sites of the broad ring, and flags rings off their target size and policies that drift from the ring standard.

## One laptop model fails the update on a third of its devices

One laptop model fails with the same error code on a third of its devices, a sign of one fix to make once rather than devices to repair one by one. Ninety devices have been waiting for a restart since before the deadline, and a whole office stops checking in on the same day because of the VPN. The review also lists devices in no ring or in two, on a Windows 11 version near its end of servicing, or held back by a safeguard hold.

Over time, the share of devices on the build two weeks after Patch Tuesday has fallen three months in a row. The tool tracks that share at day 7, 14 and 21 and the median days to install by ring.

## How to use it with real data

A device counts as up to date when its OS revision is the month's Patch Tuesday revision or later. Its ring comes from the groups or collections its policies are assigned to, with co-managed devices following Configuration Manager while the Windows Update workload has not moved to Intune. Each device is judged against its own deadline and grace, so one still inside its window is not counted as behind. The repository includes a read-only PowerShell exporter for Microsoft Graph, the Windows Update for Business reports in Log Analytics and Configuration Manager, and produces a web report with a timeline of the month and a pack for the patch meeting or the CAB with a decision line. It runs on Python with only the standard library and comes with 13 tests and a runbook. The demo uses the real builds, KB numbers and known issues from Windows release health; the firm and its devices are fictional. Since a ring promotion is a change, the review pairs with the change calendar published the same day.

## Where it comes from

The tool comes from leading the Windows 11 migration of an office with a trading floor, running Intune and MECM in co-management, years of automation with PowerShell and Microsoft Graph, and release management and the CAB as change process owner, supporting about 2,500 users across European offices. The lesson behind it: a deferral says when a ring can get the update, and only a gate says whether it should.""",
 es="""
El anillo tardío de la sala de trading se pausó tras una actualización problemática y nadie se acordó de él, así que cinco semanas después lleva dos meses de retraso y la pausa caduca sin que nadie haya decidido qué pasa después. Así lo detecta la revisión del despliegue de Windows Update que acompaña a este post, una herramienta de código abierto que se ejecuta con datos de ejemplo de una empresa inventada con sala de trading y 1.500 equipos con Windows 11 en cuatro ciudades europeas, revisada veinte días después del Patch Tuesday de octubre, con los problemas puestos a propósito.

Los anillos de actualización son grupos de equipos que reciben la actualización mensual con un retraso fijado, y funcionan como temporizadores. El anillo general recibe la actualización diez días después del Patch Tuesday haya ido bien el piloto o no, y en esta demo arranca con el piloto todavía al 77%. Un informe que cuenta instalaciones no dice si el despliegue está bajo control. La herramienta añade una puerta entre anillos, basada en el porcentaje del anillo anterior con la compilación, su tasa de fallos, los días desde que se le ofreció, los incidentes P1 o P2 abiertos por la actualización y los problemas conocidos, y da un go/no-go para la siguiente promoción.

## Sesenta puestos de trading en el anillo equivocado y un piloto de informáticos

Sesenta puestos de trading están en el anillo general en lugar del tardío, y se quedan sin audio en los cascos a la apertura del mercado. El piloto, que debería detectar los problemas primero, son nueve informáticos de cada diez. La revisión comprueba si al piloto le faltan los departamentos, modelos y sedes del anillo general, y señala los que no tienen el tamaño previsto y las directivas que se apartan del estándar.

## Un modelo de portátil falla la actualización en un tercio de sus equipos

Un modelo de portátil falla con el mismo código de error en un tercio de sus equipos, señal de un arreglo que se hace una vez y no de equipos que se reparan uno a uno. Noventa equipos llevan esperando un reinicio desde antes de la fecha límite, y una oficina entera deja de sincronizar el mismo día por la VPN. La revisión lista además los equipos sin anillo o en dos, en una versión de Windows 11 cerca del fin de servicio o retenidos por una safeguard hold.

En el tiempo, el porcentaje de equipos con la compilación al día dos semanas después del Patch Tuesday ha bajado tres meses seguidos. La herramienta sigue ese porcentaje al día 7, 14 y 21 y la mediana de días hasta instalar por anillo.

## Cómo usarlo con datos reales

Un equipo cuenta como actualizado cuando la revisión de su versión del sistema es la del Patch Tuesday del mes o posterior. Su anillo sale de los grupos o colecciones a los que están asignadas sus directivas, y los equipos en cogestión siguen a Configuration Manager mientras la carga de trabajo de Windows Update no haya pasado a Intune. Cada equipo se mide con su propia fecha límite y su gracia, así que uno que aún está en plazo no cuenta como retrasado. El repositorio incluye un exportador de solo lectura en PowerShell para Microsoft Graph, los informes de Windows Update for Business en Log Analytics y Configuration Manager, y genera un informe web con una línea temporal del mes y un informe para la reunión de parches o el CAB con una línea para la decisión. Funciona con Python y solo la librería estándar, e incluye 13 tests y un runbook. La demo usa las compilaciones, los KB y los problemas conocidos reales del estado de versiones de Windows; la empresa y sus equipos son ficticios. Como promocionar un anillo es un cambio, la revisión encaja con el calendario de cambios publicado el mismo día.

## De dónde sale

La herramienta nace de dirigir la migración a Windows 11 de una oficina con sala de trading, de gestionar Intune y MECM en cogestión, de años automatizando con PowerShell y Microsoft Graph, y de la gestión de versiones y el CAB como responsable del proceso de cambios, dando soporte a unos 2.500 usuarios en oficinas europeas. La lección que hay detrás: el aplazamiento dice cuándo puede recibir un anillo la actualización, y solo una puerta dice si debe."""),

dict(n="42", repo="42-retail-store-it-health", date="2026-11-03", cat="tools",
 title_en="A store failed over to 4G nine times in a week and nobody saw its backup SIM at 93% of its data cap",
 title_es="Una tienda saltó al 4G nueve veces en una semana y nadie vio que su SIM de respaldo iba por el 93% de sus datos",
 seo_title_en="Store IT health review for a retail chain · Iñigo González",
 seo_title_es="Revisión semanal del IT de cada tienda · Iñigo González",
 seo_desc="Weekly store IT review for a retail chain: lines and 4G backup, tunnels, devices, printers, tickets, openings and users, with a visit and ship list.",
 seo_desc_es="A partir de la lista de tiendas, la conectividad diaria de cada una, los equipos de Intune y Active Directory, el estado de las impresoras, los tickets…",
 dek_en="The weekly store review, published with fictional data from an eyewear chain with 122 stores, cross-checks connectivity, devices, printers, tickets, opening checklists and joiners and leavers to give each store a red, amber or green status and a list of visits, shipments and vendor calls.",
 dek_es="La revisión semanal de tiendas, publicada con datos ficticios de una cadena de ópticas con 122 tiendas, cruza la conectividad, los equipos, las impresoras, los tickets, las aperturas y las altas y bajas para dar a cada una un estado rojo, ámbar o verde y una lista de visitas, envíos y llamadas.",
 en="""
A shopping centre store failed over to its 4G backup router nine times in one week and kept selling, and nobody noticed that its backup SIM was at 93% of its data cap until the router was throttled on a Saturday afternoon. That is what the weekly store IT review published with this post finds. It is an open-source tool that runs on demo data from a made-up eyewear chain with 122 stores in Spain and Portugal, street stores, shopping centres and corners inside a department store, reviewed on a Tuesday morning with the problems placed on purpose.

A chain's central IT sees its stores through a monitoring console, a device list and a ticket queue, and none of the stores has anyone from IT inside. The tool ties every issue to a store and says what it needs: a visit from the field technician, a shipment, a vendor call or remote work. That way the list for each technician comes out of the checks instead of being written by hand, ranked by region.

## Fourteen untested backup routers and a region that loses its tunnel at eight

Fourteen backup routers have never been tested. Every store in one region loses its tunnel to head office, the permanent connection between the store and central systems, at around eight in the evening, and the service desk logs it as seventeen separate problems when it is one cause. A corner inside a department store opens in ten days and its line is still not installed, because the carrier cannot get past the department store's comms room.

The connectivity checks cover primary line availability over the week compared with the week before, time on backup, stores with no backup line, backup SIMs near their cap and failed AnyConnect VPN connections.

## A receipt printer model that jams in three stores

Three stores with the same receipt printer model log jam after jam, which makes it a vendor call rather than three repairs. One store raises four times the median number of tickets across the estate, nearly all about handhelds losing Wi-Fi in the stockroom. Two stores closed weeks ago with their laptops and card terminals still inside, and two people start tomorrow without an account.

The review also checks computers not checked in or on an unsupported Windows, printers offline or low on toner, terminals not reporting and UPS units that failed their self-test. Tickets cover the last thirty days, and a ticket on hold with a vendor does not count against the SLA. Stores in refurbishment are skipped until they reopen.

## How to use it with real data

The connectivity and printer data are exports of the monitoring tool, with printer status and toner read from standard SNMP printer objects. The repository includes a read-only PowerShell exporter for Microsoft Graph, Active Directory and Entra ID, and runs on Python with only the standard library. It produces a status per store with its reasons, a store grid by region, a visit and ship list by field technician, a pack for the weekly retail operations meeting with the trend against last week, and CSV files. It comes with 14 tests and a runbook. The chain and its stores are fictional. The tool is not the venue readiness check or the hotel pre-opening tracker published earlier: it covers a whole estate of stores, week after week.

## Where it comes from

The tool comes from supporting the boutiques and points of sale of luxury retail brands, about 200 pre-openings of brand corners inside department stores, Intune and Microsoft Graph, and owning the incident and change processes. At one of those openings the connectivity failed two hours before the doors opened, and I brought the corner back online with a temporary USB 4G router while checking the floor's comms room with the department store's technicians. The lesson: a store on its backup is one failure away from not selling, and an untested backup is only a hope.""",
 es="""
Una tienda de centro comercial saltó a su router 4G de respaldo nueve veces en una semana y siguió vendiendo, y nadie se dio cuenta de que su SIM de respaldo iba por el 93% de su límite de datos hasta que el router se quedó sin velocidad un sábado por la tarde. Así lo detecta la revisión semanal del IT de tiendas que acompaña a este post, una herramienta de código abierto que se ejecuta con datos de ejemplo de una cadena de ópticas inventada con 122 tiendas en España y Portugal, entre tiendas de calle, centros comerciales y córners dentro de unos grandes almacenes, revisada un martes por la mañana con los problemas puestos a propósito.

El IT central de una cadena ve sus tiendas a través de una consola de monitorización, un listado de equipos y una cola de tickets, y en ninguna de ellas hay nadie de informática. La herramienta asigna cada problema a una tienda y dice lo que necesita: una visita del técnico de campo, un envío, una llamada al proveedor o trabajo en remoto. Así la lista de cada técnico sale de las comprobaciones en lugar de escribirse a mano, ordenada por región.

## Catorce routers de respaldo sin probar y una región que pierde el túnel a las ocho

Catorce routers de respaldo no se han probado nunca. Todas las tiendas de una región pierden el túnel con la central, la conexión permanente entre la tienda y los sistemas centrales, hacia las ocho de la tarde, y el service desk lo registra como diecisiete problemas distintos cuando es una sola causa. Un córner dentro de unos grandes almacenes abre en diez días y su línea sigue sin instalar, porque el operador no puede pasar del cuarto de comunicaciones de los grandes almacenes.

Las comprobaciones de conectividad incluyen la disponibilidad de la línea principal en la semana frente a la anterior, el tiempo en respaldo, las tiendas sin línea de respaldo, las SIM cerca de su límite y las conexiones fallidas de la VPN AnyConnect.

## Un modelo de impresora de tickets que se atasca en tres tiendas

Tres tiendas con el mismo modelo de impresora de tickets acumulan atasco tras atasco, lo que lo convierte en una llamada al proveedor y no en tres reparaciones. Una tienda abre cuatro veces la mediana de tickets de la red, casi todos porque las PDA pierden el Wi-Fi en el almacén. Dos tiendas cerraron hace semanas con los portátiles y los datáfonos todavía dentro, y dos personas empiezan mañana sin cuenta.

La revisión comprueba también los PC sin sincronizar o con un Windows sin soporte, las impresoras desconectadas o con poco tóner, los datáfonos que no reportan y los SAI que han fallado su autotest. Los tickets cubren los últimos treinta días, y uno en espera del proveedor no cuenta para el SLA. Las tiendas en reforma no se revisan hasta que reabren.

## Cómo usarlo con datos reales

Los datos de conectividad e impresoras son exportaciones de la herramienta de monitorización, y el estado y el tóner de las impresoras salen de los objetos SNMP estándar de impresora. El repositorio incluye un exportador de solo lectura en PowerShell para Microsoft Graph, Active Directory y Entra ID, y funciona con Python y solo la librería estándar. Genera un estado por tienda con sus motivos, una cuadrícula de tiendas por región, una lista de visitas y envíos por técnico de campo, un informe para la reunión semanal de operaciones de tienda con la tendencia frente a la semana anterior y ficheros CSV. Incluye 14 tests y un runbook. La cadena y sus tiendas son ficticias. La herramienta no es la comprobación de preparación de un local ni el seguimiento de la preapertura de un hotel publicados antes: cubre toda una red de tiendas, semana tras semana.

## De dónde sale

La herramienta nace de dar soporte a las boutiques y puntos de venta de marcas de lujo, de unas 200 preaperturas de córners de marca dentro de grandes almacenes, de Intune y Microsoft Graph y de ser responsable de los procesos de incidencias y cambios. En una de esas aperturas la conectividad se cayó dos horas antes de abrir, y volví a dar servicio al córner con un router USB 4G provisional mientras revisaba el cuarto de comunicaciones de la planta con los técnicos de los grandes almacenes. La lección: una tienda en respaldo está a un fallo de no poder vender, y un respaldo sin probar es solo una esperanza."""),
dict(n="43", repo="43-azure-cost-rightsizing", date="2026-11-04", updated="2026-11-20", cat="tools",
 title_en="Azure review finds 11,101 euros a month of savings and a reservation at 55% that was set to renew itself",
 title_es="Una revisión de Azure halla 11.101 euros al mes de ahorro y una reserva al 55% que iba a renovarse sola",
 seo_title_en="Monthly Azure cost review and right-sizing · Iñigo González",
 seo_title_es="Revisión de costes de Azure y redimensionado · Iñigo González",
 seo_desc="Monthly Azure cost review from the FOCUS export: right-sizing, waste, reservations and savings plans, showback by cost centre, budgets and unit cost.",
 seo_desc_es="Revisión mensual de costes de Azure: redimensionado, desperdicio, reservas y planes de ahorro, showback por centro de coste, presupuestos y coste unitario.",
 dek_en="The monthly Azure cost review, published with fictional data from an insurance group with five subscriptions and 133 VMs, cross-checks the cost export, 30 days of VM metrics, disks, public IPs, commitments and budgets to decide what to resize, delete, schedule and commit, and who pays for each line.",
 dek_es="La revisión mensual de costes de Azure, publicada con datos ficticios de un grupo asegurador con cinco suscripciones y 133 VMs, cruza la exportación de costes, 30 días de métricas, discos, IP públicas, compromisos y presupuestos para decidir qué redimensionar, borrar, programar y comprometer, y quién paga cada línea.",
 en="""
A reservation for ten batch servers has been running at 55% since half of the batch moved elsewhere, it expires in six weeks and it is set to renew itself. It is one of the findings of a 94,403 euro month in which the review identifies 11,101 euros a month of savings. That is what the monthly Azure cost review published with this post finds. It is a tool that runs on demo data from a made-up insurance group with five subscriptions and 133 virtual machines, reviewed on 4 November for October, with round fictional prices and the problems placed on purpose.

A reservation is a commitment to pay for capacity in advance in exchange for a lower price, and the tool treats one under 80% of use as money paid for nothing. For every reservation and savings plan under its target it shows the unused cost of the month, and for the ones expiring in the next 90 days it asks for a decision: renew or exchange. When a commitment would renew itself at low use, the finding is critical.

## Three SQL Server machines that never pass 15% CPU

Three SQL Server VMs on E16s_v5 peak at 15% CPU and use a third of their memory, because they were sized for a migration two years ago. The tool looks for VMs whose CPU p95, the level the machine stays under 95% of the time, and peak memory over 30 days fit in one size down within the same family. A VM covered by a reservation is flagged, because resizing it saves nothing until the freed capacity is used or exchanged.

A reporting VM was shut down from inside Windows three weeks ago and is still billed as if it were running, because nobody deallocated it, that is, nobody released it in Azure. Fourteen development and test VMs run every night and every weekend. The disks and public IPs of a migration project that finished in August are still there, unattached and untagged, and an unattached disk is billed in full.

## Forty production VMs on pay-as-you-go and 11% of the bill with no owner

Forty production VMs run all month on pay-as-you-go while only a quarter of the VM spend is covered by a commitment. The review lists the steady pay-as-you-go VMs a commitment would cover, but only after the waste: buying first would lock in today's oversizing for years.

On showback, the practice of showing each area what it spends, 11% of the bill has no cost centre, so nobody is asked about it. One cost centre ends the month 14% over budget and is on course to do it again. The cost per active user of the digital channels goes up 15%, because the users fell and the cost did not.

## How each saving is worked out

Every saving is an estimate per month at the run rate of the last seven days, and the pack explains how it was calculated. Half the vCPUs in the same family is half the compute cost; an office-hours schedule is 60 of 168 hours; a commitment is an upper estimate to be checked against Azure Advisor before buying. Coverage is measured in hours, because a Windows or SQL Server VM covered by a reservation still has pay-as-you-go rows for its licence.

## How to use it with real data

The cost side is the FOCUS export, a standard cost format, as Azure Cost Management writes it: effective cost for the amortised spend, billed cost next to it, and the unused part of commitments from the rows marked as unused. The repository includes a read-only PowerShell exporter for the Az modules and the reservations and savings plans APIs, and runs on Python with only the standard library. It produces a report with a verdict for the month, a savings pack for the monthly FinOps review with a decision column for every resize and commitment, and CSV files for right-sizing, waste, commitments, showback and actions. It comes with 15 tests and a runbook. It is not the cost dashboard published at the start of the series, which watches AWS and Azure week by week: it is the monthly review that comes after. The insurance group and its figures are fictional.

## Where it comes from

The tool comes from working with Azure Cost Management and the FinOps Framework, optimising Azure costs with right-sizing and reservations, implementing showback, chargeback and unit cost metrics, owning an IT budget and operating a hybrid AWS and Azure environment. The lessons I keep from it: the peak decides a resize, not the average, and a stopped VM is not a deallocated one.""",
 es="""
Una reserva para diez servidores de batch va al 55% desde que la mitad del batch se fue a otra plataforma, caduca en seis semanas y está configurada para renovarse sola. Es uno de los hallazgos de un mes de 94.403 euros en el que la revisión identifica 11.101 euros al mes de ahorro. Así lo detecta la revisión mensual de costes de Azure que acompaña a este post, una herramienta que se ejecuta con datos de ejemplo de un grupo asegurador inventado con cinco suscripciones y 133 máquinas virtuales, revisado el 4 de noviembre sobre octubre, con precios redondos inventados y los problemas puestos a propósito.

Una reserva es un compromiso de pagar capacidad por adelantado a cambio de un precio menor, y la herramienta considera que una por debajo del 80% de uso es dinero pagado por nada. Para cada reserva y plan de ahorro por debajo de su objetivo muestra el coste sin usar del mes, y para los que caducan en los próximos 90 días pide una decisión: renovar o cambiar. Cuando un compromiso se renovaría solo con un uso bajo, el hallazgo es crítico.

## Tres máquinas de SQL Server que no pasan del 15% de CPU

Tres VMs de SQL Server en E16s_v5 llegan como mucho al 15% de CPU y usan un tercio de su memoria, porque se dimensionaron para una migración hace dos años. La herramienta busca VMs cuyo p95 de CPU, el nivel por debajo del que está la máquina el 95% del tiempo, y cuyo pico de memoria en 30 días caben en un tamaño menos dentro de la misma familia. Una VM cubierta por una reserva se marca, porque redimensionarla no ahorra nada hasta que la capacidad liberada se usa o se cambia.

Una VM de informes se apagó desde dentro de Windows hace tres semanas y se sigue pagando como si estuviera encendida, porque nadie la desasignó, es decir, nadie la liberó en Azure. Catorce VMs de desarrollo y pruebas funcionan todas las noches y todos los fines de semana. Los discos y las IP públicas de un proyecto de migración que terminó en agosto siguen ahí, sin conectar y sin etiquetar, y un disco sin conectar se paga entero.

## Cuarenta VMs de producción con pago por uso y un 11% de la factura sin dueño

Cuarenta VMs de producción funcionan todo el mes con pago por uso mientras solo una cuarta parte del gasto en VMs está cubierta por un compromiso. La revisión enumera las VMs estables en pago por uso que cubriría un compromiso, pero solo después del desperdicio: comprar antes congelaría durante años el sobredimensionado de hoy.

En el showback, la práctica de enseñar a cada área lo que gasta, el 11% de la factura no tiene centro de coste, así que nadie pregunta por él. Un centro de coste cierra el mes un 14% por encima del presupuesto y va camino de repetirlo. El coste por usuario activo de los canales digitales sube un 15%, porque los usuarios han bajado y el coste no.

## Cómo se calcula cada ahorro

Cada ahorro es una estimación mensual al ritmo de los últimos siete días, y el pack explica cómo se ha calculado. La mitad de vCPU en la misma familia es la mitad del coste de cómputo; un horario de oficina son 60 de 168 horas; un compromiso es una estimación por arriba que hay que contrastar con Azure Advisor antes de comprar. La cobertura se mide en horas, porque una VM de Windows o de SQL Server cubierta por una reserva sigue teniendo filas de pago por uso por su licencia.

## Cómo usarlo con datos reales

La parte de costes es la exportación FOCUS, un formato estándar de costes, tal como la escribe Azure Cost Management: el coste efectivo para el gasto amortizado, el coste facturado al lado y la parte sin usar de los compromisos a partir de las filas marcadas como no usadas. El repositorio incluye un exportador de solo lectura en PowerShell para los módulos Az y las API de reservas y planes de ahorro, y funciona con Python solo con la librería estándar. Genera un informe con un veredicto del mes, un pack de ahorro para la revisión mensual de FinOps con una columna de decisión para cada redimensionado y cada compromiso, y ficheros CSV de redimensionado, desperdicio, compromisos, showback y acciones. Incluye 15 tests y un runbook. No es el panel de costes publicado al principio de la serie, que vigila AWS y Azure semana a semana: es la revisión mensual que viene después. El grupo asegurador y sus cifras son ficticios.

## De dónde sale

La herramienta nace de trabajar con Azure Cost Management y el FinOps Framework, de optimizar costes de Azure con redimensionado y reservas, de implantar showback, chargeback y métricas de coste unitario, de ser responsable de un presupuesto de IT y de operar un entorno híbrido de AWS y Azure. Las lecciones que me quedo: un redimensionado lo decide el pico, no la media, y una VM parada no es una VM desasignada."""),
dict(n="44", repo="44-m365-copilot-readiness", date="2026-11-05", updated="2026-11-18", cat="tools",
 title_en="An HR site open to the whole company could reach 1,650 people through Copilot two weeks before a new wave",
 title_es="Un sitio de RR. HH. abierto a toda la empresa podría llegar a 1.650 personas por Copilot antes de una oleada",
 seo_title_en="Microsoft 365 Copilot readiness review · Iñigo González",
 seo_title_es="Revisión de preparación para Copilot · Iñigo González",
 seo_desc="Microsoft 365 Copilot readiness before each wave: licences to reclaim, training, MFA, SharePoint oversharing, labels, DLP, agents and adoption.",
 seo_desc_es="A partir de los usuarios de Entra ID, el informe de uso de Microsoft 365 Copilot, los sitios de SharePoint, la cobertura de etiquetas y las directivas de DLP…",
 dek_en="The Copilot readiness review, published with fictional data from an energy company with 1,800 people in three waves, cross-checks users, usage, SharePoint sites, labels, DLP, Copilot Studio agents and training to say what Copilot could surface that it should not and whether each wave is ready.",
 dek_es="La revisión de preparación para Copilot, publicada con datos ficticios de una empresa de energía con 1.800 personas en tres oleadas, cruza usuarios, uso, sitios de SharePoint, etiquetas, DLP, agentes de Copilot Studio y formación para decir qué podría mostrar Copilot que no debería y si cada oleada está lista.",
 en="""
Two weeks before a Copilot wave of 400 people, the HR employee relations site has been shared with Everyone except external users since a migration, and 1,650 people could get its content back in an answer. That is what the Microsoft 365 Copilot readiness review published with this post finds. It is a tool that runs on demo data from a made-up energy company with 1,800 people in three waves, reviewed on 5 November, two weeks before the second wave, with the problems placed on purpose. Its verdict: four critical sites, and no wave ready until they are fixed.

Copilot answers from everything a person can already open. It does not create new access, but it makes old oversharing easy to find, so a rollout that went well in the pilot can go wrong in the next wave for reasons no single console shows. The tool says which waves every issue reaches: the waves with people in its department, or every wave when it is critical oversharing or an agent open to the whole company. A wave is not ready when a critical issue reaches it.

## A recruitment site with open links and a litigation site with no owner

The HR site is not alone. The recruitment site has Anyone links, which open without signing in, and no label. A closed litigation site has no owner and is still searchable. The review checks SharePoint sites shared with Everyone except external users or with Anyone links, sites with no owner or only one, sites without a sensitivity label and inactive sites Copilot can still search. While they are fixed, it proposes Restricted Content Discovery, a setting that keeps a site out of Copilot answers; it buys time but changes no permission.

A quarter of Finance's files carry a sensitivity label, the tag that marks how confidential a document is, and the DLP policy for Copilot, the rule meant to stop sensitive data leaving, is still in simulation.

## An agent built by someone who has left, reading from an unapproved Dropbox

An agent published to the whole company was built by someone who has left and reads from a Dropbox connector nobody approved. An HR agent helps screen candidates and is not in the AI register. The tool flags agents with no owner, published to everyone, using connectors not on the allowed list or unused, and agents that support decisions about people with no entry in the register. That column is a record, not a legal assessment.

## Thirty-seven licences to reclaim and a wave 70% trained

Thirty-four licences have not been used in a month, while the next wave is 14 licences short. In all, the review finds 37 licences to reclaim, worth 1,110 euros a month at the price set in the settings, and checks whether the pool covers the next wave once they are back. The wave itself is 70% trained, with 14 people not registered for MFA and 31 without a compliant device. For every wave the tool checks training, MFA, a compliant device, a licence and a champion in each department, and it tracks adoption by department and app with its trend and the survey.

## How to use it with real data

The usage data is the Microsoft Graph Copilot report per user, the site data comes from Get-SPOSite and the SharePoint data access governance report, and the agents come from the Power Platform inventory. The repository includes a read-only PowerShell exporter for Microsoft Graph and SharePoint Online, and runs on Python with only the standard library. It produces a verdict per wave (ready, attention or not ready), a web report, a pack for the Copilot steering group with a decision column per wave, and CSV files for licences, oversharing, agents, adoption, waves and actions. It comes with 14 tests and a runbook with the steering group agenda, go or no go per wave and the ADKAR steps. It is not the tenant governance review published earlier, which looks at admin roles and Conditional Access: it is the review before each wave and every month after. The energy company is fictional.

## Where it comes from

The tool comes from deploying Microsoft 365 Copilot and driving its adoption, administering Copilot Studio agents, being Global Administrator of Microsoft 365, working with Purview, DLP and sensitivity labels, and change management with Prosci, ADKAR and Kotter. The lesson I keep: the permissions have to be fixed before the wave, not after.""",
 es="""
Dos semanas antes de una oleada de Copilot de 400 personas, el sitio de relaciones laborales de RR. HH. está compartido con Todos excepto los usuarios externos desde una migración, y 1.650 personas podrían recibir su contenido en una respuesta. Así lo detecta la revisión de preparación para Microsoft 365 Copilot que acompaña a este post, una herramienta que se ejecuta con datos de ejemplo de una empresa de energía inventada con 1.800 personas en tres oleadas, revisada el 5 de noviembre, a dos semanas de la segunda, con los problemas puestos a propósito. Su veredicto: cuatro sitios críticos y ninguna oleada lista hasta que se arreglen.

Copilot responde a partir de todo lo que una persona ya puede abrir. No crea accesos nuevos, pero hace fácil encontrar la sobreexposición de siempre, así que un despliegue que fue bien en el piloto puede torcerse en la siguiente oleada por motivos que ninguna consola enseña por sí sola. La herramienta dice a qué oleadas alcanza cada problema: a las que tienen personas de su departamento, o a todas cuando es una sobreexposición crítica o un agente abierto a toda la empresa. Una oleada no está lista cuando le alcanza un problema crítico.

## Un sitio de selección con vínculos abiertos y uno de un litigio sin propietario

El sitio de RR. HH. no es el único. El de selección tiene vínculos de cualquier persona, que se abren sin iniciar sesión, y ninguna etiqueta. Un sitio de un litigio cerrado no tiene propietario y sigue siendo buscable. La revisión comprueba los sitios de SharePoint compartidos con Todos excepto los usuarios externos o con vínculos de cualquier persona, los sitios sin propietario o con uno solo, los que no tienen etiqueta de confidencialidad y los inactivos que Copilot todavía puede buscar. Mientras se arreglan, propone Restricted Content Discovery, una opción que deja un sitio fuera de las respuestas de Copilot; da tiempo, pero no cambia ningún permiso.

Una cuarta parte de los archivos de Finanzas lleva etiqueta de confidencialidad, la marca que indica lo reservado que es un documento, y la directiva de DLP para Copilot, la regla que debe impedir que salgan datos sensibles, sigue en simulación.

## Un agente creado por alguien que ya se fue y que lee de un Dropbox sin aprobar

Un agente publicado para toda la empresa lo creó alguien que ya se ha ido y lee de un conector de Dropbox que nadie aprobó. Un agente de RR. HH. ayuda a cribar candidatos y no está en el registro de IA. La herramienta marca los agentes sin propietario, publicados para todos, con conectores fuera de la lista permitida o sin uso, y los que apoyan decisiones sobre personas sin entrada en el registro. Esa columna es un registro, no una valoración jurídica.

## Treinta y siete licencias a recuperar y una oleada formada al 70%

Treinta y cuatro licencias llevan un mes sin usarse mientras a la siguiente oleada le faltan 14. En total, la revisión encuentra 37 licencias a recuperar, 1.110 euros al mes al precio fijado en la configuración, y comprueba si el remanente cubre la siguiente oleada una vez recuperadas. La propia oleada está formada al 70%, con 14 personas sin registrar en MFA y 31 sin un equipo conforme. Para cada oleada la herramienta comprueba formación, MFA, equipo conforme, licencia y un champion en cada departamento, y sigue la adopción por departamento y aplicación con su tendencia y la encuesta.

## Cómo usarlo con datos reales

El uso sale del informe de Copilot por usuario de Microsoft Graph, los datos de los sitios de Get-SPOSite y del informe de gobierno de acceso a datos de SharePoint, y los agentes del inventario de Power Platform. El repositorio incluye un exportador de solo lectura en PowerShell para Microsoft Graph y SharePoint Online, y funciona con Python solo con la librería estándar. Genera un veredicto por oleada (lista, atención o no lista), un informe web, un pack para el comité de dirección de Copilot con una columna de decisión por oleada y ficheros CSV de licencias, sobreexposición, agentes, adopción, oleadas y acciones. Incluye 14 tests y un runbook con el orden del día del comité, el sí o no de cada oleada y los pasos de ADKAR. No es la revisión de gobierno del tenant publicada antes, que mira roles de administración y Acceso condicional: es la revisión antes de cada oleada y cada mes después. La empresa de energía es ficticia.

## De dónde sale

La herramienta nace de desplegar Microsoft 365 Copilot e impulsar su adopción, de administrar agentes de Copilot Studio, de ser administrador global de Microsoft 365, de trabajar con Purview, DLP y etiquetas de confidencialidad, y de la gestión del cambio con Prosci, ADKAR y Kotter. La lección que me quedo: los permisos hay que arreglarlos antes de la oleada, no después."""),
dict(n="45", repo="45-network-config-compliance", date="2026-11-06", cat="tools",
 title_en="Weekly network review rates 8 of 34 devices non-compliant and finds telnet still open and a change never saved",
 title_es="La revisión semanal de la red da por no conformes 8 de 34 equipos y halla telnet abierto y un cambio sin guardar",
 seo_title_en="Network configuration compliance review · Iñigo González",
 seo_title_es="Cumplimiento de configuración de red · Iñigo González",
 seo_desc="Weekly compliance review of Cisco, Aruba and FortiGate configs: backups, unsaved changes, management plane, SNMP, VLANs, policies and end of support.",
 seo_desc_es="Revisión semanal de configuraciones Cisco, Aruba y FortiGate: copias, cambios sin guardar, gestión, SNMP, VLAN, políticas y fin de soporte.",
 dek_en="The weekly network compliance review, published with fictional data from a logistics company with three comms rooms and 34 devices, cross-checks Cisco, Aruba and FortiGate configuration backups, the Device42 inventory, a baseline and the approved changes to give each device and site a status.",
 dek_es="La revisión semanal de cumplimiento de la red, publicada con datos ficticios de una empresa de logística con tres salas de comunicaciones y 34 equipos, cruza las copias de configuración de Cisco, Aruba y FortiGate, el inventario de Device42, una línea base y los cambios aprobados para dar un estado a cada equipo y sede.",
 en="""
An access switch was changed at two in the morning with no ticket and the change was never saved, so the next power cut will take it away. A branch switch still accepts telnet, the old unencrypted remote login, because it was installed from an old template. Both are among the findings of the weekly network configuration review published with this post, which rates 8 of 34 devices non-compliant. It is a tool that runs on demo data from a made-up logistics company with three comms rooms, reviewed on 6 November with the problems placed on purpose: 9 devices compliant, 17 drifting and 8 non-compliant, with seven critical findings for the next change window.

Network configurations drift one night change at a time, and in a company with several comms rooms nobody reads every running configuration every week. Each problem is visible in one place, the backup, the inventory or the change calendar, and nobody joins them. The tool reads the backups, compares them with a baseline and with the approved changes, and gives every device, every site and the whole network a status: compliant, drift or non-compliant.

## A FortiGate open on its WAN and an all-to-all policy left from a cutover

A FortiGate has HTTPS and SSH administration open on its WAN interface, the side facing the internet, and an accept policy from all to all with service ALL and logging off, left from a cutover two months ago. The review checks admin access on WAN interfaces, any-any accept policies, policies without logging, disabled policies kept for months and firmware below the baseline.

Two devices answer SNMP, the protocol monitoring tools use to read devices, with the community public, one of them because nobody removed the factory default. The switches of one site point NTP, the time service, to a server that was switched off, so their logs disagree with everyone else's. The management checks cover SSH v2 only, no telnet, password encryption, AAA with TACACS+ or RADIUS and a local fallback, a login banner, an idle timeout and management access limited to the management network.

## Two devices with no backup and a site ten days behind

Two devices have no backup at all, and a whole site's backups are ten days old since a firewall rule broke the backup job. The tool flags devices with no backup, backups older than a week, Cisco configurations changed after the last save and changes made outside an approved ticket.

Six unused ports are up in VLAN 1, the default network segment. A router runs a release that is not on the approved list, and an access switch went out of vendor support five years ago and is still in the rack. On switching, the review checks unused ports shut down in the parking VLAN, PortFast and BPDU guard on user ports, no native VLAN 1 on trunks and port security where the baseline asks for it. Unused ports are the ones with no description, because the description is the record that a port is in use.

## How to use it with real data

There is a small parser per platform: Cisco IOS-XE with its `Last configuration change` and `NVRAM config last updated` lines, ArubaOS-Switch, and FortiOS. Every rule gives every device pass, fail or not applicable, so the audit evidence is one CSV; a critical failure makes a device non-compliant and a site takes the worst status of its devices. The repository includes a read-only PowerShell collector with Posh-SSH that only sends `show running-config` or `show full-configuration`, and Oxidized and RANCID backups work as they are. It runs on Python with only the standard library and produces a web report with a grid of devices, a pack for the change board with a proposed window and a decision column per finding, and CSV files. It comes with 14 tests and a runbook for the weekly cycle. The end-of-support dates come from the same Device42 export used by the asset lifecycle planner published earlier in the series. The company and its devices are fictional.

## Where it comes from

The tool comes from operating Cisco switches and routers, comms rooms and racks across several sites, Device42, Fortinet FortiGate and LAN, WAN and Wi-Fi in Spain, Italy and Turkey, and from being the process owner of change management and the CMDB. The lessons I keep: a backup nobody checks is not a backup, and a temporary any-any policy is never temporary unless someone puts a date on it.""",
 es="""
Un switch de acceso se cambió a las dos de la madrugada sin ticket y el cambio nunca se guardó, así que el próximo corte de luz se lo llevará. Un switch de una sede sigue aceptando telnet, el acceso remoto antiguo y sin cifrar, porque se instaló con una plantilla antigua. Así lo detecta la revisión semanal de configuración de red que acompaña a este post, que da por no conformes 8 de 34 equipos, una herramienta que se ejecuta con datos de ejemplo de una empresa de logística inventada con tres salas de comunicaciones, revisada el 6 de noviembre con los problemas puestos a propósito: 9 equipos conformes, 17 con desviaciones y 8 no conformes, con siete hallazgos críticos para la próxima ventana de cambios.

Las configuraciones de red se desvían de cambio nocturno en cambio nocturno, y en una empresa con varias salas de comunicaciones nadie lee todas las configuraciones cada semana. Cada problema se ve en un sitio, la copia, el inventario o el calendario de cambios, y nadie los junta. La herramienta lee las copias, las compara con una línea base y con los cambios aprobados, y da a cada equipo, a cada sede y a toda la red un estado: conforme, con desviaciones o no conforme.

## Un FortiGate abierto por la WAN y una política de todo a todo que quedó de una migración

Un FortiGate tiene la administración por HTTPS y SSH abierta en su interfaz WAN, la que da a internet, y una política que acepta de all a all con servicio ALL y sin log, que quedó de una migración hace dos meses. La revisión comprueba la administración en interfaces WAN, las políticas any-any que aceptan, las políticas sin log, las desactivadas que se quedan meses y el firmware por debajo de la línea base.

Dos equipos responden a SNMP, el protocolo con el que la monitorización lee los equipos, con la comunidad public, uno de ellos porque nadie quitó la que trae de fábrica. Los switches de una sede apuntan el NTP, el servicio de hora, a un servidor que se apagó, así que sus logs no cuadran con los del resto. Las comprobaciones de gestión cubren solo SSH v2, nada de telnet, cifrado de contraseñas, AAA con TACACS+ o RADIUS y respaldo local, un banner de acceso, un tiempo de inactividad y el acceso de gestión limitado a la red de gestión.

## Dos equipos sin copia y una sede con diez días de retraso

Dos equipos no tienen ninguna copia, y las copias de toda una sede tienen diez días desde que una regla de firewall rompió la tarea de copia. La herramienta marca los equipos sin copia, las copias de más de una semana, las configuraciones de Cisco cambiadas después del último guardado y los cambios hechos fuera de un ticket aprobado.

Seis puertos sin usar están levantados en la VLAN 1, el segmento de red por defecto. Un router tiene una versión que no está en la lista aprobada, y un switch de acceso lleva cinco años sin soporte del fabricante y sigue en el rack. En switching, la revisión comprueba que los puertos sin usar estén apagados en la VLAN de aparcamiento, PortFast y BPDU guard en los puertos de usuario, nada de VLAN nativa 1 en las troncales y port security donde la línea base lo pide. Los puertos sin usar son los que no tienen descripción, porque la descripción es el registro de que un puerto está en uso.

## Cómo usarlo con datos reales

Hay un pequeño parser por plataforma: Cisco IOS-XE con sus líneas `Last configuration change` y `NVRAM config last updated`, ArubaOS-Switch y FortiOS. Cada regla da a cada equipo cumple, no cumple o no aplica, así que la evidencia para una auditoría es un CSV; un fallo crítico hace no conforme a un equipo y una sede toma el peor estado de sus equipos. El repositorio incluye un recolector de solo lectura en PowerShell con Posh-SSH que solo envía `show running-config` o `show full-configuration`, y las copias de Oxidized y RANCID sirven tal cual. Funciona con Python solo con la librería estándar y genera un informe web con una cuadrícula de equipos, un pack para el comité de cambios con una ventana propuesta y una columna de decisión por hallazgo, y ficheros CSV. Incluye 14 tests y un runbook para el ciclo semanal. Las fechas de fin de soporte salen de la misma exportación de Device42 que usa el planificador del ciclo de vida de equipos publicado antes en la serie. La empresa y sus equipos son ficticios.

## De dónde sale

La herramienta nace de operar switches y routers Cisco, salas de comunicaciones y racks en varias sedes, de Device42, de Fortinet FortiGate y de redes LAN, WAN y wifi en España, Italia y Turquía, y de ser responsable del proceso de gestión de cambios y de la CMDB. Las lecciones que me quedo: una copia que nadie comprueba no es una copia, y una política any-any temporal nunca es temporal si nadie le pone fecha."""),
dict(n="46", repo="46-problem-management-review", date="2026-11-08", updated="2026-11-17", cat="tools",
 title_en="Forty-six VPN certificate incidents were closed one by one since August and nobody opened a problem record",
 title_es="Cuarenta y seis incidencias de certificado de la VPN se cerraron una a una desde agosto sin abrir ningún problema",
 seo_title_en="Problem management review · Iñigo González",
 seo_title_es="Revisión de gestión de problemas · Iñigo González",
 seo_desc="Monthly problem review from ITSM exports: recurring incidents with no problem, major incidents without RCA, stuck problems, known errors and fixes.",
 seo_desc_es="Revisión mensual de problemas con exportaciones de ITSM: incidencias repetidas sin problema, incidentes graves sin RCA, errores conocidos y soluciones.",
 dek_en="The monthly problem management review, published with fictional data from a logistics company with 1,572 incidents in six months, cross-checks incidents, problems, linked changes and the CMDB to find repeat incidents with no problem, major incidents with no root cause and fixes that did not work.",
 dek_es="La revisión mensual de gestión de problemas, publicada con datos ficticios de una empresa de logística con 1.572 incidencias en seis meses, cruza incidencias, problemas, cambios vinculados y la CMDB para encontrar repeticiones sin problema, incidentes graves sin causa raíz y soluciones que no funcionaron.",
 en="""
Forty-six incidents about a VPN certificate error have been closed one by one since late August and nobody has opened a problem record, the ticket meant to find and remove the cause behind repeat incidents. That is what the monthly problem management review published with this post finds. It is a tool that runs on demo data from a made-up logistics company with three sites, six months of history, 1,572 incidents, 35 problems and 20 changes, reviewed on 8 November with the problems placed on purpose. Its verdict for the month is at risk.

Problem management is the part of ITSM that everyone agrees with and nobody has time for. The service desk resolves the same incident again and again with the same workaround, every ticket closes inside its SLA and the dashboard looks fine. The tool groups similar incidents on the same configuration item, the CI, and category, and ranks the clusters with no problem record by how many incidents they hold, their priority and how critical the CI is in the CMDB. In the demo, seventeen printer driver incidents at one site look like seventeen different tickets until they are grouped.

## A warehouse outage with no problem record three weeks later

The warehouse system went down for four hours three weeks ago and there is still no problem record. The transport system outage of the week before has one, under investigation, with no root cause. The review checks every major incident five working days after it happened, leaving weekends and holidays out: it needs a problem record and that problem needs a root cause.

Three open problems have no owner and two of them are the same problem. The tool counts six stuck problems in all: no update for a month, past the target date, under investigation for more than 60 days, with no owner, or owned by a team other than the one that owns the CI. Almost a third of the root causes say Unknown or Other, which is valid while investigating but never as the way to close.

## A fix closed in September and eleven more incidents since

A change closed the file share problem in September and eleven more incidents of the same kind have arrived since, most of them not linked to it. The tool checks whether a fix worked by looking for the words the problem's incidents had in common, on the same CI, after the implementation date. It also flags problems closed on a change that was backed out and reopened incidents.

A known error on the warehouse scanners, a problem whose cause is known and has a workaround, has lived on that workaround for 120 days and nobody has raised the change for the permanent fix. The review lists workarounds older than 90 days with no change behind them, and workarounds the service desk has not got.

## Why the grouping is simple on purpose

Each incident summary becomes a set of words without stop words, and two summaries are similar when they share at least two words and half the words of the shorter one. Each incident joins a cluster in order of creation, so the result is the same every time and the common words explain why the incidents were grouped.

## How to use it with real data

The tool reads incidents and problems exported from Jira Service Management, HaloITSM or EasyVista, the linked changes and the CMDB. The repository includes a read-only PowerShell exporter for the Jira Service Management Cloud REST API that only sends GET requests with JQL, with an API token asked for at run time and never stored. It runs on Python with only the standard library and produces a status per area, a web report, a pack with a 60-minute agenda, a decision column and the list for the next CAB, and CSV files. It comes with 14 tests and a runbook. It sits between the major incident kit and the change calendar review published earlier in the series. The company and its tickets are fictional.

## Where it comes from

The tool comes from being the formal process owner of incident, change and problem management and the CMDB, leading the technical response in major incidents and their root cause analysis, and administering Jira Service Management. The lessons I keep: a workaround that works is the most expensive thing in the service desk, because it hides the problem, and closing a problem when the change goes in is too early.""",
 es="""
Cuarenta y seis incidencias por un error de certificado de la VPN se han cerrado una a una desde finales de agosto y nadie ha abierto un problema, el registro que sirve para encontrar y eliminar la causa de las incidencias que se repiten. Así lo detecta la revisión mensual de gestión de problemas que acompaña a este post, una herramienta que se ejecuta con datos de ejemplo de una empresa de logística inventada con tres sedes, seis meses de historial, 1.572 incidencias, 35 problemas y 20 cambios, revisada el 8 de noviembre con los problemas puestos a propósito. Su veredicto para el mes es en riesgo.

La gestión de problemas es la parte de ITSM en la que todo el mundo está de acuerdo y para la que nadie tiene tiempo. El service desk resuelve una y otra vez la misma incidencia con la misma solución temporal, cada ticket se cierra dentro de su SLA y el cuadro de mando parece estar bien. La herramienta agrupa las incidencias parecidas en el mismo elemento de configuración, el CI, y la misma categoría, y ordena los grupos sin problema por cuántas incidencias tienen, su prioridad y la criticidad del CI en la CMDB. En la demo, diecisiete incidencias de un driver de impresora en una sede parecen diecisiete tickets distintos hasta que se agrupan.

## Una caída del almacén sin registro de problema tres semanas después

El sistema de almacén se cayó cuatro horas hace tres semanas y sigue sin registro de problema. La caída del sistema de transporte de la semana anterior tiene uno, en investigación y sin causa raíz. La revisión comprueba cada incidente grave cinco días laborables después, sin contar fines de semana ni festivos: necesita un problema y ese problema necesita una causa raíz.

Tres problemas abiertos no tienen responsable y dos de ellos son el mismo problema. La herramienta cuenta seis problemas atascados en total: sin actualizar en un mes, con la fecha objetivo vencida, más de 60 días en investigación, sin responsable o en manos de un equipo distinto del que es dueño del CI. Casi un tercio de las causas raíz dicen Desconocida u Otra, algo válido mientras se investiga pero nunca para cerrar.

## Una solución cerrada en septiembre y once incidencias más desde entonces

Un cambio cerró en septiembre el problema de la carpeta compartida y desde entonces han llegado once incidencias más del mismo tipo, casi todas sin vincular. La herramienta comprueba si una solución funcionó buscando las palabras que tenían en común las incidencias del problema, en el mismo CI, después de la fecha de implantación. También marca los problemas cerrados con un cambio que se deshizo y las incidencias reabiertas.

Un error conocido de los lectores del almacén, un problema cuya causa se conoce y que tiene solución temporal, lleva 120 días viviendo de esa solución y nadie ha pedido el cambio que lo arregle. La revisión enumera las soluciones temporales de más de 90 días sin cambio detrás y las que el service desk no tiene.

## Por qué la agrupación es simple a propósito

Cada resumen de incidencia se convierte en un conjunto de palabras sin las vacías, y dos resúmenes se parecen cuando comparten al menos dos palabras y la mitad de las palabras del más corto. Cada incidencia entra en un grupo por orden de creación, así que el resultado es siempre el mismo y las palabras comunes explican por qué se agruparon.

## Cómo usarlo con datos reales

La herramienta lee las incidencias y los problemas exportados de Jira Service Management, HaloITSM o EasyVista, los cambios vinculados y la CMDB. El repositorio incluye un exportador de solo lectura en PowerShell para la API REST de Jira Service Management Cloud que solo envía peticiones GET con JQL, con un token de API que se pide al ejecutarlo y nunca se guarda. Funciona con Python solo con la librería estándar y genera un estado por área, un informe web, un pack con un orden del día de 60 minutos, una columna de decisión y la lista para el próximo CAB, y ficheros CSV. Incluye 14 tests y un runbook. Se sitúa entre el kit de incidentes graves y la revisión del calendario de cambios publicados antes en la serie. La empresa y sus tickets son ficticios.

## De dónde sale

La herramienta nace de ser responsable formal de los procesos de gestión de incidencias, cambios y problemas y de la CMDB, de dirigir la respuesta técnica en incidentes graves y su análisis de causa raíz, y de administrar Jira Service Management. Las lecciones que me quedo: una solución temporal que funciona es lo más caro del service desk, porque esconde el problema, y cerrar un problema cuando se implanta el cambio es demasiado pronto."""),
dict(n="47", repo="47-multi-site-it-scorecard", date="2026-11-08", updated="2026-11-17", cat="tools",
 title_en="An office lost its only local engineer and first-contact resolution fell from 79% to 56% the next month",
 title_es="Una oficina se quedó sin su único técnico local y la resolución en el primer contacto cayó del 79% al 56%",
 seo_title_en="Multi-site IT scorecard with RAG · Iñigo González",
 seo_title_es="Cuadro de mando de IT multisede · Iñigo González",
 seo_desc="Monthly IT scorecard per office: SLA, FCR, backlog and ageing, CSAT, availability, Intune compliance, DR tests, RAG, trend and the reason behind every red.",
 seo_desc_es="Cuadro de mando mensual de IT por oficina: SLA, FCR, backlog, CSAT, disponibilidad, cumplimiento en Intune y pruebas de DR, con RAG, tendencia y motivos.",
 dek_en="The monthly multi-site IT scorecard, published with fictional data from a company with 2,500 people in eight European offices, cross-checks tickets, monitoring outages, Intune devices, open actions and DR tests to rate each office red, amber or green with the reason behind every red.",
 dek_es="El cuadro de mando mensual de IT multisede, publicado con datos ficticios de una empresa con 2.500 personas en ocho oficinas europeas, cruza tickets, caídas de la monitorización, equipos de Intune, acciones abiertas y pruebas de DR para poner a cada oficina en rojo, ámbar o verde con el motivo de cada rojo.",
 en="""
An office lost its only local engineer and, the next month, first-contact resolution fell from 79% to 56%, escalations to the central team went from 14% to 39% and satisfaction from 4.5 to 3.4. That is what the multi-site IT scorecard published with this post finds. It is a tool that runs on demo data from a made-up company with 2,500 people in eight European offices, reporting October against September with the problems placed on purpose: the region amber, two offices red, nine red KPIs and six not rated.

A regional IT lead gets the same question every month: how is IT doing at each office, which one is slipping and why. The numbers live in five places and on their own they rarely tell the story. The tool gives every KPI a red, amber or green status against its target, the trend against the previous month and, for every red, the reason found in the data, such as an office with no local IT staff. The reason sits next to the red, so the review does not spend its time looking for it.

## A backup circuit down for almost nine hours that nobody noticed

The backup circuit of one office was down twice for almost nine hours in the month and nobody noticed, because the primary stayed up. It is the outage nobody reports and the one that matters on the day the primary fails. Availability is computed from the outage events of the monitoring tool, unplanned minutes over the minutes in the month, against a target per service, because a backup circuit and a printer do not deserve the same one.

A fifth of another office's laptops fell out of compliance the week a new Windows 11 build reached them, and the scorecard shows that build as the reason. Device KPIs use the last Intune snapshot of each month: compliance, devices that stopped checking in and hardware older than four years.

## Eight tickets are too few to rate

The smallest office has eight tickets, and an SLA percentage on eight tickets is green or red by chance. Under its minimum volume a KPI is not rated, and not rated is never shown as green. A small office is scored on what it has, its backlog, availability, devices and DR test, and its few tickets are read one by one.

One office has not tested its DR plan, the plan for recovering from a disaster, for seventeen months. The busiest office has 91 open tickets, 35 of them older than 30 days. For the service desk the scorecard tracks SLA by priority, first-contact resolution, reopen and escalation rates, backlog per 100 users and its ageing, and satisfaction.

## How the score is built

Every KPI is computed per office and month from the raw exports, the same way for both months, so the trend is not a number someone typed. The site score is the weighted share of points over the rated KPIs, and a site with a red is never green. The regional row pools tickets and devices but takes the worst office for availability, actions and DR tests, so it never averages one office's outage away.

## How to use it with real data

The repository includes a read-only PowerShell exporter for Intune through Microsoft Graph and for Jira Service Management through its REST API, and runs on Python with only the standard library. It produces a web report with a heatmap of offices by KPI, a pack for the regional review with one section per office and a decision column, and CSV files with the scorecard, the detail per KPI, the trend, the findings and the actions. It comes with 14 tests and a runbook covering the review agenda, what to do with each red, how to set targets and how to keep the KPIs from being gamed. The service desk KPIs published at the start of the series look at one desk; this puts the offices side by side. The company and its offices are fictional.

## Where it comes from

The tool comes from leading the IT of one office with two engineers at a multi-site financial services company, supporting around 2,500 users across European offices, in an office that grew from about 15 to over 120 people, and from defining SLAs and OLAs and running availability and capacity management. The lesson I keep: a scorecard is for deciding where to help, not for ranking people.""",
 es="""
Una oficina se quedó sin su único técnico local y, al mes siguiente, la resolución en el primer contacto bajó del 79% al 56%, los escalados al equipo central pasaron del 14% al 39% y la satisfacción de 4,5 a 3,4. Así lo detecta el cuadro de mando de IT multisede que acompaña a este post, una herramienta que se ejecuta con datos de ejemplo de una empresa inventada con 2.500 personas en ocho oficinas europeas, que informa de octubre frente a septiembre con los problemas puestos a propósito: la región en ámbar, dos oficinas en rojo, nueve indicadores en rojo y seis sin valorar.

Un responsable de IT regional recibe cada mes la misma pregunta: cómo va IT en cada oficina, cuál se está quedando atrás y por qué. Los datos están en cinco sitios y, por separado, rara vez cuentan la historia. La herramienta da a cada indicador un estado rojo, ámbar o verde frente a su objetivo, la tendencia frente al mes anterior y, en cada rojo, el motivo que hay en los datos, como una oficina sin personal de IT local. El motivo está al lado del rojo, así que la revisión no se pasa el rato buscándolo.

## Un circuito de respaldo caído casi nueve horas sin que nadie se enterase

El circuito de respaldo de una oficina se cayó dos veces durante casi nueve horas en el mes y nadie se enteró, porque el principal siguió arriba. Es la caída que nadie reporta y la que importa el día que cae el principal. La disponibilidad sale de los eventos de caída de la herramienta de monitorización, minutos no planificados sobre los minutos del mes, frente a un objetivo por servicio, porque un circuito de respaldo y una impresora no merecen el mismo.

Una quinta parte de los portátiles de otra oficina dejó de cumplir la semana en que les llegó una nueva versión de Windows 11, y el cuadro de mando muestra esa versión como motivo. Los indicadores de equipos usan la última foto de Intune de cada mes: cumplimiento, equipos que dejaron de sincronizarse y equipos con más de cuatro años.

## Ocho tickets son demasiado pocos para valorar

La oficina más pequeña tiene ocho tickets, y un porcentaje de SLA sobre ocho tickets sale verde o rojo por azar. Por debajo de su volumen mínimo un indicador no se valora, y lo que no se valora nunca aparece en verde. Una oficina pequeña se puntúa por lo que tiene, su backlog, la disponibilidad, los equipos y la prueba de DR, y sus pocos tickets se leen uno a uno.

Una oficina lleva diecisiete meses sin probar su plan de DR, el plan para recuperarse de un desastre. La oficina con más actividad tiene 91 tickets abiertos, 35 de ellos con más de 30 días. Para el service desk, el cuadro de mando sigue el SLA por prioridad, la resolución en el primer contacto, las tasas de reapertura y de escalado, el backlog por cada 100 usuarios y su antigüedad, y la satisfacción.

## Cómo se calcula la puntuación

Cada indicador se calcula por oficina y mes a partir de las exportaciones en bruto, igual para los dos meses, así que la tendencia no es un número que alguien ha tecleado. La puntuación de la sede es la parte ponderada de puntos sobre los indicadores valorados, y una sede con un rojo nunca está en verde. La fila regional junta los tickets y los equipos pero toma la peor oficina en disponibilidad, acciones y pruebas de DR, así que nunca diluye la caída de una oficina en la media.

## Cómo usarlo con datos reales

El repositorio incluye un exportador de solo lectura en PowerShell para Intune a través de Microsoft Graph y para Jira Service Management a través de su API REST, y funciona con Python solo con la librería estándar. Genera un informe web con un mapa de calor de oficinas por indicador, un dosier para la revisión regional con una sección por oficina y una columna de decisión, y ficheros CSV con el cuadro de mando, el detalle por indicador, la tendencia, los hallazgos y las acciones. Incluye 14 tests y un runbook con el orden del día de la revisión, qué hacer con cada rojo, cómo fijar los objetivos y cómo evitar que se maquillen los indicadores. Los indicadores del service desk publicados al principio de la serie miran un solo service desk; esto pone las oficinas una al lado de otra. La empresa y sus oficinas son ficticias.

## De dónde sale

La herramienta nace de dirigir la IT de una oficina con dos técnicos en una empresa de servicios financieros con varias sedes, dando soporte a unos 2.500 usuarios en oficinas europeas, en una oficina que pasó de unas 15 a más de 120 personas, y de definir SLA y OLA y llevar la gestión de la disponibilidad y la capacidad. La lección que me quedo: un cuadro de mando sirve para decidir dónde ayudar, no para clasificar a las personas."""),
dict(n="48", repo="48-new-starter-day-one-readiness", date="2026-11-09", cat="tools",
 title_en="Four of 25 new starters are blocked before day one, one with an Exchange admin group copied from a colleague",
 title_es="Cuatro de 25 altas están bloqueadas antes del primer día, una con un grupo de administrador copiado de un compañero",
 seo_title_en="New starter day-one readiness check · Iñigo González",
 seo_title_es="Altas: listos para el primer día · Iñigo González",
 seo_desc="Day-one readiness for new starters: account, licence, groups, access, laptop, phone and MFA per joiner, with owners, due dates and a countdown.",
 seo_desc_es="Preparación del primer día de cada alta: cuenta, licencia, grupos, accesos, portátil, móvil y MFA, con responsables, fechas y cuenta atrás.",
 dek_en="The day-one readiness check, published with fictional data from a trading and distribution company with four sites and 25 joiners, cross-checks the HR joiner list, role profiles, Entra ID, devices, licences, stock and access requests to say who will have everything working on day one.",
 dek_es="El control del primer día, publicado con datos ficticios de una empresa de distribución y trading con cuatro sedes y 25 altas, cruza la lista de altas de RR. HH., los perfiles por puesto, Entra ID, los equipos, las licencias, el stock y las peticiones de acceso para decir quién lo tendrá todo funcionando el primer día.",
 en="""
An account created by copying a colleague who used to work in IT comes with an Exchange administrators group, before its owner has even started. It is one of four joiners blocked out of 25 starting in the next two weeks, according to the day-one readiness check published with this post. It is a tool that runs on demo data from a made-up trading and distribution company with four sites, checked on Monday 9 November with the problems placed on purpose: 13 joiners ready, 8 at risk and 4 blocked, and the whole intake blocked.

Day one is the first impression IT makes on a new starter, and it is decided in the two weeks before. HR knows the start dates, Entra ID knows the accounts, Intune knows the laptops, the asset register knows the stock and the ITSM tool knows the access requests, and nobody looks at them together until the joiner is at the desk. The tool compares each joiner with the profile of their role, a file listing the groups, licence, apps, shared mailboxes and whether the role needs a phone. Copying a model user is fast but brings the colleague's history with it, so a privileged group the role does not list is a blocker at any distance from the start.

## A request on Friday for Tuesday and a MacBook with no stock

A warehouse operative's request arrived on Friday for Tuesday, and on Monday his role group and his access to the warehouse system are still missing. A MacBook was requested in an office with none in stock, and an order takes longer than the days left. The laptop of someone starting tomorrow is enrolled but not compliant because BitLocker, the disk encryption, is still pending.

Every fix has the working days it needs, from one for a group to five for a device order. A gap becomes a blocker when its fix no longer fits before the start date, or when the start is within three working days; otherwise it is a risk with an owner and a due date. Each joiner gets a countdown in working days, because the start date is the only deadline that cannot move.

## Two free licences for five joiners

The licence pool has two free units for five joiners. The licence pool and the device stock are shared out in start date order, so the forecast says who will be short, not only by how many. Another account has no usage location, the country setting Microsoft 365 needs, so its licence was never assigned.

A rehire's old account is disabled and someone created a second one with the same employee ID, when the old one should have been reused. A trader starting next Monday has no approval yet for the market data terminal. The check also covers how each joiner will register MFA, with a Temporary Access Pass, a temporary passcode, for the first sign-in.

## How to use it with real data

Each joiner is matched to an account by employee ID, then by the planned UPN, then by name. The repository includes a read-only PowerShell exporter for Microsoft Graph that reads accounts, managers, groups, authentication methods, licences and Intune devices with an interactive sign-in; Jamf Pro inventory exports with the same columns are accepted. It runs on Python with only the standard library and produces a web report with a fix-first list and a countdown board, a pack for the weekly joiners call with owner, due date and done columns, and CSV files with joiner status, gaps, licence and device forecasts and actions. It comes with 15 tests and a runbook covering the weekly call, what ready means, model users, rehires and late requests. The monthly access review published earlier in the series finds an admin group three months later; this check is meant to stop it on day one. The company and its joiners are fictional.

## Where it comes from

The tool comes from running user onboarding for retail stores and head office, Entra ID, Intune and Jamf Pro, automating with PowerShell and Microsoft Graph, and being the IT site leader of an office that grew from about 15 to over 120 people. The lessons I keep: a late request is a conversation with HR, not a heroic weekend, and ready has to mean the same thing for every joiner, written down.""",
 es="""
Una cuenta creada copiando a un compañero que antes trabajaba en IT llega con un grupo de administradores de Exchange, antes de que su dueño haya empezado. Es una de las cuatro altas bloqueadas de las 25 que empiezan en las próximas dos semanas, según el control del primer día que acompaña a este post, una herramienta que se ejecuta con datos de ejemplo de una empresa inventada de distribución y trading con cuatro sedes, revisada el lunes 9 de noviembre con los problemas puestos a propósito: 13 altas listas, 8 en riesgo y 4 bloqueadas, y el conjunto bloqueado.

El primer día es la primera impresión que IT da a una persona nueva, y se decide en las dos semanas anteriores. RR. HH. sabe las fechas de incorporación, Entra ID sabe las cuentas, Intune sabe los portátiles, el inventario sabe el stock y la herramienta de ITSM sabe las peticiones de acceso, y nadie lo mira todo junto hasta que la persona está sentada en su puesto. La herramienta compara cada alta con el perfil de su puesto, un fichero con los grupos, la licencia, las aplicaciones, los buzones compartidos y si el puesto necesita móvil. Copiar a un usuario modelo es rápido pero trae consigo la historia del compañero, así que un grupo privilegiado que el puesto no incluye es un bloqueo, quede el tiempo que quede.

## Una petición el viernes para el martes y un MacBook sin stock

La petición de un operario de almacén llegó el viernes para el martes, y el lunes todavía le faltan el grupo de su puesto y el acceso al sistema de almacén. Se pidió un MacBook en una oficina sin ninguno en stock, y un pedido tarda más que los días que quedan. El portátil de alguien que empieza mañana está inscrito pero no cumple porque BitLocker, el cifrado del disco, sigue pendiente.

Cada solución tiene los días laborables que necesita, desde uno para un grupo hasta cinco para pedir un equipo. Un hueco pasa a bloqueo cuando su solución ya no cabe antes de la incorporación, o cuando la persona empieza en tres días laborables o menos; si no, es un riesgo con responsable y fecha límite. Cada alta tiene una cuenta atrás en días laborables, porque la fecha de incorporación es el único plazo que no se mueve.

## Dos licencias libres para cinco altas

En la bolsa de licencias quedan dos libres para cinco altas. La bolsa de licencias y el stock de equipos se reparten por orden de incorporación, así que la previsión dice a quién le va a faltar, no solo cuántos faltan. Otra cuenta no tiene ubicación de uso, el país que Microsoft 365 necesita, así que su licencia nunca se asignó.

La cuenta antigua de una recontratación está deshabilitada y alguien creó una segunda con el mismo número de empleado, cuando había que reutilizar la antigua. Un trader que empieza el lunes que viene todavía no tiene aprobado el terminal de datos de mercado. El control también cubre cómo registrará cada persona el MFA, con un pase de acceso temporal, un código provisional, para el primer inicio de sesión.

## Cómo usarlo con datos reales

Cada alta se cruza con una cuenta por número de empleado, después por el UPN previsto y después por el nombre. El repositorio incluye un exportador de solo lectura en PowerShell para Microsoft Graph que lee las cuentas, los responsables, los grupos, los métodos de autenticación, las licencias y los equipos de Intune con inicio de sesión interactivo, y acepta exportaciones del inventario de Jamf Pro con las mismas columnas. Funciona con Python solo con la librería estándar y genera un informe web con la lista de lo que hay que arreglar primero y un tablero con la cuenta atrás, un dosier para la reunión semanal de altas con columnas de responsable, fecha y hecho, y ficheros CSV con el estado de cada alta, los huecos, la previsión de licencias y equipos y las acciones. Incluye 15 tests y un runbook con la reunión semanal, qué significa estar listo, los usuarios modelo, las recontrataciones y las peticiones tardías. La revisión mensual de accesos publicada antes en la serie encuentra un grupo de administradores tres meses después; este control está pensado para pararlo el primer día. La empresa y sus altas son ficticias.

## De dónde sale

La herramienta nace de llevar las altas de usuarios en tiendas y oficina central, de Entra ID, Intune y Jamf Pro, de automatizar con PowerShell y Microsoft Graph, y de ser el responsable de IT de una oficina que pasó de unas 15 a más de 120 personas. Las lecciones que me quedo: una petición tardía es una conversación con RR. HH., no un fin de semana heroico, y estar listo tiene que significar lo mismo para todas las altas, y estar escrito."""),
dict(n="49", repo="49-it-project-portfolio-health", date="2026-11-10", cat="tools",
 title_en="A project reported green buys 78 cents of work per euro spent, in a portfolio 6 % over its approved budget",
 title_es="Un proyecto en verde obtiene 78 céntimos de trabajo por euro, en una cartera un 6 % por encima de lo aprobado",
 seo_title_en="IT project portfolio health check · Iñigo González",
 seo_title_es="Salud de la cartera de proyectos IT · Iñigo González",
 seo_desc="IT portfolio health before the SteerCo: computed RAG per project with the reason, watermelon projects, CPI and SPI, people, freezes and decisions needed.",
 seo_desc_es="Salud de la cartera de IT antes del comité: RAG calculado por proyecto y su motivo, proyectos sandía, CPI y SPI, personas, congelaciones y decisiones.",
 dek_en="The portfolio health check, published with fictional data from an insurer with eighteen projects, cross-checks the PPM tool, the milestones, the RAID log, the resource plan and the sprint history to compute each project's status and the decisions for the steering committee.",
 dek_es="La revisión de salud de la cartera, publicada con datos ficticios de una aseguradora con dieciocho proyectos, cruza la herramienta de PPM, los hitos, el registro RAID, el plan de recursos y el histórico de sprints para calcular el estado de cada proyecto y las decisiones del comité.",
 en="""
A document capture project is reported GREEN by its project manager while each euro it spends buys 78 cents of the planned work and its build milestone is six weeks late. That is what the IT project portfolio health check published with this post finds a week before the steering committee. It is an open-source tool that runs on demo data from a made-up insurer with three programmes and eighteen waterfall, agile and SAFe projects, checked on 10 November with the problems placed on purpose.

The 78 cents is the CPI, the cost performance index, and the tool computes it with a deliberately simple version of earned value. The work done is worth the budget times the % complete, or the story points done over the total in agile projects. The work planned by today is the budget times the share of the planned time that has passed, on a straight line. CPI and its schedule twin, the SPI, come from those two numbers, and the budget divided by the CPI says where the cost lands if the rest of the work costs what the work so far did.

## Five projects red and one green only on the outside

Overall, the demo portfolio is red: 5 projects red, 6 amber and 7 green. One of them is what the tool calls a "watermelon", green outside and red inside, and the sum of all the forecasts is 6 % over the envelope that was approved. The review shows its computed GREEN, AMBER or RED with the reason next to the status the project manager reported, per project, per programme and overall.

A project's status is its worst finding in each dimension, and a programme is red when one of its critical projects is red or a third of its projects are. The thresholds sit in a settings file agreed with the committee, and every finding has a severity, an owner and a due date.

## An architect at 180 % and a go-live inside a change freeze

The enterprise architect is planned at 180 % across three critical projects, so the three will slip together. The tool counts an over-allocated person as amber for each of those projects, because it is a portfolio problem rather than a problem of one project.

The other findings are the kind nobody sees from a slide deck. The Windows 11 rollout has not updated its status in five weeks. A network cutover is planned in the middle of the year-end change freeze, and another project goes live on Friday with its change still waiting for the CAB, the change advisory board. An automation project counts a yearly benefit nobody in the business owns. A low-priority intranet redesign is three months late and a quarter over budget, and nobody has asked whether it should go on. An agile portal keeps adding scope while its velocity falls, and three items in the RAID log, the register of risks and issues, are past their date with no owner.

## Eight decisions for the committee, each with its options

The review turns the findings into 8 decisions for the committee, in a fixed order: the gap to the approved envelope first, then the low-priority red projects that could be paused or stopped, the watermelons, the other red projects, the key people, the releases in a freeze and the benefits with no owner. Each decision carries its options (continue, re-plan, pause or stop), a proposal, the impact and an owner. The aim is that the committee spends its hour deciding rather than going through status.

## How to use it with real data

The inputs are the project list of the PPM tool, the milestones, the RAID log, the resource plan, the releases and the sprint history from Jira or Azure DevOps. A read-only exporter takes the closed sprints of a Jira Cloud board through the current issue search, or the past iterations of an Azure DevOps team through a WIQL query, with a token that stays in memory, and writes the points committed, completed and added per sprint.

The tool runs on Python with the standard library only and produces `report.html`, with a heat map of the portfolio, a card per project, a cost and schedule scatter and the resource load; `steerco-pack.md`, one page for the committee; and CSV files for project health, findings, resource load, decisions and actions. It comes with 14 tests and a runbook for the monthly committee: what to send before it, the agenda, how to frame the decisions, how to handle watermelon projects without blame and how to follow up the actions. The intended rhythm is a week before every committee, and weekly for the red projects.

## Where it comes from

I built it from managing a portfolio of initiatives, working as Scrum Master and Product Owner with SAFe and PI Planning, writing business cases with ROI, and taking part in release management and the change advisory board. Two lessons are behind it: a RAG someone types in and one computed from the numbers should always be shown side by side, because the difference is the conversation; and stopping a low-priority project that is red is a good outcome, not a failure.""",
 es="""
Un proyecto de captura de documentos figura en verde según su jefe de proyecto mientras cada euro que gasta compra 78 céntimos del trabajo previsto y su hito de construcción va seis semanas tarde. Así lo detecta la revisión de salud de la cartera de proyectos de IT que acompaña a este post, una semana antes del comité de seguimiento. Es un proyecto de código abierto que se ejecuta con datos de ejemplo de una aseguradora inventada, con tres programas y dieciocho proyectos en cascada, ágiles y SAFe, revisada el 10 de noviembre con los problemas puestos a propósito.

Esos 78 céntimos son el CPI, el índice de rendimiento del coste, y la herramienta lo calcula con una versión del valor ganado sencilla a propósito. El trabajo hecho vale el presupuesto por el % completado, o los puntos de historia hechos sobre el total en los proyectos ágiles. El trabajo previsto a día de hoy es el presupuesto por la parte del plazo que ya ha pasado, en línea recta. El CPI y su equivalente para el plazo, el SPI, salen de esos dos números, y el presupuesto dividido por el CPI dice dónde acaba el coste si lo que queda cuesta lo mismo que lo hecho.

## Cinco proyectos en rojo y uno que solo es verde por fuera

En conjunto, la cartera de la demo está en rojo: 5 proyectos en rojo, 6 en ámbar y 7 en verde. Uno de ellos es lo que la herramienta llama un proyecto «sandía», verde por fuera y rojo por dentro, y la suma de todas las previsiones supera en un 6 % el presupuesto aprobado. La revisión muestra su VERDE, ÁMBAR o ROJO calculado, con el motivo, al lado del semáforo que puso el jefe de proyecto, por proyecto, por programa y en total.

El semáforo de un proyecto es su peor hallazgo en cada dimensión, y un programa está en rojo cuando lo está uno de sus proyectos críticos o un tercio de sus proyectos. Los umbrales están en un fichero de configuración pactado con el comité, y cada hallazgo tiene una gravedad, un responsable y una fecha.

## Un arquitecto al 180 % y una puesta en producción en plena congelación

El arquitecto empresarial está planificado al 180 % entre tres proyectos críticos, así que los tres se retrasarán a la vez. La herramienta cuenta a una persona sobreasignada como ámbar en cada uno de esos proyectos, porque es un problema de la cartera y no de un solo proyecto.

El resto de hallazgos son de los que no se ven en unas diapositivas. El despliegue de Windows 11 lleva cinco semanas sin actualizar su estado. Un corte de red está planificado en plena congelación de cambios de fin de año, y otro proyecto sale a producción el viernes con su cambio todavía esperando al CAB, el comité de cambios. Un proyecto de automatización cuenta con un beneficio anual que nadie del negocio tiene a su cargo. El rediseño de la intranet, de prioridad baja, va tres meses tarde y un cuarto por encima del presupuesto, y nadie ha preguntado si debe seguir. Un portal ágil no deja de añadir alcance mientras su velocidad cae, y tres elementos del registro RAID, donde se apuntan riesgos y problemas, están vencidos y sin responsable.

## Ocho decisiones para el comité, cada una con sus opciones

La revisión convierte los hallazgos en 8 decisiones para el comité, en un orden fijo: primero la diferencia con el presupuesto aprobado, después los proyectos en rojo y de prioridad baja que se podrían pausar o parar, los proyectos sandía, el resto de proyectos en rojo, las personas clave, las entregas dentro de una congelación y los beneficios sin responsable. Cada decisión lleva sus opciones (seguir, replanificar, pausar o parar), una propuesta, el impacto y un responsable. El objetivo es que el comité dedique su hora a decidir y no a repasar estados.

## Cómo usarlo con datos reales

Los datos de entrada son la lista de proyectos de la herramienta de PPM, los hitos, el registro RAID, el plan de recursos, las entregas y el histórico de sprints de Jira o Azure DevOps. Un exportador de solo lectura toma los sprints cerrados de un tablero de Jira Cloud con la búsqueda de incidencias actual, o las iteraciones pasadas de un equipo de Azure DevOps con una consulta WIQL, con un token que se queda en memoria, y escribe los puntos comprometidos, completados y añadidos en cada sprint.

La herramienta funciona con Python y solo la librería estándar, y genera `report.html`, con un mapa de calor de la cartera, una ficha por proyecto, un gráfico de coste y plazo y la carga de recursos; `steerco-pack.md`, una página para el comité; y ficheros CSV con la salud de cada proyecto, los hallazgos, la carga de recursos, las decisiones y las acciones. Incluye 14 tests y un runbook para el comité mensual: qué enviar antes, el orden del día, cómo plantear las decisiones, cómo tratar los proyectos sandía sin buscar culpables y cómo seguir las acciones. La idea es ejecutarla una semana antes de cada comité, y cada semana para los proyectos en rojo.

## De dónde sale

La hice a partir de gestionar una cartera de iniciativas, trabajar como Scrum Master y Product Owner con SAFe y el PI Planning, redactar casos de negocio con ROI y participar en la gestión de entregas y el comité de cambios. Detrás hay dos lecciones: el semáforo que alguien escribe y el que sale de los números hay que enseñarlos siempre juntos, porque la diferencia es la conversación; y parar un proyecto en rojo y de prioridad baja es un buen resultado, no un fracaso."""),
dict(n="50", repo="50-saas-licence-spend-review", date="2026-11-11", cat="tools",
 title_en="A licence review finds EUR 223.7k of savings, starting with 180 people on E5 who use nothing beyond E3",
 title_es="Una revisión de licencias halla 223.700 euros de ahorro, empezando por 180 personas con E5 que no usan más que E3",
 seo_title_en="SaaS and licence spend review · Iñigo González",
 seo_title_es="Revisión del gasto en SaaS y licencias · Iñigo González",
 seo_desc="SaaS and licence spend review: unused and leaver licences, E5 to E3, shelfware, notice deadlines, uplifts, overlap, shadow IT and savings per action.",
 seo_desc_es="Revisión del gasto en SaaS y licencias: licencias sin uso o de bajas, E5 a E3, asientos sobrantes, preavisos, subidas, solapes, shadow IT y ahorro por acción.",
 dek_en="The monthly SaaS and licence review, published with fictional data from a distribution company with 1,370 employees and 24 apps, cross-checks the licence register, each user's last activity, the HR or Entra ID user list and card expenses to price every saving before its notice deadline.",
 dek_es="La revisión mensual de SaaS y licencias, publicada con datos ficticios de una distribuidora con 1.370 empleados y 24 aplicaciones, cruza el registro de licencias, la última actividad de cada usuario, la lista de RR. HH. o de Entra ID y los gastos con tarjeta para valorar cada ahorro antes de su preaviso.",
 en="""
180 people have Microsoft 365 E5 and use nothing that E3, the cheaper plan, does not already give them, and the price difference is the first saving on the list. In all, the SaaS and licence spend review published with this post identifies EUR 223.7k of savings, 15.4 % of a bill of EUR 1.45M a year. It is an open-source tool that runs on demo data from a made-up distribution company with 1,370 employees in four countries and 24 apps, reviewed on 11 November with the problems placed on purpose.

Software and SaaS spend grows one reasonable request at a time, and licences are almost never taken back. The data to see where the money goes exists, in the register, the admin consoles, Entra ID, HR and the expense tool, but it is rarely read together until a renewal arrives. The review reads it every month and ties every saving to one action: reclaim, downgrade, right-size, negotiate, consolidate or cancel, with the users behind it, an owner and a due date.

## 46 licences on people who left and a deadline in nine days

The demo finds 46 licences still assigned to people who left months ago, which is a cost and an open door. A third of the Adobe Creative Cloud licences have not been opened for three months. The e-signature contract renews automatically with a third of its seats unassigned and nine days left to give notice, and the CRM comes back with a 9 % uplift against a 5 % cap.

For the tool, the date that matters is the notice deadline, the renewal date minus the notice period, not the renewal itself. An auto-renewing contract whose renewal date has passed rolls forward a year at a time, and the review keeps a renewal calendar for the next twelve months.

## Two video tools next to Teams and five apps paid on cards

The review also looks at the portfolio as a whole. The company pays for Zoom and Webex while everyone has Teams, and for Dropbox and Box next to OneDrive, so they come up as consolidation candidates. The whiteboard tool has more people than seats, and the true-up, the adjustment the vendor bills for the extra users, will come at list price. Nobody owns one contract that holds confidential data without single sign-on, and people pay for Canva, Notion, ChatGPT Plus, Calendly and Grammarly on their cards, which is shadow IT: software bought outside the register.

The cost is also shown per department and cost centre, a practice known as showback. Each per-user licence is charged to the department of the person who holds it, while empty seats and flat contracts stay with IT, so the rows add up to the total.

## Every euro counted once

So that finance can trust the total, the savings are applied per app in a fixed order, reclaim, downgrade, right-size, negotiate, cancel duplicates and then consolidate, and capped at what the app costs. Exiting a video tool therefore only counts what is left of its cost after its inactive licences and empty seats have been removed. The thresholds sit in a settings file agreed with finance, and each finding has a severity, an owner and a due date.

## How to use it with real data

The inputs are the licence and SaaS register, the licence assignments with each user's last activity, the HR or Entra ID user list and the card expenses. A read-only exporter reads from Microsoft Graph the SKUs the tenant has bought with their seats and the users with their licences and their last successful sign-in, with an app registration and a secret that stays in memory. The last sign-in shows that the account is in use, not that a particular app is, so the reclaim list goes to the app owner before anything is removed.

The tool runs on Python with the standard library only and produces `report.html`, with utilisation bars per app, the renewal calendar and the showback; `review-pack.md`, one page with the decisions before the renewals for the IT manager and finance; and CSV files for utilisation, the reclaim list, the calendar, showback, findings and actions. It comes with 15 tests and a runbook for the monthly reclaim cycle, the steps 120, 90 and 60 days before a renewal, how to negotiate with usage data and how to handle shadow IT without blocking people.

## Where it comes from

I built it from software asset management and licence cost control with Apptio and Flexera, administering Microsoft 365 as Global Administrator and managing Office 365 and Adobe licences, and negotiating vendor contracts. Two lessons are behind it: the same euro must not appear in two savings, or finance stops believing the total; and shadow IT is usually a need IT did not meet, so talking to the people who buy it works better than blocking the card.""",
 es="""
180 personas tienen Microsoft 365 E5 y no usan nada que no les dé ya E3, el plan más barato, y la diferencia de precio es el primer ahorro de la lista. En total, la revisión del gasto en SaaS y licencias que acompaña a este post identifica 223.700 euros de ahorro, un 15,4 % de una factura de 1,45 millones de euros al año. Es un proyecto de código abierto que se ejecuta con datos de ejemplo de una empresa de distribución inventada, con 1.370 empleados en cuatro países y 24 aplicaciones, revisada el 11 de noviembre con los problemas puestos a propósito.

El gasto en software y SaaS crece petición razonable a petición razonable, y las licencias casi nunca se recuperan. Los datos para ver a dónde va el dinero existen, en el registro, las consolas de administración, Entra ID, RR. HH. y la herramienta de gastos, pero pocas veces se leen juntos hasta que llega una renovación. La revisión los lee cada mes y une cada ahorro a una acción: recuperar, bajar de plan, ajustar asientos, negociar, consolidar o cancelar, con los usuarios que hay detrás, un responsable y una fecha.

## 46 licencias de gente que ya no está y un preaviso en nueve días

La demo encuentra 46 licencias que siguen asignadas a personas que se fueron hace meses, lo que es un coste y una puerta abierta. Un tercio de las licencias de Adobe Creative Cloud llevan tres meses sin abrirse. El contrato de firma electrónica se renueva solo con un tercio de los asientos sin asignar y nueve días para avisar, y el CRM vuelve con una subida del 9 % frente a un tope del 5 %.

Para la herramienta, la fecha que importa es la del preaviso, la de renovación menos el plazo de preaviso, no la renovación en sí. Un contrato con renovación automática cuya fecha ya ha pasado avanza un año cada vez, y la revisión mantiene un calendario de renovaciones de los próximos doce meses.

## Dos herramientas de videollamada junto a Teams y cinco aplicaciones pagadas con tarjeta

La revisión también mira la cartera en conjunto. La empresa paga Zoom y Webex cuando todo el mundo tiene Teams, y Dropbox y Box al lado de OneDrive, así que aparecen como candidatas a consolidar. La pizarra colaborativa tiene más personas que asientos, y el ajuste, lo que el fabricante cobra por los usuarios de más, llegará a precio de tarifa. Nadie es responsable de un contrato que guarda datos confidenciales sin inicio de sesión único, y hay gente que paga Canva, Notion, ChatGPT Plus, Calendly y Grammarly con su tarjeta: es el shadow IT, el software que se compra fuera del registro.

El coste se reparte además por departamento y centro de coste, lo que se conoce como showback. Cada licencia por usuario se carga al departamento de la persona que la tiene, y los asientos vacíos y los contratos de tarifa plana se quedan en IT, así que las filas suman el total.

## Cada euro se cuenta una sola vez

Para que finanzas pueda fiarse del total, los ahorros se aplican por aplicación en un orden fijo, recuperar, bajar de plan, ajustar asientos, negociar, cancelar duplicados y por último consolidar, con el coste de la aplicación como tope. Dejar una herramienta de videollamadas solo cuenta, por tanto, lo que queda de su coste después de quitar sus licencias sin uso y sus asientos vacíos. Los umbrales están en un fichero de configuración pactado con finanzas, y cada hallazgo tiene una gravedad, un responsable y una fecha.

## Cómo usarlo con datos reales

Los datos de entrada son el registro de licencias y SaaS, las licencias asignadas con la última actividad de cada usuario, la lista de usuarios de RR. HH. o de Entra ID y los gastos con tarjeta. Un exportador de solo lectura lee de Microsoft Graph los SKU que ha comprado el tenant con sus asientos y los usuarios con sus licencias y su último inicio de sesión correcto, con un registro de aplicación y un secreto que se queda en memoria. El último inicio de sesión dice que la cuenta se usa, no que se use una aplicación concreta, así que la lista de licencias a recuperar pasa por el responsable de la aplicación antes de quitar nada.

La herramienta funciona con Python y solo la librería estándar, y genera `report.html`, con barras de uso por aplicación, el calendario de renovaciones y el reparto por departamento; `review-pack.md`, una página con las decisiones antes de las renovaciones para el responsable de IT y finanzas; y ficheros CSV con el uso, la lista de licencias a recuperar, el calendario, el reparto, los hallazgos y las acciones. Incluye 15 tests y un runbook para el ciclo mensual de recuperación, los pasos 120, 90 y 60 días antes de una renovación, cómo negociar con los datos de uso y cómo tratar el shadow IT sin bloquear a la gente.

## De dónde sale

La hice a partir de la gestión de activos de software y el control de costes de licencias con Apptio y Flexera, de administrar Microsoft 365 como administrador global y gestionar las licencias de Office 365 y de Adobe, y de negociar contratos con proveedores. Detrás hay dos lecciones: el mismo euro no puede aparecer en dos ahorros, o finanzas deja de creerse el total; y el shadow IT suele ser una necesidad que IT no cubrió, así que hablar con quien lo paga funciona mejor que bloquear la tarjeta."""),
dict(n="51", repo="51-windows-server-baseline-drift", date="2026-11-12", cat="tools",
 title_en="One GPO not linked to a new OU explains 112 of the 138 settings that drifted on Windows servers in a month",
 title_es="Una GPO sin vincular a una OU nueva explica 112 de los 138 ajustes desviados en los servidores Windows en un mes",
 seo_title_en="Windows Server baseline drift review · Iñigo González",
 seo_title_es="Deriva de la línea base de Windows Server · Iñigo González",
 seo_desc="Windows Server security baseline review: compliance per server and tier, high-risk deviations, drift since last month, GPOs not applied and exceptions.",
 seo_desc_es="Revisión de la línea base de seguridad de Windows Server: cumplimiento por servidor, desviaciones de alto riesgo, deriva, GPO que no se aplican y excepciones.",
 dek_en="The monthly baseline review, published with fictional data from an aerospace manufacturer with 56 servers, compares each server's settings with the approved security baseline, last month's state, the exceptions and the Group Policy results to explain why it drifted.",
 dek_es="La revisión mensual de la línea base, publicada con datos ficticios de un fabricante aeroespacial con 56 servidores, compara la configuración de cada servidor con la línea base de seguridad aprobada, el mes anterior, las excepciones y las directivas de grupo para explicar por qué se ha desviado.",
 en="""
Of the 138 security settings that drifted on a company's Windows servers in one month, 112 have a single cause: a group of servers moved to a new OU for a project, and the GPO that applies the baseline was never linked there. That is what the Windows Server baseline review published with this post finds. It is an open-source tool that runs on demo data from a made-up aerospace manufacturer with two sites, 56 servers and a 45-setting baseline, reviewed on 12 November with the problems placed on purpose.

A security baseline is the approved list of how every server should be configured, and a GPO, a Group Policy Object, is how Active Directory pushes those settings to the servers in an OU, an organisational unit. On the servers that lost the GPO, LLMNR, NTLM, TLS 1.0 and RDP fell back to their defaults without anyone noticing. The review gives each deviation the first cause that applies, from the Group Policy results, the exceptions and where the value came from, so the GPO comes first in the report rather than 112 separate lines.

## Compliance falls from 98.8 % to 92.4 %

The demo estate is red: 92.4 % compliance against 98.8 % a month earlier, and 79 high-risk deviations on 41 servers. Compliance is measured on every applicable setting of every server, by tier and role, and shown per server, area, tier, site and environment against a target per tier. Last month's collection is evaluated with the same rules, which is how the tool tells what is new.

High-risk deviations come first in the list: SMBv1, LM and NTLMv1, LLMNR, RDP without NLA, LAPS, Defender real-time protection, ASR rules left in audit where block is expected, logon and lockout auditing, PowerShell script block logging, the Print Spooler on domain controllers, TLS 1.0 and 1.1, and firewall profiles.

## SMBv1 back on the file servers and a pilot that never ended

The other causes are the ones a baseline drifts through, one reasonable change at a time. A scanner integration needed SMBv1, the old file-sharing protocol, and someone turned it back on locally on the file servers. The new servers are not in the LAPS group, the tool that rotates the local administrator password. A test GPO turns LLMNR back on so the tests work, and the Print Spooler ended up on automatic on a domain controller after an incident.

An ASR pilot has left two rules in audit for months. An exception for TLS 1.0 has expired while the old application is still there, and a GPO link disabled during troubleshooting switches off PowerShell logging for a whole site. Some servers have also stopped reporting, and the review lists them as unknown rather than compliant.

## A decision for each deviation

An approved and valid exception counts as compliant; one without an approver, a ticket or an expiry does not, and expired or expiring ones come back as findings. Each high-risk item gets an owner and a date, and every deviation needs one of three decisions: fix it, accept it as an exception or change the baseline. The one-page pack for the monthly security and infrastructure review carries those decisions and the evidence for ISO 27001 and NIS2 audits.

## How to use it with real data

The baseline is a CSV with one row per setting: what to read (a registry value, an audit subcategory, a service, a firewall profile, the SMB configuration, Defender, an ASR rule, a user right or the LAPS attribute in AD), the expected value, the severity, the tiers it applies to, the GPO that should set it and its ISO 27001 reference. A PowerShell collector opens one remoting session per server and only reads, with commands such as Get-ItemProperty, auditpol, Get-SmbServerConfiguration, Get-MpPreference and Get-GPResultantSetOfPolicy; credentials come from the session and stay in memory.

The analysis runs on Python with the standard library only and produces `report.html`, with a heat map of servers by area, the top deviations and the trend; `review-pack.md`; and CSV files per server, deviation, drift, exception, finding and action. It comes with 14 tests and a runbook for the monthly cycle, which includes piloting a baseline change in audit mode first. The intended rhythm is the first working day of every month and after every change to a baseline GPO.

## Where it comes from

I built it from administering Windows Server, Active Directory and Group Policy since early in my career, patching servers without cutting the service, and applied work with ISO 27001 and NIS2. Two lessons are behind it: one GPO that stops applying explains more deviations than all the local changes together, so the cause comes before the list of settings; and an auditor trusts a report more when it shows its own gaps.""",
 es="""
De los 138 ajustes de seguridad que se desviaron en un mes en los servidores Windows de una empresa, 112 tienen una sola causa: un grupo de servidores pasó a una OU nueva por un proyecto y la GPO que aplica la línea base nunca se vinculó allí. Así lo detecta la revisión de la línea base de Windows Server que acompaña a este post, un proyecto de código abierto que se ejecuta con datos de ejemplo de un fabricante aeroespacial inventado, con dos sedes, 56 servidores y una línea base de 45 ajustes, revisado el 12 de noviembre con los problemas puestos a propósito.

Una línea base de seguridad es la lista aprobada de cómo debe estar configurado cada servidor, y una GPO, un objeto de directiva de grupo, es la forma en que Active Directory lleva esos ajustes a los servidores de una OU, una unidad organizativa. En los servidores que se quedaron sin la GPO, LLMNR, NTLM, TLS 1.0 y RDP volvieron a sus valores por defecto sin que nadie se diera cuenta. La revisión asigna a cada desviación la primera causa que encaja, a partir de los resultados de las directivas, las excepciones y el origen del valor, así que la GPO aparece primero en el informe en lugar de 112 líneas sueltas.

## El cumplimiento cae del 98,8 % al 92,4 %

El parque de la demo está en rojo: un 92,4 % de cumplimiento frente al 98,8 % de hace un mes, y 79 desviaciones de alto riesgo en 41 servidores. El cumplimiento se mide sobre cada ajuste que aplica en cada servidor, por nivel y rol, y se enseña por servidor, área, nivel, sede y entorno frente a un objetivo por nivel. La recogida del mes anterior se evalúa con las mismas reglas, y así la herramienta distingue lo que es nuevo.

Las desviaciones de alto riesgo van primero: SMBv1, LM y NTLMv1, LLMNR, RDP sin NLA, LAPS, la protección en tiempo real de Defender, reglas ASR en auditoría donde deberían bloquear, la auditoría de inicios de sesión y bloqueos, el registro de bloques de script de PowerShell, la cola de impresión en los controladores de dominio, TLS 1.0 y 1.1, y los perfiles del firewall.

## SMBv1 activo otra vez en los servidores de ficheros y un piloto que nunca terminó

El resto de causas son las de siempre, cambio razonable a cambio razonable. Una integración con un escáner necesitaba SMBv1, el antiguo protocolo para compartir ficheros, y alguien lo volvió a activar a mano en los servidores de ficheros. Los servidores nuevos no están en el grupo de LAPS, la herramienta que rota la contraseña del administrador local. Una GPO de pruebas vuelve a activar LLMNR «para que funcionen las pruebas», y la cola de impresión acabó en automático en un controlador de dominio después de una incidencia.

Un piloto de ASR ha dejado dos reglas en auditoría durante meses. Una excepción para TLS 1.0 ha caducado y la aplicación antigua sigue ahí, y un vínculo de GPO desactivado mientras se investigaba un problema apaga el registro de PowerShell en toda una sede. Además, algunos servidores han dejado de reportar, y la revisión los marca como desconocidos, no como conformes.

## Una decisión para cada desviación

Una excepción aprobada y en vigor cuenta como cumplimiento; una sin aprobador, ticket o fecha de caducidad no, y las caducadas o a punto de caducar vuelven como hallazgos. Cada punto de alto riesgo tiene responsable y fecha, y cada desviación necesita una de tres decisiones: corregirla, aceptarla como excepción o cambiar la línea base. El dosier de una página para la revisión mensual de seguridad e infraestructura recoge esas decisiones y las evidencias para las auditorías de ISO 27001 y NIS2.

## Cómo usarlo con datos reales

La línea base es un CSV con una fila por ajuste: qué leer (un valor del registro, una subcategoría de auditoría, un servicio, un perfil del firewall, la configuración SMB, Defender, una regla ASR, un derecho de usuario o el atributo de LAPS en AD), el valor esperado, la gravedad, los niveles a los que aplica, la GPO que debería fijarlo y su referencia a ISO 27001. Un recolector de PowerShell abre una sesión remota por servidor y solo lee, con comandos como Get-ItemProperty, auditpol, Get-SmbServerConfiguration, Get-MpPreference y Get-GPResultantSetOfPolicy; las credenciales salen de la sesión y se quedan en memoria.

El análisis funciona con Python y solo la librería estándar, y genera `report.html`, con un mapa de calor de servidores por área, las desviaciones principales y la tendencia; `review-pack.md`; y ficheros CSV por servidor, desviación, deriva, excepción, hallazgo y acción. Incluye 14 tests y un runbook para el ciclo mensual, que contempla pilotar cada cambio de la línea base empezando en modo auditoría. La idea es ejecutarlo el primer día laborable de cada mes y después de cada cambio en una GPO de la línea base.

## De dónde sale

La hice a partir de administrar Windows Server, Active Directory y las directivas de grupo desde el principio de mi carrera, parchear servidores sin cortar el servicio y el trabajo aplicado con ISO 27001 y NIS2. Detrás hay dos lecciones: una GPO que deja de aplicarse explica más desviaciones que todos los cambios locales juntos, así que la causa va antes que la lista de ajustes; y un auditor se fía más de un informe que enseña sus propias lagunas."""),
dict(n="52", repo="52-endpoint-security-coverage", date="2026-11-13", updated="2026-11-21", cat="tools",
 title_en="Only 76.9 % of laptops and desktops are fully protected, and the gaps sit between Intune, Defender and the CMDB",
 title_es="Solo el 76,9 % de los equipos está protegido del todo, y los huecos están entre Intune, Defender y la CMDB",
 seo_title_en="Endpoint security: Intune, Defender, BitLocker · Iñigo González",
 seo_title_es="Cobertura de seguridad de los equipos: Intune, Defender y BitLocker · Iñigo González",
 seo_desc="Monthly endpoint security review: inventory, Intune and Defender reconciled, BitLocker keys, EDR health, local admins, EPM elevations and unsupported OS.",
 seo_desc_es="Revisión mensual de seguridad de los equipos: inventario, Intune y Defender cruzados, claves de BitLocker, EDR, administradores locales, EPM y sistemas sin soporte.",
 dek_en="The monthly endpoint review, published with fictional data from a drone and avionics parts maker with 368 devices, matches the asset inventory, Intune and Defender device by device and checks encryption keys, local admins, elevations and operating systems.",
 dek_es="La revisión mensual de los equipos, publicada con datos ficticios de un fabricante de piezas para drones y aviónica con 368 dispositivos, cruza equipo a equipo el inventario, Intune y Defender y revisa las claves de cifrado, los administradores locales, las elevaciones y los sistemas.",
 en="""
Only 76.9 % of a company's laptops and desktops are fully protected, against 93.2 % a month earlier, and the gaps sit between the tools rather than inside any of them. That is what the endpoint security coverage review published with this post finds. It is an open-source tool that runs on demo data from a made-up maker of drone and avionics parts with two sites and 368 devices in use, reviewed on 13 November with the problems placed on purpose.

Every security tool shows its own view, and each looks fine on its own. Intune shows compliance for the devices it manages, Defender shows sensor health for the devices that are onboarded, and the CMDB, the asset database, shows what was bought. The review starts from the inventory and matches Intune records to it by serial number and then name, and Defender records by Entra device ID and then name, so one physical device is one row whatever each tool calls it.

## 11 devices no tool manages and 25 without a working sensor

The demo is red. 11 devices are not managed, 25 have no working EDR sensor, the endpoint detection and response agent that watches for attacks, 14 have standing local administrators and 11 run an unsupported operating system. A field team built a few laptops locally to save time and they never reached Intune or Defender, and new workstations were enrolled but their group is not in the onboarding policy.

Findings are grouped by cause, so six workstations missing from Defender appear as one problem with one owner. The same reconciliation also shows devices the inventory does not have and retired laptops that still check in.

## Encrypted laptops whose key the service desk cannot find

Every device is checked control by control: managed, compliant, checking in, encrypted, recovery key escrowed, EDR onboarded and healthy, antivirus healthy, no standing local administrators and a supported operating system. A firmware update suspended BitLocker and nobody resumed it. Laptops imaged by an old process are encrypted, but their recovery key is not in Entra ID, so the service desk cannot unlock them.

A vendor asked to turn off the antivirus on two CAD workstations and it stayed off. Windows 10 lingers on the production floor after its end of support. Each control gives pass, fail, exception or unknown, and a device missing from the local admin report counts as unknown, not covered, with the report saying how many.

## An installer approved 37 times and admin rights "for a week"

On privilege, a software rollout added engineers to the local Administrators group for a week. The service desk approves the same installer dozens of times a month through Endpoint Privilege Management, the Intune feature that lets users run one file with admin rights after approval, and the review flags such files as candidates for an automatic rule. An unsigned lab tool is elevated on a test bench.

The gaps that need a choice, an unsupported OS, standing admin rights, an automatic elevation rule, unmanaged devices or an expired exception, become decisions; the demo has five. Valid exceptions, with an approver, a ticket and an expiry, count as covered, and the one-page pack carries the evidence for ISO 27001 and NIS2 audits.

## How to use it with real data

A read-only PowerShell collector reads the Intune managed devices and the antivirus state of each Windows device through Microsoft Graph, and the BitLocker recovery key metadata in Entra ID, never the key itself. Defender data comes from the portal's device export, and the local administrators from an Intune Remediations detection script that changes nothing.

The analysis runs on Python with the standard library only and produces `report.html`, with coverage per control, a heat map of departments by control and the three sources reconciled; `review-pack.md`, one page for the monthly endpoint security review; and CSV files per device, gap, source, elevation, exception, finding and action. It comes with 15 tests and a runbook for the monthly cycle and for rolling out policy changes without breaking users. The intended rhythm is the first working day of every month and after every change to the onboarding, encryption or account protection policies.

## Where it comes from

I built it from managing Windows, macOS, iOS and Android devices with Intune, BitLocker encryption and compliance, leading a migration to Windows 11, and working with Endpoint Privilege Management, Defender and Entra ID. Two lessons are behind it: the most dangerous device is the one no tool knows about, so the reconciliation comes before any percentage; and an installer approved by hand dozens of times a month is a rule nobody has written yet.""",
 es="""
Solo el 76,9 % de los portátiles y sobremesas de una empresa está protegido del todo, frente al 93,2 % de hace un mes, y los huecos están entre las herramientas y no dentro de ninguna. Así lo detecta la revisión de cobertura de seguridad de los equipos que acompaña a este post, un proyecto de código abierto que se ejecuta con datos de ejemplo de un fabricante inventado de piezas para drones y aviónica, con dos sedes y 368 dispositivos en uso, revisado el 13 de noviembre con los problemas puestos a propósito.

Cada herramienta de seguridad enseña su propia vista, y cada una parece correcta por separado. Intune enseña el cumplimiento de los equipos que gestiona, Defender la salud del sensor de los equipos incorporados, y la CMDB, la base de datos de activos, lo que se compró. La revisión parte del inventario y le une los registros de Intune por número de serie y luego por nombre, y los de Defender por el identificador de dispositivo de Entra y luego por nombre, así que un equipo físico es una fila se llame como se llame en cada herramienta.

## 11 equipos sin gestionar y 25 sin un sensor que funcione

La demo está en rojo. 11 equipos no están gestionados, 25 no tienen un sensor EDR que funcione, el agente de detección y respuesta que vigila los ataques, 14 tienen administradores locales permanentes y 11 usan un sistema operativo sin soporte. Un equipo de campo montó unos cuantos portátiles en local para ganar tiempo y nunca llegaron a Intune ni a Defender, y unas estaciones de trabajo nuevas se inscribieron, pero su grupo no está en la directiva de incorporación.

Los hallazgos se agrupan por causa, así que seis estaciones de trabajo que faltan en Defender aparecen como un solo problema con un solo responsable. El mismo cruce enseña también los equipos que el inventario no tiene y los portátiles retirados que siguen conectándose.

## Portátiles cifrados cuya clave el service desk no encuentra

Cada equipo se revisa control a control: gestionado, conforme, reportando, cifrado, clave de recuperación guardada, EDR incorporado y sano, antivirus sano, sin administradores locales permanentes y con un sistema operativo con soporte. Una actualización de firmware suspendió BitLocker y nadie lo reanudó. Los portátiles instalados con un proceso antiguo están cifrados, pero su clave de recuperación no está en Entra ID, así que el service desk no puede desbloquearlos.

Un proveedor pidió desactivar el antivirus en dos estaciones de CAD y se quedó desactivado. Windows 10 sigue en la planta de producción después del fin de su soporte. Cada control da cumple, no cumple, excepción o desconocido, y un equipo que falta en el informe de administradores locales cuenta como desconocido, no como cubierto, y el informe dice cuántos son.

## Un instalador aprobado 37 veces y permisos de administrador «para una semana»

En privilegios, un despliegue de software añadió a varios ingenieros al grupo de administradores locales para una semana. El service desk aprueba el mismo instalador decenas de veces al mes con Endpoint Privilege Management, la función de Intune que deja a un usuario ejecutar un fichero con permisos de administrador tras una aprobación, y la revisión marca esos ficheros como candidatos a una regla automática. Una herramienta de laboratorio sin firmar se eleva en un banco de pruebas.

Los huecos que necesitan una elección, un sistema sin soporte, permisos de administrador permanentes, una regla de elevación automática, equipos sin gestionar o una excepción caducada, se convierten en decisiones; la demo tiene cinco. Las excepciones válidas, con aprobador, ticket y caducidad, cuentan como cubiertas, y el dosier de una página recoge las evidencias para las auditorías de ISO 27001 y NIS2.

## Cómo usarlo con datos reales

Un recolector de PowerShell de solo lectura lee con Microsoft Graph los dispositivos gestionados de Intune y el estado del antivirus de cada equipo Windows, y los metadatos de las claves de recuperación de BitLocker en Entra ID, nunca la clave. Los datos de Defender salen de la exportación de dispositivos del portal, y los administradores locales de un script de detección de Intune Remediations que no cambia nada.

El análisis funciona con Python y solo la librería estándar, y genera `report.html`, con la cobertura por control, un mapa de calor de departamentos por control y las tres fuentes cruzadas; `review-pack.md`, una página para la revisión mensual de seguridad de los equipos; y ficheros CSV por equipo, hueco, fuente, elevación, excepción, hallazgo y acción. Incluye 15 tests y un runbook para el ciclo mensual y para desplegar cambios de directivas sin romper nada a los usuarios. La idea es ejecutarlo el primer día laborable de cada mes y después de cada cambio en las directivas de incorporación, cifrado o protección de cuentas.

## De dónde sale

La hice a partir de gestionar equipos Windows, macOS, iOS y Android con Intune, el cifrado con BitLocker y el cumplimiento, dirigir una migración a Windows 11 y trabajar con Endpoint Privilege Management, Defender y Entra ID. Detrás hay dos lecciones: el equipo más peligroso es el que ninguna herramienta conoce, así que el cruce va antes que cualquier porcentaje; y un instalador que se aprueba a mano decenas de veces al mes es una regla que nadie ha escrito todavía."""),
dict(n="53", repo="53-dns-dhcp-ipam-review", date="2026-11-14", cat="tools",
 title_en="An eight-day lease leaves a guest Wi-Fi at 94 %, and a retired domain controller is still handed out in five scopes",
 title_es="Una concesión de ocho días deja la wifi de invitados al 94 %, y cinco ámbitos aún reparten un controlador retirado",
 seo_title_en="DNS, DHCP and IPAM review on Windows Server · Iñigo González",
 seo_title_es="DNS, DHCP e IPAM en Windows Server: revisión · Iñigo González",
 seo_desc="Monthly Windows Server DNS and DHCP review: scopes filling up, failover, stale and static records, rogue DHCP, insecure zones and the IP plan.",
 seo_desc_es="Revisión mensual de DNS y DHCP en Windows Server: ámbitos que se llenan, conmutación, registros antiguos, DHCP no autorizado, zonas inseguras y el plan IP.",
 dek_en="The monthly DNS and DHCP review, published with fictional data from a toy retailer with 19 scopes and 3,487 records, cross-checks scopes, leases, failover, zones, records and the IP address plan to see which pools fill up first and what still points to old servers.",
 dek_es="La revisión mensual de DNS y DHCP, publicada con datos ficticios de una juguetera con 19 ámbitos y 3.487 registros, cruza ámbitos, concesiones, conmutación, zonas, registros y el plan de direccionamiento IP para ver qué pools se llenan antes y qué apunta aún a servidores antiguos.",
 en="""
The guest Wi-Fi of a retailer is at 94 % of its addresses because it still keeps the default eight-day lease, so by the second week of a busy month visitors cannot connect. That is what the DNS, DHCP and IPAM review published with this post finds. It is an open-source tool that runs on demo data from a made-up toy retailer with a head office, a distribution centre and two offices, 19 scopes and 3,487 records, reviewed on 14 November with the problems placed on purpose.

A lease is how long a device keeps the address DHCP gives it, and a scope is the pool of addresses for one subnet. On a guest network, each visitor's address stays taken for eight days after they leave. The review checks lease lengths against the standard for guest, Wi-Fi and user subnets, and treats the choice between a shorter lease and a wider subnet as a decision for the infrastructure review.

## Handheld scanners will fill their scope in about 26 days

The tool ranks scopes by pace rather than percentage. The growth since the last review gives the days until each pool is full, so a scope at 79 % that grew by 120 devices in a month comes up before one at 81 % that barely moves. In the demo, a batch of new handheld scanners arrived for the peak season, and their scope will be full in about 26 days, before Christmas.

Overall the demo is red, with a broken failover relationship, a rogue router, 735 stale records and five decisions. The link to one site dropped after a firewall change and the failover partners, the two DHCP servers that share a scope, stopped replicating leases. Someone plugged a consumer router into the showroom for a launch event, and the review flags it as a rogue DHCP server.

## A domain controller retired in September is still in five scopes

A domain controller was retired, but five scopes still hand it out as a DNS server and six records still point to it, including its SRV records. It was also the only server that scavenged, the job that deletes stale records. The tool checks option 006, the DNS servers each scope hands out, against the live servers, and looks for the retired server in A, NS, SRV and PTR records.

The DNS checks also find a zone a vendor set to accept nonsecure updates, which lets any device overwrite a name, and printers a technician gave static addresses in the middle of a pool. A static record is only flagged when its address is inside an active pool and is not a reservation. A scope created during an outage is still active on another server, and the IP address plan says one thing while the scopes say another.

## How to use it with real data

The export only reads, with the standard DhcpServer and DnsServer PowerShell cmdlets: scopes, options, reservations and leases per server, and zones and records. A scope in a failover relationship is exported once, so its statistics are not counted twice. The IP plan is compared with both, to find scopes not in the plan, planned subnets with no scope, overlapping subnets and subnets with no owner or reverse lookup zone.

Every finding has a severity, an owner and a due date, and valid exceptions remove the item while expired or incomplete ones do not. The analysis runs on Python with the standard library only and produces `report.html`, with every scope, its growth and its days to full; `review-pack.md`, one page with the decisions and the evidence for ISO 27001 and NIS2 audits; and CSV files per scope, reservation, zone, stale record, subnet, exception, finding and action. It comes with 13 tests and a runbook for changing leases, scopes, secure updates and scavenging without surprises, and is meant to run on the first working day of every month and before and after every network change at a site.

## Where it comes from

I built it from administering Windows Server DNS and DHCP and Active Directory since early in my career, and from running Cisco switches and routers, FortiGate firewalls and multi-site networks. Two lessons are behind it: a scope's percentage matters less than its pace, because the one that fills up is the one that is growing; and retiring a domain controller is not finished until DHCP and DNS stop pointing to it.""",
 es="""
La wifi de invitados de una cadena de tiendas está al 94 % de sus direcciones porque sigue con la concesión por defecto de ocho días, así que a mitad de un mes con mucho movimiento las visitas no pueden conectarse. Así lo detecta la revisión de DNS, DHCP e IPAM que acompaña a este post, un proyecto de código abierto que se ejecuta con datos de ejemplo de una juguetera inventada con una sede central, un centro de distribución y dos oficinas, 19 ámbitos y 3.487 registros, revisada el 14 de noviembre con los problemas puestos a propósito.

Una concesión es el tiempo que un equipo conserva la dirección que le da DHCP, y un ámbito es el conjunto de direcciones de una subred. En una red de invitados, la dirección de cada visita sigue ocupada ocho días después de que se vaya. La revisión compara la duración de las concesiones con el estándar para las subredes de invitados, wifi y usuarios, y deja la elección entre una concesión más corta y una subred más amplia como decisión para la revisión de infraestructura.

## Los lectores de mano llenarán su ámbito en unos 26 días

La herramienta ordena los ámbitos por ritmo y no por porcentaje. El crecimiento desde la última revisión da los días que faltan para que cada pool se llene, así que un ámbito al 79 % que ha crecido 120 equipos en un mes sale antes que uno al 81 % que apenas se mueve. En la demo llegó un lote de lectores de mano nuevos para la campaña, y su ámbito se llenará en unos 26 días, antes de Navidad.

En conjunto la demo está en rojo, con una relación de conmutación rota, un router no autorizado, 735 registros obsoletos y cinco decisiones. El enlace con una sede cayó tras un cambio en el firewall y los dos servidores DHCP que comparten los ámbitos en conmutación dejaron de replicar las concesiones. Alguien conectó un router doméstico en la exposición para un evento de lanzamiento, y la revisión lo marca como un servidor DHCP no autorizado.

## Un controlador de dominio retirado en septiembre sigue en cinco ámbitos

Se retiró un controlador de dominio, pero cinco ámbitos lo siguen dando como servidor DNS y seis registros apuntan todavía a él, entre ellos sus registros SRV. Además era el único servidor que hacía la limpieza, la tarea que borra los registros obsoletos. La herramienta compara la opción 006, los servidores DNS que entrega cada ámbito, con los servidores que siguen en marcha, y busca el servidor retirado en los registros A, NS, SRV y PTR.

Las comprobaciones de DNS encuentran también una zona que un proveedor dejó aceptando actualizaciones no seguras, lo que permite a cualquier equipo sobrescribir un nombre, e impresoras a las que un técnico dio una dirección fija en mitad de un pool. Un registro estático solo se marca cuando su dirección está dentro de un pool activo y no es una reserva. Un ámbito creado durante una caída sigue activo en otro servidor, y el plan de direccionamiento IP dice una cosa mientras los ámbitos dicen otra.

## Cómo usarlo con datos reales

La exportación solo lee, con los cmdlets estándar de PowerShell DhcpServer y DnsServer: ámbitos, opciones, reservas y concesiones por servidor, y zonas y registros. Un ámbito en conmutación se exporta una sola vez, para no contar dos veces sus estadísticas. El plan IP se compara con ambos para encontrar ámbitos que no están en el plan, subredes planificadas sin ámbito, subredes que se solapan y subredes sin responsable o sin zona de búsqueda inversa.

Cada hallazgo tiene una gravedad, un responsable y una fecha, y las excepciones válidas quitan el punto mientras que las caducadas o incompletas no. El análisis funciona con Python y solo la librería estándar, y genera `report.html`, con cada ámbito, su crecimiento y los días que le quedan; `review-pack.md`, una página con las decisiones y las evidencias para las auditorías de ISO 27001 y NIS2; y ficheros CSV por ámbito, reserva, zona, registro obsoleto, subred, excepción, hallazgo y acción. Incluye 13 tests y un runbook para cambiar concesiones, ámbitos, actualizaciones seguras y limpieza sin sorpresas, y está pensado para ejecutarse el primer día laborable de cada mes y antes y después de cada cambio de red en una sede.

## De dónde sale

La hice a partir de administrar DNS, DHCP y Active Directory en Windows Server desde el principio de mi carrera, y de llevar switches y routers Cisco, firewalls FortiGate y redes con varias sedes. Detrás hay dos lecciones: el porcentaje de un ámbito importa menos que su ritmo, porque el que se llena es el que crece; y retirar un controlador de dominio no termina hasta que DHCP y DNS dejan de apuntar a él."""),
dict(n="54", repo="54-it-business-case-builder", date="2026-11-15", cat="tools",
 title_en="An ERP option that looked best at an NPV of 1.89 million falls to 1.10 million once 825,000 of benefits go",
 title_es="Una opción de ERP que parecía la mejor con un VAN de 1,89 millones cae a 1,10 al quitar 825.000 de beneficios",
 seo_title_en="IT business case: NPV, payback and checks · Iñigo González",
 seo_title_es="Business case de IT: VAN, payback y revisión · Iñigo González",
 seo_desc="IT business case builder: options against doing nothing, NPV, IRR and payback, the checks finance makes, ranges, sensitivity and the paper for the committee.",
 seo_desc_es="Business case de IT: opciones frente a no hacer nada, VAN, TIR y payback, la revisión de finanzas, rangos, sensibilidad y el documento para el comité.",
 dek_en="The business case builder, published with a fictional leasing company choosing what to do with its ERP, compares every option with doing nothing, runs the checks a finance partner makes before the committee and shows the figures as submitted and after the checks.",
 dek_es="El constructor de business cases, publicado con una empresa de leasing ficticia que decide qué hacer con su ERP, compara cada opción con no hacer nada, aplica las comprobaciones de un controller de finanzas antes del comité y enseña las cifras tal como se presentaron y tras la revisión.",
 en="""
Moving an ERP to SaaS in one go looks like the best option as submitted, with a net present value of 1.89 million, but it falls to 1.10 million and is marked not ready once the checks remove 825,000 of benefits. That is what the IT business case builder published with this post finds. It is an open-source tool, and its demo is a made-up leasing company deciding what to do with its ERP before support ends: staying, upgrading on premises, a SaaS big bang or SaaS in two phases.

The net present value, NPV, is the sum of each year's net cash flow discounted to today. For every option, the tool takes the cost of doing nothing minus the cost of the option plus the hard benefits, year by year from year zero, and computes NPV, IRR, payback, ROI, the one-off cost, the total cost of ownership and the NPV after the expected cost of the risks. The comparison is always with doing nothing, which is never free.

## The two-phase option wins, with a gate before phase two

The tool recommends SaaS in two phases, at an NPV of 563,000 and a payback of three and a half years. It adds a gate before phase two, because that option loses money in the pessimistic case. An option with a red finding on its costs or benefits is not ready and is not recommended, whatever its NPV; among the rest, the highest risk-adjusted NPV that pays back in time wins, and weighted non-financial criteria break ties.

## The mistakes a finance partner looks for

The checks are the ones a finance partner makes before the committee. A saving is counted twice when it names a cost the current platform pays and the option no longer has, because that saving is already in the difference between the two. Benefits that start before the go-live year are removed for those years, and hard benefits with no owner move to soft. Hours saved counted as cash, benefits with no KPI and unvalidated assumptions that carry the case, such as a vendor discount or the release of a contractor, are flagged too.

On the cost side, the tool looks for missing migration, decommission, training and internal staff costs, years with no running cost and risks with no mitigation. Where contingency is missing, it adds what the estimates need: more for a rough estimate than for a quote.

## Pessimistic and optimistic cases

A base case shown alone hides what happens if costs go up a fifth or go-live slips six months. The tool moves each cost by its confidence and each benefit by its evidence to build a pessimistic and an optimistic case, and measures how sensitive the NPV is to costs, benefits, a late go-live and the discount rate. It also produces the decisions for the committee and a benefits register with a KPI, an owner and reviews six and twelve months after go-live.

## How to use it with real data

A template command starts a case from a spreadsheet with the options, their costs year by year, the benefits, the risks, the assumptions and the non-financial criteria. The tool runs on Python with the standard library only and produces `report.html`, with the cumulative cash flow and the sensitivity chart; `business-case.md`, the paper for the committee; and CSV files for the options, cash flows, sensitivity, benefits, assumptions, findings and actions. It comes with 16 tests and a runbook from first draft to the committee.

## Where it comes from

I built it from preparing business cases with ROI and measurable benefits, estimating costs and timelines, managing IT budgets, using FinOps and TBM for cost transparency, negotiating vendor contracts and supporting an ERP (SAP) for the business. Two lessons are behind it: the most common mistake is counting the same saving twice; and a committee trusts a case that shows what was removed and what the downside is.""",
 es="""
Llevar un ERP a SaaS de golpe parece la mejor opción tal como se presenta, con un valor actual neto de 1,89 millones, pero baja a 1,10 millones y queda como no lista al quitar 825.000 de beneficios en la revisión. Así lo detecta el constructor de business cases de IT que acompaña a este post, un proyecto de código abierto cuya demo es una empresa de leasing inventada que decide qué hacer con su ERP antes de que acabe el soporte: quedarse, actualizar en local, un SaaS de golpe o un SaaS en dos fases.

El valor actual neto, o VAN, es la suma de los flujos de caja netos de cada año descontados a hoy. Para cada opción, la herramienta toma el coste de no hacer nada menos el coste de la opción más los beneficios tangibles, año a año desde el año cero, y calcula el VAN, la TIR, el payback, el ROI, la inversión inicial, el coste total de propiedad y el VAN descontando el coste esperado de los riesgos. La comparación siempre es con no hacer nada, que nunca sale gratis.

## Gana la opción en dos fases, con una puerta antes de la segunda

La herramienta recomienda el SaaS en dos fases, con un VAN de 563.000 y un payback de tres años y medio. Añade una puerta antes de la segunda fase, porque esa opción pierde dinero en el escenario pesimista. Una opción con un hallazgo rojo en sus costes o beneficios no está lista y no se recomienda, tenga el VAN que tenga; entre las demás gana el mayor VAN ajustado al riesgo que recupera la inversión a tiempo, y los criterios no financieros ponderados deshacen empates.

## Los errores que busca un controller de finanzas

Las comprobaciones son las que hace un controller de finanzas antes del comité. Un ahorro está contado dos veces cuando nombra un coste que paga la plataforma actual y que la opción ya no tiene, porque ese ahorro ya está en la diferencia entre las dos. Los beneficios anteriores al año de puesta en marcha se quitan para esos años, y los beneficios tangibles sin responsable pasan a intangibles. También se marcan las horas ahorradas contadas como dinero, los beneficios sin KPI y las hipótesis sin validar que sostienen el caso, como el descuento de un proveedor o la salida de un contratista.

En los costes, la herramienta busca la migración, la retirada, la formación y el personal interno que faltan, los años sin coste de operación y los riesgos sin mitigación. Donde falta contingencia, añade la que necesitan las estimaciones: más para una estimación aproximada que para un presupuesto firmado.

## Escenarios pesimista y optimista

Un caso base presentado solo esconde lo que pasa si los costes suben una quinta parte o la puesta en marcha se retrasa seis meses. La herramienta mueve cada coste según su confianza y cada beneficio según su evidencia para construir un escenario pesimista y otro optimista, y mide la sensibilidad del VAN a los costes, los beneficios, un retraso en la puesta en marcha y la tasa de descuento. Genera además las decisiones para el comité y un registro de beneficios con KPI, responsable y revisiones a los seis y doce meses de la puesta en marcha.

## Cómo usarlo con datos reales

Un comando de plantilla permite empezar un caso desde una hoja de cálculo con las opciones, sus costes año a año, los beneficios, los riesgos, las hipótesis y los criterios no financieros. La herramienta funciona con Python y solo la biblioteca estándar, y genera `report.html`, con el flujo de caja acumulado y el gráfico de sensibilidad; `business-case.md`, el documento para el comité; y ficheros CSV de opciones, flujos de caja, sensibilidad, beneficios, hipótesis, hallazgos y acciones. Incluye 16 tests y un runbook desde el primer borrador hasta el comité.

## De dónde sale

La hice a partir de preparar business cases con ROI y beneficios medibles, estimar costes y plazos, gestionar presupuestos de IT, usar FinOps y TBM para dar transparencia a los costes, negociar contratos con proveedores y dar soporte a un ERP (SAP) para el negocio. Detrás hay dos lecciones: el error más común es contar el mismo ahorro dos veces; y un comité confía en un caso que enseña lo que se ha quitado y cuál es el riesgo a la baja."""),
dict(n="55", repo="55-printer-fleet-health", date="2026-11-16", cat="tools",
 title_en="A store opened four 'printer offline' tickets because a queue was printing to an old address",
 title_es="Una tienda abrió cuatro tickets de «impresora sin conexión» por una cola que imprimía a una dirección antigua",
 seo_title_en="Printer fleet review: queues, toner and cost · Iñigo González",
 seo_title_es="Revisión de impresoras: colas, tóner y coste · Iñigo González",
 seo_desc="Monthly printer fleet review: printers down, stuck queues, toner to order, usage and cost per site, secure release, default passwords and vendor SLA.",
 seo_desc_es="Revisión mensual de impresoras: equipos caídos, colas atascadas, tóner a pedir, uso y coste por sede, impresión segura, contraseñas y SLA del proveedor.",
 dek_en="The monthly review, published with fictional data from a chain with 37 printers, cross-checks the printer register, the print servers, the managed print portal and the tickets to find the cause of repeat faults, what needs ordering and what is left over.",
 dek_es="La revisión mensual, publicada con datos ficticios de una cadena con 37 impresoras, cruza el registro de equipos, los servidores de impresión, el portal del proveedor y los tickets para encontrar la causa de las averías repetidas, lo que falta por pedir y lo que sobra.",
 en="""
The four "printer offline" tickets a Barcelona store opened in three weeks had a single cause: after a power cut, the multifunction printer took a new address on the network and the print server queue kept sending jobs to the old one. That is what the monthly printer review published with this post finds. It is an open-source project that runs on sample data from a fictional home goods retailer with a head office in Madrid, a warehouse in Zaragoza and eight stores.

Every time the support team restarted the queue, jobs came out for a few hours and the ticket was closed. The tool compares the address each queue prints to with the address the device itself reports to the managed print portal, flags a mismatch in red and links it to the repeat tickets. That is the difference between closing tickets and fixing the problem: the proposed fix is to correct the queue port and reserve the printer's address on the DHCP server, the service that hands out addresses on the network.

## Three empty consumables and a stuck delivery-note queue

The same review finds other faults that nobody sees until someone cannot print. In the warehouse, the queue for delivery notes has been stuck for 140 minutes behind 37 jobs. Three consumables are empty and not ordered, and five more will run out within ten days at last month's rate; for each one the report works out the last day to order it, allowing three days for delivery.

In all, 34 of the 37 printers are working on the day of the review, 92%. The report gives every finding an owner and a date: two days for the red ones and two weeks for the rest.

## HR payslips in a corridor tray

On security, two multifunction printers in confidential areas, Human Resources and Legal, print without secure release, the feature that holds a document until its owner identifies at the device with a badge or a PIN. Two others still have the factory admin password, which lets anyone on the network change their settings or read their address book.

The review ends with five decisions for the site leads: turn on secure release in those two areas; remove five desk printers that print 40 to 120 pages a month next to a multifunction used at a quarter of its capacity; decide on three leases, one with its notice date this Saturday; switch off the old print server, which still shares six printers; and print in black and white by default.

## How to use it with real data

The repository includes a PowerShell script that only reads the queues of the Windows print servers; the rest of the data comes from the managed print portal, the printer register and the ticketing tool. It runs on Python with no external dependencies and produces a web report, a one-page summary for the monthly meeting and CSV files with every finding and its action. The demo data is fictional: models, firmware, addresses, prices and tickets.

## Where it comes from

The tool comes from supporting the printers of retail stores and taking part in store openings, running the IT of an office site with users across several offices, and managing hardware vendors, their contracts and their SLAs.""",
 es="""
Los cuatro tickets de «impresora sin conexión» que abrió una tienda de Barcelona en tres semanas tenían una sola causa: tras un corte de luz, la multifunción cogió una dirección nueva en la red y la cola del servidor de impresión siguió enviando los trabajos a la antigua. Así lo detecta la revisión mensual de impresoras que acompaña a este post, un proyecto de código abierto que se ejecuta con datos de ejemplo de una cadena ficticia de artículos para el hogar, con sede en Madrid, un almacén en Zaragoza y ocho tiendas.

Cada vez que el equipo de soporte reiniciaba la cola, los trabajos salían durante unas horas y el ticket se cerraba. La herramienta compara la dirección a la que imprime cada cola con la que el propio equipo comunica al portal del proveedor, y cuando no coinciden lo marca en rojo y lo relaciona con los tickets repetidos. Es la diferencia entre cerrar avisos y resolver el problema: la solución propuesta es corregir el puerto de la cola y reservar la dirección de la impresora en el servidor DHCP, el servicio que reparte las direcciones de la red.

## Tres consumibles vacíos y una cola de albaranes parada

La misma revisión encuentra otros fallos que no se ven hasta que alguien no puede imprimir. En el almacén, la cola de los albaranes de entrega lleva 140 minutos parada detrás de 37 trabajos. Tres consumibles están vacíos y sin pedir, y otros cinco se acabarán en menos de diez días al ritmo de consumo del último mes; para cada uno, el informe calcula la fecha límite para pedirlo, descontando los tres días de entrega.

En total, 34 de las 37 impresoras funcionan el día de la revisión, un 92%. El informe asigna cada hallazgo a un responsable con fecha: dos días para los rojos y dos semanas para el resto.

## Las nóminas de RR. HH., en una bandeja del pasillo

En seguridad, dos multifunciones de áreas confidenciales, Recursos Humanos y Legal, imprimen sin impresión segura, el sistema que retiene el documento hasta que su dueño se identifica en el equipo con la tarjeta o un PIN. Otras dos conservan la contraseña de administrador de fábrica, lo que permite a cualquiera en la red cambiar su configuración o leer su libreta de direcciones.

La revisión termina con cinco decisiones para los responsables de las sedes: activar la impresión segura en esas dos áreas; retirar cinco impresoras de sobremesa que imprimen entre 40 y 120 páginas al mes junto a una multifunción usada a una cuarta parte de su capacidad; decidir qué hacer con tres contratos de renting, uno con la fecha de preaviso este sábado; apagar el servidor de impresión antiguo, que aún comparte seis impresoras, e imprimir en blanco y negro por defecto.

## Cómo usarlo con datos reales

El repositorio incluye un script de PowerShell que solo lee las colas de los servidores de impresión de Windows; el resto de datos sale del portal del proveedor de impresión gestionada, del registro de impresoras y de la herramienta de tickets. Funciona con Python y sin dependencias externas, y genera un informe web, un resumen de una página para la reunión mensual y ficheros CSV con cada hallazgo y su acción. Los datos de la demo son ficticios: modelos, firmware, direcciones, precios y tickets.

## De dónde sale

La herramienta nace de dar soporte a las impresoras de tiendas y participar en sus aperturas, de llevar la IT de una sede con usuarios en varias oficinas, y de gestionar proveedores de hardware, sus contratos y sus SLA."""),
dict(n="56", repo="56-cmdb-data-quality-review", date="2026-11-17", cat="tools",
 title_en="A server switched off in the summer was still live in the CMDB, and a reporting database still ran on it",
 title_es="Un servidor apagado en verano seguía activo en la CMDB, y una base de datos de informes seguía colgando de él",
 seo_title_en="CMDB data quality review: stale CIs, owners · Iñigo González",
 seo_title_es="Calidad de la CMDB: CI obsoletos y dueños · Iñigo González",
 seo_desc="Monthly CMDB review: stale CIs, devices with no CI, records that disagree with discovery, owners who left, broken relationships and incidents with no CI.",
 seo_desc_es="Revisión mensual de la CMDB: CI que nadie ve, equipos sin CI, fichas que no cuadran con el descubrimiento, dueños que se fueron y relaciones rotas.",
 dek_en="The monthly review, published with fictional data from a logistics company with 115 records, cross-checks the CMDB with Active Directory, Intune, vCenter, a network scan, the directory and the month's tickets, and gives every CI, class and support group a data quality score.",
 dek_es="La revisión mensual, publicada con datos ficticios de una empresa de logística con 115 fichas, cruza la CMDB con Active Directory, Intune, vCenter, un escaneo de red, el directorio y los tickets del mes, y da una nota de calidad a cada CI, clase y grupo de soporte.",
 en="""
A critical legacy SQL server that no discovery source had seen since early September was still operational in the CMDB, and the reporting database of the finance team still ran on it. That is what the CMDB data quality review published with this post finds. It is an open-source project that runs on sample data from a fictional logistics company with a head office and data room in Madrid, a warehouse in Zaragoza and a sales office in Valencia.

A CMDB, the configuration management database that records every server, application and device and how they depend on each other, is only useful if people trust it. The review compares each live record with what Active Directory, Intune, vCenter and a network scan see. A server nobody has seen lately is flagged as stale; when no ticket, change or live system needs it either, it becomes a candidate to retire. The legacy SQL server is not one, because something still runs on it, so the finding is red and goes to its support group within two days.

## Six devices with no record and a laptop retired in September

The same cross-check finds six devices seen on the network in the last 45 days that have no record: a migration VM, a test server, a switch in Zaragoza and three laptops. A laptop retired in September is still checking in to Intune. Seven records disagree with discovery: three VMs that were re-addressed, three PCs upgraded to Windows 11 whose records still say Windows 10, and a laptop that moved site.

Those three upgrades were done under a change, but the records were last updated in September. The review reads the month's changes and flags each one implemented after the record's last update, so the gap shows up in how changes are closed rather than in the people who did the work.

## Owners who left and a service with nothing mapped

Five records belong to two people who left, one of them the order management API, which makes the finding red. The finance reports application runs on a server retired in June, and a change was implemented on that server last week. The customer returns portal, a critical business service, has no record mapped to it, so an outage could not be traced to it. In Field Services, 31% of the month's incidents were logged with no configuration item.

Every record gets a data quality score: the share of the fields its class needs, whether discovery sees it and agrees with it, and, for applications and databases, whether they have what they run on. The demo scores 94.7%, 1.5 points down on last month, with 7 red and 32 amber findings. It ends with five decisions: retire six records, register or remove six devices, new owners for five records, map the customer returns portal, and make the configuration item mandatory on Field Services incidents.

## How to use it with real data

The repository includes a PowerShell script that only reads the computers Active Directory knows about; the CMDB export, its relationships and the other discovery sources come from the ITSM tool, Intune, vCenter or a network scan in the same columns. It runs on Python with no external dependencies and produces a web report, a one-page pack for the monthly review and CSV files with every record, finding and action. The demo data is fictional: names, serials, addresses and tickets.

## Where it comes from

The tool comes from owning the incident, change and problem processes with their dashboards, running CMDB and configuration management and answering audits, working with ITSM tools such as EasyVista, GLPI and HaloITSM, and keeping the comms rooms inventory in Device42.""",
 es="""
Un servidor SQL heredado y crítico que ningún sistema de descubrimiento veía desde principios de septiembre seguía activo en la CMDB, y la base de datos de informes de Finanzas seguía funcionando sobre él. Así lo detecta la revisión de calidad de la CMDB que acompaña a este post, un proyecto de código abierto que se ejecuta con datos de ejemplo de una empresa ficticia de logística, con sede y sala técnica en Madrid, un almacén en Zaragoza y una oficina comercial en Valencia.

Una CMDB, la base de datos de configuración que registra cada servidor, aplicación y equipo y de qué depende cada uno, solo sirve si la gente se fía de ella. La revisión compara cada ficha activa con lo que ven Active Directory, Intune, vCenter y un escaneo de red. Un servidor que nadie ha visto últimamente se marca como obsoleto; si además ningún ticket, cambio ni sistema activo lo necesita, pasa a ser candidato a retirar. El SQL heredado no lo es, porque algo sigue funcionando sobre él, así que el hallazgo es rojo y va a su grupo de soporte con dos días de plazo.

## Seis equipos sin ficha y un portátil retirado en septiembre

El mismo cruce encuentra seis equipos vistos en la red en los últimos 45 días que no tienen ficha: una máquina virtual de una migración, un servidor de pruebas, un switch en Zaragoza y tres portátiles. Un portátil retirado en septiembre sigue conectándose a Intune. Siete fichas no cuadran con el descubrimiento: tres máquinas virtuales a las que se cambió la dirección, tres PC actualizados a Windows 11 cuyas fichas siguen diciendo Windows 10 y un portátil que cambió de sede.

Esas tres actualizaciones se hicieron con un cambio, pero las fichas se tocaron por última vez en septiembre. La revisión lee los cambios del mes y marca cada uno que se implantó después de la última actualización de la ficha, de modo que el hueco aparece en cómo se cierran los cambios y no en las personas que hicieron el trabajo.

## Dueños que se fueron y un servicio sin nada asociado

Cinco fichas pertenecen a dos personas que ya no están, una de ellas la API de gestión de pedidos, lo que convierte el hallazgo en rojo. La aplicación de informes de Finanzas funciona sobre un servidor retirado en junio, y la semana pasada se implantó un cambio en ese servidor. El portal de devoluciones de clientes, un servicio de negocio crítico, no tiene ninguna ficha asociada, así que una caída no se podría relacionar con él. En Field Services, el 31% de las incidencias del mes se registraron sin elemento de configuración.

Cada ficha recibe una nota de calidad: la parte de los campos que necesita su clase, si el descubrimiento la ve y coincide con ella y, en aplicaciones y bases de datos, si tienen sobre qué funcionar. La demo saca un 94,7%, 1,5 puntos menos que el mes anterior, con 7 hallazgos rojos y 32 ámbar. Termina con cinco decisiones: retirar seis fichas, registrar o quitar seis equipos, nuevos dueños para cinco fichas, asociar el portal de devoluciones y hacer obligatorio el elemento de configuración en las incidencias de Field Services.

## Cómo usarlo con datos reales

El repositorio incluye un script de PowerShell que solo lee los equipos que conoce Active Directory; la exportación de la CMDB, sus relaciones y el resto de fuentes de descubrimiento salen de la herramienta ITSM, Intune, vCenter o un escaneo de red con las mismas columnas. Funciona con Python y sin dependencias externas, y genera un informe web, un dosier de una página para la revisión mensual y ficheros CSV con cada ficha, hallazgo y acción. Los datos de la demo son ficticios: nombres, números de serie, direcciones y tickets.

## De dónde sale

La herramienta nace de ser responsable de los procesos de incidencias, cambios y problemas con sus cuadros de mando, de llevar la CMDB y la gestión de la configuración y responder a auditorías, de trabajar con herramientas ITSM como EasyVista, GLPI y HaloITSM, y de llevar en Device42 el inventario de las salas de comunicaciones."""),
dict(n="57", repo="57-ai-use-case-register", date="2026-11-18", cat="tools",
 title_en="A pilot scoring the emotions of contact-centre agents was running, and the company's AI policy does not allow it",
 title_es="Un piloto que puntuaba las emociones de los agentes del contact center estaba en marcha, y la política de IA de la empresa no lo permite",
 seo_title_en="AI use case register: shadow AI, risk tiers · Iñigo González",
 seo_title_es="Registro de casos de uso de IA y riesgo · Iñigo González",
 seo_desc="Monthly AI use case register review: shadow AI, risk tiers set by the AI policy, controls per tier, sensitive data, vendors and unused licences.",
 seo_desc_es="Revisión mensual del registro de casos de uso de IA: IA sin registrar, nivel de riesgo según la política, controles, datos sensibles y licencias sin uso.",
 dek_en="The monthly review, published with fictional data from an insurer with 24 AI use cases, cross-checks the register with what discovery finds in the tenant, the directory and the AI incidents, and checks each use case against the risk tier and the controls the company's AI policy asks for.",
 dek_es="La revisión mensual, publicada con datos ficticios de una aseguradora con 24 casos de uso de IA, cruza el registro con lo que el descubrimiento encuentra en el tenant, el directorio y los incidentes de IA, y comprueba cada caso de uso contra el nivel de riesgo y los controles que pide la política de IA de la empresa.",
 en="""
A pilot that scores how stressed contact-centre agents sound in their call recordings had been running for five weeks, registered as limited risk. The company's AI policy lists emotion recognition at work among the practices it does not allow. That is what the AI use case register review published with this post finds. It is an open-source project that runs on sample data from a fictional insurer with its head office in Madrid and offices in Barcelona and Seville.

The register is the list of every place the company uses AI: what it does, who owns it, which tool it runs on, which data goes into it and how risky it is. The review does not take the declared tier at face value. It works the tier out from the policy: areas the policy prohibits, areas it treats as high risk (hiring, staff evaluation, insurance pricing, claims decisions), use cases that customers talk to or that feed decisions about people, and everything else. The emotion scoring pilot ends up as the first decision of the month: stop it and record why.

## A CV screening assistant registered as limited risk

The same check finds two use cases declared lower than the policy makes them. A CV screening assistant that ranks applicants for contact-centre roles was registered as limited because the form asked who uses it, not what it decides; the policy makes hiring high risk. A health policy pricing pilot is in the same position. The CV assistant is already in production with no DPIA, risk assessment or test evidence, so the finding is red and the controls of the new tier get a date.

Each tier has its controls: human oversight, a data protection impact assessment, a risk assessment, test evidence, logging, the vendor's data processing agreement, a notice for the people it talks to or decides about, and an owner with current AI training. The chatbot on the website has no notice that it is a bot, and a wrong answer it gave about dental cover has been open as an incident for four weeks.

## Six AI tools nobody registered

Discovery in the tenant finds six AI tools in use with no entry in the register: a claims FAQ agent built in Copilot Studio with 142 users, a note-taking app consented by 23 people that records calls with clients, a slides app, a chat app with personal data, a proposal agent and a translation app. The sales team's meeting notes run on a tool that is not approved for confidential data, and its vendor can train its models on the recordings.

The review also looks at value: two pilots past 90 days with no decision, a use case in production with no business case, 41 unused seats of a writing tool and a report drafting assistant that saves a third of the hours it promised. Every use case gets a governance score. The demo scores 85.3%, 2.7 points up on last month, with 13 red and 27 amber findings, and ends with seven decisions for the AI governance committee.

## How to use it with real data

The repository includes a PowerShell script that only reads the enterprise apps in Entra ID that look like AI tools and how many users are assigned to each; the register, the Copilot Studio agents, cloud app discovery, the directory with the training dates and the incidents go in CSV files with the same columns. The tiers and controls are the organisation's own policy in a settings file, and the review does not decide whether a law applies. It runs on Python with no external dependencies and produces a web report, a one-page pack for the committee and CSV files with every use case, gap, review and action. The demo data is fictional: names, tools, vendors, figures and tickets.

## Where it comes from

The tool comes from deploying Microsoft 365 Copilot and AI tools for users and driving their adoption, administering Microsoft 365 agents and Copilot Studio, working with responsible AI and the EU AI Act alongside ISO 27001, GDPR and NIS2, Microsoft Purview, and writing business cases with measurable benefits.""",
 es="""
Un piloto que puntúa lo estresados que suenan los agentes del contact center en sus grabaciones llevaba cinco semanas en marcha, registrado como riesgo limitado. La política de IA de la empresa incluye el reconocimiento de emociones en el trabajo entre las prácticas que no permite. Así lo detecta la revisión del registro de casos de uso de IA que acompaña a este post, un proyecto de código abierto que se ejecuta con datos de ejemplo de una aseguradora ficticia con sede en Madrid y oficinas en Barcelona y Sevilla.

El registro es la lista de todos los sitios donde la empresa usa IA: qué hace, quién es el responsable, en qué herramienta funciona, qué datos entran y cuánto riesgo tiene. La revisión no se queda con el nivel declarado. Lo calcula a partir de la política: ámbitos que la política prohíbe, ámbitos que trata como alto riesgo (selección de personal, evaluación de empleados, tarificación de seguros, decisiones sobre siniestros), casos de uso con los que hablan los clientes o que alimentan decisiones sobre personas, y todo lo demás. El piloto de emociones acaba siendo la primera decisión del mes: pararlo y dejar constancia del motivo.

## Un asistente de cribado de CV registrado como riesgo limitado

La misma comprobación encuentra dos casos de uso declarados por debajo de lo que dice la política. Un asistente que ordena las candidaturas para puestos del contact center se registró como limitado porque el formulario preguntaba quién lo usa, no qué decide; la política considera alto riesgo la selección de personal. Un piloto de tarificación de pólizas de salud está en la misma situación. El asistente de CV ya está en producción sin evaluación de impacto, análisis de riesgos ni pruebas documentadas, así que el hallazgo es rojo y los controles del nuevo nivel reciben una fecha.

Cada nivel tiene sus controles: supervisión humana, evaluación de impacto en protección de datos, análisis de riesgos, pruebas documentadas, registro de actividad, el contrato de encargo de tratamiento con el proveedor, un aviso para las personas con las que habla o sobre las que decide y un responsable con la formación en IA al día. El chatbot de la web no avisa de que es un bot, y una respuesta equivocada que dio sobre la cobertura dental lleva cuatro semanas abierta como incidente.

## Seis herramientas de IA que nadie registró

El descubrimiento en el tenant encuentra seis herramientas de IA en uso sin entrada en el registro: un agente de preguntas sobre siniestros hecho en Copilot Studio con 142 usuarios, una aplicación de notas consentida por 23 personas que graba llamadas con clientes, una aplicación de presentaciones, un chat con datos personales, un agente de propuestas y una aplicación de traducción. Las notas de reuniones del equipo comercial funcionan en una herramienta que no está aprobada para datos confidenciales, y su proveedor puede entrenar sus modelos con las grabaciones.

La revisión también mira el valor: dos pilotos con más de 90 días y sin decisión, un caso de uso en producción sin business case, 41 licencias sin usar de una herramienta de redacción y un asistente de informes que ahorra un tercio de las horas que prometía. Cada caso de uso recibe una nota de gobierno. La demo saca un 85,3%, 2,7 puntos más que el mes anterior, con 13 hallazgos rojos y 27 ámbar, y termina con siete decisiones para el comité de gobierno de la IA.

## Cómo usarlo con datos reales

El repositorio incluye un script de PowerShell que solo lee las aplicaciones empresariales de Entra ID que parecen herramientas de IA y cuántos usuarios tiene asignados cada una; el registro, los agentes de Copilot Studio, el descubrimiento de aplicaciones en la nube, el directorio con las fechas de formación y los incidentes van en ficheros CSV con las mismas columnas. Los niveles y los controles son la política de la propia organización en un fichero de configuración, y la revisión no decide si se aplica una ley. Funciona con Python y sin dependencias externas, y genera un informe web, un dosier de una página para el comité y ficheros CSV con cada caso de uso, control pendiente, revisión y acción. Los datos de la demo son ficticios: nombres, herramientas, proveedores, cifras y tickets.

## De dónde sale

La herramienta nace de desplegar Microsoft 365 Copilot y herramientas de IA para los usuarios e impulsar su adopción, de administrar agentes de Microsoft 365 y Copilot Studio, de trabajar con IA responsable y el reglamento europeo de IA junto con ISO 27001, RGPD y NIS2, de Microsoft Purview y de preparar business cases con beneficios medibles."""),
dict(n="58", repo="58-business-impact-analysis", date="2026-11-19", cat="tools",
 title_en="Settlement could wait twelve hours, and the file shares it reads would take a day to come back and had never been tested",
 title_es="La liquidación podía esperar doce horas, y las carpetas compartidas que lee tardarían un día en volver y nunca se habían probado",
 seo_title_en="Business impact analysis: MTPD, RTO and RPO · Iñigo González",
 seo_title_es="Análisis de impacto (BIA): MTPD, RTO y RPO · Iñigo González",
 seo_desc="Business impact analysis review: MTPD and tier per process, required RTO and RPO against what IT, suppliers and people can do, DR tests and recovery order.",
 seo_desc_es="Revisión del análisis de impacto: MTPD y nivel por proceso, RTO y RPO necesarios frente a lo que pueden IT, proveedores y personas, pruebas de DR y orden.",
 dek_en="The review, published with fictional data from a financial services firm with 14 business processes, works out how long each process can be down and how much data it can lose, and checks whether the IT services, suppliers and people it depends on can meet that.",
 dek_es="La revisión, publicada con datos ficticios de una empresa de servicios financieros con 14 procesos de negocio, calcula cuánto tiempo puede parar cada proceso y cuántos datos puede perder, y comprueba si los servicios de IT, los proveedores y las personas de los que depende pueden cumplirlo.",
 en="""
Settlement and reconciliation could be stopped for twelve hours before the damage became intolerable. The file shares it reads would take a day to come back, keep one restore point a day, are run as a tier 3 service and had never been part of a DR test. That is what the business impact analysis review published with this post finds. It is an open-source project that runs on sample data from a fictional financial services firm with its head office in Madrid and a disaster recovery site in Barcelona.

A business impact analysis, or BIA, asks each process owner what happens if the process stops for four hours, a day, three days or a week. The review takes those answers and the organisation's continuity policy and works out three figures for each process: the maximum tolerable period of disruption, the tier, and the recovery time and data loss it can accept. Settlement reaches a major impact after one day, so it is tier 2 and needs to be back within twelve hours.

## A process is as fast as the slowest service under it

The review then follows each process down to everything it runs on. Settlement uses its own application, which a DR test brought back in ten hours, and that application needs the SQL cluster and the file shares. The file shares are the slowest link: a claimed 24 hours, never tested, with daily backups for a process that can lose one hour of data. The finding is red and lands on the file shares, not on the application everyone looks at first.

The same reading finds payments, which cannot lose any data, sitting on a database that keeps a restore point every 15 minutes, and a payments hub whose two-hour recovery has never been shown in a test. One replica of the risk engine stopped replicating the night before, so its real restore point is the four-hour backup. The order management system is a month past its six-monthly test, and document management failed its last one in February.

## Outside IT

Not every gap is a server. The bureau that connects payments to the payment network promises four hours in its contract for a process that can only wait two. One person operates that network connection and nobody covers her, and another is the only one who runs the reconciliation scripts. The client service desk has no alternate site, two suppliers have no current continuity evidence and three BIAs are out of date or unsigned.

Each process gets a resilience score. The demo scores 88.5%, with 12 red and 17 amber findings, and ends with six decisions: close the recovery gaps of four services, run six DR tests, raise the tier of three services, review three supplier contracts, train two deputies and review three BIAs. The review also lists the order in which to bring services back: the network first, then directory and databases, then the applications that need them, the most urgent first.

## How to use it with real data

The repository includes a PowerShell script that only reads the Hyper-V Replica status of each host; the processes, their dependencies, the services with their DR tests, suppliers and key people go in CSV files. Tiers, recovery factors and test frequency are the organisation's own policy in a settings file. It runs on Python with no external dependencies and produces a web report, a one-page pack for the continuity steering committee and CSV files with every process, service, test and action. The demo data is fictional: names, services, suppliers and dates.

## Where it comes from

The tool comes from supervising disaster recovery and business continuity tests, designing and testing backup and DR plans, applying ISO 22301 and ISO 27001, working with Veeam, Commvault, Hyper-V and vSphere, and running availability and capacity management as a formal practice.""",
 es="""
La liquidación y conciliación podía estar parada doce horas antes de que el daño fuera intolerable. Las carpetas compartidas que lee tardarían un día en volver, guardan un punto de restauración al día, se gestionan como servicio de nivel 3 y nunca habían entrado en una prueba de recuperación ante desastres. Así lo detecta la revisión del análisis de impacto en el negocio que acompaña a este post, un proyecto de código abierto que se ejecuta con datos de ejemplo de una empresa ficticia de servicios financieros con sede en Madrid y centro de respaldo en Barcelona.

Un análisis de impacto en el negocio, o BIA, pregunta a cada responsable qué pasa si su proceso se para cuatro horas, un día, tres días o una semana. La revisión toma esas respuestas y la política de continuidad de la organización y calcula tres cifras por proceso: el periodo máximo de interrupción tolerable, el nivel, y el tiempo de recuperación y la pérdida de datos que puede aceptar. La liquidación llega a un impacto grave al día, así que es de nivel 2 y tiene que estar de vuelta en doce horas.

## Un proceso es tan rápido como el servicio más lento que tiene debajo

Después, la revisión sigue cada proceso hasta todo aquello sobre lo que funciona. La liquidación usa su propia aplicación, que una prueba de DR recuperó en diez horas, y esa aplicación necesita el clúster de SQL y las carpetas compartidas. Las carpetas son el eslabón más lento: 24 horas declaradas y nunca probadas, con copias diarias para un proceso que solo puede perder una hora de datos. El hallazgo es rojo y recae en las carpetas, no en la aplicación que todos miran primero.

La misma lectura encuentra los pagos, que no pueden perder ningún dato, sobre una base de datos con un punto de restauración cada 15 minutos, y un hub de pagos cuya recuperación en dos horas nunca se ha demostrado en una prueba. Una réplica del motor de riesgos dejó de replicar la noche anterior, así que su punto de restauración real es la copia de cada cuatro horas. El sistema de órdenes lleva un mes de retraso en su prueba semestral y la gestión documental falló la última, en febrero.

## Fuera de IT

No todos los huecos son un servidor. El proveedor que conecta los pagos con la red de pagos promete cuatro horas en su contrato para un proceso que solo puede esperar dos. Una sola persona opera esa conexión y nadie la cubre, y otra es la única que ejecuta los scripts de conciliación. El servicio de atención a clientes no tiene sede alternativa, dos proveedores no tienen evidencias de continuidad al día y tres BIA están caducados o sin firmar.

Cada proceso recibe una nota de resiliencia. La demo saca un 88,5%, con 12 hallazgos rojos y 17 ámbar, y termina con seis decisiones: cerrar los huecos de recuperación de cuatro servicios, hacer seis pruebas de DR, subir el nivel de tres servicios, revisar tres contratos de proveedores, formar a dos suplentes y revisar tres BIA. La revisión también da el orden en el que recuperar los servicios: primero la red, después el directorio y las bases de datos, y luego las aplicaciones que dependen de ellos, las más urgentes primero.

## Cómo usarlo con datos reales

El repositorio incluye un script de PowerShell que solo lee el estado de Hyper-V Replica de cada host; los procesos, sus dependencias, los servicios con sus pruebas de DR, los proveedores y las personas clave van en ficheros CSV. Los niveles, los factores de recuperación y la frecuencia de pruebas son la política de la propia organización en un fichero de configuración. Funciona con Python y sin dependencias externas, y genera un informe web, un dosier de una página para el comité de continuidad y ficheros CSV con cada proceso, servicio, prueba y acción. Los datos de la demo son ficticios: nombres, servicios, proveedores y fechas.

## De dónde sale

La herramienta nace de supervisar pruebas de recuperación ante desastres y de continuidad de negocio, de diseñar y probar planes de copias y de DR, de aplicar ISO 22301 e ISO 27001, de trabajar con Veeam, Commvault, Hyper-V y vSphere, y de llevar la gestión de disponibilidad y capacidad como práctica formal."""),
dict(n="59", repo="59-market-data-entitlement-review", date="2026-11-20", updated="2026-11-21", cat="tools",
 title_en="A trader who left in October still had four market data packages, and nobody had opened commodity futures since July",
 title_es="Un trader que se fue en octubre seguía con cuatro paquetes de datos de mercado, y nadie abría los futuros de materias primas desde julio",
 seo_title_en="Market data entitlements: LSEG and Bloomberg · Iñigo González",
 seo_title_es="Datos de mercado: permisos LSEG y Bloomberg · Iñigo González",
 seo_desc="Market data entitlement review for LSEG RTDS and Bloomberg B-PIPE: leavers still entitled, unused and duplicate packages, invoice checks, switch-off list.",
 seo_desc_es="Revisión de permisos de datos de mercado en LSEG RTDS y Bloomberg B-PIPE: bajas con acceso, paquetes sin uso o duplicados, factura y lista de cortes.",
 dek_en="The review, published with fictional data from a broker with 34 people on its trading floor, checks who can see which market data on LSEG and Bloomberg, what nobody uses and whether the invoice matches, and lists what to switch off before the vendors' cut-off.",
 dek_es="La revisión, publicada con datos ficticios de un bróker con 34 personas en su sala de trading, comprueba quién ve qué datos de mercado en LSEG y Bloomberg, qué no usa nadie y si la factura cuadra, y saca lo que hay que dar de baja antes del cierre de los proveedores.",
 en="""
A rates trader left at the end of October and was still entitled to four market data packages three weeks later. A test account that nobody remembered had swap data on both platforms, and a commodity futures package paid for two people had not been opened since July. That is what the market data entitlement review published with this post finds. It is an open-source project that runs on sample data from a fictional broker with its trading floor in Madrid.

Market data is charged per person and per package every month, on LSEG and on Bloomberg. Each platform has its own system that says who can see what: DACS for LSEG RTDS and EMRS for Bloomberg B-PIPE. The review joins both exports with the directory, the contract fees, the vendor invoice and the packages each desk may have, five days before the cut-off for the December invoice.

## Who should not be there at all

Three accounts are red: the trader who left, a salesperson whose account is disabled and still has three packages, and the test account, which is not in the directory. Two entitlements fall outside their desk's policy, such as credit index data for an equities salesperson, and four have no recorded approval.

## What nobody uses

Five entitlements have not been used for more than 90 days, and one given in July has never been opened. A government bond trader has the same Eurozone bonds data on both platforms and only uses the LSEG one. The review puts all of them, with the leavers, on a switch-off list with what each one costs: 16 entitlements and €1,500 a month, €18,000 a year, before the cut-off.

## The invoice and the applications

The invoice charges for eleven credit index users when nine are entitled, a credit to claim. The other way round is the risky one: six people can see European equities depth and four are declared, the difference an audit would find. A bond pricing engine reads Bloomberg data without a screen and there is no non-display licence for it; another application has no business owner, and a legacy risk feed stopped reading in August.

The demo scores 78.4% clean entitlements, seven points up on the last review, with five red and 16 amber findings and six decisions: switch off the 16 entitlements, cancel the idle package, correct one declaration, licence or stop the pricing engine, claim the credit and have the desk heads approve or remove what is outside policy.

## How to use it with real data

The repository includes a PowerShell script that only reads Active Directory for the people who hold an entitlement; the DACS and EMRS exports, the packages with their fees, the invoice and the desk policies go in CSV files. The periods, the cut-off date and the fees are the organisation's own policy and contracts in a settings file. It runs on Python with no external dependencies and produces a web report, a one-page pack for the desk heads and CSV files with every entitlement, the switch-off list, packages, invoice lines and actions. The demo data is fictional: names, packages, fees and dates, and the fees are not any vendor's prices.

## Where it comes from

The tool comes from supporting trading desks and their market data platforms, LSEG RTDS / TREP and Bloomberg B-PIPE, and from software asset management, licence cost control, vendor management and access reviews under ISO 27001.""",
 es="""
Un trader de tipos se fue a finales de octubre y tres semanas después seguía con permiso para cuatro paquetes de datos de mercado. Una cuenta de pruebas de la que nadie se acordaba tenía datos de swaps en las dos plataformas, y un paquete de futuros de materias primas que se pagaba para dos personas no se abría desde julio. Así lo detecta la revisión de permisos de datos de mercado que acompaña a este post, un proyecto de código abierto que se ejecuta con datos de ejemplo de un bróker ficticio con su sala de trading en Madrid.

Los datos de mercado se cobran por persona y por paquete cada mes, en LSEG y en Bloomberg. Cada plataforma tiene su propio sistema que dice quién puede ver qué: DACS para LSEG RTDS y EMRS para Bloomberg B-PIPE. La revisión cruza las dos exportaciones con el directorio, las tarifas del contrato, la factura del proveedor y los paquetes que puede tener cada mesa, cinco días antes del cierre de la factura de diciembre.

## Quién no debería estar

Tres cuentas salen en rojo: el trader que se fue, una comercial con la cuenta deshabilitada que mantiene tres paquetes y la cuenta de pruebas, que no está en el directorio. Dos permisos quedan fuera de la política de su mesa, como los índices de crédito de un comercial de renta variable, y cuatro no tienen aprobación registrada.

## Lo que no usa nadie

Cinco permisos llevan más de 90 días sin usarse y uno concedido en julio no se ha abierto nunca. Un trader de deuda pública tiene los mismos datos de bonos de la zona euro en las dos plataformas y solo usa los de LSEG. La revisión los pone todos, junto con las bajas, en una lista de cortes con lo que cuesta cada uno: 16 permisos y 1.500 € al mes, 18.000 € al año, antes del cierre.

## La factura y las aplicaciones

La factura cobra once usuarios de índices de crédito cuando hay nueve con permiso: un abono que reclamar. Al revés es lo arriesgado: seis personas ven la profundidad de renta variable europea y hay cuatro declaradas, la diferencia que encontraría una auditoría. Un motor de precios de bonos lee datos de Bloomberg sin pantalla y no hay licencia non-display para ello; otra aplicación no tiene responsable de negocio, y una antigua alimentación de riesgos dejó de leer en agosto.

La demo saca un 78,4% de permisos limpios, siete puntos más que en la revisión anterior, con cinco hallazgos rojos y 16 ámbar, y seis decisiones: dar de baja los 16 permisos, cancelar el paquete que nadie usa, corregir una declaración, licenciar o parar el motor de precios, reclamar el abono y que los jefes de mesa aprueben o quiten lo que está fuera de política.

## Cómo usarlo con datos reales

El repositorio incluye un script de PowerShell que solo lee Active Directory para las personas que tienen algún permiso; las exportaciones de DACS y EMRS, los paquetes con sus tarifas, la factura y las políticas de cada mesa van en ficheros CSV. Los plazos, la fecha de cierre y las tarifas son la política y los contratos de la propia organización en un fichero de configuración. Funciona con Python y sin dependencias externas, y genera un informe web, un dosier de una página para los jefes de mesa y ficheros CSV con cada permiso, la lista de cortes, los paquetes, las líneas de factura y las acciones. Los datos de la demo son ficticios: nombres, paquetes, tarifas y fechas, y las tarifas no son los precios de ningún proveedor.

## De dónde sale

La herramienta nace de dar soporte a mesas de trading y a sus plataformas de datos de mercado, LSEG RTDS / TREP y Bloomberg B-PIPE, y de la gestión de activos de software, el control de costes de licencias, la gestión de proveedores y las revisiones de accesos con ISO 27001."""),
dict(n="60", repo="60-fix-session-health", date="2026-11-21", cat="tools",
 title_en="A logon refused at ten to ten on Friday night would have left an order session down at Monday's open",
 title_es="Un logon rechazado a las diez menos diez del viernes habría dejado una sesión de órdenes caída en la apertura del lunes",
 seo_title_en="FIX session health: drops, gaps and resets · Iñigo González",
 seo_title_es="Sesiones FIX: caídas, huecos y resets · Iñigo González",
 seo_desc="FIX session health review: drops, refused logons, sequence gaps and resets, missed heartbeats, rejects, latency and a watchlist before the open.",
 seo_desc_es="Revisión de sesiones FIX: caídas, logons rechazados, huecos y resets de secuencia, heartbeats perdidos, rechazos, latencia y lista para antes de la apertura.",
 dek_en="The review, published with fictional data from a broker with 12 FIX sessions, reads a week of session messages from the engine logs and lists the sessions to look at before the market opens.",
 dek_es="La revisión, publicada con datos ficticios de un bróker con 12 sesiones FIX, lee una semana de mensajes de sesión de los logs del motor y saca las sesiones que hay que mirar antes de que abra el mercado.",
 en="""
At 21:58 on Friday, an order session with Adatum Capital tried to log on again after a disconnect and was refused: "MsgSeqNum too low, expecting 4812 but received 1". Nobody would have looked at it until Monday's open. That is what the FIX session health review published with this post puts first on its list. It is an open-source project that runs on sample data from a fictional broker with its electronic trading desk in Madrid.

FIX is the protocol orders, executions and drop copies travel on between a broker and its counterparties. Every session leaves a log, and the review only needs the session-level messages in it: logons and logouts, test requests, resend requests, sequence resets and rejects. A read-only PowerShell script takes them from the engine logs; the review reads a week of them, session by session, against the desk's thresholds.

## What can have been lost

On Wednesday at 14:12, Northwind Clearing's drop copy received a sequence reset without gap fill, from 18322 to 18450. Resend requests that are answered are normal; a reset like this means 128 messages were never resent, so the orders and trades of that window have to be reconciled before Monday. It is the second line of the watchlist.

## What is unstable

Tailspin Bank's order session dropped five times without a logout, four of them in market hours, and needed six resends to recover. On Friday its order round trip went from about 4 ms to 38 ms at the 99th percentile. Litware's market data needed 14 test requests, almost all around the open, because its heartbeats stopped arriving. Relecloud's RFQ session has not logged on since Wednesday, Wingtip Prime rejected 22 allocations for an unknown account and Woodgrove logs on with a 60-second heartbeat when 30 is configured.

## What will break on its own

The TLS certificate of the two Contoso MTF sessions expires on Thursday, and Proseware's failover to the backup gateway has never been tested.

The demo scores 89% session health, 4.8 points up on the last review, with six red and eight amber findings, five sessions on the watchlist before Monday at 08:00 and six decisions: check the watchlist an hour before the open, open cases with two counterparties, reconcile the reset, renew the certificates, book the failover test and fix the static data behind the rejects.

## How to use it with real data

The script reads QuickFIX/J or QuickFIX/n style logs; the session list with its counterparty, purpose, heartbeat, hosts, failover test and certificate goes in a CSV, and the daily latency in another if the monitoring has it. Market hours, thresholds and latency limits are the desk's own policy in a settings file. It runs on Python with no external dependencies and produces a web report, a one-page pack for the desk and CSV files with every session, day, finding and action. The demo data is fictional: names, CompIDs, hosts and times.

## Where it comes from

The tool comes from keeping trading floors connected: FIX and electronic trading connectivity with counterparties, LSEG and Bloomberg market data platforms, monitoring and major incident response, and network operations.""",
 es="""
A las 21:58 del viernes, una sesión de órdenes con Adatum Capital intentó volver a conectarse tras una desconexión y fue rechazada: «MsgSeqNum too low, expecting 4812 but received 1». Nadie lo habría mirado hasta la apertura del lunes. Es lo primero de la lista de la revisión de salud de sesiones FIX que acompaña a este post, un proyecto de código abierto que se ejecuta con datos de ejemplo de un bróker ficticio con su mesa de trading electrónico en Madrid.

FIX es el protocolo por el que viajan las órdenes, las ejecuciones y las copias de operaciones entre un bróker y sus contrapartes. Cada sesión deja un log, y a la revisión solo le hacen falta sus mensajes de sesión: logons y logouts, test requests, peticiones de reenvío, resets de secuencia y rechazos. Un script de PowerShell de solo lectura los saca de los logs del motor, y la revisión lee una semana entera, sesión a sesión, frente a los umbrales de la mesa.

## Lo que se puede haber perdido

El miércoles a las 14:12, la copia de operaciones de Northwind Clearing recibió un reset de secuencia sin gap fill, del 18322 al 18450. Que haya peticiones de reenvío atendidas es normal; un reset así significa que 128 mensajes no se reenviaron nunca, así que hay que conciliar las órdenes y operaciones de esa ventana antes del lunes. Es la segunda línea de la lista.

## Lo que está inestable

La sesión de órdenes de Tailspin Bank se cayó cinco veces sin logout, cuatro de ellas en horario de mercado, y necesitó seis reenvíos para recuperarse. El viernes, el tiempo de ida y vuelta de sus órdenes pasó de unos 4 ms a 38 ms en el percentil 99. Los datos de mercado de Litware necesitaron 14 test requests, casi todos alrededor de la apertura, porque dejaban de llegar sus heartbeats. La sesión de RFQ de Relecloud no se conecta desde el miércoles, Wingtip Prime rechazó 22 asignaciones por una cuenta desconocida y Woodgrove se conecta con un heartbeat de 60 segundos cuando el configurado es de 30.

## Lo que se va a romper solo

El certificado TLS de las dos sesiones de Contoso MTF caduca el jueves, y nadie ha probado nunca el paso de Proseware a la pasarela de respaldo.

La demo saca un 89% de salud de sesiones, 4,8 puntos más que en la revisión anterior, con seis hallazgos rojos y ocho ámbar, cinco sesiones en la lista para antes del lunes a las 08:00 y seis decisiones: revisar la lista una hora antes de la apertura, abrir casos con dos contrapartes, conciliar el reset, renovar los certificados, reservar la prueba de failover y corregir los datos maestros que provocan los rechazos.

## Cómo usarlo con datos reales

El script lee logs al estilo de QuickFIX/J o QuickFIX/n; la lista de sesiones con su contraparte, uso, heartbeat, servidores, prueba de failover y certificado va en un CSV, y la latencia diaria en otro si la monitorización la tiene. El horario de mercado, los umbrales y los límites de latencia son la política de la propia mesa en un fichero de configuración. Funciona con Python y sin dependencias externas, y genera un informe web, un dosier de una página para la mesa y ficheros CSV con cada sesión, día, hallazgo y acción. Los datos de la demo son ficticios: nombres, CompIDs, servidores y horas.

## De dónde sale

La herramienta nace de mantener conectadas las salas de trading: FIX y conectividad de trading electrónico con contrapartes, plataformas de datos de mercado de LSEG y Bloomberg, monitorización y respuesta a incidentes graves, y operación de red."""),
dict(n="61", repo="61-change-freeze-oncall-planner", date="2026-11-23", cat="tools",
 title_en="Three weeks before the freeze, the rota had nobody on call for the network on the weekend after Christmas",
 title_es="A tres semanas de la congelación, la guardia no tenía a nadie de redes el fin de semana después de Navidad",
 seo_title_en="Change freeze and on-call rota review · Iñigo González",
 seo_title_es="Congelación de cambios y guardias · Iñigo González",
 seo_desc="Year-end change freeze review: on-call rota gaps, leave, load and holidays, emergency approvers, changes inside the freeze, runbooks and vendor cover.",
 seo_desc_es="Revisión de la congelación de fin de año: huecos en la guardia, vacaciones, carga y festivos, aprobadores de emergencia, cambios dentro, runbooks y proveedores.",
 dek_en="The review, published with fictional data from a bank with six IT teams, reads the services, the people, their leave, the on-call rota and the changes, and lists what to fix before the freeze starts.",
 dek_es="La revisión, publicada con datos ficticios de un banco con seis equipos de IT, lee los servicios, las personas, sus vacaciones, la guardia y los cambios, y saca lo que hay que arreglar antes de que empiece la congelación.",
 en="""
On Saturday 26 and Sunday 27 December, the network team's rota has a secondary and no primary. Nobody noticed, because the rota is a spreadsheet with one tab per team and nobody reads them all together until the night someone needs them. That is one of the first lines of the change freeze review published with this post. It is an open-source project that runs on sample data from a fictional bank with its IT operations in Madrid.

The freeze in the demo runs from Friday 18 December at 18:00 to Thursday 7 January at 08:00: twenty nights, three of them holidays. The review runs three weeks before, on Monday 30 November, and reads five things together: the services with their tier and support team, the people who can be on call, their leave, the rota and the changes planned around the freeze.

## Who picks up the phone

Every team that runs a service needs a primary every day, and a different secondary if any of its services is critical or high. The report draws it as a calendar, team by team and day by day. Besides the network gap, Marta Gil is on the Identity rota from the 24th to the 28th, exactly the days she is on holiday. Database has no secondary from 30 December to 2 January. Applications has the same person as primary and secondary on 2 January. One name on the network rota is not in the team list at all, and Business Applications, which runs document management, has no rota.

## Whether they can do anything

Jorge Ruiz is primary nine days in a row, Christmas Day and New Year's Day included. Two engineers on call have no phone number on file. Three have not tested remote access from home for months, or ever. The three people who can approve an emergency change are all on leave from 28 December to 1 January, so for five days a fix that needs approval has nobody to approve it.

## What should not be happening

A firewall clean-up was approved for 21 December without anybody calling it an exception. A draft intranet change sits on the 28th. A SQL Server update for 9 December is still waiting for CAB, and the core banking quarterly patch is planned 21 hours before the freeze starts. The payments gateway runbook was last reviewed in March 2025, the network has none, and the core banking vendor answers the phone in business hours only. Two changes are approved freeze exceptions, and the review leaves them alone.

The demo scores 78.3% rota coverage, 13.1 points down on last year's freeze, with five red and seventeen amber findings, twenty-one things to fix before the freeze and six decisions: close the holes in the rota, take four changes to the last CAB, name a deputy emergency approver, rebalance one person's shifts, check phones and remote access, and agree vendor cover.

## How to use it with real data

A read-only PowerShell script takes the changes for the weeks around the freeze from ServiceNow. The services, the people, the leave and the rota go in CSV files, the rota as one row per day or per block of days. Freeze dates, holidays and limits are the organisation's own policy in a settings file. It runs on Python with no external dependencies and produces a web report, a one-page pack for the last CAB before the freeze and CSV files with every team, day, person, change, finding and action. The demo data is fictional: names, services, vendors and changes.

## Where it comes from

The tool comes from running change and release management: process owner for incidents, changes and problems, CAB and go-live reviews, release planning with rollback, runbooks and training, major incident response and DR/BCP tests.""",
 es="""
El sábado 26 y el domingo 27 de diciembre, la guardia del equipo de redes tiene secundario y no tiene primario. Nadie lo había visto, porque la guardia es una hoja de cálculo con una pestaña por equipo y nadie las lee todas juntas hasta la noche en que hacen falta. Es una de las primeras líneas de la revisión de la congelación de cambios que acompaña a este post, un proyecto de código abierto que se ejecuta con datos de ejemplo de un banco ficticio con sus operaciones de IT en Madrid.

La congelación de la demo va del viernes 18 de diciembre a las 18:00 al jueves 7 de enero a las 08:00: veinte noches, tres de ellas festivas. La revisión se hace tres semanas antes, el lunes 30 de noviembre, y lee cinco cosas juntas: los servicios con su nivel y su equipo de soporte, las personas que pueden estar de guardia, sus vacaciones, la guardia y los cambios previstos alrededor de la congelación.

## Quién coge el teléfono

Cada equipo que lleva un servicio necesita un primario cada día, y un secundario distinto si alguno de sus servicios es crítico o alto. El informe lo dibuja como un calendario, equipo a equipo y día a día. Además del hueco de redes, Marta Gil está en la guardia de Identidad del 24 al 28, justo los días que tiene de vacaciones. Bases de datos no tiene secundario del 30 de diciembre al 2 de enero. Aplicaciones tiene a la misma persona de primaria y secundaria el 2 de enero. Un nombre de la guardia de redes ni siquiera está en la lista del equipo, y Aplicaciones de Negocio, que lleva la gestión documental, no tiene guardia.

## Si pueden hacer algo

Jorge Ruiz es primario nueve días seguidos, con Navidad y Año Nuevo incluidos. Dos técnicos de guardia no tienen un teléfono registrado. Tres llevan meses sin probar el acceso remoto desde casa, o no lo han probado nunca. Las tres personas que pueden aprobar un cambio de emergencia están de vacaciones del 28 de diciembre al 1 de enero, así que durante cinco días un arreglo que necesite aprobación no tiene quién lo apruebe.

## Lo que no debería estar pasando

Una limpieza de reglas del cortafuegos se aprobó para el 21 de diciembre sin que nadie la tratara como excepción. Un cambio de la intranet en borrador está puesto el 28. Una actualización de SQL Server para el 9 de diciembre sigue esperando al CAB, y el parche trimestral del core bancario está previsto 21 horas antes de que empiece la congelación. El runbook de la pasarela de pagos se revisó por última vez en marzo de 2025, el de redes no existe y el proveedor del core bancario solo atiende en horario de oficina. Hay dos cambios aprobados como excepción, y la revisión no los toca.

La demo saca un 78,3% de cobertura de la guardia, 13,1 puntos menos que en la congelación del año pasado, con cinco hallazgos rojos y diecisiete ámbar, veintiuna cosas que arreglar antes de la congelación y seis decisiones: cerrar los huecos de la guardia, llevar cuatro cambios al último CAB, nombrar un aprobador de emergencia suplente, repartir mejor los turnos de una persona, comprobar teléfonos y acceso remoto y acordar la cobertura de los proveedores.

## Cómo usarlo con datos reales

Un script de PowerShell de solo lectura saca de ServiceNow los cambios de las semanas alrededor de la congelación. Los servicios, las personas, las vacaciones y la guardia van en ficheros CSV, la guardia con una fila por día o por bloque de días. Las fechas de la congelación, los festivos y los límites son la política de la propia organización en un fichero de configuración. Funciona con Python y sin dependencias externas, y genera un informe web, un dosier de una página para el último CAB antes de la congelación y ficheros CSV con cada equipo, día, persona, cambio, hallazgo y acción. Los datos de la demo son ficticios: nombres, servicios, proveedores y cambios.

## De dónde sale

La herramienta nace de llevar la gestión de cambios y releases: responsable de los procesos de incidencias, cambios y problemas, CAB y revisiones de puesta en producción, planificación de releases con marcha atrás, runbooks y formación, respuesta a incidentes graves y pruebas de DR/BCP."""),

dict(n="62", repo="62-conditional-access-policy-review", date="2026-11-24", cat="tools",
 title_en="A /10 range in the office trusted location let 74 sign-ins through with no Conditional Access policy at all",
 title_es="Un rango /10 en la ubicación de confianza de la oficina dejó pasar 74 accesos sin ninguna política de acceso condicional",
 seo_title_en="Conditional Access policy review · Iñigo González",
 seo_title_es="Revisión de acceso condicional · Iñigo González",
 seo_desc="Conditional Access review against the sign-in log: missing baseline, report-only policies, exclusions, break-glass, trusted locations and legacy auth.",
 seo_desc_es="Revisión del acceso condicional con los inicios de sesión: base que falta, modo informe, exclusiones, break-glass, ubicaciones y autenticación heredada.",
 dek_en="The review, published with fictional data from an insurer with seven policies, reads every Conditional Access policy next to a month of sign-ins and lists what the policies really do.",
 dek_es="La revisión, publicada con datos ficticios de una aseguradora con siete políticas, lee cada política de acceso condicional junto a un mes de inicios de sesión y saca lo que hacen de verdad.",
 en="""
The office is a trusted location, and the MFA policy skips it. Somewhere along the way the location gained a /10 range, and in the last 30 days 74 successful sign-ins from it went through with no enforced policy at all. That is the first thing the Conditional Access review published with this post points at. It is an open-source project that runs on sample data from a fictional insurer.

Conditional Access drifts one reasonable change at a time, and the policies and the sign-in log are rarely read together. The review does exactly that: it takes the policies, the named locations, the users, the groups and a month of sign-ins, all exported read-only from Microsoft Graph, and reads them side by side.

## The baseline

First, four controls the organisation expects to be enforced: MFA for every user and app, legacy authentication blocked, a stronger method for admins and MFA for guests. In the demo two are missing. The policy that blocks legacy authentication has been in report-only since August, and in the period it would have stopped 62 sign-ins of four accounts: a scanner sending mail over SMTP AUTH, a CRM sync reading a mailbox over IMAP and two phones still on Exchange ActiveSync. Guests are excluded from the MFA policy, and the policy written for them is disabled.

## Exclusions and break-glass

The group excluded from MFA started with two service accounts and now has 14 members; seven of them are disabled or have not signed in for three months. One of the two break-glass accounts was left inside the MFA policy, so the day MFA fails it can be locked out too, and it was used on a Saturday afternoon. A helpdesk admin sits in the exclusion group and signs in to the Azure portal with a password only.

## What the sign-in log says

121 successful sign-ins of 33 users went through no enforced policy: 74 from the trusted location, 32 by guests and 15 by excluded accounts. Coverage is worked out per app, so the gaps show where they are: the expense and HR portals, which the device compliance policy does not cover.

The demo scores 86.8% of sign-ins under an enforced policy, 2.8 points down on the last review, with 37.4% using MFA, five red and eight amber findings and six decisions: fix the break-glass exclusion today, move the legacy clients and switch the block on, clean up the exclusions and the trusted location, decide on three policies that do nothing today, bring every admin under the stronger method and cover guests.

## How to use it with real data

A read-only PowerShell script exports the policies with names instead of ids, the named locations, the sign-ins of the period with the result of each policy, the users with their roles and the members of the groups the policies use. The baseline, the limits and the owners are the organisation's own policy in a settings file. It runs on Python with no external dependencies and produces a web report, a one-page pack for the identity and security review and CSV files with every policy, exclusion, user, app, finding and action. The demo data is fictional: names, addresses, apps and figures.

## Where it comes from

The tool comes from running Microsoft 365 and Entra ID day to day: configuring and managing Conditional Access, Global Admin with PIM and just-in-time access, app integration with SAML and SSO, Exchange Online, Intune device compliance and Microsoft Graph with PowerShell.""",
 es="""
La oficina es una ubicación de confianza y la política de MFA la deja fuera. En algún momento la ubicación ganó un rango /10, y en los últimos 30 días 74 inicios de sesión correctos desde ella pasaron sin ninguna política aplicada. Es lo primero que señala la revisión de acceso condicional que acompaña a este post, un proyecto de código abierto que se ejecuta con datos de ejemplo de una aseguradora ficticia.

El acceso condicional se va desviando con cambios que, uno a uno, tienen sentido, y casi nunca se leen juntas las políticas y el registro de inicios de sesión. La revisión hace justo eso: toma las políticas, las ubicaciones con nombre, los usuarios, los grupos y un mes de inicios de sesión, todo exportado en solo lectura desde Microsoft Graph, y los lee lado a lado.

## La base

Primero, cuatro controles que la organización espera tener activos: MFA para todos los usuarios y aplicaciones, autenticación heredada bloqueada, un método más fuerte para los administradores y MFA para los invitados. En la demo faltan dos. La política que bloquea la autenticación heredada está en modo informe desde agosto, y en el periodo habría parado 62 inicios de sesión de cuatro cuentas: un escáner que envía correo por SMTP AUTH, una sincronización del CRM que lee un buzón por IMAP y dos móviles que siguen con Exchange ActiveSync. Los invitados están excluidos de la política de MFA, y la política que se escribió para ellos está desactivada.

## Exclusiones y break-glass

El grupo excluido de MFA empezó con dos cuentas de servicio y hoy tiene 14 miembros; siete están deshabilitados o llevan tres meses sin iniciar sesión. Una de las dos cuentas break-glass se quedó dentro de la política de MFA, así que el día que falle el MFA también puede quedarse bloqueada, y se usó un sábado por la tarde. Un administrador del service desk está en el grupo de exclusión y entra al portal de Azure solo con contraseña.

## Lo que dice el registro de inicios de sesión

121 inicios de sesión correctos de 33 usuarios no pasaron por ninguna política aplicada: 74 desde la ubicación de confianza, 32 de invitados y 15 de cuentas excluidas. La cobertura se calcula por aplicación, así que los huecos se ven donde están: los portales de gastos y de RR. HH., que la política de dispositivo conforme no cubre.

La demo saca un 86,8% de inicios de sesión bajo una política aplicada, 2,8 puntos menos que en la revisión anterior, con un 37,4% usando MFA, cinco hallazgos rojos y ocho ámbar y seis decisiones: arreglar hoy la exclusión de la break-glass, mover los clientes heredados y activar el bloqueo, limpiar las exclusiones y la ubicación de confianza, decidir sobre tres políticas que hoy no hacen nada, meter a todos los administradores en la política del método fuerte y cubrir a los invitados.

## Cómo usarlo con datos reales

Un script de PowerShell de solo lectura exporta las políticas con nombres en lugar de identificadores, las ubicaciones con nombre, los inicios de sesión del periodo con el resultado de cada política, los usuarios con sus roles y los miembros de los grupos que usan las políticas. La base, los límites y los responsables son la política de la propia organización en un fichero de configuración. Funciona con Python y sin dependencias externas, y genera un informe web, un dosier de una página para la revisión de identidad y seguridad y ficheros CSV con cada política, exclusión, usuario, aplicación, hallazgo y acción. Los datos de la demo son ficticios: nombres, direcciones, aplicaciones y cifras.

## De dónde sale

La herramienta nace de llevar Microsoft 365 y Entra ID en el día a día: configurar y gestionar el acceso condicional, administración global con PIM y acceso just-in-time, integración de aplicaciones con SAML y SSO, Exchange Online, cumplimiento de dispositivos con Intune y Microsoft Graph con PowerShell."""),

]
