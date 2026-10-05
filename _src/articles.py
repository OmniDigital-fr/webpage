import re
from common import I, U, SITE, CONTACT_NAME, PAULO_IMG, head, header, footer, cta_band, btn_arrow
from data import POSTS
from parts import post_card

BODIES = {}

BODIES["seo-local-google-maps"] = """
<p>Quand un client cherche « plombier près de moi » ou « restaurant italien + votre ville », Google affiche en tête trois entreprises sur une carte : le fameux <strong>pack local</strong>. Ces trois places captent la majorité des clics… et des appels. Bonne nouvelle : avec une méthode rigoureuse, une PME peut y accéder sans budget publicitaire.</p>
<h2 id="s1">1. Revendiquez et complétez à 100 % votre fiche Google Business Profile</h2>
<p>C'est la base. Renseignez le nom exact de votre entreprise, l'adresse, le téléphone, les horaires (y compris les jours fériés), le site web, la zone desservie et une description riche de 750 caractères qui intègre naturellement vos services et votre ville.</p>
<h2 id="s2">2. Choisissez la bonne catégorie principale</h2>
<p>La catégorie principale est l'un des facteurs de classement les plus puissants. Soyez précis : « Avocat en droit de la famille » plutôt que « Avocat ». Ajoutez ensuite des catégories secondaires pertinentes.</p>
<h2 id="s3">3. Publiez de vraies photos, régulièrement</h2>
<p>Les fiches avec des photos reçoivent nettement plus de demandes d'itinéraire et de clics vers le site. Publiez votre devanture, votre équipe, vos réalisations, vos produits. Évitez les images de banque : Google et vos clients préfèrent l'authentique.</p>
<h2 id="s4">4. Mettez en place une stratégie d'avis clients</h2>
<p>Le nombre, la note et la fraîcheur des avis influencent directement votre position. Demandez systématiquement un avis après une prestation réussie, avec un lien direct (QR code en boutique, SMS, e-mail de remerciement).</p>
<div class="tip"><strong>Astuce Omni Digital :</strong> répondez à <em>tous</em> les avis, positifs comme négatifs, sous 48 h. Une réponse professionnelle à un avis négatif rassure souvent plus qu'une note parfaite.</div>
<h2 id="s5">5. Garantissez la cohérence NAP partout</h2>
<p>NAP = <em>Name, Address, Phone</em>. Ces informations doivent être strictement identiques sur votre site, votre fiche Google, Pages Jaunes, les réseaux sociaux et les annuaires. La moindre incohérence brouille les signaux envoyés à Google.</p>
<h2 id="s6">6. Créez des pages locales sur votre site</h2>
<p>Si vous intervenez dans plusieurs villes, créez une page dédiée et utile pour chacune : services proposés, réalisations locales, témoignages de clients de la zone, informations pratiques. Pas de copier-coller : chaque page doit apporter une vraie valeur.</p>
<h2 id="s7">7. Ajoutez les données structurées LocalBusiness</h2>
<p>Le balisage Schema.org aide Google à comprendre précisément qui vous êtes, où vous êtes et quand vous êtes ouvert. C'est invisible pour vos visiteurs, mais très lisible pour les moteurs de recherche.</p>
<h2 id="s8">8. Obtenez des liens locaux</h2>
<p>Un lien depuis le site de votre mairie, d'une association locale, d'un club sportif que vous sponsorisez ou d'un média régional est un signal de proximité fort. Pensez partenariats, événements et relations presse locales.</p>
<h2 id="s9">9. Utilisez les Posts et les Questions/Réponses Google</h2>
<p>Publiez chaque semaine une actualité, une offre ou un événement. Anticipez les questions fréquentes de vos clients dans la section Q&R. Une fiche vivante est une fiche mieux classée.</p>
<h2 id="s10">10. Mesurez et ajustez</h2>
<p>Suivez dans les statistiques de votre fiche le nombre d'appels, de demandes d'itinéraire et de clics vers le site. Croisez avec Google Search Console pour identifier les requêtes locales qui progressent… et celles à travailler.</p>
<blockquote>Le SEO local n'est pas une action ponctuelle mais une routine. Les entreprises qui dominent Google Maps sont celles qui entretiennent leur présence chaque semaine.</blockquote>
<h2>En résumé</h2>
<p>Une fiche complète, des avis réguliers, des informations cohérentes et un site optimisé localement : c'est la combinaison gagnante. Vous manquez de temps pour tout mettre en place ? C'est exactement ce que nous faisons pour nos clients, avec des résultats visibles souvent dès les premières semaines.</p>
"""

