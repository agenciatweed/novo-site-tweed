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


## Rodada 11 — quatro publicações — 19/10/2026

Publicados marca-recomendada-por-ia-confianca, microcomunidades-relevancia-alem-das-impressoes, legibilidade-digital-marca-pessoas-ia e identidade-visual-2027-textura-cor-autoria. Aprovação humana em Pronto e capas existentes preservadas. Planos new-only, um link contextual e dois relacionados por artigo; recomendações antigas copiadas intactas. Cada job passou em dry-run, backup individual e verificação FTP/HTTP antes do arquivo em Artigos. Atualizados somente artigo, capa, índices, sitemap e regras estreitas, além dos registros. Backups por ID do job em TweedEditorial/backups/publicacoes/.


## Rodada 20 — vídeo e manutenção — 21/10/2026

Publicado reaproveitamento-video-adaptacao-criativa após aprovação humana, dry-run e confirmação FTP/HTTP dos seis arquivos. Capa 1344 × 896, um link contextual, dois relacionados e FAQ apenas estruturado. Arquivado em Artigos. Backups por job e8cbd758-645e-440d-a407-7f0dd7a368b9. Planos históricos no painel: 2026-10-21-video.json.

Manutenção da execução 20: reavaliados 68 pares; cinco alterados e 63 preservados. Inseridos cinco links de entrada para os cinco posts recentes, sem reescrita, respeitando quatro links por corpo. Publicados seis artigos antigos e sitemap em cinco planos sequenciais, com dry-run, backups e confirmação FTP/HTTP. Planos no painel: 2026-10-21-ciclo20-1.json a -5.json e relacionados 2026-10-21-ciclo20.json. Validadores: 68 artigos e 76 URLs; novo artigo desktop/mobile e home preservada conferidos. Contador concluído; próxima manutenção na execução 30. Commit restrito às saídas desta rodada, deixando as alterações anteriores da home, menu e layout fora do índice.


## Rodada 23 — dados de campanha — 22/10/2026

Publicado qualidade-dados-campanha-conversoes após aprovação humana, dry-run e confirmação FTP/HTTP dos seis arquivos. Capa 1344 × 896, um link contextual, duas recomendações e FAQ apenas estruturado. Arquivado em Artigos após confirmação. Planos new-only preservam integralmente relacionados e HTML antigos. Índices, sitemap e rota estreita atualizados. Backups por job 10919fe7-5d72-40f2-a038-3f89df4f7a91; planos no painel 2026-10-22-dados.json. Validados 69 artigos e 77 URLs; desktop/mobile, menu Blog, capa e home preservada conferidos. Sem manutenção ampla nesta rodada.


## Rodada 25 — IA e contexto de marca — 22/10/2026

Publicado ia-materiais-marca-alem-das-cores após aprovação humana, dry-run e confirmação FTP/HTTP dos seis arquivos. Capa 1344 × 896, um link contextual, duas recomendações e FAQ apenas estruturado. Arquivado em Artigos após confirmação. Planos new-only mantêm intactos os HTML e relacionados antigos; atualizados somente novo artigo, capa, índices, sitemap e rota estreita. Backups por job 2150c50d-8ae2-4f8b-a650-0ce0d8eab477; planos no painel 2026-10-22-ia.json. Validadores: 70 artigos e 78 URLs. Desktop/mobile, menu Blog, capa e home preservada conferidos. Próxima manutenção ampla continua na execução 30.


## Rodada 29 — parcerias de marca — 23/10/2026

Publicado parceria-marca-alem-dos-logotipos após aprovação humana, dry-run e confirmação FTP/HTTP dos seis arquivos. Capa 1344 × 896, um link contextual, dois relacionados e FAQ apenas estruturado. Arquivado em Artigos após confirmação. Planos new-only preservam HTML e recomendações antigas. Atualizados somente capa, novo artigo, blog, série, sitemap e regra estreita de URL. Backups por job 49196560-de07-4e53-9ff0-72088d295b77; planos no painel 2026-10-23-parcerias.json. Validação: 71 artigos e 79 URLs. Desktop/mobile, menu Blog, capa e home preservada conferidos. Manutenção ampla permanece prevista na execução 30.


## Execução manual 30 — manutenção e jornada de compra — 23/10/2026

