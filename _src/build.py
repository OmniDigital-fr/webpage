"""Génère toutes les pages HTML du site, ainsi que sitemap.xml et robots.txt.

Usage : python3 _src/build.py
"""
import os
from common import SITE
import pages, articles
from data import POSTS
# Les pages sont écrites à la racine du dépôt (dossier parent de _src/)
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
files = {
    "index.html": pages.home(), "services.html": pages.services(), "portfolio.html": pages.portfolio(),
    "a-propos.html": pages.about(), "contact.html": pages.contact(), "rendez-vous.html": pages.rendezvous(),
    "blog.html": pages.blog(), "mentions-legales.html": pages.legal(), "404.html": pages.notfound(),
}
for p in POSTS:
    files[f"blog/{p['slug']}.html"] = articles.article(p)
for k, v in files.items():
    with open(os.path.join(OUT, k), "w", encoding="utf-8") as f:
        f.write(v)
prio = {"index.html": "1.0", "services.html": "0.9", "contact.html": "0.9", "rendez-vous.html": "0.8", "portfolio.html": "0.8", "a-propos.html": "0.7", "blog.html": "0.7", "mentions-legales.html": "0.2"}
urls = ""
for k in files:
    if k == "404.html": continue
    loc = SITE + "/" + ("" if k == "index.html" else k)
    urls += f"  <url><loc>{loc}</loc><priority>{prio.get(k, '0.6')}</priority></url>\n"
open(os.path.join(OUT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n")
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
print("built", len(files))
