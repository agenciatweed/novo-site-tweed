# Artigos recuperados e publicação

Data de preparação: 16/10/2026.

Foram recuperados os 55 posts publicados retornados pela API pública do WordPress antigo (X-WP-Total: 55; uma página de resultados). Nenhum artigo precisou ser reescrito a partir de snippets.

Fonte de leitura: `https://www.agenciatweed.com.br/old_wp_site/index.php?rest_route=/wp/v2/posts&per_page=100`. A instalação antiga não foi modificada.

## Escopo

- 55 novas pastas com `index.html`, preservando exatamente os slugs.
- 80 arquivos de imagem recuperados em `assets/artigos-restaurados/` e `assets/artigos-tweed.css`.
- Novos `robots.txt`, `sitemap.xml` e `.htaccess` na raiz publicada.
- Nenhuma alteração na home, menu da home, assets existentes ou materiais de clientes.
- Artigos indexáveis e presentes no sitemap, mas sem links de entrada na home.
- `.htaccess` aplica HTTP → HTTPS e sem www → com www somente à home, aos dois arquivos SEO e às 55 rotas nomeadas. Outros caminhos não entram nas regras. Não existe regra de WordPress ou redirecionamento de artigo para a home.

## Conteúdo e rastreabilidade

Textos e datas de publicação originais foram preservados. A recuperação em 16/10/2026 fica registrada apenas na documentação técnica, sem aviso nas páginas públicas, conforme solicitação do proprietário. A adaptação limpa atributos de edição do WordPress, normaliza headings e liga o domínio antigo ao canônico. A comparação de texto normalizado entre fonte e página garante que não houve perda de conteúdo.

`artigos-recuperados.json` guarda os textos e metadados originais. `imagens-recuperadas.json` registra fontes, dimensões e SHA-256 dos arquivos. `publicacao-artigos-manifesto.json` lista os 139 arquivos autorizados, tamanho e hash. Nenhum destes documentos é enviado ao servidor.

## Manutenção local

`python tools/generate_articles.py` regenera os HTMLs e o sitemap. `python tools/validate_articles.py` confere conteúdo, links internos, metadados, robots e integridade da home. Esses utilitários locais usam BeautifulSoup; não há dependência Python, framework ou build na hospedagem. A lista explícita de slugs no `.htaccess` precisa ser revista quando houver novas rotas.

## Relação de artigos

