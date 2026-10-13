# Blog posts: one per GitHub repo. Mini-markup: "## " heading, "- " bullet, blank line = new paragraph, `code`.
# Only facts that are in each repo's README. Labs 06-16 are labs: say so.

CATS = {
    "tools": ("Herramientas de IT Ops", "IT Ops tools"),
    "cloud": ("Laboratorio cloud y SRE", "Cloud & SRE lab"),
    "gpu": ("Laboratorio GPU", "GPU lab"),
}

POSTS = [
dict(n="01", repo="01-finops-cloud-cost-dashboard", date="2026-09-03", cat="tools",
 title_en="Catching cloud cost drift before the invoice does", title_es="Ver la deriva del gasto cloud antes que la factura",
 dek_en="A small Streamlit dashboard for AWS and Azure spend that flags the week that looks wrong.",
 dek_es="Un panel pequeño en Streamlit para el gasto de AWS y Azure que señala la semana que no cuadra.",
 en="""## The problem
Cloud costs rarely explode overnight. They drift: a test environment left running over a weekend, a service scaled up and never scaled down. By the time the monthly invoice arrives, the money is already spent.

I wanted a view that answers three questions fast: how much are we spending and where, is this week different from last week, and is anything clearly out of line.

## What I built
- A consolidated view of daily spend across AWS and Azure, with filters by provider, environment and department.
- A weekly KPI: the last 7 days against the previous 7.
- An anomaly alert with a probable cause and a suggested action, such as auto-shutdown for idle development instances.

## How it is built
Python, pandas, Plotly and Streamlit. `data_generator.py` creates 90 days of synthetic billing for 10 services, 4 departments and 3 environments, and injects a spike into EC2 / Development in the last week so the detection has something to find.

## What's next
The detection is rule-based and aimed at that injected scenario. The next steps are a statistical baseline per service, importing real Cost Explorer and Azure Cost Management CSV exports, and budget thresholds per department.""",
 es="""## El problema
El gasto cloud casi nunca se dispara de un día para otro. Se desvía poco a poco: un entorno de pruebas encendido todo el fin de semana, un servicio que se escala y nunca se vuelve a bajar. Cuando llega la factura, el dinero ya se ha gastado.

Quería una vista que respondiera rápido a tres preguntas: cuánto gastamos y dónde, si esta semana es distinta de la anterior y si hay algo claramente fuera de lugar.

## Qué he hecho
- Una vista única del gasto diario en AWS y Azure, con filtros por proveedor, entorno y departamento.
- Un KPI semanal: los últimos 7 días frente a los 7 anteriores.
- Una alerta de anomalía con causa probable y acción sugerida, como el apagado automático de instancias de desarrollo ociosas.

## Cómo está hecho
Python, pandas, Plotly y Streamlit. `data_generator.py` crea 90 días de facturación ficticia para 10 servicios, 4 departamentos y 3 entornos, e inyecta un pico en EC2 / Development la última semana para que la detección tenga algo que encontrar.

## Siguientes pasos
La detección se basa en reglas y apunta a ese escenario inyectado. Lo siguiente: una línea base estadística por servicio, importar exportaciones CSV reales de Cost Explorer y Azure Cost Management, y umbrales de presupuesto por departamento."""),

dict(n="02", repo="02-intune-compliance-report", date="2026-09-30", cat="tools",
 title_en="An Intune compliance report you can hand to a manager", title_es="Un informe de cumplimiento de Intune que se puede enseñar a dirección",
 dek_en="PowerShell pulls the devices from Microsoft Graph, Python turns them into a report and an action list.",
 dek_es="PowerShell saca los dispositivos de Microsoft Graph y Python los convierte en un informe y una lista de acciones.",
 en="""## The problem
The Intune portal tells you a device is non-compliant. It doesn't give you a one-page answer to "how are we doing, by OS, and which machines do I chase this week?".

## What I built
- `scripts/Export-IntuneDevices.ps1` exports managed devices through Microsoft Graph with a read-only permission.
- A Python report (standard library only) that produces `report.html`: KPIs, compliance by operating system, devices to review and OS versions.
- `action_list.csv`, the list of devices someone actually has to go and fix.

## How it is built
Python with no third-party packages plus PowerShell, which is the split I use for anything Microsoft. `generate_sample_data.py` creates a fictional fleet so the repo runs without a tenant. Seven tests cover the logic.

## What I learned
Keeping the export and the analysis apart pays off: the PowerShell side only needs read access, and the Python side can be tested with fake data.""",
 es="""## El problema
El portal de Intune te dice que un equipo no cumple. No te da en una página la respuesta a "cómo vamos, por sistema operativo, y a qué equipos hay que perseguir esta semana".

## Qué he hecho
- `scripts/Export-IntuneDevices.ps1` exporta los dispositivos gestionados por Microsoft Graph con un permiso de solo lectura.
- Un informe en Python (solo librería estándar) que genera `report.html`: KPIs, cumplimiento por sistema operativo, dispositivos a revisar y versiones de SO.
- `action_list.csv`, la lista de equipos que alguien tiene que ir a arreglar.

## Cómo está hecho
Python sin paquetes de terceros y PowerShell, el reparto que uso para todo lo de Microsoft. `generate_sample_data.py` crea una flota ficticia para que el repo funcione sin tenant. Siete tests cubren la lógica.

## Qué aprendí
Separar la exportación del análisis compensa: la parte de PowerShell solo necesita permisos de lectura y la de Python se prueba con datos falsos."""),

dict(n="03", repo="03-entra-id-hygiene-audit", date="2026-09-30", cat="tools",
 title_en="Auditing Entra ID hygiene: MFA gaps and forgotten accounts", title_es="Auditar la higiene de Entra ID: huecos de MFA y cuentas olvidadas",
 dek_en="Admins without MFA, inactive members and stale guests, found in one pass.",
 dek_es="Administradores sin MFA, miembros inactivos e invitados obsoletos, en una sola pasada.",
 en="""## The problem
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
Most of the work is deciding what "inactive" and "stale" mean and writing it down, so the report can be defended when someone asks why their account is on it.""",
 es="""## El problema
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
Casi todo el trabajo está en decidir qué significa "inactivo" y "obsoleto" y dejarlo escrito, para poder defender el informe cuando alguien pregunte por qué sale su cuenta."""),

dict(n="04", repo="04-itsm-kpi-dashboard", date="2026-09-30", cat="tools",
 title_en="Service desk KPIs from a plain ticket export", title_es="KPIs de service desk a partir de una exportación de tickets",
 dek_en="SLA by priority and team, time to resolve, weekly trend and the open tickets already out of SLA.",
 dek_es="SLA por prioridad y por equipo, tiempo de resolución, tendencia semanal y los tickets abiertos ya fuera de SLA.",
 en="""## The problem
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
The median tells a different story from the mean: a few very long tickets move the mean a lot, and the median shows what most users actually live with.""",
 es="""## El problema
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
La mediana cuenta otra historia que la media: unos pocos tickets muy largos mueven mucho la media, y la mediana enseña lo que vive la mayoría de usuarios."""),

dict(n="05", repo="05-it-ops-console", date="2026-09-30", cat="tools",
 title_en="Rebuilding an on-site IT operations console from scratch", title_es="Rehacer desde cero una consola de operaciones IT de sede",
 dek_en="Assets, warranties, room checklists, joiners and leavers, shifts and service health in one Flask app.",
 dek_es="Activos, garantías, checklists de salas, altas y bajas, turnos y salud de servicios en una app Flask.",
 en="""## The problem
Running a site means keeping a lot of small things in your head: which machines are offline, which warranties expire, which rooms were checked this morning, who starts on Monday. I wanted all of it in one place, built from scratch and anonymised.

## What I built
- Dashboard, assets (offline, non-compliant, duplicate serials, remote queries), warranties and software.
- People, floor maps, meeting-room checklists, joiners and leavers, visitors and shifts.
- Service health, role-based admin and an audit log.

Access is invite-only: the first admin is created with `bootstrap-admin`, accounts are activated with a 6-character code sent by email, and every sign-in after that needs an authenticator app (TOTP).

## How it is built
Flask and SQLite, with PowerShell over CIM/WinRM for remote queries. ARCHITECTURE.md, docs/decisions.md (PowerShell and WMI lessons) and docs/security.md explain the choices. Sixteen tests.

## Not tested yet
LDAP, SMTP, remote PowerShell and QR codes have not been run against a real environment, and the README says so.""",
 es="""## El problema
Llevar una sede es tener muchas cosas pequeñas en la cabeza: qué equipos están offline, qué garantías caducan, qué salas se han revisado esta mañana, quién empieza el lunes. Lo quería todo en un sitio, hecho desde cero y anonimizado.

## Qué he hecho
- Panel, activos (offline, no conformes, seriales duplicados, consultas remotas), garantías y software.
- Personas, planos de planta, checklists de salas, altas y bajas, visitas y turnos.
- Salud de servicios, administración por roles y log de auditoría.

El acceso es solo por invitación: el primer administrador se crea con `bootstrap-admin`, las cuentas se activan con un código de 6 caracteres por email y desde entonces cada inicio de sesión pide app autenticadora (TOTP).

## Cómo está hecho
Flask y SQLite, con PowerShell por CIM/WinRM para las consultas remotas. ARCHITECTURE.md, docs/decisions.md (lecciones de PowerShell y WMI) y docs/security.md explican las decisiones. Dieciséis tests.

## Sin probar todavía
LDAP, SMTP, PowerShell remoto y los códigos QR no se han probado contra un entorno real, y el README lo dice."""),

dict(n="06", repo="06-kubernetes-ingress-lab", date="2026-10-01", cat="cloud",
 title_en="A Kubernetes ingress lab built from zero in every CI run", title_es="Un laboratorio de ingress en Kubernetes que la CI construye desde cero",
 dek_en="Cilium, Envoy Gateway, cert-manager and external-dns on kind, with nine end-to-end checks.",
 dek_es="Cilium, Envoy Gateway, cert-manager y external-dns sobre kind, con nueve pruebas de punta a punta.",
 en="""## Why this lab
This is a learning lab, not production experience. I wanted to understand how traffic gets into a Kubernetes cluster today: Gateway API instead of the old Ingress, eBPF networking, certificates and DNS handled by controllers.

## What I built
- kind with no CNI and no kube-proxy, replaced by Cilium (LB IPAM, L2 announcements, an L7 policy and Hubble).
- Envoy Gateway with Gateway API: redirect, TLS and rate limiting.
- cert-manager with a lab CA and a wildcard certificate.
- external-dns writing to BIND over RFC 2136 with TSIG, using TXT ownership records.
- Default deny in the apps namespace and an L7 allow-list (`/env` returns 403), with no way around the gateway.

## How it is tested
A GitHub Actions workflow builds the cluster from scratch and runs nine end-to-end tests. It has been green in the last four runs.

## What's next
The plan includes an open source contribution, docs or a good first issue, in one of these projects.""",
 es="""## Por qué este laboratorio
Es un laboratorio para aprender, no experiencia en producción. Quería entender cómo entra hoy el tráfico en un clúster de Kubernetes: Gateway API en lugar del Ingress clásico, red con eBPF, y certificados y DNS gestionados por controladores.

## Qué he hecho
- kind sin CNI ni kube-proxy, sustituidos por Cilium (LB IPAM, anuncios L2, una política L7 y Hubble).
- Envoy Gateway con Gateway API: redirección, TLS y limitación de peticiones.
- cert-manager con una CA del laboratorio y un certificado wildcard.
- external-dns escribiendo en BIND por RFC 2136 con TSIG y registros TXT de propiedad.
- Denegación por defecto en el namespace de las apps y lista blanca L7 (`/env` devuelve 403), sin forma de saltarse el gateway.

## Cómo se prueba
Un workflow de GitHub Actions construye el clúster desde cero y pasa nueve pruebas de punta a punta. Ha salido en verde en las cuatro últimas ejecuciones.

## Siguientes pasos
El plan incluye una contribución open source, documentación o una good first issue, en alguno de estos proyectos."""),

dict(n="07", repo="07-aws-private-connectivity", date="2026-10-01", cat="cloud",
 title_en="Private connectivity on AWS with Terraform, and the bug CI caught", title_es="Conectividad privada en AWS con Terraform, y el fallo que pilló la CI",
 dek_en="PrivateLink, private DNS and SSM endpoints in five modules, tested without an AWS account.",
 dek_es="PrivateLink, DNS privado y endpoints de SSM en cinco módulos, probados sin cuenta de AWS.",
 en="""## Why this lab
A learning lab on a pattern I see a lot in hybrid environments: reaching a service privately, with no internet gateway and no NAT.

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

## Not tested yet
`apply` against a real AWS account.""",
 es="""## Por qué este laboratorio
Un laboratorio para aprender un patrón que veo mucho en entornos híbridos: llegar a un servicio de forma privada, sin internet gateway ni NAT.

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

## Sin probar todavía
`apply` en una cuenta real de AWS."""),

dict(n="08", repo="08-edge-health-slo-monitor", date="2026-10-01", cat="cloud",
 title_en="SLOs and burn-rate alerts for the edge, in plain Python", title_es="SLO y alertas por burn rate para el edge, en Python sin dependencias",
 dek_en="DNS, TLS, HTTP and TCP probes, an error budget and a fictional postmortem.",
 dek_es="Sondas DNS, TLS, HTTP y TCP, un presupuesto de error y un postmortem ficticio.",
 en="""## Why this lab
A learning lab on how SRE teams decide when to wake someone up: not on every failed check, but when the error budget is burning too fast.

## What I built
- DNS, TLS, HTTP and TCP probes.
- An SLO with an error budget and multi-window burn-rate alerts, with a minimum number of bad probes before firing.
- Export to Elasticsearch (ECS) and Prometheus, a signed webhook and an HTML report.
- A postmortem template and a fictional postmortem: a DNS record lost during a zone migration.

## How it is built
Python 3.11, standard library only, 14 tests.

## Not tested yet
Sending to a real Elasticsearch, the systemd units and the webhook against a real n8n.""",
 es="""## Por qué este laboratorio
Un laboratorio para aprender cómo deciden los equipos SRE cuándo despertar a alguien: no con cada fallo, sino cuando el presupuesto de error se consume demasiado rápido.

## Qué he hecho
- Sondas DNS, TLS, HTTP y TCP.
- Un SLO con presupuesto de error y alertas multiventana por burn rate, con un mínimo de sondas malas antes de avisar.
- Exportación a Elasticsearch (ECS) y Prometheus, un webhook firmado y un informe HTML.
- Una plantilla de postmortem y un postmortem ficticio: un registro DNS perdido en una migración de zona.

## Cómo está hecho
Python 3.11, solo librería estándar, 14 tests.

## Sin probar todavía
El envío a un Elasticsearch real, las units de systemd y el webhook contra un n8n real."""),

dict(n="09", repo="09-gpu-node-remediation", date="2026-10-01", cat="gpu",
 title_en="Teaching a Kubernetes controller to drain, repair or quarantine GPU nodes", title_es="Un controlador de Kubernetes que drena, repara o pone en cuarentena nodos GPU",
 dek_en="First GPU lab: XID errors, ECC and temperature drive each node through a state machine.",
 dek_es="Primer laboratorio de GPU: los XID, el ECC y la temperatura llevan cada nodo por una máquina de estados.",
 en="""## Why this lab
I don't have production experience with GPU fleets. This is the first of a series of labs to learn how they are operated day to day, and every README says so. No paid GPU machines were used.

## What I built
A Kubernetes controller in Go (standard library only, no client-go) that reads DCGM metrics (XID errors, double-bit ECC, row remapping, temperature) and moves each node through Healthy → Draining → Repairing → Validating → Healthy, or to Cordoned for thermal issues, or Quarantined.
- State is kept in node annotations, with a budget of nodes in remediation (max-unavailable).
- Evictions respect PodDisruptionBudgets, and validation runs as a Job pinned to the node with all its GPUs.
- A repeat-offender rule, dry-run mode, events and Prometheus metrics.
- The XID policy is based on NVIDIA's documentation (docs/xid-policy.md).

## How it is tested
A `gpu-sim` simulator stands in for dcgm-exporter. CI runs unit tests, shellcheck and an end-to-end test on kind with 8 scenarios (28 checks), green on the first run. There is also a `gpuremediate check` mode that uses nvidia-smi on a real GPU.

## Not tested yet
A real GPU: neither a real dcgm-exporter nor the check mode on a machine with one.""",
 es="""## Por qué este laboratorio
No tengo experiencia en producción con flotas de GPU. Este es el primero de una serie de laboratorios para aprender cómo se operan en el día a día, y cada README lo dice. No he pagado máquinas con GPU.

## Qué he hecho
Un controlador de Kubernetes en Go (solo librería estándar, sin client-go) que lee métricas DCGM (errores XID, ECC de doble bit, row remapping, temperatura) y lleva cada nodo por Healthy → Draining → Repairing → Validating → Healthy, o a Cordoned por temperatura, o a Quarantined.
- El estado vive en anotaciones del nodo, con un presupuesto de nodos en remediación (max-unavailable).
- Las evicciones respetan los PodDisruptionBudget y la validación es un Job fijado al nodo con todas sus GPU.
- Regla de reincidencia, modo dry-run, eventos y métricas de Prometheus.
- La política de XID se basa en la documentación de NVIDIA (docs/xid-policy.md).

## Cómo se prueba
Un simulador `gpu-sim` hace de dcgm-exporter. La CI pasa tests unitarios, shellcheck y una prueba de punta a punta en kind con 8 escenarios (28 comprobaciones), en verde a la primera. Hay además un modo `gpuremediate check` que usa nvidia-smi en una GPU real.

## Sin probar todavía
Una GPU real: ni un dcgm-exporter real ni el modo check en una máquina con GPU."""),

dict(n="10", repo="10-gpu-fleet-observability", date="2026-10-01", cat="gpu",
 title_en="Observability for a GPU fleet: alerts that say what to do", title_es="Observabilidad de una flota de GPU: alertas que dicen qué hacer",
 dek_en="Recording rules, alerts with runbooks, Alertmanager routing and a Grafana dashboard on DCGM metrics.",
 dek_es="Recording rules, alertas con runbook, rutas de Alertmanager y un dashboard de Grafana sobre métricas DCGM.",
 en="""## Why this lab
A learning lab, with no production GPU experience behind it. The question: which GPU metrics deserve an alert, and who should get it?

## What I built
- A Go simulator with 4 nodes × 8 GPUs that uses dcgm-exporter's metric names and labels, pod and namespace included, plus fault injection.
- 17 recording rules and 10 alerts, each with a runbook (docs/alerts.md) and an `action` label: drain, quarantine or cordon.
- Alertmanager with pager, ticket and team routes, and inhibitions so a broken GPU doesn't also alert the team about an "idle GPU".
- A Grafana dashboard generated by a script, and `fleetreport` with GPU-hours and idle GPU-hours per namespace.

## How it is tested
7 `promtool test rules` cases, Go tests, config checks, shellcheck and an end-to-end run with Docker Compose (Prometheus, Alertmanager, Grafana): 32 checks, green on the first run.

## What I learned
The energy-versus-power check gave false failures with a single sample because of scrape jitter. It now uses 1 minute of rate over 2 minutes of data.

## Not tested yet
A real dcgm-exporter.""",
 es="""## Por qué este laboratorio
Un laboratorio para aprender, sin experiencia de GPU en producción detrás. La pregunta: qué métricas de GPU merecen una alerta y a quién le tiene que llegar.

## Qué he hecho
- Un simulador en Go de 4 nodos × 8 GPU que usa los nombres y etiquetas de métricas de dcgm-exporter, pod y namespace incluidos, con inyección de fallos.
- 17 recording rules y 10 alertas, cada una con su runbook (docs/alerts.md) y una etiqueta `action`: drain, quarantine o cordon.
- Alertmanager con rutas a guardia, ticket y equipo, e inhibiciones para que una GPU rota no avise además de "GPU ociosa" al equipo.
- Un dashboard de Grafana generado por script y `fleetreport` con GPU-horas y GPU-horas ociosas por namespace.

## Cómo se prueba
7 casos de `promtool test rules`, tests en Go, comprobaciones de configuración, shellcheck y una prueba de punta a punta con Docker Compose (Prometheus, Alertmanager, Grafana): 32 comprobaciones, en verde a la primera.

## Qué aprendí
La comprobación de energía frente a potencia daba falsos fallos con una sola muestra por el jitter del scrape. Ahora usa 1 minuto sobre 2 minutos de datos.

## Sin probar todavía
Un dcgm-exporter real."""),

dict(n="11", repo="11-gpu-fleet-lifecycle", date="2026-10-02", cat="gpu",
 title_en="Rolling a GPU driver across a fleet: canary, approval, rollback", title_es="Desplegar un driver de GPU por la flota: canary, aprobación y rollback",
 dek_en="A Go controller that upgrades nodes in batches and backs out on its own when something breaks.",
 dek_es="Un controlador en Go que actualiza nodos por lotes y da marcha atrás solo cuando algo falla.",
 en="""## Why this lab
A learning lab on day-2 operations, without real GPUs. The README says that in production you would use the GPU Operator's own upgrade controller; this is about understanding what it has to get right.

## What I built
A Go controller (standard library only) that rolls a driver version across the fleet:
- Canary, human approval by rollout name, batches, a maintenance window, pause and abort, and a failure budget.
- maxUnavailable also counts nodes that are out for other reasons, such as the quarantine and remediation from lab 09.
- Each node goes Draining → Installing → Validating → Soaking → Done. A hardware XID or ECC error during the soak counts as a failure.
- On failure it rolls back to the previous version, and if that also fails, it quarantines the node with lab 09's label.

## How it is tested
The plan lives in a validated ConfigMap where unknown fields are errors. CI runs 12 controller unit tests, shellcheck and an end-to-end test on kind with 4 workers: 26 checks, green on the first run, including a closed window, a bad driver stopped at the canary and an XID during the soak with rollback.

## Not tested yet
Real GPUs and real drivers.""",
 es="""## Por qué este laboratorio
Un laboratorio sobre operaciones del día 2, sin GPU reales. El README dice que en producción se usaría el upgrade controller del propio GPU Operator; esto va de entender qué tiene que hacer bien.

## Qué he hecho
Un controlador en Go (solo librería estándar) que despliega una versión de driver por la flota:
- Canary, aprobación humana por nombre de rollout, lotes, ventana de mantenimiento, pausa y aborto, y presupuesto de fallos.
- maxUnavailable cuenta también los nodos que están fuera por otros motivos, como la cuarentena y la remediación del laboratorio 09.
- Cada nodo pasa por Draining → Installing → Validating → Soaking → Done. Un XID de hardware o un error ECC durante el soak cuenta como fallo.
- Si falla, vuelve a la versión anterior y, si eso también falla, pone el nodo en cuarentena con la etiqueta del laboratorio 09.

## Cómo se prueba
El plan vive en un ConfigMap validado donde los campos desconocidos son error. La CI pasa 12 tests unitarios del controlador, shellcheck y una prueba de punta a punta en kind con 4 workers: 26 comprobaciones, en verde a la primera, con ventana cerrada, un driver malo parado en el canary y un XID en el soak con rollback.

## Sin probar todavía
GPU y drivers reales."""),

dict(n="12", repo="12-gpu-goodput-mtbi", date="2026-10-02", cat="gpu",
 title_en="Where do the GPU-hours go? A goodput simulator", title_es="¿Adónde van las GPU-horas? Un simulador de goodput",
 dek_en="A 1,024-GPU training job, simulated with failures, to see what checkpoints, spares and fast detection are worth.",
 dek_es="Un entrenamiento de 1.024 GPU simulado con fallos, para ver cuánto valen los checkpoints, los spares y la detección rápida.",
 en="""## Why this lab
A learning lab. In a large training job, failures are normal; what matters is how much useful work survives them. I wanted to put numbers on that.

## What I built
- A discrete-event simulator of a 1,024-GPU job (128 nodes) with spares, failure causes with their own detection time, and repairs.
- An analyser that reads a JSONL event log and splits every GPU-hour into productive, checkpoint, lost work, detection, waiting for nodes and restart, charging the cost to each cause.
- MTBI and per-node MTBF, the Young and Daly formulas for checkpoint intervals, a goodput SLO with an error budget and an HTML report with SVG charts.

## What the numbers say
Seven scenarios, 20 seeds each: baseline 79.6 %, Daly's interval 85.1 %, asynchronous checkpoints 91.7 %, no spares 36.1 %, a firmware regression 73.5 %, and everything combined 94.0 %. The assumptions sit between two public references, Llama 3's interruption count and Meta's paper on cluster reliability.

## How it is tested
34 unit tests on Python 3.11 to 3.13, and a CI job that regenerates docs/results.md and fails if it changes.

## Not tested yet
Logs from a real cluster.""",
 es="""## Por qué este laboratorio
Un laboratorio para aprender. En un entrenamiento grande los fallos son normales; lo que importa es cuánto trabajo útil sobrevive. Quería ponerle números.

## Qué he hecho
- Un simulador de eventos discretos de un trabajo de 1.024 GPU (128 nodos) con spares, causas de fallo con su propio tiempo de detección y reparaciones.
- Un analizador que lee un log de eventos JSONL y reparte cada GPU-hora en productivo, checkpoint, trabajo perdido, detección, espera de nodos y reinicio, cargando el coste a cada causa.
- MTBI y MTBF por nodo, las fórmulas de Young y Daly para el intervalo de checkpoint, un SLO de goodput con presupuesto de error y un informe HTML con gráficos SVG.

## Lo que dicen los números
Siete escenarios con 20 semillas cada uno: base 79,6 %, intervalo de Daly 85,1 %, checkpoints asíncronos 91,7 %, sin spares 36,1 %, regresión de firmware 73,5 % y todo combinado 94,0 %. Los supuestos están entre dos referencias públicas: las interrupciones de Llama 3 y el paper de Meta sobre fiabilidad de clústeres.

## Cómo se prueba
34 tests unitarios en Python 3.11 a 3.13 y un job de CI que regenera docs/results.md y falla si cambia.

## Sin probar todavía
Logs de un clúster real."""),

dict(n="13", repo="13-cluster-acceptance-burnin", date="2026-10-04", cat="gpu",
 title_en="From handover to sign-off: accepting a new GPU cluster", title_es="Del handover a la firma: aceptar un clúster de GPU nuevo",
 dek_en="Inventory, diagnostics, NCCL tests and a 72-hour burn-in, ending in a report a customer can sign.",
 dek_es="Inventario, diagnósticos, pruebas NCCL y un burn-in de 72 horas, con un informe que el cliente puede firmar.",
 en="""## Why this lab
A learning lab. Accepting hardware is something I know from IT operations; here I wanted to see what it looks like for a GPU cluster.

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

## Not tested yet
Real dcgmi diag and nccl-tests output. The parsers follow the general format and are only tested with samples.""",
 es="""## Por qué este laboratorio
Un laboratorio para aprender. Aceptar hardware es algo que conozco de operaciones IT; aquí quería ver cómo es con un clúster de GPU.

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

## Sin probar todavía
Salidas reales de dcgmi diag y nccl-tests. Los parsers siguen el formato general y solo se prueban con muestras."""),

dict(n="14", repo="14-slurm-gpu-ops", date="2026-10-04", cat="gpu",
 title_en="A real Slurm cluster in Docker Compose, with GPU health checks", title_es="Un clúster Slurm real en Docker Compose, con health checks de GPU",
 dek_en="Drain, requeue and validate, and four CI iterations to get cgroups v2 working.",
 dek_es="Drain, requeue y validate, y cuatro iteraciones de CI para que funcionen los cgroups v2.",
 en="""## Why this lab
A learning lab. Many GPU clusters run Slurm rather than Kubernetes, so I wanted the same XID policy from lab 09 working in a real Slurm.

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

## Not tested yet
Real GPUs, cgroup isolation and NHC.""",
 es="""## Por qué este laboratorio
Un laboratorio para aprender. Muchos clústeres de GPU usan Slurm y no Kubernetes, así que quería la misma política de XID del laboratorio 09 funcionando en un Slurm real.

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

## Sin probar todavía
GPU reales, aislamiento por cgroups y NHC."""),

dict(n="15", repo="15-multi-tenant-gpu-scheduling", date="2026-10-05", cat="gpu",
 title_en="Sharing GPUs between teams with Kueue and KAI Scheduler", title_es="Repartir GPU entre equipos con Kueue y KAI Scheduler",
 dek_en="One quota agreement in a TOML file, rendered into both schedulers and tested on kind.",
 dek_es="Un acuerdo de cuotas en un fichero TOML, traducido a los dos planificadores y probado en kind.",
 en="""## Why this lab
A learning lab. When several teams share a GPU cluster, the hard part is the agreement: who is guaranteed what, who can borrow, and what happens when the owner wants it back.

## What I built
- `tenancy.toml` with three teams: training (16 guaranteed, 8 can be borrowed), research (8 + 8) and inference (8, never lent).
- `python -m tenancy render` turns it into Kueue ClusterQueues in a cohort and KAI Scheduler Queues. CI fails if the manifests drift from the file.
- A kind cluster with 4 workers × 8 GPUs simulated by Run:ai's fake-gpu-operator, plus KubeVirt.

## How it is tested
Kueue, 22 checks: borrowing, reclaim, priority within a team and all-or-nothing admission. KAI, 19 checks: two pods sharing one GPU at 0.5 each, over-quota, reclaim and gang scheduling. KubeVirt, 5 checks: a VM boots with QEMU emulation and the team's ResourceQuota rejects a second one.

## What I learned
Three rounds of fixes after the first CI run, written up in docs/decisions.md: queue usage is reported with a delay, the preemption reason is in a condition, and fractional GPUs are passed as text.

## Not tested yet
Real GPUs, Kueue and KAI together, fair sharing, topology-aware scheduling and KubeVirt with GPUs.""",
 es="""## Por qué este laboratorio
Un laboratorio para aprender. Cuando varios equipos comparten un clúster de GPU, lo difícil es el acuerdo: qué tiene garantizado cada uno, quién puede pedir prestado y qué pasa cuando el dueño lo quiere de vuelta.

## Qué he hecho
- `tenancy.toml` con tres equipos: training (16 garantizadas, 8 prestables), research (8 + 8) e inference (8 que nunca presta).
- `python -m tenancy render` lo convierte en ClusterQueues de Kueue dentro de una cohort y en Queues de KAI Scheduler. La CI falla si los manifiestos no coinciden con el fichero.
- Un clúster kind con 4 workers × 8 GPU simuladas por el fake-gpu-operator de Run:ai, más KubeVirt.

## Cómo se prueba
Kueue, 22 comprobaciones: préstamo, recuperación, prioridad dentro del equipo y admisión todo o nada. KAI, 19: dos pods compartiendo una GPU a 0,5 cada uno, exceso de cuota, recuperación y gang scheduling. KubeVirt, 5: una VM arranca con emulación QEMU y la ResourceQuota del equipo rechaza una segunda.

## Qué aprendí
Tres rondas de arreglos tras la primera CI, explicadas en docs/decisions.md: el uso de las colas se informa con retraso, el motivo de la preemption está en una condición y las GPU fraccionarias se pasan como texto.

## Sin probar todavía
GPU reales, Kueue y KAI juntos, fair sharing, planificación por topología y KubeVirt con GPU."""),

dict(n="16", repo="16-gitops-gpu-fleet", date="2026-10-09", cat="gpu",
 title_en="Promoting GPU Operator releases from staging to prod with Flux", title_es="Promocionar versiones del GPU Operator de staging a prod con Flux",
 dek_en="One file defines releases and clusters; Git and Flux do the rest, with a gate before production.",
 dek_es="Un fichero define versiones y clústeres; Git y Flux hacen el resto, con una puerta antes de producción.",
 en="""## Why this lab
A learning lab that ties several earlier ones together: how do you upgrade the GPU software stack across a fleet of clusters without doing it by hand?

## What I built
- `fleet.toml` defines releases (GPU Operator, Network Operator and driver versions, plus one release that fails on purpose) and clusters with GPU pools.
- Waves go staging → prod H100 → prod A100, with a pause after the canary.
- `python -m fleet render` writes each cluster's folder, and Flux applies it in three steps: operators → config → lifecycle. The lifecycle step is lab 11's controller, with its rollout plan generated from the same file.
- `fleet start / promote / approve` each edit one line, `fleet gate` checks the live clusters before promoting, and approving prod is a commit.

## How it is tested
CI: 21 unit tests; a validate step that renders the real NGC Helm charts at every version and checks them against the CRD schemas of that exact version (it catches a misspelt `nodeSelecter`); and a 20-minute end-to-end run with Gitea and two kind clusters, 29 checks, including drift corrected by Flux and a bad release stopped in staging.

## What I learned
One CI iteration: the rollout plan was applied before the NVIDIADriver objects, so lifecycle now depends on config. I also found a difference in the NVIDIADriver CRD between two GPU Operator versions.

## Not tested yet
Real GPUs and NICs, the GPU Operator's own upgrade controller, Argo CD and `flux bootstrap`.""",
 es="""## Por qué este laboratorio
Un laboratorio que une varios de los anteriores: cómo actualizar el software de GPU en una flota de clústeres sin hacerlo a mano.

## Qué he hecho
- `fleet.toml` define versiones (GPU Operator, Network Operator y driver, más una versión que falla a propósito) y clústeres con pools de GPU.
- Las olas van staging → prod H100 → prod A100, con una pausa tras el canary.
- `python -m fleet render` escribe la carpeta de cada clúster y Flux la aplica en tres pasos: operators → config → lifecycle. El paso lifecycle es el controlador del laboratorio 11, con su plan generado desde el mismo fichero.
- `fleet start / promote / approve` editan una línea cada uno, `fleet gate` revisa los clústeres vivos antes de promocionar y aprobar producción es un commit.

## Cómo se prueba
CI: 21 tests unitarios; un paso de validación que renderiza los charts de Helm reales de NGC en cada versión y los comprueba contra los esquemas de CRD de esa versión exacta (detecta un `nodeSelecter` mal escrito); y una prueba de punta a punta de 20 minutos con Gitea y dos clústeres kind, 29 comprobaciones, incluida la deriva corregida por Flux y una versión mala parada en staging.

## Qué aprendí
Una iteración de CI: el plan de rollout se aplicaba antes que los objetos NVIDIADriver, así que lifecycle ahora depende de config. También encontré una diferencia en el CRD NVIDIADriver entre dos versiones del GPU Operator.

## Sin probar todavía
GPU y NIC reales, el upgrade controller del propio GPU Operator, Argo CD y `flux bootstrap`."""),
]
