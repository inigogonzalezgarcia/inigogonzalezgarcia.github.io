"""Legal pages (legal notice, terms). Same shell as the hand-written privacidad.html. Imported by build.py."""
import base64
from pages import MAIL, SEC_HEAD

UPDATED_ES = "18 de octubre de 2026"
UPDATED_EN = "18 October 2026"
SITE = "https://inigogonzalezgarcia.github.io"
def mail_tag(addr=MAIL, link=True):
    """Email shown without the address in the HTML (against harvesting bots). assets/legal.js turns it into a mailto link;
    without JavaScript the reader sees "user [at] domain [dot] tld"."""
    user, dom = addr.split("@")
    enc = base64.b64encode(addr[::-1].encode()).decode()
    return f'<span class="eml" data-e="{enc}"{"" if link else " data-plain"}>{user} [at] {dom.replace(".", " [dot] ")}</span>'

M = mail_tag()
MT = mail_tag(link=False)  # same address shown as plain text, where the page had no link

def shell(*, path, title_es, title_en, desc, es, en):
    return f'''<!doctype html>
<html lang="en" data-title-es="{title_es} · Iñigo González" data-title-en="{title_en} · Iñigo González">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
{SEC_HEAD}
<title>{title_es} · Iñigo González</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0e1a24">
<meta name="robots" content="noindex">
<link rel="canonical" href="{SITE}/{path}">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/style.css">
<script src="assets/boot.js"></script>
</head>
<body>
<header class="site-header solid">
  <div class="wrap">
    <a class="brand" href="./" aria-label="Iñigo González">
      <svg class="brand-mark" viewBox="0 0 34 34" aria-hidden="true"><rect x="1" y="1" width="32" height="32" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 9v16M17 9v16M17 9h7M17 17h5M24 17v8h-7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="square"/><circle cx="10" cy="9" r="2.2" fill="#c4672b"/></svg>
      <span class="brand-name">Iñigo González<small>IT Operations · Infra</small></span>
    </a>
    <div class="head-actions">
      <a class="menu-btn u-nounder" href="./"><span class="es">← Volver</span><span class="en">← Back</span></a>
      <span class="sep" aria-hidden="true"></span>
      <button class="lang-btn" id="langBtn" aria-label="Cambiar idioma / Change language"><span data-l="es">ES</span> · <span data-l="en">EN</span></button>
    </div>
  </div>
</header>

<main class="policy">
  <div class="wrap">

<!-- ===================== ES ===================== -->
<div class="es">
{es}
</div>

<!-- ===================== EN ===================== -->
<div class="en">
{en}
</div>

  </div>
</main>

<footer>
  <div class="wrap">
    <span>© 2026 Iñigo González · Madrid</span>
    <span><a href="aviso-legal.html"><span class="es">Aviso legal</span><span class="en">Legal notice</span></a> · <a href="privacidad.html"><span class="es">Privacidad y cookies</span><span class="en">Privacy and cookies</span></a> · <a href="condiciones.html"><span class="es">Condiciones</span><span class="en">Terms</span></a> · <a href="recursos.html">Newsletter</a> · <span class="es">SysAdmin Desks: <a href="https://sysadmindesksbyigg.pages.dev/about?lang=es" target="_blank" rel="noopener noreferrer">qué es</a> · <a href="https://sysadmindesksbyigg.pages.dev/faq?lang=es" target="_blank" rel="noopener noreferrer">preguntas frecuentes</a></span><span class="en">SysAdmin Desks: <a href="https://sysadmindesksbyigg.pages.dev/about?lang=en" target="_blank" rel="noopener noreferrer">about</a> · <a href="https://sysadmindesksbyigg.pages.dev/faq?lang=en" target="_blank" rel="noopener noreferrer">FAQ</a></span></span>
    <a href="./"><span class="es">Volver a la web</span><span class="en">Back to the site</span></a>
  </div>
</footer>

<script src="assets/data.js"></script>
<script src="assets/legal.js"></script>
<script src="assets/consent.js"></script>
</body>
</html>
'''

