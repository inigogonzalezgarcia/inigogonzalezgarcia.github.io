"""IT guides (guias/). Level 1 topics and the guides under each one. Text in a small markup rendered by gmd() in build.py:
## / ### headings, - lists, 1. numbered steps, > tip, ! warning, **bold**, `code`, and two blocks:
:::term Title       a simulated terminal: lines starting with "$ " are commands (copied by the button), "# " are comments, the rest is output
:::ui Title         a simulated window: lines starting with "> " are a navigation path, "[ ]" / "[x]" are options, the rest is text
Both end with ":::". No real hostnames, users, tenants or company names: every example is fictional."""

LEVELS = {
    "nivel-1": dict(key="nivel-1", n_es="Nivel 1", n_en="Level 1", t_es="Primeros pasos", t_en="First steps",
                    h_es="Primeros pasos<br>en soporte IT.", h_en="First steps<br>in IT support.",
                    d_es="Lo que necesitas para empezar en soporte: el puesto, el usuario y sus herramientas.",
                    d_en="What you need to start in support: the device, the user and their tools.",
                    l_es="Once temas para empezar: el puesto, el usuario y sus herramientas. Paso a paso, con los comandos y las comprobaciones que harías en un ticket real.",
                    l_en="Eleven topics to get started: the device, the user and their tools. Step by step, with the commands and checks you would run on a real ticket.",
                    seo="Beginner IT support guides: Active Directory, Android, BitLocker, Cisco AnyConnect, printers, iPhone and iPad, Jira Service Management, Microsoft 365 licences, Teams, Outlook and Windows."),
    "nivel-2": dict(key="nivel-2", n_es="Nivel 2", n_en="Level 2", t_es="Base sólida", t_en="Solid foundations",
                    h_es="Servidores, despliegues<br>y los primeros scripts.", h_en="Servers, deployments<br>and your first scripts.",
                    d_es="Servidores, despliegue de aplicaciones y los primeros scripts.",
                    d_en="Servers, app deployment and your first scripts.",
                    l_es="Dieciséis temas para pasar del puesto de usuario a lo que hay detrás: servidores Windows y Linux, despliegue de aplicaciones, copias, escritorios virtuales, salas y los primeros scripts en PowerShell y Bash.",
                    l_en="Sixteen topics to move from the user's device to what sits behind it: Windows and Linux servers, app deployment, backups, virtual desktops, meeting rooms and your first PowerShell and Bash scripts.",
                    seo="Intermediate IT guides: Azure AD Connect, Bash, Citrix, Confluence, Git, Jamf Pro, MECM/SCCM, Microsoft Teams Rooms, PDQ and MDT, PowerShell, Red Hat, SharePoint, Ubuntu, Veeam, VMware Horizon and Windows Server."),
    "nivel-3": dict(key="nivel-3", n_es="Nivel 3", n_en="Level 3", t_es="Avanzado", t_en="Advanced",
                    h_es="Gestión moderna, identidad<br>y automatización.", h_en="Modern management, identity<br>and automation.",
                    d_es="Gestión moderna del puesto, identidad, virtualización y automatización.",
                    d_en="Modern device management, identity, virtualisation and automation.",
                    l_es="Diecisiete temas para quien ya administra: Intune en todas las plataformas, Entra ID y certificados, hipervisores, bases de datos, monitorización y logs, y la automatización con Ansible, Docker, Jenkins y Microsoft Graph.",
                    l_en="Seventeen topics for people who already administer: Intune on every platform, Entra ID and certificates, hypervisors, databases, monitoring and logs, and automation with Ansible, Docker, Jenkins and Microsoft Graph.",
                    seo="Advanced IT guides: Ansible, Docker, Elasticsearch and Kibana, Entra ID Conditional Access and SSO, Grafana, Hyper-V, Intune, Intune EPM, Jenkins, Linux joined to Active Directory, Microsoft Graph, NDES and Cloud PKI, PostgreSQL, MySQL and SQL Server, SolarWinds, Ubuntu Landscape, VMware vSphere."),
    "nivel-4": dict(key="nivel-4", n_es="Nivel 4", n_en="Level 4", t_es="Experto", t_en="Expert",
                    h_es="Infraestructura híbrida,<br>seguridad y continuidad.", h_en="Hybrid infrastructure,<br>security and continuity.",
                    d_es="Infraestructura híbrida, redes, seguridad y continuidad de negocio.",
                    d_en="Hybrid infrastructure, networking, security and business continuity.",
                    l_es="Para quien diseña, decide y responde cuando algo grande falla: escritorios en la nube, recuperación ante desastres, la red de una sede, el gobierno de los administradores de Microsoft 365, la detección con Sentinel y las migraciones de tenant. Seis temas ya publicados; el resto, en camino.",
                    l_en="For people who design, decide and respond when something big fails: cloud desktops, disaster recovery, a site's network, governing Microsoft 365 administrators, detection with Sentinel and tenant migrations. Six topics published so far; the rest are on the way.",
                    seo="Expert IT guides: Azure Virtual Desktop and Windows 365, backup and disaster recovery (DR/BCP), Cisco switches and routers, Microsoft 365 Global Admin and PIM, Microsoft Sentinel, and Microsoft 365 tenant migrations."),
}
LEVEL1 = LEVELS["nivel-1"]

# level, key, name_es, name_en, one-line description es/en
TOPICS = [
    ("nivel-1", "active-directory", "Active Directory: usuarios y grupos", "Active Directory: users and groups",
     "Altas, bajas, grupos y las incidencias de cada día: cuentas bloqueadas y contraseñas.",
     "Joiners, leavers, groups and the everyday tickets: locked accounts and passwords."),
    ("nivel-1", "android", "Android", "Android",
     "Móviles corporativos y perfil de trabajo con Intune.",
     "Corporate phones and the work profile with Intune."),
    ("nivel-1", "bitlocker", "BitLocker", "BitLocker",
     "Cifrado del disco, claves de recuperación y qué hacer cuando un equipo pide la clave.",
     "Disk encryption, recovery keys and what to do when a device asks for one."),
    ("nivel-1", "anyconnect", "Cisco AnyConnect (VPN)", "Cisco AnyConnect (VPN)",
     "Instalar el cliente, conectar y diagnosticar los fallos más habituales.",
     "Install the client, connect and diagnose the usual failures."),
    ("nivel-1", "impresoras", "Impresoras y periféricos", "Printers and peripherals",
     "Instalar una impresora de red, colas atascadas y periféricos que no responden.",
     "Install a network printer, stuck queues and peripherals that stop responding."),
    ("nivel-1", "ios", "iPhone y iPad", "iPhone and iPad",
     "Enrolar un dispositivo Apple en Intune y comprobar que recibe las políticas.",
     "Enrol an Apple device in Intune and check that it receives its policies."),
    ("nivel-1", "jira", "Jira Service Management: tickets", "Jira Service Management: tickets",
     "Abrir, clasificar, trabajar y cerrar un ticket de forma que ayude al siguiente.",
     "Open, classify, work and close a ticket in a way that helps the next person."),
    ("nivel-1", "m365", "Microsoft 365 y licencias", "Microsoft 365 and licences",
     "Asignar y retirar licencias, y saber qué incluye cada una.",
     "Assign and remove licences, and know what each one includes."),
    ("nivel-1", "teams", "Microsoft Teams", "Microsoft Teams",
     "Los problemas que más llegan al service desk y cómo resolverlos en minutos.",
     "The issues that reach the service desk most often, and how to fix them in minutes."),
    ("nivel-1", "outlook", "Outlook y Exchange Online", "Outlook and Exchange Online",
     "Buzones compartidos, permisos, respuestas automáticas y perfiles que no abren.",
     "Shared mailboxes, permissions, automatic replies and profiles that won't open."),
    ("nivel-1", "windows", "Windows 10 y 11", "Windows 10 and 11",
     "Diagnóstico básico de un equipo: lento, con errores o que no sincroniza con Intune.",
     "Basic diagnosis of a device: slow, throwing errors or not syncing with Intune."),
    # ---- Level 2
    ("nivel-2", "azure-ad-connect", "Azure AD Connect", "Azure AD Connect",
     "La sincronización entre Active Directory y Entra ID: forzar un ciclo y arreglar objetos que no pasan.",
     "The sync between Active Directory and Entra ID: force a cycle and fix objects that don't make it across."),
    ("nivel-2", "bash", "Bash", "Bash",
     "El primer script de comprobación de un servidor Linux, con las reglas que evitan los sustos.",
     "Your first health-check script for a Linux server, with the rules that avoid nasty surprises."),
    ("nivel-2", "citrix-vdi", "Citrix VDI", "Citrix VDI",
     "Publicar una aplicación y diagnosticar una sesión que no abre.",
     "Publish an application and diagnose a session that won't launch."),
    ("nivel-2", "confluence", "Confluence", "Confluence",
     "Montar el espacio de IT y escribir runbooks que el equipo use de verdad.",
     "Set up the IT space and write runbooks the team actually uses."),
    ("nivel-2", "git", "Git", "Git",
     "Poner los scripts del equipo bajo control de versiones: repo, ramas, commits y revisión.",
     "Put the team's scripts under version control: repo, branches, commits and review."),
    ("nivel-2", "jamf-pro", "Jamf Pro", "Jamf Pro",
     "Enrolar un Mac y desplegar una política con un grupo inteligente.",
     "Enrol a Mac and deploy a policy with a smart group."),
    ("nivel-2", "mecm-sccm", "MECM / SCCM: empaquetado de aplicaciones", "MECM / SCCM: app packaging",
     "Crear una aplicación, su método de detección y desplegarla a una colección.",
     "Create an application, its detection method, and deploy it to a collection."),
    ("nivel-2", "teams-rooms", "Microsoft Teams Rooms", "Microsoft Teams Rooms",
     "Poner en marcha una sala: cuenta de recurso, licencia, inicio de sesión y supervisión.",
     "Bring a room online: resource account, licence, sign-in and monitoring."),
    ("nivel-2", "pdq-mdt", "PDQ y MDT", "PDQ and MDT",
     "Desplegar software en lote con PDQ e instalar Windows desde cero con MDT.",
     "Deploy software in bulk with PDQ and install Windows from scratch with MDT."),
    ("nivel-2", "powershell", "PowerShell", "PowerShell",
     "Un script de inventario que se ejecuta en remoto, maneja errores y deja un CSV.",
     "An inventory script that runs remotely, handles errors and leaves a CSV."),
    ("nivel-2", "rhel", "Red Hat Enterprise Linux", "Red Hat Enterprise Linux",
     "Registrar el sistema, parchear, y controlar servicios, firewall y SELinux.",
     "Register the system, patch it, and manage services, the firewall and SELinux."),
    ("nivel-2", "sharepoint", "SharePoint", "SharePoint",
     "Crear un sitio de equipo, dar permisos bien y entender el uso compartido.",
     "Create a team site, grant permissions properly and understand sharing."),
    ("nivel-2", "ubuntu", "Ubuntu", "Ubuntu",
     "Un Ubuntu Server recién instalado: usuarios, SSH con claves, firewall y actualizaciones.",
     "A freshly installed Ubuntu Server: users, SSH with keys, firewall and updates."),
    ("nivel-2", "veeam", "Veeam Backup", "Veeam Backup",
     "Crear un trabajo de copia, comprobar que termina bien y hacer una restauración de prueba.",
     "Create a backup job, check it completes, and run a test restore."),
    ("nivel-2", "vmware-horizon", "VMware Horizon", "VMware Horizon",
     "Un pool de escritorios desde una imagen maestra y el diagnóstico de una conexión que falla.",
     "A desktop pool from a golden image, and diagnosing a connection that fails."),
    ("nivel-2", "windows-server", "Windows Server", "Windows Server",
     "Instalar un rol, parchear sin cortar el servicio y leer los eventos que importan.",
     "Install a role, patch without cutting the service, and read the events that matter."),
    # ---- Level 3
    ("nivel-3", "ansible", "Ansible", "Ansible",
     "El primer playbook: inventario, parcheo de servidores Linux servidor a servidor y comprobación.",
     "Your first playbook: inventory, patching Linux servers one at a time, and verification."),
    ("nivel-3", "docker", "Docker", "Docker",
     "Contenedores en un servidor de operaciones: imágenes, volúmenes, Compose y qué mirar cuando uno se cae.",
     "Containers on an operations server: images, volumes, Compose and what to look at when one dies."),
    ("nivel-3", "elk", "Elasticsearch, Logstash y Kibana", "Elasticsearch, Logstash and Kibana",
     "Centralizar los logs de servidores y buscar un error en Kibana en lugar de en veinte máquinas.",
     "Centralise server logs and search for an error in Kibana instead of on twenty machines."),
    ("nivel-3", "conditional-access", "Entra ID: Conditional Access", "Entra ID: Conditional Access",
     "Las políticas base, el modo solo informe y cómo leer por qué un usuario se queda bloqueado.",
     "The baseline policies, report-only mode and how to read why a user gets blocked."),
    ("nivel-3", "entra-sso", "Entra ID: SSO, SAML y App Registrations", "Entra ID: SSO, SAML and App Registrations",
     "Dar de alta una aplicación con SAML, asignar usuarios y diagnosticar un inicio de sesión que falla.",
     "Onboard an application with SAML, assign users and diagnose a sign-in that fails."),
    ("nivel-3", "grafana", "Grafana", "Grafana",
     "Un origen de datos, el primer panel y una alerta que avisa al canal del equipo.",
     "A data source, your first dashboard and an alert that notifies the team channel."),
    ("nivel-3", "hyper-v", "Hyper-V", "Hyper-V",
     "Crear una máquina virtual, el conmutador virtual, puntos de control y la exportación.",
     "Create a virtual machine, the virtual switch, checkpoints and export."),
    ("nivel-3", "intune", "Intune: Windows, macOS, iOS y Android", "Intune: Windows, macOS, iOS and Android",
     "Perfiles de configuración y cumplimiento por plataforma, y un dispositivo que no cumple.",
     "Configuration and compliance profiles per platform, and a device that is non-compliant."),
    ("nivel-3", "intune-epm", "Intune EPM", "Intune EPM",
     "Quitar el administrador local y elevar solo lo que hace falta con Endpoint Privilege Management.",
     "Remove local admin and elevate only what is needed with Endpoint Privilege Management."),
    ("nivel-3", "jenkins", "Jenkins (CI/CD)", "Jenkins (CI/CD)",
     "Un pipeline que prueba los scripts del equipo en cada cambio y avisa cuando algo se rompe.",
     "A pipeline that tests the team's scripts on every change and shouts when something breaks."),
    ("nivel-3", "linux-ad", "Linux integrado con Active Directory", "Linux joined to Active Directory",
     "Unir un servidor Linux al dominio con SSSD: login con la cuenta de AD, sudo por grupo y diagnóstico.",
     "Join a Linux server to the domain with SSSD: log in with the AD account, sudo by group, and diagnosis."),
    ("nivel-3", "graph", "Microsoft Graph", "Microsoft Graph",
     "Las primeras consultas con PowerShell: permisos, usuarios, dispositivos y un informe que no existe en el portal.",
     "Your first queries with PowerShell: permissions, users, devices and a report the portal doesn't have."),
    ("nivel-3", "ndes-pki", "NDES y Cloud PKI", "NDES and Cloud PKI",
     "Certificados a los dispositivos desde Intune: la cadena, el perfil SCEP y un certificado que no llega.",
     "Certificates to devices from Intune: the chain, the SCEP profile and a certificate that never arrives."),
    ("nivel-3", "databases", "PostgreSQL, MySQL y SQL Server", "PostgreSQL, MySQL and SQL Server",
     "Lo que operaciones hace con una base de datos: conectar, copia y restauración, espacio, usuarios y una consulta lenta.",
     "What operations does with a database: connect, back up and restore, disk space, users and a slow query."),
    ("nivel-3", "solarwinds", "SolarWinds", "SolarWinds",
     "Añadir un nodo, afinar una alerta que salta demasiado y leer qué pasó antes de la caída.",
     "Add a node, tune an alert that fires too much and read what happened before the outage."),
    ("nivel-3", "landscape", "Ubuntu Landscape", "Ubuntu Landscape",
     "Registrar la flota de Ubuntu, parchear por grupos con ventana y comprobar reinicios pendientes.",
     "Register the Ubuntu fleet, patch by group within a window and check for pending reboots."),
    ("nivel-3", "vsphere", "VMware vSphere y vCenter", "VMware vSphere and vCenter",
     "Crear una máquina virtual, snapshots con fecha de caducidad y poner un host en mantenimiento sin cortar nada.",
     "Create a virtual machine, snapshots with an expiry date, and put a host into maintenance without cutting anything."),
    # ---- Level 4
    ("nivel-4", "avd-w365", "Azure Virtual Desktop y Windows 365", "Azure Virtual Desktop and Windows 365",
     "Cuándo usar cada uno, un host pool con FSLogix y escalado automático, y una conexión que falla.",
     "When to use each, a host pool with FSLogix and autoscaling, and a connection that fails."),
    ("nivel-4", "dr-bcp", "Backup y recuperación ante desastres (DR/BCP)", "Backup and disaster recovery (DR/BCP)",
     "RPO y RTO por servicio, copias inmutables, el plan de recuperación y una prueba completa medida.",
     "RPO and RTO per service, immutable backups, the recovery plan and a measured full test."),
    ("nivel-4", "cisco", "Cisco: switches y routers", "Cisco switches and routers",
     "VLANs, troncales sin cortar una planta, el router con circuito de respaldo y un puerto que no da red.",
     "VLANs, trunks without cutting off a floor, the router with a backup circuit and a port that gives no network."),
    ("nivel-4", "m365-pim", "Microsoft 365: Global Admin y PIM", "Microsoft 365: Global Admin and PIM",
     "Roles mínimos, cuentas de emergencia y administradores que activan su rol solo cuando lo necesitan.",
     "Least-privileged roles, emergency accounts and administrators who activate their role only when they need it."),
    ("nivel-4", "sentinel", "Microsoft Sentinel", "Microsoft Sentinel",
     "Conectores, una regla de análisis en KQL, la automatización y un incidente de principio a fin.",
     "Connectors, a KQL analytics rule, automation and an incident from start to finish."),
    ("nivel-4", "tenant-migration", "Migraciones de tenant Microsoft 365", "Microsoft 365 tenant migrations",
     "Inventario, identidades, buzones entre tenants, OneDrive, dispositivos y el fin de semana del corte.",
     "Inventory, identities, cross-tenant mailboxes, OneDrive, devices and the cutover weekend."),
]

GUIDES = []
def g(**k): GUIDES.append(k)

# ---------------------------------------------------------------- 1 · Active Directory
g(slug="active-directory-alta-usuario-grupos", topic="active-directory", date="2026-10-21",
  title_es="Alta de un usuario en Active Directory y sus grupos",
  title_en="Creating a user in Active Directory and adding them to groups",
  dek_es="Crear la cuenta, ponerla en la OU correcta, añadir los grupos y comprobar que todo está bien antes de avisar al usuario.",
  dek_en="Create the account, place it in the right OU, add the groups and check everything before telling the user.",
  es="""
## Qué vas a conseguir

Una cuenta nueva en Active Directory lista para el primer día: en su unidad organizativa (OU), con los grupos que le dan acceso a carpetas y aplicaciones, y con la contraseña inicial que el usuario cambiará en su primer inicio de sesión.

## Antes de empezar

- Una cuenta de administración delegada sobre la OU (no uses tu cuenta de usuario diario).
- El ticket con los datos: nombre, departamento, responsable y a quién tiene que parecerse (el "usuario modelo" del mismo equipo).
- Las herramientas RSAT instaladas: **Usuarios y equipos de Active Directory** y el módulo de PowerShell.

> Si tu empresa tiene un proceso de alta automatizado (RRHH → identidad), esta guía te sirve para entender lo que hace por debajo y para corregir lo que el proceso no cubre.

## 1. Mira cómo está el usuario modelo

Antes de crear nada, copia la referencia. Así evitas inventarte grupos o OUs.

:::term PowerShell · RSAT
$ Get-ADUser modelo.ventas -Properties MemberOf, Department, Title, Manager | Select-Object SamAccountName, DistinguishedName, Department, Title
SamAccountName    : modelo.ventas
DistinguishedName : CN=Modelo Ventas,OU=Ventas,OU=Usuarios,DC=contoso,DC=local
Department        : Ventas
Title             : Account Manager
$ (Get-ADUser modelo.ventas -Properties MemberOf).MemberOf | ForEach-Object { ($_ -split ",")[0] -replace "CN=" }
GG-Ventas
GG-Carpeta-Ventas-RW
GG-App-CRM-Usuarios
GG-VPN-Usuarios
:::

Apunta la OU (`OU=Ventas,OU=Usuarios`) y la lista de grupos. Si el modelo tiene un grupo que parece de otra época (una app retirada, un proyecto cerrado), no lo copies: pregúntalo en el ticket.

## 2. Crea la cuenta

En la consola gráfica: botón derecho sobre la OU → **Nuevo → Usuario**. Rellena nombre, apellidos, nombre de inicio de sesión y marca **El usuario debe cambiar la contraseña en el siguiente inicio de sesión**.

Con PowerShell es lo mismo, y queda registrado en el ticket tal cual lo ejecutaste:

:::term PowerShell · RSAT
$ $pwd = Read-Host "Contraseña inicial" -AsSecureString
$ New-ADUser -Name "Laura Prado" -GivenName Laura -Surname Prado -SamAccountName laura.prado -UserPrincipalName laura.prado@contoso.com -Path "OU=Ventas,OU=Usuarios,DC=contoso,DC=local" -Department Ventas -Title "Account Manager" -AccountPassword $pwd -ChangePasswordAtLogon $true -Enabled $true
$ Get-ADUser laura.prado | Select-Object Enabled, UserPrincipalName, DistinguishedName
Enabled           : True
UserPrincipalName : laura.prado@contoso.com
DistinguishedName : CN=Laura Prado,OU=Ventas,OU=Usuarios,DC=contoso,DC=local
:::

! El `UserPrincipalName` tiene que coincidir con el correo que tendrá el usuario. Si no, el inicio de sesión en Microsoft 365 y en las aplicaciones con SSO fallará aunque la cuenta de AD esté perfecta.

## 3. Añade los grupos

:::term PowerShell · RSAT
$ "GG-Ventas","GG-Carpeta-Ventas-RW","GG-App-CRM-Usuarios","GG-VPN-Usuarios" | ForEach-Object { Add-ADGroupMember -Identity $_ -Members laura.prado }
$ (Get-ADUser laura.prado -Properties MemberOf).MemberOf.Count
4
:::

Los grupos de seguridad se aplican en el siguiente inicio de sesión del usuario. Si ya había iniciado sesión, tiene que cerrarla y volver a entrar (o ejecutar `klist purge` y volver a abrir la carpeta).

## 4. Comprueba

- La cuenta está habilitada y en la OU correcta.
- Los grupos coinciden con el modelo.
- Si hay sincronización con Entra ID (Azure AD Connect), espera al siguiente ciclo (normalmente 30 minutos) o pide que lo fuercen. El usuario aparecerá en Microsoft 365 y entonces se le podrá asignar la licencia.
- Deja en el ticket el nombre de inicio de sesión, la OU y los grupos. La contraseña inicial se entrega por un canal aparte, nunca en el ticket.

## Las incidencias que llegarán después

:::term PowerShell · RSAT
# ¿Cuenta bloqueada por intentos fallidos?
$ Get-ADUser laura.prado -Properties LockedOut, BadLogonCount, LastBadPasswordAttempt | Select-Object LockedOut, BadLogonCount, LastBadPasswordAttempt
LockedOut              : True
BadLogonCount          : 5
LastBadPasswordAttempt : 21/10/2026 9:02:14
$ Unlock-ADAccount -Identity laura.prado
# Restablecer la contraseña y forzar el cambio
$ Set-ADAccountPassword -Identity laura.prado -Reset -NewPassword (Read-Host "Nueva" -AsSecureString)
$ Set-ADUser -Identity laura.prado -ChangePasswordAtLogon $true
:::

Si una cuenta se bloquea una y otra vez, el origen suele ser una contraseña antigua guardada en un móvil, una unidad de red mapeada o una tarea programada. El atributo `LastBadPasswordAttempt` y el visor de eventos del controlador de dominio (evento 4740) te dicen desde qué equipo viene.

## Siguientes pasos

- Haz una plantilla de PowerShell por departamento: OU y grupos fijos, y solo cambian nombre y cargo.
- Aprende a leer `Get-ADPrincipalGroupMembership` para auditorías de acceso.
- En el Nivel 2 verás cómo Azure AD Connect lleva estas cuentas a Entra ID y qué atributos importan.
""",
  en="""
## What you'll get

A new Active Directory account ready for day one: in its organisational unit (OU), with the groups that give access to folders and applications, and with an initial password the user will change at first sign-in.

## Before you start

- A delegated admin account over the OU (not your everyday user account).
- The ticket with the details: name, department, manager and who to mirror (the "model user" from the same team).
- The RSAT tools installed: **Active Directory Users and Computers** and the PowerShell module.

> If your company has an automated joiner process (HR → identity), this guide helps you understand what it does underneath and fix what the process doesn't cover.

## 1. Look at the model user

Before creating anything, copy the reference. That way you don't invent groups or OUs.

:::term PowerShell · RSAT
$ Get-ADUser model.sales -Properties MemberOf, Department, Title, Manager | Select-Object SamAccountName, DistinguishedName, Department, Title
SamAccountName    : model.sales
DistinguishedName : CN=Model Sales,OU=Sales,OU=Users,DC=contoso,DC=local
Department        : Sales
Title             : Account Manager
$ (Get-ADUser model.sales -Properties MemberOf).MemberOf | ForEach-Object { ($_ -split ",")[0] -replace "CN=" }
GG-Sales
GG-Folder-Sales-RW
GG-App-CRM-Users
GG-VPN-Users
:::

Note the OU (`OU=Sales,OU=Users`) and the group list. If the model has a group that looks like a leftover (a retired app, a closed project), don't copy it: ask in the ticket.

## 2. Create the account

In the GUI: right-click the OU → **New → User**. Fill in first name, last name and logon name, and tick **User must change password at next logon**.

PowerShell does the same, and it goes into the ticket exactly as you ran it:

:::term PowerShell · RSAT
$ $pwd = Read-Host "Initial password" -AsSecureString
$ New-ADUser -Name "Laura Prado" -GivenName Laura -Surname Prado -SamAccountName laura.prado -UserPrincipalName laura.prado@contoso.com -Path "OU=Sales,OU=Users,DC=contoso,DC=local" -Department Sales -Title "Account Manager" -AccountPassword $pwd -ChangePasswordAtLogon $true -Enabled $true
$ Get-ADUser laura.prado | Select-Object Enabled, UserPrincipalName, DistinguishedName
Enabled           : True
UserPrincipalName : laura.prado@contoso.com
DistinguishedName : CN=Laura Prado,OU=Sales,OU=Users,DC=contoso,DC=local
:::

! The `UserPrincipalName` has to match the email address the user will have. Otherwise sign-in to Microsoft 365 and to SSO applications fails even though the AD account is perfect.

## 3. Add the groups

:::term PowerShell · RSAT
$ "GG-Sales","GG-Folder-Sales-RW","GG-App-CRM-Users","GG-VPN-Users" | ForEach-Object { Add-ADGroupMember -Identity $_ -Members laura.prado }
$ (Get-ADUser laura.prado -Properties MemberOf).MemberOf.Count
4
:::

Security groups apply at the user's next sign-in. If they were already signed in, they need to sign out and back in (or run `klist purge` and reopen the folder).

## 4. Check

- The account is enabled and in the right OU.
- The groups match the model.
- If there is synchronisation with Entra ID (Azure AD Connect), wait for the next cycle (usually 30 minutes) or ask for it to be forced. The user then appears in Microsoft 365 and can get a licence.
- Leave the logon name, OU and groups in the ticket. The initial password goes through a separate channel, never in the ticket.

## The tickets that come later

:::term PowerShell · RSAT
# Locked out after failed attempts?
$ Get-ADUser laura.prado -Properties LockedOut, BadLogonCount, LastBadPasswordAttempt | Select-Object LockedOut, BadLogonCount, LastBadPasswordAttempt
LockedOut              : True
BadLogonCount          : 5
LastBadPasswordAttempt : 21/10/2026 9:02:14
$ Unlock-ADAccount -Identity laura.prado
# Reset the password and force a change
$ Set-ADAccountPassword -Identity laura.prado -Reset -NewPassword (Read-Host "New" -AsSecureString)
$ Set-ADUser -Identity laura.prado -ChangePasswordAtLogon $true
:::

If an account locks again and again, the cause is usually an old password saved on a phone, a mapped network drive or a scheduled task. The `LastBadPasswordAttempt` attribute and the domain controller's event log (event 4740) tell you which device it comes from.

## Next steps

- Make a PowerShell template per department: fixed OU and groups, only name and title change.
- Learn to read `Get-ADPrincipalGroupMembership` for access audits.
- In Level 2 you'll see how Azure AD Connect takes these accounts to Entra ID and which attributes matter.
""")

# ---------------------------------------------------------------- 2 · Android
g(slug="android-perfil-de-trabajo-intune", topic="android", date="2026-10-21",
  title_es="Enrolar un Android con perfil de trabajo en Intune",
  title_en="Enrolling an Android phone with a work profile in Intune",
  dek_es="Qué le pides al usuario, qué hace el Portal de empresa y cómo compruebas que el perfil de trabajo recibe las políticas y las aplicaciones.",
  dek_en="What you ask the user to do, what Company Portal does, and how you check that the work profile receives its policies and apps.",
  es="""
## Qué vas a conseguir

Un móvil Android personal o corporativo con un **perfil de trabajo**: un contenedor separado donde viven el correo, Teams y las aplicaciones de la empresa, con sus políticas, sin tocar las fotos ni las apps personales del usuario. Es el modelo más habitual para "trae tu propio móvil" y el más fácil de dar soporte.

## Antes de empezar

- El usuario tiene licencia que incluye Intune y cuenta en Entra ID.
- En Intune, **Inscripción de Android → Perfil de trabajo de propiedad personal** está permitido para su grupo (si no, el Portal de empresa dirá que el dispositivo no se puede inscribir).
- El móvil tiene Android 8 o superior, Google Play y espacio libre. Los teléfonos sin servicios de Google (algunos modelos chinos) no pueden crear perfil de trabajo.
- Si usáis Conditional Access, el usuario verá "necesitas registrar el dispositivo" al abrir Outlook o Teams: es el camino esperado, no un error.

## 1. Lo que hace el usuario

Mándale estos pasos tal cual. Son cinco minutos.

:::ui Android · Portal de empresa
> Google Play › Intune Company Portal › Instalar
> Portal de empresa › Iniciar sesión › laura.prado@contoso.com
> Configuración del acceso › Comenzar
[x] Crear perfil de trabajo
[x] Aceptar los términos de Google
> Registro del dispositivo › Activar el perfil de trabajo
= Estado: Configurando el perfil de trabajo…
[Siguiente]
:::

Al terminar, Android muestra una pestaña **Trabajo** en el cajón de aplicaciones, y las apps de trabajo llevan un maletín pequeño en el icono. Outlook, Teams y Authenticator aparecen allí solas si están asignadas como obligatorias.

> Si el usuario ya tenía Outlook instalado en la parte personal, que lo deje: el de trabajo es otra copia y la cuenta corporativa solo entra en esa.

## 2. Comprueba en Intune

:::ui Intune · Dispositivos › Android
> Dispositivos › Android › Dispositivos Android
= Nombre: Laura_AndroidForWork_21/10/2026
= Propiedad: Personal
= Tipo de inscripción: Perfil de trabajo de propiedad personal
= Cumplimiento: Conforme
= Último check-in: 21/10/2026 10:14
[Sincronizar] [Retirar] [Restablecer código de acceso]
:::

Si aparece **No conforme**, entra en el dispositivo → **Cumplimiento del dispositivo** y mira qué regla falla. Las habituales: versión de Android por debajo del mínimo, sin bloqueo de pantalla, o el dispositivo está rooteado. La política de cumplimiento te lo dice y el Portal de empresa se lo dice al usuario con el mismo texto.

## 3. Las aplicaciones no llegan

La causa más común es la espera: Google Play administrado tarda unos minutos en instalar en el perfil de trabajo. Si pasan más de 15:

1. En el móvil: Portal de empresa → **Dispositivos** → el móvil → **Comprobar estado**. Eso fuerza un check-in.
2. En Intune: **Aplicaciones → Android → la app → Estado de instalación del dispositivo**. Si pone "No aplicable", el grupo asignado no incluye al usuario o la app está asignada como disponible y no obligatoria.
3. Si la app es de Google Play administrado, comprueba que está **aprobada** en Google Play administrado y sincronizada con Intune (Aplicaciones → Google Play administrado → Sincronizar).

## 4. Retirar el perfil (baja o cambio de móvil)

Desde Intune, **Retirar** borra solo el perfil de trabajo: correo, apps y datos de empresa. Las fotos y las apps personales no se tocan. Desde el móvil, el usuario puede hacerlo en Ajustes → Cuentas → **Quitar perfil de trabajo**. Apunta en el ticket la fecha y desde dónde se retiró.

! **Borrar** (wipe) devuelve el móvil a fábrica y solo tiene sentido en dispositivos corporativos. En un móvil personal, retira, no borres.

## Siguientes pasos

- Para móviles corporativos sin uso personal, mira el modo **dispositivo dedicado** o **totalmente administrado** con Zero-touch.
- Las políticas de protección de aplicaciones (APP/MAM) permiten proteger Outlook y Teams sin inscribir el dispositivo. Es la alternativa cuando el usuario no quiere perfil de trabajo.
- Un filtro de dispositivos por fabricante y versión de Android evita sorpresas con modelos sin servicios de Google.
""",
  en="""
## What you'll get

A personal or corporate Android phone with a **work profile**: a separate container where company email, Teams and apps live with their policies, without touching the user's photos or personal apps. It is the most common model for "bring your own phone" and the easiest to support.

## Before you start

- The user has a licence that includes Intune and an account in Entra ID.
- In Intune, **Android enrolment → Personally-owned work profile** is allowed for their group (otherwise Company Portal says the device cannot be enrolled).
- The phone runs Android 8 or later, has Google Play and free space. Phones without Google services (some Chinese models) cannot create a work profile.
- If you use Conditional Access, the user sees "you need to register this device" when opening Outlook or Teams: that is the expected path, not an error.

## 1. What the user does

Send them these steps as they are. It takes five minutes.

:::ui Android · Company Portal
> Google Play › Intune Company Portal › Install
> Company Portal › Sign in › laura.prado@contoso.com
> Access setup › Begin
[x] Create work profile
[x] Accept Google's terms
> Device registration › Activate work profile
= Status: Setting up your work profile…
[Next]
:::

When it finishes, Android shows a **Work** tab in the app drawer, and work apps carry a small briefcase on their icon. Outlook, Teams and Authenticator appear there on their own if they are assigned as required.

> If the user already had Outlook installed on the personal side, they can leave it: the work one is a separate copy and the corporate account only signs in there.

## 2. Check in Intune

:::ui Intune · Devices › Android
> Devices › Android › Android devices
= Name: Laura_AndroidForWork_21/10/2026
= Ownership: Personal
= Enrolment type: Personally-owned work profile
= Compliance: Compliant
= Last check-in: 21/10/2026 10:14
[Sync] [Retire] [Reset passcode]
:::

If it shows **Not compliant**, open the device → **Device compliance** and see which rule fails. The usual ones: Android version below the minimum, no screen lock, or the device is rooted. The compliance policy tells you, and Company Portal tells the user with the same text.

## 3. The apps don't arrive

The most common cause is waiting: managed Google Play takes a few minutes to install into the work profile. If it has been more than 15:

1. On the phone: Company Portal → **Devices** → the phone → **Check status**. That forces a check-in.
2. In Intune: **Apps → Android → the app → Device install status**. If it says "Not applicable", the assigned group does not include the user, or the app is assigned as available rather than required.
3. If the app comes from managed Google Play, check it is **approved** in managed Google Play and synced with Intune (Apps → Managed Google Play → Sync).

## 4. Retire the profile (leaver or new phone)

From Intune, **Retire** removes only the work profile: email, apps and company data. Photos and personal apps are untouched. From the phone, the user can do it in Settings → Accounts → **Remove work profile**. Note the date and where it was retired from in the ticket.

! **Wipe** returns the phone to factory settings and only makes sense on corporate devices. On a personal phone, retire, don't wipe.

## Next steps

- For corporate phones with no personal use, look at **dedicated** or **fully managed** mode with Zero-touch.
- App protection policies (APP/MAM) protect Outlook and Teams without enrolling the device. That is the alternative when the user does not want a work profile.
- A device filter by manufacturer and Android version avoids surprises with models that lack Google services.
""")

# ---------------------------------------------------------------- 3 · BitLocker
g(slug="bitlocker-estado-y-clave-de-recuperacion", topic="bitlocker", date="2026-10-21",
  title_es="BitLocker: comprobar el cifrado y recuperar un equipo que pide la clave",
  title_en="BitLocker: checking encryption and recovering a device that asks for the key",
  dek_es="Ver si el disco está cifrado, dónde está guardada la clave de recuperación y qué hacer cuando un portátil arranca en la pantalla azul de BitLocker.",
  dek_en="See whether the disk is encrypted, where the recovery key is stored, and what to do when a laptop boots into the blue BitLocker screen.",
  es="""
## Qué vas a conseguir

Saber en un minuto si un equipo está cifrado y con qué protector, encontrar la clave de recuperación en Entra ID o en Active Directory, y devolver a un usuario su portátil cuando aparece la pantalla azul que pide 48 dígitos.

## Antes de empezar

- Para leer el estado del equipo necesitas una consola de PowerShell **como administrador** en ese equipo.
- Para ver claves de recuperación necesitas un rol que las muestre: en Entra ID, **Helpdesk Administrator** o un rol personalizado con `microsoft.directory/bitlockerKeys/key/read`; en Active Directory, permiso de lectura sobre el objeto equipo con RSAT y la pestaña de recuperación de BitLocker instalada.
- Cada lectura de una clave queda en el registro de auditoría. Es normal y es bueno: escribe el número de ticket en tus notas.

## 1. Comprueba el estado del cifrado

:::term PowerShell · como administrador
$ manage-bde -status C:
Volumen C: [Windows]
[Volumen del sistema operativo]
    Tamaño:                 476,00 GB
    Versión de BitLocker:   2.0
    Estado de la conversión: Cifrado completo
    Porcentaje cifrado:     100,0 %
    Método de cifrado:      XTS-AES 128
    Estado de la protección: Protección activada
    Protectores de clave:
        TPM
        Contraseña numérica
$ Get-BitLockerVolume C: | Select-Object VolumeStatus, ProtectionStatus, EncryptionPercentage, KeyProtector
VolumeStatus         : FullyEncrypted
ProtectionStatus     : On
EncryptionPercentage : 100
KeyProtector         : {Tpm, RecoveryPassword}
:::

Lo que quieres ver: **Cifrado completo**, **Protección activada** y dos protectores, `TPM` y `Contraseña numérica` (la clave de recuperación). Si la protección está **desactivada**, el disco está cifrado pero cualquiera puede arrancarlo: suele ser porque alguien la suspendió para una actualización de firmware y no se reanudó.

:::term PowerShell · como administrador
# Reanudar la protección si estaba suspendida
$ Resume-BitLocker -MountPoint C:
# Confirmar que la clave de recuperación está guardada en Entra ID (equipos unidos o registrados en Entra)
$ $kp = (Get-BitLockerVolume C:).KeyProtector | Where-Object KeyProtectorType -eq "RecoveryPassword"
$ BackupToAAD-BitLockerKeyProtector -MountPoint C: -KeyProtectorId $kp.KeyProtectorId
:::

## 2. Encuentra la clave de recuperación

En un equipo gestionado con Intune la clave está en Entra ID. Busca el equipo por nombre y abre **Claves de BitLocker**.

:::ui Entra ID · Dispositivos
> Entra ID › Dispositivos › Todos los dispositivos › LAPTOP-7F2K9Q › Claves de BitLocker
= Id. de clave: 7a1c…-…-…-…-…3e9d
= Unidad: Unidad del sistema operativo
= Clave de recuperación: 123456-654321-112233-445566-778899-998877-665544-332211
[Mostrar clave de recuperación]
:::

En un dominio clásico, la clave está en el objeto **equipo** de Active Directory, pestaña **Recuperación de BitLocker**, siempre que la directiva de grupo la guarde allí. Si el equipo es híbrido, mira primero en Entra ID.

! Comprueba que el **Id. de clave** coincide con los 8 primeros caracteres que muestra la pantalla azul del portátil. Un equipo puede tener varias claves (una por cada vez que se cifró) y solo una vale.

## 3. El portátil pide la clave de recuperación

Pasa casi siempre después de una de estas cosas: actualización de BIOS/firmware, cambio en la placa o en el orden de arranque, Secure Boot desactivado, o un disco que se ha movido de equipo. Es BitLocker haciendo su trabajo.

1. Pide al usuario el **Id. de clave** que ve en pantalla (los primeros 8 caracteres bastan) y el nombre del equipo (en la etiqueta o en el ticket).
2. Busca la clave como en el paso 2 y dictásela por teléfono o por un canal cifrado. Nunca la pegues en el ticket ni en un correo.
3. Cuando arranque, inicia sesión y comprueba por qué saltó: si fue una actualización de firmware ya está; si Secure Boot está desactivado, actívalo.
4. Si va a volver a pedirla en cada arranque, **suspende y reanuda** la protección una vez para que el TPM vuelva a sellar las medidas de arranque:

:::term PowerShell · como administrador
$ Suspend-BitLocker -MountPoint C: -RebootCount 1
$ Restart-Computer
# Tras el reinicio, la protección se reanuda sola. Compruébalo:
$ (Get-BitLockerVolume C:).ProtectionStatus
On
:::

5. Si tu política lo exige, **rota la clave de recuperación** después de usarla. Desde Intune: el dispositivo → **Rotación de la clave de BitLocker**. Así la clave que se dictó por teléfono deja de valer.

## 4. Un equipo nuevo no se cifra

En Intune, el informe **Dispositivos → Supervisar → Informe de cifrado** te dice el motivo. Los más frecuentes: el TPM no está listo (`Get-Tpm` muestra `TpmReady : False`), el usuario no es administrador local y la política no permite cifrado silencioso, o el perfil de cifrado no está asignado al equipo.

## Siguientes pasos

- Haz que la clave se guarde en Entra ID por política antes de cifrar: un equipo cifrado sin clave guardada es un equipo perdido el día que la pida.
- Revisa el informe de cifrado de Intune cada semana y persigue los equipos que llevan días en "pendiente".
- En el Nivel 3 verás cómo configurar el perfil de cifrado de Intune con cifrado silencioso y rotación automática.
""",
  en="""
## What you'll get

Know in a minute whether a device is encrypted and with which protector, find the recovery key in Entra ID or Active Directory, and give a user their laptop back when the blue screen asking for 48 digits appears.

## Before you start

- To read a device's status you need a PowerShell console **as administrator** on that device.
- To view recovery keys you need a role that shows them: in Entra ID, **Helpdesk Administrator** or a custom role with `microsoft.directory/bitlockerKeys/key/read`; in Active Directory, read permission on the computer object with RSAT and the BitLocker recovery tab installed.
- Every key read lands in the audit log. That is normal and good: put the ticket number in your notes.

## 1. Check the encryption status

:::term PowerShell · as administrator
$ manage-bde -status C:
Volume C: [Windows]
[OS Volume]
    Size:                 476.00 GB
    BitLocker Version:    2.0
    Conversion Status:    Fully Encrypted
    Percentage Encrypted: 100.0%
    Encryption Method:    XTS-AES 128
    Protection Status:    Protection On
    Key Protectors:
        TPM
        Numerical Password
$ Get-BitLockerVolume C: | Select-Object VolumeStatus, ProtectionStatus, EncryptionPercentage, KeyProtector
VolumeStatus         : FullyEncrypted
ProtectionStatus     : On
EncryptionPercentage : 100
KeyProtector         : {Tpm, RecoveryPassword}
:::

What you want to see: **Fully Encrypted**, **Protection On** and two protectors, `TPM` and `Numerical Password` (the recovery key). If protection is **Off**, the disk is encrypted but anyone can boot it: usually someone suspended it for a firmware update and it was never resumed.

:::term PowerShell · as administrator
# Resume protection if it was suspended
$ Resume-BitLocker -MountPoint C:
# Confirm the recovery key is stored in Entra ID (Entra joined or registered devices)
$ $kp = (Get-BitLockerVolume C:).KeyProtector | Where-Object KeyProtectorType -eq "RecoveryPassword"
$ BackupToAAD-BitLockerKeyProtector -MountPoint C: -KeyProtectorId $kp.KeyProtectorId
:::

## 2. Find the recovery key

On a device managed with Intune the key is in Entra ID. Search the device by name and open **BitLocker keys**.

:::ui Entra ID · Devices
> Entra ID › Devices › All devices › LAPTOP-7F2K9Q › BitLocker keys
= Key ID: 7a1c…-…-…-…-…3e9d
= Drive: OS drive
= Recovery key: 123456-654321-112233-445566-778899-998877-665544-332211
[Show recovery key]
:::

In a classic domain the key sits on the **computer** object in Active Directory, **BitLocker Recovery** tab, as long as Group Policy stores it there. On a hybrid device, look in Entra ID first.

! Check that the **Key ID** matches the first 8 characters shown on the laptop's blue screen. A device can have several keys (one per time it was encrypted) and only one works.

## 3. The laptop asks for the recovery key

It almost always happens after one of these: a BIOS/firmware update, a change to the board or the boot order, Secure Boot turned off, or a disk moved to another device. That is BitLocker doing its job.

1. Ask the user for the **Key ID** on screen (the first 8 characters are enough) and the device name (on the label or in the ticket).
2. Find the key as in step 2 and read it out by phone or over an encrypted channel. Never paste it into the ticket or an email.
3. Once it boots, sign in and check why it triggered: a firmware update needs nothing more; if Secure Boot is off, turn it on.
4. If it will ask again at every boot, **suspend and resume** protection once so the TPM re-seals the boot measurements:

:::term PowerShell · as administrator
$ Suspend-BitLocker -MountPoint C: -RebootCount 1
$ Restart-Computer
# After the reboot, protection resumes on its own. Check it:
$ (Get-BitLockerVolume C:).ProtectionStatus
On
:::

5. If your policy requires it, **rotate the recovery key** after using it. From Intune: the device → **BitLocker key rotation**. The key read out by phone then stops working.

## 4. A new device won't encrypt

In Intune, the report **Devices → Monitor → Encryption report** gives the reason. The most frequent: the TPM is not ready (`Get-Tpm` shows `TpmReady : False`), the user is not a local administrator and the policy does not allow silent encryption, or the encryption profile is not assigned to the device.

## Next steps

- Make the key back up to Entra ID by policy before encrypting: an encrypted device with no stored key is a lost device the day it asks.
- Review the Intune encryption report weekly and chase devices that have been "pending" for days.
- In Level 3 you'll see how to configure the Intune encryption profile with silent encryption and automatic rotation.
""")

# ---------------------------------------------------------------- 4 · Cisco AnyConnect
g(slug="anyconnect-instalar-y-diagnosticar-vpn", topic="anyconnect", date="2026-10-21",
  title_es="Cisco AnyConnect: instalar el cliente y diagnosticar una VPN que no conecta",
  title_en="Cisco AnyConnect: installing the client and diagnosing a VPN that won't connect",
  dek_es="Instalar Secure Client, conectar, y seguir un orden fijo cuando falla: red, DNS, certificado, credenciales o el propio cliente.",
  dek_en="Install Secure Client, connect, and follow a fixed order when it fails: network, DNS, certificate, credentials or the client itself.",
  es="""
## Qué vas a conseguir

Un usuario conectado a la VPN desde casa o desde un hotel, y un método para que el ticket "la VPN no me va" se resuelva en cinco minutos en lugar de media hora de pruebas al azar.

Cisco ha renombrado AnyConnect como **Cisco Secure Client**. El icono y los mensajes cambian un poco, pero los pasos son los mismos.

## Antes de empezar

- El instalador que usa tu empresa (normalmente lo despliega Intune o SCCM, y en el equipo ya está). Si no, se descarga del portal de la propia VPN al conectarse por el navegador.
- La dirección del concentrador VPN (`vpn.contoso.com`) y el **grupo** o perfil que debe elegir el usuario.
- Cómo se autentica: usuario y contraseña de dominio, MFA con Authenticator, certificado de equipo, o una combinación.

## 1. Instalar y conectar

:::ui Cisco Secure Client · AnyConnect VPN
> Cisco Secure Client › AnyConnect VPN
= Conectar a: vpn.contoso.com
[Conectar]
> Cisco Secure Client › Inicio de sesión
= Grupo: Empleados
= Usuario: laura.prado
= Contraseña: ••••••••••
= Segundo factor: aprobación en Authenticator
[Aceptar]
= Estado: Conectado a vpn.contoso.com
:::

Cuando conecta, el icono de la bandeja muestra un candado cerrado. Pide al usuario que abra una unidad de red o la intranet para confirmar que el túnel funciona, no solo que dice "conectado".

## 2. Cuando no conecta: el orden

Haz las comprobaciones en este orden y para en la primera que falle. Cada una descarta una capa.

### 2.1 ¿Hay internet?

:::term CMD · usuario
$ ping -n 2 1.1.1.1
Respuesta desde 1.1.1.1: bytes=32 tiempo=14ms TTL=57
$ nslookup vpn.contoso.com
Servidor:  UnKnown
Address:  192.168.1.1
Respuesta no autoritativa:
Nombre:  vpn.contoso.com
Address:  203.0.113.10
:::

Sin respuesta al ping: es la red del usuario (wifi del hotel con portal cautivo, cable suelto, datos móviles sin cobertura). Si el ping va pero `nslookup` no resuelve, es DNS: que pruebe con los datos del móvil para confirmarlo.

### 2.2 ¿Se llega al concentrador?

Abre en el navegador `https://vpn.contoso.com`. Si aparece el portal de la VPN, la red y el DNS están bien y el problema está en el cliente o en las credenciales. Si el navegador avisa de **certificado no válido**, lo verá también el cliente: suele ser una red que intercepta TLS (wifi pública, proxy de hotel) o la hora del equipo mal puesta.

### 2.3 ¿Qué dice el cliente?

Los mensajes de Secure Client son más útiles de lo que parecen:

- **Login failed**: usuario o contraseña incorrectos, o la cuenta bloqueada o caducada en Active Directory. Compruébalo con `Get-ADUser -Properties LockedOut, PasswordExpired`.
- **The VPN connection failed due to unsuccessful domain name resolution**: DNS, vuelve al 2.1.
- **Untrusted VPN Server certificate**: el 2.2; en redes de hotel suele arreglarse conectando primero el móvil como punto de acceso.
- **VPN establishment capability for a remote user is disabled**: el usuario está en sesión remota (RDP) y la política no permite VPN desde ahí. Que lo haga desde el equipo físico.
- **The VPN client agent was unable to create the interprocess communication depot** o el cliente no abre: el servicio no arranca, ve al 2.4.
- **Posture assessment failed** o "tu equipo no cumple": el módulo de cumplimiento (ISE, HostScan) exige antivirus al día, disco cifrado o una versión mínima de Windows. El propio mensaje dice qué falta.

### 2.4 ¿Está bien el cliente?

:::term PowerShell · como administrador
$ Get-Service -Name "csc_vpnagent","vpnagent" -ErrorAction SilentlyContinue | Select-Object Name, Status, StartType
Name         Status  StartType
----         ------  ---------
csc_vpnagent Running Automatic
$ Restart-Service csc_vpnagent
# Adaptador virtual de la VPN: tiene que existir y no estar deshabilitado
$ Get-NetAdapter | Where-Object InterfaceDescription -like "Cisco AnyConnect*" | Select-Object Name, Status
Name                      Status
----                      ------
Ethernet 3                Disabled
$ Enable-NetAdapter -Name "Ethernet 3"
:::

Si el servicio no arranca o el adaptador no existe, reinstala el cliente: desinstalar desde **Aplicaciones**, reiniciar, instalar de nuevo. Muchas veces una actualización de Windows a medias deja el adaptador virtual a medio camino.

## 3. Conecta pero no llega a nada

- Con la VPN conectada, `ipconfig /all` tiene que mostrar el adaptador de la VPN con una IP del rango corporativo y los DNS internos.
- `nslookup intranet.contoso.local` debe resolver con el DNS interno. Si resuelve con el de casa, el cliente no ha cambiado los DNS: reconecta, y si sigue, es el perfil del concentrador (split-DNS) y toca escalar.
- Si solo falla una aplicación, pide la IP o el nombre y prueba `Test-NetConnection servidor -Port 443`. Si el puerto no responde con la VPN pero sí desde la oficina, es una regla del firewall para el rango VPN: escalar a redes con el nombre, el puerto y la hora de la prueba.

## 4. Qué poner en el ticket

Mensaje exacto del cliente, red desde la que conecta (casa, hotel, datos móviles), hora de la prueba, y el resultado de 2.1 y 2.2. Con eso, redes puede buscar en los logs del concentrador en un minuto. Si hay que escalar a Cisco, el **DART** (Diagnostics and Reporting Tool, en el menú del cliente) genera un paquete con todos los logs.

## Siguientes pasos

- Documenta los mensajes de error y su causa en la base de conocimiento del service desk: cada uno que añades ahorra una escalada.
- Pide a redes el perfil XML del cliente para saber si usa split-tunnel y qué DNS empuja: así entiendes qué debería verse cuando conecta.
- En el Nivel 4 verás el concentrador por dentro: FortiGate y Cisco, perfiles, grupos y las reglas que deciden qué ve cada usuario.
""",
  en="""
## What you'll get

A user connected to the VPN from home or a hotel, and a method that resolves the "my VPN doesn't work" ticket in five minutes rather than half an hour of random tests.

Cisco has renamed AnyConnect to **Cisco Secure Client**. The icon and messages change a little, but the steps are the same.

## Before you start

- The installer your company uses (Intune or SCCM usually deploys it, so it is already on the device). If not, it downloads from the VPN's own portal when connecting through the browser.
- The address of the VPN concentrator (`vpn.contoso.com`) and the **group** or profile the user has to pick.
- How it authenticates: domain username and password, MFA with Authenticator, a device certificate, or a combination.

## 1. Install and connect

:::ui Cisco Secure Client · AnyConnect VPN
> Cisco Secure Client › AnyConnect VPN
= Connect to: vpn.contoso.com
[Connect]
> Cisco Secure Client › Login
= Group: Employees
= Username: laura.prado
= Password: ••••••••••
= Second factor: approve in Authenticator
[OK]
= Status: Connected to vpn.contoso.com
:::

When it connects, the tray icon shows a closed padlock. Ask the user to open a network drive or the intranet to confirm the tunnel works, not just that it says "connected".

## 2. When it doesn't connect: the order

Run the checks in this order and stop at the first one that fails. Each one rules out a layer.

### 2.1 Is there internet?

:::term CMD · user
$ ping -n 2 1.1.1.1
Reply from 1.1.1.1: bytes=32 time=14ms TTL=57
$ nslookup vpn.contoso.com
Server:  UnKnown
Address:  192.168.1.1
Non-authoritative answer:
Name:    vpn.contoso.com
Address: 203.0.113.10
:::

No ping reply: it is the user's network (hotel wifi with a captive portal, loose cable, mobile data with no coverage). If ping works but `nslookup` does not resolve, it is DNS: have them try on mobile data to confirm.

### 2.2 Can the concentrator be reached?

Open `https://vpn.contoso.com` in the browser. If the VPN portal appears, network and DNS are fine and the problem is in the client or the credentials. If the browser warns of an **invalid certificate**, the client sees it too: usually a network that intercepts TLS (public wifi, hotel proxy) or the device clock set wrong.

### 2.3 What does the client say?

Secure Client's messages are more useful than they look:

- **Login failed**: wrong username or password, or the account locked or expired in Active Directory. Check with `Get-ADUser -Properties LockedOut, PasswordExpired`.
- **The VPN connection failed due to unsuccessful domain name resolution**: DNS, back to 2.1.
- **Untrusted VPN Server certificate**: see 2.2; on hotel networks it is often fixed by tethering to the phone first.
- **VPN establishment capability for a remote user is disabled**: the user is in a remote session (RDP) and policy does not allow VPN from there. They need to do it from the physical device.
- **The VPN client agent was unable to create the interprocess communication depot** or the client does not open: the service is not starting, go to 2.4.
- **Posture assessment failed** or "your device is not compliant": the compliance module (ISE, HostScan) requires an up-to-date antivirus, an encrypted disk or a minimum Windows version. The message itself says what is missing.

### 2.4 Is the client healthy?

:::term PowerShell · as administrator
$ Get-Service -Name "csc_vpnagent","vpnagent" -ErrorAction SilentlyContinue | Select-Object Name, Status, StartType
Name         Status  StartType
----         ------  ---------
csc_vpnagent Running Automatic
$ Restart-Service csc_vpnagent
# The VPN's virtual adapter: it has to exist and not be disabled
$ Get-NetAdapter | Where-Object InterfaceDescription -like "Cisco AnyConnect*" | Select-Object Name, Status
Name                      Status
----                      ------
Ethernet 3                Disabled
$ Enable-NetAdapter -Name "Ethernet 3"
:::

If the service won't start or the adapter does not exist, reinstall the client: uninstall from **Apps**, reboot, install again. A half-finished Windows update often leaves the virtual adapter in a broken state.

## 3. It connects but reaches nothing

- With the VPN connected, `ipconfig /all` has to show the VPN adapter with an IP from the corporate range and the internal DNS servers.
- `nslookup intranet.contoso.local` must resolve through the internal DNS. If it resolves through the home one, the client has not switched DNS: reconnect, and if it persists it is the concentrator profile (split-DNS) and it is time to escalate.
- If only one application fails, ask for the IP or name and test `Test-NetConnection server -Port 443`. If the port does not answer over VPN but does from the office, it is a firewall rule for the VPN range: escalate to networks with the name, the port and the time of the test.

## 4. What to put in the ticket

The client's exact message, the network they connect from (home, hotel, mobile data), the time of the test, and the result of 2.1 and 2.2. With that, networks can search the concentrator logs in a minute. If it has to go to Cisco, the **DART** (Diagnostics and Reporting Tool, in the client menu) builds a bundle with all the logs.

## Next steps

- Document the error messages and their cause in the service desk knowledge base: every one you add saves an escalation.
- Ask networks for the client's XML profile to learn whether it uses split-tunnel and which DNS it pushes: then you know what should appear when it connects.
- In Level 4 you'll see the concentrator from the inside: FortiGate and Cisco, profiles, groups and the rules that decide what each user can reach.
""")

# ---------------------------------------------------------------- 5 · Impresoras
g(slug="impresoras-instalar-impresora-de-red-y-cola-atascada", topic="impresoras", date="2026-10-21",
  title_es="Impresoras: instalar una impresora de red y desatascar la cola",
  title_en="Printers: installing a network printer and clearing a stuck queue",
  dek_es="Añadir una impresora por IP o desde el servidor de impresión, y los tres arreglos que resuelven casi todas las incidencias de impresión.",
  dek_en="Add a printer by IP or from the print server, and the three fixes that resolve almost every printing ticket.",
  es="""
## Qué vas a conseguir

Un usuario imprimiendo en la impresora de su planta, y un método corto para "no imprime", que es el ticket más repetido de cualquier service desk.

## Antes de empezar

- Cómo se publican las impresoras en tu empresa: desde un **servidor de impresión** (`\\\\print01`), por **Universal Print** en Intune, o directamente por IP.
- El nombre o la IP de la impresora. Suele estar en una pegatina en la propia impresora o en su página de configuración (botón de menú → Red).
- Permisos: añadir una impresora del servidor no necesita administrador; instalar un controlador por IP, normalmente sí.

## 1. Añadir una impresora

### Desde el servidor de impresión

:::ui Windows · Ejecutar
> Win + R › \\\\print01
> print01 › PRN-MAD-2P-COLOR › Conectar…
= Estado: Instalando controlador… Listo
:::

Con PowerShell, igual, y vale para hacerlo en remoto o en lote:

:::term PowerShell · usuario
$ Add-Printer -ConnectionName "\\\\print01\\PRN-MAD-2P-COLOR"
$ Get-Printer | Select-Object Name, DriverName, PortName, PrinterStatus
Name                          DriverName                 PortName            PrinterStatus
----                          ----------                 --------            -------------
\\\\print01\\PRN-MAD-2P-COLOR    HP Universal Printing PCL6 PRN-MAD-2P-COLOR    Normal
Microsoft Print to PDF        Microsoft Print To PDF     PORTPROMPT:         Normal
:::

Si aparece **0x0000011b** o "Windows no puede conectarse a la impresora", es la protección contra PrintNightmare: el controlador tiene que estar firmado y en el servidor, o la impresora se instala por IP. Escálalo al equipo del servidor de impresión con el código, no toques el registro del equipo.

### Por IP (sin servidor)

:::term PowerShell · como administrador
$ Add-PrinterPort -Name "IP_10.20.5.41" -PrinterHostAddress "10.20.5.41"
$ Get-PrinterDriver | Where-Object Name -like "*Universal*" | Select-Object Name
Name
----
HP Universal Printing PCL6
$ Add-Printer -Name "Impresora planta 2 (color)" -DriverName "HP Universal Printing PCL6" -PortName "IP_10.20.5.41"
:::

Con una impresora por IP, el controlador universal del fabricante (HP UPD, Xerox Global, Canon Generic) cubre casi todos los modelos. Si el fabricante no es ninguno de esos, descarga el controlador de su web, nunca de un buscador.

## 2. "No imprime": el orden

### 2.1 ¿La impresora está viva?

:::term CMD · usuario
$ ping 10.20.5.41
Respuesta desde 10.20.5.41: bytes=32 tiempo=2ms TTL=64
:::

Sin respuesta: apagada, sin red o con otra IP (las impresoras con DHCP y sin reserva cambian de IP y dejan huérfano el puerto). Mira la pantalla de la impresora: si muestra una IP distinta, cambia el puerto o pide una reserva DHCP.

### 2.2 ¿Hay trabajos atascados?

Un trabajo con error bloquea todos los siguientes. En **Configuración → Impresoras → la impresora → Abrir cola** se ven; si "Cancelar todos" no los quita, limpia la cola:

:::term PowerShell · como administrador
$ Get-PrintJob -PrinterName "Impresora planta 2 (color)" | Select-Object Id, DocumentName, JobStatus, UserName
Id DocumentName        JobStatus       UserName
-- ------------        ---------       --------
 7 Informe Q3.pdf      Error, Printing laura.prado
 8 Factura 1021.docx   Spooling        laura.prado
$ Stop-Service Spooler
$ Remove-Item "$env:SystemRoot\\System32\\spool\\PRINTERS\\*" -Force
$ Start-Service Spooler
:::

### 2.3 ¿Es el equipo o la impresora?

Imprime la **página de prueba** desde las propiedades de la impresora. Si sale, el problema está en la aplicación del usuario (un PDF enorme, una fuente, una versión antigua de Office). Si no sale desde ningún equipo, es la impresora o el servidor: escala con el modelo, la IP y lo que muestra la pantalla de la impresora.

## 3. Periféricos que dejan de responder

El mismo método sirve para un escáner, un lector de tarjetas o una base de carga: **Administrador de dispositivos** (`devmgmt.msc`) muestra un triángulo amarillo si falta el controlador o un código de error. Los tres arreglos por orden: otro puerto USB (mejor directo al equipo, no al monitor o a un hub), **desinstalar el dispositivo** desde el administrador y volver a conectarlo, y actualizar el controlador desde la web del fabricante.

> En los portátiles con base de carga, la mitad de los "no funciona el teclado/monitor/red" son la base: prueba con otra base o conecta el periférico directo al portátil antes de abrir el ticket al fabricante.

## 4. Qué poner en el ticket

Nombre de la impresora, IP, qué equipo, qué aplicación, y el resultado de la página de prueba. Si has limpiado la cola, dilo: así quien venga después no repite el paso.

## Siguientes pasos

- Pide que las impresoras tengan **reserva DHCP** o IP fija: desaparecen la mitad de los tickets.
- Si tu empresa usa Intune, mira **Universal Print**: las impresoras se asignan por grupo y el usuario no instala nada.
- Para lotes (una planta entera), un script con `Add-Printer` sobre una lista de equipos ahorra una tarde.
""",
  en="""
## What you'll get

A user printing on their floor's printer, and a short method for "it doesn't print", the most repeated ticket at any service desk.

## Before you start

- How printers are published in your company: from a **print server** (`\\\\print01`), through **Universal Print** in Intune, or directly by IP.
- The printer's name or IP. It is usually on a sticker on the printer itself or on its configuration page (menu button → Network).
- Permissions: adding a server printer needs no admin rights; installing a driver by IP usually does.

## 1. Add a printer

### From the print server

:::ui Windows · Run
> Win + R › \\\\print01
> print01 › PRN-MAD-2P-COLOR › Connect…
= Status: Installing driver… Done
:::

PowerShell does the same, and it works remotely or in bulk:

:::term PowerShell · user
$ Add-Printer -ConnectionName "\\\\print01\\PRN-MAD-2P-COLOR"
$ Get-Printer | Select-Object Name, DriverName, PortName, PrinterStatus
Name                          DriverName                 PortName            PrinterStatus
----                          ----------                 --------            -------------
\\\\print01\\PRN-MAD-2P-COLOR    HP Universal Printing PCL6 PRN-MAD-2P-COLOR    Normal
Microsoft Print to PDF        Microsoft Print To PDF     PORTPROMPT:         Normal
:::

If you see **0x0000011b** or "Windows cannot connect to the printer", it is the PrintNightmare protection: the driver has to be signed and on the server, or the printer is installed by IP. Escalate to the print server team with the code; do not touch the device's registry.

### By IP (no server)

:::term PowerShell · as administrator
$ Add-PrinterPort -Name "IP_10.20.5.41" -PrinterHostAddress "10.20.5.41"
$ Get-PrinterDriver | Where-Object Name -like "*Universal*" | Select-Object Name
Name
----
HP Universal Printing PCL6
$ Add-Printer -Name "Floor 2 printer (colour)" -DriverName "HP Universal Printing PCL6" -PortName "IP_10.20.5.41"
:::

With an IP printer, the manufacturer's universal driver (HP UPD, Xerox Global, Canon Generic) covers almost every model. If the manufacturer is none of those, download the driver from their website, never from a search engine.

## 2. "It doesn't print": the order

### 2.1 Is the printer alive?

:::term CMD · user
$ ping 10.20.5.41
Reply from 10.20.5.41: bytes=32 time=2ms TTL=64
:::

No reply: switched off, off the network, or on another IP (DHCP printers without a reservation change IP and orphan the port). Look at the printer's screen: if it shows a different IP, change the port or ask for a DHCP reservation.

### 2.2 Are there stuck jobs?

A job in error blocks everything after it. **Settings → Printers → the printer → Open queue** shows them; if "Cancel all" does not clear them, clean the queue:

:::term PowerShell · as administrator
$ Get-PrintJob -PrinterName "Floor 2 printer (colour)" | Select-Object Id, DocumentName, JobStatus, UserName
Id DocumentName        JobStatus       UserName
-- ------------        ---------       --------
 7 Q3 report.pdf       Error, Printing laura.prado
 8 Invoice 1021.docx   Spooling        laura.prado
$ Stop-Service Spooler
$ Remove-Item "$env:SystemRoot\\System32\\spool\\PRINTERS\\*" -Force
$ Start-Service Spooler
:::

### 2.3 Is it the device or the printer?

Print the **test page** from the printer's properties. If it comes out, the problem is in the user's application (a huge PDF, a font, an old Office version). If nothing prints from any device, it is the printer or the server: escalate with the model, the IP and what the printer's screen shows.

## 3. Peripherals that stop responding

The same method works for a scanner, a card reader or a docking station: **Device Manager** (`devmgmt.msc`) shows a yellow triangle if the driver is missing or an error code. The three fixes in order: another USB port (ideally straight into the device, not the monitor or a hub), **uninstall the device** from Device Manager and plug it in again, and update the driver from the manufacturer's website.

> On laptops with a dock, half of the "keyboard/monitor/network doesn't work" tickets are the dock: try another dock or plug the peripheral straight into the laptop before opening a ticket with the manufacturer.

## 4. What to put in the ticket

Printer name, IP, which device, which application, and the result of the test page. If you cleared the queue, say so: whoever comes next does not repeat the step.

## Next steps

- Ask for printers to have a **DHCP reservation** or a fixed IP: half the tickets disappear.
- If your company uses Intune, look at **Universal Print**: printers are assigned by group and the user installs nothing.
- For batches (a whole floor), a script with `Add-Printer` over a list of devices saves an afternoon.
""")

# ---------------------------------------------------------------- 6 · iPhone y iPad
g(slug="iphone-ipad-enrolar-en-intune", topic="ios", date="2026-10-21",
  title_es="iPhone y iPad: enrolar en Intune y comprobar que llegan las políticas",
  title_en="iPhone and iPad: enrolling in Intune and checking that policies arrive",
  dek_es="El camino del usuario con el Portal de empresa, qué cambia si el dispositivo viene por Apple Business Manager, y cómo verificar correo, Wi-Fi y apps.",
  dek_en="The user's path with Company Portal, what changes when the device comes through Apple Business Manager, and how to verify email, Wi-Fi and apps.",
  es="""
## Qué vas a conseguir

Un iPhone o iPad gestionado por Intune: con el perfil de administración instalado, el correo configurado solo, la Wi-Fi corporativa y las aplicaciones obligatorias. Y saber dónde mirar cuando algo de eso no llega.

## Antes de empezar

- El **certificado push de Apple (APNs)** del tenant tiene que estar vigente. Caduca cada año y, si caduca, ningún dispositivo Apple se enrola ni recibe políticas. Está en Intune → Dispositivos → Inscripción → Apple.
- El usuario tiene licencia con Intune y, en el dispositivo, un **ID de Apple** para instalar el Portal de empresa desde el App Store (si las apps se despliegan con licencias VPP asignadas al dispositivo, el ID de Apple no hace falta para ellas).
- Sabes si el dispositivo es **personal** (el usuario lo enrola con el Portal de empresa) o **corporativo** comprado a través de Apple Business Manager (se enrola solo al encenderlo, con el Asistente de configuración).

## 1. Dispositivo personal: el camino del usuario

:::ui iOS · Portal de empresa
> App Store › Intune Company Portal › Obtener
> Portal de empresa › Iniciar sesión › laura.prado@contoso.com
> Configuración del acceso › Comenzar › Descargar perfil
> Ajustes › Perfil descargado › Instalar › Introducir código del iPhone
= Perfil: Administración de Microsoft Intune
[Instalar]
> Portal de empresa › Continuar › Comprobando el dispositivo…
= Estado: Ya tienes acceso a los recursos de la empresa
:::

El paso que más se atasca es el de **Ajustes → Perfil descargado**: el Portal de empresa descarga el perfil pero el usuario tiene que ir a Ajustes a instalarlo. Si cierra la app en ese punto, se queda a medias; con volver al Portal de empresa y pulsar "Continuar" se retoma.

## 2. Dispositivo corporativo (Apple Business Manager)

Si el iPhone se compró con el número de cliente de la empresa, aparece en Apple Business Manager y de ahí pasa a Intune por el **token de inscripción automatizada**. Al encenderlo por primera vez, el Asistente de configuración muestra "contoso configurará este dispositivo" y el usuario solo inicia sesión. No hay Portal de empresa que instalar.

Si un iPhone corporativo se enciende y no muestra esa pantalla, suele ser que no está asignado al token en Apple Business Manager o que el perfil de inscripción no está asignado en Intune. Lo ves en **Intune → Dispositivos → Inscripción → Apple → Tokens de inscripción → Dispositivos**: busca el número de serie.

## 3. Comprueba en Intune

:::ui Intune · Dispositivos › iOS/iPadOS
> Dispositivos › iOS/iPadOS › iPhone de Laura
= Propiedad: Corporativo
= Inscrito por: laura.prado@contoso.com
= Versión del SO: iOS 18.1
= Supervisado: Sí
= Cumplimiento: Conforme
= Último check-in: 21/10/2026 10:41
[Sincronizar] [Retirar] [Bloqueo remoto] [Quitar código]
:::

**Supervisado: Sí** solo aparece en los que vienen por Apple Business Manager, y es lo que permite las políticas más restrictivas (bloquear el App Store, modo de una sola app). Un dispositivo personal nunca está supervisado, y eso no es un fallo.

## 4. Lo que no llega y por qué

- **El correo no se configura solo**: el perfil de correo necesita que el usuario tenga el atributo correcto (UPN o correo principal) y que Outlook esté instalado si el perfil apunta a Outlook. Mira **Dispositivos → el dispositivo → Perfiles de configuración**: el perfil de correo tiene que estar "Correcto". Si está "Pendiente", pulsa **Sincronizar** y espera dos minutos.
- **La Wi-Fi corporativa no aparece**: lo mismo, perfil de Wi-Fi pendiente o con error. Si usa certificado (EAP-TLS), el perfil SCEP tiene que haber llegado antes: aparece en Ajustes → General → VPN y gestión de dispositivos → el perfil de Intune → Más detalles → Certificados.
- **Las apps obligatorias no se instalan**: en un dispositivo personal, iOS pregunta al usuario "contoso quiere instalar Teams" y hay que aceptar. Si no aparece la pregunta, la app está asignada como disponible, no como obligatoria, o las licencias VPP se han agotado (Aplicaciones → iOS → la app → Licencias).
- **Pide el ID de Apple para una app de empresa**: la licencia VPP está asignada por usuario en lugar de por dispositivo. Para dispositivos compartidos o corporativos, asignar por dispositivo evita esa pregunta.

## 5. Retirar y bloquear

- **Retirar** quita el perfil de administración, el correo y las apps de empresa. Es lo que haces en una baja o cuando el usuario cambia de móvil. Las fotos y las apps personales no se tocan.
- **Bloqueo remoto** bloquea la pantalla con el código del usuario; sirve si lo ha dejado en un taxi.
- **Borrar** devuelve el dispositivo a fábrica. En uno personal, solo con el permiso del usuario por escrito en el ticket. En uno corporativo con **bloqueo de activación**, antes de borrar asegúrate de tener el código de omisión (Intune lo guarda si el dispositivo está supervisado): si no, el iPhone queda inservible para el siguiente usuario.

## Siguientes pasos

- Apunta en el calendario del equipo la fecha de caducidad del certificado APNs y de los tokens de Apple Business Manager y VPP: los tres caducan cada año.
- Para los iPad compartidos de una sala o un mostrador, mira el **modo de una sola app** y la inscripción sin usuario.
- En el Nivel 3 verás cómo diseñar los perfiles de configuración (correo, Wi-Fi, certificados, restricciones) para iOS, macOS, Windows y Android desde la misma consola.
""",
  en="""
## What you'll get

An iPhone or iPad managed by Intune: with the management profile installed, email configured on its own, the corporate Wi-Fi and the required apps. And knowing where to look when any of that does not arrive.

## Before you start

- The tenant's **Apple push certificate (APNs)** has to be valid. It expires every year and, if it does, no Apple device enrols or receives policies. It is in Intune → Devices → Enrolment → Apple.
- The user has a licence with Intune and, on the device, an **Apple ID** to install Company Portal from the App Store (if apps are deployed with device-assigned VPP licences, no Apple ID is needed for those).
- You know whether the device is **personal** (the user enrols it with Company Portal) or **corporate**, bought through Apple Business Manager (it enrols on its own at first power-on, through Setup Assistant).

## 1. Personal device: the user's path

:::ui iOS · Company Portal
> App Store › Intune Company Portal › Get
> Company Portal › Sign in › laura.prado@contoso.com
> Access setup › Begin › Download profile
> Settings › Profile downloaded › Install › Enter the iPhone passcode
= Profile: Microsoft Intune management
[Install]
> Company Portal › Continue › Checking your device…
= Status: You can now access company resources
:::

The step that gets stuck most is **Settings → Profile downloaded**: Company Portal downloads the profile but the user has to go to Settings to install it. If they close the app at that point, it stays half done; going back to Company Portal and tapping "Continue" picks it up again.

## 2. Corporate device (Apple Business Manager)

If the iPhone was bought with the company's customer number, it appears in Apple Business Manager and from there passes to Intune through the **automated enrolment token**. At first power-on, Setup Assistant shows "contoso will configure this device" and the user only signs in. There is no Company Portal to install.

If a corporate iPhone powers on and does not show that screen, it is usually not assigned to the token in Apple Business Manager, or the enrolment profile is not assigned in Intune. You can see it in **Intune → Devices → Enrolment → Apple → Enrolment program tokens → Devices**: search by serial number.

## 3. Check in Intune

:::ui Intune · Devices › iOS/iPadOS
> Devices › iOS/iPadOS › Laura's iPhone
= Ownership: Corporate
= Enrolled by: laura.prado@contoso.com
= OS version: iOS 18.1
= Supervised: Yes
= Compliance: Compliant
= Last check-in: 21/10/2026 10:41
[Sync] [Retire] [Remote lock] [Remove passcode]
:::

**Supervised: Yes** only appears on devices that come through Apple Business Manager, and it is what allows the stricter policies (blocking the App Store, single-app mode). A personal device is never supervised, and that is not a fault.

## 4. What doesn't arrive and why

- **Email does not configure itself**: the email profile needs the user to have the right attribute (UPN or primary email) and Outlook installed if the profile points to Outlook. Look at **Devices → the device → Configuration profiles**: the email profile has to be "Succeeded". If it is "Pending", tap **Sync** and wait two minutes.
- **The corporate Wi-Fi does not appear**: same thing, Wi-Fi profile pending or in error. If it uses a certificate (EAP-TLS), the SCEP profile has to have arrived first: it shows in Settings → General → VPN & Device Management → the Intune profile → More details → Certificates.
- **Required apps don't install**: on a personal device, iOS asks the user "contoso wants to install Teams" and they have to accept. If the prompt never appears, the app is assigned as available rather than required, or the VPP licences have run out (Apps → iOS → the app → Licences).
- **It asks for an Apple ID for a company app**: the VPP licence is assigned per user instead of per device. For shared or corporate devices, device assignment avoids that prompt.

## 5. Retire and lock

- **Retire** removes the management profile, email and company apps. That is what you do for a leaver or when the user changes phone. Photos and personal apps are untouched.
- **Remote lock** locks the screen with the user's passcode; useful if it was left in a taxi.
- **Wipe** returns the device to factory settings. On a personal one, only with the user's written permission in the ticket. On a corporate one with **Activation Lock**, make sure you have the bypass code before wiping (Intune stores it if the device is supervised): otherwise the iPhone is useless for the next user.

## Next steps

- Put the expiry dates of the APNs certificate and the Apple Business Manager and VPP tokens in the team calendar: all three expire every year.
- For shared iPads in a meeting room or at a counter, look at **single-app mode** and userless enrolment.
- In Level 3 you'll see how to design configuration profiles (email, Wi-Fi, certificates, restrictions) for iOS, macOS, Windows and Android from the same console.
""")

# ---------------------------------------------------------------- 7 · Jira Service Management
g(slug="jira-service-management-un-ticket-bien-hecho", topic="jira", date="2026-10-21",
  title_es="Jira Service Management: un ticket bien hecho, de principio a fin",
  title_en="Jira Service Management: a well-made ticket, from start to finish",
  dek_es="Clasificar, priorizar, escribir para el siguiente, escalar y cerrar. Y las búsquedas JQL que usarás cada día.",
  dek_en="Classify, prioritise, write for the next person, escalate and close. Plus the JQL searches you'll use every day.",
  es="""
## Qué vas a conseguir

Tickets que cualquiera del equipo puede retomar sin llamarte, tiempos de respuesta dentro del SLA, y una cola que al final del día dice la verdad. Suena a poco; es lo que diferencia a un técnico de soporte bueno en la primera semana.

## Antes de empezar

- Tu proyecto de servicio en Jira (por ejemplo `SD`) y los **tipos de solicitud** que tiene: incidencia, petición de servicio, pregunta, cambio.
- La **matriz de prioridad** de tu empresa: impacto (cuántos usuarios o qué servicio) por urgencia (si pueden trabajar o no). Si no existe por escrito, pídela.
- Los SLA del proyecto (tiempo de primera respuesta y de resolución por prioridad). Se ven en cada ticket, en el panel de la derecha.

## 1. Al recibirlo: clasifica en dos minutos

Antes de tocar nada, deja el ticket bien puesto. Es lo que permite que los informes y las colas de los demás funcionen.

:::ui Jira Service Management · SD-4821
= Resumen: Outlook no abre tras la actualización de esta mañana
= Tipo de solicitud: Incidencia
= Prioridad: Media (impacto: 1 usuario · urgencia: alta, no puede trabajar)
= Componente: Correo y Outlook
= Elemento afectado: LAPTOP-7F2K9Q
= Asignado a: Iñigo
= SLA · Tiempo de primera respuesta: 00:42 restantes
[Responder al cliente] [Comentario interno] [Transición: En curso]
:::

- **Incidencia** es algo que funcionaba y ha dejado de funcionar. **Petición de servicio** es algo nuevo (un acceso, una licencia, un equipo). No las mezcles: tienen SLA y flujos distintos.
- El **resumen** dice el síntoma y el contexto en una línea. "Outlook" no sirve; "Outlook no abre tras la actualización de esta mañana" sí.
- La **prioridad** sale de la matriz, no de lo nervioso que esté el usuario. Un usuario sin trabajar es urgencia alta; un director que quiere un fondo de pantalla, baja.

## 2. La primera respuesta

El SLA de primera respuesta se cumple con un comentario **al cliente**, no con un comentario interno ni con cambiar el estado. Que sea corto, concreto y con una pregunta si falta información:

> He visto el ticket. Para localizar el fallo necesito que me digas: ¿sale algún mensaje de error al abrir Outlook? ¿Puedes entrar en el correo desde el navegador (outlook.office.com)? Mientras, lo estoy revisando desde aquí.

Con eso paras el reloj de primera respuesta y el usuario sabe que alguien está con ello.

## 3. Trabajar el ticket: escribe para el siguiente

Cada paso que das va en un **comentario interno** con lo que probaste y el resultado. No para tu jefe: para el compañero que lo retoma a las 17:00 cuando tú te vas.

:::ui Jira Service Management · SD-4821 · comentario interno
Probado: outlook.office.com abre bien → el buzón está OK, es el cliente de Outlook.
Probado: Outlook en modo seguro (outlook.exe /safe) abre → es un complemento o el perfil.
Deshabilitado el complemento de la app de firmas → Outlook abre con normalidad.
Siguiente: pedir al proveedor de la app de firmas la versión compatible con la build 2410. Ticket con ellos: PRV-118.
:::

Un comentario así tiene cuatro cosas: qué probaste, qué pasó, qué descartas y cuál es el siguiente paso. Si el ticket queda **En espera del cliente** o **En espera del proveedor**, el reloj del SLA se para (si el flujo está configurado así; compruébalo en tu proyecto) y queda claro de quién depende.

## 4. Escalar

Escalas cuando el siguiente paso necesita permisos o conocimiento que no tienes, no cuando llevas mucho tiempo. Al escalar, el ticket pasa al grupo correspondiente (**Asignado a** el equipo, o un ticket enlazado en su proyecto) con un resumen de lo que ya está descartado. Un ticket escalado con "no funciona, mirad" vuelve a los diez minutos.

## 5. Cerrar

- La **solución** va en un comentario al cliente, en lenguaje de usuario: "Era un complemento de Outlook incompatible con la última actualización. Lo he desactivado y he pedido al proveedor la versión nueva. Si vuelve a pasar, responde a este correo".
- El campo **Resolución** se rellena con honestidad: *Resuelto*, *Solución alternativa* (si lo has parcheado y queda un ticket de problema abierto), *No se puede reproducir*, *Duplicado* (enlazado al original).
- Si el usuario no contesta a "¿lo puedes comprobar?", el flujo lo cierra solo a los pocos días. No lo cierres a mano en el minuto uno: el que reabre un ticket cerrado a la fuerza nunca vuelve contento.

## 6. Las búsquedas JQL de cada día

:::term Jira · JQL
# Mi cola, lo más urgente primero
$ project = SD AND assignee = currentUser() AND statusCategory != Done ORDER BY priority DESC, created ASC
# Tickets sin asignar que van a incumplir el SLA en la próxima hora
$ project = SD AND assignee IS EMPTY AND "Time to first response" < remaining("1h")
# Todo lo que ha abierto este usuario (para ver si es recurrente)
$ project = SD AND reporter = "laura.prado@contoso.com" ORDER BY created DESC
# Lo que lleva más de 5 días esperando al proveedor
$ project = SD AND status = "Waiting for vendor" AND updated < -5d
:::

Guarda las dos primeras como filtros y ponlas en tu tablero: la cola deja de ser una lista y pasa a ser un plan.

## Siguientes pasos

- Cuando veas el mismo ticket tres veces, abre un **problema** enlazado: ahí vive la causa raíz, y los incidentes solo se enlazan.
- Aprende a escribir un artículo de la **base de conocimiento** desde el ticket: Jira lo sugiere al usuario antes de que abra el siguiente.
- En el Nivel 2 verás Confluence y, en el 4, cómo se administran los flujos, los SLA y las automatizaciones del proyecto.
""",
  en="""
## What you'll get

Tickets anyone on the team can pick up without calling you, response times inside the SLA, and a queue that tells the truth at the end of the day. It sounds small; it is what sets a good support technician apart in the first week.

## Before you start

- Your service project in Jira (say `SD`) and the **request types** it has: incident, service request, question, change.
- Your company's **priority matrix**: impact (how many users or which service) by urgency (whether they can work or not). If it is not written down, ask for it.
- The project's SLAs (first response and resolution time per priority). They show on every ticket, in the right-hand panel.

## 1. On arrival: classify in two minutes

Before touching anything, set the ticket up properly. That is what lets reports and everyone else's queues work.

:::ui Jira Service Management · SD-4821
= Summary: Outlook won't open after this morning's update
= Request type: Incident
= Priority: Medium (impact: 1 user · urgency: high, cannot work)
= Component: Email and Outlook
= Affected item: LAPTOP-7F2K9Q
= Assignee: Iñigo
= SLA · Time to first response: 00:42 remaining
[Reply to customer] [Internal comment] [Transition: In progress]
:::

- An **incident** is something that worked and has stopped working. A **service request** is something new (an access, a licence, a device). Don't mix them: they have different SLAs and workflows.
- The **summary** states the symptom and the context in one line. "Outlook" is useless; "Outlook won't open after this morning's update" works.
- **Priority** comes from the matrix, not from how nervous the user is. A user unable to work is high urgency; a director who wants a wallpaper is low.

## 2. The first response

The first-response SLA is met with a comment **to the customer**, not with an internal comment or a status change. Keep it short, concrete and with a question if information is missing:

> I've seen the ticket. To locate the fault I need to know: does any error message appear when opening Outlook? Can you get into your email from the browser (outlook.office.com)? Meanwhile I'm checking from here.

That stops the first-response clock and the user knows someone is on it.

## 3. Working the ticket: write for the next person

Every step you take goes into an **internal comment** with what you tried and the result. Not for your manager: for the colleague who picks it up at 17:00 when you leave.

:::ui Jira Service Management · SD-4821 · internal comment
Tried: outlook.office.com opens fine → the mailbox is OK, it's the Outlook client.
Tried: Outlook in safe mode (outlook.exe /safe) opens → it's an add-in or the profile.
Disabled the signature app's add-in → Outlook opens normally.
Next: ask the signature app vendor for the version compatible with build 2410. Ticket with them: PRV-118.
:::

A comment like that has four things: what you tried, what happened, what you rule out and what the next step is. If the ticket goes to **Waiting for customer** or **Waiting for vendor**, the SLA clock pauses (if the workflow is set up that way; check your project) and it is clear who it depends on.

## 4. Escalating

You escalate when the next step needs permissions or knowledge you don't have, not when it has taken a long time. When escalating, the ticket moves to the right group (**Assignee** set to the team, or a linked ticket in their project) with a summary of what is already ruled out. A ticket escalated with "doesn't work, have a look" comes back in ten minutes.

## 5. Closing

- The **solution** goes in a comment to the customer, in user language: "It was an Outlook add-in incompatible with the latest update. I've disabled it and asked the vendor for the new version. If it happens again, reply to this email".
- The **Resolution** field is filled in honestly: *Done*, *Workaround* (if you patched it and a problem ticket stays open), *Cannot reproduce*, *Duplicate* (linked to the original).
- If the user does not answer "can you check?", the workflow closes it on its own after a few days. Don't close it by hand in minute one: whoever reopens a force-closed ticket never comes back happy.

## 6. The everyday JQL searches

:::term Jira · JQL
# My queue, most urgent first
$ project = SD AND assignee = currentUser() AND statusCategory != Done ORDER BY priority DESC, created ASC
# Unassigned tickets about to breach the SLA in the next hour
$ project = SD AND assignee IS EMPTY AND "Time to first response" < remaining("1h")
# Everything this user has opened (to see if it is recurring)
$ project = SD AND reporter = "laura.prado@contoso.com" ORDER BY created DESC
# What has been waiting for the vendor for more than 5 days
$ project = SD AND status = "Waiting for vendor" AND updated < -5d
:::

Save the first two as filters and put them on your board: the queue stops being a list and becomes a plan.

## Next steps

- When you see the same ticket three times, open a linked **problem**: that is where the root cause lives, and the incidents only link to it.
- Learn to write a **knowledge base** article from the ticket: Jira suggests it to the user before they open the next one.
- In Level 2 you'll see Confluence and, in Level 4, how the project's workflows, SLAs and automations are administered.
""")

# ---------------------------------------------------------------- 8 · Microsoft 365 y licencias
g(slug="microsoft-365-asignar-y-retirar-licencias", topic="m365", date="2026-10-21",
  title_es="Microsoft 365: asignar y retirar licencias, y saber qué incluye cada una",
  title_en="Microsoft 365: assigning and removing licences, and knowing what each one includes",
  dek_es="Desde el centro de administración y desde PowerShell con Microsoft Graph, con los errores típicos y la baja de un usuario sin perder su buzón.",
  dek_en="From the admin centre and from PowerShell with Microsoft Graph, with the typical errors and a leaver's offboarding without losing their mailbox.",
  es="""
## Qué vas a conseguir

Un usuario nuevo con su licencia y sus aplicaciones en marcha, un usuario que se va sin que la empresa pierda su correo, y una idea clara de qué da cada licencia para no asignar E5 a quien solo necesita correo.

## Antes de empezar

- Un rol que pueda tocar licencias: **Administrador de licencias** es el mínimo; no uses Administrador global para esto.
- Saber si tu empresa asigna licencias **por grupo** (licencias basadas en grupos de Entra ID) o **directamente** al usuario. Si es por grupo, tu trabajo es meter al usuario en el grupo correcto, no asignar la licencia a mano.
- Para PowerShell, el módulo `Microsoft.Graph` (`Install-Module Microsoft.Graph -Scope CurrentUser`). El módulo antiguo `MSOnline` ya no funciona.

## 1. Qué incluye cada licencia (lo que preguntan en los tickets)

| | Business Basic / E1 | Business Standard | E3 | E5 |
|---|---|---|---|---|
| Correo (Exchange Online) | 50 GB | 50 GB | 100 GB | 100 GB |
| Office de escritorio (Word, Excel…) | solo web | sí | sí | sí |
| Teams | sí | sí | sí (según región, aparte) | sí |
| Intune y Entra ID P1 | no | no | sí | sí |
| Defender, Purview avanzado, Entra ID P2 | no | no | no | sí |

Las que más líos dan: **F3** (primera línea: correo de 2 GB, sin Office de escritorio), **Exchange Online Plan 1/2** (solo correo, para buzones de servicio con usuario) y los **complementos** (Teams Phone, Power BI Pro, Copilot) que se suman a una base.

## 2. Asignar desde el centro de administración

:::ui Microsoft 365 · Centro de administración
> Usuarios › Usuarios activos › Laura Prado › Licencias y aplicaciones
= Ubicación de uso: España
[x] Microsoft 365 E3 (312 de 350 disponibles)
[ ] Power BI Pro (0 de 40 disponibles)
> Aplicaciones › Microsoft 365 E3
[x] Exchange Online (Plan 2)
[x] Microsoft Intune
[ ] Yammer Enterprise
[Guardar cambios]
:::

Dos cosas que fallan siempre:

- **Ubicación de uso vacía**: la licencia no se puede asignar hasta ponerla. Si el usuario viene de Active Directory, el atributo `msExchUsageLocation` o la sincronización deberían rellenarla; si no, ponla a mano.
- **0 disponibles**: no quedan licencias. No reasignes la de otro sin un ticket aprobado: pide compra o pregunta al propietario de las licencias qué usuario de baja todavía la tiene.

## 3. Asignar con PowerShell (Graph)

:::term PowerShell · Microsoft Graph
$ Connect-MgGraph -Scopes "User.ReadWrite.All","Organization.Read.All"
$ Get-MgSubscribedSku | Select-Object SkuPartNumber, @{n="Usadas";e={$_.ConsumedUnits}}, @{n="Total";e={$_.PrepaidUnits.Enabled}}
SkuPartNumber   Usadas Total
-------------   ------ -----
SPE_E3             312   350
POWER_BI_PRO        40    40
EXCHANGESTANDARD    18    25
$ Update-MgUser -UserId laura.prado@contoso.com -UsageLocation ES
$ $e3 = (Get-MgSubscribedSku | Where-Object SkuPartNumber -eq "SPE_E3").SkuId
$ Set-MgUserLicense -UserId laura.prado@contoso.com -AddLicenses @{SkuId = $e3} -RemoveLicenses @()
$ (Get-MgUserLicenseDetail -UserId laura.prado@contoso.com).SkuPartNumber
SPE_E3
:::

Los nombres internos no coinciden con los comerciales: `SPE_E3` es Microsoft 365 E3, `ENTERPRISEPACK` es Office 365 E3, `SPB` es Business Premium, `DESKLESSPACK` es F3. Hay una tabla oficial de Microsoft con todos; ten el enlace a mano.

> Si la licencia viene por grupo, `Get-MgUserLicenseDetail` la muestra igual, pero al intentar quitarla a mano dará error: hay que sacar al usuario del grupo.

## 4. El usuario tiene licencia pero "no le funciona"

- **Outlook o Teams dicen que no tiene licencia**: espera hasta 30 minutos tras asignarla, y que cierre sesión y vuelva a entrar. Si persiste, en el centro de administración el usuario mostrará un error de aprovisionamiento en la licencia (texto rojo bajo el servicio).
- **Office de escritorio pide activación**: tiene E1 o Basic (solo web). O tiene E3 pero el servicio **Microsoft 365 Apps for enterprise** está desmarcado en la licencia.
- **Error de aprovisionamiento con conflicto**: dos licencias con el mismo servicio (Exchange Online Plan 1 junto a E3, por ejemplo). Quita la pequeña.
- **La licencia la pone un grupo y el usuario no la tiene**: mira en Entra ID → Grupos → el grupo → Licencias → **Errores de procesamiento**; casi siempre es ubicación de uso vacía o que no quedan licencias.

## 5. La baja: retirar la licencia sin perder el buzón

El error clásico es quitar la licencia el primer día y descubrir que el buzón desaparece a los 30 días con el correo que necesitaba el responsable. El orden correcto:

1. Bloquear el inicio de sesión (`Update-MgUser -AccountEnabled:$false`) y revocar las sesiones (`Revoke-MgUserSignInSession`).
2. Convertir el buzón en **compartido** desde Exchange Online (no necesita licencia si tiene menos de 50 GB y no tiene archivo) y dar permiso al responsable. Esto va en la guía de Outlook y Exchange Online.
3. Quitar la licencia. Ahora sí: el buzón compartido se queda.
4. Si la licencia es por grupo, sacar al usuario de los grupos de licencia; si es directa, `Set-MgUserLicense -RemoveLicenses @($e3) -AddLicenses @()`.
5. Apuntar en el ticket la fecha de cada paso y cuándo caduca la retención del buzón compartido según vuestra política.

## Siguientes pasos

- Si asignáis licencias a mano, propón pasar a licencias por grupo: una alta es meter al usuario en un grupo y no se olvida ningún servicio.
- Un informe mensual de licencias asignadas a usuarios deshabilitados o sin inicio de sesión en 90 días paga más de una renovación.
- En el Nivel 4 verás el gobierno del tenant completo: roles de administración, PIM, Conditional Access y la revisión mensual con el proveedor.
""",
  en="""
## What you'll get

A new user with their licence and apps working, a leaver who goes without the company losing their email, and a clear idea of what each licence gives so you don't assign E5 to someone who only needs email.

## Before you start

- A role that can touch licences: **Licence Administrator** is the minimum; don't use Global Administrator for this.
- Know whether your company assigns licences **by group** (Entra ID group-based licensing) or **directly** to the user. If by group, your job is to put the user in the right group, not to assign the licence by hand.
- For PowerShell, the `Microsoft.Graph` module (`Install-Module Microsoft.Graph -Scope CurrentUser`). The old `MSOnline` module no longer works.

## 1. What each licence includes (what tickets ask)

| | Business Basic / E1 | Business Standard | E3 | E5 |
|---|---|---|---|---|
| Email (Exchange Online) | 50 GB | 50 GB | 100 GB | 100 GB |
| Desktop Office (Word, Excel…) | web only | yes | yes | yes |
| Teams | yes | yes | yes (separate in some regions) | yes |
| Intune and Entra ID P1 | no | no | yes | yes |
| Defender, advanced Purview, Entra ID P2 | no | no | no | yes |

The ones that cause the most confusion: **F3** (frontline: 2 GB mailbox, no desktop Office), **Exchange Online Plan 1/2** (email only, for service mailboxes with a user) and the **add-ons** (Teams Phone, Power BI Pro, Copilot) that sit on top of a base.

## 2. Assign from the admin centre

:::ui Microsoft 365 · Admin centre
> Users › Active users › Laura Prado › Licences and apps
= Usage location: Spain
[x] Microsoft 365 E3 (312 of 350 available)
[ ] Power BI Pro (0 of 40 available)
> Apps › Microsoft 365 E3
[x] Exchange Online (Plan 2)
[x] Microsoft Intune
[ ] Yammer Enterprise
[Save changes]
:::

Two things that always fail:

- **Empty usage location**: the licence cannot be assigned until it is set. If the user comes from Active Directory, the `msExchUsageLocation` attribute or the sync should fill it; if not, set it by hand.
- **0 available**: no licences left. Don't reassign someone else's without an approved ticket: request a purchase or ask the licence owner which leaver still holds one.

## 3. Assign with PowerShell (Graph)

:::term PowerShell · Microsoft Graph
$ Connect-MgGraph -Scopes "User.ReadWrite.All","Organization.Read.All"
$ Get-MgSubscribedSku | Select-Object SkuPartNumber, @{n="Used";e={$_.ConsumedUnits}}, @{n="Total";e={$_.PrepaidUnits.Enabled}}
SkuPartNumber   Used Total
-------------   ---- -----
SPE_E3           312   350
POWER_BI_PRO      40    40
EXCHANGESTANDARD  18    25
$ Update-MgUser -UserId laura.prado@contoso.com -UsageLocation ES
$ $e3 = (Get-MgSubscribedSku | Where-Object SkuPartNumber -eq "SPE_E3").SkuId
$ Set-MgUserLicense -UserId laura.prado@contoso.com -AddLicenses @{SkuId = $e3} -RemoveLicenses @()
$ (Get-MgUserLicenseDetail -UserId laura.prado@contoso.com).SkuPartNumber
SPE_E3
:::

Internal names don't match the commercial ones: `SPE_E3` is Microsoft 365 E3, `ENTERPRISEPACK` is Office 365 E3, `SPB` is Business Premium, `DESKLESSPACK` is F3. Microsoft publishes an official table with all of them; keep the link handy.

> If the licence comes from a group, `Get-MgUserLicenseDetail` shows it just the same, but trying to remove it by hand errors out: the user has to leave the group.

## 4. The user has a licence but "it doesn't work"

- **Outlook or Teams say there is no licence**: wait up to 30 minutes after assigning, and have them sign out and in again. If it persists, the admin centre shows a provisioning error on the licence (red text under the service).
- **Desktop Office asks for activation**: they have E1 or Basic (web only). Or they have E3 but the **Microsoft 365 Apps for enterprise** service is unticked in the licence.
- **Provisioning error with a conflict**: two licences with the same service (Exchange Online Plan 1 alongside E3, for example). Remove the small one.
- **The licence comes from a group and the user doesn't have it**: look in Entra ID → Groups → the group → Licences → **Processing errors**; it is almost always an empty usage location or no licences left.

## 5. The leaver: removing the licence without losing the mailbox

The classic mistake is removing the licence on day one and discovering the mailbox vanished after 30 days along with the email the manager needed. The right order:

1. Block sign-in (`Update-MgUser -AccountEnabled:$false`) and revoke sessions (`Revoke-MgUserSignInSession`).
2. Convert the mailbox to **shared** in Exchange Online (no licence needed if it is under 50 GB and has no archive) and give the manager permission. That is in the Outlook and Exchange Online guide.
3. Remove the licence. Now it is safe: the shared mailbox stays.
4. If the licence is group-based, remove the user from the licence groups; if direct, `Set-MgUserLicense -RemoveLicenses @($e3) -AddLicenses @()`.
5. Note the date of each step in the ticket and when the shared mailbox's retention expires under your policy.

## Next steps

- If you assign licences by hand, propose moving to group-based licensing: a joiner becomes adding the user to a group, and no service gets forgotten.
- A monthly report of licences assigned to disabled users or users with no sign-in for 90 days pays for more than one renewal.
- In Level 4 you'll see the full tenant governance: admin roles, PIM, Conditional Access and the monthly review with the provider.
""")

# ---------------------------------------------------------------- 9 · Microsoft Teams
g(slug="teams-los-problemas-mas-comunes", topic="teams", date="2026-10-21",
  title_es="Microsoft Teams: los cinco problemas que más llegan y cómo resolverlos",
  title_en="Microsoft Teams: the five issues that come up most and how to fix them",
  dek_es="No abre o va lento, no se oye, el estado no cambia, no aparece un equipo o un canal, y la cámara no funciona en la reunión.",
  dek_en="Won't open or runs slow, no audio, the status won't change, a team or channel is missing, and the camera fails in the meeting.",
  es="""
## Qué vas a conseguir

Resolver en la primera llamada los tickets de Teams que se repiten cada semana, y saber cuáles son de verdad del cliente, cuáles del equipo y cuáles de la configuración del tenant (esos se escalan con los datos correctos).

## Antes de empezar

- El usuario está en el **nuevo Teams** (el icono sin la "T" dentro de un cuadrado morado antiguo). El Teams clásico ya no recibe soporte; si lo tiene, lo primero es actualizar.
- Tienes acceso de lectura al **centro de administración de Teams** (`admin.teams.microsoft.com`), aunque sea solo para mirar.
- Antes de tocar nada, comprueba el **estado del servicio** en el centro de administración de Microsoft 365 → Estado → Estado del servicio. Si Teams está en incidente, el ticket es "esperar a Microsoft", y hay que decírselo así al usuario.

## 1. No abre, se queda en blanco o va muy lento

Casi siempre es la caché local. Limpiarla no borra nada del usuario (chats, archivos y configuración están en la nube).

:::term PowerShell · usuario
# Cerrar Teams del todo (también el icono de la bandeja)
$ Get-Process -Name "ms-teams","msteams" -ErrorAction SilentlyContinue | Stop-Process -Force
# Caché del nuevo Teams
$ Remove-Item "$env:LOCALAPPDATA\\Packages\\MSTeams_8wekyb3d8bbwe\\LocalCache\\Microsoft\\MSTeams" -Recurse -Force -ErrorAction SilentlyContinue
# Si todavía queda el Teams clásico
$ Remove-Item "$env:APPDATA\\Microsoft\\Teams" -Recurse -Force -ErrorAction SilentlyContinue
$ Start-Process "ms-teams:"
:::

Si tras limpiar la caché sigue sin abrir, **repara** la aplicación: Configuración → Aplicaciones → Microsoft Teams → Opciones avanzadas → Reparar. Y si el equipo va lento en general (no solo Teams), es el equipo: mira la guía de Windows.

## 2. No se oye o no me oyen

1. En Teams: **Configuración → Dispositivos**: el altavoz y el micrófono tienen que ser los auriculares, no "Micrófono (Realtek)" del portátil. Teams cambia de dispositivo solo cuando se conecta uno nuevo, y a veces elige mal.
2. En Windows: **Configuración → Privacidad y seguridad → Micrófono**: "Permitir que las aplicaciones accedan al micrófono" activado. Una actualización de Windows o un portátil nuevo a veces lo deja apagado.
3. Haz una **llamada de prueba** desde Configuración → Dispositivos: si se oye el eco, el audio funciona y el problema es de la reunión del otro lado.
4. Auriculares con base o Bluetooth: cámbialos al USB directo. Los Bluetooth dan problemas con el perfil de manos libres en Windows.

:::ui Teams · Configuración › Dispositivos
= Dispositivos de audio: Auriculares USB Jabra Evolve2
= Altavoz: Auriculares (Jabra Evolve2 40)
= Micrófono: Micrófono de auriculares (Jabra Evolve2 40)
= Cámara: HD Pro Webcam C920
[Hacer una llamada de prueba]
:::

## 3. El estado no cambia o aparece "Sin conexión"

- Si el estado está **fijado** a mano (Disponible, Ocupado…), Teams no lo cambia solo. Que lo ponga en "Restablecer estado".
- "Ausente" cuando está trabajando: Teams se basa en la actividad del equipo; si trabaja con el portátil cerrado y un monitor, o con una sesión remota, puede marcarlo ausente. Es comportamiento esperado, no un fallo.
- "Sin conexión" todo el día: casi siempre caché (punto 1) o el reloj del equipo desajustado (el inicio de sesión moderno necesita la hora bien puesta).
- El estado viene del **calendario de Exchange**: si Outlook no funciona, "En una reunión" tampoco. Primero arregla el correo.

## 4. No aparece un equipo, un canal o un archivo

- Un equipo al que lo acaban de añadir tarda hasta una hora en aparecer. Que cierre y abra Teams; si no, limpia la caché.
- Un **canal privado** solo lo ven sus miembros; el propietario del equipo los gestiona, no IT. Pide al propietario que lo añada.
- "No tienes acceso a este archivo": los archivos de un canal viven en SharePoint; si el usuario fue añadido al equipo pero no a SharePoint (pasa cuando se le añade desde un grupo anidado), el propietario tiene que quitarlo y volver a añadirlo.
- Un equipo que desapareció para todos: puede estar **archivado** o eliminado. Los eliminados se recuperan 30 días desde el centro de administración → Equipos → el equipo eliminado → Restaurar.

## 5. La cámara no va en la reunión

1. Prueba la cámara en la aplicación **Cámara** de Windows. Si ahí tampoco, es Windows o el controlador: Administrador de dispositivos → Cámaras → desinstalar y reconectar.
2. Si en Cámara va y en Teams no: **Configuración → Privacidad y seguridad → Cámara**, acceso permitido para aplicaciones de escritorio.
3. Otra aplicación tiene la cámara abierta (Zoom, el navegador con una reunión anterior, Skype). Ciérrala.
4. En equipos con **base de carga**, cámara externa conectada a la base: prueba directa al USB del portátil.

## 6. Qué poner en el ticket al escalar

Versión de Teams (Configuración → Acerca de), si pasa en el navegador (`teams.microsoft.com`) o solo en la app, desde cuándo, y si le pasa a más gente. Un problema que ocurre también en el navegador no es del cliente: es del tenant o de Microsoft, y el equipo de Microsoft 365 lo ve en el centro de administración de Teams → Usuarios → el usuario → **Llamadas y reuniones** (la calidad de cada llamada de los últimos 30 días).

## Siguientes pasos

- Añade a la base de conocimiento el script del punto 1: el 40 % de los tickets de Teams se cierran con él.
- Para auriculares y cámaras, pide a compras una lista corta de modelos certificados para Teams: cada modelo nuevo es un tipo de ticket nuevo.
- En el Nivel 2 verás Microsoft Teams Rooms: las salas con Crestron, Logitech y Poly, y cómo se gestionan desde el Pro Management Portal.
""",
  en="""
## What you'll get

Close the Teams tickets that repeat every week on the first call, and know which ones are really the client, which the device, and which the tenant configuration (those get escalated with the right data).

## Before you start

- The user is on the **new Teams** (the icon without the old "T" inside a purple square). Classic Teams is no longer supported; if they have it, update first.
- You have read access to the **Teams admin centre** (`admin.teams.microsoft.com`), even if only to look.
- Before touching anything, check the **service health** in the Microsoft 365 admin centre → Health → Service health. If Teams has an incident, the ticket is "wait for Microsoft", and the user should be told exactly that.

## 1. Won't open, stays blank or runs very slow

It is almost always the local cache. Clearing it deletes nothing of the user's (chats, files and settings live in the cloud).

:::term PowerShell · user
# Close Teams completely (tray icon too)
$ Get-Process -Name "ms-teams","msteams" -ErrorAction SilentlyContinue | Stop-Process -Force
# New Teams cache
$ Remove-Item "$env:LOCALAPPDATA\\Packages\\MSTeams_8wekyb3d8bbwe\\LocalCache\\Microsoft\\MSTeams" -Recurse -Force -ErrorAction SilentlyContinue
# If classic Teams is still around
$ Remove-Item "$env:APPDATA\\Microsoft\\Teams" -Recurse -Force -ErrorAction SilentlyContinue
$ Start-Process "ms-teams:"
:::

If it still won't open after clearing the cache, **repair** the app: Settings → Apps → Microsoft Teams → Advanced options → Repair. And if the device is slow in general (not only Teams), it is the device: see the Windows guide.

## 2. No audio, or they can't hear me

1. In Teams: **Settings → Devices**: speaker and microphone have to be the headset, not the laptop's "Microphone (Realtek)". Teams switches device on its own when a new one is plugged in, and sometimes picks wrong.
2. In Windows: **Settings → Privacy & security → Microphone**: "Let apps access your microphone" on. A Windows update or a new laptop sometimes leaves it off.
3. Make a **test call** from Settings → Devices: if the echo plays back, audio works and the problem is on the other side of the meeting.
4. Headsets on a dock or Bluetooth: switch them to direct USB. Bluetooth gives trouble with the hands-free profile on Windows.

:::ui Teams · Settings › Devices
= Audio devices: Jabra Evolve2 USB headset
= Speaker: Headset (Jabra Evolve2 40)
= Microphone: Headset microphone (Jabra Evolve2 40)
= Camera: HD Pro Webcam C920
[Make a test call]
:::

## 3. The status won't change or shows "Offline"

- If the status is **set** by hand (Available, Busy…), Teams won't change it on its own. Have them pick "Reset status".
- "Away" while working: Teams goes by device activity; working with the laptop lid closed and a monitor, or in a remote session, can mark them away. That is expected behaviour, not a fault.
- "Offline" all day: almost always cache (point 1) or the device clock off (modern sign-in needs the right time).
- The status comes from the **Exchange calendar**: if Outlook is broken, "In a meeting" is too. Fix email first.

## 4. A team, a channel or a file is missing

- A team they were just added to takes up to an hour to appear. Have them close and open Teams; if not, clear the cache.
- A **private channel** is only visible to its members; the team owner manages them, not IT. Ask the owner to add them.
- "You don't have access to this file": channel files live in SharePoint; if the user was added to the team but not to SharePoint (it happens when added through a nested group), the owner has to remove and re-add them.
- A team that vanished for everyone: it may be **archived** or deleted. Deleted ones are recoverable for 30 days from the admin centre → Teams → the deleted team → Restore.

## 5. The camera fails in the meeting

1. Test the camera in the Windows **Camera** app. If it fails there too, it is Windows or the driver: Device Manager → Cameras → uninstall and reconnect.
2. If Camera works and Teams doesn't: **Settings → Privacy & security → Camera**, access allowed for desktop apps.
3. Another app holds the camera (Zoom, the browser with an earlier meeting, Skype). Close it.
4. On devices with a **dock**, external camera on the dock: try it straight into the laptop's USB.

## 6. What to put in the ticket when escalating

Teams version (Settings → About), whether it happens in the browser (`teams.microsoft.com`) or only in the app, since when, and whether it affects more people. A problem that also happens in the browser is not the client: it is the tenant or Microsoft, and the Microsoft 365 team sees it in the Teams admin centre → Users → the user → **Meetings & calls** (the quality of every call from the last 30 days).

## Next steps

- Add the script from point 1 to the knowledge base: 40% of Teams tickets close with it.
- For headsets and cameras, ask purchasing for a short list of Teams-certified models: every new model is a new kind of ticket.
- In Level 2 you'll see Microsoft Teams Rooms: rooms on Crestron, Logitech and Poly, and how they are managed from the Pro Management Portal.
""")

# ---------------------------------------------------------------- 10 · Outlook y Exchange Online
g(slug="outlook-exchange-online-buzon-compartido-permisos-autorespuesta", topic="outlook", date="2026-10-21",
  title_es="Outlook y Exchange Online: buzón compartido, permisos y respuesta automática",
  title_en="Outlook and Exchange Online: shared mailbox, permissions and automatic replies",
  dek_es="Las tres peticiones de correo más frecuentes resueltas con PowerShell, y qué hacer con un Outlook que no abre o no sincroniza.",
  dek_en="The three most frequent email requests solved with PowerShell, and what to do with an Outlook that won't open or sync.",
  es="""
## Qué vas a conseguir

Crear un buzón compartido y dar acceso a un equipo, dar permisos sobre el buzón o el calendario de otra persona, poner una respuesta automática a quien no puede hacerlo (o se ha ido), y un método para "Outlook no me abre".

## Antes de empezar

- Rol de **Administrador de Exchange** o **Administrador de destinatarios** (este último basta para buzones y permisos).
- El módulo `ExchangeOnlineManagement` (`Install-Module ExchangeOnlineManagement -Scope CurrentUser`) y `Connect-ExchangeOnline`.
- Para permisos sobre el buzón de otra persona, un ticket aprobado por el propietario del buzón o su responsable. Nunca por la petición del que quiere entrar.

## 1. Buzón compartido

:::term PowerShell · Exchange Online
$ Connect-ExchangeOnline
$ New-Mailbox -Shared -Name "Soporte Ventas" -DisplayName "Soporte Ventas" -PrimarySmtpAddress soporte.ventas@contoso.com
$ Add-MailboxPermission -Identity soporte.ventas@contoso.com -User GG-Ventas -AccessRights FullAccess -AutoMapping $true
$ Add-RecipientPermission -Identity soporte.ventas@contoso.com -Trustee GG-Ventas -AccessRights SendAs -Confirm:$false
$ Get-MailboxPermission soporte.ventas@contoso.com | Where-Object User -notlike "NT AUTHORITY*" | Select-Object User, AccessRights
User                    AccessRights
----                    ------------
GG-Ventas               {FullAccess}
:::

- **FullAccess** abre el buzón; **SendAs** permite enviar como el buzón; **SendOnBehalf** (`Set-Mailbox -GrantSendOnBehalfTo`) envía "en nombre de". Pregunta cuál quieren: casi siempre es SendAs.
- Con `-AutoMapping $true`, el buzón aparece solo en Outlook en una hora (a veces hace falta cerrar y abrir). Para un grupo, el automapeo no funciona en todas las versiones: si no aparece, el usuario lo añade a mano en **Archivo → Configuración de la cuenta → Más opciones → Buzones de correo**.
- Un buzón compartido no necesita licencia si tiene menos de 50 GB y no usa archivo ni retención por litigio. Nadie debe iniciar sesión en él directamente: no tiene contraseña por diseño.

## 2. Permisos sobre el buzón o el calendario de otra persona

:::term PowerShell · Exchange Online
# Acceso completo al buzón del responsable (por ejemplo, su asistente)
$ Add-MailboxPermission -Identity carlos.rey@contoso.com -User ana.sol@contoso.com -AccessRights FullAccess -AutoMapping $true
# Solo el calendario: Editor puede crear y modificar, Reviewer solo leer
$ Add-MailboxFolderPermission -Identity "carlos.rey@contoso.com:\\Calendario" -User ana.sol@contoso.com -AccessRights Editor
$ Get-MailboxFolderPermission -Identity "carlos.rey@contoso.com:\\Calendario"
FolderName User     AccessRights
---------- ----     ------------
Calendario Default  {AvailabilityOnly}
Calendario Ana Sol  {Editor}
:::

El nombre de la carpeta depende del idioma del buzón: `\\Calendario` en español, `\\Calendar` en inglés. Si el comando dice que la carpeta no existe, prueba el otro. Y apunta en el ticket quién aprobó el acceso.

## 3. Respuesta automática para otro usuario

Para una baja, una ausencia larga o un usuario que no puede hacerlo él mismo:

:::term PowerShell · Exchange Online
$ Set-MailboxAutoReplyConfiguration -Identity laura.prado@contoso.com -AutoReplyState Scheduled -StartTime "27/10/2026 00:00" -EndTime "07/11/2026 23:59" -InternalMessage "Estoy fuera de la oficina hasta el 10 de noviembre. Para temas urgentes, escribe a soporte.ventas@contoso.com." -ExternalMessage "I am out of the office until 10 November. For urgent matters, please contact soporte.ventas@contoso.com." -ExternalAudience All
$ Get-MailboxAutoReplyConfiguration laura.prado@contoso.com | Select-Object AutoReplyState, StartTime, EndTime
AutoReplyState : Scheduled
StartTime      : 27/10/2026 0:00:00
EndTime        : 07/11/2026 23:59:00
:::

Para una baja definitiva, `-AutoReplyState Enabled` sin fechas, y el texto lo decide el responsable: nunca inventes el motivo de la ausencia.

## 4. Outlook no abre o no sincroniza

En orden, y para en el primero que funcione:

1. **¿Funciona en el navegador?** `outlook.office.com`. Si sí, el buzón está bien y el problema es el cliente. Si no, es la cuenta (licencia, contraseña, MFA, bloqueo) y Outlook no tiene la culpa.
2. **Modo seguro**: `outlook.exe /safe`. Si abre, es un complemento: Archivo → Opciones → Complementos → Administrar complementos COM → Ir, y desactiva los de terceros uno a uno.
3. **Estado de la conexión**: con Ctrl pulsado, botón derecho sobre el icono de Outlook en la bandeja → **Estado de conexión**. Todo tiene que estar "Establecido"; si hay "Desconectado" con el buzón bien en el navegador, es la red del equipo (proxy, VPN) o el perfil.
4. **Perfil nuevo**: Panel de control → Correo → Mostrar perfiles → Agregar. Un perfil nuevo tarda en descargar el correo, pero resuelve casi todo lo que queda. No borres el antiguo hasta comprobar que el nuevo funciona.
5. **Archivo OST demasiado grande o corrupto**: si Outlook abre pero tarda minutos o se cierra, baja el tiempo de correo sin conexión (Archivo → Configuración de la cuenta → la cuenta → Cambiar → 1 año) o renombra el `.ost` en `%LOCALAPPDATA%\\Microsoft\\Outlook` con Outlook cerrado: se vuelve a crear.

> Una regla de reenvío creada por el usuario (o por alguien que entró en su cuenta) es la causa de la mitad de los "me llegan correos raros" y "no me llegan correos". `Get-InboxRule -Mailbox laura.prado@contoso.com` las lista; si ves una que reenvía fuera, es un ticket de seguridad, no de soporte.

## Siguientes pasos

- Todos los permisos de buzón deberían pasar por un grupo, no por usuarios: cuando alguien cambia de puesto, lo quitas de un sitio.
- Un informe trimestral de `Get-MailboxPermission` sobre buzones de dirección evita sorpresas en auditoría.
- En el Nivel 2 verás reglas de transporte, DKIM/DMARC y el rastreo de mensajes; en el 4, Purview, DLP y las etiquetas de confidencialidad.
""",
  en="""
## What you'll get

Create a shared mailbox and give a team access, grant permissions on someone else's mailbox or calendar, set an automatic reply for someone who cannot (or has left), and a method for "Outlook won't open".

## Before you start

- The **Exchange Administrator** or **Recipient Administrator** role (the latter is enough for mailboxes and permissions).
- The `ExchangeOnlineManagement` module (`Install-Module ExchangeOnlineManagement -Scope CurrentUser`) and `Connect-ExchangeOnline`.
- For permissions on someone else's mailbox, a ticket approved by the mailbox owner or their manager. Never on the request of the person who wants in.

## 1. Shared mailbox

:::term PowerShell · Exchange Online
$ Connect-ExchangeOnline
$ New-Mailbox -Shared -Name "Sales Support" -DisplayName "Sales Support" -PrimarySmtpAddress sales.support@contoso.com
$ Add-MailboxPermission -Identity sales.support@contoso.com -User GG-Sales -AccessRights FullAccess -AutoMapping $true
$ Add-RecipientPermission -Identity sales.support@contoso.com -Trustee GG-Sales -AccessRights SendAs -Confirm:$false
$ Get-MailboxPermission sales.support@contoso.com | Where-Object User -notlike "NT AUTHORITY*" | Select-Object User, AccessRights
User                    AccessRights
----                    ------------
GG-Sales                {FullAccess}
:::

- **FullAccess** opens the mailbox; **SendAs** sends as the mailbox; **SendOnBehalf** (`Set-Mailbox -GrantSendOnBehalfTo`) sends "on behalf of". Ask which one they want: it is almost always SendAs.
- With `-AutoMapping $true`, the mailbox appears in Outlook on its own within an hour (sometimes a restart is needed). For a group, automapping does not work in every version: if it does not show up, the user adds it by hand under **File → Account Settings → More settings → Mailboxes**.
- A shared mailbox needs no licence if it is under 50 GB and uses no archive or litigation hold. Nobody should sign in to it directly: it has no password by design.

## 2. Permissions on someone else's mailbox or calendar

:::term PowerShell · Exchange Online
# Full access to the manager's mailbox (their assistant, for example)
$ Add-MailboxPermission -Identity carlos.rey@contoso.com -User ana.sol@contoso.com -AccessRights FullAccess -AutoMapping $true
# Calendar only: Editor can create and change, Reviewer can only read
$ Add-MailboxFolderPermission -Identity "carlos.rey@contoso.com:\\Calendar" -User ana.sol@contoso.com -AccessRights Editor
$ Get-MailboxFolderPermission -Identity "carlos.rey@contoso.com:\\Calendar"
FolderName User     AccessRights
---------- ----     ------------
Calendar   Default  {AvailabilityOnly}
Calendar   Ana Sol  {Editor}
:::

The folder name depends on the mailbox language: `\\Calendar` in English, `\\Calendario` in Spanish. If the command says the folder does not exist, try the other. And note in the ticket who approved the access.

## 3. Automatic reply for another user

For a leaver, a long absence or a user who cannot do it themselves:

:::term PowerShell · Exchange Online
$ Set-MailboxAutoReplyConfiguration -Identity laura.prado@contoso.com -AutoReplyState Scheduled -StartTime "27/10/2026 00:00" -EndTime "07/11/2026 23:59" -InternalMessage "I am out of the office until 10 November. For urgent matters, please contact sales.support@contoso.com." -ExternalMessage "I am out of the office until 10 November. For urgent matters, please contact sales.support@contoso.com." -ExternalAudience All
$ Get-MailboxAutoReplyConfiguration laura.prado@contoso.com | Select-Object AutoReplyState, StartTime, EndTime
AutoReplyState : Scheduled
StartTime      : 27/10/2026 0:00:00
EndTime        : 07/11/2026 23:59:00
:::

For a permanent leaver, `-AutoReplyState Enabled` with no dates, and the manager decides the text: never make up the reason for the absence.

## 4. Outlook won't open or sync

In order, stopping at the first that works:

1. **Does it work in the browser?** `outlook.office.com`. If yes, the mailbox is fine and the problem is the client. If not, it is the account (licence, password, MFA, lockout) and Outlook is not to blame.
2. **Safe mode**: `outlook.exe /safe`. If it opens, it is an add-in: File → Options → Add-ins → Manage COM Add-ins → Go, and disable the third-party ones one at a time.
3. **Connection status**: with Ctrl held, right-click the Outlook tray icon → **Connection Status**. Everything has to be "Established"; if there is "Disconnected" with the mailbox fine in the browser, it is the device's network (proxy, VPN) or the profile.
4. **New profile**: Control Panel → Mail → Show Profiles → Add. A new profile takes a while to download mail, but it fixes almost everything left. Don't delete the old one until the new one is confirmed working.
5. **OST file too large or corrupt**: if Outlook opens but takes minutes or crashes, reduce the offline mail period (File → Account Settings → the account → Change → 1 year) or rename the `.ost` in `%LOCALAPPDATA%\\Microsoft\\Outlook` with Outlook closed: it is recreated.

> A forwarding rule created by the user (or by someone who got into their account) is the cause of half the "I get strange emails" and "emails don't reach me" tickets. `Get-InboxRule -Mailbox laura.prado@contoso.com` lists them; if you see one forwarding outside, it is a security ticket, not a support one.

## Next steps

- Every mailbox permission should go through a group, not through users: when someone changes role, you remove them from one place.
- A quarterly `Get-MailboxPermission` report on executive mailboxes avoids audit surprises.
- In Level 2 you'll see transport rules, DKIM/DMARC and message trace; in Level 4, Purview, DLP and sensitivity labels.
""")

# ---------------------------------------------------------------- 11 · Windows 10 y 11
g(slug="windows-diagnostico-basico-equipo-lento-o-con-errores", topic="windows", date="2026-10-21",
  title_es="Windows 10 y 11: diagnóstico básico de un equipo lento, con errores o que no sincroniza con Intune",
  title_en="Windows 10 and 11: basic diagnosis of a slow device, one with errors, or one not syncing with Intune",
  dek_es="Diez minutos de comprobaciones con un orden fijo: versión y actualizaciones, disco y memoria, integridad del sistema, eventos, y el estado de Entra ID e Intune.",
  dek_en="Ten minutes of checks in a fixed order: version and updates, disk and memory, system integrity, events, and the Entra ID and Intune state.",
  es="""
## Qué vas a conseguir

Saber en diez minutos si un equipo "va lento" por el disco, la memoria, una actualización a medias o algo roto en el sistema, y si está bien unido a Entra ID y recibe las políticas de Intune. Con los resultados, o lo arreglas o lo escalas con datos.

## Antes de empezar

- Una consola de PowerShell **como administrador** en el equipo (en remoto, con la herramienta de asistencia que use tu empresa).
- El nombre del equipo y el usuario del ticket.
- Diez minutos sin que el usuario necesite el equipo: algunas comprobaciones consumen CPU.

## 1. Qué equipo es y en qué versión está

:::term PowerShell · como administrador
$ Get-ComputerInfo | Select-Object CsName, OsName, OsVersion, OsBuildNumber, CsManufacturer, CsModel, OsLastBootUpTime
CsName           : LAPTOP-7F2K9Q
OsName           : Microsoft Windows 11 Enterprise
OsVersion        : 10.0.26100
OsBuildNumber    : 26100
CsManufacturer   : Fabrikam
CsModel          : Portable 14 G3
OsLastBootUpTime : 03/10/2026 8:12:40
$ Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 3 HotFixID, InstalledOn
HotFixID  InstalledOn
--------  -----------
KB5044284 09/10/2026
KB5043080 11/09/2026
:::

Dos cosas que ya te dicen mucho: **OsLastBootUpTime** de hace 18 días significa que el equipo no se ha reiniciado (el apagado rápido de Windows no cuenta como reinicio) y, si hay una actualización pendiente de reinicio, va lento por eso. Y una **build** antigua (Windows 10 en 2026, o un Windows 11 de hace dos versiones) es un equipo que no recibe parches: hay que ponerlo al día antes de nada.

## 2. Disco y memoria

:::term PowerShell · como administrador
$ Get-PSDrive C | Select-Object @{n="UsadoGB";e={[math]::Round($_.Used/1GB)}}, @{n="LibreGB";e={[math]::Round($_.Free/1GB)}}
UsadoGB LibreGB
------- -------
    455      21
$ Get-PhysicalDisk | Select-Object FriendlyName, MediaType, HealthStatus
FriendlyName            MediaType HealthStatus
------------            --------- ------------
Fabrikam NVMe 512GB     SSD       Healthy
$ (Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory / 1GB
15.8
$ Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 5 Name, @{n="MB";e={[math]::Round($_.WorkingSet64/1MB)}}
Name      MB
----      --
msedge  2410
Teams   1180
OUTLOOK  890
:::

- Menos de un 10 % de disco libre hace que todo vaya lento. El **Liberador de espacio** (`cleanmgr`) y Configuración → Sistema → Almacenamiento → Recomendaciones de limpieza suelen recuperar 10-20 GB (archivos de actualizaciones anteriores, papelera, descargas).
- **MediaType HDD** en 2026: ese equipo va lento porque es viejo, no porque esté roto. Propón sustitución.
- 8 GB de RAM con Teams, Edge con 30 pestañas y Outlook: va a ir lento. Si no se puede ampliar, el consejo honesto es cerrar lo que no usa.

## 3. Integridad del sistema

Si hay errores raros, aplicaciones que se cierran o Windows Update que falla, repara los archivos del sistema. Tarda 10-20 minutos y no borra nada.

:::term PowerShell · como administrador
$ DISM /Online /Cleanup-Image /RestoreHealth
Herramienta Administración y mantenimiento de imágenes de implementación
[==========================100.0%==========================]
La operación de restauración se completó correctamente.
$ sfc /scannow
Comenzando el examen del sistema. Este proceso tardará algún tiempo.
Protección de recursos de Windows no encontró ninguna infracción de integridad.
:::

Primero DISM (repara la imagen de la que SFC saca los archivos) y luego SFC. Si SFC dice que encontró archivos dañados y los reparó, reinicia y comprueba si el síntoma sigue.

## 4. Los eventos del sistema

El **Visor de eventos** dice lo que pasó. En lugar de mirarlo entero, pide solo lo crítico y los errores de las últimas 24 horas:

:::term PowerShell · como administrador
$ Get-WinEvent -FilterHashtable @{LogName="System","Application"; Level=1,2; StartTime=(Get-Date).AddDays(-1)} | Select-Object -First 8 TimeCreated, ProviderName, Id, @{n="Msg";e={$_.Message.Substring(0, [math]::Min(90, $_.Message.Length))}}
TimeCreated         ProviderName                Id Msg
-----------         ------------                -- ---
21/10/2026 8:41:02  Microsoft-Windows-WHEA-Logger 17 Se ha producido un error de hardware corregido. Origen: PCI Express…
21/10/2026 8:40:55  disk                        153 Se reintentó la operación de E/S en el dispositivo \\Device\\Harddisk0…
20/10/2026 17:02:10 Application Error         1000 Nombre de la aplicación con errores: OUTLOOK.EXE, versión 16.0.18…
:::

Lo que buscas: eventos **disk** (7, 51, 153) o **WHEA-Logger** repetidos son hardware y van al fabricante; **Application Error 1000** de la misma aplicación cada día es esa aplicación (y la guía de esa aplicación); **Kernel-Power 41** son apagados bruscos: batería, sobrecalentamiento o el usuario manteniendo pulsado el botón.

## 5. Entra ID e Intune

Un equipo que no sincroniza con Intune no recibe políticas, aplicaciones ni Conditional Access funciona bien. `dsregcmd` lo dice todo:

:::term PowerShell · usuario
$ dsregcmd /status
+----------------------------------------------------------------------+
| Device State                                                         |
+----------------------------------------------------------------------+
             AzureAdJoined : YES
          DomainJoined : NO
             DeviceId : 4c1e7a2b-9d3f-4b2a-8e1c-2f6a9b0d7e55
+----------------------------------------------------------------------+
| SSO State                                                            |
+----------------------------------------------------------------------+
                AzureAdPrt : YES
      AzureAdPrtUpdateTime : 2026-10-21 07:58:12.000 UTC
+----------------------------------------------------------------------+
| Device Details                                                       |
+----------------------------------------------------------------------+
   MDM URL : https://enrollment.manage.microsoft.com/enrollmentserver/discovery.svc
:::

- **AzureAdJoined : YES** y **AzureAdPrt : YES** es lo que quieres. Si el PRT es **NO**, el usuario no tiene inicio de sesión único y verá peticiones de contraseña y MFA constantes: que bloquee y desbloquee el equipo con la contraseña (no con el PIN) y, si sigue, cerrar sesión y volver a entrar.
- Sin **MDM URL**, el equipo no está inscrito en Intune: Configuración → Cuentas → Obtener acceso a trabajo o escuela → la cuenta → Información → **Sincronizar**. Si no hay botón de información, hay que volver a inscribirlo (escalar a Intune con el DeviceId).
- La sincronización manual con Intune también se fuerza desde esa pantalla. Un equipo que lleva más de 7 días sin check-in en Intune aparece como no conforme y Conditional Access lo bloquea.

## 6. Qué poner en el ticket

Nombre y modelo, build de Windows, último reinicio, disco libre, los eventos críticos de 24 horas y el resultado de `dsregcmd`. Con esto, el segundo nivel no tiene que repetir nada, y tú tienes la mitad de los casos resueltos: reinicio, disco lleno, DISM/SFC o sincronizar con Intune.

## Siguientes pasos

- Convierte los puntos 1, 2, 4 y 5 en un script que se ejecute en remoto y pegue el resultado en el ticket: diez minutos pasan a ser uno.
- El informe de **Windows Update for Business** y el de **estado de los dispositivos** en Intune te adelantan los equipos que van a dar problemas.
- En el Nivel 2 verás MECM/SCCM y PowerShell en serio; en el Nivel 3, Intune de principio a fin.
""",
  en="""
## What you'll get

Know in ten minutes whether a device "runs slow" because of the disk, the memory, a half-finished update or something broken in the system, and whether it is properly joined to Entra ID and receiving Intune policies. With the results, you either fix it or escalate it with data.

## Before you start

- A PowerShell console **as administrator** on the device (remotely, through whatever assistance tool your company uses).
- The device name and the user from the ticket.
- Ten minutes during which the user does not need the device: some checks use CPU.

## 1. Which device it is and which version it runs

:::term PowerShell · as administrator
$ Get-ComputerInfo | Select-Object CsName, OsName, OsVersion, OsBuildNumber, CsManufacturer, CsModel, OsLastBootUpTime
CsName           : LAPTOP-7F2K9Q
OsName           : Microsoft Windows 11 Enterprise
OsVersion        : 10.0.26100
OsBuildNumber    : 26100
CsManufacturer   : Fabrikam
CsModel          : Portable 14 G3
OsLastBootUpTime : 03/10/2026 8:12:40
$ Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 3 HotFixID, InstalledOn
HotFixID  InstalledOn
--------  -----------
KB5044284 09/10/2026
KB5043080 11/09/2026
:::

Two things that already tell you a lot: an **OsLastBootUpTime** from 18 days ago means the device has not been restarted (Windows fast shutdown does not count as a restart) and, if an update is pending a reboot, that is why it is slow. And an old **build** (Windows 10 in 2026, or a Windows 11 two versions back) is a device not receiving patches: bring it up to date before anything else.

## 2. Disk and memory

:::term PowerShell · as administrator
$ Get-PSDrive C | Select-Object @{n="UsedGB";e={[math]::Round($_.Used/1GB)}}, @{n="FreeGB";e={[math]::Round($_.Free/1GB)}}
UsedGB FreeGB
------ ------
   455     21
$ Get-PhysicalDisk | Select-Object FriendlyName, MediaType, HealthStatus
FriendlyName            MediaType HealthStatus
------------            --------- ------------
Fabrikam NVMe 512GB     SSD       Healthy
$ (Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory / 1GB
15.8
$ Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 5 Name, @{n="MB";e={[math]::Round($_.WorkingSet64/1MB)}}
Name      MB
----      --
msedge  2410
Teams   1180
OUTLOOK  890
:::

- Under 10% free disk makes everything slow. **Disk Cleanup** (`cleanmgr`) and Settings → System → Storage → Cleanup recommendations usually recover 10-20 GB (previous update files, recycle bin, downloads).
- **MediaType HDD** in 2026: that device is slow because it is old, not because it is broken. Propose a replacement.
- 8 GB of RAM with Teams, Edge with 30 tabs and Outlook: it will be slow. If it cannot be upgraded, the honest advice is to close what they are not using.

## 3. System integrity

If there are odd errors, apps crashing or Windows Update failing, repair the system files. It takes 10-20 minutes and deletes nothing.

:::term PowerShell · as administrator
$ DISM /Online /Cleanup-Image /RestoreHealth
Deployment Image Servicing and Management tool
[==========================100.0%==========================]
The restore operation completed successfully.
$ sfc /scannow
Beginning system scan. This process will take some time.
Windows Resource Protection did not find any integrity violations.
:::

DISM first (it repairs the image SFC takes its files from), then SFC. If SFC says it found corrupt files and repaired them, reboot and check whether the symptom persists.

## 4. The system events

**Event Viewer** says what happened. Instead of reading all of it, ask only for critical and error events from the last 24 hours:

:::term PowerShell · as administrator
$ Get-WinEvent -FilterHashtable @{LogName="System","Application"; Level=1,2; StartTime=(Get-Date).AddDays(-1)} | Select-Object -First 8 TimeCreated, ProviderName, Id, @{n="Msg";e={$_.Message.Substring(0, [math]::Min(90, $_.Message.Length))}}
TimeCreated         ProviderName                Id Msg
-----------         ------------                -- ---
21/10/2026 8:41:02  Microsoft-Windows-WHEA-Logger 17 A corrected hardware error has occurred. Component: PCI Express…
21/10/2026 8:40:55  disk                        153 The IO operation at logical block address … was retried…
20/10/2026 17:02:10 Application Error         1000 Faulting application name: OUTLOOK.EXE, version: 16.0.18…
:::

What you are looking for: repeated **disk** (7, 51, 153) or **WHEA-Logger** events are hardware and go to the manufacturer; **Application Error 1000** from the same app every day is that app (and that app's guide); **Kernel-Power 41** means hard shutdowns: battery, overheating or the user holding the power button.

## 5. Entra ID and Intune

A device not syncing with Intune receives no policies or apps, and Conditional Access misbehaves. `dsregcmd` tells you everything:

:::term PowerShell · user
$ dsregcmd /status
+----------------------------------------------------------------------+
| Device State                                                         |
+----------------------------------------------------------------------+
             AzureAdJoined : YES
          DomainJoined : NO
             DeviceId : 4c1e7a2b-9d3f-4b2a-8e1c-2f6a9b0d7e55
+----------------------------------------------------------------------+
| SSO State                                                            |
+----------------------------------------------------------------------+
                AzureAdPrt : YES
      AzureAdPrtUpdateTime : 2026-10-21 07:58:12.000 UTC
+----------------------------------------------------------------------+
| Device Details                                                       |
+----------------------------------------------------------------------+
   MDM URL : https://enrollment.manage.microsoft.com/enrollmentserver/discovery.svc
:::

- **AzureAdJoined : YES** and **AzureAdPrt : YES** is what you want. If the PRT is **NO**, the user has no single sign-on and will see constant password and MFA prompts: have them lock and unlock the device with the password (not the PIN) and, if it persists, sign out and back in.
- No **MDM URL** means the device is not enrolled in Intune: Settings → Accounts → Access work or school → the account → Info → **Sync**. If there is no Info button, it has to be re-enrolled (escalate to Intune with the DeviceId).
- A manual Intune sync is also forced from that screen. A device with no Intune check-in for more than 7 days shows as non-compliant and Conditional Access blocks it.

## 6. What to put in the ticket

Name and model, Windows build, last reboot, free disk, the critical events from 24 hours and the `dsregcmd` result. With that, second line repeats nothing, and you have half the cases solved: reboot, full disk, DISM/SFC or an Intune sync.

## Next steps

- Turn points 1, 2, 4 and 5 into a script that runs remotely and pastes the result into the ticket: ten minutes become one.
- The **Windows Update for Business** report and the **device health** report in Intune tell you in advance which devices are about to cause trouble.
- In Level 2 you'll see MECM/SCCM and PowerShell properly; in Level 3, Intune from start to finish.
""")

# ================================================================ Level 2
# ---------------------------------------------------------------- 2.1 · Azure AD Connect
g(slug="azure-ad-connect-forzar-sincronizacion-y-objetos-que-no-pasan", topic="azure-ad-connect", date="2026-10-21",
  title_es="Azure AD Connect: forzar una sincronización y arreglar un objeto que no pasa a Entra ID",
  title_en="Azure AD Connect: forcing a sync and fixing an object that won't reach Entra ID",
  dek_es="Dónde mirar cuando un usuario nuevo no aparece en Microsoft 365, cómo forzar el ciclo y cómo leer los errores de exportación.",
  dek_en="Where to look when a new user doesn't appear in Microsoft 365, how to force the cycle, and how to read export errors.",
  es="""
## Qué vas a conseguir

Entender el camino que sigue una cuenta desde Active Directory hasta Entra ID, forzar una sincronización cuando no puedes esperar 30 minutos, y resolver los tres errores que explican casi todos los "no aparece en Microsoft 365".

## Antes de empezar

- Acceso al servidor donde está instalado **Microsoft Entra Connect** (el nombre nuevo de Azure AD Connect). Suele ser un servidor miembro, no un controlador de dominio.
- Pertenecer al grupo local **ADSyncAdmins** de ese servidor, o ser administrador local. No necesitas ser Global Admin para forzar un ciclo.
- Saber qué OUs están incluidas en la sincronización: si el usuario está en una OU fuera del filtro, nunca pasará, haga lo que haga.

## 1. Cómo viaja un objeto

Entra Connect sincroniza cada **30 minutos** en tres pasos: importa de AD al espacio del conector, lo pasa al metaverso aplicando las reglas, y exporta a Entra ID. Un cambio en AD tarda, como mucho, 30 minutos más lo que tarde Entra ID en aprovisionar el buzón y las licencias.

Lo que sí es instantáneo es lo contrario: si quieres que algo se vea hoy, se fuerza; si se ve mal, el origen casi siempre es el objeto en AD, no el conector.

## 2. Forzar el ciclo

:::term PowerShell · servidor de Entra Connect
$ Import-Module ADSync
$ Get-ADSyncScheduler | Select-Object SyncCycleEnabled, NextSyncCycleStartTimeInUTC, SyncCycleInProgress
SyncCycleEnabled            : True
NextSyncCycleStartTimeInUTC : 21/10/2026 15:30:02
SyncCycleInProgress         : False
$ Start-ADSyncSyncCycle -PolicyType Delta
Result
------
Success
:::

`Delta` sincroniza solo los cambios y tarda un par de minutos. `Initial` relee todo y solo se usa tras cambiar el filtrado de OUs o las reglas. Si `SyncCycleInProgress` es `True`, espera a que acabe: lanzar otro no lo acelera.

! Si `SyncCycleEnabled` es `False`, alguien lo desactivó (suele hacerse durante una migración o un cambio de reglas) y se olvidó de volver a activarlo. `Set-ADSyncScheduler -SyncCycleEnabled $true` lo devuelve a la normalidad.

## 3. El usuario sigue sin aparecer

Abre **Synchronization Service Manager** (`miisclient.exe`, en la carpeta de instalación) y mira la pestaña **Operations**: cada ejecución muestra el conector, el perfil y si hubo errores.

:::ui Synchronization Service Manager · Operations
> Operations › contoso.local › Delta Import · Success
> Operations › contoso.onmicrosoft.com - AAD › Export · completed-export-errors
= Errores: 1
= Objeto: CN=Laura Prado,OU=Ventas,OU=Usuarios,DC=contoso,DC=local
= Error: AttributeValueMustBeUnique
= Atributo: ProxyAddresses
= Valor en conflicto: SMTP:laura.prado@contoso.com
:::

Los tres errores que verás una y otra vez:

- **AttributeValueMustBeUnique**: otro objeto en Entra ID ya tiene ese correo o `proxyAddresses`. Suele ser un usuario antiguo (en la papelera de Entra ID o un invitado) o un buzón compartido. Busca el valor en Entra ID y en los eliminados (`Get-MgDirectoryDeletedItemAsUser`) y resuelve el duplicado.
- **InvalidSoftMatch** o **LargeObject**: el UPN o el correo contienen caracteres no permitidos, o un atributo tiene más valores de la cuenta. **IdFix** (herramienta gratuita de Microsoft) recorre todo el AD y lista estos problemas antes de que lleguen al conector.
- **El objeto no está en el espacio del conector**: no es error, es filtro. En **Connectors → contoso.local → Properties → Configure Directory Partitions → Containers** se ve qué OUs se sincronizan. Si la OU no está marcada, el usuario no existe para Entra ID.

Para ver un objeto concreto: pestaña **Metaverse Search**, busca por `displayName` y abre **Connectors**: tiene que aparecer en los dos (AD y Entra ID). Si solo está en AD, mira **Lineage** y la regla que lo dejó fuera (`cloudFiltered`).

## 4. Atributos que importan

- `userPrincipalName` tiene que ser un dominio **verificado** en Entra ID. Un UPN `@contoso.local` se convierte en `@contoso.onmicrosoft.com` y el usuario no podrá iniciar sesión con su correo.
- `mail` y `proxyAddresses` definen las direcciones del buzón. La principal lleva `SMTP:` en mayúsculas.
- `msExchUsageLocation` rellena la ubicación de uso que exige la licencia (guía de Microsoft 365 y licencias).
- `extensionAttribute1-15` viajan si se seleccionaron en el asistente: son útiles para grupos dinámicos.

## 5. Qué poner en el ticket

Hora del último ciclo, el conector que dio error, el nombre del objeto y el texto del error. Con eso, quien administre Entra ID sabe si es un duplicado o un filtro sin abrir la consola.

## Siguientes pasos

- Pasa **IdFix** antes de incorporar una OU nueva: evita los errores de exportación en bloque.
- Activa **Entra Connect Health** para ver los ciclos y los errores desde el portal, sin entrar en el servidor.
- En el Nivel 4 verás las migraciones de tenant, donde Entra Connect es la pieza que hay que desmontar y volver a montar con cuidado.
""",
  en="""
## What you'll get

Understand the path an account takes from Active Directory to Entra ID, force a sync when you can't wait 30 minutes, and resolve the three errors behind almost every "doesn't appear in Microsoft 365".

## Before you start

- Access to the server where **Microsoft Entra Connect** (the new name for Azure AD Connect) is installed. It is usually a member server, not a domain controller.
- Membership of that server's local **ADSyncAdmins** group, or local administrator. You don't need Global Admin to force a cycle.
- Know which OUs are included in the sync: if the user sits in an OU outside the filter, it will never cross, whatever you do.

## 1. How an object travels

Entra Connect syncs every **30 minutes** in three steps: import from AD into the connector space, pass to the metaverse applying the rules, and export to Entra ID. A change in AD takes at most 30 minutes plus whatever Entra ID needs to provision the mailbox and licences.

What is immediate is the opposite: if you need something visible today, you force it; if it looks wrong, the cause is almost always the object in AD, not the connector.

## 2. Force the cycle

:::term PowerShell · Entra Connect server
$ Import-Module ADSync
$ Get-ADSyncScheduler | Select-Object SyncCycleEnabled, NextSyncCycleStartTimeInUTC, SyncCycleInProgress
SyncCycleEnabled            : True
NextSyncCycleStartTimeInUTC : 21/10/2026 15:30:02
SyncCycleInProgress         : False
$ Start-ADSyncSyncCycle -PolicyType Delta
Result
------
Success
:::

`Delta` syncs only the changes and takes a couple of minutes. `Initial` re-reads everything and is only used after changing OU filtering or rules. If `SyncCycleInProgress` is `True`, wait for it to finish: launching another does not speed it up.

! If `SyncCycleEnabled` is `False`, someone turned it off (usually during a migration or a rule change) and forgot to turn it back on. `Set-ADSyncScheduler -SyncCycleEnabled $true` restores normal service.

## 3. The user still doesn't appear

Open **Synchronization Service Manager** (`miisclient.exe`, in the installation folder) and look at the **Operations** tab: every run shows the connector, the profile and whether there were errors.

:::ui Synchronization Service Manager · Operations
> Operations › contoso.local › Delta Import · Success
> Operations › contoso.onmicrosoft.com - AAD › Export · completed-export-errors
= Errors: 1
= Object: CN=Laura Prado,OU=Sales,OU=Users,DC=contoso,DC=local
= Error: AttributeValueMustBeUnique
= Attribute: ProxyAddresses
= Conflicting value: SMTP:laura.prado@contoso.com
:::

The three errors you will see again and again:

- **AttributeValueMustBeUnique**: another object in Entra ID already holds that email or `proxyAddresses`. It is usually an old user (in the Entra ID recycle bin, or a guest) or a shared mailbox. Search the value in Entra ID and among deleted items (`Get-MgDirectoryDeletedItemAsUser`) and resolve the duplicate.
- **InvalidSoftMatch** or **LargeObject**: the UPN or email contains characters that are not allowed, or an attribute has more values than permitted. **IdFix** (Microsoft's free tool) walks the whole AD and lists these problems before they reach the connector.
- **The object is not in the connector space**: not an error, a filter. **Connectors → contoso.local → Properties → Configure Directory Partitions → Containers** shows which OUs are synced. If the OU is unticked, the user does not exist for Entra ID.

To look at one object: **Metaverse Search** tab, search by `displayName` and open **Connectors**: it has to appear in both (AD and Entra ID). If it is only in AD, check **Lineage** and the rule that left it out (`cloudFiltered`).

## 4. Attributes that matter

- `userPrincipalName` has to be a domain **verified** in Entra ID. A `@contoso.local` UPN becomes `@contoso.onmicrosoft.com` and the user can't sign in with their email.
- `mail` and `proxyAddresses` define the mailbox addresses. The primary carries `SMTP:` in upper case.
- `msExchUsageLocation` fills the usage location the licence requires (see the Microsoft 365 and licences guide).
- `extensionAttribute1-15` travel if they were selected in the wizard: useful for dynamic groups.

## 5. What to put in the ticket

Time of the last cycle, the connector that errored, the object name and the error text. With that, whoever administers Entra ID knows whether it is a duplicate or a filter without opening the console.

## Next steps

- Run **IdFix** before onboarding a new OU: it avoids export errors in bulk.
- Enable **Entra Connect Health** to see cycles and errors from the portal, without logging on to the server.
- In Level 4 you'll see tenant migrations, where Entra Connect is the piece that has to be taken apart and rebuilt with care.
""")

# ---------------------------------------------------------------- 2.2 · Bash
g(slug="bash-primer-script-de-comprobacion-de-un-servidor", topic="bash", date="2026-10-21",
  title_es="Bash: tu primer script de comprobación de un servidor Linux",
  title_en="Bash: your first health-check script for a Linux server",
  dek_es="Un script que mira disco, memoria, carga y servicios, avisa si algo pasa de un umbral y se programa en cron. Con las cinco reglas que evitan sustos.",
  dek_en="A script that checks disk, memory, load and services, warns when something crosses a threshold, and runs from cron. With the five rules that avoid nasty surprises.",
  es="""
## Qué vas a conseguir

Un script de Bash que puedes dejar en cualquier servidor Linux y que, cada mañana, te dice si el disco se llena, si un servicio se ha caído o si la carga está disparada. Y, de paso, las reglas de escritura que separan un script que ayuda de uno que un día borra algo.

## Antes de empezar

- Un servidor Linux (Ubuntu, RHEL, Debian) con acceso por SSH y `sudo`.
- Un editor: `nano` vale para empezar; `vim` cuando quieras.
- Para probar, un directorio propio: `mkdir -p ~/scripts`.

## 1. Las cinco reglas

1. **Empieza siempre igual**: `#!/usr/bin/env bash` y `set -euo pipefail`. Para en el primer error (`-e`), falla si usas una variable no definida (`-u`) y no esconde errores en una tubería (`-o pipefail`).
2. **Comillas en las variables**: `"$ruta"`, nunca `$ruta`. Un espacio en un nombre de archivo y un `rm` sin comillas es cómo se pierden carpetas.
3. **Nunca `rm -rf` sobre una variable** sin comprobar antes que no está vacía y que apunta a donde crees: `[[ -n "$dir" && "$dir" != "/" ]]`.
4. **Primero en modo lectura**. Un script que solo lee y avisa no puede romper nada. Lo que escribe (borrar logs, reiniciar servicios) se añade después, con `--apply` explícito.
5. **Pásalo por `shellcheck`** antes de ejecutarlo en un servidor. Encuentra los errores clásicos que el ojo no ve.

## 2. El script

:::term nano ~/scripts/check-server.sh
#!/usr/bin/env bash
set -euo pipefail

DISK_MAX=85          # % de uso de disco a partir del que avisa
LOAD_MAX=4           # carga media de 5 min
SERVICES=(sshd cron) # servicios que deben estar activos
STATUS=0

warn() { echo "AVISO: $*"; STATUS=1; }

echo "== $(hostname) · $(date '+%d/%m/%Y %H:%M') =="

# Disco: cada sistema de ficheros real por encima del umbral
while read -r fs use mount; do
  use=${use%\\%}
  (( use >= DISK_MAX )) && warn "disco $mount al $use% ($fs)"
done < <(df -h --output=source,pcent,target -x tmpfs -x devtmpfs | tail -n +2)

# Memoria y carga
read -r _ total used _ < <(free -m | awk '/^Mem:/')
echo "memoria: $used/$total MB"
load=$(cut -d' ' -f2 /proc/loadavg)
awk -v l="$load" -v m="$LOAD_MAX" 'BEGIN{exit !(l>=m)}' && warn "carga a 5 min: $load"

# Servicios
for s in "${SERVICES[@]}"; do
  systemctl is-active --quiet "$s" || warn "servicio $s no está activo"
done

(( STATUS == 0 )) && echo "OK: sin avisos"
exit $STATUS
:::

Notas sobre lo que hace: `df --output` evita tener que contar columnas; `tail -n +2` salta la cabecera; `${use%\\%}` quita el `%`; `read ... < <(...)` lee de un comando sin abrir una subshell (así `STATUS` sí cambia dentro del bucle). La comparación de la carga va con `awk` porque Bash no compara decimales.

## 3. Probar

:::term bash · servidor
$ chmod +x ~/scripts/check-server.sh
$ shellcheck ~/scripts/check-server.sh && echo "shellcheck ok"
shellcheck ok
$ ~/scripts/check-server.sh
== srv-files-01 · 21/10/2026 08:00 ==
AVISO: disco /var al 91% (/dev/sda3)
memoria: 3105/7812 MB
AVISO: servicio cron no está activo
$ echo $?
1
:::

El código de salida (`1` con avisos, `0` sin ellos) es lo que permite que cron, un monitor o otro script sepan si ha ido bien sin leer el texto.

## 4. Programarlo

:::term bash · servidor
$ sudo cp ~/scripts/check-server.sh /usr/local/bin/check-server
$ sudo crontab -e
# cada día a las 7:00, guardando la salida en un log que rota
0 7 * * * /usr/local/bin/check-server >> /var/log/check-server.log 2>&1
$ sudo tail -n 20 /var/log/check-server.log
:::

En cron no hay tu `PATH` ni tus alias: usa rutas completas y prueba el script con `env -i bash -c /usr/local/bin/check-server` para ver cómo se comporta sin tu entorno. Para que avise por correo, `MAILTO=it@contoso.com` al principio del crontab (si el servidor tiene correo configurado), o mejor, que escriba en el log que ya recoge tu monitorización.

## Siguientes pasos

- Añade un `--apply` que haga algo útil y seguro: rotar un log, reiniciar el servicio caído con `systemctl restart`.
- Pon el script en el repositorio del equipo (guía de Git) para que cambie con revisión y no por SSH a mano.
- En el Nivel 3 verás Ansible: cuando el mismo script tiene que correr en 40 servidores, es su trabajo.
""",
  en="""
## What you'll get

A Bash script you can drop on any Linux server which, every morning, tells you whether the disk is filling up, a service has died or the load is through the roof. And, along the way, the writing rules that separate a script that helps from one that deletes something one day.

## Before you start

- A Linux server (Ubuntu, RHEL, Debian) with SSH access and `sudo`.
- An editor: `nano` is fine to start; `vim` whenever you like.
- A folder of your own to test in: `mkdir -p ~/scripts`.

## 1. The five rules

1. **Always start the same way**: `#!/usr/bin/env bash` and `set -euo pipefail`. It stops at the first error (`-e`), fails on an undefined variable (`-u`) and does not hide errors inside a pipe (`-o pipefail`).
2. **Quote your variables**: `"$path"`, never `$path`. A space in a file name plus an unquoted `rm` is how folders get lost.
3. **Never `rm -rf` on a variable** without first checking it is not empty and points where you think: `[[ -n "$dir" && "$dir" != "/" ]]`.
4. **Read-only first**. A script that only reads and warns cannot break anything. Whatever writes (deleting logs, restarting services) is added later, behind an explicit `--apply`.
5. **Run it through `shellcheck`** before executing it on a server. It finds the classic mistakes the eye misses.

## 2. The script

:::term nano ~/scripts/check-server.sh
#!/usr/bin/env bash
set -euo pipefail

DISK_MAX=85          # % disk usage that triggers a warning
LOAD_MAX=4           # 5-minute load average
SERVICES=(sshd cron) # services that must be active
STATUS=0

warn() { echo "WARN: $*"; STATUS=1; }

echo "== $(hostname) · $(date '+%d/%m/%Y %H:%M') =="

# Disk: every real filesystem above the threshold
while read -r fs use mount; do
  use=${use%\\%}
  (( use >= DISK_MAX )) && warn "disk $mount at $use% ($fs)"
done < <(df -h --output=source,pcent,target -x tmpfs -x devtmpfs | tail -n +2)

# Memory and load
read -r _ total used _ < <(free -m | awk '/^Mem:/')
echo "memory: $used/$total MB"
load=$(cut -d' ' -f2 /proc/loadavg)
awk -v l="$load" -v m="$LOAD_MAX" 'BEGIN{exit !(l>=m)}' && warn "5-min load: $load"

# Services
for s in "${SERVICES[@]}"; do
  systemctl is-active --quiet "$s" || warn "service $s is not active"
done

(( STATUS == 0 )) && echo "OK: no warnings"
exit $STATUS
:::

Notes on what it does: `df --output` avoids counting columns; `tail -n +2` skips the header; `${use%\\%}` strips the `%`; `read ... < <(...)` reads from a command without opening a subshell (so `STATUS` really changes inside the loop). The load comparison goes through `awk` because Bash does not compare decimals.

## 3. Test it

:::term bash · server
$ chmod +x ~/scripts/check-server.sh
$ shellcheck ~/scripts/check-server.sh && echo "shellcheck ok"
shellcheck ok
$ ~/scripts/check-server.sh
== srv-files-01 · 21/10/2026 08:00 ==
WARN: disk /var at 91% (/dev/sda3)
memory: 3105/7812 MB
WARN: service cron is not active
$ echo $?
1
:::

The exit code (`1` with warnings, `0` without) is what lets cron, a monitor or another script know whether it went well without reading the text.

## 4. Schedule it

:::term bash · server
$ sudo cp ~/scripts/check-server.sh /usr/local/bin/check-server
$ sudo crontab -e
# every day at 07:00, appending to a log that gets rotated
0 7 * * * /usr/local/bin/check-server >> /var/log/check-server.log 2>&1
$ sudo tail -n 20 /var/log/check-server.log
:::

Cron has neither your `PATH` nor your aliases: use full paths and test the script with `env -i bash -c /usr/local/bin/check-server` to see how it behaves without your environment. To get an email, put `MAILTO=it@contoso.com` at the top of the crontab (if the server has mail configured), or better, have it write to the log your monitoring already collects.

## Next steps

- Add an `--apply` that does something useful and safe: rotate a log, restart the dead service with `systemctl restart`.
- Put the script in the team repository (see the Git guide) so it changes through review, not by hand over SSH.
- In Level 3 you'll see Ansible: when the same script has to run on 40 servers, that is its job.
""")

# ---------------------------------------------------------------- 2.3 · Citrix VDI
g(slug="citrix-vdi-publicar-aplicacion-y-sesion-que-no-abre", topic="citrix-vdi", date="2026-10-21",
  title_es="Citrix VDI: publicar una aplicación y diagnosticar una sesión que no abre",
  title_en="Citrix VDI: publishing an application and diagnosing a session that won't launch",
  dek_es="Los cuatro objetos que hay que entender (catálogo, grupo de entrega, VDA, StoreFront), cómo publicar una app y el orden para resolver 'no me abre'.",
  dek_en="The four objects you need to understand (catalog, delivery group, VDA, StoreFront), how to publish an app, and the order for solving 'it won't open'.",
  es="""
## Qué vas a conseguir

Publicar una aplicación en Citrix Virtual Apps and Desktops para un grupo de usuarios y resolver, con un orden fijo, el ticket más común de VDI: "pulso en la aplicación y no se abre" o "se queda en Connecting...".

## Antes de empezar

- Acceso a **Citrix Studio** (o Web Studio) con un rol de administrador de aplicaciones o de ayuda al usuario, y a **Citrix Director** para ver sesiones.
- Saber dónde está instalada la aplicación: en los servidores del **catálogo de máquinas** (Windows Server con el VDA), no en el equipo del usuario.
- El **Citrix Workspace app** en el equipo del usuario, y la URL del StoreFront o de Workspace.

## 1. Las piezas

- **Catálogo de máquinas**: los servidores o escritorios con el **VDA** (Virtual Delivery Agent) instalado. Se crean desde una imagen maestra.
- **Grupo de entrega**: une máquinas del catálogo con los usuarios que pueden usarlas. Aquí se publican las aplicaciones y los escritorios.
- **Delivery Controller**: el cerebro. Los VDA se **registran** en él; sin registro, la máquina existe pero no sirve sesiones.
- **StoreFront / Workspace**: la tienda que ve el usuario. Pide la lista de apps al Controller y entrega el fichero `.ica` que abre la sesión.

## 2. Publicar la aplicación

:::ui Citrix Studio · Applications
> Applications › Add Applications
> Delivery Groups › [x] DG-Finanzas-Apps
> Applications › From start menu › [x] ERP Client 7.2
= Nombre (usuario): ERP
= Ruta: C:\\Program Files\\ERP\\erp.exe
= Directorio de trabajo: C:\\Program Files\\ERP
= Carpeta en StoreFront: Finanzas
> Limit Visibility › [x] GG-ERP-Usuarios
[Finish]
:::

Con PowerShell desde el Controller se hace lo mismo y queda documentado:

:::term PowerShell · Delivery Controller
$ Add-PSSnapin Citrix*
$ New-BrokerApplication -Name "ERP" -CommandLineExecutable "C:\\Program Files\\ERP\\erp.exe" -WorkingDirectory "C:\\Program Files\\ERP" -DesktopGroup "DG-Finanzas-Apps" -UserFilterEnabled $true
$ Add-BrokerUser -Name "CONTOSO\\GG-ERP-Usuarios" -Application "ERP"
$ Get-BrokerApplication -Name "ERP" | Select-Object Name, Enabled, AssociatedDesktopGroupUids, UserFilterEnabled
Name Enabled AssociatedDesktopGroupUids UserFilterEnabled
---- ------- -------------------------- -----------------
ERP     True {3}                                     True
:::

El usuario la verá en Workspace tras actualizar la lista (icono de refrescar, o cerrar y abrir la app). Si no aparece: no está en el grupo del filtro, o el grupo de entrega no incluye su cuenta.

## 3. "No me abre": el orden

### 3.1 ¿Hay máquinas disponibles?

:::term PowerShell · Delivery Controller
$ Get-BrokerMachine -DesktopGroupName "DG-Finanzas-Apps" | Select-Object MachineName, RegistrationState, InMaintenanceMode, SessionCount, LoadIndex
MachineName          RegistrationState InMaintenanceMode SessionCount LoadIndex
-----------          ----------------- ----------------- ------------ ---------
CONTOSO\\XA-APP-01       Registered                  False           41      8200
CONTOSO\\XA-APP-02     Unregistered                  False            0         0
CONTOSO\\XA-APP-03       Registered                   True            0         0
:::

Aquí ya ves el problema del día: una máquina **Unregistered** (el VDA no habla con el Controller: casi siempre se ha reiniciado mal, el servicio `BrokerAgent` está parado o tiene la hora desajustada), otra en **mantenimiento** (alguien la dejó así tras parchear), y la que queda con carga al tope (`LoadIndex` 10000 es el máximo). Resultado: las sesiones nuevas no entran.

- Unregistered: en la máquina, `Restart-Service BrokerAgent`; si sigue, revisa el visor de eventos (origen *Citrix Desktop Service*) y que resuelve el nombre del Controller.
- Mantenimiento: `Set-BrokerMachine -MachineName "CONTOSO\\XA-APP-03" -InMaintenanceMode $false` una vez comprobado que está parcheada y bien.

### 3.2 ¿Es el usuario o es todo el mundo?

En **Director → Buscar usuario** aparecen sus sesiones: si tiene una sesión **Disconnected** de ayer en otra máquina, la app intenta reconectar a esa y falla. **Log off** de esa sesión desde Director y que vuelva a probar. Si nadie puede abrir la app, es el 3.1 o la propia aplicación en el servidor.

### 3.3 ¿Llega el .ica?

Si al pulsar en la app el navegador descarga un fichero `.ica` y no pasa nada, Workspace app no está asociado al tipo de fichero o no está instalado. Si el fichero se abre y se queda en **Connecting**: el equipo del usuario no llega al VDA por el puerto **1494** (ICA) o **2598** (Session Reliability): `Test-NetConnection XA-APP-01 -Port 2598` desde el equipo. Lo normal es un firewall entre la red del usuario (VPN, oficina nueva) y los servidores VDA.

### 3.4 La aplicación abre y se cierra

Ya no es Citrix: es la aplicación. Entra por RDP en el servidor VDA como el usuario (o con una cuenta de prueba del mismo grupo) y ábrela a mano. Lo que falle ahí (licencia de la app, permisos en una carpeta, un perfil de usuario corrupto en `C:\\Users`) es lo que hay que arreglar. Los perfiles con **Citrix Profile Management** o FSLogix se restablecen borrando el contenedor del usuario, con su permiso y con copia.

## 4. Qué poner en el ticket

Nombre de la app, grupo de entrega, resultado de `Get-BrokerMachine`, en qué paso se queda (lista, .ica, Connecting, dentro) y el nombre de la máquina a la que intentaba conectar (Director lo muestra). Con eso, el equipo de Citrix no tiene que repetir nada.

## Siguientes pasos

- Un script diario con `Get-BrokerMachine` que avise de máquinas Unregistered o en mantenimiento evita la mitad de los tickets de la mañana.
- Aprende a actualizar la imagen maestra y a hacer *rollout* a un catálogo con MCS: es el siguiente paso natural.
- En el Nivel 2 también está VMware Horizon, la alternativa con los mismos conceptos y otros nombres.
""",
  en="""
## What you'll get

Publish an application in Citrix Virtual Apps and Desktops for a group of users and solve, in a fixed order, the most common VDI ticket: "I click the app and nothing opens" or "it sits on Connecting...".

## Before you start

- Access to **Citrix Studio** (or Web Studio) with an application administrator or help desk role, and to **Citrix Director** to see sessions.
- Know where the application is installed: on the servers in the **machine catalog** (Windows Server with the VDA), not on the user's device.
- The **Citrix Workspace app** on the user's device, and the StoreFront or Workspace URL.

## 1. The pieces

- **Machine catalog**: the servers or desktops with the **VDA** (Virtual Delivery Agent) installed. Created from a master image.
- **Delivery group**: joins machines from the catalog with the users who may use them. Applications and desktops are published here.
- **Delivery Controller**: the brain. VDAs **register** with it; without registration, the machine exists but serves no sessions.
- **StoreFront / Workspace**: the store the user sees. It asks the Controller for the app list and hands over the `.ica` file that opens the session.

## 2. Publish the application

:::ui Citrix Studio · Applications
> Applications › Add Applications
> Delivery Groups › [x] DG-Finance-Apps
> Applications › From start menu › [x] ERP Client 7.2
= Name (for user): ERP
= Path: C:\\Program Files\\ERP\\erp.exe
= Working directory: C:\\Program Files\\ERP
= StoreFront folder: Finance
> Limit Visibility › [x] GG-ERP-Users
[Finish]
:::

PowerShell from the Controller does the same, and it stays documented:

:::term PowerShell · Delivery Controller
$ Add-PSSnapin Citrix*
$ New-BrokerApplication -Name "ERP" -CommandLineExecutable "C:\\Program Files\\ERP\\erp.exe" -WorkingDirectory "C:\\Program Files\\ERP" -DesktopGroup "DG-Finance-Apps" -UserFilterEnabled $true
$ Add-BrokerUser -Name "CONTOSO\\GG-ERP-Users" -Application "ERP"
$ Get-BrokerApplication -Name "ERP" | Select-Object Name, Enabled, AssociatedDesktopGroupUids, UserFilterEnabled
Name Enabled AssociatedDesktopGroupUids UserFilterEnabled
---- ------- -------------------------- -----------------
ERP     True {3}                                     True
:::

The user sees it in Workspace after refreshing the list (refresh icon, or close and reopen the app). If it does not appear: they are not in the filter group, or the delivery group does not include their account.

## 3. "It won't open": the order

### 3.1 Are there machines available?

:::term PowerShell · Delivery Controller
$ Get-BrokerMachine -DesktopGroupName "DG-Finance-Apps" | Select-Object MachineName, RegistrationState, InMaintenanceMode, SessionCount, LoadIndex
MachineName          RegistrationState InMaintenanceMode SessionCount LoadIndex
-----------          ----------------- ----------------- ------------ ---------
CONTOSO\\XA-APP-01       Registered                  False           41      8200
CONTOSO\\XA-APP-02     Unregistered                  False            0         0
CONTOSO\\XA-APP-03       Registered                   True            0         0
:::

The day's problem is right there: one machine **Unregistered** (the VDA is not talking to the Controller: almost always a bad reboot, the `BrokerAgent` service stopped, or the clock off), another in **maintenance** (someone left it there after patching), and the remaining one at full load (`LoadIndex` 10000 is the maximum). Result: new sessions don't get in.

- Unregistered: on the machine, `Restart-Service BrokerAgent`; if it persists, check Event Viewer (source *Citrix Desktop Service*) and that it resolves the Controller's name.
- Maintenance: `Set-BrokerMachine -MachineName "CONTOSO\\XA-APP-03" -InMaintenanceMode $false` once you have confirmed it is patched and healthy.

### 3.2 Is it the user or everyone?

In **Director → Search user** their sessions appear: if they have a **Disconnected** session from yesterday on another machine, the app tries to reconnect to that one and fails. **Log off** that session from Director and have them try again. If nobody can open the app, it is 3.1 or the application itself on the server.

### 3.3 Does the .ica arrive?

If clicking the app makes the browser download an `.ica` file and nothing happens, Workspace app is not associated with the file type or not installed. If the file opens and sits on **Connecting**: the user's device cannot reach the VDA on port **1494** (ICA) or **2598** (Session Reliability): `Test-NetConnection XA-APP-01 -Port 2598` from the device. It is usually a firewall between the user's network (VPN, new office) and the VDA servers.

### 3.4 The application opens and closes

That is no longer Citrix: it is the application. RDP into the VDA server as the user (or with a test account from the same group) and open it by hand. Whatever fails there (the app's licence, permissions on a folder, a corrupt user profile in `C:\\Users`) is what needs fixing. Profiles with **Citrix Profile Management** or FSLogix are reset by deleting the user's container, with their permission and a backup.

## 4. What to put in the ticket

App name, delivery group, the `Get-BrokerMachine` output, which step it gets stuck at (list, .ica, Connecting, inside) and the name of the machine it tried to connect to (Director shows it). With that, the Citrix team repeats nothing.

## Next steps

- A daily script with `Get-BrokerMachine` that flags Unregistered or maintenance machines removes half the morning tickets.
- Learn to update the master image and roll it out to a catalog with MCS: that is the natural next step.
- Level 2 also has VMware Horizon, the alternative with the same concepts and different names.
""")

# ---------------------------------------------------------------- 2.4 · Confluence
g(slug="confluence-espacio-de-it-y-runbooks-que-se-usan", topic="confluence", date="2026-10-21",
  title_es="Confluence: montar el espacio de IT y escribir runbooks que el equipo use",
  title_en="Confluence: setting up the IT space and writing runbooks the team actually uses",
  dek_es="Estructura del espacio, permisos, una plantilla de runbook con los campos que importan, y cómo enlazarlo con los tickets de Jira.",
  dek_en="Space structure, permissions, a runbook template with the fields that matter, and how to link it to Jira tickets.",
  es="""
## Qué vas a conseguir

Un espacio de Confluence donde el equipo de IT encuentra en 30 segundos cómo se hace cada cosa, con runbooks que se mantienen porque están ligados a los tickets. Lo contrario de una wiki con 400 páginas que nadie abre.

## Antes de empezar

- Permiso para **crear espacios** en Confluence (lo da el administrador del sitio) o un espacio de IT ya creado donde seas administrador.
- Decidir con el equipo quién puede **leer** (toda la empresa o solo IT) y quién puede **editar** (IT). Los runbooks con contraseñas o IPs internas no se escriben; se enlaza al gestor de secretos.
- Jira Service Management en el mismo sitio de Atlassian, para enlazar artículos y tickets.

## 1. Estructura: poca y estable

Un espacio por equipo (`IT`), no uno por proyecto. Dentro, cuatro ramas de primer nivel que no cambian:

:::ui Confluence · Espacio IT › Árbol de páginas
> IT › Runbooks (cómo se hace cada tarea, uno por tarea)
> IT › Servicios (qué es cada sistema, quién lo lleva, proveedor, contrato)
> IT › Procedimientos (altas, bajas, cambios, incidentes graves)
> IT › Decisiones (una página por decisión técnica, con fecha y motivo)
= Página de inicio: buscador + los 10 runbooks más usados + "quién lleva qué"
:::

Un runbook es **una tarea**: "Dar de alta un usuario", "Renovar el certificado del portal", "Reiniciar el servicio de impresión". Si una página explica tres cosas, son tres runbooks.

## 2. La plantilla de runbook

Crea una **plantilla de espacio** (Configuración del espacio → Plantillas) con estos bloques y usa la macro de **estado** para que se vea de un vistazo si está vigente:

:::ui Confluence · Plantilla "Runbook"
= Estado: VIGENTE · Propietario: @persona · Revisado: 21/10/2026 · Servicio: enlace a Servicios
= Cuándo se usa: una frase. Si no sabes si aplica, aquí lo sabes.
= Requisitos: accesos, herramientas, a quién avisar antes
= Pasos: numerados, un comando o una acción por paso, con el resultado esperado
= Comprobación: cómo sabes que ha funcionado
= Si falla: los dos o tres errores conocidos y qué hacer
= Tickets relacionados: macro de Jira con el filtro "labels = runbook-alta-usuario"
:::

Dos reglas que hacen que se mantenga: cada runbook tiene **un propietario** (no "el equipo") y una fecha de **revisión** que se actualiza al usarlo. Una página sin revisar en 6 meses se marca como DUDOSA, no se borra.

## 3. Enlazar con Jira

Cuando resuelves un ticket siguiendo un runbook, enlaza la página desde el ticket (**Enlazar → Página de Confluence**). Y en la página, la macro de Jira muestra los tickets que la han usado: así ves cuáles valen y cuáles no se usan nunca.

Si el service desk tiene **base de conocimiento** activada, el espacio de IT (o uno aparte para usuarios) se vincula desde Jira Service Management → Proyecto → Base de conocimiento. Jira sugiere los artículos al usuario mientras escribe el ticket, y ahí es donde un buen título ("Outlook pide la contraseña una y otra vez") desvía tickets antes de que existan.

## 4. Permisos

:::ui Confluence · Configuración del espacio › Permisos
= Grupo confluence-users (toda la empresa): Ver páginas
= Grupo it-team: Ver, Añadir, Eliminar páginas · Añadir comentarios
= Grupo it-admins: Administrar espacio
= Anónimo: sin acceso
:::

Las páginas con información sensible (diagramas de red con IPs, procedimientos de emergencia) van en una rama con **restricciones de página** a `it-team`. Las contraseñas no van en ningún sitio de Confluence: se enlaza al gestor de contraseñas del equipo.

## 5. Buscar que funcione

- **Etiquetas** por sistema (`intune`, `exchange`, `vpn`) y por tipo (`runbook`, `decision`). Una página de "Runbooks por sistema" con la macro de **Content by Label** se mantiene sola.
- Títulos con el verbo y el objeto: "Renovar el certificado de vpn.contoso.com", no "Certificados".
- Al final de cada página, **Páginas relacionadas** (macro) con dos o tres enlaces.

## Siguientes pasos

- Migra los procedimientos que hoy viven en Word o en el correo, uno por semana, empezando por los que más tickets generan.
- Una vez al trimestre, revisa la lista de páginas sin visitas en 90 días: se archivan o se fusionan.
- En el Nivel 4 verás la administración de Jira y Confluence a nivel de sitio: esquemas, automatizaciones y la relación con Atlassian.
""",
  en="""
## What you'll get

A Confluence space where the IT team finds how to do anything in 30 seconds, with runbooks that stay maintained because they are tied to tickets. The opposite of a wiki with 400 pages nobody opens.

## Before you start

- Permission to **create spaces** in Confluence (the site administrator grants it) or an existing IT space where you are an administrator.
- Decide with the team who can **read** (the whole company or only IT) and who can **edit** (IT). Runbooks with passwords or internal IPs are not written down; you link to the secrets manager.
- Jira Service Management on the same Atlassian site, to link articles and tickets.

## 1. Structure: small and stable

One space per team (`IT`), not one per project. Inside, four top-level branches that never change:

:::ui Confluence · IT space › Page tree
> IT › Runbooks (how each task is done, one per task)
> IT › Services (what each system is, who owns it, vendor, contract)
> IT › Procedures (joiners, leavers, changes, major incidents)
> IT › Decisions (one page per technical decision, with date and reason)
= Home page: search box + the 10 most used runbooks + "who owns what"
:::

A runbook is **one task**: "Create a user", "Renew the portal certificate", "Restart the print service". If a page explains three things, that is three runbooks.

## 2. The runbook template

Create a **space template** (Space settings → Templates) with these blocks, and use the **status** macro so you can see at a glance whether it is current:

:::ui Confluence · "Runbook" template
= Status: CURRENT · Owner: @person · Reviewed: 21/10/2026 · Service: link to Services
= When to use: one sentence. If you don't know whether it applies, this tells you.
= Requirements: access, tools, who to warn beforehand
= Steps: numbered, one command or action per step, with the expected result
= Check: how you know it worked
= If it fails: the two or three known errors and what to do
= Related tickets: Jira macro with the filter "labels = runbook-new-user"
:::

Two rules that keep it maintained: every runbook has **one owner** (not "the team") and a **review** date that gets updated when it is used. A page not reviewed in 6 months is marked DOUBTFUL, not deleted.

## 3. Link with Jira

When you resolve a ticket by following a runbook, link the page from the ticket (**Link → Confluence page**). And on the page, the Jira macro shows the tickets that used it: that way you see which ones earn their keep and which are never used.

If the service desk has a **knowledge base** enabled, the IT space (or a separate one for users) is linked from Jira Service Management → Project → Knowledge base. Jira suggests articles to the user while they type the ticket, and that is where a good title ("Outlook keeps asking for the password") deflects tickets before they exist.

## 4. Permissions

:::ui Confluence · Space settings › Permissions
= Group confluence-users (whole company): View pages
= Group it-team: View, Add, Delete pages · Add comments
= Group it-admins: Administer space
= Anonymous: no access
:::

Pages with sensitive information (network diagrams with IPs, emergency procedures) go in a branch with **page restrictions** to `it-team`. Passwords go nowhere in Confluence: link to the team's password manager.

## 5. Search that works

- **Labels** per system (`intune`, `exchange`, `vpn`) and per type (`runbook`, `decision`). A "Runbooks by system" page with the **Content by Label** macro maintains itself.
- Titles with the verb and the object: "Renew the certificate for vpn.contoso.com", not "Certificates".
- At the bottom of every page, **Related pages** (macro) with two or three links.

## Next steps

- Migrate the procedures that live in Word or email today, one per week, starting with those that generate the most tickets.
- Once a quarter, review the list of pages with no visits in 90 days: archive or merge them.
- In Level 4 you'll see site-level Jira and Confluence administration: schemes, automations and the relationship with Atlassian.
""")

# ---------------------------------------------------------------- 2.5 · Git
g(slug="git-scripts-del-equipo-bajo-control-de-versiones", topic="git", date="2026-10-21",
  title_es="Git: poner los scripts del equipo bajo control de versiones",
  title_en="Git: putting the team's scripts under version control",
  dek_es="Repositorio, ramas, commits que se entienden, pull request con revisión, y lo que nunca debe entrar en un repo.",
  dek_en="Repository, branches, commits that make sense, pull requests with review, and what must never go into a repo.",
  es="""
## Qué vas a conseguir

Que los scripts de PowerShell y Bash del equipo dejen de vivir en `C:\\Scripts\\final_v3_bueno.ps1` y pasen a un repositorio con historial, revisión y un sitio único del que todo el mundo tira. Con el flujo mínimo que un equipo de IT usa de verdad.

## Antes de empezar

- Git instalado (`git --version`). En Windows, **Git for Windows**; en Linux viene o se instala con `apt`/`dnf`.
- Una cuenta en el servidor de Git de tu empresa (GitHub, GitLab, Azure DevOps, Bitbucket) y un repositorio vacío creado por quien administre: `it-scripts`.
- Tu nombre y correo configurados una vez: `git config --global user.name "Laura Prado"` y `git config --global user.email laura.prado@contoso.com`.

## 1. Lo que nunca entra en un repo

Antes de la primera subida, porque después es muy difícil sacarlo del historial:

- **Contraseñas, claves de API, tokens, certificados con clave privada.** Van en el gestor de secretos y el script los lee de una variable de entorno o de un vault.
- Ficheros con datos de personas (exports de AD con correos, listados de usuarios).
- Lo que se genera: logs, `output/`, CSV de resultados.

Un `.gitignore` en la raíz lo evita:

:::term .gitignore
# resultados y temporales
output/
*.log
*.csv
# secretos: nunca
*.pfx
*.key
.env
secrets.*
:::

## 2. Primer repositorio

:::term bash · tu equipo
$ git clone https://git.contoso.com/it/it-scripts.git
$ cd it-scripts
$ mkdir -p powershell bash
$ cp ~/scripts/check-server.sh bash/
$ git status --short
?? .gitignore
?? bash/check-server.sh
$ git add .gitignore bash/check-server.sh
$ git commit -m "bash: comprobación diaria de disco, carga y servicios"
[main 3f2a9c1] bash: comprobación diaria de disco, carga y servicios
 2 files changed, 58 insertions(+)
$ git push -u origin main
:::

`git status` antes de cada `add` te enseña qué vas a subir. `git add .` a ciegas es como se cuela un `.pfx`.

## 3. Cambios con rama y revisión

El flujo que evita que un cambio a medias llegue a producción: cada cambio en una **rama**, se sube, alguien lo revisa en un **pull request** (merge request en GitLab) y se fusiona a `main`.

:::term bash · tu equipo
$ git switch -c fix/umbral-disco-90
$ nano bash/check-server.sh
$ git diff
-DISK_MAX=85
+DISK_MAX=90
$ git commit -am "check-server: umbral de disco al 90% (acordado en la reunión del 20/10)"
$ git push -u origin fix/umbral-disco-90
remote: Create a pull request for 'fix/umbral-disco-90':
remote:   https://git.contoso.com/it/it-scripts/pull/new/fix/umbral-disco-90
:::

En el pull request, el compañero ve el `diff`, comenta y aprueba. Después, `main` se actualiza y todos hacen `git pull`. Nombres de rama que ayudan: `fix/…`, `feat/…`, `docs/…`.

## 4. Commits que se entienden

Un commit es un cambio con un motivo. El mensaje: qué cambia y por qué, en una línea de menos de 70 caracteres, en imperativo o en presente. Si hace falta más, una línea en blanco y el detalle.

- Bien: `vpn-check: reintentar 3 veces antes de avisar (falsos positivos en la VPN de Milán)`.
- Mal: `cambios`, `arreglo`, `v2`.

Si lo que vas a escribir es "varios cambios", son varios commits.

## 5. Lo que harás cada semana

:::term bash · chuleta
# ponerte al día antes de empezar
$ git switch main && git pull
# ver qué ha cambiado y quién
$ git log --oneline -10
$ git log -p bash/check-server.sh
# deshacer un cambio local que no has confirmado
$ git restore bash/check-server.sh
# volver a una versión anterior de un fichero sin perder el historial
$ git checkout 3f2a9c1 -- bash/check-server.sh
:::

! `git push --force` y `git reset --hard` reescriben o borran. Si no sabes exactamente qué hacen, no los uses sobre `main`; pide ayuda y se arregla en dos minutos. Casi todo en Git se recupera; lo que se pierde es por forzar.

## Siguientes pasos

- Protege `main` en el servidor: sin push directo, pull request obligatorio con una aprobación.
- Añade una comprobación automática al pull request: `shellcheck` para Bash, `PSScriptAnalyzer` para PowerShell.
- En el Nivel 3 verás Jenkins y CI/CD: el repositorio es lo que dispara las pruebas y los despliegues.
""",
  en="""
## What you'll get

The team's PowerShell and Bash scripts stop living in `C:\\Scripts\\final_v3_good.ps1` and move into a repository with history, review and one place everyone pulls from. With the minimal flow an IT team really uses.

## Before you start

- Git installed (`git --version`). On Windows, **Git for Windows**; on Linux it ships or installs with `apt`/`dnf`.
- An account on your company's Git server (GitHub, GitLab, Azure DevOps, Bitbucket) and an empty repository created by whoever administers it: `it-scripts`.
- Your name and email set once: `git config --global user.name "Laura Prado"` and `git config --global user.email laura.prado@contoso.com`.

## 1. What never goes into a repo

Before the first push, because afterwards it is very hard to get out of the history:

- **Passwords, API keys, tokens, certificates with private keys.** They live in the secrets manager and the script reads them from an environment variable or a vault.
- Files with personal data (AD exports with emails, user lists).
- Anything generated: logs, `output/`, result CSVs.

A `.gitignore` at the root prevents it:

:::term .gitignore
# results and temporary files
output/
*.log
*.csv
# secrets: never
*.pfx
*.key
.env
secrets.*
:::

## 2. First repository

:::term bash · your device
$ git clone https://git.contoso.com/it/it-scripts.git
$ cd it-scripts
$ mkdir -p powershell bash
$ cp ~/scripts/check-server.sh bash/
$ git status --short
?? .gitignore
?? bash/check-server.sh
$ git add .gitignore bash/check-server.sh
$ git commit -m "bash: daily check of disk, load and services"
[main 3f2a9c1] bash: daily check of disk, load and services
 2 files changed, 58 insertions(+)
$ git push -u origin main
:::

`git status` before every `add` shows what you are about to push. A blind `git add .` is how a `.pfx` slips in.

## 3. Changes with a branch and a review

The flow that stops a half-finished change reaching production: every change on a **branch**, pushed, reviewed by someone in a **pull request** (merge request in GitLab) and merged into `main`.

:::term bash · your device
$ git switch -c fix/disk-threshold-90
$ nano bash/check-server.sh
$ git diff
-DISK_MAX=85
+DISK_MAX=90
$ git commit -am "check-server: disk threshold to 90% (agreed in the 20/10 meeting)"
$ git push -u origin fix/disk-threshold-90
remote: Create a pull request for 'fix/disk-threshold-90':
remote:   https://git.contoso.com/it/it-scripts/pull/new/fix/disk-threshold-90
:::

In the pull request, a colleague sees the `diff`, comments and approves. Then `main` is updated and everyone runs `git pull`. Branch names that help: `fix/…`, `feat/…`, `docs/…`.

## 4. Commits that make sense

A commit is one change with one reason. The message: what changes and why, in one line under 70 characters, in the imperative or present tense. If more is needed, a blank line and the detail.

- Good: `vpn-check: retry 3 times before warning (false positives on the Milan VPN)`.
- Bad: `changes`, `fix`, `v2`.

If what you are about to write is "various changes", that is several commits.

## 5. What you'll do every week

:::term bash · cheat sheet
# catch up before starting
$ git switch main && git pull
# see what changed and who did it
$ git log --oneline -10
$ git log -p bash/check-server.sh
# undo a local change you haven't committed
$ git restore bash/check-server.sh
# bring back an earlier version of a file without losing history
$ git checkout 3f2a9c1 -- bash/check-server.sh
:::

! `git push --force` and `git reset --hard` rewrite or delete. If you don't know exactly what they do, don't use them on `main`; ask for help and it is fixed in two minutes. Almost everything in Git is recoverable; what gets lost is lost by forcing.

## Next steps

- Protect `main` on the server: no direct push, pull request required with one approval.
- Add an automatic check to the pull request: `shellcheck` for Bash, `PSScriptAnalyzer` for PowerShell.
- In Level 3 you'll see Jenkins and CI/CD: the repository is what triggers tests and deployments.
""")

# ---------------------------------------------------------------- 2.6 · Jamf Pro
g(slug="jamf-pro-enrolar-un-mac-y-desplegar-una-politica", topic="jamf-pro", date="2026-10-21",
  title_es="Jamf Pro: enrolar un Mac y desplegar una política con un grupo inteligente",
  title_en="Jamf Pro: enrolling a Mac and deploying a policy with a smart group",
  dek_es="Enrolamiento automatizado o por el usuario, el inventario que lo alimenta todo, un grupo inteligente y una política que instala y configura. Más los comandos del día a día.",
  dek_en="Automated or user-initiated enrolment, the inventory that feeds everything, a smart group and a policy that installs and configures. Plus the everyday commands.",
  es="""
## Qué vas a conseguir

Un Mac gestionado en Jamf Pro desde el primer encendido, y una política que instala una aplicación solo en los equipos que la necesitan, elegidos por un **grupo inteligente** en lugar de a mano. Es la base de todo lo que harás después en Jamf.

## Antes de empezar

- Acceso a la consola de Jamf Pro con un rol que pueda crear políticas y grupos.
- Para el enrolamiento automatizado: el Mac comprado a través de **Apple Business Manager** y asignado al servidor MDM de Jamf; un **PreStage Enrollment** configurado.
- Para el enrolamiento por el usuario: la URL de enrolamiento (`https://contoso.jamfcloud.com/enroll`) y una cuenta de usuario en Jamf o en el directorio integrado.
- El certificado **APNs** vigente (Configuración → Push certificates). Caduca cada año; sin él, nada.

## 1. Enrolar

**Automatizado (ABM)**: el Mac arranca, el Asistente de configuración muestra "contoso configurará este Mac", el usuario inicia sesión y el PreStage crea la cuenta local, instala el agente y aplica los perfiles. No hay nada que descargar.

**Por el usuario**: en `https://contoso.jamfcloud.com/enroll`, inicia sesión, descarga el perfil de gestión y lo aprueba en **Ajustes del Sistema → Privacidad y seguridad → Perfiles**. Desde macOS 11 el usuario tiene que pulsar **Aprobar** a mano: si no lo hace, el Mac aparece en Jamf pero sin MDM supervisado y los perfiles no se aplican.

:::ui Jamf Pro · Equipos › Inventario
> Equipos › Buscar inventario › MBP-LAURA
= Gestionado: Sí · Supervisado: Sí · MDM aprobado por el usuario: Sí
= macOS: 15.1 · Modelo: MacBook Pro 14" (M3)
= Última entrada: 21/10/2026 10:52 · Último inventario: 21/10/2026 10:52
= Usuario: laura.prado · Departamento: Ventas
[Gestión] [Historial] [Enviar comando MDM]
:::

**Supervisado: Sí** y **MDM aprobado por el usuario: Sí** son las dos casillas que tienen que estar. Sin ellas, FileVault, las restricciones y los comandos remotos fallan en silencio.

## 2. El inventario manda

Todo en Jamf (grupos, políticas, informes) se decide a partir del **inventario** que el Mac envía al hacer `recon`. Por defecto se actualiza una vez al día; si acabas de cambiar algo en el Mac y Jamf no lo refleja, fuerza uno:

:::term Terminal · en el Mac
$ sudo jamf recon
Retrieving inventory preferences from https://contoso.jamfcloud.com/...
Locating hardware information (macOS 15.1)...
Locating applications...
Submitting data to https://contoso.jamfcloud.com/...
<computer_id>417</computer_id>
:::

## 3. Un grupo inteligente

Un grupo inteligente es una consulta sobre el inventario que se recalcula sola. Ejemplo: los Mac de Ventas que todavía no tienen la app del CRM.

:::ui Jamf Pro · Equipos › Grupos inteligentes › Nuevo
= Nombre: Ventas sin CRM
> Criterios
= Departamento: es · Ventas
= y · Título de la aplicación: no tiene · CRM Desktop.app
= y · Último inventario: menos de x días · 7
[Guardar]
= Miembros: 23 equipos
:::

El tercer criterio (inventario reciente) evita que la política persiga equipos apagados desde hace meses.

## 4. La política

:::ui Jamf Pro · Equipos › Políticas › Nueva
= Nombre: Instalar CRM Desktop
= Activador: Check-in recurrente · Frecuencia: Una vez por equipo
> Paquetes › CRM-Desktop-4.2.pkg › Instalar
> Mantenimiento › [x] Actualizar inventario
> Alcance › Equipos de destino: Ventas sin CRM
> Autoservicio › [ ] (no: instalación obligatoria)
[Guardar]
:::

Qué pasa después: cada Mac del grupo, en su siguiente check-in (cada 15 minutos por defecto), ejecuta la política, instala el paquete y actualiza el inventario. En el siguiente recálculo deja de cumplir el criterio y **sale del grupo solo**. Cuando el grupo llega a 0 miembros, has terminado, sin tocar nada.

Para probar en un Mac sin esperar al check-in:

:::term Terminal · en el Mac
$ sudo jamf policy -verbose
Checking for policies triggered by "recurring check-in" for user "laura.prado"...
Executing Policy Instalar CRM Desktop
Downloading CRM-Desktop-4.2.pkg...
Installing CRM-Desktop-4.2.pkg...
Successfully installed CRM-Desktop-4.2.pkg.
Running Recon...
$ sudo jamf policy -event instalar-crm   # si la política tiene un activador personalizado
:::

## 5. Cuando una política no se ejecuta

- **Registros de la política** (Políticas → la política → Registros): si el Mac aparece con "Pendiente", no ha hecho check-in; si aparece "Fallida", el log dice por qué (paquete que no existe en el punto de distribución, disco lleno, `pkg` que exige reinicio).
- En el Mac: `sudo jamf checkJSSConnection` comprueba que llega al servidor; `tail -f /var/log/jamf.log` muestra la ejecución en vivo.
- Una política con frecuencia "Una vez por equipo" que falló no se reintenta sola: **Limpiar registros** para esos equipos y vuelve a ejecutarse.
- El Mac no aparece en el grupo: criterio mal escrito (el nombre de la app es el del bundle, `CRM Desktop.app`, con `.app`) o inventario sin actualizar.

## Siguientes pasos

- Empaqueta las aplicaciones con **Jamf Composer** o usa el **Jamf App Catalog** para que se actualicen solas.
- Mira **Autoservicio** para lo que el usuario puede instalar cuando quiera: baja tickets y les da autonomía.
- En el Nivel 3 verás la gestión de Mac desde Intune y cuándo tiene sentido Jamf, Intune o los dos.
""",
  en="""
## What you'll get

A Mac managed in Jamf Pro from first power-on, and a policy that installs an application only on the devices that need it, picked by a **smart group** rather than by hand. It is the foundation of everything you will do in Jamf afterwards.

## Before you start

- Access to the Jamf Pro console with a role that can create policies and groups.
- For automated enrolment: the Mac bought through **Apple Business Manager** and assigned to Jamf's MDM server; a **PreStage Enrollment** configured.
- For user-initiated enrolment: the enrolment URL (`https://contoso.jamfcloud.com/enroll`) and a user account in Jamf or the integrated directory.
- A valid **APNs** certificate (Settings → Push certificates). It expires every year; without it, nothing works.

## 1. Enrol

**Automated (ABM)**: the Mac boots, Setup Assistant shows "contoso will configure this Mac", the user signs in and the PreStage creates the local account, installs the agent and applies the profiles. Nothing to download.

**User-initiated**: at `https://contoso.jamfcloud.com/enroll`, sign in, download the management profile and approve it in **System Settings → Privacy & Security → Profiles**. Since macOS 11 the user has to click **Approve** by hand: if they don't, the Mac appears in Jamf without supervised MDM and profiles don't apply.

:::ui Jamf Pro · Computers › Inventory
> Computers › Search Inventory › MBP-LAURA
= Managed: Yes · Supervised: Yes · User Approved MDM: Yes
= macOS: 15.1 · Model: MacBook Pro 14" (M3)
= Last check-in: 21/10/2026 10:52 · Last inventory: 21/10/2026 10:52
= User: laura.prado · Department: Sales
[Management] [History] [Send MDM command]
:::

**Supervised: Yes** and **User Approved MDM: Yes** are the two boxes that must be ticked. Without them, FileVault, restrictions and remote commands fail silently.

## 2. Inventory rules everything

Everything in Jamf (groups, policies, reports) is decided from the **inventory** the Mac submits when it runs `recon`. By default it updates once a day; if you just changed something on the Mac and Jamf doesn't show it, force one:

:::term Terminal · on the Mac
$ sudo jamf recon
Retrieving inventory preferences from https://contoso.jamfcloud.com/...
Locating hardware information (macOS 15.1)...
Locating applications...
Submitting data to https://contoso.jamfcloud.com/...
<computer_id>417</computer_id>
:::

## 3. A smart group

A smart group is a query on the inventory that recalculates itself. Example: Sales Macs that don't yet have the CRM app.

:::ui Jamf Pro · Computers › Smart Computer Groups › New
= Name: Sales without CRM
> Criteria
= Department: is · Sales
= and · Application Title: does not have · CRM Desktop.app
= and · Last Inventory Update: less than x days ago · 7
[Save]
= Members: 23 computers
:::

The third criterion (recent inventory) stops the policy chasing Macs that have been switched off for months.

## 4. The policy

:::ui Jamf Pro · Computers › Policies › New
= Name: Install CRM Desktop
= Trigger: Recurring Check-in · Frequency: Once per computer
> Packages › CRM-Desktop-4.2.pkg › Install
> Maintenance › [x] Update Inventory
> Scope › Target Computers: Sales without CRM
> Self Service › [ ] (no: mandatory install)
[Save]
:::

What happens next: every Mac in the group, at its next check-in (every 15 minutes by default), runs the policy, installs the package and updates the inventory. At the next recalculation it no longer meets the criterion and **leaves the group on its own**. When the group reaches 0 members, you are done, without touching anything.

To test on one Mac without waiting for check-in:

:::term Terminal · on the Mac
$ sudo jamf policy -verbose
Checking for policies triggered by "recurring check-in" for user "laura.prado"...
Executing Policy Install CRM Desktop
Downloading CRM-Desktop-4.2.pkg...
Installing CRM-Desktop-4.2.pkg...
Successfully installed CRM-Desktop-4.2.pkg.
Running Recon...
$ sudo jamf policy -event install-crm   # if the policy has a custom trigger
:::

## 5. When a policy doesn't run

- **Policy logs** (Policies → the policy → Logs): if the Mac shows "Pending", it has not checked in; if "Failed", the log says why (package missing from the distribution point, disk full, a `pkg` that requires a reboot).
- On the Mac: `sudo jamf checkJSSConnection` confirms it reaches the server; `tail -f /var/log/jamf.log` shows execution live.
- A "Once per computer" policy that failed does not retry on its own: **Flush logs** for those computers and it runs again.
- The Mac is not in the group: criterion written wrong (the app name is the bundle name, `CRM Desktop.app`, with `.app`) or inventory not updated.

## Next steps

- Package applications with **Jamf Composer** or use the **Jamf App Catalog** so they update themselves.
- Look at **Self Service** for what the user may install whenever they want: it lowers tickets and gives them autonomy.
- In Level 3 you'll see Mac management from Intune and when Jamf, Intune or both make sense.
""")

# ---------------------------------------------------------------- 2.7 · MECM / SCCM
g(slug="mecm-sccm-empaquetar-una-aplicacion-y-desplegarla", topic="mecm-sccm", date="2026-10-21",
  title_es="MECM / SCCM: empaquetar una aplicación y desplegarla a una colección",
  title_en="MECM / SCCM: packaging an application and deploying it to a collection",
  dek_es="El modelo de aplicación paso a paso: instalación silenciosa, método de detección, distribución de contenido, despliegue y los logs del cliente que dicen la verdad.",
  dek_en="The application model step by step: silent install, detection method, content distribution, deployment, and the client logs that tell the truth.",
  es="""
## Qué vas a conseguir

Una aplicación empaquetada en Microsoft Configuration Manager (MECM, antes SCCM) que se instala sola en los equipos de una colección, con un método de detección que evita reinstalarla, y los tres logs que te dicen por qué un equipo no la recibe.

## Antes de empezar

- Rol de **Application Administrator** (o superior) en la consola de Configuration Manager.
- El instalador en un recurso compartido al que llegue el servidor de sitio: `\\\\cm01\\Sources\\Apps\\7-Zip\\24.08\\`. Una carpeta por aplicación y versión; nunca se sobrescribe una versión anterior.
- Los parámetros de instalación silenciosa del fabricante. Para un MSI son estándar; para un EXE, los pone el fabricante (`/S`, `/quiet`, `/VERYSILENT`).
- Una colección de prueba con dos o tres equipos tuyos antes de cualquier colección real.

## 1. Probar la instalación silenciosa a mano

Antes de tocar la consola, el comando tiene que funcionar en un equipo limpio sin preguntar nada. Si no funciona a mano, no funcionará desde MECM.

:::term PowerShell · como administrador, equipo de prueba
$ msiexec /i "\\\\cm01\\Sources\\Apps\\7-Zip\\24.08\\7z2408-x64.msi" /qn /norestart /l*v C:\\Windows\\Temp\\7zip-install.log
$ $LASTEXITCODE
0
$ Get-ItemProperty "HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\*" | Where-Object DisplayName -like "7-Zip*" | Select-Object DisplayName, DisplayVersion, UninstallString
DisplayName          DisplayVersion UninstallString
-----------          -------------- ---------------
7-Zip 24.08 (x64)    24.08          MsiExec.exe /I{23170F69-40C1-2702-2408-000001000000}
:::

Código de salida `0` (o `3010` si pide reinicio) y la entrada en el registro: eso es lo que MECM va a necesitar para saber que está instalada.

## 2. Crear la aplicación

:::ui Configuration Manager · Biblioteca de software › Aplicaciones › Crear aplicación
= Tipo: Windows Installer (archivo *.msi)
= Ubicación: \\\\cm01\\Sources\\Apps\\7-Zip\\24.08\\7z2408-x64.msi
> Información general
= Nombre: 7-Zip 24.08 (x64)
= Programa de instalación: msiexec /i "7z2408-x64.msi" /qn /norestart
= Comportamiento: Instalar para el sistema · Tanto si el usuario inició sesión como si no
> Tipo de implementación › Método de detección
= Regla: Windows Installer · Código de producto {23170F69-40C1-2702-2408-000001000000}
> Tipo de implementación › Programa de desinstalación
= msiexec /x {23170F69-40C1-2702-2408-000001000000} /qn
[Siguiente] [Cerrar]
:::

Al importar un MSI, el asistente rellena el código de producto y el método de detección solo. Para un EXE tienes que escribirlos tú: el método de detección más fiable es la clave del registro de desinstalación con `DisplayVersion` igual o mayor que la versión que instalas.

! Sin un método de detección correcto, MECM instala la aplicación en cada ciclo de evaluación o la marca como fallida aunque se haya instalado bien. Es el error número uno de los despliegues "que no funcionan".

## 3. Distribuir el contenido

Botón derecho sobre la aplicación → **Distribuir contenido** → el grupo de puntos de distribución. Hasta que el contenido no está en los DP, los clientes no pueden descargarlo. Se comprueba en **Supervisión → Estado de distribución → Estado del contenido**: tiene que estar al 100 % en verde.

## 4. Desplegar

:::ui Configuration Manager · Aplicación › Implementar
= Colección: Pilot - IT (3 miembros)
= Acción: Instalar · Propósito: Obligatorio
= Programación: Disponible ahora · Fecha límite de instalación: lo antes posible
= Experiencia del usuario: Mostrar en Centro de software y todas las notificaciones
= Reinicio: Suprimir el reinicio en estaciones de trabajo
[Siguiente] [Cerrar]
:::

**Disponible** la pone en el Centro de software para que el usuario la instale si quiere; **Obligatorio** con fecha límite la instala sola. Para el piloto, Obligatorio; para la colección real, primero Disponible una semana y después Obligatorio: así los usuarios ya la conocen cuando se les impone.

## 5. En el cliente: forzar y leer los logs

El cliente evalúa las políticas cada hora. Para no esperar:

:::term PowerShell · como administrador, equipo de prueba
# Pedir la política nueva y evaluar las aplicaciones
$ Invoke-CimMethod -Namespace root\\ccm -ClassName SMS_Client -MethodName TriggerSchedule -Arguments @{sScheduleID="{00000000-0000-0000-0000-000000000021}"}
$ Invoke-CimMethod -Namespace root\\ccm -ClassName SMS_Client -MethodName TriggerSchedule -Arguments @{sScheduleID="{00000000-0000-0000-0000-000000000121}"}
# Los tres logs, en C:\\Windows\\CCM\\Logs (ábrelos con CMTrace)
$ Get-Content C:\\Windows\\CCM\\Logs\\AppEnforce.log -Tail 5
    Performing detection of app deployment type 7-Zip 24.08 (x64)...
    App enforcement environment: ... Context: Machine ...
    Prepared command line: "C:\\Windows\\system32\\msiexec.exe" /i "7z2408-x64.msi" /qn /norestart
    Matched exit code 0 to a Success entry in exit codes table.
    ++++++ App enforcement completed (5 seconds) ++++++
:::

- **AppDiscovery.log**: si el método de detección encuentra la app. "Not discovered" cuando sí está instalada = método de detección mal.
- **AppEnforce.log**: el comando que ejecutó y el código de salida. Un `1603` es error genérico del MSI: abre el log del `msiexec` (`/l*v`) para ver el motivo real.
- **CAS.log** y **ContentTransferManager.log**: si no encuentra el contenido ("No DP locations found"), el equipo está en un límite sin DP asignado o el contenido no se distribuyó.

## 6. Qué poner en el ticket

Nombre de la aplicación, colección, nombre del equipo y las líneas de `AppDiscovery` y `AppEnforce` con la hora. Con eso, el administrador de MECM resuelve sin conectarse al equipo.

## Siguientes pasos

- Convierte el EXE más usado del equipo en una aplicación con detección por registro: es el ejercicio que enseña el modelo entero.
- Añade **requisitos** (solo x64, solo Windows 11) y **supersedencia** (la versión nueva reemplaza a la vieja) cuando tengas dos versiones.
- En el Nivel 3 verás Intune y la coadministración: qué cargas de trabajo pasan a la nube y cuáles siguen en MECM.
""",
  en="""
## What you'll get

An application packaged in Microsoft Configuration Manager (MECM, formerly SCCM) that installs itself on the devices in a collection, with a detection method that stops it reinstalling, and the three logs that tell you why a device isn't getting it.

## Before you start

- The **Application Administrator** role (or higher) in the Configuration Manager console.
- The installer on a share the site server can reach: `\\\\cm01\\Sources\\Apps\\7-Zip\\24.08\\`. One folder per application and version; an earlier version is never overwritten.
- The vendor's silent install parameters. For an MSI they are standard; for an EXE the vendor sets them (`/S`, `/quiet`, `/VERYSILENT`).
- A pilot collection with two or three of your own devices before any real collection.

## 1. Test the silent install by hand

Before touching the console, the command has to work on a clean device without asking anything. If it does not work by hand, it will not work from MECM.

:::term PowerShell · as administrator, test device
$ msiexec /i "\\\\cm01\\Sources\\Apps\\7-Zip\\24.08\\7z2408-x64.msi" /qn /norestart /l*v C:\\Windows\\Temp\\7zip-install.log
$ $LASTEXITCODE
0
$ Get-ItemProperty "HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\*" | Where-Object DisplayName -like "7-Zip*" | Select-Object DisplayName, DisplayVersion, UninstallString
DisplayName          DisplayVersion UninstallString
-----------          -------------- ---------------
7-Zip 24.08 (x64)    24.08          MsiExec.exe /I{23170F69-40C1-2702-2408-000001000000}
:::

Exit code `0` (or `3010` if it asks for a reboot) and the registry entry: that is what MECM will need to know it is installed.

## 2. Create the application

:::ui Configuration Manager · Software Library › Applications › Create Application
= Type: Windows Installer (*.msi file)
= Location: \\\\cm01\\Sources\\Apps\\7-Zip\\24.08\\7z2408-x64.msi
> General Information
= Name: 7-Zip 24.08 (x64)
= Installation program: msiexec /i "7z2408-x64.msi" /qn /norestart
= Install behavior: Install for system · Whether or not a user is logged on
> Deployment Type › Detection Method
= Rule: Windows Installer · Product code {23170F69-40C1-2702-2408-000001000000}
> Deployment Type › Uninstall program
= msiexec /x {23170F69-40C1-2702-2408-000001000000} /qn
[Next] [Close]
:::

When importing an MSI, the wizard fills in the product code and the detection method on its own. For an EXE you write them yourself: the most reliable detection method is the uninstall registry key with `DisplayVersion` equal to or greater than the version you install.

! Without a correct detection method, MECM installs the application on every evaluation cycle, or marks it failed even though it installed fine. It is the number one cause of deployments "that don't work".

## 3. Distribute the content

Right-click the application → **Distribute Content** → the distribution point group. Until the content is on the DPs, clients cannot download it. Check it under **Monitoring → Distribution Status → Content Status**: it has to be 100% green.

## 4. Deploy

:::ui Configuration Manager · Application › Deploy
= Collection: Pilot - IT (3 members)
= Action: Install · Purpose: Required
= Scheduling: Available now · Installation deadline: As soon as possible
= User Experience: Display in Software Center and show all notifications
= Restart: Suppress restart on workstations
[Next] [Close]
:::

**Available** puts it in Software Center for the user to install if they want; **Required** with a deadline installs it on its own. For the pilot, Required; for the real collection, Available for a week first and then Required: users already know it by the time it is enforced.

## 5. On the client: force it and read the logs

The client evaluates policies every hour. To avoid waiting:

:::term PowerShell · as administrator, test device
# Request the new policy and evaluate applications
$ Invoke-CimMethod -Namespace root\\ccm -ClassName SMS_Client -MethodName TriggerSchedule -Arguments @{sScheduleID="{00000000-0000-0000-0000-000000000021}"}
$ Invoke-CimMethod -Namespace root\\ccm -ClassName SMS_Client -MethodName TriggerSchedule -Arguments @{sScheduleID="{00000000-0000-0000-0000-000000000121}"}
# The three logs, in C:\\Windows\\CCM\\Logs (open them with CMTrace)
$ Get-Content C:\\Windows\\CCM\\Logs\\AppEnforce.log -Tail 5
    Performing detection of app deployment type 7-Zip 24.08 (x64)...
    App enforcement environment: ... Context: Machine ...
    Prepared command line: "C:\\Windows\\system32\\msiexec.exe" /i "7z2408-x64.msi" /qn /norestart
    Matched exit code 0 to a Success entry in exit codes table.
    ++++++ App enforcement completed (5 seconds) ++++++
:::

- **AppDiscovery.log**: whether the detection method finds the app. "Not discovered" when it is installed = detection method wrong.
- **AppEnforce.log**: the command it ran and the exit code. A `1603` is the MSI's generic error: open the `msiexec` log (`/l*v`) for the real reason.
- **CAS.log** and **ContentTransferManager.log**: if it cannot find the content ("No DP locations found"), the device is in a boundary with no DP assigned, or the content was not distributed.

## 6. What to put in the ticket

Application name, collection, device name and the `AppDiscovery` and `AppEnforce` lines with the time. With that, the MECM administrator resolves it without connecting to the device.

## Next steps

- Turn the team's most used EXE into an application with registry detection: it is the exercise that teaches the whole model.
- Add **requirements** (x64 only, Windows 11 only) and **supersedence** (the new version replaces the old one) once you have two versions.
- In Level 3 you'll see Intune and co-management: which workloads move to the cloud and which stay in MECM.
""")

# ---------------------------------------------------------------- 2.8 · Microsoft Teams Rooms
g(slug="teams-rooms-poner-en-marcha-una-sala", topic="teams-rooms", date="2026-10-21",
  title_es="Microsoft Teams Rooms: poner en marcha una sala y supervisarla",
  title_en="Microsoft Teams Rooms: bringing a room online and keeping an eye on it",
  dek_es="Cuenta de recurso, licencia, inicio de sesión del dispositivo, periféricos y el Pro Management Portal. Y los fallos típicos de una sala el lunes por la mañana.",
  dek_en="Resource account, licence, device sign-in, peripherals and the Pro Management Portal. Plus the typical Monday-morning room failures.",
  es="""
## Qué vas a conseguir

Una sala de reuniones con Microsoft Teams Rooms (MTR) que aparece en el calendario, se une a las reuniones con un toque y se supervisa desde el portal sin ir a la sala. Y un método corto para "la sala no funciona".

## Antes de empezar

- Rol de **Administrador de Teams** y de **Exchange** (o un compañero que los tenga): la sala es un buzón de recurso.
- Licencia **Teams Rooms Pro** (o Basic, para menos de 25 salas, sin el portal completo) disponible para asignarla a la cuenta de la sala.
- El equipo de la sala (Crestron, Logitech, Poly, Yealink… con Windows o Android) montado, con la pantalla táctil, la cámara y el audio conectados, y red (cable mejor que Wi-Fi).

## 1. La cuenta de recurso

La sala es un buzón de tipo **sala** en Exchange Online con una contraseña que no caduca y la licencia de Teams Rooms. Todo lo demás depende de esto.

:::term PowerShell · Exchange Online + Graph
$ Connect-ExchangeOnline
$ New-Mailbox -Room -Name "Sala Madrid 2.1" -Alias sala-mad-21 -PrimarySmtpAddress sala-mad-21@contoso.com
$ Set-CalendarProcessing -Identity sala-mad-21 -AutomateProcessing AutoAccept -AddOrganizerToSubject $false -DeleteComments $false -DeleteSubject $false -RemovePrivateProperty $false -ProcessExternalMeetingMessages $true
$ Set-Mailbox -Identity sala-mad-21 -Type Regular   # permite iniciar sesión; después vuelve a Room si tu política lo pide
$ Connect-MgGraph -Scopes "User.ReadWrite.All","Organization.Read.All"
$ Update-MgUser -UserId sala-mad-21@contoso.com -UsageLocation ES -PasswordPolicies DisablePasswordExpiration -AccountEnabled:$true
$ $sku = (Get-MgSubscribedSku | Where-Object SkuPartNumber -eq "Microsoft_Teams_Rooms_Pro").SkuId
$ Set-MgUserLicense -UserId sala-mad-21@contoso.com -AddLicenses @{SkuId = $sku} -RemoveLicenses @()
:::

`DeleteComments $false` y `DeleteSubject $false` son lo que hace que la reunión llegue al panel de la sala con el enlace de Teams dentro. Si se dejan por defecto, Exchange borra el cuerpo de la invitación y el botón **Unirse** no aparece.

! Si usáis Conditional Access que exige MFA a todos, la cuenta de la sala no podrá iniciar sesión. Lo habitual es una política específica para las cuentas de sala: exclusión de MFA, pero restringida a las IP de las oficinas o a dispositivos conformes.

## 2. Inicio de sesión en el dispositivo

En la consola táctil: **Más → Configuración → contraseña de administrador → Cuenta**, correo y contraseña de la sala, modo **Exchange/Teams** (o solo Teams si no hay buzón híbrido). Al reiniciar, el panel muestra el nombre de la sala y el calendario del día.

:::ui Teams Rooms · consola táctil › Configuración › Cuenta
= Correo electrónico: sala-mad-21@contoso.com
= Modo compatible: Exchange y Teams
= Dirección de Exchange: autodetectar
= Estado: Teams conectado · Exchange conectado · Calendario sincronizado
[Guardar y salir]
:::

Si pone "Exchange: error de autenticación" pero Teams conecta, el buzón sigue siendo de tipo Room sin permitir inicio de sesión, o la contraseña ha caducado.

## 3. Periféricos

En **Configuración → Periféricos** se elige qué cámara, micrófono y altavoz usa la sala. Las barras todo-en-uno (Logitech Rally Bar, Poly Studio) aparecen como un solo dispositivo; con un procesador Crestron y periféricos separados, cada uno va por USB y hay que elegirlos uno a uno. Regla práctica: un solo cable USB desde la barra o el hub al equipo de la sala, sin alargadores de dudosa calidad; la mitad de los "no hay cámara" es un cable.

## 4. Supervisar desde el portal

Con la licencia Pro, el **Teams Rooms Pro Management Portal** (`portal.rooms.microsoft.com`) muestra cada sala, su estado, los periféricos y los incidentes, y permite reiniciar y actualizar sin ir a la sala.

:::ui Teams Rooms Pro Management · Salas
= Sala Madrid 2.1 · Estado: Correcto · Última señal: hace 2 min
= Dispositivo: Crestron Flex UC-C100 · Windows · App 5.2
= Periféricos: cámara OK · micrófono OK · altavoz OK · pantalla OK
= Incidentes: 0 abiertos · Última reunión: hoy 10:00 (2 participantes remotos)
[Reiniciar] [Actualizar] [Ver registro]
:::

Un **ticket** en el portal se abre solo cuando un periférico deja de responder o la app lleva sin señal un tiempo. Conviene ir ahí antes de que el usuario lo diga.

## 5. "La sala no funciona": el orden

1. **¿La consola está encendida y con la hora correcta?** Una sala con la hora mal no inicia sesión (certificados). Reinicio desde el portal o apagado físico 30 segundos.
2. **¿Aparece el calendario?** Si no, es la cuenta (paso 1 y 2): contraseña, licencia, Conditional Access. Prueba a iniciar sesión con la cuenta de la sala en `outlook.office.com` desde un portátil: si pide MFA o está bloqueada, ahí está.
3. **¿La reunión no tiene botón Unirse?** `Set-CalendarProcessing` con `DeleteComments` a `$true`, o la reunión no es de Teams (invitación sin enlace). Las reuniones de terceros (Zoom, Webex) necesitan la **unión directa a invitados** activada en la configuración de la sala.
4. **¿No hay audio, vídeo o pantalla compartida?** Periféricos (paso 3): cable, hub, o el dispositivo elegido en la configuración no es el que está conectado. Un reinicio del dispositivo reconoce los periféricos de nuevo.
5. **¿Todo bien pero los remotos no oyen?** Calidad de red: la sala por Wi-Fi o en una VLAN con QoS mal configurada. El portal muestra la calidad de cada reunión; si es la red, va a redes con la hora y la sala.

## Siguientes pasos

- Pon la cuenta de la sala en un grupo con **licencias por grupo** y una política de Conditional Access propia: así cada sala nueva es dar de alta un buzón y meterlo en el grupo.
- Activa en el portal las **actualizaciones automáticas** en un anillo de prueba con una sala antes del resto.
- En el Nivel 4 verás el soporte a comités y dirección: cuando una sala de consejo falla, no hay segundo intento.
""",
  en="""
## What you'll get

A meeting room with Microsoft Teams Rooms (MTR) that shows up in the calendar, joins meetings with one tap and is monitored from the portal without walking to the room. Plus a short method for "the room doesn't work".

## Before you start

- The **Teams Administrator** and **Exchange** roles (or a colleague who has them): the room is a resource mailbox.
- A **Teams Rooms Pro** licence (or Basic, for fewer than 25 rooms, without the full portal) available to assign to the room account.
- The room hardware (Crestron, Logitech, Poly, Yealink… on Windows or Android) installed, with the touch console, camera and audio connected, and network (cable rather than Wi-Fi).

## 1. The resource account

The room is a **room** mailbox in Exchange Online with a non-expiring password and the Teams Rooms licence. Everything else depends on this.

:::term PowerShell · Exchange Online + Graph
$ Connect-ExchangeOnline
$ New-Mailbox -Room -Name "Madrid Room 2.1" -Alias room-mad-21 -PrimarySmtpAddress room-mad-21@contoso.com
$ Set-CalendarProcessing -Identity room-mad-21 -AutomateProcessing AutoAccept -AddOrganizerToSubject $false -DeleteComments $false -DeleteSubject $false -RemovePrivateProperty $false -ProcessExternalMeetingMessages $true
$ Set-Mailbox -Identity room-mad-21 -Type Regular   # allows sign-in; switch back to Room afterwards if your policy requires it
$ Connect-MgGraph -Scopes "User.ReadWrite.All","Organization.Read.All"
$ Update-MgUser -UserId room-mad-21@contoso.com -UsageLocation ES -PasswordPolicies DisablePasswordExpiration -AccountEnabled:$true
$ $sku = (Get-MgSubscribedSku | Where-Object SkuPartNumber -eq "Microsoft_Teams_Rooms_Pro").SkuId
$ Set-MgUserLicense -UserId room-mad-21@contoso.com -AddLicenses @{SkuId = $sku} -RemoveLicenses @()
:::

`DeleteComments $false` and `DeleteSubject $false` are what make the meeting reach the room's console with the Teams link inside. Left at the defaults, Exchange strips the invitation body and the **Join** button never appears.

! If you use Conditional Access requiring MFA for everyone, the room account won't be able to sign in. The usual approach is a dedicated policy for room accounts: MFA exclusion, but restricted to office IPs or compliant devices.

## 2. Sign in on the device

On the touch console: **More → Settings → admin password → Account**, the room's email and password, **Exchange/Teams** mode (or Teams only if there is no hybrid mailbox). After a restart, the console shows the room name and the day's calendar.

:::ui Teams Rooms · touch console › Settings › Account
= Email address: room-mad-21@contoso.com
= Supported meeting mode: Exchange and Teams
= Exchange address: autodiscover
= Status: Teams connected · Exchange connected · Calendar synced
[Save and exit]
:::

If it says "Exchange: authentication error" but Teams connects, the mailbox is still of type Room without sign-in allowed, or the password has expired.

## 3. Peripherals

**Settings → Peripherals** is where you pick which camera, microphone and speaker the room uses. All-in-one bars (Logitech Rally Bar, Poly Studio) appear as a single device; with a Crestron processor and separate peripherals, each one comes over USB and has to be selected one by one. Practical rule: a single USB cable from the bar or hub to the room PC, with no dubious extenders; half of all "no camera" tickets are a cable.

## 4. Monitor from the portal

With the Pro licence, the **Teams Rooms Pro Management Portal** (`portal.rooms.microsoft.com`) shows every room, its status, peripherals and incidents, and lets you restart and update without visiting the room.

:::ui Teams Rooms Pro Management · Rooms
= Madrid Room 2.1 · Status: Healthy · Last signal: 2 min ago
= Device: Crestron Flex UC-C100 · Windows · App 5.2
= Peripherals: camera OK · microphone OK · speaker OK · display OK
= Incidents: 0 open · Last meeting: today 10:00 (2 remote participants)
[Restart] [Update] [View log]
:::

A **ticket** opens in the portal on its own when a peripheral stops responding or the app has gone silent for a while. Worth looking there before the user tells you.

## 5. "The room doesn't work": the order

1. **Is the console on, with the right time?** A room with the wrong time can't sign in (certificates). Restart from the portal, or a physical 30-second power-off.
2. **Does the calendar appear?** If not, it is the account (steps 1 and 2): password, licence, Conditional Access. Try signing in with the room account at `outlook.office.com` from a laptop: if it asks for MFA or is blocked, there is your answer.
3. **The meeting has no Join button?** `Set-CalendarProcessing` with `DeleteComments` at `$true`, or the meeting isn't a Teams one (invitation with no link). Third-party meetings (Zoom, Webex) need **direct guest join** enabled in the room settings.
4. **No audio, video or screen sharing?** Peripherals (step 3): cable, hub, or the device chosen in settings isn't the one plugged in. A device restart re-detects the peripherals.
5. **All fine but remote people can't hear?** Network quality: the room on Wi-Fi or on a VLAN with misconfigured QoS. The portal shows each meeting's quality; if it is the network, it goes to networks with the time and the room.

## Next steps

- Put the room account in a group with **group-based licensing** and its own Conditional Access policy: every new room then becomes creating a mailbox and adding it to the group.
- Enable **automatic updates** in the portal on a test ring with one room before the rest.
- In Level 4 you'll see board and executive support: when a boardroom fails, there is no second attempt.
""")

# ---------------------------------------------------------------- 2.9 · PDQ y MDT
g(slug="pdq-y-mdt-desplegar-software-en-lote-e-instalar-windows", topic="pdq-mdt", date="2026-10-21",
  title_es="PDQ y MDT: desplegar software en lote e instalar Windows desde cero",
  title_en="PDQ and MDT: deploying software in bulk and installing Windows from scratch",
  dek_es="PDQ Deploy e Inventory para empujar un instalador a 50 equipos esta tarde, y MDT para una instalación limpia de Windows con un recurso compartido de implementación. Cuándo sigue teniendo sentido frente a Intune.",
  dek_en="PDQ Deploy and Inventory to push an installer to 50 devices this afternoon, and MDT for a clean Windows install from a deployment share. When it still makes sense next to Intune.",
  es="""
## Qué vas a conseguir

Dos herramientas que resuelven el día a día de una oficina sin MECM: con **PDQ Deploy** instalas o actualizas una aplicación en decenas de equipos en minutos; con **MDT** (Microsoft Deployment Toolkit) preparas un Windows limpio con los controladores y las aplicaciones base para un equipo nuevo o reinstalado.

## Antes de empezar

- Un servidor o equipo de administración unido al dominio para PDQ y para el recurso compartido de MDT.
- Una cuenta de dominio con **administrador local** en los equipos de destino (PDQ la usa para instalar). Guárdala en PDQ como credencial, no en un script.
- En los equipos de destino: compartición de archivos e impresoras activada y el firewall permitiendo **Administración remota** (PDQ usa SMB y el servicio de administración remota, no WinRM).
- Para MDT: el ADK de Windows y el complemento WinPE instalados en el servidor, y una ISO de Windows 11 Enterprise.

## 1. PDQ Inventory: saber qué hay

Antes de desplegar, saber dónde. PDQ Inventory escanea los equipos del dominio y mantiene colecciones dinámicas (por aplicación, versión, SO, disco).

:::ui PDQ Inventory · Colecciones
> Colecciones › Nueva colección dinámica
= Nombre: 7-Zip desactualizado
= Equipos donde: Aplicación · Nombre · contiene · 7-Zip
= y · Aplicación · Versión · menor que · 24.08
= y · Equipo · Visto por última vez · en los últimos · 7 días
= Miembros: 38 equipos
:::

Con esto, "¿cuántos equipos tienen el Java viejo?" o "¿qué portátiles no han aparecido en 30 días?" es una colección, no una tarde.

## 2. PDQ Deploy: el paquete y el despliegue

:::ui PDQ Deploy · Paquetes › Nuevo paquete
= Nombre: 7-Zip 24.08 (x64)
> Paso 1 · Instalar
= Archivo: \\\\srv-files-01\\Deploy\\7-Zip\\7z2408-x64.msi
= Parámetros: /qn /norestart
= Códigos de éxito: 0, 1641, 3010
> Condiciones
= Arquitectura: 64 bits · SO: Windows 10, Windows 11
[Guardar]
:::

Despliegue: botón derecho sobre el paquete → **Implementar una vez** → elegir la colección de Inventory "7-Zip desactualizado" → **Implementar ahora**. La ventana de estado muestra cada equipo en vivo: Correcto, Error (con el código) o Sin conexión.

- **Sin conexión**: el equipo está apagado o fuera de la red. Con **Implementación automática** ligada a la colección, PDQ lo instalará cuando aparezca (lo que PDQ llama *heartbeat*).
- **Error 1603** o similar: el instalador falla en ese equipo. Prueba el comando a mano en él (igual que en la guía de MECM): casi siempre es una versión antigua que no se desinstala o un proceso abierto.
- **Acceso denegado**: la credencial no es administrador local en ese equipo, o el firewall bloquea.

> PDQ no tiene cliente: todo lo hace por SMB y servicios remotos desde la consola. Por eso es tan rápido de montar, y por eso solo llega a los equipos que están en la red corporativa o en VPN.

## 3. MDT: un Windows limpio

MDT instala Windows a partir de un **recurso compartido de implementación** (`\\\\srv-mdt-01\\DeploymentShare$`) con una **secuencia de tareas** que formatea, instala el SO, los controladores y las aplicaciones base, une al dominio y pone el nombre.

:::ui Deployment Workbench · Deployment Share
> Deployment Shares › MDT Production › Operating Systems › Importar: Windows 11 Enterprise 24H2 (install.wim)
> Deployment Shares › MDT Production › Out-of-Box Drivers › Fabrikam › Portable 14 G3 (importados desde el paquete del fabricante)
> Deployment Shares › MDT Production › Applications › 7-Zip 24.08 · Office 365 Apps · Cisco Secure Client
> Deployment Shares › MDT Production › Task Sequences › Nueva: "W11 Estándar oficina" (Standard Client Task Sequence)
> Task Sequence › Preinstall › Inject Drivers › Selección por perfil: modelo (%Model%)
> Task Sequence › State Restore › Install Applications › 7-Zip, Office, Secure Client
[Update Deployment Share] (genera el WinPE de arranque: LiteTouchPE_x64.iso / .wim)
:::

Dos ficheros deciden casi todo:

- **CustomSettings.ini**: las respuestas por defecto (dominio, OU, zona horaria, idioma, nombre del equipo con `OSDComputerName=%SerialNumber%`), para que el asistente no pregunte lo que ya sabes.
- **Bootstrap.ini**: la ruta del recurso compartido y la credencial de solo lectura con la que WinPE lo monta. Se mete dentro del WinPE al actualizar el share.

Después: arrancar el equipo desde el USB o por PXE (si hay WDS) con `LiteTouchPE_x64`, elegir la secuencia de tareas y en 25-40 minutos el equipo está en el dominio con todo instalado. El log que importa si algo falla: `C:\\MININT\\SMSOSD\\OSDLOGS\\BDD.log` durante la instalación, y `C:\\Windows\\Temp\\DeploymentLogs\\` al final (ábrelos con CMTrace).

## 4. Dónde encajan hoy

PDQ y MDT siguen siendo útiles en oficinas con equipos en red local, sin MECM, y para reinstalar en el taller. Lo que ha cambiado: los portátiles que nunca pisan la oficina se gestionan con **Intune y Autopilot** (la imagen viene de fábrica y se configura sola), y las aplicaciones en esos equipos se despliegan con **Win32 apps** de Intune. Lo normal en 2026 es tener las dos cosas: MDT para el taller y el equipo de sobremesa, Autopilot para el portátil remoto.

## Siguientes pasos

- En PDQ, crea una **implementación automática** para los parches de navegadores y Java: se mantienen al día sin que nadie lo lance.
- En MDT, añade un paso de **actualización de Windows** al final de la secuencia (Windows Update dentro de la secuencia de tareas) para que el equipo salga ya parcheado.
- En el Nivel 3 verás Intune de principio a fin, y en la guía de MECM/SCCM el equivalente de todo esto con infraestructura propia.
""",
  en="""
## What you'll get

Two tools that handle the everyday needs of an office without MECM: with **PDQ Deploy** you install or update an application on dozens of devices in minutes; with **MDT** (Microsoft Deployment Toolkit) you prepare a clean Windows with drivers and base applications for a new or rebuilt device.

## Before you start

- A domain-joined server or admin workstation for PDQ and for the MDT share.
- A domain account with **local administrator** on the target devices (PDQ uses it to install). Store it in PDQ as a credential, not in a script.
- On the targets: file and printer sharing enabled and the firewall allowing **Remote Administration** (PDQ uses SMB and the remote admin service, not WinRM).
- For MDT: the Windows ADK and the WinPE add-on installed on the server, and a Windows 11 Enterprise ISO.

## 1. PDQ Inventory: know what's there

Before deploying, know where. PDQ Inventory scans the domain's devices and keeps dynamic collections (by application, version, OS, disk).

:::ui PDQ Inventory · Collections
> Collections › New Dynamic Collection
= Name: 7-Zip outdated
= Computers where: Application · Name · contains · 7-Zip
= and · Application · Version · less than · 24.08
= and · Computer · Last seen · within the last · 7 days
= Members: 38 computers
:::

With this, "how many devices have the old Java?" or "which laptops haven't shown up in 30 days?" is a collection, not an afternoon.

## 2. PDQ Deploy: the package and the deployment

:::ui PDQ Deploy · Packages › New Package
= Name: 7-Zip 24.08 (x64)
> Step 1 · Install
= File: \\\\srv-files-01\\Deploy\\7-Zip\\7z2408-x64.msi
= Parameters: /qn /norestart
= Success codes: 0, 1641, 3010
> Conditions
= Architecture: 64-bit · OS: Windows 10, Windows 11
[Save]
:::

Deployment: right-click the package → **Deploy Once** → pick the Inventory collection "7-Zip outdated" → **Deploy Now**. The status window shows every device live: Successful, Failed (with the code) or Offline.

- **Offline**: the device is off or away from the network. With an **Auto Deployment** tied to the collection, PDQ installs it when it reappears (what PDQ calls *heartbeat*).
- **Error 1603** or similar: the installer fails on that device. Try the command by hand on it (as in the MECM guide): almost always an old version that won't uninstall, or an open process.
- **Access denied**: the credential is not a local admin on that device, or the firewall blocks it.

> PDQ has no client: it does everything over SMB and remote services from the console. That is why it is so quick to set up, and why it only reaches devices on the corporate network or VPN.

## 3. MDT: a clean Windows

MDT installs Windows from a **deployment share** (`\\\\srv-mdt-01\\DeploymentShare$`) with a **task sequence** that formats, installs the OS, drivers and base apps, joins the domain and sets the name.

:::ui Deployment Workbench · Deployment Share
> Deployment Shares › MDT Production › Operating Systems › Import: Windows 11 Enterprise 24H2 (install.wim)
> Deployment Shares › MDT Production › Out-of-Box Drivers › Fabrikam › Portable 14 G3 (imported from the vendor's driver pack)
> Deployment Shares › MDT Production › Applications › 7-Zip 24.08 · Office 365 Apps · Cisco Secure Client
> Deployment Shares › MDT Production › Task Sequences › New: "W11 Standard office" (Standard Client Task Sequence)
> Task Sequence › Preinstall › Inject Drivers › Selection profile: model (%Model%)
> Task Sequence › State Restore › Install Applications › 7-Zip, Office, Secure Client
[Update Deployment Share] (builds the WinPE boot media: LiteTouchPE_x64.iso / .wim)
:::

Two files decide almost everything:

- **CustomSettings.ini**: the default answers (domain, OU, time zone, language, computer name with `OSDComputerName=%SerialNumber%`), so the wizard doesn't ask what you already know.
- **Bootstrap.ini**: the share path and the read-only credential WinPE mounts it with. It is baked into WinPE when you update the share.

Then: boot the device from USB or PXE (if WDS is there) with `LiteTouchPE_x64`, pick the task sequence, and in 25-40 minutes the device is in the domain with everything installed. The log that matters if something fails: `C:\\MININT\\SMSOSD\\OSDLOGS\\BDD.log` during the install, and `C:\\Windows\\Temp\\DeploymentLogs\\` at the end (open them with CMTrace).

## 4. Where they fit today

PDQ and MDT are still useful in offices with devices on the LAN, without MECM, and for rebuilding in the workshop. What has changed: laptops that never set foot in the office are managed with **Intune and Autopilot** (the image comes from the factory and configures itself), and applications on those devices are deployed as Intune **Win32 apps**. The normal setup in 2026 is both: MDT for the workshop and the desktop, Autopilot for the remote laptop.

## Next steps

- In PDQ, create an **Auto Deployment** for browser and Java patches: they stay current without anyone launching them.
- In MDT, add a **Windows Update** step at the end of the sequence (Windows Update inside the task sequence) so the device comes out already patched.
- In Level 3 you'll see Intune from start to finish, and in the MECM/SCCM guide the equivalent of all this with your own infrastructure.
""")

# ---------------------------------------------------------------- 2.10 · PowerShell
g(slug="powershell-script-de-inventario-remoto-con-csv", topic="powershell", date="2026-10-21",
  title_es="PowerShell: un script de inventario que corre en remoto, maneja errores y deja un CSV",
  title_en="PowerShell: an inventory script that runs remotely, handles errors and leaves a CSV",
  dek_es="Objetos en lugar de texto, Invoke-Command sobre una lista de equipos, try/catch para los que no responden, y un CSV que abre Excel. Con la política de ejecución y la firma explicadas.",
  dek_en="Objects instead of text, Invoke-Command over a list of devices, try/catch for the ones that don't answer, and a CSV Excel can open. With execution policy and signing explained.",
  es="""
## Qué vas a conseguir

Un script que, dada una lista de equipos, se conecta a cada uno, saca modelo, número de serie, versión de Windows, disco libre y último arranque, y deja un CSV con una fila por equipo, incluidos los que no respondieron y por qué. Es el patrón que repetirás en la mitad de los scripts de IT.

## Antes de empezar

- PowerShell 5.1 (viene con Windows) o PowerShell 7 (`winget install Microsoft.PowerShell`). El script vale en los dos.
- **WinRM** activado en los equipos de destino (en dominio suele estarlo por GPO; si no, `Enable-PSRemoting -Force` en cada uno, o la GPO *Permitir la administración remota del servidor a través de WinRM*).
- Tu cuenta con administrador local en los equipos, o una credencial para pasarla con `-Credential`.
- Un editor con PowerShell integrado: **VS Code** con la extensión de PowerShell marca errores mientras escribes.

## 1. Objetos, no texto

La diferencia con `cmd` y con Bash: un comando de PowerShell devuelve **objetos** con propiedades, no líneas. Por eso puedes seleccionar, filtrar y exportar sin cortar cadenas.

:::term PowerShell
$ Get-CimInstance Win32_OperatingSystem | Select-Object Caption, Version, LastBootUpTime
Caption                          Version    LastBootUpTime
-------                          -------    --------------
Microsoft Windows 11 Enterprise  10.0.26100 03/10/2026 8:12:40
$ (Get-CimInstance Win32_OperatingSystem).LastBootUpTime -lt (Get-Date).AddDays(-14)
True
:::

`Get-CimInstance` sustituye a `Get-WmiObject` (obsoleto). `Get-Member` sobre cualquier objeto te enseña qué propiedades tiene.

## 2. El script

:::term VS Code · Get-DeviceInventory.ps1
#Requires -Version 5.1
<#
.SYNOPSIS  Inventario básico de equipos por WinRM, con un CSV de salida.
.EXAMPLE   .\\Get-DeviceInventory.ps1 -ComputerName (Get-Content equipos.txt) -OutFile inventario.csv
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory)] [string[]] $ComputerName,
    [string] $OutFile = "inventario-$(Get-Date -Format yyyyMMdd).csv",
    [pscredential] $Credential
)

$remote = {
    $os  = Get-CimInstance Win32_OperatingSystem
    $cs  = Get-CimInstance Win32_ComputerSystem
    $bio = Get-CimInstance Win32_BIOS
    $c   = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'"
    [pscustomobject]@{
        Computer   = $env:COMPUTERNAME
        Model      = "$($cs.Manufacturer) $($cs.Model)"
        Serial     = $bio.SerialNumber
        OS         = $os.Caption
        Build      = $os.Version
        FreeGB     = [math]::Round($c.FreeSpace / 1GB, 1)
        LastBoot   = $os.LastBootUpTime
        LastUser   = $cs.UserName
    }
}

$results = foreach ($pc in $ComputerName) {
    Write-Verbose "Consultando $pc"
    try {
        $p = @{ ComputerName = $pc; ScriptBlock = $remote; ErrorAction = 'Stop' }
        if ($Credential) { $p.Credential = $Credential }
        $r = Invoke-Command @p
        $r | Select-Object * -ExcludeProperty PSComputerName, RunspaceId, PSShowComputerName |
             Add-Member -NotePropertyName Status -NotePropertyValue OK -PassThru
    }
    catch {
        [pscustomobject]@{ Computer = $pc; Model = $null; Serial = $null; OS = $null; Build = $null
                           FreeGB = $null; LastBoot = $null; LastUser = $null
                           Status = "ERROR: $($_.Exception.Message -replace '\\s+',' ')" }
    }
}

$results | Export-Csv -Path $OutFile -NoTypeInformation -Encoding UTF8 -Delimiter ';'
$ok = ($results | Where-Object Status -eq 'OK').Count
Write-Host "$ok de $($ComputerName.Count) equipos respondieron. CSV: $OutFile"
:::

Lo que hace que sea un script y no un apaño: `param` con tipos (así `-ComputerName` acepta una lista), `[CmdletBinding()]` que da `-Verbose` gratis, el bloque remoto que devuelve un **objeto** por equipo, `try/catch` con `ErrorAction Stop` para que un equipo apagado no pare el bucle, y el CSV con **`;`** como separador para que Excel en español lo abra en columnas.

## 3. Ejecutarlo

:::term PowerShell
$ .\\Get-DeviceInventory.ps1 -ComputerName LAPTOP-7F2K9Q, DESK-MAD-201, LAPTOP-OLD-1 -Verbose
VERBOSE: Consultando LAPTOP-7F2K9Q
VERBOSE: Consultando DESK-MAD-201
VERBOSE: Consultando LAPTOP-OLD-1
2 de 3 equipos respondieron. CSV: inventario-20261021.csv
$ Import-Csv .\\inventario-20261021.csv -Delimiter ';' | Format-Table Computer, FreeGB, LastBoot, Status
Computer       FreeGB LastBoot            Status
--------       ------ --------            ------
LAPTOP-7F2K9Q    21,4 03/10/2026 8:12:40  OK
DESK-MAD-201    188,0 20/10/2026 7:55:02  OK
LAPTOP-OLD-1                              ERROR: Connecting to remote server LAPTOP-OLD-1 failed with the following error message : WinRM cannot complete the operation...
:::

Para cientos de equipos, `Invoke-Command` acepta la lista entera a la vez y los consulta en paralelo (`-ThrottleLimit 32`); el bucle de arriba es más lento pero deja claro qué equipo falló y por qué.

## 4. Política de ejecución y firma

Si al ejecutarlo aparece *"no se puede cargar porque la ejecución de scripts está deshabilitada"*, es la **política de ejecución**. No es seguridad contra atacantes; es un seguro contra ejecutar scripts por accidente.

:::term PowerShell
$ Get-ExecutionPolicy -List
        Scope ExecutionPolicy
        ----- ---------------
  MachinePolicy       Undefined
     UserPolicy       Undefined
        Process       Undefined
    CurrentUser       Undefined
   LocalMachine      Restricted
$ Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
:::

`RemoteSigned` ejecuta lo que escribes tú y exige firma a lo descargado. Si la empresa la fija por GPO en `AllSigned`, los scripts del equipo se **firman** con un certificado de firma de código de la CA interna (`Set-AuthenticodeSignature`). Es lo correcto en producción y encaja con el repositorio de la guía de Git: solo lo revisado se firma.

## Siguientes pasos

- Cambia la lista de equipos por `Get-ADComputer -Filter {OperatingSystem -like "Windows 11*"}` y tendrás el inventario de todo el dominio.
- Pasa el resultado por `PSScriptAnalyzer` (`Invoke-ScriptAnalyzer .\\Get-DeviceInventory.ps1`) antes de subirlo al repo.
- En el Nivel 3 verás Microsoft Graph desde PowerShell: el mismo patrón, contra Entra ID e Intune en lugar de WinRM.
""",
  en="""
## What you'll get

A script that, given a list of devices, connects to each one, pulls model, serial number, Windows version, free disk and last boot, and leaves a CSV with one row per device, including the ones that didn't answer and why. It is the pattern you'll repeat in half of all IT scripts.

## Before you start

- PowerShell 5.1 (ships with Windows) or PowerShell 7 (`winget install Microsoft.PowerShell`). The script works on both.
- **WinRM** enabled on the target devices (in a domain it usually is, by GPO; if not, `Enable-PSRemoting -Force` on each, or the GPO *Allow remote server management through WinRM*).
- Your account as local administrator on the devices, or a credential to pass with `-Credential`.
- An editor with PowerShell support: **VS Code** with the PowerShell extension flags errors as you type.

## 1. Objects, not text

The difference from `cmd` and Bash: a PowerShell command returns **objects** with properties, not lines. That is why you can select, filter and export without slicing strings.

:::term PowerShell
$ Get-CimInstance Win32_OperatingSystem | Select-Object Caption, Version, LastBootUpTime
Caption                          Version    LastBootUpTime
-------                          -------    --------------
Microsoft Windows 11 Enterprise  10.0.26100 03/10/2026 8:12:40
$ (Get-CimInstance Win32_OperatingSystem).LastBootUpTime -lt (Get-Date).AddDays(-14)
True
:::

`Get-CimInstance` replaces `Get-WmiObject` (deprecated). `Get-Member` on any object shows you which properties it has.

## 2. The script

:::term VS Code · Get-DeviceInventory.ps1
#Requires -Version 5.1
<#
.SYNOPSIS  Basic device inventory over WinRM, with a CSV output.
.EXAMPLE   .\\Get-DeviceInventory.ps1 -ComputerName (Get-Content devices.txt) -OutFile inventory.csv
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory)] [string[]] $ComputerName,
    [string] $OutFile = "inventory-$(Get-Date -Format yyyyMMdd).csv",
    [pscredential] $Credential
)

$remote = {
    $os  = Get-CimInstance Win32_OperatingSystem
    $cs  = Get-CimInstance Win32_ComputerSystem
    $bio = Get-CimInstance Win32_BIOS
    $c   = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'"
    [pscustomobject]@{
        Computer   = $env:COMPUTERNAME
        Model      = "$($cs.Manufacturer) $($cs.Model)"
        Serial     = $bio.SerialNumber
        OS         = $os.Caption
        Build      = $os.Version
        FreeGB     = [math]::Round($c.FreeSpace / 1GB, 1)
        LastBoot   = $os.LastBootUpTime
        LastUser   = $cs.UserName
    }
}

$results = foreach ($pc in $ComputerName) {
    Write-Verbose "Querying $pc"
    try {
        $p = @{ ComputerName = $pc; ScriptBlock = $remote; ErrorAction = 'Stop' }
        if ($Credential) { $p.Credential = $Credential }
        $r = Invoke-Command @p
        $r | Select-Object * -ExcludeProperty PSComputerName, RunspaceId, PSShowComputerName |
             Add-Member -NotePropertyName Status -NotePropertyValue OK -PassThru
    }
    catch {
        [pscustomobject]@{ Computer = $pc; Model = $null; Serial = $null; OS = $null; Build = $null
                           FreeGB = $null; LastBoot = $null; LastUser = $null
                           Status = "ERROR: $($_.Exception.Message -replace '\\s+',' ')" }
    }
}

$results | Export-Csv -Path $OutFile -NoTypeInformation -Encoding UTF8
$ok = ($results | Where-Object Status -eq 'OK').Count
Write-Host "$ok of $($ComputerName.Count) devices answered. CSV: $OutFile"
:::

What makes it a script rather than a hack: `param` with types (so `-ComputerName` takes a list), `[CmdletBinding()]` which gives you `-Verbose` for free, the remote block returning one **object** per device, `try/catch` with `ErrorAction Stop` so a switched-off device doesn't stop the loop, and a UTF-8 CSV Excel opens straight away (add `-Delimiter ';'` if your Excel locale expects semicolons).

## 3. Run it

:::term PowerShell
$ .\\Get-DeviceInventory.ps1 -ComputerName LAPTOP-7F2K9Q, DESK-MAD-201, LAPTOP-OLD-1 -Verbose
VERBOSE: Querying LAPTOP-7F2K9Q
VERBOSE: Querying DESK-MAD-201
VERBOSE: Querying LAPTOP-OLD-1
2 of 3 devices answered. CSV: inventory-20261021.csv
$ Import-Csv .\\inventory-20261021.csv | Format-Table Computer, FreeGB, LastBoot, Status
Computer       FreeGB LastBoot            Status
--------       ------ --------            ------
LAPTOP-7F2K9Q    21.4 03/10/2026 8:12:40  OK
DESK-MAD-201    188.0 20/10/2026 7:55:02  OK
LAPTOP-OLD-1                              ERROR: Connecting to remote server LAPTOP-OLD-1 failed with the following error message : WinRM cannot complete the operation...
:::

For hundreds of devices, `Invoke-Command` takes the whole list at once and queries them in parallel (`-ThrottleLimit 32`); the loop above is slower but makes it obvious which device failed and why.

## 4. Execution policy and signing

If running it shows *"cannot be loaded because running scripts is disabled"*, that is the **execution policy**. It is not security against attackers; it is a guard against running scripts by accident.

:::term PowerShell
$ Get-ExecutionPolicy -List
        Scope ExecutionPolicy
        ----- ---------------
  MachinePolicy       Undefined
     UserPolicy       Undefined
        Process       Undefined
    CurrentUser       Undefined
   LocalMachine      Restricted
$ Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
:::

`RemoteSigned` runs what you write and requires a signature on anything downloaded. If the company pins it to `AllSigned` by GPO, the team's scripts are **signed** with a code-signing certificate from the internal CA (`Set-AuthenticodeSignature`). That is the right thing in production and fits the repository from the Git guide: only what is reviewed gets signed.

## Next steps

- Swap the device list for `Get-ADComputer -Filter {OperatingSystem -like "Windows 11*"}` and you have the inventory of the whole domain.
- Run the result through `PSScriptAnalyzer` (`Invoke-ScriptAnalyzer .\\Get-DeviceInventory.ps1`) before pushing it to the repo.
- In Level 3 you'll see Microsoft Graph from PowerShell: the same pattern, against Entra ID and Intune instead of WinRM.
""")

# ---------------------------------------------------------------- 2.11 · Red Hat Enterprise Linux
g(slug="rhel-registrar-parchear-servicios-firewall-selinux", topic="rhel", date="2026-10-21",
  title_es="Red Hat Enterprise Linux: registrar, parchear y controlar servicios, firewall y SELinux",
  title_en="Red Hat Enterprise Linux: registering, patching, and managing services, the firewall and SELinux",
  dek_es="Lo que haces en un RHEL recién entregado y lo que repites cada mes: suscripción, dnf, systemd, journalctl, firewalld y los dos comandos de SELinux que evitan desactivarlo.",
  dek_en="What you do on a freshly delivered RHEL and what you repeat every month: subscription, dnf, systemd, journalctl, firewalld, and the two SELinux commands that save you from turning it off.",
  es="""
## Qué vas a conseguir

Saber manejar un servidor RHEL (o Rocky/Alma, que son compatibles) para lo que se pide en operaciones: que esté registrado y reciba parches, que los servicios arranquen y se vigilen, que el firewall deje pasar solo lo necesario, y que SELinux siga activado aunque una aplicación proteste.

## Antes de empezar

- Acceso por SSH con un usuario que tenga `sudo`. No trabajes como `root` directamente.
- La cuenta o la clave de activación de Red Hat para registrar el sistema (la tiene quien gestione las suscripciones).
- Saber qué servicios debe dar ese servidor (web, base de datos, aplicación) y en qué puertos: es lo que decide el firewall.

## 1. Registrar y parchear

:::term bash · servidor RHEL
$ sudo subscription-manager register --org 1234567 --activationkey rhel9-servers
The system has been registered with ID: 8a1c...-...-...
$ sudo subscription-manager status
Overall Status: Current
$ sudo dnf check-update | tail -n +2 | wc -l
47
$ sudo dnf update -y
...
Complete!
$ sudo dnf needs-restarting -r
Core libraries or services have been updated since boot-up:
  * kernel
Reboot is required to fully utilize these updates.
:::

`needs-restarting -r` es lo que te dice si el parche necesita reinicio (kernel, glibc, systemd). Un servidor parcheado y sin reiniciar sigue corriendo el kernel viejo. Planifica el reinicio en la ventana de cambios y apúntalo en el ticket.

Para parchear solo seguridad (lo habitual fuera de la ventana mensual): `sudo dnf update --security -y`.

## 2. Servicios con systemd

:::term bash · servidor RHEL
$ systemctl status httpd --no-pager
● httpd.service - The Apache HTTP Server
     Loaded: loaded (/usr/lib/systemd/system/httpd.service; enabled; preset: disabled)
     Active: failed (Result: exit-code) since Wed 2026-10-21 08:02:11 CEST; 3min ago
$ sudo journalctl -u httpd -n 20 --no-pager
oct 21 08:02:11 srv-web-01 httpd[1842]: (13)Permission denied: AH00072: make_sock: could not bind to address 0.0.0.0:8081
$ sudo systemctl enable --now httpd      # activar al arranque y arrancar ahora
$ systemctl is-enabled httpd; systemctl is-active httpd
enabled
active
:::

Las cuatro órdenes que usarás todos los días: `status`, `restart`, `enable --now` y `journalctl -u <servicio>`. `journalctl -p err -b` muestra todos los errores desde el último arranque, de cualquier servicio; `journalctl -f` los sigue en vivo.

## 3. Firewall: firewalld

En RHEL el firewall es **firewalld**, con zonas y servicios con nombre. Lo que no está abierto, está cerrado.

:::term bash · servidor RHEL
$ sudo firewall-cmd --get-default-zone
public
$ sudo firewall-cmd --list-all
public (active)
  interfaces: ens192
  services: cockpit dhcpv6-client ssh
  ports:
$ sudo firewall-cmd --add-service=http --add-service=https --permanent
$ sudo firewall-cmd --add-port=8081/tcp --permanent
$ sudo firewall-cmd --reload
$ sudo firewall-cmd --list-services --list-ports
cockpit dhcpv6-client http https ssh
8081/tcp
:::

`--permanent` escribe la regla a disco; sin `--reload` no se aplica. Prueba desde fuera con `nc -zv srv-web-01 8081` o `Test-NetConnection` desde Windows. Y antes de tocar `ssh` en el firewall, ten otra sesión abierta.

## 4. SELinux: no lo desactives

El error del paso 2 (`Permission denied` al abrir el puerto 8081) no es el firewall ni los permisos del fichero: es **SELinux**, que solo permite a Apache escuchar en los puertos etiquetados como `http_port_t`. La solución correcta es decírselo, no apagarlo.

:::term bash · servidor RHEL
$ getenforce
Enforcing
$ sudo sealert -a /var/log/audit/audit.log | grep -A3 "httpd"     # instala setroubleshoot-server si no está
SELinux is preventing /usr/sbin/httpd from name_bind access on the tcp_socket port 8081.
*****  Plugin bind_ports (92.2 confidence) suggests   ************************
If you want to allow /usr/sbin/httpd to bind to network port 8081
Then you need to modify the port type.
Do: # semanage port -a -t http_port_t -p tcp 8081
$ sudo semanage port -a -t http_port_t -p tcp 8081
$ sudo systemctl restart httpd && systemctl is-active httpd
active
:::

Los dos comandos que resuelven el 90 %: `semanage port` para puertos y `restorecon -Rv /ruta` para ficheros con contexto incorrecto (los que se copiaron desde otro sitio y Apache no puede leer). Los **booleanos** (`getsebool -a | grep httpd`, `setsebool -P httpd_can_network_connect on`) cubren el resto. `setenforce 0` solo sirve para confirmar en un minuto que es SELinux; después vuelve a `1` y arregla el contexto.

## 5. Lo que miras cada mes

- `subscription-manager status` y `dnf check-update`: que sigue registrado y cuánto hay pendiente.
- `needs-restarting -r` tras parchear, y el reinicio en la ventana.
- `journalctl -p err -S "1 month ago" --no-pager | tail`: errores repetidos que nadie ha mirado.
- `df -h` y el script de la guía de Bash en cron.
- Con **Red Hat Insights** (incluido en la suscripción), los sistemas registrados aparecen en `console.redhat.com` con CVE pendientes y recomendaciones; es el informe que llevas a la reunión de parcheo.

## Siguientes pasos

- Con más de cinco servidores, el parcheo mensual se hace con **Ansible** (Nivel 3): un playbook con `dnf update` y reinicio controlado, servidor a servidor.
- Mira **Cockpit** (`https://srv-web-01:9090`): la consola web que viene con RHEL para ver servicios, logs y actualizaciones sin SSH.
- La guía de Ubuntu cubre lo mismo con `apt`, `ufw` y AppArmor: las diferencias son menos de lo que parece.
""",
  en="""
## What you'll get

Handle a RHEL server (or Rocky/Alma, which are compatible) for what operations asks of you: it is registered and receives patches, services start and are watched, the firewall lets through only what is needed, and SELinux stays on even when an application complains.

## Before you start

- SSH access with a user that has `sudo`. Don't work directly as `root`.
- The Red Hat account or activation key to register the system (whoever manages subscriptions has it).
- Know which services that server must provide (web, database, application) and on which ports: that is what decides the firewall.

## 1. Register and patch

:::term bash · RHEL server
$ sudo subscription-manager register --org 1234567 --activationkey rhel9-servers
The system has been registered with ID: 8a1c...-...-...
$ sudo subscription-manager status
Overall Status: Current
$ sudo dnf check-update | tail -n +2 | wc -l
47
$ sudo dnf update -y
...
Complete!
$ sudo dnf needs-restarting -r
Core libraries or services have been updated since boot-up:
  * kernel
Reboot is required to fully utilize these updates.
:::

`needs-restarting -r` is what tells you whether the patch needs a reboot (kernel, glibc, systemd). A patched server that has not rebooted is still running the old kernel. Schedule the reboot in the change window and note it in the ticket.

To patch security only (the usual outside the monthly window): `sudo dnf update --security -y`.

## 2. Services with systemd

:::term bash · RHEL server
$ systemctl status httpd --no-pager
● httpd.service - The Apache HTTP Server
     Loaded: loaded (/usr/lib/systemd/system/httpd.service; enabled; preset: disabled)
     Active: failed (Result: exit-code) since Wed 2026-10-21 08:02:11 CEST; 3min ago
$ sudo journalctl -u httpd -n 20 --no-pager
Oct 21 08:02:11 srv-web-01 httpd[1842]: (13)Permission denied: AH00072: make_sock: could not bind to address 0.0.0.0:8081
$ sudo systemctl enable --now httpd      # enable at boot and start now
$ systemctl is-enabled httpd; systemctl is-active httpd
enabled
active
:::

The four commands you'll use every day: `status`, `restart`, `enable --now` and `journalctl -u <service>`. `journalctl -p err -b` shows every error since the last boot, from any service; `journalctl -f` follows them live.

## 3. Firewall: firewalld

On RHEL the firewall is **firewalld**, with zones and named services. What is not open is closed.

:::term bash · RHEL server
$ sudo firewall-cmd --get-default-zone
public
$ sudo firewall-cmd --list-all
public (active)
  interfaces: ens192
  services: cockpit dhcpv6-client ssh
  ports:
$ sudo firewall-cmd --add-service=http --add-service=https --permanent
$ sudo firewall-cmd --add-port=8081/tcp --permanent
$ sudo firewall-cmd --reload
$ sudo firewall-cmd --list-services --list-ports
cockpit dhcpv6-client http https ssh
8081/tcp
:::

`--permanent` writes the rule to disk; without `--reload` it is not applied. Test from outside with `nc -zv srv-web-01 8081` or `Test-NetConnection` from Windows. And before touching `ssh` in the firewall, keep a second session open.

## 4. SELinux: don't turn it off

The error in step 2 (`Permission denied` opening port 8081) is neither the firewall nor file permissions: it is **SELinux**, which only lets Apache listen on ports labelled `http_port_t`. The right fix is to tell it, not to switch it off.

:::term bash · RHEL server
$ getenforce
Enforcing
$ sudo sealert -a /var/log/audit/audit.log | grep -A3 "httpd"     # install setroubleshoot-server if missing
SELinux is preventing /usr/sbin/httpd from name_bind access on the tcp_socket port 8081.
*****  Plugin bind_ports (92.2 confidence) suggests   ************************
If you want to allow /usr/sbin/httpd to bind to network port 8081
Then you need to modify the port type.
Do: # semanage port -a -t http_port_t -p tcp 8081
$ sudo semanage port -a -t http_port_t -p tcp 8081
$ sudo systemctl restart httpd && systemctl is-active httpd
active
:::

The two commands that solve 90%: `semanage port` for ports and `restorecon -Rv /path` for files with the wrong context (the ones copied from elsewhere that Apache can't read). **Booleans** (`getsebool -a | grep httpd`, `setsebool -P httpd_can_network_connect on`) cover the rest. `setenforce 0` is only for confirming in a minute that SELinux is the cause; then go back to `1` and fix the context.

## 5. What you look at every month

- `subscription-manager status` and `dnf check-update`: still registered, and how much is pending.
- `needs-restarting -r` after patching, and the reboot in the window.
- `journalctl -p err -S "1 month ago" --no-pager | tail`: repeated errors nobody has looked at.
- `df -h` and the script from the Bash guide in cron.
- With **Red Hat Insights** (included in the subscription), registered systems show up at `console.redhat.com` with pending CVEs and recommendations; that is the report you take to the patching meeting.

## Next steps

- With more than five servers, monthly patching is done with **Ansible** (Level 3): a playbook with `dnf update` and a controlled reboot, server by server.
- Look at **Cockpit** (`https://srv-web-01:9090`): the web console that ships with RHEL to see services, logs and updates without SSH.
- The Ubuntu guide covers the same with `apt`, `ufw` and AppArmor: the differences are smaller than they look.
""")

# ---------------------------------------------------------------- 2.12 · SharePoint
g(slug="sharepoint-sitio-de-equipo-permisos-y-uso-compartido", topic="sharepoint", date="2026-10-21",
  title_es="SharePoint Online: crear un sitio de equipo, dar permisos bien y entender el uso compartido",
  title_en="SharePoint Online: creating a team site, granting permissions properly and understanding sharing",
  dek_es="Sitio de equipo con grupo de Microsoft 365, los tres niveles de permiso, el uso compartido externo, versiones y papelera. Con PowerShell para no hacerlo a mano cien veces.",
  dek_en="A team site with a Microsoft 365 group, the three permission levels, external sharing, versioning and the recycle bin. With PowerShell so you don't do it by hand a hundred times.",
  es="""
## Qué vas a conseguir

Un sitio de SharePoint para un equipo con los permisos bien puestos desde el principio, saber por qué un usuario "no ve la carpeta" y recuperar un documento borrado o sobrescrito. Y cómo se comparte fuera de la empresa sin perder el control.

## Antes de empezar

- Rol de **Administrador de SharePoint** para crear sitios y tocar la configuración del tenant. Para administrar un sitio concreto basta con ser **propietario** del sitio.
- El módulo `Microsoft.Online.SharePoint.PowerShell` (`Install-Module -Name Microsoft.Online.SharePoint.PowerShell`) o **PnP.PowerShell** para automatizar.
- Saber si el sitio va ligado a un **equipo de Teams** (sí, casi siempre): entonces se crea desde Teams y SharePoint viene detrás.

## 1. Crear el sitio

Un **sitio de equipo** lleva un grupo de Microsoft 365 (propietarios y miembros) y un buzón; es el que quieres para un departamento o proyecto. Un **sitio de comunicación** es para publicar (intranet, noticias), sin grupo.

:::term PowerShell · SharePoint Online
$ Connect-SPOService -Url https://contoso-admin.sharepoint.com
$ New-SPOSite -Url https://contoso.sharepoint.com/sites/ventas -Title "Ventas" -Owner laura.prado@contoso.com -Template "STS#3" -StorageQuota 26214400 -LocaleId 3082
# Mejor aún: con PnP, un sitio de equipo con grupo M365 desde el principio
$ Connect-PnPOnline -Url https://contoso-admin.sharepoint.com -Interactive
$ New-PnPSite -Type TeamSite -Title "Ventas" -Alias ventas -Owners laura.prado@contoso.com -Lcid 3082
https://contoso.sharepoint.com/sites/ventas
:::

Si el equipo ya existe en Teams, el sitio ya está creado: `https://contoso.sharepoint.com/sites/<alias del equipo>`. No crees otro.

## 2. Permisos: tres grupos y nada más

Cada sitio nace con tres grupos de SharePoint: **Propietarios** (control total), **Miembros** (editar) y **Visitantes** (leer). La regla que evita el caos: los usuarios entran en esos grupos (o en el grupo de Microsoft 365, que alimenta Propietarios y Miembros), nunca con permisos directos sobre carpetas sueltas.

:::ui SharePoint · Ventas › Configuración › Permisos del sitio
= Propietarios del sitio: Laura Prado, Carlos Rey (grupo M365: propietarios)
= Miembros del sitio: GG-Ventas (34) (grupo M365: miembros)
= Visitantes del sitio: GG-Direccion (lectura)
> Configuración avanzada de permisos › Comprobar permisos
= Usuario: ana.sol@contoso.com
= Resultado: Leer · dado por · Visitantes del sitio › GG-Direccion
:::

**Comprobar permisos** es la herramienta para "no veo la carpeta": dice exactamente por qué camino tiene (o no tiene) acceso. Si una carpeta tiene **permisos únicos** (herencia rota), aparece ahí: eso es lo que hace que alguien vea el sitio pero no una carpeta concreta. Se arregla restaurando la herencia o dando acceso en esa carpeta, pero lo primero es mejor.

! "Control total" para Miembros, o un grupo de 300 personas en Propietarios, es cómo un sitio acaba con documentos borrados y nadie sabe por quién. Propietarios: dos o tres personas.

## 3. Uso compartido: lo que ve el usuario

Cuando un usuario pulsa **Compartir**, lo que puede hacer depende de la configuración del tenant y del sitio:

:::term PowerShell · SharePoint Online
$ Get-SPOTenant | Select-Object SharingCapability, DefaultSharingLinkType, RequireAnonymousLinksExpireInDays
SharingCapability                : ExternalUserSharingOnly
DefaultSharingLinkType           : Internal
RequireAnonymousLinksExpireInDays : 30
$ Get-SPOSite https://contoso.sharepoint.com/sites/ventas | Select-Object SharingCapability
SharingCapability : Disabled
$ Set-SPOSite https://contoso.sharepoint.com/sites/ventas -SharingCapability ExternalUserSharingOnly
:::

- **Disabled**: solo gente de la empresa. Lo normal para RRHH, Finanzas y dirección.
- **ExternalUserSharingOnly**: invitados que inician sesión (aparecen en Entra ID como `#EXT#`). Lo normal para proyectos con proveedores.
- **ExternalUserAndGuestSharing**: enlaces "Cualquiera" sin iniciar sesión. Solo si la política lo permite, y con caducidad.

El sitio nunca puede ser más abierto que el tenant. Si un usuario dice "no me deja compartir con el proveedor", mira primero el sitio y después el tenant.

## 4. Recuperar: versiones y papelera

- **Versiones**: en una biblioteca, botón derecho sobre el documento → **Historial de versiones** → restaurar la de antes del cambio. Está activado por defecto (500 versiones principales). Un documento "sobrescrito" casi nunca está perdido.
- **Papelera**: `Contenido del sitio → Papelera de reciclaje`, 93 días. Lo que el usuario borra pasa por ahí; lo que se vacía de ahí, pasa a la **papelera de segunda etapa** (solo administradores del sitio) hasta completar los 93 días.
- Lo borrado hace más de 93 días o un sitio entero eliminado: `Get-SPODeletedSite` y `Restore-SPODeletedSite` para sitios (93 días también); para documentos, la retención de Purview si existe. Después de eso, no hay copia que valga: SharePoint no tiene "backup" clásico, tiene retención.

## 5. Lo que preguntan en los tickets

- **"El sitio va lento o no carga"**: estado del servicio en el centro de administración de Microsoft 365 antes de nada. Si solo le pasa a uno, caché del navegador o OneDrive sincronizando una biblioteca de 200.000 ficheros (límite recomendado: 300.000 en total por usuario sincronizado).
- **"Me pide iniciar sesión todo el rato"**: Conditional Access y dispositivo no conforme, o un invitado con cuenta en dos tenants.
- **"Han desaparecido archivos"**: `Compartido conmigo`, vista con filtro, o la papelera. Casi nunca han desaparecido.

## Siguientes pasos

- Un informe mensual de sitios con uso compartido externo activo y de enlaces "Cualquiera" vivos: `Get-SPOSite -Limit All | Where-Object SharingCapability -ne Disabled`.
- Aprende las **etiquetas de confidencialidad** aplicadas a sitios: deciden el uso compartido y el acceso desde dispositivos no gestionados sin tocar cada sitio.
- En el Nivel 4 verás Purview completo: retención, DLP y las etiquetas que protegen un documento allá donde vaya.
""",
  en="""
## What you'll get

A SharePoint site for a team with permissions set properly from day one, knowing why a user "can't see the folder", and recovering a deleted or overwritten document. Plus how sharing outside the company works without losing control.

## Before you start

- The **SharePoint Administrator** role to create sites and touch tenant settings. To administer one site, being a site **owner** is enough.
- The `Microsoft.Online.SharePoint.PowerShell` module (`Install-Module -Name Microsoft.Online.SharePoint.PowerShell`) or **PnP.PowerShell** to automate.
- Know whether the site is tied to a **Teams team** (yes, almost always): then it is created from Teams and SharePoint follows.

## 1. Create the site

A **team site** carries a Microsoft 365 group (owners and members) and a mailbox; it is what you want for a department or project. A **communication site** is for publishing (intranet, news), with no group.

:::term PowerShell · SharePoint Online
$ Connect-SPOService -Url https://contoso-admin.sharepoint.com
$ New-SPOSite -Url https://contoso.sharepoint.com/sites/sales -Title "Sales" -Owner laura.prado@contoso.com -Template "STS#3" -StorageQuota 26214400 -LocaleId 1033
# Better still: with PnP, a group-connected team site from the start
$ Connect-PnPOnline -Url https://contoso-admin.sharepoint.com -Interactive
$ New-PnPSite -Type TeamSite -Title "Sales" -Alias sales -Owners laura.prado@contoso.com -Lcid 1033
https://contoso.sharepoint.com/sites/sales
:::

If the team already exists in Teams, the site is already there: `https://contoso.sharepoint.com/sites/<team alias>`. Don't create another one.

## 2. Permissions: three groups and nothing else

Every site is born with three SharePoint groups: **Owners** (full control), **Members** (edit) and **Visitors** (read). The rule that avoids chaos: users go into those groups (or into the Microsoft 365 group, which feeds Owners and Members), never with direct permissions on loose folders.

:::ui SharePoint · Sales › Settings › Site permissions
= Site owners: Laura Prado, Carlos Rey (M365 group: owners)
= Site members: GG-Sales (34) (M365 group: members)
= Site visitors: GG-Management (read)
> Advanced permissions settings › Check Permissions
= User: ana.sol@contoso.com
= Result: Read · given through · Site visitors › GG-Management
:::

**Check Permissions** is the tool for "I can't see the folder": it says exactly through which path they have (or don't have) access. If a folder has **unique permissions** (broken inheritance), it shows there: that is what makes someone see the site but not one folder. Fix it by restoring inheritance or granting access on that folder, but the first is better.

! "Full control" for Members, or a 300-person group in Owners, is how a site ends up with deleted documents and nobody knows who did it. Owners: two or three people.

## 3. Sharing: what the user sees

When a user clicks **Share**, what they can do depends on tenant and site settings:

:::term PowerShell · SharePoint Online
$ Get-SPOTenant | Select-Object SharingCapability, DefaultSharingLinkType, RequireAnonymousLinksExpireInDays
SharingCapability                : ExternalUserSharingOnly
DefaultSharingLinkType           : Internal
RequireAnonymousLinksExpireInDays : 30
$ Get-SPOSite https://contoso.sharepoint.com/sites/sales | Select-Object SharingCapability
SharingCapability : Disabled
$ Set-SPOSite https://contoso.sharepoint.com/sites/sales -SharingCapability ExternalUserSharingOnly
:::

- **Disabled**: company people only. The norm for HR, Finance and management.
- **ExternalUserSharingOnly**: guests who sign in (they appear in Entra ID as `#EXT#`). The norm for projects with vendors.
- **ExternalUserAndGuestSharing**: "Anyone" links with no sign-in. Only if policy allows it, and with expiry.

A site can never be more open than the tenant. If a user says "it won't let me share with the vendor", look at the site first and then the tenant.

## 4. Recover: versions and the recycle bin

- **Versions**: in a library, right-click the document → **Version history** → restore the one before the change. It is on by default (500 major versions). An "overwritten" document is almost never lost.
- **Recycle bin**: `Site contents → Recycle bin`, 93 days. What the user deletes goes through there; what is emptied from there goes to the **second-stage recycle bin** (site admins only) until the 93 days are up.
- Deleted more than 93 days ago, or a whole site removed: `Get-SPODeletedSite` and `Restore-SPODeletedSite` for sites (93 days too); for documents, Purview retention if it exists. After that there is no backup to fall back on: SharePoint has no classic "backup", it has retention.

## 5. What tickets ask

- **"The site is slow or won't load"**: service health in the Microsoft 365 admin centre before anything else. If only one person is affected, browser cache, or OneDrive syncing a library of 200,000 files (recommended limit: 300,000 in total per synced user).
- **"It keeps asking me to sign in"**: Conditional Access and a non-compliant device, or a guest with accounts in two tenants.
- **"Files have disappeared"**: `Shared with me`, a filtered view, or the recycle bin. They have almost never disappeared.

## Next steps

- A monthly report of sites with external sharing on and live "Anyone" links: `Get-SPOSite -Limit All | Where-Object SharingCapability -ne Disabled`.
- Learn **sensitivity labels** applied to sites: they decide sharing and access from unmanaged devices without touching each site.
- In Level 4 you'll see the whole of Purview: retention, DLP and the labels that protect a document wherever it goes.
""")

# ---------------------------------------------------------------- 2.13 · Ubuntu
g(slug="ubuntu-server-usuarios-ssh-firewall-y-actualizaciones", topic="ubuntu", date="2026-10-21",
  title_es="Ubuntu Server: los primeros 30 minutos tras la instalación",
  title_en="Ubuntu Server: the first 30 minutes after installation",
  dek_es="Usuario con sudo, SSH solo con claves, ufw, actualizaciones automáticas de seguridad, hora y nombre. Lo que convierte un Ubuntu recién instalado en un servidor que puedes dejar solo.",
  dek_en="A sudo user, SSH with keys only, ufw, automatic security updates, time and hostname. What turns a fresh Ubuntu into a server you can leave alone.",
  es="""
## Qué vas a conseguir

Un Ubuntu Server (22.04 o 24.04 LTS) endurecido lo justo para producción: nadie entra por contraseña, el firewall solo abre lo que das de alta, los parches de seguridad se instalan solos y el sistema tiene nombre y hora correctos. Treinta minutos que te ahorran un incidente.

## Antes de empezar

- Acceso a la consola (hipervisor o KVM) o por SSH al usuario creado en la instalación.
- Tu **clave pública SSH** (`~/.ssh/id_ed25519.pub` en tu equipo; si no la tienes, `ssh-keygen -t ed25519`).
- Decidido con el equipo: nombre del servidor, qué servicios dará y qué puertos abrir.

## 1. Nombre, hora y actualización inicial

:::term bash · servidor Ubuntu
$ sudo hostnamectl set-hostname srv-app-02
$ sudo timedatectl set-timezone Europe/Madrid
$ timedatectl | grep -E "Time zone|synchronized"
                Time zone: Europe/Madrid (CEST, +0200)
System clock synchronized: yes
$ sudo apt update && sudo apt full-upgrade -y
$ [ -f /var/run/reboot-required ] && echo "Reinicio necesario"
Reinicio necesario
$ sudo reboot
:::

`timedatectl` tiene que decir `synchronized: yes` (Ubuntu usa `systemd-timesyncd`). Un servidor con la hora mal falla en certificados, en Kerberos y en los logs correlacionados con el resto.

## 2. Usuario de administración y sudo

Un usuario por persona, nunca una cuenta compartida. `root` sin contraseña y sin acceso por SSH.

:::term bash · servidor Ubuntu
$ sudo adduser laura
$ sudo usermod -aG sudo laura
$ sudo mkdir -p /home/laura/.ssh && sudo chmod 700 /home/laura/.ssh
$ echo "ssh-ed25519 AAAAC3Nza...  laura@laptop" | sudo tee /home/laura/.ssh/authorized_keys
$ sudo chmod 600 /home/laura/.ssh/authorized_keys && sudo chown -R laura:laura /home/laura/.ssh
# Probar desde tu equipo, en OTRA ventana, antes de seguir:
#   ssh laura@srv-app-02   → debe entrar sin pedir contraseña
:::

## 3. SSH solo con claves

:::term bash · servidor Ubuntu
$ sudo nano /etc/ssh/sshd_config.d/10-hardening.conf
PasswordAuthentication no
PermitRootLogin no
KbdInteractiveAuthentication no
MaxAuthTries 3
$ sudo sshd -t && sudo systemctl reload ssh
$ sudo sshd -T | grep -E "^(passwordauthentication|permitrootlogin)"
passwordauthentication no
permitrootlogin no
:::

`sshd -t` comprueba la sintaxis antes de recargar: un error aquí con la sesión cerrada es un viaje a la consola. Y la regla de oro: **no cierres la sesión actual** hasta haber entrado con otra usando solo la clave.

! Los ficheros en `/etc/ssh/sshd_config.d/` se cargan antes que `sshd_config` y la primera aparición de cada opción gana. Si Ubuntu ya trae ahí un `50-cloud-init.conf` con `PasswordAuthentication yes`, tu fichero `10-…` lo adelanta por orden alfabético.

## 4. Firewall con ufw

:::term bash · servidor Ubuntu
$ sudo ufw default deny incoming
$ sudo ufw default allow outgoing
$ sudo ufw allow from 10.20.0.0/16 to any port 22 proto tcp comment "SSH desde la red de IT"
$ sudo ufw allow 443/tcp comment "HTTPS app"
$ sudo ufw enable
Firewall is active and enabled on system startup
$ sudo ufw status numbered
     To                         Action      From
     --                         ------      ----
[ 1] 22/tcp                     ALLOW IN    10.20.0.0/16    # SSH desde la red de IT
[ 2] 443/tcp                    ALLOW IN    Anywhere        # HTTPS app
:::

`ufw` es una capa sobre `nftables`; lo que no está en la lista no entra. Limitar SSH a la red de administración o a la VPN es la medida que más ataques automáticos quita de los logs.

## 5. Actualizaciones de seguridad automáticas

:::term bash · servidor Ubuntu
$ sudo apt install -y unattended-upgrades
$ sudo dpkg-reconfigure -plow unattended-upgrades    # responde Sí
$ sudo nano /etc/apt/apt.conf.d/50unattended-upgrades
Unattended-Upgrade::Allowed-Origins {
        "${distro_id}:${distro_codename}-security";
};
Unattended-Upgrade::Automatic-Reboot "false";
Unattended-Upgrade::Mail "it@contoso.com";
$ sudo unattended-upgrade --dry-run --debug 2>&1 | tail -n 3
:::

Solo el origen `-security`: los parches de seguridad entran solos cada noche, el resto (y los reinicios) se hacen en la ventana de cambios con `apt full-upgrade`. `/var/log/unattended-upgrades/` guarda lo que instaló cada noche.

## 6. Comprobación final

:::term bash · servidor Ubuntu
$ hostnamectl --static; timedatectl show -p NTPSynchronized --value
srv-app-02
yes
$ sudo ss -tlnp | awk 'NR==1 || /LISTEN/' | awk '{print $4, $7}'
Local Address:Port Process
0.0.0.0:22 users:(("sshd",pid=812,fd=3))
0.0.0.0:443 users:(("nginx",pid=1204,fd=6))
$ sudo ufw status | head -n 1; systemctl is-active unattended-upgrades
Status: active
active
$ sudo journalctl -p err -b --no-pager | tail -n 5
:::

`ss -tlnp` es la lista de lo que escucha: si hay algo que no esperas (una base de datos en `0.0.0.0`, un panel de administración), o se cierra o se limita a `127.0.0.1`.

## Siguientes pasos

- Instala el script de comprobación de la guía de Bash en cron, y **fail2ban** si SSH tiene que estar expuesto.
- Para más de un servidor, la secuencia entera de esta guía es un playbook de Ansible de 40 líneas (Nivel 3).
- **Ubuntu Landscape** (Nivel 3) hace el inventario, el parcheo y los informes de toda la flota desde una consola.
""",
  en="""
## What you'll get

An Ubuntu Server (22.04 or 24.04 LTS) hardened just enough for production: nobody gets in with a password, the firewall opens only what you register, security patches install themselves, and the system has the right name and time. Thirty minutes that save you an incident.

## Before you start

- Console access (hypervisor or KVM) or SSH to the user created at install time.
- Your **SSH public key** (`~/.ssh/id_ed25519.pub` on your device; if you don't have one, `ssh-keygen -t ed25519`).
- Agreed with the team: server name, which services it will provide and which ports to open.

## 1. Name, time and first update

:::term bash · Ubuntu server
$ sudo hostnamectl set-hostname srv-app-02
$ sudo timedatectl set-timezone Europe/Madrid
$ timedatectl | grep -E "Time zone|synchronized"
                Time zone: Europe/Madrid (CEST, +0200)
System clock synchronized: yes
$ sudo apt update && sudo apt full-upgrade -y
$ [ -f /var/run/reboot-required ] && echo "Reboot required"
Reboot required
$ sudo reboot
:::

`timedatectl` has to say `synchronized: yes` (Ubuntu uses `systemd-timesyncd`). A server with the wrong time fails on certificates, on Kerberos, and in logs correlated with everything else.

## 2. Admin user and sudo

One user per person, never a shared account. `root` with no password and no SSH access.

:::term bash · Ubuntu server
$ sudo adduser laura
$ sudo usermod -aG sudo laura
$ sudo mkdir -p /home/laura/.ssh && sudo chmod 700 /home/laura/.ssh
$ echo "ssh-ed25519 AAAAC3Nza...  laura@laptop" | sudo tee /home/laura/.ssh/authorized_keys
$ sudo chmod 600 /home/laura/.ssh/authorized_keys && sudo chown -R laura:laura /home/laura/.ssh
# Test from your device, in ANOTHER window, before going on:
#   ssh laura@srv-app-02   → must log in without asking for a password
:::

## 3. SSH with keys only

:::term bash · Ubuntu server
$ sudo nano /etc/ssh/sshd_config.d/10-hardening.conf
PasswordAuthentication no
PermitRootLogin no
KbdInteractiveAuthentication no
MaxAuthTries 3
$ sudo sshd -t && sudo systemctl reload ssh
$ sudo sshd -T | grep -E "^(passwordauthentication|permitrootlogin)"
passwordauthentication no
permitrootlogin no
:::

`sshd -t` checks the syntax before reloading: a mistake here with the session closed means a trip to the console. And the golden rule: **don't close the current session** until you have logged in with another one using only the key.

! Files in `/etc/ssh/sshd_config.d/` load before `sshd_config` and the first occurrence of each option wins. If Ubuntu already ships a `50-cloud-init.conf` there with `PasswordAuthentication yes`, your `10-…` file overrides it by alphabetical order.

## 4. Firewall with ufw

:::term bash · Ubuntu server
$ sudo ufw default deny incoming
$ sudo ufw default allow outgoing
$ sudo ufw allow from 10.20.0.0/16 to any port 22 proto tcp comment "SSH from the IT network"
$ sudo ufw allow 443/tcp comment "HTTPS app"
$ sudo ufw enable
Firewall is active and enabled on system startup
$ sudo ufw status numbered
     To                         Action      From
     --                         ------      ----
[ 1] 22/tcp                     ALLOW IN    10.20.0.0/16    # SSH from the IT network
[ 2] 443/tcp                    ALLOW IN    Anywhere        # HTTPS app
:::

`ufw` is a layer over `nftables`; what is not on the list does not get in. Limiting SSH to the admin network or the VPN is the measure that removes the most automated attacks from the logs.

## 5. Automatic security updates

:::term bash · Ubuntu server
$ sudo apt install -y unattended-upgrades
$ sudo dpkg-reconfigure -plow unattended-upgrades    # answer Yes
$ sudo nano /etc/apt/apt.conf.d/50unattended-upgrades
Unattended-Upgrade::Allowed-Origins {
        "${distro_id}:${distro_codename}-security";
};
Unattended-Upgrade::Automatic-Reboot "false";
Unattended-Upgrade::Mail "it@contoso.com";
$ sudo unattended-upgrade --dry-run --debug 2>&1 | tail -n 3
:::

Only the `-security` origin: security patches install themselves every night, the rest (and reboots) happen in the change window with `apt full-upgrade`. `/var/log/unattended-upgrades/` keeps what was installed each night.

## 6. Final check

:::term bash · Ubuntu server
$ hostnamectl --static; timedatectl show -p NTPSynchronized --value
srv-app-02
yes
$ sudo ss -tlnp | awk 'NR==1 || /LISTEN/' | awk '{print $4, $7}'
Local Address:Port Process
0.0.0.0:22 users:(("sshd",pid=812,fd=3))
0.0.0.0:443 users:(("nginx",pid=1204,fd=6))
$ sudo ufw status | head -n 1; systemctl is-active unattended-upgrades
Status: active
active
$ sudo journalctl -p err -b --no-pager | tail -n 5
:::

`ss -tlnp` is the list of what is listening: if there is something you don't expect (a database on `0.0.0.0`, an admin panel), either close it or bind it to `127.0.0.1`.

## Next steps

- Install the check script from the Bash guide in cron, and **fail2ban** if SSH has to be exposed.
- For more than one server, the whole sequence in this guide is a 40-line Ansible playbook (Level 3).
- **Ubuntu Landscape** (Level 3) does inventory, patching and reports for the whole fleet from one console.
""")

# ---------------------------------------------------------------- 2.14 · Veeam Backup
g(slug="veeam-crear-un-job-comprobar-copias-y-restaurar", topic="veeam", date="2026-10-21",
  title_es="Veeam Backup: crear un trabajo, comprobar que termina bien y hacer una restauración de prueba",
  title_en="Veeam Backup: creating a job, checking it completes, and running a test restore",
  dek_es="Repositorio, trabajo de copia con retención, los avisos que no hay que ignorar, y la restauración de un fichero y de una máquina entera. Porque una copia sin restaurar no es una copia.",
  dek_en="Repository, backup job with retention, the warnings you must not ignore, and restoring a file and a whole machine. Because a backup you never restored is not a backup.",
  es="""
## Qué vas a conseguir

Un trabajo de copia en Veeam Backup & Replication que protege las máquinas virtuales de un servicio, con retención definida, y la rutina que de verdad importa: leer el resultado cada mañana y restaurar algo cada mes para saber que funciona.

## Antes de empezar

- Acceso a la consola de Veeam con rol **Backup Administrator** (o **Backup Operator** para restaurar sin cambiar trabajos).
- El hipervisor añadido en **Inventory** (vCenter o Hyper-V) con una cuenta de solo lectura más los permisos de snapshot que Veeam documenta.
- Un **repositorio** con espacio: como regla, 2-3 veces el tamaño de los datos protegidos para dos semanas de retención con incrementales.
- Para el **3-2-1**: una segunda copia fuera (otro sitio, cinta o nube) planificada como *Backup Copy Job*; esta guía monta la primera.

## 1. El trabajo de copia

:::ui Veeam Backup & Replication · Home › Jobs › Backup › Virtual machine
= Name: BKP-APP-ERP (diario)
> Virtual Machines › Add › vCenter › Carpeta "ERP" (3 VMs: erp-app-01, erp-db-01, erp-web-01)
> Storage
= Backup repository: REPO-NAS-01 (libre: 9,2 TB)
= Retention policy: 14 restore points
= [x] Keep certain full backups longer for archival purposes: Weekly 4 · Monthly 3
> Advanced › Backup › Incremental (recommended) · [x] Create synthetic full backups periodically: Saturday
> Guest Processing › [x] Enable application-aware processing (cuenta de dominio con admin local en las VMs)
> Schedule › [x] Run the job automatically · Daily at 22:00 · Retry 3 times every 10 minutes
[Finish]
:::

Dos decisiones que importan: **application-aware processing** para la VM de base de datos (hace la copia consistente con VSS y trunca los logs de SQL si lo configuras), y la **retención** acordada con negocio, no inventada: 14 puntos diarios + 4 semanales + 3 mensuales cubre "lo que había hace tres meses".

> Un **job por servicio**, no uno gigante. Así un fallo en una VM no deja sin copia a otras, y el informe de la mañana dice qué servicio está sin proteger.

## 2. Leer el resultado cada mañana

El correo de Veeam (o el panel **Home → Last 24 hours**) tiene tres colores y hay que mirar los tres:

:::ui Veeam · Home › Last 24 Hours
= BKP-APP-ERP · Success · 3 of 3 VMs · 21/10/2026 22:00 · 00:41:12 · Transferred 38,4 GB
= BKP-FILES · Warning · 1 of 1 VMs · 21/10/2026 23:00 · 01:55:08
> Warning › srv-files-01: Unable to truncate transaction logs. Details: Failed to call RPC function 'VssFreezeSnapshot'
= BKP-INFRA · Failed · 2 of 3 VMs · 22/10/2026 01:00
> Error › dc-02: Error: VM is disconnected from the host or powered off (object not found)
:::

- **Success**: todo bien. Aun así, mira el tamaño transferido: un incremental que de repente pesa como un full suele ser un cambio masivo (actualización, cifrado por ransomware, un disco añadido).
- **Warning**: la copia existe pero algo no fue como debía. El de VSS de arriba es el más frecuente: la cuenta de guest processing no tiene permisos, o el servicio VSS en la VM está roto. No se ignora dos días seguidos.
- **Failed**: esa VM no tiene copia de hoy. `dc-02` ha desaparecido del inventario (borrada, migrada a otro clúster, renombrada): hay que actualizar el job y lanzar un **Retry**.

El informe que llevas a la reunión semanal: **Reports → Backup Job Reports** o, mejor, **Veeam ONE** si está instalado, con el porcentaje de éxito por job y las VMs sin copia en 7 días.

## 3. Restaurar un fichero

:::ui Veeam · Home › Backups › Disk › BKP-FILES › srv-files-01 › Restore guest files › Microsoft Windows
> Restore point: 21/10/2026 23:00 (incremental)
> Backup Browser › C: › Shares › Ventas › Ofertas › Oferta-1021.xlsx
= Tamaño: 412 KB · Modificado: 20/10/2026 17:40
[Restore › Keep (restaura junto al original con sufijo RESTORED-)] [Copy To…]
:::

**Keep** deja el original y añade la versión restaurada al lado; **Overwrite** pisa el actual. Para un usuario que ha borrado o sobrescrito un fichero, **Copy To** una carpeta tuya y entregárselo es lo más seguro. Todo el proceso tarda minutos y no toca la VM.

## 4. Restaurar una máquina entera (la prueba mensual)

Una vez al mes, restaura una VM en un **entorno aislado** y comprueba que arranca y que la aplicación responde. Es lo único que demuestra que la copia sirve.

:::ui Veeam · Home › Backups › BKP-APP-ERP › erp-web-01 › Restore entire VM
> Restore point: 20/10/2026 22:00
> Restore mode: Restore to a new location, or with different settings
= Name: erp-web-01_RESTORETEST
= Host: esx-test-01 · Datastore: DS-TEST · Network: VLAN-AISLADA (sin salida a producción)
= [ ] Power on target VM after restoring   (arráncala tú, con la red aislada confirmada)
[Finish]
= Resultado: Restore completed successfully · 00:23:40
:::

Con **SureBackup** (Veeam lo automatiza) la prueba se programa y el informe dice cada semana si cada VM arranca. Sin SureBackup, la prueba manual con una VM distinta cada mes y una línea en el ticket de cambios es suficiente, y es lo que piden las auditorías.

! Restaurar una VM **en producción con la misma red y el mismo nombre** mientras la original está encendida provoca un conflicto de IP y de identidad en el dominio. Siempre a red aislada o con la original apagada.

## 5. Qué poner en el ticket

Nombre del job, VM, punto de restauración usado, dónde se restauró, cuánto tardó y la comprobación hecha (fichero abierto, aplicación responde). Esa línea es la evidencia del DR/BCP.

## Siguientes pasos

- Monta el **Backup Copy Job** a un segundo repositorio (otro sitio, S3 con inmutabilidad, cinta): sin él no hay 3-2-1.
- Activa la **inmutabilidad** en el repositorio si lo soporta (Linux hardened repository u object lock): es lo que salva la copia en un ransomware.
- En el Nivel 4 verás DR/BCP de principio a fin: planes, pruebas de recuperación completas y los tiempos (RPO/RTO) que negocias con cada servicio.
""",
  en="""
## What you'll get

A backup job in Veeam Backup & Replication that protects a service's virtual machines, with defined retention, and the routine that really matters: reading the result every morning and restoring something every month to know it works.

## Before you start

- Access to the Veeam console with the **Backup Administrator** role (or **Backup Operator** to restore without changing jobs).
- The hypervisor added in **Inventory** (vCenter or Hyper-V) with a read-only account plus the snapshot permissions Veeam documents.
- A **repository** with space: as a rule, 2-3 times the size of the protected data for two weeks of retention with incrementals.
- For **3-2-1**: a second copy elsewhere (another site, tape or cloud) planned as a *Backup Copy Job*; this guide sets up the first one.

## 1. The backup job

:::ui Veeam Backup & Replication · Home › Jobs › Backup › Virtual machine
= Name: BKP-APP-ERP (daily)
> Virtual Machines › Add › vCenter › Folder "ERP" (3 VMs: erp-app-01, erp-db-01, erp-web-01)
> Storage
= Backup repository: REPO-NAS-01 (free: 9.2 TB)
= Retention policy: 14 restore points
= [x] Keep certain full backups longer for archival purposes: Weekly 4 · Monthly 3
> Advanced › Backup › Incremental (recommended) · [x] Create synthetic full backups periodically: Saturday
> Guest Processing › [x] Enable application-aware processing (domain account with local admin on the VMs)
> Schedule › [x] Run the job automatically · Daily at 22:00 · Retry 3 times every 10 minutes
[Finish]
:::

Two decisions that matter: **application-aware processing** for the database VM (makes the backup VSS-consistent and truncates SQL logs if you configure it), and **retention** agreed with the business, not invented: 14 daily points + 4 weekly + 3 monthly covers "what we had three months ago".

> One **job per service**, not one giant job. That way a failure on one VM does not leave others unprotected, and the morning report says which service is uncovered.

## 2. Read the result every morning

Veeam's email (or the **Home → Last 24 hours** panel) has three colours and you have to look at all three:

:::ui Veeam · Home › Last 24 Hours
= BKP-APP-ERP · Success · 3 of 3 VMs · 21/10/2026 22:00 · 00:41:12 · Transferred 38.4 GB
= BKP-FILES · Warning · 1 of 1 VMs · 21/10/2026 23:00 · 01:55:08
> Warning › srv-files-01: Unable to truncate transaction logs. Details: Failed to call RPC function 'VssFreezeSnapshot'
= BKP-INFRA · Failed · 2 of 3 VMs · 22/10/2026 01:00
> Error › dc-02: Error: VM is disconnected from the host or powered off (object not found)
:::

- **Success**: all good. Still, look at the transferred size: an incremental that suddenly weighs as much as a full is usually a massive change (an update, ransomware encryption, a disk added).
- **Warning**: the backup exists but something did not go as it should. The VSS one above is the most frequent: the guest processing account lacks permissions, or the VSS service inside the VM is broken. Not to be ignored two days running.
- **Failed**: that VM has no backup for today. `dc-02` has vanished from the inventory (deleted, migrated to another cluster, renamed): update the job and launch a **Retry**.

The report you take to the weekly meeting: **Reports → Backup Job Reports** or, better, **Veeam ONE** if installed, with success rate per job and VMs with no backup in 7 days.

## 3. Restore a file

:::ui Veeam · Home › Backups › Disk › BKP-FILES › srv-files-01 › Restore guest files › Microsoft Windows
> Restore point: 21/10/2026 23:00 (incremental)
> Backup Browser › C: › Shares › Sales › Quotes › Quote-1021.xlsx
= Size: 412 KB · Modified: 20/10/2026 17:40
[Restore › Keep (restores next to the original with a RESTORED- suffix)] [Copy To…]
:::

**Keep** leaves the original and adds the restored version beside it; **Overwrite** replaces the current one. For a user who deleted or overwrote a file, **Copy To** a folder of yours and handing it over is the safest. The whole thing takes minutes and does not touch the VM.

## 4. Restore a whole machine (the monthly test)

Once a month, restore a VM into an **isolated environment** and check that it boots and the application responds. It is the only thing that proves the backup is any good.

:::ui Veeam · Home › Backups › BKP-APP-ERP › erp-web-01 › Restore entire VM
> Restore point: 20/10/2026 22:00
> Restore mode: Restore to a new location, or with different settings
= Name: erp-web-01_RESTORETEST
= Host: esx-test-01 · Datastore: DS-TEST · Network: VLAN-ISOLATED (no route to production)
= [ ] Power on target VM after restoring   (power it on yourself, once the isolated network is confirmed)
[Finish]
= Result: Restore completed successfully · 00:23:40
:::

With **SureBackup** (Veeam automates it) the test is scheduled and the report says every week whether each VM boots. Without SureBackup, a manual test with a different VM every month and a line in the change ticket is enough, and it is what audits ask for.

! Restoring a VM **into production with the same network and name** while the original is running causes an IP and domain identity conflict. Always to an isolated network, or with the original switched off.

## 5. What to put in the ticket

Job name, VM, restore point used, where it was restored, how long it took and the check performed (file opened, application responds). That line is the DR/BCP evidence.

## Next steps

- Set up the **Backup Copy Job** to a second repository (another site, S3 with immutability, tape): without it there is no 3-2-1.
- Enable **immutability** on the repository if it supports it (Linux hardened repository or object lock): it is what saves the backup in a ransomware event.
- In Level 4 you'll see DR/BCP end to end: plans, full recovery tests and the times (RPO/RTO) you negotiate with each service.
""")

# ---------------------------------------------------------------- 2.15 · VMware Horizon
g(slug="vmware-horizon-pool-de-escritorios-y-conexion-que-falla", topic="vmware-horizon", date="2026-10-21",
  title_es="VMware Horizon: un pool de escritorios desde una imagen maestra y la conexión que falla",
  title_en="VMware Horizon: a desktop pool from a golden image, and the connection that fails",
  dek_es="Imagen maestra con el agente, pool de clones instantáneos, asignación a un grupo, y el orden para diagnosticar 'el escritorio no conecta' con Horizon Console y los logs del cliente.",
  dek_en="Golden image with the agent, an instant-clone pool, entitlement to a group, and the order for diagnosing 'the desktop won't connect' with Horizon Console and the client logs.",
  es="""
## Qué vas a conseguir

Un pool de escritorios virtuales en VMware Horizon (ahora bajo Omnissa) que se crea desde una imagen maestra, se asigna a un grupo de Active Directory y se recrea limpio en cada sesión. Y un método fijo para el ticket "me conecto y se queda en negro" o "no aparece mi escritorio".

## Antes de empezar

- Acceso a **Horizon Console** (`https://horizon-cs-01.contoso.local/admin`) con rol de administrador o de help desk.
- vCenter añadido en **Settings → Servers** con la cuenta de servicio que Horizon documenta, y un **Connection Server** sano.
- Una VM de Windows 11 Enterprise preparada como **imagen maestra**: unida al dominio, optimizada (OS Optimization Tool), con **Horizon Agent** instalado y las aplicaciones base. Apagada y con una **snapshot** con nombre y fecha.
- Un grupo de AD con los usuarios del pool (`GG-VDI-Finanzas`).

## 1. Las piezas (y su equivalente en Citrix)

- **Connection Server**: el broker; los clientes se autentican aquí (equivale al Delivery Controller).
- **Horizon Agent** en la VM: lo que hace que el escritorio sea gestionable (el VDA).
- **Pool**: el conjunto de escritorios y su política (grupo de entrega + catálogo).
- **Entitlement**: qué usuarios o grupos ven el pool.
- **Protocolo**: **Blast Extreme** (el de Horizon, puerto 8443/22443) o PCoIP (4172). El cliente es **Horizon Client**.

## 2. Crear un pool de clones instantáneos

:::ui Horizon Console · Inventory › Desktops › Add
= Type: Automated Desktop Pool · vCenter Server · Instant Clone
= User Assignment: Floating
= ID: POOL-FIN-W11 · Display name: Finanzas (Windows 11)
> vCenter Settings
= Golden image: /DC-MAD/vm/Templates/W11-GOLD-FIN · Snapshot: 2026-10-20_agent-2406_office
= VM folder: /VDI/Finanzas · Cluster: CL-VDI-01 · Datastore: DS-VDI-FLASH-01
> Provisioning
= Naming pattern: FIN-W11-{n:fixed=3} · Max machines: 40 · Spare (powered on): 5
> Desktop Pool Settings
= Remote display protocol: VMware Blast · Allow users to choose: No
= [x] Refresh OS disk after logoff: Always
> Guest Customization
= Domain: contoso.local · AD container: OU=VDI,OU=Equipos
[Submit]
:::

Clones instantáneos: cada escritorio se crea en segundos a partir de la snapshot y se **destruye al cerrar sesión**. Un usuario arranca siempre limpio; lo que tiene que persistir (perfil, datos) va en FSLogix o en un perfil de DEM, nunca en el escritorio.

Después: **Entitlements → Add entitlement → GG-VDI-Finanzas**. Hasta que no hay entitlement, el pool existe pero nadie lo ve.

## 3. Comprobar que está sano

:::ui Horizon Console · Inventory › Desktops › POOL-FIN-W11 › Machines
= FIN-W11-001 · Available · Agent 2406 · Last connected: laura.prado 21/10/2026 09:12
= FIN-W11-002 · Connected · laura.prado · Blast · 21/10/2026 10:05
= FIN-W11-003 · Agent unreachable · (tombstoned)
= FIN-W11-004 · Provisioning · 48%
= FIN-W11-005 · Available
> Dashboard › System Health › Connection Servers: 2/2 OK · vCenter: OK · Domains: contoso.local OK
:::

**Available** y **Connected** son los estados buenos. **Agent unreachable** es un escritorio cuyo agente no habla con el Connection Server (red, DNS, hora, o clon a medias): con clones instantáneos, se **recrea** (Machines → la máquina → Remove, el pool crea otra). **Provisioning** atascado largo rato suele ser vCenter o el datastore lleno.

## 4. "No conecta": el orden

1. **¿Ve el pool en Horizon Client?** Si no: entitlement (el usuario no está en el grupo o el grupo no está en el pool) o el pool está deshabilitado. Comprueba `Users and Groups → el usuario → Entitlements`.
2. **¿Se queda en "Connecting…" o pantalla negra?** El cliente ha llegado al Connection Server pero no al escritorio. Hace falta el puerto **8443/22443 (Blast)** desde el cliente hasta la **VM del escritorio** (no solo al broker) cuando se conecta por túnel desactivado, o hasta el **Unified Access Gateway** si viene de internet. `Test-NetConnection FIN-W11-002 -Port 22443` desde el equipo del usuario lo dice.
3. **¿Conecta y a los segundos se cierra?** El escritorio está asignado pero el inicio de sesión falla: perfil de FSLogix bloqueado (otro escritorio tiene el contenedor abierto; se ve en el log de FSLogix `C:\\ProgramData\\FSLogix\\Logs`), o la GPO de inicio tarda más que el tiempo de espera.
4. **¿Le toca siempre la misma máquina rota?** En pools flotantes, Horizon reintenta la última; **Reset** o **Remove** de esa máquina desde la consola y que vuelva a entrar.

Logs del cliente cuando hay que escalar: en Windows, `%LOCALAPPDATA%\\VMware\\VDM\\Logs\\` (`vmware-horizon-client-*.log`); en el escritorio, `C:\\ProgramData\\VMware\\VDM\\logs\\` (`debug-*.txt` del agente). Horizon Console → **Help Desk** (con el usuario) resume sesión, protocolo, latencia y los eventos de inicio de sesión en una pantalla: es por donde empieza el soporte de primer nivel.

## 5. Actualizar la imagen maestra

Cambiar algo en el pool (parche, aplicación nueva) es: encender la imagen maestra, hacer el cambio, apagarla, **nueva snapshot** con fecha, y en el pool **Maintain → Push Image** eligiendo esa snapshot y cuándo (al cerrar sesión cada usuario, o forzado en una ventana). Nunca se toca un escritorio del pool a mano: desaparece en el siguiente cierre de sesión.

! Antes del Push Image, prueba la snapshot nueva en un **pool de prueba** de 2 máquinas. Una imagen con el agente mal instalado deja los 40 escritorios en *Agent unreachable* a la vez.

## Siguientes pasos

- Monta **FSLogix** para los perfiles si no está: es lo que hace que un escritorio flotante parezca el del usuario.
- Un **Unified Access Gateway** en la DMZ para el acceso desde fuera sin VPN; y en el Nivel 4, **Azure Virtual Desktop y Windows 365**, la alternativa en nube.
- La guía de Citrix VDI es el espejo de esta: mismos problemas, otros nombres. Conocer las dos te sitúa en cualquier empresa.
""",
  en="""
## What you'll get

A virtual desktop pool in VMware Horizon (now under Omnissa) created from a golden image, entitled to an Active Directory group and rebuilt clean on every session. And a fixed method for the ticket "I connect and it stays black" or "my desktop doesn't appear".

## Before you start

- Access to **Horizon Console** (`https://horizon-cs-01.contoso.local/admin`) with an administrator or help desk role.
- vCenter added under **Settings → Servers** with the service account Horizon documents, and a healthy **Connection Server**.
- A Windows 11 Enterprise VM prepared as the **golden image**: domain-joined, optimised (OS Optimization Tool), with **Horizon Agent** installed and the base applications. Powered off, with a **snapshot** named and dated.
- An AD group with the pool's users (`GG-VDI-Finance`).

## 1. The pieces (and their Citrix equivalent)

- **Connection Server**: the broker; clients authenticate here (equivalent to the Delivery Controller).
- **Horizon Agent** on the VM: what makes the desktop manageable (the VDA).
- **Pool**: the set of desktops and their policy (delivery group + catalog).
- **Entitlement**: which users or groups see the pool.
- **Protocol**: **Blast Extreme** (Horizon's own, port 8443/22443) or PCoIP (4172). The client is **Horizon Client**.

## 2. Create an instant-clone pool

:::ui Horizon Console · Inventory › Desktops › Add
= Type: Automated Desktop Pool · vCenter Server · Instant Clone
= User Assignment: Floating
= ID: POOL-FIN-W11 · Display name: Finance (Windows 11)
> vCenter Settings
= Golden image: /DC-MAD/vm/Templates/W11-GOLD-FIN · Snapshot: 2026-10-20_agent-2406_office
= VM folder: /VDI/Finance · Cluster: CL-VDI-01 · Datastore: DS-VDI-FLASH-01
> Provisioning
= Naming pattern: FIN-W11-{n:fixed=3} · Max machines: 40 · Spare (powered on): 5
> Desktop Pool Settings
= Remote display protocol: VMware Blast · Allow users to choose: No
= [x] Refresh OS disk after logoff: Always
> Guest Customization
= Domain: contoso.local · AD container: OU=VDI,OU=Computers
[Submit]
:::

Instant clones: each desktop is created in seconds from the snapshot and **destroyed at logoff**. A user always starts clean; whatever must persist (profile, data) lives in FSLogix or a DEM profile, never on the desktop.

Then: **Entitlements → Add entitlement → GG-VDI-Finance**. Until there is an entitlement, the pool exists but nobody sees it.

## 3. Check that it is healthy

:::ui Horizon Console · Inventory › Desktops › POOL-FIN-W11 › Machines
= FIN-W11-001 · Available · Agent 2406 · Last connected: laura.prado 21/10/2026 09:12
= FIN-W11-002 · Connected · laura.prado · Blast · 21/10/2026 10:05
= FIN-W11-003 · Agent unreachable · (tombstoned)
= FIN-W11-004 · Provisioning · 48%
= FIN-W11-005 · Available
> Dashboard › System Health › Connection Servers: 2/2 OK · vCenter: OK · Domains: contoso.local OK
:::

**Available** and **Connected** are the good states. **Agent unreachable** is a desktop whose agent is not talking to the Connection Server (network, DNS, time, or a half-made clone): with instant clones, you **rebuild** it (Machines → the machine → Remove, the pool creates another). **Provisioning** stuck for a long time is usually vCenter or a full datastore.

## 4. "It won't connect": the order

1. **Can they see the pool in Horizon Client?** If not: entitlement (the user is not in the group, or the group is not on the pool) or the pool is disabled. Check `Users and Groups → the user → Entitlements`.
2. **Stuck on "Connecting…" or a black screen?** The client reached the Connection Server but not the desktop. Port **8443/22443 (Blast)** is needed from the client to the **desktop VM** (not just the broker) when tunnelling is off, or to the **Unified Access Gateway** when coming from the internet. `Test-NetConnection FIN-W11-002 -Port 22443` from the user's device tells you.
3. **Connects and closes after a few seconds?** The desktop is assigned but logon fails: a locked FSLogix profile (another desktop has the container open; visible in the FSLogix log `C:\\ProgramData\\FSLogix\\Logs`), or the logon GPO takes longer than the timeout.
4. **Always lands on the same broken machine?** In floating pools, Horizon retries the last one; **Reset** or **Remove** that machine from the console and have them log in again.

Client logs when escalating: on Windows, `%LOCALAPPDATA%\\VMware\\VDM\\Logs\\` (`vmware-horizon-client-*.log`); on the desktop, `C:\\ProgramData\\VMware\\VDM\\logs\\` (the agent's `debug-*.txt`). Horizon Console → **Help Desk** (with the user) summarises session, protocol, latency and logon events on one screen: that is where first-line support starts.

## 5. Update the golden image

Changing something in the pool (a patch, a new application) means: power on the golden image, make the change, power it off, **new snapshot** with a date, and on the pool **Maintain → Push Image** choosing that snapshot and when (as each user logs off, or forced in a window). Never touch a pool desktop by hand: it vanishes at the next logoff.

! Before the Push Image, test the new snapshot on a 2-machine **test pool**. An image with the agent badly installed leaves all 40 desktops in *Agent unreachable* at once.

## Next steps

- Set up **FSLogix** for profiles if it is not there: it is what makes a floating desktop feel like the user's own.
- A **Unified Access Gateway** in the DMZ for access from outside without VPN; and in Level 4, **Azure Virtual Desktop and Windows 365**, the cloud alternative.
- The Citrix VDI guide is this one's mirror: same problems, other names. Knowing both puts you at home in any company.
""")

# ---------------------------------------------------------------- 2.16 · Windows Server
g(slug="windows-server-instalar-rol-parchear-y-leer-eventos", topic="windows-server", date="2026-10-21",
  title_es="Windows Server: instalar un rol, parchear sin cortar el servicio y leer los eventos que importan",
  title_en="Windows Server: installing a role, patching without cutting the service, and reading the events that matter",
  dek_es="Roles y características con PowerShell, la rutina de parcheo con ventana y comprobación, y las tres consultas al visor de eventos que resuelven la mayoría de los 'el servidor va raro'.",
  dek_en="Roles and features with PowerShell, the patching routine with a window and a check, and the three Event Viewer queries that solve most 'the server is acting up' tickets.",
  es="""
## Qué vas a conseguir

Manejar un Windows Server (2019, 2022 o 2025) para lo que se pide en operaciones: añadir un rol sin asistente, parchearlo un martes por la noche sin que nadie lo note, y saber leer el visor de eventos para decir con datos qué pasó.

## Antes de empezar

- Acceso por RDP o, mejor, por **PowerShell remoto** (`Enter-PSSession srv-files-01`) con una cuenta de administración del servidor. Instala **RSAT** y **Windows Admin Center** si no están: la mitad del trabajo se hace sin entrar.
- Saber qué servicio da el servidor y quién depende de él: es lo que decide la ventana de parcheo y a quién avisas.
- Un ticket de cambio aprobado para cualquier cosa que reinicie.

## 1. Instalar un rol o característica

Ejemplo: un servidor de ficheros nuevo necesita el rol **File Server** y la herramienta de administración de deduplicación.

:::term PowerShell · servidor (o remoto con -ComputerName)
$ Get-WindowsFeature | Where-Object Installed | Select-Object -ExpandProperty Name
FileAndStorage-Services
Storage-Services
...
$ Get-WindowsFeature FS-FileServer, FS-Data-Deduplication, RSAT-File-Services | Select-Object Name, InstallState
Name                   InstallState
----                   ------------
FS-FileServer             Available
FS-Data-Deduplication     Available
RSAT-File-Services        Available
$ Install-WindowsFeature FS-FileServer, FS-Data-Deduplication -IncludeManagementTools
Success Restart Needed Exit Code      Feature Result
------- -------------- ---------      --------------
True    No             Success        {Data Deduplication, File Server, File Server ...}
:::

`Restart Needed: No` es lo que esperas en la mayoría; cuando dice `Yes` (p. ej. al instalar Hyper-V), el rol no funciona hasta reiniciar. En **Server Core** (sin interfaz) esto es la única forma, y es la razón de aprenderlo así.

## 2. Parchear sin cortar el servicio

La rutina mensual, en este orden:

1. **Antes**: snapshot o copia reciente (Veeam de la noche anterior vale), ticket de cambio con la ventana, y aviso a los que dependen del servicio.
2. **Ver qué hay pendiente** y aprobarlo (si hay WSUS o Windows Update for Business, ya llega filtrado):

:::term PowerShell · servidor
$ Install-Module PSWindowsUpdate -Scope AllUsers -Force   # una vez
$ Get-WindowsUpdate
ComputerName Status KB        Size Title
------------ ------ --        ---- -----
SRV-FILES-01 ------ KB5044281 712MB 2026-10 Cumulative Update for Microsoft server operating system version 21H2
SRV-FILES-01 ------ KB5043066  45MB Security Update for .NET Framework
$ Install-WindowsUpdate -AcceptAll -IgnoreReboot
...
Reboot is required.
:::

3. **Reiniciar en la ventana**, no al acabar de instalar: `Restart-Computer -ComputerName srv-files-01 -Wait -For PowerShell -Timeout 900` desde tu equipo espera a que vuelva y te devuelve el control.
4. **Después**: que el servicio responde (un `Test-NetConnection` al puerto, abrir el recurso compartido, un inicio de sesión de prueba), que no hay errores nuevos en el visor de eventos, y cerrar el ticket con la hora.

En un **clúster de conmutación por error** (ficheros, SQL, Hyper-V), el truco para no cortar es parchear nodo a nodo: `Suspend-ClusterNode -Drain` mueve los roles al otro nodo, parcheas y reinicias ese, `Resume-ClusterNode`, y repites. **Cluster-Aware Updating** lo automatiza.

! Un servidor con `Pending reboot` desde hace semanas es un servidor a medio parchear: las actualizaciones no se aplican hasta reiniciar, y el siguiente parche fallará con `0x800f0922` o similar. `Test-PendingReboot` (módulo del mismo nombre) te lo dice en una línea para toda la lista de servidores.

## 3. Leer el visor de eventos con criterio

Abrirlo y mirar es perder la tarde. Pregúntale lo concreto:

:::term PowerShell · servidor
# 1. ¿Qué errores y críticos hubo desde el último arranque?
$ Get-WinEvent -FilterHashtable @{LogName="System"; Level=1,2; StartTime=(Get-Date).AddDays(-1)} | Group-Object Id, ProviderName | Sort-Object Count -Descending | Select-Object -First 5 Count, Name
Count Name
----- ----
   14 7031, Service Control Manager
    3 5719, NETLOGON
    1 1074, User32
# 2. ¿Quién reinició el servidor y por qué? (1074 planificado, 6008 apagado sucio, 41 Kernel-Power)
$ Get-WinEvent -FilterHashtable @{LogName="System"; Id=1074,6008,41} -MaxEvents 3 | Select-Object TimeCreated, Id, @{n="Msg";e={$_.Message.Substring(0,[math]::Min(110,$_.Message.Length))}}
TimeCreated         Id Msg
-----------         -- ---
21/10/2026 23:41:02 1074 The process C:\\Windows\\system32\\winlogon.exe (SRV-FILES-01) has initiated the restart of computer SRV-FILES-01 on behalf of user CONTOSO\\laura.prado for the following reason: Operating System: Service pack (Planned)
# 3. ¿Qué servicio se cae y cuándo? (7031/7034 = terminó inesperadamente)
$ Get-WinEvent -FilterHashtable @{LogName="System"; Id=7031,7034} -MaxEvents 5 | Select-Object TimeCreated, @{n="Svc";e={$_.Properties[0].Value}}
TimeCreated         Svc
-----------         ---
21/10/2026 08:02:11 Print Spooler
21/10/2026 07:47:55 Print Spooler
:::

Las tres consultas cubren casi todo: **qué se repite** (la primera), **por qué se reinició** (la segunda: un 6008 sin 1074 antes es un apagón o un cuelgue) y **qué servicio falla** (la tercera). Un 5719 de NETLOGON repetido es el servidor sin contacto con un controlador de dominio al arrancar: red o DNS. Lo demás se busca por ID en la documentación de Microsoft, con el texto exacto.

## 4. Lo que miras cada semana

- `Get-Service | Where-Object {$_.StartType -eq "Automatic" -and $_.Status -ne "Running"}`: servicios automáticos parados.
- `Get-PSDrive -PSProvider FileSystem`: disco libre; y en un servidor de ficheros, `Get-DedupStatus`.
- `Get-WindowsUpdate` y `Test-PendingReboot`.
- El visor de eventos con la consulta 1 de arriba.
- En **Windows Admin Center**, todo esto para varios servidores en una pantalla, sin RDP.

## Siguientes pasos

- Pon la rutina de parcheo en un script con `PSWindowsUpdate` sobre la lista de servidores, con el reinicio en la ventana y el informe al final: es el mismo patrón que la guía de PowerShell.
- Aprende **Server Core**: los servidores nuevos sin interfaz tienen menos parches, menos superficie y se gestionan igual desde PowerShell y Admin Center.
- En el Nivel 3 verás Hyper-V y, en el 4, los clústeres, el DR y la nube híbrida donde estos servidores acaban viviendo.
""",
  en="""
## What you'll get

Handle a Windows Server (2019, 2022 or 2025) for what operations asks: add a role without a wizard, patch it on a Tuesday night without anyone noticing, and know how to read Event Viewer to say, with data, what happened.

## Before you start

- Access by RDP or, better, by **PowerShell remoting** (`Enter-PSSession srv-files-01`) with a server admin account. Install **RSAT** and **Windows Admin Center** if they are missing: half the work is done without logging on.
- Know what service the server provides and who depends on it: that decides the patch window and who you warn.
- An approved change ticket for anything that reboots.

## 1. Install a role or feature

Example: a new file server needs the **File Server** role and the deduplication management tool.

:::term PowerShell · server (or remote with -ComputerName)
$ Get-WindowsFeature | Where-Object Installed | Select-Object -ExpandProperty Name
FileAndStorage-Services
Storage-Services
...
$ Get-WindowsFeature FS-FileServer, FS-Data-Deduplication, RSAT-File-Services | Select-Object Name, InstallState
Name                   InstallState
----                   ------------
FS-FileServer             Available
FS-Data-Deduplication     Available
RSAT-File-Services        Available
$ Install-WindowsFeature FS-FileServer, FS-Data-Deduplication -IncludeManagementTools
Success Restart Needed Exit Code      Feature Result
------- -------------- ---------      --------------
True    No             Success        {Data Deduplication, File Server, File Server ...}
:::

`Restart Needed: No` is what you expect for most; when it says `Yes` (e.g. installing Hyper-V), the role does not work until you reboot. On **Server Core** (no GUI) this is the only way, and the reason to learn it like this.

## 2. Patch without cutting the service

The monthly routine, in this order:

1. **Before**: a snapshot or recent backup (last night's Veeam is fine), a change ticket with the window, and a heads-up to those who depend on the service.
2. **See what is pending** and approve it (with WSUS or Windows Update for Business it already arrives filtered):

:::term PowerShell · server
$ Install-Module PSWindowsUpdate -Scope AllUsers -Force   # once
$ Get-WindowsUpdate
ComputerName Status KB        Size Title
------------ ------ --        ---- -----
SRV-FILES-01 ------ KB5044281 712MB 2026-10 Cumulative Update for Microsoft server operating system version 21H2
SRV-FILES-01 ------ KB5043066  45MB Security Update for .NET Framework
$ Install-WindowsUpdate -AcceptAll -IgnoreReboot
...
Reboot is required.
:::

3. **Reboot in the window**, not right after installing: `Restart-Computer -ComputerName srv-files-01 -Wait -For PowerShell -Timeout 900` from your device waits for it to come back and hands control back to you.
4. **After**: the service responds (a `Test-NetConnection` to the port, opening the share, a test logon), no new errors in Event Viewer, and close the ticket with the time.

On a **failover cluster** (files, SQL, Hyper-V), the trick to avoid downtime is to patch node by node: `Suspend-ClusterNode -Drain` moves the roles to the other node, you patch and reboot that one, `Resume-ClusterNode`, and repeat. **Cluster-Aware Updating** automates it.

! A server with `Pending reboot` for weeks is a half-patched server: updates don't apply until it reboots, and the next patch fails with `0x800f0922` or similar. `Test-PendingReboot` (module of the same name) tells you in one line for the whole server list.

## 3. Read Event Viewer with intent

Opening it and browsing wastes the afternoon. Ask it something specific:

:::term PowerShell · server
# 1. Which errors and criticals since yesterday?
$ Get-WinEvent -FilterHashtable @{LogName="System"; Level=1,2; StartTime=(Get-Date).AddDays(-1)} | Group-Object Id, ProviderName | Sort-Object Count -Descending | Select-Object -First 5 Count, Name
Count Name
----- ----
   14 7031, Service Control Manager
    3 5719, NETLOGON
    1 1074, User32
# 2. Who rebooted the server and why? (1074 planned, 6008 dirty shutdown, 41 Kernel-Power)
$ Get-WinEvent -FilterHashtable @{LogName="System"; Id=1074,6008,41} -MaxEvents 3 | Select-Object TimeCreated, Id, @{n="Msg";e={$_.Message.Substring(0,[math]::Min(110,$_.Message.Length))}}
TimeCreated         Id Msg
-----------         -- ---
21/10/2026 23:41:02 1074 The process C:\\Windows\\system32\\winlogon.exe (SRV-FILES-01) has initiated the restart of computer SRV-FILES-01 on behalf of user CONTOSO\\laura.prado for the following reason: Operating System: Service pack (Planned)
# 3. Which service keeps dying and when? (7031/7034 = terminated unexpectedly)
$ Get-WinEvent -FilterHashtable @{LogName="System"; Id=7031,7034} -MaxEvents 5 | Select-Object TimeCreated, @{n="Svc";e={$_.Properties[0].Value}}
TimeCreated         Svc
-----------         ---
21/10/2026 08:02:11 Print Spooler
21/10/2026 07:47:55 Print Spooler
:::

The three queries cover almost everything: **what repeats** (the first), **why it rebooted** (the second: a 6008 without a 1074 before it is a power cut or a hang) and **which service fails** (the third). A repeated NETLOGON 5719 is the server with no contact to a domain controller at boot: network or DNS. The rest is looked up by ID in Microsoft's documentation, with the exact text.

## 4. What you check every week

- `Get-Service | Where-Object {$_.StartType -eq "Automatic" -and $_.Status -ne "Running"}`: automatic services that are stopped.
- `Get-PSDrive -PSProvider FileSystem`: free disk; and on a file server, `Get-DedupStatus`.
- `Get-WindowsUpdate` and `Test-PendingReboot`.
- Event Viewer with query 1 above.
- In **Windows Admin Center**, all of this for several servers on one screen, without RDP.

## Next steps

- Turn the patching routine into a script with `PSWindowsUpdate` over the server list, with the reboot in the window and a report at the end: the same pattern as the PowerShell guide.
- Learn **Server Core**: new servers without a GUI have fewer patches, less surface, and are managed the same from PowerShell and Admin Center.
- In Level 3 you'll see Hyper-V and, in Level 4, clusters, DR and the hybrid cloud where these servers end up living.
""")

# ---------------------------------------------------------------- L3 · Ansible
g(slug="ansible-primer-playbook-parchear-servidores-linux", topic="ansible", date="2026-10-22",
  title_es="Ansible: el primer playbook para parchear servidores Linux uno a uno",
  title_en="Ansible: your first playbook to patch Linux servers one at a time",
  dek_es="Inventario, conexión por SSH, un playbook que actualiza, reinicia solo si hace falta y comprueba el servicio, ejecutado servidor a servidor con `serial`.",
  dek_en="Inventory, SSH connection, a playbook that updates, reboots only when needed and checks the service, run one server at a time with `serial`.",
  es="""
## Qué vas a conseguir

Sustituir el parcheo manual de la guía de RHEL y Ubuntu por un playbook que hace lo mismo en todos los servidores, en orden, parando si uno falla. Al terminar tendrás un repositorio con el inventario, el playbook y la salida de la primera ejecución para el ticket de cambio.

## Antes de empezar

- Una máquina de control con Python 3 y acceso SSH a los servidores (tu portátil Linux/macOS, WSL o una VM pequeña).
- Una clave SSH desplegada en los servidores para un usuario con `sudo` sin contraseña (o con contraseña: Ansible la pide con `-K`).
- Los servidores en la guía de Git del Nivel 2: el playbook es código y va bajo control de versiones desde el primer día.

## 1. Instalar y comprobar la conexión

:::term bash · máquina de control
$ python3 -m pip install --user ansible
$ ansible --version | head -1
ansible [core 2.17.4]
$ mkdir -p ~/ops/ansible && cd ~/ops/ansible
$ cat > inventory.ini <<'EOF'
[web]
srv-web-01.contoso.local
srv-web-02.contoso.local

[db]
srv-db-01.contoso.local

[linux:children]
web
db

[linux:vars]
ansible_user=ansible
ansible_become=true
EOF
$ ansible linux -i inventory.ini -m ping
srv-web-01.contoso.local | SUCCESS => {"changed": false, "ping": "pong"}
srv-web-02.contoso.local | SUCCESS => {"changed": false, "ping": "pong"}
srv-db-01.contoso.local | SUCCESS => {"changed": false, "ping": "pong"}
:::

`ping` aquí no es ICMP: es "me conecto por SSH y encuentro Python". Si uno falla, prueba `ssh ansible@srv-db-01.contoso.local` a mano antes de buscar en Ansible.

## 2. Comandos sueltos antes del playbook

:::term bash · máquina de control
$ ansible linux -i inventory.ini -m shell -a "uptime; df -h / | tail -1"
srv-web-01.contoso.local | CHANGED | rc=0 >>
 08:12:03 up 41 days,  2:17,  0 users,  load average: 0.08, 0.05, 0.01
/dev/mapper/rhel-root   50G   31G   20G  62% /
...
$ ansible web -i inventory.ini -m service -a "name=httpd state=started" --check
srv-web-01.contoso.local | SUCCESS => {"changed": false, "name": "httpd", "state": "started"}
:::

`--check` es el modo ensayo: dice qué cambiaría sin tocar nada. Úsalo siempre la primera vez.

## 3. El playbook de parcheo

:::term patch.yml
---
- name: Parcheo mensual de servidores Linux
  hosts: linux
  serial: 1
  max_fail_percentage: 0
  tasks:
    - name: Actualizar paquetes (RHEL)
      ansible.builtin.dnf:
        name: "*"
        state: latest
      when: ansible_os_family == "RedHat"
      register: dnf_result

    - name: Actualizar paquetes (Ubuntu)
      ansible.builtin.apt:
        upgrade: dist
        update_cache: true
      when: ansible_os_family == "Debian"
      register: apt_result

    - name: ¿Hace falta reiniciar? (RHEL)
      ansible.builtin.command: needs-restarting -r
      register: nr
      failed_when: nr.rc not in [0, 1]
      changed_when: false
      when: ansible_os_family == "RedHat"

    - name: ¿Hace falta reiniciar? (Ubuntu)
      ansible.builtin.stat:
        path: /var/run/reboot-required
      register: rr
      when: ansible_os_family == "Debian"

    - name: Reiniciar solo si hace falta
      ansible.builtin.reboot:
        reboot_timeout: 600
      when: (nr.rc is defined and nr.rc == 1) or (rr.stat is defined and rr.stat.exists)

    - name: Comprobar que el servicio principal está activo
      ansible.builtin.service_facts:

    - name: Fallar si httpd no está corriendo en los web
      ansible.builtin.assert:
        that: ansible_facts.services['httpd.service'].state == 'running'
        fail_msg: "httpd no arrancó tras el parcheo"
      when: "'web' in group_names"
:::

Lo importante está en tres líneas: `serial: 1` (un servidor a la vez), `max_fail_percentage: 0` (si uno falla, se para todo) y el `reboot` condicionado. `needs-restarting -r` devuelve 1 cuando hace falta reiniciar, por eso se acepta como código válido.

## 4. Ejecutar: ensayo, real y evidencia

:::term bash · máquina de control
$ ansible-playbook -i inventory.ini patch.yml --check --diff
PLAY [Parcheo mensual de servidores Linux] ************************************
TASK [Actualizar paquetes (RHEL)] *********************************************
changed: [srv-web-01.contoso.local]
...
PLAY RECAP ********************************************************************
srv-web-01.contoso.local : ok=5 changed=1 unreachable=0 failed=0 skipped=3
$ ansible-playbook -i inventory.ini patch.yml | tee logs/patch-2026-10.log
...
TASK [Reiniciar solo si hace falta] *******************************************
changed: [srv-web-01.contoso.local]
TASK [Fallar si httpd no está corriendo en los web] ***************************
ok: [srv-web-01.contoso.local]
PLAY RECAP ********************************************************************
srv-web-01.contoso.local : ok=7 changed=2 unreachable=0 failed=0 skipped=2
srv-web-02.contoso.local : ok=7 changed=2 unreachable=0 failed=0 skipped=2
srv-db-01.contoso.local  : ok=6 changed=1 unreachable=0 failed=0 skipped=3
:::

El `PLAY RECAP` con `failed=0` y el log con `tee` son la evidencia que adjuntas al ticket de cambio. Si un servidor falla, Ansible se detiene ahí y los siguientes quedan sin tocar: eso es lo que quieres en una ventana de parcheo.

> Consejo: `ansible-playbook ... --limit srv-web-01.contoso.local` ejecuta el mismo playbook en uno solo. Es la forma de probar en el servidor menos crítico antes de la ventana.

## 5. Lo que apuntas en el ticket

- Versión del playbook (el commit de Git), inventario usado y la fecha.
- El `PLAY RECAP` completo y qué servidores se reiniciaron.
- Si alguno falló: el error de la tarea y qué se hizo a mano.

## Siguientes pasos

- Separa variables por entorno (`group_vars/web.yml`) y guarda secretos con `ansible-vault`, nunca en claro en el repo.
- Con Windows, Ansible funciona por WinRM o SSH con los módulos `ansible.windows.*`: el mismo playbook, otro inventario.
- El siguiente paso natural es un rol: `ansible-galaxy init roles/baseline` para la configuración base de un servidor nuevo (usuarios, NTP, firewall, agente de monitorización).
""",
  en="""
## What you'll get

Replace the manual patching from the RHEL and Ubuntu guides with a playbook that does the same on every server, in order, stopping if one fails. By the end you will have a repository with the inventory, the playbook and the output of the first run for the change ticket.

## Before you start

- A control machine with Python 3 and SSH access to the servers (your Linux/macOS laptop, WSL or a small VM).
- An SSH key deployed on the servers for a user with passwordless `sudo` (or with a password: Ansible asks for it with `-K`).
- The servers in the Level 2 Git guide: the playbook is code and lives under version control from day one.

## 1. Install and check the connection

:::term bash · control machine
$ python3 -m pip install --user ansible
$ ansible --version | head -1
ansible [core 2.17.4]
$ mkdir -p ~/ops/ansible && cd ~/ops/ansible
$ cat > inventory.ini <<'EOF'
[web]
srv-web-01.contoso.local
srv-web-02.contoso.local

[db]
srv-db-01.contoso.local

[linux:children]
web
db

[linux:vars]
ansible_user=ansible
ansible_become=true
EOF
$ ansible linux -i inventory.ini -m ping
srv-web-01.contoso.local | SUCCESS => {"changed": false, "ping": "pong"}
srv-web-02.contoso.local | SUCCESS => {"changed": false, "ping": "pong"}
srv-db-01.contoso.local | SUCCESS => {"changed": false, "ping": "pong"}
:::

`ping` here is not ICMP: it means "I can SSH in and find Python". If one fails, try `ssh ansible@srv-db-01.contoso.local` by hand before looking in Ansible.

## 2. Ad-hoc commands before the playbook

:::term bash · control machine
$ ansible linux -i inventory.ini -m shell -a "uptime; df -h / | tail -1"
srv-web-01.contoso.local | CHANGED | rc=0 >>
 08:12:03 up 41 days,  2:17,  0 users,  load average: 0.08, 0.05, 0.01
/dev/mapper/rhel-root   50G   31G   20G  62% /
...
$ ansible web -i inventory.ini -m service -a "name=httpd state=started" --check
srv-web-01.contoso.local | SUCCESS => {"changed": false, "name": "httpd", "state": "started"}
:::

`--check` is dry-run mode: it says what would change without touching anything. Always use it the first time.

## 3. The patching playbook

:::term patch.yml
---
- name: Monthly patching of Linux servers
  hosts: linux
  serial: 1
  max_fail_percentage: 0
  tasks:
    - name: Update packages (RHEL)
      ansible.builtin.dnf:
        name: "*"
        state: latest
      when: ansible_os_family == "RedHat"
      register: dnf_result

    - name: Update packages (Ubuntu)
      ansible.builtin.apt:
        upgrade: dist
        update_cache: true
      when: ansible_os_family == "Debian"
      register: apt_result

    - name: Reboot needed? (RHEL)
      ansible.builtin.command: needs-restarting -r
      register: nr
      failed_when: nr.rc not in [0, 1]
      changed_when: false
      when: ansible_os_family == "RedHat"

    - name: Reboot needed? (Ubuntu)
      ansible.builtin.stat:
        path: /var/run/reboot-required
      register: rr
      when: ansible_os_family == "Debian"

    - name: Reboot only if needed
      ansible.builtin.reboot:
        reboot_timeout: 600
      when: (nr.rc is defined and nr.rc == 1) or (rr.stat is defined and rr.stat.exists)

    - name: Check the main service is up
      ansible.builtin.service_facts:

    - name: Fail if httpd is not running on web servers
      ansible.builtin.assert:
        that: ansible_facts.services['httpd.service'].state == 'running'
        fail_msg: "httpd did not start after patching"
      when: "'web' in group_names"
:::

What matters is in three lines: `serial: 1` (one server at a time), `max_fail_percentage: 0` (if one fails, everything stops) and the conditional `reboot`. `needs-restarting -r` returns 1 when a reboot is needed, which is why it is accepted as a valid code.

## 4. Run: dry run, real run and evidence

:::term bash · control machine
$ ansible-playbook -i inventory.ini patch.yml --check --diff
PLAY [Monthly patching of Linux servers] **************************************
TASK [Update packages (RHEL)] *************************************************
changed: [srv-web-01.contoso.local]
...
PLAY RECAP ********************************************************************
srv-web-01.contoso.local : ok=5 changed=1 unreachable=0 failed=0 skipped=3
$ ansible-playbook -i inventory.ini patch.yml | tee logs/patch-2026-10.log
...
TASK [Reboot only if needed] **************************************************
changed: [srv-web-01.contoso.local]
TASK [Fail if httpd is not running on web servers] ****************************
ok: [srv-web-01.contoso.local]
PLAY RECAP ********************************************************************
srv-web-01.contoso.local : ok=7 changed=2 unreachable=0 failed=0 skipped=2
srv-web-02.contoso.local : ok=7 changed=2 unreachable=0 failed=0 skipped=2
srv-db-01.contoso.local  : ok=6 changed=1 unreachable=0 failed=0 skipped=3
:::

The `PLAY RECAP` with `failed=0` and the log from `tee` are the evidence you attach to the change ticket. If a server fails, Ansible stops there and the rest are left untouched: that is what you want in a patch window.

> Tip: `ansible-playbook ... --limit srv-web-01.contoso.local` runs the same playbook on a single host. It is the way to test on the least critical server before the window.

## 5. What you write in the ticket

- Playbook version (the Git commit), inventory used and the date.
- The full `PLAY RECAP` and which servers rebooted.
- If one failed: the task error and what was done by hand.

## Next steps

- Split variables per environment (`group_vars/web.yml`) and keep secrets in `ansible-vault`, never in clear text in the repo.
- With Windows, Ansible works over WinRM or SSH with the `ansible.windows.*` modules: same playbook, different inventory.
- The natural next step is a role: `ansible-galaxy init roles/baseline` for the base configuration of a new server (users, NTP, firewall, monitoring agent).
""")

# ---------------------------------------------------------------- L3 · Docker
g(slug="docker-contenedores-en-un-servidor-de-operaciones", topic="docker", date="2026-10-22",
  title_es="Docker: montar y mantener contenedores en un servidor de operaciones",
  title_en="Docker: running and maintaining containers on an operations server",
  dek_es="Instalar Docker, arrancar una herramienta interna con Compose, dejar los datos en volúmenes y saber qué mirar cuando un contenedor se reinicia solo.",
  dek_en="Install Docker, start an internal tool with Compose, keep the data in volumes and know what to look at when a container keeps restarting.",
  es="""
## Qué vas a conseguir

Un servidor Linux con Docker donde las herramientas internas (un panel, un Grafana, un runner de Jenkins) corren como contenedores: se arrancan con un fichero, se actualizan cambiando una versión y sus datos sobreviven a los reinicios. Y la rutina de diagnóstico cuando uno falla.

## Antes de empezar

- Un servidor Ubuntu o RHEL ya configurado (guías del Nivel 2), con 20 GB libres en `/var/lib/docker`.
- Saber qué puertos va a exponer cada herramienta: el firewall del servidor tiene que dejarlos pasar.
- Un lugar donde guardar los ficheros Compose bajo Git.

## 1. Instalar y comprobar

:::term bash · srv-tools-01
$ curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh
...
$ sudo usermod -aG docker ansible && newgrp docker
$ docker version --format '{{.Server.Version}}'
27.3.1
$ docker run --rm hello-world | head -3
Hello from Docker!
This message shows that your installation appears to be working correctly.
$ docker system df
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          1         0         13.3kB    13.3kB (100%)
Containers      0         0         0B        0B
Local Volumes   0         0         0B        0B
:::

El usuario en el grupo `docker` equivale a root en ese servidor: solo quien administra la máquina debe estar en él.

## 2. La primera herramienta con Compose

:::term docker-compose.yml
services:
  grafana:
    image: grafana/grafana-oss:11.3.0
    container_name: grafana
    restart: unless-stopped
    ports:
      - "3000:3000"
    environment:
      GF_SERVER_ROOT_URL: https://tools.contoso.local/grafana/
      GF_SECURITY_ADMIN_PASSWORD__FILE: /run/secrets/grafana_admin
    volumes:
      - grafana-data:/var/lib/grafana
    secrets:
      - grafana_admin
    healthcheck:
      test: ["CMD-SHELL", "wget -qO- http://localhost:3000/api/health || exit 1"]
      interval: 30s
      timeout: 5s
      retries: 3

volumes:
  grafana-data:

secrets:
  grafana_admin:
    file: ./secrets/grafana_admin.txt
:::

Tres decisiones que te ahorran problemas: la **versión fija** de la imagen (nunca `latest` en un servidor), los datos en un **volumen con nombre** (no dentro del contenedor) y la contraseña en un **secreto** desde fichero, que va al `.gitignore`.

:::term bash · srv-tools-01
$ mkdir -p ~/stacks/grafana/secrets && cd ~/stacks/grafana
$ openssl rand -base64 24 > secrets/grafana_admin.txt && chmod 600 secrets/grafana_admin.txt
$ echo "secrets/" >> .gitignore
$ docker compose up -d
[+] Running 2/2
 ✔ Volume "grafana_grafana-data"  Created
 ✔ Container grafana             Started
$ docker compose ps
NAME      IMAGE                       STATUS                   PORTS
grafana   grafana/grafana-oss:11.3.0  Up 40 seconds (healthy)  0.0.0.0:3000->3000/tcp
$ sudo firewall-cmd --add-port=3000/tcp --permanent && sudo firewall-cmd --reload
:::

## 3. Cuando un contenedor se cae

:::term bash · srv-tools-01
$ docker compose ps
NAME      IMAGE                       STATUS
grafana   grafana/grafana-oss:11.3.0  Restarting (1) 12 seconds ago
$ docker compose logs --tail 30 grafana
grafana  | Error: ✗ failed to connect to database: open /var/lib/grafana/grafana.db: permission denied
$ docker inspect grafana --format '{{.State.ExitCode}} {{.State.Error}} {{.RestartCount}}'
1  7
$ docker run --rm -v grafana_grafana-data:/data alpine ls -ln /data | head -3
total 1032
-rw-r----- 1 0 0 1056768 Oct 22 07:40 grafana.db
$ docker run --rm -v grafana_grafana-data:/data alpine chown -R 472:0 /data
$ docker compose restart grafana && sleep 20 && docker compose ps --format '{{.Name}} {{.Status}}'
grafana Up 20 seconds (healthy)
:::

El orden siempre es el mismo: `ps` (qué estado), `logs --tail` (qué dice), `inspect` (código de salida y reinicios). Un contenedor en `Restarting` con el mismo error en bucle no se arregla reiniciando: se arregla leyendo el log. Aquí el volumen había sido restaurado con `root` y Grafana corre como el usuario 472.

Si el problema es de red, `docker exec -it grafana sh` te mete dentro para hacer `wget` a lo que el contenedor no alcanza, y `docker network inspect bridge` enseña qué IP tiene cada uno.

## 4. Actualizar sin perder datos

:::term bash · srv-tools-01
$ docker run --rm -v grafana_grafana-data:/data -v $PWD/backup:/backup alpine tar czf /backup/grafana-data-2026-10-22.tgz -C /data .
$ sed -i 's/grafana-oss:11.3.0/grafana-oss:11.3.1/' docker-compose.yml
$ docker compose pull && docker compose up -d
[+] Running 1/1
 ✔ Container grafana  Started
$ docker compose logs --tail 3 grafana | grep -i "http server listen"
grafana  | logger=http.server t=2026-10-22T08:01:12Z level=info msg="HTTP Server Listen" address=[::]:3000
:::

Copia del volumen, cambio de versión en el fichero, `pull`, `up -d`. Si la nueva versión falla, vuelves a la anterior con el mismo `sed` y, si hace falta, restauras el `.tgz`. El fichero Compose con el cambio de versión es el commit que va al ticket.

## 5. Limpieza mensual

:::term bash · srv-tools-01
$ docker system df
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          9         3         4.1GB     2.7GB (65%)
Build Cache     41        0         1.2GB     1.2GB
$ docker image prune -a --filter "until=720h"
$ docker builder prune -f
$ docker system df
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          3         3         1.4GB     0B (0%)
:::

! Nunca ejecutes `docker volume prune` en un servidor sin revisar antes `docker volume ls`: borra los volúmenes que ningún contenedor usa en ese momento, incluidos los de un servicio parado a propósito.

## Siguientes pasos

- Pon un proxy inverso (Traefik o Caddy) delante de los contenedores para que todos salgan por 443 con certificado y sin abrir un puerto por herramienta.
- Mete `docker compose pull && up -d` en el playbook de Ansible: la actualización de las herramientas pasa a ser una tarea más del parcheo.
- Con más de un servidor o con alta disponibilidad, el salto es Kubernetes (Nivel 4); hasta entonces, Compose en un servidor bien respaldado es suficiente para las herramientas internas.
""",
  en="""
## What you'll get

A Linux server with Docker where internal tools (a dashboard, a Grafana, a Jenkins runner) run as containers: they start from one file, they update by changing a version, and their data survives restarts. Plus the diagnosis routine when one fails.

## Before you start

- An Ubuntu or RHEL server already configured (Level 2 guides), with 20 GB free in `/var/lib/docker`.
- Know which ports each tool will expose: the server firewall has to let them through.
- A place to keep the Compose files under Git.

## 1. Install and check

:::term bash · srv-tools-01
$ curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh
...
$ sudo usermod -aG docker ansible && newgrp docker
$ docker version --format '{{.Server.Version}}'
27.3.1
$ docker run --rm hello-world | head -3
Hello from Docker!
This message shows that your installation appears to be working correctly.
$ docker system df
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          1         0         13.3kB    13.3kB (100%)
Containers      0         0         0B        0B
Local Volumes   0         0         0B        0B
:::

A user in the `docker` group is effectively root on that server: only the people who administer the machine belong in it.

## 2. The first tool with Compose

:::term docker-compose.yml
services:
  grafana:
    image: grafana/grafana-oss:11.3.0
    container_name: grafana
    restart: unless-stopped
    ports:
      - "3000:3000"
    environment:
      GF_SERVER_ROOT_URL: https://tools.contoso.local/grafana/
      GF_SECURITY_ADMIN_PASSWORD__FILE: /run/secrets/grafana_admin
    volumes:
      - grafana-data:/var/lib/grafana
    secrets:
      - grafana_admin
    healthcheck:
      test: ["CMD-SHELL", "wget -qO- http://localhost:3000/api/health || exit 1"]
      interval: 30s
      timeout: 5s
      retries: 3

volumes:
  grafana-data:

secrets:
  grafana_admin:
    file: ./secrets/grafana_admin.txt
:::

Three decisions that save you trouble: a **pinned image version** (never `latest` on a server), data in a **named volume** (not inside the container) and the password as a **secret** from a file, which goes in `.gitignore`.

:::term bash · srv-tools-01
$ mkdir -p ~/stacks/grafana/secrets && cd ~/stacks/grafana
$ openssl rand -base64 24 > secrets/grafana_admin.txt && chmod 600 secrets/grafana_admin.txt
$ echo "secrets/" >> .gitignore
$ docker compose up -d
[+] Running 2/2
 ✔ Volume "grafana_grafana-data"  Created
 ✔ Container grafana             Started
$ docker compose ps
NAME      IMAGE                       STATUS                   PORTS
grafana   grafana/grafana-oss:11.3.0  Up 40 seconds (healthy)  0.0.0.0:3000->3000/tcp
$ sudo firewall-cmd --add-port=3000/tcp --permanent && sudo firewall-cmd --reload
:::

## 3. When a container dies

:::term bash · srv-tools-01
$ docker compose ps
NAME      IMAGE                       STATUS
grafana   grafana/grafana-oss:11.3.0  Restarting (1) 12 seconds ago
$ docker compose logs --tail 30 grafana
grafana  | Error: ✗ failed to connect to database: open /var/lib/grafana/grafana.db: permission denied
$ docker inspect grafana --format '{{.State.ExitCode}} {{.State.Error}} {{.RestartCount}}'
1  7
$ docker run --rm -v grafana_grafana-data:/data alpine ls -ln /data | head -3
total 1032
-rw-r----- 1 0 0 1056768 Oct 22 07:40 grafana.db
$ docker run --rm -v grafana_grafana-data:/data alpine chown -R 472:0 /data
$ docker compose restart grafana && sleep 20 && docker compose ps --format '{{.Name}} {{.Status}}'
grafana Up 20 seconds (healthy)
:::

The order is always the same: `ps` (what state), `logs --tail` (what it says), `inspect` (exit code and restart count). A container in `Restarting` with the same error in a loop is not fixed by restarting: it is fixed by reading the log. Here the volume had been restored as `root` and Grafana runs as user 472.

If the problem is network, `docker exec -it grafana sh` gets you inside to `wget` whatever the container can't reach, and `docker network inspect bridge` shows which IP each one has.

## 4. Update without losing data

:::term bash · srv-tools-01
$ docker run --rm -v grafana_grafana-data:/data -v $PWD/backup:/backup alpine tar czf /backup/grafana-data-2026-10-22.tgz -C /data .
$ sed -i 's/grafana-oss:11.3.0/grafana-oss:11.3.1/' docker-compose.yml
$ docker compose pull && docker compose up -d
[+] Running 1/1
 ✔ Container grafana  Started
$ docker compose logs --tail 3 grafana | grep -i "http server listen"
grafana  | logger=http.server t=2026-10-22T08:01:12Z level=info msg="HTTP Server Listen" address=[::]:3000
:::

Volume backup, version change in the file, `pull`, `up -d`. If the new version fails, you go back to the previous one with the same `sed` and, if needed, restore the `.tgz`. The Compose file with the version change is the commit that goes in the ticket.

## 5. Monthly clean-up

:::term bash · srv-tools-01
$ docker system df
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          9         3         4.1GB     2.7GB (65%)
Build Cache     41        0         1.2GB     1.2GB
$ docker image prune -a --filter "until=720h"
$ docker builder prune -f
$ docker system df
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          3         3         1.4GB     0B (0%)
:::

! Never run `docker volume prune` on a server without checking `docker volume ls` first: it deletes the volumes no container is using at that moment, including those of a service you stopped on purpose.

## Next steps

- Put a reverse proxy (Traefik or Caddy) in front of the containers so everything comes out on 443 with a certificate, without opening one port per tool.
- Add `docker compose pull && up -d` to the Ansible playbook: updating the tools becomes one more patching task.
- With more than one server or with high availability, the jump is Kubernetes (Level 4); until then, Compose on a well backed-up server is enough for internal tools.
""")

# ---------------------------------------------------------------- L3 · ELK
g(slug="elk-centralizar-logs-de-servidores-y-buscar-un-error-en-kibana", topic="elk", date="2026-10-22",
  title_es="Elasticsearch, Logstash y Kibana: centralizar los logs de los servidores y buscar un error",
  title_en="Elasticsearch, Logstash and Kibana: centralising server logs and finding an error",
  dek_es="Un nodo de Elasticsearch, Filebeat en los servidores, el pipeline de Logstash que da forma a los eventos y la búsqueda en Kibana que sustituye a veinte sesiones SSH.",
  dek_en="One Elasticsearch node, Filebeat on the servers, the Logstash pipeline that shapes events, and the Kibana search that replaces twenty SSH sessions.",
  es="""
## Qué vas a conseguir

Que los logs de todos los servidores Linux (y los de Windows, con el mismo agente) lleguen a un único sitio donde buscar "permission denied" o un ID de correlación en segundos, con gráficos de cuántos errores hubo y cuándo. Al terminar tendrás la pila mínima en Docker y dos servidores enviando.

## Antes de empezar

- El servidor de herramientas de la guía de Docker, con 8 GB de RAM y 100 GB de disco para los índices.
- Puertos abiertos en su firewall: 5044 (Beats → Logstash) desde los servidores, 5601 (Kibana) desde la red de IT.
- Decidir la **retención**: cuántos días de logs guardas. Treinta es un buen punto de partida.

## 1. La pila con Compose

:::term docker-compose.yml
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.15.3
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=true
      - ELASTIC_PASSWORD_FILE=/run/secrets/elastic
      - ES_JAVA_OPTS=-Xms2g -Xmx2g
    volumes: [es-data:/usr/share/elasticsearch/data]
    secrets: [elastic]
    ulimits: { memlock: { soft: -1, hard: -1 } }
  logstash:
    image: docker.elastic.co/logstash/logstash:8.15.3
    volumes: [./pipeline:/usr/share/logstash/pipeline:ro]
    ports: ["5044:5044"]
    depends_on: [elasticsearch]
  kibana:
    image: docker.elastic.co/kibana/kibana:8.15.3
    ports: ["5601:5601"]
    environment:
      - ELASTICSEARCH_HOSTS=http://elasticsearch:9200
    depends_on: [elasticsearch]
volumes:
  es-data:
secrets:
  elastic:
    file: ./secrets/elastic.txt
:::

:::term bash · srv-tools-01
$ sudo sysctl -w vm.max_map_count=262144 && echo "vm.max_map_count=262144" | sudo tee /etc/sysctl.d/99-elastic.conf
$ docker compose up -d && sleep 60
$ curl -s -u elastic:$(cat secrets/elastic.txt) http://localhost:9200/_cluster/health?pretty | grep -E 'status|number_of_nodes'
  "status" : "green",
  "number_of_nodes" : 1,
:::

Un solo nodo y `status: green` es lo normal para un entorno de IT interno. Kibana necesita su propia cuenta de servicio: `docker compose exec elasticsearch bin/elasticsearch-reset-password -u kibana_system` y la pones en la variable `ELASTICSEARCH_PASSWORD` de Kibana.

## 2. El pipeline de Logstash

:::term pipeline/syslog.conf
input {
  beats { port => 5044 }
}
filter {
  if [event][dataset] == "system.syslog" {
    grok {
      match => { "message" => "%{SYSLOGTIMESTAMP:ts} %{SYSLOGHOST:host.name} %{DATA:process.name}(?:\\[%{POSINT:process.pid}\\])?: %{GREEDYDATA:log.message}" }
    }
    date { match => ["ts", "MMM  d HH:mm:ss", "MMM dd HH:mm:ss"] }
    mutate { remove_field => ["ts"] }
  }
  if "Permission denied" in [message] or "Failed password" in [message] {
    mutate { add_tag => ["security"] }
  }
}
output {
  elasticsearch {
    hosts => ["http://elasticsearch:9200"]
    user => "elastic"
    password => "${ELASTIC_PASSWORD}"
    index => "logs-linux-%{+YYYY.MM.dd}"
  }
}
:::

El `grok` convierte una línea de texto en campos (`host.name`, `process.name`, `log.message`): sin eso solo podrías buscar texto libre. La etiqueta `security` es el primer ejemplo de algo que luego usarás en una alerta. Comprueba la sintaxis antes de arrancar: `docker compose exec logstash bin/logstash --config.test_and_exit -f /usr/share/logstash/pipeline/syslog.conf`.

## 3. Filebeat en los servidores

:::term bash · srv-web-01
$ curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-8.15.3-x86_64.rpm && sudo rpm -vi filebeat-8.15.3-x86_64.rpm
$ sudo filebeat modules enable system
$ sudo sed -i 's|#output.logstash:|output.logstash:|; s|#hosts: \\["localhost:5044"\\]|hosts: ["srv-tools-01.contoso.local:5044"]|' /etc/filebeat/filebeat.yml
$ sudo sed -i 's|^output.elasticsearch:|#output.elasticsearch:|; s|^  hosts: \\["localhost:9200"\\]|#  hosts: ["localhost:9200"]|' /etc/filebeat/filebeat.yml
$ sudo filebeat test output
logstash: srv-tools-01.contoso.local:5044...
  connection...
    parse host... OK
    dns lookup... OK
    TCP... OK
  talk to server... OK
$ sudo systemctl enable --now filebeat
:::

`filebeat test output` es la prueba que haces antes de abrir un ticket al equipo de red: si `TCP... OK` falla, es el firewall; si falla `talk to server`, es Logstash. Con Ansible (guía anterior), este paso es un playbook de diez líneas para toda la flota.

## 4. Buscar en Kibana

:::ui Kibana · Discover
> Analytics › Discover › logs-linux-*
= Rango: Last 24 hours
= KQL: host.name : "srv-web-01" and tags : "security"
= Resultados: 37 hits
Oct 22, 2026 07:58:12  srv-web-01  sshd[2231]  Failed password for invalid user admin from 10.20.4.77 port 51022 ssh2
Oct 22, 2026 07:58:14  srv-web-01  sshd[2231]  Failed password for invalid user admin from 10.20.4.77 port 51030 ssh2
Oct 22, 2026 08:02:11  srv-web-01  httpd[1842]  (13)Permission denied: AH00072: make_sock: could not bind to address 0.0.0.0:8081
[Add filter] [Save] [Share]
:::

Para que Kibana vea los índices hace falta una **Data view** (`Stack Management → Data views → Create`, patrón `logs-linux-*`, campo de tiempo `@timestamp`). A partir de ahí: la misma búsqueda en todos los servidores a la vez, el histograma arriba te dice a qué hora empezó el problema, y **Visualize** sobre `process.name` te enseña qué servicio genera más errores.

## 5. Retención y espacio

:::term bash · srv-tools-01
$ curl -s -u elastic:$(cat secrets/elastic.txt) -X PUT http://localhost:9200/_ilm/policy/logs-30d -H 'Content-Type: application/json' -d '{"policy":{"phases":{"hot":{"actions":{}},"delete":{"min_age":"30d","actions":{"delete":{}}}}}}'
{"acknowledged":true}
$ curl -s -u elastic:$(cat secrets/elastic.txt) -X PUT http://localhost:9200/_index_template/logs-linux -H 'Content-Type: application/json' -d '{"index_patterns":["logs-linux-*"],"template":{"settings":{"index.lifecycle.name":"logs-30d","number_of_replicas":0}}}'
{"acknowledged":true}
$ curl -s -u elastic:$(cat secrets/elastic.txt) 'http://localhost:9200/_cat/indices/logs-*?v&h=index,docs.count,store.size&s=index' | tail -3
logs-linux-2026.10.20   412033   211.4mb
logs-linux-2026.10.21   398870   204.9mb
logs-linux-2026.10.22    88121    46.1mb
:::

Con un solo nodo, `number_of_replicas: 0` evita que el clúster esté siempre en amarillo. Unos 200 MB al día por veinte servidores es el orden de magnitud; mira `_cat/indices` al mes para ajustar la retención al disco que tienes.

## Siguientes pasos

- Windows: el agente es **Winlogbeat** con el mismo `output.logstash`; los eventos de seguridad (4625, 4740) llegan ya con campos.
- Una alerta en Kibana (`Alerts and Insights → Rules`) sobre `tags: security` con más de 20 eventos en 5 minutos, enviada al canal del equipo.
- Si el volumen crece, la opción es **Elastic Agent + Fleet** en lugar de Beats sueltos, o pasar los dashboards a Grafana (siguiente guía) con Elasticsearch como origen de datos.
""",
  en="""
## What you'll get

Logs from every Linux server (and Windows, with the same agent) arriving in one place where you can search for "permission denied" or a correlation ID in seconds, with charts of how many errors there were and when. By the end you will have the minimal stack in Docker and two servers shipping.

## Before you start

- The tools server from the Docker guide, with 8 GB of RAM and 100 GB of disk for the indices.
- Ports open in its firewall: 5044 (Beats → Logstash) from the servers, 5601 (Kibana) from the IT network.
- Decide the **retention**: how many days of logs you keep. Thirty is a good starting point.

## 1. The stack with Compose

:::term docker-compose.yml
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.15.3
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=true
      - ELASTIC_PASSWORD_FILE=/run/secrets/elastic
      - ES_JAVA_OPTS=-Xms2g -Xmx2g
    volumes: [es-data:/usr/share/elasticsearch/data]
    secrets: [elastic]
    ulimits: { memlock: { soft: -1, hard: -1 } }
  logstash:
    image: docker.elastic.co/logstash/logstash:8.15.3
    volumes: [./pipeline:/usr/share/logstash/pipeline:ro]
    ports: ["5044:5044"]
    depends_on: [elasticsearch]
  kibana:
    image: docker.elastic.co/kibana/kibana:8.15.3
    ports: ["5601:5601"]
    environment:
      - ELASTICSEARCH_HOSTS=http://elasticsearch:9200
    depends_on: [elasticsearch]
volumes:
  es-data:
secrets:
  elastic:
    file: ./secrets/elastic.txt
:::

:::term bash · srv-tools-01
$ sudo sysctl -w vm.max_map_count=262144 && echo "vm.max_map_count=262144" | sudo tee /etc/sysctl.d/99-elastic.conf
$ docker compose up -d && sleep 60
$ curl -s -u elastic:$(cat secrets/elastic.txt) http://localhost:9200/_cluster/health?pretty | grep -E 'status|number_of_nodes'
  "status" : "green",
  "number_of_nodes" : 1,
:::

One node and `status: green` is normal for an internal IT environment. Kibana needs its own service account: `docker compose exec elasticsearch bin/elasticsearch-reset-password -u kibana_system`, and you put it in Kibana's `ELASTICSEARCH_PASSWORD` variable.

## 2. The Logstash pipeline

:::term pipeline/syslog.conf
input {
  beats { port => 5044 }
}
filter {
  if [event][dataset] == "system.syslog" {
    grok {
      match => { "message" => "%{SYSLOGTIMESTAMP:ts} %{SYSLOGHOST:host.name} %{DATA:process.name}(?:\\[%{POSINT:process.pid}\\])?: %{GREEDYDATA:log.message}" }
    }
    date { match => ["ts", "MMM  d HH:mm:ss", "MMM dd HH:mm:ss"] }
    mutate { remove_field => ["ts"] }
  }
  if "Permission denied" in [message] or "Failed password" in [message] {
    mutate { add_tag => ["security"] }
  }
}
output {
  elasticsearch {
    hosts => ["http://elasticsearch:9200"]
    user => "elastic"
    password => "${ELASTIC_PASSWORD}"
    index => "logs-linux-%{+YYYY.MM.dd}"
  }
}
:::

The `grok` turns a line of text into fields (`host.name`, `process.name`, `log.message`): without it you could only search free text. The `security` tag is the first example of something you will later use in an alert. Check the syntax before starting: `docker compose exec logstash bin/logstash --config.test_and_exit -f /usr/share/logstash/pipeline/syslog.conf`.

## 3. Filebeat on the servers

:::term bash · srv-web-01
$ curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-8.15.3-x86_64.rpm && sudo rpm -vi filebeat-8.15.3-x86_64.rpm
$ sudo filebeat modules enable system
$ sudo sed -i 's|#output.logstash:|output.logstash:|; s|#hosts: \\["localhost:5044"\\]|hosts: ["srv-tools-01.contoso.local:5044"]|' /etc/filebeat/filebeat.yml
$ sudo sed -i 's|^output.elasticsearch:|#output.elasticsearch:|; s|^  hosts: \\["localhost:9200"\\]|#  hosts: ["localhost:9200"]|' /etc/filebeat/filebeat.yml
$ sudo filebeat test output
logstash: srv-tools-01.contoso.local:5044...
  connection...
    parse host... OK
    dns lookup... OK
    TCP... OK
  talk to server... OK
$ sudo systemctl enable --now filebeat
:::

`filebeat test output` is the test you run before opening a ticket with the network team: if `TCP... OK` fails, it is the firewall; if `talk to server` fails, it is Logstash. With Ansible (previous guide), this step is a ten-line playbook for the whole fleet.

## 4. Searching in Kibana

:::ui Kibana · Discover
> Analytics › Discover › logs-linux-*
= Range: Last 24 hours
= KQL: host.name : "srv-web-01" and tags : "security"
= Results: 37 hits
Oct 22, 2026 07:58:12  srv-web-01  sshd[2231]  Failed password for invalid user admin from 10.20.4.77 port 51022 ssh2
Oct 22, 2026 07:58:14  srv-web-01  sshd[2231]  Failed password for invalid user admin from 10.20.4.77 port 51030 ssh2
Oct 22, 2026 08:02:11  srv-web-01  httpd[1842]  (13)Permission denied: AH00072: make_sock: could not bind to address 0.0.0.0:8081
[Add filter] [Save] [Share]
:::

For Kibana to see the indices you need a **Data view** (`Stack Management → Data views → Create`, pattern `logs-linux-*`, time field `@timestamp`). From there: the same search across every server at once, the histogram at the top tells you what time the problem started, and **Visualize** on `process.name` shows which service produces the most errors.

## 5. Retention and disk

:::term bash · srv-tools-01
$ curl -s -u elastic:$(cat secrets/elastic.txt) -X PUT http://localhost:9200/_ilm/policy/logs-30d -H 'Content-Type: application/json' -d '{"policy":{"phases":{"hot":{"actions":{}},"delete":{"min_age":"30d","actions":{"delete":{}}}}}}'
{"acknowledged":true}
$ curl -s -u elastic:$(cat secrets/elastic.txt) -X PUT http://localhost:9200/_index_template/logs-linux -H 'Content-Type: application/json' -d '{"index_patterns":["logs-linux-*"],"template":{"settings":{"index.lifecycle.name":"logs-30d","number_of_replicas":0}}}'
{"acknowledged":true}
$ curl -s -u elastic:$(cat secrets/elastic.txt) 'http://localhost:9200/_cat/indices/logs-*?v&h=index,docs.count,store.size&s=index' | tail -3
logs-linux-2026.10.20   412033   211.4mb
logs-linux-2026.10.21   398870   204.9mb
logs-linux-2026.10.22    88121    46.1mb
:::

With a single node, `number_of_replicas: 0` stops the cluster from being permanently yellow. Around 200 MB a day for twenty servers is the order of magnitude; look at `_cat/indices` after a month to fit the retention to the disk you have.

## Next steps

- Windows: the agent is **Winlogbeat** with the same `output.logstash`; security events (4625, 4740) arrive with fields already parsed.
- An alert in Kibana (`Alerts and Insights → Rules`) on `tags: security` with more than 20 events in 5 minutes, sent to the team channel.
- If volume grows, the option is **Elastic Agent + Fleet** instead of standalone Beats, or moving the dashboards to Grafana (next guide) with Elasticsearch as a data source.
""")

# ---------------------------------------------------------------- L3 · Conditional Access
g(slug="entra-conditional-access-politicas-base-y-usuario-bloqueado", topic="conditional-access", date="2026-10-22",
  title_es="Entra ID Conditional Access: las políticas base, el modo solo informe y un usuario bloqueado",
  title_en="Entra ID Conditional Access: the baseline policies, report-only mode and a blocked user",
  dek_es="Las cuatro políticas con las que empieza todo tenant, cómo probarlas sin bloquear a nadie, las cuentas de emergencia excluidas y cómo leer en el registro de inicios de sesión por qué alguien no entra.",
  dek_en="The four policies every tenant starts with, how to test them without locking anyone out, the excluded emergency accounts, and how to read in the sign-in log why someone can't get in.",
  es="""
## Qué vas a conseguir

Un conjunto de políticas de Conditional Access que exige MFA, bloquea la autenticación heredada y protege a los administradores, desplegado sin sorpresas gracias al modo **solo informe**. Y la rutina para el ticket de "no puedo entrar" más frecuente a partir de ahora: el que causa una de tus políticas.

## Antes de empezar

- Rol de **Conditional Access Administrator** (o Security Administrator), idealmente activado por PIM.
- Licencias Entra ID P1 en el tenant (las políticas basadas en riesgo necesitan P2).
- Dos **cuentas de emergencia** (break-glass) ya creadas, con contraseñas largas guardadas fuera de línea, y un grupo que las contenga.
- La lista de aplicaciones o servicios que usan autenticación heredada (POP/IMAP, SMTP básico): el informe `Sign-in logs` filtrado por `Client app` te la da.

## 1. Las cuentas de emergencia, primero

Toda política excluye al grupo de emergencia. Sin esa exclusión, un error en una política te deja fuera del tenant a ti también.

:::ui Entra admin center · Grupos
> Identidad › Grupos › Todos los grupos › sg-breakglass-exclude
= Tipo: Seguridad
= Miembros: brk-admin-01@contoso.onmicrosoft.com, brk-admin-02@contoso.onmicrosoft.com
= Pertenencia: Asignada
= Propietarios: IT Security
[Guardar]
:::

Las cuentas de emergencia no tienen licencia ni se usan nunca salvo emergencia. Entran con una llave FIDO2 guardada en una caja fuerte (Microsoft exige MFA en los portales de administración también a ellas), y cada inicio de sesión con ellas dispara una alerta (guías de Global Admin y PIM y de Microsoft Sentinel, Nivel 4).

## 2. Las cuatro políticas base

:::ui Entra admin center · Conditional Access
> Protección › Acceso condicional › Políticas › Nueva política
= Nombre: CA001 - Require MFA for all users
= Usuarios: Todos los usuarios · Excluir: sg-breakglass-exclude
= Recursos de destino: Todas las aplicaciones en la nube
= Condiciones: (ninguna)
= Conceder: Conceder acceso · [x] Requerir autenticación multifactor
= Habilitar política: Solo informe
[Crear]
:::

Las otras tres siguen el mismo patrón:

| Política | Usuarios | Condición | Control |
|---|---|---|---|
| CA002 - Block legacy authentication | Todos (excl. emergencia) | Aplicaciones cliente: Exchange ActiveSync, Otros clientes | Bloquear |
| CA003 - Require MFA for admins | Roles de directorio: Global Admin, Exchange Admin, SharePoint Admin, Security Admin, CA Admin, User Admin… (excl. emergencia) | — | Requerir MFA |
| CA004 - Require compliant device for Office 365 | Todos (excl. emergencia e invitados) | Plataformas: Windows, macOS, iOS, Android | Requerir dispositivo marcado como conforme **o** unido a Entra híbrido |

Todas en **Solo informe** al crearlas. Ninguna se activa el mismo día.

## 3. Una semana en solo informe

:::ui Entra admin center · Sign-in logs
> Identidad › Supervisión y estado › Registros de inicio de sesión › Inicios de sesión de usuario (interactivos)
= Filtro: Acceso condicional: Solo informe: Error
= Fecha: Últimos 7 días
= Resultados: 212 inicios de sesión · 31 usuarios
laura.prado@contoso.com   Outlook mobile    CA002   Error (solo informe)   Client app: IMAP
svc-scan@contoso.com      SMTP              CA002   Error (solo informe)   Client app: SMTP
m.ortega@contoso.com      Teams             CA004   Error (solo informe)   Dispositivo: No conforme
[Descargar] [Columnas]
:::

Esta lista es la que trabajas antes de activar nada: la impresora que envía por SMTP básico pasa a Microsoft 365 **alta disponibilidad SMTP** o a un conector; la cuenta IMAP pasa a Outlook moderno; el equipo de M. Ortega se arregla en Intune (guía de Intune). La pestaña **Insights and reporting** de Conditional Access hace la cuenta por política. Cuando una política lleva cero errores no esperados durante una semana, se pasa a **Activado**. Una política por semana, no las cuatro a la vez.

> Consejo: **What If** (en la página de políticas) simula un inicio de sesión: usuario, aplicación, plataforma, ubicación. Es lo que usas para responder "¿qué pasará con el director cuando viaje?" antes de que viaje.

## 4. El ticket: "no puedo entrar"

:::ui Entra admin center · Sign-in logs › Detalle
> Registros de inicio de sesión › laura.prado@contoso.com › 22/10/2026 09:14:02
= Estado: Error
= Código de error: 53000
= Motivo del error: Device is not in required device state: compliant
= Aplicación: Microsoft Teams
= Dispositivo: LAPTOP-7F2K9Q · Windows 11 · Unido a Entra híbrido · Conforme: No
Acceso condicional
= CA001 - Require MFA for all users: Correcto
= CA004 - Require compliant device for Office 365: Error · Control: Requerir dispositivo conforme
:::

El detalle del inicio de sesión tiene dos pestañas que resuelven el 90 %: **Información básica** (código de error) y **Acceso condicional** (qué política falló y qué control). Con el código vas a Intune: el dispositivo marca no conforme por BitLocker apagado (guía de BitLocker del Nivel 1). Lo que nunca haces es excluir al usuario de la política para "que entre ya": arreglas la causa y lo apuntas.

Los códigos que verás a menudo: **53000/53001** (dispositivo no conforme o no unido), **50074** (MFA obligatoria y el usuario no completó), **530032** (bloqueado por política de autenticación heredada), **50076** (MFA requerida por una política que acaba de activarse).

## 5. Lo que revisas cada mes

- Que las dos cuentas de emergencia siguen excluidas de todas las políticas (**Conditional Access → Políticas → filtro por exclusión**).
- Políticas que llevan más de un mes en solo informe: o se activan o se borran.
- `Insights and reporting`: usuarios con más fallos por política. Un pico de CA002 es alguien configurando IMAP en un móvil nuevo.
- Que no ha aparecido ninguna política nueva que tú no crearas: el registro de auditoría (`Audit logs`, categoría Policy) lo dice, y el repo 27 lo cruza con los tickets de cambio.

## Siguientes pasos

- **Ubicaciones con nombre**: la IP pública de la sede como ubicación de confianza, y una política que bloquee países desde los que la empresa no trabaja.
- **Frecuencia de inicio de sesión** y **sesión persistente** para los equipos no gestionados: menos tokens de larga duración fuera de tus dispositivos.
- Con P2, las políticas de **riesgo de usuario** e **inicio de sesión de riesgo** (Identity Protection) sustituyen reglas estáticas por señales.
- La guía de Entra ID SSO explica el otro lado: qué aplicaciones hay detrás de "todas las aplicaciones en la nube".
""",
  en="""
## What you'll get

A set of Conditional Access policies that requires MFA, blocks legacy authentication and protects administrators, rolled out without surprises thanks to **report-only** mode. Plus the routine for the most frequent "I can't sign in" ticket from now on: the one caused by one of your policies.

## Before you start

- The **Conditional Access Administrator** role (or Security Administrator), ideally activated through PIM.
- Entra ID P1 licences in the tenant (risk-based policies need P2).
- Two **emergency accounts** (break-glass) already created, with long passwords stored offline, and a group that contains them.
- The list of applications or services that use legacy authentication (POP/IMAP, basic SMTP): the `Sign-in logs` report filtered by `Client app` gives you that.

## 1. Emergency accounts first

Every policy excludes the emergency group. Without that exclusion, a mistake in a policy locks you out of the tenant too.

:::ui Entra admin center · Groups
> Identity › Groups › All groups › sg-breakglass-exclude
= Type: Security
= Members: brk-admin-01@contoso.onmicrosoft.com, brk-admin-02@contoso.onmicrosoft.com
= Membership: Assigned
= Owners: IT Security
[Save]
:::

Emergency accounts have no licence and are never used except in an emergency. They sign in with a FIDO2 key kept in a safe (Microsoft requires MFA for the admin portals for them too), and every sign-in with them raises an alert (Global Admin and PIM and Microsoft Sentinel guides, Level 4).

## 2. The four baseline policies

:::ui Entra admin center · Conditional Access
> Protection › Conditional Access › Policies › New policy
= Name: CA001 - Require MFA for all users
= Users: All users · Exclude: sg-breakglass-exclude
= Target resources: All cloud apps
= Conditions: (none)
= Grant: Grant access · [x] Require multifactor authentication
= Enable policy: Report-only
[Create]
:::

The other three follow the same pattern:

| Policy | Users | Condition | Control |
|---|---|---|---|
| CA002 - Block legacy authentication | All (excl. emergency) | Client apps: Exchange ActiveSync, Other clients | Block |
| CA003 - Require MFA for admins | Directory roles: Global Admin, Exchange Admin, SharePoint Admin, Security Admin, CA Admin, User Admin… (excl. emergency) | — | Require MFA |
| CA004 - Require compliant device for Office 365 | All (excl. emergency and guests) | Platforms: Windows, macOS, iOS, Android | Require device marked compliant **or** Hybrid Entra joined |

All in **Report-only** when created. None is switched on the same day.

## 3. A week in report-only

:::ui Entra admin center · Sign-in logs
> Identity › Monitoring & health › Sign-in logs › User sign-ins (interactive)
= Filter: Conditional Access: Report-only: Failure
= Date: Last 7 days
= Results: 212 sign-ins · 31 users
laura.prado@contoso.com   Outlook mobile    CA002   Failure (report-only)   Client app: IMAP
svc-scan@contoso.com      SMTP              CA002   Failure (report-only)   Client app: SMTP
m.ortega@contoso.com      Teams             CA004   Failure (report-only)   Device: Not compliant
[Download] [Columns]
:::

This list is what you work through before enabling anything: the printer that sends over basic SMTP moves to Microsoft 365 **high-volume SMTP** or a connector; the IMAP account moves to modern Outlook; M. Ortega's laptop is fixed in Intune (Intune guide). The **Insights and reporting** tab in Conditional Access does the count per policy. When a policy shows zero unexpected failures for a week, it moves to **On**. One policy a week, not all four at once.

> Tip: **What If** (on the policies page) simulates a sign-in: user, application, platform, location. It is what you use to answer "what will happen to the director when she travels?" before she travels.

## 4. The ticket: "I can't sign in"

:::ui Entra admin center · Sign-in logs › Details
> Sign-in logs › laura.prado@contoso.com › 22/10/2026 09:14:02
= Status: Failure
= Error code: 53000
= Failure reason: Device is not in required device state: compliant
= Application: Microsoft Teams
= Device: LAPTOP-7F2K9Q · Windows 11 · Hybrid Entra joined · Compliant: No
Conditional Access
= CA001 - Require MFA for all users: Success
= CA004 - Require compliant device for Office 365: Failure · Control: Require compliant device
:::

The sign-in details have two tabs that solve 90%: **Basic info** (error code) and **Conditional Access** (which policy failed and which control). With the code you go to Intune: the device is non-compliant because BitLocker is off (Level 1 BitLocker guide). What you never do is exclude the user from the policy "so they can get in now": you fix the cause and write it down.

Codes you will see often: **53000/53001** (device not compliant or not joined), **50074** (MFA required and the user did not complete it), **530032** (blocked by the legacy authentication policy), **50076** (MFA required by a policy that was just enabled).

## 5. What you review each month

- That the two emergency accounts are still excluded from every policy (**Conditional Access → Policies → filter by exclusion**).
- Policies that have been in report-only for more than a month: either enable them or delete them.
- `Insights and reporting`: users with the most failures per policy. A spike in CA002 is someone setting up IMAP on a new phone.
- That no new policy has appeared that you didn't create: the audit log (`Audit logs`, category Policy) says so, and repo 27 matches it against change tickets.

## Next steps

- **Named locations**: the site's public IP as a trusted location, and a policy that blocks countries the company does not work from.
- **Sign-in frequency** and **persistent browser session** for unmanaged devices: fewer long-lived tokens outside your devices.
- With P2, **user risk** and **sign-in risk** policies (Identity Protection) replace static rules with signals.
- The Entra ID SSO guide explains the other side: which applications sit behind "all cloud apps".
""")

# ---------------------------------------------------------------- L3 · Entra SSO
g(slug="entra-sso-saml-dar-de-alta-una-aplicacion-y-login-que-falla", topic="entra-sso", date="2026-10-22",
  title_es="Entra ID SSO con SAML: dar de alta una aplicación, asignar usuarios y arreglar un inicio de sesión que falla",
  title_en="Entra ID SSO with SAML: onboarding an application, assigning users and fixing a sign-in that fails",
  dek_es="La aplicación empresarial, los identificadores y la URL de respuesta, las reclamaciones, la asignación por grupo, el certificado que caduca y los tres errores que verás en el registro de inicios de sesión.",
  dek_en="The enterprise application, identifiers and reply URL, claims, group-based assignment, the certificate that expires, and the three errors you will see in the sign-in log.",
  es="""
## Qué vas a conseguir

Que una aplicación de terceros (aquí un gestor de gastos ficticio, "Fabrikam Expenses") se abra con la cuenta de la empresa, sin contraseña propia, solo para quien esté en el grupo correcto. Y saber qué mirar cuando el proveedor dice "el SAML está bien" y el usuario sigue viendo un error.

## Antes de empezar

- Rol de **Cloud Application Administrator** (o Application Administrator).
- Del proveedor de la aplicación: su **Identifier (Entity ID)**, su **Reply URL (ACS)** y qué atributo espera como identificador de usuario (normalmente el correo o el UPN).
- Un grupo de seguridad con los usuarios que deben tener acceso (`sg-app-expenses-users`). La asignación siempre va por grupo, nunca usuario a usuario.
- Un usuario de prueba en ese grupo que no sea tú.

## 1. Crear la aplicación empresarial

:::ui Entra admin center · Enterprise applications
> Identidad › Aplicaciones › Aplicaciones empresariales › Nueva aplicación › Crear su propia aplicación
= Nombre: Fabrikam Expenses
[x] Integrar cualquier otra aplicación que no se encuentre en la galería (que no sea de la galería)
[Crear]
:::

Si la aplicación está en la **galería**, úsala: trae las URLs y las reclamaciones ya puestas y, a menudo, el aprovisionamiento SCIM. La opción manual es para las que no están.

## 2. Configurar SAML

:::ui Fabrikam Expenses · Inicio de sesión único
> Fabrikam Expenses › Inicio de sesión único › SAML
Configuración básica de SAML
= Identificador (Id. de entidad): https://expenses.fabrikam.com/saml/metadata
= URL de respuesta (URL del Servicio de consumidor de aserciones): https://expenses.fabrikam.com/saml/acs
= URL de inicio de sesión: https://expenses.fabrikam.com/login
Atributos y reclamaciones
= Identificador de usuario único (Id. de nombre): user.userprincipalname [nameid-format:emailAddress]
= emailaddress: user.mail
= givenname: user.givenname
= surname: user.surname
= department: user.department
Certificado de firma de SAML
= Estado: Activo · Huella digital: 3F:9A:… · Expiración: 22/10/2029
= URL de metadatos de federación de aplicación: https://login.microsoftonline.com/…/federationmetadata/2007-06/federationmetadata.xml?appid=…
[Guardar] [Descargar certificado (Base64)]
:::

Lo que le das al proveedor: la **URL de metadatos de federación** (y con eso tiene todo) o, si no la acepta, el **certificado Base64**, la **URL de inicio de sesión** y el **identificador de Entra**, que están en la sección 4 de la misma página. Apunta la fecha de expiración del certificado en el calendario del equipo: dentro de tres años esto falla a las 00:00 de ese día.

## 3. Asignar el grupo y probar

:::ui Fabrikam Expenses · Usuarios y grupos
> Fabrikam Expenses › Usuarios y grupos › Agregar usuario o grupo
= Grupos: sg-app-expenses-users (84 miembros)
= Rol: User
[Asignar]
> Fabrikam Expenses › Propiedades
= ¿Asignación necesaria?: Sí
= ¿Visible para los usuarios?: Sí
:::

**Asignación necesaria: Sí** es lo que hace que solo el grupo entre. Con "No", cualquier usuario del tenant puede iniciar sesión en la aplicación. Después, con el usuario de prueba, abre `https://myapps.microsoft.com` o la URL de la aplicación y comprueba que entra. El botón **Probar** de la página de SAML también sirve, pero prueba con tu cuenta y tú eres administrador: no es la prueba que importa.

## 4. Cuando no entra

:::ui Entra admin center · Sign-in logs › Detalle
> Registros de inicio de sesión › laura.prado@contoso.com › Fabrikam Expenses › 22/10/2026 10:02
= Estado: Error
= Código de error: AADSTS50105
= Motivo del error: Your administrator has configured the application Fabrikam Expenses to block users unless they are specifically granted ('assigned') access to the application.
[Copiar] [Solucionar problemas]
:::

Los tres que verás casi siempre:

| Código | Qué significa | Qué haces |
|---|---|---|
| **AADSTS50105** | El usuario no está asignado | Comprobar que está en `sg-app-expenses-users` (y que el grupo es de seguridad, no un grupo de M365 dinámico sin sincronizar) |
| **AADSTS700016 / 50011** | El identificador o la URL de respuesta que envía la aplicación no coinciden con los de Entra | Comparar carácter a carácter con lo que el proveedor tiene configurado (`http` frente a `https`, barra final) |
| **AADSTS7500529 / "The signing certificate…"** | El proveedor tiene el certificado antiguo | Enviar el nuevo o la URL de metadatos; pasa justo cuando caduca |

Si Entra da **Correcto** y el error lo pone la aplicación ("user not found", "invalid NameID"), el problema está en la reclamación: el proveedor espera el correo y recibe el UPN, o al revés. La extensión **My Apps Secure Sign-in** del navegador o el botón **Probar** enseñan la aserción SAML que se envía, reclamación por reclamación.

## 5. Lo que revisas cada mes

- Certificados SAML que caducan en menos de 90 días: `Aplicaciones empresariales → filtro "Expiración del certificado"`, o el repo 20 de mi GitHub, que lo lista con calendario.
- Aplicaciones con **Asignación necesaria: No** que deberían tenerla.
- Aplicaciones sin propietario: cuando falle, nadie sabrá a quién llamar.
- Consentimientos de usuario a aplicaciones nuevas (`Aplicaciones empresariales → Consentimiento y permisos`).

## Siguientes pasos

- **OIDC** en lugar de SAML para aplicaciones modernas: se hace en **Registros de aplicaciones**, con URI de redirección y ámbitos en lugar de ACS y reclamaciones. La guía de Microsoft Graph usa uno.
- **Aprovisionamiento SCIM**: que la alta y la baja en el grupo creen y desactiven la cuenta en la aplicación. Es lo que cierra el ciclo con la guía de Active Directory del Nivel 1.
- Añade la aplicación a una política de Conditional Access concreta (guía anterior) si exige MFA siempre, aunque el usuario esté en un equipo conforme.
""",
  en="""
## What you'll get

A third-party application (here a fictional expense manager, "Fabrikam Expenses") that opens with the company account, with no password of its own, only for people in the right group. And knowing what to look at when the vendor says "SAML is fine" and the user still sees an error.

## Before you start

- The **Cloud Application Administrator** role (or Application Administrator).
- From the application vendor: their **Identifier (Entity ID)**, their **Reply URL (ACS)** and which attribute they expect as the user identifier (usually the email or the UPN).
- A security group with the users who should have access (`sg-app-expenses-users`). Assignment always goes through a group, never user by user.
- A test user in that group who is not you.

## 1. Create the enterprise application

:::ui Entra admin center · Enterprise applications
> Identity › Applications › Enterprise applications › New application › Create your own application
= Name: Fabrikam Expenses
[x] Integrate any other application you don't find in the gallery (Non-gallery)
[Create]
:::

If the application is in the **gallery**, use it: it comes with the URLs and claims pre-filled and, often, SCIM provisioning. The manual option is for those that are not.

## 2. Configure SAML

:::ui Fabrikam Expenses · Single sign-on
> Fabrikam Expenses › Single sign-on › SAML
Basic SAML Configuration
= Identifier (Entity ID): https://expenses.fabrikam.com/saml/metadata
= Reply URL (Assertion Consumer Service URL): https://expenses.fabrikam.com/saml/acs
= Sign on URL: https://expenses.fabrikam.com/login
Attributes & Claims
= Unique User Identifier (Name ID): user.userprincipalname [nameid-format:emailAddress]
= emailaddress: user.mail
= givenname: user.givenname
= surname: user.surname
= department: user.department
SAML Signing Certificate
= Status: Active · Thumbprint: 3F:9A:… · Expiration: 22/10/2029
= App Federation Metadata Url: https://login.microsoftonline.com/…/federationmetadata/2007-06/federationmetadata.xml?appid=…
[Save] [Download certificate (Base64)]
:::

What you give the vendor: the **federation metadata URL** (and with that they have everything) or, if they don't accept it, the **Base64 certificate**, the **Login URL** and the **Entra identifier**, which are in section 4 of the same page. Put the certificate expiry date in the team calendar: in three years this fails at 00:00 on that day.

## 3. Assign the group and test

:::ui Fabrikam Expenses · Users and groups
> Fabrikam Expenses › Users and groups › Add user/group
= Groups: sg-app-expenses-users (84 members)
= Role: User
[Assign]
> Fabrikam Expenses › Properties
= Assignment required?: Yes
= Visible to users?: Yes
:::

**Assignment required: Yes** is what makes only the group get in. With "No", any user in the tenant can sign in to the application. Then, with the test user, open `https://myapps.microsoft.com` or the application URL and check they get in. The **Test** button on the SAML page works too, but it tests with your account and you are an administrator: that is not the test that matters.

## 4. When they can't get in

:::ui Entra admin center · Sign-in logs › Details
> Sign-in logs › laura.prado@contoso.com › Fabrikam Expenses › 22/10/2026 10:02
= Status: Failure
= Error code: AADSTS50105
= Failure reason: Your administrator has configured the application Fabrikam Expenses to block users unless they are specifically granted ('assigned') access to the application.
[Copy] [Troubleshoot]
:::

The three you will see almost every time:

| Code | What it means | What you do |
|---|---|---|
| **AADSTS50105** | The user is not assigned | Check they are in `sg-app-expenses-users` (and that the group is a security group, not an unsynced dynamic M365 group) |
| **AADSTS700016 / 50011** | The identifier or reply URL the application sends do not match Entra's | Compare character by character with what the vendor has configured (`http` vs `https`, trailing slash) |
| **AADSTS7500529 / "The signing certificate…"** | The vendor has the old certificate | Send the new one or the metadata URL; happens right when it expires |

If Entra says **Success** and the error comes from the application ("user not found", "invalid NameID"), the problem is in the claim: the vendor expects the email and receives the UPN, or the other way round. The **My Apps Secure Sign-in** browser extension or the **Test** button show the SAML assertion that is sent, claim by claim.

## 5. What you review each month

- SAML certificates expiring in under 90 days: `Enterprise applications → "Certificate expiration" filter`, or repo 20 on my GitHub, which lists them with a calendar.
- Applications with **Assignment required: No** that should have it.
- Applications without an owner: when it breaks, nobody will know whom to call.
- User consents to new applications (`Enterprise applications → Consent and permissions`).

## Next steps

- **OIDC** instead of SAML for modern applications: done in **App registrations**, with redirect URIs and scopes instead of ACS and claims. The Microsoft Graph guide uses one.
- **SCIM provisioning**: so that joining and leaving the group creates and disables the account in the application. It closes the loop with the Level 1 Active Directory guide.
- Add the application to a specific Conditional Access policy (previous guide) if it must always require MFA, even on a compliant device.
""")

# ---------------------------------------------------------------- L3 · Grafana
g(slug="grafana-origen-de-datos-primer-panel-y-alerta-al-canal", topic="grafana", date="2026-10-22",
  title_es="Grafana: un origen de datos, el primer panel y una alerta que avisa al canal del equipo",
  title_en="Grafana: a data source, your first dashboard and an alert that notifies the team channel",
  dek_es="Prometheus con node_exporter en los servidores, el panel de disco y CPU que mira todo el equipo, y la regla de alerta que llega a Teams antes de que llame el usuario.",
  dek_en="Prometheus with node_exporter on the servers, the disk and CPU dashboard the whole team looks at, and the alert rule that reaches Teams before the user calls.",
  es="""
## Qué vas a conseguir

Un panel con el estado de los servidores (disco, CPU, memoria, servicios caídos) que se abre en la pantalla de la sala del equipo, y una alerta de "disco por encima del 85 %" que llega al canal de Teams con el nombre del servidor y el valor. Lo que se mide se arregla antes.

## Antes de empezar

- El Grafana de la guía de Docker ya en marcha (o uno nuevo con el mismo Compose).
- Puerto 9100 abierto en los servidores hacia el servidor de herramientas (node_exporter) y 9090 solo en local.
- Un **webhook entrante** en el canal de Teams del equipo (Workflows → "Post to a channel when a webhook request is received"); la URL es un secreto.

## 1. Prometheus y node_exporter

Grafana pinta; alguien tiene que recoger. Añade Prometheus al Compose y el exportador a los servidores:

:::term docker-compose.yml (fragmento)
  prometheus:
    image: prom/prometheus:v2.55.0
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml:ro
      - prom-data:/prometheus
    command: ["--config.file=/etc/prometheus/prometheus.yml", "--storage.tsdb.retention.time=90d"]
    ports: ["127.0.0.1:9090:9090"]
:::

:::term prometheus.yml
global:
  scrape_interval: 30s
scrape_configs:
  - job_name: linux
    static_configs:
      - targets:
          - srv-web-01.contoso.local:9100
          - srv-web-02.contoso.local:9100
          - srv-db-01.contoso.local:9100
        labels: { site: madrid }
:::

:::term bash · srv-web-01 (o con Ansible en todos)
$ sudo useradd -rs /bin/false node_exporter
$ curl -sL https://github.com/prometheus/node_exporter/releases/download/v1.8.2/node_exporter-1.8.2.linux-amd64.tar.gz | sudo tar xz -C /usr/local/bin --strip-components=1 --wildcards '*/node_exporter'
$ sudo tee /etc/systemd/system/node_exporter.service >/dev/null <<'EOF'
[Unit]
Description=Prometheus Node Exporter
After=network.target
[Service]
User=node_exporter
ExecStart=/usr/local/bin/node_exporter --collector.systemd
[Install]
WantedBy=multi-user.target
EOF
$ sudo systemctl enable --now node_exporter
$ sudo firewall-cmd --add-port=9100/tcp --permanent && sudo firewall-cmd --reload
$ curl -s localhost:9100/metrics | grep -E '^node_filesystem_avail_bytes.*mountpoint="/"'
node_filesystem_avail_bytes{device="/dev/mapper/rhel-root",fstype="xfs",mountpoint="/"} 2.0401152e+10
:::

En `http://localhost:9090/targets` (desde el servidor de herramientas, o por túnel SSH) los tres deben estar en **UP**. Si uno está en DOWN con `connection refused`, es el firewall del servidor; con `context deadline exceeded`, DNS o ruta.

## 2. El origen de datos y el primer panel

:::ui Grafana · Connections
> Connections › Data sources › Add data source › Prometheus
= Name: Prometheus
= Prometheus server URL: http://prometheus:9090
[Save & test]
Successfully queried the Prometheus API.
:::

:::ui Grafana · New dashboard › Add visualization
> Dashboards › New › New dashboard › Add visualization › Prometheus
= Query A: 100 * (1 - node_filesystem_avail_bytes{mountpoint="/"} / node_filesystem_size_bytes{mountpoint="/"})
= Legend: {{instance}}
= Visualization: Bar gauge
= Unit: Percent (0-100)
= Thresholds: 0 verde · 75 naranja · 85 rojo
= Title: Disco raíz usado (%)
[Apply] [Save dashboard]
:::

Tres paneles más y tienes el tablero del equipo: CPU `100 - avg by(instance)(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100`, memoria `100 * (1 - node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)` y servicios caídos `node_systemd_unit_state{state="failed"} == 1` como tabla. Guarda el dashboard y exporta su JSON al repo de Git: es la copia de seguridad.

> Consejo: en lugar de inventar paneles, importa el **1860 (Node Exporter Full)** desde `Dashboards → New → Import`. Es el tablero por servidor que usa medio mundo; el tuyo es la vista de flota.

## 3. El punto de contacto: Teams

:::ui Grafana · Alerting › Contact points
> Alerting › Contact points › Create contact point
= Name: teams-it-ops
= Integration: Microsoft Teams
= URL: https://prod-xx.westeurope.logic.azure.com/workflows/… (webhook del canal)
= Title: {{ .CommonLabels.alertname }} · {{ .CommonLabels.instance }}
[Test] [Save contact point]
> Alerting › Notification policies › Default policy
= Default contact point: teams-it-ops
= Group by: alertname, instance
:::

Pulsa **Test** y mira el canal antes de seguir. Si no llega, el 95 % de las veces es la URL del webhook o que el flujo de Teams está desactivado.

## 4. La regla de alerta

:::ui Grafana · Alerting › Alert rules
> Alerting › Alert rules › New alert rule
= Name: Disco raíz > 85 %
= Query A: 100 * (1 - node_filesystem_avail_bytes{mountpoint="/"} / node_filesystem_size_bytes{mountpoint="/"})
= Expression B: Reduce · Last · A
= Expression C: Threshold · B IS ABOVE 85
= Folder: Infraestructura · Evaluation group: cada 1m · Pending period: 10m
= Labels: severity=warning, team=it-ops
= Summary: {{ $labels.instance }} tiene el disco raíz al {{ $values.B | printf "%.0f" }} %
= Runbook URL: https://wiki.contoso.local/it/runbooks/disco-lleno
[Save rule and exit]
:::

El **pending period** de 10 minutos es lo que evita una alerta por un pico de un `tar`. La etiqueta `severity` y la **Runbook URL** (la página de Confluence del Nivel 2) son lo que convierte una notificación en algo accionable a las tres de la mañana. Comprueba que funciona bajando el umbral a 1 % un minuto y volviéndolo a subir.

## 5. Lo que revisas cada mes

- `Alerting → Alert rules`: reglas en estado **Error** o **NoData** (un servidor que ya no existe sigue en el inventario de Prometheus).
- Alertas que saltaron más de diez veces en el mes y nadie trató: o sobra la alerta o falta el arreglo.
- Retención de Prometheus frente al disco (`du -sh` del volumen `prom-data`).
- Exportar los dashboards cambiados al repo.

## Siguientes pasos

- Windows: **windows_exporter** da lo mismo que node_exporter (disco, CPU, servicios); el mismo panel sirve con otro `job_name`.
- Añade Elasticsearch (guía de ELK) como origen de datos: la gráfica de errores por hora junto a la de CPU del mismo servidor.
- **Grafana OnCall** o la integración con la herramienta de guardia que uses para que las alertas `severity=critical` llamen por teléfono y las `warning` se queden en Teams.
""",
  en="""
## What you'll get

A dashboard with the state of the servers (disk, CPU, memory, failed services) that opens on the team room screen, and a "disk above 85%" alert that lands in the team's Teams channel with the server name and value. What gets measured gets fixed sooner.

## Before you start

- The Grafana from the Docker guide already running (or a new one with the same Compose).
- Port 9100 open on the servers towards the tools server (node_exporter) and 9090 local only.
- An **incoming webhook** in the team's Teams channel (Workflows → "Post to a channel when a webhook request is received"); the URL is a secret.

## 1. Prometheus and node_exporter

Grafana draws; someone has to collect. Add Prometheus to the Compose and the exporter to the servers:

:::term docker-compose.yml (fragment)
  prometheus:
    image: prom/prometheus:v2.55.0
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml:ro
      - prom-data:/prometheus
    command: ["--config.file=/etc/prometheus/prometheus.yml", "--storage.tsdb.retention.time=90d"]
    ports: ["127.0.0.1:9090:9090"]
:::

:::term prometheus.yml
global:
  scrape_interval: 30s
scrape_configs:
  - job_name: linux
    static_configs:
      - targets:
          - srv-web-01.contoso.local:9100
          - srv-web-02.contoso.local:9100
          - srv-db-01.contoso.local:9100
        labels: { site: madrid }
:::

:::term bash · srv-web-01 (or with Ansible on all of them)
$ sudo useradd -rs /bin/false node_exporter
$ curl -sL https://github.com/prometheus/node_exporter/releases/download/v1.8.2/node_exporter-1.8.2.linux-amd64.tar.gz | sudo tar xz -C /usr/local/bin --strip-components=1 --wildcards '*/node_exporter'
$ sudo tee /etc/systemd/system/node_exporter.service >/dev/null <<'EOF'
[Unit]
Description=Prometheus Node Exporter
After=network.target
[Service]
User=node_exporter
ExecStart=/usr/local/bin/node_exporter --collector.systemd
[Install]
WantedBy=multi-user.target
EOF
$ sudo systemctl enable --now node_exporter
$ sudo firewall-cmd --add-port=9100/tcp --permanent && sudo firewall-cmd --reload
$ curl -s localhost:9100/metrics | grep -E '^node_filesystem_avail_bytes.*mountpoint="/"'
node_filesystem_avail_bytes{device="/dev/mapper/rhel-root",fstype="xfs",mountpoint="/"} 2.0401152e+10
:::

At `http://localhost:9090/targets` (from the tools server, or over an SSH tunnel) all three must be **UP**. If one is DOWN with `connection refused`, it is the server firewall; with `context deadline exceeded`, DNS or routing.

## 2. The data source and the first panel

:::ui Grafana · Connections
> Connections › Data sources › Add data source › Prometheus
= Name: Prometheus
= Prometheus server URL: http://prometheus:9090
[Save & test]
Successfully queried the Prometheus API.
:::

:::ui Grafana · New dashboard › Add visualization
> Dashboards › New › New dashboard › Add visualization › Prometheus
= Query A: 100 * (1 - node_filesystem_avail_bytes{mountpoint="/"} / node_filesystem_size_bytes{mountpoint="/"})
= Legend: {{instance}}
= Visualization: Bar gauge
= Unit: Percent (0-100)
= Thresholds: 0 green · 75 orange · 85 red
= Title: Root disk used (%)
[Apply] [Save dashboard]
:::

Three more panels and you have the team board: CPU `100 - avg by(instance)(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100`, memory `100 * (1 - node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)` and failed services `node_systemd_unit_state{state="failed"} == 1` as a table. Save the dashboard and export its JSON to the Git repo: that is the backup.

> Tip: instead of inventing panels, import **1860 (Node Exporter Full)** from `Dashboards → New → Import`. It is the per-server board half the world uses; yours is the fleet view.

## 3. The contact point: Teams

:::ui Grafana · Alerting › Contact points
> Alerting › Contact points › Create contact point
= Name: teams-it-ops
= Integration: Microsoft Teams
= URL: https://prod-xx.westeurope.logic.azure.com/workflows/… (channel webhook)
= Title: {{ .CommonLabels.alertname }} · {{ .CommonLabels.instance }}
[Test] [Save contact point]
> Alerting › Notification policies › Default policy
= Default contact point: teams-it-ops
= Group by: alertname, instance
:::

Press **Test** and look at the channel before going on. If nothing arrives, 95% of the time it is the webhook URL or the Teams workflow is turned off.

## 4. The alert rule

:::ui Grafana · Alerting › Alert rules
> Alerting › Alert rules › New alert rule
= Name: Root disk > 85%
= Query A: 100 * (1 - node_filesystem_avail_bytes{mountpoint="/"} / node_filesystem_size_bytes{mountpoint="/"})
= Expression B: Reduce · Last · A
= Expression C: Threshold · B IS ABOVE 85
= Folder: Infrastructure · Evaluation group: every 1m · Pending period: 10m
= Labels: severity=warning, team=it-ops
= Summary: {{ $labels.instance }} root disk is at {{ $values.B | printf "%.0f" }}%
= Runbook URL: https://wiki.contoso.local/it/runbooks/disk-full
[Save rule and exit]
:::

The 10-minute **pending period** is what avoids an alert for a spike from a `tar`. The `severity` label and the **Runbook URL** (the Level 2 Confluence page) are what turn a notification into something actionable at three in the morning. Check it works by dropping the threshold to 1% for a minute and raising it back.

## 5. What you review each month

- `Alerting → Alert rules`: rules in **Error** or **NoData** state (a server that no longer exists is still in the Prometheus inventory).
- Alerts that fired more than ten times in the month and nobody acted on: either the alert is surplus or the fix is missing.
- Prometheus retention against disk (`du -sh` of the `prom-data` volume).
- Export changed dashboards to the repo.

## Next steps

- Windows: **windows_exporter** gives the same as node_exporter (disk, CPU, services); the same panel works with another `job_name`.
- Add Elasticsearch (ELK guide) as a data source: the errors-per-hour chart next to the CPU chart of the same server.
- **Grafana OnCall** or the integration with whatever on-call tool you use, so `severity=critical` alerts phone someone and `warning` stays in Teams.
""")

# ---------------------------------------------------------------- L3 · Hyper-V
g(slug="hyper-v-crear-vm-conmutador-virtual-puntos-de-control-y-exportar", topic="hyper-v", date="2026-10-22",
  title_es="Hyper-V: crear una máquina virtual, el conmutador virtual, puntos de control y exportación",
  title_en="Hyper-V: creating a virtual machine, the virtual switch, checkpoints and export",
  dek_es="El rol en Windows Server, el conmutador externo que no te deja sin red, una VM de generación 2 con PowerShell, puntos de control antes de un cambio y la exportación como copia fría.",
  dek_en="The role on Windows Server, the external switch that doesn't cut your network, a generation 2 VM with PowerShell, checkpoints before a change and export as a cold backup.",
  es="""
## Qué vas a conseguir

Un servidor Windows con Hyper-V donde crear máquinas virtuales de pruebas y de producción pequeña con PowerShell en lugar de a golpe de asistente, con puntos de control antes de cada cambio y una exportación semanal a otro disco.

## Antes de empezar

- Windows Server 2022/2025 con la virtualización activada en la BIOS/UEFI y dos interfaces de red si puede ser: una para gestión, otra para las VMs.
- Un volumen aparte para las VMs (`D:\\VMs`), no el disco del sistema.
- Las ISO de los sistemas que vas a instalar en `D:\\ISO`.

## 1. Instalar el rol

:::term PowerShell · srv-hv-01 (administrador)
$ Install-WindowsFeature -Name Hyper-V -IncludeManagementTools -Restart
Success Restart Needed Exit Code      Feature Result
------- -------------- ---------      --------------
True    Yes            SuccessRest... {Hyper-V, Hyper-V Module for Windows PowerShell, ...}
# tras el reinicio
$ Get-VMHost | Select-Object Name, VirtualMachinePath, VirtualHardDiskPath
Name       VirtualMachinePath                      VirtualHardDiskPath
----       ------------------                      -------------------
SRV-HV-01  C:\\ProgramData\\Microsoft\\Windows\\Hyper-V  C:\\Users\\Public\\Documents\\Hyper-V\\Virtual Hard Disks
$ Set-VMHost -VirtualMachinePath D:\\VMs -VirtualHardDiskPath D:\\VMs\\Disks
:::

Cambia las rutas por defecto antes de crear la primera VM: luego cuesta mover.

## 2. El conmutador virtual

:::term PowerShell · srv-hv-01
$ Get-NetAdapter | Select-Object Name, Status, LinkSpeed
Name   Status LinkSpeed
----   ------ ---------
MGMT   Up     1 Gbps
VMNET  Up     10 Gbps
$ New-VMSwitch -Name "vSwitch-LAN" -NetAdapterName "VMNET" -AllowManagementOS $false
Name        SwitchType NetAdapterInterfaceDescription
----        ---------- ------------------------------
vSwitch-LAN External   Intel(R) Ethernet Controller X710
$ New-VMSwitch -Name "vSwitch-Lab" -SwitchType Internal
:::

! Si solo tienes una tarjeta de red, el conmutador externo tiene que llevar `-AllowManagementOS $true`; si no, el servidor se queda sin red en el momento de crearlo y pierdes la sesión remota. Hazlo desde la consola física o con iDRAC/iLO.

El conmutador **Interno** (`vSwitch-Lab`) es para pruebas que no deben tocar la red de la empresa: las VMs se ven entre sí y con el host, nada más.

## 3. Crear la VM con PowerShell

:::term PowerShell · srv-hv-01
$ $vm = New-VM -Name "srv-test-01" -Generation 2 -MemoryStartupBytes 4GB -NewVHDPath "D:\\VMs\\Disks\\srv-test-01.vhdx" -NewVHDSizeBytes 80GB -SwitchName "vSwitch-LAN"
$ Set-VM -VM $vm -ProcessorCount 2 -DynamicMemory -MemoryMinimumBytes 2GB -MemoryMaximumBytes 8GB -AutomaticStartAction StartIfRunning -AutomaticStopAction ShutDown -CheckpointType Production
$ Add-VMDvdDrive -VM $vm -Path "D:\\ISO\\WindowsServer2025.iso"
$ Set-VMFirmware -VM $vm -FirstBootDevice (Get-VMDvdDrive -VM $vm) -EnableSecureBoot On
$ Set-VMKeyProtector -VM $vm -NewLocalKeyProtector; Enable-VMTPM -VM $vm
$ Start-VM -VM $vm; vmconnect.exe localhost srv-test-01
$ Get-VM | Format-Table Name, State, CPUUsage, MemoryAssigned, Uptime, Status
Name         State   CPUUsage MemoryAssigned Uptime   Status
----         -----   -------- -------------- ------   ------
srv-test-01  Running 12       4294967296     00:02:11 Operating normally
:::

Generación 2 con **Secure Boot** y **TPM** virtual es lo que pide Windows 11 y Server 2025; para Linux cambia la plantilla: `Set-VMFirmware -SecureBootTemplate MicrosoftUEFICertificateAuthority`. `CheckpointType Production` hace que los puntos de control usen VSS dentro del invitado: consistentes con las aplicaciones, no solo con el disco.

## 4. Puntos de control antes de un cambio

:::term PowerShell · srv-hv-01
$ Checkpoint-VM -Name "srv-test-01" -SnapshotName "antes-parche-2026-10-22"
$ Get-VMSnapshot -VMName "srv-test-01" | Format-Table Name, CreationTime, ParentSnapshotName
Name                     CreationTime        ParentSnapshotName
----                     ------------        ------------------
antes-parche-2026-10-22  22/10/2026 9:40:12
# si el cambio sale mal:
$ Restore-VMSnapshot -Name "antes-parche-2026-10-22" -VMName "srv-test-01" -Confirm:$false
# si sale bien, en cuanto esté comprobado:
$ Remove-VMSnapshot -VMName "srv-test-01" -Name "antes-parche-2026-10-22"
:::

Un punto de control no es una copia de seguridad: es un disco diferencial que crece y ralentiza la VM mientras exista. La regla es **crear antes del cambio, borrar en cuanto se valide**, nunca más de unos días. `Get-VM | Get-VMSnapshot | Where-Object CreationTime -lt (Get-Date).AddDays(-7)` lista los olvidados.

## 5. Exportar: la copia fría

:::term PowerShell · srv-hv-01
$ Export-VM -Name "srv-test-01" -Path "E:\\Export\\$(Get-Date -Format yyyy-MM-dd)"
$ Get-ChildItem "E:\\Export\\2026-10-22\\srv-test-01" -Recurse -File | Measure-Object Length -Sum | Select-Object Count, @{n="GB";e={[math]::Round($_.Sum/1GB,1)}}
Count GB
----- --
    5 21,4
# importar en otro host (copia con nuevo ID para no chocar con la original):
$ Import-VM -Path "E:\\Export\\2026-10-22\\srv-test-01\\Virtual Machines\\<GUID>.vmcx" -Copy -GenerateNewId -VhdDestinationPath "D:\\VMs\\Disks"
:::

`Export-VM` funciona con la VM encendida y deja configuración, discos y puntos de control en una carpeta que se puede importar en cualquier otro Hyper-V. Programado en una tarea semanal hacia otro disco o un NAS, es la copia mínima de un host sin Veeam; con Veeam (Nivel 2), el agente hace esto mismo con deduplicación y retención.

## 6. Lo que revisas cada mes

- `Get-VM | Get-VMSnapshot`: puntos de control con más de una semana.
- `Get-VM | Where State -eq Running | Get-VMIntegrationService | Where Enabled -and -not PrimaryStatusDescription -eq 'OK'`: servicios de integración que no responden (normalmente, invitado sin actualizar).
- Espacio en `D:\\VMs` frente a la suma de los VHDX dinámicos: pueden crecer hasta su tamaño máximo sin avisar.
- Visor de eventos `Microsoft-Windows-Hyper-V-VMMS/Admin`: errores de puntos de control o de exportación.

## Siguientes pasos

- **Hyper-V Replica** hacia un segundo host: una copia de la VM a cinco minutos, con conmutación planificada; es el DR pequeño antes de un clúster.
- Un **clúster de conmutación por error** con almacenamiento compartido o S2D cuando las VMs sean de producción.
- La guía de vSphere hace lo mismo del otro lado; las ideas (snapshots cortos, exportación, host en mantenimiento) son las mismas con otros nombres.
""",
  en="""
## What you'll get

A Windows server with Hyper-V where you create test and small-production virtual machines with PowerShell instead of clicking through wizards, with checkpoints before every change and a weekly export to another disk.

## Before you start

- Windows Server 2022/2025 with virtualisation enabled in the BIOS/UEFI and, if possible, two network interfaces: one for management, one for the VMs.
- A separate volume for the VMs (`D:\\VMs`), not the system disk.
- The ISOs of the systems you will install in `D:\\ISO`.

## 1. Install the role

:::term PowerShell · srv-hv-01 (administrator)
$ Install-WindowsFeature -Name Hyper-V -IncludeManagementTools -Restart
Success Restart Needed Exit Code      Feature Result
------- -------------- ---------      --------------
True    Yes            SuccessRest... {Hyper-V, Hyper-V Module for Windows PowerShell, ...}
# after the reboot
$ Get-VMHost | Select-Object Name, VirtualMachinePath, VirtualHardDiskPath
Name       VirtualMachinePath                      VirtualHardDiskPath
----       ------------------                      -------------------
SRV-HV-01  C:\\ProgramData\\Microsoft\\Windows\\Hyper-V  C:\\Users\\Public\\Documents\\Hyper-V\\Virtual Hard Disks
$ Set-VMHost -VirtualMachinePath D:\\VMs -VirtualHardDiskPath D:\\VMs\\Disks
:::

Change the default paths before creating the first VM: moving later is painful.

## 2. The virtual switch

:::term PowerShell · srv-hv-01
$ Get-NetAdapter | Select-Object Name, Status, LinkSpeed
Name   Status LinkSpeed
----   ------ ---------
MGMT   Up     1 Gbps
VMNET  Up     10 Gbps
$ New-VMSwitch -Name "vSwitch-LAN" -NetAdapterName "VMNET" -AllowManagementOS $false
Name        SwitchType NetAdapterInterfaceDescription
----        ---------- ------------------------------
vSwitch-LAN External   Intel(R) Ethernet Controller X710
$ New-VMSwitch -Name "vSwitch-Lab" -SwitchType Internal
:::

! If you only have one network card, the external switch must carry `-AllowManagementOS $true`; otherwise the server loses its network the moment the switch is created and you lose the remote session. Do it from the physical console or through iDRAC/iLO.

The **Internal** switch (`vSwitch-Lab`) is for tests that must not touch the company network: the VMs see each other and the host, nothing else.

## 3. Create the VM with PowerShell

:::term PowerShell · srv-hv-01
$ $vm = New-VM -Name "srv-test-01" -Generation 2 -MemoryStartupBytes 4GB -NewVHDPath "D:\\VMs\\Disks\\srv-test-01.vhdx" -NewVHDSizeBytes 80GB -SwitchName "vSwitch-LAN"
$ Set-VM -VM $vm -ProcessorCount 2 -DynamicMemory -MemoryMinimumBytes 2GB -MemoryMaximumBytes 8GB -AutomaticStartAction StartIfRunning -AutomaticStopAction ShutDown -CheckpointType Production
$ Add-VMDvdDrive -VM $vm -Path "D:\\ISO\\WindowsServer2025.iso"
$ Set-VMFirmware -VM $vm -FirstBootDevice (Get-VMDvdDrive -VM $vm) -EnableSecureBoot On
$ Set-VMKeyProtector -VM $vm -NewLocalKeyProtector; Enable-VMTPM -VM $vm
$ Start-VM -VM $vm; vmconnect.exe localhost srv-test-01
$ Get-VM | Format-Table Name, State, CPUUsage, MemoryAssigned, Uptime, Status
Name         State   CPUUsage MemoryAssigned Uptime   Status
----         -----   -------- -------------- ------   ------
srv-test-01  Running 12       4294967296     00:02:11 Operating normally
:::

Generation 2 with **Secure Boot** and a virtual **TPM** is what Windows 11 and Server 2025 require; for Linux change the template: `Set-VMFirmware -SecureBootTemplate MicrosoftUEFICertificateAuthority`. `CheckpointType Production` makes checkpoints use VSS inside the guest: consistent with the applications, not just the disk.

## 4. Checkpoints before a change

:::term PowerShell · srv-hv-01
$ Checkpoint-VM -Name "srv-test-01" -SnapshotName "before-patch-2026-10-22"
$ Get-VMSnapshot -VMName "srv-test-01" | Format-Table Name, CreationTime, ParentSnapshotName
Name                     CreationTime        ParentSnapshotName
----                     ------------        ------------------
before-patch-2026-10-22  22/10/2026 9:40:12
# if the change goes wrong:
$ Restore-VMSnapshot -Name "before-patch-2026-10-22" -VMName "srv-test-01" -Confirm:$false
# if it goes well, as soon as it is verified:
$ Remove-VMSnapshot -VMName "srv-test-01" -Name "before-patch-2026-10-22"
:::

A checkpoint is not a backup: it is a differencing disk that grows and slows the VM down while it exists. The rule is **create before the change, delete as soon as it is validated**, never more than a few days. `Get-VM | Get-VMSnapshot | Where-Object CreationTime -lt (Get-Date).AddDays(-7)` lists the forgotten ones.

## 5. Export: the cold copy

:::term PowerShell · srv-hv-01
$ Export-VM -Name "srv-test-01" -Path "E:\\Export\\$(Get-Date -Format yyyy-MM-dd)"
$ Get-ChildItem "E:\\Export\\2026-10-22\\srv-test-01" -Recurse -File | Measure-Object Length -Sum | Select-Object Count, @{n="GB";e={[math]::Round($_.Sum/1GB,1)}}
Count GB
----- --
    5 21.4
# import on another host (copy with a new ID so it doesn't clash with the original):
$ Import-VM -Path "E:\\Export\\2026-10-22\\srv-test-01\\Virtual Machines\\<GUID>.vmcx" -Copy -GenerateNewId -VhdDestinationPath "D:\\VMs\\Disks"
:::

`Export-VM` works with the VM running and leaves configuration, disks and checkpoints in a folder that can be imported on any other Hyper-V. Scheduled as a weekly task to another disk or a NAS, it is the minimum backup of a host without Veeam; with Veeam (Level 2), the agent does the same with deduplication and retention.

## 6. What you review each month

- `Get-VM | Get-VMSnapshot`: checkpoints older than a week.
- `Get-VM | Where State -eq Running | Get-VMIntegrationService | Where Enabled -and -not PrimaryStatusDescription -eq 'OK'`: integration services not responding (usually an un-updated guest).
- Space on `D:\\VMs` against the sum of the dynamic VHDXs: they can grow to their maximum size without warning.
- Event Viewer `Microsoft-Windows-Hyper-V-VMMS/Admin`: checkpoint or export errors.

## Next steps

- **Hyper-V Replica** to a second host: a copy of the VM five minutes behind, with planned failover; it is the small DR before a cluster.
- A **failover cluster** with shared storage or S2D when the VMs are production.
- The vSphere guide does the same from the other side; the ideas (short snapshots, export, host in maintenance) are the same with other names.
""")

# ---------------------------------------------------------------- L3 · Intune multiplatform
g(slug="intune-perfiles-y-cumplimiento-en-windows-macos-ios-android-y-dispositivo-que-no-cumple", topic="intune", date="2026-10-22",
  title_es="Intune en Windows, macOS, iOS y Android: perfiles de configuración, cumplimiento y un dispositivo que no cumple",
  title_en="Intune on Windows, macOS, iOS and Android: configuration profiles, compliance and a device that is non-compliant",
  dek_es="La estructura de grupos y filtros que vale para las cuatro plataformas, una política de cumplimiento por sistema, el perfil de configuración con el catálogo de ajustes y la rutina para el dispositivo que aparece en rojo.",
  dek_en="The group and filter structure that works for all four platforms, one compliance policy per OS, the configuration profile with the Settings Catalog, and the routine for the device that shows up red.",
  es="""
## Qué vas a conseguir

Que un dispositivo de cualquier plataforma, al enrolarse (guías de Android, iPhone y Windows del Nivel 1, Jamf aparte), reciba su cumplimiento y su configuración sin que nadie lo asigne a mano, y que Conditional Access (guía anterior) pueda confiar en el estado **Conforme**. Y el procedimiento de siete minutos para un dispositivo **No conforme**.

## Antes de empezar

- Rol **Intune Administrator** y, para el enrolamiento de Apple, el certificado APNs y el token de Apple Business Manager ya configurados (`Dispositivos → Inscripción`).
- Grupos de Entra ID: uno de usuarios por tipo (`sg-intune-users-standard`, `sg-intune-users-vip`) y los **grupos dinámicos de dispositivos** o los **filtros** que separan plataformas.
- Un dispositivo de prueba por plataforma, enrolado con un usuario que no sea tú.

## 1. Grupos y filtros: la base

:::ui Intune · Filtros
> Administración de inquilinos › Filtros › Crear › Dispositivos administrados
= Nombre: f-windows-corp
= Plataforma: Windows 10 and later
= Regla: (device.deviceOwnership -eq "Corporate")
[Crear]
:::

Crea cuatro filtros (`f-windows-corp`, `f-macos-corp`, `f-ios-corp`, `f-android-corp`) y asigna todo a **Todos los usuarios** o a `sg-intune-users-*` con el filtro de plataforma. Es más rápido y más claro que un grupo dinámico de dispositivos por cada combinación, y los filtros se evalúan en el momento del check-in, no cada media hora.

## 2. Una política de cumplimiento por plataforma

:::ui Intune · Cumplimiento
> Dispositivos › Cumplimiento › Crear directiva › Windows 10 and later
= Nombre: Compliance - Windows
Estado del dispositivo
[x] Requerir BitLocker
[x] Requerir que el arranque seguro esté habilitado
[x] Requerir la integridad de código
Propiedades del dispositivo
= Versión mínima del SO: 10.0.22631.4317
Seguridad del sistema
[x] Requerir una contraseña para desbloquear
[x] Firewall · [x] Antivirus · [x] Antispyware · [x] Microsoft Defender Antimalware actualizado
Acciones en caso de incumplimiento
= Marcar dispositivo como no conforme: Inmediatamente
= Enviar correo al usuario final: 1 día · plantilla "Tu equipo no cumple"
= Retirar dispositivo no conforme: 30 días
Asignaciones
= Todos los usuarios · Filtro: incluir f-windows-corp
[Crear]
:::

Las otras tres con el mismo esqueleto: **macOS** (FileVault, firewall, versión mínima, integridad del sistema), **iOS/iPadOS** (código de acceso, sin jailbreak, versión mínima), **Android Enterprise** (código, sin root, nivel de parche de seguridad no anterior a X, Play Protect). La acción de "marcar inmediatamente" es la que alimenta Conditional Access; la **gracia de un día** con correo evita que un parche de madrugada bloquee a la gente a las 9:00.

> Consejo: en `Dispositivos → Cumplimiento → Configuración de la directiva de cumplimiento`, deja **Marcar dispositivos sin directiva de cumplimiento como: No conforme**. Si no, un dispositivo al que no le llega ninguna política cuenta como conforme y entra.

## 3. El perfil de configuración con el catálogo de ajustes

:::ui Intune · Configuración
> Dispositivos › Configuración › Crear › Nueva directiva › Windows 10 and later › Catálogo de configuración
= Nombre: Config - Windows - Baseline corp
Catálogo de configuración
> Agregar configuración › buscar "bitlocker"
[x] BitLocker › Require Device Encryption: Habilitado
[x] BitLocker › Allow Standard User Encryption: Habilitado
> Agregar configuración › buscar "screen saver"
[x] Local Policies Security Options › Interactive Logon Machine Inactivity Limit: 600
> Agregar configuración › buscar "Windows Hello"
[x] Windows Hello For Business › Use Windows Hello For Business: true
Asignaciones
= Todos los usuarios · Filtro: incluir f-windows-corp
[Crear]
:::

El **catálogo de configuración** sustituye a las plantillas antiguas y, para macOS, a buena parte de los `.mobileconfig` manuales: es el mismo cuadro de búsqueda en las cuatro plataformas. Un perfil por tema (cifrado, bloqueo, Wi-Fi, certificados) es más fácil de diagnosticar que uno con cien ajustes. Para iOS y Android, el equivalente son las **restricciones de dispositivo** y, para Wi-Fi/VPN/certificados, sus plantillas propias (la guía de NDES usa una).

## 4. El dispositivo que no cumple

:::ui Intune · Dispositivos
> Dispositivos › Todos los dispositivos › LAPTOP-7F2K9Q
= Usuario principal: laura.prado@contoso.com · Windows 11 23H2 · Corporativo · Último check-in: 22/10/2026 09:12
= Cumplimiento: No conforme
> Cumplimiento del dispositivo › Compliance - Windows
= Requerir BitLocker: Error
= Versión mínima del SO: Conforme
= Firewall: Conforme
[Sincronizar] [Reiniciar] [Recopilar diagnósticos]
:::

Siete minutos, en este orden:

1. **Qué regla falla** (la pantalla de arriba). No es "el equipo", es BitLocker.
2. **Sincronizar** desde el portal y, en el equipo, `Configuración → Cuentas → Acceso a trabajo → Información → Sincronizar`. Muchos "no conforme" son estado antiguo: el equipo lleva tres días apagado.
3. Si sigue, mira la **causa** en el equipo: en este caso `manage-bde -status C:` dice `Protection Off` porque se suspendió para una actualización de firmware y nadie la reanudó: `manage-bde -protectors -enable C:`.
4. Comprueba en el **Visor de eventos** `Microsoft-Windows-DeviceManagement-Enterprise-Diagnostics-Provider/Admin` que el check-in llega sin errores 0x8018xxxx.
5. Vuelve a sincronizar y espera al siguiente ciclo (hasta 8 horas; `Sincronizar` lo adelanta). Ya en **Conforme**, Conditional Access deja pasar.

Para macOS, `sudo profiles list` y el `Portal de empresa → Comprobar estado`; para iOS/Android, el mismo botón en el Portal de empresa y, si no hay check-in desde hace días, el dispositivo está apagado, sin red o el usuario quitó la app.

## 5. Lo que revisas cada mes

- **Informes → Cumplimiento del dispositivo**: no conformes por regla, no por dispositivo. Si el 30 % falla por versión mínima, el problema es el anillo de actualizaciones, no 60 tickets.
- Dispositivos **sin check-in en 30 días**: retirar o investigar (`Todos los dispositivos → filtro Último check-in`).
- Perfiles con **Error** o **Conflicto** en `Configuración → la directiva → Estado del dispositivo`: dos perfiles que fijan el mismo ajuste con valores distintos.
- Que las versiones mínimas de las políticas de cumplimiento se han subido tras el martes de parches, con el día de gracia por delante.

## Siguientes pasos

- **Autopilot** (Windows) y **ADE** (Apple): que el dispositivo salga de la caja y termine en este estado sin pasar por IT; la guía de MECM del Nivel 2 explica el camino intermedio con co-administración.
- **Líneas base de seguridad** (`Seguridad de los puntos de conexión → Líneas base`) para no inventar la configuración desde cero; compara con tu perfil antes de aplicarla.
- La guía de Intune EPM quita el administrador local a los usuarios una vez que el cumplimiento y la configuración están estables.
""",
  en="""
## What you'll get

A device on any platform that, once enrolled (Level 1 Android, iPhone and Windows guides; Jamf aside), receives its compliance and configuration without anyone assigning it by hand, so that Conditional Access (previous guide) can trust the **Compliant** state. Plus the seven-minute procedure for a device that is **Not compliant**.

## Before you start

- The **Intune Administrator** role and, for Apple enrolment, the APNs certificate and the Apple Business Manager token already configured (`Devices → Enrollment`).
- Entra ID groups: one of users per type (`sg-intune-users-standard`, `sg-intune-users-vip`) and the **dynamic device groups** or **filters** that separate platforms.
- One test device per platform, enrolled with a user who is not you.

## 1. Groups and filters: the foundation

:::ui Intune · Filters
> Tenant administration › Filters › Create › Managed devices
= Name: f-windows-corp
= Platform: Windows 10 and later
= Rule: (device.deviceOwnership -eq "Corporate")
[Create]
:::

Create four filters (`f-windows-corp`, `f-macos-corp`, `f-ios-corp`, `f-android-corp`) and assign everything to **All users** or to `sg-intune-users-*` with the platform filter. It is faster and clearer than one dynamic device group per combination, and filters are evaluated at check-in time, not every half hour.

## 2. One compliance policy per platform

:::ui Intune · Compliance
> Devices › Compliance › Create policy › Windows 10 and later
= Name: Compliance - Windows
Device Health
[x] Require BitLocker
[x] Require Secure Boot to be enabled
[x] Require code integrity
Device Properties
= Minimum OS version: 10.0.22631.4317
System Security
[x] Require a password to unlock
[x] Firewall · [x] Antivirus · [x] Antispyware · [x] Microsoft Defender Antimalware up to date
Actions for noncompliance
= Mark device noncompliant: Immediately
= Send email to end user: 1 day · template "Your device is not compliant"
= Retire the noncompliant device: 30 days
Assignments
= All users · Filter: include f-windows-corp
[Create]
:::

The other three with the same skeleton: **macOS** (FileVault, firewall, minimum version, system integrity), **iOS/iPadOS** (passcode, no jailbreak, minimum version), **Android Enterprise** (passcode, no root, security patch level not before X, Play Protect). The "mark immediately" action is what feeds Conditional Access; the **one-day grace** with an email stops a late-night patch from locking people out at 9:00.

> Tip: in `Devices → Compliance → Compliance policy settings`, keep **Mark devices with no compliance policy assigned as: Not compliant**. Otherwise a device that receives no policy counts as compliant and gets in.

## 3. The configuration profile with the Settings Catalog

:::ui Intune · Configuration
> Devices › Configuration › Create › New policy › Windows 10 and later › Settings catalog
= Name: Config - Windows - Baseline corp
Settings catalog
> Add settings › search "bitlocker"
[x] BitLocker › Require Device Encryption: Enabled
[x] BitLocker › Allow Standard User Encryption: Enabled
> Add settings › search "screen saver"
[x] Local Policies Security Options › Interactive Logon Machine Inactivity Limit: 600
> Add settings › search "Windows Hello"
[x] Windows Hello For Business › Use Windows Hello For Business: true
Assignments
= All users · Filter: include f-windows-corp
[Create]
:::

The **Settings Catalog** replaces the old templates and, for macOS, a good part of the manual `.mobileconfig` files: it is the same search box across all four platforms. One profile per topic (encryption, lock, Wi-Fi, certificates) is easier to diagnose than one with a hundred settings. For iOS and Android, the equivalent is **device restrictions** and, for Wi-Fi/VPN/certificates, their own templates (the NDES guide uses one).

## 4. The device that is non-compliant

:::ui Intune · Devices
> Devices › All devices › LAPTOP-7F2K9Q
= Primary user: laura.prado@contoso.com · Windows 11 23H2 · Corporate · Last check-in: 22/10/2026 09:12
= Compliance: Not compliant
> Device compliance › Compliance - Windows
= Require BitLocker: Error
= Minimum OS version: Compliant
= Firewall: Compliant
[Sync] [Restart] [Collect diagnostics]
:::

Seven minutes, in this order:

1. **Which rule fails** (the screen above). It is not "the laptop", it is BitLocker.
2. **Sync** from the portal and, on the device, `Settings → Accounts → Access work or school → Info → Sync`. Many "not compliant" are stale state: the laptop was off for three days.
3. If it persists, look at the **cause** on the device: here `manage-bde -status C:` says `Protection Off` because it was suspended for a firmware update and nobody resumed it: `manage-bde -protectors -enable C:`.
4. Check in **Event Viewer** `Microsoft-Windows-DeviceManagement-Enterprise-Diagnostics-Provider/Admin` that check-in arrives without 0x8018xxxx errors.
5. Sync again and wait for the next cycle (up to 8 hours; `Sync` brings it forward). Once **Compliant**, Conditional Access lets it through.

For macOS, `sudo profiles list` and `Company Portal → Check status`; for iOS/Android, the same button in Company Portal and, if there has been no check-in for days, the device is off, offline or the user removed the app.

## 5. What you review each month

- **Reports → Device compliance**: non-compliant by rule, not by device. If 30% fail on minimum version, the problem is the update ring, not 60 tickets.
- Devices **with no check-in in 30 days**: retire or investigate (`All devices → Last check-in filter`).
- Profiles with **Error** or **Conflict** in `Configuration → the policy → Device status`: two profiles setting the same value differently.
- That the minimum versions in the compliance policies were raised after Patch Tuesday, with the grace day ahead.

## Next steps

- **Autopilot** (Windows) and **ADE** (Apple): the device comes out of the box and ends up in this state without passing through IT; the Level 2 MECM guide explains the intermediate path with co-management.
- **Security baselines** (`Endpoint security → Baselines`) so you don't invent the configuration from scratch; compare with your profile before applying.
- The Intune EPM guide removes local admin from users once compliance and configuration are stable.
""")

# ---------------------------------------------------------------- L3 · Intune EPM
g(slug="intune-epm-quitar-administrador-local-y-elevar-solo-lo-necesario", topic="intune-epm", date="2026-10-22",
  title_es="Intune EPM: quitar el administrador local y elevar solo lo que hace falta",
  title_en="Intune EPM: removing local admin and elevating only what is needed",
  dek_es="La política de elevación, las reglas por aplicación con hash o certificado, el modo de solo informe para descubrir qué eleva la gente, y el informe que convence al negocio de que nadie necesita ser administrador.",
  dek_en="The elevation policy, per-application rules by hash or certificate, report-only mode to discover what people actually elevate, and the report that convinces the business nobody needs to be an administrator.",
  es="""
## Qué vas a conseguir

Que los usuarios dejen de ser administradores locales de su equipo sin que IT reciba una avalancha de tickets: Endpoint Privilege Management (EPM) eleva solo la aplicación concreta (el instalador de un driver, la herramienta de un proveedor) con una regla, con o sin aprobación, y deja registro de todo. Al terminar tendrás la política base, tres reglas y el informe para la reunión.

## Antes de empezar

- Licencia **Intune Suite** o el complemento **Endpoint Privilege Management** para los usuarios afectados.
- Windows 10 22H2 o 11 con los dispositivos **unidos a Entra ID o híbridos** y conformes (guía de Intune).
- Un grupo piloto (`sg-epm-pilot`) de 20-30 usuarios de IT y de un departamento que instale cosas a menudo, y la lista de lo que hoy hacen con derechos de administrador (pregunta; luego el informe te dirá la verdad).
- El compromiso de dirección: la fecha en la que se retira el administrador local. Sin fecha, el piloto no termina nunca.

## 1. Activar EPM y la política de elevación

:::ui Intune · Seguridad de los puntos de conexión
> Seguridad de los puntos de conexión › Endpoint Privilege Management › Crear directiva › Windows › Directiva de configuración de elevación
= Nombre: EPM - Settings - Pilot
= Endpoint Privilege Management: Habilitado
= Respuesta de elevación predeterminada: Denegar todas las solicitudes
= Validación: Justificación empresarial
= Enviar datos de elevación para informes: Sí · Datos de diagnóstico y todas las elevaciones de los puntos de conexión
= Asignaciones: sg-epm-pilot
[Crear]
:::

Dos decisiones aquí. **Denegar todas las solicitudes** como respuesta por defecto: lo que no tenga regla, no se eleva (la alternativa, "requerir confirmación del usuario", convierte a cada usuario en administrador con un clic más). Y **enviar todas las elevaciones** a los informes, porque en las primeras semanas lo importante es saber qué intenta elevar la gente.

> Consejo: antes de denegar, dos semanas con la respuesta por defecto en **Requerir confirmación del usuario** y **justificación** en el piloto. El informe de elevaciones te dirá exactamente qué reglas necesitas en el paso 3. Es el equivalente al "solo informe" de Conditional Access.

## 2. Retirar el administrador local

:::ui Intune · Cuentas
> Seguridad de los puntos de conexión › Protección de cuentas › Crear directiva › Windows › Pertenencia a grupos locales de usuarios
= Nombre: LocalAdmins - Replace - Pilot
= Grupo local: Administradores
= Acción de grupo y usuario: Reemplazar
= Tipo de selección de usuario: Usuarios/grupos
= Usuarios seleccionados: sg-workstation-admins (IT), LAPS local admin
= Asignaciones: sg-epm-pilot
[Crear]
:::

**Reemplazar** deja en `Administradores` solo lo que listas: el grupo de IT y la cuenta local que gestiona **Windows LAPS** (la contraseña rotada que IT usa in situ). El usuario desaparece del grupo en el siguiente check-in. Compruébalo en un equipo: `net localgroup Administradores` ya no lo lista. Esta política va **después** de la de EPM, nunca antes.

## 3. Las reglas de elevación

:::term PowerShell · equipo de un usuario del piloto
$ Get-AuthenticodeSignature "C:\\Users\\laura.prado\\Downloads\\DellCommandUpdate.exe" | Select-Object Status, @{n="Publisher";e={$_.SignerCertificate.Subject}}
Status Publisher
------ ---------
Valid  CN=Dell Inc, O=Dell Inc, L=Round Rock, S=Texas, C=US
$ Get-FileHash "C:\\Tools\\vendor\\ScannerDiag.exe" -Algorithm SHA256 | Select-Object -ExpandProperty Hash
7A3F…C91E
:::

:::ui Intune · Endpoint Privilege Management
> Endpoint Privilege Management › Crear directiva › Windows › Directiva de reglas de elevación
= Nombre: EPM - Rules - Pilot
Regla 1
= Nombre de regla: Dell Command Update (editor)
= Tipo de elevación: Elevación automática
= Nombre de archivo: DellCommandUpdate.exe
= Firma: Editor de certificados · Subir certificado · CN=Dell Inc …
= Regla de certificado: Sí, el certificado debe coincidir
Regla 2
= Nombre de regla: Herramienta de diagnóstico del escáner (hash)
= Tipo de elevación: Confirmación del usuario · Justificación empresarial
= Nombre de archivo: ScannerDiag.exe · Hash del archivo: 7A3F…C91E
Regla 3
= Nombre de regla: Instaladores de impresora (aprobación)
= Tipo de elevación: Aprobación del soporte técnico
= Nombre de archivo: PrinterSetup*.exe · Ruta: C:\\Users\\*\\Downloads\\
= Asignaciones: sg-epm-pilot
[Crear]
:::

Tres tipos de regla y cuándo usar cada uno: **automática** para software firmado de proveedores conocidos, que se eleva sin que el usuario note nada; **confirmación del usuario** con justificación para herramientas que IT ha revisado pero quiere que queden registradas; **aprobación del soporte técnico** para lo ocasional: el usuario pide, aparece en `Endpoint Privilege Management → Solicitudes de elevación` y alguien de IT aprueba desde el portal sin conectarse al equipo. El certificado es mejor que el hash: sobrevive a las actualizaciones del instalador.

## 4. Lo que ve el usuario

:::ui Windows · Explorador de archivos
> Descargas › DellCommandUpdate.exe › clic derecho
[Ejecutar con acceso elevado]
Endpoint Privilege Management
= Aplicación: DellCommandUpdate.exe · Dell Inc
= Esta aplicación requiere elevación. Indica el motivo:
= Motivo: Actualizar firmware del dock, ticket SD-20451
[x] Confirmo que esta elevación es para fines de trabajo
[Continuar] [Cancelar]
:::

**Ejecutar con acceso elevado** aparece en el menú contextual en los equipos con la política. Si la aplicación no tiene regla y la respuesta por defecto es denegar, el usuario ve "Tu organización no permite elevar esta aplicación" y el intento queda en el informe: ese es tu dato para la siguiente regla, o para decirle que no.

## 5. El informe y la reunión

:::ui Intune · Informes
> Informes › Endpoint Privilege Management › Informe de elevación
= Periodo: Últimos 30 días · Grupo: sg-epm-pilot
= Elevaciones totales: 412 · Automáticas: 318 · Confirmadas: 71 · Aprobadas: 9 · Denegadas: 14
Top aplicaciones
= DellCommandUpdate.exe: 203 · regla: Dell Command Update
= Teams.exe: 0 (no requiere elevación)
= setup.exe (varios): 14 denegadas · usuarios: 6
[Exportar]
:::

El dato que importa: **en 30 días, 30 usuarios necesitaron 412 elevaciones y 14 se denegaron**, ninguna de ellas con impacto en el trabajo. Eso, en una diapositiva, es lo que cierra la conversación de "yo necesito ser administrador". Las denegadas repetidas de la misma aplicación son candidatas a regla; las de instaladores descargados de internet no.

## 6. Lo que revisas cada mes

- Solicitudes de **aprobación** pendientes de más de un día: el proceso está fallando, no la herramienta.
- Reglas por **hash** que han dejado de elevar: el instalador se actualizó; cambia a certificado si puedes.
- Equipos del grupo donde `Administradores` sigue teniendo al usuario (informe de **Pertenencia a grupos locales** o la consulta de Graph de la guía siguiente).
- Nuevos grupos al despliegue: de 30 a 150 a toda la empresa, un mes por paso, y la fecha de retirada en el calendario.

## Siguientes pasos

- **Windows LAPS** para la cuenta de administrador local que queda: contraseña distinta por equipo, rotada y visible en Intune (`Dispositivos → el equipo → Contraseña de administrador local`).
- Las elevaciones aprobadas llegan como eventos al registro `Microsoft-Windows-EPMAgent/Operational`; con el agente de Sentinel (Nivel 4) tienes la alerta de "elevación fuera de horario".
- Lo mismo en macOS no existe en EPM: allí el camino es no dar administrador en el enrolamiento con Jamf y usar su **Self Service** para lo que requiera privilegios.
""",
  en="""
## What you'll get

Users stop being local administrators of their device without IT drowning in tickets: Endpoint Privilege Management (EPM) elevates only the specific application (a driver installer, a vendor tool) through a rule, with or without approval, and logs everything. By the end you will have the base policy, three rules and the report for the meeting.

## Before you start

- An **Intune Suite** licence or the **Endpoint Privilege Management** add-on for the affected users.
- Windows 10 22H2 or 11 with devices **Entra joined or hybrid joined** and compliant (Intune guide).
- A pilot group (`sg-epm-pilot`) of 20-30 users from IT and from a department that installs things often, plus the list of what they do today with admin rights (ask; the report will later tell you the truth).
- Management's commitment: the date local admin is removed. Without a date, the pilot never ends.

## 1. Enable EPM and the elevation settings policy

:::ui Intune · Endpoint security
> Endpoint security › Endpoint Privilege Management › Create policy › Windows › Elevation settings policy
= Name: EPM - Settings - Pilot
= Endpoint Privilege Management: Enabled
= Default elevation response: Deny all requests
= Validation: Business justification
= Send elevation data for reporting: Yes · Diagnostic data and all endpoint elevations
= Assignments: sg-epm-pilot
[Create]
:::

Two decisions here. **Deny all requests** as the default response: whatever has no rule does not elevate (the alternative, "require user confirmation", turns every user into an administrator with one more click). And **send all elevations** to reporting, because in the first weeks what matters is knowing what people try to elevate.

> Tip: before denying, spend two weeks with the default response on **Require user confirmation** with **justification** in the pilot. The elevation report will tell you exactly which rules you need in step 3. It is the equivalent of Conditional Access's report-only.

## 2. Remove local admin

:::ui Intune · Account protection
> Endpoint security › Account protection › Create policy › Windows › Local user group membership
= Name: LocalAdmins - Replace - Pilot
= Local group: Administrators
= Group and user action: Replace
= User selection type: Users/Groups
= Selected users: sg-workstation-admins (IT), LAPS local admin
= Assignments: sg-epm-pilot
[Create]
:::

**Replace** leaves in `Administrators` only what you list: the IT group and the local account managed by **Windows LAPS** (the rotated password IT uses on site). The user disappears from the group at the next check-in. Check on a device: `net localgroup Administrators` no longer lists them. This policy goes **after** the EPM one, never before.

## 3. The elevation rules

:::term PowerShell · a pilot user's device
$ Get-AuthenticodeSignature "C:\\Users\\laura.prado\\Downloads\\DellCommandUpdate.exe" | Select-Object Status, @{n="Publisher";e={$_.SignerCertificate.Subject}}
Status Publisher
------ ---------
Valid  CN=Dell Inc, O=Dell Inc, L=Round Rock, S=Texas, C=US
$ Get-FileHash "C:\\Tools\\vendor\\ScannerDiag.exe" -Algorithm SHA256 | Select-Object -ExpandProperty Hash
7A3F…C91E
:::

:::ui Intune · Endpoint Privilege Management
> Endpoint Privilege Management › Create policy › Windows › Elevation rules policy
= Name: EPM - Rules - Pilot
Rule 1
= Rule name: Dell Command Update (publisher)
= Elevation type: Automatic
= File name: DellCommandUpdate.exe
= Signature: Certificate publisher · Upload certificate · CN=Dell Inc …
= Certificate rule: Yes, certificate must match
Rule 2
= Rule name: Scanner diagnostic tool (hash)
= Elevation type: User confirmed · Business justification
= File name: ScannerDiag.exe · File hash: 7A3F…C91E
Rule 3
= Rule name: Printer installers (approval)
= Elevation type: Support approved
= File name: PrinterSetup*.exe · Path: C:\\Users\\*\\Downloads\\
= Assignments: sg-epm-pilot
[Create]
:::

Three rule types and when to use each: **automatic** for signed software from known vendors, which elevates without the user noticing; **user confirmed** with justification for tools IT has reviewed but wants logged; **support approved** for the occasional case: the user requests, it appears in `Endpoint Privilege Management → Elevation requests` and someone in IT approves from the portal without connecting to the device. A certificate is better than a hash: it survives installer updates.

## 4. What the user sees

:::ui Windows · File Explorer
> Downloads › DellCommandUpdate.exe › right-click
[Run with elevated access]
Endpoint Privilege Management
= Application: DellCommandUpdate.exe · Dell Inc
= This application requires elevation. Tell us why:
= Reason: Update dock firmware, ticket SD-20451
[x] I confirm this elevation is for work purposes
[Continue] [Cancel]
:::

**Run with elevated access** appears in the context menu on devices with the policy. If the application has no rule and the default response is deny, the user sees "Your organization doesn't allow you to elevate this application" and the attempt lands in the report: that is your data for the next rule, or for saying no.

## 5. The report and the meeting

:::ui Intune · Reports
> Reports › Endpoint Privilege Management › Elevation report
= Period: Last 30 days · Group: sg-epm-pilot
= Total elevations: 412 · Automatic: 318 · Confirmed: 71 · Approved: 9 · Denied: 14
Top applications
= DellCommandUpdate.exe: 203 · rule: Dell Command Update
= Teams.exe: 0 (no elevation required)
= setup.exe (various): 14 denied · users: 6
[Export]
:::

The number that matters: **in 30 days, 30 users needed 412 elevations and 14 were denied**, none of them with an impact on work. That, on one slide, is what closes the "I need to be an administrator" conversation. Repeated denials of the same application are rule candidates; denials of installers downloaded from the internet are not.

## 6. What you review each month

- **Approval** requests pending for more than a day: the process is failing, not the tool.
- **Hash** rules that have stopped elevating: the installer was updated; move to certificate if you can.
- Devices in the group where `Administrators` still contains the user (the **Local group membership** report or the Graph query from the next guide).
- New groups in the rollout: from 30 to 150 to the whole company, one month per step, and the removal date in the calendar.

## Next steps

- **Windows LAPS** for the remaining local admin account: a different password per device, rotated and visible in Intune (`Devices → the device → Local admin password`).
- Approved elevations arrive as events in the `Microsoft-Windows-EPMAgent/Operational` log; with the Sentinel agent (Level 4) you get the "out-of-hours elevation" alert.
- There is no EPM for macOS: there the path is not granting admin at Jamf enrolment and using its **Self Service** for whatever needs privileges.
""")

# ---------------------------------------------------------------- L3 · Jenkins
g(slug="jenkins-pipeline-que-prueba-los-scripts-del-equipo-en-cada-cambio", topic="jenkins", date="2026-10-22",
  title_es="Jenkins: un pipeline que prueba los scripts del equipo en cada cambio",
  title_en="Jenkins: a pipeline that tests the team's scripts on every change",
  dek_es="Jenkins en Docker, el repositorio de scripts de Git conectado, un Jenkinsfile que pasa PSScriptAnalyzer y Pester a los scripts de PowerShell y shellcheck a los de Bash, y el aviso al canal cuando algo se rompe.",
  dek_en="Jenkins in Docker, the Git scripts repository connected, a Jenkinsfile that runs PSScriptAnalyzer and Pester on the PowerShell scripts and shellcheck on the Bash ones, and the channel notification when something breaks.",
  es="""
## Qué vas a conseguir

Que ningún script del equipo llegue a la rama principal sin haber pasado un análisis estático y sus pruebas, y que cuando alguien rompa uno, el canal de Teams lo diga con el nombre y el commit. El repositorio de la guía de Git del Nivel 2 deja de ser una carpeta compartida y pasa a ser código con integración continua.

## Antes de empezar

- El servidor de herramientas con Docker (guía de Docker) y 4 GB de RAM libres.
- El repositorio de scripts en Git (GitHub, GitLab o Azure DevOps) con una cuenta de servicio de solo lectura o un token de acceso para Jenkins.
- Al menos un script de PowerShell con un test de **Pester** (`tests/*.Tests.ps1`) y uno de Bash.
- El webhook de Teams de la guía de Grafana (vale el mismo canal).

## 1. Jenkins en Docker

:::term docker-compose.yml
services:
  jenkins:
    image: jenkins/jenkins:2.479.1-lts-jdk17
    container_name: jenkins
    restart: unless-stopped
    ports: ["8080:8080", "50000:50000"]
    volumes:
      - jenkins-home:/var/jenkins_home
      - /var/run/docker.sock:/var/run/docker.sock
    environment:
      JAVA_OPTS: -Djenkins.install.runSetupWizard=true
volumes:
  jenkins-home:
:::

:::term bash · srv-tools-01
$ docker compose up -d && sleep 45
$ docker compose exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
3f9c1a2b7d4e4c88a9e0b1f2c3d4e5f6
$ docker compose exec -u root jenkins sh -c "apt-get update -qq && apt-get install -y -qq docker.io >/dev/null && usermod -aG docker jenkins"
:::

Abre `http://srv-tools-01:8080`, pega la contraseña inicial, elige **Install suggested plugins** y crea el usuario administrador (contraseña en el gestor del equipo, no en la wiki). Añade después los plugins **Docker Pipeline**, **Office 365 Connector** (Teams) y **Warnings Next Generation**. Montar el socket de Docker permite que cada etapa corra en un contenedor limpio con las herramientas que necesite, sin instalarlas en Jenkins.

## 2. Conectar el repositorio

:::ui Jenkins · New Item
> Dashboard › New Item
= Enter an item name: it-scripts
[x] Multibranch Pipeline
[OK]
> it-scripts › Configure › Branch Sources › Add source › Git
= Project Repository: https://github.com/contoso-it/it-scripts.git
= Credentials: contoso-it-ro (token de solo lectura)
= Behaviors: Discover branches · Discover pull requests from origin
= Build Configuration: by Jenkinsfile · Script Path: Jenkinsfile
= Scan Multibranch Pipeline Triggers: [x] Periodically if not otherwise run · Interval: 15 minutes
[Save]
:::

**Multibranch** crea un job por rama y por pull request automáticamente: la rama `feature/inventario-v2` de la guía de Git se prueba sola en cuanto se sube. El webhook del repositorio hacia `http://srv-tools-01:8080/github-webhook/` evita esperar los 15 minutos; si el servidor no es accesible desde internet, el sondeo periódico basta.

## 3. El Jenkinsfile

:::term Jenkinsfile
pipeline {
  agent none
  options { timestamps(); disableConcurrentBuilds() }
  stages {
    stage('Lint Bash') {
      agent { docker { image 'koalaman/shellcheck-alpine:v0.10.0' } }
      steps {
        sh 'find bash -name "*.sh" -print0 | xargs -0 shellcheck -f checkstyle > shellcheck.xml || true'
        recordIssues tool: checkStyle(pattern: 'shellcheck.xml', name: 'shellcheck'), qualityGates: [[threshold: 1, type: 'TOTAL_ERROR', unstable: false]]
      }
    }
    stage('Lint PowerShell') {
      agent { docker { image 'mcr.microsoft.com/powershell:7.4-ubuntu-22.04' } }
      steps {
        sh '''
          pwsh -NoProfile -Command "
            Install-Module PSScriptAnalyzer -Force -Scope CurrentUser
            \\$r = Invoke-ScriptAnalyzer -Path ./powershell -Recurse -Severity Error,Warning
            \\$r | Format-Table -AutoSize
            if (\\$r | Where-Object Severity -eq 'Error') { exit 1 }"
        '''
      }
    }
    stage('Test PowerShell') {
      agent { docker { image 'mcr.microsoft.com/powershell:7.4-ubuntu-22.04' } }
      steps {
        sh '''
          pwsh -NoProfile -Command "
            Install-Module Pester -Force -Scope CurrentUser -MinimumVersion 5.6
            \\$c = New-PesterConfiguration
            \\$c.Run.Path = './tests'; \\$c.Run.Exit = \\$true
            \\$c.TestResult.Enabled = \\$true; \\$c.TestResult.OutputPath = 'pester.xml'; \\$c.TestResult.OutputFormat = 'JUnitXml'
            Invoke-Pester -Configuration \\$c"
        '''
      }
      post { always { junit 'pester.xml' } }
    }
  }
  post {
    failure { office365ConnectorSend webhookUrl: credentials('teams-it-ops-webhook'), message: "❌ ${env.JOB_NAME} #${env.BUILD_NUMBER} falló (${env.GIT_COMMIT.take(7)})", status: 'Failed' }
    fixed   { office365ConnectorSend webhookUrl: credentials('teams-it-ops-webhook'), message: "✅ ${env.JOB_NAME} vuelve a estar en verde", status: 'Fixed' }
  }
}
:::

Cada etapa corre en su imagen: shellcheck, PowerShell 7 con PSScriptAnalyzer, PowerShell 7 con Pester. `recordIssues` pinta las advertencias en Jenkins; el `exit 1` en errores de PSScriptAnalyzer y `Run.Exit` de Pester son lo que hace que el pipeline falle de verdad. El webhook de Teams se guarda en **Manage Jenkins → Credentials** como texto secreto con el id `teams-it-ops-webhook`; nunca en el Jenkinsfile.

## 4. La primera ejecución y el primer fallo

:::term Jenkins · Console Output · it-scripts/main #3
[Pipeline] stage (Lint Bash)
+ find bash -name *.sh -print0
+ xargs -0 shellcheck -f checkstyle
[shellcheck] Found 2 issues (1 error, 1 warning)
[Pipeline] stage (Lint PowerShell)
RuleName                    Severity ScriptName        Line Message
--------                    -------- ----------        ---- -------
PSAvoidUsingPlainTextForPassword Warning Get-Inventory.ps1 14 Parameter '$Password' should use SecureString
[Pipeline] stage (Test PowerShell)
Starting discovery in 1 files.
Describing Get-Inventory
  [+] devuelve una fila por equipo 112ms
  [-] escribe el CSV con las columnas esperadas 38ms
    Expected 'LastBoot' to be found in collection @('Name','OS','FreeGB'), but it was not found.
Tests completed in 1.21s
Tests Passed: 1, Failed: 1, Skipped: 0
[Pipeline] junit
Recording test results
ERROR: script returned exit code 1
Finished: FAILURE
:::

El pipeline hizo su trabajo: alguien cambió las columnas del CSV y el test lo cazó antes de que el script de inventario de la guía de PowerShell dejara de servir al informe mensual. En Teams aparece el mensaje con el commit. El arreglo es un commit en la rama, y Jenkins vuelve a probar solo.

> Consejo: configura la rama `main` como **protegida** en el repositorio, con "require status checks" apuntando al job de Jenkins. Así un pull request no se puede fusionar en rojo, y la regla la pone el repositorio, no la buena voluntad.

## 5. Lo que revisas cada mes

- Jobs en rojo más de una semana: o se arreglan o se borran los scripts.
- **Manage Jenkins → Plugins**: actualizaciones de seguridad pendientes; Jenkins avisa con un banner.
- Espacio de `jenkins-home` y la **retención** de builds (`options { buildDiscarder(logRotator(numToKeepStr: '30')) }` en el Jenkinsfile).
- Credenciales que caducan (el token de Git, el webhook) y quién las conoce.

## Siguientes pasos

- Una etapa de **despliegue**: cuando `main` esté en verde, copiar los scripts al recurso compartido desde el que los lanza la tarea programada, o lanzar el playbook de Ansible con `ansible-playbook` en un contenedor.
- Lo mismo con **GitHub Actions** o **Azure Pipelines** si el repositorio ya está allí: el Jenkinsfile se traduce casi línea a línea y te ahorras el servidor.
- Añade `Pester` también a los scripts de Bash con **bats-core**: el patrón es el mismo.
""",
  en="""
## What you'll get

No team script reaches the main branch without passing static analysis and its tests, and when someone breaks one, the Teams channel says so with the name and the commit. The repository from the Level 2 Git guide stops being a shared folder and becomes code with continuous integration.

## Before you start

- The tools server with Docker (Docker guide) and 4 GB of free RAM.
- The scripts repository in Git (GitHub, GitLab or Azure DevOps) with a read-only service account or an access token for Jenkins.
- At least one PowerShell script with a **Pester** test (`tests/*.Tests.ps1`) and one Bash script.
- The Teams webhook from the Grafana guide (the same channel works).

## 1. Jenkins in Docker

:::term docker-compose.yml
services:
  jenkins:
    image: jenkins/jenkins:2.479.1-lts-jdk17
    container_name: jenkins
    restart: unless-stopped
    ports: ["8080:8080", "50000:50000"]
    volumes:
      - jenkins-home:/var/jenkins_home
      - /var/run/docker.sock:/var/run/docker.sock
    environment:
      JAVA_OPTS: -Djenkins.install.runSetupWizard=true
volumes:
  jenkins-home:
:::

:::term bash · srv-tools-01
$ docker compose up -d && sleep 45
$ docker compose exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
3f9c1a2b7d4e4c88a9e0b1f2c3d4e5f6
$ docker compose exec -u root jenkins sh -c "apt-get update -qq && apt-get install -y -qq docker.io >/dev/null && usermod -aG docker jenkins"
:::

Open `http://srv-tools-01:8080`, paste the initial password, choose **Install suggested plugins** and create the admin user (password in the team's password manager, not the wiki). Then add the **Docker Pipeline**, **Office 365 Connector** (Teams) and **Warnings Next Generation** plugins. Mounting the Docker socket lets each stage run in a clean container with the tools it needs, without installing them in Jenkins.

## 2. Connect the repository

:::ui Jenkins · New Item
> Dashboard › New Item
= Enter an item name: it-scripts
[x] Multibranch Pipeline
[OK]
> it-scripts › Configure › Branch Sources › Add source › Git
= Project Repository: https://github.com/contoso-it/it-scripts.git
= Credentials: contoso-it-ro (read-only token)
= Behaviors: Discover branches · Discover pull requests from origin
= Build Configuration: by Jenkinsfile · Script Path: Jenkinsfile
= Scan Multibranch Pipeline Triggers: [x] Periodically if not otherwise run · Interval: 15 minutes
[Save]
:::

**Multibranch** creates one job per branch and per pull request automatically: the `feature/inventory-v2` branch from the Git guide gets tested on its own as soon as it is pushed. A repository webhook to `http://srv-tools-01:8080/github-webhook/` avoids waiting the 15 minutes; if the server is not reachable from the internet, periodic polling is enough.

## 3. The Jenkinsfile

:::term Jenkinsfile
pipeline {
  agent none
  options { timestamps(); disableConcurrentBuilds() }
  stages {
    stage('Lint Bash') {
      agent { docker { image 'koalaman/shellcheck-alpine:v0.10.0' } }
      steps {
        sh 'find bash -name "*.sh" -print0 | xargs -0 shellcheck -f checkstyle > shellcheck.xml || true'
        recordIssues tool: checkStyle(pattern: 'shellcheck.xml', name: 'shellcheck'), qualityGates: [[threshold: 1, type: 'TOTAL_ERROR', unstable: false]]
      }
    }
    stage('Lint PowerShell') {
      agent { docker { image 'mcr.microsoft.com/powershell:7.4-ubuntu-22.04' } }
      steps {
        sh '''
          pwsh -NoProfile -Command "
            Install-Module PSScriptAnalyzer -Force -Scope CurrentUser
            \\$r = Invoke-ScriptAnalyzer -Path ./powershell -Recurse -Severity Error,Warning
            \\$r | Format-Table -AutoSize
            if (\\$r | Where-Object Severity -eq 'Error') { exit 1 }"
        '''
      }
    }
    stage('Test PowerShell') {
      agent { docker { image 'mcr.microsoft.com/powershell:7.4-ubuntu-22.04' } }
      steps {
        sh '''
          pwsh -NoProfile -Command "
            Install-Module Pester -Force -Scope CurrentUser -MinimumVersion 5.6
            \\$c = New-PesterConfiguration
            \\$c.Run.Path = './tests'; \\$c.Run.Exit = \\$true
            \\$c.TestResult.Enabled = \\$true; \\$c.TestResult.OutputPath = 'pester.xml'; \\$c.TestResult.OutputFormat = 'JUnitXml'
            Invoke-Pester -Configuration \\$c"
        '''
      }
      post { always { junit 'pester.xml' } }
    }
  }
  post {
    failure { office365ConnectorSend webhookUrl: credentials('teams-it-ops-webhook'), message: "❌ ${env.JOB_NAME} #${env.BUILD_NUMBER} failed (${env.GIT_COMMIT.take(7)})", status: 'Failed' }
    fixed   { office365ConnectorSend webhookUrl: credentials('teams-it-ops-webhook'), message: "✅ ${env.JOB_NAME} is green again", status: 'Fixed' }
  }
}
:::

Each stage runs in its own image: shellcheck, PowerShell 7 with PSScriptAnalyzer, PowerShell 7 with Pester. `recordIssues` renders the warnings in Jenkins; the `exit 1` on PSScriptAnalyzer errors and Pester's `Run.Exit` are what make the pipeline fail for real. The Teams webhook is stored in **Manage Jenkins → Credentials** as secret text with the id `teams-it-ops-webhook`; never in the Jenkinsfile.

## 4. The first run and the first failure

:::term Jenkins · Console Output · it-scripts/main #3
[Pipeline] stage (Lint Bash)
+ find bash -name *.sh -print0
+ xargs -0 shellcheck -f checkstyle
[shellcheck] Found 2 issues (1 error, 1 warning)
[Pipeline] stage (Lint PowerShell)
RuleName                    Severity ScriptName        Line Message
--------                    -------- ----------        ---- -------
PSAvoidUsingPlainTextForPassword Warning Get-Inventory.ps1 14 Parameter '$Password' should use SecureString
[Pipeline] stage (Test PowerShell)
Starting discovery in 1 files.
Describing Get-Inventory
  [+] returns one row per device 112ms
  [-] writes the CSV with the expected columns 38ms
    Expected 'LastBoot' to be found in collection @('Name','OS','FreeGB'), but it was not found.
Tests completed in 1.21s
Tests Passed: 1, Failed: 1, Skipped: 0
[Pipeline] junit
Recording test results
ERROR: script returned exit code 1
Finished: FAILURE
:::

The pipeline did its job: someone changed the CSV columns and the test caught it before the inventory script from the PowerShell guide stopped feeding the monthly report. In Teams the message appears with the commit. The fix is a commit on the branch, and Jenkins tests again by itself.

> Tip: set the `main` branch as **protected** in the repository, with "require status checks" pointing at the Jenkins job. That way a pull request cannot be merged while red, and the rule is enforced by the repository, not by goodwill.

## 5. What you review each month

- Jobs red for more than a week: either fix them or delete the scripts.
- **Manage Jenkins → Plugins**: pending security updates; Jenkins warns with a banner.
- `jenkins-home` disk and build **retention** (`options { buildDiscarder(logRotator(numToKeepStr: '30')) }` in the Jenkinsfile).
- Credentials that expire (the Git token, the webhook) and who knows them.

## Next steps

- A **deploy** stage: when `main` is green, copy the scripts to the share the scheduled task runs them from, or launch the Ansible playbook with `ansible-playbook` in a container.
- The same with **GitHub Actions** or **Azure Pipelines** if the repository already lives there: the Jenkinsfile translates almost line by line and you save the server.
- Add tests to the Bash scripts too with **bats-core**: the pattern is the same.
""")

# ---------------------------------------------------------------- L3 · Linux + AD
g(slug="linux-unir-un-servidor-a-active-directory-con-sssd", topic="linux-ad", date="2026-10-22",
  title_es="Linux integrado con Active Directory: unir un servidor al dominio con SSSD",
  title_en="Linux joined to Active Directory: joining a server to the domain with SSSD",
  dek_es="realm join, SSSD con los grupos de AD, sudo para el grupo de administradores de Linux, SSH solo para quien está autorizado, y los tres comandos de diagnóstico cuando el login de dominio deja de funcionar.",
  dek_en="realm join, SSSD with AD groups, sudo for the Linux admins group, SSH only for those authorised, and the three diagnostic commands when domain login stops working.",
  es="""
## Qué vas a conseguir

Que los administradores entren en los servidores Linux con su cuenta de Active Directory (la misma contraseña, la misma baja cuando se van) y que `sudo` dependa de un grupo de AD en lugar de una lista local en cada máquina. Las cuentas locales quedan solo para emergencias.

## Antes de empezar

- Un servidor RHEL o Ubuntu con **DNS apuntando a los controladores de dominio** y la hora sincronizada (Kerberos no perdona más de cinco minutos de desfase).
- Una cuenta de AD con permiso para unir equipos a la OU donde van los servidores Linux (`OU=Linux,OU=Servers,DC=contoso,DC=local`), no un Domain Admin.
- Dos grupos de AD creados: `sg-linux-admins` (sudo) y `sg-linux-ssh` (acceso por SSH).
- Una sesión SSH abierta con la cuenta local durante todo el proceso.

## 1. Requisitos y descubrimiento

:::term bash · srv-app-01 (RHEL)
$ sudo dnf install -y realmd sssd oddjob oddjob-mkhomedir adcli samba-common-tools krb5-workstation
$ timedatectl | grep -E 'synchronized|Time zone'
                Time zone: Europe/Madrid (CEST, +0200)
System clock synchronized: yes
$ dig +short _ldap._tcp.contoso.local SRV | head -2
0 100 389 dc01.contoso.local.
0 100 389 dc02.contoso.local.
$ realm discover contoso.local
contoso.local
  type: kerberos
  realm-name: CONTOSO.LOCAL
  domain-name: contoso.local
  configured: no
  server-software: active-directory
  client-software: sssd
  required-package: oddjob
  required-package: oddjob-mkhomedir
  required-package: sssd
  required-package: adcli
  required-package: samba-common-tools
:::

En Ubuntu los paquetes son `realmd sssd-ad sssd-tools adcli libnss-sss libpam-sss packagekit`. Si `realm discover` no devuelve nada, el problema es DNS: para en ese punto.

## 2. Unir al dominio

:::term bash · srv-app-01
$ sudo realm join --user=svc-linux-join --computer-ou="OU=Linux,OU=Servers,DC=contoso,DC=local" --os-name="RHEL" --os-version="9.4" contoso.local
Password for svc-linux-join:
$ realm list
contoso.local
  configured: kerberos-member
  login-formats: %U@contoso.local
  login-policy: allow-realm-logins
$ id laura.prado@contoso.local
uid=1483201105(laura.prado@contoso.local) gid=1483200513(domain users@contoso.local) groups=1483200513(domain users@contoso.local),1483201204(sg-linux-admins@contoso.local)
:::

El `id` que resuelve un usuario de AD con sus grupos es la prueba de que SSSD habla con el dominio. En AD aparece el objeto de equipo `SRV-APP-01` en la OU indicada; apunta en el ticket el nombre y la OU.

## 3. Afinar SSSD: nombres cortos y acceso por grupo

:::term /etc/sssd/sssd.conf
[sssd]
domains = contoso.local
config_file_version = 2
services = nss, pam

[domain/contoso.local]
default_shell = /bin/bash
krb5_store_password_if_offline = True
cache_credentials = True
krb5_realm = CONTOSO.LOCAL
realmd_tags = manages-system joined-with-adcli
id_provider = ad
fallback_homedir = /home/%u
ad_domain = contoso.local
use_fully_qualified_names = False
ldap_id_mapping = True
access_provider = ad
ad_gpo_access_control = disabled
:::

:::term bash · srv-app-01
$ sudo chmod 600 /etc/sssd/sssd.conf && sudo systemctl restart sssd
$ sudo realm permit -g sg-linux-ssh@contoso.local
$ sudo realm permit -g sg-linux-admins@contoso.local
$ realm list | grep permitted
  permitted-groups: sg-linux-ssh@contoso.local, sg-linux-admins@contoso.local
$ id laura.prado
uid=1483201105(laura.prado) gid=1483200513(domain users) groups=1483200513(domain users),1483201204(sg-linux-admins)
:::

`use_fully_qualified_names = False` permite `ssh laura.prado@srv-app-01` en lugar del `@contoso.local` detrás. `realm permit -g` cambia `login-policy` a **allow-permitted-logins**: solo los grupos listados entran, los demás usuarios del dominio reciben "Permission denied" aunque la contraseña sea correcta. `ad_gpo_access_control = disabled` evita que una GPO de "Allow log on locally" pensada para Windows bloquee el acceso a Linux; cámbialo a `enforcing` solo si gestionas esas GPO a propósito.

## 4. sudo por grupo de AD

:::term bash · srv-app-01
$ echo '%sg-linux-admins ALL=(ALL) ALL' | sudo tee /etc/sudoers.d/10-ad-linux-admins
$ sudo chmod 440 /etc/sudoers.d/10-ad-linux-admins && sudo visudo -c
/etc/sudoers: parsed OK
/etc/sudoers.d/10-ad-linux-admins: parsed OK
# prueba desde otra sesión, con la cuenta de AD:
$ ssh laura.prado@srv-app-01 'sudo -n true && echo SUDO_OK'
SUDO_OK
:::

Ya no hay lista de administradores en el servidor: la gestiona quien gestiona `sg-linux-admins` en AD, y la baja de la guía de Active Directory del Nivel 1 corta el acceso a todos los servidores a la vez. Con Ansible, todo este artículo es un rol que se aplica a la flota.

## 5. Cuando el login de dominio falla

:::term bash · srv-app-01
$ sudo systemctl status sssd --no-pager | head -3
● sssd.service - System Security Services Daemon
     Active: active (running) since Wed 2026-10-22 07:01:12 CEST; 3h ago
$ sudo sssctl domain-status contoso.local
Online status: Offline
Active server: not connected
$ sudo journalctl -u sssd -p err -S "1 hour ago" --no-pager | tail -3
oct 22 09:58:40 srv-app-01 sssd_be[1322]: Backend is offline
$ kinit laura.prado
kinit: Cannot find KDC for realm "CONTOSO.LOCAL" while getting initial credentials
$ dig +short dc01.contoso.local
:::

Los tres comandos: `sssctl domain-status` (¿ve al dominio?), `journalctl -u sssd -p err` (¿por qué no?) y `kinit` (¿Kerberos funciona independientemente de SSSD?). Aquí el DNS dejó de resolver los controladores: alguien cambió `/etc/resolv.conf` o NetworkManager pisó la configuración. Otros clásicos: **desfase de hora** (`timedatectl`, error `Clock skew too great`), **contraseña del equipo** caducada tras una restauración desde snapshot (`sudo adcli update` o volver a hacer `realm leave` y `realm join`), y la **caché** de SSSD con un grupo antiguo (`sudo sss_cache -E`).

## 6. Lo que revisas cada mes

- Servidores Linux en la OU de AD cuyo `lastLogon` del objeto de equipo tiene más de 30 días: ya no existen o SSSD no está arrancando.
- Miembros de `sg-linux-admins`: la revisión trimestral de accesos del repo 27 cubre este grupo igual que los de administrador de M365.
- Cuentas locales con contraseña en los servidores (`sudo awk -F: '$2 !~ /^[!*]/ {print $1}' /etc/shadow`): solo la de emergencia.
- Que `realm list` sigue en `allow-permitted-logins` después de cada reinstalación o restauración.

## Siguientes pasos

- **Claves SSH desde AD**: con `ldap_user_ssh_public_key = altSecurityIdentities` en SSSD y `AuthorizedKeysCommand /usr/bin/sss_ssh_authorizedkeys` en `sshd_config`, la clave pública vive en el objeto de usuario.
- **Kerberos para servicios**: un servidor web o PostgreSQL (guía de bases de datos) autenticando con el ticket del usuario, sin contraseña, con el keytab que `realm join` ya ha creado en `/etc/krb5.keytab`.
- Para flotas grandes, **FreeIPA/IdM con confianza hacia AD** da sudo, HBAC y claves centralizadas con una consola; hasta entonces, SSSD directo es suficiente.
""",
  en="""
## What you'll get

Administrators log in to Linux servers with their Active Directory account (same password, same offboarding when they leave) and `sudo` depends on an AD group instead of a local list on each machine. Local accounts remain for emergencies only.

## Before you start

- A RHEL or Ubuntu server with **DNS pointing at the domain controllers** and the clock synchronised (Kerberos does not forgive more than five minutes of skew).
- An AD account allowed to join computers to the OU where Linux servers go (`OU=Linux,OU=Servers,DC=contoso,DC=local`), not a Domain Admin.
- Two AD groups created: `sg-linux-admins` (sudo) and `sg-linux-ssh` (SSH access).
- An SSH session open with the local account for the whole process.

## 1. Prerequisites and discovery

:::term bash · srv-app-01 (RHEL)
$ sudo dnf install -y realmd sssd oddjob oddjob-mkhomedir adcli samba-common-tools krb5-workstation
$ timedatectl | grep -E 'synchronized|Time zone'
                Time zone: Europe/Madrid (CEST, +0200)
System clock synchronized: yes
$ dig +short _ldap._tcp.contoso.local SRV | head -2
0 100 389 dc01.contoso.local.
0 100 389 dc02.contoso.local.
$ realm discover contoso.local
contoso.local
  type: kerberos
  realm-name: CONTOSO.LOCAL
  domain-name: contoso.local
  configured: no
  server-software: active-directory
  client-software: sssd
  required-package: oddjob
  required-package: oddjob-mkhomedir
  required-package: sssd
  required-package: adcli
  required-package: samba-common-tools
:::

On Ubuntu the packages are `realmd sssd-ad sssd-tools adcli libnss-sss libpam-sss packagekit`. If `realm discover` returns nothing, the problem is DNS: stop right there.

## 2. Join the domain

:::term bash · srv-app-01
$ sudo realm join --user=svc-linux-join --computer-ou="OU=Linux,OU=Servers,DC=contoso,DC=local" --os-name="RHEL" --os-version="9.4" contoso.local
Password for svc-linux-join:
$ realm list
contoso.local
  configured: kerberos-member
  login-formats: %U@contoso.local
  login-policy: allow-realm-logins
$ id laura.prado@contoso.local
uid=1483201105(laura.prado@contoso.local) gid=1483200513(domain users@contoso.local) groups=1483200513(domain users@contoso.local),1483201204(sg-linux-admins@contoso.local)
:::

The `id` that resolves an AD user with their groups is the proof that SSSD talks to the domain. In AD the computer object `SRV-APP-01` appears in the given OU; note the name and OU in the ticket.

## 3. Tune SSSD: short names and group-based access

:::term /etc/sssd/sssd.conf
[sssd]
domains = contoso.local
config_file_version = 2
services = nss, pam

[domain/contoso.local]
default_shell = /bin/bash
krb5_store_password_if_offline = True
cache_credentials = True
krb5_realm = CONTOSO.LOCAL
realmd_tags = manages-system joined-with-adcli
id_provider = ad
fallback_homedir = /home/%u
ad_domain = contoso.local
use_fully_qualified_names = False
ldap_id_mapping = True
access_provider = ad
ad_gpo_access_control = disabled
:::

:::term bash · srv-app-01
$ sudo chmod 600 /etc/sssd/sssd.conf && sudo systemctl restart sssd
$ sudo realm permit -g sg-linux-ssh@contoso.local
$ sudo realm permit -g sg-linux-admins@contoso.local
$ realm list | grep permitted
  permitted-groups: sg-linux-ssh@contoso.local, sg-linux-admins@contoso.local
$ id laura.prado
uid=1483201105(laura.prado) gid=1483200513(domain users) groups=1483200513(domain users),1483201204(sg-linux-admins)
:::

`use_fully_qualified_names = False` allows `ssh laura.prado@srv-app-01` instead of the trailing `@contoso.local`. `realm permit -g` switches `login-policy` to **allow-permitted-logins**: only the listed groups get in, every other domain user gets "Permission denied" even with the right password. `ad_gpo_access_control = disabled` stops an "Allow log on locally" GPO meant for Windows from blocking access to Linux; change it to `enforcing` only if you manage those GPOs on purpose.

## 4. sudo by AD group

:::term bash · srv-app-01
$ echo '%sg-linux-admins ALL=(ALL) ALL' | sudo tee /etc/sudoers.d/10-ad-linux-admins
$ sudo chmod 440 /etc/sudoers.d/10-ad-linux-admins && sudo visudo -c
/etc/sudoers: parsed OK
/etc/sudoers.d/10-ad-linux-admins: parsed OK
# test from another session, with the AD account:
$ ssh laura.prado@srv-app-01 'sudo -n true && echo SUDO_OK'
SUDO_OK
:::

There is no longer an admin list on the server: whoever manages `sg-linux-admins` in AD manages it, and the leaver process from the Level 1 Active Directory guide cuts access to every server at once. With Ansible, this whole article is a role applied to the fleet.

## 5. When domain login fails

:::term bash · srv-app-01
$ sudo systemctl status sssd --no-pager | head -3
● sssd.service - System Security Services Daemon
     Active: active (running) since Wed 2026-10-22 07:01:12 CEST; 3h ago
$ sudo sssctl domain-status contoso.local
Online status: Offline
Active server: not connected
$ sudo journalctl -u sssd -p err -S "1 hour ago" --no-pager | tail -3
Oct 22 09:58:40 srv-app-01 sssd_be[1322]: Backend is offline
$ kinit laura.prado
kinit: Cannot find KDC for realm "CONTOSO.LOCAL" while getting initial credentials
$ dig +short dc01.contoso.local
:::

The three commands: `sssctl domain-status` (can it see the domain?), `journalctl -u sssd -p err` (why not?) and `kinit` (does Kerberos work independently of SSSD?). Here DNS stopped resolving the domain controllers: someone changed `/etc/resolv.conf` or NetworkManager overwrote the configuration. Other classics: **clock skew** (`timedatectl`, error `Clock skew too great`), an expired **computer password** after restoring from a snapshot (`sudo adcli update`, or `realm leave` and `realm join` again), and the SSSD **cache** holding an old group (`sudo sss_cache -E`).

## 6. What you review each month

- Linux servers in the AD OU whose computer object `lastLogon` is older than 30 days: they no longer exist or SSSD is not starting.
- Members of `sg-linux-admins`: the quarterly access review from repo 27 covers this group just like the M365 admin ones.
- Local accounts with a password on the servers (`sudo awk -F: '$2 !~ /^[!*]/ {print $1}' /etc/shadow`): only the emergency one.
- That `realm list` still shows `allow-permitted-logins` after every reinstall or restore.

## Next steps

- **SSH keys from AD**: with `ldap_user_ssh_public_key = altSecurityIdentities` in SSSD and `AuthorizedKeysCommand /usr/bin/sss_ssh_authorizedkeys` in `sshd_config`, the public key lives in the user object.
- **Kerberos for services**: a web server or PostgreSQL (databases guide) authenticating with the user's ticket, no password, using the keytab `realm join` already created at `/etc/krb5.keytab`.
- For large fleets, **FreeIPA/IdM with a trust to AD** gives sudo, HBAC and centralised keys with a console; until then, direct SSSD is enough.
""")

# ---------------------------------------------------------------- L3 · Microsoft Graph
g(slug="microsoft-graph-primeras-consultas-con-powershell-y-un-informe-que-no-existe-en-el-portal", topic="graph", date="2026-10-22",
  title_es="Microsoft Graph con PowerShell: las primeras consultas y un informe que no existe en el portal",
  title_en="Microsoft Graph with PowerShell: your first queries and a report the portal doesn't have",
  dek_es="El SDK, los ámbitos de permiso y por qué pedir los mínimos, Graph Explorer para encontrar la consulta, paginación, y el informe de dispositivos sin check-in con su usuario y su manager en un CSV.",
  dek_en="The SDK, permission scopes and why to ask for the minimum, Graph Explorer to find the query, paging, and the report of devices with no check-in together with their user and manager in a CSV.",
  es="""
## Qué vas a conseguir

Hacer con un script lo que el portal te obliga a hacer a clics: cruzar dispositivos de Intune con usuarios y managers de Entra, sacar un CSV cada lunes y, cuando lo tengas claro, automatizarlo sin que nadie inicie sesión. Es la base de los repos de mi GitHub que leen el tenant.

## Antes de empezar

- PowerShell 7 (`pwsh`), en Windows, macOS o Linux.
- Una cuenta con los roles de lectura necesarios: **Global Reader** basta para todo lo de esta guía.
- Para la automatización final, permiso para crear un **registro de aplicación** (o que lo cree el administrador de identidad con los permisos que le pidas).

## 1. El SDK y la primera conexión

:::term pwsh
$ Install-Module Microsoft.Graph.Authentication, Microsoft.Graph.Users, Microsoft.Graph.DeviceManagement -Scope CurrentUser -Force
$ Connect-MgGraph -Scopes "User.Read.All","Device.Read.All","DeviceManagementManagedDevices.Read.All" -NoWelcome
$ Get-MgContext | Select-Object Account, TenantId, @{n="Scopes";e={$_.Scopes -join ", "}}
Account                  TenantId                             Scopes
-------                  --------                             ------
inigo.admin@contoso.com  7f1c…-…-…                            Device.Read.All, DeviceManagementManagedDevices.Read.All, User.Read.All, ...
$ Get-MgUser -UserId laura.prado@contoso.com -Property displayName,department,jobTitle,accountEnabled | Format-List displayName,department,jobTitle,accountEnabled
displayName    : Laura Prado
department     : Finanzas
jobTitle       : Analista
accountEnabled : True
:::

Dos cosas que importan desde el primer día. Instala **solo los módulos** que necesitas (`Microsoft.Graph` completo son 40 módulos y tarda diez minutos). Y pide **solo los ámbitos** que la tarea necesita: `-Scopes` es lo que un administrador te concede y lo que un auditor verá; `Directory.ReadWrite.All` para un informe de lectura es lo que no quieres explicar.

## 2. Encontrar la consulta: Graph Explorer

:::ui Graph Explorer · https://developer.microsoft.com/graph/graph-explorer
> GET › v1.0 › https://graph.microsoft.com/v1.0/deviceManagement/managedDevices?$filter=lastSyncDateTime le 2026-09-22T00:00:00Z&$select=deviceName,userPrincipalName,operatingSystem,lastSyncDateTime,complianceState&$top=5
= Permisos modificados: DeviceManagementManagedDevices.Read.All ✓ consentido
Respuesta 200 OK
{ "value": [
  { "deviceName": "LAPTOP-3K8MQ2", "userPrincipalName": "j.navarro@contoso.com", "operatingSystem": "Windows", "lastSyncDateTime": "2026-08-30T06:12:44Z", "complianceState": "noncompliant" },
  { "deviceName": "Laura's iPhone", "userPrincipalName": "laura.prado@contoso.com", "operatingSystem": "iOS", "lastSyncDateTime": "2026-09-12T19:40:02Z", "complianceState": "compliant" } ] }
[Ejecutar consulta] [Fragmentos de código]
:::

Graph Explorer es donde pruebas la URL antes de escribir una línea de PowerShell: la pestaña **Permisos modificados** te dice exactamente qué ámbito necesita y **Fragmentos de código** te da el cmdlet equivalente. La regla de oro: `$select` siempre (menos datos, más rápido) y `$filter` en el servidor, no `Where-Object` en tu máquina con 5.000 dispositivos descargados.

## 3. Paginación: lo que rompe los scripts

:::term pwsh
$ $r = Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/users?`$select=id,userPrincipalName&`$top=999"
$ $r.value.Count; $r.'@odata.nextLink' -ne $null
999
True
# con el cmdlet, -All recorre todas las páginas por ti:
$ $users = Get-MgUser -All -Property id,userPrincipalName,accountEnabled -PageSize 999
$ $users.Count
3412
:::

Graph devuelve como mucho 999 objetos por llamada y un `@odata.nextLink` para la siguiente página. Un script que "funcionaba" con 800 usuarios y devuelve 999 de 3.412 cuando la empresa crece no da error: da datos incompletos. `-All` en los cmdlets o un bucle sobre `nextLink` con `Invoke-MgGraphRequest` es obligatorio.

## 4. El informe: dispositivos sin check-in, con usuario y manager

:::term Get-StaleDevices.ps1
#Requires -Modules Microsoft.Graph.Authentication, Microsoft.Graph.Users, Microsoft.Graph.DeviceManagement
param([int]$Days = 30, [string]$Out = "stale-devices-$(Get-Date -Format yyyy-MM-dd).csv")

Connect-MgGraph -Scopes "User.Read.All","DeviceManagementManagedDevices.Read.All" -NoWelcome
$since = (Get-Date).AddDays(-$Days).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")

$devices = Get-MgDeviceManagementManagedDevice -All -Filter "lastSyncDateTime le $since" `
  -Property deviceName,userPrincipalName,operatingSystem,osVersion,lastSyncDateTime,complianceState,managedDeviceOwnerType

$cache = @{}
$rows = foreach ($d in $devices) {
  $mgr = $null
  if ($d.UserPrincipalName) {
    if (-not $cache.ContainsKey($d.UserPrincipalName)) {
      $u = Get-MgUser -UserId $d.UserPrincipalName -Property accountEnabled,department -ExpandProperty manager -ErrorAction SilentlyContinue
      $cache[$d.UserPrincipalName] = $u
    }
    $u = $cache[$d.UserPrincipalName]
    $mgr = $u.Manager.AdditionalProperties.userPrincipalName
  }
  [pscustomobject]@{
    Device = $d.DeviceName; OS = "$($d.OperatingSystem) $($d.OsVersion)"; Owner = $d.ManagedDeviceOwnerType
    LastSync = $d.LastSyncDateTime; DaysSilent = [int]((Get-Date) - $d.LastSyncDateTime).TotalDays
    Compliance = $d.ComplianceState; User = $d.UserPrincipalName; UserEnabled = $u.AccountEnabled
    Department = $u.Department; Manager = $mgr
  }
}
$rows | Sort-Object DaysSilent -Descending | Export-Csv $Out -NoTypeInformation -Encoding utf8
"$($rows.Count) dispositivos sin check-in en $Days días -> $Out"
:::

:::term pwsh
$ ./Get-StaleDevices.ps1 -Days 30
47 dispositivos sin check-in en 30 días -> stale-devices-2026-10-22.csv
$ Import-Csv .\\stale-devices-2026-10-22.csv | Where-Object UserEnabled -eq False | Select-Object Device, User, DaysSilent, Manager | Format-Table
Device         User                     DaysSilent Manager
------         ----                     ---------- -------
LAPTOP-3K8MQ2  j.navarro@contoso.com            53 m.ortega@contoso.com
DESKTOP-Q71A   p.ruiz@contoso.com               41 m.ortega@contoso.com
:::

Esto es lo que el portal no te da en una pantalla: el equipo que lleva 53 días sin sincronizar pertenece a un usuario **deshabilitado** (una baja), y quien tiene que devolverlo es su manager. La caché de usuarios evita 47 llamadas repetidas al mismo manager. El CSV va al ticket de bajas y, con la guía de Jenkins, el script se prueba en cada cambio.

## 5. Automatizar sin usuario: registro de aplicación

:::ui Entra admin center · Registros de aplicaciones
> Identidad › Aplicaciones › Registros de aplicaciones › Nuevo registro
= Nombre: it-reports-graph
= Tipos de cuenta admitidos: Solo esta organización
> it-reports-graph › Permisos de API › Agregar un permiso › Microsoft Graph › Permisos de aplicación
[x] User.Read.All
[x] DeviceManagementManagedDevices.Read.All
[Conceder consentimiento de administrador para Contoso]
> it-reports-graph › Certificados y secretos › Certificados › Cargar certificado
= Huella digital: A1B2…F0 · Expira: 22/10/2027
:::

:::term pwsh · servidor de tareas
$ $cert = New-SelfSignedCertificate -Subject "CN=it-reports-graph" -CertStoreLocation Cert:\\CurrentUser\\My -KeyExportPolicy NonExportable -NotAfter (Get-Date).AddYears(1)
$ Export-Certificate -Cert $cert -FilePath .\\it-reports-graph.cer     # este .cer es el que se sube al registro
$ Connect-MgGraph -ClientId "0a1b…-…" -TenantId "7f1c…-…" -CertificateThumbprint $cert.Thumbprint -NoWelcome
$ (Get-MgContext).AuthType
AppOnly
:::

Para la tarea programada, el script usa **certificado**, no secreto de cliente: la clave privada no sale del servidor y no hay nada que copiar en un fichero. Los permisos de **aplicación** (no delegados) son los que importan aquí, y el consentimiento del administrador queda en el registro de auditoría. El repo 20 de mi GitHub revisa cada mes estos registros: quién tiene qué permiso y cuándo caduca el certificado.

## 6. Lo que revisas cada mes

- Registros de aplicaciones de IT: permisos concedidos frente a los usados (`Registros de aplicaciones → la app → Permisos de API`), certificados que caducan en 90 días.
- Que ningún script del equipo usa `Directory.ReadWrite.All` o `Mail.ReadWrite` "por si acaso".
- Los `-Scopes` interactivos que has consentido tú mismo: `Aplicaciones empresariales → Microsoft Graph Command Line Tools → Permisos`; revoca lo que no uses.

## Siguientes pasos

- **Escritura con cuidado**: `Update-MgUser`, `Invoke-MgSyncDeviceManagementManagedDevice` (forzar check-in a los 47 del informe) siempre con `-WhatIf` primero y en un grupo pequeño.
- **Azure Automation** o una tarea en el servidor de herramientas para que el informe llegue cada lunes al canal de Teams.
- Las mismas consultas sirven desde Python (`msgraph-sdk`) o `curl` con un token: Graph es una API REST, PowerShell es solo la puerta más cómoda para IT.
""",
  en="""
## What you'll get

Do with a script what the portal makes you do with clicks: join Intune devices with Entra users and managers, produce a CSV every Monday and, once it is clear, automate it without anyone signing in. It is the foundation of the repos on my GitHub that read the tenant.

## Before you start

- PowerShell 7 (`pwsh`), on Windows, macOS or Linux.
- An account with the necessary read roles: **Global Reader** is enough for everything in this guide.
- For the final automation, permission to create an **app registration** (or have the identity admin create it with the permissions you ask for).

## 1. The SDK and the first connection

:::term pwsh
$ Install-Module Microsoft.Graph.Authentication, Microsoft.Graph.Users, Microsoft.Graph.DeviceManagement -Scope CurrentUser -Force
$ Connect-MgGraph -Scopes "User.Read.All","Device.Read.All","DeviceManagementManagedDevices.Read.All" -NoWelcome
$ Get-MgContext | Select-Object Account, TenantId, @{n="Scopes";e={$_.Scopes -join ", "}}
Account                  TenantId                             Scopes
-------                  --------                             ------
inigo.admin@contoso.com  7f1c…-…-…                            Device.Read.All, DeviceManagementManagedDevices.Read.All, User.Read.All, ...
$ Get-MgUser -UserId laura.prado@contoso.com -Property displayName,department,jobTitle,accountEnabled | Format-List displayName,department,jobTitle,accountEnabled
displayName    : Laura Prado
department     : Finance
jobTitle       : Analyst
accountEnabled : True
:::

Two things matter from day one. Install **only the modules** you need (the full `Microsoft.Graph` is 40 modules and takes ten minutes). And ask for **only the scopes** the task needs: `-Scopes` is what an administrator grants you and what an auditor will see; `Directory.ReadWrite.All` for a read-only report is what you don't want to explain.

## 2. Find the query: Graph Explorer

:::ui Graph Explorer · https://developer.microsoft.com/graph/graph-explorer
> GET › v1.0 › https://graph.microsoft.com/v1.0/deviceManagement/managedDevices?$filter=lastSyncDateTime le 2026-09-22T00:00:00Z&$select=deviceName,userPrincipalName,operatingSystem,lastSyncDateTime,complianceState&$top=5
= Modify permissions: DeviceManagementManagedDevices.Read.All ✓ consented
Response 200 OK
{ "value": [
  { "deviceName": "LAPTOP-3K8MQ2", "userPrincipalName": "j.navarro@contoso.com", "operatingSystem": "Windows", "lastSyncDateTime": "2026-08-30T06:12:44Z", "complianceState": "noncompliant" },
  { "deviceName": "Laura's iPhone", "userPrincipalName": "laura.prado@contoso.com", "operatingSystem": "iOS", "lastSyncDateTime": "2026-09-12T19:40:02Z", "complianceState": "compliant" } ] }
[Run query] [Code snippets]
:::

Graph Explorer is where you test the URL before writing a line of PowerShell: the **Modify permissions** tab tells you exactly which scope it needs and **Code snippets** gives you the equivalent cmdlet. The golden rule: `$select` always (less data, faster) and `$filter` on the server, not `Where-Object` on your machine with 5,000 downloaded devices.

## 3. Paging: what breaks scripts

:::term pwsh
$ $r = Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/users?`$select=id,userPrincipalName&`$top=999"
$ $r.value.Count; $r.'@odata.nextLink' -ne $null
999
True
# with the cmdlet, -All walks every page for you:
$ $users = Get-MgUser -All -Property id,userPrincipalName,accountEnabled -PageSize 999
$ $users.Count
3412
:::

Graph returns at most 999 objects per call and an `@odata.nextLink` for the next page. A script that "worked" with 800 users and returns 999 out of 3,412 when the company grows does not error: it gives incomplete data. `-All` on the cmdlets, or a loop over `nextLink` with `Invoke-MgGraphRequest`, is mandatory.

## 4. The report: devices with no check-in, with user and manager

:::term Get-StaleDevices.ps1
#Requires -Modules Microsoft.Graph.Authentication, Microsoft.Graph.Users, Microsoft.Graph.DeviceManagement
param([int]$Days = 30, [string]$Out = "stale-devices-$(Get-Date -Format yyyy-MM-dd).csv")

Connect-MgGraph -Scopes "User.Read.All","DeviceManagementManagedDevices.Read.All" -NoWelcome
$since = (Get-Date).AddDays(-$Days).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")

$devices = Get-MgDeviceManagementManagedDevice -All -Filter "lastSyncDateTime le $since" `
  -Property deviceName,userPrincipalName,operatingSystem,osVersion,lastSyncDateTime,complianceState,managedDeviceOwnerType

$cache = @{}
$rows = foreach ($d in $devices) {
  $mgr = $null
  if ($d.UserPrincipalName) {
    if (-not $cache.ContainsKey($d.UserPrincipalName)) {
      $u = Get-MgUser -UserId $d.UserPrincipalName -Property accountEnabled,department -ExpandProperty manager -ErrorAction SilentlyContinue
      $cache[$d.UserPrincipalName] = $u
    }
    $u = $cache[$d.UserPrincipalName]
    $mgr = $u.Manager.AdditionalProperties.userPrincipalName
  }
  [pscustomobject]@{
    Device = $d.DeviceName; OS = "$($d.OperatingSystem) $($d.OsVersion)"; Owner = $d.ManagedDeviceOwnerType
    LastSync = $d.LastSyncDateTime; DaysSilent = [int]((Get-Date) - $d.LastSyncDateTime).TotalDays
    Compliance = $d.ComplianceState; User = $d.UserPrincipalName; UserEnabled = $u.AccountEnabled
    Department = $u.Department; Manager = $mgr
  }
}
$rows | Sort-Object DaysSilent -Descending | Export-Csv $Out -NoTypeInformation -Encoding utf8
"$($rows.Count) devices with no check-in in $Days days -> $Out"
:::

:::term pwsh
$ ./Get-StaleDevices.ps1 -Days 30
47 devices with no check-in in 30 days -> stale-devices-2026-10-22.csv
$ Import-Csv .\\stale-devices-2026-10-22.csv | Where-Object UserEnabled -eq False | Select-Object Device, User, DaysSilent, Manager | Format-Table
Device         User                     DaysSilent Manager
------         ----                     ---------- -------
LAPTOP-3K8MQ2  j.navarro@contoso.com            53 m.ortega@contoso.com
DESKTOP-Q71A   p.ruiz@contoso.com               41 m.ortega@contoso.com
:::

This is what the portal does not give you on one screen: the laptop that has not synced for 53 days belongs to a **disabled** user (a leaver), and the person who has to return it is their manager. The user cache avoids 47 repeated calls for the same manager. The CSV goes to the leavers ticket and, with the Jenkins guide, the script is tested on every change.

## 5. Automate without a user: app registration

:::ui Entra admin center · App registrations
> Identity › Applications › App registrations › New registration
= Name: it-reports-graph
= Supported account types: This organization only
> it-reports-graph › API permissions › Add a permission › Microsoft Graph › Application permissions
[x] User.Read.All
[x] DeviceManagementManagedDevices.Read.All
[Grant admin consent for Contoso]
> it-reports-graph › Certificates & secrets › Certificates › Upload certificate
= Thumbprint: A1B2…F0 · Expires: 22/10/2027
:::

:::term pwsh · task server
$ $cert = New-SelfSignedCertificate -Subject "CN=it-reports-graph" -CertStoreLocation Cert:\\CurrentUser\\My -KeyExportPolicy NonExportable -NotAfter (Get-Date).AddYears(1)
$ Export-Certificate -Cert $cert -FilePath .\\it-reports-graph.cer     # this .cer is what you upload to the registration
$ Connect-MgGraph -ClientId "0a1b…-…" -TenantId "7f1c…-…" -CertificateThumbprint $cert.Thumbprint -NoWelcome
$ (Get-MgContext).AuthType
AppOnly
:::

For the scheduled task, the script uses a **certificate**, not a client secret: the private key never leaves the server and there is nothing to copy into a file. **Application** permissions (not delegated) are what matter here, and the admin consent lands in the audit log. Repo 20 on my GitHub reviews these registrations every month: who has which permission and when the certificate expires.

## 6. What you review each month

- IT app registrations: permissions granted versus used (`App registrations → the app → API permissions`), certificates expiring within 90 days.
- That no team script uses `Directory.ReadWrite.All` or `Mail.ReadWrite` "just in case".
- The interactive `-Scopes` you consented to yourself: `Enterprise applications → Microsoft Graph Command Line Tools → Permissions`; revoke what you don't use.

## Next steps

- **Writing, carefully**: `Update-MgUser`, `Invoke-MgSyncDeviceManagementManagedDevice` (force a check-in on the 47 in the report), always with `-WhatIf` first and on a small group.
- **Azure Automation** or a task on the tools server so the report reaches the Teams channel every Monday.
- The same queries work from Python (`msgraph-sdk`) or `curl` with a token: Graph is a REST API, PowerShell is just the most comfortable door for IT.
""")

# ---------------------------------------------------------------- L3 · NDES / Cloud PKI
g(slug="ndes-y-cloud-pki-certificados-a-los-dispositivos-desde-intune", topic="ndes-pki", date="2026-10-22",
  title_es="NDES y Cloud PKI: certificados a los dispositivos desde Intune para Wi-Fi y VPN",
  title_en="NDES and Cloud PKI: certificates to devices from Intune for Wi-Fi and VPN",
  dek_es="Las dos formas de dar certificados con Intune (NDES con tu CA de Windows o Microsoft Cloud PKI), los perfiles de certificado raíz y SCEP, el perfil de Wi-Fi que los usa y el certificado que nunca llega.",
  dek_en="The two ways of issuing certificates with Intune (NDES with your Windows CA or Microsoft Cloud PKI), the root and SCEP certificate profiles, the Wi-Fi profile that uses them, and the certificate that never arrives.",
  es="""
## Qué vas a conseguir

Que los portátiles y móviles gestionados se conecten a la Wi-Fi corporativa (y a la VPN) con un **certificado** en lugar de la contraseña del usuario: sin ventanas de credenciales, sin contraseñas de Wi-Fi guardadas en el móvil personal y con revocación al retirar el dispositivo. Dos caminos para emitirlos; eliges uno.

## Antes de empezar

- Dispositivos enrolados y conformes (guía de Intune).
- El RADIUS/NPS o el controlador Wi-Fi configurados para **EAP-TLS** confiando en la CA que emitirá (lo hace quien gestiona la red; necesita el certificado raíz del paso 2).
- **Camino A (NDES)**: una CA empresarial de Windows (AD CS) en marcha, un servidor Windows para NDES y el **conector de certificados de Intune**. Más piezas, pero reutiliza la PKI que ya tienes.
- **Camino B (Cloud PKI)**: licencia Intune Suite o el complemento Cloud PKI. Sin servidores; Microsoft aloja la CA.

## 1. Elegir el camino y crear la CA

:::ui Intune · Cloud PKI (camino B)
> Administración de inquilinos › Cloud PKI › Crear
= Nombre: Contoso Device Root CA
= Tipo de CA: Raíz
= Validez: 10 años · Algoritmo: RSA 4096 · SHA-256
[Crear]
> Cloud PKI › Crear
= Nombre: Contoso Device Issuing CA
= Tipo de CA: Emisora · CA raíz: Contoso Device Root CA
= Validez: 5 años · Usos extendidos de clave: Autenticación de cliente, Autenticación de servidor
= URI de SCEP: https://… (generado al crear)
[Crear]
:::

Con Cloud PKI, dos clics dan la raíz y la emisora, y la **URI de SCEP** que usarás en el paso 3. Con NDES el equivalente es: plantilla de certificado en AD CS para NDES, servidor NDES con el rol instalado, conector de Intune en ese servidor, y la URL pública del NDES (normalmente detrás de Entra Application Proxy). Microsoft tiene la lista de pasos; la parte que más falla es la cuenta de servicio de NDES y el SPN.

## 2. El certificado raíz en los dispositivos

:::term pwsh · CA de Windows (camino A) o descarga desde Cloud PKI (camino B)
$ certutil -ca.cert contoso-root.cer       # camino A: exporta la raíz desde la CA
$ certutil -dump contoso-root.cer | Select-String "Subject:|NotAfter"
Subject: CN=Contoso Root CA, DC=contoso, DC=local
NotAfter: 14/03/2035 10:02
:::

:::ui Intune · Configuración › Certificado de confianza
> Dispositivos › Configuración › Crear › Windows 10 and later › Plantillas › Certificado de confianza
= Nombre: Cert - Root CA - Windows
= Archivo de certificado: contoso-root.cer
= Almacén de destino: Almacén de certificados del equipo: raíz
= Asignaciones: Todos los usuarios · Filtro: f-windows-corp
[Crear]
:::

Un perfil de raíz **por plataforma** (Windows, macOS, iOS/iPadOS, Android Enterprise), con el mismo fichero. Es el que hace que el dispositivo confíe en el RADIUS y en los certificados que va a recibir. Si tu CA emisora es intermedia, también va su certificado en otro perfil.

## 3. El perfil SCEP

:::ui Intune · Configuración › Certificado SCEP
> Dispositivos › Configuración › Crear › Windows 10 and later › Plantillas › Certificado SCEP
= Nombre: Cert - Device Auth SCEP - Windows
= Tipo de certificado: Dispositivo
= Formato del nombre del firmante: CN={{DeviceName}},O=Contoso
= Nombre alternativo del firmante: URI = IntuneDeviceId://{{DeviceId}}
= Periodo de validez: 1 año · Tamaño de clave: 2048 · Algoritmo hash: SHA-2
= Uso de la clave: Firma digital, Cifrado de clave
= Uso mejorado de clave: Autenticación de cliente (1.3.6.1.5.5.7.3.2)
= Umbral de renovación: 20 %
= Certificado raíz: Cert - Root CA - Windows
= URL del servidor SCEP: https://scep.contoso.com/certsrv/mscep/mscep.dll (A) · https://…cloudpki…/scep (B)
= Asignaciones: Todos los usuarios · Filtro: f-windows-corp
[Crear]
:::

Certificado de **dispositivo** con el nombre del equipo para Wi-Fi corporativa (el equipo se conecta antes de que nadie inicie sesión); de **usuario** (`CN={{UserPrincipalName}}`) para VPN cuando el acceso depende de la persona. El **umbral de renovación del 20 %** hace que Intune pida uno nuevo cuando quede un quinto de validez: nadie se queda sin Wi-Fi el día que caduca.

## 4. El perfil de Wi-Fi que lo usa

:::ui Intune · Configuración › Wi-Fi
> Dispositivos › Configuración › Crear › Windows 10 and later › Plantillas › Wi-Fi › Empresa
= Nombre: Wi-Fi - Contoso-Corp - Windows
= Nombre de la red Wi-Fi (SSID): Contoso-Corp
[x] Conectarse automáticamente
= Tipo de EAP: EAP-TLS
= Confianza del servidor › Nombres de servidor de certificado: radius01.contoso.local; radius02.contoso.local
= Certificados raíz para la validación del servidor: Cert - Root CA - Windows
= Método de autenticación de cliente: Certificado SCEP → Cert - Device Auth SCEP - Windows
= Asignaciones: Todos los usuarios · Filtro: f-windows-corp
[Crear]
:::

Tres perfiles encadenados: raíz → SCEP → Wi-Fi. El orden de llegada lo gestiona Intune (el perfil de Wi-Fi espera al certificado), pero en el **primer** despliegue da margen: asigna raíz y SCEP, espera a ver certificados emitidos, y luego el de Wi-Fi.

## 5. El certificado que no llega

:::term pwsh · LAPTOP-7F2K9Q
$ Get-ChildItem Cert:\\LocalMachine\\My | Where-Object Issuer -like "*Contoso Device Issuing*" | Select-Object Subject, NotAfter, Thumbprint
# (vacío: no hay certificado)
$ Get-WinEvent -LogName "Microsoft-Windows-DeviceManagement-Enterprise-Diagnostics-Provider/Admin" -MaxEvents 200 | Where-Object Message -match "SCEP" | Select-Object -First 3 TimeCreated, Id, Message
TimeCreated          Id    Message
-----------          --    -------
22/10/2026 09:31:04  32    SCEP: Certificate enroll failed. Result: (The server returned an error: 0x80070005 Access denied). ...
:::

:::ui Intune · Estado del perfil SCEP
> Dispositivos › Configuración › Cert - Device Auth SCEP - Windows › Estado del dispositivo
= LAPTOP-7F2K9Q · Error · 0x80070005
> Administración de inquilinos › Conectores y tokens › Conectores de certificados (camino A)
= srv-ndes-01 · Estado: Activo · Última conexión: 22/10/2026 09:30
:::

Los cuatro sospechosos, en orden:

| Síntoma | Dónde mirar | Causa típica |
|---|---|---|
| Error en el estado del perfil, en todos los dispositivos | Conector de certificados (A) o estado de la CA (B) | Conector caído o cuenta de servicio de NDES con la contraseña caducada |
| Error solo en algunos dispositivos | Evento 32 en el dispositivo | El dispositivo no alcanza la URL de SCEP (proxy, firewall, Application Proxy sin publicar) |
| `0x80070005` / `Access denied` | NDES: `C:\\Windows\\System32\\certsrv\\mscep` y plantilla en AD CS | La plantilla no permite "Suministrar en la solicitud" o la cuenta de NDES no tiene **Enroll** |
| Certificado emitido, Wi-Fi no conecta | Registro del RADIUS/NPS (evento 6273) | El RADIUS no confía en la emisora, o el SAN no coincide con lo que espera |

Lo que no haces: reemitir a mano desde la CA. Si el dispositivo no puede pedirlo solo, tampoco podrá renovarlo.

## 6. Lo que revisas cada mes

- Perfil SCEP: dispositivos en **Error** frente a **Correcto** (`Estado del dispositivo`), y la tendencia tras cada cambio de red.
- Caducidad de la **CA emisora** y del certificado del **RADIUS**: ambos en el calendario con un año de antelación.
- Dispositivos retirados en Intune cuyo certificado sigue válido: con Cloud PKI, `Cloud PKI → la CA → Certificados emitidos → Revocar`; con NDES, la revocación en la CA y la CRL publicada.
- (Camino A) `Get-Service -Name W3SVC, "Intune Connector Service"` en el NDES y la cuenta de servicio en la lista de contraseñas que caducan.

## Siguientes pasos

- El mismo certificado de usuario para la **VPN** (perfil VPN con EAP-TLS) y, con Entra ID, la **autenticación basada en certificados** (CBA) para quien no puede usar la app Authenticator.
- **PKCS** en lugar de SCEP cuando el certificado tiene que incluir la clave privada generada por la CA (S/MIME); mismo conector, otro perfil.
- Documenta en Confluence (Nivel 2) la cadena completa: raíz, emisora, URL de SCEP, RADIUS y a quién llamar. Es el runbook que se abre el día que caduque algo.
""",
  en="""
## What you'll get

Managed laptops and phones connect to the corporate Wi-Fi (and the VPN) with a **certificate** instead of the user's password: no credential prompts, no Wi-Fi passwords saved on the personal phone, and revocation when the device is retired. Two paths to issue them; you pick one.

## Before you start

- Devices enrolled and compliant (Intune guide).
- The RADIUS/NPS or the Wi-Fi controller configured for **EAP-TLS**, trusting the CA that will issue (whoever manages the network does this; they need the root certificate from step 2).
- **Path A (NDES)**: a Windows enterprise CA (AD CS) running, a Windows server for NDES and the **Intune Certificate Connector**. More parts, but it reuses the PKI you already have.
- **Path B (Cloud PKI)**: an Intune Suite licence or the Cloud PKI add-on. No servers; Microsoft hosts the CA.

## 1. Choose the path and create the CA

:::ui Intune · Cloud PKI (path B)
> Tenant administration › Cloud PKI › Create
= Name: Contoso Device Root CA
= CA type: Root
= Validity: 10 years · Algorithm: RSA 4096 · SHA-256
[Create]
> Cloud PKI › Create
= Name: Contoso Device Issuing CA
= CA type: Issuing · Root CA: Contoso Device Root CA
= Validity: 5 years · Extended key usages: Client Authentication, Server Authentication
= SCEP URI: https://… (generated on creation)
[Create]
:::

With Cloud PKI, two clicks give you the root and the issuing CA, plus the **SCEP URI** you will use in step 3. With NDES the equivalent is: a certificate template in AD CS for NDES, an NDES server with the role installed, the Intune connector on that server, and the public URL of NDES (usually behind Entra Application Proxy). Microsoft has the step list; the part that fails most is the NDES service account and the SPN.

## 2. The root certificate on the devices

:::term pwsh · Windows CA (path A) or download from Cloud PKI (path B)
$ certutil -ca.cert contoso-root.cer       # path A: export the root from the CA
$ certutil -dump contoso-root.cer | Select-String "Subject:|NotAfter"
Subject: CN=Contoso Root CA, DC=contoso, DC=local
NotAfter: 14/03/2035 10:02
:::

:::ui Intune · Configuration › Trusted certificate
> Devices › Configuration › Create › Windows 10 and later › Templates › Trusted certificate
= Name: Cert - Root CA - Windows
= Certificate file: contoso-root.cer
= Destination store: Computer certificate store - Root
= Assignments: All users · Filter: f-windows-corp
[Create]
:::

One root profile **per platform** (Windows, macOS, iOS/iPadOS, Android Enterprise), with the same file. It is what makes the device trust the RADIUS and the certificates it is about to receive. If your issuing CA is an intermediate, its certificate goes in another profile too.

## 3. The SCEP profile

:::ui Intune · Configuration › SCEP certificate
> Devices › Configuration › Create › Windows 10 and later › Templates › SCEP certificate
= Name: Cert - Device Auth SCEP - Windows
= Certificate type: Device
= Subject name format: CN={{DeviceName}},O=Contoso
= Subject alternative name: URI = IntuneDeviceId://{{DeviceId}}
= Validity period: 1 year · Key size: 2048 · Hash algorithm: SHA-2
= Key usage: Digital signature, Key encipherment
= Extended key usage: Client Authentication (1.3.6.1.5.5.7.3.2)
= Renewal threshold: 20%
= Root certificate: Cert - Root CA - Windows
= SCEP server URL: https://scep.contoso.com/certsrv/mscep/mscep.dll (A) · https://…cloudpki…/scep (B)
= Assignments: All users · Filter: f-windows-corp
[Create]
:::

A **device** certificate with the computer name for corporate Wi-Fi (the device connects before anyone signs in); a **user** one (`CN={{UserPrincipalName}}`) for VPN when access depends on the person. The **20% renewal threshold** makes Intune request a new one when a fifth of the validity remains: nobody loses Wi-Fi on expiry day.

## 4. The Wi-Fi profile that uses it

:::ui Intune · Configuration › Wi-Fi
> Devices › Configuration › Create › Windows 10 and later › Templates › Wi-Fi › Enterprise
= Name: Wi-Fi - Contoso-Corp - Windows
= Wi-Fi name (SSID): Contoso-Corp
[x] Connect automatically
= EAP type: EAP-TLS
= Server Trust › Certificate server names: radius01.contoso.local; radius02.contoso.local
= Root certificates for server validation: Cert - Root CA - Windows
= Client authentication method: SCEP certificate → Cert - Device Auth SCEP - Windows
= Assignments: All users · Filter: f-windows-corp
[Create]
:::

Three chained profiles: root → SCEP → Wi-Fi. Intune handles the arrival order (the Wi-Fi profile waits for the certificate), but on the **first** rollout give it room: assign root and SCEP, wait until you see certificates issued, then the Wi-Fi one.

## 5. The certificate that never arrives

:::term pwsh · LAPTOP-7F2K9Q
$ Get-ChildItem Cert:\\LocalMachine\\My | Where-Object Issuer -like "*Contoso Device Issuing*" | Select-Object Subject, NotAfter, Thumbprint
# (empty: no certificate)
$ Get-WinEvent -LogName "Microsoft-Windows-DeviceManagement-Enterprise-Diagnostics-Provider/Admin" -MaxEvents 200 | Where-Object Message -match "SCEP" | Select-Object -First 3 TimeCreated, Id, Message
TimeCreated          Id    Message
-----------          --    -------
22/10/2026 09:31:04  32    SCEP: Certificate enroll failed. Result: (The server returned an error: 0x80070005 Access denied). ...
:::

:::ui Intune · SCEP profile status
> Devices › Configuration › Cert - Device Auth SCEP - Windows › Device status
= LAPTOP-7F2K9Q · Error · 0x80070005
> Tenant administration › Connectors and tokens › Certificate connectors (path A)
= srv-ndes-01 · Status: Active · Last connection: 22/10/2026 09:30
:::

The four suspects, in order:

| Symptom | Where to look | Typical cause |
|---|---|---|
| Error in the profile status, on every device | Certificate connector (A) or CA status (B) | Connector down or NDES service account with an expired password |
| Error on some devices only | Event 32 on the device | The device cannot reach the SCEP URL (proxy, firewall, Application Proxy not published) |
| `0x80070005` / `Access denied` | NDES: `C:\\Windows\\System32\\certsrv\\mscep` and the template in AD CS | The template does not allow "Supply in the request" or the NDES account lacks **Enroll** |
| Certificate issued, Wi-Fi does not connect | RADIUS/NPS log (event 6273) | RADIUS does not trust the issuing CA, or the SAN does not match what it expects |

What you don't do: reissue by hand from the CA. If the device cannot request it on its own, it won't be able to renew it either.

## 6. What you review each month

- SCEP profile: devices in **Error** versus **Succeeded** (`Device status`), and the trend after every network change.
- Expiry of the **issuing CA** and of the **RADIUS** certificate: both in the calendar a year ahead.
- Devices retired in Intune whose certificate is still valid: with Cloud PKI, `Cloud PKI → the CA → Issued certificates → Revoke`; with NDES, revocation at the CA and the CRL published.
- (Path A) `Get-Service -Name W3SVC, "Intune Connector Service"` on the NDES and the service account in the expiring-passwords list.

## Next steps

- The same user certificate for the **VPN** (VPN profile with EAP-TLS) and, with Entra ID, **certificate-based authentication** (CBA) for people who cannot use the Authenticator app.
- **PKCS** instead of SCEP when the certificate must include a CA-generated private key (S/MIME); same connector, different profile.
- Document the whole chain in Confluence (Level 2): root, issuing CA, SCEP URL, RADIUS and whom to call. It is the runbook that gets opened the day something expires.
""")

# ---------------------------------------------------------------- L3 · Databases
g(slug="postgresql-mysql-sql-server-tareas-de-operaciones-copia-restauracion-espacio-y-consulta-lenta", topic="databases", date="2026-10-22",
  title_es="PostgreSQL, MySQL y SQL Server: las tareas de operaciones, de la copia a la consulta lenta",
  title_en="PostgreSQL, MySQL and SQL Server: the operations tasks, from backup to slow query",
  dek_es="Lo que te piden de una base de datos sin ser DBA: conectar y ver qué hay, copia y restauración probada, espacio y crecimiento, altas y bajas de usuarios y qué consulta está bloqueando la aplicación, en los tres motores a la vez.",
  dek_en="What you are asked to do with a database without being a DBA: connect and see what is there, tested backup and restore, disk space and growth, user joiners and leavers, and which query is blocking the application, across the three engines side by side.",
  es="""
## Qué vas a conseguir

Resolver el 80 % de los tickets de base de datos que llegan a operaciones sin esperar al DBA: "la aplicación va lenta", "hay que dar acceso a X", "¿tenemos copia de ayer?", "el disco del servidor de base de datos está al 92 %". Los tres motores, el mismo gesto, con el comando de cada uno.

## Antes de empezar

- Acceso al servidor de cada motor (SSH o RDP) y una cuenta con permisos de administración de la base de datos, usada solo para estas tareas y con la contraseña en el gestor del equipo.
- Los clientes: `psql`, `mysql` y `sqlcmd` (en Windows viene con SQL Server; en Linux, el paquete `mssql-tools18`).
- Un directorio de copias con espacio igual al tamaño de la base de datos más grande, y el ticket de a quién avisar antes de restaurar nada.

## 1. Conectar y ver qué hay

:::term bash · srv-db-01
$ psql -h localhost -U postgres -c "\\l+" | awk -F'|' 'NR>3 {print $1, $7}' | head -5
 appdb        | 2412 MB
 postgres     | 7501 kB
$ mysql -u root -p -e "SELECT table_schema AS db, ROUND(SUM(data_length+index_length)/1024/1024) AS mb FROM information_schema.tables GROUP BY table_schema ORDER BY mb DESC;"
+--------------------+------+
| db                 | mb   |
+--------------------+------+
| intranet           | 1870 |
| mysql              |    3 |
+--------------------+------+
$ sqlcmd -S srv-sql-01 -E -Q "SELECT name, (SELECT SUM(size)*8/1024 FROM sys.master_files mf WHERE mf.database_id=d.database_id) AS mb FROM sys.databases d ORDER BY mb DESC" -W
name    mb
ERP     38210
tempdb  4096
master  7
:::

Antes de tocar nada: qué bases de datos hay, cuánto ocupan y, en el ticket, cuál es la de la aplicación que falla. `-E` en `sqlcmd` usa tu cuenta de Windows; en PostgreSQL y MySQL la cuenta de administración va en `~/.pgpass` y `~/.my.cnf` con permisos 600, nunca en la línea de comandos de un script.

## 2. Copia y restauración (probada)

:::term bash · srv-db-01
# PostgreSQL: copia lógica comprimida y restauración en una base de datos de prueba
$ pg_dump -h localhost -U postgres -Fc appdb -f /backup/appdb-$(date +%F).dump
$ createdb -h localhost -U postgres appdb_restore_test && pg_restore -h localhost -U postgres -d appdb_restore_test -j 4 /backup/appdb-$(date +%F).dump
$ psql -h localhost -U postgres -d appdb_restore_test -tAc "SELECT count(*) FROM orders;"
184233
# MySQL
$ mysqldump --single-transaction --routines --triggers intranet | gzip > /backup/intranet-$(date +%F).sql.gz
$ mysql -e "CREATE DATABASE intranet_restore_test" && zcat /backup/intranet-$(date +%F).sql.gz | mysql intranet_restore_test
:::

:::term sqlcmd · srv-sql-01
$ sqlcmd -S srv-sql-01 -E -Q "BACKUP DATABASE ERP TO DISK='E:\\Backup\\ERP_2026-10-22.bak' WITH COMPRESSION, CHECKSUM, STATS=10"
10 percent processed. ... 100 percent processed.
BACKUP DATABASE successfully processed 4891264 pages in 98.412 seconds (388.3 MB/sec).
$ sqlcmd -S srv-sql-01 -E -Q "RESTORE VERIFYONLY FROM DISK='E:\\Backup\\ERP_2026-10-22.bak' WITH CHECKSUM"
The backup set on file 1 is valid.
$ sqlcmd -S srv-sql-01 -E -Q "RESTORE DATABASE ERP_restore_test FROM DISK='E:\\Backup\\ERP_2026-10-22.bak' WITH MOVE 'ERP' TO 'E:\\Restore\\ERP_test.mdf', MOVE 'ERP_log' TO 'E:\\Restore\\ERP_test.ldf', STATS=25"
:::

Una copia que no se ha restaurado nunca es una esperanza, no una copia. La **restauración de prueba a otra base de datos** y un `count(*)` de la tabla principal es lo que apuntas en el ticket mensual de copias (y lo que el repo 33 de mi GitHub, backup-restore-test-tracker, sigue en el tiempo). Si el servidor ya tiene Veeam o un agente de copias (Nivel 2), estos comandos son la **verificación**, no el sustituto. Borra las bases de datos `*_restore_test` al terminar.

## 3. Espacio y crecimiento

:::term bash · srv-db-01
$ psql -h localhost -U postgres -d appdb -c "SELECT relname, pg_size_pretty(pg_total_relation_size(oid)) AS size, n_dead_tup FROM pg_stat_user_tables t JOIN pg_class c ON c.oid=t.relid ORDER BY pg_total_relation_size(oid) DESC LIMIT 3;"
   relname    |  size   | n_dead_tup
--------------+---------+------------
 audit_log    | 1412 MB |    2203110
 orders       |  611 MB |       8120
$ psql -h localhost -U postgres -d appdb -c "VACUUM (VERBOSE, ANALYZE) audit_log;" 2>&1 | tail -1
$ du -sh /var/lib/pgsql/16/data/pg_wal
3.1G    /var/lib/pgsql/16/data/pg_wal
:::

:::term sqlcmd · srv-sql-01
$ sqlcmd -S srv-sql-01 -E -d ERP -Q "SELECT name, size*8/1024 AS mb, CAST(FILEPROPERTY(name,'SpaceUsed') AS int)*8/1024 AS used_mb FROM sys.database_files" -W
name     mb     used_mb
ERP      36120  29877
ERP_log  2090   1912
$ sqlcmd -S srv-sql-01 -E -Q "SELECT name, recovery_model_desc, log_reuse_wait_desc FROM sys.databases WHERE name='ERP'" -W
name  recovery_model_desc  log_reuse_wait_desc
ERP   FULL                 LOG_BACKUP
:::

Los tres culpables habituales del disco al 92 %: en PostgreSQL, una tabla con millones de **tuplas muertas** sin `VACUUM` (y `pg_wal` creciendo porque un slot de replicación quedó huérfano); en MySQL, los **binlogs** sin `expire_logs_days`/`binlog_expire_logs_seconds`; en SQL Server, el **log de transacciones** en modo FULL sin copias de log: `log_reuse_wait_desc = LOG_BACKUP` lo dice, y la solución es programar `BACKUP LOG`, no `SHRINKFILE` cada semana.

## 4. Altas y bajas de usuarios

:::term bash · srv-db-01
# PostgreSQL: rol de solo lectura para el analista
$ psql -h localhost -U postgres -d appdb -c "CREATE ROLE laura_prado LOGIN PASSWORD 'cambiar-en-el-primer-login'; GRANT CONNECT ON DATABASE appdb TO laura_prado; GRANT USAGE ON SCHEMA public TO laura_prado; GRANT SELECT ON ALL TABLES IN SCHEMA public TO laura_prado; ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO laura_prado;"
# MySQL
$ mysql -e "CREATE USER 'laura_prado'@'10.20.%' IDENTIFIED BY 'cambiar-en-el-primer-login' PASSWORD EXPIRE; GRANT SELECT ON intranet.* TO 'laura_prado'@'10.20.%';"
# baja: revocar y, si no tiene objetos, eliminar
$ psql -h localhost -U postgres -d appdb -c "REASSIGN OWNED BY j_navarro TO postgres; DROP OWNED BY j_navarro; DROP ROLE j_navarro;"
:::

:::term sqlcmd · srv-sql-01
$ sqlcmd -S srv-sql-01 -E -Q "CREATE LOGIN [CONTOSO\\sg-erp-readonly] FROM WINDOWS; USE ERP; CREATE USER [CONTOSO\\sg-erp-readonly] FOR LOGIN [CONTOSO\\sg-erp-readonly]; ALTER ROLE db_datareader ADD MEMBER [CONTOSO\\sg-erp-readonly];"
:::

La regla que vale para los tres: **grupo, no persona**, siempre que el motor lo permita. SQL Server con un grupo de AD es el ideal: la baja se hace en Active Directory (Nivel 1) y no hay que tocar la base de datos. En PostgreSQL y MySQL, un rol de lectura con `GRANT` a usuarios nominales, y la lista de usuarios en la revisión trimestral de accesos.

## 5. "La aplicación va lenta": qué está pasando ahora

:::term bash · srv-db-01
$ psql -h localhost -U postgres -d appdb -c "SELECT pid, now()-query_start AS runtime, state, wait_event_type, left(query,60) AS query FROM pg_stat_activity WHERE state <> 'idle' AND pid <> pg_backend_pid() ORDER BY runtime DESC LIMIT 5;"
  pid  |     runtime     | state  | wait_event_type |                   query
-------+-----------------+--------+-----------------+----------------------------------------------
 18211 | 00:14:02.118    | active | Lock            | UPDATE orders SET status='X' WHERE customer_id=…
 18240 | 00:13:58.004    | active | Lock            | SELECT * FROM orders WHERE customer_id=…
 17990 | 00:14:40.771    | idle in transaction |  | BEGIN; UPDATE orders SET …
$ psql -h localhost -U postgres -d appdb -c "SELECT pg_terminate_backend(17990);"
$ mysql -e "SELECT id, user, time, state, LEFT(info,60) FROM information_schema.processlist WHERE command <> 'Sleep' ORDER BY time DESC LIMIT 5;"
:::

:::term sqlcmd · srv-sql-01
$ sqlcmd -S srv-sql-01 -E -Q "SELECT r.session_id, r.blocking_session_id, r.wait_type, r.wait_time/1000 AS wait_s, LEFT(t.text,60) AS sql_text FROM sys.dm_exec_requests r CROSS APPLY sys.dm_exec_sql_text(r.sql_handle) t WHERE r.session_id > 50 ORDER BY r.wait_time DESC" -W
session_id  blocking_session_id  wait_type  wait_s  sql_text
71          58                   LCK_M_U    812     UPDATE Invoices SET Status = …
58          0                    NULL       0       (sesión inactiva con transacción abierta)
:::

El patrón es idéntico en los tres: una sesión **inactiva con una transacción abierta** (alguien abrió una herramienta, hizo un `BEGIN` y se fue a comer) bloquea a todas las demás. `pg_stat_activity`, `processlist` y `dm_exec_requests` te dan el **pid de quién bloquea**; matar esa sesión (`pg_terminate_backend`, `KILL id`, `KILL session_id`) devuelve la aplicación a la vida, y el ticket al desarrollador dice qué consulta y desde qué cliente. Si no hay bloqueos y es una consulta pesada, `EXPLAIN ANALYZE` en PostgreSQL/MySQL o el plan de ejecución en SSMS es el siguiente paso, y ese sí es del DBA o del desarrollador.

## 6. Lo que revisas cada mes

- Restauración de prueba de cada motor, con el `count(*)` apuntado.
- Espacio: tablas que más crecen, `pg_wal`/binlogs/log de transacciones, y la previsión a seis meses con la tendencia.
- Usuarios: cuentas nominales que ya no están en Active Directory; contraseñas de las cuentas de aplicación en el gestor y con fecha.
- Parches del motor: PostgreSQL y MySQL con el parcheo mensual de Ansible; SQL Server con su CU trimestral en la ventana de cambios, con copia antes.

## Siguientes pasos

- **Monitorización**: `postgres_exporter`, `mysqld_exporter` y el de SQL Server en el Prometheus de la guía de Grafana; el panel de "sesiones bloqueadas > 0 durante 5 minutos" te avisa antes que el usuario.
- **Alta disponibilidad**: réplica en streaming (PostgreSQL), replicación (MySQL) y Always On (SQL Server) cuando el negocio no acepte una hora de parada; antes de eso, la restauración probada ya cubre lo importante.
- **Autenticación integrada** en PostgreSQL con Kerberos (guía de Linux + AD): la misma baja de AD cierra también la base de datos.
""",
  en="""
## What you'll get

Solve 80% of the database tickets that reach operations without waiting for the DBA: "the application is slow", "we need to give X access", "do we have yesterday's backup?", "the database server disk is at 92%". Three engines, the same move, with each one's command.

## Before you start

- Access to each engine's server (SSH or RDP) and an account with database administration rights, used only for these tasks and with its password in the team's password manager.
- The clients: `psql`, `mysql` and `sqlcmd` (on Windows it ships with SQL Server; on Linux, the `mssql-tools18` package).
- A backup directory with space equal to the largest database, and the ticket saying whom to warn before restoring anything.

## 1. Connect and see what is there

:::term bash · srv-db-01
$ psql -h localhost -U postgres -c "\\l+" | awk -F'|' 'NR>3 {print $1, $7}' | head -5
 appdb        | 2412 MB
 postgres     | 7501 kB
$ mysql -u root -p -e "SELECT table_schema AS db, ROUND(SUM(data_length+index_length)/1024/1024) AS mb FROM information_schema.tables GROUP BY table_schema ORDER BY mb DESC;"
+--------------------+------+
| db                 | mb   |
+--------------------+------+
| intranet           | 1870 |
| mysql              |    3 |
+--------------------+------+
$ sqlcmd -S srv-sql-01 -E -Q "SELECT name, (SELECT SUM(size)*8/1024 FROM sys.master_files mf WHERE mf.database_id=d.database_id) AS mb FROM sys.databases d ORDER BY mb DESC" -W
name    mb
ERP     38210
tempdb  4096
master  7
:::

Before touching anything: which databases exist, how big they are and, in the ticket, which one belongs to the failing application. `-E` in `sqlcmd` uses your Windows account; in PostgreSQL and MySQL the admin account goes in `~/.pgpass` and `~/.my.cnf` with 600 permissions, never on a script's command line.

## 2. Backup and (tested) restore

:::term bash · srv-db-01
# PostgreSQL: compressed logical backup and restore into a test database
$ pg_dump -h localhost -U postgres -Fc appdb -f /backup/appdb-$(date +%F).dump
$ createdb -h localhost -U postgres appdb_restore_test && pg_restore -h localhost -U postgres -d appdb_restore_test -j 4 /backup/appdb-$(date +%F).dump
$ psql -h localhost -U postgres -d appdb_restore_test -tAc "SELECT count(*) FROM orders;"
184233
# MySQL
$ mysqldump --single-transaction --routines --triggers intranet | gzip > /backup/intranet-$(date +%F).sql.gz
$ mysql -e "CREATE DATABASE intranet_restore_test" && zcat /backup/intranet-$(date +%F).sql.gz | mysql intranet_restore_test
:::

:::term sqlcmd · srv-sql-01
$ sqlcmd -S srv-sql-01 -E -Q "BACKUP DATABASE ERP TO DISK='E:\\Backup\\ERP_2026-10-22.bak' WITH COMPRESSION, CHECKSUM, STATS=10"
10 percent processed. ... 100 percent processed.
BACKUP DATABASE successfully processed 4891264 pages in 98.412 seconds (388.3 MB/sec).
$ sqlcmd -S srv-sql-01 -E -Q "RESTORE VERIFYONLY FROM DISK='E:\\Backup\\ERP_2026-10-22.bak' WITH CHECKSUM"
The backup set on file 1 is valid.
$ sqlcmd -S srv-sql-01 -E -Q "RESTORE DATABASE ERP_restore_test FROM DISK='E:\\Backup\\ERP_2026-10-22.bak' WITH MOVE 'ERP' TO 'E:\\Restore\\ERP_test.mdf', MOVE 'ERP_log' TO 'E:\\Restore\\ERP_test.ldf', STATS=25"
:::

A backup that has never been restored is a hope, not a backup. The **test restore into another database** and a `count(*)` of the main table is what you note in the monthly backup ticket (and what repo 33 on my GitHub, backup-restore-test-tracker, follows over time). If the server already has Veeam or a backup agent (Level 2), these commands are the **verification**, not the substitute. Drop the `*_restore_test` databases when done.

## 3. Disk space and growth

:::term bash · srv-db-01
$ psql -h localhost -U postgres -d appdb -c "SELECT relname, pg_size_pretty(pg_total_relation_size(oid)) AS size, n_dead_tup FROM pg_stat_user_tables t JOIN pg_class c ON c.oid=t.relid ORDER BY pg_total_relation_size(oid) DESC LIMIT 3;"
   relname    |  size   | n_dead_tup
--------------+---------+------------
 audit_log    | 1412 MB |    2203110
 orders       |  611 MB |       8120
$ psql -h localhost -U postgres -d appdb -c "VACUUM (VERBOSE, ANALYZE) audit_log;" 2>&1 | tail -1
$ du -sh /var/lib/pgsql/16/data/pg_wal
3.1G    /var/lib/pgsql/16/data/pg_wal
:::

:::term sqlcmd · srv-sql-01
$ sqlcmd -S srv-sql-01 -E -d ERP -Q "SELECT name, size*8/1024 AS mb, CAST(FILEPROPERTY(name,'SpaceUsed') AS int)*8/1024 AS used_mb FROM sys.database_files" -W
name     mb     used_mb
ERP      36120  29877
ERP_log  2090   1912
$ sqlcmd -S srv-sql-01 -E -Q "SELECT name, recovery_model_desc, log_reuse_wait_desc FROM sys.databases WHERE name='ERP'" -W
name  recovery_model_desc  log_reuse_wait_desc
ERP   FULL                 LOG_BACKUP
:::

The three usual culprits for a disk at 92%: in PostgreSQL, a table with millions of **dead tuples** without `VACUUM` (and `pg_wal` growing because a replication slot was orphaned); in MySQL, **binlogs** without `expire_logs_days`/`binlog_expire_logs_seconds`; in SQL Server, the **transaction log** in FULL recovery with no log backups: `log_reuse_wait_desc = LOG_BACKUP` says so, and the fix is scheduling `BACKUP LOG`, not `SHRINKFILE` every week.

## 4. User joiners and leavers

:::term bash · srv-db-01
# PostgreSQL: read-only role for the analyst
$ psql -h localhost -U postgres -d appdb -c "CREATE ROLE laura_prado LOGIN PASSWORD 'change-on-first-login'; GRANT CONNECT ON DATABASE appdb TO laura_prado; GRANT USAGE ON SCHEMA public TO laura_prado; GRANT SELECT ON ALL TABLES IN SCHEMA public TO laura_prado; ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO laura_prado;"
# MySQL
$ mysql -e "CREATE USER 'laura_prado'@'10.20.%' IDENTIFIED BY 'change-on-first-login' PASSWORD EXPIRE; GRANT SELECT ON intranet.* TO 'laura_prado'@'10.20.%';"
# leaver: revoke and, if they own no objects, drop
$ psql -h localhost -U postgres -d appdb -c "REASSIGN OWNED BY j_navarro TO postgres; DROP OWNED BY j_navarro; DROP ROLE j_navarro;"
:::

:::term sqlcmd · srv-sql-01
$ sqlcmd -S srv-sql-01 -E -Q "CREATE LOGIN [CONTOSO\\sg-erp-readonly] FROM WINDOWS; USE ERP; CREATE USER [CONTOSO\\sg-erp-readonly] FOR LOGIN [CONTOSO\\sg-erp-readonly]; ALTER ROLE db_datareader ADD MEMBER [CONTOSO\\sg-erp-readonly];"
:::

The rule that holds for all three: **group, not person**, whenever the engine allows it. SQL Server with an AD group is the ideal: the leaver is handled in Active Directory (Level 1) and the database is never touched. In PostgreSQL and MySQL, a read role with `GRANT` to named users, and the user list in the quarterly access review.

## 5. "The application is slow": what is happening right now

:::term bash · srv-db-01
$ psql -h localhost -U postgres -d appdb -c "SELECT pid, now()-query_start AS runtime, state, wait_event_type, left(query,60) AS query FROM pg_stat_activity WHERE state <> 'idle' AND pid <> pg_backend_pid() ORDER BY runtime DESC LIMIT 5;"
  pid  |     runtime     | state  | wait_event_type |                   query
-------+-----------------+--------+-----------------+----------------------------------------------
 18211 | 00:14:02.118    | active | Lock            | UPDATE orders SET status='X' WHERE customer_id=…
 18240 | 00:13:58.004    | active | Lock            | SELECT * FROM orders WHERE customer_id=…
 17990 | 00:14:40.771    | idle in transaction |  | BEGIN; UPDATE orders SET …
$ psql -h localhost -U postgres -d appdb -c "SELECT pg_terminate_backend(17990);"
$ mysql -e "SELECT id, user, time, state, LEFT(info,60) FROM information_schema.processlist WHERE command <> 'Sleep' ORDER BY time DESC LIMIT 5;"
:::

:::term sqlcmd · srv-sql-01
$ sqlcmd -S srv-sql-01 -E -Q "SELECT r.session_id, r.blocking_session_id, r.wait_type, r.wait_time/1000 AS wait_s, LEFT(t.text,60) AS sql_text FROM sys.dm_exec_requests r CROSS APPLY sys.dm_exec_sql_text(r.sql_handle) t WHERE r.session_id > 50 ORDER BY r.wait_time DESC" -W
session_id  blocking_session_id  wait_type  wait_s  sql_text
71          58                   LCK_M_U    812     UPDATE Invoices SET Status = …
58          0                    NULL       0       (idle session with an open transaction)
:::

The pattern is identical in all three: an **idle session with an open transaction** (someone opened a tool, ran `BEGIN` and went to lunch) blocks everyone else. `pg_stat_activity`, `processlist` and `dm_exec_requests` give you the **pid of whoever is blocking**; killing that session (`pg_terminate_backend`, `KILL id`, `KILL session_id`) brings the application back to life, and the ticket to the developer says which query and from which client. If there are no locks and it is a heavy query, `EXPLAIN ANALYZE` in PostgreSQL/MySQL or the execution plan in SSMS is the next step, and that one does belong to the DBA or the developer.

## 6. What you review each month

- Test restore of each engine, with the `count(*)` noted.
- Space: fastest-growing tables, `pg_wal`/binlogs/transaction log, and the six-month forecast from the trend.
- Users: named accounts no longer in Active Directory; application account passwords in the manager with a date.
- Engine patches: PostgreSQL and MySQL with the monthly Ansible patching; SQL Server with its quarterly CU in the change window, with a backup first.

## Next steps

- **Monitoring**: `postgres_exporter`, `mysqld_exporter` and the SQL Server one in the Prometheus from the Grafana guide; the "blocked sessions > 0 for 5 minutes" panel warns you before the user does.
- **High availability**: streaming replica (PostgreSQL), replication (MySQL) and Always On (SQL Server) when the business won't accept an hour of downtime; before that, the tested restore already covers what matters.
- **Integrated authentication** in PostgreSQL with Kerberos (Linux + AD guide): the same AD leaver closes the database too.
""")

# ---------------------------------------------------------------- L3 · SolarWinds
g(slug="solarwinds-anadir-un-nodo-afinar-una-alerta-y-leer-que-paso-antes-de-la-caida", topic="solarwinds", date="2026-10-22",
  title_es="SolarWinds: añadir un nodo, afinar una alerta que salta demasiado y leer qué pasó antes de la caída",
  title_en="SolarWinds: adding a node, tuning an alert that fires too much and reading what happened before the outage",
  dek_es="Un servidor nuevo en la plataforma con SNMP o agente, los umbrales por nodo en lugar de globales, la alerta con condición sostenida y la vista de PerfStack para la pregunta de la reunión: ¿qué pasó a las 03:12?",
  dek_en="A new server on the platform via SNMP or agent, per-node thresholds instead of global ones, the alert with a sustained condition, and the PerfStack view for the meeting question: what happened at 03:12?",
  es="""
## Qué vas a conseguir

Que un servidor nuevo esté monitorizado el mismo día que entra en producción, que las alertas que llegan al equipo sean las que hay que atender (y no las 40 de cada noche que todos ignoran), y poder reconstruir en cinco minutos qué pasó en un servidor antes de que cayera.

## Antes de empezar

- Acceso a la consola web de SolarWinds Platform (Orion) con un rol que pueda añadir nodos y editar alertas.
- En el servidor nuevo: **SNMP v3** configurado (usuario, autenticación y cifrado; nunca v2c con `public`) o permiso para instalar el **agente** de SolarWinds. Para Windows, WMI con una cuenta de servicio de solo lectura también vale.
- El firewall entre el servidor de sondeo y el nodo: UDP 161 (SNMP) o TCP 17778 (agente).
- El runbook de a quién llama cada alerta (Confluence, Nivel 2).

## 1. Añadir el nodo

:::ui SolarWinds Platform · Add Node
> Settings › Manage Nodes › Add Node
= Polling Hostname or IP Address: srv-app-01.contoso.local
= Polling Method: Most Devices: SNMP and ICMP
= SNMP Version: SNMPv3
= Credential: snmp-ro-contoso (authPriv · SHA · AES128)
[Test] Test successful.
[Next]
> Choose Resources
[x] CPU & Memory · [x] Volumes: / , /var, /backup · [x] Interfaces: ens192
[ ] Interfaces: lo
> Add Application Monitors
[x] Linux - Core Monitoring (SAM)
> Change Properties
= Custom Properties: Owner_Team = IT Ops · Environment = Production · Site = Madrid · Service = Intranet
[OK, Add Node]
:::

Las **propiedades personalizadas** son lo que luego usas para todo: a quién va la alerta (`Owner_Team`), si despierta a alguien (`Environment`), en qué informe sale (`Service`). Un nodo sin propiedades es un nodo que avisa a nadie. Deja fuera `lo` y los volúmenes temporales: cada recurso sondeado es ruido potencial.

> Consejo: con el **agente** en lugar de SNMP (`Settings → Agents → Download Agent`), el nodo sigue reportando aunque cambie de IP o esté detrás de un NAT, y SAM puede leer logs y procesos. Para servidores en la nube o en sedes remotas, es la opción.

## 2. Umbrales por nodo

:::ui SolarWinds Platform · Edit Node
> srv-db-01.contoso.local › Edit Properties › Alerting Thresholds
Memory
[x] Override Orion General Thresholds
= Warning: 92 % · Critical: 97 %
Disk Volume /backup
[x] Override · Warning: 90 % · Critical: 95 %
CPU
= (Use Orion General Thresholds: 80 % / 90 %)
[Submit]
:::

Un servidor de base de datos con el 90 % de memoria usada está bien: es la caché. Un servidor web al 90 % está a punto de caer. Los umbrales globales (`Settings → Thresholds`) sirven para el 80 % de los nodos; el 20 % restante (bases de datos, hipervisores, el volumen de copias que siempre está lleno) necesita el suyo. Esto solo ya quita la mitad de las alertas de la noche.

## 3. La alerta con condición sostenida

:::ui SolarWinds Platform · Manage Alerts
> Alerts & Activity › Alerts › Manage Alerts › Add New Alert
= Name: Node down - Production - IT Ops
= Severity: Critical
Trigger Condition
= I want to alert on: Node
= Scope: Node · Environment is equal to Production · AND Owner_Team is equal to IT Ops
= Actual trigger condition: Node Status is equal to Down
= Condition must exist for more than: 5 minutes
Reset Condition
= Reset this alert when trigger condition is no longer true
Trigger Actions
= Send an Email/Page: it-ops-oncall@contoso.com · Subject: [${N=Alerting;M=Severity}] ${N=SwisEntity;M=Caption} is ${N=SwisEntity;M=Status}
= Message: Runbook: https://wiki.contoso.local/it/runbooks/node-down · Owner: ${N=SwisEntity;M=CustomProperties.Owner_Team}
= Post to Microsoft Teams: it-ops channel
Time of Day
= Alert enabled: 24x7 (Production) · otra alerta igual con Environment = Test, solo laborables 08-19
[Submit]
:::

Tres decisiones hacen la diferencia entre una alerta y una molestia: **ámbito por propiedades** (no "todos los nodos"), **condición sostenida** cinco minutos (un reinicio planificado dura tres) y **runbook en el mensaje**. Para Test, la misma alerta en horario laboral y a un buzón, no al teléfono de guardia. Y la de "interfaz caída" solo para interfaces marcadas como `Critical = Yes` en sus propiedades: no para el `ens192` que alguien desconectó en el laboratorio.

## 4. La alerta que salta demasiado

:::ui SolarWinds Platform · Active Alerts
> Alerts & Activity › Alerts › Group by: Alert name · Last 7 days
= High CPU - All nodes: 312 triggers · 14 nodos · 0 reconocidas
= Node down - Production - IT Ops: 3 triggers · 2 nodos · 3 reconocidas
= Volume > 90% - All nodes: 88 triggers · 1 nodo (srv-db-01 /backup) · 0 reconocidas
[Acknowledge] [Edit Alert Definition]
:::

El informe de **alertas por nombre** de la última semana es la lista de tareas: 312 disparos de CPU que nadie reconoce es una alerta que hay que cambiar (umbral sostenido 15 minutos y solo Production), no un servidor que arreglar; 88 del mismo volumen es un umbral por nodo del paso 2 o, mejor, el ticket de limpiar `/backup`. La métrica que llevas a la reunión: **alertas reconocidas / disparadas**. Si está por debajo del 50 %, la plataforma avisa pero nadie escucha.

## 5. ¿Qué pasó a las 03:12? PerfStack

:::ui SolarWinds Platform · PerfStack
> My Dashboards › Performance Analysis › srv-app-01.contoso.local
= Time range: 22/10/2026 02:30 – 04:00
Métricas en el panel
= Node › CPU Load · Memory Used % · Response Time
= Volume / › Disk Space Used %
= Application › Linux - Core Monitoring › Process: java · Memory
= Events › Node events
Línea de tiempo
= 02:58  Memory Used % sube de 71 a 96 en 8 min
= 03:04  Process java Memory: 11,2 GB
= 03:09  Volume / : 100 % (logs)
= 03:12  Node Status: Down · Event: "Node srv-app-01 went down"
= 03:31  Node Status: Up (reinicio por la guardia)
[Share] [Save]
:::

PerfStack pone en una sola línea de tiempo lo que estaba disperso: la memoria del proceso Java se dispara, llena el disco de logs y el nodo cae. Esa pantalla, con **Share**, es el enlace que va al post-mortem en lugar de cuatro capturas. Junto con los logs centralizados de la guía de ELK (la hora de las 02:58 en Kibana dice qué petición disparó el consumo), tienes la causa en diez minutos.

## 6. Lo que revisas cada mes

- Nodos en estado **Unknown** o **Unmanaged** desde hace más de una semana: `Manage Nodes → filtro por estado`. Unmanaged es para mantenimientos; con un mes, se olvidó.
- Nodos **sin propiedades** (`Owner_Team` vacío): la consulta SWQL `SELECT Caption FROM Orion.Nodes WHERE CustomProperties.Owner_Team IS NULL`.
- Alertas disparadas frente a reconocidas; las tres alertas más ruidosas y qué se hizo con ellas.
- Capacidad del propio servidor de sondeo (`Settings → Polling Engines`): porcentaje de elementos sondeados frente al límite de la licencia.

## Siguientes pasos

- **Dependencias** (`Settings → Manage Dependencies`): si el switch de la sede cae, una alerta, no cuarenta de los servidores detrás.
- **NetFlow (NTA)** en el router de la sede para la pregunta "¿quién está saturando el enlace?", y **NCM** para guardar la configuración de los Cisco (Nivel 4) y avisar de cambios.
- Exporta las alertas a Teams con el runbook y, si el equipo tiene herramienta de guardia, por su webhook: el teléfono suena solo para `Critical` en `Production`.
""",
  en="""
## What you'll get

A new server is monitored the same day it goes into production, the alerts that reach the team are the ones that need attention (not the 40 a night that everyone ignores), and you can reconstruct in five minutes what happened on a server before it went down.

## Before you start

- Access to the SolarWinds Platform (Orion) web console with a role that can add nodes and edit alerts.
- On the new server: **SNMP v3** configured (user, authentication and encryption; never v2c with `public`) or permission to install the SolarWinds **agent**. For Windows, WMI with a read-only service account also works.
- The firewall between the polling engine and the node: UDP 161 (SNMP) or TCP 17778 (agent).
- The runbook of whom each alert calls (Confluence, Level 2).

## 1. Add the node

:::ui SolarWinds Platform · Add Node
> Settings › Manage Nodes › Add Node
= Polling Hostname or IP Address: srv-app-01.contoso.local
= Polling Method: Most Devices: SNMP and ICMP
= SNMP Version: SNMPv3
= Credential: snmp-ro-contoso (authPriv · SHA · AES128)
[Test] Test successful.
[Next]
> Choose Resources
[x] CPU & Memory · [x] Volumes: / , /var, /backup · [x] Interfaces: ens192
[ ] Interfaces: lo
> Add Application Monitors
[x] Linux - Core Monitoring (SAM)
> Change Properties
= Custom Properties: Owner_Team = IT Ops · Environment = Production · Site = Madrid · Service = Intranet
[OK, Add Node]
:::

**Custom properties** are what you later use for everything: whom the alert goes to (`Owner_Team`), whether it wakes someone (`Environment`), which report it appears in (`Service`). A node without properties is a node that notifies nobody. Leave out `lo` and temporary volumes: every polled resource is potential noise.

> Tip: with the **agent** instead of SNMP (`Settings → Agents → Download Agent`), the node keeps reporting even if it changes IP or sits behind NAT, and SAM can read logs and processes. For servers in the cloud or at remote sites, it is the option.

## 2. Per-node thresholds

:::ui SolarWinds Platform · Edit Node
> srv-db-01.contoso.local › Edit Properties › Alerting Thresholds
Memory
[x] Override Orion General Thresholds
= Warning: 92% · Critical: 97%
Disk Volume /backup
[x] Override · Warning: 90% · Critical: 95%
CPU
= (Use Orion General Thresholds: 80% / 90%)
[Submit]
:::

A database server at 90% memory used is fine: that is the cache. A web server at 90% is about to fall over. Global thresholds (`Settings → Thresholds`) work for 80% of nodes; the remaining 20% (databases, hypervisors, the backup volume that is always full) need their own. This alone removes half of the night-time alerts.

## 3. The alert with a sustained condition

:::ui SolarWinds Platform · Manage Alerts
> Alerts & Activity › Alerts › Manage Alerts › Add New Alert
= Name: Node down - Production - IT Ops
= Severity: Critical
Trigger Condition
= I want to alert on: Node
= Scope: Node · Environment is equal to Production · AND Owner_Team is equal to IT Ops
= Actual trigger condition: Node Status is equal to Down
= Condition must exist for more than: 5 minutes
Reset Condition
= Reset this alert when trigger condition is no longer true
Trigger Actions
= Send an Email/Page: it-ops-oncall@contoso.com · Subject: [${N=Alerting;M=Severity}] ${N=SwisEntity;M=Caption} is ${N=SwisEntity;M=Status}
= Message: Runbook: https://wiki.contoso.local/it/runbooks/node-down · Owner: ${N=SwisEntity;M=CustomProperties.Owner_Team}
= Post to Microsoft Teams: it-ops channel
Time of Day
= Alert enabled: 24x7 (Production) · a twin alert with Environment = Test, weekdays 08-19 only
[Submit]
:::

Three decisions make the difference between an alert and a nuisance: **scope by properties** (not "all nodes"), a **sustained condition** of five minutes (a planned reboot takes three) and the **runbook in the message**. For Test, the same alert in working hours to a mailbox, not the on-call phone. And the "interface down" alert only for interfaces marked `Critical = Yes` in their properties: not for the `ens192` someone unplugged in the lab.

## 4. The alert that fires too much

:::ui SolarWinds Platform · Active Alerts
> Alerts & Activity › Alerts › Group by: Alert name · Last 7 days
= High CPU - All nodes: 312 triggers · 14 nodes · 0 acknowledged
= Node down - Production - IT Ops: 3 triggers · 2 nodes · 3 acknowledged
= Volume > 90% - All nodes: 88 triggers · 1 node (srv-db-01 /backup) · 0 acknowledged
[Acknowledge] [Edit Alert Definition]
:::

The **alerts by name** report for the last week is the to-do list: 312 CPU triggers nobody acknowledges is an alert to change (sustained 15 minutes and Production only), not a server to fix; 88 from the same volume is a per-node threshold from step 2 or, better, the ticket to clean up `/backup`. The metric you take to the meeting: **acknowledged / triggered alerts**. Below 50%, the platform is warning but nobody is listening.

## 5. What happened at 03:12? PerfStack

:::ui SolarWinds Platform · PerfStack
> My Dashboards › Performance Analysis › srv-app-01.contoso.local
= Time range: 22/10/2026 02:30 – 04:00
Metrics on the board
= Node › CPU Load · Memory Used % · Response Time
= Volume / › Disk Space Used %
= Application › Linux - Core Monitoring › Process: java · Memory
= Events › Node events
Timeline
= 02:58  Memory Used % climbs from 71 to 96 in 8 min
= 03:04  Process java Memory: 11.2 GB
= 03:09  Volume / : 100% (logs)
= 03:12  Node Status: Down · Event: "Node srv-app-01 went down"
= 03:31  Node Status: Up (reboot by on-call)
[Share] [Save]
:::

PerfStack puts on one timeline what was scattered: the Java process memory spikes, fills the disk with logs and the node goes down. That screen, with **Share**, is the link that goes into the post-mortem instead of four screenshots. Together with the centralised logs from the ELK guide (the 02:58 timestamp in Kibana says which request triggered the consumption), you have the cause in ten minutes.

## 6. What you review each month

- Nodes in **Unknown** or **Unmanaged** state for more than a week: `Manage Nodes → filter by status`. Unmanaged is for maintenance; after a month, it was forgotten.
- Nodes **without properties** (`Owner_Team` empty): the SWQL query `SELECT Caption FROM Orion.Nodes WHERE CustomProperties.Owner_Team IS NULL`.
- Alerts triggered versus acknowledged; the three noisiest alerts and what was done about them.
- Capacity of the polling engine itself (`Settings → Polling Engines`): percentage of polled elements against the licence limit.

## Next steps

- **Dependencies** (`Settings → Manage Dependencies`): if the site switch goes down, one alert, not forty from the servers behind it.
- **NetFlow (NTA)** on the site router for the question "who is saturating the link?", and **NCM** to store the Cisco configurations (Level 4) and warn about changes.
- Export alerts to Teams with the runbook and, if the team has an on-call tool, through its webhook: the phone rings only for `Critical` in `Production`.
""")

# ---------------------------------------------------------------- L3 · Ubuntu Landscape
g(slug="ubuntu-landscape-registrar-la-flota-y-parchear-por-grupos-con-ventana", topic="landscape", date="2026-10-22",
  title_es="Ubuntu Landscape: registrar la flota de Ubuntu y parchear por grupos con ventana",
  title_en="Ubuntu Landscape: registering the Ubuntu fleet and patching by group within a window",
  dek_es="El cliente de Landscape con Ubuntu Pro, grupos de acceso y etiquetas, el perfil de actualizaciones que parchea cada grupo en su ventana, los reinicios pendientes y el informe de CVE para la reunión de parcheo.",
  dek_en="The Landscape client with Ubuntu Pro, access groups and tags, the upgrade profile that patches each group in its window, pending reboots and the CVE report for the patching meeting.",
  es="""
## Qué vas a conseguir

Ver los servidores (y los escritorios) Ubuntu en una consola: qué versión tienen, qué parches les faltan, cuáles necesitan reinicio, y que las actualizaciones de seguridad se apliquen solas por grupos, en la ventana de cada grupo, con un informe para el ticket mensual. Es lo que Ansible hace por línea de comandos (guía de Ansible), con la vista de flota que el negocio quiere ver.

## Antes de empezar

- **Ubuntu Pro** activado en las máquinas (`pro status`); Landscape SaaS viene incluido, y la versión autoalojada también requiere Pro en los clientes.
- Acceso a `landscape.canonical.com` (SaaS) o al servidor Landscape propio con una cuenta de administrador.
- Decidir los **grupos**: por entorno (prod, test) y por ventana de parcheo (martes 22:00, jueves 22:00). Dos o tres grupos bastan al principio.
- Salida HTTPS de los clientes hacia Landscape.

## 1. Registrar un cliente

:::term bash · srv-web-02 (Ubuntu 24.04)
$ sudo pro status | grep -E 'landscape|esm-infra'
esm-infra        yes       enabled   Expanded Security Maintenance for Infrastructure
landscape        yes       disabled  Management and administration tool for Ubuntu
$ sudo apt-get install -y landscape-client
$ sudo landscape-config --computer-title "srv-web-02" --account-name contoso-it --registration-key "$(sudo cat /root/.landscape-key)" --tags prod,web,window-tue --access-group prod --silent
Please wait...
System successfully registered.
$ sudo landscape-config --is-registered && echo REGISTERED
REGISTERED
:::

:::ui Landscape · Computers
> Computers › Pending computers
= srv-web-02 · Ubuntu 24.04.1 LTS · Tags: prod, web, window-tue · Access group: prod
[Accept] [Reject]
:::

Tres cosas en el registro: el **título** igual que el hostname, las **etiquetas** (entorno, rol y ventana) y el **grupo de acceso**, que decide quién puede administrar la máquina en Landscape. La clave de registro va en un fichero con permisos 600, no en el historial de Bash; con Ansible, este paso es una tarea con la clave en `ansible-vault`. En **Pending computers** aceptas (o automatizas la aceptación por clave).

## 2. Grupos de acceso y etiquetas

:::ui Landscape · Access groups
> Account › Access groups
= global · (todo)
= prod · Padre: global · Administradores: IT Ops · Equipos: 23
= test · Padre: global · Administradores: IT Ops, Desarrollo · Equipos: 11
> Computers › Search
= tag:prod AND tag:window-tue
= Resultados: 12 equipos
[Save search as: prod-tuesday]
:::

Los **grupos de acceso** controlan permisos (Desarrollo puede reiniciar los de test, no los de prod); las **etiquetas** controlan a quién se aplica cada perfil. Una búsqueda guardada (`prod-tuesday`) es lo que luego referencias en los perfiles y los informes. Si una máquina cambia de ventana, cambias la etiqueta y nada más.

## 3. El perfil de actualizaciones

:::ui Landscape · Upgrade profiles
> Profiles › Upgrade profiles › Add upgrade profile
= Name: prod-security-tuesday
= Upgrade type: [x] Security upgrades only
= Schedule: Weekly · Tuesday · 22:00 · Deliver within: 2 hours
= Autoremove: [x]
= Access group: prod
= Tags: prod, window-tue
[Save]
> Profiles › Upgrade profiles › Add upgrade profile
= Name: test-all-wednesday
= Upgrade type: [x] All upgrades
= Schedule: Weekly · Wednesday · 20:00 · Deliver within: 2 hours
= Tags: test
[Save]
:::

**Test recibe todo los miércoles; prod recibe solo seguridad los martes**, una semana después de que lo mismo haya pasado por test. Lo que no es seguridad en prod va en el ciclo mensual, como ventana de cambios con su ticket. **Deliver within: 2 hours** reparte el inicio para que doce servidores no descarguen a la vez.

## 4. Reinicios pendientes

:::ui Landscape · Computers
> Computers › Search: tag:prod AND alert:computer-reboot
= srv-web-01 · Reboot required · Since: 21/10/2026 22:41 · Kernel 6.8.0-47 → 6.8.0-48
= srv-db-01 · Reboot required · Since: 21/10/2026 22:38
= Resultados: 5 equipos
[Select all] [Reboot] › Deliver after: 22/10/2026 23:00 · Deliver within: 1 hour
= Activity queued: "Reboot 5 computers" · Approval: required (prod)
:::

El parche de seguridad se aplica solo; el **reinicio no**, y bien está. La alerta `computer-reboot` lista quién lo necesita; la actividad de reinicio se programa a la hora de la ventana y, en prod, exige **aprobación** de un segundo administrador (`Account → Alerts → Computer reboot required` y `Activities → Approval required`). Eso es el ticket de cambio con cuatro ojos sin salir de la consola. Por línea de comandos, lo mismo que veías en la guía de Ubuntu: `/var/run/reboot-required`.

## 5. El informe para la reunión de parcheo

:::ui Landscape · Reports
> Reports › USG & Security › Security upgrades report › Tag: prod
= Equipos: 23 · Totalmente parcheados: 19 · Con parches de seguridad pendientes: 4 · Con reinicio pendiente: 5
= CVE abiertos (prod): 7 · Críticos: 1 (CVE-2026-xxxxx · openssl · 2 equipos)
= Equipos sin contacto > 7 días: 1 (srv-legacy-03)
[Download CSV] [Schedule report]
:::

:::term bash · máquina de control (API de Landscape)
$ landscape-api --json get-computers --query "tag:prod AND alert:security-upgrades" | jq -r '.[] | "\\(.hostname)\\t\\(.last_ping_time)"'
srv-app-01	2026-10-22T08:14:02Z
srv-legacy-03	2026-10-14T21:02:19Z
:::

Tres números y una lista: **parcheados / pendientes / reinicio**, y el CVE crítico con nombre de paquete y equipos. `Schedule report` lo manda al buzón del equipo el lunes; `landscape-api` (o la API REST) saca lo mismo para el repo de evidencias. `srv-legacy-03` sin contacto desde hace ocho días es el hallazgo real de este informe: o está apagado o el cliente de Landscape no arranca.

## 6. Lo que revisas cada mes

- Equipos **sin contacto** más de 7 días: apagados, migrados o con el cliente roto (`sudo systemctl status landscape-client`).
- Actividades **fallidas** (`Activities → Failed`): normalmente un `apt` bloqueado por un `dpkg` interrumpido; `sudo dpkg --configure -a` lo arregla.
- Equipos en prod con **todas** las actualizaciones pendientes desde hace un mes: la ventana mensual no se está ejecutando.
- Versiones de Ubuntu: lo que ya está en **ESM** (`esm-infra`) va a la lista de migraciones; Landscape te lo marca por equipo.

## Siguientes pasos

- **Perfiles de paquetes** y **de repositorio**: que todos los prod tengan el agente de monitorización y usen el mirror interno; Landscape los instala y avisa de la desviación.
- **Scripts remotos** (`Scripts → Run`): el mismo check de la guía de Bash lanzado a los 23 de prod con la salida en la consola.
- Si la flota incluye Windows y RHEL, Landscape solo cubre Ubuntu: el inventario único lo hace Ansible, y Landscape queda como la consola de parches y CVE de la parte Ubuntu.
""",
  en="""
## What you'll get

See the Ubuntu servers (and desktops) in one console: which version they run, which patches they are missing, which ones need a reboot, and have security updates apply on their own by group, in each group's window, with a report for the monthly ticket. It is what Ansible does from the command line (Ansible guide), with the fleet view the business wants to see.

## Before you start

- **Ubuntu Pro** enabled on the machines (`pro status`); Landscape SaaS is included, and the self-hosted version also requires Pro on the clients.
- Access to `landscape.canonical.com` (SaaS) or your own Landscape server with an administrator account.
- Decide the **groups**: by environment (prod, test) and by patch window (Tuesday 22:00, Thursday 22:00). Two or three groups are enough at first.
- HTTPS egress from the clients to Landscape.

## 1. Register a client

:::term bash · srv-web-02 (Ubuntu 24.04)
$ sudo pro status | grep -E 'landscape|esm-infra'
esm-infra        yes       enabled   Expanded Security Maintenance for Infrastructure
landscape        yes       disabled  Management and administration tool for Ubuntu
$ sudo apt-get install -y landscape-client
$ sudo landscape-config --computer-title "srv-web-02" --account-name contoso-it --registration-key "$(sudo cat /root/.landscape-key)" --tags prod,web,window-tue --access-group prod --silent
Please wait...
System successfully registered.
$ sudo landscape-config --is-registered && echo REGISTERED
REGISTERED
:::

:::ui Landscape · Computers
> Computers › Pending computers
= srv-web-02 · Ubuntu 24.04.1 LTS · Tags: prod, web, window-tue · Access group: prod
[Accept] [Reject]
:::

Three things at registration: the **title** equal to the hostname, the **tags** (environment, role and window) and the **access group**, which decides who can administer the machine in Landscape. The registration key lives in a file with 600 permissions, not in the Bash history; with Ansible, this step is one task with the key in `ansible-vault`. In **Pending computers** you accept (or automate acceptance by key).

## 2. Access groups and tags

:::ui Landscape · Access groups
> Account › Access groups
= global · (everything)
= prod · Parent: global · Administrators: IT Ops · Computers: 23
= test · Parent: global · Administrators: IT Ops, Development · Computers: 11
> Computers › Search
= tag:prod AND tag:window-tue
= Results: 12 computers
[Save search as: prod-tuesday]
:::

**Access groups** control permissions (Development can reboot test machines, not prod); **tags** control which profile applies to whom. A saved search (`prod-tuesday`) is what you later reference in profiles and reports. If a machine changes window, you change the tag and nothing else.

## 3. The upgrade profile

:::ui Landscape · Upgrade profiles
> Profiles › Upgrade profiles › Add upgrade profile
= Name: prod-security-tuesday
= Upgrade type: [x] Security upgrades only
= Schedule: Weekly · Tuesday · 22:00 · Deliver within: 2 hours
= Autoremove: [x]
= Access group: prod
= Tags: prod, window-tue
[Save]
> Profiles › Upgrade profiles › Add upgrade profile
= Name: test-all-wednesday
= Upgrade type: [x] All upgrades
= Schedule: Weekly · Wednesday · 20:00 · Deliver within: 2 hours
= Tags: test
[Save]
:::

**Test gets everything on Wednesdays; prod gets security only on Tuesdays**, a week after the same thing has gone through test. Non-security updates in prod go in the monthly cycle, as a change window with its ticket. **Deliver within: 2 hours** spreads the start so twelve servers don't download at once.

## 4. Pending reboots

:::ui Landscape · Computers
> Computers › Search: tag:prod AND alert:computer-reboot
= srv-web-01 · Reboot required · Since: 21/10/2026 22:41 · Kernel 6.8.0-47 → 6.8.0-48
= srv-db-01 · Reboot required · Since: 21/10/2026 22:38
= Results: 5 computers
[Select all] [Reboot] › Deliver after: 22/10/2026 23:00 · Deliver within: 1 hour
= Activity queued: "Reboot 5 computers" · Approval: required (prod)
:::

The security patch applies on its own; the **reboot does not**, and rightly so. The `computer-reboot` alert lists who needs it; the reboot activity is scheduled at the window time and, in prod, requires **approval** from a second administrator (`Account → Alerts → Computer reboot required` and `Activities → Approval required`). That is the four-eyes change ticket without leaving the console. From the command line, the same thing you saw in the Ubuntu guide: `/var/run/reboot-required`.

## 5. The report for the patching meeting

:::ui Landscape · Reports
> Reports › USG & Security › Security upgrades report › Tag: prod
= Computers: 23 · Fully patched: 19 · With pending security upgrades: 4 · With pending reboot: 5
= Open CVEs (prod): 7 · Critical: 1 (CVE-2026-xxxxx · openssl · 2 computers)
= Computers not seen > 7 days: 1 (srv-legacy-03)
[Download CSV] [Schedule report]
:::

:::term bash · control machine (Landscape API)
$ landscape-api --json get-computers --query "tag:prod AND alert:security-upgrades" | jq -r '.[] | "\\(.hostname)\\t\\(.last_ping_time)"'
srv-app-01	2026-10-22T08:14:02Z
srv-legacy-03	2026-10-14T21:02:19Z
:::

Three numbers and a list: **patched / pending / reboot**, and the critical CVE with package name and machines. `Schedule report` sends it to the team mailbox on Monday; `landscape-api` (or the REST API) pulls the same for the evidence repo. `srv-legacy-03` not seen for eight days is the real finding of this report: it is either off or the Landscape client is not starting.

## 6. What you review each month

- Computers **not seen** for more than 7 days: off, migrated or with a broken client (`sudo systemctl status landscape-client`).
- **Failed** activities (`Activities → Failed`): usually `apt` blocked by an interrupted `dpkg`; `sudo dpkg --configure -a` fixes it.
- Prod machines with **all** updates pending for a month: the monthly window is not running.
- Ubuntu versions: whatever is already in **ESM** (`esm-infra`) goes on the migration list; Landscape flags it per machine.

## Next steps

- **Package profiles** and **repository profiles**: every prod machine has the monitoring agent and uses the internal mirror; Landscape installs them and flags drift.
- **Remote scripts** (`Scripts → Run`): the same check from the Bash guide launched on the 23 prod machines with the output in the console.
- If the fleet includes Windows and RHEL, Landscape only covers Ubuntu: the single inventory is Ansible's job, and Landscape remains the patch and CVE console for the Ubuntu part.
""")

# ---------------------------------------------------------------- L3 · vSphere
g(slug="vsphere-vcenter-crear-vm-snapshots-con-caducidad-y-host-en-mantenimiento", topic="vsphere", date="2026-10-22",
  title_es="VMware vSphere y vCenter: crear una VM, snapshots con caducidad y un host en mantenimiento sin cortar nada",
  title_en="VMware vSphere and vCenter: creating a VM, snapshots with an expiry and a host in maintenance without cutting anything",
  dek_es="La VM desde plantilla con PowerCLI, la regla de los snapshots (cortos, con nombre y fecha), vMotion y el modo de mantenimiento para parchear un host con las VMs en marcha, y lo que miras cuando un datastore se queda sin espacio.",
  dek_en="The VM from a template with PowerCLI, the snapshot rule (short, named and dated), vMotion and maintenance mode to patch a host with the VMs running, and what you look at when a datastore runs out of space.",
  es="""
## Qué vas a conseguir

Operar un clúster de vSphere en el día a día sin pasar por el asistente cada vez: una VM nueva desde plantilla en dos minutos, snapshots que no se olvidan, y la rutina para sacar un host del clúster, parchearlo y devolverlo con las máquinas moviéndose solas. Y los tres sitios donde mirar cuando "todo va lento".

## Antes de empezar

- Acceso a vCenter con un rol que pueda crear VMs, snapshots y poner hosts en mantenimiento (no `Administrator@vsphere.local` para el día a día: un rol propio con lo justo, asignado a tu grupo de AD).
- **PowerCLI** instalado en tu equipo: `Install-Module VMware.PowerCLI -Scope CurrentUser`.
- Una **plantilla** de Windows Server y otra de Linux ya preparadas, con una **especificación de personalización** (nombre, red, unión al dominio).
- Un clúster con **DRS** y **HA** activados y al menos dos hosts con almacenamiento compartido; sin eso, vMotion no tiene adónde ir.

## 1. Conectar con PowerCLI y mirar el clúster

:::term pwsh
$ Connect-VIServer -Server vcenter.contoso.local
Name                           Port  User
----                           ----  ----
vcenter.contoso.local          443   CONTOSO\\laura.prado
$ Get-Cluster | Select-Object Name, HAEnabled, DrsEnabled, DrsAutomationLevel
Name     HAEnabled DrsEnabled DrsAutomationLevel
----     --------- ---------- ------------------
CL-PROD  True      True       FullyAutomated
$ Get-VMHost | Select-Object Name, ConnectionState, @{n="CPU%";e={[int]($_.CpuUsageMhz/$_.CpuTotalMhz*100)}}, @{n="Mem%";e={[int]($_.MemoryUsageGB/$_.MemoryTotalGB*100)}}, Version, Build
Name                      ConnectionState CPU% Mem% Version Build
----                      --------------- ---- ---- ------- -----
esx01.contoso.local       Connected         41   68 8.0.3   24022510
esx02.contoso.local       Connected         38   71 8.0.3   24022510
esx03.contoso.local       Connected         44   66 8.0.3   24022510
$ Get-Datastore | Select-Object Name, @{n="FreeGB";e={[int]$_.FreeSpaceGB}}, @{n="Free%";e={[int]($_.FreeSpaceGB/$_.CapacityGB*100)}}
Name          FreeGB Free%
----          ------ -----
DS-SAN-01       1840    31
DS-SAN-02        212     4
:::

Tres comandos y ya sabes si hay sitio para una VM más (memoria al 70 % con tres hosts significa que si uno cae, los otros dos van al 100 %) y que `DS-SAN-02` está a punto de dar problemas. Esa lectura es la que se hace antes de aceptar cualquier petición de "una VM pequeña".

## 2. Crear la VM desde plantilla

:::term pwsh
$ New-VM -Name "srv-app-02" -Template (Get-Template "tpl-ws2025-core") -OSCustomizationSpec "spec-windows-domain" -ResourcePool (Get-Cluster CL-PROD) -Datastore DS-SAN-01 -Location (Get-Folder "Aplicaciones") | Out-Null
$ Set-VM -VM srv-app-02 -NumCpu 4 -MemoryGB 8 -Notes "Ticket CHG-20471 · Owner: IT Ops · App: Intranet" -Confirm:$false | Out-Null
$ Get-NetworkAdapter -VM srv-app-02 | Set-NetworkAdapter -NetworkName "VLAN20-Servers" -Type Vmxnet3 -Confirm:$false | Out-Null
$ New-TagAssignment -Entity (Get-VM srv-app-02) -Tag (Get-Tag -Category Backup -Name "Daily-30d") | Out-Null
$ Start-VM -VM srv-app-02 | Out-Null; Get-VM srv-app-02 | Select-Object Name, PowerState, NumCpu, MemoryGB, @{n="Host";e={$_.VMHost.Name}}, @{n="IP";e={$_.Guest.IPAddress[0]}}
Name       PowerState NumCpu MemoryGB Host                 IP
----       ---------- ------ -------- ----                 --
srv-app-02 PoweredOn       4        8 esx02.contoso.local  10.20.20.47
:::

Dos cosas que no son opcionales en una VM de producción: las **notas** con el ticket y el propietario (dentro de un año nadie recordará para qué era) y la **etiqueta de backup**, que es lo que Veeam (Nivel 2) usa para incluirla en el job sin que nadie la añada a mano. La especificación de personalización se encarga del nombre, la IP y la unión al dominio; a los cinco minutos la VM aparece en Active Directory.

## 3. Snapshots: cortos, con nombre y con fecha

:::term pwsh
$ New-Snapshot -VM srv-app-02 -Name "CHG-20471 antes de parche · borrar 2026-10-25" -Description "laura.prado · parche de la aplicación" -Memory:$false -Quiesce:$true | Out-Null
$ Get-VM | Get-Snapshot | Where-Object Created -lt (Get-Date).AddDays(-3) | Select-Object VM, Name, Created, @{n="SizeGB";e={[math]::Round($_.SizeGB,1)}}
VM          Name                                   Created             SizeGB
--          ----                                   -------             ------
srv-erp-01  antes de actualizar                    2026-09-02 21:14      184,3
srv-file-02 prueba                                 2026-08-19 10:02       61,0
# cuando el cambio esté validado:
$ Get-Snapshot -VM srv-app-02 | Remove-Snapshot -Confirm:$false
:::

Un snapshot de 184 GB de hace siete semanas en el servidor del ERP es la causa número uno de "el ERP va lento" y de datastores llenos. La regla: **nombre con el ticket y la fecha de borrado**, nunca más de 72 horas, `-Quiesce` para que sea consistente con la aplicación, sin memoria salvo que necesites volver al estado exacto de ejecución. El comando de la segunda línea, en una tarea semanal que mande el resultado al canal del equipo, es la política de snapshots. Un snapshot no es una copia de seguridad: si el datastore se pierde, se pierde con él.

## 4. Un host en mantenimiento sin cortar nada

:::term pwsh
$ Get-VMHost esx03.contoso.local | Get-VM | Select-Object Name, PowerState | Measure-Object | Select-Object Count
Count
-----
   14
$ Set-VMHost -VMHost esx03.contoso.local -State Maintenance -Evacuate -Confirm:$false
# DRS mueve las 14 VMs con vMotion a esx01 y esx02; tarda unos minutos
$ Get-VMHost esx03.contoso.local | Select-Object Name, ConnectionState, @{n="VMs";e={($_ | Get-VM).Count}}
Name                 ConnectionState VMs
----                 --------------- ---
esx03.contoso.local  Maintenance       0
# parchear con Lifecycle Manager (o desde la consola: Updates › Remediate) y reiniciar
$ Restart-VMHost -VMHost esx03.contoso.local -Confirm:$false | Out-Null
$ Set-VMHost -VMHost esx03.contoso.local -State Connected | Out-Null
$ Get-VMHost | Select-Object Name, ConnectionState, Version, Build
:::

Esto es lo que hace que parchear un hipervisor no sea un cambio con corte: **modo de mantenimiento con evacuación**, DRS reparte las VMs, se parchea, se reinicia, se devuelve, y DRS vuelve a equilibrar. Compruébalo antes con la pregunta del paso 1: si los otros dos hosts no tienen memoria para absorber las 14 VMs, el `Set-VMHost` se queda esperando. En vCenter, **Lifecycle Manager** con una imagen por clúster hace la parte del parche y deja el informe de cumplimiento.

> Consejo: haz esto en un host de test o con una VM de pruebas la primera vez, y mira en `Monitor → Tasks and Events` cómo se mueve cada VM. Lo que ves ahí es lo que explicas en el ticket de cambio.

## 5. Datastore lleno y "todo va lento"

:::term pwsh
$ Get-Datastore DS-SAN-02 | Get-VM | Get-Snapshot | Measure-Object SizeGB -Sum | Select-Object @{n="SnapshotGB";e={[int]$_.Sum}}
SnapshotGB
----------
       412
$ Get-Datastore DS-SAN-02 | Get-VM | Where-Object {$_.PowerState -eq "PoweredOff"} | Select-Object Name, @{n="ProvisionedGB";e={[int]$_.ProvisionedSpaceGB}}
Name          ProvisionedGB
----          -------------
srv-old-crm          520
$ Get-VM srv-erp-01 | Get-Stat -Stat disk.maxTotalLatency.latest -Realtime -MaxSamples 10 | Select-Object Timestamp, Value
Timestamp           Value
---------           -----
22/10/2026 10:12:00    48
22/10/2026 10:11:40    61
:::

Los tres sitios donde mirar: **snapshots** en el datastore (412 GB aquí, el 90 % del problema), **VMs apagadas** que nadie borró (520 GB provisionados) y la **latencia de disco** de la VM que se queja (`disk.maxTotalLatency` por encima de 20-30 ms sostenidos es almacenamiento, no la VM). En la consola, `Monitor → Performance → Advanced` muestra lo mismo con gráfico; `esxtop` en el host, con `d` y `u`, es la vista fina. Con Grafana (guía anterior), **vmware_exporter** o el plugin de vCenter dan estas métricas en el panel del equipo.

## 6. Lo que revisas cada mes

- Snapshots con más de 3 días y VMs apagadas con más de 30 (`Get-VM | Where PowerState -eq PoweredOff | Select Name, @{n="Days";e={((Get-Date)-($_ | Get-VIEvent -MaxSamples 1).CreatedTime).Days}}`).
- Datastores por debajo del 15 % libre y el crecimiento mensual.
- Hosts con builds distintos en el mismo clúster (`Get-VMHost | Group-Object Build`): el que no se parcheó.
- **Skyline Health** / `Monitor → Health` del clúster y las alarmas de vCenter no reconocidas.
- Que vCenter tiene su propia copia (`File-Based Backup` en la VAMI, puerto 5480) y que se probó una restauración este trimestre.

## Siguientes pasos

- **VCF / NSX** cuando el clúster crezca a varios y la red pase a definirse por software; la operación diaria es la misma, con más capas.
- **vSphere Replication** o **SRM** para el DR del Nivel 4: la VM replicada en el otro CPD y el plan de recuperación probado dos veces al año.
- Para quien venga de Hyper-V (guía anterior) o vaya a **Nutanix** (Nivel 4): snapshots cortos, host en mantenimiento, datastore con margen y notas en la VM son las mismas reglas con otros nombres.
""",
  en="""
## What you'll get

Operate a vSphere cluster day to day without the wizard every time: a new VM from a template in two minutes, snapshots that don't get forgotten, and the routine to take a host out of the cluster, patch it and bring it back with the machines moving by themselves. Plus the three places to look when "everything is slow".

## Before you start

- Access to vCenter with a role that can create VMs, snapshots and put hosts in maintenance (not `Administrator@vsphere.local` for daily work: a custom role with just enough, assigned to your AD group).
- **PowerCLI** installed on your machine: `Install-Module VMware.PowerCLI -Scope CurrentUser`.
- A Windows Server **template** and a Linux one already prepared, with a **customization specification** (name, network, domain join).
- A cluster with **DRS** and **HA** enabled and at least two hosts on shared storage; without that, vMotion has nowhere to go.

## 1. Connect with PowerCLI and look at the cluster

:::term pwsh
$ Connect-VIServer -Server vcenter.contoso.local
Name                           Port  User
----                           ----  ----
vcenter.contoso.local          443   CONTOSO\\laura.prado
$ Get-Cluster | Select-Object Name, HAEnabled, DrsEnabled, DrsAutomationLevel
Name     HAEnabled DrsEnabled DrsAutomationLevel
----     --------- ---------- ------------------
CL-PROD  True      True       FullyAutomated
$ Get-VMHost | Select-Object Name, ConnectionState, @{n="CPU%";e={[int]($_.CpuUsageMhz/$_.CpuTotalMhz*100)}}, @{n="Mem%";e={[int]($_.MemoryUsageGB/$_.MemoryTotalGB*100)}}, Version, Build
Name                      ConnectionState CPU% Mem% Version Build
----                      --------------- ---- ---- ------- -----
esx01.contoso.local       Connected         41   68 8.0.3   24022510
esx02.contoso.local       Connected         38   71 8.0.3   24022510
esx03.contoso.local       Connected         44   66 8.0.3   24022510
$ Get-Datastore | Select-Object Name, @{n="FreeGB";e={[int]$_.FreeSpaceGB}}, @{n="Free%";e={[int]($_.FreeSpaceGB/$_.CapacityGB*100)}}
Name          FreeGB Free%
----          ------ -----
DS-SAN-01       1840    31
DS-SAN-02        212     4
:::

Three commands and you already know whether there is room for one more VM (memory at 70% with three hosts means that if one fails, the other two go to 100%) and that `DS-SAN-02` is about to cause trouble. That reading is what you do before accepting any request for "a small VM".

## 2. Create the VM from a template

:::term pwsh
$ New-VM -Name "srv-app-02" -Template (Get-Template "tpl-ws2025-core") -OSCustomizationSpec "spec-windows-domain" -ResourcePool (Get-Cluster CL-PROD) -Datastore DS-SAN-01 -Location (Get-Folder "Applications") | Out-Null
$ Set-VM -VM srv-app-02 -NumCpu 4 -MemoryGB 8 -Notes "Ticket CHG-20471 · Owner: IT Ops · App: Intranet" -Confirm:$false | Out-Null
$ Get-NetworkAdapter -VM srv-app-02 | Set-NetworkAdapter -NetworkName "VLAN20-Servers" -Type Vmxnet3 -Confirm:$false | Out-Null
$ New-TagAssignment -Entity (Get-VM srv-app-02) -Tag (Get-Tag -Category Backup -Name "Daily-30d") | Out-Null
$ Start-VM -VM srv-app-02 | Out-Null; Get-VM srv-app-02 | Select-Object Name, PowerState, NumCpu, MemoryGB, @{n="Host";e={$_.VMHost.Name}}, @{n="IP";e={$_.Guest.IPAddress[0]}}
Name       PowerState NumCpu MemoryGB Host                 IP
----       ---------- ------ -------- ----                 --
srv-app-02 PoweredOn       4        8 esx02.contoso.local  10.20.20.47
:::

Two things that are not optional on a production VM: the **notes** with the ticket and the owner (in a year nobody will remember what it was for) and the **backup tag**, which is what Veeam (Level 2) uses to include it in the job without anyone adding it by hand. The customization specification takes care of the name, the IP and the domain join; five minutes later the VM appears in Active Directory.

## 3. Snapshots: short, named and dated

:::term pwsh
$ New-Snapshot -VM srv-app-02 -Name "CHG-20471 before patch · delete 2026-10-25" -Description "laura.prado · application patch" -Memory:$false -Quiesce:$true | Out-Null
$ Get-VM | Get-Snapshot | Where-Object Created -lt (Get-Date).AddDays(-3) | Select-Object VM, Name, Created, @{n="SizeGB";e={[math]::Round($_.SizeGB,1)}}
VM          Name                                   Created             SizeGB
--          ----                                   -------             ------
srv-erp-01  before upgrade                         2026-09-02 21:14      184.3
srv-file-02 test                                   2026-08-19 10:02       61.0
# once the change is validated:
$ Get-Snapshot -VM srv-app-02 | Remove-Snapshot -Confirm:$false
:::

A 184 GB snapshot from seven weeks ago on the ERP server is the number one cause of "the ERP is slow" and of full datastores. The rule: **name with the ticket and the deletion date**, never more than 72 hours, `-Quiesce` so it is application-consistent, no memory unless you need to return to the exact running state. The second command, in a weekly task that posts the result to the team channel, is the snapshot policy. A snapshot is not a backup: if the datastore is lost, it goes with it.

## 4. A host in maintenance without cutting anything

:::term pwsh
$ Get-VMHost esx03.contoso.local | Get-VM | Select-Object Name, PowerState | Measure-Object | Select-Object Count
Count
-----
   14
$ Set-VMHost -VMHost esx03.contoso.local -State Maintenance -Evacuate -Confirm:$false
# DRS moves the 14 VMs with vMotion to esx01 and esx02; takes a few minutes
$ Get-VMHost esx03.contoso.local | Select-Object Name, ConnectionState, @{n="VMs";e={($_ | Get-VM).Count}}
Name                 ConnectionState VMs
----                 --------------- ---
esx03.contoso.local  Maintenance       0
# patch with Lifecycle Manager (or from the console: Updates › Remediate) and reboot
$ Restart-VMHost -VMHost esx03.contoso.local -Confirm:$false | Out-Null
$ Set-VMHost -VMHost esx03.contoso.local -State Connected | Out-Null
$ Get-VMHost | Select-Object Name, ConnectionState, Version, Build
:::

This is what makes patching a hypervisor a change without an outage: **maintenance mode with evacuation**, DRS spreads the VMs, patch, reboot, bring it back, and DRS rebalances. Check beforehand with the question from step 1: if the other two hosts lack the memory to absorb the 14 VMs, the `Set-VMHost` just waits. In vCenter, **Lifecycle Manager** with one image per cluster does the patching part and leaves the compliance report.

> Tip: do this on a test host or with a test VM the first time, and watch in `Monitor → Tasks and Events` how each VM moves. What you see there is what you explain in the change ticket.

## 5. Full datastore and "everything is slow"

:::term pwsh
$ Get-Datastore DS-SAN-02 | Get-VM | Get-Snapshot | Measure-Object SizeGB -Sum | Select-Object @{n="SnapshotGB";e={[int]$_.Sum}}
SnapshotGB
----------
       412
$ Get-Datastore DS-SAN-02 | Get-VM | Where-Object {$_.PowerState -eq "PoweredOff"} | Select-Object Name, @{n="ProvisionedGB";e={[int]$_.ProvisionedSpaceGB}}
Name          ProvisionedGB
----          -------------
srv-old-crm          520
$ Get-VM srv-erp-01 | Get-Stat -Stat disk.maxTotalLatency.latest -Realtime -MaxSamples 10 | Select-Object Timestamp, Value
Timestamp           Value
---------           -----
22/10/2026 10:12:00    48
22/10/2026 10:11:40    61
:::

The three places to look: **snapshots** on the datastore (412 GB here, 90% of the problem), **powered-off VMs** nobody deleted (520 GB provisioned) and the **disk latency** of the VM that complains (`disk.maxTotalLatency` sustained above 20-30 ms is storage, not the VM). In the console, `Monitor → Performance → Advanced` shows the same with a chart; `esxtop` on the host, with `d` and `u`, is the fine-grained view. With Grafana (previous guide), **vmware_exporter** or the vCenter plugin put these metrics on the team board.

## 6. What you review each month

- Snapshots older than 3 days and VMs powered off for more than 30 (`Get-VM | Where PowerState -eq PoweredOff | Select Name, @{n="Days";e={((Get-Date)-($_ | Get-VIEvent -MaxSamples 1).CreatedTime).Days}}`).
- Datastores below 15% free and the monthly growth.
- Hosts with different builds in the same cluster (`Get-VMHost | Group-Object Build`): the one that didn't get patched.
- **Skyline Health** / the cluster's `Monitor → Health` and unacknowledged vCenter alarms.
- That vCenter has its own backup (`File-Based Backup` in the VAMI, port 5480) and that a restore was tested this quarter.

## Next steps

- **VCF / NSX** when the cluster grows into several and the network becomes software-defined; the daily operation is the same, with more layers.
- **vSphere Replication** or **SRM** for Level 4 DR: the VM replicated in the other data centre and the recovery plan tested twice a year.
- For those coming from Hyper-V (previous guide) or going to **Nutanix** (Level 4): short snapshots, host in maintenance, datastore headroom and notes on the VM are the same rules with other names.
""")

# ---------------------------------------------------------------- L4 · Azure Virtual Desktop and Windows 365
g(slug="azure-virtual-desktop-y-windows-365-host-pool-cloud-pc-y-conexion-que-falla", topic="avd-w365", date="2026-10-27",
  title_es="Azure Virtual Desktop y Windows 365: cuál elegir, un host pool con FSLogix y una conexión que falla",
  title_en="Azure Virtual Desktop and Windows 365: which one to choose, a host pool with FSLogix and a connection that fails",
  dek_es="Cuándo encaja cada uno, un host pool multisesión unido a Entra ID con perfiles en FSLogix y escalado automático, un Cloud PC de Windows 365 en tres pasos, y cómo leer por qué un usuario no llega a su escritorio.",
  dek_en="When each one fits, a multi-session host pool joined to Entra ID with FSLogix profiles and autoscaling, a Windows 365 Cloud PC in three steps, and how to read why a user can't reach their desktop.",
  es="""
## Qué vas a conseguir

Saber cuándo proponer Azure Virtual Desktop (AVD) y cuándo Windows 365, montar un host pool multisesión que arranca y apaga máquinas solo, con perfiles que siguen al usuario, y la rutina para el ticket de "no me conecta al escritorio", que en estos entornos casi nunca es la red del usuario.

## Antes de empezar

- Una suscripción de Azure con los roles **Desktop Virtualization Contributor** y **Virtual Machine Contributor** en el grupo de recursos (activados por PIM).
- Licencias que dan derecho a usar AVD con Windows cliente: Microsoft 365 E3/E5, Business Premium o Windows Enterprise E3/E5 por usuario. El coste aparte es el de las máquinas, el disco y el almacenamiento de Azure.
- Una red virtual con salida a internet y, si los hosts se unen a Active Directory, DNS que resuelva el dominio.
- Una cuenta de almacenamiento **Azure Files Premium** para los perfiles de FSLogix.

## 1. AVD o Windows 365

| | Azure Virtual Desktop | Windows 365 |
|---|---|---|
| Pago | Por uso: máquinas, discos y almacenamiento de Azure | Licencia fija al mes por usuario y tamaño de Cloud PC |
| Sesiones | Multisesión (varios usuarios por máquina) o personal | Un Cloud PC por usuario |
| Quién gestiona qué | Tú: host pools, imágenes, escalado, red | Microsoft la infraestructura; tú el Cloud PC con Intune |
| Encaja con | Turnos, muchos usuarios ligeros, aplicaciones publicadas (RemoteApp) | Contratistas, puesto persistente, coste previsible, equipos pequeños de IT |

La pregunta que decide casi siempre es quién va a mantener las imágenes y el escalado. Si no hay nadie con tiempo para eso, Windows 365.

## 2. El host pool

:::ui Azure portal · Azure Virtual Desktop
> Azure Virtual Desktop › Grupos de hosts › Crear
= Nombre: hp-oficina-01
= Tipo de grupo de hosts: Agrupado
= Algoritmo de equilibrio de carga: En amplitud (breadth-first)
= Límite máximo de sesiones: 8
= Imagen: Windows 11 Enterprise multisesión + aplicaciones de Microsoft 365
= Tamaño de máquina virtual: Standard D4s v5 (4 vCPU, 16 GiB)
= Número de máquinas virtuales: 3
= Red virtual: vnet-avd / snet-hosts
= Dominio al que unirse: Microsoft Entra ID · [x] Inscribir la máquina virtual en Intune
= Registrar el grupo de aplicaciones de escritorio: Sí · Área de trabajo: ws-oficina
[Revisar y crear]
:::

Con hosts unidos a Entra ID hacen falta dos asignaciones al mismo grupo de usuarios (`sg-avd-oficina`):

- En el **grupo de aplicaciones de escritorio**: la asignación de usuarios, para que vean el escritorio.
- En el **grupo de recursos** de las máquinas: el rol **Virtual Machine User Login** (o *Administrator Login* para IT). Sin él, el usuario ve el escritorio en la lista pero el inicio de sesión en el host falla.

En las propiedades RDP del host pool, `enablerdsaadauth:i:1` activa el inicio de sesión único con Entra ID: el usuario no vuelve a escribir la contraseña al entrar en la sesión.

## 3. Perfiles con FSLogix

En multisesión el usuario no cae siempre en la misma máquina: su perfil tiene que viajar con él. FSLogix lo guarda en un disco VHDX en Azure Files y lo monta al iniciar sesión.

:::term PowerShell · en la imagen o por Intune (catálogo de configuración, FSLogix)
$ New-Item -Path "HKLM:\\SOFTWARE\\FSLogix\\Profiles" -Force | Out-Null
$ Set-ItemProperty "HKLM:\\SOFTWARE\\FSLogix\\Profiles" -Name Enabled -Value 1 -Type DWord
$ Set-ItemProperty "HKLM:\\SOFTWARE\\FSLogix\\Profiles" -Name VHDLocations -Value "\\\\stavdperfiles.file.core.windows.net\\perfiles" -Type String
$ Set-ItemProperty "HKLM:\\SOFTWARE\\FSLogix\\Profiles" -Name DeleteLocalProfileWhenVHDShouldApply -Value 1 -Type DWord
$ Set-ItemProperty "HKLM:\\SOFTWARE\\FSLogix\\Profiles" -Name FlipFlopProfileDirectoryName -Value 1 -Type DWord
:::

- `FlipFlopProfileDirectoryName` nombra la carpeta de cada perfil como `usuario_SID`: se encuentra a simple vista cuando hay que soltar o borrar uno.
- Para que los hosts unidos a Entra ID monten el recurso con la identidad del usuario, la cuenta de almacenamiento usa **Microsoft Entra Kerberos** (identidades híbridas) y los permisos de recurso compartido se dan al mismo grupo `sg-avd-oficina`.

## 4. Escalado automático

Tres máquinas encendidas de noche son dinero tirado. Un **plan de escalado** las enciende y apaga según la hora y la carga.

:::ui Azure portal · Plan de escalado
> Azure Virtual Desktop › Planes de escalado › sp-oficina › Programaciones › Laborables
= Inicio de aumento: 07:30 · Hosts mínimos: 20 % · Umbral de capacidad: 60 %
= Horas punta: 08:30 · Equilibrio de carga: En amplitud
= Inicio de reducción: 18:00 · Hosts mínimos: 10 % · Forzar cierre de sesión: Sí, tras 30 min con aviso
= Horas valle: 20:00 · Equilibrio de carga: En profundidad
= Grupo de hosts asignado: hp-oficina-01
[Guardar]
:::

Para que el plan pueda encender y apagar máquinas, la entidad de servicio de **Azure Virtual Desktop** necesita el rol **Desktop Virtualization Power On Off Contributor** en la suscripción o el grupo de recursos. Es el olvido más habitual: el plan existe, pero nunca hace nada.

## 5. Windows 365 en tres pasos

:::ui Intune admin center · Windows 365
> Dispositivos › Windows 365 › Directivas de aprovisionamiento › Crear directiva
= Nombre: w365-contratistas
= Tipo de unión: Microsoft Entra Join
= Red: Red hospedada por Microsoft · Región: Europa (Oeste)
= Imagen: Galería · Windows 11 Enterprise + aplicaciones de Microsoft 365
= Asignaciones: sg-w365-contratistas
[Crear]
:::

1. La directiva de aprovisionamiento (arriba).
2. Una licencia de **Windows 365 Enterprise** del tamaño adecuado (por ejemplo 2 vCPU, 8 GB, 128 GB) a cada usuario del grupo.
3. Esperar el estado **Aprovisionado** en *Todos los PC en la nube* y mandar al usuario a `windows365.microsoft.com` o a la aplicación Windows.

El Cloud PC se gestiona después como cualquier equipo de Intune: perfiles, cumplimiento, aplicaciones (guía de Intune del Nivel 3).

## 6. El ticket: "no me conecta al escritorio"

Primero, el estado de los hosts:

:::ui Azure portal · Hosts de sesión
> Azure Virtual Desktop › Grupos de hosts › hp-oficina-01 › Hosts de sesión
avd-ofi-0   Disponible        Sesiones: 8/8   Modo de purga: No
avd-ofi-1   No disponible     Sesiones: 0/8   Modo de purga: No   Comprobación: FSLogix · Error
avd-ofi-2   Apagado           Sesiones: 0/8   Modo de purga: No
:::

Con una máquina llena, otra con FSLogix roto y la tercera apagada por el plan de escalado, ningún usuario nuevo entra. Las **comprobaciones de estado** de cada host (unión al dominio, FSLogix, pila de AVD, agente) dicen cuál falla sin entrar en la máquina.

Después, los errores de conexión. Con el diagnóstico del host pool enviado a Log Analytics (o la página **Insights**):

:::term Log Analytics · KQL
$ WVDErrors
$ | where TimeGenerated > ago(4h) and UserName == "laura.prado@contoso.com"
$ | project TimeGenerated, CodeSymbolic, Source, Message
TimeGenerated         CodeSymbolic                              Source        Message
27/10/2026 08:41:12   ConnectionFailedNoHealthyRdshAvailable    RDBroker      No healthy session host is available
:::

- `ConnectionFailedNoHealthyRdshAvailable`: no hay hosts sanos con hueco. Mira las comprobaciones de estado y el plan de escalado (umbral de capacidad demasiado alto, hosts mínimos demasiado bajos).
- En el host, `C:\\ProgramData\\FSLogix\\Logs\\Profile` explica los perfiles que no se montan. El clásico: **0x00000020** (el disco del perfil está en uso), una sesión anterior que se quedó colgada en otro host. Se cierra esa sesión y el usuario vuelve a entrar.
- En Windows 365, *Todos los PC en la nube* tiene **Solucionar problemas** (prueba de conectividad), **Reiniciar** y **Restaurar** a un punto anterior.

## 7. Lo que revisas cada mes

- **Coste** por grupo de recursos en Cost Management: si sube sin más usuarios, el escalado no está apagando.
- Hosts con una imagen de hace más de un mes: se sustituyen por hosts nuevos con la imagen actual, no se parchean a mano uno a uno.
- En Windows 365, el informe de **utilización de PC en la nube**: los que nadie usa se reasignan o se retira la licencia.
- Tamaño de los perfiles en Azure Files: un perfil que crece sin parar suele ser la caché de Teams u OneDrive sin excluir.

## Siguientes pasos

- **Azure Compute Gallery** con Azure Image Builder para que la imagen mensual se construya sola.
- Grupos de aplicaciones **RemoteApp**: publicar solo el ERP en lugar de todo el escritorio.
- **Windows 365 Frontline** para puestos compartidos por turnos.
- La guía de VMware Horizon del Nivel 2 tiene la versión local de todo esto: comparar las dos ayuda a defender la propuesta.
""",
  en="""
## What you'll get

Knowing when to propose Azure Virtual Desktop (AVD) and when Windows 365, building a multi-session host pool that powers machines on and off by itself, with profiles that follow the user, and the routine for the "I can't connect to my desktop" ticket, which in these environments is almost never the user's network.

## Before you start

- An Azure subscription with the **Desktop Virtualization Contributor** and **Virtual Machine Contributor** roles on the resource group (activated through PIM).
- Licences that grant the right to use AVD with Windows client: Microsoft 365 E3/E5, Business Premium or Windows Enterprise E3/E5 per user. The separate cost is the Azure machines, disks and storage.
- A virtual network with internet egress and, if the hosts join Active Directory, DNS that resolves the domain.
- An **Azure Files Premium** storage account for the FSLogix profiles.

## 1. AVD or Windows 365

| | Azure Virtual Desktop | Windows 365 |
|---|---|---|
| Billing | Pay as you go: Azure machines, disks and storage | Fixed monthly licence per user and Cloud PC size |
| Sessions | Multi-session (several users per machine) or personal | One Cloud PC per user |
| Who manages what | You: host pools, images, scaling, network | Microsoft the infrastructure; you the Cloud PC with Intune |
| Fits | Shifts, many light users, published apps (RemoteApp) | Contractors, persistent desktop, predictable cost, small IT teams |

The question that usually decides is who will maintain the images and the scaling. If nobody has time for that, Windows 365.

## 2. The host pool

:::ui Azure portal · Azure Virtual Desktop
> Azure Virtual Desktop › Host pools › Create
= Name: hp-office-01
= Host pool type: Pooled
= Load balancing algorithm: Breadth-first
= Max session limit: 8
= Image: Windows 11 Enterprise multi-session + Microsoft 365 apps
= Virtual machine size: Standard D4s v5 (4 vCPU, 16 GiB)
= Number of VMs: 3
= Virtual network: vnet-avd / snet-hosts
= Domain to join: Microsoft Entra ID · [x] Enroll VM with Intune
= Register desktop app group: Yes · Workspace: ws-office
[Review + create]
:::

With hosts joined to Entra ID you need two assignments to the same user group (`sg-avd-office`):

- On the **desktop application group**: the user assignment, so they see the desktop.
- On the machines' **resource group**: the **Virtual Machine User Login** role (or *Administrator Login* for IT). Without it, users see the desktop in their list but the sign-in to the host fails.

In the host pool's RDP properties, `enablerdsaadauth:i:1` turns on single sign-on with Entra ID: users don't type their password again when the session starts.

## 3. Profiles with FSLogix

In multi-session, users don't always land on the same machine: their profile has to travel with them. FSLogix keeps it in a VHDX disk on Azure Files and mounts it at sign-in.

:::term PowerShell · in the image or through Intune (settings catalog, FSLogix)
$ New-Item -Path "HKLM:\\SOFTWARE\\FSLogix\\Profiles" -Force | Out-Null
$ Set-ItemProperty "HKLM:\\SOFTWARE\\FSLogix\\Profiles" -Name Enabled -Value 1 -Type DWord
$ Set-ItemProperty "HKLM:\\SOFTWARE\\FSLogix\\Profiles" -Name VHDLocations -Value "\\\\stavdprofiles.file.core.windows.net\\profiles" -Type String
$ Set-ItemProperty "HKLM:\\SOFTWARE\\FSLogix\\Profiles" -Name DeleteLocalProfileWhenVHDShouldApply -Value 1 -Type DWord
$ Set-ItemProperty "HKLM:\\SOFTWARE\\FSLogix\\Profiles" -Name FlipFlopProfileDirectoryName -Value 1 -Type DWord
:::

- `FlipFlopProfileDirectoryName` names each profile folder `user_SID`: you find it at a glance when one has to be released or deleted.
- For hosts joined to Entra ID to mount the share with the user's identity, the storage account uses **Microsoft Entra Kerberos** (hybrid identities), and the share permissions go to the same `sg-avd-office` group.

## 4. Autoscaling

Three machines running all night is money thrown away. A **scaling plan** powers them on and off by time and load.

:::ui Azure portal · Scaling plan
> Azure Virtual Desktop › Scaling plans › sp-office › Schedules › Weekdays
= Ramp-up start: 07:30 · Minimum hosts: 20% · Capacity threshold: 60%
= Peak hours: 08:30 · Load balancing: Breadth-first
= Ramp-down start: 18:00 · Minimum hosts: 10% · Force logoff: Yes, after 30 min with a warning
= Off-peak: 20:00 · Load balancing: Depth-first
= Assigned host pool: hp-office-01
[Save]
:::

For the plan to power machines on and off, the **Azure Virtual Desktop** service principal needs the **Desktop Virtualization Power On Off Contributor** role on the subscription or resource group. It is the most common miss: the plan exists, but never does anything.

## 5. Windows 365 in three steps

:::ui Intune admin center · Windows 365
> Devices › Windows 365 › Provisioning policies › Create policy
= Name: w365-contractors
= Join type: Microsoft Entra Join
= Network: Microsoft hosted network · Region: Europe (West)
= Image: Gallery · Windows 11 Enterprise + Microsoft 365 apps
= Assignments: sg-w365-contractors
[Create]
:::

1. The provisioning policy (above).
2. A **Windows 365 Enterprise** licence of the right size (for example 2 vCPU, 8 GB, 128 GB) for each user in the group.
3. Wait for the **Provisioned** status in *All Cloud PCs* and send the user to `windows365.microsoft.com` or the Windows app.

From then on the Cloud PC is managed like any Intune device: profiles, compliance, apps (Level 3 Intune guide).

## 6. The ticket: "I can't connect to my desktop"

First, the state of the hosts:

:::ui Azure portal · Session hosts
> Azure Virtual Desktop › Host pools › hp-office-01 › Session hosts
avd-off-0   Available       Sessions: 8/8   Drain mode: Off
avd-off-1   Unavailable     Sessions: 0/8   Drain mode: Off   Health check: FSLogix · Failed
avd-off-2   Shutdown        Sessions: 0/8   Drain mode: Off
:::

With one machine full, another with FSLogix broken and the third powered off by the scaling plan, no new user gets in. Each host's **health checks** (domain join, FSLogix, AVD stack, agent) tell you which one fails without logging on to the machine.

Then the connection errors. With the host pool diagnostics sent to Log Analytics (or the **Insights** page):

:::term Log Analytics · KQL
$ WVDErrors
$ | where TimeGenerated > ago(4h) and UserName == "laura.prado@contoso.com"
$ | project TimeGenerated, CodeSymbolic, Source, Message
TimeGenerated         CodeSymbolic                              Source        Message
27/10/2026 08:41:12   ConnectionFailedNoHealthyRdshAvailable    RDBroker      No healthy session host is available
:::

- `ConnectionFailedNoHealthyRdshAvailable`: no healthy host with room. Look at the health checks and the scaling plan (capacity threshold too high, minimum hosts too low).
- On the host, `C:\\ProgramData\\FSLogix\\Logs\\Profile` explains profiles that won't mount. The classic: **0x00000020** (the profile disk is in use), an earlier session left hanging on another host. Close that session and the user signs in again.
- In Windows 365, *All Cloud PCs* has **Troubleshoot** (connectivity test), **Restart** and **Restore** to an earlier point.

## 7. What you review each month

- **Cost** per resource group in Cost Management: if it rises without more users, scaling isn't powering off.
- Hosts on an image more than a month old: they are replaced by new hosts on the current image, not patched by hand one by one.
- In Windows 365, the **Cloud PC utilization** report: the ones nobody uses are reassigned or the licence is removed.
- Profile size on Azure Files: a profile that keeps growing is usually an unexcluded Teams or OneDrive cache.

## Next steps

- **Azure Compute Gallery** with Azure Image Builder so the monthly image builds itself.
- **RemoteApp** application groups: publish just the ERP instead of the whole desktop.
- **Windows 365 Frontline** for devices shared across shifts.
- The Level 2 VMware Horizon guide has the on-premises version of all this: comparing the two helps you defend the proposal.
""")

# ---------------------------------------------------------------- L4 · DR/BCP
g(slug="dr-bcp-rpo-y-rto-por-servicio-plan-de-recuperacion-y-prueba-completa", topic="dr-bcp", date="2026-10-27",
  title_es="DR/BCP: RPO y RTO por servicio, el plan de recuperación y una prueba completa",
  title_en="DR/BCP: RPO and RTO per service, the recovery plan and a full test",
  dek_es="El análisis de impacto que fija cuánto dato y cuánto tiempo puede perder cada servicio, la regla 3-2-1-1-0 con una copia inmutable, el runbook con el orden de arranque, y una prueba de recuperación medida con informe y acciones.",
  dek_en="The impact analysis that sets how much data and how much time each service can lose, the 3-2-1-1-0 rule with an immutable copy, the runbook with the start-up order, and a measured recovery test with a report and actions.",
  es="""
## Qué vas a conseguir

Pasar de "tenemos copias" a "sabemos cuánto tardamos en volver y lo hemos medido". Cada servicio con su RPO y RTO acordados con negocio, copias que un ransomware no puede borrar, un plan de recuperación que otra persona puede seguir a las tres de la mañana, y una prueba anual que demuestra que todo eso funciona.

## Antes de empezar

- La lista de servicios y sus dependencias (CMDB, inventario o la hoja que haya). El repo 32 del portfolio, *Backup Restore Test Tracker*, sirve de plantilla para llevar servicios, RPO y pruebas.
- Un responsable de negocio por servicio que pueda decidir cuánto puede estar parado.
- La herramienta de copias con trabajos funcionando (guía de Veeam del Nivel 2) y un segundo emplazamiento o región de nube.
- Dos palabras claras: **RPO** es cuánto dato puedes perder (la antigüedad de la última copia buena) y **RTO** es cuánto puedes tardar en volver a dar servicio.

## 1. El análisis de impacto (BIA) en una tabla

Una reunión por área con una pregunta: "si este servicio cae a las 10:00 de un lunes, ¿a partir de qué hora es un problema serio, y cuánto trabajo perdido aceptas rehacer?". De ahí sale la tabla, no de IT.

| Servicio | Si cae | RPO | RTO | Nivel |
|---|---|---|---|---|
| ERP (pedidos y facturación) | No se factura ni se envía | 15 min | 4 h | 1 |
| Active Directory y DNS | No entra nadie a nada | 1 h | 2 h | 1 |
| Servidor de ficheros (unidad S:) | Se trabaja con copias locales | 24 h | 8 h | 2 |
| Intranet | Molestia, hay alternativas | 24 h | 48 h | 3 |
| Correo (Microsoft 365) | SaaS: depende de Microsoft | 24 h (copia propia) | — | 1 |

- El **nivel** decide el orden de recuperación y el presupuesto: un RPO de 15 minutos exige replicación o logs de base de datos, no una copia nocturna.
- Microsoft 365 no es "sin copia": Microsoft garantiza el servicio, no que recuperes lo que un usuario o un atacante borró hace cuatro meses. Una copia propia (por ejemplo Veeam Backup for Microsoft 365) cubre ese hueco.

## 2. La regla 3-2-1-1-0

- **3** copias de los datos (la producción y dos más).
- **2** soportes distintos (disco y objeto, o disco y cinta).
- **1** fuera del emplazamiento.
- **1** inmutable o desconectada: ni un administrador comprometido puede borrarla antes de que caduque.
- **0** errores en la verificación: una copia que nunca se ha restaurado es una hipótesis.

:::ui Veeam Backup & Replication · Repositorio reforzado
> Infraestructura de copia › Repositorios › Añadir › Directo › Linux reforzado
= Servidor: vbr-hardened-01 (Ubuntu, sin SSH, credenciales de un solo uso)
= Ruta: /mnt/veeam-xfs (XFS con bloques compartidos)
= [x] Hacer inmutables las copias recientes durante: 14 días
= Copia secundaria: Objeto (S3 compatible) con Object Lock · 30 días
[Aplicar]
:::

:::term PowerShell · Veeam (consola de copias)
$ Get-VBRBackupSession | Where-Object { $_.EndTime -gt (Get-Date).AddDays(-1) } | Sort-Object JobName | Format-Table JobName, Result, EndTime
JobName              Result    EndTime
-------              ------    -------
BK-ERP-SQL           Success   27/10/2026 02:14:51
BK-FS01              Warning   27/10/2026 03:40:09
BK-Tier1-AD          Success   27/10/2026 01:05:33
:::

Cada aviso (*Warning*) tiene una causa y un dueño antes del mediodía: un archivo bloqueado hoy es una restauración incompleta mañana.

## 3. El plan de recuperación (runbook)

El plan vive fuera de la infraestructura que protege: impreso, en el gestor de documentos de otro proveedor o en el repositorio, no solo en el SharePoint que puede estar caído.

:::ui Confluence · DR · Runbook de recuperación
> Espacio IT › Continuidad › RB-DR-01 Recuperación completa de la sede
= Quién declara el desastre: Director de IT (suplente: responsable de infraestructura)
= Árbol de llamadas: IT → Dirección → Responsables de área → Proveedores (circuitos, nube, copias)
= Orden 1: DC01 y DC02 (AD y DNS) · comprobación: dcdiag sin errores, resolución de nombres
= Orden 2: SQL01 (ERP) · comprobación: base de datos en línea, último log aplicado
= Orden 3: APP01 y APP02 (servidores del ERP) · comprobación: servicio del ERP arrancado
= Orden 4: FS01, INTRANET01 · comprobación: unidad S: accesible desde un puesto
= Vuelta atrás: cómo volver al sitio principal cuando esté sano (y quién decide)
:::

- El orden sale de las **dependencias**, no del nivel: el ERP es nivel 1, pero sin AD y DNS no arranca.
- Cada paso tiene una **comprobación** que demuestra que ha funcionado, y la hora a la que se marcó.
- Los teléfonos de los proveedores y los contratos con sus números de cliente van dentro del plan.

## 4. La prueba

Hay tres tipos y se hacen los tres: **de mesa** (se lee el plan en voz alta con un escenario y aparecen los huecos), **parcial** (se restaura un servicio en una red aislada) y **completa** (se recupera la sede entera en el sitio secundario, sin tocar producción).

:::ui Veeam · Trabajo SureBackup
> Copia de seguridad › SureBackup › Trabajos › SB-Tier1
= Laboratorio virtual: VLAB-DR (red aislada, sin salida a producción)
= Grupo de aplicaciones: DC01 → SQL01 → APP01 (con orden y esperas)
= Comprobaciones: latido, ping, puerto 1433 en SQL01, script que consulta un pedido de prueba
= Programación: primer sábado de cada mes, 06:00
[Iniciar]
:::

En la prueba completa se cronometra cada paso del runbook:

| Paso | RTO objetivo | Medido | Nota |
|---|---|---|---|
| AD y DNS en línea | 2 h | 1 h 10 min | — |
| ERP dando servicio | 4 h | 5 h 25 min | La licencia del ERP estaba ligada a la MAC del servidor original |
| Unidad S: accesible | 8 h | 3 h 05 min | — |
| Último dato del ERP (RPO) | 15 min | 12 min | — |

El ERP se pasó de su RTO por algo que ninguna copia arregla: la licencia. Para eso se hacen las pruebas.

## 5. El informe y las acciones

- Alcance, escenario, hora de inicio y de fin, quién participó.
- La tabla de tiempos medidos contra los objetivos, servicio a servicio.
- Cada desviación con una **acción, un dueño y una fecha** (en el ejemplo: pedir al fabricante una licencia para el sitio secundario y añadirla al runbook).
- Qué cambia en el plan. La versión nueva del runbook se publica el mismo mes.
- Se presenta a dirección: el BCP es una decisión de negocio, IT aporta los números.

## 6. Lo que revisas cada mes y cada año

- Cada mes: trabajos con aviso o error, resultado del SureBackup, que la copia inmutable sigue siéndolo (fecha de bloqueo del último punto).
- Cada vez que entra un servicio nuevo: su fila en la tabla del BIA y su paso en el runbook. Sin eso, no entra en producción.
- Cada año: la prueba completa y la revisión del BIA con negocio (los RPO y RTO cambian cuando cambia el negocio).

## Siguientes pasos

- **Azure Site Recovery** para usar una región de Azure como sitio secundario y pagar el cómputo solo cuando se usa.
- Un **plan específico de ransomware**: aislar, decidir desde qué punto restaurar (el último limpio, no el último) y comprobar con antivirus el punto antes de devolverlo a producción.
- **ISO 22301** si la empresa necesita certificar su continuidad de negocio.
- La alerta de Sentinel que avisa cuando alguien intenta borrar copias o cambiar la inmutabilidad (guía de Microsoft Sentinel).
""",
  en="""
## What you'll get

Moving from "we have backups" to "we know how long it takes us to come back, and we have measured it". Every service with an RPO and RTO agreed with the business, backups ransomware can't delete, a recovery plan someone else can follow at three in the morning, and a yearly test that proves all of it works.

## Before you start

- The list of services and their dependencies (CMDB, inventory or whatever spreadsheet exists). Repo 32 in the portfolio, *Backup Restore Test Tracker*, works as a template to track services, RPOs and tests.
- One business owner per service who can decide how long it may be down.
- The backup tool with working jobs (Level 2 Veeam guide) and a second site or cloud region.
- Two clear words: **RPO** is how much data you can lose (the age of the last good backup) and **RTO** is how long you can take to restore service.

## 1. The impact analysis (BIA) in one table

One meeting per area with one question: "if this service goes down at 10:00 on a Monday, from what time is it a serious problem, and how much lost work will you accept redoing?". The table comes from there, not from IT.

| Service | If it goes down | RPO | RTO | Tier |
|---|---|---|---|---|
| ERP (orders and invoicing) | No invoicing, no shipping | 15 min | 4 h | 1 |
| Active Directory and DNS | Nobody can get into anything | 1 h | 2 h | 1 |
| File server (S: drive) | People work from local copies | 24 h | 8 h | 2 |
| Intranet | Annoying, there are alternatives | 24 h | 48 h | 3 |
| Email (Microsoft 365) | SaaS: depends on Microsoft | 24 h (own backup) | — | 1 |

- The **tier** decides the recovery order and the budget: a 15-minute RPO needs replication or database logs, not a nightly backup.
- Microsoft 365 is not "no backup needed": Microsoft guarantees the service, not that you recover what a user or an attacker deleted four months ago. Your own backup (for example Veeam Backup for Microsoft 365) covers that gap.

## 2. The 3-2-1-1-0 rule

- **3** copies of the data (production plus two).
- **2** different media (disk and object, or disk and tape).
- **1** off site.
- **1** immutable or offline: not even a compromised administrator can delete it before it expires.
- **0** errors in verification: a backup that has never been restored is a hypothesis.

:::ui Veeam Backup & Replication · Hardened repository
> Backup Infrastructure › Backup Repositories › Add › Direct attached › Hardened Linux
= Server: vbr-hardened-01 (Ubuntu, no SSH, single-use credentials)
= Path: /mnt/veeam-xfs (XFS with shared blocks)
= [x] Make recent backups immutable for: 14 days
= Secondary copy: Object (S3 compatible) with Object Lock · 30 days
[Apply]
:::

:::term PowerShell · Veeam (backup console)
$ Get-VBRBackupSession | Where-Object { $_.EndTime -gt (Get-Date).AddDays(-1) } | Sort-Object JobName | Format-Table JobName, Result, EndTime
JobName              Result    EndTime
-------              ------    -------
BK-ERP-SQL           Success   27/10/2026 02:14:51
BK-FS01              Warning   27/10/2026 03:40:09
BK-Tier1-AD          Success   27/10/2026 01:05:33
:::

Every *Warning* has a cause and an owner before midday: a locked file today is an incomplete restore tomorrow.

## 3. The recovery plan (runbook)

The plan lives outside the infrastructure it protects: printed, in another provider's document store or in the repository, not only in the SharePoint that may be down.

:::ui Confluence · DR · Recovery runbook
> IT space › Continuity › RB-DR-01 Full site recovery
= Who declares the disaster: IT Director (deputy: infrastructure lead)
= Call tree: IT → Management → Area leads → Providers (circuits, cloud, backup)
= Order 1: DC01 and DC02 (AD and DNS) · check: dcdiag with no errors, name resolution
= Order 2: SQL01 (ERP) · check: database online, last log applied
= Order 3: APP01 and APP02 (ERP servers) · check: ERP service started
= Order 4: FS01, INTRANET01 · check: S: drive reachable from a desktop
= Failback: how to return to the main site once it is healthy (and who decides)
:::

- The order comes from **dependencies**, not from the tier: the ERP is tier 1, but without AD and DNS it won't start.
- Every step has a **check** that proves it worked, and the time it was ticked.
- The providers' phone numbers and the contracts with their customer numbers go inside the plan.

## 4. The test

There are three kinds and you do all three: **tabletop** (the plan is read aloud against a scenario and the gaps appear), **partial** (one service is restored into an isolated network) and **full** (the whole site is recovered at the secondary site, without touching production).

:::ui Veeam · SureBackup job
> Backup › SureBackup › Jobs › SB-Tier1
= Virtual lab: VLAB-DR (isolated network, no route to production)
= Application group: DC01 → SQL01 → APP01 (with order and waits)
= Checks: heartbeat, ping, port 1433 on SQL01, a script that queries a test order
= Schedule: first Saturday of every month, 06:00
[Start]
:::

In the full test each runbook step is timed:

| Step | Target RTO | Measured | Note |
|---|---|---|---|
| AD and DNS online | 2 h | 1 h 10 min | — |
| ERP serving | 4 h | 5 h 25 min | The ERP licence was tied to the original server's MAC address |
| S: drive reachable | 8 h | 3 h 05 min | — |
| Latest ERP data (RPO) | 15 min | 12 min | — |

The ERP missed its RTO because of something no backup fixes: the licence. That is what tests are for.

## 5. The report and the actions

- Scope, scenario, start and end time, who took part.
- The table of measured times against the targets, service by service.
- Every deviation with an **action, an owner and a date** (in the example: ask the vendor for a licence for the secondary site and add it to the runbook).
- What changes in the plan. The new runbook version is published the same month.
- It goes to management: the BCP is a business decision, IT brings the numbers.

## 6. What you review every month and every year

- Every month: jobs with warnings or errors, the SureBackup result, that the immutable copy still is (the lock date of the latest point).
- Whenever a new service arrives: its row in the BIA table and its step in the runbook. Without them, it doesn't go into production.
- Every year: the full test and the BIA review with the business (RPOs and RTOs change when the business changes).

## Next steps

- **Azure Site Recovery** to use an Azure region as the secondary site and pay for compute only when you use it.
- A **ransomware-specific plan**: isolate, decide which point to restore from (the last clean one, not the last one) and scan that point before it goes back to production.
- **ISO 22301** if the company needs to certify its business continuity.
- The Sentinel alert that fires when someone tries to delete backups or change immutability (Microsoft Sentinel guide).
""")

# ---------------------------------------------------------------- L4 · Cisco
g(slug="cisco-vlans-troncales-router-de-la-sede-y-un-puerto-que-no-da-red", topic="cisco", date="2026-10-27",
  title_es="Cisco: VLANs, troncales, el router de la sede y un puerto que no da red",
  title_en="Cisco: VLANs, trunks, the site router and a port that gives no network",
  dek_es="Leer un switch Catalyst antes de tocarlo, configurar puertos de acceso y troncales sin cortar una planta, la ruta por defecto con respaldo automático en el router, el diagnóstico de un puerto en err-disabled y cómo hacer cambios en remoto con red de seguridad.",
  dek_en="Read a Catalyst switch before touching it, configure access ports and trunks without cutting off a floor, the default route with automatic failover on the router, diagnosing a port in err-disabled, and how to make remote changes with a safety net.",
  es="""
## Qué vas a conseguir

Moverte con soltura en la red de una sede con switches Catalyst y un router ISR: entender qué hay antes de cambiar nada, dar de alta puestos y teléfonos en su VLAN, ampliar una troncal sin dejar a nadie sin red, que el router cambie solo al circuito de respaldo, y resolver el ticket de red más habitual en minutos.

## Antes de empezar

- Acceso por **SSH** (nunca Telnet) o consola, con usuario nominal (TACACS+ o RADIUS si existe; cuenta local solo de emergencia).
- Una **copia de la configuración** de cada equipo antes de la ventana de cambio, y el cambio aprobado.
- El plano de la sede: qué switch da servicio a qué planta, qué VLAN es qué, dónde está el uplink al core y qué IP tiene cada circuito.

## 1. Leer el switch antes de tocarlo

:::term SW-P2-01 · Catalyst 9200 (IOS XE)
$ show version | include uptime|Software
$ show vlan brief
$ show interfaces status
$ show interfaces trunk
$ show cdp neighbors
SW-P2-01 uptime is 41 weeks, 2 days, 3 hours, 12 minutes
Cisco IOS XE Software, Version 17.09.04a
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
10   GESTION                          active
20   USUARIOS                         active    Gi1/0/1, Gi1/0/2, ... Gi1/0/40
30   VOZ                              active
99   IMPRESORAS                       active    Gi1/0/41, Gi1/0/42
Port      Mode     Encapsulation  Status        Native vlan
Te1/1/1   on       802.1q         trunking      999
Port      Vlans allowed on trunk
Te1/1/1   10,20,30,99
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
CORE-01          Ten 1/1/1         141             R S I  C9500     Ten 1/0/7
:::

Con esto sabes la versión, qué VLAN existe y dónde, qué troncales hay y qué VLAN dejan pasar, y quién está al otro lado de cada enlace (CDP). Si una VLAN no aparece en *Vlans allowed on trunk*, esa VLAN no llega a esta planta.

## 2. Un puesto con teléfono: puerto de acceso

:::term SW-P2-01 · configuración
$ configure terminal
$ interface GigabitEthernet1/0/12
$  description PUESTO 2.14
$  switchport mode access
$  switchport access vlan 20
$  switchport voice vlan 30
$  spanning-tree portfast
$  spanning-tree bpduguard enable
$  no shutdown
$ end
$ copy running-config startup-config
:::

- `switchport voice vlan 30`: el teléfono IP marca su tráfico en la VLAN de voz y el PC que cuelga de él sigue en la 20. Un solo cable, dos redes.
- `portfast` hace que el puerto pase a reenviar al instante (el PC coge IP sin esperar 30 segundos) y `bpduguard` lo apaga si alguien conecta un switch. Siempre van juntos en los puertos de usuario.
- Sin `copy running-config startup-config`, el cambio se pierde en el siguiente reinicio.

## 3. La troncal: añadir una VLAN sin cortar la planta

:::term SW-P2-01 · troncal hacia el core
$ show interfaces Te1/1/1 trunk
$ configure terminal
$ interface TenGigabitEthernet1/1/1
$  switchport trunk allowed vlan add 40
$ end
:::

! `switchport trunk allowed vlan 40` (sin **add**) sustituye la lista entera: la troncal deja pasar solo la VLAN 40 y la planta se queda sin red de usuarios, voz y gestión, incluida tu sesión SSH. Es el error de red más caro y más repetido. Siempre `add` o `remove`, y la lista completa revisada con `show interfaces trunk` antes y después.

La VLAN 40 también tiene que existir en el switch (`vlan 40`, `name INVITADOS`) y estar permitida en el otro extremo, en el core. Y la VLAN nativa de las troncales es una que no use nadie (aquí la 999), no la 1.

## 4. El router de la sede: salida y circuito de respaldo

La sede tiene un circuito principal y uno de respaldo. El router sale por el principal mientras el proveedor responda, y cambia solo al respaldo cuando deja de hacerlo.

:::term RT-SEDE-01 · ISR 4331
$ configure terminal
$ ip sla 1
$  icmp-echo 203.0.113.1 source-interface GigabitEthernet0/0/0
$  frequency 10
$ ip sla schedule 1 life forever start-time now
$ track 1 ip sla 1 reachability
$ ip route 0.0.0.0 0.0.0.0 203.0.113.1 track 1
$ ip route 0.0.0.0 0.0.0.0 198.51.100.1 250
$ end
$ show track 1
Track 1
  IP SLA 1 reachability
  Reachability is Up
    2 changes, last change 3d04h
:::

- **IP SLA** hace ping cada 10 segundos a la puerta de enlace del proveedor principal; el **track** sigue ese resultado.
- La ruta por defecto principal depende del track. Cuando el ping falla, desaparece y queda la de respaldo, que tiene distancia administrativa 250 (*ruta flotante*).
- Para comprobarlo sin esperar a una avería: `show ip route 0.0.0.0` dice qué ruta está activa; en una ventana de cambio, se apaga la interfaz del principal y se mira cuánto tarda en cambiar.

En la interfaz de cada VLAN de usuarios del core, `ip helper-address 10.20.1.10` reenvía las peticiones de DHCP al servidor: sin ella, los puestos de una VLAN nueva se quedan con una IP 169.254.x.x.

## 5. El ticket: "el puesto 2.14 no tiene red"

:::term SW-P2-01 · diagnóstico
$ show interfaces Gi1/0/12 status
$ show logging | include Gi1/0/12
Port      Name          Status       Vlan  Duplex  Speed Type
Gi1/0/12  PUESTO 2.14   err-disabled 20    auto    auto  10/100/1000BaseTX
%SPANTREE-2-BLOCK_BPDUGUARD: Received BPDU on port Gi1/0/12 with BPDU Guard enabled. Disabling port.
%PM-4-ERR_DISABLE: bpduguard error detected on Gi1/0/12, putting Gi1/0/12 in err-disable state
:::

El estado del puerto dice casi todo:

| Estado | Qué significa | Qué haces |
|---|---|---|
| **connected** | Hay enlace | `show mac address-table interface Gi1/0/12`: ¿aparece la MAC del PC? Si sí, el problema es IP/DHCP, no el switch |
| **notconnect** | No hay enlace | Cable, roseta, el patch del armario o la tarjeta del PC |
| **err-disabled** | El switch lo ha apagado a propósito | `show logging` dice por qué (bpduguard, port-security, flapping) |
| **disabled** | Alguien lo apagó (`shutdown`) | El historial de cambios dice quién y por qué |

Aquí alguien conectó un switch pequeño en su mesa para tener más puertos. Se retira el aparato y se reactiva el puerto:

:::term SW-P2-01
$ configure terminal
$ interface Gi1/0/12
$  shutdown
$  no shutdown
$ end
:::

Si en `show interfaces Gi1/0/12` aparecen errores de **CRC** o *input errors* que suben, el problema es físico: el cable o la roseta.

## 6. Cambios en remoto con red de seguridad

:::term Antes de un cambio que podría dejarte sin acceso
$ reload in 10
$ configure terminal
# ... el cambio ...
$ end
# si sigues conectado y todo va bien:
$ reload cancel
$ copy running-config startup-config
:::

`reload in 10` programa un reinicio dentro de 10 minutos. Si el cambio te deja fuera, el equipo arranca con la configuración guardada (la anterior) y vuelves a entrar. Si todo va bien, `reload cancel` y se guarda. Es la diferencia entre una corrección en dos minutos y un viaje a la sede.

## 7. Lo que revisas cada mes

- Copias de configuración automáticas (Oxidized, RANCID o el propio `archive` de IOS) y que el último cambio está en el repositorio.
- Versiones de IOS XE frente a los avisos de seguridad de Cisco: los equipos con un aviso crítico tienen fecha de actualización.
- Puertos `err-disabled` y puertos sin uso en más de 90 días (`show interfaces | include line protocol|Last input`): los que no se usan se apagan y se dejan en una VLAN sin servicio.
- Que el track del router ha cambiado tantas veces como averías ha tenido el circuito. Si cambia sin avería, el ping se está perdiendo y hay que hablar con el proveedor.

## Siguientes pasos

- **802.1X** con Cisco ISE o NPS: el puerto da la VLAN según quién se conecta, no según el puerto.
- **NetBox** como fuente de verdad (qué puerto va a qué roseta) y **Ansible** con la colección `cisco.ios` para cambios repetibles (guía de Ansible del Nivel 3).
- SD-WAN cuando las sedes son muchas y los circuitos, variados.
- La guía de FortiGate (próximamente) cubre el cortafuegos que suele estar entre este router y el resto del mundo.
""",
  en="""
## What you'll get

Moving with ease in a site's network with Catalyst switches and an ISR router: understanding what is there before changing anything, bringing desks and phones onto their VLAN, extending a trunk without leaving anyone offline, having the router switch to the backup circuit by itself, and solving the most common network ticket in minutes.

## Before you start

- Access over **SSH** (never Telnet) or console, with a named account (TACACS+ or RADIUS if available; local account for emergencies only).
- A **copy of the configuration** of every device before the change window, and the change approved.
- The site map: which switch serves which floor, which VLAN is which, where the uplink to the core is and which IP each circuit has.

## 1. Read the switch before touching it

:::term SW-F2-01 · Catalyst 9200 (IOS XE)
$ show version | include uptime|Software
$ show vlan brief
$ show interfaces status
$ show interfaces trunk
$ show cdp neighbors
SW-F2-01 uptime is 41 weeks, 2 days, 3 hours, 12 minutes
Cisco IOS XE Software, Version 17.09.04a
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
10   MANAGEMENT                       active
20   USERS                            active    Gi1/0/1, Gi1/0/2, ... Gi1/0/40
30   VOICE                            active
99   PRINTERS                         active    Gi1/0/41, Gi1/0/42
Port      Mode     Encapsulation  Status        Native vlan
Te1/1/1   on       802.1q         trunking      999
Port      Vlans allowed on trunk
Te1/1/1   10,20,30,99
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
CORE-01          Ten 1/1/1         141             R S I  C9500     Ten 1/0/7
:::

With this you know the version, which VLANs exist and where, which trunks there are and which VLANs they carry, and who is on the other side of each link (CDP). If a VLAN isn't in *Vlans allowed on trunk*, that VLAN doesn't reach this floor.

## 2. A desk with a phone: access port

:::term SW-F2-01 · configuration
$ configure terminal
$ interface GigabitEthernet1/0/12
$  description DESK 2.14
$  switchport mode access
$  switchport access vlan 20
$  switchport voice vlan 30
$  spanning-tree portfast
$  spanning-tree bpduguard enable
$  no shutdown
$ end
$ copy running-config startup-config
:::

- `switchport voice vlan 30`: the IP phone tags its traffic on the voice VLAN and the PC hanging off it stays on 20. One cable, two networks.
- `portfast` makes the port forward straight away (the PC gets an IP without waiting 30 seconds) and `bpduguard` shuts it down if someone plugs in a switch. They always go together on user ports.
- Without `copy running-config startup-config`, the change is lost at the next reload.

## 3. The trunk: adding a VLAN without cutting off the floor

:::term SW-F2-01 · trunk to the core
$ show interfaces Te1/1/1 trunk
$ configure terminal
$ interface TenGigabitEthernet1/1/1
$  switchport trunk allowed vlan add 40
$ end
:::

! `switchport trunk allowed vlan 40` (without **add**) replaces the whole list: the trunk carries only VLAN 40 and the floor loses the user, voice and management networks, including your SSH session. It is the most expensive and most repeated network mistake. Always `add` or `remove`, and the full list checked with `show interfaces trunk` before and after.

VLAN 40 also has to exist on the switch (`vlan 40`, `name GUESTS`) and be allowed at the other end, on the core. And the trunks' native VLAN is one nobody uses (999 here), not 1.

## 4. The site router: egress and backup circuit

The site has a primary circuit and a backup one. The router goes out through the primary while the provider responds, and switches to the backup by itself when it stops responding.

:::term RT-SITE-01 · ISR 4331
$ configure terminal
$ ip sla 1
$  icmp-echo 203.0.113.1 source-interface GigabitEthernet0/0/0
$  frequency 10
$ ip sla schedule 1 life forever start-time now
$ track 1 ip sla 1 reachability
$ ip route 0.0.0.0 0.0.0.0 203.0.113.1 track 1
$ ip route 0.0.0.0 0.0.0.0 198.51.100.1 250
$ end
$ show track 1
Track 1
  IP SLA 1 reachability
  Reachability is Up
    2 changes, last change 3d04h
:::

- **IP SLA** pings the primary provider's gateway every 10 seconds; the **track** follows that result.
- The primary default route depends on the track. When the ping fails it disappears and the backup one remains, with administrative distance 250 (a *floating route*).
- To check it without waiting for a fault: `show ip route 0.0.0.0` says which route is active; in a change window, shut the primary interface and time how long it takes to switch.

On each user VLAN interface on the core, `ip helper-address 10.20.1.10` forwards DHCP requests to the server: without it, desks on a new VLAN end up with a 169.254.x.x address.

## 5. The ticket: "desk 2.14 has no network"

:::term SW-F2-01 · diagnosis
$ show interfaces Gi1/0/12 status
$ show logging | include Gi1/0/12
Port      Name          Status       Vlan  Duplex  Speed Type
Gi1/0/12  DESK 2.14     err-disabled 20    auto    auto  10/100/1000BaseTX
%SPANTREE-2-BLOCK_BPDUGUARD: Received BPDU on port Gi1/0/12 with BPDU Guard enabled. Disabling port.
%PM-4-ERR_DISABLE: bpduguard error detected on Gi1/0/12, putting Gi1/0/12 in err-disable state
:::

The port status says almost everything:

| Status | What it means | What you do |
|---|---|---|
| **connected** | There is a link | `show mac address-table interface Gi1/0/12`: does the PC's MAC show up? If yes, the problem is IP/DHCP, not the switch |
| **notconnect** | No link | Cable, wall socket, the patch in the cabinet or the PC's network card |
| **err-disabled** | The switch shut it down on purpose | `show logging` says why (bpduguard, port-security, flapping) |
| **disabled** | Someone shut it down (`shutdown`) | The change history says who and why |

Here someone plugged a small switch into their desk to get more ports. The device is removed and the port re-enabled:

:::term SW-F2-01
$ configure terminal
$ interface Gi1/0/12
$  shutdown
$  no shutdown
$ end
:::

If `show interfaces Gi1/0/12` shows **CRC** errors or *input errors* going up, the problem is physical: the cable or the wall socket.

## 6. Remote changes with a safety net

:::term Before a change that could lock you out
$ reload in 10
$ configure terminal
# ... the change ...
$ end
# if you are still connected and everything works:
$ reload cancel
$ copy running-config startup-config
:::

`reload in 10` schedules a reload in 10 minutes. If the change locks you out, the device boots with the saved (previous) configuration and you get back in. If all is well, `reload cancel` and save. It is the difference between a two-minute fix and a trip to the site.

## 7. What you review each month

- Automatic configuration backups (Oxidized, RANCID or IOS's own `archive`) and that the latest change is in the repository.
- IOS XE versions against Cisco's security advisories: devices with a critical advisory have an upgrade date.
- Ports in `err-disabled` and ports unused for more than 90 days (`show interfaces | include line protocol|Last input`): unused ones are shut down and left in a VLAN with no service.
- That the router's track has changed as many times as the circuit has had faults. If it changes without a fault, pings are being lost and it's time to talk to the provider.

## Next steps

- **802.1X** with Cisco ISE or NPS: the port gives a VLAN based on who connects, not on the port.
- **NetBox** as the source of truth (which port goes to which socket) and **Ansible** with the `cisco.ios` collection for repeatable changes (Level 3 Ansible guide).
- SD-WAN when there are many sites and the circuits are varied.
- The FortiGate guide (coming soon) covers the firewall that usually sits between this router and the rest of the world.
""")

# ---------------------------------------------------------------- L4 · Global Admin and PIM
g(slug="microsoft-365-roles-de-administracion-pim-y-cuentas-de-emergencia", topic="m365-pim", date="2026-10-27",
  title_es="Microsoft 365: los roles de administración, PIM y las cuentas de emergencia",
  title_en="Microsoft 365: admin roles, PIM and the emergency accounts",
  dek_es="Inventariar quién es administrador hoy, pasar cada tarea al rol mínimo, dejar dos cuentas de emergencia bien guardadas, convertir el resto en asignaciones elegibles con PIM (MFA, justificación y aprobación), y las revisiones y alertas que lo mantienen así.",
  dek_en="Inventory who is an administrator today, move each task to the least-privileged role, keep two well-guarded emergency accounts, turn the rest into eligible assignments with PIM (MFA, justification and approval), and the reviews and alerts that keep it that way.",
  es="""
## Qué vas a conseguir

Un tenant donde nadie es administrador global por costumbre. Cada técnico tiene el rol justo para su trabajo, lo activa cuando lo necesita durante un tiempo limitado y dejando rastro, y solo dos cuentas de emergencia tienen el rol de forma permanente. Si roban la contraseña de un técnico un martes cualquiera, el atacante no se lleva el tenant.

## Antes de empezar

- Licencias **Microsoft Entra ID P2** (incluidas en Microsoft 365 E5 o en Entra ID Governance) para los usuarios que usarán PIM.
- El rol **Privileged Role Administrator** para configurar PIM (y, al principio, un Global Administrator a mano).
- El módulo **Microsoft Graph PowerShell** (guía de Graph del Nivel 3).
- Una conversación previa con el equipo: va a cambiar cómo trabajan. Explicar el porqué ahorra muchas quejas.

## 1. Quién es administrador hoy

:::term PowerShell · Microsoft Graph
$ Connect-MgGraph -Scopes "RoleManagement.Read.Directory","User.Read.All"
$ Get-MgDirectoryRole | ForEach-Object { $r = $_; Get-MgDirectoryRoleMember -DirectoryRoleId $r.Id | ForEach-Object { [pscustomobject]@{ Rol = $r.DisplayName; Miembro = $_.AdditionalProperties.userPrincipalName } } } | Sort-Object Rol | Format-Table
Rol                          Miembro
---                          -------
Exchange Administrator       a.vidal@contoso.com
Global Administrator         admin@contoso.onmicrosoft.com
Global Administrator         j.serrano@contoso.com
Global Administrator         m.ortega@contoso.com
Global Administrator         p.ruiz@contoso.com
Global Administrator         proveedor.soporte@contoso.com
Global Administrator         s.navas@contoso.com
User Administrator           l.prado@contoso.com
:::

Seis administradores globales, uno de ellos la cuenta de un proveedor y otro la cuenta con la que se creó el tenant. Es lo normal en un tenant de unos años, y es lo que vas a cambiar.

## 2. Cada tarea a su rol mínimo

| Tarea habitual | Rol suficiente |
|---|---|
| Restablecer contraseñas de usuarios | Helpdesk Administrator |
| Métodos de MFA de los usuarios | Authentication Administrator |
| Altas, bajas y grupos | User Administrator |
| Licencias | License Administrator |
| Buzones, reglas de transporte | Exchange Administrator |
| Teams, directivas de reuniones | Teams Administrator |
| Dispositivos y directivas de Intune | Intune Administrator |
| Conditional Access | Conditional Access Administrator |
| Leer todo sin cambiar nada (auditorías) | Global Reader |
| Facturación y suscripciones | Billing Administrator |

Con esta tabla, casi nadie necesita Global Administrator para su día a día. El proveedor tampoco: se le da un rol concreto mediante **GDAP** (relaciones de administración delegada con permisos granulares y caducidad) en lugar de una cuenta dentro del tenant.

## 3. Las dos cuentas de emergencia

- Dos cuentas **solo en la nube** con el dominio `onmicrosoft.com` (`brk-admin-01`, `brk-admin-02`), sin licencia, sin buzón, sin dependencia de AD local ni de un proveedor de identidad federado.
- Son las únicas con **Global Administrator permanente (activo)**.
- Excluidas de todas las políticas de Conditional Access (guía de Conditional Access del Nivel 3), salvo de una propia que exija su método de autenticación.
- Microsoft exige MFA para entrar en los portales de administración, también a estas cuentas: cada una tiene una **llave FIDO2 (passkey)** guardada en una caja fuerte, distinta para cada cuenta, y la contraseña larga en un sobre en otra ubicación.
- Cada inicio de sesión con ellas genera una alerta inmediata (guía de Microsoft Sentinel). Se prueban cada tres meses, con un cambio registrado, para saber que funcionan.

## 4. PIM: elegible en lugar de permanente

:::ui Entra admin center · PIM · Configuración del rol
> Gobierno de identidades › Privileged Identity Management › Roles de Microsoft Entra › Configuración › Global Administrator
= Duración máxima de la activación: 2 horas
= Al activar, requerir: Contexto de autenticación de Conditional Access (c1 · MFA resistente a phishing)
= Requerir justificación al activar: Sí
= Requerir información del ticket al activar: Sí
= Requerir aprobación para activar: Sí · Aprobadores: sg-pim-aprobadores
= Permitir asignación elegible permanente: No · Caducar asignaciones elegibles tras: 6 meses
= Notificaciones: al activar, aviso a sg-pim-aprobadores y al equipo de seguridad
[Actualizar]
:::

Se configuran así los roles más sensibles (Global Administrator, Privileged Role Administrator, Security Administrator, Conditional Access Administrator). Para roles de menos impacto (Helpdesk, License) basta con MFA y justificación, sin aprobación: si cada reseteo de contraseña espera a un aprobador, la gente buscará atajos.

Después, en **Asignaciones › Agregar asignaciones › Elegible**, cada técnico recibe sus roles como elegibles y se retiran las asignaciones activas que tenía.

El técnico activa el rol desde **Mis roles** cuando lo necesita, o con PowerShell:

:::term PowerShell · activar un rol elegible
$ $me = (Get-MgUser -UserId "m.ortega@contoso.com").Id
$ $rol = (Get-MgRoleManagementDirectoryRoleDefinition -Filter "displayName eq 'Exchange Administrator'").Id
$ $params = @{ Action = "selfActivate"; PrincipalId = $me; RoleDefinitionId = $rol; DirectoryScopeId = "/"; Justification = "CHG-1042 regla de transporte"; ScheduleInfo = @{ StartDateTime = (Get-Date); Expiration = @{ Type = "AfterDuration"; Duration = "PT2H" } } }
$ New-MgRoleManagementDirectoryRoleAssignmentScheduleRequest -BodyParameter $params | Format-List Status, Action
Status : Provisioned
Action : selfActivate
:::

> Consejo: el **contexto de autenticación** de Conditional Access (en "Al activar, requerir") es más fuerte que el simple "MFA de Azure": exige que la activación se haga con una llave FIDO2 o Windows Hello, no con un SMS que se puede interceptar.

## 5. El ticket: "no me deja activar el rol"

| Lo que ve el técnico | Causa | Qué haces |
|---|---|---|
| No aparece el rol en *Mis roles* | La asignación elegible caducó (6 meses) | Se renueva tras revisar que sigue haciéndole falta |
| "Pendiente de aprobación" | El rol requiere aprobación | El aprobador lo ve en *Aprobar solicitudes*; si es urgente, el teléfono |
| Error de autenticación al activar | No cumple el contexto de autenticación (sin llave FIDO2 registrada) | Registrar el método en *Mi información de seguridad* |
| Activado pero el portal dice que no tiene permiso | El token anterior no lleva el rol | Cerrar sesión y volver a entrar en el portal (o esperar unos minutos) |

## 6. Revisiones y alertas

- **Revisiones de acceso** trimestrales de los roles privilegiados (*PIM › Revisiones de acceso*): cada técnico confirma que sigue necesitando sus roles, o su responsable lo decide; si nadie responde, se retira el acceso.
- **Alertas de PIM** que revisas cada semana: *Demasiados administradores globales*, *Se asignan roles fuera de Privileged Identity Management*, *Los administradores no usan sus roles privilegiados*.
- **Historial de auditoría de PIM**: quién activó qué, cuándo, con qué justificación y qué ticket. Es lo que te pedirá un auditor de ISO 27001.

## 7. Lo que revisas cada mes

- Número de Global Administrator activos: dos (las de emergencia). Si hay más, alguien se asignó el rol fuera de PIM.
- Activaciones sin número de ticket válido o con justificaciones vacías ("necesario", "trabajo").
- Las cuentas de emergencia: sin inicios de sesión salvo las pruebas, llaves en su sitio.
- Las relaciones GDAP de los proveedores: roles concedidos y fecha de caducidad.

## Siguientes pasos

- **PIM para grupos**: grupos con acceso a recursos (por ejemplo, propietarios de una suscripción) que también se activan bajo demanda.
- **PIM para recursos de Azure**: los roles de suscripción y grupo de recursos con el mismo modelo.
- **Unidades administrativas**: un técnico de una sede administra solo los usuarios de su sede.
- **Estaciones de trabajo con acceso privilegiado** (PAW) para las tareas de Global Administrator.
""",
  en="""
## What you'll get

A tenant where nobody is a global administrator out of habit. Each technician has just the role their work needs, activates it when they need it for a limited time and leaving a trail, and only two emergency accounts hold the role permanently. If a technician's password is stolen on any given Tuesday, the attacker doesn't walk away with the tenant.

## Before you start

- **Microsoft Entra ID P2** licences (included in Microsoft 365 E5 or Entra ID Governance) for the users who will use PIM.
- The **Privileged Role Administrator** role to configure PIM (and, at the start, a Global Administrator at hand).
- The **Microsoft Graph PowerShell** module (Level 3 Graph guide).
- A conversation with the team first: the way they work is going to change. Explaining why saves a lot of complaints.

## 1. Who is an administrator today

:::term PowerShell · Microsoft Graph
$ Connect-MgGraph -Scopes "RoleManagement.Read.Directory","User.Read.All"
$ Get-MgDirectoryRole | ForEach-Object { $r = $_; Get-MgDirectoryRoleMember -DirectoryRoleId $r.Id | ForEach-Object { [pscustomobject]@{ Role = $r.DisplayName; Member = $_.AdditionalProperties.userPrincipalName } } } | Sort-Object Role | Format-Table
Role                         Member
----                         ------
Exchange Administrator       a.vidal@contoso.com
Global Administrator         admin@contoso.onmicrosoft.com
Global Administrator         j.serrano@contoso.com
Global Administrator         m.ortega@contoso.com
Global Administrator         p.ruiz@contoso.com
Global Administrator         supplier.support@contoso.com
Global Administrator         s.navas@contoso.com
User Administrator           l.prado@contoso.com
:::

Six global administrators, one of them a supplier's account and another the account the tenant was created with. That is normal in a tenant a few years old, and it is what you are going to change.

## 2. Every task to its least-privileged role

| Common task | Role that is enough |
|---|---|
| Reset user passwords | Helpdesk Administrator |
| Users' MFA methods | Authentication Administrator |
| Joiners, leavers and groups | User Administrator |
| Licences | License Administrator |
| Mailboxes, transport rules | Exchange Administrator |
| Teams, meeting policies | Teams Administrator |
| Intune devices and policies | Intune Administrator |
| Conditional Access | Conditional Access Administrator |
| Read everything without changing anything (audits) | Global Reader |
| Billing and subscriptions | Billing Administrator |

With this table, almost nobody needs Global Administrator for their daily work. Neither does the supplier: they get a specific role through **GDAP** (granular delegated admin privileges, with expiry) instead of an account inside the tenant.

## 3. The two emergency accounts

- Two **cloud-only** accounts on the `onmicrosoft.com` domain (`brk-admin-01`, `brk-admin-02`), with no licence, no mailbox and no dependency on on-premises AD or a federated identity provider.
- They are the only ones with **permanent (active) Global Administrator**.
- Excluded from every Conditional Access policy (Level 3 Conditional Access guide), except one of their own that requires their authentication method.
- Microsoft requires MFA to sign in to the admin portals, for these accounts too: each one has a **FIDO2 security key (passkey)** kept in a safe, a different one per account, and the long password in a sealed envelope in another location.
- Every sign-in with them raises an immediate alert (Microsoft Sentinel guide). They are tested every three months, with a logged change, so you know they work.

## 4. PIM: eligible instead of permanent

:::ui Entra admin center · PIM · Role settings
> Identity governance › Privileged Identity Management › Microsoft Entra roles › Settings › Global Administrator
= Activation maximum duration: 2 hours
= On activation, require: Conditional Access authentication context (c1 · phishing-resistant MFA)
= Require justification on activation: Yes
= Require ticket information on activation: Yes
= Require approval to activate: Yes · Approvers: sg-pim-approvers
= Allow permanent eligible assignment: No · Expire eligible assignments after: 6 months
= Notifications: on activation, notify sg-pim-approvers and the security team
[Update]
:::

The most sensitive roles are set up like this (Global Administrator, Privileged Role Administrator, Security Administrator, Conditional Access Administrator). For lower-impact roles (Helpdesk, License) MFA and justification are enough, without approval: if every password reset waits for an approver, people will look for shortcuts.

Then, in **Assignments › Add assignments › Eligible**, each technician gets their roles as eligible and their active assignments are removed.

The technician activates the role from **My roles** when needed, or with PowerShell:

:::term PowerShell · activate an eligible role
$ $me = (Get-MgUser -UserId "m.ortega@contoso.com").Id
$ $role = (Get-MgRoleManagementDirectoryRoleDefinition -Filter "displayName eq 'Exchange Administrator'").Id
$ $params = @{ Action = "selfActivate"; PrincipalId = $me; RoleDefinitionId = $role; DirectoryScopeId = "/"; Justification = "CHG-1042 transport rule"; ScheduleInfo = @{ StartDateTime = (Get-Date); Expiration = @{ Type = "AfterDuration"; Duration = "PT2H" } } }
$ New-MgRoleManagementDirectoryRoleAssignmentScheduleRequest -BodyParameter $params | Format-List Status, Action
Status : Provisioned
Action : selfActivate
:::

> Tip: the Conditional Access **authentication context** (in "On activation, require") is stronger than plain "Azure MFA": it requires the activation to be done with a FIDO2 key or Windows Hello, not with a text message that can be intercepted.

## 5. The ticket: "it won't let me activate the role"

| What the technician sees | Cause | What you do |
|---|---|---|
| The role isn't in *My roles* | The eligible assignment expired (6 months) | Renew it after checking they still need it |
| "Pending approval" | The role requires approval | The approver sees it in *Approve requests*; if urgent, the phone |
| Authentication error on activation | The authentication context isn't met (no FIDO2 key registered) | Register the method in *My security info* |
| Activated but the portal says no permission | The previous token doesn't carry the role | Sign out of the portal and back in (or wait a few minutes) |

## 6. Reviews and alerts

- Quarterly **access reviews** of privileged roles (*PIM › Access reviews*): each technician confirms they still need their roles, or their manager decides; if nobody answers, access is removed.
- **PIM alerts** you review every week: *There are too many global administrators*, *Roles are being assigned outside of Privileged Identity Management*, *Administrators aren't using their privileged roles*.
- The **PIM audit history**: who activated what, when, with what justification and which ticket. It is what an ISO 27001 auditor will ask you for.

## 7. What you review each month

- The number of active Global Administrators: two (the emergency ones). If there are more, someone was assigned the role outside PIM.
- Activations without a valid ticket number or with empty justifications ("needed", "work").
- The emergency accounts: no sign-ins except the tests, keys where they should be.
- The suppliers' GDAP relationships: roles granted and expiry date.

## Next steps

- **PIM for Groups**: groups with access to resources (for example, owners of a subscription) that are also activated on demand.
- **PIM for Azure resources**: subscription and resource group roles under the same model.
- **Administrative units**: a site technician administers only that site's users.
- **Privileged access workstations** (PAW) for Global Administrator tasks.
""")

# ---------------------------------------------------------------- L4 · Microsoft Sentinel
g(slug="microsoft-sentinel-conectores-una-regla-en-kql-y-un-incidente-de-principio-a-fin", topic="sentinel", date="2026-10-27",
  title_es="Microsoft Sentinel: conectores, una regla en KQL y un incidente de principio a fin",
  title_en="Microsoft Sentinel: connectors, a KQL rule and an incident from start to finish",
  dek_es="El área de trabajo y los conectores que importan (Entra ID, Microsoft 365, Defender, servidores), la primera regla de análisis que avisa cuando entra una cuenta de emergencia, la automatización que asigna y avisa, la investigación de un incidente con KQL y cómo no arruinarse con la ingesta.",
  dek_en="The workspace and the connectors that matter (Entra ID, Microsoft 365, Defender, servers), the first analytics rule that alerts when an emergency account signs in, the automation that assigns and notifies, investigating an incident with KQL, and how not to go broke on ingestion.",
  es="""
## Qué vas a conseguir

Un Sentinel que recibe los registros que importan, genera incidentes que alguien atiende y no se come el presupuesto. Una regla de análisis escrita por ti, una automatización que la asigna y avisa al canal del equipo, y la rutina para investigar y cerrar un incidente con una clasificación que sirva para mejorar las reglas.

## Antes de empezar

- Un **área de trabajo de Log Analytics** en la región que corresponda a tus datos, y el rol **Microsoft Sentinel Contributor** sobre ella (y Log Analytics Contributor para los conectores).
- Sentinel se usa desde el **portal de Microsoft Defender** (operaciones de seguridad unificadas), junto con los incidentes de Defender XDR. Las rutas de esta guía son las de ese portal.
- Una idea del presupuesto: se paga por GB ingerido. Hay orígenes gratuitos (actividad de Azure, auditoría de Office 365, alertas de Defender) y otros que no lo son (inicios de sesión de Entra ID, eventos de seguridad de Windows).
- La guía de Azure Monitor y Log Analytics (próximamente) explica el área de trabajo por dentro; aquí basta con saber escribir una consulta KQL sencilla.

## 1. Los conectores que importan

:::ui Microsoft Defender · Sentinel · Centro de contenido
> Microsoft Sentinel › Administración de contenido › Centro de contenido
= Microsoft Entra ID: instalado · Tablas: SigninLogs, AuditLogs, AADNonInteractiveUserSignInLogs
= Microsoft 365: instalado · Tabla: OfficeActivity (Exchange, SharePoint, Teams) · sin coste de ingesta
= Microsoft Defender XDR: instalado · Incidentes y alertas sincronizados
= Windows Security Events via AMA: instalado · Regla de recopilación: dcr-servidores-seguridad (conjunto Común)
= Syslog via AMA: instalado · Regla de recopilación: dcr-linux-auth (auth, authpriv)
[Administrar]
:::

- Empieza por **identidad** (Entra ID) y **correo y documentos** (Microsoft 365): es por donde entra la mayoría de los ataques en un tenant de oficina.
- Los eventos de Windows se recogen con el **agente de Azure Monitor** y una regla de recopilación de datos. El conjunto **Común** basta para empezar; *Todos los eventos* multiplica el coste sin multiplicar las detecciones.
- Comprueba que llegan datos antes de escribir ninguna regla:

:::term Sentinel · Búsqueda avanzada (KQL)
$ SigninLogs
$ | where TimeGenerated > ago(1h)
$ | summarize Inicios = count() by ResultType
ResultType   Inicios
0            1 284
50126        37
50074        12
53003        4
:::

`ResultType` 0 es un inicio correcto; el resto son códigos de error de Entra ID (50126: credenciales incorrectas; 50074: falta completar MFA; 53003: bloqueado por Conditional Access).

## 2. La primera regla: entra una cuenta de emergencia

Las cuentas de emergencia no se usan nunca (guía de Global Admin y PIM). Si alguien entra con una, tiene que saberse en minutos. Primero, una **watchlist** con sus nombres para no escribirlos dentro de la regla:

:::ui Microsoft Defender · Sentinel · Watchlists
> Microsoft Sentinel › Configuración › Watchlists › Nueva
= Nombre y alias: breakglass
= Origen: archivo CSV con la columna UserPrincipalName
= Clave de búsqueda: UserPrincipalName
= Filas: brk-admin-01@contoso.onmicrosoft.com · brk-admin-02@contoso.onmicrosoft.com
[Crear]
:::

:::term Regla de análisis · consulta
$ let breakglass = _GetWatchlist("breakglass") | project UserPrincipalName;
$ SigninLogs
$ | where UserPrincipalName in~ (breakglass)
$ | project TimeGenerated, UserPrincipalName, IPAddress, Location, AppDisplayName, ResultType, UserAgent
:::

:::ui Microsoft Defender · Sentinel · Regla de análisis
> Microsoft Sentinel › Configuración › Análisis › Crear › Regla de consulta casi en tiempo real (NRT)
= Nombre: Inicio de sesión de una cuenta de emergencia
= Gravedad: Alta · Táctica MITRE ATT&CK: Acceso inicial, Cuentas válidas (T1078)
= Asignación de entidades: Cuenta → UserPrincipalName · IP → IPAddress
= Detalles de la alerta: título dinámico "Cuenta de emergencia {{UserPrincipalName}} desde {{IPAddress}}"
= Creación de incidentes: Habilitada · Agrupación de alertas: por cuenta, 24 horas
[Revisar y crear]
:::

- Una regla **NRT** se ejecuta cada minuto. Para la mayoría de reglas basta una **programada** cada 5 o 15 minutos; las NRT se reservan para lo que no puede esperar.
- La **asignación de entidades** es lo que permite después ver la cuenta y la IP como objetos en la investigación, y que Sentinel relacione este incidente con otros de la misma IP.

## 3. La automatización: asignar y avisar

:::ui Microsoft Defender · Sentinel · Automatización
> Microsoft Sentinel › Configuración › Automatización › Crear › Regla de automatización
= Nombre: Cuentas de emergencia → seguridad
= Desencadenador: Cuando se crea el incidente
= Condiciones: Nombre de la regla de análisis contiene "cuenta de emergencia"
= Acciones: Asignar propietario: equipo de seguridad de guardia · Cambiar gravedad: Alta · Agregar etiqueta: breakglass
= Acción: Ejecutar playbook: pb-aviso-teams (publica el incidente en el canal de seguridad)
[Aplicar]
:::

El **playbook** es una aplicación lógica de Azure: recibe el incidente y publica en Teams con el enlace. Las reglas de automatización ordenan el trabajo; los playbooks hacen cosas fuera de Sentinel (avisar, deshabilitar una cuenta, abrir un ticket en Jira Service Management).

## 4. Un incidente de principio a fin

Lunes, 07:12. El canal de seguridad recibe: *Cuenta de emergencia brk-admin-02 desde 198.51.100.23*.

1. **Abrir el incidente** (*Investigación y respuesta › Incidentes y alertas › Incidentes*): ver la alerta, las entidades (cuenta e IP) y la línea temporal.
2. **¿Fue un cambio planificado?** El registro de cambios dice que no hay prueba de las cuentas de emergencia programada esta semana.
3. **¿Qué hizo esa IP?**

:::term Búsqueda avanzada · la IP del incidente
$ SigninLogs
$ | where TimeGenerated > ago(24h) and IPAddress == "198.51.100.23"
$ | summarize Usuarios = dcount(UserPrincipalName), Fallos = countif(ResultType != "0"), Correctos = countif(ResultType == "0") by bin(TimeGenerated, 1h)
TimeGenerated         Usuarios   Fallos   Correctos
27/10/2026 05:00      143        141      0
27/10/2026 06:00      211        208      1
27/10/2026 07:00      1          0        1
:::

Muchos usuarios distintos, casi todo fallos y un acierto: un **ataque de difusión de contraseñas** (password spray) que acertó con la contraseña de una cuenta de emergencia.

4. **Contener**: deshabilitar la cuenta, revocar sus sesiones (`Revoke-MgUserSignInSession`), cambiar la contraseña, bloquear la IP en una ubicación con nombre de Conditional Access y revisar en *AuditLogs* qué hizo la cuenta en esos minutos.
5. **Clasificar y cerrar**: *Verdadero positivo — actividad sospechosa*, con un comentario de lo que se hizo y las acciones pendientes (por qué la cuenta de emergencia podía entrar solo con contraseña).

La clasificación no es burocracia: los incidentes cerrados como *Falso positivo* te dicen qué reglas hay que afinar, y los *Benignos* (actividad sospechosa pero esperada, como una prueba planificada) qué excepciones faltan.

## 5. El coste

:::term Búsqueda avanzada · qué ingiere más
$ Usage
$ | where TimeGenerated > ago(30d) and IsBillable == true
$ | summarize GB = round(sum(Quantity) / 1000, 1) by DataType
$ | sort by GB desc
DataType                          GB
SecurityEvent                     412.6
AADNonInteractiveUserSignInLogs   188.3
SigninLogs                        41.2
Syslog                            19.8
:::

- `SecurityEvent` arriba del todo suele ser un conjunto de eventos demasiado amplio o un servidor ruidoso: se ajusta la regla de recopilación.
- Las tablas que solo se consultan en una investigación pueden ir al plan **Basic** o **Auxiliary**, mucho más barato, a cambio de consultas más limitadas.
- Con un volumen estable, un **nivel de compromiso** diario abarata el GB.

## 6. Lo que revisas cada mes

- Reglas que no han generado ningún incidente en 90 días (¿siguen llegando los datos que miran?) y reglas que generan tantos que nadie los lee.
- El estado de los conectores y de las reglas: la tabla `SentinelHealth` y la página de cada conector dicen cuándo dejaron de llegar datos.
- Tiempo medio hasta asignar y hasta cerrar los incidentes de gravedad alta.
- La factura de ingesta frente al mes anterior, por tabla.

## Siguientes pasos

- Las **plantillas de reglas** de cada solución del Centro de contenido: se activan, se prueban y se afinan en lugar de escribirlas desde cero.
- **UEBA** (análisis de comportamiento de usuarios y entidades): detecta lo raro para cada usuario, no lo raro en general.
- **Inteligencia de amenazas**: indicadores de IP y dominios cruzados con tus registros.
- La alerta de copias borradas o inmutabilidad cambiada de la guía de DR/BCP, como segunda regla propia.
""",
  en="""
## What you'll get

A Sentinel that receives the logs that matter, raises incidents someone actually handles, and doesn't eat the budget. An analytics rule written by you, an automation that assigns it and notifies the team channel, and the routine to investigate and close an incident with a classification that helps improve the rules.

## Before you start

- A **Log Analytics workspace** in the region your data belongs in, and the **Microsoft Sentinel Contributor** role on it (plus Log Analytics Contributor for the connectors).
- Sentinel is used from the **Microsoft Defender portal** (unified security operations), alongside the Defender XDR incidents. The paths in this guide are that portal's.
- A rough budget: you pay per GB ingested. Some sources are free (Azure activity, Office 365 audit, Defender alerts) and others are not (Entra ID sign-ins, Windows security events).
- The Azure Monitor and Log Analytics guide (coming soon) explains the workspace from the inside; here it is enough to be able to write a simple KQL query.

## 1. The connectors that matter

:::ui Microsoft Defender · Sentinel · Content hub
> Microsoft Sentinel › Content management › Content hub
= Microsoft Entra ID: installed · Tables: SigninLogs, AuditLogs, AADNonInteractiveUserSignInLogs
= Microsoft 365: installed · Table: OfficeActivity (Exchange, SharePoint, Teams) · no ingestion cost
= Microsoft Defender XDR: installed · Incidents and alerts synchronised
= Windows Security Events via AMA: installed · Collection rule: dcr-servers-security (Common set)
= Syslog via AMA: installed · Collection rule: dcr-linux-auth (auth, authpriv)
[Manage]
:::

- Start with **identity** (Entra ID) and **mail and documents** (Microsoft 365): that is where most attacks on an office tenant come in.
- Windows events are collected with the **Azure Monitor agent** and a data collection rule. The **Common** set is enough to start; *All events* multiplies the cost without multiplying the detections.
- Check data is arriving before writing any rule:

:::term Sentinel · Advanced hunting (KQL)
$ SigninLogs
$ | where TimeGenerated > ago(1h)
$ | summarize SignIns = count() by ResultType
ResultType   SignIns
0            1,284
50126        37
50074        12
53003        4
:::

`ResultType` 0 is a successful sign-in; the rest are Entra ID error codes (50126: wrong credentials; 50074: MFA not completed; 53003: blocked by Conditional Access).

## 2. The first rule: an emergency account signs in

Emergency accounts are never used (Global Admin and PIM guide). If someone signs in with one, it has to be known within minutes. First, a **watchlist** with their names so they aren't written inside the rule:

:::ui Microsoft Defender · Sentinel · Watchlists
> Microsoft Sentinel › Configuration › Watchlists › New
= Name and alias: breakglass
= Source: CSV file with the UserPrincipalName column
= Search key: UserPrincipalName
= Rows: brk-admin-01@contoso.onmicrosoft.com · brk-admin-02@contoso.onmicrosoft.com
[Create]
:::

:::term Analytics rule · query
$ let breakglass = _GetWatchlist("breakglass") | project UserPrincipalName;
$ SigninLogs
$ | where UserPrincipalName in~ (breakglass)
$ | project TimeGenerated, UserPrincipalName, IPAddress, Location, AppDisplayName, ResultType, UserAgent
:::

:::ui Microsoft Defender · Sentinel · Analytics rule
> Microsoft Sentinel › Configuration › Analytics › Create › NRT query rule
= Name: Emergency account sign-in
= Severity: High · MITRE ATT&CK tactic: Initial Access, Valid Accounts (T1078)
= Entity mapping: Account → UserPrincipalName · IP → IPAddress
= Alert details: dynamic title "Emergency account {{UserPrincipalName}} from {{IPAddress}}"
= Incident creation: Enabled · Alert grouping: by account, 24 hours
[Review and create]
:::

- An **NRT** rule runs every minute. For most rules a **scheduled** one every 5 or 15 minutes is enough; NRT is kept for what can't wait.
- **Entity mapping** is what later lets you see the account and the IP as objects in the investigation, and lets Sentinel relate this incident to others from the same IP.

## 3. The automation: assign and notify

:::ui Microsoft Defender · Sentinel · Automation
> Microsoft Sentinel › Configuration › Automation › Create › Automation rule
= Name: Emergency accounts → security
= Trigger: When incident is created
= Conditions: Analytics rule name contains "emergency account"
= Actions: Assign owner: on-call security team · Change severity: High · Add tag: breakglass
= Action: Run playbook: pb-notify-teams (posts the incident to the security channel)
[Apply]
:::

The **playbook** is an Azure Logic App: it receives the incident and posts to Teams with the link. Automation rules organise the work; playbooks do things outside Sentinel (notify, disable an account, open a ticket in Jira Service Management).

## 4. An incident from start to finish

Monday, 07:12. The security channel receives: *Emergency account brk-admin-02 from 198.51.100.23*.

1. **Open the incident** (*Investigation & response › Incidents & alerts › Incidents*): see the alert, the entities (account and IP) and the timeline.
2. **Was it a planned change?** The change log says no emergency account test is scheduled this week.
3. **What did that IP do?**

:::term Advanced hunting · the incident's IP
$ SigninLogs
$ | where TimeGenerated > ago(24h) and IPAddress == "198.51.100.23"
$ | summarize Users = dcount(UserPrincipalName), Failures = countif(ResultType != "0"), Successes = countif(ResultType == "0") by bin(TimeGenerated, 1h)
TimeGenerated         Users   Failures   Successes
27/10/2026 05:00      143     141        0
27/10/2026 06:00      211     208        1
27/10/2026 07:00      1       0          1
:::

Many different users, almost all failures and one hit: a **password spray** attack that guessed an emergency account's password.

4. **Contain**: disable the account, revoke its sessions (`Revoke-MgUserSignInSession`), change the password, block the IP with a Conditional Access named location, and review in *AuditLogs* what the account did in those minutes.
5. **Classify and close**: *True positive — suspicious activity*, with a comment on what was done and the pending actions (why the emergency account could sign in with only a password).

The classification is not bureaucracy: incidents closed as *False positive* tell you which rules need tuning, and *Benign* ones (suspicious but expected activity, such as a planned test) which exceptions are missing.

## 5. The cost

:::term Advanced hunting · what ingests most
$ Usage
$ | where TimeGenerated > ago(30d) and IsBillable == true
$ | summarize GB = round(sum(Quantity) / 1000, 1) by DataType
$ | sort by GB desc
DataType                          GB
SecurityEvent                     412.6
AADNonInteractiveUserSignInLogs   188.3
SigninLogs                        41.2
Syslog                            19.8
:::

- `SecurityEvent` at the top is usually an event set that is too broad or a noisy server: adjust the collection rule.
- Tables that are only queried during an investigation can go to the **Basic** or **Auxiliary** plan, much cheaper, in exchange for more limited queries.
- With a steady volume, a daily **commitment tier** lowers the price per GB.

## 6. What you review each month

- Rules that haven't raised an incident in 90 days (is the data they look at still arriving?) and rules that raise so many that nobody reads them.
- Connector and rule health: the `SentinelHealth` table and each connector's page say when data stopped arriving.
- Mean time to assign and to close high-severity incidents.
- The ingestion bill against the previous month, per table.

## Next steps

- The **rule templates** in each Content hub solution: enable, test and tune them instead of writing from scratch.
- **UEBA** (user and entity behaviour analytics): it detects what is unusual for each user, not what is unusual in general.
- **Threat intelligence**: IP and domain indicators matched against your logs.
- The alert for deleted backups or changed immutability from the DR/BCP guide, as your second rule of your own.
""")

# ---------------------------------------------------------------- L4 · Microsoft 365 tenant migrations
g(slug="migracion-de-tenant-microsoft-365-inventario-identidades-buzones-onedrive-y-dia-del-corte", topic="tenant-migration", date="2026-10-27",
  title_es="Migraciones de tenant de Microsoft 365: inventario, identidades, buzones, OneDrive y el día del corte",
  title_en="Microsoft 365 tenant migrations: inventory, identities, mailboxes, OneDrive and cutover day",
  dek_es="Fusiones, escisiones y cambios de dominio: qué se mueve y qué se rehace, el inventario que evita sorpresas, la migración de buzones entre tenants sin respuestas que rebotan, OneDrive, los dispositivos, y el runbook del fin de semana del corte con su semana de soporte posterior.",
  dek_en="Mergers, divestitures and domain changes: what moves and what gets rebuilt, the inventory that avoids surprises, cross-tenant mailbox migration without bouncing replies, OneDrive, the devices, and the runbook for the cutover weekend with the week of support after it.",
  es="""
## Qué vas a conseguir

Llevar los usuarios, el correo y los archivos de una empresa de un tenant de Microsoft 365 a otro con un fin de semana de corte y un lunes tranquilo. Saber desde el principio qué se migra con herramientas, qué hay que rehacer a mano y qué no se puede mover, para que nadie se entere el lunes.

## Antes de empezar

- El escenario claro: **fusión** (dos tenants pasan a uno), **escisión** (una parte de la empresa sale a un tenant nuevo, normalmente con un acuerdo de servicios transitorios, TSA, que fija hasta cuándo el origen da servicio) o **cambio de marca** (el dominio cambia de tenant).
- Roles administrativos en los dos tenants, activados por PIM (guía de Global Admin y PIM).
- Las herramientas: la migración nativa de buzones y de OneDrive entre tenants necesita una licencia **Cross-Tenant User Data Migration** por usuario migrado; la alternativa son herramientas de terceros (para correo, OneDrive, SharePoint y Teams) con su propio coste.
- El repo 29 del portfolio, *Tenant Separation Cutover Planner*, sirve de plantilla para el plan del corte y sus dependencias.

## 1. El inventario

Todo lo que no está en el inventario aparece el lunes como ticket.

:::term PowerShell · tenant de origen
$ Connect-ExchangeOnline
$ Get-EXOMailbox -ResultSize Unlimited -Properties RecipientTypeDetails | Group-Object RecipientTypeDetails | Select-Object Name, Count
$ Get-EXOMailbox -ResultSize Unlimited | Get-EXOMailboxStatistics | Sort-Object TotalItemSize -Descending | Select-Object -First 5 DisplayName, TotalItemSize, ItemCount
Name                  Count
----                  -----
UserMailbox           412
SharedMailbox         37
RoomMailbox           18
EquipmentMailbox      3
DisplayName           TotalItemSize                      ItemCount
-----------           -------------                      ---------
Carlos Martín         48.71 GB (52,302,131,200 bytes)    398112
Facturación           31.02 GB (33,307,705,344 bytes)    521007
:::

| Elemento | Cómo se mueve |
|---|---|
| Usuarios y grupos | Se crean en el destino (o los sincroniza Entra Connect del destino) |
| Buzones de usuario, compartidos y archivos | Migración entre tenants (nativa o herramienta) |
| OneDrive | Migración entre tenants (nativa o herramienta) |
| Sitios de SharePoint y archivos de Teams | Herramienta de migración, sitio a sitio |
| Chats de Teams | No se mueven de forma nativa: se avisa y se exportan si hace falta por cumplimiento |
| Aplicaciones con SSO | Se dan de alta otra vez en el destino (guía de Entra ID SSO) |
| Dispositivos | No se mueven: se restablecen y se inscriben en el destino |
| Licencias, Conditional Access, Intune | Se rehacen en el destino antes del corte |
| Dominio de correo | Se mueve el día del corte (solo puede estar en un tenant) |

## 2. Las identidades en el destino

- Cada usuario existe en el destino **antes** del corte, con un UPN provisional en el dominio `onmicrosoft.com` del destino (el dominio de verdad aún está en el origen).
- Un CSV de correspondencias es la columna vertebral de todo el proyecto: `SourceUPN,TargetUPN,FinalUPN`. Lo usan los scripts de buzones, de OneDrive, de licencias y de UPN final.
- Los usuarios tendrán que registrar MFA otra vez en el tenant destino: se prepara la comunicación y, si se puede, se usan **Temporary Access Pass** el lunes para que el primer inicio de sesión sea sencillo.

## 3. Los buzones entre tenants

Las piezas de la migración nativa: una aplicación de migración en el tenant destino con consentimiento del origen, una **relación de organización** en cada tenant que permite mover buzones, y un **punto de conexión de migración** en el destino.

En el destino, cada usuario es primero un **usuario de correo** (MailUser) que se convierte en buzón al migrar. Tres atributos tienen que coincidir con el origen:

:::term PowerShell · tenant destino (un usuario; en la práctica, desde el CSV)
$ Set-MailUser -Identity "laura.prado" -ExchangeGuid "4f1d2a9c-0b3e-4c8e-9a51-7c2d1e6b3f10" -ArchiveGuid "9b7e3c21-5d4a-4e0f-8c6b-2a1f9d0e7c45"
$ Set-MailUser -Identity "laura.prado" -EmailAddresses @{ add = "x500:/o=ExchangeLabs/ou=Exchange Administrative Group (FYDIBOHF23SPDLT)/cn=Recipients/cn=7a1c0e5b9d2f4c3a8e6b1d0f2a9c4e7b-laura.prado" }
:::

- `ExchangeGuid` y `ArchiveGuid` iguales a los del buzón de origen: sin ellos, la migración no encuentra destino.
- La dirección **x500** con el `LegacyExchangeDN` del origen: sin ella, responder a un correo antiguo o a una convocatoria vieja rebota con un error `IMCEAEX`. Es el fallo que más tickets genera tras una migración.

:::term PowerShell · tenant destino · lotes
$ New-MigrationBatch -Name "ola1-finanzas" -SourceEndpoint "ep-origen" -CSVData ([System.IO.File]::ReadAllBytes("C:\\mig\\ola1.csv")) -TargetDeliveryDomain "fabrikam.onmicrosoft.com" -Autostart
$ Get-MigrationUser -BatchId "ola1-finanzas" | Get-MigrationUserStatistics | Format-Table Identity, Status, SyncedItemCount, SkippedItemCount
Identity                     Status    SyncedItemCount   SkippedItemCount
--------                     ------    ---------------   ----------------
laura.prado@fabrikam.com     Synced    84211             0
carlos.martin@fabrikam.com   Syncing   301455            12
:::

Los lotes se crean y sincronizan **semanas antes** del corte: copian casi todo y se quedan en *Synced*, actualizándose. El día del corte solo se completa el último incremento, que tarda minutos y no días. Los elementos omitidos (*SkippedItemCount*) se revisan antes, no el lunes.

## 4. OneDrive, SharePoint y Teams

- **OneDrive**: la migración nativa entre tenants (`Start-SPOCrossTenantUserContentMove` en SharePoint Online PowerShell, tras confiar los dos tenants) mueve el OneDrive completo y deja una redirección en el origen. Con herramientas de terceros, el modelo es el mismo: copia previa y delta el fin de semana.
- **SharePoint y Teams**: sitio a sitio con la herramienta de migración, con los propietarios de cada sitio validando antes del corte qué se lleva y qué se archiva.
- Los **chats de Teams** no viajan: se avisa con tiempo para que lo importante se guarde en un canal o un documento.

## 5. El fin de semana del corte

:::ui Runbook · corte del viernes 06/11/2026
> Proyecto › Migración de tenant › RB-CORTE
= Martes T-3: TTL de los registros MX, autodiscover y SPF bajado a 5 minutos
= Viernes 18:00: congelación de cambios · aviso a usuarios: cerrar Outlook y Teams al salir
= Viernes 19:00: quitar el dominio de todos los objetos del origen (UPN, direcciones proxy, grupos) y eliminarlo del tenant origen
= Viernes 20:00: verificar el dominio en el destino (registro TXT), asignar UPN finales desde el CSV
= Viernes 21:00: completar los lotes de buzones y el último delta de OneDrive
= Sábado 09:00: MX, autodiscover, SPF, DKIM y DMARC apuntando al destino; prueba de correo entrante y saliente
= Sábado 11:00: aplicaciones SSO apuntando al destino; Conditional Access e Intune activos
= Domingo: pruebas de un grupo piloto de cada área con su lista de comprobaciones
= Lunes 07:30: soporte en las sedes y canal de incidencias abierto
:::

El dominio no puede estar en dos tenants a la vez, y Entra ID no te deja quitarlo del origen mientras algún objeto lo use. Encontrarlos lleva tiempo; se ensaya antes con un script:

:::term PowerShell · tenant de origen · ¿quién usa aún el dominio?
$ Get-Recipient -ResultSize Unlimited | Where-Object { $_.EmailAddresses -match "@fabrikam\\.com" } | Select-Object Name, RecipientTypeDetails
:::

**Dispositivos**: los equipos unidos a Entra ID y gestionados por Intune no se pueden mover entre tenants. Se borra su registro de Autopilot en el origen, se importa el hash en el destino y se restablecen (en el corte o por olas, con los datos ya en OneDrive). Los equipos unidos a un AD local se vuelven a unir al dominio del destino.

## 6. La semana de hipercuidado

- **Rebotes**: seguimiento de mensajes en el destino buscando `550 5.1.1` e `IMCEAEX`; cada uno suele ser una x500 que falta.
- **MFA y primer inicio de sesión**: el pico de llamadas del lunes. Los Temporary Access Pass y una guía de una página con capturas reducen la cola.
- **Outlook**: perfiles que hay que volver a crear y buzones compartidos que no aparecen (los permisos se vuelven a aplicar en el destino desde el inventario).
- Un **parte diario** a dirección: incidencias abiertas, cerradas y las que requieren decisión.
- Al cerrar el TSA: retirar licencias y cerrar el tenant de origen (o la parte que corresponda) con copia de lo que haya que conservar por cumplimiento.

## Siguientes pasos

- Si los tenants van a convivir, **sincronización entre tenants** y la **organización multiinquilino** de Microsoft 365: los usuarios se ven en el directorio y en Teams sin migrar nada.
- **Acceso B2B** durante el TSA: que los usuarios ya migrados entren como invitados a lo que aún vive en el origen.
- La guía de Azure AD Connect del Nivel 2: en una migración híbrida es la pieza que se desmonta en el origen y se monta en el destino.
""",
  en="""
## What you'll get

Moving a company's users, mail and files from one Microsoft 365 tenant to another with a single cutover weekend and a quiet Monday. Knowing from the start what is migrated with tools, what has to be rebuilt by hand and what cannot be moved, so nobody finds out on Monday.

## Before you start

- A clear scenario: **merger** (two tenants become one), **divestiture** (part of the company moves to a new tenant, usually with a transitional services agreement, TSA, that sets how long the source keeps providing service) or **rebrand** (the domain changes tenant).
- Admin roles in both tenants, activated through PIM (Global Admin and PIM guide).
- The tools: native cross-tenant mailbox and OneDrive migration needs a **Cross-Tenant User Data Migration** licence per migrated user; the alternative is third-party tools (for mail, OneDrive, SharePoint and Teams) with their own cost.
- Repo 29 in the portfolio, *Tenant Separation Cutover Planner*, works as a template for the cutover plan and its dependencies.

## 1. The inventory

Everything that isn't in the inventory turns up on Monday as a ticket.

:::term PowerShell · source tenant
$ Connect-ExchangeOnline
$ Get-EXOMailbox -ResultSize Unlimited -Properties RecipientTypeDetails | Group-Object RecipientTypeDetails | Select-Object Name, Count
$ Get-EXOMailbox -ResultSize Unlimited | Get-EXOMailboxStatistics | Sort-Object TotalItemSize -Descending | Select-Object -First 5 DisplayName, TotalItemSize, ItemCount
Name                  Count
----                  -----
UserMailbox           412
SharedMailbox         37
RoomMailbox           18
EquipmentMailbox      3
DisplayName           TotalItemSize                      ItemCount
-----------           -------------                      ---------
Carlos Martín         48.71 GB (52,302,131,200 bytes)    398112
Invoicing             31.02 GB (33,307,705,344 bytes)    521007
:::

| Item | How it moves |
|---|---|
| Users and groups | Created in the target (or synchronised by the target's Entra Connect) |
| User and shared mailboxes, archives | Cross-tenant migration (native or a tool) |
| OneDrive | Cross-tenant migration (native or a tool) |
| SharePoint sites and Teams files | Migration tool, site by site |
| Teams chats | Not moved natively: users are warned and they are exported if compliance requires it |
| Apps with SSO | Onboarded again in the target (Entra ID SSO guide) |
| Devices | Not moved: reset and enrolled in the target |
| Licences, Conditional Access, Intune | Rebuilt in the target before the cutover |
| Mail domain | Moved on cutover day (it can only live in one tenant) |

## 2. Identities in the target

- Every user exists in the target **before** the cutover, with a temporary UPN on the target's `onmicrosoft.com` domain (the real domain is still in the source).
- A mapping CSV is the backbone of the whole project: `SourceUPN,TargetUPN,FinalUPN`. The mailbox, OneDrive, licence and final-UPN scripts all use it.
- Users will have to register MFA again in the target tenant: prepare the communication and, where possible, use **Temporary Access Pass** on Monday so the first sign-in is simple.

## 3. Cross-tenant mailboxes

The pieces of the native migration: a migration application in the target tenant with consent from the source, an **organization relationship** in each tenant that allows mailbox moves, and a **migration endpoint** in the target.

In the target, each user starts as a **mail user** (MailUser) that becomes a mailbox when migrated. Three attributes must match the source:

:::term PowerShell · target tenant (one user; in practice, from the CSV)
$ Set-MailUser -Identity "laura.prado" -ExchangeGuid "4f1d2a9c-0b3e-4c8e-9a51-7c2d1e6b3f10" -ArchiveGuid "9b7e3c21-5d4a-4e0f-8c6b-2a1f9d0e7c45"
$ Set-MailUser -Identity "laura.prado" -EmailAddresses @{ add = "x500:/o=ExchangeLabs/ou=Exchange Administrative Group (FYDIBOHF23SPDLT)/cn=Recipients/cn=7a1c0e5b9d2f4c3a8e6b1d0f2a9c4e7b-laura.prado" }
:::

- `ExchangeGuid` and `ArchiveGuid` equal to the source mailbox's: without them, the migration finds no target.
- The **x500** address with the source `LegacyExchangeDN`: without it, replying to an old email or an old meeting invite bounces with an `IMCEAEX` error. It is the failure that generates most tickets after a migration.

:::term PowerShell · target tenant · batches
$ New-MigrationBatch -Name "wave1-finance" -SourceEndpoint "ep-source" -CSVData ([System.IO.File]::ReadAllBytes("C:\\mig\\wave1.csv")) -TargetDeliveryDomain "fabrikam.onmicrosoft.com" -Autostart
$ Get-MigrationUser -BatchId "wave1-finance" | Get-MigrationUserStatistics | Format-Table Identity, Status, SyncedItemCount, SkippedItemCount
Identity                     Status    SyncedItemCount   SkippedItemCount
--------                     ------    ---------------   ----------------
laura.prado@fabrikam.com     Synced    84211             0
carlos.martin@fabrikam.com   Syncing   301455            12
:::

Batches are created and synchronised **weeks before** the cutover: they copy almost everything and stay in *Synced*, keeping up to date. On cutover day only the last increment is completed, which takes minutes rather than days. Skipped items (*SkippedItemCount*) are reviewed beforehand, not on Monday.

## 4. OneDrive, SharePoint and Teams

- **OneDrive**: native cross-tenant migration (`Start-SPOCrossTenantUserContentMove` in SharePoint Online PowerShell, once the two tenants trust each other) moves the whole OneDrive and leaves a redirect in the source. With third-party tools the model is the same: a pre-copy and a delta over the weekend.
- **SharePoint and Teams**: site by site with the migration tool, with each site's owners validating before the cutover what is taken and what is archived.
- **Teams chats** don't travel: users are warned early so anything important is saved to a channel or a document.

## 5. The cutover weekend

:::ui Runbook · cutover Friday 06/11/2026
> Project › Tenant migration › RB-CUTOVER
= Tuesday T-3: TTL of the MX, autodiscover and SPF records lowered to 5 minutes
= Friday 18:00: change freeze · user notice: close Outlook and Teams when leaving
= Friday 19:00: remove the domain from every object in the source (UPNs, proxy addresses, groups) and delete it from the source tenant
= Friday 20:00: verify the domain in the target (TXT record), set final UPNs from the CSV
= Friday 21:00: complete the mailbox batches and the last OneDrive delta
= Saturday 09:00: MX, autodiscover, SPF, DKIM and DMARC pointing at the target; inbound and outbound mail test
= Saturday 11:00: SSO apps pointing at the target; Conditional Access and Intune active
= Sunday: tests by a pilot group from each area with their checklist
= Monday 07:30: on-site support and incident channel open
:::

The domain can't live in two tenants at once, and Entra ID won't let you remove it from the source while any object still uses it. Finding them takes time; rehearse it beforehand with a script:

:::term PowerShell · source tenant · who still uses the domain?
$ Get-Recipient -ResultSize Unlimited | Where-Object { $_.EmailAddresses -match "@fabrikam\\.com" } | Select-Object Name, RecipientTypeDetails
:::

**Devices**: devices joined to Entra ID and managed by Intune can't be moved between tenants. Their Autopilot registration is deleted in the source, the hash is imported into the target and they are reset (at cutover or in waves, with the data already in OneDrive). Devices joined to an on-premises AD are re-joined to the target's domain.

## 6. The hypercare week

- **Bounces**: message trace in the target looking for `550 5.1.1` and `IMCEAEX`; each one is usually a missing x500.
- **MFA and first sign-in**: Monday's call peak. Temporary Access Pass and a one-page guide with screenshots shorten the queue.
- **Outlook**: profiles that need recreating and shared mailboxes that don't appear (permissions are re-applied in the target from the inventory).
- A **daily report** to management: incidents open, closed and those that need a decision.
- When the TSA ends: remove licences and close the source tenant (or the relevant part) with a copy of whatever must be kept for compliance.

## Next steps

- If the tenants will live side by side, **cross-tenant synchronisation** and Microsoft 365's **multitenant organization**: users see each other in the directory and in Teams without migrating anything.
- **B2B access** during the TSA: users already migrated sign in as guests to whatever still lives in the source.
- The Level 2 Azure AD Connect guide: in a hybrid migration it is the piece taken apart in the source and rebuilt in the target.
""")