BODIES["prix-site-internet-pme"] = """
<p>« Combien coûte un site internet ? » C'est la première question que nous posent les dirigeants de PME. Et la réponse honnête est : <strong>tout dépend de ce que le site doit vous rapporter</strong>. Voici les ordres de grandeur du marché français et les critères qui font varier le prix.</p>
<h2 id="s1">Les grandes fourchettes de prix en 2026</h2>
<table>
<thead><tr><th>Type de site</th><th>Fourchette indicative</th><th>Pour qui ?</th></tr></thead>
<tbody>
<tr><td>Site « fait soi-même » (Wix, etc.)</td><td>0 – 500 €/an</td><td>Lancement, très petit budget</td></tr>
<tr><td>Site vitrine professionnel</td><td>1 500 – 5 000 €</td><td>Artisans, commerçants, professions libérales</td></tr>
<tr><td>Site vitrine premium + SEO</td><td>3 000 – 8 000 €</td><td>PME qui veulent générer des contacts</td></tr>
<tr><td>Site e-commerce</td><td>4 000 – 15 000 €</td><td>Vente de produits en ligne</td></tr>
<tr><td>Plateforme sur-mesure</td><td>15 000 € et plus</td><td>Besoins métier spécifiques</td></tr>
</tbody>
</table>
<h2 id="s2">Ce qui fait varier le prix</h2>
<h3>Le design : modèle ou sur-mesure</h3>
<p>Un thème générique coûte moins cher, mais votre site ressemblera à des milliers d'autres. Un design sur-mesure reflète votre identité et inspire davantage confiance — un facteur clé de conversion.</p>
<h3>Le nombre de pages et les contenus</h3>
<p>Chaque page doit être conçue, rédigée et optimisée. La rédaction SEO professionnelle représente souvent une part importante du budget… et du retour sur investissement.</p>
<h3>Les fonctionnalités</h3>
<p>Prise de rendez-vous, devis en ligne, espace client, paiement, multilingue, connexion à votre CRM : chaque fonctionnalité ajoute du temps de développement.</p>
<h3>Le référencement</h3>
<p>Un site non optimisé pour Google est un site invisible. Vérifiez que le devis inclut la structure SEO, l'optimisation technique, la vitesse et les balises.</p>
<h2 id="s3">Les coûts récurrents à prévoir</h2>
<ul>
<li><strong>Nom de domaine :</strong> 10 à 30 € par an.</li>
<li><strong>Hébergement performant :</strong> 10 à 50 € par mois.</li>
<li><strong>Maintenance & sécurité :</strong> 30 à 150 € par mois selon le niveau de service.</li>
<li><strong>Référencement continu :</strong> 300 à 1 500 € par mois selon la concurrence.</li>
</ul>
<div class="tip"><strong>Notre conseil :</strong> raisonnez en coût d'acquisition client, pas en prix du site. Un site à 3 000 € qui apporte 5 clients par mois est infiniment plus rentable qu'un site à 500 € qui n'en apporte aucun.</div>
<h2 id="s4">Les pièges à éviter</h2>
<ul>
<li>Ne pas être propriétaire de son nom de domaine ou de son site.</li>
<li>Les contrats de location avec engagement de 48 mois.</li>
<li>Les devis flous, sans détail des livrables.</li>
<li>L'absence de formation : vous devez pouvoir modifier votre site vous-même.</li>
</ul>
<h2>Obtenir un devis précis</h2>
<p>Chez Omni Digital, chaque proposition est détaillée ligne par ligne. Après un appel de 30 minutes, vous savez exactement ce que vous payez et ce que vous obtenez.</p>
"""

