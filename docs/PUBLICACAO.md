# Publicação e proteção do servidor

## Destino

- Protocolo: SFTP.
- Host: `ftp.web-ded-128487a.kinghost.net`.
- Usuário: `agenciatweed`.
- Raiz publicada: `/home/agenciatweed/www/`.
- Página inicial: `/home/agenciatweed/www/index.html`.
- Origem local do site: `site/parallax/`.

Senha não deve ser salva em código, documentação, comandos de deploy, URLs ou Git. Fornecer de forma interativa ou por armazenamento seguro de credenciais.

## Limites definidos pelo proprietário em 16/10/2026

A raiz hospeda também materiais de clientes. Não alterar, mover, sobrescrever ou apagar pastas e arquivos existentes fora do escopo do site. O único arquivo existente na raiz que pode integrar uma futura atualização do site é `index.html`.

`assets/` contém recursos do site, mas não deve sofrer limpeza ou substituição integral. Qualquer futura atualização exige uma lista explícita dos arquivos individuais envolvidos. Esta preparação não autoriza publicação automática.

Novos artigos, `robots.txt`, `sitemap.xml` ou configurações de servidor devem ser preparados localmente e ter seu destino e escopo acordados antes do primeiro envio. O plano de SEO não amplia automaticamente a autorização de escrita no servidor.

Proibido usar sincronização com exclusão, espelhamento da raiz, upload recursivo do repositório ou remoção de arquivos não encontrados localmente. Não alterar `old_wp_site/` nem remover sinais do site antigo por exclusão de arquivos sem análise e autorização específicas.

## Inventário observado em 16/10/2026

Listagem somente da raiz; nenhum conteúdo de cliente foi aberto:

```text
ankorsig/
arquetipos/
assets/
conteudo/
dados/
fnx/
index.html
lgbt.zip
mapadobem/
modelica.zip
old_wp_site/
plano.pdf
sig/
sycl/
```

Na listagem SFTP da raiz não apareceram `robots.txt`, `sitemap.xml` ou `.htaccess`. Isso não confirma o comportamento HTTP: regras podem existir na configuração da hospedagem.

## Conferência inicial

Em 16/10/2026, o `index.html` publicado foi baixado apenas para comparação. A cópia está em `.local/publicado/index.html`, excluída do Git. É uma cópia da home, não um backup completo da hospedagem.

O arquivo publicado e `site/parallax/index.html` têm 144288 bytes e o mesmo SHA-256:

```text
0231D4D86F1AE71588CA6479DCDA41CA1AA13C313D2D3888A2CA678465ABA575
```

Na conferência inicial, não foi realizada nenhuma escrita no servidor.

## Publicação autorizada de artigos — 16/10/2026

Posteriormente, o proprietário autorizou expressamente criar e publicar os artigos recuperados, `robots.txt` e `.htaccess` se necessário, preservando a home e a navegação principal. O sitemap acompanha as páginas indexáveis conforme `AGENTS.md`.

Foram publicados 55 artigos em pastas novas, 80 imagens recuperadas em `assets/artigos-restaurados/`, `assets/artigos-tweed.css`, `robots.txt`, `sitemap.xml` e `.htaccess`. Total: 139 arquivos novos. Não houve sobrescrita de arquivo preexistente nem exclusão.

O `.htaccess` restringe a canonicalização às rotas nomeadas do site institucional. As pastas e arquivos de clientes e a instalação antiga não participam das regras. Qualquer nova rota exige revisão dessa lista explícita.

O inventário, manifesto com hashes e resultados estão em `docs/ARTIGOS-RESTAURADOS.md` e `docs/publicacao-artigos-manifesto.json`. Naquela etapa, a home publicada manteve o hash da conferência inicial. Esta autorização não permite alterações gerais nos outros projetos hospedados.

## Extensão do blog — 16/10/2026

O proprietário solicitou reconstruir `/blog/` e seis páginas de séries, com listas minimalistas, e ligar os eyebrows dos artigos a essas séries. A home permanece fora dessa integração. O envio da extensão fica limitado a 121 arquivos: sete páginas novas, 55 artigos com links de categoria e breadcrumbs atualizados, 55 miniaturas novas, dois CSS, sitemap e `.htaccess`. Cópias dos arquivos anteriores ficam em `.local/backups/`, fora do Git. O manifesto específico está em `docs/publicacao-blog-manifesto.json`.

## Revisão da home: manifesto e justificativas — 16/10/2026

Por solicitação do proprietário, foram inseridas suas quatro justificativas dentro das caixas de “Talvez a Tweed não seja para você”, abaixo dos títulos existentes. Apenas quatro elementos `p` foram adicionados; CSS, demais conteúdos, menu e metadados permaneceram intactos. O corpo secundário reutiliza `.card p` (15px, entrelinha 1,65 e cor para superfície tingida), preservando a largura dos títulos.