# ------------------------------------------------------------------ legal notice
AVISO_ES = f'''  <p class="label kicker">Aviso legal · Última actualización: {UPDATED_ES}</p>
  <h1>Aviso legal</h1>
  <p class="lede">Quién está detrás de esta web y en qué condiciones puedes usarla.</p>

  <h2>1. Titular de la web</h2>
  <ul>
    <li><strong>Titular:</strong> Iñigo González, Madrid (España).</li>
    <li><strong>Email:</strong> {M}.</li>
    <li><strong>Web:</strong> {SITE}</li>
    <li><strong>Actividad:</strong> web personal y profesional. Publica mi trayectoria, artículos sobre tecnología y carrera en IT y el catálogo de servicios de asesoría profesional <em>IGG-ICS · IT · Tech Career, Lab &amp; Strategy</em>.</li>
  </ul>
  <p class="note">Desde esta web se puede reservar la sesión inicial de orientación profesional, que se paga por adelantado con un enlace de pago enviado por email. Las condiciones están en <a href="condiciones.html">condiciones de contratación</a>.</p>

  <h2>2. Objeto</h2>
  <p>Este aviso regula el uso de la web. Al navegar por ella aceptas estas condiciones. Si no estás de acuerdo, no la uses.</p>

  <h2>3. Condiciones de uso</h2>
  <p>Te comprometes a usar la web y sus formularios de forma lícita y de buena fe: sin enviar contenido falso u ofensivo ni spam, y sin intentar dañar la web, sobrecargarla o afectar a otras personas.</p>

  <h2>4. Propiedad intelectual</h2>
  <p>Los textos, guías, plantillas, imágenes propias y el diseño de la web son de mi autoría, salvo que se indique lo contrario. Puedes compartir enlaces y citar fragmentos breves indicando la fuente. Para cualquier otro uso, como copiarlos, venderlos o publicarlos en otro sitio, necesitas mi permiso por escrito. El código de los repositorios públicos de GitHub se rige por la licencia que indica cada uno.</p>

  <h2>5. Contenidos y responsabilidad</h2>
  <p>Los contenidos son informativos y se basan en mi experiencia personal. No garantizan ningún resultado, como conseguir un empleo o un ascenso. Intento que la información sea correcta y esté al día, pero no puedo garantizar que lo esté siempre ni que la web funcione sin interrupciones.</p>

  <h2>6. Enlaces externos</h2>
  <p>La web enlaza a sitios de terceros, como LinkedIn o GitHub. No controlo su contenido ni respondo de él. Cada uno tiene sus propias condiciones y su política de privacidad.</p>

  <h2>7. Servicios</h2>
  <p>Los servicios de la <a href="store.html">Store</a> se rigen por las <a href="condiciones.html">condiciones de contratación</a>.</p>

  <h2>8. Datos personales y cookies</h2>
  <p>Cómo trato tus datos y qué cookies uso se explica en la <a href="privacidad.html">política de privacidad y cookies</a>.</p>

  <h2>9. Ley aplicable</h2>
  <p>Este aviso se rige por la ley española. Si eres consumidor, son competentes los juzgados de tu domicilio. En los demás casos, los de Madrid.</p>'''

AVISO_EN = f'''  <p class="label kicker">Legal notice · Last updated: {UPDATED_EN}</p>
  <h1>Legal notice</h1>
  <p class="lede">Who is behind this site and the terms for using it.</p>

  <h2>1. Site owner</h2>
  <ul>
    <li><strong>Owner:</strong> Iñigo González, Madrid (Spain).</li>
    <li><strong>Email:</strong> {M}.</li>
    <li><strong>Website:</strong> {SITE}</li>
    <li><strong>Activity:</strong> a personal and professional website. It publishes my career path, articles on technology and IT careers, and the catalogue of career advisory services <em>IGG-ICS · IT · Tech Career, Lab &amp; Strategy</em>.</li>
  </ul>
  <p class="note">The initial career session can be booked through this site and is paid in advance through a payment link sent by email. The terms are in the <a href="condiciones.html">terms of service</a>.</p>

  <h2>2. Purpose</h2>
  <p>This notice governs the use of the site. By browsing it you accept these terms. If you don't agree, please don't use it.</p>

  <h2>3. Terms of use</h2>
  <p>You agree to use the site and its forms lawfully and in good faith: no false or offensive content, no spam, and no attempts to damage or overload the site or affect other people.</p>

  <h2>4. Intellectual property</h2>
  <p>The texts, guides, templates, my own images and the design of the site are my work unless stated otherwise. You may share links and quote short extracts with credit. Any other use, such as copying, selling or republishing them, needs my written permission. Code in public GitHub repositories is covered by the licence stated in each one.</p>

  <h2>5. Content and liability</h2>
  <p>The content is informative and based on my personal experience. It does not guarantee any outcome, such as getting a job or a promotion. I try to keep the information accurate and up to date, but I can't guarantee that it always is, or that the site runs without interruptions.</p>

  <h2>6. External links</h2>
  <p>The site links to third-party sites such as LinkedIn or GitHub. I don't control their content and I'm not responsible for it. Each has its own terms and privacy policy.</p>

  <h2>7. Services</h2>
  <p>The services in the <a href="store.html">Store</a> are governed by the <a href="condiciones.html">terms of service</a>.</p>

  <h2>8. Personal data and cookies</h2>
  <p>How I handle your data and which cookies I use is explained in the <a href="privacidad.html">privacy and cookie policy</a>.</p>

  <h2>9. Governing law</h2>
  <p>This notice is governed by Spanish law. If you are a consumer, the courts of your place of residence have jurisdiction. Otherwise, the courts of Madrid.</p>'''

