from common import I, U, SITE, EMAIL, PHONE, PHONE_LINK, CONTACT_NAME, STREET, POSTCODE, CITY, ADDRESS, MAPS_Q, PAULO_IMG, head, header, footer, cta_band, page_hero, btn_arrow
from data import PROJECTS, TESTIMONIALS, POSTS
from parts import project_card, testimonial_card, post_card, faq_block, faq_jsonld, tools_strip, reviews_block, FAQ_HOME
from common import GOOGLE_REVIEWS_URL

ORG_LD = {
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "name": "Omni Digital",
    "description": "Agence web pour PME : création de sites internet, référencement naturel SEO, SEO local et transformation digitale.",
    "url": SITE,
    "logo": SITE + "/assets/img/logo-omni-digital.png",
    "image": U("1522071820081-009f0129c71c", 1200),
    "email": EMAIL,
    "telephone": "+33 6 78 00 59 83",
    "founder": {"@type": "Person", "name": CONTACT_NAME},
    "areaServed": ["Le Perreux-sur-Marne", "Val-de-Marne", "Île-de-France", "France"],
    "priceRange": "€€",
    "address": {"@type": "PostalAddress", "streetAddress": STREET, "postalCode": POSTCODE, "addressLocality": CITY, "addressRegion": "Île-de-France", "addressCountry": "FR"},
    "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "18:00"}],
    "sameAs": [GOOGLE_REVIEWS_URL],
}

SERVICES = [
    ("creation", "monitor", "Création de site web", "Des sites vitrines et e-commerce rapides, élégants et pensés pour convertir vos visiteurs en clients.",
     ["Design sur-mesure & responsive", "Optimisé pour la conversion", "Facile à mettre à jour"]),
    ("seo", "search", "Référencement naturel SEO", "Gagnez des positions durables sur Google grâce à une stratégie SEO technique, éditoriale et netlinking.",
     ["Audit & stratégie de mots-clés", "Contenus optimisés", "Suivi mensuel des positions"]),
    ("seo-local", "map", "SEO local & Google Maps", "Soyez la première entreprise que vos clients trouvent dans votre ville et sur Google Maps.",
     ["Fiche Google Business Profile", "Gestion des avis clients", "Pages locales ciblées"]),
    ("digital", "rocket", "Transformation digitale", "On accompagne votre PME dans le passage au numérique : outils, process, présence en ligne.",
     ["Prise de RDV & devis en ligne", "Automatisation & CRM", "Formation de vos équipes"]),
]


