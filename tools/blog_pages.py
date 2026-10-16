"""Sete páginas estáticas do blog; usa apenas textos e imagens do acervo."""
from pathlib import Path
import html
import json

BASE = 'https://www.agenciatweed.com.br'
esc = lambda value: html.escape(str(value), quote=True)

def build_blog(root, records, sections, nav, footer):
    site = root / 'site/parallax'
    thumbnails = json.loads((root / 'docs/miniaturas-blog.json').read_text(encoding='utf8'))
    (site / 'assets/blog-tweed.css').write_text((root / 'tools/blog-layout.css').read_text(encoding='utf8'), encoding='utf8')

    def entries(section):
        return sorted((r for r in records if section['name'] in r['categories']), key=lambda r: (r['published'], r['slug']), reverse=True)

    def rows(posts, heading):
        result = []
        for post in posts:
            thumb = thumbnails[post['slug']]
            result.append(f'''<li><a class="post-row" href="{BASE}/{post['slug']}/">
<img src="{thumb['path']}" alt="" width="{thumb['width']}" height="{thumb['height']}" loading="lazy" decoding="async">
<{heading}>{esc(post['title'])}</{heading}></a></li>''')
        return '\n'.join(result)

    def document(slug, title, description, heading_html, body, posts, section=None):
        url = f'{BASE}/{slug}/'
        crumb = f'<a href="{BASE}/">Tweed</a><span aria-hidden="true">/</span>'
        crumb += f'<a href="{BASE}/blog/">Blog</a><span aria-hidden="true">/</span><span aria-current="page">{esc(section["name"])}</span>' if section else '<span aria-current="page">Blog</span>'
        breadcrumb_items = [{'@type': 'ListItem', 'position': 1, 'name': 'Agência Tweed', 'item': BASE + '/'},
                            {'@type': 'ListItem', 'position': 2, 'name': 'Blog', 'item': BASE + '/blog/'}]
        if section:
            breadcrumb_items.append({'@type':'ListItem','position':3,'name':section['name'],'item':url})
        graph = {'@context':'https://schema.org','@graph':[
            {'@type':'CollectionPage','@id':url+'#pagina','url':url,'name':title,'description':description,'inLanguage':'pt-BR',
             'isPartOf':{'@id':BASE+'/#site'},'publisher':{'@id':BASE+'/#organizacao'},'mainEntity':{'@id':url+'#artigos'}},
            {'@type':'ItemList','@id':url+'#artigos','numberOfItems':len(posts),'itemListElement':[
                {'@type':'ListItem','position':i,'name':p['title'],'url':BASE+'/'+p['slug']+'/'} for i,p in enumerate(posts,1)]},
            {'@type':'BreadcrumbList','itemListElement':breadcrumb_items}]}
        image = posts[0]['image']
        page = f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} | Agência Tweed</title><meta name="description" content="{esc(description)}"><meta name="theme-color" content="#0b0c13">
<link rel="canonical" href="{url}"><meta property="og:locale" content="pt_BR"><meta property="og:type" content="website">
<meta property="og:site_name" content="Agência Tweed"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}{image['path']}"><meta property="og:image:width" content="{image['width']}"><meta property="og:image:height" content="{image['height']}"><meta property="og:image:alt" content="{esc(posts[0]['image_alt'])}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title)}"><meta name="twitter:description" content="{esc(description)}"><meta name="twitter:image" content="{BASE}{image['path']}">
<link rel="icon" href="/assets/logo_tweed_teal.svg" type="image/svg+xml"><link rel="preload" href="/assets/fonts/inter-28pt-bold.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/inter-18pt-regular.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/artigos-tweed.css"><link rel="stylesheet" href="/assets/blog-tweed.css">
<script type="application/ld+json">{json.dumps(graph,ensure_ascii=False).replace('</','<\\/')}</script></head>
<body><a href="#conteudo" class="sr-only skip-link">Pular para o conteúdo</a>{nav}
<main id="conteudo" class="blog-page"><header class="wrap blog-intro"><nav class="blog-breadcrumb" aria-label="Caminho da página">{crumb}</nav>{heading_html}</header>
{body}</main>{footer}
<script>document.getElementById('ano').textContent=new Date().getFullYear();const nav=document.getElementById('nav');function updateNav(){{nav.classList.toggle('is-scrolled',scrollY>24)}}addEventListener('scroll',updateNav,{{passive:true}});updateNav();</script>
</body></html>'''
        target = site / slug
        target.mkdir(exist_ok=True)
        (target / 'index.html').write_text(page, encoding='utf8')

    blocks = []
    previews = []
    for section in sections:
        posts = entries(section)
        recent = posts[:3]
        previews.extend(recent)
        blocks.append(f'''<section class="blog-series" aria-labelledby="{section['slug']}">
<header><h2 id="{section['slug']}"><a href="{BASE}/{section['slug']}/">{esc(section['name'])}</a></h2><p>{esc(section['description'])}</p></header>
<ul class="post-list">{rows(recent,'h3')}</ul><a class="series-all" href="{BASE}/{section['slug']}/">Ver os {len(posts)} artigos da série<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></a></section>''')
        heading = f'<h1>{esc(section["name"])}.</h1><p class="blog-lead">{esc(section["intro"])}</p><p class="blog-count">{len(posts)} artigos · do mais recente ao mais antigo</p>'
        body = f'''<section class="wrap blog-archive" aria-labelledby="artigos"><h2 class="sr-only" id="artigos">Artigos de {esc(section['name'])}</h2><ul class="post-list archive-list">{rows(posts,'h3')}</ul></section>
<nav class="wrap blog-series-nav" aria-label="Outras séries"><a class="series-all" href="{BASE}/blog/">Explorar todas as séries</a></nav>'''
        document(section['slug'], section['name'], section['description'], heading, body, posts, section)

    heading = '<h1>Blog da Tweed.</h1><p class="blog-lead">Estratégia, branding e comportamento em seis séries. Reflexões, exemplos e ideias para construir marcas com clareza, consistência e propósito.</p>'
    body = '<div class="wrap"><div class="blog-grid">'+''.join(blocks)+'</div></div>'
    document('blog', 'Blog da Tweed — estratégia, branding e comportamento',
             'Explore seis séries da Tweed sobre estratégia, branding, comportamento e crescimento de marcas. Encontre os artigos mais recentes de cada tema.',
             heading, body, previews)
