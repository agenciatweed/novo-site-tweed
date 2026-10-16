"""Verifica conteúdo recuperado, navegação, metadados e arquivos estáticos."""
from pathlib import Path
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'site/parallax'
BASE = 'https://www.agenciatweed.com.br'
records = json.loads((ROOT / 'docs/artigos-recuperados.json').read_text(encoding='utf8'))
sections = json.loads((ROOT / 'docs/secoes-blog.json').read_text(encoding='utf8'))
home = BeautifulSoup((SITE / 'index.html').read_text(encoding='utf8'), 'html.parser')
home_ids = {x['id'] for x in home.select('[id]')}
errors = []
def check(condition, message):
    if not condition:
        errors.append(message)

for r in records:
    name = r['slug']
    soup = BeautifulSoup((SITE / name / 'index.html').read_text(encoding='utf8'), 'html.parser')
    check(len(soup.find_all('h1')) == 1, name + ': H1')
    check(len(soup.select('.progress .progress__bar#progressBar')) == 1, name + ': barra de progresso')
    check(soup.h1.get_text() == r['title'], name + ': título')
    check(soup.find('link', rel='canonical')['href'] == BASE + '/' + name + '/', name + ': canonical')
    check(bool(soup.find('meta', attrs={'name':'description'})['content']), name + ': description')
    check({a['href'] for a in soup.select('.article-category')} == {BASE+'/'+s['slug']+'/' for s in sections if s['name'] in r['categories']}, name + ': links de categoria')
    for script in soup.find_all('script', type='application/ld+json'):
        json.loads(script.string)
    ids = [x['id'] for x in soup.select('[id]')]
    check(len(ids) == len(set(ids)), name + ': IDs duplicados')
    source = BeautifulSoup(r['content'], 'html.parser')
    for h in list(source.find_all(re.compile('^h[1-6]$'))):
        if h.get_text(' ', strip=True) == r['title']:
            h.decompose()
    normalize = lambda s: re.sub(r'\s+', ' ', s).strip()
    body = soup.select_one('.article-body')
    toc = body.select_one('.article-toc')
    if toc:
        toc.decompose()
    check(normalize(body.get_text(' ', strip=True)) == normalize(source.get_text(' ', strip=True)), name + ': texto alterado')
    for tag in soup.find_all(['a','img','link']):
        attr = 'src' if tag.name == 'img' else 'href'
        link = tag.get(attr, '')
        u = urlparse(link)
        if link.startswith('#'):
            check(link[1:] in ids, name + ': âncora ' + link)
        elif u.scheme not in ('mailto', 'tel', 'data') and u.hostname in (None, 'www.agenciatweed.com.br', 'agenciatweed.com.br') and link:
            check(u.hostname != 'agenciatweed.com.br', name + ': hostname antigo')
            if u.path in ('', '/'):
                if u.fragment:
                    check(u.fragment in home_ids, name + ': seção ausente na home')
            else:
                path = SITE / u.path.lstrip('/')
                check(path.is_file() or (path / 'index.html').is_file(), name + ': arquivo ausente ' + link)
        if tag.name == 'img':
            check(all(tag.get(x) for x in ('width','height','alt')), name + ': imagem incompleta')
    for a in soup.select('header.nav a, footer.footer a'):
        href = a.get('href','')
        check(not href.startswith('#'), name + ': navegação não volta à home')

robots = RobotFileParser()
robots.parse((SITE / 'robots.txt').read_text().splitlines())
for bot in ('Googlebot','bingbot','OAI-SearchBot','ChatGPT-User','PerplexityBot','Perplexity-User','Claude-SearchBot','Claude-User','Google-Extended'):
    check(robots.can_fetch(bot, BASE + '/'), 'Bot bloqueado: ' + bot)
for bot in ('GPTBot','ClaudeBot'):
    check(not robots.can_fetch(bot, BASE + '/'), 'Bot não bloqueado: ' + bot)
tree = ET.parse(SITE / 'sitemap.xml')
urls = [n.text for n in tree.findall('.//{*}loc')]
check(set(urls) == {BASE+'/',BASE+'/blog/'} | {BASE+'/'+r['slug']+'/' for r in records} | {BASE+'/'+s['slug']+'/' for s in sections}, 'Sitemap divergente')
check(hashlib.sha256((SITE / 'index.html').read_bytes()).hexdigest() == '9c77eb0c302fdd182cdc2314d6f7abafc5a9da92faff3de7c1e9d38afc0a9e84', 'Home alterada fora da revisão aprovada')
print(json.dumps({'articles':len(records), 'sitemap_urls':len(urls), 'errors':errors}, ensure_ascii=True, indent=2))
raise SystemExit(bool(errors))
