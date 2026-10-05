import json

SITE = "https://www.omnidigital.fr"
EMAIL = "contact@omnidigital.fr"
PHONE = "06 78 00 59 83"
PHONE_LINK = "+33678005983"
CONTACT_NAME = "Paulo Da Costa"
STREET = "25 Rue Jean d'Estienne d'Orves"
POSTCODE = "94170"
CITY = "Le Perreux-sur-Marne"
ADDRESS = f"{STREET}, {POSTCODE} {CITY}"
MAPS_Q = "25+Rue+Jean+d%27Estienne+d%27Orves,+94170+Le+Perreux-sur-Marne"
PAULO_IMG = "assets/img/paulo-da-costa.svg"
GOOGLE_REVIEWS_URL = "https://maps.app.goo.gl/xSVsCDgXn7mug36A7"


def U(pid, w=1200, h=None):
    s = f"https://images.unsplash.com/photo-{pid}?auto=format&fit=crop&w={w}&q=80"
    if h:
        s += f"&h={h}"
    return s


I = {
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "calendar": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>',
    "video": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m22 8-6 4 6 4V8z"/><rect x="2" y="6" width="14" height="12" rx="2"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12l5 5L20 7"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>',
    "monitor": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/><path d="m7 8 3 3-3 3M13 14h4"/></svg>',
    "search": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>',
    "trend": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m22 7-8.5 8.5-5-5L2 17"/><path d="M16 7h6v6"/></svg>',
    "rocket": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4.5 16.5c-1.5 1.3-2 5-2 5s3.7-.5 5-2c.7-.8.7-2.1-.1-2.9a2.2 2.2 0 0 0-2.9-.1z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.9A12.9 12.9 0 0 1 22 2c0 2.7-.8 7.5-6 11a22.4 22.4 0 0 1-4 2z"/><path d="M9 12H4s.6-3 2-4c1.6-1.1 5 0 5 0M12 15v5s3-.6 4-2c1.1-1.6 0-5 0-5"/></svg>',
    "zap": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/></svg>',
    "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/></svg>',
    "target": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>',
    "map": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M1 6v16l7-4 8 4 7-4V2l-7 4-8-4-7 4z"/><path d="M8 2v16M16 6v16"/></svg>',
    "pen": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/></svg>',
    "cart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.7 13.4a2 2 0 0 0 2 1.6h9.7a2 2 0 0 0 2-1.6L23 6H6"/></svg>',
    "settings": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z"/></svg>',
    "chart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 3v18h18"/><path d="M7 15v2M11 11v6M15 7v10M19 12v5"/></svg>',
    "heart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8l1 1.1L12 21l7.8-7.5 1-1.1a5.5 5.5 0 0 0 0-7.8z"/></svg>',
    "eye": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8S1 12 1 12z"/><circle cx="12" cy="12" r="3"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
    "lock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>',
    "left": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 18-6-6 6-6"/></svg>',
    "right": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 18 6-6-6-6"/></svg>',
    "link": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7l-1.7 1.7"/><path d="M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7l1.7-1.7"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.4 20.5h-3.6v-5.6c0-1.3 0-3-1.8-3s-2.1 1.4-2.1 2.9v5.7H9.4V9h3.4v1.6c.5-.9 1.6-1.8 3.4-1.8 3.6 0 4.3 2.4 4.3 5.5v6.2zM5.3 7.4a2.1 2.1 0 1 1 0-4.2 2.1 2.1 0 0 1 0 4.2zM7.1 20.5H3.6V9h3.5v11.5zM22.2 0H1.8C.8 0 0 .8 0 1.7v20.6c0 .9.8 1.7 1.8 1.7h20.4c1 0 1.8-.8 1.8-1.7V1.7C24 .8 23.2 0 22.2 0z"/></svg>',
    "facebook": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M24 12a12 12 0 1 0-13.9 11.9v-8.4h-3V12h3V9.4c0-3 1.8-4.7 4.5-4.7 1.3 0 2.7.2 2.7.2v3h-1.5c-1.5 0-2 .9-2 1.9V12h3.4l-.5 3.5h-2.9v8.4A12 12 0 0 0 24 12z"/></svg>',
    "instagram": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 11.4A4 4 0 1 1 12.6 8 4 4 0 0 1 16 11.4zM17.5 6.5h0"/></svg>',
    "x": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18.2 2.3h3.4l-7.4 8.4L23 21.7h-6.8l-5.3-7-6.1 7H1.4l7.9-9L1 2.3h7l4.8 6.4 5.4-6.4zm-1.2 17.4h1.9L7.1 4.2H5.1l11.9 15.5z"/></svg>',
    "quote": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M9.6 5C5.6 6.7 3 10 3 14.3 3 17.4 4.8 19 7 19c2 0 3.6-1.5 3.6-3.5S9.2 12 7.4 12c-.4 0-.8 0-1 .1.4-2.3 2.3-4.4 4.4-5.4L9.6 5zm10 0c-4 1.7-6.6 5-6.6 9.3 0 3.1 1.8 4.7 4 4.7 2 0 3.6-1.5 3.6-3.5S19.2 12 17.4 12c-.4 0-.8 0-1 .1.4-2.3 2.3-4.4 4.4-5.4L19.6 5z"/></svg>',
    "google": '<svg viewBox="0 0 48 48" aria-hidden="true"><path fill="#FFC107" d="M43.6 20.1H42V20H24v8h11.3C33.7 32.7 29.2 36 24 36c-6.6 0-12-5.4-12-12s5.4-12 12-12c3.1 0 5.8 1.2 7.9 3.1l5.7-5.7C34 6.1 29.3 4 24 4 13 4 4 13 4 24s9 20 20 20 20-9 20-20c0-1.3-.1-2.6-.4-3.9z"/><path fill="#FF3D00" d="m6.3 14.7 6.6 4.8C14.7 15.1 19 12 24 12c3.1 0 5.8 1.2 7.9 3.1l5.7-5.7C34 6.1 29.3 4 24 4 16.3 4 9.7 8.3 6.3 14.7z"/><path fill="#4CAF50" d="M24 44c5.2 0 9.9-2 13.4-5.2l-6.2-5.2A11.9 11.9 0 0 1 24 36c-5.2 0-9.6-3.3-11.3-8l-6.5 5C9.5 39.6 16.2 44 24 44z"/><path fill="#1976D2" d="M43.6 20.1H42V20H24v8h11.3a12 12 0 0 1-4.1 5.6l6.2 5.2C37 39.2 44 34 44 24c0-1.3-.1-2.6-.4-3.9z"/></svg>',
}


