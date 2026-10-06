"""Génère la page d'accueil au format Elementor (JSON + CSS) pour le WordPress.

Usage : python3 _src/elementor_home.py
Sortie : wordpress/elementor-accueil.json (éléments + réglages de page, CSS inclus)
"""
import json
import os
import random

from common import EMAIL, PHONE, PHONE_LINK, STREET, POSTCODE, CITY, CONTACT_NAME, GOOGLE_REVIEWS_URL
from data import PROJECTS, TESTIMONIALS
from pages import SERVICES
from parts import FAQ_HOME

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WP = "https://claude.omnidigital.fr"
URL = {
    "home": WP + "/", "services": WP + "/services/", "portfolio": WP + "/portfolio/", "apropos": WP + "/a-propos/",
    "blog": WP + "/blog/", "contact": WP + "/contact/", "rdv": WP + "/contact/audit-gratuit/",
    "confidentialite": WP + "/politique-de-confidentialite/",
    "maps": "https://www.google.com/maps/search/?api=1&query=25+Rue+Jean+d%27Estienne+d%27Orves,+94170+Le+Perreux-sur-Marne",
}
# Médias importés dans la médiathèque WordPress (id, url)
MEDIA = {
    "logo_h": (3959, WP + "/wp-content/uploads/2026/10/od-logo-omni-digital-horizontal.png"),
    "logo_full": (3960, WP + "/wp-content/uploads/2026/10/od-logo-omni-digital-creative-agency.png"),
    "digitalreseau.fr": (3961, WP + "/wp-content/uploads/2026/10/od-portfolio-digitalreseau.webp"),
    "lesbrascasses.fr": (3962, WP + "/wp-content/uploads/2026/10/od-portfolio-lesbrascasses.webp"),
    "brokenarms.fr": (3963, WP + "/wp-content/uploads/2026/10/od-portfolio-brokenarms.webp"),
    "pratik-informatique.fr": (3964, WP + "/wp-content/uploads/2026/10/od-portfolio-pratik-informatique.webp"),
    "photo_hero": (3965, WP + "/wp-content/uploads/2026/10/od-atelier-strategie-web.jpg"),
    "photo_why": (3966, WP + "/wp-content/uploads/2026/10/od-atelier-client-pme.jpg"),
}
MENU_SLUG = "omni-digital-navigation"
HEAD_FONT, BODY_FONT = "Plus Jakarta Sans", "Inter"

random.seed(42)  # identifiants stables d'une génération à l'autre
_ids = set()


def uid():
    while True:
        i = "%07x" % random.getrandbits(28)
        if i not in _ids:
            _ids.add(i)
            return i


def px(v):
    return {"unit": "px", "size": v, "sizes": []}


def pad(t, r=None, b=None, l=None):
    r = t if r is None else r
    b = t if b is None else b
    l = r if l is None else l
    return {"unit": "px", "top": str(t), "right": str(r), "bottom": str(b), "left": str(l), "isLinked": False}


def icon(name, lib="fa-solid"):
    return {"value": name, "library": lib}


# ---------- éléments ----------
def con(cls="", children=(), direction="column", gap=None, boxed=False, width=None, wrap=False, justify=None,
        align=None, padding=None, tag=None, link=None, **extra):
    s = {"content_width": "boxed" if boxed else "full", "flex_direction": direction, "css_classes": cls,
         "padding": padding or pad(0)}
    if boxed:
        s["boxed_width"] = px(1200)
    if gap is not None:
        s["flex_gap"] = {"unit": "px", "size": gap, "column": str(gap), "row": str(gap), "isLinked": True}
    if width is not None:
        s["width"] = {"unit": "%", "size": width}
        s["width_mobile"] = {"unit": "%", "size": 100}
    if wrap:
        s["flex_wrap"] = "wrap"
    if justify:
        s["flex_justify_content"] = justify
    if align:
        s["flex_align_items"] = align
    if tag:
        s["html_tag"] = tag
    if link:
        s["html_tag"] = "a"
        s["link"] = {"url": link, "is_external": "on" if link.startswith("http") and WP not in link else ""}
    s.update(extra)
    return {"id": uid(), "elType": "container", "isInner": False, "settings": s, "elements": list(children)}


def widget(kind, settings, cls=""):
    if cls:
        settings["_css_classes"] = cls
    return {"id": uid(), "elType": "widget", "widgetType": kind, "settings": settings, "elements": []}


def font(settings, family, weight, prefix="typography"):
    settings[prefix + "_typography"] = "custom"
    settings[prefix + "_font_family"] = family
    settings[prefix + "_font_weight"] = str(weight)
    return settings


def heading(text, tag="h2", cls="", link=None):
    s = font({"title": text, "header_size": tag}, HEAD_FONT, 800)
    if link:
        s["link"] = {"url": link}
    return widget("heading", s, cls)


def text(html, cls=""):
    return widget("text-editor", font({"editor": html}, BODY_FONT, 400), cls)


def eyebrow(label):
    return widget("heading", font({"title": label, "header_size": "div"}, BODY_FONT, 700), "od-eyebrow")


def button(label, url, style="primary", external=False, cls=""):
    s = font({"text": label, "link": {"url": url, "is_external": "on" if external else ""}}, BODY_FONT, 700)
    return widget("button", s, f"od-btn od-btn--{style} {cls}".strip())


def image(media_key, cls="", link=None, alt=None):
    mid, url = MEDIA[media_key]
    s = {"image": {"id": mid, "url": url, "source": "library"}, "image_size": "full"}
    if link:
        s["link_to"] = "custom"
        s["link"] = {"url": link, "is_external": "on" if WP not in link else ""}
    return widget("image", s, cls)


def ico(name, cls="", lib="fa-solid"):
    return widget("icon", {"selected_icon": icon(name, lib)}, cls)