BODIES["site-qui-genere-des-contacts"] = """
<p>Votre site a du trafic, il est joli… mais le téléphone ne sonne pas. C'est l'une des situations les plus frustrantes pour un dirigeant. Dans 9 cas sur 10, le problème vient d'erreurs de conversion faciles à corriger. Voici les sept que nous rencontrons le plus souvent.</p>
<h2 id="s1">1. On ne comprend pas ce que vous faites en 5 secondes</h2>
<p>Votre titre principal doit dire clairement <strong>ce que vous faites, pour qui, et où</strong>. « Bienvenue sur notre site » ne convertit pas. « Plombier chauffagiste à Lyon — intervention en 2 h » convertit.</p>
<h2 id="s2">2. Aucun appel à l'action visible</h2>
<p>Le visiteur doit savoir quoi faire ensuite. Un bouton contrasté (« Demander un devis gratuit », « Prendre rendez-vous ») doit être visible dès le premier écran et répété au fil de la page.</p>
<h2 id="s3">3. Un site lent, surtout sur mobile</h2>
<p>Au-delà de 3 secondes de chargement, une part importante des visiteurs mobiles abandonne. Images non compressées, thèmes trop lourds et extensions inutiles sont les coupables habituels.</p>
<h2 id="s4">4. Pas de preuves de confiance</h2>
<p>Avis clients, logos de références, réalisations, certifications, photos de l'équipe : ce sont ces éléments qui transforment un inconnu en client. Sans eux, le visiteur va voir ailleurs.</p>
<div class="tip"><strong>À tester dès aujourd'hui :</strong> ajoutez 3 témoignages clients avec photo et nom juste au-dessus de votre formulaire de contact.</div>
<h2 id="s5">5. Un formulaire trop long</h2>
<p>Chaque champ supplémentaire fait baisser le taux de remplissage. Demandez l'essentiel (nom, e-mail, téléphone, besoin) et qualifiez le reste lors de l'appel.</p>
<h2 id="s6">6. Un seul moyen de contact</h2>
<p>Certains préfèrent appeler, d'autres écrire, d'autres réserver un créneau directement. Proposez plusieurs options : téléphone cliquable, formulaire, prise de rendez-vous en ligne.</p>
<h2 id="s7">7. Aucune mesure</h2>
<p>Sans suivi des conversions (appels, formulaires, clics), impossible de savoir ce qui fonctionne. Google Analytics 4 et le suivi des événements sont indispensables pour progresser.</p>
<blockquote>Un site qui convertit n'est pas forcément plus beau : il est plus clair, plus rapide et plus rassurant.</blockquote>
<h2>Et maintenant ?</h2>
<p>Corrigez ces sept points et vous verrez une différence rapidement. Si vous souhaitez un regard extérieur, notre audit gratuit identifie précisément ce qui freine vos conversions.</p>
"""