def btn_arrow(text, href, cls="btn btn-primary"):
    return f'<a class="{cls}" href="{href}">{text} {I["arrow"]}</a>'


NAV = [
    ("index.html", "Accueil"),
    ("services.html", "Services"),
    ("portfolio.html", "Portfolio"),
    ("a-propos.html", "À propos"),
    ("blog.html", "Blog"),
    ("contact.html", "Contact"),
]


def head(title, desc, path, root="", image=None, jsonld=None, ogtype="website"):
    url = SITE + "/" + (path if path != "index.html" else "")
    image = image or U("1522071820081-009f0129c71c", 1200, 630)
    ld = ""
    for block in (jsonld or []):
        ld += '\n  <script type="application/ld+json">' + json.dumps(block, ensure_ascii=False) + "</script>"
    return f"""<!doctype html>
<html lang="fr" class="no-js">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{url}">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#0a2540">
  <meta property="og:type" content="{ogtype}">
  <meta property="og:site_name" content="Omni Digital">
  <meta property="og:locale" content="fr_FR">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{image}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="{root}assets/img/favicon.png" type="image/png">
  <link rel="apple-touch-icon" href="{root}assets/img/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preconnect" href="https://images.unsplash.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{root}assets/css/style.css">{ld}
</head>
<body>
<a class="skip-link" href="#main">Aller au contenu</a>
"""


def header(active, root=""):
    items = ""
    for href, label in NAV:
        cur = ' aria-current="page"' if href == active else ""
        items += f'\n        <li><a href="{root}{href}"{cur}>{label}</a></li>'
    return f"""
<div class="topbar">
  <div class="container">
    <div class="topbar-info">
      <a href="tel:{PHONE_LINK}">{I["phone"]} {PHONE}</a>
      <a href="mailto:{EMAIL}" class="topbar-hide-md">{I["mail"]} {EMAIL}</a>
      <span class="topbar-hide-md">{I["pin"]} {CITY} (94)</span>
    </div>
    <div class="topbar-social">
      <a href="{root}rendez-vous.html">Audit SEO offert — réservez votre appel →</a>
    </div>
  </div>
</div>
<header class="site-header">
  <div class="container nav">
    <a class="logo" href="{root}index.html" aria-label="Omni Digital — accueil">
      <img src="{root}assets/img/logo-omni-digital-h.png" alt="Omni Digital" width="365" height="160">
    </a>
    <nav aria-label="Navigation principale">
      <ul class="nav-menu" id="nav-menu">{items}
        <li class="mobile-only"><a class="btn btn-primary" href="{root}contact.html">Parlons de votre projet</a></li>
      </ul>
    </nav>
    <div class="nav-cta">
      <a class="btn btn-outline btn-sm" href="{root}rendez-vous.html">{I["calendar"]} Prendre RDV</a>
      <a class="btn btn-primary btn-sm" href="{root}contact.html">Parlons-en</a>
      <button class="nav-toggle" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="nav-menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
"""


def cta_band(root="", title="Prêt à attirer plus de clients grâce au web ?", text="Parlez-nous de votre projet : nous vous répondons sous 24 h ouvrées avec un premier diagnostic gratuit et sans engagement."):
    return f"""
<section class="section" aria-label="Contact">
  <div class="container">
    <div class="cta-band reveal">
      <div>
        <h2>{title}</h2>
        <p>{text}</p>
      </div>
      <div class="cta-actions">
        <a class="btn btn-primary btn-lg" href="{root}contact.html">Parlons de votre projet {I["arrow"]}</a>
        <a class="btn btn-ghost-light btn-lg" href="{root}rendez-vous.html">{I["calendar"]} Réserver un appel de 30 min</a>
        <span class="cta-note">✔ Gratuit · ✔ Sans engagement · ✔ Réponse sous 24 h</span>
      </div>
    </div>
  </div>
</section>
"""