def icon_list(items, inline=False, cls=""):
    s = {"icon_list": [], "view": "inline" if inline else "traditional"}
    for it in items:
        txt, ic = it[0], it[1]
        row = {"_id": uid(), "text": txt, "selected_icon": icon(*ic) if isinstance(ic, tuple) else icon(ic)}
        if len(it) > 2 and it[2]:
            row["link"] = {"url": it[2], "is_external": "on" if WP not in it[2] and not it[2].startswith(("tel:", "mailto:")) else ""}
        s["icon_list"].append(row)
    return widget("icon-list", font(s, BODY_FONT, 500, "icon_typography"), cls)


def section_head(eb, title, sub=None, center=True):
    kids = [eyebrow(eb)] if eb else []
    kids.append(heading(title, "h2"))
    if sub:
        kids.append(text(f"<p>{sub}</p>", "od-lead"))
    return con("od-section-head" + (" od-center" if center else ""), kids, gap=0)


def section(cls, children, tint=None, padding=(104, 24)):
    extra = {}
    return con("od-section " + cls, children, boxed=True, gap=0, padding=pad(padding[0], padding[1]),
               padding_mobile=pad(64, 16), tag="section", **extra)


# ---------- contenu ----------
SERVICE_ICONS = {"monitor": "fas fa-desktop", "search": "fas fa-search", "map": "fas fa-map-marked-alt", "rocket": "fas fa-rocket"}
SERVICE_ANCHOR = URL["services"]


def topbar():
    left = icon_list([(PHONE, "fas fa-phone-alt", "tel:" + PHONE_LINK), (EMAIL, "fas fa-envelope", "mailto:" + EMAIL),
                      (f"{CITY} (94)", "fas fa-map-marker-alt", URL["maps"])], inline=True, cls="od-topbar-list")
    right = text(f'<p><a href="{URL["rdv"]}">Audit SEO offert, réservez votre appel →</a></p>', "od-topbar-link")
    right["settings"]["hide_mobile"] = "hidden-mobile"
    return con("od-topbar", [left, right], direction="row", boxed=True, justify="space-between", align="center",
               padding=pad(8, 24), padding_mobile=pad(8, 16), background_background="classic", background_color="#061A2E")


def header():
    logo = image("logo_h", "od-logo", link=URL["home"])
    nav = widget("nav-menu", font({
        "menu": MENU_SLUG, "layout": "horizontal", "align_items": "center", "pointer": "underline",
        "animation_line": "fade", "dropdown": "tablet", "toggle": "burger", "full_width": "stretch",
        "color_menu_item": "#0C1D2E", "color_menu_item_hover": "#0A6AA8", "pointer_color_menu_item_hover": "#DC3A2C",
        "color_menu_item_active": "#0A6AA8", "pointer_color_menu_item_active": "#DC3A2C",
        "padding_horizontal_menu_item": px(12), "toggle_color": "#0C1D2E", "toggle_size": px(26),
        "color_dropdown_item": "#0C1D2E", "background_color_dropdown_item": "#FFFFFF",
        "color_dropdown_item_hover": "#0A6AA8", "background_color_dropdown_item_hover": "#F0F9FD",
        "color_dropdown_item_active": "#0A6AA8", "background_color_dropdown_item_active": "#F0F9FD",
        "menu_typography_font_size": px(16), "_flex_size": "grow",
    }, BODY_FONT, 600, "menu_typography"), "od-nav")
    rdv = button("Prendre RDV", URL["rdv"], "outline", cls="od-btn--sm")
    rdv["settings"]["hide_tablet"] = "hidden-tablet"
    rdv["settings"]["hide_mobile"] = "hidden-mobile"
    cta = button("Parlons-en", URL["contact"], "primary", cls="od-btn--sm")
    cta["settings"]["hide_mobile"] = "hidden-mobile"
    actions = con("od-header-actions", [rdv, cta], direction="row", gap=12, align="center")
    return con("od-header", [logo, nav, actions], direction="row", boxed=True, justify="space-between", align="center",
               gap=20, padding=pad(8, 24), padding_mobile=pad(6, 16), background_background="classic",
               background_color="#FFFFFF", sticky="top", sticky_on=["desktop", "tablet", "mobile"])


def hero():
    left = con("od-hero-text", [
        eyebrow("Agence web & SEO pour PME"),
        heading('Votre site web devient votre <span class="od-hl">meilleur commercial</span>.', "h1"),
        text("<p>Omni Digital crée, modernise et référence les sites des PME pour qu'ils <strong>apparaissent en haut de Google</strong> "
             "et transforment chaque visiteur en demande de contact.</p>", "od-hero-lead"),
        con("od-actions", [button("Parlons de votre projet", URL["contact"], "primary", cls="od-btn--lg od-btn--arrow"),
                           button("Audit SEO offert", URL["rdv"], "outline", cls="od-btn--lg")], direction="row", gap=14, wrap=True),
        con("od-hero-proof", [ico("fab fa-google", "od-google-badge", "fa-brands"),
                              text(f"<p><strong>5,0/5 sur Google</strong><br><span>Lire les {len(TESTIMONIALS)} avis de nos clients →</span></p>")],
            direction="row", gap=14, align="center", link=GOOGLE_REVIEWS_URL),
    ], gap=0, width=52)
    floats = [
        ("od-float od-float--a", "fas fa-chart-line", "Visible", "sur Google & Google Maps", "od-ic--green"),
        ("od-float od-float--b", "fas fa-comments", "+ de contacts", "appels, formulaires, RDV", "od-ic--coral"),
        ("od-float od-float--c", "fab fa-google", "SEO local", "fiche Google optimisée", "od-ic--blue"),
    ]
    vis = [image("photo_hero", "od-hero-photo")]
    for cls, ic, t, sub, icc in floats:
        lib = "fa-brands" if ic.startswith("fab") else "fa-solid"
        vis.append(con(cls, [ico(ic, "od-float-ic " + icc, lib), text(f"<p><strong>{t}</strong><br><span>{sub}</span></p>")],
                       direction="row", gap=12, align="center"))
    right = con("od-hero-visual", vis, width=48)
    return section("od-hero", [con("od-split", [left, right], direction="row", gap=64, align="center",
                                   flex_direction_mobile="column", flex_direction_tablet="column")], padding=(88, 24))