A versão anterior foi salva em `.local/backups/` e comparada com a origem publicada. A referência aprovada da home para as verificações posteriores passa a ser SHA-256 `9c77eb0c302fdd182cdc2314d6f7abafc5a9da92faff3de7c1e9d38afc0a9e84`. O único arquivo do servidor envolvido nesta revisão é `/home/agenciatweed/www/index.html`.

## Procedimento para uma futura publicação autorizada

1. Preparar e verificar os arquivos locais; revisar a lista exata de destinos.
2. Baixar cópias datadas de cada arquivo remoto que será sobrescrito, fora do Git.
3. Comparar novamente a origem remota para detectar alterações posteriores à preparação.
4. Enviar somente os arquivos aprovados, sem exclusões nem operações em pastas inteiras.
5. Conferir o conteúdo servido por HTTP e os arquivos enviados; verificar links, metadados e comportamento nos tamanhos relevantes.
6. Registrar a lista publicada e o caminho das cópias para eventual restauração pontual.

## Primeiro artigo publicado pela mesa editorial — 17/10/2026

Após aprovação humana em Pronto, foi publicado `/o-custo-invisivel-de-coordenar-o-proprio-marketing/`, com capa de 1344 × 896 px e BlogPosting específico. O FAQ permanece apenas no JSON-LD. A lista explícita de envio teve seis arquivos: capa, artigo, `blog/index.html`, `blog-pequeno-mas-estrategico/index.html`, `sitemap.xml` e `.htaccess` com a nova rota. Não houve alteração na home nem nos 55 artigos anteriores ou em pastas de clientes.

O job `83e1387a-fa22-4d5a-8e1a-8cfd13ac8bed` passou no dry-run, comparação prévia de hashes, upload por arquivo e verificação SFTP/HTTP. Backups locais dos arquivos sobrescritos: `TweedEditorial/backups/publicacoes/83e1387a-fa22-4d5a-8e1a-8cfd13ac8bed/`, fora do Git. O registro de retomada está em `TweedEditorial/.local/publicacoes/83e1387a-fa22-4d5a-8e1a-8cfd13ac8bed.json`.

Página e capa conferidas em desktop/mobile, links dos dois índices verificados e post confirmado na aba Artigos, fora da mesa editorial. Validação final: 56 artigos, sete páginas de blog e 64 URLs no sitemap.

## Links contextuais e recomendações por conteúdo — 17/10/2026

Por solicitação do proprietário, foram reavaliados os 56 artigos e seus dois destinos de Continue a leitura. Os 112 destinos selecionados têm justificativas editoriais em `docs/leituras-relacionadas.json` e são validados contra o catálogo. Todos os 56 HTML foram atualizados, além do sitemap; a home, o menu, as imagens e pastas de clientes não foram alterados.

Foram inseridos também dois links dentro dos textos, sem reescrever frases: o artigo de integração de marketing e vendas aponta para o novo artigo de coordenação do marketing, que aponta para UX como extensão do branding. Âncoras/contextos e razões estão em `docs/planos-links/2026-10-17-integracao-marketing.json`; o registro persistente é `docs/links-internos.json`. Contagem final por corpo: nenhum acima de quatro, máximo atual três; o artigo novo possui um. As duas recomendações finais são contadas separadamente.

Backups dos arquivos anteriores em `TweedEditorial/backups/publicacoes/links-9cb716882a7b26f3/`, fora do Git. Envio por lista explícita, comparação prévia dos hashes e conferência SFTP/HTTP concluídos. As 56 páginas e os 64 endereços do sitemap passaram nos validadores; quatro páginas representativas foram conferidas em desktop e mobile, incluindo os links novos e a integridade da home publicada. As próximas publicações exigem planos atualizados de links e recomendações, e incluem na lista de envio todos os artigos antigos afetados. Fontes e notas vazio é opcional e não produz seção na página.

## Remoção de nota herdada — 17/10/2026

Removida a seção Fontes e notas do artigo o-custo-invisivel-de-coordenar-o-proprio-marketing, incluindo a entrada no índice. A nota veio do rascunho inicial e foi retirada também do registro editorial e dos metadados arquivados. Preservados corpo, links e recomendações. Somente o HTML deste artigo foi enviado, com comparação de hash e confirmação SFTP/HTTP. Backup: TweedEditorial/backups/publicacoes/remocao-notas-a1-20261017/. Manifesto e hashes dos planos foram atualizados sem mudar suas escolhas editoriais.

## Anel nas capas dos artigos — 17/10/2026

