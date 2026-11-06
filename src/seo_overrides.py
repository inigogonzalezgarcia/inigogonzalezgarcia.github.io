"""Hand-written meta descriptions for the pages with the most Search Console impressions. Applied when pages.py is imported.

Without these, build.py uses seo_desc or dek_en for English and desc_cut(dek_es) for Spanish, which can stop mid-sentence
and leave out the words people search for. Keep each one at 160 characters or fewer (checked below).
Posts are keyed by repo, guides by slug. "en" fills seo_desc, "es" fills seo_desc_es."""

POSTS_SEO = {
    "02-intune-compliance-report": {
        "en": "Intune compliance report with Microsoft Graph: PowerShell pulls the devices, Python turns them into a report for managers and an action list.",
        "es": "Informe de cumplimiento de Intune con Microsoft Graph: PowerShell saca los dispositivos y Python genera un informe para dirección y una lista de acciones.",
    },
    "05-it-ops-console": {
        "en": "On-site IT operations console in Flask and PowerShell: assets, warranties, room checklists, joiners and leavers, shifts and service health in one app.",
        "es": "Consola de operaciones IT de sede en Flask y PowerShell: activos, garantías, checklists de salas, altas y bajas, turnos y salud de servicios en una app.",
    },
    "09-gpu-node-remediation": {
        "en": "Kubernetes controller for GPU nodes: XID errors, ECC and temperature move each node through a state machine to drain, repair or quarantine it.",
        "es": "Controlador de Kubernetes para nodos GPU: los XID, el ECC y la temperatura llevan cada nodo por una máquina de estados para drenarlo, repararlo o aislarlo.",
    },
    "12-gpu-goodput-mtbi": {
        "en": "GPU goodput and MTBI simulator: a 1,024-GPU training job with failures, to see what checkpoints, spares and fast detection are worth.",
        "es": "Simulador de goodput y MTBI en GPU: un entrenamiento de 1.024 GPU con fallos para ver cuánto valen los checkpoints, los spares y la detección rápida.",
    },
    "19-ad-infra-health-check": {
        "es": "Chequeo de salud de Active Directory con PowerShell: controladores de dominio, replicación, DHCP, GPO y cuentas de administrador, por prioridad.",
    },
    "20-entra-sso-app-audit": {
        "en": "Entra ID SSO audit: SAML certificates and secrets about to expire, app owners, MFA coverage, risky permissions and SCIM across enterprise apps.",
        "es": "Auditoría SSO de Entra ID: certificados SAML y secretos a punto de caducar, propietarios, cobertura de MFA, permisos de riesgo y SCIM.",
    },
    "22-dex-experience-score": {
        "es": "Puntuación DEX: convierte la telemetría de los equipos en una nota de 0 a 10 por dispositivo, sede y departamento y ordena los arreglos que más la suben.",
    },
}

GUIDES_SEO = {
    "hotel-en-pre-apertura-checklist-de-it-hasta-el-dia-de-apertura": {
        "es": "Checklist IT para la pre-apertura de un hotel: calendario desde la apertura, red por usos, circuitos, interfaces con el PMS, pruebas de check-in y soporte.",
    },
    "mecm-sccm-empaquetar-una-aplicacion-y-desplegarla": {
        "en": "MECM / SCCM application model step by step: silent install, detection method, content distribution, deployment and the client logs that tell the truth.",
        "es": "MECM / SCCM paso a paso: instalación silenciosa, método de detección, distribución de contenido, despliegue y los logs del cliente que dicen la verdad.",
    },
    "keycloak-sso-realm-clientes-oidc-y-saml-active-directory-por-ldap-mfa-e-invalid-redirect-uri": {
        "es": "Keycloak 26 para SSO interno: producción tras un proxy, realm, clientes OIDC y SAML, Active Directory por LDAP, roles, OTP e invalid_redirect_uri.",
    },
    "jamf-pro-enrolar-un-mac-y-desplegar-una-politica": {
        "en": "Jamf Pro step by step: automated or user-initiated Mac enrolment, inventory, a smart group and a policy that installs and configures, plus daily commands.",
        "es": "Jamf Pro paso a paso: enrolar un Mac (automatizado o por el usuario), inventario, un grupo inteligente y una política que instala y configura.",
    },
    "veeam-crear-un-job-comprobar-copias-y-restaurar": {
        "en": "Veeam Backup step by step: repository, backup job with retention, the warnings not to ignore, and restoring a file and a whole machine.",
        "es": "Veeam Backup paso a paso: repositorio, trabajo de copia con retención, los avisos que no hay que ignorar y la restauración de un fichero y de una máquina.",
    },
    "teams-rooms-poner-en-marcha-una-sala": {
        "en": "Microsoft Teams Rooms setup: resource account, licence, device sign-in, peripherals, the Pro Management Portal and typical Monday-morning room failures.",
        "es": "Microsoft Teams Rooms: cuenta de recurso, licencia, inicio de sesión del dispositivo, periféricos, Pro Management Portal y los fallos típicos de una sala.",
    },
}

KEYS = {"en": "seo_desc", "es": "seo_desc_es"}


def apply():
    from posts import POSTS
    from guides import GUIDES
    for items, field, table in ((POSTS, "repo", POSTS_SEO), (GUIDES, "slug", GUIDES_SEO)):
        by_key = {x[field]: x for x in items}
        for key, descs in table.items():
            assert key in by_key, f"seo_overrides: unknown {field} {key}"
            for lang, text in descs.items():
                assert len(text) <= 160, f"seo_overrides: {key} ({lang}) is {len(text)} characters"
                by_key[key][KEYS[lang]] = text
