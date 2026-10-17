"""Confere o índice, as seis séries e os links de retorno dos artigos."""
from pathlib import Path
import os
from urllib.parse import urlparse
import hashlib
import json
from bs4 import BeautifulSoup

ROOT=Path(os.environ.get('TWEED_BUILD_ROOT', Path(__file__).resolve().parents[1]))
SITE=ROOT/'site/parallax'
BASE='https://www.agenciatweed.com.br'
posts=json.loads((ROOT/'docs/artigos-recuperados.json').read_text(encoding='utf8'))
extra_records = ROOT / 'docs/artigos-editoriais.json'
if extra_records.exists():
    posts += json.loads(extra_records.read_text(encoding='utf8'))
sections=json.loads((ROOT/'docs/secoes-blog.json').read_text(encoding='utf8'))
thumbs=json.loads((ROOT/'docs/miniaturas-blog.json').read_text(encoding='utf8'))
all_urls={BASE+'/'+p['slug']+'/' for p in posts}
seen=[]
overview=BeautifulSoup((SITE/'blog/index.html').read_text(encoding='utf8'),'html.parser')
assert len(overview.select('.blog-series'))==6
for section,block in zip(sections,overview.select('.blog-series')):
    group=sorted((p for p in posts if section['name'] in p['categories']),key=lambda p:(p['published'],p['slug']),reverse=True)
    expected=[BASE+'/'+p['slug']+'/' for p in group]
    assert [a['href'] for a in block.select('.post-row')]==expected[:3]
    page=BeautifulSoup((SITE/section['slug']/'index.html').read_text(encoding='utf8'),'html.parser')
    actual=[a['href'] for a in page.select('.post-row')]
    assert actual==expected,section['slug']
    assert page.select_one('.blog-lead').get_text()==section['intro']
    seen.extend(actual)
assert len(seen)==len(posts) and set(seen)==all_urls
for slug in ['blog']+[s['slug'] for s in sections]:
    soup=BeautifulSoup((SITE/slug/'index.html').read_text(encoding='utf8'),'html.parser')
    assert len(soup.select('h1'))==1,slug
    assert soup.select_one('link[rel=canonical]')['href']==BASE+'/'+slug+'/'
    assert soup.select_one('meta[name=description]')['content']
    for script in soup.select('script[type="application/ld+json"]'):
        json.loads(script.string)
    for tag in soup.select('a[href],img[src],link[href]'):
        ref=tag.get('href',tag.get('src'));url=urlparse(ref)
        if url.scheme in ('mailto','tel') or url.hostname not in (None,'www.agenciatweed.com.br'):
            continue
        if url.path in ('','/'):
            continue
        target=SITE/url.path.lstrip('/')
        assert target.is_file() or (target/'index.html').is_file(),(slug,ref)
    for img in soup.select('img'):
        assert all(k in img.attrs for k in ('alt','width','height'))
    assert 'semanais' not in soup.get_text().lower(),slug
for thumb in thumbs.values():
    assert hashlib.sha256((SITE/thumb['path'].lstrip('/')).read_bytes()).hexdigest()==thumb['sha256']
print(f'Blog: 7 páginas, 6 séries, {len(posts)} artigos alcançáveis e miniaturas conferidos.')
