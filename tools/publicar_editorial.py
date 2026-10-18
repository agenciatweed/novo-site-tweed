"""Publica Pronto aprovado via transporte configurado; dry-run não altera site/servidor."""
from pathlib import Path
import argparse,base64,hashlib,json,os,re,shutil,subprocess,sys,tempfile,datetime,errno,io
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'.local/editorial-runtime'))
from bs4 import BeautifulSoup
from PIL import Image
import markdown
from internal_links import merge_plan, patch_document
from related_articles import validate_related,patch_related
BASE='https://www.agenciatweed.com.br'
HOST='ftp.web-ded-128487a.kinghost.net'
REMOTE='/home/agenciatweed/www'
PIN='TLa1PfZFQ3c33qr7ztHYa2RBuj31oB2qrv8unoyANec'
def sha(data):return hashlib.sha256(data).hexdigest()
def load(file,default=None):return json.loads(file.read_text(encoding='utf-8-sig')) if file.exists() else default
def write(file,obj):
    file.parent.mkdir(parents=True,exist_ok=True);tmp=file.with_suffix(file.suffix+'.tmp');tmp.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf8');os.replace(tmp,file)
def fingerprint(item):return sha(json.dumps({k:v for k,v in item.items() if k not in ('automation','publication')},ensure_ascii=False,separators=(',',':')).encode())
def guard(item,job):
    assert job['action']=='publicar' and job['state'] in ('pending','running'),'Solicitação de publicação não está ativa.'
    assert fingerprint(item)==job['snapshot'],'Texto ou capa mudou após a aprovação.'
    assert item.get('automation',{}).get('reviewKey')==review_key(item),'O texto mudou após a revisão automática.'
    assert item['status']=='Pronto' and all(item.get('checks',{}).get(k) is True for k in ('thesis','facts','voice','privacy')),'Revisão não aprovada.'
    assert all(item.get(k,'').strip() for k in ('title','body','keyword','meta','imageAlt','prompt','slug','date')),'Metadados incompletos.'
    assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',item['slug']) and len(item['slug'])<=180,'Slug inválido.'
    assert datetime.date.fromisoformat(item['date'])<=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3))).date(),'A data de publicação ainda não chegou.'
    assert re.fullmatch(r'conteudos/'+re.escape(item['id'])+r'/imagens/[a-f0-9]{64}\.(png|jpg|webp)',item.get('imageFile','')),'Capa local obrigatória.'
def faq_metadata(item):
    pairs=[]
    for block in re.split(r'\n\s*\n',item.get('faq','').strip()):
        lines=block.strip().splitlines()
        if len(lines)>1:
            pairs.append({'q':lines[0].strip(),'a':' '.join(lines[1:]).strip()})
    return pairs

def review_key(item):
    return sha(json.dumps([item.get(k,'') for k in ('title','edition','expert','angle','audience','goal','body','sources','prompt')],ensure_ascii=False,separators=(',',':')).encode())

def render_body(item):
    source=item['body']
    soup=BeautifulSoup(markdown.markdown(source,extensions=['extra','sane_lists']),'html.parser')
    allowed={'p','h2','h3','h4','ul','ol','li','strong','em','a','blockquote','br','code','pre','hr','table','thead','tbody','tr','td','th'}
    for tag in list(soup.find_all(True)):
        if tag.name in ('script','style','iframe','object','embed','form'):tag.decompose();continue
        if tag.name=='h1':tag.name='h2'
        if tag.name not in allowed:tag.unwrap();continue
        href=tag.get('href','');tag.attrs={}
        if tag.name=='a' and re.match(r'^(https?://|/|#|mailto:)',href):tag['href']=href
    # Fontes são visíveis e correspondem às referências do BlogPosting.
    urls=list(dict.fromkeys(re.findall(r'https://[^\s<>\]\)]+',item.get('sources',''))))
    if item.get('sources','').strip():
        section=soup.new_tag('h2');section.string='Fontes e notas';soup.append(section)
        p=soup.new_tag('p');p.string=item['sources'];soup.append(p)
    return str(soup),urls

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--editorial-root',type=Path,required=True);parser.add_argument('--job',required=True);parser.add_argument('--dry-run',action='store_true');parser.add_argument('--links',type=Path,required=True);parser.add_argument('--related',type=Path,required=True);args=parser.parse_args();editorial=args.editorial_root.resolve()
    config=load(editorial/'editorial/integracao.json');assert (editorial/config['siteRoot']).resolve()==ROOT,'Raiz do site divergente da configuração.'
    lock=editorial/'.local/project.lock';lock.parent.mkdir(exist_ok=True)
    try:fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
    except FileExistsError:raise RuntimeError('Painel/automação em gravação. Tente novamente.')
    try:publish(args,editorial)
    finally:os.close(fd);lock.unlink()