Revisado o texto jornada-compra-antes-da-campanha somente em metadados, preservando corpo, prompt e ALT. Felipe aprovou Pronto durante a execução; o job 8fe73062-c9b9-470a-a531-a536fb9f262b foi publicado após dry-run e confirmação FTP/HTTP dos seis arquivos e arquivado em Artigos. Capa 1344 × 896, um link contextual, dois relacionados e FAQ exclusivamente estruturado. Planos no painel: 2026-10-23-jornada.json. Desktop/mobile, menu Blog, índices e home preservada conferidos; 72 artigos e 80 URLs validados.

Manutenção da execução 30, antes da publicação: reavaliados 71 pares, quatro atualizados e 67 preservados. Inseridos três links naturais de entrada para os artigos sobre dados de campanha, IA e parcerias, sem reescrever textos. Quatro HTML antigos e sitemap enviados por três planos sequenciais com dry-run e confirmação FTP/HTTP. Planos 2026-10-23-ciclo30-1.json a -3.json e relacionados 2026-10-23-ciclo30.json; backups links-<hash> em TweedEditorial/backups/publicacoes/. Contador concluído, próxima revisão na execução 40.


## Fontes clicáveis — 23/10/2026

Por solicitação do proprietário, os 11 artigos com Fontes e notas passaram a exibir o nome da referência como link clicável. Notas explicativas mantidas em parágrafos separados. Publicados exclusivamente esses 11 HTML, com pré-verificação, backups individuais em TweedEditorial/backups/publicacoes/fontes-clicaveis-20261023/ e confirmação FTP/HTTP. Corpo aprovado, JSON-LD, relacionados, home e sitemap preservados. Atualizados render_body e tools/editorial_sources.py para fontes futuras, com suporte ao formato legado Nome: URL e Markdown [Nome](URL), escapando HTML arbitrário. Registro editorial e hash do catálogo atualizados, sem mudar escolhas de relacionados. Quatro testes da formatação e validadores de 72 artigos/80 URLs aprovados; rótulo e destino NRF conferidos em desktop/mobile.


## Execução manual 34 — atribuição de vendas — 24/10/2026

Publicado atribuicao-vendas-efeito-campanha após aprovação humana, dry-run e confirmação FTP/HTTP dos seis arquivos. Capa 1344 × 896, um link contextual, duas recomendações e FAQ somente estruturado. Fontes Walmart Connect e Google Ads Help exibidas como nomes clicáveis, com notas separadas. Arquivado em Artigos após confirmação. Planos new-only preservam HTML e recomendações antigas. Atualizados apenas artigo, capa, índices, sitemap e rota estreita. Backups por job 1fc722de-3307-484c-a839-4fb3a5d2acda; planos no painel 2026-10-24-atribuicao.json. Validadores: 73 artigos e 81 URLs. Desktop/mobile, capa, menu Blog, fontes e home preservada conferidos.


## Rodada 37 — referências visuais — 24/10/2026

Publicado interpretar-referencias-visuais-cliente após aprovação humana, dry-run e confirmação FTP/HTTP dos seis arquivos. Capa 1344 × 896, um link contextual para atendimento e duas recomendações relacionadas à escuta e às escolhas de marca. FAQ somente estruturado; fonte Pinterest exibida como nome clicável. Arquivado em Artigos após confirmação. Planos new-only preservam HTML e recomendações antigas; atualizados apenas artigo, capa, blog, série, sitemap e rota estreita. Backups por job 56714b7d-d871-4e27-a1ef-d70b8dcb032c; planos no painel 2026-10-24-referencias.json. Validadores: 74 artigos e 82 URLs. Desktop/mobile, anel da capa, menu Blog, fontes e home preservada conferidos. Manutenção ampla permanece prevista para a execução 40.


## Rodada 39 — aprovação de campanhas — 25/10/2026

Publicado aprovacao-campanha-feedback-decisoes após aprovação humana, dry-run e confirmação FTP/HTTP dos seis arquivos. Capa 1344 × 896, um link contextual sobre critérios criativos, dois relacionados e FAQ somente estruturado. Fonte Adobe/NVIDIA exibida como nome clicável. Arquivado em Artigos após confirmação. Planos new-only preservam HTML e recomendações antigas; atualizados somente artigo, capa, blog, série, sitemap e rota estreita. Backups por job d8e5dd6b-a7ea-4b6b-b06b-3026fe948694; planos no painel 2026-10-25-aprovacao.json. Validadores: 75 artigos e 83 URLs. Desktop/mobile, anel da capa, menu Blog, fontes e home preservada conferidos. Manutenção ampla segue prevista para a execução 40.


