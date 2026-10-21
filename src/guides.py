"""IT guides (guias/). Level 1 topics and the guides under each one. Text in a small markup rendered by gmd() in build.py:
## / ### headings, - lists, 1. numbered steps, > tip, ! warning, **bold**, `code`, and two blocks:
:::term Title       a simulated terminal: lines starting with "$ " are commands (copied by the button), "# " are comments, the rest is output
:::ui Title         a simulated window: lines starting with "> " are a navigation path, "[ ]" / "[x]" are options, the rest is text
Both end with ":::". No real hostnames, users, tenants or company names: every example is fictional."""

LEVEL1 = dict(key="nivel-1", n_es="Nivel 1", n_en="Level 1", t_es="Primeros pasos", t_en="First steps",
              d_es="Lo que necesitas para empezar en soporte: el puesto, el usuario y sus herramientas.",
              d_en="What you need to start in support: the device, the user and their tools.")

# key, name_es, name_en, one-line description es/en
TOPICS = [
    ("active-directory", "Active Directory: usuarios y grupos", "Active Directory: users and groups",
     "Altas, bajas, grupos y las incidencias de cada día: cuentas bloqueadas y contraseñas.",
     "Joiners, leavers, groups and the everyday tickets: locked accounts and passwords."),
    ("android", "Android", "Android",
     "Móviles corporativos y perfil de trabajo con Intune.",
     "Corporate phones and the work profile with Intune."),
    ("bitlocker", "BitLocker", "BitLocker",
     "Cifrado del disco, claves de recuperación y qué hacer cuando un equipo pide la clave.",
     "Disk encryption, recovery keys and what to do when a device asks for one."),
    ("anyconnect", "Cisco AnyConnect (VPN)", "Cisco AnyConnect (VPN)",
     "Instalar el cliente, conectar y diagnosticar los fallos más habituales.",
     "Install the client, connect and diagnose the usual failures."),
    ("impresoras", "Impresoras y periféricos", "Printers and peripherals",
     "Instalar una impresora de red, colas atascadas y periféricos que no responden.",
     "Install a network printer, stuck queues and peripherals that stop responding."),
    ("ios", "iPhone y iPad", "iPhone and iPad",
     "Enrolar un dispositivo Apple en Intune y comprobar que recibe las políticas.",
     "Enrol an Apple device in Intune and check that it receives its policies."),
    ("jira", "Jira Service Management: tickets", "Jira Service Management: tickets",
     "Abrir, clasificar, trabajar y cerrar un ticket de forma que ayude al siguiente.",
     "Open, classify, work and close a ticket in a way that helps the next person."),
    ("m365", "Microsoft 365 y licencias", "Microsoft 365 and licences",
     "Asignar y retirar licencias, y saber qué incluye cada una.",
     "Assign and remove licences, and know what each one includes."),
    ("teams", "Microsoft Teams", "Microsoft Teams",
     "Los problemas que más llegan al service desk y cómo resolverlos en minutos.",
     "The issues that reach the service desk most often, and how to fix them in minutes."),
    ("outlook", "Outlook y Exchange Online", "Outlook and Exchange Online",
     "Buzones compartidos, permisos, respuestas automáticas y perfiles que no abren.",
     "Shared mailboxes, permissions, automatic replies and profiles that won't open."),
    ("windows", "Windows 10 y 11", "Windows 10 and 11",
     "Diagnóstico básico de un equipo: lento, con errores o que no sincroniza con Intune.",
     "Basic diagnosis of a device: slow, throwing errors or not syncing with Intune."),
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
