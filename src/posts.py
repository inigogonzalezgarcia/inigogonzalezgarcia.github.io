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

dict(n="05", repo="05-it-ops-console", date="2026-09-30", cat="tools",
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

dict(n="06", repo="06-kubernetes-ingress-lab", date="2026-10-01", cat="cloud",
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

dict(n="19", repo="19-ad-infra-health-check", date="2026-10-16", cat="tools",
 title_en="A Monday-morning health check for Active Directory", title_es="Un chequeo de los lunes para Active Directory",
 seo_title_en="Active Directory health check with PowerShell · Iñigo González",
 seo_title_es="Chequeo de salud de Active Directory con PowerShell · Iñigo González",
 dek_en="Domain controllers, replication, DHCP, Group Policy and admin accounts from one read-only export, ordered by what to fix today.",
 dek_es="Controladores de dominio, replicación, DHCP, directivas de grupo y cuentas de administrador desde una exportación de solo lectura, ordenados por lo que hay que arreglar hoy.",
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

dict(n="22", repo="22-dex-experience-score", date="2026-10-17", cat="tools",
 title_en="A 0-10 experience score for every laptop", title_es="Una nota de 0 a 10 para la experiencia de cada portátil",
 seo_title_en="DEX score: a 0-10 experience per laptop · Iñigo González",
 seo_title_es="Puntuación DEX de 0 a 10 por portátil · Iñigo González",
 dek_en="A lab that turns endpoint telemetry into a score per device, site and department, and ranks the five fixes that would raise it most.",
 dek_es="Un laboratorio que convierte la telemetría de los equipos en una nota por dispositivo, sede y departamento, y ordena los cinco arreglos que más la subirían.",
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
 title_en="The plan says wave 3 on the 30th; the inventory says no: readiness for a Microsoft 365 tenant separation", title_es="El plan dice ola 3 el día 30; el inventario dice que no: preparación de una separación de tenant de Microsoft 365",
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
 title_en="128 licences nobody uses and a sprint still open nine days late: a monthly review of a Jira and Confluence site", title_es="128 licencias que nadie usa y un sprint abierto nueve días tarde: una revisión mensual de un sitio de Jira y Confluence",
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
 title_en="The warranty feed stopped on Thursday and the dealer found out on Tuesday: a weekly review of a dealer network's systems", title_es="El feed de garantías se paró el jueves y el concesionario se enteró el martes: una revisión semanal de los sistemas de una red de concesionarios",
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
 title_en="The backup ran every night, but would it bring the system back? A monthly review of backups, restore tests and DR",
 title_es="El backup corrió cada noche, pero ¿devolvería el sistema? Una revisión mensual de backups, pruebas de restauración y DR",
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
 title_en="The only kitchen printer had been down since yesterday: a morning readiness check for a hospitality venue",
 title_es="La única impresora de cocina llevaba caída desde ayer: una revisión de cada mañana para un local de hostelería",
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
 title_en="He left three weeks ago and is still in Domain Admins: a monthly access review for joiners, movers, leavers and privileged access",
 title_es="Se fue hace tres semanas y sigue en Domain Admins: una revisión mensual de accesos para altas, cambios, bajas y accesos privilegiados",
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
 seo_desc="Free IT support simulator in English and Spanish: 18 tickets with SLA, a console, Active Directory, a marked work note and a fix that looks right but is not.",
 dek_en="A support desk in the browser: a ticket queue with SLA, the requester and the device, a console where the commands do something, a simulated Active Directory, a desktop to fix things on the user's machine, 18 tickets from first line to second line, a tempting fix that does not solve the cause, and a work note that gets marked. Free, in English and Spanish.",
 dek_es="Una mesa de soporte en el navegador: cola de tickets con SLA, el solicitante y su equipo, una consola donde los comandos hacen algo, un Active Directory simulado, un escritorio para arreglar en la máquina del usuario, 18 tickets de primer y segundo nivel, un arreglo tentador que no resuelve la causa y una nota de trabajo que se corrige. Gratis, en español e inglés.",
 en="""
## The problem
Most people learn support on the job, with real users waiting. Labs teach the commands, but not the ticket: reading what the user really says, finding the cause instead of the symptom, checking that it works before closing, and leaving a note the next engineer can use. The classic mistake is the fix that looks right. You unlock the account that locks every morning, the user is happy for an hour, and the ticket comes back because the old password is still saved on the phone. I wanted a place to practise that loop without a real company behind it.

## What I built
- A ticket queue with priority, SLA (20, 30 or 45 minutes) and status. Assigning a ticket starts the clock and opens the console.
- A ticket page with the requester and the device, cards that change as the scenario changes, and actions from the page that do the same as the command, traps included.
- 18 tickets across Active Directory, DNS, Windows, printers, Exchange Online, Intune and BitLocker, VPN, Microsoft 365 licences, Azure AD Connect, Veeam, MECM, Red Hat, Citrix, Conditional Access, SAML single sign-on, Linux joined to AD and SQL Server. Each one has a root cause, a tempting fix that does not close it and a check to prove it works.
- Closing a ticket asks for a resolution code and a work note. The note is marked on cause, change, verification and follow-up, and the result is Resolved, Resolved with remarks or Not resolved, with what is missing.
- A simulated Active Directory with OUs, users, groups and computers, where every button runs a visible PowerShell command; a desktop for the tickets that are fixed on the user's machine, with an event viewer; and an inventory of servers and printers linked to the open tickets.
- A knowledge base built from your own approved notes, downloadable as Markdown, progress with a streak, a weekly goal and badges, and an internal mailbox with real requests and phishing to tell apart from them.
- A "Practise it" box in 17 of the guides on this website, which opens the matching ticket in the right language.

## How it is built
A static site with plain JavaScript and a small database for accounts and results. Every ticket has automated tests, so the tempting fix can never close it. Everything is fictional: a made-up company, no real systems. It is practice, not work experience.

## What I learned
From working tickets and teaching others to work them: the work note is part of the fix, a ticket is not closed until the user confirms it works, and the fix that looks right is the most common way to reopen one.

## Next steps
- Contact the requester from the ticket with scripted questions, where some clues only come out by asking, and mark the note to the user apart from the work note.
- Workflow states (pending user, pending vendor) with the SLA paused, and password reset by email for accounts.
- A network room with switches, routers and firewalls, a switch CLI and network tickets, then shipments and RMA linked to tickets.
""",
 es="""
## El problema
Casi todo el mundo aprende soporte trabajando, con usuarios reales esperando. Los laboratorios enseñan los comandos, pero no el ticket: leer lo que el usuario dice de verdad, encontrar la causa y no el síntoma, comprobar que funciona antes de cerrar y dejar una nota que le sirva al siguiente técnico. El error clásico es el arreglo que parece bueno. Desbloqueas la cuenta que se bloquea cada mañana, el usuario está contento una hora y el ticket vuelve, porque la contraseña antigua sigue guardada en el móvil. Quería un sitio para practicar ese ciclo sin una empresa real detrás.

## Qué he hecho
- Una cola de tickets con prioridad, SLA (20, 30 o 45 minutos) y estado. Al asignarte un ticket empieza a correr el reloj y se abre la consola.
- Una ficha del ticket con el solicitante y su equipo, tarjetas que cambian según avanza el caso y acciones desde la ficha que hacen lo mismo que el comando, trampas incluidas.
- 18 tickets de Active Directory, DNS, Windows, impresoras, Exchange Online, Intune y BitLocker, VPN, licencias de Microsoft 365, Azure AD Connect, Veeam, MECM, Red Hat, Citrix, acceso condicional, inicio de sesión único con SAML, Linux unido a AD y SQL Server. Cada uno tiene una causa raíz, un arreglo tentador que no lo cierra y una comprobación para demostrar que funciona.
- Para cerrar un ticket hay que elegir un código de resolución y escribir una nota de trabajo. La nota se corrige por causa, cambio, verificación y seguimiento, y el resultado es Resuelto, Resuelto con observaciones o No resuelto, con lo que falta.
- Un Active Directory simulado con OU, usuarios, grupos y equipos, donde cada botón ejecuta un comando de PowerShell visible; un escritorio para los tickets que se arreglan en la máquina del usuario, con visor de eventos; y un inventario de servidores e impresoras ligado a los tickets abiertos.
- Una base de conocimiento que se crea con tus propias notas aprobadas y se descarga en Markdown, progreso con racha, objetivo semanal e insignias, y un buzón interno con peticiones reales y phishing que hay que saber distinguir.
- Un bloque «Practícalo» en 17 de las guías de esta web, que abre el ticket correspondiente en el idioma de la guía.

## Cómo está hecho
Un sitio estático con JavaScript sin frameworks y una pequeña base de datos para las cuentas y los resultados. Cada ticket tiene tests automáticos, para que el arreglo tentador nunca pueda cerrarlo. Todo es ficticio: una empresa inventada y ningún sistema real. Es práctica, no experiencia laboral.

## Qué aprendí
De trabajar tickets y enseñar a otros a trabajarlos: la nota de trabajo es parte del arreglo, un ticket no está cerrado hasta que el usuario confirma que funciona, y el arreglo que parece bueno es la forma más habitual de reabrirlo.

## Siguientes pasos
- Contactar con el solicitante desde el ticket con preguntas guionizadas, donde algunas pistas solo salen preguntando, y corregir la nota al usuario aparte de la nota de trabajo.
- Estados de flujo (pendiente del usuario, pendiente del proveedor) con el SLA en pausa, y restablecer la contraseña de la cuenta por email.
- Una sala de red con switches, routers y cortafuegos, una CLI de switch y tickets de red; después, envíos y RMA ligados a los tickets.
"""),
dict(n="38", repo="38-it-asset-lifecycle-planner", date="2026-10-30", cat="tools",
 title_en="Nine laptops nobody registered and half the budget in one quarter: one inventory and a refresh plan for the office hardware",
 title_es="Nueve portátiles que nadie registró y medio presupuesto en un trimestre: un inventario único y un plan de renovación para el hardware de la oficina",
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
]
