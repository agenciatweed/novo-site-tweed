"""Recomendações finais revisadas pelo GPT; catálogo completo e versão por conteúdo."""
from pathlib import Path
from collections import Counter
import hashlib,json,re,html,math,unicodedata
from bs4 import BeautifulSoup
BASE='https://www.agenciatweed.com.br'
ASIDE=re.compile(r'(<aside class="wrap article-related"[^>]*><h2[^>]*>Continue a leitura\.</h2><div>)(.*?)(</div></aside>)',re.S)
def catalog_hash(records):
 return hashlib.sha256(json.dumps(sorted([(r['slug'],r['title'],r['content']) for r in records]),ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def read_related(root):
 file=Path(root)/'docs/leituras-relacionadas.json'
 return json.loads(file.read_text(encoding='utf8')) if file.exists() else None
def validate_related(plan,records):
 assert plan and plan.get('version')==1 and plan.get('catalogSha256')==catalog_hash(records),'As recomendações precisam ser revistas para o catálogo atual.'
 slugs={r['slug'] for r in records};assert set(plan['articles'])==slugs,'Revise os dois relacionados de todos os artigos.'
 for slug,item in plan['articles'].items():
  assert len(item['targets'])==2 and len(set(item['targets']))==2 and set(item['targets'])<=slugs and slug not in item['targets'],slug+': recomendações inválidas.'
  assert item.get('reason','').strip(),slug+': falta justificativa editorial.'
 return plan

def related_html(slug,plan,records):
 by_slug={r['slug']:r for r in records}
 return ''.join('<a href="'+BASE+'/'+target+'/">'+html.escape(by_slug[target]['title'],quote=True)+'</a>' for target in plan['articles'][slug]['targets'])
def patch_related(document,slug,plan,records):
 match=ASIDE.search(document);assert match,slug+': seção Continue a leitura ausente.'
 result=related_html(slug,plan,records)
 if match[2]==result:return document
 doc=document[:match.start(2)]+result+document[match.end(2):]
 date=related_modified(plan,slug)
 if date:
  def update_schema(match):
   graph=json.loads(match[2])
   for n in graph.get('@graph',[]):
    if n.get('@type') in ('Article','BlogPosting'):n['dateModified']=max(n.get('dateModified',''),date)
   return match[1]+json.dumps(graph,ensure_ascii=False).replace('</','<\\/')+match[3]
  doc=re.sub(r'(<script type="application/ld\+json">)(.*?)(</script>)',update_schema,doc,count=1,flags=re.S)
 return doc
def related_modified(plan,slug):return plan['articles'].get(slug,{}).get('modifiedAt','') if plan else ''
def validate_related_site(root,records,plan):
 validate_related(plan,records)
 for r in records:
  s=BeautifulSoup((Path(root)/'site/parallax'/r['slug']/'index.html').read_text(encoding='utf8'),'html.parser')
  links=s.select('.article-related a');expected=[BASE+'/'+t+'/' for t in plan['articles'][r['slug']]['targets']]
  assert [a['href'] for a in links]==expected,r['slug']+': relacionados divergentes.'

def rank_related(records):
 # Triagem lexical de todo o corpo; a seleção final continua sendo uma análise editorial.
 stop=set('para como mais pelo pela esse essa isso sobre entre quando onde porque pode uma mesmo cada seus suas muito voce marca marcas empresa empresas marketing branding'.split())
 def words(r):
  text=(r['title']+' ')*4+BeautifulSoup(r['content'],'html.parser').get_text(' ')
  text=unicodedata.normalize('NFKD',text.lower()).encode('ascii','ignore').decode()
  terms=[w for w in re.findall('[a-z]{4,}',text) if w not in stop];return Counter(terms)
 counts={r['slug']:words(r) for r in records};df=Counter()
 for v in counts.values():df.update(v.keys())
 vectors={s:{w:(1+math.log(n))*math.log(1+len(records)/(1+df[w])) for w,n in c.items()} for s,c in counts.items()};norm={s:math.sqrt(sum(v*v for v in c.values())) for s,c in vectors.items()}
 ranked={}
 for source,vector in vectors.items():
  scores=[]
  for target,other in vectors.items():
   if source==target:continue
   score=sum(v*other.get(w,0) for w,v in vector.items())/(norm[source]*norm[target] or 1);scores.append((score,target))
  ranked[source]=[{'slug':s,'score':round(score,4)} for score,s in sorted(scores,reverse=True)[:6]]
 return ranked