def publish(args,editorial):
    queue=load(editorial/'editorial/fila.json');job=next(j for j in queue['jobs'] if j['id']==args.job);doc=load(editorial/'editorial/pautas.json');item=next(i for i in doc['items'] if i['id']==job['itemId']);guard(item,job)
    slug=item['slug'];source=editorial/item['imageFile'];image_bytes=source.read_bytes();assert sha(image_bytes)==source.stem,'Hash da capa divergente.'
    with Image.open(io.BytesIO(image_bytes)) as image:
        image.verify()
    with Image.open(io.BytesIO(image_bytes)) as image:width,height=image.size
    assert width>=600 and height>=400 and width*height<=80_000_000,'Use uma capa de pelo menos 600 × 400 px e no máximo 80 MP.'
    ledger=load(ROOT/'docs/artigos-editoriais.json',[]);previous=next((r for r in ledger if r.get('editorial_id')==item['id']),None)
    journal_path=editorial/'.local/publicacoes'/f"{job['id']}.json";journal=load(journal_path)
    assert previous is None or journal,'Artigo já registrado. Não publique uma nova versão sem revisão.'
    restored=load(ROOT/'docs/artigos-recuperados.json');assert slug not in {r['slug'] for r in restored},'Slug histórico já existente.'
    assert not any(r['slug']==slug and r.get('editorial_id')!=item['id'] for r in ledger),'Slug editorial já existente.'
    if not journal:assert not (ROOT/'site/parallax'/slug).exists(),'Pasta já existente: publicação cancelada.'
    body,citations=render_body(item);img_path='/assets/artigos-editoriais/'+source.name;published=item['date']+'T12:00:00-03:00'
    record={'id':'editorial-'+item['id'],'editorial_id':item['id'],'slug':slug,'title':item['title'],'original_url':BASE+'/'+slug+'/','author':'Felipe Rijo','published':published,'original_modified':published,'categories':[load(editorial/'editorial/editorias.json')['editorias'][item['edition']]['name']],'description':item['meta'],'content':body,'image':{'path':img_path,'width':width,'height':height,'source':item['imageFile'],'sha256':sha(image_bytes)},'image_alt':item['imageAlt'],'keyword':item['keyword'],'citations':citations,'faq':faq_metadata(item)}
    ledger=[r for r in ledger if r.get('editorial_id')!=item['id']]+[record]
    links_plan=load(args.links);assert links_plan['newSlug']==slug,'Plano de links pertence a outro artigo.'
    registry=merge_plan(ROOT,restored+ledger,links_plan)
    related_plan=validate_related(load(args.related),restored+ledger)
    if links_plan.get('scope')=='new-only':
        previous_related=load(ROOT/'docs/leituras-relacionadas.json')
        assert all(related_plan['articles'].get(r['slug'])==previous_related['articles'][r['slug']] for r in restored+ledger if r['slug']!=slug),'Na rodada reduzida, preserve as recomendações dos artigos antigos.'
    thumbs=load(ROOT/'docs/miniaturas-blog.json');thumbs[slug]={'path':img_path,'width':width,'height':height,'source':item['imageFile'],'sha256':sha(image_bytes)}
    section=next(s for s in load(ROOT/'docs/secoes-blog.json') if s['name']==record['categories'][0])
    with tempfile.TemporaryDirectory(prefix='tweed-editorial-') as tmp:
        stage=Path(tmp);shutil.copytree(ROOT/'site/parallax',stage/'site/parallax');shutil.copytree(ROOT/'docs',stage/'docs');shutil.copytree(ROOT/'tools',stage/'tools',ignore=shutil.ignore_patterns('__pycache__'))
        write(stage/'docs/leituras-relacionadas.json',related_plan);write(stage/'docs/links-internos.json',registry);write(stage/'docs/artigos-editoriais.json',ledger);write(stage/'docs/miniaturas-blog.json',thumbs);dest=stage/'site/parallax'/img_path.lstrip('/');dest.parent.mkdir(exist_ok=True);dest.write_bytes(image_bytes)
        env={**os.environ,'TWEED_BUILD_ROOT':str(stage)}
        subprocess.run([sys.executable,str(ROOT/'tools/generate_articles.py')],env=env,check=True,stdout=subprocess.DEVNULL)
        # Preserva o conteúdo anterior e aplica somente os links e relacionados revisados.
        for r in restored+[r for r in ledger if r['slug']!=slug]:
            old=ROOT/'site/parallax'/r['slug']/'index.html'
            if old.exists():
                patched=patch_document(old.read_text(encoding='utf8'),r['slug'],registry,{p['slug'] for p in restored+ledger})
                patched=patch_related(patched,r['slug'],related_plan,restored+ledger)
                if patched==old.read_text(encoding='utf8'):shutil.copyfile(old,stage/'site/parallax'/r['slug']/'index.html')
                else:(stage/'site/parallax'/r['slug']/'index.html').write_text(patched,encoding='utf8')
        subprocess.run([sys.executable,str(ROOT/'tools/validate_articles.py')],env=env,check=True)
        subprocess.run([sys.executable,str(ROOT/'tools/validate_blog.py')],env=env,check=True)
        page=BeautifulSoup((stage/'site/parallax'/slug/'index.html').read_text(encoding='utf8'),'html.parser')
        data=json.loads(page.find('script',type='application/ld+json').string)
        article=next(n for n in data['@graph'] if n.get('@type')=='BlogPosting')
        assert article.get('hasPart',[])==[{'@type':'Question','name':f['q'],'acceptedAnswer':{'@type':'Answer','text':f['a']}} for f in record['faq']],'FAQ estruturado divergente.'
        candidates=[img_path.lstrip('/'),slug+'/index.html','blog/index.html',section['slug']+'/index.html','sitemap.xml','.htaccess']
        candidates=list(dict.fromkeys(candidates+[link['from']+'/index.html' for link in links_plan['links']]+[r['slug']+'/index.html' for r in restored+ledger]))
        # Uma retomada mantém exatamente a lista validada no primeiro envio.
        if journal:candidates=[e['path'] for e in journal['plan']]
        plan=[]
        for rel in candidates:
            new=(stage/'site/parallax'/rel).read_bytes();old=ROOT/'site/parallax'/rel
            if not old.exists() or old.read_bytes()!=new or journal:
                plan.append({'path':rel,'sha256':sha(new),'before':sha(old.read_bytes()) if old.exists() else None,'bytes':len(new)})
        assert plan and all(e['path']!='index.html' for e in plan)
        print(json.dumps({'job':job['id'],'url':record['original_url'],'image':{'width':width,'height':height},'files':plan,'dryRun':args.dry_run},ensure_ascii=False,indent=2))
        if args.dry_run:return
        assert fingerprint(next(i for i in load(editorial/'editorial/pautas.json')['items'] if i['id']==item['id']))==job['snapshot'],'Aprovação mudou.'
        if not journal:
            journal={'job':job['id'],'snapshot':job['snapshot'],'plan':plan,'startedAt':datetime.datetime.now(datetime.timezone.utc).isoformat()};write(journal_path,journal)
        else:
            assert journal['snapshot']==job['snapshot'] and [(e['path'],e['sha256']) for e in journal['plan']]==[(e['path'],e['sha256']) for e in plan],'Plano divergente na retomada.'
            plan=journal['plan']
        deploy(stage/'site/parallax',plan,editorial,job['id'])
        for entry in plan:
            out=ROOT/'site/parallax'/entry['path'];out.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(stage/'site/parallax'/entry['path'],out)
        write(ROOT/'docs/leituras-relacionadas.json',related_plan);write(ROOT/'docs/links-internos.json',registry);write(ROOT/'docs/artigos-editoriais.json',ledger);write(ROOT/'docs/miniaturas-blog.json',thumbs)
        manifest=load(ROOT/'docs/publicacao-artigos-manifesto.json');by_path={e['path']:e for e in manifest}
        for entry in plan:by_path[entry['path']]={k:entry[k] for k in ('path','bytes','sha256')}
        write(ROOT/'docs/publicacao-artigos-manifesto.json',sorted(by_path.values(),key=lambda e:e['path']))
        item['publication']={'state':'published','url':record['original_url'],'publishedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'job':job['id'],'files':[e['path'] for e in plan]};item['url']=record['original_url'];item['image']=BASE+img_path
        write(editorial/'editorial/pautas.json',doc);write(editorial/'conteudos'/item['id']/'metadados.json',item)
        job['state']='done';job['completedAt']=datetime.datetime.now(datetime.timezone.utc).isoformat();write(editorial/'editorial/fila.json',queue)
        journal['completedAt']=job['completedAt'];write(journal_path,journal)
        print('Publicação e arquivos remotos verificados. Faça commit/push dos dois repositórios.')

def deploy(site,plan,editorial,job_id):
    transport=load(editorial/'editorial/integracao.json').get('transport','sftp')
    if transport=='ftp':return deploy_ftp(site,plan,editorial,job_id)
    assert transport=='sftp','Transporte desconhecido.'
    import paramiko
    sys.path.insert(0,str(editorial/'scripts'))
    from credencial_sftp import read as credential
    class Pinned(paramiko.MissingHostKeyPolicy):
        def missing_host_key(self,client,hostname,key):
            assert hostname==HOST and base64.b64encode(hashlib.sha256(key.asbytes()).digest()).decode().rstrip('=')==PIN,'Chave do servidor SFTP divergente.'
    client=paramiko.SSHClient();client.set_missing_host_key_policy(Pinned());client.connect(HOST,username='agenciatweed',password=credential(),allow_agent=False,look_for_keys=False,timeout=20,banner_timeout=20,auth_timeout=20)
    try:
        sftp=client.open_sftp();sftp.get_channel().settimeout(30);remote_data={}
        # Verificação completa antes do primeiro upload. Nunca enumerar nem sincronizar a raiz.
        for entry in plan:
            name=entry['path'];assert '..' not in name.split('/') and not name.startswith('/')
            try:
                with sftp.open(REMOTE+'/'+name,'rb') as f:data=f.read()
                assert sha(data) in (entry['before'],entry['sha256']),f'Arquivo remoto mudou: {name}'
                remote_data[name]=data
            except OSError as e:
                if e.errno!=errno.ENOENT:raise
                assert entry['before'] is None,f'Arquivo remoto ausente: {name}'
                remote_data[name]=None
        backup=editorial/'backups/publicacoes'/job_id
        for name,data in remote_data.items():
            if data is not None:
                target=backup/name;target.parent.mkdir(parents=True,exist_ok=True)
                if not target.exists():target.write_bytes(data)
        for entry in plan:
            name=entry['path'];parts=name.split('/')[:-1];current=REMOTE
            for part in parts:
                current+='/'+part
                try:sftp.stat(current)
                except OSError as e:
                    if e.errno!=errno.ENOENT:raise
                    sftp.mkdir(current)
            if remote_data[name] is not None and sha(remote_data[name])==entry['sha256']:continue
            temp=REMOTE+'/'+name+'.tweed-'+job_id;sftp.put(str(site/name),temp)
            with sftp.open(temp,'rb') as f:assert sha(f.read())==entry['sha256'],'Upload incompleto.'
            sftp.posix_rename(temp,REMOTE+'/'+name)
        for entry in plan:
            with sftp.open(REMOTE+'/'+entry['path'],'rb') as f:assert sha(f.read())==entry['sha256'],'Verificação remota falhou.'
        import requests
        for entry in plan:
            if entry['path']=='.htaccess':continue
            url=BASE+'/'+entry['path'].removesuffix('index.html');r=requests.get(url,timeout=30);r.raise_for_status();assert sha(r.content)==entry['sha256'],'HTTP diverge: '+url
    finally:client.close()
def deploy_ftp(site,plan,editorial,job_id):
    import ftplib,requests
    sys.path.insert(0,str(editorial/'scripts'))
    from credencial_sftp import read as credential
    remote='/www'
    ftp=ftplib.FTP()
    try:
        ftp.connect(HOST,21,timeout=30);ftp.login('agenciatweed',credential());ftp.set_pasv(True)
        def download(name):
            output=io.BytesIO();ftp.retrbinary('RETR '+remote+'/'+name,output.write);return output.getvalue()
        previous={}
        for entry in plan:
            name=entry['path'];assert '..' not in name.split('/') and not name.startswith('/')
            try:data=download(name)
            except ftplib.error_perm as error:
                if not str(error).startswith('550') or entry['before'] is not None:raise
                data=None
            assert data is None or sha(data) in (entry['before'],entry['sha256']),'Arquivo remoto mudou: '+name
            previous[name]=data
        for name,data in previous.items():
            if data is not None:
                backup=editorial/'backups/publicacoes'/job_id/name;backup.parent.mkdir(parents=True,exist_ok=True)
                if not backup.exists():backup.write_bytes(data)
        for entry in plan:
            name=entry['path']
            if previous[name] is not None and sha(previous[name])==entry['sha256']:continue
            current=remote
            for part in name.split('/')[:-1]:
                current+='/'+part
                try:ftp.cwd(current)
                except ftplib.error_perm as error:
                    if not str(error).startswith('550'):raise
                    ftp.mkd(current)
                finally:ftp.cwd(remote)
            temporary=name+'.tweed-'+job_id
            with (site/name).open('rb') as source:ftp.storbinary('STOR '+remote+'/'+temporary,source)
            assert sha(download(temporary))==entry['sha256'],'Upload FTP incompleto.'
            ftp.rename(remote+'/'+temporary,remote+'/'+name)
        for entry in plan:
            assert sha(download(entry['path']))==entry['sha256'],'Verificação FTP falhou.'
            if entry['path']=='.htaccess':continue
            url=BASE+'/'+entry['path'].removesuffix('index.html');response=requests.get(url,timeout=30);response.raise_for_status()
            assert sha(response.content)==entry['sha256'],'HTTP diverge: '+url
    finally:ftp.close()

if __name__=='__main__':
    try:main()
    except Exception as e:raise SystemExit(str(e))