BODIES["transformation-digitale-pme"] = """
<p>« Transformation digitale » : le terme fait peur et semble réservé aux grands groupes. Pourtant, pour une PME, il s'agit surtout de <strong>gagner du temps, des clients et de la sérénité</strong> grâce à quelques outils bien choisis. Voici un plan en 5 étapes pour démarrer sans vous disperser.</p>
<h2 id="s1">Étape 1 : faire l'état des lieux</h2>
<p>Listez vos tâches répétitives (devis, relances, prises de rendez-vous, facturation) et les points de friction avec vos clients. Où perdez-vous du temps ? Où perdez-vous des opportunités ?</p>
<h2 id="s2">Étape 2 : soigner votre vitrine en ligne</h2>
<p>Votre site internet et votre fiche Google sont souvent le premier contact avec un client. Ils doivent être professionnels, rapides, à jour et pensés pour générer des demandes.</p>
<h2 id="s3">Étape 3 : digitaliser la relation client</h2>
<ul>
<li><strong>Prise de rendez-vous en ligne :</strong> vos clients réservent 24 h/24, sans appel.</li>
<li><strong>Devis en ligne :</strong> un formulaire qualifié qui vous fait gagner du temps.</li>
<li><strong>CRM simple :</strong> plus aucun prospect oublié, des relances automatiques.</li>
</ul>
<h2 id="s4">Étape 4 : automatiser l'administratif</h2>
<p>Facturation électronique (bientôt obligatoire pour toutes les entreprises en France), signature électronique, comptabilité connectée : ces outils libèrent plusieurs heures par semaine.</p>
<div class="tip"><strong>Bon à savoir :</strong> la généralisation de la facturation électronique entre entreprises est en cours en France. C'est le moment idéal pour moderniser vos outils.</div>
<h2 id="s5">Étape 5 : former et embarquer vos équipes</h2>
<p>Un outil n'est utile que s'il est utilisé. Prévoyez une formation, désignez un référent interne et avancez par petites étapes.</p>
<blockquote>La meilleure transformation digitale est celle que vos équipes adoptent naturellement, parce qu'elle leur simplifie la vie.</blockquote>
<h2>Par où commencer concrètement ?</h2>
<p>Commencez par ce qui rapporte le plus vite : un site qui génère des contacts et une prise de rendez-vous en ligne. Nous accompagnons les PME dans ce passage au digital, étape par étape, avec un interlocuteur unique.</p>
"""

BODIES["vitesse-site-core-web-vitals"] = """
<p>La vitesse de votre site influence à la fois votre position sur Google et le comportement de vos visiteurs. Depuis plusieurs années, Google mesure l'expérience utilisateur à travers les <strong>Core Web Vitals</strong>. Voici ce qu'il faut savoir.</p>
<h2 id="s1">Les 3 indicateurs clés</h2>
<table>
<thead><tr><th>Indicateur</th><th>Ce qu'il mesure</th><th>Objectif</th></tr></thead>
<tbody>
<tr><td><strong>LCP</strong> (Largest Contentful Paint)</td><td>Le temps d'affichage du contenu principal</td><td>&lt; 2,5 s</td></tr>
<tr><td><strong>INP</strong> (Interaction to Next Paint)</td><td>La réactivité aux clics et saisies</td><td>&lt; 200 ms</td></tr>
<tr><td><strong>CLS</strong> (Cumulative Layout Shift)</td><td>La stabilité visuelle de la page</td><td>&lt; 0,1</td></tr>
</tbody>
</table>
<h2 id="s2">Pourquoi c'est important</h2>
<p>Un site lent fait fuir les visiteurs avant même qu'ils voient votre offre. À contenu équivalent, Google privilégie les pages offrant la meilleure expérience. Et un visiteur satisfait convertit davantage.</p>
<h2 id="s3">Les optimisations qui comptent vraiment</h2>
<h3>Images</h3>
<p>Formats modernes (WebP, AVIF), dimensions adaptées, chargement différé (<em>lazy loading</em>) pour les images sous la ligne de flottaison.</p>
<h3>Hébergement</h3>
<p>Un serveur rapide, proche de vos visiteurs, avec cache et CDN. C'est souvent l'amélioration la plus rentable.</p>
<h3>Code et extensions</h3>
<p>Moins d'extensions, moins de scripts tiers, CSS et JavaScript optimisés. Chaque script de suivi ou widget a un coût en performance.</p>
<h3>Polices et mise en page</h3>
<p>Précharger les polices, réserver l'espace des images et publicités pour éviter les décalages visuels.</p>
<div class="tip"><strong>Testez votre site :</strong> rendez-vous sur PageSpeed Insights et entrez votre adresse. Concentrez-vous sur les résultats mobiles, ce sont ceux que Google utilise en priorité.</div>
<h2>Notre approche</h2>
<p>Tous les sites que nous livrons visent un score de 90+ sur mobile. Pour les sites existants, notre audit technique identifie les optimisations les plus rentables et nous les mettons en œuvre sans refonte complète.</p>
"""

