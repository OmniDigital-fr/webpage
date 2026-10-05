# Omni Digital — Site web da agência

Site premium e estático (HTML + CSS + JavaScript, sem dependências) para a agência **Omni Digital**: criação de sites, referenciamento SEO, SEO local e transformação digital das PME.

O conteúdo do site está em **francês** (mercado `.fr`).

## Páginas

| Ficheiro | Página |
|---|---|
| `index.html` | Página inicial (hero, serviços, números, método, portfolio, testemunhos, blog, FAQ, CTA) |
| `services.html` | Serviços detalhados + tabela de preços "a partir de" |
| `portfolio.html` | Portfolio com filtros por categoria |
| `a-propos.html` | À propos: história, valores, equipa |
| `contact.html` | Formulário de contacto / pedido de orçamento |
| `rendez-vous.html` | Marcação de reunião online (calendário + horários + confirmação + ficheiro .ics) |
| `blog.html` + `blog/*.html` | Blog com pesquisa e filtros + 6 artigos completos |
| `mentions-legales.html` | Menções legais e política de privacidade |
| `404.html` | Página de erro |

SEO incluído: títulos e meta descriptions por página, URLs canónicas, Open Graph, dados estruturados (ProfessionalService, FAQPage, BlogPosting), `sitemap.xml` e `robots.txt`.

## ⚠️ A personalizar antes de publicar

1. **Contactos** — ✅ já configurados: Paulo Da Costa · `contact@omnidigital.fr` · 06 78 00 59 83 · 25 Rue Jean d'Estienne d'Orves, 94170 Le Perreux-sur-Marne.
2. **Domínio** — `https://www.omnidigital.fr` em `<link rel="canonical">`, `sitemap.xml` e `robots.txt`.
3. **Formulários** — em `assets/js/main.js`, no topo (`OMNI_CONFIG`):
   - `FORM_ENDPOINT`: crie um formulário gratuito em [formspree.io](https://formspree.io) e cole o URL (`https://formspree.io/f/xxxx`). Os pedidos de orçamento, marcações e newsletter chegam ao seu e-mail.
   - Enquanto estiver vazio, os formulários abrem o programa de e-mail do visitante com a mensagem pré-preenchida.
   - `BOOKING`: dias e horários disponíveis para marcações.
4. **Conteúdos de exemplo** — os projetos do portfolio, testemunhos, os outros membros da equipa (além de Paulo Da Costa), estatísticas (150+ projetos, 4,9/5…) e preços são **exemplos ilustrativos**: substitua-os pelos seus dados reais.
5. **Menções legais** — completar os campos `[à compléter]` (forma jurídica, SIRET, alojamento…).
6. **Redes sociais** — links LinkedIn / Facebook / Instagram no rodapé.

## Imagens

As fotografias são imagens reais do [Unsplash](https://unsplash.com) (licença gratuita, uso comercial permitido), carregadas diretamente do CDN do Unsplash. Para melhor desempenho e autenticidade, recomenda-se substituí-las progressivamente por fotos reais da equipa e dos seus projetos (colocá-las em `assets/img/`).

## Publicação

Basta enviar todos os ficheiros para qualquer alojamento web (OVH, o2switch, Netlify, Vercel, GitHub Pages…). Não há nenhuma etapa de compilação.

Para testar localmente:

```bash
python3 -m http.server 8000
# depois abrir http://localhost:8000
```

> Nota: a página `404.html` usa caminhos absolutos (`/assets/...`) e funciona quando o site está na raiz do domínio.
