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

O inventário, manifesto com hashes e resultados estão em `docs/ARTIGOS-RESTAURADOS.md` e `docs/publicacao-artigos-manifesto.json`. A home publicada continua com o hash da conferência inicial. Esta autorização não permite alterações gerais nos outros projetos hospedados.

## Procedimento para uma futura publicação autorizada

1. Preparar e verificar os arquivos locais; revisar a lista exata de destinos.
2. Baixar cópias datadas de cada arquivo remoto que será sobrescrito, fora do Git.
3. Comparar novamente a origem remota para detectar alterações posteriores à preparação.
4. Enviar somente os arquivos aprovados, sem exclusões nem operações em pastas inteiras.
5. Conferir o conteúdo servido por HTTP e os arquivos enviados; verificar links, metadados e comportamento nos tamanhos relevantes.
6. Registrar a lista publicada e o caminho das cópias para eventual restauração pontual.