BODIES["contenus-qui-se-positionnent"] = """
<p>Publier des articles ne suffit pas : encore faut-il qu'ils apparaissent sur Google et attirent les bons visiteurs. Voici la méthode que nous appliquons pour nos clients, étape par étape.</p>
<h2 id="s1">1. Partir des questions de vos clients</h2>
<p>Les meilleurs sujets viennent du terrain : quelles questions vos clients posent-ils avant d'acheter ? Listez-les, puis vérifiez leur volume de recherche avec un outil de mots-clés.</p>
<h2 id="s2">2. Comprendre l'intention de recherche</h2>
<p>Tapez votre mot-clé sur Google et analysez la première page. S'agit-il de guides, de comparatifs, de pages de services, de vidéos ? Votre contenu doit répondre au même besoin… en mieux.</p>
<h2 id="s3">3. Structurer pour le lecteur et pour Google</h2>
<ul>
<li>Un titre H1 clair contenant le mot-clé principal.</li>
<li>Des sous-titres H2/H3 qui reprennent les questions secondaires.</li>
<li>Des paragraphes courts, des listes, des tableaux.</li>
<li>Une réponse directe dès l'introduction.</li>
</ul>
<h2 id="s4">4. Apporter une vraie expertise</h2>
<p>Google valorise l'expérience, l'expertise, l'autorité et la fiabilité (E-E-A-T). Partagez vos exemples, vos chiffres, vos retours d'expérience : c'est ce qu'aucun concurrent ne peut copier.</p>
<div class="tip"><strong>Astuce :</strong> signez vos articles avec une vraie biographie d'auteur et illustrez-les avec vos propres photos de chantiers, de produits ou d'équipe.</div>
<h2 id="s5">5. Soigner le maillage interne</h2>
<p>Reliez vos articles entre eux et vers vos pages de services. Cela aide Google à comprendre votre site et guide le lecteur vers la prise de contact.</p>
<h2 id="s6">6. Optimiser les balises</h2>
<p>Balise title (55-60 caractères) et meta description (150-160 caractères) rédigées pour donner envie de cliquer : ce sont votre annonce dans les résultats de recherche.</p>
<h2 id="s7">7. Mettre à jour régulièrement</h2>
<p>Un contenu actualisé conserve et améliore ses positions. Revoyez vos articles les plus importants tous les 6 à 12 mois.</p>
<blockquote>Un bon contenu SEO, c'est d'abord un contenu utile. Le référencement suit naturellement.</blockquote>
<h2>Besoin d'un coup de main ?</h2>
<p>Chez Omni Digital, je rédige chaque mois des contenus optimisés pour mes clients, en collaboration étroite avec eux pour garantir l'expertise métier.</p>
"""

AUTHORS = {
    "seo-local-google-maps": (CONTACT_NAME, "Direction & stratégie SEO", PAULO_IMG),
    "prix-site-internet-pme": (CONTACT_NAME, "Direction & stratégie SEO", PAULO_IMG),
    "site-qui-genere-des-contacts": (CONTACT_NAME, "Direction & stratégie SEO", PAULO_IMG),
    "transformation-digitale-pme": (CONTACT_NAME, "Direction & stratégie SEO", PAULO_IMG),
    "vitesse-site-core-web-vitals": (CONTACT_NAME, "Direction & stratégie SEO", PAULO_IMG),
    "contenus-qui-se-positionnent": (CONTACT_NAME, "Direction & stratégie SEO", PAULO_IMG),
}