## Manutenção da execução 40 — 25/10/2026

Reavaliados os dois relacionados dos 75 artigos contra as quatro publicações desde a manutenção anterior. Sete pares atualizados e 68 preservados. Inseridos quatro links naturais de entrada para jornada de compra, atribuição de vendas, interpretação de referências e aprovação de campanhas, respeitando quatro links por corpo e recomendações separadas. Publicados sete HTML e sitemap em quatro planos sequenciais com dry-run, backups e confirmação FTP/HTTP. Planos no painel 2026-10-25-ciclo40-1.json a -4.json e relacionados 2026-10-25-ciclo40.json. Textos dos sete artigos, home e demais páginas preservados; 75 artigos e 83 URLs validados. Contador concluído; próxima revisão na execução 50.


## Rodada 42 — três publicações — 25/10/2026

Publicados mensagem-contexto-momento-cliente, informacoes-empresa-atualizadas-canais e personalizacao-atendimento-corrigir-preferencias após aprovações humanas, dry-runs sequenciais e confirmação FTP/HTTP. Cada artigo tem capa 1344 × 896, um link contextual, duas recomendações e FAQ somente estruturado; fontes exibidas como nomes clicáveis. Todos arquivados em Artigos após confirmação. Planos new-only preservam HTML e recomendações antigas e acompanham o catálogo atualizado a cada envio. Atualizados somente artigos, capas, blog, séries, sitemap e rotas estreitas. Backups por jobs afe20a6c-fb51-4dc3-8fc5-6d11a51e6fcd, a99c92ab-2799-4739-b55d-04b90c217373 e eeea1e0c-4f55-4eba-963d-9b4217e7cc09; planos 2026-10-25-contexto.json, -informacoes.json e -preferencias.json. Validados 78 artigos e 86 URLs, desktop/mobile dos três posts e home preservada. Manutenção ampla permanece na execução 50.


## Rodada 45 — valor do serviço — 26/10/2026

Publicado valor-servico-beneficios-compreender-utilizar após aprovação humana recebida durante a rodada, dry-run e confirmação FTP/HTTP. Capa aprovada de 1344 × 896 preservada; um link contextual, dois relacionados, fonte clicável e FAQ somente estruturado. Atualizados artigo, capa, blog, série, sitemap e rota estreita; home e artigos antigos preservados. Arquivado em Artigos após confirmação. Backups por job b6a6d1c4-ce85-45ab-9b99-178410ddfe00; planos no painel 2026-10-26-valor.json. Validados 79 artigos, 87 URLs e desktop/mobile. Próxima manutenção ampla na execução 50.


## Rodada 46 — propostas e experiência sensorial — 26/10/2026

Publicados proposta-comercial-comparavel-criterios e experiencia-sensorial-marca-sentido após aprovação humana, dry-runs sequenciais e confirmação FTP/HTTP. Capas aprovadas de 1344 × 896 preservadas. Cada artigo tem um link contextual, dois relacionados e FAQ somente estruturado; fontes clicáveis. Arquivados em Artigos após confirmação. Planos new-only preservam HTML e recomendações antigas. Atualizados apenas artigos, capas, blog, séries, sitemap e rotas estreitas. Backups por jobs d7eb574a-ca14-45c0-a3a3-c277c0e0ca23 e ea599a2f-b2e7-4a85-83a0-24baae6e0294; planos no painel 2026-10-26-propostas.json e -sensorial.json. Validados 81 artigos, 89 URLs, desktop/mobile e home preservada. Próxima manutenção ampla na execução 50.


## Rodada 49 — demonstração de produto — 27/10/2026

Publicado demonstracao-produto-ajudar-cliente-decidir após aprovação humana, dry-run e confirmação FTP/HTTP dos seis arquivos. Capa aprovada preservada, um link contextual, dois relacionados e FAQ somente estruturado; fonte clicável. Arquivado em Artigos após confirmação. Planos new-only preservam artigos e recomendações antigos. Validados 82 artigos e 90 URLs; desktop/mobile e home preservada conferidos. Backups por job f684ee53-fa29-45b9-a279-640badccd5e0; planos no painel 2026-10-27-demonstracao.json. Próxima manutenção ampla na execução 50.


## Rodada 50 — redesign e manutenção periódica — 27/10/2026