# ------------------------------------------------------------------ terms of service
COND_ES = f'''  <p class="label kicker">Condiciones · {UPDATED_ES}</p>
  <h1>Condiciones de contratación</h1>
  <p class="lede">Cómo funcionan los servicios de la Store: qué incluyen, cómo se pagan, cómo se cancelan y qué derechos tienes.</p>
  <p class="note"><strong>Ya puedes reservar la sesión inicial (30 min).</strong> El resto de servicios de la Store se contratará más adelante. Antes de abrirlos, explicaré aquí cómo se contratan.</p>

  <h2>1. Quién presta el servicio</h2>
  <p>Iñigo González, Madrid (España). Email: {M}. En adelante, «yo». Tú, como cliente, en adelante «tú».</p>

  <h2>2. Servicios</h2>
  <p>Servicios de asesoría y orientación profesional para perfiles IT, todos online. Cada servicio tiene su ficha en la <a href="store.html">Store</a> con lo que incluye, el formato y el plazo. Esa ficha forma parte de estas condiciones.</p>
  <p><strong>Sesión inicial:</strong> videollamada de 30 minutos sobre tu situación profesional y tu objetivo, con siguientes pasos concretos. Se reserva desde el <a href="about.html?reserva=1#reservar">formulario de contacto</a>.</p>

  <h2>3. Qué no incluyen</h2>
  <p>Son servicios de orientación: te doy criterio, revisión y un plan de acción. No soy una agencia de colocación ni un servicio de empleo. No garantizo que consigas un trabajo, una entrevista o una subida de sueldo, porque eso depende de ti y del mercado. Tampoco ofrezco asesoría legal, fiscal ni psicológica.</p>

  <h2>4. Precio y pago</h2>
  <ul>
    <li><strong>Precio:</strong> te lo indico por email, en euros y con los impuestos incluidos, antes de que pagues. No hay ningún cargo ni compromiso hasta que pagas.</li>
    <li>Se paga por adelantado con el enlace de pago seguro que te envío en ese mismo email, en el que también te indico la entidad de pago. Puedes pagar con tarjeta. Yo no veo ni guardo los datos de tu tarjeta.</li>
    <li>Si necesitas factura, pídemela por email con tus datos fiscales (o los de tu empresa).</li>
  </ul>

  <h2>5. Cómo se contrata</h2>
  <ol>
    <li>En el formulario de contacto marcas la sesión inicial y eliges una hora preferida, de lunes a viernes entre las 10:30 y las 18:00 (hora de Madrid). Aceptas estas condiciones y pides que la sesión se haga dentro del plazo de desistimiento (punto 8).</li>
    <li>Enviar el formulario es una solicitud, no un contrato, y no te obliga a nada. En un máximo de 24 horas laborables te envío por email el enlace de pago y estas condiciones.</li>
    <li>El contrato queda cerrado cuando recibo el pago. Te confirmo la cita por email con el enlace de la videollamada. Si la hora que elegiste ya no está libre, te propongo otra; si no encontramos ninguna que te venga bien, te devuelvo el importe íntegro.</li>
    <li>Si después quieres más sesiones, te envío un enlace para reservarlas y se pagan de la misma forma, por adelantado.</li>
  </ol>

  <h2>6. Cómo se presta</h2>
  <ul>
    <li><strong>Sesiones:</strong> por videollamada en la fecha que reserves. El enlace te llega por email.</li>
    <li><strong>Revisiones por escrito:</strong> me envías el material (CV, perfil de LinkedIn…) y te entrego el informe en el plazo de la ficha, contado desde que tengo todo lo necesario.</li>
    <li><strong>Planes de varias semanas:</strong> las sesiones se usan dentro del plazo del plan. Las que no se usen en ese plazo caducan, salvo causa justificada.</li>
  </ul>

  <h2>7. Cambios y cancelaciones</h2>
  <ul>
    <li><strong>Si cambias de fecha:</strong> puedes hacerlo sin coste hasta 24 horas antes de la sesión, una vez por sesión.</li>
    <li><strong>Si cancelas con más de 24 horas:</strong> eliges entre otra fecha o la devolución íntegra.</li>
    <li><strong>Si no te presentas:</strong> si no avisas, o avisas con menos de 24 horas, la sesión se considera realizada.</li>
    <li><strong>Si cancelo yo:</strong> te propongo otra fecha o te devuelvo el importe de esa sesión, como prefieras.</li>
  </ul>

  <h2>8. Derecho de desistimiento (si eres consumidor)</h2>
  <p>Tienes 14 días naturales desde que contratas para desistir sin dar explicaciones. Para hacerlo, escríbeme a {M} o envíame el formulario del final. Te devolveré el importe en un máximo de 14 días desde que me lo comuniques, por el mismo medio de pago.</p>
  <p>Si quieres que el servicio empiece antes de que terminen esos 14 días, tienes que pedírmelo expresamente al contratar (en la sesión inicial, con la casilla del formulario). En ese caso:</p>
  <ul>
    <li>Si desistes antes de terminar el servicio, pagas solo la parte ya prestada, en proporción al precio total.</li>
    <li>Una vez prestado el servicio completo, ya no puedes desistir.</li>
  </ul>
  <p>Si contratas como empresa o profesional, el derecho de desistimiento no aplica.</p>

  <h2>9. Reclamaciones</h2>
  <p>Si algo no ha ido bien, escríbeme a {M}. Te responderé en un máximo de 10 días. Si eres consumidor, también puedes acudir a los servicios de consumo de tu comunidad autónoma.</p>

  <h2>10. Confidencialidad y material</h2>
  <ul>
    <li>Lo que me cuentes y me envíes (CV, situación laboral, empresas) es confidencial y solo lo uso para prestarte el servicio. Más detalles en la <a href="privacidad.html">política de privacidad</a>.</li>
    <li>Los informes, plantillas y guías que te entregue son para tu uso personal. No puedes revenderlos ni publicarlos como propios.</li>
    <li>No grabo las sesiones salvo que lo acordemos antes los dos.</li>
  </ul>

  <h2>11. Ley aplicable</h2>
  <p>Estas condiciones se rigen por la ley española. Si eres consumidor, puedes reclamar ante los juzgados de tu domicilio.</p>

  <h2>Formulario de desistimiento</h2>
  <p>Solo si quieres desistir del contrato. Cópialo, rellénalo y envíamelo por email.</p>
  <p class="note">A la atención de Iñigo González, {MT}:<br>
  Por la presente le comunico que desisto de mi contrato de prestación del siguiente servicio: […]<br>
  Contratado el: […]<br>
  Nombre del consumidor: […]<br>
  Domicilio del consumidor: […]<br>
  Firma del consumidor (solo si el formulario se presenta en papel)<br>
  Fecha: […]</p>'''

