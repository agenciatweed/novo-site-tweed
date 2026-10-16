# CONTEXT-SEO-GEO.md — Handoff do ChatGPT para Codex

## Objetivo atual

Transformar o site novo da Agência Tweed em uma base sólida para:
1. consolidar a versão atual do site e eliminar sinais conflitantes do site antigo;
2. melhorar SEO técnico;
3. aumentar a probabilidade de a Tweed ser encontrada e recomendada em buscas conversacionais e mecanismos de IA;
4. reconstruir uma biblioteca editorial de autoridade em HTML estático.

A iniciativa começou após um prospect informar que encontrou a Agência Tweed conversando com uma IA.

## Situação técnica conhecida

- O site novo é HTML estático.
- O projeto local informado pelo usuário está em:
  `H:\TweedMD\site\parallax\`
- O domínio canônico definido é:
  `https://www.agenciatweed.com.br/`
- O usuário informou que existem arquivos `design.md` no projeto. Eles devem ser lidos antes de qualquer decisão visual.
- Não usar pressupostos herdados de WordPress/LiteSpeed.

## Decisões tomadas

### Canonização
Consolidar tudo em:

`https://www.agenciatweed.com.br/`

A versão sem `www`, HTTP e outras variações devem redirecionar permanentemente para essa versão quando a infraestrutura permitir.

### Robots
Permitir mecanismos de pesquisa e agentes de busca:

- OAI-SearchBot
- ChatGPT-User
- PerplexityBot
- Perplexity-User
- Claude-SearchBot
- Claude-User
- Googlebot
- Google-Extended
- bingbot
- demais crawlers genéricos

Manter bloqueados, salvo decisão posterior:

- GPTBot
- ClaudeBot

Motivo: estes últimos são associados a usos de treinamento e não são necessários para aparecer em busca por IA.

### Sitemap
`sitemap.xml` deve usar apenas URLs canônicas com `https://www.agenciatweed.com.br/`.

Cada nova página ou artigo indexável deve ser incluído no sitemap.

## Site antigo

Foram identificados sinais de URLs antigas ainda conhecidas pelos mecanismos de busca, incluindo:

- `/home-old/`
- `/servicos/`
- `/quem-somos/`
- `/blog/`

Não redirecionar indiscriminadamente artigos antigos para a homepage.

## Estratégia para artigos antigos

O usuário não possui mais os arquivos originais dos posts.

A estratégia definida é:
- recuperar o que for possível a partir de títulos, snippets, arquivos antigos eventualmente encontrados e outras evidências legítimas;
- quando o texto original não existir, reconstruir um artigo novo sobre o mesmo tema;
- nunca apresentar uma reconstrução como cópia literal do texto perdido;
- preservar o slug antigo quando o tema for recuperado;
- responder 200 nessa URL em vez de 301;
- usar esses artigos como patrimônio editorial para SEO, GEO e autoridade.

## Artigos antigos já identificados como bons candidatos

Prioridade alta:

1. **O Que o Seu Site Diz Sobre Sua Marca: UX como Extensão do Branding**
   `/o-que-o-seu-site-diz-sobre-sua-marca-ux-como-extensao-do-branding/`

2. **Marketing não é persuasão. É arquitetura de escolha.**
   `/marketing-nao-e-persuasao-e-arquitetura-de-escolha/`

3. **Crescer sem Perder a Alma: Mantendo o Propósito da Marca na Expansão**
   `/crescer-sem-perder-a-alma/`

4. **Marketing que não termina no lead: por que PMEs precisam integrar marketing e vendas de verdade**
   `/marketing-que-nao-termina-no-lead-por-que-pmes-precisam-integrar-marketing-e-vendas-de-verdade/`

Outros títulos identificados:

- Da Embalagem ao Pós-venda: A Prova de Fogo do Branding na Experiência de Entrega
- Sua marca precisa de consistência, não de perfeição
- A cultura interna é o branding que o cliente ainda vai sentir
- O que você vê é tudo o que existe
- Do Oceano Vermelho ao Azul: Estratégias de Nicho para PMEs Fugirem da Concorrência
- Se o seu cliente não consegue explicar sua marca, talvez ela ainda não exista de verdade
- 3 decisões de branding que levaram pequenas marcas a outro patamar
- Como marcas locais constroem comunidades mais fortes do que muitas multinacionais
- O Melhor Cliente é Aquele que Você Já Tem: Fidelização e Indicação para Crescimento Sustentável
- A Biblioteca Estratégica da Tweed
- Marca não é um logotipo: por que PMEs precisam contar boas histórias
- De sobrevivência à relevância: o poder do branding estratégico nas PMEs
- Branding: o superpoder escondido para pequenas empresas

## Posicionamento editorial

O conteúdo deve fortalecer a associação:

**Agência Tweed = agência boutique full-service + estratégia + branding + design + conteúdo + websites + audiovisual + IA + social + performance + atendimento sênior e próximo.**

Diferencial central:
reduzir a fragmentação do marketing do cliente, integrando pensamento estratégico e execução em um único parceiro.

Evitar:
- "agência para fazer posts";
- discurso de preço baixo;
- textos genéricos sobre marketing;
- excesso de jargão;
- artigos produzidos apenas para volume.

## Próximo trabalho recomendado ao Codex

Fazer primeiro uma passagem de descoberta SOMENTE LEITURA:

1. Ler `AGENTS.md`.
2. Ler todos os `design.md` aplicáveis.
3. Mapear a estrutura atual do site.
4. Identificar index.html, CSS, JS, assets, navegação, metadados, robots.txt, sitemap.xml e configurações de hospedagem presentes.
5. Identificar se existe Git e informar o estado do working tree.
6. Comparar o projeto existente com estas decisões de SEO/GEO.
7. Não modificar nada nessa primeira etapa.
8. Entregar:
   - resumo da arquitetura;
   - sistema visual encontrado em `design.md`;
   - inconsistências técnicas;
   - itens já corretos;
   - riscos;
   - plano priorizado de implementação.

Depois da aprovação, implementar as correções em fases pequenas e verificáveis.

## Observação importante

O contexto deste arquivo resume decisões de uma conversa anterior. Os arquivos reais do projeto são a fonte de verdade para implementação. Em caso de conflito técnico ou visual, sinalizar antes de sobrescrever decisões existentes.
