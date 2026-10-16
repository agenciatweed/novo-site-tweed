# AGENTS.md — Agência Tweed / Site institucional

## Fonte de verdade

Antes de alterar qualquer arquivo deste projeto:

1. Leia este `AGENTS.md`.
2. Leia `design.md` integralmente e trate as decisões nele como fonte de verdade para identidade visual, layout, tipografia, componentes, espaçamentos e comportamento.
3. Leia os arquivos HTML/CSS/JS existentes antes de criar novas estruturas.
4. Se houver conflito entre uma sugestão deste arquivo e `design.md`, preserve `design.md` e sinalize o conflito antes de alterar o sistema visual.

## Contexto do projeto

Este é o site institucional da Agência Tweed.

A Tweed é uma agência boutique full-service que integra estratégia, branding, design, conteúdo, websites, audiovisual, IA, redes sociais e performance.

O site deve comunicar:
- autoridade sem arrogância;
- criatividade com propósito;
- sofisticação sem afetação;
- proximidade sem amadorismo;
- velocidade com qualidade;
- confiança e visão de negócio.

Não posicionar a Tweed como agência barata, fábrica de posts ou simples terceirização.

O posicionamento central é:
"A agência boutique full-service para empresas que querem centralizar o marketing sem abrir mão de estratégia, qualidade e atendimento sênior."

## Arquitetura técnica

- Site atual: HTML estático.
- Não assumir WordPress.
- Não introduzir framework, CMS, build system ou dependência sem necessidade e sem explicar o benefício.
- Preservar a arquitetura existente sempre que possível.
- Preferir HTML semântico, CSS organizado e JavaScript mínimo.
- Manter compatibilidade com hospedagem estática.

## Domínio canônico

A única versão oficial deve ser:

https://www.agenciatweed.com.br/

Todas as referências internas, canonical URLs, Open Graph URLs, sitemap e dados estruturados devem usar esse hostname.

## SEO e GEO

O site deve ser legível por mecanismos de busca tradicionais e mecanismos de busca por IA.

Regras:
- Não bloquear Googlebot, Bingbot, OAI-SearchBot, ChatGPT-User, PerplexityBot, Perplexity-User, Claude-SearchBot ou Claude-User.
- `GPTBot` e `ClaudeBot` podem permanecer bloqueados, pois não são necessários para aparecer em resultados de busca por IA.
- Toda página indexável deve ter title, meta description, canonical e estrutura de headings coerente.
- Usar dados estruturados Schema.org quando fizer sentido.
- Não criar conteúdo em massa apenas para palavras-chave.
- Priorizar conteúdo útil, específico, original e comercialmente relevante.
- Preservar URLs históricas de artigos recuperados sempre que possível.

## Conteúdo editorial

O objetivo do conteúdo não é "encher blog". Cada página deve ajudar a:
- construir percepção de marca;
- aumentar autoridade;
- esclarecer diferenciais;
- reduzir risco percebido;
- responder perguntas reais de prospects;
- melhorar a capacidade de Google, ChatGPT, Gemini, Claude, Perplexity e outros sistemas entenderem quando recomendar a Tweed.

Priorizar temas ligados a:
- agência boutique x agência grande;
- agência full-service;
- centralização de fornecedores;
- branding e percepção;
- integração entre marketing e vendas;
- estratégia + execução;
- marketing B2B;
- sites como extensão da marca;
- experiência de marca;
- crescimento sem perda de posicionamento.

## Artigos

Preferência de URL:

/slug-do-artigo/
    index.html

Exemplo:

/o-que-o-seu-site-diz-sobre-sua-marca-ux-como-extensao-do-branding/
    index.html

Ao reconstruir um artigo antigo:
- preservar o slug original;
- preservar a intenção e o tema;
- não inventar que o texto novo é reprodução literal do conteúdo perdido;
- atualizar conceitos e exemplos quando necessário;
- manter voz editorial consistente com a Tweed atual;
- adicionar links internos relevantes;
- atualizar sitemap.xml.

## Migração e redirecionamentos

- URL antiga com equivalente real: usar 301 para o equivalente.
- Artigo relevante que pode ser reconstruído: recriar no mesmo slug e responder 200.
- Conteúdo removido sem equivalente e sem valor: considerar 410 após revisão.
- Não redirecionar dezenas de URLs sem relação para a homepage.

## Forma de trabalhar

Antes de mudanças relevantes:
- faça uma leitura do projeto;
- descreva brevemente o que pretende alterar;
- preserve decisões existentes;
- evite mudanças cosméticas fora do escopo;
- não sobrescreva conteúdo útil sem necessidade.

Depois de mudanças:
- verifique links relativos;
- valide HTML/CSS quando possível;
- verifique responsividade;
- verifique canonical e metadados;
- confirme que sitemap e navegação permanecem coerentes;
- liste os arquivos alterados e o motivo.

## Segurança de alterações

### Hospedagem compartilhada com materiais de clientes

- Leia `docs/PUBLICACAO.md` antes de qualquer acesso com escrita ao servidor.
- A raiz `/home/agenciatweed/www/` contém outros projetos e materiais de clientes.
- Não alterar nem apagar pastas e arquivos existentes fora do escopo do site. O único arquivo existente na raiz elegível para uma futura atualização do site é `index.html`.
- Não executar espelhamento, sincronização com exclusão ou upload da raiz do repositório.
- Atualizações de assets exigem uma lista explícita de arquivos; não limpar nem substituir a pasta inteira.
- Novas rotas, arquivos SEO e configurações precisam ter o escopo de publicação acordado antes do primeiro envio.
- Nunca versionar credenciais, contexto pessoal, documentos de carteira ou cópias da hospedagem.

Se o diretório estiver sob Git:
- verifique o estado do repositório antes de começar;
- não faça commit ou push sem solicitação explícita;
- evite alterações fora do escopo solicitado.

Se não estiver sob Git:
- recomende criar um repositório ou backup antes de mudanças amplas.
