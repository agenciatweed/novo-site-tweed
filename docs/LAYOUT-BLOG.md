# Índice do blog e séries

Extensão minimalista do sistema editorial. Não altera a home institucional, seu menu ou seu rodapé. Sete rotas restauradas: `/blog/` e os seis slugs `blog-*` preservados em `secoes-blog.json`.

## Direção

Modo Read. Fundo escuro, Inter local e teal pontual herdados. Abertura textual, sem ilustração de seção. Cada série tem nome, descrição concisa, três artigos recentes em linhas de miniatura à esquerda e título à direita, e um link para todos os artigos. A página de série conserva a introdução recuperada, sem prometer frequência de publicação, e lista todos os seus artigos do mais recente ao mais antigo.

## Comparação das grades

Foram renderizadas grades de duas e três colunas em 1280, 1440 e 1920px, com as mesmas descrições e os mesmos 18 títulos. A opção escolhida foi duas colunas e três linhas: em 1280px, todos os títulos ficam em até duas linhas, enquanto três colunas exigem até quatro. A grade final privilegia leitura e espaço para a miniatura, mesmo resultando em página um pouco mais longa. Até 720px, as séries empilham em uma coluna.

Nos navegadores com suporte, `subgrid` alinha o início das listas entre as séries da mesma linha; o fallback conserva a ordem e o conteúdo sem ocultações.

## Estrutura e manutenção

- `tools/blog_pages.py` gera as sete páginas; é chamado por `tools/generate_articles.py`.
- `tools/blog-layout.css` gera `assets/blog-tweed.css`, carregado apenas pelas sete páginas novas.
- Textos, slugs e proveniência ficam em `docs/secoes-blog.json`; miniaturas e hashes, em `docs/miniaturas-blog.json`.
- As 55 miniaturas são versões pequenas já existentes no acervo antigo, sem nova geração ou edição de imagens. Total aproximado: 2,91 MB.
- Os artigos apontam às respectivas séries pelo eyebrow. Os breadcrumbs estruturados passam por Blog e série antes do artigo.
- Sitemap contém 63 URLs: home, 55 artigos e sete páginas do blog. As regras de canonicalização continuam restritas às rotas institucionais explicitamente nomeadas.
- A validação usa `python tools/validate_articles.py` e `python tools/validate_blog.py`. Não há CMS, framework ou ferramenta de publicação na hospedagem.

## Publicação e conferência — 16/10/2026

Foram enviados somente os 121 arquivos do manifesto específico, sem exclusões. Os 120 arquivos públicos enviados foram conferidos por SHA-256 via HTTP; `.htaccess` foi conferido pelos redirecionamentos. As sete páginas retornaram 200 e suas variantes HTTP sem www redirecionaram ao endereço canônico. O fluxo real Blog → série → artigo → eyebrow → mesma série passou no Chrome. A comparação responsiva incluiu 320, 390, 720, 960 e 1440px, sem imagens quebradas, overflow ou erros JS nos casos testados. As grades alternativas foram comparadas também em 1280 e 1920px.

A home manteve o SHA-256 `0231d4d86f1ae71588ca6479dcda41ca1aa13c313d2d3888a2ca678465aba575`. As 13 verificações HTTP das rotas de clientes permaneceram iguais. O relatório operacional está em `.local/recuperacao/blog-publicado.json`, fora do Git.