def home():
    root = ""
    out = head("Omni Digital — Agence web & SEO pour PME | Création de sites et référencement Google",
               "Omni Digital crée et optimise des sites internet qui attirent des clients. Création de site, référencement SEO, SEO local et transformation digitale pour PME. Audit gratuit.",
               "index.html", jsonld=[ORG_LD, faq_jsonld(FAQ_HOME)])
    out += header("index.html")
    out += f"""
<main id="main">
<section class="hero">
  <div class="container hero-grid">
    <div>
      <span class="eyebrow reveal">Agence web & SEO pour PME</span>
      <h1 class="reveal reveal-d1">Votre site web devient votre <span class="hl">meilleur commercial</span>.</h1>
      <p class="hero-lead reveal reveal-d2">Omni Digital crée, modernise et référence les sites des PME pour qu'ils <strong>apparaissent en haut de Google</strong> et transforment chaque visiteur en demande de contact ou de devis.</p>
      <div class="hero-actions reveal reveal-d3">
        <a class="btn btn-primary btn-lg" href="contact.html">Parlons de votre projet {I["arrow"]}</a>
        <a class="btn btn-outline btn-lg" href="rendez-vous.html">{I["calendar"]} Audit SEO offert</a>
      </div>
      <a class="hero-proof reveal reveal-d3" href="{GOOGLE_REVIEWS_URL}" target="_blank" rel="noopener">
        <span class="reviews-g reviews-g--sm">{I["google"]}</span>
        <div><strong>Avis clients vérifiables</strong><small>Consultez nos avis sur Google →</small></div>
      </a>
    </div>
    <div class="hero-visual reveal reveal-d2">
      <div class="hero-photo"><img src="{U('1522071820081-009f0129c71c', 1000)}" alt="Atelier de stratégie web autour d'un ordinateur" width="1000" height="1100" fetchpriority="high"></div>
      <div class="float-card float-card--a"><span class="ic ic-green">{I["trend"]}</span><div><strong>Visible</strong><small>sur Google & Google Maps</small></div></div>
      <div class="float-card float-card--b"><span class="ic ic-orange">{I["chat"]}</span><div><strong>+ de contacts</strong><small>appels, formulaires, RDV</small></div><div class="mini-chart" aria-hidden="true"><i style="height:30%"></i><i style="height:45%"></i><i style="height:40%"></i><i style="height:65%"></i><i style="height:100%"></i></div></div>
      <div class="float-card float-card--c"><span class="ic ic-blue" style="width:36px;height:36px">{I["google"]}</span><div><strong style="font-size:1rem">SEO local</strong><small>fiche Google optimisée</small></div></div>
    </div>
  </div>
</section>
{tools_strip()}
<section class="section">
  <div class="container">
    <div class="section-head text-center">
      <span class="eyebrow">Nos expertises</span>
      <h2>Tout ce qu'il faut pour <span class="hl">gagner des clients</span> en ligne</h2>
      <p>Une seule agence pour concevoir votre site, le rendre visible sur Google et faire entrer votre PME dans l'ère du digital.</p>
    </div>
    <div class="grid grid-4">"""
    for i, (anchor, ic, t, d, li) in enumerate(SERVICES):
        lis = "".join(f"<li>{x}</li>" for x in li)
        box = "icon-box icon-box--orange" if i % 2 else "icon-box"
        out += f"""
      <article class="card service-card reveal reveal-d{i % 4}">
        <span class="num">0{i + 1}</span>
        <div class="{box}">{I[ic]}</div>
        <h3>{t}</h3>
        <p>{d}</p>
        <ul>{lis}</ul>
        <a class="link-arrow" href="services.html#{anchor}">En savoir plus</a>
      </article>"""
    out += f"""
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="container split">
    <div class="split-media reveal">
      <div class="photo"><img src="{U('1552664730-d307ca884978', 1000)}" alt="Atelier de travail avec un client PME autour d'une stratégie digitale" loading="lazy" width="1000" height="800"></div>
      <div class="badge-exp"><strong>1</strong><span>interlocuteur unique, du début à la fin</span></div>
    </div>
    <div class="reveal reveal-d1">
      <span class="eyebrow">Pourquoi Omni Digital</span>
      <h2>Un partenaire qui parle <span class="hl-underline">résultats</span>, pas jargon.</h2>
      <p>Nous savons qu'un dirigeant de PME n'a pas de temps à perdre. Notre rôle : vous apporter des clients, simplement, avec un interlocuteur unique et des résultats mesurables chaque mois.</p>
      <ul class="check-list">
        <li><span class="tick">{I["check"]}</span><div><strong>Un interlocuteur unique</strong> qui connaît votre entreprise et vous répond sous 24 h ouvrées.</div></li>
        <li><span class="tick">{I["check"]}</span><div><strong>Des sites rapides</strong> et sécurisés, optimisés pour les critères de Google.</div></li>
        <li><span class="tick">{I["check"]}</span><div><strong>Un reporting clair</strong> : positions, trafic, appels et formulaires reçus.</div></li>
        <li><span class="tick">{I["check"]}</span><div><strong>Vous restez propriétaire</strong> de votre site, domaine et contenus. Sans engagement caché.</div></li>
      </ul>
      {btn_arrow("Découvrir notre approche", "a-propos.html")}
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="container">
    <div class="section-head text-center">
      <span class="eyebrow">Nos engagements</span>
      <h2>Ce que vous pouvez attendre de nous</h2>
    </div>
    <div class="stats">
      <div class="stat reveal"><strong><span data-count="24">24</span><em>h</em></strong><span>pour vous répondre (jours ouvrés)</span></div>
      <div class="stat reveal reveal-d1"><strong><span>1</span></strong><span>interlocuteur unique, du début à la fin</span></div>
      <div class="stat reveal reveal-d2"><strong><span>0</span><em>€</em></strong><span>pour l'audit et le premier échange</span></div>
      <div class="stat reveal reveal-d3"><strong><span data-count="100">100</span><em>%</em></strong><span>propriétaire de votre site et de vos contenus</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head text-center">
      <span class="eyebrow">Notre méthode</span>
      <h2>Du premier appel aux premiers clients, <span class="hl">en 4 étapes</span></h2>
      <p>Une méthode simple, transparente et sans surprise.</p>
    </div>
    <div class="process">
      <div class="step reveal"><div class="step-num">01</div><h3>Audit gratuit</h3><p>Nous analysons votre site, votre visibilité Google et vos concurrents.</p></div>
      <div class="step reveal reveal-d1"><div class="step-num">02</div><h3>Stratégie</h3><p>Un plan d'action clair, chiffré et priorisé selon vos objectifs.</p></div>
      <div class="step reveal reveal-d2"><div class="step-num">03</div><h3>Création & SEO</h3><p>Design, développement, contenus et optimisation technique.</p></div>
      <div class="step reveal reveal-d3"><div class="step-num">04</div><h3>Croissance</h3><p>Suivi mensuel, améliorations continues et reporting des résultats.</p></div>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="container">
    <div class="section-head" style="display:flex;justify-content:space-between;align-items:flex-end;gap:24px;max-width:none;flex-wrap:wrap">
      <div style="max-width:640px"><span class="eyebrow">Portfolio</span><h2 style="margin:0">Quelques <span class="hl">réalisations</span></h2></div>
      <a class="btn btn-outline" href="portfolio.html">Voir le portfolio {I["arrow"]}</a>
    </div>
    <div class="grid grid-3">{"".join(project_card(p, f" reveal-d{i}") for i, p in enumerate(PROJECTS[:3]))}
    </div>
  </div>
</section>

{reviews_block()}

<section class="section section--tint">
  <div class="container">
    <div class="section-head" style="display:flex;justify-content:space-between;align-items:flex-end;gap:24px;max-width:none;flex-wrap:wrap">
      <div style="max-width:640px"><span class="eyebrow">Blog & conseils</span><h2 style="margin:0">Conseils & bonnes pratiques</h2></div>
      <a class="btn btn-outline" href="blog.html">Tous les articles {I["arrow"]}</a>
    </div>
    <div class="grid grid-3">{"".join(post_card(p, "", f" reveal-d{i}") for i, p in enumerate(POSTS[:3]))}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head text-center">
      <span class="eyebrow">FAQ</span>
      <h2>Vos questions, nos réponses</h2>
    </div>
    {faq_block(FAQ_HOME)}
  </div>
</section>
{cta_band()}
</main>
"""
    out += footer()
    return out