COND_EN = f'''  <p class="label kicker">Terms · {UPDATED_EN}</p>
  <h1>Terms of service</h1>
  <p class="lede">How the Store services work: what they include, how you pay, how to cancel and what rights you have.</p>
  <p class="note"><strong>You can now book the initial session (30 min).</strong> The other Store services will open for booking later. Before they do, I'll explain here how to book them.</p>

  <h2>1. Who provides the service</h2>
  <p>Iñigo González, Madrid (Spain). Email: {M}. Referred to as "I" or "me", and you, the client, as "you".</p>

  <h2>2. Services</h2>
  <p>Career advisory services for IT professionals, all online. Each service has its own entry in the <a href="store.html">Store</a> with what it includes, the format and the timeframe. That entry forms part of these terms.</p>
  <p><strong>Initial session:</strong> a 30-minute video call about your career situation and goal, with concrete next steps. It's booked through the <a href="about.html?reserva=1#reservar">contact form</a>.</p>

  <h2>3. What they don't include</h2>
  <p>These are guidance services: I give you judgement, a review and an action plan. I'm not a recruitment agency or an employment service. I don't guarantee you'll get a job, an interview or a pay rise, because that depends on you and on the market. I don't provide legal, tax or psychological advice.</p>

  <h2>4. Price and payment</h2>
  <ul>
    <li><strong>Price:</strong> I tell you by email, in euros and with taxes included, before you pay. There is no charge or commitment until you pay.</li>
    <li>Payment is made in advance through the secure payment link in that same email, which also names the payment provider. You can pay by card. I never see or store your card details.</li>
    <li>If you need an invoice, email me your tax details (or your company's).</li>
  </ul>

  <h2>5. How to book</h2>
  <ol>
    <li>In the contact form, tick the initial session and pick a preferred time, Monday to Friday between 10:30 and 18:00 (Madrid time). You accept these terms and ask for the session to take place within the withdrawal period (section 8).</li>
    <li>Sending the form is a request, not a contract, and doesn't commit you to anything. Within 24 working hours I email you the payment link and these terms.</li>
    <li>The contract is concluded when I receive payment. I confirm the appointment by email with the video call link. If the time you picked is no longer free, I'll suggest another; if we can't find one that suits you, I'll refund you in full.</li>
    <li>If you then want more sessions, I'll send you a link to book them and they're paid the same way, in advance.</li>
  </ol>

  <h2>6. How the service is provided</h2>
  <ul>
    <li><strong>Sessions:</strong> by video call on the date you book. The link reaches you by email.</li>
    <li><strong>Written reviews:</strong> you send me your material (CV, LinkedIn profile…) and I deliver the report within the timeframe on the service entry, counted from when I have everything I need.</li>
    <li><strong>Multi-week plans:</strong> sessions are used within the plan's timeframe. Sessions not used in that time expire, unless there's a justified reason.</li>
  </ul>

  <h2>7. Changes and cancellations</h2>
  <ul>
    <li><strong>If you reschedule:</strong> free of charge up to 24 hours before the session, once per session.</li>
    <li><strong>If you cancel more than 24 hours ahead:</strong> you choose between a new date or a full refund.</li>
    <li><strong>If you don't show up:</strong> without notice, or with less than 24 hours' notice, the session counts as held.</li>
    <li><strong>If I cancel:</strong> I'll offer you a new date or refund that session, whichever you prefer.</li>
  </ul>

  <h2>8. Right of withdrawal (if you're a consumer)</h2>
  <p>You have 14 calendar days from booking to withdraw without giving a reason. To do so, email me at {M} or send me the form below. I'll refund you within 14 days of being told, using the same payment method.</p>
  <p>If you want the service to start before those 14 days end, you must ask for it explicitly when booking (for the initial session, with the checkbox on the form). In that case:</p>
  <ul>
    <li>If you withdraw before the service is finished, you only pay for the part already provided, in proportion to the total price.</li>
    <li>Once the service has been fully provided, you can no longer withdraw.</li>
  </ul>
  <p>If you book as a business or professional, the right of withdrawal doesn't apply.</p>

  <h2>9. Complaints</h2>
  <p>If something hasn't gone well, email me at {M}. I'll reply within 10 days. If you're a consumer, you can also contact the consumer affairs services in your region.</p>

  <h2>10. Confidentiality and materials</h2>
  <ul>
    <li>What you tell me and send me (CV, job situation, companies) is confidential and I only use it to provide the service. More in the <a href="privacidad.html">privacy policy</a>.</li>
    <li>The reports, templates and guides I give you are for your personal use. You may not resell them or publish them as your own.</li>
    <li>I don't record sessions unless we both agree beforehand.</li>
  </ul>

  <h2>11. Governing law</h2>
  <p>These terms are governed by Spanish law. If you're a consumer, you can bring a claim before the courts of your place of residence.</p>

  <h2>Withdrawal form</h2>
  <p>Only if you wish to withdraw from the contract. Copy it, fill it in and email it to me.</p>
  <p class="note">To Iñigo González, {MT}:<br>
  I hereby give notice that I withdraw from my contract for the provision of the following service: […]<br>
  Booked on: […]<br>
  Name of consumer: […]<br>
  Address of consumer: […]<br>
  Signature of consumer (only if this form is sent on paper)<br>
  Date: […]</p>'''

PAGES = {
    "aviso-legal.html": dict(title_es="Aviso legal", title_en="Legal notice",
                             desc="Aviso legal de inigogonzalezgarcia.github.io / Legal notice.", es=AVISO_ES, en=AVISO_EN),
    "condiciones.html": dict(title_es="Condiciones de contratación", title_en="Terms of service",
                             desc="Condiciones de contratación de los servicios IGG-ICS / Terms of service.", es=COND_ES, en=COND_EN),
}
