# Integração do estúdio editorial

O painel está em `H:\TweedMD\TweedEditorial`, em repositório Git próprio (`agenciatweed/mesa-editorial-tweed`), ignorado pelo repositório do site. Abra `TweedEditorial/Abrir-Estudio.cmd`; o painel usa http://127.0.0.1:4173.

A tarefa horária do Codex, “Mesa editorial Tweed — fila e publicação”, processa solicitações explícitas e executa publicação após aprovação Pronto. Sua especificação durável está em `TweedEditorial/editorial/AUTOMACAO.md`. A criação usa o GPT da tarefa, sem API key no navegador. Exige computador ligado, internet e Codex aberto.

`tools/publicar_editorial.py` recebe `--editorial-root CAMINHO --job ID [--dry-run]`. O wrapper `TweedEditorial/scripts/publicar.py` resolve a localização do site pela configuração. Dependências locais: BeautifulSoup, Pillow, requests, Markdown e Paramiko. As duas últimas foram instaladas em `.local/editorial-runtime`, fora do Git e do FTP.

O publicador:
- valida a revisão humana, o snapshot aprovado, a data, os metadados e o arquivo da capa;
- prepara um build temporário com o gerador já usado pelo site;
- gera BlogPosting com autoria, datas, idioma, editoria, palavras-chave, referências e dimensões reais; mantém FAQs visíveis e não promete rich results;
- preserva HTML de artigos anteriores e a home byte a byte;
- envia somente capa, artigo, blog, seção afetada, sitemap e .htaccess estreito, quando alterados;
- compara hashes remotos antes de sobrescrever, guarda backups privados e verifica o resultado por SFTP e HTTP;
- registra a publicação no painel apenas depois de validar o envio.

A senha está no Gerenciador de Credenciais do Windows (`TweedEditorial/Kinghost`), não em arquivos. A chave do servidor SSH é fixada. Nunca usar mirror, exclusão em massa ou sincronização da raiz FTP. Credenciais precisam ser cadastradas novamente se o fluxo for instalado com outro usuário Windows.

Artigos novos aprovados entram em `docs/artigos-editoriais.json` (criado na primeira publicação), separado do acervo original. `generate_articles.py` e os validadores leem ambos. As miniaturas usam a capa aprovada com apresentação reduzida na listagem, evitando outra imagem artificial ou URL externa. O manifesto de publicação é atualizado após envio.

Em 17/10/2026: seis pautas e rascunho original preservados, fila real vazia; testes reais de persistência/reabertura, entregas GPT por helper, upload e aprovação em cópia isolada; dry-run com 56 artigos e 64 URLs passou; SFTP validado por leitura com credencial do cofre. Nenhum conteúdo de teste foi publicado. A home e os 55 artigos publicados permaneceram intactos. A tarefa horária foi criada ativa; sua primeira execução agendada ainda é posterior à implantação.