def services():
    out = head("Services — Création de site, SEO, SEO local & transformation digitale | Omni Digital",
               "Découvrez les services d'Omni Digital : création de sites internet, référencement naturel SEO, SEO local Google Maps, refonte et transformation digitale des PME.",
               "services.html", jsonld=[ORG_LD])
    out += header("services.html")
    out += "<main id=\"main\">" + page_hero("Nos services", "Des solutions web complètes pour faire <span class=\"hl-orange\">grandir votre PME</span>",
                     "De la création de votre site à sa première place sur Google, nous prenons en charge chaque étape de votre croissance en ligne.",
                     [("Services", None)], U("1497366216548-37526070297c", 1600))

    blocks = [
        ("creation", "Création de site web", "Un site qui vous ressemble et qui <span class=\"hl\">vend pour vous</span>",
         "Site vitrine, site e-commerce ou plateforme sur-mesure : nous concevons des sites premium, rapides et pensés dès le départ pour le référencement et la conversion.",
         ["<strong>Design sur-mesure</strong> aligné sur votre image de marque", "<strong>100 % responsive</strong> : parfait sur mobile, tablette et ordinateur",
          "<strong>Appels à l'action</strong>, formulaires et prise de RDV intégrés", "<strong>Back-office simple</strong> + formation pour être autonome"],
         U("1547658719-da2b51169166", 1000), "Maquettes de site web en cours de conception", "creation"),
        ("seo", "Référencement naturel SEO", "Montez en haut de Google <span class=\"hl\">durablement</span>",
         "Le SEO est le canal d'acquisition le plus rentable sur le long terme. Nous construisons une stratégie complète pour faire de votre site une référence dans votre secteur.",
         ["<strong>Audit technique</strong> complet et corrections", "<strong>Recherche de mots-clés</strong> à fort potentiel commercial",
          "<strong>Rédaction de contenus</strong> optimisés pour vos clients et pour Google", "<strong>Netlinking</strong> de qualité et suivi mensuel des positions"],
         U("1460925895917-afdab827c52f", 1000), "Tableau de bord d'analyse de trafic SEO sur un ordinateur", "seo"),
        ("seo-local", "SEO local & Google Maps", "Soyez trouvé par les clients <span class=\"hl\">près de chez vous</span>",
         "46 % des recherches Google ont une intention locale. Nous optimisons votre présence pour que vous apparaissiez dans le « pack local » de Google Maps.",
         ["<strong>Optimisation Google Business Profile</strong> (catégories, photos, posts)", "<strong>Stratégie d'avis clients</strong> et réponses professionnelles",
          "<strong>Citations locales</strong> et annuaires de référence", "<strong>Pages locales</strong> par ville ou zone d'intervention"],
         U("1524661135-423995f22d0b", 1000), "Carte avec repères de localisation pour le référencement local", "seo-local"),
        ("refonte", "Refonte & optimisation", "Votre site actuel ne rapporte rien ? <span class=\"hl\">On le transforme.</span>",
         "Un site lent, daté ou mal structuré vous fait perdre des clients chaque jour. Nous le modernisons sans perdre votre référencement existant.",
         ["<strong>Audit UX & conversion</strong> de votre site actuel", "<strong>Migration SEO sécurisée</strong> (redirections, contenus)",
          "<strong>Optimisation de la vitesse</strong> et des Core Web Vitals", "<strong>Tests A/B</strong> sur les pages clés"],
         U("1498050108023-c5249f4df085", 1000), "Développeur optimisant le code d'un site internet", "refonte"),
        ("digital", "Transformation digitale", "Faites passer votre PME <span class=\"hl\">au digital</span>, sereinement",
         "Prise de rendez-vous, devis en ligne, CRM, automatisations, réseaux sociaux : nous vous aidons à choisir et déployer les bons outils, sans complexité.",
         ["<strong>Diagnostic digital</strong> de votre entreprise", "<strong>Mise en place d'outils</strong> : agenda, CRM, facturation, e-mailing",
          "<strong>Automatisation</strong> des tâches répétitives", "<strong>Formation</strong> et accompagnement de vos équipes"],
         U("1556761175-5973dc0f32e7", 1000), "Accompagnement d'une équipe de PME dans sa transformation digitale", "digital"),
    ]
    for i, (aid, eb, title, text, items, img, alt, svc) in enumerate(blocks):
        rev = " split--reverse" if i % 2 else ""
        tint = " section--tint" if i % 2 else ""
        lis = "".join(f'<li><span class="tick">{I["check"]}</span><div>{x}</div></li>' for x in items)
        out += f"""
<section class="section{tint}" id="{aid}">
  <div class="container split{rev}">
    <div class="split-media reveal"><div class="photo"><img src="{img}" alt="{alt}" loading="lazy" width="1000" height="800"></div></div>
    <div class="reveal reveal-d1">
      <span class="eyebrow">{eb}</span>
      <h2>{title}</h2>
      <p>{text}</p>
      <ul class="check-list">{lis}</ul>
      <div style="display:flex;gap:12px;flex-wrap:wrap">{btn_arrow("Discutons-en", "contact.html?service=" + svc)}<a class="btn btn-outline" href="rendez-vous.html">En parler 30 min</a></div>
    </div>
  </div>
</section>"""

    plans = [
        ("Site Vitrine", "Sur mesure", "Proposition gratuite", "Pour les artisans, commerçants et indépendants qui veulent une présence professionnelle.",
         ["Jusqu'à 6 pages sur-mesure", "Design responsive premium", "SEO de base & Google Business", "Formulaire de contact + RDV", "Formation & 1 mois de support"], False),
        ("Croissance", "Sur mesure", "Site + accompagnement SEO mensuel", "Pour les PME qui veulent générer des contacts réguliers grâce à Google.",
         ["Site jusqu'à 15 pages", "Stratégie de mots-clés complète", "2 articles SEO par mois", "SEO local & gestion des avis", "Reporting mensuel des résultats"], True),
        ("E-commerce", "Sur mesure", "Proposition gratuite", "Pour vendre vos produits en ligne avec une boutique performante.",
         ["Boutique Shopify ou WooCommerce", "Fiches produits optimisées SEO", "Paiement sécurisé & livraisons", "Tunnel de commande optimisé", "Formation & 3 mois de support"], False),
    ]
    out += """
<section class="section" id="tarifs">
  <div class="container">
    <div class="section-head text-center">
      <span class="eyebrow">Formules</span>
      <h2>Des offres claires, <span class="hl">sans surprise</span></h2>
      <p>Chaque projet fait l'objet d'une proposition personnalisée, gratuite et détaillée. Voici les formules les plus courantes.</p>
    </div>
    <div class="grid grid-3" style="align-items:stretch">"""
    for i, (n, p, unit, d, li, feat) in enumerate(plans):
        lis = "".join(f"<li>{x}</li>" for x in li)
        out += f"""
      <article class="card service-card price-card{' is-featured' if feat else ''} reveal reveal-d{i}">
        {'<span class="ribbon">Recommandé</span>' if feat else ''}
        <h3>{n}</h3>
        <p style="font-size:.95rem">{d}</p>
        <div class="price" style="font-size:1.7rem">{p}</div>
        <p style="font-size:.88rem;color:var(--muted)">{unit}</p>
        <ul>{lis}</ul>
        <a class="btn {'btn-primary' if feat else 'btn-outline'} btn-block" href="contact.html">Discutons-en {I['arrow']}</a>
      </article>"""
    out += """
    </div>
  </div>
</section>
"""
    out += cta_band(title="Un projet ? Recevez une proposition sur-mesure sous 48 h.")
    out += "</main>" + footer()
    return out


