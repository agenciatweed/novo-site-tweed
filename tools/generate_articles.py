"""Geração opcional das páginas estáticas recuperadas; não é um build de produção.

Usa BeautifulSoup apenas na manutenção local. O servidor entrega HTML/CSS puro.
Fontes e proveniência ficam em docs/, nunca são enviadas com o site.
"""
from pathlib import Path
import os
from urllib.parse import urlparse, unquote
import hashlib
import html
import json
import re
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup
from blog_pages import build_blog

ROOT = Path(os.environ.get('TWEED_BUILD_ROOT', Path(__file__).resolve().parents[1]))
SITE = ROOT / 'site/parallax'
BASE = 'https://www.agenciatweed.com.br'
DATE = '2026-10-16'
records = json.loads((ROOT / 'docs/artigos-recuperados.json').read_text(encoding='utf8'))
extra_records = ROOT / 'docs/artigos-editoriais.json'
if extra_records.exists():
    records += json.loads(extra_records.read_text(encoding='utf8'))
sections = json.loads((ROOT / 'docs/secoes-blog.json').read_text(encoding='utf8'))
section_by_name = {s['name']: s for s in sections}
home_bytes = (SITE / 'index.html').read_bytes()
home = home_bytes.decode('utf8')
home_soup = BeautifulSoup(home, 'html.parser')
slugs = {r['slug'] for r in records}
image_manifest = json.loads((ROOT / 'docs/imagens-recuperadas.json').read_text(encoding='utf8'))
esc = lambda x: html.escape(str(x), quote=True)

def home_component(selector):
    component = BeautifulSoup(str(home_soup.select_one(selector)), 'html.parser')
    for tag in component.find_all(True):
        for attr in ('href', 'src'):
            val = tag.get(attr, '')
            if val.startswith('#'):
                tag[attr] = BASE + '/' + val
            elif val.startswith('assets/'):
                tag[attr] = '/' + val
    for img in component.find_all('img'):
        if img.get('class') == ['footer__dog']:
            img['width'] = '263'
            img['height'] = '218'
    return str(component)

nav = home_component('header.nav')
footer = home_component('footer.footer')
base_css = home_soup.style.string.replace("url('assets/", "url('/assets/")
extra_css = (ROOT / 'tools/article-layout.css').read_text(encoding='utf8')
(SITE / 'assets/artigos-tweed.css').write_text(base_css + '\n' + extra_css, encoding='utf8')
months = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']

def clean_content(record):
    soup = BeautifulSoup(record['content'], 'html.parser')
    for node in soup.find_all(['script', 'style', 'iframe']):
        node.decompose()
    for node in list(soup.find_all(True)):
        if node.name == 'span':
            node.unwrap()
            continue
        if node.name in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            if node.get_text(' ', strip=True) == record['title']:
                node.decompose()
                continue
            node.name = 'h2'
        attrs = dict(node.attrs)
        node.attrs = {}
        if node.name == 'a':
            href = attrs.get('href', '')
            u = urlparse(href)
            if u.hostname in ('agenciatweed.com.br', 'www.agenciatweed.com.br'):
                href = BASE + u.path + ('#' + u.fragment if u.fragment else '')
            if u.scheme in ('https', 'http', 'mailto', 'tel') or href.startswith(('/', '#')):
                node['href'] = href
                if u.hostname and u.hostname not in ('agenciatweed.com.br', 'www.agenciatweed.com.br'):
                    node['rel'] = 'noopener noreferrer'
        if node.name == 'img':
            src = attrs.get('src', '')
            image = image_manifest[src]
            node.attrs = {'src': image['path'], 'width': image['width'], 'height': image['height'],
                          'alt': attrs.get('alt') or 'Imagem do artigo ' + record['title'],
                          'loading': 'lazy', 'decoding': 'async'}
        if node.name == 'p' and not node.get_text(strip=True) and not node.find('img'):
            node.decompose()
    for i, heading in enumerate(soup.find_all('h2'), 1):
        heading['id'] = f'secao-{i}'
    return str(soup)