Aplicado aos 56 artigos o mesmo anel de luz dos cards da seção 01: 1px, teal e branco, volta em 8 segundos. Pausa fora da tela ou com aba oculta; movimento reduzido mantém borda estática. Alterados tools/article-layout.css e tools/generate_articles.py para persistir nas futuras publicações, além do registro em design.md. Publicados exclusivamente assets/artigos-tweed.css e 56 HTML de artigos, com versão da URL do CSS para atualizar caches. Backup em TweedEditorial/backups/publicacoes/capas-anel-20261017/. Os 57 arquivos foram conferidos por SFTP/HTTP; desktop/mobile e preferência de movimento reduzido verificados. Conteúdo, links, imagens, metadados, sitemap, home e materiais de clientes preservados.


## Publicações sobre valor e atendimento — 17/10/2026

Publicados os artigos seu-cliente-pede-desconto-ou-pede-uma-razao-para-confiar e o-atendimento-esta-desmentindo-o-seu-posicionamento, ambos aprovados em Pronto, com capas 1344 × 896 e FAQ apenas estruturado. Cada publicação passou por análise completa do acervo, planos de links e relacionados, dry-run e verificação SFTP/HTTP. Planos históricos no painel em editorial/planos-links/2026-10-17-a2.json, a3.json e editorial/planos-relacionados/ equivalentes. Inseridos cinco links no corpo no total; nenhum post acima de quatro. Atualizados os pares de recomendação mais pertinentes, além dos índices, sitemap e regras estreitas. Backups por job e88fa5e0-566f-4497-844f-93ccd63565b2 e 79b8dc87-4703-4649-8ea4-d3aec67a05fa. Confirmados 58 artigos e 66 URLs, páginas em desktop/mobile, efeito de capa herdado e home preservada. Os dois registros foram arquivados em Artigos após confirmação.


## FTP normal e retomada de três artigos — 18/10/2026

Por solicitação de Felipe, o publicador passou a usar FTP normal na porta 21, modo passivo, raiz /www/, selecionado por transport em TweedEditorial/editorial/integracao.json. A credencial permanece no cofre TweedEditorial/Kinghost. A autenticação e a leitura da home foram conferidas antes de qualquer escrita. Preservados pré-verificação de hashes, backups individuais, envio temporário, renomeação e confirmação FTP/HTTP. A retomada mantém exatamente a lista do journal original.

Publicados e arquivados após confirmação: uma-boa-restricao-pode-melhorar-uma-ideia; antes-de-investir-em-midia-sua-oferta-precisa-fazer-sentido; personalidade-de-marca-aparece-nas-escolhas-pequenas. Cada job passou em dry-run antes do envio, com planos scope:new-only. Posts antigos não foram reavaliados nem modificados. Backups em TweedEditorial/backups/publicacoes/ nos respectivos IDs dos jobs. Índices, capas, sitemap e regras estreitas de URL atualizados. Home e materiais de clientes preservados.


## Rodada 7 — plano de mídia e comentários — 18/10/2026

Publicados plano-de-midia-2027-alem-de-uma-plataforma e comentarios-parte-do-produto-experiencia-de-marca, aprovados em Pronto, após dry-run e verificação FTP/HTTP. Planos new-only preservaram todas as entradas antigas de relacionados e os HTML antigos. Cada novo post tem um link contextual e duas sugestões por pertinência. Notas preenchidas foram preservadas; FAQ permanece exclusivamente estruturado. Índices do blog e séries, capas, sitemap e regras estreitas atualizados. Backups sob os jobs 07e0b0e0-31f5-4e14-91a6-539eaf05f8d0 e bab89bc8-2b6d-4823-8d34-f117ff12476c. Acervo validado: 63 artigos e 71 URLs; home preservada.


## Manutenção periódica — execução 10 — 19/10/2026

Reavaliados os 63 pares de Continue a leitura contra o acervo atual: nove pares atualizados e 54 preservados. Inseridos cinco links naturais de artigos anteriores para os posts recentes sobre restrições criativas, oferta antes de mídia, personalidade cotidiana, plano de mídia e comentários. Sem reescrita do corpo. Planos históricos no painel: editorial/planos-links/2026-10-19-ciclo10-1.json até -5.json e editorial/planos-relacionados/2026-10-19-ciclo10.json. Cada plano passou em dry-run e verificação FTP/HTTP; backups individuais em TweedEditorial/backups/publicacoes/links-<hash-do-plano>/. Atualizados somente nove artigos e sitemap, mais registros locais. Os 63 artigos e 71 URLs passaram nos validadores; nove páginas ao vivo, cinco âncoras, pares relacionados e desktop/mobile conferidos. Home e materiais de clientes preservados. Próxima manutenção prevista na execução 20.