def portfolio():
    out = head("Portfolio — Nos réalisations web & SEO | Omni Digital",
               "Découvrez des sites internet créés par Omni Digital : Digital Réseau, Les Bras Cassés, Broken Arms, Pratik Informatique. Création de sites et référencement pour PME.",
               "portfolio.html")
    out += header("portfolio.html")
    out += "<main id=\"main\">" + page_hero("Portfolio", "Quelques sites créés par <span class=\"hl-orange\">Omni Digital</span>",
                     "Des sites réels, en ligne, que vous pouvez visiter. Cliquez sur un projet pour le découvrir.",
                     [("Portfolio", None)], U("1531482615713-2afd69097998", 1600))
    out += f"""
<section class="section">
  <div class="container">
    <div class="grid grid-2">{"".join(project_card(p, f" reveal-d{i % 2}") for i, p in enumerate(PROJECTS))}
    </div>
  </div>
</section>

{reviews_block()}"""
    out += cta_band(title="Votre projet sera notre prochaine réussite.", text="Racontez-nous vos objectifs : nous vous proposons une stratégie et une proposition sur-mesure, gratuitement.")
    out += "</main>" + footer()
    return out


def about():
    out = head("À propos — Paulo Da Costa, votre interlocuteur web & SEO | Omni Digital",
               "Omni Digital, c'est Paulo Da Costa : un interlocuteur unique pour créer votre site internet, le référencer sur Google et accompagner votre PME dans le digital. Basé au Perreux-sur-Marne.",
               "a-propos.html", jsonld=[ORG_LD])
    out += header("a-propos.html")
    out += "<main id=\"main\">" + page_hero("À propos", "Le digital au service <span class=\"hl-orange\">des PME</span>, tout simplement",
                     "Omni Digital, c'est un interlocuteur unique pour créer, référencer et faire évoluer la présence en ligne de votre entreprise.",
                     [("À propos", None)], U("1504384308090-c894fdcc538d", 1600))
    values = [("target", "Orienté résultats", "Chaque action est mesurée : visites, positions, appels, demandes. Ce qui compte, c'est votre croissance."),
              ("heart", "Proximité", "Un seul interlocuteur, joignable, qui parle votre langage — pas celui des développeurs."),
              ("eye", "Transparence", "Propositions détaillées, pas de frais cachés, et vous restez propriétaire de tout ce qui est créé."),
              ("zap", "Exigence", "Design soigné, code propre, site rapide : chaque projet est traité avec la même attention.")]
    values_html = "".join(f"""
      <div class="value-card reveal reveal-d{i}"><div class="icon-box{' icon-box--orange' if i % 2 else ''}">{I[ic]}</div><h3>{t}</h3><p>{d}</p></div>""" for i, (ic, t, d) in enumerate(values))
    out += f"""
<section class="section">
  <div class="container split">
    <div class="split-media reveal">
      <div class="photo"><img src="{U('1551434678-e076c223a692', 1000)}" alt="Espace de travail dédié à la création de sites internet" loading="lazy" width="1000" height="800"></div>
      <div class="badge-exp"><strong>94</strong><span>Basé au Perreux-sur-Marne, interventions partout en France</span></div>
    </div>
    <div class="reveal reveal-d1">
      <span class="eyebrow">Qui suis-je ?</span>
      <h2>{CONTACT_NAME}, votre interlocuteur digital</h2>
      <!-- À COMPLÉTER : ajoutez ici votre parcours (années d'expérience, formation, spécialités). -->
      <p>Je suis {CONTACT_NAME}, à l'origine d'Omni Digital. J'accompagne les PME, artisans, commerçants et indépendants qui veulent un site internet professionnel, visible sur Google et qui leur apporte de vrais contacts.</p>
      <p>Avec Omni Digital, vous n'avez pas affaire à une grande structure : vous avez <strong>un interlocuteur unique</strong>, qui suit votre projet du premier appel à la mise en ligne, puis dans la durée. Pas d'intermédiaire, pas de jargon : des explications claires et des décisions prises ensemble.</p>
      <p>Le nom résume l'approche : <strong>« Omni »</strong>, parce que je couvre l'ensemble de votre présence digitale — site, référencement, outils — avec un seul point de contact.</p>
      {btn_arrow("Travaillons ensemble", "contact.html")}
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="container">
    <div class="section-head text-center"><span class="eyebrow">Mes valeurs</span><h2>Ce qui guide chaque projet</h2></div>
    <div class="grid grid-4">{values_html}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="owner-card reveal">
      <img src="{PAULO_IMG}" alt="{CONTACT_NAME}" width="600" height="660" loading="lazy">
      <div>
        <span class="eyebrow">Votre interlocuteur</span>
        <h2>{CONTACT_NAME}</h2>
        <p class="owner-role">Création de sites · Référencement SEO · Transformation digitale</p>
        <p>Un projet, une question, un doute sur votre site actuel ? Appelez-moi ou réservez un créneau : le premier échange est offert et sans engagement.</p>
        <div style="display:flex;gap:12px;flex-wrap:wrap">{btn_arrow("Réserver un appel", "rendez-vous.html")}<a class="btn btn-outline" href="tel:{PHONE_LINK}">{I["phone"]} {PHONE}</a></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="container split split--reverse">
    <div class="split-media reveal"><div class="photo"><img src="{U('1542744173-8e7e53415bb0', 1000)}" alt="Présentation d'une stratégie digitale à un client" loading="lazy" width="1000" height="800"></div></div>
    <div class="reveal reveal-d1">
      <span class="eyebrow">Mon engagement</span>
      <h2>Votre réussite est la <span class="hl">seule mesure</span></h2>
      <ul class="check-list">
        <li><span class="tick">{I["check"]}</span><div><strong>Audit et premier échange offerts</strong>, sans engagement.</div></li>
        <li><span class="tick">{I["check"]}</span><div><strong>Vous restez propriétaire</strong> de votre site, de votre nom de domaine et de vos contenus.</div></li>
        <li><span class="tick">{I["check"]}</span><div><strong>Sites sécurisés (HTTPS)</strong> et conformes au RGPD.</div></li>
        <li><span class="tick">{I["check"]}</span><div><strong>Réponse rapide</strong> par téléphone, e-mail ou visio.</div></li>
      </ul>
      {btn_arrow("Réserver un appel découverte", "rendez-vous.html")}
    </div>
  </div>
</section>
"""
    out += cta_band()
    out += "</main>" + footer()
    return out


