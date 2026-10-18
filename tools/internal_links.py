"""Links editoriais persistentes: escolha humana/GPT, inserção exata e limite por corpo."""
from pathlib import Path
from urllib.parse import urlparse
import hashlib,json,re
from bs4 import BeautifulSoup,NavigableString
BASE='https://www.agenciatweed.com.br'
LIMIT=4
BODY=re.compile(r'(<div class="wrap article-body">)(.*?)(\n</div></article>)',re.S)
def read_registry(root):
    file=Path(root)/'docs/links-internos.json'
    return json.loads(file.read_text(encoding='utf8')) if file.exists() else {'version':1,'links':[]}
def post_target(href,slugs):
    u=urlparse(href)
    if u.scheme not in ('','http','https') or u.netloc not in ('','www.agenciatweed.com.br','agenciatweed.com.br'):return None
    slug=u.path.strip('/')
    return slug if slug in slugs else None
def post_links(content,slugs):
    soup=BeautifulSoup(content,'html.parser') if isinstance(content,str) else content
    return [a for a in soup.select('a[href]') if post_target(a['href'],slugs) and not a.find_parent(class_='article-toc')]
def apply_links(content,source,registry,slugs):
    rules=[r for r in registry['links'] if r['from']==source]
    if not rules:
        assert len(post_links(content,slugs))<=LIMIT,f'{source}: mais de {LIMIT} links para artigos.'
        return content
    soup=BeautifulSoup(content,'html.parser');original=soup.get_text()
    for rule in rules:
        target=rule['to'];anchor=rule['anchor'];context=rule['context']
        assert target in slugs and target!=source,'Destino inexistente ou link para si mesmo.'
        assert anchor.strip() and context.strip() and rule.get('reason','').strip(),'Link precisa de âncora, contexto e justificativa editorial.'
        existing=[a for a in post_links(soup,slugs) if post_target(a['href'],slugs)==target]
        if existing:
            assert any(a.get_text()==anchor and context in a.find_parent(['p','li','blockquote']).get_text() for a in existing if a.find_parent(['p','li','blockquote'])),f'{source}: destino já vinculado em outro trecho.'
            continue
        assert len(post_links(soup,slugs))<LIMIT,f'{source}: capacidade de {LIMIT} links esgotada.'
        matches=[]
        for node in soup.find_all(string=True):
            parent=node.find_parent(['p','li','blockquote'])
            if not parent or node.find_parent(['a','script','style','code','pre']) or node.find_parent(class_='article-toc'):continue
            if context not in parent.get_text():continue
            if str(node).count(anchor):matches.extend([node]*str(node).count(anchor))
        assert len(matches)==1,f'{source}: âncora ausente ou ambígua: {anchor}'
        node=matches[0];before,after=str(node).split(anchor,1);link=soup.new_tag('a',href=BASE+'/'+target+'/');link.string=anchor
        node.replace_with(NavigableString(before),link,NavigableString(after))
    assert soup.get_text()==original,f'{source}: texto não pode mudar ao inserir links.'
    assert len(post_links(soup,slugs))<=LIMIT
    return str(soup)
def modified(registry,slug):
    return max((r['modifiedAt'] for r in registry['links'] if r['from']==slug),default='')
def merge_plan(root,records,plan):
    assert plan.get('version')==1 and isinstance(plan.get('links'),list),'Plano de links inválido.'
    by_slug={r['slug']:r for r in records};slug=plan['newSlug'];assert slug in by_slug,'Artigo novo não existe no catálogo.'
    expected=hashlib.sha256(by_slug[slug]['content'].encode()).hexdigest()
    assert plan.get('contentSha256')==expected,'O artigo mudou depois da análise de links.'
    registry=read_registry(root);registry=json.loads(json.dumps(registry))
    scope=plan.get('scope','full')
    assert scope in ('full','new-only'),'Escopo de links inválido.'
    if scope=='new-only':
        assert all(r.get('from')==slug for r in plan['links']),'A rodada reduzida só pode inserir links no artigo novo.'
    else:
        assert any(r.get('to')==slug and r.get('from')!=slug for r in plan['links']),'Escolha ao menos um post anterior apontando para o novo.'
    for r in plan['links']:
        assert r['from'] in by_slug and r['to'] in by_slug and (r['from']==slug or r['to']==slug),'Plano contém artigo fora da publicação atual.'
        assert r['from']==slug or by_slug[r['from']]['published']<=by_slug[slug]['published'],'O link de entrada precisa vir de um artigo anterior.'
        assert r['from']!=r['to'] and r.get('reason','').strip()
        key=(r['from'],r['to'],r['anchor'],r['context'])
        if any((v['from'],v['to'],v['anchor'],v['context'])==key for v in registry['links']):continue
        assert re.fullmatch(r'\d{4}-\d{2}-\d{2}',plan['modifiedAt']),'Data inválida.'
        registry['links'].append({**r,'modifiedAt':plan['modifiedAt']})
    return registry

def patch_document(document,slug,registry,slugs):
    match=BODY.search(document);assert match,f'{slug}: corpo não encontrado.'
    body=apply_links(match[2],slug,registry,slugs)
    if body==match[2]:return document
    doc=document[:match.start(2)]+body+document[match.end(2):]
    date=modified(registry,slug)
    def update_schema(match):
        graph=json.loads(match[2])
        for node in graph.get('@graph',[]):
            if node.get('@type') in ('Article','BlogPosting'):node['dateModified']=max(node.get('dateModified',''),date)
        return match[1]+json.dumps(graph,ensure_ascii=False).replace('</','<\\/')+match[3]
    doc=re.sub(r'(<script type="application/ld\+json">)(.*?)(</script>)',update_schema,doc,count=1,flags=re.S)
    return doc

def validate_site(root,records,registry):
    slugs={r['slug'] for r in records}
    for slug in slugs:
        doc=(Path(root)/'site/parallax'/slug/'index.html').read_text(encoding='utf8');match=BODY.search(doc);assert match
        assert len(post_links(match[2],slugs))<=LIMIT,f'{slug}: limite de links excedido.'
        # Reaplicar é uma operação nula: todas as âncoras planejadas já devem existir.
        soup=BeautifulSoup(match[2],'html.parser')
        for r in [r for r in registry['links'] if r['from']==slug]:
            assert any(a.get_text()==r['anchor'] and post_target(a['href'],slugs)==r['to'] for a in post_links(soup,slugs)),f'{slug}: link planejado ausente.'