def article(p):
    root = "../"
    body = BODIES[p["slug"]]
    toc = re.findall(r'<h2 id="(s\d+)">(.*?)</h2>', body)
    toc_html = "".join(f'<li><a href="#{i}">{re.sub("<.*?>", "", t)}</a></li>' for i, t in toc)
    a_name, a_role, a_img = AUTHORS[p["slug"]]
    path = f"blog/{p['slug']}.html"
    ld = {
        "@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"], "description": p["excerpt"],
        "image": U(p["img"], 1200), "datePublished": p["date"], "dateModified": p["date"],
        "author": {"@type": "Person", "name": a_name}, "publisher": {"@type": "Organization", "name": "Omni Digital", "logo": {"@type": "ImageObject", "url": SITE + "/assets/img/logo-omni-digital.png"}},
        "mainEntityOfPage": SITE + "/" + path,
    }
    out = head(f"{p['title']} | Blog Omni Digital", p["excerpt"], path, root=root, image=U(p["img"], 1200, 630), jsonld=[ld], ogtype="article")
    out += header("blog.html", root=root)
    related = [x for x in POSTS if x["slug"] != p["slug"]][:3]
    out += f"""
<main id="main">
<article>
  <header class="article-hero">
    <div class="container">
      <ol class="breadcrumb"><li><a href="../index.html">Accueil</a></li><li><a href="../blog.html">Blog</a></li><li aria-current="page">{p['cat']}</li></ol>
      <div class="post-meta"><span class="post-cat">{p['cat']}</span><time datetime="{p['date']}">{p['date_h']}</time><span>· {p['read']} de lecture</span></div>
      <h1>{p['title']}</h1>
      <div class="article-author"><img src="{root + a_img if a_img.endswith('.svg') else U(a_img, 120)}" alt="{a_name}" width="48" height="48"><div><strong>{a_name}</strong><span>{a_role} chez Omni Digital</span></div></div>
    </div>
  </header>
  <div class="article-cover"><img src="{U(p['img'], 1600)}" alt="{p['title']}" width="1600" height="686" fetchpriority="high"></div>
  <div class="article-layout">
    <div class="prose">
      <p style="font-size:1.22rem;color:var(--ink)"><strong>{p['excerpt']}</strong></p>
      {body}
      <div class="share"><strong style="color:var(--ink);margin-right:6px">Partager :</strong>
        <a data-share="linkedin" href="#" target="_blank" rel="noopener" aria-label="Partager sur LinkedIn">{I['linkedin']}</a>
        <a data-share="facebook" href="#" target="_blank" rel="noopener" aria-label="Partager sur Facebook">{I['facebook']}</a>
        <a data-share="x" href="#" target="_blank" rel="noopener" aria-label="Partager sur X">{I['x']}</a>
        <button type="button" data-copy-link aria-label="Copier le lien">{I['link']}</button>
      </div>
    </div>
    <aside class="article-aside">
      <div class="aside-card"><h4>Sommaire</h4><ol>{toc_html}</ol></div>
      <div class="aside-card aside-card--cta"><h4>Audit SEO gratuit</h4><p>Découvrez en 30 minutes ce qui freine votre visibilité sur Google.</p><a class="btn btn-primary btn-block" href="../rendez-vous.html">Réserver mon audit {I['arrow']}</a></div>
    </aside>
  </div>
</article>
<section class="section section--tint" style="margin-top:80px">
  <div class="container">
    <div class="section-head"><span class="eyebrow">À lire aussi</span><h2>Articles similaires</h2></div>
    <div class="grid grid-3">{"".join(post_card(x, root, f" reveal-d{i}") for i, x in enumerate(related))}
    </div>
  </div>
</section>
{cta_band(root=root)}
</main>
"""
    out += footer(root=root)
    return out
