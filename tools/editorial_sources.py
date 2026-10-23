"""Fontes opcionais: rótulos clicáveis e notas preservadas, sem HTML arbitrário."""
import html,re
URL=r'https?://[^\s<>]+'
INLINE=re.compile(r'\[([^\]]+)\]\((https?://[^\s<>]+)\)|(https?://[^\s<>]+)')
def link(label,url):return '<a href="'+html.escape(url,quote=True)+'" rel="noopener noreferrer">'+html.escape(label)+'</a>'
def render_line(line):
 labelled=re.fullmatch(r'(.+?):\s*('+URL+r')\s*',line)
 if labelled and not re.search(r'https?://',labelled[1]):return link(labelled[1].strip(),labelled[2])
 out=[];last=0
 for m in INLINE.finditer(line):
  out.append(html.escape(line[last:m.start()]));out.append(link(m[1] or m[3],m[2] or m[3]));last=m.end()
 out.append(html.escape(line[last:]));return ''.join(out)
def render_sources(text):
 return ''.join('<p>'+'<br/>'.join(render_line(line.strip()) for line in block.splitlines())+'</p>' for block in re.split(r'\n\s*\n',text.strip()) if block.strip())