def contact():
    out = head("Contact — Parlons de votre projet web | Omni Digital",
               "Contactez Omni Digital pour échanger sur votre projet de site internet, de référencement SEO ou de transformation digitale. Premier conseil offert, réponse sous 24 h ouvrées.",
               "contact.html", jsonld=[ORG_LD])
    out += header("contact.html")
    out += "<main id=\"main\">" + page_hero("Contact", "Parlons de votre projet <span class=\"hl-orange\">dès aujourd'hui</span>",
                     "Remplissez le formulaire ci-dessous : Paulo vous recontacte sous 24 h ouvrées avec un premier diagnostic gratuit.",
                     [("Contact", None)], U("1556761175-5973dc0f32e7", 1600))
    chips = [("creation", "Création de site"), ("seo", "Référencement SEO"), ("seo-local", "SEO local"),
             ("refonte", "Refonte"), ("ecommerce", "E-commerce"), ("digital", "Transformation digitale")]
    chips_html = "".join(f'<label class="chip"><input type="checkbox" name="services" value="{v}"><span>{l}</span></label>' for v, l in chips)
    out += f"""
<section class="section">
  <div class="container contact-grid">
    <div class="reveal">
      <span class="eyebrow">Nos coordonnées</span>
      <h2>Un projet, une question&nbsp;? Nous sommes là.</h2>
      <p>Choisissez le moyen qui vous convient le mieux. Pour un échange approfondi, réservez directement un créneau dans notre agenda.</p>
      <div class="contact-info">
        <div class="info-item"><span class="ic">{I["phone"]}</span><div><strong>Téléphone</strong><a href="tel:{PHONE_LINK}">{PHONE}</a></div></div>
        <div class="info-item"><span class="ic">{I["mail"]}</span><div><strong>E-mail</strong><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
        <div class="info-item"><span class="ic">{I["clock"]}</span><div><strong>Horaires</strong><span>Du lundi au vendredi, de 9h à 18h</span></div></div>
        <div class="info-item"><span class="ic">{I["users"]}</span><div><strong>Votre interlocuteur</strong><span>{CONTACT_NAME}</span></div></div>
        <div class="info-item"><span class="ic">{I["pin"]}</span><div><strong>Adresse</strong><a href="https://www.google.com/maps/search/?api=1&amp;query={MAPS_Q}" target="_blank" rel="noopener">{STREET}<br>{POSTCODE} {CITY}</a><span style="display:block;font-size:.9rem;color:var(--muted)">Interventions dans toute la France, en visio ou sur place</span></div></div>
      </div>
      <div class="card" style="margin-top:24px;background:var(--blue-50);border:0">
        <h3 style="display:flex;gap:10px;align-items:center"><span style="color:var(--orange-500);width:24px">{I["calendar"]}</span> Préférez un échange en direct&nbsp;?</h3>
        <p>Réservez un appel découverte de 30 minutes, gratuit et sans engagement.</p>
        {btn_arrow("Choisir un créneau", "rendez-vous.html")}
      </div>
    </div>

    <div class="form-card reveal reveal-d1" data-form-wrap id="devis">
      <form class="form-body" data-omni-form novalidate>
        <h2 style="font-size:1.7rem">Parlez-nous de votre projet</h2>
        <p style="color:var(--muted)">Les champs marqués d'un <span style="color:var(--orange-600)">*</span> sont obligatoires.</p>
        <input type="hidden" name="_subject" value="Nouveau message — site Omni Digital">
        <div class="hp-field" aria-hidden="true"><label>Ne pas remplir<input type="text" name="_gotcha" tabindex="-1" autocomplete="off"></label></div>
        <div class="form-grid">
          <div class="field"><label for="nom">Nom & prénom <span class="req">*</span></label><input id="nom" name="nom" autocomplete="name" required><p class="error-msg">Merci d'indiquer votre nom.</p></div>
          <div class="field"><label for="entreprise">Entreprise</label><input id="entreprise" name="entreprise" autocomplete="organization"></div>
          <div class="field"><label for="email">E-mail <span class="req">*</span></label><input id="email" name="email" type="email" autocomplete="email" required><p class="error-msg">Merci d'indiquer un e-mail valide.</p></div>
          <div class="field"><label for="tel">Téléphone <span class="req">*</span></label><input id="tel" name="telephone" type="tel" autocomplete="tel" required><p class="error-msg">Merci d'indiquer un numéro valide.</p></div>
          <div class="field full"><label for="site">Site actuel (si vous en avez un)</label><input id="site" name="site_actuel" type="url" placeholder="https://"></div>
          <div class="field full"><span class="label">Vos besoins</span><div class="chips">{chips_html}</div></div>
          <div class="field"><label for="budget">Budget envisagé</label>
            <select id="budget" name="budget"><option value="">Je ne sais pas encore</option><option>Moins de 1 500 €</option><option>1 500 € – 3 000 €</option><option>3 000 € – 6 000 €</option><option>Plus de 6 000 €</option><option>Abonnement mensuel SEO</option></select></div>
          <div class="field"><label for="delai">Délai souhaité</label>
            <select id="delai" name="delai"><option value="">Pas d'urgence</option><option>Dès que possible</option><option>Sous 1 mois</option><option>Sous 3 mois</option></select></div>
          <div class="field full"><label for="message">Votre projet <span class="req">*</span></label><textarea id="message" name="message" placeholder="Parlez-nous de votre activité, de vos objectifs et de ce que vous attendez de votre site…" required></textarea><p class="error-msg">Décrivez-nous brièvement votre projet.</p></div>
          <div class="field full"><label class="consent"><input type="checkbox" name="consentement" value="oui" required><span>J'accepte que mes données soient utilisées pour être recontacté(e) au sujet de ma demande. <a href="mentions-legales.html#confidentialite">Politique de confidentialité</a></span></label><p class="error-msg">Merci de cocher cette case pour continuer.</p></div>
        </div>
        <button class="btn btn-primary btn-lg btn-block" type="submit" style="margin-top:24px">Envoyer mon message {I["arrow"]}</button>
        <p class="form-note">{I["lock"]} Vos données restent confidentielles et ne sont jamais revendues.</p>
      </form>
      <div class="form-success" role="status">
        <div class="ok">{I["check"]}</div>
        <h2 style="font-size:1.7rem">Merci, votre demande est bien partie !</h2>
        <p>Paulo vous recontacte sous 24 h ouvrées. En attendant, découvrez nos conseils sur le blog.</p>
        <a class="btn btn-outline" href="blog.html">Lire nos conseils {I["arrow"]}</a>
      </div>
    </div>
  </div>
</section>
<section class="section section--tint" aria-label="Plan d'accès">
  <div class="container">
    <div class="section-head text-center"><span class="eyebrow">Nous trouver</span><h2>Omni Digital au Perreux-sur-Marne</h2><p>{ADDRESS}</p></div>
    <div class="map-embed reveal"><iframe title="Plan d'accès à Omni Digital" src="https://www.google.com/maps?q={MAPS_Q}&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head text-center"><span class="eyebrow">Ce qui se passe ensuite</span><h2>Simple, rapide, sans engagement</h2></div>
    <div class="process">
      <div class="step reveal"><div class="step-num">01</div><h3>Vous nous écrivez</h3><p>Formulaire, téléphone ou rendez-vous en ligne.</p></div>
      <div class="step reveal reveal-d1"><div class="step-num">02</div><h3>Appel découverte</h3><p>30 minutes pour comprendre vos objectifs.</p></div>
      <div class="step reveal reveal-d2"><div class="step-num">03</div><h3>Audit & proposition</h3><p>Diagnostic gratuit et proposition détaillée sous 48 h.</p></div>
      <div class="step reveal reveal-d3"><div class="step-num">04</div><h3>Lancement</h3><p>On démarre votre projet dès votre validation.</p></div>
    </div>
  </div>
</section>
</main>
"""
    out += footer()
    return out