Publicado redesign-site-transicao-usabilidade após aprovação humana, dry-run e confirmação FTP/HTTP. Capa aprovada preservada, um link contextual, dois relacionados e FAQ somente estruturado. Arquivado em Artigos após confirmação. Avaliados os relacionados dos 83 artigos: oito pares atualizados e 75 preservados. Oito links naturais de entrada conectam artigos antigos às oito publicações desde o ciclo 40, respeitando quatro links por corpo e recomendações separadas. Oito planos sequenciais com dry-run, backups e verificação FTP/HTTP. Textos dos oito artigos preservados; home preservada. Validados 83 artigos e 91 URLs; novo post conferido em desktop/mobile. Planos no painel 2026-10-27-redesign.json, 2026-10-27-ciclo50-1.json a -8.json e relacionados 2026-10-27-ciclo50.json. Próxima manutenção na execução 60.


## Rodada 54 — trocas e imagens de campanha — 28/10/2026

Publicados atendimento-troca-clareza-encaminhamento e imagem-campanha-prova-entrega após aprovação humana, dry-runs sequenciais e confirmação FTP/HTTP. Capas aprovadas preservadas; cada artigo tem um link contextual, dois relacionados e FAQ somente estruturado, com fontes clicáveis. Arquivados em Artigos após confirmação. Planos new-only preservam artigos e recomendações antigas, com catálogo atualizado entre as publicações. Validados 85 artigos e 93 URLs; desktop/mobile e home preservada conferidos. Backups por jobs cb13e3f6-9ebf-42ca-943c-ce18e4eb56de e 2a5b3447-3948-4824-9fc5-67688782acf0; planos 2026-10-28-troca.json e -imagem.json no painel. Próxima manutenção na execução 60.


## Rodada 55 — humor de marca — 28/10/2026

Publicado humor-marca-cliente-alvo-piada após aprovação humana, dry-run e confirmação FTP/HTTP dos seis arquivos. Capa aprovada preservada, um link contextual, dois relacionados e FAQ somente estruturado, com fonte clicável. Arquivado em Artigos após confirmação. Planos new-only preservam artigos e recomendações antigas. Validados 86 artigos e 94 URLs; desktop/mobile e home preservada conferidos. Backups por job 99ff3297-ab1b-446f-8ae8-eab88eb24565; planos no painel 2026-10-28-humor.json. Manutenção ampla segue prevista para a execução 60.


## Rodada manual 59 — capacitação em IA e nome de produto — 29/10/2026

Publicados adocao-ia-equipe-conhecimento-compartilhado e nome-produto-clareza-proposta após aprovação humana, dry-runs sequenciais e confirmação FTP/HTTP. Capas aprovadas preservadas: PNG 1536 × 1024 e JPEG 816 × 544. Cada artigo tem um link contextual, dois relacionados e FAQ somente estruturado, com fontes clicáveis. Arquivados em Artigos após confirmação. Planos new-only preservam artigos e recomendações antigas. Validados 88 artigos e 96 URLs; desktop/mobile e home preservada conferidos. Backups por jobs da910c9d-706d-4076-9c52-c79dc2d43463 e 9a56409f-7a49-4e88-8d8f-0b7570683f30; planos no painel 2026-10-29-capacitacao.json e -nome.json. Embalagem e tendências mantidos para a data aprovada de 30/10. Manutenção ampla segue prevista para a execução 60.


## Manutenção editorial ciclo 60 — 29/10/2026

Reavaliados os dois relacionados dos 88 artigos: cinco pares atualizados e 83 preservados. Inseridos cinco links naturais de artigos anteriores para os cinco publicados desde o ciclo 50: troca e encaminhamento, imagem e prova, humor, capacitação em IA e nome de produto. Textos e capas preservados; máximo de quatro links por corpo. Planos 2026-10-29-ciclo60-1 a -5 e relacionados ciclo60 no painel. Dry-runs e envios sequenciais confirmados por FTP/HTTP, com backups privados e hashes. Home e materiais de clientes preservados.


## Publicação de embalagem — rodada 63 — 30/10/2026

Publicado design-embalagem-gesto-uso na data aprovada, após dry-run e confirmação FTP/HTTP. Capa aprovada PNG 1536 × 1024 preservada, um link contextual e dois relacionados. Planos new-only 2026-10-30-embalagem preservam artigos e recomendações antigas. FAQ somente estruturado e fontes clicáveis. Home e materiais de clientes preservados. Registro privado pelo job 4011b0d2-2ffd-489c-9d91-f17e0a743ca7.