def tools():
    items = [("WordPress", "fab fa-wordpress"), ("Elementor", "fab fa-elementor"), ("Shopify", "fab fa-shopify"),
             ("Google Analytics 4", "fas fa-chart-bar"), ("Search Console", "fas fa-search"),
             ("Semrush", "fas fa-chart-line"), ("Google Business", "fas fa-map-marked-alt")]
    items = [(n, (i, "fa-brands" if i.startswith("fab") else "fa-solid")) for n, i in items]
    return section("od-tools", [text("<p>Les outils et plateformes que nous maîtrisons</p>", "od-tools-label"),
                                icon_list(items, inline=True, cls="od-tools-list")], padding=(40, 24))


def services():
    cards = []
    for i, (anchor, ic, t, d, li) in enumerate(SERVICES):
        lis = "".join(f"<li>{x}</li>" for x in li)
        cards.append(con("od-card od-service", [
            heading(f"0{i + 1}", "div", "od-num"),
            ico(SERVICE_ICONS[ic], "od-iconbox" + (" od-iconbox--coral" if i % 2 else "")),
            heading(t, "h3"),
            text(f"<p>{d}</p><ul>{lis}</ul>"),
            button("En savoir plus", SERVICE_ANCHOR, "link"),
        ], gap=0, width=23, width_tablet={"unit": "%", "size": 48}, padding=pad(34), padding_mobile=pad(26)))
    return section("od-services", [
        section_head("Nos expertises", 'Tout ce qu\'il faut pour <span class="od-hl">gagner des clients</span> en ligne',
                     "Une seule agence pour concevoir votre site, le rendre visible sur Google et faire entrer votre PME dans l'ère du digital."),
        con("od-grid", cards, direction="row", wrap=True, gap=24, justify="space-between"),
    ])


def why():
    checks = [
        ("<strong>Un interlocuteur unique</strong> qui connaît votre entreprise et vous répond sous 24 h ouvrées.",),
        ("<strong>Des sites rapides</strong> et sécurisés, optimisés pour les critères de Google.",),
        ("<strong>Un reporting clair</strong> : positions, trafic, appels et formulaires reçus.",),
        ("<strong>Vous restez propriétaire</strong> de votre site, domaine et contenus. Sans engagement caché.",),
    ]
    media = con("od-why-media", [image("photo_why", "od-photo"),
                                 con("od-badge", [heading("1", "div", "od-badge-num"),
                                                  text("<p>interlocuteur unique, du début à la fin</p>")], gap=0, padding=pad(22, 26))],
                width=48)
    body = con("od-why-text", [
        eyebrow("Pourquoi Omni Digital"),
        heading('Un partenaire qui parle <span class="od-hl-underline">résultats</span>, pas jargon.', "h2"),
        text("<p>Nous savons qu'un dirigeant de PME n'a pas de temps à perdre. Notre rôle : vous apporter des clients, simplement, "
             "avec un interlocuteur unique et des résultats mesurables chaque mois.</p>"),
        icon_list([(c[0], "fas fa-check") for c in checks], cls="od-checks"),
        button("Découvrir notre approche", URL["apropos"], "primary", cls="od-btn--arrow"),
    ], gap=0, width=48)
    return section("od-why od-tint", [con("od-split", [media, body], direction="row", gap=72, align="center",
                                         flex_direction_mobile="column", flex_direction_tablet="column")])


def engagements():
    stats = [(24, "", "h", "pour vous répondre (jours ouvrés)"), (1, "", "", "interlocuteur unique, du début à la fin"),
             (0, "", "€", "pour l'audit et le premier échange"), (100, "", "%", "propriétaire de votre site et de vos contenus")]
    cards = [widget("counter", font(font({"starting_number": 0, "ending_number": n, "prefix": pre, "suffix": suf, "title": t,
                                          "thousand_separator": ""}, HEAD_FONT, 800, "typography_number"), BODY_FONT, 400, "typography_title"),
                    "od-stat") for n, pre, suf, t in stats]
    return section("od-engagements od-navy", [
        section_head("Nos engagements", "Ce que vous pouvez attendre de nous"),
        con("od-stats", cards, direction="row", wrap=True, gap=24, justify="space-between"),
    ])


def method():
    steps = [("Audit gratuit", "Nous analysons votre site, votre visibilité Google et vos concurrents."),
             ("Stratégie", "Un plan d'action clair, chiffré et priorisé selon vos objectifs."),
             ("Création & SEO", "Design, développement, contenus et optimisation technique."),
             ("Croissance", "Suivi mensuel, améliorations continues et reporting des résultats.")]
    cards = [con("od-step", [heading(f"0{i + 1}", "div", "od-step-num"), heading(t, "h3"), text(f"<p>{d}</p>")],
                 gap=0, width=23, width_tablet={"unit": "%", "size": 48}, align="center")
             for i, (t, d) in enumerate(steps)]
    return section("od-method", [
        section_head("Notre méthode", 'Du premier appel aux premiers clients, <span class="od-hl">en 4 étapes</span>',
                     "Une méthode simple, transparente et sans surprise."),
        con("od-steps", cards, direction="row", wrap=True, gap=24, justify="space-between"),
    ])


def portfolio():
    cards = []
    for p in PROJECTS[:3]:
        cards.append(con("od-card od-project", [
            con("od-browser", [text(f"<p>{p['domain']}</p>", "od-browser-bar"),
                               image(p["domain"], "od-browser-screen", link=p["url"])], gap=0),
            con("od-project-body", [heading(p["tag"], "div", "od-kind"), heading(p["title"], "h3"), text(f"<p>{p['text']}</p>"),
                                    button("Visiter le site", p["url"], "link", external=True)], gap=0, padding=pad(26, 28, 28)),
        ], gap=0, width=31.5, width_tablet={"unit": "%", "size": 100}))
    head = con("od-head-row", [con("", [eyebrow("Portfolio"), heading('Quelques <span class="od-hl">réalisations</span>', "h2")], gap=0),
                               button("Voir le portfolio", URL["portfolio"], "outline", cls="od-btn--arrow")],
               direction="row", justify="space-between", align="end", wrap=True, gap=24)
    return section("od-portfolio od-tint", [head, con("od-grid", cards, direction="row", wrap=True, gap=28, justify="space-between")])