def rendezvous():
    out = head("Prendre rendez-vous en ligne — Appel découverte gratuit | Omni Digital",
               "Réservez en ligne un appel découverte gratuit de 30 minutes avec Paulo Da Costa (Omni Digital) : audit SEO offert et conseils personnalisés pour votre site internet.",
               "rendez-vous.html")
    out += header("rendez-vous.html")
    out += "<main id=\"main\">" + page_hero("Rendez-vous en ligne", "Réservez votre <span class=\"hl-orange\">appel découverte</span> gratuit",
                     "Choisissez le créneau qui vous convient : 30 minutes avec Paulo pour analyser votre situation et vous présenter votre audit SEO offert.",
                     [("Prendre rendez-vous", None)], U("1486312338219-ce68d2c6f44d", 1600))
    out += f"""
<section class="section">
  <div class="container">
    <div class="booking reveal" data-booking id="agenda">
      <aside class="booking-side">
        <div class="host"><img src="{PAULO_IMG}" alt="{CONTACT_NAME}, Omni Digital" width="56" height="56"><div><strong>{CONTACT_NAME}</strong><span>Direction & stratégie SEO</span></div></div>
        <h2>Appel découverte & audit SEO offert</h2>
        <ul>
          <li>{I["clock"]} 30 minutes</li>
          <li>{I["video"]} Visioconférence ou téléphone</li>
          <li>{I["search"]} Audit de votre visibilité Google</li>
          <li>{I["shield"]} 100 % gratuit, sans engagement</li>
        </ul>
        <div class="booking-summary" aria-live="polite">Aucun créneau sélectionné pour l'instant.</div>
      </aside>
      <div class="booking-main">
        <div class="booking-steps" aria-hidden="true"><span class="is-active">1. Date & heure</span><span>2. Vos informations</span><span>3. Confirmation</span></div>

        <div class="booking-panel is-active">
          <div class="field" style="margin-bottom:24px"><span class="label">Format du rendez-vous</span>
            <div class="chips">
              <label class="chip"><input type="radio" name="type_rdv" value="Visioconférence" checked><span>🎥 Visioconférence</span></label>
              <label class="chip"><input type="radio" name="type_rdv" value="Appel téléphonique"><span>📞 Téléphone</span></label>
              <label class="chip"><input type="radio" name="type_rdv" value="Rendez-vous sur place"><span>🤝 Sur place</span></label>
            </div>
          </div>
          <div class="cal-head"><h3 class="cal-title">Mois</h3><div class="cal-nav"><button type="button" class="cal-prev" aria-label="Mois précédent">{I["left"]}</button><button type="button" class="cal-next" aria-label="Mois suivant">{I["right"]}</button></div></div>
          <div class="cal-grid" role="group" aria-label="Calendrier"></div>
          <div class="slots-wrap"><h4 class="slots-title">Choisissez une date</h4><div class="slots" role="group" aria-label="Créneaux horaires"></div></div>
          <div class="booking-actions"><span></span><button type="button" class="btn btn-primary" data-to-step="2" disabled>Continuer {I["arrow"]}</button></div>
        </div>

        <div class="booking-panel">
          <form novalidate>
            <div class="hp-field" aria-hidden="true"><label>Ne pas remplir<input type="text" name="_gotcha" tabindex="-1" autocomplete="off"></label></div>
            <div class="form-grid">
              <div class="field"><label for="b-nom">Nom & prénom <span class="req">*</span></label><input id="b-nom" name="nom" autocomplete="name" required><p class="error-msg">Merci d'indiquer votre nom.</p></div>
              <div class="field"><label for="b-ent">Entreprise</label><input id="b-ent" name="entreprise" autocomplete="organization"></div>
              <div class="field"><label for="b-email">E-mail <span class="req">*</span></label><input id="b-email" name="email" type="email" autocomplete="email" required><p class="error-msg">Merci d'indiquer un e-mail valide.</p></div>
              <div class="field"><label for="b-tel">Téléphone <span class="req">*</span></label><input id="b-tel" name="telephone" type="tel" autocomplete="tel" required><p class="error-msg">Merci d'indiquer un numéro valide.</p></div>
              <div class="field full"><label for="b-site">Votre site internet (pour préparer l'audit)</label><input id="b-site" name="site_actuel" type="url" placeholder="https://"></div>
              <div class="field full"><label for="b-msg">Un mot sur votre projet</label><textarea id="b-msg" name="message" style="min-height:100px" placeholder="Vos objectifs, vos questions…"></textarea></div>
              <div class="field full"><label class="consent"><input type="checkbox" name="consentement" value="oui" required><span>J'accepte que mes données soient utilisées pour organiser ce rendez-vous. <a href="mentions-legales.html#confidentialite">Confidentialité</a></span></label><p class="error-msg">Merci de cocher cette case pour continuer.</p></div>
            </div>
            <div class="booking-actions"><button type="button" class="btn btn-outline" data-to-step="1">{I["left"]} Retour</button><button type="submit" class="btn btn-primary">Confirmer le rendez-vous {I["arrow"]}</button></div>
          </form>
        </div>

        <div class="booking-panel">
          <div class="form-success" style="display:block" role="status">
            <div class="ok">{I["check"]}</div>
            <h2 style="font-size:1.7rem">C'est noté, à très vite !</h2>
            <p><strong class="confirm-when"></strong><br><span class="confirm-type"></span></p>
            <p>Vous allez recevoir une confirmation par e-mail. Pensez à ajouter le rendez-vous à votre agenda.</p>
            <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap"><a class="btn btn-primary ics-link" href="#">{I["calendar"]} Ajouter à mon agenda</a><a class="btn btn-outline" href="portfolio.html">Voir nos réalisations</a></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
<section class="section section--tint">
  <div class="container">
    <div class="section-head text-center"><span class="eyebrow">Pendant l'appel</span><h2>30 minutes pour y voir clair</h2></div>
    <div class="grid grid-3">
      <div class="card reveal"><div class="icon-box">{I["search"]}</div><h3>Diagnostic de votre visibilité</h3><p>Où apparaissez-vous sur Google ? Qui sont vos concurrents directs ? Nous vous montrons tout, chiffres à l'appui.</p></div>
      <div class="card reveal reveal-d1"><div class="icon-box icon-box--orange">{I["target"]}</div><h3>Vos objectifs & priorités</h3><p>Plus d'appels, plus de devis, plus de ventes en ligne ? Nous définissons ensemble ce qui compte vraiment.</p></div>
      <div class="card reveal reveal-d2"><div class="icon-box">{I["rocket"]}</div><h3>Un plan d'action concret</h3><p>Vous repartez avec 5 recommandations prioritaires, que vous travailliez avec nous ou non.</p></div>
    </div>
  </div>
</section>
</main>
"""
    out += footer()
    return out


