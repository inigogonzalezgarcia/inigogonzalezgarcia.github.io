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
 title_en="Catching cloud cost drift before the invoice does", title_es="Ver la deriva del gasto cloud antes que la factura",
 seo_title_en="Cloud cost anomalies in AWS and Azure · Iñigo González",
 seo_title_es="Desvíos de coste cloud en AWS y Azure · Iñigo González",
 dek_en="A small Streamlit dashboard for AWS and Azure spend that flags the week that looks wrong.",
 dek_es="Un panel pequeño en Streamlit para el gasto de AWS y Azure que señala la semana que no cuadra.",
 en="""

## The problem
Cloud costs rarely explode overnight. They drift: a test environment left running over a weekend, a service scaled up and never scaled down. By the time the monthly invoice arrives, the money is already spent.

I wanted a view that answers three questions fast: how much are we spending and where, is this week different from last week, and is anything clearly out of line.

## What I built
- A consolidated view of daily spend across AWS and Azure, with filters by provider, environment and department.
- A weekly KPI: the last 7 days against the previous 7.
- An anomaly alert with a probable cause and a suggested action, such as auto-shutdown for idle development instances.

## How it is built
Python, pandas, Plotly and Streamlit. `data_generator.py` creates 90 days of synthetic billing for 10 services, 4 departments and 3 environments, and injects a spike into EC2 / Development in the last week so the detection has something to find.

## Next steps
- Import the CSV exports from AWS Cost Explorer and Azure Cost Management instead of the synthetic data.
- Add a statistical baseline per service, so each service is compared with its own history.
- Set budget thresholds per department.""",
 es="""

## El problema
El gasto cloud casi nunca se dispara de un día para otro. Se desvía poco a poco: un entorno de pruebas encendido todo el fin de semana, un servicio que se escala y nunca se vuelve a bajar. Cuando llega la factura, el dinero ya se ha gastado.

Quería una vista que respondiera rápido a tres preguntas: cuánto gastamos y dónde, si esta semana es distinta de la anterior y si hay algo claramente fuera de lugar.

## Qué he hecho
- Una vista única del gasto diario en AWS y Azure, con filtros por proveedor, entorno y departamento.
- Un KPI semanal: los últimos 7 días frente a los 7 anteriores.
- Una alerta de anomalía con causa probable y acción sugerida, como el apagado automático de instancias de desarrollo ociosas.

## Cómo está hecho
Python, pandas, Plotly y Streamlit. `data_generator.py` crea 90 días de facturación ficticia para 10 servicios, 4 departamentos y 3 entornos, e inyecta un pico en EC2 / Development la última semana para que la detección tenga algo que encontrar.

## Siguientes pasos
- Importar las exportaciones CSV de AWS Cost Explorer y Azure Cost Management en lugar de los datos ficticios.
- Añadir una línea base estadística por servicio, para comparar cada servicio con su propio histórico.
- Fijar umbrales de presupuesto por departamento."""),

dict(n="02", repo="02-intune-compliance-report", date="2026-09-30", cat="tools",
 title_en="An Intune compliance report you can hand to a manager", title_es="Un informe de cumplimiento de Intune que se puede enseñar a dirección",
 seo_title_en="Intune compliance report with Microsoft Graph · Iñigo González",
 seo_title_es="Informe de cumplimiento de Intune con Graph · Iñigo González",
 dek_en="PowerShell pulls the devices from Microsoft Graph, Python turns them into a report and an action list.",
 dek_es="PowerShell saca los dispositivos de Microsoft Graph y Python los convierte en un informe y una lista de acciones.",
 en="""

## The problem
The Intune portal tells you a device is non-compliant. It doesn't give you a one-page answer to "how are we doing, by OS, and which machines do I chase this week?".

## What I built
- `scripts/Export-IntuneDevices.ps1` exports managed devices through Microsoft Graph with a read-only permission.
- A Python report (standard library only) that produces `report.html`: KPIs, compliance by operating system, devices to review and OS versions.
- `action_list.csv`, the list of devices someone actually has to go and fix.

## How it is built
Python with no third-party packages plus PowerShell, which is the split I use for anything Microsoft. `generate_sample_data.py` creates a fictional fleet so the repo runs without a tenant. Seven tests cover the logic.

## What I learned
Keeping the export and the analysis apart pays off: the PowerShell side only needs read access, and the Python side can be tested with fake data.

## Next steps
- Create an app registration with read-only Intune permissions in Microsoft Graph.
- Run `Export-IntuneDevices.ps1` and point the report at the export.
- Schedule it weekly and send the action list to the team that chases devices.""",
 es="""

## El problema
El portal de Intune te dice que un equipo no cumple. No te da en una página la respuesta a "cómo vamos, por sistema operativo, y a qué equipos hay que perseguir esta semana".

## Qué he hecho
- `scripts/Export-IntuneDevices.ps1` exporta los dispositivos gestionados por Microsoft Graph con un permiso de solo lectura.
- Un informe en Python (solo librería estándar) que genera `report.html`: KPIs, cumplimiento por sistema operativo, dispositivos a revisar y versiones de SO.
- `action_list.csv`, la lista de equipos que alguien tiene que ir a arreglar.

## Cómo está hecho
Python sin paquetes de terceros y PowerShell, el reparto que uso para todo lo de Microsoft. `generate_sample_data.py` crea una flota ficticia para que el repo funcione sin tenant. Siete tests cubren la lógica.

## Qué aprendí
Separar la exportación del análisis compensa: la parte de PowerShell solo necesita permisos de lectura y la de Python se prueba con datos falsos.

## Siguientes pasos
- Crear un registro de aplicación con permisos de solo lectura de Intune en Microsoft Graph.
- Ejecutar `Export-IntuneDevices.ps1` y generar el informe a partir de la exportación.
- Programarlo cada semana y enviar la lista de acciones al equipo que persigue los equipos."""),

dict(n="03", repo="03-entra-id-hygiene-audit", date="2026-09-30", cat="tools",
 title_en="Auditing Entra ID hygiene: MFA gaps and forgotten accounts", title_es="Auditar la higiene de Entra ID: huecos de MFA y cuentas olvidadas",
 seo_title_en="Entra ID audit: MFA gaps and stale accounts · Iñigo González",
 seo_title_es="Auditoría de Entra ID: MFA y cuentas olvidadas · Iñigo González",
 dek_en="Admins without MFA, inactive members and stale guests, found in one pass.",
 dek_es="Administradores sin MFA, miembros inactivos e invitados obsoletos, en una sola pasada.",
 en="""

## The problem
Identity debt builds up quietly: an admin who never registered MFA, a leaver whose account is still enabled, guests invited for a project that ended a year ago.

## What I built
An audit that flags four things:
- Admins without MFA.
- Members without MFA.
- Members inactive for more than 90 days.
- Stale guest accounts.

## How it is built
`scripts/Export-EntraUsers.ps1` reads users, their `signInActivity` and the MFA registration report through Microsoft Graph, with `User.Read.All` and `AuditLog.Read.All`. Sign-in activity needs Entra ID P1 or P2, and the README says so. Python does the analysis and the report. Seven tests.

## What I learned
Most of the work is deciding what "inactive" and "stale" mean and writing it down, so the report can be defended when someone asks why their account is on it.

## Next steps
- Grant read-only Graph permissions (`User.Read.All`, `AuditLog.Read.All`) on a tenant with Entra ID P1 or P2.
- Agree with security what "inactive" and "stale" mean in your organisation and set those thresholds.
- Run it monthly and keep each report as evidence for access reviews.""",
 es="""

## El problema
La deuda de identidad crece sin hacer ruido: un administrador que nunca registró MFA, una baja cuya cuenta sigue activa, invitados de un proyecto que acabó hace un año.

## Qué he hecho
Una auditoría que señala cuatro cosas:
- Administradores sin MFA.
- Miembros sin MFA.
- Miembros sin actividad en más de 90 días.
- Cuentas de invitado obsoletas.

## Cómo está hecho
`scripts/Export-EntraUsers.ps1` lee los usuarios, su `signInActivity` y el informe de registro de MFA por Microsoft Graph, con `User.Read.All` y `AuditLog.Read.All`. La actividad de inicio de sesión requiere Entra ID P1 o P2, y el README lo dice. Python hace el análisis y el informe. Siete tests.

## Qué aprendí
Casi todo el trabajo está en decidir qué significa "inactivo" y "obsoleto" y dejarlo escrito, para poder defender el informe cuando alguien pregunte por qué sale su cuenta.

## Siguientes pasos
- Dar permisos de solo lectura en Graph (`User.Read.All`, `AuditLog.Read.All`) en un tenant con Entra ID P1 o P2.
- Acordar con seguridad qué significan "inactivo" y "obsoleto" en tu organización y fijar esos umbrales.
- Ejecutarlo cada mes y guardar cada informe como evidencia para las revisiones de acceso."""),

dict(n="04", repo="04-itsm-kpi-dashboard", date="2026-09-30", cat="tools",
 title_en="Service desk KPIs from a plain ticket export", title_es="KPIs de service desk a partir de una exportación de tickets",
 seo_title_en="Service desk KPIs: SLA, MTTR and backlog · Iñigo González",
 seo_title_es="KPIs del service desk: SLA, MTTR y backlog · Iñigo González",
 dek_en="SLA by priority and team, time to resolve, weekly trend and the open tickets already out of SLA.",
 dek_es="SLA por prioridad y por equipo, tiempo de resolución, tendencia semanal y los tickets abiertos ya fuera de SLA.",
 en="""

## The problem
Every service desk tool has dashboards, but the monthly review usually starts from a CSV export and a spreadsheet. I wanted the same numbers, every time, from that export.

## What I built
A report that reads a ServiceNow-style CSV (number, opened, resolved, priority, category, assignment group, state) and produces:
- SLA compliance by priority and by team.
- Median and mean time to resolve.
- The weekly trend.
- Open tickets already out of SLA, plus `sla_breaches.csv`.

## How it is built
Python, standard library only. The default SLA targets are P1 4 h, P2 8 h, P3 24 h and P4 72 h, and `--sla` changes them. Six tests.

## What I learned
The median tells a different story from the mean: a few very long tickets move the mean a lot, and the median shows what most users actually live with.

## Next steps
- Export your tickets to CSV from ServiceNow or any other tool and map the columns.
- Set your own SLA targets per priority with `--sla`.
- Use the same report every month so the numbers are comparable.""",
 es="""

## El problema
Todas las herramientas de service desk tienen paneles, pero la revisión mensual suele empezar con una exportación CSV y una hoja de cálculo. Quería los mismos números, siempre igual, desde esa exportación.

## Qué he hecho
Un informe que lee un CSV tipo ServiceNow (número, apertura, resolución, prioridad, categoría, grupo asignado, estado) y genera:
- Cumplimiento de SLA por prioridad y por equipo.
- Tiempo de resolución mediano y medio.
- La tendencia semanal.
- Los tickets abiertos ya fuera de SLA, más `sla_breaches.csv`.

## Cómo está hecho
Python, solo librería estándar. Los objetivos por defecto son P1 4 h, P2 8 h, P3 24 h y P4 72 h, y `--sla` los cambia. Seis tests.

## Qué aprendí
La mediana cuenta otra historia que la media: unos pocos tickets muy largos mueven mucho la media, y la mediana enseña lo que vive la mayoría de usuarios.

## Siguientes pasos
- Exportar tus tickets a CSV desde ServiceNow o cualquier otra herramienta y mapear las columnas.
- Fijar tus objetivos de SLA por prioridad con `--sla`.
- Usar el mismo informe cada mes para que las cifras se puedan comparar."""),

dict(n="05", repo="05-it-ops-console", date="2026-09-30", updated="2026-11-08", cat="tools",
 title_en="Rebuilding an on-site IT operations console from scratch", title_es="Rehacer desde cero una consola de operaciones IT de sede",
 seo_title_en="On-site IT ops console: Flask + PowerShell · Iñigo González",
 seo_title_es="Consola de operaciones IT: Flask + PowerShell · Iñigo González",
 dek_en="Assets, warranties, room checklists, joiners and leavers, shifts and service health in one Flask app.",
 dek_es="Activos, garantías, checklists de salas, altas y bajas, turnos y salud de servicios en una app Flask.",
 en="""

## The problem
Running a site means keeping a lot of small things in your head: which machines are offline, which warranties expire, which rooms were checked this morning, who starts on Monday. I wanted all of it in one place, built from scratch and anonymised.

## What I built
- Dashboard, assets (offline, non-compliant, duplicate serials, remote queries), warranties and software.
- People, floor maps, meeting-room checklists, joiners and leavers, visitors and shifts.
- Service health, role-based admin and an audit log.

Access is invite-only: the first admin is created with `bootstrap-admin`, accounts are activated with a 6-character code sent by email, and every sign-in after that needs an authenticator app (TOTP).

## How it is built
Flask and SQLite, with PowerShell over CIM/WinRM for remote queries. ARCHITECTURE.md, docs/decisions.md (PowerShell and WMI lessons) and docs/security.md explain the choices. Sixteen tests.

## Next steps
- Connect LDAP for sign-in and SMTP for the activation emails.
- Enable remote PowerShell (WinRM) for the live device queries.
- Load your asset inventory and floor plans, and adapt the room checklists to your site.""",
 es="""

## El problema
Llevar una sede es tener muchas cosas pequeñas en la cabeza: qué equipos están offline, qué garantías caducan, qué salas se han revisado esta mañana, quién empieza el lunes. Lo quería todo en un sitio, hecho desde cero y anonimizado.

## Qué he hecho
- Panel, activos (offline, no conformes, seriales duplicados, consultas remotas), garantías y software.
- Personas, planos de planta, checklists de salas, altas y bajas, visitas y turnos.
- Salud de servicios, administración por roles y log de auditoría.

El acceso es solo por invitación: el primer administrador se crea con `bootstrap-admin`, las cuentas se activan con un código de 6 caracteres por email y desde entonces cada inicio de sesión pide app autenticadora (TOTP).

## Cómo está hecho
Flask y SQLite, con PowerShell por CIM/WinRM para las consultas remotas. ARCHITECTURE.md, docs/decisions.md (lecciones de PowerShell y WMI) y docs/security.md explican las decisiones. Dieciséis tests.

## Siguientes pasos
- Conectar LDAP para el inicio de sesión y SMTP para los emails de activación.
- Activar PowerShell remoto (WinRM) para las consultas en vivo a los equipos.
- Cargar tu inventario de activos y tus planos, y adaptar los checklists de salas a tu oficina."""),

dict(n="06", repo="06-kubernetes-ingress-lab", date="2026-10-01", updated="2026-11-11", cat="cloud",
 title_en="A Kubernetes ingress lab built from zero in every CI run", title_es="Un laboratorio de ingress en Kubernetes que la CI construye desde cero",
 seo_title_en="Kubernetes ingress lab: Cilium and Envoy · Iñigo González",
 seo_title_es="Laboratorio de ingress en Kubernetes: Cilium y Envoy · Iñigo González",
 dek_en="Cilium, Envoy Gateway, cert-manager and external-dns on kind, with nine end-to-end checks.",
 dek_es="Cilium, Envoy Gateway, cert-manager y external-dns sobre kind, con nueve pruebas de punta a punta.",
 en="""

## Why this lab
Comes from working with container platforms such as Red Hat OpenShift and Kubernetes on premises. In this lab I go deeper into how traffic gets into a cluster today: Gateway API instead of the classic Ingress, eBPF networking, and certificates and DNS handled by controllers.

## What I built
- kind with no CNI and no kube-proxy, replaced by Cilium (LB IPAM, L2 announcements, an L7 policy and Hubble).
- Envoy Gateway with Gateway API: redirect, TLS and rate limiting.
- cert-manager with a lab CA and a wildcard certificate.
- external-dns writing to BIND over RFC 2136 with TSIG, using TXT ownership records.
- Default deny in the apps namespace and an L7 allow-list (`/env` returns 403), with no way around the gateway.

## How it is tested
A GitHub Actions workflow builds the cluster from scratch and runs nine end-to-end tests. It has been green in the last four runs.

## Next steps
- Replace kind with your own cluster and BIND with your DNS provider in external-dns.
- Swap the lab CA for ACME or your internal PKI in cert-manager.
- Contribute back: docs or a good first issue in one of these projects is the next step on my side.""",
 es="""

## Por qué este laboratorio
Viene de trabajar con plataformas de contenedores como Red Hat OpenShift y Kubernetes en local. En este laboratorio profundizo en cómo entra hoy el tráfico en un clúster: Gateway API en lugar del Ingress clásico, red con eBPF, y certificados y DNS gestionados por controladores.

## Qué he hecho
- kind sin CNI ni kube-proxy, sustituidos por Cilium (LB IPAM, anuncios L2, una política L7 y Hubble).
- Envoy Gateway con Gateway API: redirección, TLS y limitación de peticiones.
- cert-manager con una CA del laboratorio y un certificado wildcard.
- external-dns escribiendo en BIND por RFC 2136 con TSIG y registros TXT de propiedad.
- Denegación por defecto en el namespace de las apps y lista blanca L7 (`/env` devuelve 403), sin forma de saltarse el gateway.

## Cómo se prueba
Un workflow de GitHub Actions construye el clúster desde cero y pasa nueve pruebas de punta a punta. Ha salido en verde en las cuatro últimas ejecuciones.

## Siguientes pasos
- Cambiar kind por tu clúster y BIND por tu proveedor de DNS en external-dns.
- Cambiar la CA del laboratorio por ACME o tu PKI interna en cert-manager.
- Contribuir de vuelta: documentación o una good first issue en alguno de estos proyectos es mi siguiente paso."""),

dict(n="07", repo="07-aws-private-connectivity", date="2026-10-01", cat="cloud",
 title_en="Private connectivity on AWS with Terraform, and the bug CI caught", title_es="Conectividad privada en AWS con Terraform, y el fallo que pilló la CI",
 seo_title_en="AWS PrivateLink and private DNS with Terraform · Iñigo González",
 seo_title_es="AWS PrivateLink y DNS privado con Terraform · Iñigo González",
 dek_en="PrivateLink, private DNS and SSM endpoints in five modules, tested without an AWS account.",
 dek_es="PrivateLink, DNS privado y endpoints de SSM en cinco módulos, probados sin cuenta de AWS.",
 en="""

## Why this lab
Comes from operating a hybrid AWS and Azure environment, where a common need is reaching a service privately, with no internet gateway and no NAT. This lab builds that pattern end to end with Terraform.

## What I built
Five Terraform modules:
- A private VPC with flow logs.
- An internal NLB with an endpoint service that requires acceptance and explicit principals.
- An interface endpoint with a narrow security group.
- A private Route 53 zone with an alias and query logs.
- SSM and S3 endpoints, plus a lab with two test instances (IMDSv2, no public IP, Session Manager).

## How it is tested
`terraform test` with a mocked AWS provider (5 tests) and a GitHub Actions pipeline with fmt, validate, test and tfsec, all green. The estimated cost of running the lab is about $0.11 an hour.

## What I learned
Running CI with Terraform caught a real bug that OpenTofu didn't flag: a `for_each` over IDs that are unknown at plan time. It is fixed and written up in docs/decisions.md.

## Next steps
- Run `terraform apply` in a sandbox AWS account (the lab costs around $0.11 per hour).
- Plug in your own VPCs, allowed principals and private DNS zone.
- Keep the CI checks (fmt, validate, test, tfsec) in your pipeline.""",
 es="""

## Por qué este laboratorio
Viene de operar un entorno híbrido con AWS y Azure, donde una necesidad habitual es llegar a un servicio de forma privada, sin internet gateway y sin NAT. Este laboratorio construye ese patrón de principio a fin con Terraform.

## Qué he hecho
Cinco módulos de Terraform:
- Una VPC privada con flow logs.
- Un NLB interno con un endpoint service que exige aceptación y principals explícitos.
- Un interface endpoint con un security group estrecho.
- Una zona privada de Route 53 con alias y logs de consultas.
- Endpoints de SSM y S3, más un laboratorio con dos instancias de prueba (IMDSv2, sin IP pública, Session Manager).

## Cómo se prueba
`terraform test` con el proveedor de AWS simulado (5 tests) y un pipeline de GitHub Actions con fmt, validate, test y tfsec, todo en verde. Tener el laboratorio encendido cuesta unos 0,11 $ la hora.

## Qué aprendí
La CI con Terraform encontró un fallo real que OpenTofu no marcó: un `for_each` sobre IDs que no se conocen en el plan. Está corregido y explicado en docs/decisions.md.

## Siguientes pasos
- Ejecutar `terraform apply` en una cuenta de AWS de pruebas (el laboratorio cuesta unos 0,11 $ por hora).
- Conectar tus VPC, los principals permitidos y tu zona DNS privada.
- Mantener las comprobaciones de CI (fmt, validate, test, tfsec) en tu pipeline."""),

dict(n="08", repo="08-edge-health-slo-monitor", date="2026-10-01", cat="cloud",
 title_en="SLOs and burn-rate alerts for the edge, in plain Python", title_es="SLO y alertas por burn rate para el edge, en Python sin dependencias",
 seo_title_en="SLOs and burn-rate alerts in Python · Iñigo González",
 seo_title_es="SLO y alertas por burn rate en Python · Iñigo González",
 dek_en="DNS, TLS, HTTP and TCP probes, an error budget and a fictional postmortem.",
 dek_es="Sondas DNS, TLS, HTTP y TCP, un presupuesto de error y un postmortem ficticio.",
 en="""

## Why this lab
Comes from years of monitoring and alert response with tools such as Grafana, SolarWinds and the Elastic stack. This lab applies the SRE approach to the edge: wake someone up when the error budget is burning too fast, not on every failed check.

## What I built
- DNS, TLS, HTTP and TCP probes.
- An SLO with an error budget and multi-window burn-rate alerts, with a minimum number of bad probes before firing.
- Export to Elasticsearch (ECS) and Prometheus, a signed webhook and an HTML report.
- A postmortem template and a fictional postmortem: a DNS record lost during a zone migration.

## How it is built
Python 3.11, standard library only, 14 tests.

## Next steps
- Send the results to your Elasticsearch or Prometheus.
- Install the systemd units on a small VM close to your users.
- Connect the signed webhook to n8n, Teams or Slack, and agree the SLOs with the service owners.""",
 es="""

## Por qué este laboratorio
Viene de años de monitorización y respuesta a alertas con herramientas como Grafana, SolarWinds y el stack de Elastic. Este laboratorio aplica el enfoque SRE al edge: despertar a alguien cuando el presupuesto de error se consume demasiado rápido, no en cada comprobación fallida.

## Qué he hecho
- Sondas DNS, TLS, HTTP y TCP.
- Un SLO con presupuesto de error y alertas multiventana por burn rate, con un mínimo de sondas malas antes de avisar.
- Exportación a Elasticsearch (ECS) y Prometheus, un webhook firmado y un informe HTML.
- Una plantilla de postmortem y un postmortem ficticio: un registro DNS perdido en una migración de zona.

## Cómo está hecho
Python 3.11, solo librería estándar, 14 tests.

## Siguientes pasos
- Enviar los resultados a tu Elasticsearch o Prometheus.
- Instalar las units de systemd en una VM pequeña cerca de tus usuarios.
- Conectar el webhook firmado a n8n, Teams o Slack, y acordar los SLO con los responsables del servicio."""),

dict(n="09", repo="09-gpu-node-remediation", date="2026-10-01", cat="gpu",
 title_en="Teaching a Kubernetes controller to drain, repair or quarantine GPU nodes", title_es="Un controlador de Kubernetes que drena, repara o pone en cuarentena nodos GPU",
 seo_title_en="Kubernetes GPU node remediation controller · Iñigo González",
 seo_title_es="Controlador de remediación de nodos GPU · Iñigo González",
 dek_en="First GPU lab: XID errors, ECC and temperature drive each node through a state machine.",
 dek_es="Primer laboratorio de GPU: los XID, el ECC y la temperatura llevan cada nodo por una máquina de estados.",
 en="""

## Why this lab
Comes from hardware operations: validating and certifying servers, and automating the detection and remediation of hardware failures. This is the first of a series of labs that applies that to GPU fleets. It runs on simulated GPUs, so anyone can reproduce it on a laptop.

## What I built
A Kubernetes controller in Go (standard library only, no client-go) that reads DCGM metrics (XID errors, double-bit ECC, row remapping, temperature) and moves each node through Healthy → Draining → Repairing → Validating → Healthy, or to Cordoned for thermal issues, or Quarantined.
- State is kept in node annotations, with a budget of nodes in remediation (max-unavailable).
- Evictions respect PodDisruptionBudgets, and validation runs as a Job pinned to the node with all its GPUs.
- A repeat-offender rule, dry-run mode, events and Prometheus metrics.
- The XID policy is based on NVIDIA's documentation (docs/xid-policy.md).

## How it is tested
A `gpu-sim` simulator stands in for dcgm-exporter. CI runs unit tests, shellcheck and an end-to-end test on kind with 8 scenarios (28 checks), green on the first run. There is also a `gpuremediate check` mode that uses nvidia-smi on a real GPU.

## Next steps
- On a cluster with GPUs, deploy dcgm-exporter instead of the simulator.
- Start in dry-run mode and set the budget of nodes in remediation (max-unavailable).
- `gpuremediate check` runs on any machine with `nvidia-smi`, including a Windows workstation.""",
 es="""

## Por qué este laboratorio
Viene de la operación de hardware: validar y certificar servidores, y automatizar la detección y la reparación de fallos de hardware. Es el primero de una serie de laboratorios que lleva eso a las flotas de GPU. Funciona con GPU simuladas, así que cualquiera puede reproducirlo en un portátil.

## Qué he hecho
Un controlador de Kubernetes en Go (solo librería estándar, sin client-go) que lee métricas DCGM (errores XID, ECC de doble bit, row remapping, temperatura) y lleva cada nodo por Healthy → Draining → Repairing → Validating → Healthy, o a Cordoned por temperatura, o a Quarantined.
- El estado vive en anotaciones del nodo, con un presupuesto de nodos en remediación (max-unavailable).
- Las evicciones respetan los PodDisruptionBudget y la validación es un Job fijado al nodo con todas sus GPU.
- Regla de reincidencia, modo dry-run, eventos y métricas de Prometheus.
- La política de XID se basa en la documentación de NVIDIA (docs/xid-policy.md).

## Cómo se prueba
Un simulador `gpu-sim` hace de dcgm-exporter. La CI pasa tests unitarios, shellcheck y una prueba de punta a punta en kind con 8 escenarios (28 comprobaciones), en verde a la primera. Hay además un modo `gpuremediate check` que usa nvidia-smi en una GPU real.

## Siguientes pasos
- En un clúster con GPU, desplegar dcgm-exporter en lugar del simulador.
- Empezar en modo dry-run y fijar el presupuesto de nodos en reparación (max-unavailable).
- `gpuremediate check` funciona en cualquier máquina con `nvidia-smi`, también en un puesto Windows."""),

dict(n="10", repo="10-gpu-fleet-observability", date="2026-10-01", cat="gpu",
 title_en="Observability for a GPU fleet: alerts that say what to do", title_es="Observabilidad de una flota de GPU: alertas que dicen qué hacer",
 seo_title_en="GPU fleet observability with dcgm-exporter · Iñigo González",
 seo_title_es="Observabilidad de una flota GPU con dcgm-exporter · Iñigo González",
 dek_en="Recording rules, alerts with runbooks, Alertmanager routing and a Grafana dashboard on DCGM metrics.",
 dek_es="Recording rules, alertas con runbook, rutas de Alertmanager y un dashboard de Grafana sobre métricas DCGM.",
 en="""

## Why this lab
Builds on years of monitoring and Grafana dashboards. Here the metrics come from NVIDIA DCGM, and the question is which ones deserve an alert and who should get it.

## What I built
- A Go simulator with 4 nodes × 8 GPUs that uses dcgm-exporter's metric names and labels, pod and namespace included, plus fault injection.
- 17 recording rules and 10 alerts, each with a runbook (docs/alerts.md) and an `action` label: drain, quarantine or cordon.
- Alertmanager with pager, ticket and team routes, and inhibitions so a broken GPU doesn't also alert the team about an "idle GPU".
- A Grafana dashboard generated by a script, and `fleetreport` with GPU-hours and idle GPU-hours per namespace.

## How it is tested
7 `promtool test rules` cases, Go tests, config checks, shellcheck and an end-to-end run with Docker Compose (Prometheus, Alertmanager, Grafana): 32 checks, green on the first run.

## What I learned
The energy-versus-power check gave false failures with a single sample because of scrape jitter. It now uses 1 minute of rate over 2 minutes of data.

## Next steps
- Replace the simulator with dcgm-exporter on your nodes.
- Import the Grafana dashboard and the recording rules.
- Route the alerts in Alertmanager to your on-call and ticketing tools.""",
 es="""

## Por qué este laboratorio
Se apoya en años de monitorización y cuadros de Grafana. Aquí las métricas vienen de NVIDIA DCGM, y la pregunta es cuáles merecen una alerta y quién debe recibirla.

## Qué he hecho
- Un simulador en Go de 4 nodos × 8 GPU que usa los nombres y etiquetas de métricas de dcgm-exporter, pod y namespace incluidos, con inyección de fallos.
- 17 recording rules y 10 alertas, cada una con su runbook (docs/alerts.md) y una etiqueta `action`: drain, quarantine o cordon.
- Alertmanager con rutas a guardia, ticket y equipo, e inhibiciones para que una GPU rota no avise además de "GPU ociosa" al equipo.
- Un dashboard de Grafana generado por script y `fleetreport` con GPU-horas y GPU-horas ociosas por namespace.

## Cómo se prueba
7 casos de `promtool test rules`, tests en Go, comprobaciones de configuración, shellcheck y una prueba de punta a punta con Docker Compose (Prometheus, Alertmanager, Grafana): 32 comprobaciones, en verde a la primera.

## Qué aprendí
La comprobación de energía frente a potencia daba falsos fallos con una sola muestra por el jitter del scrape. Ahora usa 1 minuto sobre 2 minutos de datos.

## Siguientes pasos
- Cambiar el simulador por dcgm-exporter en tus nodos.
- Importar el cuadro de Grafana y las recording rules.
- Enrutar las alertas de Alertmanager a tus herramientas de guardia y de tickets."""),

dict(n="11", repo="11-gpu-fleet-lifecycle", date="2026-10-02", cat="gpu",
 title_en="Rolling a GPU driver across a fleet: canary, approval, rollback", title_es="Desplegar un driver de GPU por la flota: canary, aprobación y rollback",
 seo_title_en="GPU driver rollout: canary and rollback · Iñigo González",
 seo_title_es="Despliegue de drivers GPU: canary y rollback · Iñigo González",
 dek_en="A Go controller that upgrades nodes in batches and backs out on its own when something breaks.",
 dek_es="Un controlador en Go que actualiza nodos por lotes y da marcha atrás solo cuando algo falla.",
 en="""

## Why this lab
Builds on release management: planning, testing, rollback and validation after each release, applied to rolling a GPU driver across a fleet. In production the GPU Operator's own upgrade controller does this job; the lab shows what it has to get right.

## What I built
A Go controller (standard library only) that rolls a driver version across the fleet:
- Canary, human approval by rollout name, batches, a maintenance window, pause and abort, and a failure budget.
- maxUnavailable also counts nodes that are out for other reasons, such as the quarantine and remediation from lab 09.
- Each node goes Draining → Installing → Validating → Soaking → Done. A hardware XID or ECC error during the soak counts as a failure.
- On failure it rolls back to the previous version, and if that also fails, it quarantines the node with lab 09's label.

## How it is tested
The plan lives in a validated ConfigMap where unknown fields are errors. CI runs 12 controller unit tests, shellcheck and an end-to-end test on kind with 4 workers: 26 checks, green on the first run, including a closed window, a bad driver stopped at the canary and an XID during the soak with rollback.

## Next steps
- Use the lab to rehearse your rollout policy: canary, approval, batches and rollback.
- Apply the same policy with the GPU Operator's upgrade controller on your clusters.
- Reuse the quarantine label from lab 09, so a node that fails twice is taken out of service.""",
 es="""

## Por qué este laboratorio
Se apoya en la gestión de releases: planificación, pruebas, vuelta atrás y validación después de cada despliegue, aplicadas a actualizar el driver de GPU en toda una flota. En producción lo hace el controlador de actualización del propio GPU Operator; el laboratorio enseña lo que tiene que hacer bien.

## Qué he hecho
Un controlador en Go (solo librería estándar) que despliega una versión de driver por la flota:
- Canary, aprobación humana por nombre de rollout, lotes, ventana de mantenimiento, pausa y aborto, y presupuesto de fallos.
- maxUnavailable cuenta también los nodos que están fuera por otros motivos, como la cuarentena y la remediación del laboratorio 09.
- Cada nodo pasa por Draining → Installing → Validating → Soaking → Done. Un XID de hardware o un error ECC durante el soak cuenta como fallo.
- Si falla, vuelve a la versión anterior y, si eso también falla, pone el nodo en cuarentena con la etiqueta del laboratorio 09.

## Cómo se prueba
El plan vive en un ConfigMap validado donde los campos desconocidos son error. La CI pasa 12 tests unitarios del controlador, shellcheck y una prueba de punta a punta en kind con 4 workers: 26 comprobaciones, en verde a la primera, con ventana cerrada, un driver malo parado en el canary y un XID en el soak con rollback.

## Siguientes pasos
- Usar el laboratorio para ensayar tu política de despliegue: canary, aprobación, lotes y vuelta atrás.
- Aplicar la misma política con el controlador de actualización del GPU Operator en tus clústeres.
- Reutilizar la etiqueta de cuarentena del laboratorio 09, para que un nodo que falla dos veces salga de servicio."""),

dict(n="12", repo="12-gpu-goodput-mtbi", date="2026-10-02", cat="gpu",
 title_en="Where do the GPU-hours go? A goodput simulator", title_es="¿Adónde van las GPU-horas? Un simulador de goodput",
 seo_title_en="GPU goodput and MTBI simulator · Iñigo González",
 seo_title_es="Simulador de goodput y MTBI en GPU · Iñigo González",
 dek_en="A 1,024-GPU training job, simulated with failures, to see what checkpoints, spares and fast detection are worth.",
 dek_es="Un entrenamiento de 1.024 GPU simulado con fallos, para ver cuánto valen los checkpoints, los spares y la detección rápida.",
 en="""

## Why this lab
Builds on availability and capacity management and on post-incident reviews. In a large training job failures are normal; what matters is how much useful work survives them, and this lab puts numbers on it.

## What I built
- A discrete-event simulator of a 1,024-GPU job (128 nodes) with spares, failure causes with their own detection time, and repairs.
- An analyser that reads a JSONL event log and splits every GPU-hour into productive, checkpoint, lost work, detection, waiting for nodes and restart, charging the cost to each cause.
- MTBI and per-node MTBF, the Young and Daly formulas for checkpoint intervals, a goodput SLO with an error budget and an HTML report with SVG charts.

## What the numbers say
Seven scenarios, 20 seeds each: baseline 79.6 %, Daly's interval 85.1 %, asynchronous checkpoints 91.7 %, no spares 36.1 %, a firmware regression 73.5 %, and everything combined 94.0 %. The assumptions sit between two public references, Llama 3's interruption count and Meta's paper on cluster reliability.

## How it is tested
34 unit tests on Python 3.11 to 3.13, and a CI job that regenerates docs/results.md and fails if it changes.

## Next steps
- Export your own job events in the documented JSONL format to see where your GPU-hours go.
- Use the Young and Daly formulas to tune the checkpoint interval.
- Track goodput as an SLO with an error budget.""",
 es="""

## Por qué este laboratorio
Se apoya en la gestión de disponibilidad y capacidad y en las revisiones post-incidente. En un entrenamiento grande los fallos son normales; lo que importa es cuánto trabajo útil sobrevive a ellos, y este laboratorio le pone números.

## Qué he hecho
- Un simulador de eventos discretos de un trabajo de 1.024 GPU (128 nodos) con spares, causas de fallo con su propio tiempo de detección y reparaciones.
- Un analizador que lee un log de eventos JSONL y reparte cada GPU-hora en productivo, checkpoint, trabajo perdido, detección, espera de nodos y reinicio, cargando el coste a cada causa.
- MTBI y MTBF por nodo, las fórmulas de Young y Daly para el intervalo de checkpoint, un SLO de goodput con presupuesto de error y un informe HTML con gráficos SVG.

## Lo que dicen los números
Siete escenarios con 20 semillas cada uno: base 79,6 %, intervalo de Daly 85,1 %, checkpoints asíncronos 91,7 %, sin spares 36,1 %, regresión de firmware 73,5 % y todo combinado 94,0 %. Los supuestos están entre dos referencias públicas: las interrupciones de Llama 3 y el paper de Meta sobre fiabilidad de clústeres.

## Cómo se prueba
34 tests unitarios en Python 3.11 a 3.13 y un job de CI que regenera docs/results.md y falla si cambia.

## Siguientes pasos
- Exportar los eventos de tus trabajos en el formato JSONL documentado para ver adónde van tus GPU-horas.
- Usar las fórmulas de Young y Daly para ajustar el intervalo de checkpoints.
- Seguir el goodput como un SLO con presupuesto de error."""),

dict(n="13", repo="13-cluster-acceptance-burnin", date="2026-10-04", cat="gpu",
 title_en="From handover to sign-off: accepting a new GPU cluster", title_es="Del handover a la firma: aceptar un clúster de GPU nuevo",
 seo_title_en="GPU cluster acceptance and burn-in tests · Iñigo González",
 seo_title_es="Aceptación y burn-in de un clúster GPU · Iñigo González",
 dek_en="Inventory, diagnostics, NCCL tests and a 72-hour burn-in, ending in a report a customer can sign.",
 dek_es="Inventario, diagnósticos, pruebas NCCL y un burn-in de 72 horas, con un informe que el cliente puede firmar.",
 en="""

## Why this lab
Accepting new hardware and running go-live and service-acceptance reviews are part of my IT operations work. This lab applies the same discipline to a GPU cluster, from handover to the customer's signature.

## What I built
A pipeline that runs inventory (GPU, driver, VBIOS, InfiniBand ports) → `dcgmi diag -r 3` → nccl-tests per node → per rack → a 72-hour burn-in → a whole-cluster burn-in job scored with lab 12's rules.
- A node stops at its first failure, and every failure gets a disposition (RMA, firmware, fabric, facility, investigate, collect evidence), an owner and a next step.
- Criteria live in criteria.toml, and unknown keys are errors.
- A second round replaces the evidence of the first.
- Outputs: report.md and report.html for the customer (verdict, rack × node grid, punch list, criteria and a signature table), punch-list.csv and result.json.

## The example
A fictional cluster with 4 racks × 8 nodes × 8 GPUs and 8 defects. Round 1 ends NOT READY with 144 of 256 GPUs. After round 2 it is READY with 248, and one node is still waiting on an RMA.

## How it is tested
25 tests, and a CI job that runs both rounds and requires NOT READY and then READY.

## Next steps
- Write your acceptance criteria in `criteria.toml`.
- Collect the real `dcgmi diag` and nccl-tests output with the commands that `accept plan` prints.
- Hand the HTML report and the punch list to the customer for sign-off.""",
 es="""

## Por qué este laboratorio
Aceptar hardware nuevo y llevar revisiones de puesta en producción y aceptación del servicio forman parte de mi trabajo en operaciones IT. Este laboratorio aplica la misma disciplina a un clúster de GPU, de la entrega a la firma del cliente.

## Qué he hecho
Un proceso que pasa por inventario (GPU, driver, VBIOS, puertos InfiniBand) → `dcgmi diag -r 3` → nccl-tests por nodo → por rack → burn-in de 72 horas → un trabajo de burn-in de todo el clúster medido con las reglas del laboratorio 12.
- Un nodo se para en su primer fallo, y cada fallo tiene disposición (RMA, firmware, fabric, instalaciones, investigar, recoger evidencia), responsable y siguiente paso.
- Los criterios están en criteria.toml, y las claves desconocidas son error.
- Una segunda ronda sustituye la evidencia de la primera.
- Salidas: report.md y report.html para el cliente (veredicto, rejilla rack × nodo, lista de pendientes, criterios y tabla de firmas), punch-list.csv y result.json.

## El ejemplo
Un clúster ficticio de 4 racks × 8 nodos × 8 GPU con 8 defectos. La ronda 1 acaba NO LISTO con 144 de 256 GPU. Tras la ronda 2 queda LISTO con 248, y un nodo sigue esperando un RMA.

## Cómo se prueba
25 tests y un job de CI que corre las dos rondas y exige NO LISTO y después LISTO.

## Siguientes pasos
- Escribir tus criterios de aceptación en `criteria.toml`.
- Recoger la salida real de `dcgmi diag` y nccl-tests con los comandos que imprime `accept plan`.
- Entregar al cliente el informe HTML y la punch list para la firma."""),

dict(n="14", repo="14-slurm-gpu-ops", date="2026-10-04", cat="gpu",
 title_en="A real Slurm cluster in Docker Compose, with GPU health checks", title_es="Un clúster Slurm real en Docker Compose, con health checks de GPU",
 seo_title_en="Slurm GPU cluster in Docker with health checks · Iñigo González",
 seo_title_es="Clúster Slurm con GPU en Docker y health checks · Iñigo González",
 dek_en="Drain, requeue and validate, and four CI iterations to get cgroups v2 working.",
 dek_es="Drain, requeue y validate, y cuatro iteraciones de CI para que funcionen los cgroups v2.",
 en="""

## Why this lab
Builds on running Linux (Red Hat) servers. Many GPU clusters run Slurm rather than Kubernetes, so this lab brings the XID policy from lab 09 to a real Slurm cluster.

## What I built
- Slurm 23.11 from Ubuntu 24.04 packages in Docker Compose: MariaDB, slurmdbd, slurmctld and 4 nodes with 4 simulated GPUs each.
- `gpuops health` as the HealthCheckProgram every 10 seconds: cordon (drain and let jobs finish), drain (drain and requeue) or quarantine. It never resumes a node and respects a drain reason set by a human.
- `gpuops validate`: a maintenance reservation, resume, a burn-in on every GPU, then release or drain again.
- A two-node training job with checkpoints on shared storage that hangs, rather than fails, on a hardware XID.
- `gpuops events` joins sacct, the job log and the health-check log into lab 12's event format.

## How it is tested
CI: 36 checks in about 7 minutes. XID 79 drains the node in 2 seconds and requeues the job; the job finishes its 150 steps; sacct shows REQUEUED, REQUEUED, COMPLETED. The real files from that run are kept as fixtures.

## What I learned
It took four CI iterations to get cgroups v2 working without systemd, and the requeue delay was 60 to 80 seconds. Both are written up in docs/design.md.

## Next steps
- On real nodes, switch the health source to `nvidia-smi` and the kernel log.
- Enable cgroup isolation for the GPUs.
- Run NHC (Node Health Check) alongside the GPU health check.""",
 es="""

## Por qué este laboratorio
Se apoya en la administración de servidores Linux (Red Hat). Muchos clústeres de GPU usan Slurm en lugar de Kubernetes, así que este laboratorio lleva la política XID del laboratorio 09 a un Slurm real.

## Qué he hecho
- Slurm 23.11 con paquetes de Ubuntu 24.04 en Docker Compose: MariaDB, slurmdbd, slurmctld y 4 nodos con 4 GPU simuladas cada uno.
- `gpuops health` como HealthCheckProgram cada 10 segundos: cordon (drenar y dejar que acaben los trabajos), drain (drenar y reencolar) o cuarentena. Nunca reactiva un nodo y respeta el motivo de un drain puesto por una persona.
- `gpuops validate`: reserva de mantenimiento, resume, burn-in en todas las GPU y después libera o vuelve a drenar.
- Un entrenamiento de dos nodos con checkpoints en almacenamiento compartido que se cuelga, en lugar de fallar, ante un XID de hardware.
- `gpuops events` une sacct, el log del trabajo y el del health check en el formato de eventos del laboratorio 12.

## Cómo se prueba
CI: 36 comprobaciones en unos 7 minutos. El XID 79 drena el nodo en 2 segundos y reencola el trabajo; el trabajo termina sus 150 pasos; sacct muestra REQUEUED, REQUEUED, COMPLETED. Los ficheros reales de esa ejecución se guardan como fixtures.

## Qué aprendí
Hicieron falta cuatro iteraciones de CI para que funcionaran los cgroups v2 sin systemd, y el reencolado tardaba entre 60 y 80 segundos. Las dos cosas están en docs/design.md.

## Siguientes pasos
- En nodos reales, cambiar la fuente de salud a `nvidia-smi` y el log del kernel.
- Activar el aislamiento por cgroups de las GPU.
- Ejecutar NHC (Node Health Check) junto al chequeo de salud de GPU."""),

dict(n="15", repo="15-multi-tenant-gpu-scheduling", date="2026-10-05", cat="gpu",
 title_en="Sharing GPUs between teams with Kueue and KAI Scheduler", title_es="Repartir GPU entre equipos con Kueue y KAI Scheduler",
 seo_title_en="Multi-tenant GPU scheduling: Kueue and KAI · Iñigo González",
 seo_title_es="GPU compartidas entre equipos: Kueue y KAI · Iñigo González",
 dek_en="One quota agreement in a TOML file, rendered into both schedulers and tested on kind.",
 dek_es="Un acuerdo de cuotas en un fichero TOML, traducido a los dos planificadores y probado en kind.",
 en="""

## Why this lab
Builds on capacity management and on SLA and OLA agreements between teams that share the same infrastructure. When several teams share a GPU cluster, the key is the agreement: who is guaranteed what, who can borrow, and what happens when the owner wants it back.

## What I built
- `tenancy.toml` with three teams: training (16 guaranteed, 8 can be borrowed), research (8 + 8) and inference (8, never lent).
- `python -m tenancy render` turns it into Kueue ClusterQueues in a cohort and KAI Scheduler Queues. CI fails if the manifests drift from the file.
- A kind cluster with 4 workers × 8 GPUs simulated by Run:ai's fake-gpu-operator, plus KubeVirt.

## How it is tested
Kueue, 22 checks: borrowing, reclaim, priority within a team and all-or-nothing admission. KAI, 19 checks: two pods sharing one GPU at 0.5 each, over-quota, reclaim and gang scheduling. KubeVirt, 5 checks: a VM boots with QEMU emulation and the team's ResourceQuota rejects a second one.

## What I learned
Three rounds of fixes after the first CI run, written up in docs/decisions.md: queue usage is reported with a delay, the preemption reason is in a condition, and fractional GPUs are passed as text.

## Next steps
- Describe your teams and quotas in `tenancy.toml` and render the manifests for Kueue or KAI Scheduler.
- Add fair sharing and topology-aware scheduling as the cluster grows.
- Review the agreement with the teams every quarter.""",
 es="""

## Por qué este laboratorio
Se apoya en la gestión de capacidad y en los acuerdos de SLA y OLA entre equipos que comparten la misma infraestructura. Cuando varios equipos comparten un clúster de GPU, la clave es el acuerdo: quién tiene qué garantizado, quién puede pedir prestado y qué pasa cuando el dueño lo quiere de vuelta.

## Qué he hecho
- `tenancy.toml` con tres equipos: training (16 garantizadas, 8 prestables), research (8 + 8) e inference (8 que nunca presta).
- `python -m tenancy render` lo convierte en ClusterQueues de Kueue dentro de una cohort y en Queues de KAI Scheduler. La CI falla si los manifiestos no coinciden con el fichero.
- Un clúster kind con 4 workers × 8 GPU simuladas por el fake-gpu-operator de Run:ai, más KubeVirt.

## Cómo se prueba
Kueue, 22 comprobaciones: préstamo, recuperación, prioridad dentro del equipo y admisión todo o nada. KAI, 19: dos pods compartiendo una GPU a 0,5 cada uno, exceso de cuota, recuperación y gang scheduling. KubeVirt, 5: una VM arranca con emulación QEMU y la ResourceQuota del equipo rechaza una segunda.

## Qué aprendí
Tres rondas de arreglos tras la primera CI, explicadas en docs/decisions.md: el uso de las colas se informa con retraso, el motivo de la preemption está en una condición y las GPU fraccionarias se pasan como texto.

## Siguientes pasos
- Describir tus equipos y cuotas en `tenancy.toml` y generar los manifiestos para Kueue o KAI Scheduler.
- Añadir fair sharing y planificación según topología a medida que crece el clúster.
- Revisar el acuerdo con los equipos cada trimestre."""),

dict(n="16", repo="16-gitops-gpu-fleet", date="2026-10-09", cat="gpu",
 title_en="Promoting GPU Operator releases from staging to prod with Flux", title_es="Promocionar versiones del GPU Operator de staging a prod con Flux",
 seo_title_en="GitOps GPU fleet: GPU Operator with Flux · Iñigo González",
 seo_title_es="Flota GPU con GitOps: GPU Operator y Flux · Iñigo González",
 dek_en="One file defines releases and clusters; Git and Flux do the rest, with a gate before production.",
 dek_es="Un fichero define versiones y clústeres; Git y Flux hacen el resto, con una puerta antes de producción.",
 en="""

## Why this lab
Builds on Git, CI/CD pipelines and release management, and ties several earlier labs together: how to upgrade the GPU software stack across a fleet of clusters from Git, with a gate before production.

## What I built
- `fleet.toml` defines releases (GPU Operator, Network Operator and driver versions, plus one release that fails on purpose) and clusters with GPU pools.
- Waves go staging → prod H100 → prod A100, with a pause after the canary.
- `python -m fleet render` writes each cluster's folder, and Flux applies it in three steps: operators → config → lifecycle. The lifecycle step is lab 11's controller, with its rollout plan generated from the same file.
- `fleet start / promote / approve` each edit one line, `fleet gate` checks the live clusters before promoting, and approving prod is a commit.

## How it is tested
CI: 21 unit tests; a validate step that renders the real NGC Helm charts at every version and checks them against the CRD schemas of that exact version (it catches a misspelt `nodeSelecter`); and a 20-minute end-to-end run with Gitea and two kind clusters, 29 checks, including drift corrected by Flux and a bad release stopped in staging.

## What I learned
One CI iteration: the rollout plan was applied before the NVIDIADriver objects, so lifecycle now depends on config. I also found a difference in the NVIDIADriver CRD between two GPU Operator versions.

## Next steps
- Describe your clusters and releases in `fleet.toml`.
- Bootstrap Flux on each cluster (or use Argo CD, the same structure works).
- Keep the gate before production as a required check in your repository.""",
 es="""

## Por qué este laboratorio
Se apoya en Git, pipelines de CI/CD y gestión de releases, y une varios laboratorios anteriores: cómo actualizar el software de GPU en una flota de clústeres desde Git, con una puerta antes de producción.

## Qué he hecho
- `fleet.toml` define versiones (GPU Operator, Network Operator y driver, más una versión que falla a propósito) y clústeres con pools de GPU.
- Las olas van staging → prod H100 → prod A100, con una pausa tras el canary.
- `python -m fleet render` escribe la carpeta de cada clúster y Flux la aplica en tres pasos: operators → config → lifecycle. El paso lifecycle es el controlador del laboratorio 11, con su plan generado desde el mismo fichero.
- `fleet start / promote / approve` editan una línea cada uno, `fleet gate` revisa los clústeres vivos antes de promocionar y aprobar producción es un commit.

## Cómo se prueba
CI: 21 tests unitarios; un paso de validación que renderiza los charts de Helm reales de NGC en cada versión y los comprueba contra los esquemas de CRD de esa versión exacta (detecta un `nodeSelecter` mal escrito); y una prueba de punta a punta de 20 minutos con Gitea y dos clústeres kind, 29 comprobaciones, incluida la deriva corregida por Flux y una versión mala parada en staging.

## Qué aprendí
Una iteración de CI: el plan de rollout se aplicaba antes que los objetos NVIDIADriver, así que lifecycle ahora depende de config. También encontré una diferencia en el CRD NVIDIADriver entre dos versiones del GPU Operator.

## Siguientes pasos
- Describir tus clústeres y releases en `fleet.toml`.
- Instalar Flux en cada clúster (o usar Argo CD, la misma estructura sirve).
- Mantener la puerta antes de producción como comprobación obligatoria en tu repositorio."""),

dict(n="17", repo="17-teams-rooms-fleet-health", date="2026-10-15", cat="tools",
 title_en="Which meeting rooms will fail today, and in what order to fix them", title_es="Qué salas de reuniones van a fallar hoy y en qué orden arreglarlas",
 seo_title_en="Teams Rooms health check with Microsoft Graph · Iñigo González",
 seo_title_es="Salud de Teams Rooms con Microsoft Graph · Iñigo González",
 dek_en="Teams Rooms health from Microsoft Graph, a room register and today's bookings, turned into a morning walk-round.",
 dek_es="La salud de Teams Rooms desde Microsoft Graph, un registro de salas y las reservas del día, convertidos en la ronda de primera hora.",
 en="""

## The problem
The Teams admin center shows the health of every room, one device at a time. What the engineer on site needs at 08:00 is a short list: the boardroom with a meeting in 30 minutes first, the small room that is free all day last, and the first thing to try for each problem.

## What I built
- `scripts/Export-TeamsRoomsHealth.ps1` reads devices and their health from Microsoft Graph (`/teamwork/devices`, read-only).
- A readiness state per room: Not ready (offline, Teams sign-in failed, camera, microphone, speaker or main display down), At risk (no calendar on the console, stale heartbeat, outdated software, second display or HDMI ingest down) or Ready.
- `morning_check.md`, ordered by readiness, priority room and next meeting, with a first step for each issue. Also `report.html`, `actions.csv` with serial numbers for the ticket, and a daily trend.
- A housekeeping list: firmware that drifted from the rest of the model and devices nobody added to the room register.

## How it is built
Python with the standard library only, plus PowerShell for the Graph exports. The demo is a made-up company with 25 devices in three offices and faults placed on purpose. 14 tests. A short runbook explains the morning routine.

## What I learned
Most of the value is in the order of the list, not in the detection. And an offline console should show one issue, not five: everything else about it is noise until it is back.

## Next steps
- Run the PowerShell export against your tenant (the `/teamwork/devices` API is in Graph beta).
- Fill in the room register with your rooms and their priority.
- Run it every morning before the first meetings.""",
 es="""

## El problema
El Teams admin center enseña la salud de cada sala, de dispositivo en dispositivo. Lo que necesita el técnico a las 8:00 es una lista corta: primero la sala de Consejo con reunión en 30 minutos, al final la sala pequeña que está libre todo el día, y lo primero que hay que probar en cada problema.

## Qué he hecho
- `scripts/Export-TeamsRoomsHealth.ps1` lee los dispositivos y su salud desde Microsoft Graph (`/teamwork/devices`, solo lectura).
- Un estado por sala: No lista (sin conexión, fallo de inicio de sesión en Teams, cámara, micrófono, altavoz o pantalla principal caídos), En riesgo (sin calendario en la consola, sin latido reciente, software desactualizado, segunda pantalla o entrada HDMI caídas) o Lista.
- `morning_check.md`, ordenado por estado, sala prioritaria y próxima reunión, con un primer paso para cada problema. Además `report.html`, `actions.csv` con números de serie para el ticket y una tendencia diaria.
- Una lista de mantenimiento: firmware que se ha quedado distinto al resto del modelo y dispositivos que nadie dio de alta en el registro de salas.

## Cómo está hecho
Python solo con la librería estándar y PowerShell para las exportaciones de Graph. La demo es una empresa inventada con 25 dispositivos en tres oficinas y fallos puestos a propósito. 14 tests. Un runbook corto explica la rutina de primera hora.

## Qué aprendí
Casi todo el valor está en el orden de la lista, no en la detección. Y una consola sin conexión debe mostrar un problema, no cinco: lo demás es ruido hasta que vuelva.

## Siguientes pasos
- Ejecutar la exportación de PowerShell contra tu tenant (la API `/teamwork/devices` está en la beta de Graph).
- Completar el registro de salas con tus salas y su prioridad.
- Ejecutarlo cada mañana antes de las primeras reuniones."""),

dict(n="18", repo="18-mecm-intune-comanagement-tracker", date="2026-10-15", cat="tools",
 title_en="A go/no-go for the next co-management slider move", title_es="Un go/no-go para el siguiente paso del slider de co-management",
 seo_title_en="MECM + Intune co-management tracker · Iñigo González",
 seo_title_es="Seguimiento de co-management MECM + Intune · Iñigo González",
 dek_en="MECM and Intune joined in one report: real co-management state, workload authority against the plan and Windows 11 waves.",
 dek_es="MECM e Intune en un solo informe: estado real de co-management, autoridad por workload frente al plan y olas de Windows 11.",
 en="""

## The problem
In a co-management and Windows 11 migration, every status meeting asks the same things: how many devices are really co-managed, what breaks if we move a workload to Intune for everyone, and will the next wave finish on time. The answers sit in two consoles that do not share a report.

## What I built
- A read-only SQL query for the MECM side (reporting views: client health, OS build, collections) and a PowerShell export for Intune (`managedDevices` with `configurationManagerClientEnabledFeatures`).
- A join by device name with five states: co-managed, MECM only (not enrolled), enrolled outside co-management, in MECM without client, Intune only.
- For each co-managed device, the workload authority the plan expects against what Intune reports.
- Progress per Windows 11 wave and hardware that blocks the upgrade.
- `gates.md`: for every workload on Pilot, GO or NO-GO against limits agreed in `plan.json`, ready to paste into the change request.

## How it is built
Python with the standard library only. The demo is a made-up company with 260 devices halfway through the migration; the gates say NO-GO because only 91.9 % of devices are co-managed and one pilot device has not picked up the change. 14 tests and a playbook for running it alongside a change board.

## What I learned
From the Windows 11 migration I led: most of the effort is not the upgrade, it is finding the devices that are not where the plan says they are. Agreeing the gates before the CAB, not during it, saves the longest discussions.

## Next steps
- Run the read-only SQL query against your MECM site database and the Intune export from Graph.
- Write your workloads, waves and gates in `plan.json`.
- Bring `gates.md` to each change advisory board before moving the slider.""",
 es="""

## El problema
En una migración a co-management y Windows 11, cada reunión de seguimiento pregunta lo mismo: cuántos equipos están de verdad co-gestionados, qué se rompe si pasamos un workload a Intune para todos y si la siguiente ola va a acabar a tiempo. Las respuestas están en dos consolas que no comparten informe.

## Qué he hecho
- Una consulta SQL de solo lectura para MECM (vistas de informes: salud del cliente, build del SO, colecciones) y una exportación en PowerShell para Intune (`managedDevices` con `configurationManagerClientEnabledFeatures`).
- Un cruce por nombre de equipo con cinco estados: co-gestionado, solo MECM (sin inscribir), inscrito fuera de co-management, en MECM sin cliente y solo Intune.
- Para cada equipo co-gestionado, la autoridad por workload que espera el plan frente a la que informa Intune.
- El avance de cada ola de Windows 11 y el hardware que impide la actualización.
- `gates.md`: para cada workload en Pilot, GO o NO-GO frente a límites acordados en `plan.json`, listo para pegar en la petición de cambio.

## Cómo está hecho
Python solo con la librería estándar. La demo es una empresa inventada con 260 equipos a mitad de migración; los gates dicen NO-GO porque solo el 91,9 % de los equipos está co-gestionado y un equipo del piloto no ha recogido el cambio. 14 tests y un playbook para usarlo junto al comité de cambios.

## Qué aprendí
De la migración a Windows 11 que lideré: casi todo el esfuerzo no está en la actualización, sino en encontrar los equipos que no están donde dice el plan. Acordar los gates antes del CAB, y no durante, ahorra las discusiones más largas.

## Siguientes pasos
- Ejecutar la consulta SQL de solo lectura contra la base de datos de tu sitio MECM y la exportación de Intune desde Graph.
- Escribir tus workloads, olas y gates en `plan.json`.
- Llevar `gates.md` a cada comité de cambios antes de mover el slider."""),

dict(n="19", repo="19-ad-infra-health-check", date="2026-10-16", updated="2026-11-07", cat="tools",
 title_en="A Monday-morning health check for Active Directory", title_es="Un chequeo de los lunes para Active Directory",
 seo_title_en="Active Directory health check with PowerShell · Iñigo González",
 seo_title_es="Chequeo de salud de Active Directory con PowerShell · Iñigo González",
 dek_en="Domain controllers, replication, DHCP, Group Policy and admin accounts from one read-only export, ordered by what to fix today.",
 dek_es="Controladores de dominio, replicación, DHCP, directivas de grupo y cuentas de administrador desde una exportación de solo lectura, ordenados por lo que hay que arreglar hoy.",
 seo_desc="Active Directory health check with PowerShell: one read-only export for domain controllers, replication, DHCP, Group Policy and admin accounts, by priority.",
 en="""

## The problem
`dcdiag` and `repadmin` tell you everything, one domain controller at a time. Most Active Directory problems give a warning first: a clock drifting, DFSR stopped after patching, a replication link failing quietly for weeks, a DHCP scope full the week new joiners arrive, an admin account nobody has used since spring. On Monday morning you want one page with what to fix today.

## What I built
- `scripts/Export-ADHealth.ps1`: one read-only export with the standard RSAT modules (domain and forest, every DC, replication metadata, DHCP scopes and failover, GPO links, privileged groups, inactive accounts, NO_CLIENT_SITE lines). If one section fails, the rest is still exported.
- Six areas of checks: domain controllers, replication (with the tombstone risk), DHCP, Group Policy, privileged access (including the krbtgt password age) and directory hygiene.
- `health_check.md` with Fix today / Plan this week / Housekeeping, `findings.csv` with the first step for each finding and `report.html`.
- Comparison with last week's run: what is new and what was resolved.

## How it is built
Python with the standard library only, plus PowerShell. The demo is a made-up domain with six DCs in four sites and faults placed on purpose. 15 tests. A short runbook for the weekly check.

## What I learned
An unreachable DC should give one finding, not ten. And most of the value is in the order of the list: what has to be fixed before 09:00 and what can go to a change.

## Next steps
- Run `Export-ADHealth.ps1` with RSAT from an admin workstation joined to the domain.
- On servers in other languages, adapt the parsing of the `w32tm` output.
- Schedule it for Monday morning and keep last week's run for the comparison.""",
 es="""

## El problema
`dcdiag` y `repadmin` te lo cuentan todo, de controlador en controlador. La mayoría de problemas de Active Directory avisan antes: un reloj que se desvía, DFSR parado después de parchear, un enlace de replicación fallando en silencio durante semanas, un ámbito de DHCP lleno la semana que llegan las incorporaciones, una cuenta de administrador que nadie usa desde la primavera. El lunes a primera hora quieres una página con lo que hay que arreglar hoy.

## Qué he hecho
- `scripts/Export-ADHealth.ps1`: una exportación de solo lectura con los módulos estándar de RSAT (dominio y bosque, cada DC, metadatos de replicación, ámbitos y conmutación de DHCP, vínculos de GPO, grupos privilegiados, cuentas inactivas, líneas NO_CLIENT_SITE). Si una sección falla, el resto se exporta igual.
- Seis áreas de comprobaciones: controladores de dominio, replicación (con el riesgo de tombstone), DHCP, directivas de grupo, acceso privilegiado (incluida la antigüedad de la contraseña de krbtgt) e higiene del directorio.
- `health_check.md` con Arreglar hoy / Planificar esta semana / Limpieza, `findings.csv` con el primer paso de cada hallazgo y `report.html`.
- Comparación con la ejecución de la semana anterior: qué es nuevo y qué se ha resuelto.

## Cómo está hecho
Python solo con la librería estándar y PowerShell. La demo es un dominio inventado con seis DC en cuatro sedes y fallos puestos a propósito. 15 tests. Un runbook corto para el chequeo semanal.

## Qué aprendí
Un DC que no responde debe dar un hallazgo, no diez. Y casi todo el valor está en el orden de la lista: qué hay que arreglar antes de las 9:00 y qué puede ir a un cambio.

## Siguientes pasos
- Ejecutar `Export-ADHealth.ps1` con RSAT desde un puesto de administración unido al dominio.
- En servidores en otros idiomas, adaptar la lectura de la salida de `w32tm`.
- Programarlo para el lunes a primera hora y guardar la ejecución anterior para la comparación."""),

dict(n="20", repo="20-entra-sso-app-audit", date="2026-10-16", cat="tools",
 title_en="Which SSO app will break next, and which one nobody is watching", title_es="Qué app con SSO va a fallar la próxima y cuál no vigila nadie",
 seo_title_en="Entra ID SSO audit: SAML certificate expiry · Iñigo González",
 seo_title_es="Auditoría SSO de Entra ID: caducidad de certificados SAML · Iñigo González",
 dek_en="Enterprise apps and app registrations in Entra ID: certificates and secrets about to expire, owners, MFA coverage, risky permissions and SCIM.",
 dek_es="Aplicaciones empresariales y registros de aplicaciones en Entra ID: certificados y secretos a punto de caducar, propietarios, cobertura de MFA, permisos de riesgo y SCIM.",
 en="""

## The problem
Single sign-on puts access in one place, but the details are spread over hundreds of enterprise apps. The same problems come back: a SAML signing certificate expires and a SaaS app stops accepting logons at 09:00, a client secret expires and a nightly job fails, an app has no owner, every user can open it, it was excluded from the MFA policy "for now", a daemon can write to the whole directory, or provisioning is in quarantine and leavers keep their account in the app.

## What I built
- `scripts/Export-EntraAppInventory.ps1`: a read-only Microsoft Graph export of service principals, app registrations (only the dates of secrets and certificates, never the values) and Conditional Access policies.
- Checks in six areas: credentials, ownership, access (assignment required and MFA coverage), permissions (application permissions, tenant-wide consent, unverified publishers, redirect URIs), SCIM provisioning and unused apps.
- `review.md` for the monthly access review, `renewals.csv` as a renewal calendar with owners, `findings.csv` and `report.html`.

## How it is built
Python with the standard library only, plus PowerShell for Graph. The demo is a made-up tenant with 21 enterprise apps and faults placed on purpose. 15 tests. A runbook that includes renewing a SAML certificate without an outage.

## What I learned
From integrating SaaS apps in Entra ID: the hard part is not the SSO setup, it is who renews the certificate two years later. A secret expired while the app still signs in is urgent; an expired secret already replaced by a newer one is just clean-up.

## Next steps
- Run `Export-EntraAppInventory.ps1` with read-only Graph permissions on your tenant.
- Assign an owner to every app in the renewal calendar.
- Extend the SCIM provisioning and OIDC checks, which are the next ones I am growing.""",
 es="""

## El problema
El inicio de sesión único concentra el acceso en un sitio, pero los detalles están repartidos en cientos de aplicaciones empresariales. Los problemas se repiten: caduca un certificado de firma SAML y una aplicación SaaS deja de aceptar inicios de sesión a las 9:00, caduca un secreto y falla un proceso nocturno, una aplicación no tiene propietario, cualquier usuario puede abrirla, se excluyó de la política de MFA "de momento", un proceso desatendido puede escribir en todo el directorio o el aprovisionamiento está en cuarentena y las bajas siguen teniendo cuenta en la aplicación.

## Qué he hecho
- `scripts/Export-EntraAppInventory.ps1`: una exportación de solo lectura con Microsoft Graph de las entidades de servicio, los registros de aplicaciones (solo las fechas de secretos y certificados, nunca su valor) y las políticas de acceso condicional.
- Comprobaciones en seis áreas: credenciales, propietarios, acceso (asignación obligatoria y cobertura de MFA), permisos (permisos de aplicación, consentimiento para toda la organización, editores sin verificar, URI de redirección), aprovisionamiento SCIM y aplicaciones sin uso.
- `review.md` para la revisión mensual de accesos, `renewals.csv` como calendario de renovaciones con propietarios, `findings.csv` y `report.html`.

## Cómo está hecho
Python solo con la librería estándar y PowerShell para Graph. La demo es un tenant inventado con 21 aplicaciones empresariales y fallos puestos a propósito. 15 tests. Un runbook que incluye cómo renovar un certificado SAML sin corte.

## Qué aprendí
De integrar aplicaciones SaaS en Entra ID: lo difícil no es configurar el SSO, sino quién renueva el certificado dos años después. Un secreto caducado mientras la aplicación sigue iniciando sesión es urgente; uno caducado que ya se sustituyó por otro nuevo es solo limpieza.

## Siguientes pasos
- Ejecutar `Export-EntraAppInventory.ps1` con permisos de solo lectura de Graph en tu tenant.
- Asignar un propietario a cada aplicación del calendario de renovaciones.
- Ampliar las comprobaciones de aprovisionamiento SCIM y de OIDC, que son las siguientes que estoy desarrollando."""),

dict(n="21", repo="21-apple-fleet-audit", date="2026-10-17", cat="tools",
 title_en="A weekly review for a Jamf Pro Apple fleet", title_es="Una revisión semanal para una flota Apple en Jamf Pro",
 seo_title_en="Jamf Pro weekly audit for an Apple fleet · Iñigo González",
 seo_title_es="Auditoría semanal de Jamf Pro (flota Apple) · Iñigo González",
 dek_en="Push certificate and tokens, OS currency, FileVault, SIP, bootstrap token, passcodes, stale devices and full disks, with the executives' devices first.",
 dek_es="Certificado push y tokens, versiones de sistema, FileVault, SIP, bootstrap token, códigos de acceso, equipos que no se conectan y discos llenos, con los dispositivos de dirección primero.",
 en="""

## The problem
Jamf Pro shows every detail of every Mac, iPhone and iPad, but the weekly questions are spread over smart groups, settings pages and Apple's portals. The same problems come back: the APNs push certificate expires and no device gets a command (or someone creates a new one instead of renewing it and every device has to re-enroll), the ADE token expires and new laptops come out of the box unmanaged, a Mac has FileVault on but no recovery key in Jamf Pro, an Apple silicon Mac has no bootstrap token and updates never install, an iPhone has no passcode, a laptop has not checked in for two months, and the CEO's iPad has a full disk the evening before the board meeting.

## What I built
- A read-only Jamf Pro API exporter (an API client with read privileges only; the secret comes from an environment variable).
- Checks in seven areas: platform tokens (APNs, ADE, Apps and Books), OS currency, Mac security, mobile security, enrollment, hardware (storage and warranty) and VIP devices, whose findings go up one level and get their own section.
- `review.md` for the weekly meeting with a token calendar, `device_actions.csv` as a work list per device, `findings.csv` and `report.html`.

## How it is built
Python with the standard library only. The demo is a made-up fleet of 40 devices (18 Macs, 14 iPhones, 8 iPads) with three VIP users and faults placed on purpose. 17 tests. A runbook for the weekly review and for renewing the APNs certificate and the ADE and VPP tokens without surprises.

## What I learned
From managing MacBooks, iPhones and iPads with Jamf Pro and supporting VIP users and board meetings: the expensive mistakes are not on one device, they are the certificate or token that stops the whole fleet. And a value Jamf Pro did not collect should skip the check, not raise a false alarm.

## Next steps
- Create a Jamf Pro API role with read privileges only and an API client.
- Run the export and add the APNs expiry date from Settings > Global > Push certificates.
- Add your VIP list and bring `review.md` to the weekly meeting.""",
 es="""

## El problema
Jamf Pro muestra cada detalle de cada Mac, iPhone y iPad, pero las preguntas de cada semana están repartidas entre grupos inteligentes, páginas de ajustes y los portales de Apple. Los problemas se repiten: caduca el certificado push de APNs y ningún dispositivo recibe órdenes (o alguien crea uno nuevo en lugar de renovarlo y toca volver a inscribirlos todos), caduca el token de ADE y los portátiles nuevos salen de la caja sin gestionar, un Mac tiene FileVault activado pero sin clave de recuperación en Jamf Pro, un Mac con Apple silicon no tiene bootstrap token y las actualizaciones nunca se instalan, un iPhone no tiene código, un portátil lleva dos meses sin conectarse y el iPad del CEO tiene el disco lleno la tarde antes del consejo.

## Qué he hecho
- Un exportador de solo lectura con la API de Jamf Pro (un cliente de API con permisos solo de lectura; el secreto se lee de una variable de entorno).
- Comprobaciones en siete áreas: tokens de la plataforma (APNs, ADE, Apps and Books), versiones de sistema, seguridad del Mac, seguridad del móvil, inscripción, hardware (almacenamiento y garantía) y dispositivos VIP, cuyos hallazgos suben un nivel y tienen su propia sección.
- `review.md` para la reunión semanal con un calendario de tokens, `device_actions.csv` como lista de trabajo por dispositivo, `findings.csv` y `report.html`.

## Cómo está hecho
Python solo con la librería estándar. La demo es una flota inventada de 40 dispositivos (18 Mac, 14 iPhone, 8 iPad) con tres usuarios VIP y fallos puestos a propósito. 17 tests. Un runbook para la revisión semanal y para renovar el certificado de APNs y los tokens de ADE y VPP sin sustos.

## Qué aprendí
De gestionar MacBooks, iPhones e iPads con Jamf Pro y dar soporte a usuarios VIP y reuniones de consejo: los errores caros no están en un dispositivo, sino en el certificado o el token que para toda la flota. Y un dato que Jamf Pro no ha recogido debe saltarse la comprobación, no dar una falsa alarma.

## Siguientes pasos
- Crear en Jamf Pro un rol de API solo con permisos de lectura y un cliente de API.
- Ejecutar la exportación y añadir la caducidad de APNs desde Settings > Global > Push certificates.
- Añadir tu lista de VIP y llevar `review.md` a la reunión semanal."""),

dict(n="22", repo="22-dex-experience-score", date="2026-10-17", updated="2026-11-07", cat="tools",
 title_en="A 0-10 experience score for every laptop", title_es="Una nota de 0 a 10 para la experiencia de cada portátil",
 seo_title_en="DEX score: a 0-10 experience per laptop · Iñigo González",
 seo_title_es="Puntuación DEX de 0 a 10 por portátil · Iñigo González",
 dek_en="A lab that turns endpoint telemetry into a score per device, site and department, and ranks the five fixes that would raise it most.",
 dek_es="Un laboratorio que convierte la telemetría de los equipos en una nota por dispositivo, sede y departamento, y ordena los cinco arreglos que más la subirían.",
 seo_desc="DEX score lab: turns endpoint telemetry into a 0-10 digital experience score per device, site and department, and ranks the fixes that raise it most.",
 en="""

## Why this lab
Comes from years of supporting Windows users and executives on site. It is inspired by the public descriptions of digital employee experience (DEX) tools such as Nexthink; the model, thresholds and weights are my own and are explained in the repository.

## The problem
Anyone who has supported Windows users on site knows it: tickets show a fraction of the problems. People live with a slow laptop or a crashing app for weeks, stop reporting and just say "IT is slow". A monthly update adds 40 seconds to every logon, an Outlook add-in crashes on twenty laptops, the Wi-Fi on one floor is weak, batteries die in meetings. Endpoint telemetry sees all of it.

## What I built
- A read-only PowerShell collector: boot and logon times, app crashes and hangs, blue screens, Wi-Fi drops and signal, latency, VPN failures, battery and disk.
- A score per device from five categories (performance, stability, network and collaboration, hardware, optional survey), with caps for blue screens and very poor categories. Missing data is left out, never scored as zero.
- Top fixes ranked by how much the fleet score would rise if the problem were gone, a 6-week trend by site, `review.md` for the service owner and `report.html` with inline SVG charts.

## How it is built
Python with the standard library only, plus PowerShell. The demo is a made-up company with 120 devices in three cities and six weeks of data; it finds the five problems placed on purpose, led by blue screens on one laptop model after a driver update. 15 tests.

## What I learned
Explaining the score matters more than the number: every point lost has to point to a cause and a fix. And telemetry linked to a person is personal data, so report by site and department and talk to the DPO first.

## Next steps
- Deploy the collector through an Intune remediation script or your RMM tool.
- Tune the thresholds after a few weeks of real data.
- Talk to your data protection officer first, and report by site and department.""",
 es="""

## Por qué este laboratorio
Viene de años dando soporte presencial a usuarios de Windows y a dirección. Se inspira en las descripciones públicas de herramientas de experiencia digital del empleado (DEX) como Nexthink; el modelo, los umbrales y los pesos son míos y están explicados en el repositorio.

## El problema
Quien haya dado soporte presencial a usuarios de Windows lo sabe: los tickets muestran una parte de los problemas. La gente convive semanas con un portátil lento o una aplicación que se cierra, deja de avisar y solo dice "IT va lento". Una actualización mensual añade 40 segundos a cada inicio de sesión, un complemento de Outlook falla en veinte portátiles, el wifi de una planta es débil, las baterías mueren en mitad de una reunión. La telemetría de los equipos lo ve todo.

## Qué he hecho
- Un recolector de solo lectura en PowerShell: tiempos de arranque e inicio de sesión, cierres y bloqueos de aplicaciones, pantallazos azules, cortes y señal de wifi, latencia, fallos de VPN, batería y disco.
- Una nota por dispositivo a partir de cinco categorías (rendimiento, estabilidad, red y colaboración, hardware y una encuesta opcional), con topes para pantallazos azules y categorías muy malas. Los datos que faltan se dejan fuera, nunca cuentan como cero.
- Los arreglos ordenados por cuánto subiría la nota de la flota si el problema desapareciera, la tendencia de 6 semanas por sede, `review.md` para el responsable del servicio y `report.html` con gráficos SVG.

## Cómo está hecho
Python solo con la librería estándar y PowerShell. La demo es una empresa inventada con 120 equipos en tres ciudades y seis semanas de datos; encuentra los cinco problemas puestos a propósito, empezando por pantallazos azules en un modelo de portátil tras actualizar un driver. 15 tests.

## Qué aprendí
Explicar la nota importa más que el número: cada punto perdido tiene que llevar a una causa y a un arreglo. Y la telemetría ligada a una persona es un dato personal, así que hay que informar por sede y departamento y hablar antes con el DPO.

## Siguientes pasos
- Desplegar el recolector con un script de corrección de Intune o tu herramienta RMM.
- Ajustar los umbrales tras unas semanas de datos reales.
- Hablar antes con tu delegado de protección de datos e informar por sede y departamento."""),
dict(n="23", repo="23-it-vendor-contract-tracker", date="2026-10-18", cat="tools",
 title_en="Every IT contract renewal, notice deadline and saving in one monthly review", title_es="Cada renovación, preaviso y ahorro de los contratos de IT en una revisión mensual",
 seo_title_en="IT vendor contract and renewal tracker · Iñigo González",
 seo_title_es="Contratos y renovaciones de IT en una revisión · Iñigo González",
 dek_en="A tracker that reads the contract register and finds the notice deadlines, unused licences, budget overruns and missed SLAs before they cost money.",
 dek_es="Un tracker que lee el registro de contratos y encuentra los preavisos, licencias sin usar, desviaciones de presupuesto y SLA incumplidos antes de que cuesten dinero.",
 en="""

## The problem
IT contracts rarely fail in a dramatic way. They fail quietly: a contract with 60 days' notice renews by itself for another year because nobody looked at the date in time, the support on a firewall ends and nobody notices until a replacement is needed, an add-on has 60 licences and 34 users while the main suite is 12 seats over what was bought, a budget line is on pace to end 14% over, a vendor misses its SLA two months running and the service credit is never claimed.

## What I built
- Checks in six areas from the register you already keep in a spreadsheet: renewals and notice deadlines (including contracts that already renewed by themselves), licences, budget forecast, SLA and service credits, supplier risk and data quality.
- `review.md` for the monthly vendor meeting, `actions.csv` as a work list with owners, dates and the money at stake, and `report.html` with a 12-month renewal calendar.
- `renewals.ics`: every notice deadline in the team calendar, with a reminder 14 days before.

## How it is built
Python with the standard library only. The demo is a made-up company with 21 contracts from 17 vendors, six budget lines and six months of SLA reports, with faults placed on purpose. 17 tests. A runbook for the monthly review and a checklist for each renewal decision.

## What I learned
From managing IT suppliers, renewals and budgets: the most expensive date in a contract is not the end date, it is the notice deadline. And usage data turns a renewal into a negotiation.

## Next steps
- Export your contract register to CSV and map its columns.
- Add the spend to date from finance and last month's SLA figures before each review.
- Import `renewals.ics` into the team calendar.""",
 es="""

## El problema
Los contratos de IT casi nunca fallan de forma espectacular. Fallan en silencio: un contrato con 60 días de preaviso se renueva solo otro año porque nadie miró la fecha a tiempo, se acaba el soporte de un firewall y nadie se entera hasta que hace falta un repuesto, un complemento tiene 60 licencias y 34 usuarios mientras la suite principal tiene 12 puestos más de los comprados, una partida del presupuesto va camino de acabar un 14% por encima, un proveedor incumple su SLA dos meses seguidos y nadie reclama la penalización.

## Qué he hecho
- Comprobaciones en seis áreas a partir del registro que ya tienes en una hoja de cálculo: renovaciones y preavisos (también los contratos que ya se han renovado solos), licencias, previsión del presupuesto, SLA y penalizaciones, riesgo de proveedor y calidad de los datos.
- `review.md` para la reunión mensual de proveedores, `actions.csv` como lista de trabajo con responsable, fecha y el dinero en juego, y `report.html` con un calendario de renovaciones a 12 meses.
- `renewals.ics`: cada fecha límite de preaviso en el calendario del equipo, con aviso 14 días antes.

## Cómo está hecho
Python solo con la librería estándar. La demo es una empresa inventada con 21 contratos de 17 proveedores, seis partidas de presupuesto y seis meses de informes de SLA, con fallos puestos a propósito. 17 tests. Un runbook para la revisión mensual y una lista de comprobación para cada decisión de renovación.

## Qué aprendí
De gestionar proveedores, renovaciones y presupuesto de IT: la fecha más cara de un contrato no es la de fin, es la del preaviso. Y los datos de uso convierten una renovación en una negociación.

## Siguientes pasos
- Exportar tu registro de contratos a CSV y adaptar sus columnas.
- Añadir el gasto acumulado de finanzas y las cifras de SLA del mes antes de cada revisión.
- Importar `renewals.ics` en el calendario del equipo."""),
dict(n="24", repo="24-hospitality-it-preopening", date="2026-10-18", cat="tools",
 title_en="Will IT be ready before the hotel opens? A pre-opening tracker", title_es="¿Estará IT lista antes de que abra el hotel? Un tracker de pre-apertura",
 seo_title_en="Hotel IT pre-opening tracker and checklist · Iñigo González",
 seo_title_es="Pre-apertura de hotel: plan y checklist de IT · Iñigo González",
 dek_en="A plan with lead times and dependencies that calculates the critical path, the gates at risk and the work that must start this week.",
 dek_es="Un plan con plazos de entrega y dependencias que calcula el camino crítico, los hitos en riesgo y lo que tiene que empezar esta semana.",
 en="""

## The problem
In a hotel pre-opening every system depends on another one, and most of them on the internet line. The circuits have a 75-day lead time; the cloud PMS, the room-charge interface, the call charges and the interface tests slide with them; training can only start when the interfaces are tested; and the dress rehearsal needs everything. A spreadsheet lists the tasks, but it does not say which delay moves the opening.

## What I built
- A schedule from the task list: forecast dates, float and the critical path to the day IT is ready, from durations, dependencies and progress.
- Gates from T-90 (design frozen) to T-1 (ready to open), with gates already passed with open tasks, tasks forecast late, blocked work, tasks that must start this week and a risk register.
- `report.html` with a Gantt chart, `review.md` for the weekly meeting, `actions.csv` and a go-live checklist for T-7, T-1, opening day and the first week.

## How it is built
Python with the standard library only. The demo is a made-up 120-room resort hotel opening in January, with 30 tasks in nine workstreams and delays placed on purpose. 14 tests, including the same plan reviewed three weeks later without progress, which puts the opening at risk.

## What I learned
From years supporting POS, hotel PMS and IPTV at a technology consultancy: integrations and lead times decide the opening, not the installation of each system. The tool makes that visible every week.

## Next steps
- Export your pre-opening plan with real vendor lead times and dependencies.
- Set your own gates if your brand uses different milestones.
- Run it before each weekly meeting, daily from T-7, and print the go-live checklist for the dress rehearsal.""",
 es="""

## El problema
En la pre-apertura de un hotel cada sistema depende de otro, y casi todos de la línea de internet. Los circuitos tardan 75 días en llegar; el PMS en la nube, el interfaz de cargos a habitación, los cargos de llamadas y las pruebas de interfaces se retrasan con ellos; la formación solo puede empezar cuando los interfaces están probados, y el ensayo general lo necesita todo. Una hoja de cálculo lista las tareas, pero no dice qué retraso mueve la apertura.

## Qué he hecho
- Un calendario a partir de la lista de tareas: fechas previstas, holgura y el camino crítico hasta el día en que IT está lista, con duraciones, dependencias y avance.
- Hitos de T-90 (diseño cerrado) a T-1 (listos para abrir), con hitos ya pasados con tareas abiertas, tareas que llegan tarde, trabajo bloqueado, tareas que tienen que empezar esta semana y un registro de riesgos.
- `report.html` con un diagrama de Gantt, `review.md` para la reunión semanal, `actions.csv` y una lista de comprobación de puesta en marcha para T-7, T-1, el día de apertura y la primera semana.

## Cómo está hecho
Python solo con la librería estándar. La demo es un hotel vacacional inventado de 120 habitaciones que abre en enero, con 30 tareas en nueve áreas y retrasos puestos a propósito. 14 tests, entre ellos el mismo plan revisado tres semanas después sin avances, que pone la apertura en riesgo.

## Qué aprendí
De años dando soporte a TPV, PMS hotelero e IPTV en una consultora tecnológica: lo que decide una apertura son los interfaces y los plazos de entrega, no la instalación de cada sistema. La herramienta lo hace visible cada semana.

## Siguientes pasos
- Exportar tu plan de pre-apertura con los plazos reales de los proveedores y las dependencias.
- Definir tus propios hitos si tu marca usa otros.
- Ejecutarlo antes de cada reunión semanal, a diario desde T-7, e imprimir la lista de comprobación para el ensayo general."""),
dict(n="25", repo="25-security-controls-evidence", date="2026-10-19", cat="tools",
 title_en="What will the auditor ask for that you cannot show yet? One register for ISO 27001, NIS2 and GDPR", title_es="¿Qué te pedirá el auditor que aún no puedes enseñar? Un registro para ISO 27001, NIS2 y RGPD",
 seo_title_en="ISO 27001, NIS2 and GDPR evidence tracker · Iñigo González",
 seo_title_es="Evidencias para ISO 27001, NIS2 y RGPD · Iñigo González",
 dek_en="One control register mapped to three frameworks that finds missing, late or failing evidence, expired exceptions and how ready each framework is for the audit date.",
 dek_es="Un registro de controles mapeado a tres marcos que encuentra evidencias que faltan, llegan tarde o fallan, excepciones caducadas y cómo de listo está cada marco para la fecha de auditoría.",
 en="""

## The problem
Most audit findings are not about missing security, they are about missing proof. The quarterly restore test was done in June but not in September, and the audit is in five weeks. The immutable backup copy has been failing for a week and nobody linked it to the controls. A control is marked implemented with no evidence behind it. The DLP exception expired last month. And the same restore test answers ISO 27001, NIS2 and GDPR, but it is collected three times by three people, or not at all.

## What I built
- One register of controls and evidence mapped to ISO/IEC 27001:2022, NIS2 and GDPR, with checks in five areas: evidence, controls, exceptions, coverage per requirement and data quality.
- Readiness per framework for the audit date: each requirement is covered, excluded, at risk or a gap, with what stands in its way.
- `report.html` with a nine-week collection plan, `review.md` for the security review, `actions.csv`, an `audit-pack.csv` index for the auditor, a `soa.csv` in Statement-of-Applicability form and `evidence-calendar.ics` with every due date.

## How it is built
Python with the standard library only. The demo is a made-up company with 23 controls, 33 evidence items and 3 exceptions against 48 requirements, five weeks before an ISO 27001 surveillance audit, with gaps placed on purpose. 14 tests.

## What I learned
From applying ISO 27001, NIS2 and GDPR in IT operations, preparing evidence and answering audits: one piece of evidence well kept serves several frameworks, and the calendar of what to collect matters as much as the controls themselves.

## Next steps
- Export your control register and evidence index to CSV and map the columns.
- Add the requirements you are audited against to the catalogue.
- Import `evidence-calendar.ics` into the team calendar and run it before each security review.""",
 es="""

## El problema
La mayoría de hallazgos de auditoría no son por falta de seguridad, sino por falta de pruebas. La prueba de restauración trimestral se hizo en junio pero no en septiembre, y la auditoría es en cinco semanas. La copia inmutable del backup lleva una semana fallando y nadie lo ha relacionado con los controles. Un control está marcado como implantado sin ninguna evidencia detrás. La excepción de DLP caducó el mes pasado. Y la misma prueba de restauración responde a ISO 27001, NIS2 y RGPD, pero la recogen tres personas tres veces, o nadie.

## Qué he hecho
- Un único registro de controles y evidencias mapeado a ISO/IEC 27001:2022, NIS2 y RGPD, con comprobaciones en cinco áreas: evidencias, controles, excepciones, cobertura por requisito y calidad de los datos.
- El grado de preparación de cada marco para la fecha de auditoría: cada requisito queda cubierto, excluido, en riesgo o como brecha, con lo que lo impide.
- `report.html` con un plan de recogida a nueve semanas, `review.md` para la revisión de seguridad, `actions.csv`, un índice `audit-pack.csv` para el auditor, un `soa.csv` en formato de Declaración de Aplicabilidad y `evidence-calendar.ics` con cada fecha de vencimiento.

## Cómo está hecho
Python solo con la librería estándar. La demo es una empresa inventada con 23 controles, 33 evidencias y 3 excepciones frente a 48 requisitos, cinco semanas antes de una auditoría de seguimiento de ISO 27001, con brechas puestas a propósito. 14 tests.

## Qué aprendí
De aplicar ISO 27001, NIS2 y RGPD en operaciones de IT, preparando evidencias y respondiendo auditorías: una evidencia bien guardada sirve para varios marcos, y el calendario de lo que hay que recoger importa tanto como los propios controles.

## Siguientes pasos
- Exportar tu registro de controles y tu índice de evidencias a CSV y adaptar las columnas.
- Añadir al catálogo los requisitos frente a los que te auditan.
- Importar `evidence-calendar.ics` en el calendario del equipo y ejecutarlo antes de cada revisión de seguridad."""),
dict(n="26", repo="26-ot-segmentation-lab", date="2026-10-20", cat="tools",
 title_en="Which paths into the plant network should not exist? A Purdue and IEC 62443 segmentation lab", title_es="¿Qué caminos hacia la red de planta no deberían existir? Un laboratorio de segmentación Purdue e IEC 62443",
 seo_title_en="OT segmentation lab: Purdue and IEC 62443 · Iñigo González",
 seo_title_es="Segmentación OT: Purdue e IEC 62443 · Iñigo González",
 dek_en="Zones, assets, firewall rules and observed traffic side by side: risky paths into OT, remote access that skips the jump host, and a tighter rule set built from what the plant really uses.",
 dek_es="Zonas, activos, reglas de firewall y tráfico observado juntos: caminos de riesgo hacia OT, accesos remotos que se saltan el jump host y un conjunto de reglas más ajustado a partir de lo que la planta usa de verdad.",
 en="""

## The problem
On a plant network the risky paths are rarely the ones in the diagram. A commissioning rule that allows anything from the office to the plant servers is still there years later. A finance PC reads a PLC with Modbus for a report. A vendor connects with RDP straight to an HMI. A temporary rule for an upgrade expired a month ago and still carries traffic. The rule set, the inventory and the real traffic each tell a different story.

## What I built
- A check of zones, assets, conduits and observed flows against the Purdue model and the zones and conduits idea of IEC 62443: rules that bypass the DMZ or skip a level, controller protocols from L3 or above, cleartext admin protocols, OT devices talking to the internet, remote access that does not start on the jump host and the safety system reachable from control.
- Asset and data checks: devices missing from the inventory, assets outside their zone's subnet, end-of-life Windows in OT and zones without an owner.
- `report.html` with a Purdue diagram coloured by status, `firewall-proposal.csv` with allow, review, re-route via DMZ or block for each observed service, `review.md`, `actions.csv` and a zone-to-zone matrix.

## How it is built
Python with the standard library only. The demo is a made-up bottling plant with 8 zones, 25 assets, 16 conduits and a week of flows, with problems placed on purpose. 16 tests and a runbook for the segmentation review.

## What I learned
From years supporting data centre and IT-OT integration work: Cisco switches and routers, comms rooms and racks, FortiGate firewalls, connectivity providers, DR/BCP tests and changes through CAB with a rollback plan. That work showed me that a firewall change in a plant is only safe when you know what traffic really crosses it. Now I am studying IEC 62443 zones and conduits, and this lab is how I practise it.

## Next steps
- Export your zones, inventory and firewall rules to CSV and a week of flows from your firewall or NetFlow.
- Review the proposal with the plant before blocking anything, and plan each change through CAB with a rollback.
- Go deeper into IEC 62443-3-2 risk assessment and security levels per zone.""",
 es="""

## El problema
En una red de planta los caminos de riesgo casi nunca son los del diagrama. Una regla de la puesta en marcha que permite todo desde la oficina hacia los servidores de planta sigue ahí años después. Un PC de finanzas lee un PLC con Modbus para un informe. Un proveedor entra por RDP directamente a un HMI. Una regla temporal de una actualización caducó hace un mes y sigue pasando tráfico. Las reglas, el inventario y el tráfico real cuentan cada uno una historia distinta.

## Qué he hecho
- Una revisión de zonas, activos, conductos y flujos observados frente al modelo Purdue y la idea de zonas y conductos de IEC 62443: reglas que se saltan la DMZ o un nivel, protocolos de controlador desde L3 o superior, protocolos de administración en claro, equipos OT hablando con internet, accesos remotos que no empiezan en el jump host y el sistema de seguridad alcanzable desde control.
- Comprobaciones de activos y datos: equipos que no están en el inventario, activos fuera de la subred de su zona, Windows sin soporte en OT y zonas sin responsable.
- `report.html` con un diagrama Purdue coloreado por estado, `firewall-proposal.csv` con permitir, revisar, redirigir por la DMZ o bloquear para cada servicio observado, `review.md`, `actions.csv` y una matriz zona a zona.

## Cómo está hecho
Python solo con la librería estándar. La demo es una planta embotelladora inventada con 8 zonas, 25 activos, 16 conductos y una semana de flujos, con problemas puestos a propósito. 16 tests y un runbook para la revisión de segmentación.

## Qué aprendí
De años dando soporte a centro de datos e integración IT-OT: switches y routers Cisco, salas de comunicaciones y racks, firewalls FortiGate, proveedores de conectividad, pruebas de DR/BCP y cambios por CAB con plan de vuelta atrás. Ese trabajo me enseñó que un cambio de firewall en planta solo es seguro cuando sabes qué tráfico pasa de verdad. Ahora estoy estudiando zonas y conductos de IEC 62443, y este laboratorio es mi forma de practicarlo.

## Siguientes pasos
- Exportar tus zonas, inventario y reglas de firewall a CSV, y una semana de flujos del firewall o de NetFlow.
- Revisar la propuesta con la planta antes de bloquear nada, y planificar cada cambio por CAB con vuelta atrás.
- Profundizar en la evaluación de riesgos de IEC 62443-3-2 y los niveles de seguridad por zona."""),
dict(n="27", repo="27-m365-tenant-governance-review", date="2026-10-21", cat="tools",
 title_en="Is the tenant still governed the way we agreed? A monthly Microsoft 365 review", title_es="¿Sigue el tenant gobernado como acordamos? Una revisión mensual de Microsoft 365",
 seo_title_en="Microsoft 365 tenant governance review · Iñigo González",
 seo_title_es="Revisión de gobierno del tenant Microsoft 365 · Iñigo González",
 dek_en="Admin roles and PIM, emergency accounts, Conditional Access basics, settings drift, licences to reclaim, and admin changes matched to change tickets, including the provider's.",
 dek_es="Roles de administración y PIM, cuentas de emergencia, lo básico de Acceso condicional, desviaciones de configuración, licencias a recuperar y cambios de administración cruzados con los tickets de cambio, también los del proveedor.",
 en="""

## The problem
A Microsoft 365 tenant drifts one reasonable change at a time. A Global Administrator given for a migration is still always-on two years later. The provider's engineers hold permanent admin roles with no end date. The change to allow automatic forwarding was rejected at CAB and made anyway. The legacy authentication block has been in report-only since July. When the platform is operated by a provider, the internal team still owns the risk, and it needs a short list for the monthly review.

## What I built
- A review of a read-only export of the tenant in six areas: privileged access, emergency accounts, the four Conditional Access basics, ten tenant settings against a baseline, licences, and sensitive admin changes.
- Each admin change on roles, Conditional Access, tenant or mail-flow settings is matched to a change ticket by implementer and window: approved, emergency, rejected, no ticket, or made with an emergency account.
- `report.html`, `review.md` with a section for the service review with the provider, `actions.csv`, `privileged-access.csv` for the quarterly access review, `licence-reclaim.csv` and `admin-changes.csv`.

## How it is built
Python with the standard library only, and a read-only PowerShell exporter on Microsoft Graph and, optionally, Exchange Online. The demo is a made-up retailer with 395 accounts, operated by a fictional provider, with problems placed on purpose. 16 tests and a runbook for the monthly review.

## What I learned
From running Microsoft 365 as Global Administrator: PIM and just-in-time access, Conditional Access, Exchange Online, Purview, tenant-to-tenant migrations and changes through CAB with providers. Governance is not a one-off hardening project; it is a monthly habit, and the change ticket is what keeps the provider and the internal team on the same page.

## Next steps
- Run the exporter with a Global Reader account against your tenant and check the role names and the Conditional Access mapping on the first run.
- Agree the baseline with security before the first review.
- Ask the provider to put the change reference in every admin session, so the change matching becomes a formality.""",
 es="""

## El problema
Un tenant de Microsoft 365 se desvía cambio razonable a cambio razonable. Un Global Administrator dado para una migración sigue activo dos años después. Los ingenieros del proveedor tienen roles de administración permanentes sin fecha de fin. El cambio para permitir el reenvío automático se rechazó en el CAB y se hizo igualmente. El bloqueo de la autenticación heredada lleva en modo solo informe desde julio. Cuando la plataforma la opera un proveedor, el riesgo sigue siendo del equipo interno, que necesita una lista corta para la revisión mensual.

## Qué he hecho
- Una revisión de una exportación de solo lectura del tenant en seis áreas: acceso privilegiado, cuentas de emergencia, lo básico de Acceso condicional, diez ajustes del tenant frente a una línea base, licencias y cambios de administración sensibles.
- Cada cambio de administración en roles, Acceso condicional, ajustes del tenant o del flujo de correo se cruza con un ticket de cambio por implementador y ventana: aprobado, de emergencia, rechazado, sin ticket o hecho con una cuenta de emergencia.
- `report.html`, `review.md` con una sección para la revisión de servicio con el proveedor, `actions.csv`, `privileged-access.csv` para la revisión trimestral de accesos, `licence-reclaim.csv` y `admin-changes.csv`.

## Cómo está hecho
Python solo con la librería estándar, y un exportador de solo lectura en PowerShell sobre Microsoft Graph y, si se quiere, Exchange Online. La demo es un comercio inventado con 395 cuentas, operado por un proveedor ficticio, con problemas puestos a propósito. 16 tests y un runbook para la revisión mensual.

## Qué aprendí
De administrar Microsoft 365 como Global Administrator: PIM y acceso just-in-time, Acceso condicional, Exchange Online, Purview, migraciones de tenant a tenant y cambios por CAB con proveedores. El gobierno de un tenant no es un proyecto de bastionado puntual, es un hábito mensual, y el ticket de cambio es lo que mantiene alineados al proveedor y al equipo interno.

## Siguientes pasos
- Ejecutar el exportador con una cuenta Global Reader en tu tenant y revisar en la primera ejecución los nombres de roles y el mapeo de Acceso condicional.
- Acordar la línea base con seguridad antes de la primera revisión.
- Pedir al proveedor que ponga la referencia del cambio en cada sesión de administración, para que el cruce con los cambios sea un trámite."""),
dict(n="28", repo="28-euc-provider-service-review", date="2026-10-22", cat="tools",
 title_en="The provider says 96% and the users say it is slow: a monthly EUC service review from the tickets", title_es="El proveedor dice 96% y los usuarios dicen que va lento: una revisión mensual del servicio EUC desde los tickets",
 seo_title_en="EUC provider service review: SLA and OLA · Iñigo González",
 seo_title_es="Revisión del servicio EUC del proveedor: SLA y OLA · Iñigo González",
 dek_en="SLA scorecard with the breach list, backlog and ageing, escalations and the OLAs we owe the provider, out-of-hours coverage, the quality signals a compliance figure hides, and the service credits nobody has claimed.",
 dek_es="Cuadro de SLA con la lista de incumplimientos, backlog y antigüedad, escalados y las OLAs que le debemos al proveedor, cobertura fuera de horario, las señales de calidad que un porcentaje esconde y los créditos de servicio que nadie ha reclamado.",
 en="""

## The problem
The provider's monthly pack says 96% and the users say the service is slow. Both are usually right. The P2 figure leaves out the tickets that spent a week in "waiting for customer". The out-of-hours P2s wait for the follow-the-sun hand-over, and the average hides them. A fifth of the compliant tickets were closed in the last 10% of the window. The provider escalated 19% of its tickets to the internal teams, and the network team is sitting on twelve of them since July, so that breach is ours. And the contract has service credits nobody has ever claimed, because nobody computed them. A service review needs one set of numbers both sides accept, computed from the raw tickets with the rules written down.

## What I built
- A review of a month of tickets in six areas: SLA per type and priority with business-hours or 24x7 clocks and pending time subtracted; backlog and ageing by team; escalations to the internal teams and their OLAs, with the clock starting at the hand-over; coverage in and out of hours; quality (reopens, first-contact resolution, satisfaction, last-minute closes, parked tickets, instant closes); and the contract, with service credits per missed metric and the monthly cap.
- `report.html`, `service-review.md` as the agenda for the meeting with two sides (what to raise with the provider, what we owe them), `actions.csv` with owners, `scorecard.csv`, `breaches.csv` with a `cause` column for the provider, `ageing.csv` with a `decision` column, `escalations.csv` and `findings.csv`.
- A read-only PowerShell exporter for Jira Cloud; ServiceNow list exports load as they are.

## How it is built
Python with the standard library only. The demo is a made-up trading company with offices in four cities whose service is run by a fictional provider, with an offshore desk and onsite teams, and 1,454 tickets with the problems placed on purpose. 16 tests and a runbook for before, during and after the meeting.

## What I learned
From managing end-user services with providers: SLAs and OLAs defined and followed, provider and contract negotiation, backlog and ageing follow-up, escalations with offshore teams, and process ownership for incidents, requests, changes and problems. The lesson that shaped the tool is that the review goes better when the internal teams' OLAs are on the same page as the provider's SLAs. Half of the "provider problems" turn out to be queues on our side.

## Next steps
- Run it on last month's export next to the provider's own pack and reconcile the two before the meeting. The difference is the exclusions, and that is the first thing to agree.
- Put the OLAs in `settings.json` only after the internal team leads have agreed them.
- Keep each month's output so the third review can show the trend.""",
 es="""

## El problema
El informe mensual del proveedor dice 96% y los usuarios dicen que el servicio va lento. Normalmente los dos tienen razón. El dato de P2 deja fuera los tickets que pasaron una semana en "esperando al usuario". Los P2 fuera de horario esperan al relevo del follow-the-sun, y la media los esconde. Una quinta parte de los tickets cumplidos se cerraron en el último 10% de la ventana. El proveedor escaló el 19% de sus tickets a los equipos internos, y el equipo de red tiene doce desde julio, así que ese incumplimiento es nuestro. Y el contrato tiene créditos de servicio que nadie ha reclamado, porque nadie los ha calculado. Una revisión de servicio necesita un único conjunto de números que acepten las dos partes, calculado desde los tickets en bruto y con las reglas escritas.

## Qué he hecho
- Una revisión de un mes de tickets en seis áreas: SLA por tipo y prioridad con reloj de horario laboral o 24x7 y el tiempo en pendiente descontado; backlog y antigüedad por equipo; escalados a los equipos internos y sus OLAs, con el reloj arrancando en el traspaso; cobertura dentro y fuera de horario; calidad (reaperturas, resolución al primer contacto, satisfacción, cierres de último minuto, tickets aparcados, cierres instantáneos); y el contrato, con créditos de servicio por métrica incumplida y el tope mensual.
- `report.html`, `service-review.md` como orden del día de la reunión con dos lados (qué plantear al proveedor, qué le debemos), `actions.csv` con responsables, `scorecard.csv`, `breaches.csv` con una columna `cause` para el proveedor, `ageing.csv` con una columna `decision`, `escalations.csv` y `findings.csv`.
- Un exportador de solo lectura en PowerShell para Jira Cloud; las exportaciones de lista de ServiceNow cargan tal cual.

## Cómo está hecho
Python solo con la librería estándar. La demo es una empresa de trading inventada con oficinas en cuatro ciudades cuyo servicio lo opera un proveedor ficticio, con un service desk offshore y equipos presenciales, y 1.454 tickets con los problemas puestos a propósito. 16 tests y un runbook para antes, durante y después de la reunión.

## Qué aprendí
De gestionar servicios de puesto de trabajo con proveedores: SLAs y OLAs definidos y seguidos, negociación de proveedores y contratos, seguimiento del backlog y la antigüedad, escalados con equipos offshore, y ser process owner de incidencias, peticiones, cambios y problemas. La lección que da forma a la herramienta es que la revisión va mejor cuando las OLAs de los equipos internos están en la misma página que los SLAs del proveedor. La mitad de los "problemas del proveedor" resultan ser colas de nuestro lado.

## Siguientes pasos
- Ejecutarlo sobre la exportación del mes pasado junto al informe del proveedor y conciliar los dos antes de la reunión. La diferencia son las exclusiones, y eso es lo primero que hay que acordar.
- Poner las OLAs en `settings.json` solo cuando los responsables de los equipos internos las hayan aceptado.
- Guardar la salida de cada mes para que la tercera revisión pueda enseñar la tendencia."""),
dict(n="29", repo="29-tenant-separation-cutover-planner", date="2026-10-23", cat="tools",
 title_en="Wave 3 is on the 30th and the inventory says no: readiness for a Microsoft 365 tenant split", title_es="La ola 3 es el día 30 y el inventario dice que no: la separación de un tenant de Microsoft 365",
 seo_title_en="Microsoft 365 tenant separation planner · Iñigo González",
 seo_title_es="Separación de tenant Microsoft 365: plan de olas · Iñigo González",
 dek_en="Devices that cannot be reset into the target, users who will fail on day 1, applications without a decision, and a go or no-go per wave with the reason, from the source tenant's own exports.",
 dek_es="Equipos que no se pueden resetear al tenant destino, usuarios que van a fallar el primer día, aplicaciones sin decisión y un go o no-go por ola con su motivo, a partir de las exportaciones del propio tenant origen.",
 en="""

## The problem
A tenant separation is a thousand small resets that all have to work on the same weekend. The programme plan says "wave 3, the plant, 30 November". The inventory says a third of the plant's devices have no TPM, fourteen kiosks have no primary user, ninety devices run an HMI application nobody has catalogued, and the wave has two more devices than the technicians can reset in four days. None of that shows in the project tracker, and all of it is in the Intune, Entra and Exchange exports. The readiness review should start from those exports, not from the plan.

## What I built
- Device readiness with four blockers that stop a wave: no Autopilot hardware hash in the target, BitLocker key not escrowed, hardware not Windows 11 capable, and devices not seen for weeks. Plus the actions for the day itself: OS below the baseline, low disk, domain-only joins, non-compliant devices, local admins the reset will remove, kiosks and applications without a decision.
- User readiness: no MFA method (Conditional Access in the target stops them on day 1), mailboxes too big for the window, licences with no SKU bought in the target, shared mailboxes split across waves, dormant users and leavers.
- A go, go with actions or no-go per wave, with the reason: capacity (technicians, devices per day, days), blocked share, mailbox hours against the migration window, freeze windows, and a pilot that waits for the target tenant to be finished.
- `report.html`, `cutover-plan.md` for the change board with the prerequisites checklist and the order of the cutover day, `blockers.csv` with owner and cleared columns, and the CSVs per wave, device, user and application.
- A read-only PowerShell exporter for Microsoft Graph and Exchange Online.

## How it is built
Python with the standard library only. The demo is a made-up carve-out of an automotive dealer group from its parent: four sites, 1,208 devices, 1,182 users and six waves, with the problems placed on purpose so each wave fails for a different reason. 22 tests and a runbook with the weekly cadence, how to read the verdicts and the usual fix per finding.

## What I learned
From tenant-to-tenant migrations and the Microsoft 365 administration behind them, Windows Autopilot and Intune with ConfigMgr co-management, a Windows 11 migration across sites, and changes taken through the CAB with freeze windows. The lesson that shaped the tool is that a wave rarely fails on the day. It fails weeks before, when nobody counts the devices without a hardware hash or the users without MFA, and the date stays on the plan anyway.

## Next steps
- Join the Windows 11 hardware readiness report to the Graph export, so the hardware check uses real TPM and Secure Boot data.
- Re-run it every week of the programme and keep the dated outputs, so the review shows the blockers going down.
- Agree the wave rules and the freeze calendar with the change board before the first run, not after.""",
 es="""

## El problema
Una separación de tenant son mil reseteos pequeños que tienen que salir bien el mismo fin de semana. El plan del programa dice "ola 3, la planta, 30 de noviembre". El inventario dice que un tercio de los equipos de la planta no tienen TPM, que catorce kioscos no tienen usuario principal, que noventa equipos llevan una aplicación HMI que nadie ha catalogado, y que la ola tiene dos equipos más de los que los técnicos pueden resetear en cuatro días. Nada de eso aparece en el seguimiento del proyecto, y todo está en las exportaciones de Intune, Entra y Exchange. La revisión de preparación debería empezar por esas exportaciones, no por el plan.

## Qué he hecho
- Preparación de equipos con cuatro bloqueos que paran una ola: sin hardware hash de Autopilot en el destino, clave de BitLocker sin custodiar, hardware no apto para Windows 11 y equipos que no se conectan desde hace semanas. Además, las acciones para el propio día: sistema por debajo de la línea base, poco disco, equipos solo unidos al dominio, equipos no conformes, administradores locales que el reseteo va a quitar, kioscos y aplicaciones sin decisión.
- Preparación de usuarios: sin método de MFA (el acceso condicional del destino los para el primer día), buzones demasiado grandes para la ventana, licencias sin SKU comprado en el destino, buzones compartidos repartidos entre olas, usuarios inactivos y bajas.
- Un go, go con acciones o no-go por ola, con su motivo: capacidad (técnicos, equipos por día, días), porcentaje de bloqueados, horas de migración de buzones frente a la ventana, periodos de congelación y un piloto que espera a que el tenant destino esté terminado.
- `report.html`, `cutover-plan.md` para el comité de cambios con el checklist de prerrequisitos y el orden del día del corte, `blockers.csv` con columnas de responsable y resuelto, y los CSV por ola, equipo, usuario y aplicación.
- Un exportador de solo lectura en PowerShell para Microsoft Graph y Exchange Online.

## Cómo está hecho
Python solo con la librería estándar. La demo es una segregación inventada de un grupo de concesionarios de automoción respecto a su matriz: cuatro sedes, 1.208 equipos, 1.182 usuarios y seis olas, con los problemas puestos a propósito para que cada ola falle por un motivo distinto. 22 tests y un runbook con la cadencia semanal, cómo leer los veredictos y la corrección habitual de cada hallazgo.

## Qué aprendí
De migraciones tenant a tenant y la administración de Microsoft 365 que hay detrás, de Windows Autopilot e Intune con co-gestión de ConfigMgr, de una migración a Windows 11 en varias sedes, y de cambios pasados por el CAB con periodos de congelación. La lección que da forma a la herramienta es que una ola rara vez falla el día del corte. Falla semanas antes, cuando nadie cuenta los equipos sin hardware hash o los usuarios sin MFA, y la fecha sigue en el plan igualmente.

## Siguientes pasos
- Unir el informe de preparación de hardware para Windows 11 con la exportación de Graph, para que la comprobación de hardware use datos reales de TPM y Secure Boot.
- Ejecutarlo cada semana del programa y guardar las salidas con fecha, para que la revisión enseñe cómo bajan los bloqueos.
- Acordar las reglas de las olas y el calendario de congelación con el comité de cambios antes de la primera ejecución, no después."""),
dict(n="30", repo="30-jira-confluence-admin-kit", date="2026-10-24", cat="tools",
 title_en="128 unused licences and a sprint nine days late: a monthly Jira and Confluence review", title_es="128 licencias sin uso y un sprint abierto nueve días tarde: revisión mensual de Jira y Confluence",
 seo_title_en="Jira and Confluence admin review · Iñigo González",
 seo_title_es="Revisión de admin de Jira y Confluence · Iñigo González",
 dek_en="Licences to reclaim with the saving, admins who should not be admins, external users and service accounts without an owner, projects, spaces and custom fields to clean up, and the agile health of every Scrum board, from the site's own exports.",
 dek_es="Licencias a recuperar con el ahorro, administradores que no deberían serlo, usuarios externos y cuentas de servicio sin responsable, proyectos, espacios y campos personalizados que limpiar, y la salud ágil de cada tablero Scrum, a partir de las exportaciones del propio sitio.",
 en="""

## The problem
An Atlassian site grows by itself. Everybody who joins gets Jira through a default group, whether they will use it or not. Contractors keep access after the project ends. Somebody added a colleague to `jira-admins` "for a day" two years ago. A demo project still lets Anyone browse it. There are 460 custom fields, and a third of them have not been used in a year. And two Scrum boards carry over a third of every sprint, which nobody notices because the board still looks busy. None of this is hard to fix. It is hard to see. The licence renewal, the access review and the retrospective all need the same thing: a list, the rule that put each item on it, and a column for the decision.

## What I built
- Licences: product access not used for 90 days, never used after the grace period (the default-group problem), or kept by suspended accounts, with the cost per year and the seats against what was bought.
- Access: more admins than the target, admins who are deactivated or idle, admins on personal domains, external users by domain, and service accounts without a named owner.
- Jira and Confluence hygiene: projects open to Anyone, projects without a lead or with a lead who has left, idle projects and spaces to archive, one-off permission and workflow schemes, spaces with anonymous access or no active admin, personal spaces of leavers, and custom fields to remove.
- Agile health per Scrum board over the last six sprints: sprints still open past their end date, carry-over, scope added after the start, say/do, and idle boards.
- `report.html`, `admin-review.md` as the agenda with the decisions as a checklist, `licences.csv` with `manager_ok` and `removed` columns, `access-review.csv` with a `decision` column, and the CSVs per project, space, field and board.
- A read-only PowerShell exporter for the Jira, Agile and Confluence Cloud REST APIs; the user export from admin.atlassian.com loads as it is.

## How it is built
Python with the standard library only. The demo is a made-up warehouse-robotics company on Jira, Jira Service Management and Confluence Cloud: 437 user accounts, 61 projects, 77 spaces, 460 custom fields and 12 Scrum boards, with the problems placed on purpose. 17 tests and a 45-minute runbook with how to read the agile numbers.

## What I learned
From administering Jira and Confluence and managing the relationship with Atlassian, working as Scrum Master and Product Owner with Kanban and portfolio views, running release management with changes through the CAB, and managing licences and vendors. The lesson that shaped the tool is that the licence saving pays for the review, but the agile numbers are what the teams come for. They are conversation starters for the retrospective, not targets, and one team's trend against itself is the only comparison that means anything.

## Next steps
- Run it before the next renewal and give managers a week to object before any licence is removed.
- Agree the admin target and the service-account owners with security before the first review.
- Keep each month's output, so the next review opens with what changed since the last one.""",
 es="""

## El problema
Un sitio de Atlassian crece solo. Todo el que entra recibe Jira por un grupo por defecto, lo vaya a usar o no. Los externos siguen con acceso cuando termina el proyecto. Alguien metió a un compañero en `jira-admins` "por un día" hace dos años. Un proyecto de demo sigue abierto a Anyone. Hay 460 campos personalizados y un tercio no se ha usado en un año. Y dos tableros Scrum arrastran un tercio de cada sprint al siguiente, cosa que nadie nota porque el tablero sigue pareciendo activo. Nada de esto es difícil de arreglar. Es difícil de ver. La renovación de licencias, la revisión de accesos y la retrospectiva necesitan lo mismo: una lista, la regla que puso cada elemento en ella y una columna para la decisión.

## Qué he hecho
- Licencias: acceso a producto sin usar en 90 días, nunca usado pasado el periodo de gracia (el problema del grupo por defecto) o en manos de cuentas suspendidas, con el coste anual y las licencias frente a las compradas.
- Accesos: más administradores que el objetivo, administradores desactivados o inactivos, administradores con dominios personales, usuarios externos por dominio y cuentas de servicio sin responsable con nombre.
- Higiene de Jira y Confluence: proyectos abiertos a Anyone, proyectos sin responsable o con un responsable que ya no está, proyectos y espacios inactivos para archivar, esquemas de permisos y de flujo usados por un solo proyecto, espacios con acceso anónimo o sin administrador activo, espacios personales de bajas y campos personalizados que eliminar.
- Salud ágil por tablero Scrum en los últimos seis sprints: sprints abiertos después de su fecha de fin, trabajo arrastrado, alcance añadido después del inicio, say/do y tableros parados.
- `report.html`, `admin-review.md` como orden del día con las decisiones en forma de checklist, `licences.csv` con columnas `manager_ok` y `removed`, `access-review.csv` con una columna `decision`, y los CSV por proyecto, espacio, campo y tablero.
- Un exportador de solo lectura en PowerShell para las API REST de Jira, Agile y Confluence Cloud; la exportación de usuarios de admin.atlassian.com carga tal cual.

## Cómo está hecho
Python solo con la librería estándar. La demo es una empresa inventada de robótica de almacenes con Jira, Jira Service Management y Confluence Cloud: 437 cuentas de usuario, 61 proyectos, 77 espacios, 460 campos personalizados y 12 tableros Scrum, con los problemas puestos a propósito. 17 tests y un runbook de 45 minutos con cómo leer los números ágiles.

## Qué aprendí
De administrar Jira y Confluence y llevar la relación con Atlassian, de trabajar como Scrum Master y Product Owner con Kanban y vistas de portfolio, de llevar la gestión de releases con los cambios por el CAB, y de gestionar licencias y proveedores. La lección que da forma a la herramienta es que el ahorro en licencias paga la revisión, pero los números ágiles son lo que interesa a los equipos. Sirven para abrir la conversación en la retrospectiva, no son objetivos, y la única comparación que tiene sentido es la de un equipo consigo mismo en el tiempo.

## Siguientes pasos
- Ejecutarlo antes de la próxima renovación y dar a los responsables una semana para objetar antes de quitar ninguna licencia.
- Acordar con seguridad el objetivo de administradores y los responsables de las cuentas de servicio antes de la primera revisión.
- Guardar la salida de cada mes, para que la siguiente revisión empiece por lo que ha cambiado desde la anterior."""),
dict(n="31", repo="31-dealer-systems-health", date="2026-10-25", cat="tools",
 title_en="The warranty feed stopped on Thursday and the dealer found out on Tuesday: a dealer network review", title_es="El feed de garantías paró el jueves y el concesionario lo supo el martes: la red de concesionarios",
 seo_title_en="Dealer network systems: weekly health review · Iñigo González",
 seo_title_es="Sistemas de una red de concesionarios: revisión semanal · Iñigo González",
 seo_desc="Weekly review of a dealer network: stopped DMS feeds, warranty claims near the deadline, parts and price files per dealer, in red, amber or green.",
 dek_en="DMS feeds that stopped or send nothing, warranty claims about to miss the deadline and why they are rejected, the parts catalogue and price file each dealer really uses, and the dealers opening or leaving, per dealer and in red, amber or green.",
 dek_es="Feeds del DMS parados o vacíos, garantías a punto de caducar y por qué se rechazan, el catálogo de recambios y la tarifa que usa de verdad cada concesionario, y los concesionarios que abren o se van, por concesionario y en rojo, ámbar o verde.",
 en="""

## The problem
A car brand's aftersales runs on systems that live at the dealers. When a dealer's warranty feed stops on a Thursday night, nobody notices until the dealer asks on Tuesday why its claims have no answer. A DMS job that "succeeds" with zero records alerts nobody at all. A dealer still on last month's parts catalogue sends labour operations the warranty system no longer accepts, its rejection rate climbs, and the conversation turns to bad claims instead of an old catalogue. A price file that did not apply means a week of parts sold at the wrong price. And the dealer that closed in September still has working interface credentials. Each of these lives in a different system; the weekly review needs them side by side, per dealer, with the team that owns each fix.

## What I built
- Interfaces: feeds with no successful run within the limit (one failed night is already red for repair orders and warranty claims), feeds rejecting records, and feeds that succeed with nothing in them.
- Warranty: drafts past or close to the submission limit, claims waiting for the brand's own decision, information requests nobody answered, rejection rate per dealer with the main reasons, possible duplicates (same VIN and labour operation), and accepted claims that were never paid.
- Parts: the catalogue version and price file each dealer has actually applied, against the current ones and their grace periods.
- Network: DMS versions not certified for the brand interfaces, dealers opening with checklist items still open, and terminated dealers still sending data.
- `report.html` with the network as a red/amber/green grid, `dealer-review.md` as the agenda for the weekly call, `dealers.csv`, `interfaces.csv`, `claims-at-risk.csv` with who each claim is waiting on, `rejections.csv` and `catalogue.csv`.
- A read-only PowerShell exporter with example SQL queries that refuses anything but a single SELECT.

## How it is built
Python with the standard library only. The demo is a made-up importer with 53 dealers in Spain and Portugal, two weeks of interface runs and about 4,600 warranty claims, with the problems placed on purpose. 15 tests, a runbook for the weekly review, and a GitHub Actions workflow that runs the tests and rebuilds the demo data and the screenshot.

## What I learned
From working with dealer management systems and dealer networks, warranty claim management and aftersales parts catalogues, together with integrations, vendors, SLAs and OLAs. The lesson that shaped the tool is that most "dealer problems" have a systems cause one step upstream: a rejection rate that is really an old catalogue, a late claim that is really a feed that stopped, a backlog that is really the brand's own queue. Putting the four sources on one page per dealer is what makes that visible.

## Next steps
- Run it on one region's real exports first and agree the limits with the warranty team before showing it to the dealers.
- Adapt the three SQL queries to the integration log and the warranty system once, and schedule the export for Monday morning.
- Send each red dealer's line to its area manager before the call, so the meeting is about fixes and not about discovering the problems.""",
 es="""

## El problema
La posventa de una marca de coches funciona con sistemas que están en los concesionarios. Cuando el feed de garantías de un concesionario se para un jueves por la noche, nadie se entera hasta que el concesionario pregunta el martes por qué sus reclamaciones no tienen respuesta. Un trabajo del DMS que "termina bien" con cero registros no avisa a nadie. Un concesionario que sigue con el catálogo de recambios del mes pasado envía operaciones de mano de obra que el sistema de garantías ya no acepta, su tasa de rechazo sube y la conversación acaba en reclamaciones mal hechas en vez de en un catálogo viejo. Una tarifa que no se aplicó significa una semana de recambios vendidos al precio equivocado. Y el concesionario que cerró en septiembre sigue teniendo credenciales de interfaz que funcionan. Cada cosa vive en un sistema distinto; la revisión semanal necesita verlas juntas, por concesionario, con el equipo responsable de cada corrección.

## Qué he hecho
- Interfaces: feeds sin una ejecución correcta dentro del límite (una noche fallida ya es rojo para órdenes de reparación y garantías), feeds que rechazan registros y feeds que terminan bien sin traer nada.
- Garantías: borradores pasados o cerca del límite de envío, reclamaciones esperando la decisión de la propia marca, peticiones de información sin contestar, tasa de rechazo por concesionario con los motivos principales, posibles duplicados (mismo VIN y misma operación) y reclamaciones aceptadas que nunca se pagaron.
- Recambios: la versión de catálogo y la tarifa que cada concesionario ha aplicado de verdad, frente a las vigentes y sus periodos de gracia.
- Red: versiones de DMS no certificadas para las interfaces de la marca, concesionarios que abren con tareas del checklist sin cerrar y concesionarios dados de baja que siguen enviando datos.
- `report.html` con la red en una cuadrícula roja, ámbar y verde, `dealer-review.md` como orden del día de la reunión semanal, `dealers.csv`, `interfaces.csv`, `claims-at-risk.csv` con a quién está esperando cada reclamación, `rejections.csv` y `catalogue.csv`.
- Un exportador de solo lectura en PowerShell con consultas SQL de ejemplo que rechaza cualquier cosa que no sea un único SELECT.

## Cómo está hecho
Python solo con la librería estándar. La demo es un importador inventado con 53 concesionarios en España y Portugal, dos semanas de ejecuciones de interfaces y unas 4.600 reclamaciones de garantía, con los problemas puestos a propósito. 15 tests, un runbook para la revisión semanal y un workflow de GitHub Actions que ejecuta los tests y regenera los datos de la demo y la captura.

## Qué aprendí
De trabajar con sistemas de gestión de concesionarios (DMS) y redes de concesionarios, gestión de garantías y catálogos de recambios de posventa, junto con integraciones, proveedores, SLAs y OLAs. La lección que da forma a la herramienta es que la mayoría de los "problemas del concesionario" tienen una causa de sistemas un paso antes: una tasa de rechazo que en realidad es un catálogo viejo, una reclamación tardía que en realidad es un feed parado, un atasco que en realidad es la cola de la propia marca. Poner las cuatro fuentes en una sola página por concesionario es lo que lo hace visible.

## Siguientes pasos
- Ejecutarlo primero con las exportaciones reales de una región y acordar los límites con el equipo de garantías antes de enseñárselo a los concesionarios.
- Adaptar una vez las tres consultas SQL al log de integraciones y al sistema de garantías, y programar la exportación para el lunes por la mañana.
- Enviar la línea de cada concesionario en rojo a su jefe de zona antes de la reunión, para que la reunión vaya de soluciones y no de descubrir los problemas."""),
dict(n="32", repo="32-backup-restore-test-tracker", date="2026-10-25", cat="tools",
 title_en="The backup ran every night, but would it bring the system back? Backups, restores and DR monthly",
 title_es="El backup corrió cada noche, pero ¿devolvería el sistema? Backups, restauraciones y DR cada mes",
 seo_title_en="Backup restore tests and DR review · Iñigo González",
 seo_title_es="Pruebas de restauración de backups y DR · Iñigo González",
 dek_en="The last good backup of each system against its RPO, offsite and immutable copies that actually ran, restore tests against the plan and the RTO, and the DR exercises and their actions, per system and tier, in red, amber or green.",
 dek_es="El último backup bueno de cada sistema frente a su RPO, las copias offsite e inmutables que de verdad se hicieron, las pruebas de restauración frente al plan y al RTO, y los ejercicios de DR y sus acciones, por sistema y nivel, en rojo, ámbar o verde.",
 en="""

## The problem
A green backup dashboard says the jobs ran. It does not say the system can be brought back within the time the business was promised. A job scheduled every night that failed three nights in a row is three days outside a 24-hour RPO. A copy job that exists but has failed for a week leaves the system with one copy, in one place. Restoring a file proves the backup is readable, not that the ERP comes back in four hours. A test where "the database came back but the application could not log in" is exactly what a real recovery would hit. And an auditor counts the evidence, not the tests. The answers live in the backup console, a spreadsheet of tests, the change tickets and the continuity plan; the monthly review needs them side by side.

## What I built
- Backups: systems in scope with no backup job, the last good backup against each system's RPO, failure streaks, the offsite and immutable copies each tier requires, and jobs still running for retired or unknown systems.
- Restore tests: systems never restored, last tests that failed or half worked, tests overdue against the plan for their tier, restores slower than the RTO (measured only on full restores), systems only tested with file or item restores, and tests with no evidence.
- DR exercises: the last exercise, exercises planned and not done, and actions past their due date.
- `report.html` with tier 1 at a glance and a 12-month calendar of tests due, `restore-review.md` as the agenda, `tests-due.csv` with booked and done columns, `failing-backups.csv` and `evidence-pack.csv` for the auditor.
- A read-only PowerShell exporter for Veeam job sessions; other tools' job reports work as CSV.

## How it is built
Python with the standard library only. The demo is a made-up manufacturer with 76 systems in three tiers, two weeks of job runs, a year of restore tests and its DR exercises, with the problems placed on purpose. 13 tests, a runbook for the monthly review, and a GitHub Actions workflow that runs the tests and rebuilds the demo data and the screenshot.

## What I learned
From my work with Veeam Backup and Commvault, and tape backups earlier on, designing and testing backup and DR plans, and supervising DR and business continuity tests aligned with ISO 22301. The lesson that shaped the tool is that the question is never "did the job run?" but "when did we last prove we can get this system back, how long did it take, and where is the evidence?". Measuring the RPO from the last good backup and the RTO only from full restores is what turns a green dashboard into an honest one.

## Next steps
- Run it first on the tier 1 systems with one month of real exports, and agree the test frequency per tier with the service owners.
- Schedule the Veeam export for the first Monday of the month and keep each month's output folder.
- Use `tests-due.csv` to book the next month's restore tests in the change calendar, tier 1 first.""",
 es="""

## El problema
Un panel de backups en verde dice que los trabajos se ejecutaron. No dice que el sistema se pueda recuperar en el tiempo que se prometió al negocio. Un trabajo programado cada noche que ha fallado tres noches seguidas está tres días fuera de un RPO de 24 horas. Una copia que existe pero lleva una semana fallando deja el sistema con una sola copia, en un solo sitio. Restaurar un fichero demuestra que el backup se puede leer, no que el ERP vuelva en cuatro horas. Una prueba en la que "la base de datos volvió pero la aplicación no podía iniciar sesión" es justo lo que pasaría en una recuperación real. Y un auditor cuenta las evidencias, no las pruebas. Las respuestas están en la consola de backup, una hoja de pruebas, los tickets de cambio y el plan de continuidad; la revisión mensual necesita verlas juntas.

## Qué he hecho
- Backups: sistemas en alcance sin trabajo de backup, el último backup bueno frente al RPO de cada sistema, rachas de fallos, las copias offsite e inmutables que exige cada nivel y trabajos que siguen corriendo para sistemas retirados o desconocidos.
- Pruebas de restauración: sistemas nunca restaurados, últimas pruebas fallidas o a medias, pruebas vencidas frente al plan de su nivel, restauraciones más lentas que el RTO (medido solo con restauraciones completas), sistemas probados solo con ficheros o elementos y pruebas sin evidencia.
- Ejercicios de DR: el último ejercicio, ejercicios planificados y no hechos, y acciones pasadas de fecha.
- `report.html` con el nivel 1 de un vistazo y un calendario de 12 meses de pruebas pendientes, `restore-review.md` como orden del día, `tests-due.csv` con columnas de reservado y hecho, `failing-backups.csv` y `evidence-pack.csv` para el auditor.
- Un exportador de solo lectura en PowerShell para las sesiones de Veeam; los informes de otras herramientas sirven en CSV.

## Cómo está hecho
Python solo con la librería estándar. La demo es un fabricante inventado con 76 sistemas en tres niveles, dos semanas de trabajos, un año de pruebas de restauración y sus ejercicios de DR, con los problemas puestos a propósito. 13 tests, un runbook para la revisión mensual y un workflow de GitHub Actions que ejecuta los tests y regenera los datos de la demo y la captura.

## Qué aprendí
De mi trabajo con Veeam Backup y Commvault, y antes con backups en cinta, diseñando y probando planes de backup y DR, y supervisando pruebas de DR y continuidad de negocio alineadas con ISO 22301. La lección que da forma a la herramienta es que la pregunta nunca es "¿se ejecutó el trabajo?", sino "¿cuándo demostramos por última vez que podemos recuperar este sistema, cuánto tardó y dónde está la evidencia?". Medir el RPO desde el último backup bueno y el RTO solo con restauraciones completas es lo que convierte un panel en verde en uno honesto.

## Siguientes pasos
- Ejecutarlo primero con los sistemas de nivel 1 y un mes de exportaciones reales, y acordar la frecuencia de pruebas por nivel con los responsables de servicio.
- Programar la exportación de Veeam para el primer lunes de cada mes y guardar la carpeta de resultados de cada mes.
- Usar `tests-due.csv` para reservar las pruebas del mes siguiente en el calendario de cambios, empezando por el nivel 1."""),
dict(n="33", repo="33-executive-meeting-readiness", date="2026-10-25", cat="tools",
 title_en="The chair's iPad had not synced for twelve days: a readiness check for board and executive meetings",
 title_es="El iPad del presidente llevaba doce días sin sincronizar: una revisión de preparación para consejos y comités",
 seo_title_en="Board meeting IT readiness: Teams Rooms, VIP · Iñigo González",
 seo_title_es="Preparación IT de consejos: Teams Rooms y VIP · Iñigo González",
 dek_en="For every board, committee and executive meeting in the next two weeks: the tech check, the Teams Room and its peripherals, updates inside the freeze, the VIP devices and the support engineer, with a verdict per meeting.",
 dek_es="Para cada consejo, comité y reunión de dirección de las próximas dos semanas: la prueba técnica, la sala Teams Rooms y sus periféricos, actualizaciones dentro de la congelación, los dispositivos VIP y el técnico de soporte, con un veredicto por reunión.",
 en="""

## The problem
When a board meeting starts, nobody remembers the dashboard was green. They remember the remote director who could not hear the room, the chair's iPad that had not synced the pack, or the update that rebooted the room at 08:55. Each of those was visible days before: the microphone array showed as disconnected in the Teams Rooms health, the iPad had not checked in to the MDM for twelve days, the update was scheduled for the night before, and the rehearsal planned for last week never happened. The signals live in the Teams admin center, Intune or Jamf, the room calendars and the service desk; the check that matters joins them per meeting.

## What I built
- Meetings: board, committee and investor meetings without a tech check in the last week, rooms that do not fit (too small, or hybrid in a room with no Teams Room), overlapping bookings or no setup time, and meetings with no support engineer.
- Rooms: Teams Rooms offline or not reporting, faulty camera, microphone, speaker or display (critical when audio or video is down in a hybrid meeting), updates inside the freeze before the meeting, and rooms with repeated incidents.
- VIP devices: not compliant or not checked in, OS or board app below the minimum, worn batteries, attendees with no registered device, and warranties ending.
- A verdict per meeting (ready, attention or at risk), `report.html` day by day, `readiness-pack.md` with a checklist per meeting and attendee, and CSVs for meetings, rooms, VIP devices and incidents.
- A read-only PowerShell exporter for Microsoft Graph: Teams Rooms health, room calendars and Intune devices.

## How it is built
Python with the standard library only. The demo is a made-up insurer with eleven rooms in three offices (Crestron, Logitech and Poly systems), 13 meetings in the next two weeks, 20 VIP devices and 90 days of room incidents, with the problems placed on purpose. 13 tests, a runbook for the weekly check, and a GitHub Actions workflow that runs the tests and rebuilds the demo data and the screenshot.

## What I learned
From supporting board and executive committee meetings: Teams Rooms on Crestron with Logitech and Poly systems, iPads, MacBooks and iPhones managed with Jamf Pro and Intune, and VIP support for executives and board members. The lesson that shaped the tool is that readiness belongs to the meeting, not to the room: the same degraded display is a note for an internal workshop and a decision for the board. It complements the fleet view of repo 17, which looks at every room every morning.

## Next steps
- Run it on the next month of board and committee meetings, with the executive office filling in the tech checks and the support engineers.
- Agree the freeze window and the minimum OS and board app versions with the AV provider and the VIP support team.
- Send the readiness pack to the company secretary's team the day before each board meeting.""",
 es="""

## El problema
Cuando empieza un consejo, nadie se acuerda de que el panel estaba en verde. Se acuerdan del consejero en remoto que no oía la sala, del iPad del presidente que no había sincronizado la documentación o de la actualización que reinició la sala a las 08:55. Todo eso se veía días antes: el array de micrófonos aparecía desconectado en la salud de Teams Rooms, el iPad llevaba doce días sin conectar con el MDM, la actualización estaba programada para la noche anterior y la prueba técnica prevista la semana pasada nunca se hizo. Las señales están en el centro de administración de Teams, Intune o Jamf, los calendarios de las salas y la herramienta de soporte; la revisión que importa las junta por reunión.

## Qué he hecho
- Reuniones: consejos, comités y reuniones con inversores sin prueba técnica en la última semana, salas que no encajan (pequeñas, o reunión híbrida en una sala sin Teams Rooms), reservas solapadas o sin tiempo de preparación, y reuniones sin técnico asignado.
- Salas: Teams Rooms desconectadas o sin reportar, cámara, micrófono, altavoz o pantalla con fallos (crítico si el audio o el vídeo caen en una reunión híbrida), actualizaciones dentro de la congelación previa y salas con incidencias repetidas.
- Dispositivos VIP: sin cumplir la política o sin conectar, sistema operativo o app del consejo por debajo del mínimo, baterías gastadas, asistentes sin dispositivo registrado y garantías que vencen.
- Un veredicto por reunión (lista, atención o en riesgo), `report.html` día a día, `readiness-pack.md` con una lista de comprobación por reunión y asistente, y CSVs de reuniones, salas, dispositivos VIP e incidencias.
- Un exportador de solo lectura en PowerShell para Microsoft Graph: salud de Teams Rooms, calendarios de salas y dispositivos de Intune.

## Cómo está hecho
Python solo con la librería estándar. La demo es una aseguradora inventada con once salas en tres oficinas (sistemas Crestron, Logitech y Poly), 13 reuniones en las próximas dos semanas, 20 dispositivos VIP y 90 días de incidencias de salas, con los problemas puestos a propósito. 13 tests, un runbook para la revisión semanal y un workflow de GitHub Actions que ejecuta los tests y regenera los datos de la demo y la captura.

## Qué aprendí
De dar soporte a consejos y comités de dirección: Teams Rooms sobre Crestron con sistemas Logitech y Poly, iPads, MacBooks e iPhones gestionados con Jamf Pro e Intune, y soporte VIP a directivos y consejeros. La lección que da forma a la herramienta es que la preparación es de la reunión, no de la sala: la misma pantalla degradada es una nota para un taller interno y una decisión para el consejo. Complementa la vista de flota del repo 17, que revisa todas las salas cada mañana.

## Siguientes pasos
- Ejecutarlo con los consejos y comités del próximo mes, con la oficina de presidencia rellenando las pruebas técnicas y los técnicos asignados.
- Acordar la ventana de congelación y las versiones mínimas de sistema operativo y app del consejo con el proveedor audiovisual y el equipo de soporte VIP.
- Enviar el pack de preparación al equipo de secretaría del consejo el día antes de cada consejo."""),
dict(n="34", repo="34-venue-service-readiness", date="2026-10-26", cat="tools",
 title_en="The only kitchen printer had been down since yesterday: a morning check for a hospitality venue",
 title_es="La única impresora de cocina llevaba caída desde ayer: la revisión de cada mañana en hostelería",
 seo_title_en="Hospitality IT opening check: POS and Wi-Fi · Iñigo González",
 seo_title_es="Revisión IT de apertura en hostelería: TPV y Wi-Fi · Iñigo González",
 dek_en="For every service in the next week, in a restaurant, a pool club, a bar and a hotel: the opening check, enough working tills and handhelds, kitchen printers, card terminals and cash machines, the network and the failover, the PMS and IPTV, and the vendor who would fix each of them, with a verdict per service.",
 dek_es="Para cada servicio de la próxima semana, en un restaurante, un pool club, un bar y un hotel: la prueba de apertura, suficientes TPV y comanderos funcionando, impresoras de cocina, datáfonos y cajones de efectivo, la red y su respaldo, el PMS y la IPTV, y el proveedor que arreglaría cada cosa, con un veredicto por servicio.",
 en="""

## The problem
When the pool club fills up at one o'clock, nobody remembers that the monitoring was green at nine. They remember the orders that never reached the kitchen, the queue at the only card terminal that worked, or the room charges that never reached the guest's bill. Each of those was visible that morning: the beach kitchen printer had been in error since the afternoon before, two of the four handhelds were dead or in a drawer, the backup internet line had been down for five days, and the PMS interface had 37 charges waiting. The POS vendor answers until seven in the evening; the bar closes at one. The signals live in the POS back office, the network controller, the cash machine and PMS consoles and the vendors' portals; the check that matters joins them per service.

## What I built
- Services: no opening check close to opening, big services and events with nobody from IT on duty, and device updates scheduled inside the freeze before a service.
- POS and payments: fewer working tills and handhelds than the guests need, kitchen printers or KDS down where there is food, card terminals down, and cash machines in error, short of change or with a full stacker.
- Network and guest systems: primary or backup internet line down, Wi-Fi access points, switches and firewall, the PMS interface for room charges, IPTV in the rooms and the key card encoders.
- Vendors: open tickets past each vendor's SLA, contracts ended or ending, and services that open or close outside the vendor's support hours.
- `report.html` with the services day by day and devices by outlet, `opening-pack.md` as the checklist for the outlet managers, and CSVs for services, devices, vendor cover and incidents.
- A read-only PowerShell probe that pings every device on the venue network and keeps the last time each one answered.

## How it is built
Python with the standard library only. The demo is a made-up beach club and boutique hotel with a restaurant, a pool club, a sunset bar and 24 rooms, 16 services in a week including a 900-guest Halloween night, 74 devices and five vendors, with the problems placed on purpose. 15 tests, a runbook for the morning check, and a GitHub Actions workflow that runs the tests and rebuilds the demo data and the screenshot.

## What I learned
From my first years in IT supporting hospitality clients, with POS systems such as ICG and HIOPOS, CashDro cash machines, hotel PMS and IPTV, and later from around 200 pre-openings of luxury brand corners in department stores. At one of them the connection failed two hours before opening; I solved it with a temporary USB router while I checked the line and the floor's comms room with the store's technicians. The lesson that shaped the tool is that a service is only as ready as its weakest device and the vendor who would fix it at that hour, so the verdict is per service, and the backup line, the spare handheld and the vendor's hours are part of the plan.

## Next steps
- Run it every morning for two weeks with the real device register and service plan, and tune the guests per till and the opening check with the outlet managers.
- Read the device states from the POS back office and the network controller instead of the probe.
- Send each outlet manager their service's checklist before opening, and write the minutes lost back after closing for the vendors' monthly reviews.""",
 es="""

## El problema
Cuando el pool club se llena a la una, nadie se acuerda de que la monitorización estaba en verde a las nueve. Se acuerdan de las comandas que nunca llegaron a cocina, de la cola en el único datáfono que funcionaba o de los cargos a habitación que nunca llegaron a la factura del cliente. Todo eso se veía esa misma mañana: la impresora de la cocina de playa llevaba en error desde la tarde anterior, dos de los cuatro comanderos estaban sin batería o en un cajón, la línea de internet de respaldo llevaba cinco días caída y el interfaz del PMS tenía 37 cargos pendientes. El proveedor del TPV atiende hasta las siete de la tarde; el bar cierra a la una. Las señales están en el back office del TPV, el controlador de red, las consolas de los cajones de efectivo y del PMS y los portales de los proveedores; la revisión que importa las junta por servicio.

## Qué he hecho
- Servicios: sin prueba de apertura cerca de abrir, servicios grandes y eventos sin nadie de IT de guardia, y actualizaciones de equipos programadas dentro de la congelación antes de un servicio.
- TPV y pagos: menos TPV y comanderos funcionando de los que necesitan los clientes, impresoras de cocina o KDS caídas donde hay comida, datáfonos caídos, y cajones de efectivo en error, sin cambio o con el depósito lleno.
- Red y sistemas del cliente: línea de internet principal o de respaldo caída, puntos de acceso Wi-Fi, switches y firewall, el interfaz del PMS para los cargos a habitación, la IPTV de las habitaciones y los codificadores de tarjetas.
- Proveedores: tickets abiertos fuera del SLA de cada proveedor, contratos vencidos o a punto de vencer, y servicios que abren o cierran fuera del horario de soporte del proveedor.
- `report.html` con los servicios día a día y los equipos por zona, `opening-pack.md` como checklist para los responsables de cada zona, y CSV de servicios, equipos, cobertura de proveedores e incidencias.
- Una prueba de solo lectura en PowerShell que hace ping a cada equipo de la red del local y guarda la última vez que respondió.

## Cómo está hecho
Python solo con la librería estándar. La demo es un beach club con hotel boutique inventado, con restaurante, pool club, bar de atardecer y 24 habitaciones, 16 servicios en una semana con una noche de Halloween para 900 personas, 74 equipos y cinco proveedores, con los problemas puestos a propósito. 15 tests, un runbook para la revisión de cada mañana y un workflow de GitHub Actions que ejecuta los tests y regenera los datos de la demo y la captura.

## Qué aprendí
De mis primeros años en IT dando soporte a clientes de hostelería, con TPV como ICG y HIOPOS, cajones CashDro, PMS hotelero e IPTV, y después de unas 200 preaperturas de corners de marcas de lujo en grandes almacenes. En una de ellas la conexión falló a dos horas de abrir; lo resolví con un router USB temporal mientras revisaba la línea y la sala de comunicaciones de la planta con los técnicos de los grandes almacenes. La lección que da forma a la herramienta es que un servicio está tan preparado como su equipo más débil y el proveedor que lo arreglaría a esa hora, así que el veredicto es por servicio, y la línea de respaldo, el comandero de repuesto y el horario del proveedor forman parte del plan.

## Siguientes pasos
- Ejecutarlo cada mañana durante dos semanas con el inventario real de equipos y el plan de servicios, y ajustar los clientes por TPV y la prueba de apertura con los responsables de cada zona.
- Leer el estado de los equipos del back office del TPV y del controlador de red en lugar de la prueba de ping.
- Enviar a cada responsable el checklist de su servicio antes de abrir, y registrar los minutos perdidos al cerrar para las revisiones mensuales con los proveedores."""),
dict(n="35", repo="35-private-cloud-capacity-review", date="2026-10-27", cat="tools",
 title_en="The cluster looked fine at 74%: a monthly capacity and availability review of a private cloud",
 title_es="El clúster parecía ir bien al 74%: una revisión mensual de capacidad y disponibilidad de una nube privada",
 seo_title_en="Private cloud capacity: vSphere and Nutanix · Iñigo González",
 seo_title_es="Capacidad de nube privada: vSphere y Nutanix · Iñigo González",
 dek_en="For every vSphere and Nutanix cluster: the CPU and RAM left after a host failure, the vCPU ratio, a 12-month trend with the approved projects and the reclaim list, the month it crosses its N+1 limit against the purchase lead time, datastores, and the month's availability.",
 dek_es="Para cada clúster vSphere y Nutanix: la CPU y la RAM que quedan tras caer un host, el ratio de vCPU, una tendencia de 12 meses con los proyectos aprobados y la lista de recuperación, el mes en que cruza su límite N+1 frente al plazo de compra, los datastores y la disponibilidad del mes.",
 en="""

## The problem
Capacity is a date, not a percentage. A cluster at 74% of its RAM looks healthy on the dashboard. Take away the host that HA needs as a spare, though, and it is at 85% of what is left. It grows half a point a month, and two approved projects land in January and March. Put the three facts together and the cluster crosses its N+1 limit in January. New hosts take four months to order, deliver and add to the cluster, so the decision was due in September. The facts live in different places: capacity and utilisation in vCenter and Prism Central, projects in the portfolio, powered-off VMs and forgotten snapshots in the inventory, outages in the incident records. The monthly capacity review is where they meet.

## What I built
- Headroom after a host failure: the CPU and RAM left when the largest host fails, the vCPU:pCPU ratio against the policy, vRAM overcommit, and hosts in maintenance.
- Runway: the latest p95 plus a linear trend over 12 months, with the approved projects added at their go-live month and the reclaim list taken away. The result is the month each cluster crosses its limit, the month to order by and the hosts to add.
- Reclaim: VMs powered off for 30 or 90 days, idle VMs, VMs oversized against their p95 with the recommended size, old snapshots, and VMs without an owner, with the RAM and storage each one gives back.
- Storage and availability: datastores below the free space threshold, thin provisioning, cluster outages against the availability target, host failures and HA restarts, and hosts out of vendor support.
- `report.html` with a card and a runway chart per cluster, `capacity-review.md` with the decisions table for the meeting, and CSVs for clusters, forecast, reclaim, datastores and demand.
- A read-only PowerShell exporter for vCenter with PowerCLI and for Nutanix Prism Central through its REST API.

## How it is built
Python with the standard library only. The demo is a made-up engineering company with a private cloud in Madrid and Guadalajara: two vSphere production clusters, a Nutanix AHV cluster, a management cluster, 23 hosts, 458 VMs, 13 months of utilisation and seven demand items. The problems are placed on purpose. The Madrid production cluster crosses its N+1 limit in January once the approved projects are counted, and the reclaim list moves that date to March, enough to order the hosts in November. 15 tests, a runbook for the monthly meeting, and a GitHub Actions workflow that runs the tests and rebuilds the demo data and the screenshot.

## What I learned
From running private cloud infrastructure on vCenter and vSphere, VMware VCF with vSAN and NSX-T, Nutanix, OpenShift and HPE GreenLake, on Dell, HP and Supermicro servers with SAN, NAS and NetApp storage, and from formal capacity and availability management with metrics, trends and availability plans. Right-sizing and reservations in Azure taught me the same lesson on the cost side. The lesson that shaped the tool: the capacity meeting should end with dates and owners, not percentages. The runway is set against the purchase lead time, and the reclaim list only counts when it moves the date.

## Next steps
- Run it with the last 12 months of vCenter and Prism Central data, and check the N+1 limits and the vCPU policy with the platform team before the first meeting.
- Put the project portfolio into the demand file every month, and send each service owner their reclaim rows a week before the meeting.
- Keep each month's output, so the next review compares the forecast with what actually happened.""",
 es="""

## El problema
La capacidad es una fecha, no un porcentaje. Un clúster al 74% de su RAM parece sano en el panel. Pero si quitas el host que HA necesita de reserva, está al 85% de lo que queda. Crece medio punto al mes, y hay dos proyectos aprobados que llegan en enero y en marzo. Juntando las tres cosas, el clúster cruza su límite N+1 en enero. Pedir, recibir y añadir hosts nuevos al clúster lleva cuatro meses, así que la decisión había que tomarla en septiembre. Los datos están en sitios distintos: capacidad y uso en vCenter y Prism Central, proyectos en la cartera, máquinas apagadas y snapshots olvidados en el inventario, caídas en los registros de incidencias. La revisión mensual de capacidad es donde se juntan.

## Qué he hecho
- Margen tras caer un host: la CPU y la RAM que quedan si cae el host más grande, el ratio vCPU:pCPU frente a la política, la sobreasignación de vRAM y los hosts en mantenimiento.
- Autonomía: el último p95 más una tendencia lineal de 12 meses, sumando los proyectos aprobados en su mes de puesta en marcha y restando la lista de recuperación. El resultado es el mes en que cada clúster cruza su límite, el mes límite para pedir y los hosts a añadir.
- Recuperación: máquinas apagadas desde hace 30 o 90 días, máquinas ociosas, máquinas sobredimensionadas según su p95 con el tamaño recomendado, snapshots antiguos y máquinas sin responsable, con la RAM y el almacenamiento que devuelve cada una.
- Almacenamiento y disponibilidad: datastores por debajo del umbral de espacio libre, thin provisioning, caídas de clúster frente al objetivo de disponibilidad, fallos de host y reinicios de HA, y hosts sin soporte del fabricante.
- `report.html` con una tarjeta y una gráfica de autonomía por clúster, `capacity-review.md` con la tabla de decisiones para la reunión, y CSV de clústeres, previsión, recuperación, datastores y demanda.
- Un exportador de solo lectura en PowerShell para vCenter con PowerCLI y para Nutanix Prism Central con su API REST.

## Cómo está hecho
Python solo con la librería estándar. La demo es una empresa de ingeniería inventada con una nube privada en Madrid y Guadalajara: dos clústeres vSphere de producción, un clúster Nutanix AHV, un clúster de gestión, 23 hosts, 458 máquinas virtuales, 13 meses de uso y siete peticiones de demanda. Los problemas están puestos a propósito. El clúster de producción de Madrid cruza su límite N+1 en enero al contar los proyectos aprobados, y la lista de recuperación mueve esa fecha a marzo, lo justo para pedir los hosts en noviembre. 15 tests, un runbook para la reunión mensual y un workflow de GitHub Actions que ejecuta los tests y regenera los datos de la demo y la captura.

## Qué aprendí
De gestionar infraestructura de nube privada con vCenter y vSphere, VMware VCF con vSAN y NSX-T, Nutanix, OpenShift y HPE GreenLake, sobre servidores Dell, HP y Supermicro con almacenamiento SAN, NAS y NetApp, y de la gestión formal de capacidad y disponibilidad con métricas, tendencias y planes de disponibilidad. El ajuste de tamaños y las reservas en Azure me enseñaron lo mismo desde el lado del coste. La lección que da forma a la herramienta: la reunión de capacidad tiene que acabar con fechas y responsables, no con porcentajes. La autonomía se compara con el plazo de compra, y la lista de recuperación solo cuenta si mueve la fecha.

## Siguientes pasos
- Ejecutarlo con los últimos 12 meses de datos de vCenter y Prism Central, y revisar los límites N+1 y la política de vCPU con el equipo de plataforma antes de la primera reunión.
- Pasar cada mes la cartera de proyectos al fichero de demanda, y enviar a cada responsable de servicio sus filas de recuperación una semana antes de la reunión.
- Guardar la salida de cada mes, para que la siguiente revisión compare la previsión con lo que pasó de verdad."""),
dict(n="36", repo="36-major-incident-command-kit", date="2026-10-28", cat="tools",
 title_en="Users told us 40 minutes before monitoring did: a kit to run and review major incidents",
 title_es="Los usuarios nos avisaron 40 minutos antes que la monitorización: un kit para dirigir y revisar incidentes mayores",
 seo_title_en="Major incident review kit: MTTA, MTTR, PIR · Iñigo González",
 seo_title_es="Kit de incidentes graves: MTTA, MTTR y revisión · Iñigo González",
 dek_en="For every P1 and P2 of the quarter: the first alert against the first user report, time to acknowledge, mitigate and resolve against target, who ran it, the gaps in stakeholder updates, the change the night before, the review, the root cause and the overdue actions, with a timeline and a draft post-incident review per incident.",
 dek_es="Para cada P1 y P2 del trimestre: la primera alerta frente al primer aviso de los usuarios, el tiempo de respuesta, mitigación y resolución frente al objetivo, quién lo dirigió, los huecos en las comunicaciones, el cambio de la noche anterior, la revisión, la causa raíz y las acciones vencidas, con una línea de tiempo y un borrador de revisión post-incidente por incidente.",
 en="""

## The problem
The post-incident review is usually written a week later, from memory, by the person who was busiest on the bridge. By then the timeline is a guess, and the questions that would change something next time are not asked. The service desk had dozens of calls about logins before anyone in IT knew, and no alert fired until well after detection. An alert on the payments queue fired at ten past two and nobody acted until three. The trading desk went an hour and a half without an update and never got the resolution notice. The change the night before was the cause, and the ticket does not say so. The action that would have caught the login outage is a month overdue. The facts are in the ITSM tool, the monitoring consoles, the bridge chat and the sent folder; the review that matters joins them per incident and measures them against the policy the team signed up to.

## What I built
- Detection: the first alert on the service or CI against the first user report and the ticket, with blind spots (users first, no alert) and alerts nobody acted on.
- Response: time to acknowledge, mitigate and resolve against the targets of each priority, and whether an incident commander, a comms lead and a tech lead were recorded.
- Communications: a stakeholder update every N minutes as the policy says, the first one late, the gaps, and the missing resolution notice.
- Before and after: changes on the service in the 72 hours before the impact, the post-incident review within N business days, the root cause in the problem record, overdue actions, and incidents that came back on the same CI within 30 days.
- `report.html` with a timeline per incident as inline SVG, one draft post-incident review per major incident with the parts only people can write clearly marked, and CSVs for the incidents, MTTD/MTTA/MTTM/MTTR by month and priority, comms gaps, overdue actions and repeats.
- A `start` command that prints the role card, the first-fifteen-minutes checklist and the first stakeholder update for a new incident, and a read-only PowerShell exporter for ServiceNow and Jira Service Management.

## How it is built
Python with the standard library only. The demo is the IT operations team of a made-up bank over one quarter: 54 incidents, six of them major, on card payments, online banking, trader voice, the mobile API, the payments hub and market data, with alerts from five monitoring tools, changes, bridge timelines, stakeholder updates, problems and actions, and the problems placed on purpose. 15 tests, a runbook for the first fifteen minutes and the weekly review, and a GitHub Actions workflow that runs the tests and rebuilds the demo data and the screenshot.

## What I learned
From leading the technical response in major incidents and the post-mortems that followed, and from owning the incident, change and problem processes. One of them was the outage of a voice line used by a trading desk at a financial services firm: the fix was technical, but what the desk remembered was how often they heard from us. The lessons that shaped the tool are that detection starts at the first signal, not at the ticket; that an update with nothing new is still an update; that a change in the days before is a suspect until the review rules it out; and that a review without an owner and a date for each action is a meeting, not a review.

## Next steps
- Run it on last quarter's real exports and tune the targets, the update interval and the review days with the major incident managers.
- Read the alerts from the monitoring APIs and the updates from the communication plan instead of two CSVs.
- Write the draft review into the problem record, and bring the blind spots and overdue actions to the monthly service review.""",
 es="""

## El problema
La revisión post-incidente se suele escribir una semana después, de memoria, por la persona que más trabajo tuvo en el puente. Para entonces la línea de tiempo es una suposición, y las preguntas que cambiarían algo la próxima vez no se hacen. El service desk había recibido decenas de llamadas por el login antes de que nadie en IT lo supiera, y ninguna alerta saltó hasta mucho después de la detección. Una alerta de la cola de pagos saltó a las dos y diez y nadie actuó hasta las tres. La mesa de trading pasó hora y media sin una actualización y nunca recibió el aviso de resolución. El cambio de la noche anterior fue la causa, y el ticket no lo dice. La acción que habría detectado la caída del login lleva un mes vencida. Los datos están en la herramienta ITSM, las consolas de monitorización, el chat del puente y la bandeja de enviados; la revisión que importa los junta por incidente y los mide contra la política que el equipo se comprometió a cumplir.

## Qué he hecho
- Detección: la primera alerta sobre el servicio o el CI frente al primer aviso de los usuarios y el ticket, con los puntos ciegos (avisan los usuarios, sin alerta) y las alertas que nadie atendió.
- Respuesta: el tiempo hasta la asignación, la mitigación y la resolución frente a los objetivos de cada prioridad, y si constan un incident commander, un responsable de comunicaciones y un responsable técnico.
- Comunicaciones: una actualización a los interesados cada N minutos según la política, la primera tarde, los huecos y el aviso de resolución que falta.
- Antes y después: cambios en el servicio en las 72 horas previas al impacto, la revisión post-incidente en N días laborables, la causa raíz en el registro de problema, las acciones vencidas y los incidentes que vuelven en el mismo CI en 30 días.
- `report.html` con una línea de tiempo por incidente en SVG, un borrador de revisión post-incidente por cada incidente mayor con las partes que solo pueden escribir las personas bien marcadas, y CSV de incidentes, MTTD/MTTA/MTTM/MTTR por mes y prioridad, huecos de comunicación, acciones vencidas y repeticiones.
- Un comando `start` que imprime la tarjeta de roles, el checklist de los primeros quince minutos y la primera comunicación para un incidente nuevo, y un exportador de solo lectura en PowerShell para ServiceNow y Jira Service Management.

## Cómo está hecho
Python solo con la librería estándar. La demo es el equipo de operaciones IT de un banco inventado durante un trimestre: 54 incidentes, seis de ellos mayores, en pagos con tarjeta, banca online, voz de trading, la API móvil, el hub de pagos y datos de mercado, con alertas de cinco herramientas de monitorización, cambios, líneas de tiempo del puente, comunicaciones, problemas y acciones, y los problemas puestos a propósito. 15 tests, un runbook para los primeros quince minutos y la revisión semanal, y un workflow de GitHub Actions que ejecuta los tests y regenera los datos de la demo y la captura.

## Qué aprendí
De liderar la respuesta técnica en incidentes mayores y los post-mortems que vinieron después, y de ser responsable de los procesos de incidencias, cambios y problemas. Uno de ellos fue la caída de una línea de voz que usaba una mesa de trading en una empresa de servicios financieros: la solución fue técnica, pero lo que la mesa recordaba era cada cuánto tenía noticias nuestras. Las lecciones que dan forma a la herramienta son que la detección empieza con la primera señal, no con el ticket; que una actualización sin novedades sigue siendo una actualización; que un cambio en los días previos es sospechoso hasta que la revisión lo descarta; y que una revisión sin responsable y fecha para cada acción es una reunión, no una revisión.

## Siguientes pasos
- Ejecutarlo con las exportaciones reales del último trimestre y ajustar los objetivos, el intervalo de comunicaciones y los días para la revisión con los responsables de incidentes mayores.
- Leer las alertas de las APIs de monitorización y las comunicaciones del plan de comunicación en lugar de dos CSV.
- Escribir el borrador de revisión en el registro de problema, y llevar los puntos ciegos y las acciones vencidas a la revisión mensual de servicio."""),
dict(n="37", repo="37-iam-access-review", date="2026-10-29", cat="tools",
 title_en="He left three weeks ago and is still in Domain Admins: the monthly access review",
 title_es="Se fue hace tres semanas y sigue en Domain Admins: la revisión mensual de accesos",
 seo_title_en="IAM access review: joiners, movers, leavers · Iñigo González",
 seo_title_es="Revisión de accesos IAM: altas, cambios y bajas · Iñigo González",
 seo_desc="Monthly IAM review from HR, AD and Entra ID exports: leavers still enabled, movers keeping access, orphan accounts, standing admin roles and recertification.",
 dek_en="From the HR roster and the Active Directory, Entra ID, PAM and recertification exports: leavers still enabled, movers who kept their old access, accounts nobody owns, standing roles outside PIM, passwords the vault never rotated, service accounts whose owner left, and reviewers who approved everything in minutes, with a status per area and a pack the auditor can test.",
 dek_es="A partir de la plantilla de RR. HH. y de las exportaciones de Active Directory, Entra ID, la bóveda PAM y la recertificación: bajas todavía habilitadas, cambios de puesto que conservan el acceso anterior, cuentas sin dueño, roles permanentes fuera de PIM, contraseñas que la bóveda no ha rotado, cuentas de servicio cuyo responsable se fue y revisores que lo aprueban todo en minutos, con un estado por área y un informe que el auditor puede comprobar.",
 en="""

## The problem
Access reviews are usually a spreadsheet sent to managers once a quarter and a box ticked for the auditor. Meanwhile the things that would turn into an incident are in plain sight in the exports. A systems administrator left three weeks ago and his admin account is still enabled and in Domain Admins. A trader signed in four days after his last day. Someone moved from trading to finance in August and kept the trading platform, and the platform owner approved it in the campaign. A Global Administrator was assigned permanently, outside PIM. A service account password in the vault has not changed in 200 days, and the batch account belongs to someone who left and is still used interactively. One reviewer approved 140 items in three minutes, and three revokes were never actioned. HR knows who left and who moved, the directories know who can still sign in, the vault knows what was rotated and the campaign knows who said what; the review that matters joins them per person and per account, every month.

## What I built
- Leavers: accounts still enabled after the end date and its grace, sign-ins after leaving, and the groups, admin accounts and directory roles they still hold.
- Movers and joiners: access of the previous department kept beyond the grace, access before the start date, joiners without a manager.
- Accounts: enabled accounts with no HR record, duplicate employee IDs, accounts unused for 90 days and human passwords that never expire.
- Privileged access: standing Entra ID roles outside PIM, privileged users without MFA or unused, Tier 0 members beyond the approved list, vaulted passwords not rotated and admin accounts not vaulted; service accounts without an owner in employment or signing in interactively, and guests without a sponsor or inactive.
- Recertification: items not reviewed on time, revokes not actioned, rubber-stamping, and entitlements overdue for review by sensitivity tier.
- `report.html` with a status per area and an overall status, `access-review.md` as the pack for the monthly IAM service review with 13 controls written the way an auditor tests them, CSVs for leavers, movers, orphans, privileged access, service accounts and the campaign, and a read-only PowerShell exporter for Active Directory and Microsoft Graph.

## How it is built
Python with the standard library only. The demo is a made-up clearing house of 600 people reviewed for one month: Active Directory and Entra ID accounts, group memberships over a catalogue of entitlements by tier, Entra ID roles active and eligible, the PAM vault, the service account register and a recertification campaign of 446 items, with the problems placed on purpose. 18 tests, a runbook for the day of the review and the monthly service review, and a GitHub Actions workflow that runs the tests and rebuilds the demo data and the screenshot.

## What I learned
From administering Active Directory and Entra ID, with PIM and just-in-time access for the admin roles, managing privileged accounts in CyberArk and ManageEngine Password Manager Pro, owning the joiner process, and answering audits under ISO 27001. The lessons that shaped the tool are that a leaver's account is a finding even if nobody used it; that admin accounts must leave with their owner, which only works if they carry the owner's employee ID; that a move is the moment access goes wrong, not the next campaign; that standing should be the exception and eligible the rule; and that an approval in seconds is not a review, so the pack measures how the campaign was done, not only whether it was finished.

## Next steps
- Run it on last month's real exports and tune the grace periods, the thresholds, the PIM roles and the approved Tier 0 list with the IAM and infrastructure leads.
- Read the HR roster and the vault from their APIs instead of two CSVs, and compare each month with the previous one in the pack.
- Generate the next campaign from the catalogue, with the last sign-in and the department next to each item so reviewers see what they approve.""",
 es="""

## El problema
Las revisiones de accesos suelen ser una hoja de cálculo que se manda a los responsables una vez al trimestre y una casilla marcada para el auditor. Mientras tanto, lo que acabaría siendo un incidente está a la vista en las exportaciones. Un administrador de sistemas se fue hace tres semanas y su cuenta de administración sigue habilitada y en Domain Admins. Un trader inició sesión cuatro días después de su último día. Alguien pasó de trading a finanzas en agosto y conservó la plataforma de trading, y el responsable de la plataforma lo aprobó en la campaña. Un Global Administrator se asignó de forma permanente, fuera de PIM. La contraseña de una cuenta de servicio en la bóveda lleva 200 días sin cambiar, y la cuenta del batch es de alguien que se fue y se sigue usando de forma interactiva. Un revisor aprobó 140 elementos en tres minutos y tres revocaciones no se llegaron a ejecutar. RR. HH. sabe quién se fue y quién cambió de puesto, los directorios saben quién puede seguir entrando, la bóveda sabe qué se rotó y la campaña sabe quién dijo qué; la revisión que importa los junta por persona y por cuenta, todos los meses.

## Qué he hecho
- Bajas: cuentas todavía habilitadas pasada la fecha de baja y su margen, inicios de sesión después de irse, y los grupos, cuentas de administración y roles de directorio que conservan.
- Cambios de puesto y altas: acceso del departamento anterior mantenido más allá del margen, accesos antes de la fecha de incorporación y altas sin responsable.
- Cuentas: cuentas habilitadas sin registro en RR. HH., IDs de empleado duplicados, cuentas sin uso en 90 días y contraseñas de personas que nunca caducan.
- Accesos privilegiados: roles permanentes de Entra ID fuera de PIM, usuarios privilegiados sin MFA o sin uso, miembros de Tier 0 fuera de la lista aprobada, contraseñas en bóveda sin rotar y cuentas de administración fuera de la bóveda; cuentas de servicio sin un responsable en plantilla o con inicio de sesión interactivo, e invitados sin patrocinador o inactivos.
- Recertificación: elementos sin revisar a tiempo, revocaciones sin ejecutar, aprobaciones en bloque y derechos con la revisión vencida según su nivel de sensibilidad.
- `report.html` con un estado por área y un estado global, `access-review.md` como informe para la revisión mensual del servicio de IAM con 13 controles redactados como los prueba un auditor, CSV de bajas, cambios de puesto, cuentas huérfanas, accesos privilegiados, cuentas de servicio y la campaña, y un exportador de solo lectura en PowerShell para Active Directory y Microsoft Graph.

## Cómo está hecho
Python solo con la librería estándar. La demo es una cámara de compensación inventada de 600 personas revisada durante un mes: cuentas de Active Directory y Entra ID, pertenencias a grupos sobre un catálogo de derechos por nivel, roles de Entra ID activos y elegibles, la bóveda PAM, el registro de cuentas de servicio y una campaña de recertificación de 446 elementos, con los problemas puestos a propósito. 18 tests, un runbook para el día de la revisión y la revisión mensual del servicio, y un workflow de GitHub Actions que ejecuta los tests y regenera los datos de la demo y la captura.

## Qué aprendí
De administrar Active Directory y Entra ID, con PIM y acceso just-in-time para los roles de administración, gestionando cuentas privilegiadas en CyberArk y ManageEngine Password Manager Pro, siendo responsable del proceso de altas y respondiendo a auditorías bajo ISO 27001. Las lecciones que dan forma a la herramienta son que la cuenta de una baja es un hallazgo aunque nadie la haya usado; que las cuentas de administración tienen que irse con su dueño, y eso solo funciona si llevan su ID de empleado; que el cambio de puesto es el momento en que el acceso se tuerce, no la siguiente campaña; que lo permanente debe ser la excepción y lo elegible la norma; y que una aprobación en segundos no es una revisión, así que el informe mide cómo se hizo la campaña, no solo si se terminó.

## Siguientes pasos
- Ejecutarlo con las exportaciones reales del último mes y ajustar los márgenes, los umbrales, los roles de PIM y la lista aprobada de Tier 0 con los responsables de IAM e infraestructura.
- Leer la plantilla de RR. HH. y la bóveda desde sus APIs en lugar de dos CSV, y comparar cada mes con el anterior en el informe.
- Generar la siguiente campaña desde el catálogo, con el último inicio de sesión y el departamento junto a cada elemento para que los revisores vean lo que aprueban."""),
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
dict(n="38", repo="38-it-asset-lifecycle-planner", date="2026-10-30", cat="tools",
 title_en="Nine unregistered laptops and half the budget in one quarter: one inventory and a refresh plan for the office",
 title_es="Nueve portátiles sin registrar y medio presupuesto en un trimestre: inventario y plan de renovación de la oficina",
 seo_title_en="IT asset inventory and refresh forecast · Iñigo González",
 seo_title_es="Inventario de hardware y plan de renovación · Iñigo González",
 seo_desc="Monthly IT asset review from Device42, Intune, Jamf and purchases: one inventory by serial, leavers' devices, stock and a refresh forecast by quarter.",
 dek_en="From the Device42 export of the comms rooms, Intune and Jamf Pro, the vendor's purchases, the office register, HR and the stock: devices nobody registered, laptops not seen for weeks, switches past end of support, leavers who kept their laptop, stock below the minimum, and the replacements by quarter with their cost, ready for the budget.",
 dek_es="A partir de la exportación de Device42 de las salas de comunicaciones, Intune y Jamf Pro, las compras al fabricante, el registro de la oficina, RR. HH. y el almacén: equipos que nadie registró, portátiles que no se ven desde hace semanas, switches sin soporte del fabricante, bajas que se quedaron el portátil, almacén por debajo del mínimo y las renovaciones por trimestre con su coste, listas para el presupuesto.",
 en="""

## The problem
In many offices the inventory is split by who looks after it. The comms rooms are in Device42, the laptops and phones in Intune and Jamf, the monitors and docks in a spreadsheet, and the warranties in the vendor's portal. Each list looks complete on its own. Put together, the gaps show: laptops in Intune that nobody registered because they were bought outside the usual channel, a laptop that has not synced for months, a leaver's laptop still checking in weeks after the last day, access switches past end of support and the core switch's warranty ending in six weeks. And when the budget comes, the question "what do we have to buy next year" is answered from memory, until someone notices that the laptops of a big refresh and the trading floor desktops all fall due in the same quarter.

## What I built
- Coverage: one inventory joined by serial number from Device42, the purchases, the office register and MDM; devices in Intune or Jamf with no inventory record, devices not seen for 30 days, duplicate and mismatched serials, and items without owner or site.
- Comms rooms: devices past end of support or out of warranty, warranties ending in the next 90 days, devices without rack position or owner, and firmware not recorded.
- Lifecycle: one state for every item (in stock, deployed, in repair, to be retired, retired) and one replacement date from the refresh policy, with what is overdue and what is due in the next two quarters.
- People and stock: devices assigned to leavers and not returned after 14 days, more devices than the policy allows, people without a computer, and stock per site against the minimum and against next quarter's replacements.
- Forecast: replacements for the next four quarters by category and site, with units and cost, and the overdue backlog apart.
- `report.html` with a status per area and an overall verdict, `asset-review.md` as the pack for the monthly review with the forecast ready for the budget, CSVs for every area, and a read-only PowerShell exporter for Device42, Intune (Microsoft Graph) and Jamf Pro.

## How it is built
Python with the standard library only. The demo is a made-up broker with offices in Madrid, Paris and Amsterdam and two comms rooms: 51 devices in Device42, about 300 devices in Intune and Jamf, 740 purchase lines and 457 register lines, 198 people and the stock of the three sites, with the problems placed on purpose. 14 tests, a runbook for the monthly review, and a GitHub Actions workflow that runs the tests and rebuilds the demo data and the screenshot.

## What I learned
From running an office IT site, where I use Device42 for the inventory of the comms rooms (racks, network equipment and servers) and an operations console with PowerShell for inventory and asset control; from managing macOS, iOS, Android and Windows with Intune and Jamf Pro; from the relationship with Dell for hardware and renewals; and from preparing and tracking the annual IT budget in a multi-site company. The lessons that shaped the tool are that the serial number is the only key every system shares; that a device MDM sees and nobody bought is still yours, with no warranty and no replacement date; that a laptop not seen for weeks is an answer waiting for a question; that for the comms rooms end of support beats age; and that a budget built from purchase dates shows the waves before they arrive.

## Next steps
- Run it on the real exports of one site and tune the refresh policy, the unit costs and the device policy with the site and finance leads.
- Read purchases and warranties from the vendor's API by service tag instead of a CSV.
- Write the end-user devices back to Device42 by serial, so that it becomes the one inventory for the whole office and this report checks it instead of building it.""",
 es="""

## El problema
En muchas oficinas el inventario está repartido según quién lo cuida. Las salas de comunicaciones están en Device42, los portátiles y los móviles en Intune y Jamf, los monitores y las bases en una hoja de cálculo y las garantías en el portal del fabricante. Cada lista parece completa por separado. Juntas, aparecen los huecos: portátiles en Intune que nadie registró porque se compraron fuera del canal habitual, un portátil que no sincroniza desde hace meses, el portátil de una baja que sigue conectándose semanas después de su último día, switches de acceso sin soporte del fabricante y la garantía del switch de núcleo a seis semanas de vencer. Y cuando llega el presupuesto, la pregunta «qué tenemos que comprar el año que viene» se responde de memoria, hasta que alguien se da cuenta de que los portátiles de una renovación grande y los equipos de sobremesa de la sala de trading vencen todos en el mismo trimestre.

## Qué he hecho
- Cobertura: un inventario único cruzado por número de serie entre Device42, las compras, el registro de la oficina y el MDM; equipos en Intune o Jamf sin registro en el inventario, equipos que no se ven desde hace 30 días, números de serie duplicados o que no cuadran y equipos sin responsable o sin sede.
- Salas de comunicaciones: equipos sin soporte del fabricante o fuera de garantía, garantías que vencen en los próximos 90 días, equipos sin posición en el rack o sin responsable, y firmware sin registrar.
- Ciclo de vida: un estado para cada equipo (en almacén, desplegado, en reparación, para retirar, retirado) y una fecha de renovación según la política, con lo que está vencido y lo que vence en los dos próximos trimestres.
- Personas y almacén: equipos asignados a bajas y no devueltos a los 14 días, más equipos de los que permite la política, personas sin ordenador, y el almacén de cada sede frente al mínimo y frente a las renovaciones del próximo trimestre.
- Previsión: las renovaciones de los cuatro próximos trimestres por categoría y sede, con unidades y coste, y lo atrasado aparte.
- `report.html` con un estado por área y un veredicto global, `asset-review.md` como informe para la revisión mensual con la previsión lista para el presupuesto, CSV de cada área y un exportador de solo lectura en PowerShell para Device42, Intune (Microsoft Graph) y Jamf Pro.

## Cómo está hecho
Python solo con la librería estándar. La demo es un bróker inventado con oficinas en Madrid, París y Ámsterdam y dos salas de comunicaciones: 51 equipos en Device42, unos 300 equipos en Intune y Jamf, 740 líneas de compra y 457 del registro, 198 personas y el almacén de las tres sedes, con los problemas puestos a propósito. 14 tests, un runbook para la revisión mensual y un workflow de GitHub Actions que ejecuta los tests y regenera los datos de la demo y la captura.

## Qué aprendí
De llevar la IT de una sede, donde uso Device42 para el inventario de las salas de comunicaciones (racks, equipos de red y servidores) y una consola de operaciones con PowerShell para el inventario y el control de activos; de gestionar macOS, iOS, Android y Windows con Intune y Jamf Pro; de la relación con Dell para el hardware y las renovaciones; y de preparar y seguir el presupuesto anual de IT en una empresa con varias sedes. Las lecciones que dan forma a la herramienta son que el número de serie es la única clave que comparten todos los sistemas; que un equipo que el MDM ve y nadie compró sigue siendo tuyo, sin garantía y sin fecha de renovación; que un portátil que no se ve desde hace semanas es una respuesta esperando una pregunta; que en las salas de comunicaciones el fin de soporte manda sobre la antigüedad; y que un presupuesto hecho con las fechas de compra enseña las olas antes de que lleguen.

## Siguientes pasos
- Ejecutarlo con las exportaciones reales de una sede y ajustar la política de renovación, los costes unitarios y la política de equipos por persona con los responsables de la sede y de finanzas.
- Leer las compras y las garantías desde la API del fabricante por número de serie en lugar de un CSV.
- Volcar los equipos de usuario en Device42 por número de serie, para que sea el inventario único de toda la oficina y este informe lo compruebe en lugar de construirlo."""),
dict(n="39", repo="39-vulnerability-remediation-sla", date="2026-10-31", cat="tools",
 title_en="A VPN with a known exploit and thirty servers waiting for a reboot: vulnerability remediation against the SLA",
 title_es="Una VPN con un exploit conocido y treinta servidores sin reiniciar: la corrección de vulnerabilidades frente al SLA",
 seo_title_en="Vulnerability remediation SLA review · Iñigo González",
 seo_title_es="Revisión del SLA de vulnerabilidades · Iñigo González",
 seo_desc="Weekly and monthly vulnerability SLA review from Qualys, CISA KEV, EPSS, the asset register and Tanium or Intune: what is late, why it is stuck, what to fix.",
 dek_en="From the Qualys detections, the CISA KEV catalog, EPSS, the asset register, the patch status and the exceptions register: every open vulnerability against its deadline, known exploited ones past the CISA date, internet-facing hosts, patches waiting for a reboot, detections back after an old image, servers that cannot be patched, expired exceptions, the teams behind, and the fixes that close most risk.",
 dek_es="A partir de las detecciones de Qualys, el catálogo KEV de CISA, EPSS, el inventario de activos, el estado de parcheo y el registro de excepciones: cada vulnerabilidad abierta frente a su plazo, las explotadas conocidas pasada la fecha de CISA, los equipos expuestos a internet, parches que esperan un reinicio, detecciones que vuelven tras una imagen antigua, servidores que ya no se pueden parchear, excepciones caducadas, los equipos que van con retraso y los arreglos que cierran más riesgo.",
 en="""

## The problem
The scanner says how many vulnerabilities there are; it does not say whether we are keeping the promise we made, the remediation deadlines by severity. Those deadlines are usually tracked in a spreadsheet updated by hand, and the numbers hide the reasons: a VPN appliance back from an RMA swap on old firmware with a vulnerability that has been exploited for two years; servers with the patch installed a week ago that are still vulnerable because nobody agreed the reboot; trading desktops vulnerable again after being rebuilt from an old golden image; servers on an operating system that can no longer be patched, covered by an exception that expired a month ago; one team closing half of its fixes on time while the rest are above 90%; and a browser update, held back by a pinned version, that is 40% of all the critical and high findings on the laptops.

## What I built
- SLA: every open Qualys detection with its deadline (15, 30, 90 or 180 days by severity, 7 days for CISA KEV, a high EPSS score or a critical on an internet-facing host) and its status: on time, due in 7 days, overdue, or overdue more than twice the SLA.
- KEV and exposure: known exploited vulnerabilities still open past the CISA due date, internet-facing hosts with critical or high findings, and overdue detections with a high EPSS.
- Why fixes do not close: patch installed and reboot pending, detections re-opened after a fix, and operating systems past end of support.
- Coverage and exceptions: hosts that Qualys does not scan or has not scanned for two weeks, hosts nobody owns, patch agents failing, and exceptions expired, without a compensating control or too broad.
- Top fixes and trend: the ten updates or packages that remove most risk, the share closed inside the SLA in each of the last three months, the mean time to remediate by severity, and the owner teams behind.
- `report.html` with a status per area and an overall verdict, `sla-review.md` with the weekly critical list and the monthly pack, CSVs for every area, and a read-only PowerShell exporter for the Qualys API, the CISA KEV feed, the EPSS API and Intune.

## How it is built
Python with the standard library only. The demo is a made-up broker with about 400 servers and 1,200 Windows 11 endpoints owned by six teams: almost 7,000 Qualys detections (open and recently fixed), the asset register, the patch status from Tanium and Intune, seven exceptions, EPSS scores and a small KEV snapshot, with the problems placed on purpose. 15 tests, a runbook for the weekly and monthly reviews and for raising or renewing an exception, and a GitHub Actions workflow that runs the tests and rebuilds the demo data and the screenshot.

## What I learned
From running an office IT site, where I use Qualys and Tanium for vulnerability and patch management, Microsoft Defender (which I have used since a previous role), and Intune and MECM in co-management, including the Windows 11 migration of an office with a trading floor; from cybersecurity risk management, treatment plans and remediation tracking with security metrics and KPIs; from applying ISO 27001, NIS2 and NIST CSF, and from audits; and from the CAB as process owner for changes. The lessons that shaped the tool are that the clock starts when the scanner finds the vulnerability, so coverage is part of the SLA; that a known exploit beats a severity score; that installed is not fixed until the host reboots; that many hosts re-opened in the same week point to an image, not to bad luck; that an exception is a time-boxed decision with a control, not a way to make the report green; and that one well deployed update can close half of the list.

## Next steps
- Read Qualys and Tanium through their APIs on a schedule, so the weekly critical list is ready on Monday morning without exports.
- Open one ticket per owner team with its overdue detections and the fixes that close them, closed when the rescan confirms it.
- Compare each month with the previous one: new, closed and still overdue, and the share inside the SLA by team.""",
 es="""

## El problema
El escáner dice cuántas vulnerabilidades hay; no dice si estamos cumpliendo lo que prometimos, los plazos de corrección por severidad. Esos plazos se suelen seguir en una hoja de cálculo actualizada a mano, y las cifras esconden los motivos: un equipo de VPN que vuelve de un cambio por garantía con un firmware antiguo y una vulnerabilidad explotada desde hace dos años; servidores con el parche instalado hace una semana que siguen siendo vulnerables porque nadie acordó el reinicio; equipos de la sala de trading vulnerables otra vez tras reinstalarse desde una imagen maestra antigua; servidores con un sistema operativo que ya no se puede parchear, cubiertos por una excepción que caducó hace un mes; un equipo que cierra la mitad de sus correcciones a tiempo mientras el resto supera el 90 %; y una actualización del navegador, retenida por una versión fijada, que supone el 40 % de todas las vulnerabilidades críticas y altas de los portátiles.

## Qué he hecho
- SLA: cada detección abierta de Qualys con su plazo (15, 30, 90 o 180 días según la severidad; 7 días si está en el catálogo KEV de CISA, tiene un EPSS alto o es crítica en un equipo expuesto a internet) y su estado: en plazo, vence en 7 días, vencida o vencida más del doble del plazo.
- KEV y exposición: vulnerabilidades explotadas conocidas abiertas después de la fecha límite de CISA, equipos expuestos a internet con vulnerabilidades críticas o altas, y detecciones vencidas con un EPSS alto.
- Por qué no se cierran: parche instalado con el reinicio pendiente, detecciones que vuelven a abrirse tras corregirse y sistemas operativos sin soporte del fabricante.
- Cobertura y excepciones: equipos que Qualys no analiza o no analiza desde hace dos semanas, equipos sin responsable, agentes de parcheo que fallan, y excepciones caducadas, sin control compensatorio o demasiado amplias.
- Arreglos y tendencia: las diez actualizaciones o paquetes que más riesgo eliminan, el porcentaje cerrado dentro del plazo en cada uno de los tres últimos meses, el tiempo medio de corrección por severidad y los equipos responsables que van con retraso.
- `report.html` con un estado por área y un veredicto global, `sla-review.md` con la lista semanal de críticas y el informe mensual, CSV de cada área y un exportador de solo lectura en PowerShell para la API de Qualys, el catálogo KEV de CISA, la API de EPSS e Intune.

## Cómo está hecho
Python solo con la librería estándar. La demo es un bróker inventado con unos 400 servidores y 1.200 equipos con Windows 11 repartidos entre seis equipos responsables: casi 7.000 detecciones de Qualys (abiertas y corregidas recientemente), el inventario de activos, el estado de parcheo de Tanium e Intune, siete excepciones, puntuaciones EPSS y una pequeña muestra del catálogo KEV, con los problemas puestos a propósito. 15 tests, un runbook para las revisiones semanal y mensual y para pedir o renovar una excepción, y un workflow de GitHub Actions que ejecuta los tests y regenera los datos de la demo y la captura.

## Qué aprendí
De llevar la IT de una sede, donde uso Qualys y Tanium para la gestión de vulnerabilidades y parches, Microsoft Defender (que uso desde un puesto anterior) e Intune y MECM en cogestión, incluida la migración a Windows 11 de una oficina con sala de trading; de la gestión de riesgos de ciberseguridad, los planes de tratamiento y el seguimiento de la corrección con métricas e indicadores de seguridad; de aplicar ISO 27001, NIS2 y NIST CSF, y de las auditorías; y del CAB como responsable del proceso de cambios. Las lecciones que dan forma a la herramienta son que el reloj empieza cuando el escáner encuentra la vulnerabilidad, así que la cobertura forma parte del SLA; que un exploit conocido manda sobre la puntuación de severidad; que instalado no es corregido hasta que el equipo se reinicia; que muchos equipos que vuelven a abrirse la misma semana apuntan a una imagen, no a la mala suerte; que una excepción es una decisión con fecha de caducidad y un control, no una forma de poner el informe en verde; y que una sola actualización bien desplegada puede cerrar la mitad de la lista.

## Siguientes pasos
- Leer Qualys y Tanium desde sus API de forma programada, para que la lista semanal de críticas esté lista el lunes por la mañana sin exportaciones.
- Abrir un ticket por equipo responsable con sus detecciones vencidas y los arreglos que las cierran, y cerrarlo cuando el nuevo análisis lo confirme.
- Comparar cada mes con el anterior: nuevas, cerradas y aún vencidas, y el porcentaje dentro del plazo por equipo."""),

dict(n="40", repo="40-change-calendar-risk-review", date="2026-11-02", updated="2026-11-11", cat="tools",
 title_en="Two changes on the same night and a patch inside the month-end freeze: the change calendar before the CAB",
 title_es="Dos cambios la misma noche y un parche en pleno cierre de mes: el calendario de cambios antes del CAB",
 seo_title_en="Change calendar and CAB risk review · Iñigo González",
 seo_title_es="Calendario de cambios y revisión del CAB · Iñigo González",
 seo_desc="Weekly CAB pack from ServiceNow changes, the service map, freezes and incidents: what is not ready, what collides, and how last month's changes went.",
 dek_en="From the change requests, the business service map, the freeze register, the incidents and the approvals: the next two weeks by day and service, the changes not ready for the CAB, the ones that collide on the same night or through the dependencies, the ones inside a freeze, standard changes used for risky work, rising emergencies, and last month's success rate, incidents after changes, unauthorised work and overdue reviews.",
 dek_es="A partir de las peticiones de cambio, el mapa de servicios, el registro de congelaciones, los incidentes y las aprobaciones: las dos próximas semanas por día y servicio, los cambios que no están listos para el CAB, los que coinciden la misma noche o a través de las dependencias, los que caen dentro de una congelación, cambios estándar usados para trabajos con riesgo, emergencias en aumento, y la tasa de éxito del mes pasado, los incidentes tras un cambio, los trabajos sin autorizar y las revisiones pendientes.",
 en="""

## The problem
The change calendar in the ITSM tool is a list, and the CAB approves each change on its own merits. What the list does not show is how the changes relate to each other and to the rest of the month: the data centre firewalls and the core switches upgraded the same night by two different teams, both in the path of the trading platform; a database patch on the trading platform booked inside the month-end close freeze; a high-risk change raised two days before its window with no backout plan; a firmware upgrade on the storage of critical services booked as a standard change, so it never reaches the CAB; one team raising more emergencies every month for the same reasons; and a change closed as successful two hours before a P1 at the market open, with no post-implementation review booked. The other half of the job is the review afterwards, which links with the major incident kit I published a few days ago: the incident that follows a change is where the change review should start.

## What I built
- Readiness for the CAB: changes without a backout, test or implementation plan, with the risk not assessed or below what the impact and the tier of the service suggest, raised inside the lead time, not approved when they start before the CAB, without an owner, or outside the maintenance window of their tier.
- Collisions: overlapping changes on the same CI or service, changes that affect the same critical services through the dependencies, too many changes for one team on one night, and changes inside a freeze or blackout window without an approved exception.
- Emergency and standard changes: the emergency share by month and its reasons, standard changes used for risky work, and emergency changes never approved afterwards.
- Outcomes and teams: last month's success rate and the trend, unsuccessful changes, incidents linked to a change or opened on the same service within hours of one, overruns, unauthorised work, overdue post-implementation reviews, and the teams with a low success rate or rising emergencies.
- `report.html` with a two-week calendar by day and service where collisions, freezes and gaps stand out, a status per area and an overall verdict; `cab-pack.md` with the CAB agenda and the monthly review; CSVs for every area; and a read-only PowerShell exporter for the ServiceNow Table API (changes, incidents, approvals and the service map).

## How it is built
Python with the standard library only. The demo is a made-up bank with a trading floor, reviewed on a Monday morning before the CAB: 16 business services in three tiers with their dependencies, 263 change requests from nine teams (three months of history and the next two weeks), the approvals, the incidents and a freeze register with the month-end close and an index rebalance, with the problems placed on purpose. The impact of each change is worked out through the dependency map, so a change on the core network collides with anything on the services that depend on it. 15 tests, a runbook for the weekly CAB and the monthly change review, and a GitHub Actions workflow that runs the tests and rebuilds the demo data and the screenshot.

## What I learned
From being process owner for incidents, changes and problems and taking part in CABs and in go-live and service acceptance reviews; from release management, with its planning, testing, rollback and validation after the release; from writing procedures and runbooks for these processes and training others to use them; from leading the technical response in major incidents and the post-mortems afterwards; and from ServiceNow, EasyVista and HaloITSM, Jira and Confluence. The lessons that shaped the tool are that two changes on the same path the same night mean two backout plans for one symptom; that the impact of a change runs through the dependencies, not through the name of the service in the form; that lead time is the time other people have to look; that a standard change is pre-approved because it is boring, and a firmware upgrade on critical storage is not; that repeated emergencies are a problem record waiting to be opened; and that a change followed by a P1 is not a success, however it was closed.

## Next steps
- Read the change calendar through the API on a schedule, so the pack is ready on Monday morning without exports.
- Read the freezes from the blackout schedules of the ITSM tool instead of a CSV.
- Compare each week with the previous one: changes moved, collisions resolved, reviews closed.""",
 es="""

## El problema
El calendario de cambios de la herramienta de ITSM es una lista, y el CAB aprueba cada cambio por separado. Lo que la lista no enseña es cómo se relacionan los cambios entre sí y con el resto del mes: los cortafuegos del centro de datos y los switches del núcleo actualizados la misma noche por dos equipos distintos, ambos en el camino de la plataforma de trading; un parche de base de datos de la plataforma de trading programado dentro de la congelación del cierre de mes; un cambio de riesgo alto dado de alta dos días antes de su ventana y sin plan de marcha atrás; una actualización de firmware del almacenamiento de servicios críticos registrada como cambio estándar, así que nunca llega al CAB; un equipo que cada mes abre más emergencias por los mismos motivos; y un cambio cerrado con éxito dos horas antes de un P1 en la apertura del mercado, sin revisión posterior programada. La otra mitad del trabajo es la revisión de después, que enlaza con el kit de incidentes mayores que publiqué hace unos días: el incidente que sigue a un cambio es donde debería empezar la revisión del cambio.

## Qué he hecho
- Preparación para el CAB: cambios sin plan de marcha atrás, de pruebas o de implementación, con el riesgo sin evaluar o por debajo de lo que indican el impacto y el nivel del servicio, dados de alta dentro del plazo mínimo, sin aprobar cuando empiezan antes del CAB, sin responsable o fuera de la ventana de mantenimiento de su nivel.
- Coincidencias: cambios que se solapan en el mismo elemento de configuración o servicio, cambios que afectan a los mismos servicios críticos a través de las dependencias, demasiados cambios de un equipo en una noche y cambios dentro de una congelación o un periodo de bloqueo sin una excepción aprobada.
- Cambios de emergencia y estándar: el porcentaje de emergencias por mes y sus motivos, cambios estándar usados para trabajos con riesgo y emergencias que nunca se aprobaron después.
- Resultados y equipos: la tasa de éxito del mes pasado y su evolución, cambios fallidos, incidentes vinculados a un cambio o abiertos en el mismo servicio pocas horas después, cambios que se pasaron de su ventana, trabajos sin autorizar, revisiones posteriores pendientes, y los equipos con poca tasa de éxito o con emergencias en aumento.
- `report.html` con un calendario de dos semanas por día y servicio donde destacan las coincidencias, las congelaciones y los huecos, un estado por área y un veredicto global; `cab-pack.md` con el orden del día del CAB y la revisión mensual; CSV de cada área; y un exportador de solo lectura en PowerShell para la Table API de ServiceNow (cambios, incidentes, aprobaciones y el mapa de servicios).

## Cómo está hecho
Python solo con la librería estándar. La demo es un banco inventado con sala de trading, revisado un lunes por la mañana antes del CAB: 16 servicios de negocio en tres niveles con sus dependencias, 263 peticiones de cambio de nueve equipos (tres meses de histórico y las dos próximas semanas), las aprobaciones, los incidentes y un registro de congelaciones con el cierre de mes y un rebalanceo de índices, con los problemas puestos a propósito. El impacto de cada cambio se calcula a través del mapa de dependencias, así que un cambio en la red troncal coincide con cualquier otro en los servicios que dependen de ella. 15 tests, un runbook para el CAB semanal y la revisión mensual de cambios, y un workflow de GitHub Actions que ejecuta los tests y regenera los datos de la demo y la captura.

## Qué aprendí
De ser responsable de los procesos de incidentes, cambios y problemas y de participar en CAB y en revisiones de puesta en producción y aceptación del servicio; de la gestión de versiones, con su planificación, pruebas, marcha atrás y validación después de cada versión; de escribir procedimientos y runbooks de estos procesos y formar a otros para usarlos; de dirigir la respuesta técnica en incidentes mayores y los análisis posteriores; y de ServiceNow, EasyVista y HaloITSM, Jira y Confluence. Las lecciones que dan forma a la herramienta son que dos cambios en el mismo camino la misma noche suponen dos planes de marcha atrás para un solo síntoma; que el impacto de un cambio va por las dependencias, no por el nombre del servicio que pone el formulario; que el plazo mínimo es el tiempo que tienen otros para revisarlo; que un cambio estándar está preaprobado porque es rutinario, y una actualización de firmware del almacenamiento crítico no lo es; que las emergencias repetidas son un problema esperando a que alguien lo registre; y que un cambio seguido de un P1 no es un éxito, se cierre como se cierre.

## Siguientes pasos
- Leer el calendario de cambios desde la API de forma programada, para que el informe del CAB esté listo el lunes por la mañana sin exportaciones.
- Leer las congelaciones desde los calendarios de bloqueo de la herramienta de ITSM en lugar de un CSV.
- Comparar cada semana con la anterior: cambios movidos, coincidencias resueltas y revisiones cerradas."""),

dict(n="41", repo="41-windows-update-ring-tracker", date="2026-11-02", cat="tools",
 title_en="A paused ring nobody remembered and a pilot of IT staff: the Windows update rollout, ring by ring",
 title_es="Un anillo pausado y olvidado y un piloto solo de informáticos: Windows Update, anillo a anillo",
 seo_title_en="Windows update rings: gates and go/no-go · Iñigo González",
 seo_title_es="Anillos de Windows Update y go/no-go · Iñigo González",
 seo_desc="Patch Tuesday through the Intune update rings: each ring against its deadline, the go/no-go gates, devices behind and why, failures by model and the trend.",
 dek_en="From the Intune devices and update rings, the Configuration Manager deployments of co-managed devices, the Windows Update for Business reports and Windows release health: each ring against its deferral and deadline, the gate before the next promotion, devices behind and why, failure codes by model, whether the pilot looks like the rest of the fleet, and the share on the build at day 7, 14 and 21 for the last three months.",
 dek_es="A partir de los dispositivos y los anillos de actualización de Intune, los despliegues de Configuration Manager de los equipos en cogestión, los informes de Windows Update for Business y el estado de versiones de Windows: cada anillo frente a su aplazamiento y su fecha límite, la puerta antes de la siguiente promoción, los equipos que van con retraso y por qué, los códigos de error por modelo, si el piloto se parece al resto del parque y el porcentaje con la compilación al día 7, 14 y 21 de los tres últimos meses.",
 en="""

## The problem
Update rings are timers. The broad ring is offered the update ten days after Patch Tuesday whether the pilot went well or not, and the report that counts installs does not say whether the rollout is under control. In a typical month the broad ring starts with the pilot still at 77%; the late ring for the trading floor was paused after a bad update and forgotten, so five weeks later it is two months behind and the pause expires with nobody deciding what happens next; sixty trading desktops sit in the broad ring and lose their headset audio at the market open; one laptop model fails the update with the same error code on a third of its devices; ninety devices have been waiting for a restart since before the deadline; a whole office stops checking in on the same day because of the VPN; the pilot is nine IT engineers out of ten; and the share of devices on the build two weeks after Patch Tuesday falls three months in a row. This is not the co-management tracker I published a while ago, which follows the state of each workload, nor the vulnerability SLA review of a few days ago: it follows one monthly update through the rings, and it pairs with the change calendar I published today, because a ring promotion is a change and should get a decision like any other.

## What I built
- Rings and gates: each ring against its offer date, deadline and grace; the gate between rings (the previous ring's share on the build, its failure rate, the days since it was offered, open P1 or P2 incidents on the update, known issues that block the next ring); rings promoted without a met gate; the go/no-go for the next promotion; paused rings; and policies that drift from the ring standard.
- Devices behind: past the deadline and grace without the update, with a restart pending, not checked in (by site), in no ring or in two, on a Windows 11 version close to its end of servicing, or under a feature update safeguard hold.
- Failures and composition: error codes by model, devices failing month after month, incidents tagged to the update, trading desktops outside the late ring, a pilot that misses the departments, models and sites of the broad ring, and rings off their target size.
- Trend: the share on each month's update by day 7, 14 and 21 after Patch Tuesday, the median days to install by ring, and the devices behind every month.
- `report.html` with a timeline of the month showing each ring's offer, deadline, grace, pause and gates; `rollout-pack.md` for the monthly patch meeting or the CAB, with the go/no-go and a decision line; CSVs for every area; and a read-only PowerShell exporter for Microsoft Graph, the Windows Update for Business reports in Log Analytics and Configuration Manager.

## How it is built
Python with the standard library only. A device is on the build when the revision in its OS version is the month's Patch Tuesday revision or later; its ring comes from the groups or collections its policies are assigned to, with co-managed devices following the Configuration Manager deployment when the Windows Update workload has not moved to Intune; and each device is judged against its own deadline and grace, so a device that is still inside its window is not counted as behind. The demo is a made-up firm with a trading floor and 1,500 Windows 11 devices in four European cities, reviewed twenty days after the October Patch Tuesday, with the real builds, KB numbers, end of servicing dates and known issues from Windows release health and the problems placed on purpose. 13 tests, a runbook for the monthly cycle and the patch meeting, and a GitHub Actions workflow that runs the tests and rebuilds the demo data and the screenshot.

## What I learned
From leading the Windows 11 migration of an office with a trading floor; from running Intune and MECM in co-management, with application packaging in SCCM, PDQ and MDT, Endpoint Privilege Management, BitLocker and Microsoft Defender; from years of automation with PowerShell and Microsoft Graph; and from release management, with its planning, testing, rollback and validation after each release, and the CAB as change process owner, supporting about 2,500 users across European offices. The lessons behind the tool are that a deferral says when a ring can get the update and only a gate says whether it should; that a pause is a clock that runs out on its own; that the late ring only protects the devices that are actually in it; that a pilot of IT staff tests IT's applications; that a whole site going quiet is the network, not the users; that one error code on one model is a baseline to fix once, not devices to repair one by one; that an installed update waiting for a restart protects nothing; and that the real measure is the share on the build at day 14 and 21, month after month.

## Next steps
- Run the export and the review on a schedule after Patch Tuesday and before each promotion, and post the gate to the patch channel.
- Read the builds and known issues from the Windows Updates API in Microsoft Graph instead of copying them.
- Add driver and firmware updates by model as a category of their own.""",
 es="""

## El problema
Los anillos de actualización son temporizadores. El anillo general recibe la actualización diez días después del Patch Tuesday haya ido bien el piloto o no, y el informe que cuenta instalaciones no dice si el despliegue está bajo control. En un mes normal el anillo general arranca con el piloto todavía al 77%; el anillo tardío de la sala de trading se pausó tras una actualización problemática y nadie se acordó de él, así que cinco semanas después lleva dos meses de retraso y la pausa caduca sin que nadie haya decidido qué pasa después; sesenta puestos de trading están en el anillo general y se quedan sin audio en los cascos a la apertura del mercado; un modelo de portátil falla la actualización con el mismo código de error en un tercio de sus equipos; noventa equipos llevan esperando un reinicio desde antes de la fecha límite; una oficina entera deja de sincronizar el mismo día por la VPN; el piloto son nueve informáticos de cada diez; y el porcentaje de equipos con la compilación al día dos semanas después del Patch Tuesday baja tres meses seguidos. No es el seguimiento de cogestión que publiqué hace tiempo, que sigue el estado de cada carga de trabajo, ni la revisión del SLA de vulnerabilidades de hace unos días: sigue una actualización mensual a través de los anillos, y encaja con el calendario de cambios que he publicado hoy, porque promocionar un anillo es un cambio y merece una decisión como cualquier otro.

## Qué he hecho
- Anillos y puertas: cada anillo frente a su fecha de oferta, su fecha límite y su periodo de gracia; la puerta entre anillos (el porcentaje del anillo anterior con la compilación, su tasa de fallos, los días desde que se le ofreció, incidentes P1 o P2 abiertos por la actualización y problemas conocidos que bloquean el siguiente anillo); anillos promocionados sin cumplir la puerta; el go/no-go de la siguiente promoción; anillos en pausa; y directivas que se apartan del estándar del anillo.
- Equipos con retraso: sin la actualización pasada la fecha límite y la gracia, con un reinicio pendiente, sin sincronizar (por sede), sin anillo o en dos, en una versión de Windows 11 cerca del fin de servicio, o retenidos por una safeguard hold de la actualización de características.
- Fallos y composición: códigos de error por modelo, equipos que fallan mes tras mes, incidentes asociados a la actualización, puestos de trading fuera del anillo tardío, un piloto al que le faltan los departamentos, modelos y sedes del anillo general, y anillos que no tienen el tamaño previsto.
- Tendencia: el porcentaje con la actualización de cada mes al día 7, 14 y 21 del Patch Tuesday, la mediana de días hasta instalar por anillo y los equipos que van con retraso todos los meses.
- `report.html` con una línea temporal del mes que muestra la oferta, la fecha límite, la gracia, la pausa y las puertas de cada anillo; `rollout-pack.md` para la reunión mensual de parches o el CAB, con el go/no-go y una línea para la decisión; CSV de cada área; y un exportador de solo lectura en PowerShell para Microsoft Graph, los informes de Windows Update for Business en Log Analytics y Configuration Manager.

## Cómo está hecho
Python solo con la librería estándar. Un equipo tiene la compilación al día cuando la revisión de su versión del sistema es la del Patch Tuesday del mes o posterior; su anillo sale de los grupos o colecciones a los que están asignadas sus directivas, y los equipos en cogestión siguen el despliegue de Configuration Manager cuando la carga de trabajo de Windows Update no ha pasado a Intune; y cada equipo se mide con su propia fecha límite y su gracia, así que uno que aún está dentro de su plazo no cuenta como retrasado. La demo es una empresa inventada con sala de trading y 1.500 equipos con Windows 11 en cuatro ciudades europeas, revisada veinte días después del Patch Tuesday de octubre, con las compilaciones, los KB, las fechas de fin de servicio y los problemas conocidos reales del estado de versiones de Windows, y los problemas puestos a propósito. 13 tests, un runbook para el ciclo mensual y la reunión de parches, y un workflow de GitHub Actions que ejecuta los tests y regenera los datos de la demo y la captura.

## Qué aprendí
De dirigir la migración a Windows 11 de una oficina con sala de trading; de gestionar Intune y MECM en cogestión, con empaquetado de aplicaciones en SCCM, PDQ y MDT, Endpoint Privilege Management, BitLocker y Microsoft Defender; de años automatizando con PowerShell y Microsoft Graph; y de la gestión de versiones, con su planificación, pruebas, marcha atrás y validación después de cada versión, y del CAB como responsable del proceso de cambios, dando soporte a unos 2.500 usuarios en oficinas europeas. Las lecciones que hay detrás de la herramienta son que el aplazamiento dice cuándo puede recibir un anillo la actualización y solo una puerta dice si debe; que una pausa es un reloj que se acaba solo; que el anillo tardío solo protege a los equipos que de verdad están en él; que un piloto de informáticos prueba las aplicaciones de informática; que una sede entera sin sincronizar es la red, no los usuarios; que un código de error en un modelo es una configuración base que se arregla una vez, no equipos que se reparan uno a uno; que una actualización instalada que espera un reinicio no protege nada; y que la medida de verdad es el porcentaje con la compilación al día 14 y 21, mes tras mes.

## Siguientes pasos
- Ejecutar la exportación y la revisión de forma programada después del Patch Tuesday y antes de cada promoción, y publicar la puerta en el canal de parches.
- Leer las compilaciones y los problemas conocidos desde la API de Windows Updates de Microsoft Graph en lugar de copiarlos.
- Añadir las actualizaciones de controladores y firmware por modelo como una categoría propia."""),

dict(n="42", repo="42-retail-store-it-health", date="2026-11-03", cat="tools",
 title_en="A store failing over to 4G nine times a week and a corner without a line: IT for a retail chain",
 title_es="Una tienda que salta al 4G nueve veces en una semana y un córner sin línea: el IT de una cadena de tiendas",
 seo_title_en="Store IT health review for a retail chain · Iñigo González",
 seo_title_es="Revisión semanal del IT de cada tienda · Iñigo González",
 seo_desc="Weekly store IT review for a retail chain: lines and 4G backup, tunnels, devices, printers, tickets, openings and users, with a visit and ship list.",
 dek_en="From the store list, the daily connectivity per store, the Intune and Active Directory devices, the printer status, the store tickets, the opening checklists and the joiners and leavers: whether each store can sell and operate tomorrow, a red, amber or green status with its reasons, which stores need a visit, a shipment or a vendor call, by region and field technician, and the pack for the weekly retail operations meeting.",
 dek_es="A partir de la lista de tiendas, la conectividad diaria de cada una, los equipos de Intune y Active Directory, el estado de las impresoras, los tickets de tienda, las checklists de apertura y las altas y bajas: si cada tienda puede vender y trabajar mañana, un estado rojo, ámbar o verde con sus motivos, qué tiendas necesitan una visita, un envío o una llamada al proveedor, por región y técnico de campo, y el pack para la reunión semanal de operaciones de tienda.",
 en="""

## The problem
A retail chain's central IT sees a hundred stores through a monitoring console, a device list and a ticket queue, and none of the stores has anyone from IT inside. In a typical week a shopping centre store fails over to its 4G router nine times, keeps selling, and nobody notices that the SIM is at 93% of its data cap until the router is throttled on a Saturday afternoon; fourteen backup routers have never been tested; every store in one region loses its tunnel to head office around eight in the evening, and the service desk logs seventeen separate problems; a corner inside a department store opens in ten days and its line is still not installed, because the carrier cannot get past the department store's comms room; three stores with the same receipt printer model log jam after jam; one store raises four times the median number of tickets, nearly all about the handhelds losing Wi-Fi in the stockroom; two stores closed weeks ago with their laptops and terminals still inside; and two people start tomorrow without an account. This is not the venue readiness check I published last week, which looks at a hospitality venue's systems before service, nor the hotel pre-opening tracker: it is central IT looking after a whole estate of stores, week after week, and deciding who goes where.

## What I built
- Connectivity: primary line availability over the week, failovers to the backup router and time on backup, backup routers never tested, backup SIMs near their data cap, stores with no backup line, the site-to-site tunnel by store and by region, and failed AnyConnect connections.
- Devices: store and back-office computers not checked in or on Windows out of support, printers offline or low on toner, receipt printers that jam again and again and the model behind them, card terminals not reporting, handhelds offline and UPS that failed their self-test.
- Tickets: tickets per store against the estate median, repeat incidents, past SLA, field visits pending and vendor tickets open.
- Openings and changes: the pre-opening checklist of every store opening in the next four weeks, closed stores with devices not recovered, closings and refurbishments; and the users side kept light: joiners without an account, leavers still enabled and shared accounts of closed stores (the access review I published last week goes deeper).
- A red, amber or green status per store with its reasons, a store grid by region, the visit and ship list ranked by region and field technician, the vendor calls, `report.html`, `store-review.md` for the weekly retail operations meeting with the trend against last week, CSVs for every area, and a read-only PowerShell exporter for Microsoft Graph, Active Directory and Entra ID.

## How it is built
Python with the standard library only. Every issue belongs to a store and says what it needs: a visit from the field technician, a shipment, a vendor call or remote work, so the list for each technician falls out of the checks instead of being written by hand. Connectivity uses the last seven days and compares them with the week before; tickets use the last thirty days and the estate median, and a ticket on hold with a vendor does not count against the SLA. Stores in refurbishment are not checked until they reopen, and a closed store is only checked for its devices and accounts. The connectivity and printer data are the exports of the monitoring tool, and the printer status and toner are the standard SNMP printer objects. The demo is a made-up eyewear chain with 122 stores in Spain and Portugal, street stores, shopping centres and corners inside a department store, reviewed on a Tuesday morning with the problems placed on purpose. 14 tests, a runbook with the weekly cycle and the meeting agenda, and a GitHub Actions workflow that runs the tests and rebuilds the demo data and the screenshot.

## What I learned
From supporting the boutiques and points of sale of luxury retail brands, with their printers, the Cisco AnyConnect VPN and the onboarding of every new person (network, email, AS400 and business applications); from about 200 pre-openings of brand corners inside department stores; from Intune and Microsoft Graph; from owning the incident and change processes; and from supporting about 2,500 users across European offices. At one of those openings the connectivity failed two hours before the doors opened: I brought the corner back online with a temporary USB 4G router while I checked the store's connection and the floor's comms room with the department store's technicians. The lessons behind the tool are that a store on its backup is one failure away from not selling; that an untested backup is a hope; that a whole region going wrong at the same hour is one cause, not seventeen tickets; that the line of a corner depends on the host's comms room, so the joint visit has to be booked early and a 4G router has to be ready for opening day; that one printer model jamming in three cities is a vendor call; that a store with four times the median usually has one problem; and that tomorrow's starters need their accounts this morning.

## Next steps
- Run the exports and the review every Monday night and send each field technician their part of the list.
- Read the tickets from the ServiceNow Table API instead of a list export.
- Keep the weekly history of every store to show its trend over a quarter.""",
 es="""

## El problema
El IT central de una cadena de tiendas ve cien tiendas a través de una consola de monitorización, un listado de equipos y una cola de tickets, y en ninguna de ellas hay nadie de informática. En una semana normal, una tienda de centro comercial salta al router 4G nueve veces, sigue vendiendo y nadie se da cuenta de que la SIM va por el 93% de su límite de datos hasta que el router se queda sin velocidad un sábado por la tarde; catorce routers de respaldo no se han probado nunca; todas las tiendas de una región pierden el túnel con la central hacia las ocho de la tarde y el service desk lo registra como diecisiete problemas distintos; un córner dentro de unos grandes almacenes abre en diez días y su línea sigue sin instalar, porque el operador no puede pasar del cuarto de comunicaciones de los grandes almacenes; tres tiendas con el mismo modelo de impresora de tickets acumulan atasco tras atasco; una tienda abre cuatro veces la mediana de tickets, casi todos porque las PDA pierden el Wi-Fi en el almacén; dos tiendas cerraron hace semanas con los portátiles y los datáfonos todavía dentro; y dos personas empiezan mañana sin cuenta. No es la comprobación de preparación de un local que publiqué la semana pasada, que mira los sistemas de un local de hostelería antes del servicio, ni el seguimiento de la preapertura de un hotel: es el IT central cuidando de toda una red de tiendas, semana tras semana, y decidiendo quién va a dónde.

## Qué he hecho
- Conectividad: disponibilidad de la línea principal en la semana, saltos al router de respaldo y tiempo en respaldo, routers de respaldo sin probar nunca, SIM de respaldo cerca de su límite de datos, tiendas sin línea de respaldo, el túnel con la central por tienda y por región, y conexiones de AnyConnect fallidas.
- Equipos: PC de tienda y de trastienda sin sincronizar o con una versión de Windows sin soporte, impresoras desconectadas o con poco tóner, impresoras de tickets que se atascan una y otra vez y el modelo que hay detrás, datáfonos que no reportan, PDA desconectadas y SAI que han fallado su autotest.
- Tickets: tickets por tienda frente a la mediana de la red, incidencias repetidas, fuera de SLA, visitas pendientes y tickets abiertos con proveedores.
- Aperturas y cambios: la checklist de cada tienda que abre en las próximas cuatro semanas, tiendas cerradas con equipos sin recuperar, cierres y reformas; y la parte de usuarios, ligera a propósito: altas sin cuenta, bajas todavía activas y cuentas compartidas de tiendas cerradas (la revisión de accesos que publiqué la semana pasada va más a fondo).
- Un estado rojo, ámbar o verde por tienda con sus motivos, una cuadrícula de tiendas por región, la lista de visitas y envíos ordenada por región y técnico de campo, las llamadas a proveedores, `report.html`, `store-review.md` para la reunión semanal de operaciones de tienda con la tendencia frente a la semana anterior, CSV de cada área y un exportador de solo lectura en PowerShell para Microsoft Graph, Active Directory y Entra ID.

## Cómo está hecho
Python solo con la librería estándar. Cada problema pertenece a una tienda y dice lo que necesita: una visita del técnico de campo, un envío, una llamada al proveedor o trabajo en remoto, así que la lista de cada técnico sale de las comprobaciones en lugar de escribirse a mano. La conectividad usa los últimos siete días y los compara con la semana anterior; los tickets usan los últimos treinta días y la mediana de la red, y un ticket en espera del proveedor no cuenta para el SLA. Las tiendas en reforma no se revisan hasta que reabren, y de una tienda cerrada solo se miran sus equipos y sus cuentas. Los datos de conectividad e impresoras son las exportaciones de la herramienta de monitorización, y el estado y el tóner de las impresoras son los objetos SNMP estándar de impresora. La demo es una cadena de ópticas inventada con 122 tiendas en España y Portugal, entre tiendas de calle, centros comerciales y córners dentro de unos grandes almacenes, revisada un martes por la mañana con los problemas puestos a propósito. 14 tests, un runbook con el ciclo semanal y el orden del día de la reunión, y un workflow de GitHub Actions que ejecuta los tests y regenera los datos de la demo y la captura.

## Qué aprendí
De dar soporte a las boutiques y puntos de venta de marcas de lujo, con sus impresoras, la VPN de Cisco AnyConnect y el alta de cada persona nueva (red, correo, AS400 y aplicaciones de negocio); de unas 200 preaperturas de córners de marca dentro de grandes almacenes; de Intune y Microsoft Graph; de ser responsable de los procesos de incidencias y cambios; y de dar soporte a unos 2.500 usuarios en oficinas europeas. En una de esas aperturas la conectividad se cayó dos horas antes de abrir: volví a dar servicio al córner con un router USB 4G provisional mientras revisaba la conexión de la tienda y el cuarto de comunicaciones de la planta con los técnicos de los grandes almacenes. Las lecciones que hay detrás de la herramienta son que una tienda en respaldo está a un fallo de no poder vender; que un respaldo sin probar es una esperanza; que una región entera fallando a la misma hora es una sola causa, no diecisiete tickets; que la línea de un córner depende del cuarto de comunicaciones del anfitrión, así que hay que reservar pronto la visita conjunta y tener un router 4G listo para el día de la apertura; que un modelo de impresora que se atasca en tres ciudades es una llamada al proveedor; que una tienda con cuatro veces la mediana suele tener un único problema; y que quien empieza mañana necesita su cuenta esta mañana.

## Siguientes pasos
- Ejecutar las exportaciones y la revisión cada lunes por la noche y enviar a cada técnico de campo su parte de la lista.
- Leer los tickets desde la Table API de ServiceNow en lugar de una exportación de lista.
- Guardar el histórico semanal de cada tienda para ver su tendencia en un trimestre."""),
dict(n="43", repo="43-azure-cost-rightsizing", date="2026-11-04", updated="2026-11-11", cat="tools",
 title_en="A reservation at 55% about to auto-renew and VMs billed while stopped: the Azure cost review",
 title_es="Una reserva al 55% que se renueva sola y VMs paradas que se pagan: la revisión de costes de Azure",
 seo_title_en="Monthly Azure cost review and right-sizing · Iñigo González",
 seo_title_es="Revisión de costes de Azure y redimensionado · Iñigo González",
 seo_desc="Monthly Azure cost review from the FOCUS export: right-sizing, waste, reservations and savings plans, showback by cost centre, budgets and unit cost.",
 seo_desc_es="Revisión mensual de costes de Azure: redimensionado, desperdicio, reservas y planes de ahorro, showback por centro de coste, presupuestos y coste unitario.",
 dek_en="From the Azure Cost Management FOCUS export, the virtual machines with 30 days of Azure Monitor metrics, the disks, the public IPs, the reservations and savings plans and the budgets: which VMs go one size down, what is paid for and not used, which commitments to renew, exchange or let expire, the spend of each cost centre against its budget and forecast, and the monthly savings identified with how each one was worked out.",
 dek_es="A partir de la exportación FOCUS de Azure Cost Management, las máquinas virtuales con 30 días de métricas de Azure Monitor, los discos, las IP públicas, las reservas y los planes de ahorro y los presupuestos: qué VMs bajan un tamaño, qué se paga sin usarse, qué compromisos renovar, cambiar o dejar caducar, el gasto de cada centro de coste frente a su presupuesto y su previsión, y el ahorro mensual identificado con cómo se ha calculado cada partida.",
 en="""

## The problem
The Azure bill tells you how much, not what to do. In a typical month three SQL Server VMs on E16s_v5 peak at 15% CPU and use a third of their memory, because they were sized for a migration two years ago; a reporting VM was shut down from inside Windows three weeks ago and is still billed as if it were running, because nobody deallocated it; fourteen development and test VMs run every night and every weekend; the disks and public IPs of a migration project that finished in August are still there, unattached and untagged; a reservation for ten batch servers runs at 55% since half the batch moved elsewhere, expires in six weeks and is set to renew itself; forty production VMs run all month on pay-as-you-go while only a quarter of the VM spend is covered by a commitment; 11% of the bill has no cost centre, so nobody is asked about it; one cost centre ends the month 14% over budget and is on course to do it again; and the cost per active user of the digital channels goes up 15% because the users fell and the cost did not. This is not the cost dashboard I published at the start of the series, which looks for the week that goes wrong across AWS and Azure while it happens: it is the monthly review that comes after, and decides what to resize, delete, schedule and commit, and who pays for each line.

## What I built
- Right-sizing: VMs whose CPU p95 and peak memory over 30 days fit in one size down within the same family, with the projected use after the resize and the monthly saving, and idle VMs; VMs covered by a reservation are flagged, because resizing them saves nothing until the freed capacity is used or exchanged.
- Waste: VMs stopped but not deallocated, non-production VMs on around the clock with no schedule tag, managed disks unattached for weeks and public IPs associated with nothing.
- Commitments: reservations and savings plans under their utilisation target with the unused cost of the month, the ones expiring in the next 90 days with the renew or exchange decision (critical when they would renew themselves at a low utilisation), and the VM coverage with the steady pay-as-you-go VMs a commitment would cover.
- Showback: the month by cost centre against its budget, the forecast for the current month, the cost with no cost centre tag and where it sits, the unit cost per cost centre and the VMs missing the tags showback needs.
- `report.html` with a verdict for the month, `savings-pack.md` for the monthly FinOps review with a decision column for every resize and commitment, CSVs for right-sizing, waste, commitments, showback and actions, and a read-only PowerShell exporter for the Az modules and the reservations and savings plans APIs.

## How it is built
Python with the standard library only. The cost side is the FOCUS export as Cost Management writes it: effective cost for the amortised spend, billed cost next to it, the savings of the commitments as list minus effective cost of the rows they cover, and the unused part from the rows marked as unused. Every saving is an estimate per month at the run rate of the last seven days, and the pack says how it was worked out: half the vCPUs in the same family is half the compute cost, an office-hours schedule is 60 of 168 hours, and a commitment is an upper estimate to be checked against Azure Advisor before buying. Coverage is measured in hours, because a Windows or SQL Server VM covered by a reservation still has pay-as-you-go rows for its licence. The demo is a made-up insurance group with five subscriptions and 133 VMs, reviewed on 4 November for October with round fictional prices and the problems placed on purpose: it identifies 11,101 euros a month of savings on a 94,403 euro month. 15 tests, a runbook for the monthly cycle and the FinOps review, and a GitHub Actions workflow that runs the tests and rebuilds the demo data and the screenshot.

## What I learned
From working with Azure Cost Management and applying the FinOps Framework, with reservations, savings plans and commitments; from optimising Azure costs with right-sizing and reservations; from implementing showback and chargeback and unit cost metrics; from software asset management and licence and SaaS cost control, with Apptio and Flexera, TBM, FOCUS and GreenOps; from business cases with ROI and measurable benefits and from owning an IT budget; and from operating a hybrid AWS and Azure environment with Azure Monitor and Log Analytics. The lessons behind the tool are that the peak decides a resize, not the average; that a stopped VM is not a deallocated one; that an unattached disk is billed in full and nobody misses it; that the waste has to be fixed before buying a commitment, or the reservation locks in today's oversizing for years; that a commitment under 80% is money paid for nothing, and one that renews itself at 55% is the same mistake again; that untagged cost has no owner, so nobody is ever asked about it; and that the unit cost is the number the business reads.

## Next steps
- Run the exports and the review on the fourth day of every month and send each owner their lines.
- Size the commitments from the Cost Management benefit recommendations and price the resizes from the Azure Retail Prices API.
- Add the PaaS services that right-size the same way, such as App Service plans and Azure SQL Database.""",
 es="""

## El problema
La factura de Azure dice cuánto, no qué hacer. En un mes normal tres VMs de SQL Server en E16s_v5 llegan como mucho al 15% de CPU y usan un tercio de su memoria, porque se dimensionaron para una migración hace dos años; una VM de informes se apagó desde dentro de Windows hace tres semanas y se sigue pagando como si estuviera encendida, porque nadie la desasignó; catorce VMs de desarrollo y pruebas funcionan todas las noches y todos los fines de semana; los discos y las IP públicas de un proyecto de migración que terminó en agosto siguen ahí, sin conectar y sin etiquetar; una reserva para diez servidores de batch va al 55% desde que la mitad del batch se fue a otra plataforma, caduca en seis semanas y está configurada para renovarse sola; cuarenta VMs de producción funcionan todo el mes con pago por uso mientras solo una cuarta parte del gasto en VMs está cubierta por un compromiso; el 11% de la factura no tiene centro de coste, así que nadie pregunta por él; un centro de coste cierra el mes un 14% por encima del presupuesto y va camino de repetirlo; y el coste por usuario activo de los canales digitales sube un 15% porque los usuarios han bajado y el coste no. No es el panel de costes que publiqué al principio de la serie, que busca la semana que se tuerce en AWS y Azure mientras pasa: es la revisión mensual que viene después, y decide qué redimensionar, borrar, programar y comprometer, y quién paga cada línea.

## Qué he hecho
- Redimensionado: VMs cuyo p95 de CPU y pico de memoria en 30 días caben en un tamaño menos dentro de la misma familia, con el uso previsto después del cambio y el ahorro mensual, y VMs ociosas; las VMs cubiertas por una reserva se marcan, porque redimensionarlas no ahorra nada hasta que la capacidad liberada se usa o se cambia.
- Desperdicio: VMs paradas pero no desasignadas, VMs que no son de producción encendidas día y noche sin etiqueta de horario, discos administrados sin conectar desde hace semanas e IP públicas que no están asociadas a nada.
- Compromisos: reservas y planes de ahorro por debajo de su objetivo de uso con el coste sin usar del mes, los que caducan en los próximos 90 días con la decisión de renovar o cambiar (crítico cuando se renovarían solos con un uso bajo), y la cobertura de las VMs con las VMs estables en pago por uso que cubriría un compromiso.
- Showback: el mes por centro de coste frente a su presupuesto, la previsión del mes en curso, el coste sin etiqueta de centro de coste y dónde está, el coste unitario de cada centro de coste y las VMs a las que les faltan las etiquetas que necesita el showback.
- `report.html` con un veredicto del mes, `savings-pack.md` para la revisión mensual de FinOps con una columna de decisión para cada redimensionado y cada compromiso, CSV de redimensionado, desperdicio, compromisos, showback y acciones, y un exportador de solo lectura en PowerShell para los módulos Az y las API de reservas y planes de ahorro.

## Cómo está hecho
Python solo con la librería estándar. La parte de costes es la exportación FOCUS tal como la escribe Cost Management: el coste efectivo para el gasto amortizado, el coste facturado al lado, el ahorro de los compromisos como coste de lista menos coste efectivo de las filas que cubren, y la parte sin usar a partir de las filas marcadas como no usadas. Cada ahorro es una estimación mensual al ritmo de los últimos siete días, y el pack explica cómo se ha calculado: la mitad de vCPU en la misma familia es la mitad del coste de cómputo, un horario de oficina son 60 de 168 horas, y un compromiso es una estimación por arriba que hay que contrastar con Azure Advisor antes de comprar. La cobertura se mide en horas, porque una VM de Windows o de SQL Server cubierta por una reserva sigue teniendo filas de pago por uso por su licencia. La demo es un grupo asegurador inventado con cinco suscripciones y 133 VMs, revisado el 4 de noviembre sobre octubre con precios redondos inventados y los problemas puestos a propósito: identifica 11.101 euros al mes de ahorro sobre un mes de 94.403 euros. 15 tests, un runbook para el ciclo mensual y la revisión de FinOps, y un workflow de GitHub Actions que ejecuta los tests y regenera los datos de la demo y la captura.

## Qué aprendí
De trabajar con Azure Cost Management y aplicar el FinOps Framework, con reservas, planes de ahorro y compromisos; de optimizar costes de Azure con redimensionado y reservas; de implantar showback y chargeback y métricas de coste unitario; de la gestión de activos de software y el control del coste de licencias y SaaS, con Apptio y Flexera, TBM, FOCUS y GreenOps; de los casos de negocio con ROI y beneficios medibles y de ser responsable de un presupuesto de IT; y de operar un entorno híbrido de AWS y Azure con Azure Monitor y Log Analytics. Las lecciones que hay detrás de la herramienta son que un redimensionado lo decide el pico, no la media; que una VM parada no es una VM desasignada; que un disco sin conectar se paga entero y nadie lo echa de menos; que el desperdicio hay que arreglarlo antes de comprar un compromiso, o la reserva congela durante años el sobredimensionado de hoy; que un compromiso por debajo del 80% es dinero pagado por nada, y uno que se renueva solo al 55% es el mismo error otra vez; que el coste sin etiquetar no tiene dueño, así que nadie pregunta nunca por él; y que el coste unitario es el número que lee el negocio.

## Siguientes pasos
- Ejecutar las exportaciones y la revisión el cuarto día de cada mes y enviar a cada responsable sus líneas.
- Dimensionar los compromisos con las recomendaciones de Cost Management y poner precio a los redimensionados con la API de precios de Azure.
- Añadir los servicios PaaS que se redimensionan igual, como los planes de App Service y Azure SQL Database."""),
dict(n="44", repo="44-m365-copilot-readiness", date="2026-11-05", cat="tools",
 title_en="An HR site open to all and an agent nobody owns: is the tenant ready for the next Copilot wave?",
 title_es="Un sitio de RR. HH. abierto a todos y un agente sin dueño: ¿está listo el tenant para Copilot?",
 seo_title_en="Microsoft 365 Copilot readiness review · Iñigo González",
 seo_title_es="Revisión de preparación para Copilot · Iñigo González",
 seo_desc="Microsoft 365 Copilot readiness before each wave: licences to reclaim, training, MFA, SharePoint oversharing, labels, DLP, agents and adoption.",
 dek_en="From the Entra ID users, the Microsoft 365 Copilot usage report, the SharePoint sites, the label coverage and DLP policies, the Copilot Studio agents and the training records: which licences to reclaim, whether each wave is trained, registered for MFA and on a compliant device, what Copilot could surface that it should not, which agents have no owner or use connectors nobody approved, and a verdict per wave for the steering group.",
 dek_es="A partir de los usuarios de Entra ID, el informe de uso de Microsoft 365 Copilot, los sitios de SharePoint, la cobertura de etiquetas y las directivas de DLP, los agentes de Copilot Studio y los registros de formación: qué licencias recuperar, si cada oleada está formada, registrada en MFA y con un equipo conforme, qué podría mostrar Copilot que no debería, qué agentes no tienen dueño o usan conectores que nadie ha aprobado, y un veredicto por oleada para el comité de dirección.",
 en="""

## The problem
Copilot answers from everything a person can already open, so a rollout that went well in the pilot can go wrong in the next wave for reasons no single console shows. Two weeks before a wave of 400 people, the HR employee relations site has been shared with Everyone except external users since a migration, and 1,650 people could get it back in an answer; the recruitment site has Anyone links and no label; a closed litigation site has no owner and is still searchable; a quarter of Finance's files carry a sensitivity label and the DLP policy for Copilot is still in simulation; an agent published to the whole company was built by someone who has left and reads from a Dropbox connector nobody approved; an HR agent helps screen candidates and is not in the AI register; 34 licences have not been used in a month while the next wave is 14 licences short; and the wave itself is 70% trained, with 14 people not registered for MFA and 31 without a compliant device. This is not the tenant governance review I published a couple of weeks ago, which looks at admin roles, Conditional Access and tenant settings: it is the review before each Copilot wave and every month after it, about what Copilot can reach and who is using it.

## What I built
- Licences: licensed users with no Copilot activity in 30 days or never, licences on disabled accounts, their monthly cost, and whether the pool covers the next wave once they are reclaimed.
- Waves: training, MFA registration, a compliant device and a licence for every person of a wave before its go-live, and a champion in each department.
- Oversharing: SharePoint sites shared with Everyone except external users or with Anyone links, sites with no owner or only one, no sensitivity label, and inactive sites Copilot can still search, with Restricted Content Discovery as the stopgap while they are fixed.
- Labels and DLP: label coverage per department and whether a DLP policy is enforced on the Microsoft 365 Copilot location; agents with no owner, published to everyone, using connectors not on the allowed list or unused, and agents that support decisions about people with no entry in the AI register; and adoption by department and app with its trend and the survey.
- A verdict per wave (ready, attention or not ready), `report.html`, `readiness-pack.md` for the Copilot steering group with a decision column per wave, CSVs for licences to reclaim, oversharing, agents, adoption, waves and actions, and a read-only PowerShell exporter for Microsoft Graph and SharePoint Online.

## How it is built
Python with the standard library only. Every issue says which waves it reaches: the waves with people in its department, or every wave when it is critical oversharing or an agent open to the whole company, because any Copilot user who can open the content can get it back in an answer. A wave is not ready when a critical issue reaches it. The usage report is the Microsoft Graph report per user with the last activity date overall and per app; the site columns are the Get-SPOSite properties plus the counts of the SharePoint data access governance report; the agents come from the Power Platform inventory. Licence costs are estimates at a price set in the settings, and the AI register column is a record, not a legal assessment. The demo is a made-up energy company with 1,800 people in three waves, reviewed on 5 November two weeks before wave 2, with the problems placed on purpose: 37 licences to reclaim, 1,110 euros a month, four critical sites and every wave not ready until they are fixed. 14 tests, a runbook with the steering group agenda, go or no go per wave and the ADKAR steps, and a GitHub Actions workflow that runs the tests and rebuilds the demo data and the screenshot. The findings can go as evidence into the controls register I published earlier in the series.

## What I learned
From deploying Microsoft 365 Copilot and AI tools and driving their adoption, and administering Microsoft 365 agents and Copilot Studio; from being Global Administrator of Microsoft 365, with PIM, Conditional Access and app integration; from Microsoft Purview, with DLP and sensitivity labels, from SharePoint for many years and from Power Platform; from change management with Prosci, ADKAR and Kotter; from the EU AI Act and responsible AI; and from business cases with measurable benefits. The lessons behind the tool are that Copilot does not create new access, it makes the old oversharing easy to find, so the permissions have to be fixed before the wave and not after; that Restricted Content Discovery buys time but changes no permission; that a label coverage of a quarter leaves DLP with little to act on; that an agent without an owner is nobody's problem until it answers the wrong question; that an agent that helps decide about people needs its entry in the register before it is used, not after; that a licence nobody uses is the cheapest licence for the next wave; and that training and champions decide the adoption more than the licence does.

## Next steps
- Run the review three weeks and one week before each wave, and every month after.
- Read the agents from the Power Platform inventory API and the label coverage from the Purview content explorer export.
- Add the agents usage report and keep a year of adoption to set it next to the time people say they save.""",
 es="""

## El problema
Copilot responde a partir de todo lo que una persona ya puede abrir, así que un despliegue que fue bien en el piloto puede torcerse en la siguiente oleada por motivos que ninguna consola enseña por sí sola. Dos semanas antes de una oleada de 400 personas, el sitio de relaciones laborales de RR. HH. está compartido con Todos excepto los usuarios externos desde una migración, y 1.650 personas podrían recibirlo en una respuesta; el sitio de selección tiene vínculos de cualquier persona y ninguna etiqueta; un sitio de un litigio cerrado no tiene propietario y sigue siendo buscable; una cuarta parte de los archivos de Finanzas lleva etiqueta de confidencialidad y la directiva de DLP para Copilot sigue en simulación; un agente publicado para toda la empresa lo creó alguien que ya se ha ido y lee de un conector de Dropbox que nadie aprobó; un agente de RR. HH. ayuda a cribar candidatos y no está en el registro de IA; 34 licencias llevan un mes sin usarse mientras a la siguiente oleada le faltan 14; y la propia oleada está formada al 70%, con 14 personas sin registrar en MFA y 31 sin un equipo conforme. No es la revisión de gobierno del tenant que publiqué hace un par de semanas, que mira roles de administración, Acceso condicional y configuración: es la revisión antes de cada oleada de Copilot y cada mes después, sobre lo que Copilot puede alcanzar y quién lo está usando.

## Qué he hecho
- Licencias: usuarios con licencia sin actividad en Copilot en 30 días o nunca, licencias en cuentas deshabilitadas, su coste mensual, y si el remanente cubre la siguiente oleada una vez recuperadas.
- Oleadas: formación, registro en MFA, un equipo conforme y una licencia para cada persona de una oleada antes de su arranque, y un champion en cada departamento.
- Sobreexposición: sitios de SharePoint compartidos con Todos excepto los usuarios externos o con vínculos de cualquier persona, sitios sin propietario o con uno solo, sin etiqueta de confidencialidad, y sitios inactivos que Copilot todavía puede buscar, con Restricted Content Discovery como medida provisional mientras se arreglan.
- Etiquetas y DLP: cobertura de etiquetas por departamento y si hay una directiva de DLP aplicada en la ubicación de Microsoft 365 Copilot; agentes sin propietario, publicados para todos, con conectores fuera de la lista permitida o sin uso, y agentes que apoyan decisiones sobre personas sin entrada en el registro de IA; y la adopción por departamento y aplicación con su tendencia y la encuesta.
- Un veredicto por oleada (lista, atención o no lista), `report.html`, `readiness-pack.md` para el comité de dirección de Copilot con una columna de decisión por oleada, CSV de licencias a recuperar, sobreexposición, agentes, adopción, oleadas y acciones, y un exportador de solo lectura en PowerShell para Microsoft Graph y SharePoint Online.

## Cómo está hecho
Python solo con la librería estándar. Cada problema dice a qué oleadas alcanza: a las que tienen personas de su departamento, o a todas cuando es una sobreexposición crítica o un agente abierto a toda la empresa, porque cualquier usuario de Copilot que pueda abrir el contenido puede recibirlo en una respuesta. Una oleada no está lista cuando le alcanza un problema crítico. El informe de uso es el informe de Microsoft Graph por usuario, con la fecha de última actividad global y por aplicación; las columnas de los sitios son las propiedades de Get-SPOSite más los recuentos del informe de gobierno de acceso a datos de SharePoint; los agentes salen del inventario de Power Platform. El coste de las licencias es una estimación a un precio que se fija en la configuración, y la columna del registro de IA es un registro, no una valoración jurídica. La demo es una empresa de energía inventada con 1.800 personas en tres oleadas, revisada el 5 de noviembre a dos semanas de la segunda, con los problemas puestos a propósito: 37 licencias a recuperar, 1.110 euros al mes, cuatro sitios críticos y ninguna oleada lista hasta que se arreglen. 14 tests, un runbook con el orden del día del comité, el sí o no de cada oleada y los pasos de ADKAR, y un workflow de GitHub Actions que ejecuta los tests y regenera los datos de la demo y la captura. Los hallazgos pueden ir como evidencia al registro de controles que publiqué antes en la serie.

## Qué aprendí
De desplegar Microsoft 365 Copilot y herramientas de IA e impulsar su adopción, y de administrar los agentes de Microsoft 365 y Copilot Studio; de ser administrador global de Microsoft 365, con PIM, Acceso condicional e integración de aplicaciones; de Microsoft Purview, con DLP y etiquetas de confidencialidad, de muchos años con SharePoint y de Power Platform; de la gestión del cambio con Prosci, ADKAR y Kotter; del Reglamento Europeo de IA y la IA responsable; y de los casos de negocio con beneficios medibles. Las lecciones que hay detrás de la herramienta son que Copilot no crea accesos nuevos, hace fácil encontrar la sobreexposición de siempre, así que los permisos hay que arreglarlos antes de la oleada y no después; que Restricted Content Discovery da tiempo pero no cambia ningún permiso; que con una cuarta parte de los archivos etiquetados la DLP tiene poco sobre lo que actuar; que un agente sin propietario no es problema de nadie hasta que responde lo que no debe; que un agente que ayuda a decidir sobre personas necesita su entrada en el registro antes de usarse, no después; que una licencia que nadie usa es la licencia más barata para la siguiente oleada; y que la formación y los champions deciden la adopción más que la licencia.

## Siguientes pasos
- Ejecutar la revisión tres semanas y una semana antes de cada oleada, y cada mes después.
- Leer los agentes desde la API de inventario de Power Platform y la cobertura de etiquetas desde la exportación del explorador de contenido de Purview.
- Añadir el informe de uso de agentes y guardar un año de adopción para ponerlo al lado del tiempo que la gente dice ahorrar."""),
dict(n="45", repo="45-network-config-compliance", date="2026-11-06", cat="tools",
 title_en="Telnet on a branch switch and a night change nobody saved: the weekly network compliance review",
 title_es="Telnet en un switch de sede y un cambio nocturno sin guardar: la revisión semanal de la red",
 seo_title_en="Network configuration compliance review · Iñigo González",
 seo_title_es="Cumplimiento de configuración de red · Iñigo González",
 seo_desc="Weekly compliance review of Cisco, Aruba and FortiGate configs: backups, unsaved changes, management plane, SNMP, VLANs, policies and end of support.",
 seo_desc_es="Revisión semanal de configuraciones Cisco, Aruba y FortiGate: copias, cambios sin guardar, gestión, SNMP, VLAN, políticas y fin de soporte.",
 dek_en="From the configuration backups of the Cisco, HPE Aruba and FortiGate devices, the comms-room inventory in Device42, a baseline and the approved changes: which devices have no recent backup or unsaved changes, which were changed without a ticket, where telnet, SNMP public or admin access on the WAN are still open, which ports and trunks are out of baseline, what is past end of support, and a status per device and site with the change window for each fix.",
 dek_es="A partir de las copias de configuración de los equipos Cisco, HPE Aruba y FortiGate, el inventario de las salas de comunicaciones en Device42, una línea base y los cambios aprobados: qué equipos no tienen copia reciente o tienen cambios sin guardar, cuáles se cambiaron sin ticket, dónde siguen abiertos telnet, SNMP public o la administración por la WAN, qué puertos y troncales se salen de la línea base, qué está fuera de soporte, y un estado por equipo y por sede con la ventana de cambios de cada corrección.",
 en="""

## The problem
Network configurations drift one night change at a time, and in a company with several comms rooms nobody reads every running configuration every week. In a normal week a branch switch still accepts telnet because it was installed from an old template; two devices answer SNMP with the community public, one of them because nobody removed the factory default; the switches of one site point NTP to a server that was switched off, so their logs disagree with everyone else's; a FortiGate has HTTPS and SSH admin open on its WAN interface and an accept policy from all to all with service ALL and logging off, left from a cutover two months ago; an access switch was changed at two in the morning with no ticket and the change was never saved, so the next power cut takes it away; two devices have no backup at all and a whole site's backups are ten days old since a firewall rule broke the backup job; six unused ports are up in VLAN 1; a router runs a release that is not on the approved list; and an access switch went out of vendor support five years ago and is still in the rack. Each of these is visible in one place, the backup, the inventory or the change calendar, and nobody joins them. The end-of-support dates come from the same Device42 export that the asset lifecycle planner I published earlier in the series turns into a refresh plan; this review looks at what is configured on the devices.

## What I built
- Backups: devices with no backup, backups older than a week, Cisco running configurations changed after the last save, and changes made outside an approved change ticket.
- Management plane: SSH v2 only, no telnet, enable secret and password encryption, AAA with TACACS+ or RADIUS and a local fallback, a login banner, an idle timeout and management access restricted to the management network.
- Logging and time, and switching: NTP servers, syslog hosts, time zone and SNMP v3 only; unused ports shut down in the parking VLAN, PortFast and BPDU guard on user ports, no native VLAN 1 on trunks, no user ports in VLAN 1 and port security where the baseline asks for it.
- FortiGate and lifecycle: admin access on WAN interfaces, any-any accept policies, policies without logging, disabled policies kept for months and firmware below the baseline; OS versions not approved for the model, end of support, and backups that do not match the inventory.
- A status per device (compliant, drift or non-compliant), per site and overall, `report.html` with a grid of devices by area, `compliance-pack.md` for the change board with a proposed window and a decision column per finding, CSVs with every rule for every device, backups, lifecycle and actions, and a read-only PowerShell collector with Posh-SSH.

## How it is built
Python with the standard library only. There is a small parser per platform, kept to what the rules read: the Cisco IOS-XE running configuration with its `Last configuration change` and `NVRAM config last updated` header lines, the ArubaOS-Switch configuration with its VLAN blocks and port ranges, and the FortiOS `config`, `edit`, `set` blocks with the defaults assumed when a plain `show` leaves them out. Every rule gives every device pass, fail or not applicable, so the evidence for an audit is one CSV; a device is non-compliant with a critical failure and a site takes the worst status of its devices. Unused ports are the ones with no description, because the description is the record that a port is in use. The collector only sends `show running-config` or `show full-configuration` and turns paging off for its own session; Oxidized and RANCID backups work as they are. The demo is a made-up logistics company with three comms rooms and 34 devices, reviewed on 6 November with the problems placed on purpose: 9 compliant, 17 drifting and 8 non-compliant, seven critical findings for the next window. 14 tests, a runbook for the weekly cycle with how each finding becomes a change and how to handle exceptions, and a GitHub Actions workflow that runs the tests and rebuilds the demo data and the screenshot. The FortiGate checks are the weekly hygiene next to the segmentation review of the OT lab I published earlier in the series.

## What I learned
From operating Cisco switches and routers, comms rooms and racks across several sites, with the connectivity, hardware and service vendors and the DR and BCP tests; from Device42 for the comms-room inventory; from Fortinet FortiGate; from HP switches, MikroTik and TP-Link, and LAN, WAN and Wi-Fi in Spain, Italy and Turkey; from IP/MPLS and QoS, BGP, OSPF and VXLAN; from monitoring with SolarWinds and Zabbix and automating with PowerShell and Python; and from being the process owner of change management and the CMDB, and from audit responses applying ISO 27001 and NIS2. The lessons behind the tool are that a backup nobody checks is not a backup; that a change that was never saved is a problem that waits for the next power cut; that the change calendar and the running configuration have to agree, and when they do not, the conversation is with the engineer, not about the device; that factory defaults like SNMP public outlive every template; that a temporary any-any policy is never temporary unless someone puts a date on it; that a description on every used port is what makes unused ports visible; and that the baseline has to be a document under change control, or every exception becomes the new standard.

## Next steps
- Run the collection every night and the review every Friday before the change board.
- Compare with last week's results to show what was fixed, what is new and what keeps coming back.
- Add parsers for ArubaOS-CX and NX-OS, and read the inventory and the changes from the Device42 and ITSM APIs.""",
 es="""

## El problema
Las configuraciones de red se desvían de cambio nocturno en cambio nocturno, y en una empresa con varias salas de comunicaciones nadie lee todas las configuraciones cada semana. En una semana normal un switch de una sede sigue aceptando telnet porque se instaló con una plantilla antigua; dos equipos responden a SNMP con la comunidad public, uno de ellos porque nadie quitó la que trae de fábrica; los switches de una sede apuntan el NTP a un servidor que se apagó, así que sus logs no cuadran con los del resto; un FortiGate tiene la administración por HTTPS y SSH abierta en su interfaz WAN y una política que acepta de all a all con servicio ALL y sin log, que quedó de una migración hace dos meses; un switch de acceso se cambió a las dos de la madrugada sin ticket y el cambio nunca se guardó, así que el próximo corte de luz se lo lleva; dos equipos no tienen ninguna copia y las copias de toda una sede tienen diez días desde que una regla de firewall rompió la tarea de copia; seis puertos sin usar están levantados en la VLAN 1; un router tiene una versión que no está en la lista aprobada; y un switch de acceso lleva cinco años sin soporte del fabricante y sigue en el rack. Cada una de estas cosas se ve en un sitio, la copia, el inventario o el calendario de cambios, y nadie las junta. Las fechas de fin de soporte salen de la misma exportación de Device42 que el planificador del ciclo de vida de equipos que publiqué antes en la serie convierte en un plan de renovación; esta revisión mira lo que está configurado en los equipos.

## Qué he hecho
- Copias: equipos sin copia, copias de más de una semana, configuraciones de Cisco cambiadas después del último guardado, y cambios hechos fuera de un ticket de cambio aprobado.
- Plano de gestión: solo SSH v2, nada de telnet, enable secret y cifrado de contraseñas, AAA con TACACS+ o RADIUS y respaldo local, un banner de acceso, un tiempo de inactividad y el acceso de gestión limitado a la red de gestión.
- Logs y hora, y switching: servidores NTP, servidores de syslog, zona horaria y solo SNMP v3; puertos sin usar apagados en la VLAN de aparcamiento, PortFast y BPDU guard en los puertos de usuario, nada de VLAN nativa 1 en las troncales, ningún puerto de usuario en la VLAN 1 y port security donde la línea base lo pide.
- FortiGate y ciclo de vida: administración en interfaces WAN, políticas any-any que aceptan, políticas sin log, políticas desactivadas que se quedan meses y firmware por debajo de la línea base; versiones no aprobadas para el modelo, fin de soporte, y copias que no cuadran con el inventario.
- Un estado por equipo (conforme, con desviaciones o no conforme), por sede y global, `report.html` con una cuadrícula de equipos por área, `compliance-pack.md` para el comité de cambios con una ventana propuesta y una columna de decisión por hallazgo, CSV con cada regla de cada equipo, copias, ciclo de vida y acciones, y un recolector de solo lectura en PowerShell con Posh-SSH.

## Cómo está hecho
Python solo con la librería estándar. Hay un pequeño parser por plataforma, limitado a lo que leen las reglas: la configuración de Cisco IOS-XE con sus líneas de cabecera `Last configuration change` y `NVRAM config last updated`, la configuración de ArubaOS-Switch con sus bloques de VLAN y rangos de puertos, y los bloques `config`, `edit`, `set` de FortiOS, con los valores por defecto que se dan por supuestos cuando un `show` normal no los muestra. Cada regla da a cada equipo cumple, no cumple o no aplica, así que la evidencia para una auditoría es un CSV; un equipo no es conforme con un fallo crítico y una sede toma el peor estado de sus equipos. Los puertos sin usar son los que no tienen descripción, porque la descripción es el registro de que un puerto está en uso. El recolector solo envía `show running-config` o `show full-configuration` y quita la paginación de su propia sesión; las copias de Oxidized y RANCID sirven tal cual. La demo es una empresa de logística inventada con tres salas de comunicaciones y 34 equipos, revisada el 6 de noviembre con los problemas puestos a propósito: 9 conformes, 17 con desviaciones y 8 no conformes, siete hallazgos críticos para la próxima ventana. 14 tests, un runbook para el ciclo semanal con cómo se convierte cada hallazgo en un cambio y cómo se tratan las excepciones, y un workflow de GitHub Actions que ejecuta los tests y regenera los datos de la demo y la captura. Las comprobaciones del FortiGate son la higiene semanal que acompaña a la revisión de segmentación del laboratorio OT que publiqué antes en la serie.

## Qué aprendí
De operar switches y routers Cisco, salas de comunicaciones y racks en varias sedes, con los proveedores de conectividad, hardware y servicios y las pruebas de DR y BCP; de Device42 para el inventario de las salas de comunicaciones; de Fortinet FortiGate; de los switches HP, MikroTik y TP-Link, y de redes LAN, WAN y wifi en España, Italia y Turquía; de IP/MPLS y QoS, BGP, OSPF y VXLAN; de monitorizar con SolarWinds y Zabbix y automatizar con PowerShell y Python; y de ser responsable del proceso de gestión de cambios y de la CMDB, y de responder auditorías aplicando ISO 27001 y NIS2. Las lecciones que hay detrás de la herramienta son que una copia que nadie comprueba no es una copia; que un cambio que nunca se guardó es un problema que espera al próximo corte de luz; que el calendario de cambios y la configuración tienen que coincidir, y cuando no coinciden la conversación es con el técnico, no sobre el equipo; que los valores de fábrica como SNMP public sobreviven a todas las plantillas; que una política any-any temporal nunca es temporal si nadie le pone fecha; que una descripción en cada puerto usado es lo que hace visibles los puertos sin usar; y que la línea base tiene que ser un documento bajo control de cambios, o cada excepción acaba siendo el nuevo estándar.

## Siguientes pasos
- Ejecutar la recolección cada noche y la revisión cada viernes antes del comité de cambios.
- Comparar con los resultados de la semana anterior para ver qué se ha corregido, qué es nuevo y qué vuelve una y otra vez.
- Añadir parsers para ArubaOS-CX y NX-OS, y leer el inventario y los cambios desde las API de Device42 y de la herramienta de ITSM."""),
dict(n="46", repo="46-problem-management-review", date="2026-11-08", updated="2026-11-11", cat="tools",
 title_en="Forty-six VPN tickets and no problem record: the monthly problem management review",
 title_es="Cuarenta y seis tickets de VPN y ningún problema abierto: la revisión mensual de problemas",
 seo_title_en="Problem management review · Iñigo González",
 seo_title_es="Revisión de gestión de problemas · Iñigo González",
 seo_desc="Monthly problem review from ITSM exports: recurring incidents with no problem, major incidents without RCA, stuck problems, known errors and fixes.",
 seo_desc_es="Revisión mensual de problemas con exportaciones de ITSM: incidencias repetidas sin problema, incidentes graves sin RCA, errores conocidos y soluciones.",
 dek_en="From the incidents and problems exported from Jira Service Management, HaloITSM or EasyVista, the changes linked to them and the CMDB: which recurring incidents should become problems, which major incidents still have no root cause, which open problems are stuck or have no owner, which known errors have lived on a workaround for months, which fixes did not stop the incidents, and the pack for the monthly problem review and the next CAB.",
 dek_es="A partir de las incidencias y los problemas exportados de Jira Service Management, HaloITSM o EasyVista, los cambios vinculados y la CMDB: qué incidencias repetidas deberían convertirse en problemas, qué incidentes graves siguen sin causa raíz, qué problemas abiertos están atascados o sin responsable, qué errores conocidos llevan meses viviendo de una solución temporal, qué soluciones no han parado las incidencias, y el paquete para la revisión mensual de problemas y el próximo CAB.",
 en="""

## The problem
Problem management is the part of ITSM that everyone agrees with and nobody has time for. The service desk resolves the same incident again and again with the same workaround, and each ticket closes inside its SLA, so the dashboard looks fine. In a normal month forty-six incidents about a VPN certificate error have been closed one by one since late August and nobody has opened a problem; seventeen printer driver incidents at one site look like seventeen different tickets; the warehouse system went down for four hours three weeks ago and there is still no problem record, and the transport system outage of the week before has one, under investigation, with no root cause; a known error on the warehouse scanners has had a workaround for 120 days and nobody has raised the change for the fix; a change closed the file share problem in September and eleven more incidents of the same kind have arrived since, most of them not linked to it; three open problems have no owner and two are the same problem; and almost a third of the root causes say Unknown or Other. All of it is in the ITSM tool, one ticket at a time. The major incident kit I published earlier in the series covers the incident itself and its review, and the change calendar review covers what goes to the CAB; this one is the loop between them, from the incident that keeps coming back to the change that should stop it.

## What I built
- Trends: clusters of similar incidents on the same CI and category with no problem record, the candidate problems, ranked by how many there are, their priority and the criticality of the CI in the CMDB.
- Major incidents: no problem record, or a problem with no root cause, five working days after the incident, with weekends and holidays left out.
- Stuck problems: no update for a month, past the target date, under investigation for more than 60 days, no owner, or owned by a team other than the one that owns the CI.
- Known errors and fixes: workarounds older than 90 days with no change for the permanent fix, workarounds the service desk has not got, problems fixed by a change while matching incidents keep arriving, problems closed on a change that was backed out, reopened incidents; and the quality of the records: root causes recorded as unknown or other, problems closed without a root cause, duplicates.
- A status per area, `report.html`, `problem-review-pack.md` with a 60-minute agenda, a decision column and the list for the next CAB, CSVs for candidate problems, problem status, known errors, fix effectiveness and actions, and a read-only PowerShell exporter for the Jira Service Management Cloud REST API.

## How it is built
Python with the standard library only. The grouping of incidents is deliberately simple and explainable: incidents are grouped by CI and category, each summary becomes a set of words without stop words, and two summaries are similar when they share at least two words and half the words of the shorter one; each incident joins the cluster whose common words it shares, in order of creation, so the result is the same every time and the common words say why the incidents were grouped. A candidate is scored by the priority weights of its incidents times the criticality of the CI. Whether a fix worked is checked the same way: the words the problem's incidents had in common before the change, on the same CI, after the implementation date. The exporter only sends GET requests to the search endpoint with JQL and token pagination, with an API token asked for at run time and never stored, and the column names of HaloITSM and EasyVista exports are accepted too. The demo is a made-up logistics company with three sites, six months and 1,572 incidents, 35 problems and 20 changes, reviewed on 8 November with the problems placed on purpose: at risk, two candidate problems, two major incidents without a root cause in time, six stuck problems and one fix that did not work. 14 tests, a runbook with who attends, the cadence, when to open a problem, the RCA techniques and how a problem becomes a change, and a GitHub Actions workflow that runs the tests and rebuilds the demo data and the screenshot.

## What I learned
From being the formal process owner of incident and request, change and problem management, the CMDB and configuration management, with process dashboards and audit responses; from leading the technical response in major incidents and the post-mortems and root cause analysis after them; from tracking the backlog, quality and ageing of tickets and escalations with offshore teams, and defining SLAs and OLAs; from administering Jira Service Management and Confluence, and working with EasyVista, HaloITSM and GLPI; from automating with PowerShell and Python; and from writing runbooks and training others in the processes. The lessons behind the tool are that a workaround that works is the most expensive thing in the service desk, because it hides the problem; that an incident counted as resolved inside its SLA says nothing about whether it will come back; that every major incident needs a problem the same day, because a week later nobody remembers the timeline; that a problem without an owner is a list, not a problem; that a known error accepted for good needs a reason and a review date, or it is just forgotten; that closing a problem when the change is implemented is too early, and the incidents of the following weeks are the real test; and that Unknown is a valid root cause while investigating, never as the way to close.

## Next steps
- Run the export every Monday and the review before each monthly problem review.
- Keep last month's candidates to show which became problems and which keep growing.
- Read the CIs from Assets, add HaloITSM and EasyVista exporters through their APIs, and track the share of incidents linked to a problem month by month.""",
 es="""

## El problema
La gestión de problemas es la parte de ITSM en la que todo el mundo está de acuerdo y para la que nadie tiene tiempo. El service desk resuelve una y otra vez la misma incidencia con la misma solución temporal, cada ticket se cierra dentro de su SLA y el cuadro de mando parece estar bien. En un mes normal se han cerrado una a una cuarenta y seis incidencias por un error de certificado de la VPN desde finales de agosto y nadie ha abierto un problema; diecisiete incidencias de un driver de impresora en una sede parecen diecisiete tickets distintos; el sistema de almacén se cayó cuatro horas hace tres semanas y sigue sin registro de problema, y la caída del sistema de transporte de la semana anterior tiene uno, en investigación y sin causa raíz; un error conocido de los lectores del almacén lleva 120 días con solución temporal y nadie ha pedido el cambio que lo arregle; un cambio cerró en septiembre el problema de la carpeta compartida y desde entonces han llegado once incidencias más del mismo tipo, casi todas sin vincular; tres problemas abiertos no tienen responsable y dos son el mismo problema; y casi un tercio de las causas raíz dicen Desconocida u Otra. Todo está en la herramienta de ITSM, ticket a ticket. El kit de incidentes graves que publiqué antes en la serie cubre el incidente y su revisión, y la revisión del calendario de cambios cubre lo que va al CAB; esta herramienta es el circuito entre ambos, desde la incidencia que vuelve una y otra vez hasta el cambio que debería pararla.

## Qué he hecho
- Tendencias: grupos de incidencias parecidas en el mismo CI y la misma categoría sin registro de problema, los problemas candidatos, ordenados por cuántas son, su prioridad y la criticidad del CI en la CMDB.
- Incidentes graves: sin registro de problema, o con un problema sin causa raíz, cinco días laborables después del incidente, sin contar fines de semana ni festivos.
- Problemas atascados: sin actualizar en un mes, con la fecha objetivo vencida, más de 60 días en investigación, sin responsable, o en manos de un equipo distinto del que es dueño del CI.
- Errores conocidos y soluciones: soluciones temporales de más de 90 días sin cambio para la solución definitiva, soluciones temporales que el service desk no tiene, problemas arreglados con un cambio mientras siguen llegando incidencias iguales, problemas cerrados con un cambio que se deshizo, incidencias reabiertas; y la calidad de los registros: causas raíz desconocidas u otras, problemas cerrados sin causa raíz y duplicados.
- Un estado por área, `report.html`, `problem-review-pack.md` con un orden del día de 60 minutos, una columna de decisión y la lista para el próximo CAB, CSV de problemas candidatos, estado de los problemas, errores conocidos, eficacia de las soluciones y acciones, y un exportador de solo lectura en PowerShell para la API REST de Jira Service Management Cloud.

## Cómo está hecho
Python solo con la librería estándar. La agrupación de incidencias es simple a propósito y se puede explicar: las incidencias se agrupan por CI y categoría, cada resumen se convierte en un conjunto de palabras sin las vacías, y dos resúmenes se parecen cuando comparten al menos dos palabras y la mitad de las palabras del más corto; cada incidencia entra, por orden de creación, en el grupo con cuyas palabras comunes coincide, así que el resultado es siempre el mismo y las palabras comunes explican por qué se agruparon. Cada candidato se puntúa con el peso de la prioridad de sus incidencias por la criticidad del CI. Si una solución funcionó se comprueba igual: las palabras que tenían en común las incidencias del problema antes del cambio, en el mismo CI, después de la fecha de implantación. El exportador solo envía peticiones GET al endpoint de búsqueda con JQL y paginación por token, con un token de API que se pide al ejecutarlo y nunca se guarda, y también acepta los nombres de columna de las exportaciones de HaloITSM y EasyVista. La demo es una empresa de logística inventada con tres sedes, seis meses y 1.572 incidencias, 35 problemas y 20 cambios, revisada el 8 de noviembre con los problemas puestos a propósito: en riesgo, dos problemas candidatos, dos incidentes graves sin causa raíz a tiempo, seis problemas atascados y una solución que no funcionó. 14 tests, un runbook con quién asiste, la cadencia, cuándo abrir un problema, las técnicas de análisis de causa raíz y cómo un problema se convierte en un cambio, y un workflow de GitHub Actions que ejecuta los tests y regenera los datos de la demo y la captura.

## Qué aprendí
De ser responsable formal de los procesos de gestión de incidencias y peticiones, cambios y problemas, de la CMDB y la gestión de la configuración, con cuadros de mando de los procesos y respuestas a auditorías; de dirigir la respuesta técnica en incidentes graves y los post-mortem y análisis de causa raíz posteriores; de seguir el backlog, la calidad y la antigüedad de los tickets y las escalaciones con equipos offshore, y de definir SLA y OLA; de administrar Jira Service Management y Confluence, y de trabajar con EasyVista, HaloITSM y GLPI; de automatizar con PowerShell y Python; y de escribir runbooks y formar a otros en los procesos. Las lecciones que hay detrás de la herramienta son que una solución temporal que funciona es lo más caro del service desk, porque esconde el problema; que una incidencia resuelta dentro de su SLA no dice nada de si va a volver; que cada incidente grave necesita su problema el mismo día, porque una semana después nadie recuerda la cronología; que un problema sin responsable es una lista, no un problema; que un error conocido que se acepta para siempre necesita un motivo y una fecha de revisión, o simplemente se olvida; que cerrar un problema cuando se implanta el cambio es demasiado pronto, y la prueba de verdad son las incidencias de las semanas siguientes; y que Desconocida es una causa raíz válida mientras se investiga, nunca para cerrar.

## Siguientes pasos
- Ejecutar la exportación cada lunes y la revisión antes de cada revisión mensual de problemas.
- Guardar los candidatos del mes anterior para ver cuáles se convirtieron en problemas y cuáles siguen creciendo.
- Leer los CI desde Assets, añadir exportadores para HaloITSM y EasyVista por sus API, y seguir mes a mes el porcentaje de incidencias vinculadas a un problema."""),
dict(n="47", repo="47-multi-site-it-scorecard", date="2026-11-08", cat="tools",
 title_en="A backup circuit down twice and an office without its engineer: the monthly multi-site scorecard",
 title_es="Un circuito de respaldo caído dos veces y una oficina sin técnico: el cuadro de mando IT multisede",
 seo_title_en="Multi-site IT scorecard with RAG · Iñigo González",
 seo_title_es="Cuadro de mando de IT multisede · Iñigo González",
 seo_desc="Monthly IT scorecard per office: SLA, FCR, backlog and ageing, CSAT, availability, Intune compliance, DR tests, RAG, trend and the reason behind every red.",
 seo_desc_es="Cuadro de mando mensual de IT por oficina: SLA, FCR, backlog, CSAT, disponibilidad, cumplimiento en Intune y pruebas de DR, con RAG, tendencia y motivos.",
 dek_en="From the sites, the ITSM tickets, the outage events of monitoring, the Intune device snapshots, the open actions and the DR tests: a RAG status per KPI and office against its target, n/a when there are too few tickets to rate, the trend against the previous month, the reason found in the data behind every red, a weighted score per site, a regional heatmap and the pack for the monthly regional review.",
 dek_es="A partir de las sedes, los tickets del ITSM, las caídas registradas por la monitorización, las fotos mensuales de los equipos en Intune, las acciones abiertas y las pruebas de DR: un estado RAG por indicador y oficina frente a su objetivo, n/a cuando hay demasiados pocos tickets para valorar, la tendencia frente al mes anterior, el motivo que hay en los datos detrás de cada rojo, una puntuación ponderada por sede, un mapa de calor regional y el dosier para la revisión regional de cada mes.",
 en="""

## The problem
A regional IT lead with eight offices gets the same question every month: how is IT doing at each office, which one is slipping and why. The numbers live in five places, and on their own they rarely tell the story. In a normal month the backup circuit of one office is down twice for almost nine hours and nobody notices, because the primary stays up; a fifth of another office's laptops fall out of compliance the week a new Windows 11 build reaches them; the smallest office has eight tickets, and an SLA percentage on eight tickets is green or red by chance; an office loses its only local engineer and the next month first-contact resolution falls from 79% to 56%, escalations to the central team go from 14% to 39% and satisfaction from 4.5 to 3.4; one office has not tested its DR plan for seventeen months; and the busiest office has 91 open tickets, 35 of them older than 30 days. The service desk KPIs I published at the start of the series look at one service desk; this is the same idea across offices side by side, with availability, devices, actions and DR next to the tickets.

## What I built
- Service desk per office: SLA attainment by priority, first-contact resolution, reopen and escalation rates, backlog per 100 users and its ageing, and satisfaction.
- Availability per service (WAN primary and backup, Wi-Fi, printing, meeting rooms, file and print), with only the unplanned minutes held against the target; devices: Intune compliance, stale check-ins and hardware older than four years; overdue actions and how long ago each office tested its DR plan.
- For every KPI a RAG status against its target and red threshold, n/a when the volume is under a minimum, the trend against the previous month and, for every red, the reason found in the data: the provider tickets of the outages, the OS build behind the noncompliant laptops, the oldest tickets, the overdue actions, an office with no local IT staff.
- A weighted score and a status per office, a regional row that never averages one office's outage away, `report.html` with a heatmap of offices by KPI, and `regional-review-pack.md` with one section per office and a decision column.
- CSVs with the scorecard, the detail per KPI, the trend, the findings and the actions, and a read-only PowerShell exporter for Intune through Microsoft Graph and for Jira Service Management through its REST API.

## How it is built
Python with the standard library only. Every KPI is computed per office and month from the raw exports, the same way for the month being reported and for the previous one, so the trend is not a number someone typed. Under its minimum volume a KPI is not rated, and not rated is never shown as green: a small office is scored on what it has, its backlog, availability, devices and DR test, and its few tickets are read one by one. The site score is the weighted share of points over the rated KPIs, a site with a red is never green, and the regional row pools tickets and devices but takes the worst office for availability, actions and DR tests. Availability is computed from the outage events of the monitoring tool, unplanned minutes over the minutes in the month, against a target per service, because a backup circuit and a printer do not deserve the same one. The device KPIs use the last Intune snapshot of each month. The demo is a made-up company with 2,500 people in eight European offices, reporting October against September with the problems placed on purpose: the region amber, two offices red, nine red KPIs and six not rated. 14 tests, a runbook for the monthly cycle with the agenda of the review, what to do with each red, how to set targets and how to keep the KPIs from being gamed, and a GitHub Actions workflow that runs the tests and rebuilds the demo data and the screenshot. When the service comes from a provider, the EUC provider review I published earlier in the series is the monthly look at their SLAs and OLAs.

## What I learned
From leading the IT of one office with two engineers at a multi-site financial services company, supporting around 2,500 users across European offices, in an office that grew from about 15 to over 120 people; from defining and tracking SLAs and OLAs, running availability and capacity management as a formal practice with metrics, trends and plans, building process dashboards and following the backlog, quality and ageing of tickets and escalations with offshore teams; from managing connectivity, hardware and service vendors and supervising DR and BCP tests; from Intune, MECM packaging and a Windows 11 migration; and from Zabbix, SolarWinds, Grafana, ELK, PowerShell, Python and Jira Service Management. The lessons behind the tool are that a percentage on eight tickets is noise and has to say so; that a backup circuit that fails while the primary works is the outage nobody reports and the one that matters on the day the primary fails; that the reason belongs next to the red, or the review spends its time finding it; that a red that is not new deserves a different conversation from a new one; that the same targets for every office keep the discussion on the reasons, not on the thresholds; that an office without a local engineer shows it first in escalations and satisfaction; and that a scorecard is for deciding where to help, not for ranking people.

## Next steps
- Run it on the first working day of every month and keep a year of trend per office.
- Read the outages straight from the Zabbix API and add the OLA of the central team next to the office SLAs.
- Add availability in business hours per time zone and capacity per office from Grafana.""",
 es="""

## El problema
Un responsable de IT regional con ocho oficinas recibe cada mes la misma pregunta: cómo va IT en cada oficina, cuál se está quedando atrás y por qué. Los datos están en cinco sitios y, por separado, rara vez cuentan la historia. En un mes normal el circuito de respaldo de una oficina se cae dos veces durante casi nueve horas y nadie se entera, porque el principal sigue arriba; una quinta parte de los portátiles de otra oficina deja de cumplir la semana en que les llega una nueva versión de Windows 11; la oficina más pequeña tiene ocho tickets, y un porcentaje de SLA sobre ocho tickets sale verde o rojo por azar; una oficina se queda sin su único técnico local y al mes siguiente la resolución en el primer contacto baja del 79% al 56%, los escalados al equipo central pasan del 14% al 39% y la satisfacción de 4,5 a 3,4; una oficina lleva diecisiete meses sin probar su plan de DR; y la oficina con más actividad tiene 91 tickets abiertos, 35 de ellos con más de 30 días. Los indicadores del service desk que publiqué al principio de la serie miran un solo service desk; esto es la misma idea con las oficinas una al lado de otra, y con la disponibilidad, los equipos, las acciones y el DR junto a los tickets.

## Qué he hecho
- Service desk por oficina: cumplimiento de SLA por prioridad, resolución en el primer contacto, tasas de reapertura y de escalado, backlog por cada 100 usuarios y su antigüedad, y satisfacción.
- Disponibilidad por servicio (WAN principal y de respaldo, wifi, impresión, salas de reuniones, ficheros e impresión), contando contra el objetivo solo los minutos no planificados; equipos: cumplimiento en Intune, equipos que no se sincronizan y equipos con más de cuatro años; acciones vencidas y cuánto hace que cada oficina probó su plan de DR.
- Para cada indicador, un estado RAG frente a su objetivo y su umbral rojo, n/a cuando el volumen no llega a un mínimo, la tendencia frente al mes anterior y, en cada rojo, el motivo que hay en los datos: los tickets del proveedor de las caídas, la versión del sistema detrás de los portátiles que no cumplen, los tickets más antiguos, las acciones vencidas, una oficina sin personal de IT local.
- Una puntuación ponderada y un estado por oficina, una fila regional que nunca diluye la caída de una oficina en la media, `report.html` con un mapa de calor de oficinas por indicador, y `regional-review-pack.md` con una sección por oficina y una columna de decisión.
- CSV con el cuadro de mando, el detalle por indicador, la tendencia, los hallazgos y las acciones, y un exportador de solo lectura en PowerShell para Intune a través de Microsoft Graph y para Jira Service Management a través de su API REST.

## Cómo está hecho
Python solo con la librería estándar. Cada indicador se calcula por oficina y mes a partir de las exportaciones en bruto, igual para el mes del informe que para el anterior, así que la tendencia no es un número que alguien ha tecleado. Por debajo de su volumen mínimo un indicador no se valora, y lo que no se valora nunca aparece en verde: una oficina pequeña se puntúa por lo que tiene, su backlog, la disponibilidad, los equipos y la prueba de DR, y sus pocos tickets se leen uno a uno. La puntuación de la sede es la parte ponderada de puntos sobre los indicadores valorados, una sede con un rojo nunca está en verde, y la fila regional junta los tickets y los equipos pero toma la peor oficina en disponibilidad, acciones y pruebas de DR. La disponibilidad sale de los eventos de caída de la herramienta de monitorización, minutos no planificados sobre los minutos del mes, frente a un objetivo por servicio, porque un circuito de respaldo y una impresora no merecen el mismo. Los indicadores de equipos usan la última foto de Intune de cada mes. La demo es una empresa inventada con 2.500 personas en ocho oficinas europeas, que informa de octubre frente a septiembre con los problemas puestos a propósito: la región en ámbar, dos oficinas en rojo, nueve indicadores en rojo y seis sin valorar. 14 tests, un runbook para el ciclo mensual con el orden del día de la revisión, qué hacer con cada rojo, cómo fijar los objetivos y cómo evitar que se maquillen los indicadores, y un workflow de GitHub Actions que ejecuta los tests y regenera los datos de la demo y la captura. Cuando el servicio lo presta un proveedor, la revisión del proveedor de EUC que publiqué antes en la serie es la mirada mensual a sus SLA y OLA.

## Qué aprendí
De dirigir la IT de una oficina con dos técnicos en una empresa de servicios financieros con varias sedes, dando soporte a unos 2.500 usuarios en oficinas europeas, en una oficina que pasó de unas 15 a más de 120 personas; de definir y seguir SLA y OLA, de llevar la gestión de la disponibilidad y la capacidad como una práctica formal con métricas, tendencias y planes, de montar cuadros de mando de procesos y de seguir el backlog, la calidad y la antigüedad de los tickets y los escalados con equipos offshore; de gestionar proveedores de conectividad, hardware y servicios y supervisar pruebas de DR y BCP; de Intune, el empaquetado con MECM y una migración a Windows 11; y de Zabbix, SolarWinds, Grafana, ELK, PowerShell, Python y Jira Service Management. Las lecciones que hay detrás de la herramienta son que un porcentaje sobre ocho tickets es ruido y tiene que decirlo; que un circuito de respaldo que falla mientras el principal funciona es la caída que nadie reporta y la que importa el día que cae el principal; que el motivo tiene que estar al lado del rojo, o la revisión se pasa el rato buscándolo; que un rojo que no es nuevo merece otra conversación que uno nuevo; que los mismos objetivos para todas las oficinas mantienen la discusión en los motivos y no en los umbrales; que una oficina sin técnico local lo enseña primero en los escalados y en la satisfacción; y que un cuadro de mando sirve para decidir dónde ayudar, no para clasificar a las personas.

## Siguientes pasos
- Ejecutarlo el primer día laborable de cada mes y guardar un año de tendencia por oficina.
- Leer las caídas directamente de la API de Zabbix y añadir el OLA del equipo central junto a los SLA de las oficinas.
- Añadir la disponibilidad en horario laboral por zona horaria y la capacidad por oficina desde Grafana."""),
dict(n="48", repo="48-new-starter-day-one-readiness", date="2026-11-09", cat="tools",
 title_en="A request on Friday for Tuesday and an admin group from a model user: the day-one readiness check",
 title_es="Una petición el viernes para el martes y un grupo de admin heredado: el control del primer día",
 seo_title_en="New starter day-one readiness check · Iñigo González",
 seo_title_es="Altas: listos para el primer día · Iñigo González",
 seo_desc="Day-one readiness for new starters: account, licence, groups, access, laptop, phone and MFA per joiner, with owners, due dates and a countdown.",
 seo_desc_es="Preparación del primer día de cada alta: cuenta, licencia, grupos, accesos, portátil, móvil y MFA, con responsables, fechas y cuenta atrás.",
 dek_en="From the HR joiner list, the role profiles, the Entra ID accounts, the Intune or Jamf devices, the licences, the stock per site and the access requests: for everyone starting in the next ten working days, whether they will have a working account, licence, groups, access, laptop and phone on day one, what is missing, who owns it and by when, with a countdown in working days and the pack for the weekly joiners call.",
 dek_es="A partir de la lista de altas de RR. HH., los perfiles por puesto, las cuentas de Entra ID, los equipos de Intune o Jamf, las licencias, el stock de cada sede y las peticiones de acceso: para todos los que empiezan en los próximos diez días laborables, si tendrán cuenta, licencia, grupos, accesos, portátil y móvil el primer día, qué falta, de quién depende y para cuándo, con una cuenta atrás en días laborables y el dosier para la reunión semanal de altas.",
 en="""

## The problem
Day one is the first impression IT makes on a new starter, and it is decided in the two weeks before. The information is spread out: HR knows the start dates, Entra ID knows the accounts, Intune knows the laptops, the asset register knows the stock and the ITSM tool knows the access requests, and nobody looks at all of them together until the joiner is at the desk. In a normal fortnight with twenty-five joiners, a warehouse operative's request arrives on Friday for Tuesday and on Monday his role group and his access to the warehouse system are still missing; the laptop of someone starting tomorrow is enrolled but not compliant because BitLocker is still pending; a MacBook was requested in an office with none in stock and an order takes longer than the days left; an account created by copying a colleague who used to work in IT comes with an Exchange administrators group; another account has no usage location, so the licence was never assigned; a rehire's old account is disabled and someone created a second one with the same employee ID; a trader starting next Monday has no approval yet for the market data terminal; and the licence pool has two free units for five joiners. The monthly access review I published earlier in the series finds the admin group three months later; this check is meant to stop it on day one.

## What I built
- Request and account: requests raised too late for the lead time; accounts missing or disabled; a rehire whose old account should be reused, or a duplicate created next to it; no employee ID, department or manager different from HR, no usage location, a cloud-only account in a hybrid directory.
- Licence, groups and access: the licence of the role missing, wrong or extra, and the pool against everyone still to licence in start date order; role groups and distribution lists missing; privileged groups the role should not have; apps and shared mailboxes not requested, waiting for approval, approved and not provisioned, or rejected.
- Device, phone and MFA: no laptop assigned, no stock of the requested model at the site, the wrong platform, enrolled but not compliant; a role that needs a phone with none requested; and how the joiner will register MFA, with a Temporary Access Pass for the first sign-in.
- Every gap with an owner, the working days its fix needs and a due date; each joiner READY, AT RISK or BLOCKED with a countdown in working days, per site and overall.
- `report.html` with the fix-first list and a countdown board, `day-one-pack.md` for the weekly joiners call with owner, due date and done columns, CSVs for joiner status, gaps, licence and device forecasts, actions and findings, and a read-only PowerShell exporter for Microsoft Graph.

## How it is built
Python with the standard library only. Each joiner is matched to an account by employee ID, then by the planned UPN, then by name, and compared with the profile of their role: a JSON file with the groups, licence, apps, shared mailboxes, lists and whether the role needs a phone, with the site as a placeholder in the group names. Every fix has the working days it needs, from one for a group to five for a device order, and a gap that stops day one becomes a blocker when its fix no longer fits before the start or the start is within three working days; otherwise it is a risk with a due date. The licence pool and the device stock are shared out in start date order, so the forecast says who will be short, not only by how many. A privileged group that the role does not list is a blocker at any distance from the start. The exporter reads the accounts with employeeId, usage location and licences, the manager, the group memberships, the authentication methods, the subscribed licences and the Intune devices with read-only scopes and an interactive sign-in, and Jamf Pro inventory exports with the same columns are accepted; Windows Autopilot registrations can be read as data too. The demo is a made-up trading and distribution company with four sites and 25 joiners in the next two weeks, checked on Monday 9 November with the problems placed on purpose: blocked overall, 13 ready, 8 at risk and 4 blocked. 15 tests, a runbook for the weekly joiners call with who attends, the cadence, what ready means, model users, rehires and late requests, and a GitHub Actions workflow that runs the tests and rebuilds the demo data and the screenshot. When the joiner is already in, the Entra ID hygiene audit from the start of the series covers MFA gaps and forgotten accounts.

## What I learned
From running user onboarding for retail stores and head office, with network, e-mail, business applications and legacy system accounts, and assigning Office 365 licences with the service desk; from Active Directory and Azure AD Connect, Entra ID with Conditional Access and PIM, Exchange Online and shared mailboxes and SharePoint; from Intune for Windows, macOS, iOS and Android, Jamf Pro for Macs, managed iPhones, iPads and MacBooks, and BitLocker; from automating with PowerShell, including Microsoft Graph, and Python, and working with Jira Service Management; and from being the IT site leader of an office that grew from about 15 to over 120 people, supporting around 2,500 users across European offices. The lessons behind the tool are that the start date is the only deadline that cannot move, so every fix has to be counted backwards from it in working days; that copying a model user is fast and brings the colleague's history with it, so the role profile has to be the reference; that a rehire is an account to reuse, not to create; that a licence pool or a stock count only means something against everyone starting, in order; that a late request is a conversation with HR, not a heroic weekend; that the first sign-in needs a plan as much as the laptop does; and that ready has to mean the same thing for every joiner, written down.

## Next steps
- Run it every Monday before the joiners call, and daily for the joiners in the urgent window.
- Read the joiners from the HR system or the ITSM joiner requests, and the access approvals from Jira Service Management.
- Keep the gaps of every week to see which roles and steps keep failing and feed them back into the role profiles.""",
 es="""

## El problema
El primer día es la primera impresión que IT da a una persona nueva, y se decide en las dos semanas anteriores. La información está repartida: RR. HH. sabe las fechas de incorporación, Entra ID sabe las cuentas, Intune sabe los portátiles, el inventario sabe el stock y la herramienta de ITSM sabe las peticiones de acceso, y nadie lo mira todo junto hasta que la persona está sentada en su puesto. En una quincena normal con veinticinco altas, la petición de un operario de almacén llega el viernes para el martes y el lunes todavía le faltan el grupo de su puesto y el acceso al sistema de almacén; el portátil de alguien que empieza mañana está inscrito pero no cumple porque BitLocker sigue pendiente; se pidió un MacBook en una oficina sin ninguno en stock y un pedido tarda más que los días que quedan; una cuenta creada copiando a un compañero que antes trabajaba en IT llega con un grupo de administradores de Exchange; otra cuenta no tiene ubicación de uso, así que la licencia nunca se asignó; la cuenta antigua de una recontratación está deshabilitada y alguien creó una segunda con el mismo número de empleado; un trader que empieza el lunes que viene todavía no tiene aprobado el terminal de datos de mercado; y en la bolsa de licencias quedan dos libres para cinco altas. La revisión mensual de accesos que publiqué antes en la serie encuentra el grupo de administradores tres meses después; este control está pensado para pararlo el primer día.

## Qué he hecho
- Petición y cuenta: peticiones que llegan tarde para el plazo; cuentas que faltan o están deshabilitadas; una recontratación cuya cuenta antigua habría que reutilizar, o un duplicado creado al lado; sin número de empleado, con un departamento o un responsable distintos de los de RR. HH., sin ubicación de uso, o una cuenta solo en la nube en un directorio híbrido.
- Licencia, grupos y accesos: la licencia del puesto que falta, es otra o sobra, y la bolsa de licencias frente a todos los que faltan por licenciar, por orden de incorporación; grupos del puesto y listas de distribución que faltan; grupos privilegiados que el puesto no debería tener; aplicaciones y buzones compartidos sin pedir, pendientes de aprobación, aprobados pero sin dar de alta, o rechazados.
- Equipo, móvil y MFA: sin portátil asignado, sin stock del modelo pedido en la sede, la plataforma equivocada, inscrito pero sin cumplir; un puesto que necesita móvil sin ninguno pedido; y cómo registrará la persona el MFA, con un pase de acceso temporal para el primer inicio de sesión.
- Cada hueco con su responsable, los días laborables que necesita su solución y una fecha límite; cada alta LISTA, EN RIESGO o BLOQUEADA, con una cuenta atrás en días laborables, por sede y en total.
- `report.html` con la lista de lo que hay que arreglar primero y un tablero con la cuenta atrás, `day-one-pack.md` para la reunión semanal de altas con columnas de responsable, fecha y hecho, CSV con el estado de cada alta, los huecos, la previsión de licencias y de equipos, las acciones y los hallazgos, y un exportador de solo lectura en PowerShell para Microsoft Graph.

## Cómo está hecho
Python solo con la librería estándar. Cada alta se cruza con una cuenta por número de empleado, después por el UPN previsto y después por el nombre, y se compara con el perfil de su puesto: un JSON con los grupos, la licencia, las aplicaciones, los buzones compartidos, las listas y si el puesto necesita móvil, con la sede como variable en los nombres de los grupos. Cada solución tiene los días laborables que necesita, desde uno para un grupo hasta cinco para pedir un equipo, y un hueco que impide el primer día pasa a bloqueo cuando su solución ya no cabe antes de la incorporación o cuando la persona empieza en tres días laborables o menos; si no, es un riesgo con fecha límite. La bolsa de licencias y el stock de equipos se reparten por orden de incorporación, así que la previsión dice a quién le va a faltar, no solo cuántos faltan. Un grupo privilegiado que el puesto no incluye es un bloqueo, quede el tiempo que quede. El exportador lee las cuentas con el número de empleado, la ubicación de uso y las licencias, el responsable, la pertenencia a grupos, los métodos de autenticación, las licencias contratadas y los equipos de Intune, con permisos de solo lectura e inicio de sesión interactivo, y acepta exportaciones del inventario de Jamf Pro con las mismas columnas; los registros de Windows Autopilot también se pueden leer como datos. La demo es una empresa inventada de distribución y trading con cuatro sedes y 25 altas en las próximas dos semanas, revisada el lunes 9 de noviembre con los problemas puestos a propósito: bloqueado en total, 13 altas listas, 8 en riesgo y 4 bloqueadas. 15 tests, un runbook para la reunión semanal de altas con quién asiste, la cadencia, qué significa estar listo, los usuarios modelo, las recontrataciones y las peticiones tardías, y un workflow de GitHub Actions que ejecuta los tests y regenera los datos de la demo y la captura. Cuando la persona ya está dentro, la auditoría de higiene de Entra ID del principio de la serie cubre los huecos de MFA y las cuentas olvidadas.

## Qué aprendí
De llevar las altas de usuarios en tiendas y oficina central, con la red, el correo, las aplicaciones de negocio y las cuentas de sistemas heredados, y de asignar licencias de Office 365 con el service desk; de Active Directory y Azure AD Connect, Entra ID con acceso condicional y PIM, Exchange Online y los buzones compartidos y SharePoint; de Intune para Windows, macOS, iOS y Android, Jamf Pro para los Mac, iPhone, iPad y MacBook gestionados, y BitLocker; de automatizar con PowerShell, también con Microsoft Graph, y con Python, y de trabajar con Jira Service Management; y de ser el responsable de IT de una oficina que pasó de unas 15 a más de 120 personas, dando soporte a unos 2.500 usuarios en oficinas europeas. Las lecciones que hay detrás de la herramienta son que la fecha de incorporación es el único plazo que no se mueve, así que cada solución hay que contarla hacia atrás desde ella en días laborables; que copiar a un usuario modelo es rápido y trae consigo la historia del compañero, así que la referencia tiene que ser el perfil del puesto; que una recontratación es una cuenta que se reutiliza, no una que se crea; que una bolsa de licencias o un recuento de stock solo dicen algo frente a todos los que empiezan, y en orden; que una petición tardía es una conversación con RR. HH., no un fin de semana heroico; que el primer inicio de sesión necesita un plan tanto como el portátil; y que estar listo tiene que significar lo mismo para todas las altas, y estar escrito.

## Siguientes pasos
- Ejecutarlo cada lunes antes de la reunión de altas, y a diario para las altas dentro de la ventana urgente.
- Leer las altas del sistema de RR. HH. o de las peticiones de alta del ITSM, y las aprobaciones de acceso de Jira Service Management.
- Guardar los huecos de cada semana para ver qué puestos y qué pasos fallan una y otra vez, y llevarlo a los perfiles de cada puesto."""),
dict(n="49", repo="49-it-project-portfolio-health", date="2026-11-10", cat="tools",
 title_en="GREEN at a CPI of 0.78 and an architect at 180 %: the portfolio health check before the SteerCo",
 title_es="En verde con un CPI de 0,78 y un arquitecto al 180 %: la salud de la cartera antes del comité",
 seo_title_en="IT project portfolio health check · Iñigo González",
 seo_title_es="Salud de la cartera de proyectos IT · Iñigo González",
 seo_desc="IT portfolio health before the SteerCo: computed RAG per project with the reason, watermelon projects, CPI and SPI, people, freezes and decisions needed.",
 seo_desc_es="Salud de la cartera de IT antes del comité: RAG calculado por proyecto y su motivo, proyectos sandía, CPI y SPI, personas, congelaciones y decisiones.",
 dek_en="From the project list of the PPM tool, the milestones, the RAID log, the resource plan, the releases and the sprint history from Jira or Azure DevOps: which projects are healthy, which are drifting and which need a decision at the next steering committee, with a computed GREEN, AMBER or RED and the reason next to the RAG the PM reported, per programme and overall, the portfolio forecast against the approved envelope, and a one-page pack with the decisions, their options and their impact.",
 dek_es="A partir de la lista de proyectos de la herramienta de PPM, los hitos, el registro RAID, el plan de recursos, las entregas y el histórico de sprints de Jira o Azure DevOps: qué proyectos van bien, cuáles se están desviando y cuáles necesitan una decisión en el próximo comité de seguimiento, con un VERDE, ÁMBAR o ROJO calculado y su motivo al lado del que puso el jefe de proyecto, por programa y en total, la previsión de la cartera frente al presupuesto aprobado, y un dosier de una página con las decisiones, sus opciones y su impacto.",
 en="""

## The problem
The monthly steering committee pack is usually a set of slides where each project manager fills in their own RAG, and the committee spends the hour on status instead of decisions. The data that would tell a different story exists, spread across the PPM tool, the RAID logs, the resource plan, the change records and Jira or Azure DevOps, and nobody puts it together before the meeting. In a normal month with eighteen projects, a document capture project is reported GREEN while each euro spent buys 78 cents of the planned work and its build milestone is six weeks late; the Windows 11 rollout has not updated its status in five weeks; a network cutover is planned in the middle of the year-end change freeze; the go-live of another project is on Friday with its change still waiting for the CAB; the enterprise architect is planned at 180 % across three critical projects, so the three will slip together; an automation project counts a yearly benefit nobody in the business owns; a low-priority intranet redesign is three months late and a quarter over budget and nobody has asked whether it should go on; an agile portal keeps adding scope while its velocity falls; three RAID items are past their date with no owner; and the sum of the forecasts is 6 % over the envelope that was approved. The change calendar review I published earlier in the series looks at the go-lives from the operations side; this check looks at them from the portfolio.

## What I built
- Schedule and cost: the forecast end against the plan, milestones late or with no forecast, gates passed without approval; a simple version of earned value, with CPI and SPI from the % complete and the budget, the forecast at completion over budget, a reported forecast below what the CPI points to, and spending faster than time.
- Status hygiene: status not updated for weeks, "watermelon" projects that are GREEN outside and RED inside, and RAID items overdue or with no owner.
- Agile, people and delivery: velocity falling sprint after sprint and scope growing faster than it is delivered; people over 100 % across projects, one key person on several critical projects and roles nobody fills; releases inside a change freeze and changes not approved a few days before the go-live.
- Value and the portfolio: a benefit with no owner, low-priority RED projects as candidates to pause or stop, and the portfolio forecast against the approved envelope.
- A computed RAG per project with the reason, next to the one the PM reported, per programme and overall, and the decisions the committee has to take, each with options (continue, re-plan, pause or stop), a proposal, the impact and an owner.
- `report.html` with a heat map of the portfolio, a card per project, the cost and schedule scatter and the resource load; `steerco-pack.md`, one page for the committee; CSVs for project health, findings, resource load, decisions and actions; and a read-only exporter for the sprint history in Jira Cloud and Azure DevOps.

## How it is built
Python with the standard library only. Each check has its thresholds in a settings file agreed with the committee, and every finding has a severity, an owner and a due date. The earned value is kept simple on purpose: the work done is worth the budget times the % complete, or story points done over total for agile projects; the work planned by today is the budget times the share of the planned time elapsed, on a straight line. CPI and SPI come from those two numbers, and the budget divided by the CPI says where the cost lands if the rest of the work costs what the work so far did. The project RAG is the worst finding per dimension, except that an over-allocated person counts as amber for each project, because it is a portfolio problem; a programme is red when a critical project is red or a third of its projects are. The decisions are built from the findings: the gap to the envelope first, then the pause and stop candidates, the watermelons, the other red projects, the key people, the releases in a freeze and the benefits with no owner. The exporter reads the closed sprints of a Jira board and their issues through the current issue search, or the past iterations of an Azure DevOps team and their work items through a WIQL query, with a token that stays in memory, and writes points committed, completed and added per sprint. The demo is a made-up insurer with three programmes and eighteen waterfall, agile and SAFe projects, checked on 10 November a week before the committee, with the problems placed on purpose: red overall, 5 projects red, 6 amber and 7 green, one watermelon and 8 decisions. 14 tests, a runbook for the monthly committee with what to send before it, the agenda, how to frame the decisions, how to handle watermelon projects without blame and how to follow up the actions, and a GitHub Actions workflow that runs the tests and rebuilds the demo data and the screenshot. The problem management review from earlier in the series is where many of the next projects start.

## What I learned
From managing a portfolio of initiatives; from working with Agile and Scrum, acting as Scrum Master and Product Owner, with SAFe and PI Planning, and with Kanban and visual management; from assessing the technical feasibility of requests and projects, estimating cost, resources and timelines, and writing business cases with ROI and measurable benefits; from workshops with the business, functional requirements, user stories and acceptance criteria; from release management, the change advisory board and go-live and service acceptance reviews; from preparing and tracking the IT budget and negotiating vendor contracts; from process dashboards and KPIs as process owner for incident, change and problem; and from Jira, Confluence, Jira Service Management, Azure DevOps, Python and PowerShell. The lessons behind the tool are that a RAG someone types in and a RAG computed from the numbers should always be shown side by side, because the difference is the conversation; that a watermelon project is usually optimism or fear of red rather than dishonesty, so the reset has to come without blame; that the committee's time belongs to decisions, and a decision needs options and their cost written down before the meeting; that stopping a low-priority project that is red is a good outcome, not a failure; that one person at 180 % is three late projects; that a benefit without an owner is a benefit nobody will collect; and that the thresholds have to stay the same from month to month, or the trend means nothing.

## Next steps
- Run it a week before every steering committee, and weekly for the red projects.
- Read the projects and milestones straight from the PPM tool's API, and keep the computed RAG of every month to see how early each red was visible.
- Add the PI objectives of each Agile Release Train, planned against achieved business value, as one more agile check.""",
 es="""

## El problema
El dosier mensual del comité de seguimiento suele ser un puñado de diapositivas en las que cada jefe de proyecto pone su propio semáforo, y el comité se pasa la hora con el estado en lugar de con las decisiones. Los datos que contarían otra historia existen, repartidos entre la herramienta de PPM, los registros RAID, el plan de recursos, los cambios y Jira o Azure DevOps, y nadie los junta antes de la reunión. En un mes normal con dieciocho proyectos, un proyecto de captura de documentos se reporta en verde mientras cada euro gastado compra 78 céntimos del trabajo previsto y su hito de construcción va seis semanas tarde; el despliegue de Windows 11 lleva cinco semanas sin actualizar su estado; un corte de red está planificado en plena congelación de cambios de fin de año; la puesta en producción de otro proyecto es el viernes y su cambio sigue esperando al CAB; el arquitecto empresarial está planificado al 180 % entre tres proyectos críticos, así que los tres se retrasarán a la vez; un proyecto de automatización cuenta con un beneficio anual que nadie del negocio tiene a su cargo; el rediseño de la intranet, de prioridad baja, va tres meses tarde y un cuarto por encima del presupuesto y nadie ha preguntado si debe seguir; un portal ágil no deja de añadir alcance mientras su velocidad cae; tres elementos del RAID están vencidos y sin responsable; y la suma de las previsiones supera en un 6 % el presupuesto aprobado. La revisión del calendario de cambios que publiqué antes en la serie mira las puestas en producción desde operaciones; este control las mira desde la cartera.

## Qué he hecho
- Plazo y coste: la fecha de fin prevista frente al plan, hitos que van tarde o sin previsión, puertas de fase superadas sin una aprobación registrada; una versión sencilla del valor ganado, con CPI y SPI a partir del % completado y el presupuesto, la previsión al cierre por encima del presupuesto, una previsión declarada por debajo de lo que indica el CPI, y un gasto que va más rápido que el tiempo.
- Higiene del estado: estados sin actualizar desde hace semanas, proyectos "sandía", verdes por fuera y rojos por dentro, y elementos del RAID vencidos o sin responsable.
- Ágil, personas y entregas: una velocidad que cae sprint tras sprint y un alcance que crece más rápido de lo que se entrega; personas por encima del 100 % entre varios proyectos, una persona clave en varios proyectos críticos y puestos sin cubrir; entregas dentro de una congelación de cambios y cambios sin aprobar a pocos días de la puesta en producción.
- Valor y cartera: un beneficio sin responsable, proyectos en rojo y de prioridad baja como candidatos a pausar o parar, y la previsión de la cartera frente al presupuesto aprobado.
- Un semáforo calculado por proyecto con su motivo, al lado del que puso el jefe de proyecto, por programa y en total, y las decisiones que tiene que tomar el comité, cada una con sus opciones (seguir, replanificar, pausar o parar), una propuesta, el impacto y un responsable.
- `report.html` con un mapa de calor de la cartera, una ficha por proyecto, el gráfico de coste y plazo y la carga de recursos; `steerco-pack.md`, una página para el comité; CSV con la salud de cada proyecto, los hallazgos, la carga de recursos, las decisiones y las acciones; y un exportador de solo lectura del histórico de sprints de Jira Cloud y Azure DevOps.

## Cómo está hecho
Python solo con la librería estándar. Cada control tiene sus umbrales en un fichero de configuración pactado con el comité, y cada hallazgo tiene una gravedad, un responsable y una fecha. El valor ganado se mantiene sencillo a propósito: el trabajo hecho vale el presupuesto por el % completado, o los puntos de historia hechos sobre el total en los proyectos ágiles; el trabajo previsto a día de hoy es el presupuesto por la parte del plazo previsto que ya ha pasado, en línea recta. El CPI y el SPI salen de esos dos números, y el presupuesto dividido por el CPI dice dónde acaba el coste si lo que queda cuesta lo mismo que lo hecho. El semáforo del proyecto es el peor hallazgo por dimensión, salvo que una persona sobreasignada cuenta como ámbar para cada proyecto, porque es un problema de la cartera; un programa está en rojo cuando lo está un proyecto crítico o un tercio de sus proyectos. Las decisiones salen de los hallazgos: primero la diferencia con el presupuesto aprobado, después los candidatos a pausar o parar, los proyectos sandía, el resto de proyectos en rojo, las personas clave, las entregas dentro de una congelación y los beneficios sin responsable. El exportador lee los sprints cerrados de un tablero de Jira y sus incidencias con la búsqueda de incidencias actual, o las iteraciones pasadas de un equipo de Azure DevOps y sus elementos de trabajo con una consulta WIQL, con un token que se queda en memoria, y escribe los puntos comprometidos, completados y añadidos en cada sprint. La demo es una aseguradora inventada con tres programas y dieciocho proyectos en cascada, ágiles y SAFe, revisada el 10 de noviembre, una semana antes del comité, con los problemas puestos a propósito: rojo en total, 5 proyectos en rojo, 6 en ámbar y 7 en verde, un proyecto sandía y 8 decisiones. 14 tests, un runbook para el comité mensual con qué enviar antes, el orden del día, cómo plantear las decisiones, cómo tratar los proyectos sandía sin buscar culpables y cómo seguir las acciones, y un workflow de GitHub Actions que ejecuta los tests y regenera los datos de la demo y la captura. La revisión de gestión de problemas de antes en la serie es donde empiezan muchos de los próximos proyectos.

## Qué aprendí
De gestionar una cartera de iniciativas; de trabajar con Agile y Scrum, como Scrum Master y como Product Owner, con SAFe y el PI Planning, y con Kanban y la gestión visual; de evaluar la viabilidad técnica de peticiones y proyectos, estimar costes, recursos y plazos, y redactar casos de negocio con ROI y beneficios medibles; de los talleres con el negocio, los requisitos funcionales, las historias de usuario y los criterios de aceptación; de la gestión de entregas, el comité de cambios y las revisiones de puesta en producción y aceptación del servicio; de preparar y seguir el presupuesto de IT y negociar contratos con proveedores; de los cuadros de mando y los KPI de proceso como responsable de los procesos de incidencias, cambios y problemas; y de Jira, Confluence, Jira Service Management, Azure DevOps, Python y PowerShell. Las lecciones que hay detrás de la herramienta son que el semáforo que alguien escribe y el que sale de los números hay que enseñarlos siempre juntos, porque la diferencia es la conversación; que un proyecto sandía suele ser optimismo o miedo al rojo más que falta de honestidad, así que el cambio a rojo tiene que llegar sin buscar culpables; que el tiempo del comité es para decidir, y una decisión necesita las opciones y su coste por escrito antes de la reunión; que parar un proyecto en rojo y de prioridad baja es un buen resultado, no un fracaso; que una persona al 180 % son tres proyectos que llegan tarde; que un beneficio sin responsable es un beneficio que nadie va a cobrar; y que los umbrales tienen que ser los mismos de un mes a otro, o la tendencia no significa nada.

## Siguientes pasos
- Ejecutarlo una semana antes de cada comité de seguimiento, y cada semana para los proyectos en rojo.
- Leer los proyectos y los hitos directamente de la API de la herramienta de PPM, y guardar el semáforo calculado de cada mes para ver con cuánta antelación se veía cada rojo.
- Añadir los objetivos de PI de cada Agile Release Train, el valor de negocio previsto frente al conseguido, como un control ágil más."""),
dict(n="50", repo="50-saas-licence-spend-review", date="2026-11-11", cat="tools",
 title_en="180 E5 licences used as E3 and a notice deadline in 9 days: the SaaS and licence spend review",
 title_es="180 licencias E5 que se usan como E3 y un preaviso en 9 días: la revisión del gasto en SaaS",
 seo_title_en="SaaS and licence spend review · Iñigo González",
 seo_title_es="Revisión del gasto en SaaS y licencias · Iñigo González",
 seo_desc="SaaS and licence spend review: unused and leaver licences, E5 to E3, shelfware, notice deadlines, uplifts, overlap, shadow IT and savings per action.",
 seo_desc_es="Revisión del gasto en SaaS y licencias: licencias sin uso o de bajas, E5 a E3, asientos sobrantes, preavisos, subidas, solapes, shadow IT y ahorro por acción.",
 dek_en="From the licence and SaaS register, the licence assignments with each user's last activity, the HR or Entra ID user list and the card expenses: what the company pays for, what is actually used, what renews soon and how much can be saved before each notice deadline, with the saving of every action (reclaim, downgrade, right-size, negotiate, consolidate or cancel), the renewal calendar, showback per department and a one-page pack for the IT manager and finance.",
 dek_es="A partir del registro de licencias y SaaS, las licencias asignadas con la última actividad de cada usuario, la lista de usuarios de RR. HH. o de Entra ID y los gastos con tarjeta: qué se paga, qué se usa de verdad, qué se renueva pronto y cuánto se puede ahorrar antes de cada fecha de preaviso, con el ahorro de cada acción (recuperar, bajar de plan, ajustar asientos, negociar, consolidar o cancelar), el calendario de renovaciones, el reparto del coste por departamento y un dosier de una página para el responsable de IT y finanzas.",
 en="""

## The problem
Software and SaaS spend grows one reasonable request at a time, and licences are almost never taken back. The data to see where the money goes exists, in the register, the admin consoles, Entra ID, HR and the expense tool, but nobody reads it together until a renewal arrives, and by then the notice deadline has often passed. In a normal month in a company of 1,400 people, 180 people have Microsoft 365 E5 and use nothing E3 does not already give them; 46 licences are still assigned to people who left months ago, which is a cost and an open door; a third of the Adobe Creative Cloud licences have not been opened for three months; the company pays for Zoom and Webex while everyone has Teams, and for Dropbox and Box next to OneDrive; the e-signature contract renews automatically with a third of its seats unassigned and nine days left to give notice; the CRM comes back with a 9 % uplift against a 5 % cap; the whiteboard tool has more people than seats, and the true-up will come at list price; nobody owns one contract that holds confidential data without single sign-on; and people pay for Canva, Notion, ChatGPT Plus, Calendly and Grammarly on their cards. The vendor contract tracker I published earlier in the series keeps every IT contract and its notice deadline, and the Azure cost review does this job for the cloud bill; this review does it for licences and SaaS, from the usage.

## What I built
- Usage: licences unused for 60 days or never used, licences still assigned to leavers, licences of people on long leave or of accounts HR does not know, and premium tiers for people who do not use the premium features, with the price difference as the saving.
- Seats: shelfware, seats bought and not assigned, and over-assignment, more people than seats, as a true-up risk.
- Renewals: auto-renewing contracts whose notice deadline is close or has passed, uplifts above the agreed cap, contracts with no owner, and a renewal calendar for the next twelve months.
- Portfolio and shadow IT: several apps for the same capability, or a capability the suite already covers, as consolidation candidates; apps without SSO that hold confidential data; SaaS bought on expenses that is not in the register, and card purchases of an app that is already under a central contract.
- Cost allocation: showback per department and cost centre, contracts with no or an unknown cost centre, and spend against budget.
- Every saving tied to an action, reclaim, downgrade, right-size, negotiate, consolidate or cancel, with the users behind it, an owner and a due date; `report.html` with utilisation bars per app, the calendar and the showback; `review-pack.md`, one page with the decisions before the renewals; CSVs for utilisation, the reclaim list, the calendar, showback, findings and actions; and a read-only exporter for the Microsoft 365 licences through Microsoft Graph.

## How it is built
Python with the standard library only. The thresholds are in a settings file agreed with finance, and each finding has a severity, an owner and a due date. Every euro is counted once: the savings are applied per app in a fixed order, reclaim, downgrade, right-size, negotiate, cancel duplicates and then consolidate, and capped at what the app costs, so exiting a video tool only counts what is left of its cost after its inactive licences and empty seats. The notice deadline is the renewal date minus the notice period, and an auto-renewing contract with a past renewal date rolls forward a year at a time. The showback charges each per-user licence to the department of the person who holds it and leaves the empty seats and the flat contracts with IT, so the rows add up to the total. The exporter reads the SKUs the tenant has bought with their seats and the users with their licences and their last successful sign-in from Microsoft Graph, with an app registration and a secret that stays in memory; the last sign-in shows that the account is in use, not that a particular app is, so the reclaim list goes to the app owner before anything is removed. The demo is a made-up distribution company with 1,370 employees in four countries and 24 apps, reviewed on 11 November, with the problems placed on purpose: red overall, EUR 1.45M a year, and EUR 223.7k of savings identified, 15.4 %, split into reclaim, consolidate, downgrade, right-size, negotiate and cancel. 15 tests, a runbook for the monthly reclaim cycle and the steps 120, 90 and 60 days before a renewal, how to negotiate with usage data and how to handle shadow IT without blocking people, and a GitHub Actions workflow that runs the tests and rebuilds the demo data and the screenshot.

## What I learned
From software asset management and licence and SaaS cost control with Apptio and Flexera, TBM and FOCUS; from showback and chargeback and unit cost metrics, and applying the FinOps Framework; from administering Microsoft 365 as Global Administrator and managing Office 365 licences with a central service desk, and Adobe licences; from Entra ID, Conditional Access, PIM and SAML single sign-on for enterprise applications, and Microsoft Graph; from the relationship with vendors such as Microsoft, Dell and Atlassian, negotiating vendor contracts, preparing and tracking the IT budget and writing business cases with ROI; and from Python and PowerShell automation. The lessons behind the tool are that the date that matters is the notice deadline, not the renewal date; that the seats you negotiate on should be the ones in use after the clean-up, not the ones assigned; that a licence on a leaver is a security problem before it is a cost; that a premium tier is assigned by habit and kept by fear, so the list of people to downgrade has to be checked with the business before the renewal; that the same euro must not appear in two savings, or finance stops believing the total; that shadow IT is usually a need IT did not meet, and talking to the people who buy it works better than blocking the card; and that showing each department what its people hold reclaims more licences than any reminder.

## Next steps
- Run it on the first working day of every month, and again 120 days before each large renewal.
- Read the other apps' assignments from their admin APIs, and use the Microsoft 365 usage reports per workload for the E5 to E3 question.
- Keep each month's utilisation to show the trend per app at the renewal meeting, and feed the savings actually realised back into the budget tracking.""",
 es="""

## El problema
El gasto en software y SaaS crece petición razonable a petición razonable, y las licencias casi nunca se recuperan. Los datos para ver a dónde va el dinero existen, en el registro, las consolas de administración, Entra ID, RR. HH. y la herramienta de gastos, pero nadie los junta hasta que llega una renovación, y para entonces la fecha de preaviso muchas veces ya ha pasado. En un mes normal en una empresa de 1.400 personas, 180 personas tienen Microsoft 365 E5 y no usan nada que no les dé ya E3; 46 licencias siguen asignadas a gente que se fue hace meses, lo que es un coste y una puerta abierta; un tercio de las licencias de Adobe Creative Cloud llevan tres meses sin abrirse; la empresa paga Zoom y Webex cuando todo el mundo tiene Teams, y Dropbox y Box al lado de OneDrive; el contrato de firma electrónica se renueva solo con un tercio de los asientos sin asignar y nueve días para avisar; el CRM vuelve con una subida del 9 % frente a un tope del 5 %; la pizarra colaborativa tiene más personas que asientos, y el ajuste llegará a precio de tarifa; nadie es responsable de un contrato que guarda datos confidenciales sin inicio de sesión único; y hay gente que paga Canva, Notion, ChatGPT Plus, Calendly y Grammarly con su tarjeta. El seguimiento de contratos con proveedores que publiqué antes en la serie guarda cada contrato de IT y su preaviso, y la revisión de costes de Azure hace este trabajo con la factura de la nube; esta revisión lo hace con las licencias y el SaaS, a partir del uso.

## Qué he hecho
- Uso: licencias sin uso desde hace 60 días o que nunca se han usado, licencias que siguen asignadas a bajas, licencias de personas con una baja larga o de cuentas que RR. HH. no conoce, y planes premium para personas que no usan sus funciones, con la diferencia de precio como ahorro.
- Asientos: licencias compradas y sin asignar, y más personas que asientos, como riesgo de un ajuste con el fabricante.
- Renovaciones: contratos con renovación automática cuyo plazo de preaviso está cerca o ya ha pasado, subidas por encima del tope pactado, contratos sin responsable, y un calendario de renovaciones de los próximos doce meses.
- Cartera y shadow IT: varias aplicaciones para la misma función, o una función que ya cubre la suite, como candidatas a consolidar; aplicaciones sin SSO con datos confidenciales; SaaS pagado con gastos que no está en el registro, y compras con tarjeta de una aplicación que ya tiene un contrato central.
- Reparto del coste: el coste por departamento y centro de coste, contratos sin centro de coste o con uno que no existe, y el gasto frente al presupuesto.
- Cada ahorro unido a una acción, recuperar, bajar de plan, ajustar asientos, negociar, consolidar o cancelar, con los usuarios que hay detrás, un responsable y una fecha; `report.html` con barras de uso por aplicación, el calendario y el reparto por departamento; `review-pack.md`, una página con las decisiones antes de las renovaciones; CSV con el uso, la lista de licencias a recuperar, el calendario, el reparto, los hallazgos y las acciones; y un exportador de solo lectura de las licencias de Microsoft 365 con Microsoft Graph.

## Cómo está hecho
Python solo con la librería estándar. Los umbrales están en un fichero de configuración pactado con finanzas, y cada hallazgo tiene una gravedad, un responsable y una fecha. Cada euro se cuenta una vez: los ahorros se aplican por aplicación en un orden fijo, recuperar, bajar de plan, ajustar asientos, negociar, cancelar duplicados y por último consolidar, con el coste de la aplicación como tope, así que dejar una herramienta de videollamadas solo cuenta lo que queda de su coste después de sus licencias sin uso y sus asientos vacíos. La fecha de preaviso es la fecha de renovación menos el plazo de preaviso, y un contrato con renovación automática y una fecha ya pasada avanza un año cada vez. El reparto carga cada licencia por usuario al departamento de la persona que la tiene y deja los asientos vacíos y los contratos de tarifa plana en IT, así que las filas suman el total. El exportador lee de Microsoft Graph los SKU que ha comprado el tenant con sus asientos y los usuarios con sus licencias y su último inicio de sesión correcto, con un registro de aplicación y un secreto que se queda en memoria; el último inicio de sesión dice que la cuenta se usa, no que se use una aplicación concreta, así que la lista de licencias a recuperar pasa por el responsable de la aplicación antes de quitar nada. La demo es una empresa de distribución inventada con 1.370 empleados en cuatro países y 24 aplicaciones, revisada el 11 de noviembre, con los problemas puestos a propósito: rojo en total, 1,45 millones de euros al año y 223.700 euros de ahorro identificado, un 15,4 %, repartido entre recuperar, consolidar, bajar de plan, ajustar asientos, negociar y cancelar. 15 tests, un runbook para el ciclo mensual de recuperación y los pasos 120, 90 y 60 días antes de una renovación, cómo negociar con los datos de uso y cómo tratar el shadow IT sin bloquear a la gente, y un workflow de GitHub Actions que ejecuta los tests y regenera los datos de la demo y la captura.

## Qué aprendí
De la gestión de activos de software y el control de costes de licencias y SaaS con Apptio y Flexera, TBM y FOCUS; del showback y el chargeback y las métricas de coste unitario, y de aplicar el FinOps Framework; de administrar Microsoft 365 como administrador global y gestionar las licencias de Office 365 con un service desk central, y las licencias de Adobe; de Entra ID, el acceso condicional, PIM y el inicio de sesión único SAML de las aplicaciones empresariales, y de Microsoft Graph; de la relación con fabricantes como Microsoft, Dell y Atlassian, de negociar contratos con proveedores, preparar y seguir el presupuesto de IT y redactar casos de negocio con ROI; y de la automatización con Python y PowerShell. Las lecciones que hay detrás de la herramienta son que la fecha que importa es la del preaviso, no la de la renovación; que los asientos que se negocian tienen que ser los que se usan después de la limpieza, no los asignados; que una licencia en una baja es un problema de seguridad antes que un coste; que un plan premium se asigna por costumbre y se mantiene por miedo, así que la lista de personas que bajan de plan hay que revisarla con el negocio antes de la renovación; que el mismo euro no puede aparecer en dos ahorros, o finanzas deja de creerse el total; que el shadow IT suele ser una necesidad que IT no cubrió, y hablar con quien lo paga funciona mejor que bloquear la tarjeta; y que enseñar a cada departamento lo que tiene su gente recupera más licencias que cualquier recordatorio.

## Siguientes pasos
- Ejecutarlo el primer día laborable de cada mes, y otra vez 120 días antes de cada renovación grande.
- Leer las asignaciones del resto de aplicaciones de sus API de administración, y usar los informes de uso de Microsoft 365 por carga de trabajo para la pregunta de E5 a E3.
- Guardar el uso de cada mes para enseñar la tendencia por aplicación en la reunión de renovación, y llevar los ahorros conseguidos de verdad al seguimiento del presupuesto."""),
dict(n="51", repo="51-windows-server-baseline-drift", date="2026-11-12", cat="tools",
 title_en="SMBv1 back on two file servers and a GPO that stopped applying: the Windows Server baseline review",
 title_es="SMBv1 activo de nuevo y una GPO que no se aplica: la revisión de la línea base de Windows Server",
 seo_title_en="Windows Server baseline drift review · Iñigo González",
 seo_title_es="Deriva de la línea base de Windows Server · Iñigo González",
 seo_desc="Windows Server security baseline review: compliance per server and tier, high-risk deviations, drift since last month, GPOs not applied and exceptions.",
 seo_desc_es="Revisión de la línea base de seguridad de Windows Server: cumplimiento por servidor, desviaciones de alto riesgo, deriva, GPO que no se aplican y excepciones.",
 dek_en="From the approved security baseline, the server inventory, the settings collected from every server with a read-only PowerShell collector, last month's collection, the exceptions register and the Group Policy results: which Windows servers are still configured as the baseline says, which have drifted since the last review and why (a GPO not applying, a local change, an exception that expired), with the high-risk deviations first, a decision for each one (fix, accept as an exception or change the baseline) and a one-page pack with the evidence for ISO 27001 and NIS2 audits.",
 dek_es="A partir de la línea base de seguridad aprobada, el inventario de servidores, la configuración recogida de cada servidor con un recolector de PowerShell de solo lectura, la recogida del mes anterior, el registro de excepciones y los resultados de las directivas de grupo: qué servidores Windows siguen configurados como dice la línea base, cuáles se han desviado desde la última revisión y por qué (una GPO que no se aplica, un cambio local, una excepción caducada), con las desviaciones de alto riesgo primero, una decisión para cada una (corregir, aceptar como excepción o cambiar la línea base) y un dosier de una página con las evidencias para las auditorías de ISO 27001 y NIS2.",
 en="""

## The problem
A security baseline for Windows servers is approved once and then drifts one reasonable change at a time. A scanner integration needs SMBv1 and someone turns it back on locally on the file servers; a few servers move to a new OU for a project and the baseline GPO is not linked there, so LLMNR, NTLM, TLS 1.0 and RDP fall back to the defaults without anyone noticing; the new servers are not in the LAPS group; a test GPO turns LLMNR back on "so the tests work"; the Print Spooler ends up on automatic on a domain controller after an incident; an ASR pilot leaves two rules in audit for months; an exception for TLS 1.0 expires and the old application is still there; some servers stop reporting and nobody knows; and a GPO link disabled during troubleshooting switches off PowerShell logging for a whole site. The data to see all of this exists, on the servers and in Group Policy, but it is rarely read against the baseline, last month's state and the exceptions at the same time. The Active Directory and infrastructure health check I published earlier in the series looks after the directory these servers depend on, and the vulnerability remediation review follows what a patch fixes; this review follows the configuration that a patch does not.

## What I built
- Compliance: every applicable baseline setting on every server, by tier and role, with the compliance per server, area, tier, site and environment against a target per tier, and the servers below it.
- High-risk deviations first: SMBv1, LM and NTLMv1, LLMNR, RDP without NLA, LAPS, Defender real-time protection and ASR rules in audit where block is expected, logon and lockout auditing, PowerShell script block logging, the Print Spooler on domain controllers, TLS 1.0 and 1.1, and firewall profiles.
- Drift: settings that were compliant at the last review and are not now, grouped by their cause, and local changes that override the GPO.
- Root cause: GPOs not applied and why (not linked, link disabled, security filtering, WMI filter), servers in an OU that is not their tier's, settings won by another GPO, and exceptions that expired, are about to expire or have no approver or ticket.
- Hygiene: servers not reporting, long uptime, old patches, and the inventory against the collection.
- `report.html` with a heat map of servers by area, the top deviations and the trend; `review-pack.md`, one page for the monthly security and infrastructure review with the decisions (fix, exception or baseline change), the high-risk items with owner and date and the audit evidence; CSVs per server, deviation, drift, exception, finding and action; and a read-only PowerShell collector.

## How it is built
Python with the standard library only. The baseline is a CSV with one row per setting: what to read (a registry value, an audit subcategory, a service, a firewall profile, the SMB server configuration, Defender, an ASR rule, a user right or the LAPS attribute in AD), the expected value and how to compare it, the severity, the tiers it applies to, the GPO that should set it and its reference to ISO 27001. An approved and valid exception counts as compliant; one without approver, ticket or expiry does not. Each deviation gets the first cause that applies, from the GPO results, the exceptions and the source of the value, and last month's collection is evaluated with the same rules to find what is new. The collector opens one remoting session per server and only reads: Get-ItemProperty, auditpol, Get-Service, Get-NetFirewallProfile, Get-SmbServerConfiguration, Get-MpComputerStatus and Get-MpPreference, secedit to a temporary file, the LAPS expiry time in AD, and the Resultant Set of Policy with Get-GPResultantSetOfPolicy; credentials come from the session and stay in memory. The demo is a made-up aerospace manufacturer with two sites, 56 servers and a 45-setting baseline, reviewed on 12 November with the problems placed on purpose: red, 92.4 % compliance against 98.8 % a month earlier, 79 high-risk deviations on 41 servers, and 138 settings drifted since the last review, 112 of them from one GPO that is not linked to the new OU. 14 tests, a runbook for the monthly cycle, piloting a baseline change in audit mode first, the exception rules and the audit evidence, and a GitHub Actions workflow that runs the tests and rebuilds the demo data and the screenshot.

## What I learned
From administering Windows Server, including DNS and DHCP, Active Directory and Group Policy since early in my career; from patching Windows servers without cutting the service and automating with PowerShell; from applied work with ISO 27001, GDPR and NIS2, NIST CSF and NIST SP 800-53, cybersecurity risk management with its treatment plans and remediation follow-up, and security policies, metrics and KPIs; from Microsoft Defender, Intune EPM, CyberArk, Tanium and Qualys and Conditional Access; and from answering audits, keeping the CMDB and owning the incident, change and problem processes. The lessons behind the tool are that one GPO that stops applying explains more deviations than all the local changes together, so the cause comes before the list of settings; that a server that does not report is not compliant but unknown, and the report has to say so; that a pilot needs an end date, or the pilot GPO wins over the baseline for months; that an exception without an approver and an expiry is just a deviation with a ticket number; that test servers should follow the production baseline, or the problems appear on the day of the release; that tightening a setting goes through audit mode and a pilot ring before the whole estate; and that an auditor trusts a report more when it shows its own gaps.

## Next steps
- Run it on the first working day of every month and after every change to a baseline GPO.
- Keep the compliance per area of each month to show the trend over the year at the security committee.
- Read the values from the configuration assessment the company already has as another source, and open the red actions as tickets with their owner and date.""",
 es="""

## El problema
Una línea base de seguridad para servidores Windows se aprueba una vez y luego se desvía cambio razonable a cambio razonable. Una integración con un escáner necesita SMBv1 y alguien lo vuelve a activar a mano en los servidores de ficheros; unos cuantos servidores pasan a una OU nueva por un proyecto y la GPO de la línea base no está vinculada allí, así que LLMNR, NTLM, TLS 1.0 y RDP vuelven a los valores por defecto sin que nadie se dé cuenta; los servidores nuevos no están en el grupo de LAPS; una GPO de pruebas vuelve a activar LLMNR "para que funcionen las pruebas"; la cola de impresión acaba en automático en un controlador de dominio después de una incidencia; un piloto de ASR deja dos reglas en auditoría durante meses; caduca una excepción para TLS 1.0 y la aplicación antigua sigue ahí; algunos servidores dejan de reportar y nadie lo sabe; y un vínculo de GPO desactivado mientras se investigaba un problema apaga el registro de PowerShell en toda una sede. Los datos para verlo existen, en los servidores y en las directivas de grupo, pero pocas veces se leen a la vez frente a la línea base, el estado del mes anterior y las excepciones. La revisión de salud de Active Directory y la infraestructura que publiqué antes en la serie cuida el directorio del que dependen estos servidores, y la revisión de la corrección de vulnerabilidades sigue lo que arregla un parche; esta revisión sigue la configuración, que un parche no arregla.

## Qué he hecho
- Cumplimiento: cada ajuste de la línea base que aplica en cada servidor, por nivel y rol, con el porcentaje de cumplimiento por servidor, área, nivel, sede y entorno frente a un objetivo por nivel, y los servidores que no llegan.
- Primero las desviaciones de alto riesgo: SMBv1, LM y NTLMv1, LLMNR, RDP sin NLA, LAPS, la protección en tiempo real de Defender y las reglas ASR en auditoría donde deberían bloquear, la auditoría de inicios de sesión y bloqueos de cuenta, el registro de bloques de script de PowerShell, la cola de impresión en los controladores de dominio, TLS 1.0 y 1.1, y los perfiles del firewall.
- Deriva: ajustes que cumplían en la revisión anterior y ahora no, agrupados por su causa, y cambios locales que pasan por encima de la GPO.
- Causa probable: GPO que no se aplican y por qué (sin vincular, vínculo desactivado, filtrado de seguridad, filtro WMI), servidores en una OU que no es la de su nivel, ajustes que gana otra GPO, y excepciones caducadas, a punto de caducar o sin aprobador ni ticket.
- Higiene: servidores que no reportan, demasiado tiempo sin reiniciar, parches antiguos, y el inventario frente a lo recogido.
- `report.html` con un mapa de calor de servidores por área, las desviaciones principales y la tendencia; `review-pack.md`, una página para la revisión mensual de seguridad e infraestructura con las decisiones (corregir, excepción o cambio de la línea base), los puntos de alto riesgo con responsable y fecha y las evidencias para auditoría; CSV por servidor, desviación, deriva, excepción, hallazgo y acción; y un recolector de PowerShell de solo lectura.

## Cómo está hecho
Python solo con la librería estándar. La línea base es un CSV con una fila por ajuste: qué leer (un valor del registro, una subcategoría de auditoría, un servicio, un perfil del firewall, la configuración del servidor SMB, Defender, una regla ASR, un derecho de usuario o el atributo de LAPS en AD), el valor esperado y cómo compararlo, la gravedad, los niveles a los que aplica, la GPO que debería fijarlo y su referencia a ISO 27001. Una excepción aprobada y en vigor cuenta como cumplimiento; una sin aprobador, ticket o fecha de caducidad, no. Cada desviación recibe la primera causa que encaja, a partir de los resultados de las GPO, las excepciones y el origen del valor, y la recogida del mes anterior se evalúa con las mismas reglas para ver qué es nuevo. El recolector abre una sesión remota por servidor y solo lee: Get-ItemProperty, auditpol, Get-Service, Get-NetFirewallProfile, Get-SmbServerConfiguration, Get-MpComputerStatus y Get-MpPreference, secedit a un fichero temporal, la fecha de caducidad de LAPS en AD, y el conjunto resultante de directivas con Get-GPResultantSetOfPolicy; las credenciales salen de la sesión y se quedan en memoria. La demo es un fabricante aeroespacial inventado con dos sedes, 56 servidores y una línea base de 45 ajustes, revisado el 12 de noviembre con los problemas puestos a propósito: rojo, un 92,4 % de cumplimiento frente al 98,8 % de hace un mes, 79 desviaciones de alto riesgo en 41 servidores y 138 ajustes desviados desde la última revisión, 112 de ellos por una sola GPO que no está vinculada a la OU nueva. 14 tests, un runbook para el ciclo mensual, cómo pilotar un cambio de la línea base empezando en modo auditoría, las reglas de las excepciones y las evidencias para auditoría, y un workflow de GitHub Actions que ejecuta los tests y regenera los datos de la demo y la captura.

## Qué aprendí
De administrar Windows Server, incluidos DNS y DHCP, Active Directory y las directivas de grupo desde el principio de mi carrera; de parchear servidores Windows sin cortar el servicio y automatizar con PowerShell; del trabajo aplicado con ISO 27001, el RGPD y NIS2, NIST CSF y NIST SP 800-53, la gestión de riesgos de ciberseguridad con sus planes de tratamiento y el seguimiento de la corrección, y las políticas, métricas y KPI de seguridad; de Microsoft Defender, Intune EPM, CyberArk, Tanium y Qualys y el acceso condicional; y de responder auditorías, mantener la CMDB y ser responsable de los procesos de incidencias, cambios y problemas. Las lecciones que hay detrás de la herramienta son que una GPO que deja de aplicarse explica más desviaciones que todos los cambios locales juntos, así que la causa va antes que la lista de ajustes; que un servidor que no reporta no cumple ni incumple, es desconocido, y el informe tiene que decirlo; que un piloto necesita fecha de fin, o la GPO del piloto le gana a la línea base durante meses; que una excepción sin aprobador ni caducidad es solo una desviación con número de ticket; que los servidores de pruebas deberían seguir la línea base de producción, o los problemas aparecen el día de la subida; que endurecer un ajuste pasa por el modo auditoría y un grupo piloto antes de todo el parque; y que un auditor se fía más de un informe que enseña sus propias lagunas.

## Siguientes pasos
- Ejecutarlo el primer día laborable de cada mes y después de cada cambio en una GPO de la línea base.
- Guardar el cumplimiento por área de cada mes para enseñar la tendencia del año en el comité de seguridad.
- Leer los valores también de la herramienta de evaluación de configuración que ya tenga la empresa, y abrir las acciones en rojo como tickets con su responsable y su fecha."""),
dict(n="52", repo="52-endpoint-security-coverage", date="2026-11-13", cat="tools",
 title_en="Nine laptops in no tool and an installer approved 37 times: the endpoint security coverage review",
 title_es="Nueve portátiles fuera de todas las herramientas y un instalador aprobado 37 veces: la revisión de cobertura de seguridad de los equipos",
 seo_title_en="Endpoint security coverage review: Intune, Defender, BitLocker · Iñigo González",
 seo_title_es="Cobertura de seguridad de los equipos: Intune, Defender y BitLocker · Iñigo González",
 seo_desc="Monthly endpoint security review: inventory, Intune and Defender reconciled, BitLocker keys, EDR health, local admins, EPM elevations and unsupported OS.",
 seo_desc_es="Revisión mensual de seguridad de los equipos: inventario, Intune y Defender cruzados, claves de BitLocker, EDR, administradores locales, EPM y sistemas sin soporte.",
 dek_en="From the asset inventory, the Intune devices, the Defender for Endpoint device inventory, the BitLocker recovery keys in Entra ID, the local administrators, the Endpoint Privilege Management elevations and the exceptions register: whether every laptop and desktop in use is managed, encrypted with its key where the service desk can find it, reporting to Defender, free of standing admin rights and on a supported operating system, with the gaps per device and their cause, a decision for each one that needs a choice and a one-page pack with the evidence for ISO 27001 and NIS2 audits.",
 dek_es="A partir del inventario de activos, los dispositivos de Intune, el inventario de Defender for Endpoint, las claves de recuperación de BitLocker en Entra ID, los administradores locales, las elevaciones de Endpoint Privilege Management y el registro de excepciones: si cada portátil y sobremesa en uso está gestionado, cifrado con su clave donde el service desk la puede encontrar, reportando a Defender, sin derechos de administrador permanentes y con un sistema operativo con soporte, con los huecos por equipo y su causa, una decisión para cada uno que la necesite y un dosier de una página con las evidencias para las auditorías de ISO 27001 y NIS2.",
 en="""

## The problem
Every security tool on the endpoints shows its own view, and each view looks fine on its own. Intune shows compliance for the devices it manages, Defender shows sensor health for the devices that are onboarded, the CMDB shows what was bought, and the gaps sit between them. A field team builds a few laptops locally to save time and they never reach Intune or Defender; new workstations are enrolled, but their group is not in the onboarding policy; a firmware update suspends BitLocker and nobody resumes it; laptops imaged by an old process are encrypted, but their recovery key is not in Entra ID, so the service desk cannot unlock them; a vendor asks to turn off the antivirus on two CAD workstations and it stays off; a software rollout adds engineers to the local Administrators group "for a week"; the service desk approves the same installer dozens of times a month; an unsigned lab tool is elevated on a test bench; Windows 10 lingers on the production floor after its end of support; and retired laptops still check in. The Intune compliance report I published early in the series looks at compliance policy by policy, and the Windows Server baseline review looks after the servers; this review asks the question for the whole fleet of laptops and desktops at once.

## What I built
- One list from three sources: every device in the inventory, Intune and Defender matched by serial number, name and Entra device ID, with what each tool is missing: devices in use that no tool manages, devices the inventory does not have, and retired devices that are still active.
- Coverage by control on every device: managed, compliant, checking in, encrypted, recovery key escrowed, EDR onboarded and healthy, antivirus healthy (real-time protection, signatures and tamper protection), no standing local administrators and a supported operating system, per site, department and platform, against a target per control and last month.
- Privilege: standing members of the local Administrators group, the files that many users elevate with approval, which are candidates for an automatic EPM rule, and unsigned files elevated.
- Exceptions: valid ones count as covered; expired, expiring and incomplete ones come back as findings.
- `report.html` with the coverage per control, a heat map of departments by control and the three sources reconciled; `review-pack.md`, one page for the monthly endpoint security review with the decisions, the actions with owner and date and the audit evidence; CSVs per device, gap, source, elevation, exception, finding and action; a read-only PowerShell collector and an Intune Remediations detection script for the local administrators.

## How it is built
Python with the standard library only. The inventory comes first, Intune records are matched to it by serial number and then name, and Defender records to those by Entra device ID and then name, so one physical device is one row whatever each tool calls it. Each control gives pass, fail, exception or unknown on each device: a device missing from the local admin report is unknown, not covered, and the report says how many. Valid exceptions, with an approver, a ticket and an expiry, count as covered; incomplete or expired ones do not. Findings are grouped by cause, so six workstations missing from Defender appear as one problem with one owner, and the gaps that need a choice (an unsupported OS, standing admin rights, an automatic elevation rule, unmanaged devices, an expired exception) become decisions. The collector only reads: the Intune managed devices and the antivirus state of each Windows device through Microsoft Graph, and the BitLocker recovery key metadata in Entra ID, never the key itself; Defender comes from the portal's device export, and the local administrators from a detection script that changes nothing. The demo is a made-up maker of drone and avionics parts with two sites and 368 devices in use, reviewed on 13 November with the problems placed on purpose: red, 76.9 % fully protected against 93.2 % a month earlier, 11 devices not managed, 25 without a working EDR sensor, 14 with standing admins, 11 on an unsupported OS, and five decisions. 15 tests, a runbook for the monthly cycle, how to read the result and roll out policy changes without breaking users, and a GitHub Actions workflow that runs the tests and rebuilds the demo data and the screenshot.

## What I learned
From managing Windows, macOS, iOS and Android devices with Intune, BitLocker encryption and compliance, and leading a migration to Windows 11; from Intune Endpoint Privilege Management, Microsoft Defender, Conditional Access and Entra ID; from Microsoft Graph and PowerShell automation; from applied work with ISO 27001, GDPR and NIS2, NIST CSF, and security policies, metrics and KPIs; and from asset management, the CMDB, answering audits and owning the incident, change and problem processes. The lessons behind the tool are that the most dangerous device is the one no tool knows about, so the reconciliation comes before any percentage; that gaps cluster by department, site, model or build process, and fixing the cause fixes the devices; that an encrypted laptop without its recovery key in the directory is a support incident waiting to happen; that "temporary" admin rights need an end date, and EPM rules make removing them painless; that the installer approved by hand dozens of times a month is a rule nobody has written yet; that a device with no data is unknown, not compliant; and that an exception is a decision with an end date, not a status.

## Next steps
- Run it on the first working day of every month and after every change to the onboarding, encryption or account protection policies.
- Keep the coverage per control of each month to show the trend over the year at the security committee.
- Read the Defender machines API directly instead of the portal export, and add the iOS and Android devices with their own controls.""",
 es="""

## El problema
Cada herramienta de seguridad de los equipos enseña su propia vista, y cada vista por separado parece estar bien. Intune enseña el cumplimiento de los equipos que gestiona, Defender la salud del sensor de los equipos incorporados, la CMDB lo que se compró, y los huecos están entre medias. Un equipo de campo monta unos portátiles por su cuenta para ganar tiempo y nunca llegan a Intune ni a Defender; se inscriben estaciones de trabajo nuevas, pero su grupo no está en la directiva de incorporación; una actualización de firmware suspende BitLocker y nadie lo reanuda; unos portátiles instalados con un proceso antiguo están cifrados, pero su clave de recuperación no está en Entra ID, así que el service desk no los puede desbloquear; un proveedor pide desactivar el antivirus en dos estaciones de CAD y se queda desactivado; un despliegue de software mete a unos ingenieros en el grupo local de Administradores "durante una semana"; el service desk aprueba el mismo instalador decenas de veces al mes; se eleva una herramienta de laboratorio sin firmar en un banco de pruebas; Windows 10 sigue en la planta de producción después del fin de su soporte; y portátiles dados de baja siguen conectándose. El informe de cumplimiento de Intune que publiqué al principio de la serie mira el cumplimiento directiva a directiva, y la revisión de la línea base de Windows Server cuida los servidores; esta revisión hace la pregunta para todo el parque de portátiles y sobremesas a la vez.

## Qué he hecho
- Una lista a partir de tres fuentes: cada equipo del inventario, Intune y Defender emparejado por número de serie, nombre e ID de dispositivo de Entra, con lo que le falta a cada herramienta: equipos en uso que ninguna herramienta gestiona, equipos que el inventario no tiene y equipos dados de baja que siguen activos.
- Cobertura por control en cada equipo: gestionado, cumple, se conecta, cifrado, clave de recuperación guardada, EDR incorporado y sano, antivirus sano (protección en tiempo real, firmas y protección contra alteraciones), sin administradores locales permanentes y con un sistema operativo con soporte, por sede, departamento y plataforma, frente a un objetivo por control y el mes anterior.
- Privilegios: miembros permanentes del grupo local de Administradores, los ficheros que muchos usuarios elevan con aprobación, candidatos a una regla automática de EPM, y ficheros sin firmar que se elevan.
- Excepciones: las válidas cuentan como cubiertas; las caducadas, a punto de caducar o incompletas vuelven como hallazgos.
- `report.html` con la cobertura por control, un mapa de calor de departamentos por control y las tres fuentes cruzadas; `review-pack.md`, una página para la revisión mensual de seguridad de los equipos con las decisiones, las acciones con responsable y fecha y las evidencias para auditoría; CSV por equipo, hueco, fuente, elevación, excepción, hallazgo y acción; un recolector de PowerShell de solo lectura y un script de detección de Intune Remediations para los administradores locales.

## Cómo está hecho
Python solo con la librería estándar. Primero va el inventario; los registros de Intune se emparejan con él por número de serie y después por nombre, y los de Defender con esos por ID de dispositivo de Entra y después por nombre, así que un equipo físico es una fila se llame como se llame en cada herramienta. Cada control da en cada equipo cumple, no cumple, excepción o desconocido: un equipo que falta en el informe de administradores locales es desconocido, no cubierto, y el informe dice cuántos hay. Las excepciones válidas, con aprobador, ticket y caducidad, cuentan como cubiertas; las incompletas o caducadas, no. Los hallazgos se agrupan por causa, así que seis estaciones que faltan en Defender aparecen como un problema con un responsable, y los huecos que necesitan elegir (un sistema sin soporte, derechos de administrador permanentes, una regla de elevación automática, equipos sin gestionar, una excepción caducada) se convierten en decisiones. El recolector solo lee: los dispositivos gestionados de Intune y el estado del antivirus de cada equipo Windows con Microsoft Graph, y los metadatos de las claves de recuperación de BitLocker en Entra ID, nunca la clave; Defender sale de la exportación de dispositivos del portal, y los administradores locales de un script de detección que no cambia nada. La demo es un fabricante inventado de piezas para drones y aviónica con dos sedes y 368 equipos en uso, revisado el 13 de noviembre con los problemas puestos a propósito: rojo, un 76,9 % de equipos totalmente protegidos frente al 93,2 % de hace un mes, 11 equipos sin gestionar, 25 sin un sensor de EDR que funcione, 14 con administradores permanentes, 11 con un sistema sin soporte, y cinco decisiones. 15 tests, un runbook para el ciclo mensual, cómo leer el resultado y desplegar cambios de directivas sin romper nada a los usuarios, y un workflow de GitHub Actions que ejecuta los tests y regenera los datos de la demo y la captura.

## Qué aprendí
De gestionar equipos Windows, macOS, iOS y Android con Intune, el cifrado con BitLocker y el cumplimiento, y de liderar una migración a Windows 11; de Intune Endpoint Privilege Management, Microsoft Defender, el acceso condicional y Entra ID; de Microsoft Graph y la automatización con PowerShell; del trabajo aplicado con ISO 27001, el RGPD y NIS2, NIST CSF, y las políticas, métricas y KPI de seguridad; y de la gestión de activos, la CMDB, responder auditorías y ser responsable de los procesos de incidencias, cambios y problemas. Las lecciones que hay detrás de la herramienta son que el equipo más peligroso es el que ninguna herramienta conoce, así que el cruce de fuentes va antes que cualquier porcentaje; que los huecos se agrupan por departamento, sede, modelo o proceso de instalación, y arreglar la causa arregla los equipos; que un portátil cifrado sin su clave de recuperación en el directorio es una incidencia esperando a pasar; que los derechos de administrador "temporales" necesitan fecha de fin, y las reglas de EPM hacen que quitarlos no duela; que el instalador que se aprueba a mano decenas de veces al mes es una regla que nadie ha escrito todavía; que un equipo sin datos es desconocido, no cumple; y que una excepción es una decisión con fecha de fin, no un estado.

## Siguientes pasos
- Ejecutarlo el primer día laborable de cada mes y después de cada cambio en las directivas de incorporación, cifrado o protección de cuentas.
- Guardar la cobertura por control de cada mes para enseñar la tendencia del año en el comité de seguridad.
- Leer directamente la API de equipos de Defender en lugar de la exportación del portal, y añadir los iPhone y Android con sus propios controles."""),
]
