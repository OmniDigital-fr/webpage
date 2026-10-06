from common import I, U, GOOGLE_REVIEWS_URL
from data import PROJECTS, TESTIMONIALS, POSTS


def project_card(p, delay="", root=""):
    title, domain, img = p["title"], p["domain"], p.get("img")
    if img:
        screen = f'<img src="{root}{img}" alt="Aperçu du site {title}" loading="lazy" width="1200" height="750">'
    else:
        screen = f'<div class="browser-placeholder"><span>{title}</span><small>{domain}</small></div>'
    return f"""
      <article class="project reveal{delay}">
        <a class="project-media browser" href="{p['url']}" target="_blank" rel="noopener" aria-label="Visiter le site {p['title']}">
          <div class="browser-bar" aria-hidden="true"><i></i><i></i><i></i><span>{p['domain']}</span></div>
          <div class="browser-screen">{screen}</div>
        </a>
        <div class="project-body">
          <span class="project-kind">{p.get('tag', 'Site internet')}</span>
          <h3>{p['title']}</h3>
          <p>{p['text']}</p>
          <a class="link-arrow" href="{p['url']}" target="_blank" rel="noopener">Visiter le site</a>
        </div>
      </article>"""


def testimonial_card(t, delay=""):
    stars = "★" * t.get("stars", 5)
    return f"""
      <figure class="testimonial reveal{delay}" style="margin:0">
        <div style="display:flex;justify-content:space-between;align-items:center"><span class="quote-mark">{I['quote']}</span><span class="stars" aria-label="{t.get('stars', 5)} étoiles sur 5">{stars}</span></div>
        <blockquote>{'<br>'.join(l for l in t['text'].split(chr(10)) if l.strip())}</blockquote>
        <figcaption class="who"><span class="google-g">{I['google']}</span><div><strong>{t['name']}</strong><span>Avis Google</span></div></figcaption>
      </figure>"""


def reviews_block(title="Ce que disent nos clients"):
    from data import TESTIMONIALS
    cards = ""
    if TESTIMONIALS:
        cards = '<div class="grid grid-3" style="margin-bottom:40px">' + "".join(testimonial_card(t, f" reveal-d{i % 3}") for i, t in enumerate(TESTIMONIALS)) + "</div>"
    return f"""
<section class="section">
  <div class="container">
    <div class="section-head text-center"><span class="eyebrow">Avis clients</span><h2>{title}</h2></div>
    {cards}
    <div class="reviews-cta reveal">
      <span class="reviews-g">{I['google']}</span>
      <div>
        <h3>{f"5,0/5 sur Google, {len(TESTIMONIALS)} avis" if TESTIMONIALS else "Nos avis clients sont publics sur Google"}</h3>
        <p>Des avis publics et vérifiables, laissés par nos clients sur notre fiche Google.</p>
      </div>
      <a class="btn btn-primary" href="{GOOGLE_REVIEWS_URL}" target="_blank" rel="noopener">Lire les avis sur Google {I['arrow']}</a>
    </div>
  </div>
</section>
"""


def post_card(p, root="", delay=""):
    href = f"{root}blog/{p['slug']}.html"
    return f"""
      <article class="post-card reveal{delay}" data-cat="{p['cat'].lower().replace(' ', '-')}">
        <a class="thumb" href="{href}" tabindex="-1" aria-hidden="true"><img src="{U(p['img'], 800)}" alt="" loading="lazy" width="800" height="500"></a>
        <div class="body">
          <div class="post-meta"><span class="post-cat">{p['cat']}</span><time datetime="{p['date']}">{p['date_h']}</time><span>· {p['read']} de lecture</span></div>
          <h3><a href="{href}">{p['title']}</a></h3>
          <p>{p['excerpt']}</p>
          <a class="link-arrow" href="{href}">Lire l'article</a>
        </div>
      </article>"""


def faq_block(items):
    out = '<div class="faq">'
    for i, (q, a) in enumerate(items):
        out += f'\n      <details class="reveal"{" open" if i == 0 else ""}><summary>{q}</summary><div class="answer"><p>{a}</p></div></details>'
    return out + "\n    </div>"


def faq_jsonld(items):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items],
    }


def tools_strip():
    tools = [("monitor", "WordPress"), ("cart", "Shopify"), ("pen", "Webflow"), ("chart", "Google Analytics 4"),
             ("search", "Search Console"), ("trend", "Semrush"), ("map", "Google Business")]
    spans = "".join(f"<span>{I[i]}{n}</span>" for i, n in tools)
    return f"""
<section class="logos" aria-label="Outils et technologies">
  <div class="container">
    <p>Les outils et plateformes que nous maîtrisons</p>
    <div class="logos-row">{spans}</div>
  </div>
</section>
"""


FAQ_HOME = [
    ("Combien coûte la création d'un site internet ?",
     "Chaque projet est unique : le prix dépend du nombre de pages, des fonctionnalités et du travail de référencement souhaité. Après un échange de 30 minutes, nous vous remettons une proposition détaillée, gratuite et sans engagement."),
    ("En combien de temps verrai-je des résultats sur Google ?",
     "Les premiers effets du référencement naturel apparaissent généralement entre 2 et 4 mois, et les résultats les plus solides entre 6 et 12 mois. Le SEO local (Google Maps) peut produire des résultats plus rapidement, parfois en quelques semaines."),
    ("Est-ce que je pourrai modifier mon site moi-même ?",
     "Oui. Nous livrons un site facile à administrer, avec une formation personnalisée et un guide vidéo. Vous restez propriétaire de votre site, de votre nom de domaine et de vos contenus."),
    ("Travaillez-vous avec des entreprises partout en France ?",
     "Absolument. Nous accompagnons des PME, artisans, commerçants et professions libérales dans toute la France, en visioconférence ou en rendez-vous sur place selon votre localisation."),
    ("Que comprend l'audit SEO gratuit ?",
     "Une analyse de votre site (technique, contenus, vitesse, mobile), de votre visibilité locale et de vos principaux concurrents, avec 5 recommandations prioritaires à fort impact. Il vous est présenté lors d'un appel de 30 minutes."),
]