for record in records:
    slug, title = record['slug'], record['title']
    assert re.fullmatch('[a-z0-9-]+', slug)
    url = BASE + '/' + slug + '/'
    content = clean_content(record)
    body_soup = BeautifulSoup(content, 'html.parser')
    count = len(body_soup.get_text(' ', strip=True).split())
    minutes = max(1, round(count / 200))
    y, m, d = map(int, record['published'][:10].split('-'))
    published_label = f'{d} de {months[m-1]} de {y}'
    description = re.sub(r'\s+', ' ', html.unescape(record['description'])).strip()
    if len(description) < 40 or 'posts do blog' in description.lower():
        first_paragraph = body_soup.find('p')
        description = first_paragraph.get_text(' ', strip=True) if first_paragraph else title
    if len(description) > 170:
        description = description[:157].rsplit(' ', 1)[0] + '…'
    image = record['image']
    img_url = BASE + image['path']
    schema = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'Organization', '@id': BASE + '/#organizacao', 'name': 'Agência Tweed', 'url': BASE + '/',
         'logo': {'@type': 'ImageObject', 'url': BASE + '/assets/logo_tweed_teal.svg'}},
        {'@type': 'Person', '@id': BASE + '/#felipe-rijo', 'name': record['author'], 'url': BASE + '/#agencia'},
        {'@type': 'BlogPosting' if record.get('editorial_id') else 'Article', '@id': url + '#artigo', 'headline': title, 'description': description,
         'inLanguage': 'pt-BR', 'url': url, 'mainEntityOfPage': url,
         'datePublished': record['published'],
         'dateModified': max(record['published'], record['original_modified']),
         'author': {'@id': BASE + '/#felipe-rijo'}, 'publisher': {'@id': BASE + '/#organizacao'},
         'image': {'@type': 'ImageObject', 'url': img_url, 'width': image['width'], 'height': image['height']},
         'articleSection': record['categories'], 'wordCount': count},
        {'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Agência Tweed', 'item': BASE + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': 'Blog', 'item': BASE + '/blog/'},
            {'@type': 'ListItem', 'position': 3, 'name': record['categories'][0], 'item': BASE + '/' + section_by_name[record['categories'][0]]['slug'] + '/'},
            {'@type': 'ListItem', 'position': 4, 'name': title, 'item': url}]}]}
    if record.get('editorial_id'):
        article_schema = schema['@graph'][2]
        article_schema['keywords'] = record['keyword']
        article_schema['isPartOf'] = {'@id': BASE + '/blog/#pagina'}
        article_schema['copyrightHolder'] = {'@id': BASE + '/#organizacao'}
        if record.get('faq'):
            article_schema['hasPart'] = [
                {'@type': 'Question', 'name': f['q'],
                 'acceptedAnswer': {'@type': 'Answer', 'text': f['a']}}
                for f in record['faq']]
        if record.get('citations'):
            article_schema['citation'] = record['citations']
    related = sorted((r for r in records if r['slug'] != slug),
                     key=lambda r: (-len(set(r['categories']) & set(record['categories'])), r['slug']))[:2]
    related_html = ''.join(f'<a href="{BASE}/{r["slug"]}/">{esc(r["title"])}</a>' for r in related)
    toc = ''.join(f'<li><a href="#{h["id"]}">{esc(h.get_text(" ", strip=True))}</a></li>' for h in body_soup.find_all('h2'))
    toc_html = f'<details class="article-toc"><summary>Neste artigo</summary><ol>{toc}</ol></details>' if toc else ''
    category_links = ' · '.join(f'<a class="article-category" href="{BASE}/{section_by_name[name]["slug"]}/">{esc(name)}</a>' for name in record['categories'])
    doc = f'''<!doctype html>
<html lang="pt-BR"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} | Agência Tweed</title>
<meta name="description" content="{esc(description)}"><meta name="author" content="{esc(record['author'])}">
<meta name="theme-color" content="#0b0c13"><link rel="canonical" href="{url}">
<meta property="og:locale" content="pt_BR"><meta property="og:type" content="article">
<meta property="og:site_name" content="Agência Tweed"><meta property="og:url" content="{url}">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}">
<meta property="og:image" content="{img_url}"><meta property="og:image:alt" content="{esc(record['image_alt'])}">
<meta property="og:image:width" content="{image['width']}"><meta property="og:image:height" content="{image['height']}">
<meta property="article:published_time" content="{record['published']}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}"><meta name="twitter:image" content="{img_url}">
<link rel="icon" href="/assets/logo_tweed_teal.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/inter-28pt-bold.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/inter-18pt-regular.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/artigos-tweed.css">
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False).replace('</', '<\\/')}</script>
</head><body>
<div class="progress" aria-hidden="true" hidden><div class="progress__bar" id="progressBar"></div></div>
<a href="#conteudo" class="sr-only skip-link">Pular para o conteúdo</a>
{nav}
<main id="conteudo"><article>
<header class="article-hero wrap">
<a class="article-back" href="{BASE}/">Voltar para a Tweed</a>
<div class="article-opening"><div>
<p class="eyebrow">{category_links}</p>
<h1>{esc(title)}</h1>
<p class="article-description">{esc(description)}</p>
<p class="article-meta"><a href="{BASE}/#agencia">{esc(record['author'])}</a><span aria-hidden="true"> · </span><time datetime="{record['published']}">{published_label}</time><span aria-hidden="true"> · </span>{minutes} min de leitura</p>
</div><figure class="article-cover"><img src="{image['path']}" alt="{esc(record['image_alt'])}" width="{image['width']}" height="{image['height']}" fetchpriority="high" decoding="async"></figure></div>
</header>
<div class="wrap article-body">{toc_html}{content}
</div></article>
<aside class="wrap article-related" aria-labelledby="leituras"><h2 id="leituras">Continue a leitura.</h2><div>{related_html}</div></aside>
<section class="wrap article-contact" aria-labelledby="conversa"><h2 id="conversa">Sua marca precisa ser percebida à altura do que entrega.</h2><p>Estratégia, design e execução sob uma direção única. Conheça o jeito Tweed de construir presença.</p><span class="btn-wrap"><a class="btn btn--primary btn--lg" href="{BASE}/#contato">Começar uma conversa</a></span></section>
</main>{footer}
<script>
(function(){{
  'use strict';
  document.getElementById('ano').textContent=new Date().getFullYear();
  var nav=document.getElementById('nav');
  var bar=document.getElementById('progressBar');
  var ticking=false;
  function update(){{
    ticking=false;
    var scrollable=document.documentElement.scrollHeight-window.innerHeight;
    var progress=scrollable>0?Math.min(1,Math.max(0,window.scrollY/scrollable)):0;
    bar.style.transform='scaleX('+progress+')';
    nav.classList.toggle('is-scrolled',window.scrollY>24);
  }}
  function scheduleUpdate(){{
    if(!ticking){{ticking=true;window.requestAnimationFrame(update)}}
  }}
  window.addEventListener('scroll',scheduleUpdate,{{passive:true}});
  window.addEventListener('resize',scheduleUpdate,{{passive:true}});
  window.addEventListener('load',scheduleUpdate);
  window.addEventListener('pageshow',scheduleUpdate);
  if(document.fonts)document.fonts.ready.then(scheduleUpdate);
  if('ResizeObserver' in window)new ResizeObserver(scheduleUpdate).observe(document.body);
  update();
  bar.parentElement.hidden=false;
}})();
</script>
</body></html>'''
    folder = SITE / slug
    folder.mkdir(exist_ok=True)
    (folder / 'index.html').write_text(doc, encoding='utf8')

