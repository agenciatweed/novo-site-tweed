# Páginas de artigos restaurados

Modo: Read. Extensão precisa do sistema existente; nenhuma alteração da home ou do DESIGN.md. Conteúdo original, proveniência e imagens recuperados do WordPress antigo.

## Direction contract

THESIS: recuperar leitura e autoridade nas URLs históricas, com a identidade da home aprovada.

OWN-WORLD: campo #0b0c13, Inter local, branco e teal pontual; navbar flutuante e rodapé reaproveitados.

STORY: reconhecer o tema, ler o texto original e encontrar o método ou contato da Tweed.

FIRST VIEWPORT: navegação da home; título forte à esquerda e imagem original à direita; categoria, descrição e autoria. No celular, imagem abaixo do texto.

FORM: extensão editorial especificada pelo usuário; sem sorteio ou comp novo. Container de 1600px e largura cheia preservados por contrato.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance

## Implementação

- Estilos da home extraídos para `assets/artigos-tweed.css`, acrescidos de `tools/article-layout.css`. A home continua com seu CSS original embutido.
- Conteúdo visível sem JavaScript; a faixa de progresso, a borda da navbar e o ano do rodapé são aprimoramentos por JS.
- Os 55 artigos reaproveitam a faixa fixa de 2px da home. A proporção é o deslocamento da página dividido pela área rolável, de zero no topo a 100% no fim. A atualização usa `requestAnimationFrame` sob demanda e eventos passivos; recalcula em redimensionamento, carregamento de fontes/imagens, abertura do índice e restauração da navegação. Sem JS a faixa fica oculta. Com movimento reduzido, o indicador continua funcional, sem animação adicional.
- O corpo público não exibe aviso de recuperação ou migração; esse histórico pertence apenas à documentação técnica.
- Índice recolhível usa `details` nativo; títulos do corpo normalizados como H2 sob um único H1.
- Menu e rodapé apontam para as âncoras da home no domínio canônico. Leituras relacionadas ligam somente artigos recuperados.
- A categoria acima do H1 é um link para a respectiva série do blog. O breadcrumb estruturado passa por Blog e série; a home continua sem links de entrada para o blog.
- Imagens mantêm os arquivos recuperados, sem geração ou alteração visual. Origem, dimensões e SHA-256 estão em `docs/imagens-recuperadas.json`.
- Textos preservados; normalizados atributos legados, headings, espaços vazios e links internos. Datas originais preservadas; quando a data de modificação legada antecede a publicação, o JSON-LD usa a publicação como piso.

## Registro do artefato concluído — 16/10/2026

Esta extensão atende às 55 páginas estáticas em `site/parallax/<slug>/index.html`. As observações abaixo descrevem o código entregue em `tools/article-layout.css` e `tools/generate_articles.py`; não acrescentam tokens ou regras ao sistema global.

- **Paleta e leitura:** campo escuro e acento teal herdados; o corpo editorial usa o texto claro sobre tingido, títulos brancos e links sublinhados com traço teal. O hover dos links acende o texto em teal.
- **Escala tipográfica:** H1 reutiliza Display; descrição reutiliza Lead. Após ajuste solicitado pelo proprietário, H2 do corpo usa `clamp(1.75rem,2.2vw,2.25rem)` (28–36px) e entrelinha 1,2 acima de 720px. Até 720px, mantém Headline e entrelinha 1,12; o corpo passa de 16px para 18px, inclusive listas e citações. A família permanece Inter local. A largura de leitura acompanha o container existente, conforme a decisão de largura cheia.
- **Abertura responsiva:** texto e capa formam duas colunas; a capa ocupa 28%, com mínimo de 220px. Até 960px, passa a 26%, com mínimo de 180px; até 720px, fica abaixo do texto. A capa preserva sua proporção e tem cantos suaves (16px).
- **Navegação editorial:** o índice nativo oferece duas colunas no desktop e uma até 720px. Duas leituras relacionadas são escolhidas por afinidade de categorias e empilham no mesmo breakpoint. O encerramento usa o botão primário existente para a âncora de contato da home.
- **Imagens e operação:** as 80 imagens são arquivos originais recuperados, com dimensões declaradas; a capa recebe prioridade alta e as imagens do corpo carregam sob demanda. Não houve criação de raster. A folha de impressão oculta navegação e blocos auxiliares e adota papel claro apenas na impressão.

**Não canonizado:** o tratamento herdado da categoria em caixa alta acima do H1 é metadado desta extensão, não autorização para introduzir novos kickers decorativos em futuras superfícies. A seta Unicode do retorno foi removida; o link entregue usa somente texto. Nenhuma dessas observações altera `DESIGN.md`, o sidecar ou a home.