def footer(root=""):
    return f"""
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a class="logo logo--footer" href="{root}index.html"><img src="{root}assets/img/logo-omni-digital.png" alt="Omni Digital — Creative Agency" width="429" height="447" loading="lazy"></a>
        <p>Agence web dédiée aux PME : création de sites internet, référencement naturel (SEO) et accompagnement à la transformation digitale pour générer plus de contacts.</p>
        <div class="socials">
          <a href="https://www.linkedin.com/" aria-label="LinkedIn" rel="noopener" target="_blank">{I["linkedin"]}</a>
          <a href="https://www.facebook.com/" aria-label="Facebook" rel="noopener" target="_blank">{I["facebook"]}</a>
          <a href="https://www.instagram.com/" aria-label="Instagram" rel="noopener" target="_blank">{I["instagram"]}</a>
        </div>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="{root}services.html#creation">Création de site web</a></li>
          <li><a href="{root}services.html#seo">Référencement SEO</a></li>
          <li><a href="{root}services.html#seo-local">SEO local & Google Maps</a></li>
          <li><a href="{root}services.html#refonte">Refonte & optimisation</a></li>
          <li><a href="{root}services.html#digital">Transformation digitale</a></li>
        </ul>
      </div>
      <div>
        <h4>Agence</h4>
        <ul>
          <li><a href="{root}a-propos.html">À propos</a></li>
          <li><a href="{root}portfolio.html">Portfolio</a></li>
          <li><a href="{root}blog.html">Blog</a></li>
          <li><a href="{root}contact.html">Nous contacter</a></li>
          <li><a href="{root}rendez-vous.html">Prendre rendez-vous</a></li>
          <li><a href="{GOOGLE_REVIEWS_URL}" target="_blank" rel="noopener">Nos avis Google</a></li>
        </ul>
      </div>
      <div>
        <h4>Restez informé</h4>
        <p>Un conseil SEO & web par mois, directement dans votre boîte mail.</p>
        <form class="newsletter" data-newsletter novalidate>
          <label class="sr-only" for="nl-email">Votre e-mail</label>
          <input id="nl-email" type="email" placeholder="Votre e-mail" autocomplete="email" required>
          <button class="btn btn-primary" type="submit">OK</button>
        </form>
        <ul style="margin-top:22px">
          <li>{CONTACT_NAME}</li>
          <li><a href="https://www.google.com/maps/search/?api=1&amp;query={MAPS_Q}" target="_blank" rel="noopener">{STREET}<br>{POSTCODE} {CITY}</a></li>
          <li><a href="tel:{PHONE_LINK}">{PHONE}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year>2026</span> Omni Digital — Agence web & SEO pour PME. Tous droits réservés.</span>
      <nav aria-label="Liens légaux">
        <a href="{root}mentions-legales.html">Mentions légales</a>
        <a href="{root}mentions-legales.html#confidentialite">Confidentialité</a>
        <a href="{root}sitemap.xml">Plan du site</a>
      </nav>
    </div>
  </div>
</footer>

<div class="sticky-cta" aria-hidden="false">
  <a class="btn btn-outline" href="tel:{PHONE_LINK}" aria-label="Appeler">{I["phone"]} Appeler</a>
  <a class="btn btn-primary" href="{root}contact.html">Nous écrire {I["arrow"]}</a>
</div>

<div class="cookie" role="dialog" aria-live="polite" aria-label="Cookies">
  <p>🍪 Nous utilisons uniquement des cookies de mesure d'audience anonymes pour améliorer votre expérience. <a href="{root}mentions-legales.html#confidentialite">En savoir plus</a></p>
  <div class="row">
    <button class="btn btn-primary btn-sm" data-cookie="accept">Accepter</button>
    <button class="btn btn-outline btn-sm" data-cookie="refuse">Refuser</button>
  </div>
</div>

<script src="{root}assets/js/main.js" defer></script>
</body>
</html>
"""


def page_hero(eyebrow, title, text, crumbs, img, root=""):
    bc = f'<li><a href="{root}index.html">Accueil</a></li>'
    for label, href in crumbs:
        if href:
            bc += f'<li><a href="{root}{href}">{label}</a></li>'
        else:
            bc += f'<li aria-current="page">{label}</li>'
    return f"""
<section class="page-hero">
  <div class="bg"><img src="{img}" alt="" fetchpriority="high"></div>
  <div class="container">
    <ol class="breadcrumb">{bc}</ol>
    <span class="eyebrow">{eyebrow}</span>
    <h1>{title}</h1>
    <p>{text}</p>
  </div>
</section>
"""