build_blog(ROOT, records, sections, nav, footer)
collection_slugs = ['blog'] + [s['slug'] for s in sections]
ns = 'http://www.sitemaps.org/schemas/sitemap/0.9'
ET.register_namespace('', ns)
urlset = ET.Element('{'+ns+'}urlset')
for slug in [''] + sorted(slugs | set(collection_slugs)):
    node = ET.SubElement(urlset, 'url')
    ET.SubElement(node, 'loc').text = BASE + '/' + (slug + '/' if slug else '')
    if slug:
        ET.SubElement(node, 'lastmod').text = next((r['published'][:10] for r in records if r['slug'] == slug and r.get('editorial_id')), DATE)
ET.indent(urlset)
ET.ElementTree(urlset).write(SITE / 'sitemap.xml', encoding='utf-8', xml_declaration=True)

route_names = '|'.join(re.escape(s) for s in sorted(slugs | set(collection_slugs)))
htaccess = '''# Agencia Tweed: canonicalizacao somente das rotas do site institucional.
# Pastas de clientes e old_wp_site nao participam destas regras.
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteCond %{HTTP_HOST} !^www\\.agenciatweed\\.com\\.br$ [NC,OR]
RewriteCond %{HTTPS} !=on
RewriteRule ^(?:index\\.html)?$ https://www.agenciatweed.com.br/ [R=301,L]

RewriteCond %{HTTP_HOST} !^www\\.agenciatweed\\.com\\.br$ [NC,OR]
RewriteCond %{HTTPS} !=on
RewriteRule ^((?:robots\\.txt|sitemap\\.xml|(?:ROUTES)(?:/index\\.html|/)?))$ https://www.agenciatweed.com.br/$1 [R=301,L,NE]
</IfModule>
'''.replace('ROUTES', route_names)
(SITE / '.htaccess').write_text(htaccess, encoding='utf8')

assert (SITE / 'index.html').read_bytes() == home_bytes, 'A home não pode mudar'
print(f'Gerados {len(records)} artigos e {len(collection_slugs)} páginas do blog; sitemap com {len(records)+len(collection_slugs)+1} URLs; home intacta ({hashlib.sha256(home_bytes).hexdigest()}).')