| Título | Publicação original | URL preservada |
|---|---|---|
| Marketing que não termina no lead: por que PMEs precisam integrar marketing e vendas de verdade | 2026-05-15 | [Abrir](https://www.agenciatweed.com.br/marketing-que-nao-termina-no-lead-por-que-pmes-precisam-integrar-marketing-e-vendas-de-verdade/) |
| Efeito Isca (Decoy): como empacotar 3 opções e vender mais sem baixar preço | 2026-03-28 | [Abrir](https://www.agenciatweed.com.br/efeito-isca/) |
| Dívida de Marca: quando sua empresa parece menor do que é | 2026-03-21 | [Abrir](https://www.agenciatweed.com.br/divida-de-marca/) |
| Narrativas Míticas: Construindo a Lenda Inspiradora da Sua Marca | 2026-03-07 | [Abrir](https://www.agenciatweed.com.br/narrativas-miticas/) |
| Crescer sem Perder a Alma: Mantendo o Propósito da Marca na Expansão | 2026-02-28 | [Abrir](https://www.agenciatweed.com.br/crescer-sem-perder-a-alma/) |
| Da Embalagem ao Pós-venda: A Prova de Fogo do Branding na Experiência de Entrega | 2026-02-21 | [Abrir](https://www.agenciatweed.com.br/da-embalagem-ao-pos-venda/) |
| Não Venda, Ajude: A Arte da Reciprocidade no Marketing das PMEs | 2026-02-14 | [Abrir](https://www.agenciatweed.com.br/nao-venda-ajude/) |
| Da Satisfação ao Encantamento: Por que Surpreender o Cliente é o Melhor Branding | 2026-02-07 | [Abrir](https://www.agenciatweed.com.br/da-satisfacao-ao-encantamento/) |
| O Melhor Cliente é Aquele que Você Já Tem: Fidelização e Indicação para Crescimento Sustentável | 2026-01-31 | [Abrir](https://www.agenciatweed.com.br/o-melhor-cliente-e-aquele-que-voce-ja-tem/) |
| Múltiplas Faces da Marca: combinando arquétipos para uma identidade rica | 2026-01-24 | [Abrir](https://www.agenciatweed.com.br/multiplas-faces-da-marca-combinando-arquetipos-para-uma-identidade-rica/) |
| Do Oceano Vermelho ao Azul: Estratégias de Nicho para PMEs Fugirem da Concorrência | 2026-01-17 | [Abrir](https://www.agenciatweed.com.br/do-oceano-vermelho-ao-azul-estrategias-de-nicho-para-pmes-fugirem-da-concorrencia/) |
| O Que o Seu Site Diz Sobre Sua Marca: UX como Extensão do Branding | 2026-01-10 | [Abrir](https://www.agenciatweed.com.br/o-que-o-seu-site-diz-sobre-sua-marca-ux-como-extensao-do-branding/) |
| Marca nas Mãos do Cliente: Como o Conteúdo Gerado pelo Usuário Impulsiona seu Branding | 2026-01-03 | [Abrir](https://www.agenciatweed.com.br/marca-nas-maos-do-cliente-como-o-conteudo-gerado-pelo-usuario-impulsiona-seu-branding/) |
| Além do Anúncio: Como o Boca a Boca Mantém Sua Marca Viva Quando a Propaganda Termina | 2025-12-27 | [Abrir](https://www.agenciatweed.com.br/alem-do-anuncio-como-o-boca-a-boca-mantem-sua-marca-viva-quando-a-propaganda-termina/) |
| Métricas Sem Vaidade: Como Medir o que Realmente Importa no Marketing da PME | 2025-12-20 | [Abrir](https://www.agenciatweed.com.br/metricas-sem-vaidade/) |
| Orçamento de Marketing 2026 para PMEs: proteja sua receita | 2025-12-08 | [Abrir](https://www.agenciatweed.com.br/orcamento-de-marketing-2026-para-pmes/) |
| Menos é mais: o poder de campanhas pequenas com grandes ideias | 2025-12-01 | [Abrir](https://www.agenciatweed.com.br/menos-e-mais-o-poder-de-campanhas-pequenas-com-grandes-ideias/) |
| Sua marca precisa de consistência, não de perfeição | 2025-11-24 | [Abrir](https://www.agenciatweed.com.br/sua-marca-precisa-de-consistencia-nao-de-perfeicao/) |
| Quando tudo parece igual, os arquétipos ajudam sua marca a ser lembrada | 2025-11-17 | [Abrir](https://www.agenciatweed.com.br/quando-tudo-parece-igual-os-arquetipos-ajudam-sua-marca-a-ser-lembrada/) |
| Como parecer grande sem ser grande: os segredos do branding enxuto | 2025-11-10 | [Abrir](https://www.agenciatweed.com.br/como-parecer-grande-sem-ser-grande-os-segredos-do-branding-enxuto/) |
| Como as PMEs podem usar a inteligência artificial sem parecerem robôs | 2025-11-03 | [Abrir](https://www.agenciatweed.com.br/como-as-pmes-podem-usar-a-inteligencia-artificial-sem-parecerem-robos/) |
| Qual é o arquétipo da sua concorrência — e por que você deveria saber disso | 2025-10-27 | [Abrir](https://www.agenciatweed.com.br/qual-e-o-arquetipo-da-sua-concorrencia-e-por-que-voce-deveria-saber-disso/) |
| Se o seu cliente não consegue explicar sua marca, talvez ela ainda não exista de verdade | 2025-10-20 | [Abrir](https://www.agenciatweed.com.br/se-o-seu-cliente-nao-consegue-explicar-sua-marca-talvez-ela-ainda-nao-exista-de-verdade/) |
| A cultura interna é o branding que o cliente ainda vai sentir | 2025-10-13 | [Abrir](https://www.agenciatweed.com.br/a-cultura-interna-e-o-branding-que-o-cliente-ainda-vai-sentir/) |
| Ancoragem: o truque psicológico que molda quanto o cliente acha que vale seu produto | 2025-10-09 | [Abrir](https://www.agenciatweed.com.br/ancoragem-o-truque-psicologico-que-molda-quanto-o-cliente-acha-que-vale-seu-produto/) |
| Marcas memoráveis não gritam — elas fazem sentido | 2025-10-06 | [Abrir](https://www.agenciatweed.com.br/marcas-memoraveis-nao-gritam-elas-fazem-sentido/) |
| O que você vê é tudo o que existe | 2025-10-02 | [Abrir](https://www.agenciatweed.com.br/o-que-voce-ve-e-tudo-o-que-existe/) |
| Marca não se faz no Canva. Se faz no cotidiano. | 2025-09-29 | [Abrir](https://www.agenciatweed.com.br/marca-nao-se-faz-no-canva-se-faz-no-cotidiano/) |
| O que pequenas empresas podem aprender com os erros das grandes | 2025-09-22 | [Abrir](https://www.agenciatweed.com.br/o-que-pequenas-empresas-podem-aprender-com-os-erros-das-grandes/) |
| Clientes não compram produtos: compram a energia da sua marca | 2025-09-15 | [Abrir](https://www.agenciatweed.com.br/clientes-nao-compram-produtos-compram-a-energia-da-sua-marca/) |
| Por que a escassez vende — mas nem sempre | 2025-09-11 | [Abrir](https://www.agenciatweed.com.br/por-que-a-escassez-vende-mas-nem-sempre/) |
| 3 decisões de branding que levaram pequenas marcas a outro patamar | 2025-09-08 | [Abrir](https://www.agenciatweed.com.br/3-decisoes-de-branding-que-levaram-pequenas-marcas-a-outro-patamar/) |
| Framing: a arte invisível que decide o sucesso da sua comunicação | 2025-09-04 | [Abrir](https://www.agenciatweed.com.br/framing-a-arte-invisivel-que-decide-o-sucesso-da-sua-comunicacao/) |
| Branding não acontece só no marketing. Ele vive na operação. | 2025-09-01 | [Abrir](https://www.agenciatweed.com.br/branding-nao-acontece-so-no-marketing-ele-vive-na-operacao/) |
| O paradoxo da escolha | 2025-08-28 | [Abrir](https://www.agenciatweed.com.br/o-paradoxo-da-escolha/) |
| Seu logotipo é bonito. Mas sua marca é clara? | 2025-08-25 | [Abrir](https://www.agenciatweed.com.br/seu-logotipo-e-bonito-mas-sua-marca-e-clara/) |
| A Biblioteca Estratégica da Tweed: os livros que moldam nossa abordagem de Branding e Marketing | 2025-08-22 | [Abrir](https://www.agenciatweed.com.br/a-biblioteca-estrategica-da-tweed-os-livros-que-moldam-nossa-abordagem-de-branding-e-marketing/) |
| O Arcabouço Invisível da Tweed: Os Livros que Moldam Nossas Estratégias | 2025-08-20 | [Abrir](https://www.agenciatweed.com.br/o-arcabouco-invisivel-da-tweed-os-livros-que-moldam-nossas-estrategias/) |
| Sua marca está viva ou só parece uma vitrine bonita? | 2025-08-18 | [Abrir](https://www.agenciatweed.com.br/sua-marca-esta-viva-ou-so-parece-uma-vitrine-bonita/) |
| Marca não é um logotipo: por que PMEs precisam contar boas histórias | 2025-08-11 | [Abrir](https://www.agenciatweed.com.br/marca-nao-e-um-logotipo-por-que-pmes-precisam-contar-boas-historias/) |
| Ninguém compra sozinho | 2025-08-07 | [Abrir](https://www.agenciatweed.com.br/ninguem-compra-sozinho/) |
| O que empresas como Harley-Davidson, Dove e Natura têm em comum com a sua PME | 2025-08-04 | [Abrir](https://www.agenciatweed.com.br/o-que-empresas-como-harley-davidson-dove-e-natura-tem-em-comum-com-a-sua-pme/) |
| Marketing não é persuasão. É arquitetura de escolha. | 2025-07-31 | [Abrir](https://www.agenciatweed.com.br/marketing-nao-e-persuasao-e-arquitetura-de-escolha/) |
| Como marcas locais constroem comunidades mais fortes do que muitas multinacionais | 2025-07-28 | [Abrir](https://www.agenciatweed.com.br/como-marcas-locais-constroem-comunidades-mais-fortes-do-que-muitas-multinacionais/) |
| Você não decide: seu cérebro decide por você (e depois inventa uma desculpa) | 2025-07-24 | [Abrir](https://www.agenciatweed.com.br/voce-nao-decide-seu-cerebro-decide-por-voce-e-depois-inventa-uma-desculpa/) |
| A marca que você posta é a mesma que você entrega? | 2025-07-21 | [Abrir](https://www.agenciatweed.com.br/a-marca-que-voce-posta-e-a-mesma-que-voce-entrega/) |
| O que sua marca comunica quando você não está por perto? | 2025-07-14 | [Abrir](https://www.agenciatweed.com.br/o-que-sua-marca-comunica-quando-voce-nao-esta-por-perto/) |
| Grandes ideias. Pequenas verbas. Marcas que marcam. | 2025-07-07 | [Abrir](https://www.agenciatweed.com.br/grandes-ideias-pequenas-verbas-marcas-que-marcam/) |
| Por que seu negócio ainda não tem uma personalidade clara — e como isso afasta clientes | 2025-07-05 | [Abrir](https://www.agenciatweed.com.br/arquetipos-de-marca-para-pequenas-empresas/) |
| Duas marcas, o mesmo produto — por que uma cresce e a outra desaparece? | 2025-07-03 | [Abrir](https://www.agenciatweed.com.br/posicionamento-de-marca-para-pequenas-empresas/) |
| Sua marca está no manual ou no comportamento? | 2025-07-02 | [Abrir](https://www.agenciatweed.com.br/branding-na-pratica-para-pmes/) |
| Branding não é sobre o que você diz — é sobre o que as pessoas lembram | 2025-07-01 | [Abrir](https://www.agenciatweed.com.br/branding-como-experiencia-do-cliente/) |
| Branding não é orçamento. É intenção. | 2025-06-30 | [Abrir](https://www.agenciatweed.com.br/branding-para-pequenos-negocios/) |
| De sobrevivência à relevância: o poder do branding estratégico nas PMEs | 2025-06-29 | [Abrir](https://www.agenciatweed.com.br/marketing-estrategico-para-pequenas-empresas/) |
| Branding: o superpoder escondido para pequenas empresas | 2025-06-28 | [Abrir](https://www.agenciatweed.com.br/branding-o-superpoder-escondido-para-pequenas-empresas/) |

## Referências técnicas

- [Google: regras de robots.txt](https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec).
- [OpenAI: identificação dos crawlers](https://developers.openai.com/api/docs/bots).

## Situação da publicação

Publicada por SFTP em 16/10/2026, conforme autorização expressa do usuário para os artigos e arquivos SEO/configuração.

- 139 novos arquivos enviados por lista explícita, sem exclusões e sem sobrescrita da home ou assets existentes.
- 55 URLs históricas responderam 200 diretamente; os artigos não redirecionam para a home.
- Os 138 arquivos públicos (55 HTMLs, 80 imagens, CSS, robots e sitemap) foram baixados via HTTP e comparados por SHA-256 com o manifesto: nenhuma divergência. O `.htaccess` foi verificado pelo comportamento HTTP, sem exposição pública do arquivo.
- 12 testes de canonicalização passaram: HTTP e host sem www redirecionam em 301 ao endereço HTTPS com www, para home, artigo representativo, robots e sitemap.
- 13 verificações das rotas de clientes conservaram status, destino de redirecionamento e tamanho informado nos headers anteriores à publicação. Nenhum conteúdo de cliente foi alterado.
- A home publicada conservou o SHA-256 `0231d4d86f1ae71588ca6479dcda41ca1aa13c313d2d3888a2ca678465aba575`.
- Uma URL inexistente continuou retornando 404; nenhuma regra converte erros em homepage.
- Validação estática dos 55 artigos: conteúdo normalizado preservado, um H1, JSON-LD válido, canonical correto, links internos e assets presentes. Robots libera os agentes de busca definidos e bloqueia apenas GPTBot e ClaudeBot.
- QA visual no Chrome: quatro artigos representativos em 1440×1000 e 390×844, sem overflow, imagens quebradas ou erros JS; títulos longos também conferidos em 320, 768 e 1920px. Revisão independente encerrou o único ajuste apontado como resolvido.
- Na publicação inicial, não houve commit ou push. A home não ganhou links para os artigos; eles são descobríveis pelo sitemap e pelas próprias URLs.

## Ajuste autorizado após publicação — 16/10/2026

O proprietário solicitou remover o aviso de recuperação das páginas e autorizou a atualização por SFTP, commit e push. O parágrafo foi removido do gerador e dos 55 HTMLs, junto de sua regra CSS sem uso. A validação passou a comparar diretamente o corpo público com o texto de origem. Os 55 artigos e o CSS foram copiados para backup local fora do Git antes da substituição. A origem histórica permanece registrada nesta documentação, sem mensagem editorial de migração nas páginas públicas.

Resultado detalhado da conferência mantido localmente em `.local/recuperacao/resultado-publicacao.json`, fora do Git e da hospedagem.
