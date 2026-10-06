from common import U

# Projets du portfolio — sites réellement créés par Omni Digital.
# Pour ajouter une capture d'écran : placez l'image dans assets/img/portfolio/ et indiquez-la dans "img".
PROJECTS = [
    dict(title="Digital Réseau", tag="Conseil B2B", url="https://digitalreseau.fr", domain="digitalreseau.fr",
         img="assets/img/portfolio/digitalreseau.webp",
         text="Site vitrine d'un cabinet de conseil en stratégie digitale et développement commercial pour les PME. "
              "Design éditorial épuré, présentation des expertises et de la méthode, appels à l'action vers la prise de contact."),
    dict(title="Les Bras Cassés", tag="Club moto", url="https://lesbrascasses.fr", domain="lesbrascasses.fr",
         img="assets/img/portfolio/lesbrascasses.webp",
         text="Site du club moto Broken Arms – Les Bras Cassés, en Île-de-France : présentation du club, "
              "agenda des sorties et soirées, souvenirs des balades, partenaires et boutique de merchandising officiel."),
    dict(title="Broken Arms", tag="E-commerce", url="https://brokenarms.fr", domain="brokenarms.fr",
         img="assets/img/portfolio/brokenarms.webp",
         text="Boutique en ligne de la marque biker lifestyle Broken Arms : t-shirts, sweats et accessoires, "
              "fiches produits avec choix de taille, panier et espace client, dans un univers de marque fort."),
    dict(title="Pratik Informatique", tag="Services locaux", url="https://pratik-informatique.fr", domain="pratik-informatique.fr",
         img="assets/img/portfolio/pratik-informatique.webp",
         text="Site d'un technicien en dépannage informatique à Gagny et dans l'Est parisien, pour particuliers et professionnels : "
              "services, zones d'intervention, demande de rendez-vous et appel en un clic."),
]

# Avis clients — UNIQUEMENT de vrais avis Google, texte copié tel quel
# (source : fiche Google « Omni Digital », importée par l'extension Trustindex du WordPress, avril 2026).
TESTIMONIALS = [
    dict(name="Paulo A.", stars=5,
         text="Très satisfait du travail d’Omni Digital.\nSite moderne, rapide et professionnel.\n"
              "On sent une vraie expertise en marketing et pas seulement en design.\nJe recommande sans hésiter."),
    dict(name="David P.", stars=5,
         text="Créateur de site web très compétent toujours à l'écoute pour modifier des pages ou la structure de votre site. "
              "Mon site https://pratik-informatique.fr a été réalisé dans un temps assez rapide me permettant de le présenter "
              "à ma clientèle pour prospecter.\nN'hésitez pas à faire appel à cette société pour une refonte de votre site ou "
              "tout simplement pour la création.\nProfessionnel à l'écoute tout ce que je recherche et généralement tout ce que "
              "tout le monde recherche."),
    dict(name="Or Tel SAV", stars=5,
         text="Nous avons sollicité Omni Digital pour obtenir des conseils ainsi que plusieurs améliorations sur notre site internet, "
              "et tout s’est déroulé parfaitement du début à la fin.\n\nL’équipe a su être à l’écoute, réactive et très "
              "professionnelle. Nous ne regrettons absolument pas d’avoir travaillé avec Omni Digital, surtout au vu du "
              "professionnalisme et du savoir-faire de Paulo.\n\nUne société sérieuse, compétente et impliquée, que nous "
              "recommandons sans hésitation."),
]

# Articles du blog
POSTS = [
    dict(slug="seo-local-google-maps", cat="SEO local", title="SEO local : 10 actions pour apparaître dans le top 3 de Google Maps",
         excerpt="Fiche Google Business Profile, avis, citations locales… La méthode concrète pour capter les clients qui cherchent près de chez vous.",
         img="1524661135-423995f22d0b", date="2026-09-22", date_h="22 sept. 2026", read="9 min"),
    dict(slug="prix-site-internet-pme", cat="Création web", title="Combien coûte un site internet pour une PME en 2026 ?",
         excerpt="Site vitrine, e-commerce, sur-mesure : les vrais prix du marché, ce qui les fait varier et comment éviter les mauvaises surprises.",
         img="1554224155-6726b3ff858f", date="2026-09-08", date_h="8 sept. 2026", read="7 min"),
    dict(slug="site-qui-genere-des-contacts", cat="Conversion", title="Votre site ne génère pas de contacts ? Les 7 erreurs à corriger",
         excerpt="Un beau site qui ne convertit pas, c'est une vitrine fermée. Voici les erreurs les plus fréquentes et comment les corriger rapidement.",
         img="1460925895917-afdab827c52f", date="2026-08-25", date_h="25 août 2026", read="8 min"),
    dict(slug="transformation-digitale-pme", cat="Digital", title="Transformation digitale des PME : par où commencer ?",
         excerpt="Outils, priorités, budget : un plan d'action en 5 étapes pour digitaliser votre entreprise sans vous disperser.",
         img="1519389950473-47ba0277781c", date="2026-08-11", date_h="11 août 2026", read="6 min"),
    dict(slug="vitesse-site-core-web-vitals", cat="SEO technique", title="Vitesse de chargement et Core Web Vitals : l'impact réel sur votre SEO",
         excerpt="LCP, INP, CLS : comprendre les indicateurs de Google et les optimisations qui font vraiment la différence.",
         img="1551288049-bebda4e38f71", date="2026-07-28", date_h="28 juil. 2026", read="7 min"),
    dict(slug="contenus-qui-se-positionnent", cat="Contenu", title="Rédiger des contenus qui se positionnent sur Google : la méthode",
         excerpt="Recherche de mots-clés, intention de recherche, structure, maillage interne : notre méthode pour écrire des pages qui rankent.",
         img="1455390582262-044cdead277a", date="2026-07-14", date_h="14 juil. 2026", read="8 min"),
]