def blog():
    out = head("Blog — Conseils SEO, création de site & digital pour PME | Omni Digital",
               "Conseils pratiques en référencement naturel, SEO local, création de site internet et transformation digitale pour les PME. Guides pratiques et actionnables.",
               "blog.html")
    out += header("blog.html")
    out += "<main id=\"main\">" + page_hero("Blog & ressources", "Les conseils web & SEO <span class=\"hl-orange\">qui font la différence</span>",
                     "Guides pratiques, retours d'expérience et bonnes pratiques pour développer la visibilité de votre PME sur Google.",
                     [("Blog", None)], U("1432888498266-38ffec3eaf0a", 1600))
    f = POSTS[0]
    cats = sorted({p["cat"] for p in POSTS}, key=lambda c: [p["cat"] for p in POSTS].index(c))
    fb = '<button class="filter-btn is-active" data-filter="all" aria-pressed="true">Tous</button>' + "".join(
        f'<button class="filter-btn" data-filter="{c.lower().replace(" ", "-")}" aria-pressed="false">{c}</button>' for c in cats)
    out += f"""
<section class="section">
  <div class="container">
    <article class="post-featured reveal">
      <a class="thumb" href="blog/{f['slug']}.html" tabindex="-1" aria-hidden="true"><img src="{U(f['img'], 1100)}" alt="" width="1100" height="700"></a>
      <div class="body">
        <div class="post-meta"><span class="post-cat">À la une</span><span class="post-cat" style="background:var(--blue-100);color:var(--blue-600)">{f['cat']}</span><time datetime="{f['date']}">{f['date_h']}</time></div>
        <h2><a href="blog/{f['slug']}.html">{f['title']}</a></h2>
        <p>{f['excerpt']}</p>
        <div>{btn_arrow("Lire l'article", "blog/" + f['slug'] + ".html")}</div>
      </div>
    </article>

    <div class="blog-tools">
      <div class="filters" data-filter-group=".post-card" role="group" aria-label="Filtrer par catégorie">{fb}</div>
      <label class="search-box"><span class="sr-only">Rechercher un article</span>{I["search"]}<input type="search" placeholder="Rechercher un article…" data-search=".post-card"></label>
    </div>
    <div class="grid grid-3">{"".join(post_card(p, "", f" reveal-d{i % 3}") for i, p in enumerate(POSTS))}
    </div>
    <p class="empty-state" data-empty=".post-card">Aucun article ne correspond à votre recherche.</p>
  </div>
</section>
"""
    out += cta_band(title="Vous préférez qu'on s'en occupe pour vous ?", text="Nous appliquons ces méthodes chaque jour pour nos clients. Demandez votre audit SEO gratuit.")
    out += "</main>" + footer()
    return out