def reviews():
    cards = []
    for t in TESTIMONIALS:
        cards.append(con("od-card od-review", [
            con("od-review-top", [ico("fas fa-quote-left", "od-quote"), text("<p>★★★★★</p>", "od-stars")],
                direction="row", justify="space-between", align="center"),
            text("<p>" + t["text"].replace("\n\n", "</p><p>").replace("\n", "<br>") + "</p>", "od-review-text"),
            con("od-review-who", [ico("fab fa-google", "od-google-badge od-google-badge--sm", "fa-brands"),
                                  text(f"<p><strong>{t['name']}</strong><br><span>Avis Google</span></p>")],
                direction="row", gap=12, align="center"),
        ], gap=0, width=31.5, width_tablet={"unit": "%", "size": 100}, padding=pad(32), padding_mobile=pad(26)))
    cta = con("od-reviews-cta", [
        ico("fab fa-google", "od-google-badge od-google-badge--lg", "fa-brands"),
        con("od-reviews-cta-text", [heading(f"5,0/5 sur Google, {len(TESTIMONIALS)} avis", "h3"),
                                    text("<p>Des avis publics et vérifiables, laissés par nos clients sur notre fiche Google.</p>")], gap=0),
        button("Lire les avis sur Google", GOOGLE_REVIEWS_URL, "primary", external=True, cls="od-btn--arrow"),
    ], direction="row", gap=28, align="center", padding=pad(30, 36), padding_mobile=pad(26, 22), flex_direction_mobile="column")
    return section("od-reviews", [section_head("Avis clients", "Ce que disent nos clients"),
                                  con("od-grid", cards, direction="row", wrap=True, gap=28, justify="space-between"), cta])


def blog():
    posts = widget("posts", {
        "_skin": "cards", "cards_columns": "3", "cards_columns_tablet": "2", "cards_columns_mobile": "1",
        "cards_posts_per_page": 3, "cards_show_excerpt": "yes", "cards_excerpt_length": 22, "cards_meta_data": ["date"],
        "cards_read_more_text": "Lire l'article →", "cards_show_badge": "yes", "cards_badge_taxonomy": "category",
        "cards_show_avatar": "", "cards_thumbnail_size_size": "medium_large", "cards_item_ratio": {"unit": "px", "size": 0.62},
        "posts_post_type": "post", "cards_column_gap": px(28), "cards_row_gap": px(28),
    }, "od-posts")
    head = con("od-head-row", [con("", [eyebrow("Blog & conseils"), heading("Conseils & bonnes pratiques", "h2")], gap=0),
                               button("Tous les articles", URL["blog"], "outline", cls="od-btn--arrow")],
               direction="row", justify="space-between", align="end", wrap=True, gap=24)
    return section("od-blog od-tint", [head, posts])


def faq():
    tabs = [{"_id": uid(), "tab_title": q, "tab_content": f"<p>{a}</p>"} for q, a in FAQ_HOME]
    tog = widget("toggle", font({"tabs": tabs, "selected_icon": icon("fas fa-plus"), "selected_active_icon": icon("fas fa-times"),
                                 "icon_align": "right", "title_html_tag": "h3"}, BODY_FONT, 700, "title_typography"), "od-faq")
    return section("od-faq-section", [section_head("FAQ", "Vos questions, nos réponses"), tog])


def cta_band():
    left = con("od-cta-text", [heading("Prêt à attirer plus de clients grâce au web ?", "h2"),
                               text("<p>Parlez-nous de votre projet : nous vous répondons sous 24 h ouvrées avec un premier diagnostic gratuit et sans engagement.</p>")],
               gap=0, width=58)
    right = con("od-cta-actions", [button("Parlons de votre projet", URL["contact"], "primary", cls="od-btn--lg od-btn--block od-btn--arrow"),
                                   button("Réserver un appel de 30 min", URL["rdv"], "ghost", cls="od-btn--lg od-btn--block"),
                                   text("<p>✔ Gratuit · ✔ Sans engagement · ✔ Réponse sous 24 h</p>", "od-cta-note")], gap=14, width=36)
    band = con("od-cta-band", [left, right], direction="row", gap=40, align="center", justify="space-between",
               padding=pad(72, 72), padding_mobile=pad(40, 24), flex_direction_mobile="column", flex_direction_tablet="column")
    return section("od-cta", [band], padding=(40, 24))


def footer():
    col1 = con("od-foot-brand", [
        image("logo_full", "od-footer-logo", link=URL["home"]),
        text("<p>Agence web dédiée aux PME : création de sites internet, référencement naturel (SEO) et accompagnement "
             "à la transformation digitale pour générer plus de contacts.</p>"),
    ], gap=0, width=28)

    def links(title, items):
        return con("od-foot-col", [heading(title, "h4"), icon_list([(t, "fas fa-angle-right", u) for t, u in items], cls="od-foot-links")],
                   gap=0, width=18)

    col2 = links("Services", [("Création de site web", URL["services"]), ("Référencement SEO", URL["services"]),
                              ("SEO local & Google Maps", URL["services"]), ("Refonte & optimisation", URL["services"]),
                              ("Transformation digitale", URL["services"])])
    col3 = links("Agence", [("À propos", URL["apropos"]), ("Portfolio", URL["portfolio"]), ("Blog", URL["blog"]),
                            ("Nous contacter", URL["contact"]), ("Prendre rendez-vous", URL["rdv"]), ("Nos avis Google", GOOGLE_REVIEWS_URL)])
    col4 = con("od-foot-col", [heading("Contact", "h4"), icon_list([
        (CONTACT_NAME, "fas fa-user"), (f"{STREET}, {POSTCODE} {CITY}", "fas fa-map-marker-alt", URL["maps"]),
        (PHONE, "fas fa-phone-alt", "tel:" + PHONE_LINK), (EMAIL, "fas fa-envelope", "mailto:" + EMAIL)], cls="od-foot-contact")],
        gap=0, width=24)
    top = con("od-foot-top", [col1, col2, col3, col4], direction="row", wrap=True, gap=40, justify="space-between",
              flex_direction_mobile="column")
    bottom = con("od-foot-bottom", [
        text("<p>© 2026 Omni Digital, agence web & SEO pour PME. Tous droits réservés.</p>"),
        text(f'<p><a href="{URL["confidentialite"]}">Politique de confidentialité</a></p>'),
    ], direction="row", justify="space-between", wrap=True, gap=16)
    return con("od-footer", [top, bottom], boxed=True, gap=0, padding=pad(80, 24, 0), padding_mobile=pad(56, 16, 0),
               tag="footer", background_background="classic", background_color="#061A2E")