def legal():
    out = head("Mentions légales & politique de confidentialité | Omni Digital",
               "Mentions légales et politique de confidentialité du site Omni Digital, agence web et SEO pour PME.", "mentions-legales.html")
    out += header("")
    out += "<main id=\"main\">" + page_hero("Informations légales", "Mentions légales & confidentialité", "Transparence et protection de vos données personnelles.",
                     [("Mentions légales", None)], U("1497366216548-37526070297c", 1600))
    out += f"""
<section class="section">
  <div class="container legal prose">
    <!-- À COMPLÉTER avec les informations légales réelles de l'entreprise -->
    <h2>Éditeur du site</h2>
    <p><strong>Omni Digital</strong><br>Forme juridique : [à compléter] — Capital : [à compléter]<br>Siège social : {ADDRESS}<br>SIRET : [à compléter] — RCS : [à compléter]<br>TVA intracommunautaire : [à compléter]<br>E-mail : <a href="mailto:{EMAIL}">{EMAIL}</a> — Téléphone : {PHONE}<br>Responsable de la publication : {CONTACT_NAME}</p>
    <h2>Hébergement</h2>
    <p>[Nom de l'hébergeur, adresse et téléphone à compléter]</p>
    <h2>Propriété intellectuelle</h2>
    <p>L'ensemble des contenus de ce site (textes, graphismes, logo, code) est la propriété d'Omni Digital, sauf mention contraire. Les photographies proviennent de la banque d'images Unsplash et sont utilisées conformément à sa licence. Toute reproduction sans autorisation est interdite.</p>
    <h2 id="confidentialite">Politique de confidentialité</h2>
    <p>Les informations recueillies via nos formulaires (contact, rendez-vous, newsletter) sont utilisées uniquement pour répondre à vos demandes et, si vous y avez consenti, vous envoyer nos conseils. Elles ne sont jamais vendues ni cédées à des tiers.</p>
    <ul>
      <li><strong>Base légale :</strong> votre consentement et l'exécution de mesures précontractuelles.</li>
      <li><strong>Durée de conservation :</strong> 3 ans à compter du dernier contact.</li>
      <li><strong>Vos droits :</strong> accès, rectification, effacement, opposition et portabilité, en écrivant à <a href="mailto:{EMAIL}">{EMAIL}</a>.</li>
      <li>Vous pouvez introduire une réclamation auprès de la CNIL (cnil.fr).</li>
    </ul>
    <h2>Cookies</h2>
    <p>Ce site peut utiliser des cookies de mesure d'audience anonymisés. Vous pouvez accepter ou refuser leur dépôt via le bandeau prévu à cet effet ; votre choix est conservé dans votre navigateur.</p>
  </div>
</section>
</main>
"""
    out += footer()
    return out


def notfound():
    out = head("Page introuvable | Omni Digital", "La page demandée est introuvable.", "404.html", root="/")
    out = out.replace('<meta name="robots" content="index, follow">', '<meta name="robots" content="noindex">')
    out += header("", root="/")
    out += f"""
<main id="main">
<section class="notfound">
  <div class="container">
    <div class="code">404</div>
    <h1 style="font-size:2rem">Oups, cette page s'est égarée…</h1>
    <p>Mais pas d'inquiétude : contrairement à cette page, votre site, lui, peut être trouvé facilement sur Google.</p>
    <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap">{btn_arrow("Retour à l'accueil", "/index.html")}<a class="btn btn-outline" href="/contact.html">Nous contacter</a></div>
  </div>
</section>
</main>
"""
    out += footer(root="/")
    return out