CSS = r"""
/* ===== Omni Digital : page d'accueil (styles complémentaires Elementor) ===== */
selector { --od-ink:#0C1D2E; --od-text:#435866; --od-muted:#5B6F7C; --od-line:#E0EBF0; --od-tint:#F0F9FD; --od-blue:#0A6AA8;
  --od-blue2:#0E86C6; --od-blue-light:#DCF2FA; --od-navy:#0A2540; --od-navy-deep:#061A2E; --od-coral:#DC3A2C; --od-coral-dark:#B92C21;
  --od-coral-light:#FF6A5A; --od-coral-tint:#FFEAE7; --od-cyan:#5CE1E6; --od-green:#8FDD6E; --od-grad:linear-gradient(120deg,#5CE1E6,#8FDD6E);
  --od-shadow:0 10px 30px -12px rgba(10,37,64,.18); --od-shadow-lg:0 30px 60px -20px rgba(10,37,64,.28); }
selector, selector .elementor-widget-text-editor { color: var(--od-text); font-family: "Inter", sans-serif; font-size: 17px; line-height: 1.7; }
selector .elementor-heading-title { color: var(--od-ink); letter-spacing: -0.02em; }
selector .elementor-widget-heading .elementor-heading-title { line-height: 1.15; }
selector h1.elementor-heading-title { font-size: clamp(2.2rem, 4.2vw, 3.4rem); margin-bottom: 22px; }
selector h2.elementor-heading-title { font-size: clamp(1.9rem, 3.4vw, 2.8rem); margin-bottom: 14px; }
selector h3.elementor-heading-title { font-size: 1.3rem; font-weight: 700; margin: 0 0 10px; }
selector .elementor-widget-text-editor p:last-child { margin-bottom: 0; }
selector .od-hl { color: var(--od-blue2); }
selector .od-hl-underline { background: linear-gradient(transparent 62%, rgba(92,225,230,.5) 62%); padding: 0 .1em; }
selector a { transition: color .2s; }

/* Pastille de section */
selector .od-eyebrow .elementor-heading-title { display: inline-flex; align-items: center; gap: 8px; font-size: .8rem; letter-spacing: .14em;
  text-transform: uppercase; color: var(--od-blue); background: var(--od-blue-light); padding: 7px 14px; border-radius: 999px; margin-bottom: 18px; line-height: 1.2; }
selector .od-eyebrow .elementor-heading-title::before { content: ""; width: 8px; height: 8px; border-radius: 50%; background: var(--od-grad); box-shadow: 0 0 0 3px rgba(92,225,230,.2); }
selector .od-navy .od-eyebrow .elementor-heading-title { background: rgba(255,255,255,.08); color: #A8E6EE; }
selector .od-section-head { max-width: 760px; margin-bottom: 52px; }
selector .od-section-head.od-center { margin-left: auto; margin-right: auto; text-align: center; align-items: center; }
selector .od-lead p { font-size: 1.12rem; color: var(--od-muted); }

/* Sections */
selector .od-tint { background: var(--od-tint); }
selector .od-navy { background: var(--od-navy); }
selector .od-navy .elementor-heading-title { color: #fff; }
selector .od-navy .od-lead p { color: #A3C0CF; }

/* Boutons */
selector .od-btn .elementor-button { border-radius: 999px; padding: 15px 28px; font-size: 16px; line-height: 1; border: 2px solid transparent; text-transform: none; letter-spacing: normal; font-family: "Inter", sans-serif; font-weight: 700;
  transition: transform .25s, box-shadow .25s, background-color .2s, color .2s, border-color .2s; }
selector .od-btn--sm .elementor-button { padding: 11px 20px; font-size: 15px; }
selector .od-btn--lg .elementor-button { padding: 19px 32px; font-size: 17px; }
selector .od-btn--block, selector .od-btn--block .elementor-button { width: 100%; }
selector .od-btn--arrow .elementor-button-text::after { content: " →"; }
selector .od-btn--primary .elementor-button { background: var(--od-coral); color: #fff; box-shadow: 0 12px 24px -10px rgba(220,58,44,.55); }
selector .od-btn--primary .elementor-button:hover { background: var(--od-coral-dark); color: #fff; transform: translateY(-2px); }
selector .od-btn--outline .elementor-button { background: #fff; color: var(--od-ink); border-color: var(--od-line); }
selector .od-btn--outline .elementor-button:hover { border-color: var(--od-blue2); color: var(--od-blue); transform: translateY(-2px); }
selector .od-btn--ghost .elementor-button { background: transparent; color: #fff; border-color: rgba(255,255,255,.4); }
selector .od-btn--ghost .elementor-button:hover { background: #fff; color: var(--od-navy); }
selector .od-btn--link .elementor-button { background: none; padding: 0; color: var(--od-blue); box-shadow: none; }
selector .od-btn--link .elementor-button-text::after { content: " →"; }
selector .od-btn--link .elementor-button:hover { color: var(--od-coral); }

/* Barre du haut & en-tête */
selector .od-topbar, selector .od-topbar a { color: #DCEBF2; font-size: 14px; }
selector .od-topbar .elementor-icon-list-icon i, selector .od-topbar .elementor-icon-list-icon svg { color: var(--od-coral-light); fill: var(--od-coral-light); font-size: 13px; }
selector .od-topbar .elementor-icon-list-text { color: #DCEBF2; }
selector .od-topbar a:hover, selector .od-topbar a:hover .elementor-icon-list-text { color: #fff; }
selector .od-header { border-bottom: 1px solid var(--od-line); z-index: 50; }
selector .od-logo img { height: 66px; width: auto; }
selector .od-nav { flex: 1 1 auto; width: auto; min-width: 0; }
selector .od-header-actions { --width: auto; width: auto; flex: 0 0 auto; }
selector .od-logo { flex: 0 0 auto; }
selector .od-header .elementor-nav-menu--main .elementor-item { white-space: nowrap; }
selector .od-header .elementor-nav-menu--main > .elementor-nav-menu { flex-wrap: nowrap; }
@media (max-width: 767px) { selector .od-logo img { height: 50px; } selector .od-topbar .elementor-icon-list-item:not(:first-child) { display: none; } }

/* Hero */
selector .od-hero { background: radial-gradient(900px 500px at 85% -10%, rgba(92,225,230,.28), transparent 60%),
  radial-gradient(600px 400px at -10% 110%, rgba(143,221,110,.20), transparent 60%), linear-gradient(180deg,#fff 0%,var(--od-tint) 100%); }
selector .od-hero-lead p { font-size: 1.2rem; max-width: 560px; margin-bottom: 30px; }
selector .od-actions { margin-bottom: 34px; }
selector .od-hero-proof { color: var(--od-text); }
selector .od-hero-proof strong { color: var(--od-ink); }
selector .od-hero-proof span { font-size: .92rem; color: var(--od-muted); }
selector .od-hero-proof:hover strong { color: var(--od-blue); }
selector .od-google-badge .elementor-icon { width: 48px; height: 48px; border-radius: 14px; background: #fff; box-shadow: 0 1px 2px rgba(10,37,64,.06), 0 2px 8px rgba(10,37,64,.05);
  display: grid; place-items: center; font-size: 24px; color: #4285F4; fill: #4285F4; }
selector .od-google-badge--lg .elementor-icon { width: 64px; height: 64px; border-radius: 18px; background: var(--od-tint); font-size: 32px; }
selector .od-google-badge--sm .elementor-icon { width: 42px; height: 42px; border-radius: 50%; background: var(--od-tint); font-size: 20px; box-shadow: none; }
selector .od-hero-visual { position: relative; }
selector .od-hero-photo img { width: 100%; aspect-ratio: 4/4.3; object-fit: cover; border-radius: 32px; box-shadow: var(--od-shadow-lg); }
selector .od-float { position: absolute !important; width: auto !important; background: #fff; border-radius: 16px; box-shadow: var(--od-shadow-lg);
  padding: 14px 18px !important; z-index: 2; animation: od-floaty 6s ease-in-out infinite; }
selector .od-float p { font-size: .82rem; color: var(--od-muted); line-height: 1.35; white-space: nowrap; }
selector .od-float strong { font-family: "Plus Jakarta Sans", sans-serif; font-size: 1.2rem; color: var(--od-ink); }
selector .od-float--a { left: -34px; top: 16%; }
selector .od-float--b { right: -26px; bottom: 12%; animation-delay: -3s; }
selector .od-float--c { right: 18px; top: -18px; animation-delay: -1.5s; }
selector .od-float-ic .elementor-icon { width: 44px; height: 44px; border-radius: 12px; display: grid; place-items: center; font-size: 20px; }
selector .od-ic--green .elementor-icon { background: #DCFCE7; color: #16A34A; fill: #16A34A; }
selector .od-ic--coral .elementor-icon { background: var(--od-coral-tint); color: var(--od-coral-dark); fill: var(--od-coral-dark); }
selector .od-ic--blue .elementor-icon { background: var(--od-blue-light); color: #4285F4; fill: #4285F4; }
@keyframes od-floaty { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-10px); } }
@media (prefers-reduced-motion: reduce) { selector .od-float { animation: none; } }
@media (max-width: 1024px) { selector .od-hero-visual { max-width: 560px; margin: 0 auto; } selector .od-float--a { left: -10px; } selector .od-float--b { right: -6px; } }
@media (max-width: 767px) { selector .od-float--c { display: none; } selector .od-float--a { left: 8px; top: 8px; } selector .od-float--b { right: 8px; bottom: 8px; }
  selector .od-actions .od-btn, selector .od-actions .od-btn .elementor-button { width: 100%; } }

/* Outils */
selector .od-tools { border-bottom: 1px solid var(--od-line); }
selector .od-tools-label p { text-align: center; font-size: .88rem; font-weight: 600; color: var(--od-muted); text-transform: uppercase; letter-spacing: .12em; margin-bottom: 20px; }
selector .od-tools-list .elementor-icon-list-items { justify-content: space-between; row-gap: 14px; }
selector .od-tools-list .elementor-icon-list-text { font-family: "Plus Jakarta Sans", sans-serif; font-weight: 700; font-size: 1.05rem; color: #7C8B97; }
selector .od-tools-list .elementor-icon-list-icon i, selector .od-tools-list .elementor-icon-list-icon svg { color: #9AA8B3; fill: #9AA8B3; font-size: 22px; }
@media (max-width: 767px) { selector .od-tools-list .elementor-icon-list-items { justify-content: center; column-gap: 22px; } }

/* Cartes */
selector .od-card { background: #fff; border: 1px solid var(--od-line); border-radius: 24px; position: relative; overflow: hidden;
  transition: transform .35s, box-shadow .35s, border-color .35s; }
selector .od-card:hover { transform: translateY(-6px); box-shadow: var(--od-shadow); border-color: transparent; }
selector .od-num .elementor-heading-title { position: absolute; top: 26px; right: 30px; font-size: 2.6rem; color: var(--od-blue-light); }
selector .od-iconbox .elementor-icon { width: 60px; height: 60px; border-radius: 16px; display: grid; place-items: center; font-size: 26px; color: #fff; fill: #fff;
  background: linear-gradient(135deg, #3BB8E0, var(--od-blue)); box-shadow: 0 10px 20px -8px rgba(10,106,168,.5); margin-bottom: 22px; }
selector .od-iconbox--coral .elementor-icon { background: linear-gradient(135deg, var(--od-coral-light), var(--od-coral-dark)); box-shadow: 0 12px 24px -10px rgba(220,58,44,.55); }
selector .od-iconbox { text-align: left; }
selector .od-service ul { list-style: none; padding: 0; margin: 14px 0 22px; }
selector .od-service li { padding: 5px 0 5px 28px; position: relative; font-size: .96rem; }
selector .od-service li::before { content: "✓"; position: absolute; left: 0; top: 7px; width: 19px; height: 19px; border-radius: 50%; background: var(--od-blue-light);
  color: var(--od-blue); font-size: 11px; font-weight: 800; display: grid; place-items: center; }
selector .od-service .elementor-widget-button { margin-top: auto; }

/* Pourquoi */
selector .od-why-media { position: relative; }
selector .od-photo img { width: 100%; aspect-ratio: 5/4; object-fit: cover; border-radius: 32px; box-shadow: var(--od-shadow-lg); }
selector .od-badge { position: absolute !important; left: -24px; bottom: -24px; width: auto !important; max-width: 220px; background: var(--od-coral);
  border-radius: 24px; box-shadow: 0 12px 24px -10px rgba(220,58,44,.55); }
selector .od-badge .elementor-heading-title { color: #fff; font-size: 2.6rem; line-height: 1; }
selector .od-badge p { color: #fff; font-weight: 600; font-size: .92rem; line-height: 1.4; }
selector .od-checks { margin: 8px 0 30px; }
selector .od-checks .elementor-icon-list-item { align-items: flex-start !important; padding-bottom: 12px !important; }
selector .od-checks .elementor-icon-list-icon { width: 26px; height: 26px; min-width: 26px; border-radius: 50%; background: var(--od-coral-tint); display: grid !important; place-items: center; margin-top: 2px; }
selector .od-checks .elementor-icon-list-icon i, selector .od-checks .elementor-icon-list-icon svg { color: var(--od-coral-dark); fill: var(--od-coral-dark); font-size: 12px; }
selector .od-checks .elementor-icon-list-text { color: var(--od-text); padding-left: 12px; }
selector .od-checks strong { color: var(--od-ink); }
@media (max-width: 767px) { selector .od-badge { left: 12px; bottom: -20px; } }

/* Engagements */
selector .od-stat { flex: 1 1 22%; min-width: 200px; text-align: center; padding: 30px 16px; border-radius: 24px; background: rgba(255,255,255,.04); border: 1px solid rgba(255,255,255,.08); }
selector .od-stat .elementor-counter-number-wrapper { color: #fff; font-family: "Plus Jakarta Sans", sans-serif; font-size: clamp(2.3rem, 4vw, 3.1rem); font-weight: 800; line-height: 1.1; justify-content: center; }
selector .od-stat .elementor-counter-number-suffix { color: var(--od-coral-light); }
selector .od-stat .elementor-counter-title { color: #A3C0CF; font-size: .97rem; line-height: 1.5; margin-top: 8px; }

/* Méthode */
selector .od-step { text-align: center; }
selector .od-step-num .elementor-heading-title { width: 68px; height: 68px; margin: 0 auto 20px; border-radius: 50%; display: grid; place-items: center; font-size: 1.3rem;
  color: var(--od-blue); background: #fff; border: 2px solid var(--od-blue-light); box-shadow: 0 1px 2px rgba(10,37,64,.06), 0 2px 8px rgba(10,37,64,.05); transition: .3s; }
selector .od-step:hover .od-step-num .elementor-heading-title { background: var(--od-coral); color: #fff; border-color: var(--od-coral); transform: scale(1.08); }
selector .od-step p { font-size: .97rem; }

/* Portfolio */
selector .od-head-row { margin-bottom: 44px; }
selector .od-browser { background: var(--od-navy); }
selector .od-browser-bar { background: #F3F6F8; border-bottom: 1px solid var(--od-line); padding: 10px 14px 10px 64px; position: relative; }
selector .od-browser-bar::before { content: ""; position: absolute; left: 14px; top: 50%; width: 10px; height: 10px; margin-top: -5px; border-radius: 50%;
  background: #FF6A5A; box-shadow: 16px 0 0 #F7C948, 32px 0 0 #8FDD6E; }
selector .od-browser-bar p { background: #fff; border-radius: 999px; padding: 2px 12px; font-size: .78rem; color: var(--od-muted); line-height: 1.6; }
selector .od-browser-screen img { width: 100%; aspect-ratio: 16/10; object-fit: cover; object-position: top; display: block; transition: transform .7s; }
selector .od-project:hover .od-browser-screen img { transform: scale(1.04); }
selector .od-browser-screen { overflow: hidden; }
selector .od-kind .elementor-heading-title { display: inline-block; font-family: "Inter", sans-serif; font-size: .74rem; font-weight: 700; text-transform: uppercase;
  letter-spacing: .08em; color: var(--od-blue); background: var(--od-blue-light); padding: 4px 10px; border-radius: 8px; margin-bottom: 12px; }
selector .od-project-body p { font-size: .97rem; margin-bottom: 16px; }

/* Avis */
selector .od-review { justify-content: space-between; }
selector .od-quote .elementor-icon { color: var(--od-coral); fill: var(--od-coral); font-size: 30px; }
selector .od-stars p { color: #FBBF24; letter-spacing: 2px; }
selector .od-review-text p { color: var(--od-ink); font-size: 1rem; margin: 16px 0 12px; }
selector .od-review-who p { line-height: 1.4; }
selector .od-review-who strong { color: var(--od-ink); }
selector .od-review-who span { font-size: .88rem; color: var(--od-muted); }
selector .od-reviews-cta { max-width: 980px; margin: 44px auto 0; background: #fff; border: 1px solid var(--od-line); border-radius: 32px; box-shadow: var(--od-shadow); }
selector .od-reviews-cta-text { flex: 1; }
selector .od-reviews-cta-text h3.elementor-heading-title { margin-bottom: 6px; }
selector .od-reviews-cta-text p { color: var(--od-muted); }
@media (max-width: 767px) { selector .od-reviews-cta { text-align: center; } }

/* Blog (widget Articles) */
selector .od-posts .elementor-post__card { border-radius: 24px; border: 1px solid var(--od-line); box-shadow: none; transition: transform .35s, box-shadow .35s; }
selector .od-posts .elementor-post__card:hover { transform: translateY(-6px); box-shadow: var(--od-shadow); }
selector .od-posts .elementor-post__title, selector .od-posts .elementor-post__title a { font-family: "Plus Jakarta Sans", sans-serif; font-weight: 700; color: var(--od-ink); font-size: 1.2rem; line-height: 1.35; }
selector .od-posts .elementor-post__badge { background: var(--od-coral-tint); color: var(--od-coral-dark); font-weight: 700; text-transform: uppercase; letter-spacing: .06em; border-radius: 8px; }
selector .od-posts .elementor-post__read-more { color: var(--od-blue); font-weight: 700; }
selector .od-posts .elementor-post__excerpt p { color: var(--od-text); font-size: .97rem; }

/* FAQ */
selector .od-faq { max-width: 860px; margin: 0 auto; width: 100%; }
selector .od-faq .elementor-toggle-item { background: #fff; border: 1px solid var(--od-line); border-radius: 16px; margin-bottom: 14px; overflow: hidden; }
selector .od-faq .elementor-tab-title { border: 0 !important; padding: 22px 26px; color: var(--od-ink); font-size: 1.05rem; }
selector .od-faq .elementor-tab-title a, selector .od-faq .elementor-toggle-title { color: var(--od-ink); }
selector .od-faq .elementor-tab-title .elementor-toggle-icon { color: var(--od-blue); }
selector .od-faq .elementor-tab-title.elementor-active .elementor-toggle-icon { color: var(--od-coral); }
selector .od-faq .elementor-tab-content { border: 0 !important; padding: 0 26px 22px; color: var(--od-text); }

/* Bandeau final */
selector .od-cta-band { position: relative; overflow: hidden; border-radius: 32px; background: linear-gradient(120deg, var(--od-blue), var(--od-navy)); }
selector .od-cta-band::before { content: ""; position: absolute; width: 520px; height: 520px; border-radius: 50%; right: -160px; top: -220px; background: radial-gradient(circle, rgba(92,225,230,.35), transparent 65%); }
selector .od-cta-band::after { content: ""; position: absolute; width: 360px; height: 360px; border-radius: 50%; left: -120px; bottom: -200px; background: radial-gradient(circle, rgba(143,221,110,.35), transparent 65%); }
selector .od-cta-band > * { position: relative; z-index: 1; }
selector .od-cta-band .elementor-heading-title { color: #fff; }
selector .od-cta-text p { color: #D6F1F7; font-size: 1.12rem; }
selector .od-cta-note p { text-align: center; font-size: .9rem; color: #A8E6EE; }

/* Pied de page */
selector .od-footer { border-top: 4px solid; border-image: var(--od-grad) 1; color: #9BB7C6; }
selector .od-footer p { color: #9BB7C6; font-size: .97rem; }
selector .od-footer .elementor-heading-title { color: #fff; font-size: 1rem; margin-bottom: 18px; }
selector .od-footer-logo img { background: #fff; border-radius: 24px; padding: 10px; width: 170px; height: auto; margin-bottom: 18px; }
selector .od-footer .elementor-icon-list-text { color: #9BB7C6; font-size: .97rem; }
selector .od-footer .elementor-icon-list-icon i, selector .od-footer .elementor-icon-list-icon svg { color: #5CE1E6; fill: #5CE1E6; font-size: 12px; }
selector .od-footer a:hover .elementor-icon-list-text, selector .od-footer a:hover { color: var(--od-coral-light); }
selector .od-foot-links .elementor-icon-list-item, selector .od-foot-contact .elementor-icon-list-item { padding-bottom: 8px !important; }
selector .od-foot-bottom { border-top: 1px solid rgba(255,255,255,.08); margin-top: 56px; padding: 22px 0; }
selector .od-foot-bottom p { font-size: .88rem; }
selector .od-foot-bottom a { color: #9BB7C6; }
@media (max-width: 767px) { selector .od-footer .e-con { width: 100% !important; } }
"""


def build():
    content = [topbar(), header(), hero(), tools(), services(), why(), engagements(), method(), portfolio(), reviews(), blog(), faq(),
               cta_band(), footer()]
    settings = {
        "custom_css": CSS.strip(),
        "background_background": "classic", "background_color": "#FFFFFF",
        "padding": pad(0), "margin": pad(0),
    }
    out = {"title": "Accueil (nouvelle version)", "template": "elementor_canvas", "menu_slug": MENU_SLUG,
           "menu": [("Accueil", URL["home"]), ("Services", URL["services"]), ("Portfolio", URL["portfolio"]),
                    ("À propos", URL["apropos"]), ("Blog", URL["blog"]), ("Contact", URL["contact"])],
           "page_settings": settings, "content": content}
    os.makedirs(os.path.join(ROOT, "wordpress"), exist_ok=True)
    path = os.path.join(ROOT, "wordpress", "elementor-accueil.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print("écrit", path, os.path.getsize(path) // 1024, "Ko,", len(_ids), "éléments")


if __name__ == "__main__":
    build()
