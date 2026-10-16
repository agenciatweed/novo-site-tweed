---
name: Agência Tweed
description: Presença de marca em campo escuro, com um único sinal teal que só acende onde importa.
colors:
  teal-tweed: "#08ffb1"
  azul-escuro: "#0b0c13"
  superficie-elevada: "#11131c"
  superficie-elevada-2: "#171a25"
  tinta-sobre-teal: "#04140d"
  teal-claro: "#5cffcb"
  branco: "#ffffff"
  texto-suave: "#a7acb9"
  texto-tenue: "#868da1"
  texto-sobre-tingido: "#d3d7df"
  teal-neblina: "#99ffdf"
  teal-profundo: "#06e0c3"
typography:
  mega:
    fontFamily: "Inter, ui-sans-serif, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: "clamp(2.75rem, 8.5vw, 8rem)"
    fontWeight: 800
    lineHeight: 0.8
    letterSpacing: "-0.05em"
  display:
    fontFamily: "Inter, ui-sans-serif, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: "clamp(2.25rem, 6.2vw, 5rem)"
    fontWeight: 800
    lineHeight: 1.02
    letterSpacing: "-0.045em"
  headline:
    fontFamily: "Inter, ui-sans-serif, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: "clamp(1.875rem, 4.6vw, 3.5rem)"
    fontWeight: 800
    lineHeight: 1.06
    letterSpacing: "-0.035em"
  title:
    fontFamily: "Inter, ui-sans-serif, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: "clamp(1.25rem, 2.2vw, 1.625rem)"
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: "-0.02em"
  metric:
    fontFamily: "Inter, ui-sans-serif, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: "1.5rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.02em"
  lead:
    fontFamily: "Inter, ui-sans-serif, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: "clamp(1.0625rem, 1.7vw, 1.375rem)"
    fontWeight: 400
    lineHeight: 1.65
  statement:
    fontFamily: "Inter, ui-sans-serif, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: "clamp(1.75rem, 4.4vw, 3.25rem)"
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: "-0.035em"
  quote:
    fontFamily: "Inter, ui-sans-serif, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: "clamp(1.375rem, 2.8vw, 2rem)"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.03em"
  body:
    fontFamily: "Inter, ui-sans-serif, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.65
  testimonial-curto:
    fontFamily: "Inter, ui-sans-serif, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: "clamp(1rem, 1.4vw, 1.25rem)"
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: "-0.01em"
  testimonial-medio:
    fontFamily: "Inter, ui-sans-serif, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: "clamp(0.9375rem, 1.05vw, 1rem)"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "-0.01em"
  label:
    fontFamily: "Inter, ui-sans-serif, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: "0.16em"
rounded:
  pilula: "999px"
  card: "18px"
  depoimento: "24px"
  nav: "14px"
  midia: "16px"
  icone: "10px"
  link: "8px"
  foco-trilho: "12px"
  foco: "4px"
  circulo: "50%"
spacing:
  gutter: "clamp(1.25rem, 5vw, 4rem)"
  secao: "clamp(4.25rem, 9.8vh, 7rem)"
  secao-alta: "clamp(5.5rem, 14vh, 9.75rem)"
  card: "clamp(1.5rem, 2.5vw, 2rem)"
  depoimento: "clamp(1.5rem, 2.4vw, 2.25rem)"
components:
  button-primary:
    backgroundColor: "{colors.teal-tweed}"
    textColor: "{colors.tinta-sobre-teal}"
    typography: "{typography.label}"
    rounded: "{rounded.pilula}"
    padding: "0 1.75rem"
    height: "48px"
  button-primary-hover:
    backgroundColor: "{colors.teal-claro}"
  button-ghost:
    backgroundColor: "rgba(11,12,19,.55)"
    textColor: "{colors.branco}"
    rounded: "{rounded.pilula}"
    padding: "0 1.75rem"
    height: "48px"
  button-ghost-hover:
    textColor: "{colors.teal-tweed}"
    backgroundColor: "rgba(11,12,19,.72)"
  button-large:
    padding: "0 2.25rem"
    height: "56px"
  chip:
    backgroundColor: "{colors.superficie-elevada}"
    textColor: "{colors.texto-suave}"
    rounded: "{rounded.pilula}"
    padding: "0.5rem 1rem"
  card:
    backgroundColor: "{colors.azul-escuro}"
    textColor: "{colors.branco}"
    rounded: "{rounded.card}"
    padding: "{spacing.card}"
  testimonial:
    backgroundColor: "{colors.azul-escuro}"
    textColor: "{colors.branco}"
    rounded: "{rounded.depoimento}"
    padding: "{spacing.depoimento}"
    width: "min(86vw, 560px)"
  navbar:
    backgroundColor: "rgba(11,12,19,.72)"
    rounded: "{rounded.nav}"
    padding: "0.75rem 1rem 0.75rem 1.25rem"
  carousel-button:
    backgroundColor: "rgba(11,12,19,.55)"
    textColor: "{colors.branco}"
    rounded: "{rounded.pilula}"
    size: "48px"
---

# Design System: Agência Tweed

## Overview

**Creative North Star: "O Sinal na Escuridão"**

Quase tudo aqui é fundo. O campo é um azul quase preto que ocupa a tela inteira e não pede nada; sobre ele existe um único sinal teal que acende em pouquíssimos lugares. Essa é a economia que governa o sistema: o acento não é cor de marca espalhada, é evento. Quando o teal aparece — num CTA, num numeral de estatística, na borda que gira, na fita de luz do hero —, ele significa alguma coisa. Se aparecesse em tudo, não significaria nada.

A consequência prática é que a hierarquia se resolve por luminância antes de se resolver por tamanho. O olho encontra a headline branca porque ela é a única coisa clara num campo escuro; encontra o botão porque ele é a única superfície saturada. Os efeitos de movimento seguem a mesma lógica: a fita de vidro em WebGL, os feixes que sobem no capítulo final e o halo sob os botões são todos luz atravessando escuridão, nunca textura decorativa aplicada por cima. Nenhum deles roda quando está fora da tela.

O sistema é preciso sem ser rígido. A tipografia é uma só família com entrelinha generosa no corpo e negativa nos títulos; as superfícies são planas e a profundidade vem de luz, não de sombra empilhada. O acabamento é o argumento comercial da agência, então cada estado de interação existe — e cada um deles foi medido contra o fundo animado que passa por trás.

**Key Characteristics:**
- Campo escuro contínuo; nenhuma seção inverte para claro.
- Um único acento, usado com parcimônia deliberada.
- Superfícies planas; profundidade feita de luz e transparência.
- Uma família tipográfica, três pesos reais, escala fluida.
- Todo movimento é condicionado: só desenha o que está em cena, e para por completo sob `prefers-reduced-motion`.

## Colors

Duas cores carregam a marca e o resto é uma rampa de cinzas para texto e bordas. Não existe cor secundária, e essa ausência é a decisão.

### Primary
- **Teal Tweed** (`#08ffb1`): o sinal. Headlines de destaque, CTAs sólidos, numerais de prova, ícones, bordas em foco, títulos de coluna no rodapé, e todos os efeitos de luz (fita do hero, feixes, halos, anel dos cards). Sobre ele o texto é sempre a tinta escura, nunca branco — branco sobre teal cai para 1,3:1 e foi um defeito real corrigido no caminho.
- **Teal Claro** (`#5cffcb`): existe só para o hover do botão primário. Não usar como cor de superfície.
- **Teal Neblina** (`#99ffdf`, escrito no código como `hsl(161 100% 80%)`): o stop mais claro da rampa que faz o degradê na base dos cards de conteúdo e dos depoimentos. Só existe dentro de `radial-gradient`, sempre com alfa entre 20% e 30% — nunca como cor chapada.
- **Teal Profundo** (`#06e0c3`, `hsl(172 95% 45%)`): o stop mais saturado e puxado para o ciano da mesma rampa, no canto oposto do degradê. Mesma regra de uso: só dentro de radial, nunca como preenchimento sólido.

### Neutral
- **Azul-Escuro** (`#0b0c13`): o campo. Fundo de página, base de todo card, tinta de véus e scrims.
- **Superfície Elevada** (`#11131c`) e **Superfície Elevada 2** (`#171a25`): degraus de elevação tonal para chips e superfícies que precisam se separar do campo sem usar borda.
- **Tinta Sobre Teal** (`#04140d`): a única cor de texto permitida sobre o acento. 14,4:1.
- **Branco** (`#ffffff`): headlines, texto de card, rótulos de botão fantasma.
- **Texto Suave** (`#a7acb9`): corpo e legendas sobre fundo chapado. 8,6:1 sobre o campo.
- **Texto Tênue** (`#868da1`): metadados, rótulos da trilha, linha de copyright. É o piso — nada abaixo disso.
- **Texto Sobre Tingido** (`#d3d7df`): corpo e legendas quando a superfície tem degradê teal ou fundo animado por trás. Existe porque o cinza normal reprova AA nessas condições.

### Named Rules

**A Regra do Sinal Único.** O teal ocupa menos de 10% de qualquer tela. Se uma peça nova precisa de teal em dois lugares que competem entre si, um dos dois está errado.

**A Regra do Fundo que Anda.** Texto secundário sobre superfície com degradê ou animação usa `texto-sobre-tingido`, não `texto-suave`. Fundo em movimento levanta o piso de luminância e o cinza padrão não sobrevive — isso foi medido três vezes na construção, e três vezes reprovou.

**A Regra da Tinta Escura.** Sobre teal, o texto é `tinta-sobre-teal`. Nunca branco.

## Typography

**Display Font:** Inter (com `ui-sans-serif, system-ui, Segoe UI, Roboto, sans-serif`)
**Body Font:** Inter — a mesma família em toda a página
**Label/Mono Font:** nenhuma; a marca não usa uma terceira voz

**Character:** uma única grotesca neutra levada aos dois extremos. Nos títulos ela é pesada e apertada, com tracking negativo até -0,05em, e ocupa a largura toda antes de quebrar linha. No corpo ela relaxa: peso normal, entrelinha 1,65, sem tracking. A tensão entre esses dois estados é o que dá caráter — não há uma segunda fonte fazendo esse trabalho.

**Realidade dos pesos:** o repositório de marca entrega três faces estáticas (Regular, Medium, Bold) mais o Bold Itálico, auto-hospedadas em WOFF2 com subset de 492 glifos. A escala CSS usa cinco passos (400/500/600/700/800), mas as faixas declaradas em `@font-face` mapeiam 500–600 para Medium e 700–800 para Bold, com `font-synthesis: none`. Ou seja: **existem três pesos reais.** Escrever 800 ou 700 dá o mesmo desenho, e isso é proposital — nada é falsificado pelo navegador.

### Hierarchy
- **Mega** (800, `clamp(2.75rem, 8.5vw, 8rem)`, line-height 0,8): numerais de capítulo ao fundo, em branco a 5,5% de opacidade. Decorativo e `aria-hidden`.
- **Display** (800, `clamp(2.25rem, 6.2vw, 5rem)`, line-height 1,02): o h1 do hero e o título do clímax. Um por página.
- **Headline** (800, `clamp(1.875rem, 4.6vw, 3.5rem)`, line-height 1,06): abertura de capítulo. Sem `max-width` — só quebra ao encostar nos 1600px.
- **Title** (700, `clamp(1.25rem, 2.2vw, 1.625rem)`, line-height 1,25): títulos de card e etapas do método.
- **Metric** (700, `1.5rem` fixo, line-height 1,2, cor teal): os três números do rodapé do hero (marcas atendidas, anos, interlocutor). Fixo, não fluido — são três dígitos e não precisam escalar com a viewport.
- **Lead** (400, `clamp(1.0625rem, 1.7vw, 1.375rem)`, line-height 1,65): o parágrafo de abertura de cada capítulo.
- **Statement** (800, `clamp(1.75rem, 4.4vw, 3.25rem)`, line-height 1,1): a declaração isolada que fecha um capítulo argumentativo — "A marca ficou menor que o negócio.", "Marcas não crescem por barulho...". Maior que Headline em peso visual apesar de menor em tamanho de fonte, porque fica sozinha na página.
- **Quote** (700, `clamp(1.375rem, 2.8vw, 2rem)`, line-height 1,2): a citação dos fundadores na seção "quem somos". Usa `text-wrap:balance`, diferente do Statement — é a única citação da página e pode se dar ao luxo de balancear.
- **Body** (400, `1.0625rem`, line-height 1,65): texto corrido.
- **Testimonial Curto** (400, `clamp(1rem, 1.4vw, 1.25rem)`, line-height 1,45): corpo dos depoimentos com texto breve — o tamanho maior é o que evita um card quase vazio.
- **Testimonial Médio** (400, `clamp(.9375rem, 1.05vw, 1rem)`, line-height 1,6): corpo dos depoimentos com texto mais longo. Ver a Regra dos Dois Corpos abaixo.
- **Label** (600, `0.8125rem`, tracking 0,16em, caixa alta): eyebrows de capítulo, legendas de figura, títulos de coluna do rodapé.

### Named Rules

**A Regra da Largura Cheia.** Títulos e texto corrido não têm `max-width`; vão até a borda dos 1600px e só quebram ali. Foi decisão explícita do cliente. O custo está medido: a mediana fica em 119 caracteres por linha, acima das 65–75 recomendadas. Quem for revisitar isso deve saber que é escolha, não descuido.

**A Regra do Tracking Negativo.** Todo título acima de 1,25rem carrega tracking negativo, começando em -0,02em e chegando a -0,05em no maior. Texto de corpo nunca leva tracking.

**A Regra dos Dois Corpos.** O texto de um depoimento nunca leva um terceiro tamanho. Curto usa Testimonial Curto; qualquer coisa mais longa usa Testimonial Médio. É o que aproxima a altura dos cards no trilho sem cortar a palavra de ninguém — resolver isso com um terceiro degrau só voltaria a espalhar a variação que os dois já contêm.

## Layout

O container é `1600px` com gutter fluido de `clamp(1.25rem, 5vw, 4rem)`, o que dá 1472px de conteúdo útil no desktop. Tudo respeita essa grade **exceto três blocos deliberadamente full-bleed**: a esteira de serviços, o trilho de depoimentos e o campo de feixes do capítulo final. Eles saem do container e medem a viewport inteira; o contraste entre a grade contida e esses três escapes é parte do ritmo da página.

O ritmo vertical tem dois valores: `clamp(4.25rem, 9.8vh, 7rem)` para seção normal e `clamp(5.5rem, 14vh, 9.75rem)` para seção alta. **No mobile os dois caem pela metade** — a mesma folga que respira no desktop vira rolagem vazia no celular.

Breakpoints, em ordem de acionamento: `1180px` (trilha de capítulos aparece; pilares vão de 5 para 3 colunas), `960px` (grades de 3 viram 1; fundadores empilham), `900px` (links secundários da navbar somem, sobra o CTA), `760px` (pilares para 2), `720px` (ritmo vertical pela metade, esteira ganha segunda linha, hero compacta), `480px` (pilares e grade de 4 para 1) e `420px` (botões ocupam a largura toda).

A navbar é flutuante: `top/left/right: 1rem`, nunca colada nas bordas. O `scroll-padding-top: 6.5rem` no `html` compensa a altura dela nos âncoras.

### Named Rules

**A Regra dos Três Escapes.** Só três blocos furam a grade de 1600px, cada um por um motivo estrutural: a esteira precisa de largura infinita, o trilho precisa de espaço para o card cortado sugerir continuação, o campo de luz precisa cobrir a seção inteira. Um quarto escape precisa justificar-se ou não entra.

## Elevation & Depth

**Este sistema é plano.** Nenhuma superfície flutua por sombra difusa em repouso. A profundidade vem de três outros mecanismos: **elevação tonal** (o campo sobe de `#0b0c13` para `#11131c` e `#171a25`), **transparência com desfoque** (navbar e botão fantasma usam `backdrop-filter: blur(16px) saturate(140%)` sobre uma tinta escura) e **luz** (glows radiais, feixes em canvas, a fita em WebGL, o anel giratório).

O vocabulário de sombra é curto de propósito — quatro entradas na página inteira, e três delas são estado, não repouso.

### Shadow Vocabulary
- **Anel de foco do botão** (`box-shadow: 0 0 0 6px rgba(8,255,177,.14)`): só no hover do botão primário. Em repouso o mesmo anel existe com spread 0, para a transição ter de onde sair.
- **Assentamento do depoimento** (`box-shadow: 0 24px 48px -28px rgba(0,0,0,.9)`): a única sombra de repouso do sistema. Escura, muito difusa, quase invisível — separa o card do campo sem sugerir que ele levita.
- **Luz interna do card** (`box-shadow: inset 0 -16px 24px -4px rgba(255,255,255,.10)`): sobe da borda inferior para dentro. É a assinatura dos cards com degradê.
- **Halo do botão** (elemento próprio, `filter: blur(11px) saturate(120%)` sobre um radial teal): nasce 7px abaixo do botão e sobe ao acender. Não é `box-shadow` porque precisa viver fora e atrás do botão.

### Named Rules

**A Regra da Luz no Lugar da Sombra.** Quando um elemento precisa de destaque, ele acende — não levanta. Sombra colorida só existe com deslocamento e desfoque reais; halo de deslocamento zero é decoração e está proibido.

## Shapes

Duas linguagens de forma convivem, separadas por função. **Ação é pílula:** todo botão, chip e controle de carrossel usa `999px`. **Superfície é retângulo suavizado:** cards em `18px`, depoimentos em `24px`, navbar em `14px`, a moldura da foto dos fundadores em `16px`, caixa de ícone em `10px`. A trilha de capítulos usa círculos de 9px.

Dois raios menores completam a escala, ambos ligados a estado em vez de conteúdo: o fundo do link de navbar no hover usa `8px`, e o anel de foco por teclado usa `4px` como padrão global — qualquer elemento focável sem raio próprio herda esse valor, e o trilho de depoimentos, que é mais arredondado que a média, sobrescreve para `12px` só no próprio foco.

A borda mais característica do sistema não é uma cor: é um **anel de luz giratório**. Os cards de conteúdo têm um `::before` com `conic-gradient` cujo ângulo é animado por `@property`, recortado em anel de 1px por `mask-composite: exclude`. A luz percorre a borda a cada 8s. Onde `mask-composite` não existe, o fallback é uma borda teal fixa a 22%.

Os depoimentos carregam uma inclinação alternada de meio grau que se desfaz no hover — o único lugar do sistema onde a geometria não é ortogonal.

### Named Rules

**A Regra Ação/Superfície.** Se clica, é pílula. Se contém, é retângulo suavizado. Não existe botão retangular nem card em pílula.

## Components

O caráter geral, escolhido com o cliente: **vivos, com luz própria.** Cada elemento interativo tem uma resposta luminosa além da mudança de cor — e todas elas morrem sob `prefers-reduced-motion`, onde só as transições de cor sobrevivem.

### Buttons
- **Shape:** pílula (`999px`), altura mínima 48px, 56px na variante grande.
- **Primary:** fundo `teal-tweed`, texto `tinta-sobre-teal`, peso 600. Hover leva o fundo para `teal-claro` e abre um anel de 6px em teal a 14%.
- **Ghost:** vidro — `rgba(11,12,19,.55)` com `backdrop-filter: blur(16px) saturate(140%)`, borda branca a 28%, texto branco. Hover leva borda e texto para teal. Carrega uma costura de luz de 1px na base, 70% da largura, que sobe de 20% para 80% de opacidade.
- **Halo:** todo botão vive dentro de um `.btn-wrap` com `isolation: isolate`. O halo teal é um `::after` do invólucro, não do botão — num pseudo-elemento do próprio botão o `transform` do hover criaria contexto de empilhamento e o `z-index: -1` passaria a pintar acima do fundo.
- **Hover / Focus:** elevação de 2px e escala 1,02 em 300ms. O halo acende também no `:focus-within`, então quem navega por teclado recebe a mesma afordância.

### Chips
- **Style:** pílula, fundo `superficie-elevada`, texto `texto-suave`, borda branca a 9%, padding `.5rem 1rem`, sem quebra de linha.
- **State:** hover leva a borda para teal a 24% e o texto para branco.
- **Contexto:** vivem exclusivamente na esteira infinita de serviços, que corre da direita para a esquerda em 38s e pausa no hover. Sob movimento reduzido a esteira vira lista estática com todos os itens visíveis.

### Cards / Containers
- **Corner Style:** `18px`.
- **Background:** seis radiais empilhados sobre o campo — três escuros no topo, que limpam a área de leitura, e três teal na base, que fazem o degradê.
- **Shadow Strategy:** sem sombra externa; a luz interna sobe da borda inferior. Ver Elevation & Depth.
- **Border:** o anel giratório de 1px. Ver Shapes.
- **Internal Padding:** `clamp(1.5rem, 2.5vw, 2rem)`.
- **Variante translúcida:** no capítulo final o card zera a cor de fundo e baixa os radiais escuros para 55%, deixando os feixes animados atravessarem. O degradê teal permanece.

### Testimonial (signature)
- Card de `min(86vw, 560px)`, raio `24px`, borda teal a 20%, degradê teal na base, inclinação de ±0,5° que se desfaz no hover.
- Corpo em dois tamanhos conforme o comprimento do depoimento — é o que aproxima as alturas sem cortar a palavra de ninguém.
- Trilho horizontal full-bleed com `scroll-snap-align: start` e `scroll-padding-inline` igual ao gutter, para que a posição de snap coincida com o alvo que o JS calcula.
- **Paginação por borda de card:** o botão de avanço procura o primeiro card que não termina dentro da janela e alinha o início dele à esquerda. Um card cortado na direita vira o primeiro da próxima página, nunca continua pela metade.
- Controles acima do trilho, alinhados à direita, para o visitante ver o comando antes de precisar dele.

### Navigation
- **Navbar:** flutuante, vidro (`rgba(11,12,19,.72)` + `blur(14px) saturate(140%)`), raio `14px`, borda branca a 9% que vira teal a 24% ao rolar.
- **Links:** `texto-suave` a 500, alvo de 44px, hover leva a branco com fundo branco a 5%. O CTA é um botão primário e exige `:not(.btn)` nas regras de cor do link — sem isso a especificidade do `:hover` do link vence a cor do botão.
- **Trilha de capítulos:** coluna fixa à direita, visível acima de 1180px. Pontos de 9px que acendem em teal no capítulo ativo; o rótulo é absoluto e `pointer-events: none`, para não criar link invisível sobre o texto.
- **Mobile:** abaixo de 900px os links secundários somem e sobra o CTA.

### Icons
- Ícones de traço em `viewBox` 24×24, 22px, dentro de caixa de 44px com fundo teal a 8% e raio `10px`.
- No capítulo final os ícones aparecem sem caixa, a 44px, tingidos por `mask` com `mask-mode: alpha` explícito. **O `alpha` é obrigatório:** em SVG o `match-source` do Chrome resolve como luminância, e arte preta zera a máscara. A arte vai embutida como `data:` URI, porque em `file://` o Chrome bloqueia máscara vinda de URL externa.

## Do's and Don'ts

### Do:
- **Do** medir contraste contra o fundo composto, não contra o campo chapado. Onde há degradê, feixe ou fita, o piso de luminância sobe — o método que funcionou foi rasterizar a superfície e amostrar o pixel real sob cada nó de texto.
- **Do** usar `texto-sobre-tingido` para texto secundário sobre qualquer superfície com degradê ou animação.
- **Do** fechar todo movimento em porta de visibilidade: `IntersectionObserver` mais `visibilitychange`, para o canvas parar quando sai de cena.
- **Do** oferecer uma alternativa real em `prefers-reduced-motion`, não um `0.01ms` global. Movimento morre; feedback de cor e borda sobrevive.
- **Do** manter o cachorrinho Tweed em opacidade cheia sempre que ele aparecer. É regra do repositório de marca.
- **Do** declarar `width`/`height` em toda imagem, e proporções por fonte quando um `<picture>` troca a arte entre breakpoints.

### Don't:
- **Don't** virar agência de tráfego genérica: nada de gradiente roxo-azul, ícone 3D flutuante, selo de resultado garantido ou número inflado. O posicionamento da casa proíbe promessa que ela não controla, e o visual precisa obedecer o mesmo limite.
- **Don't** virar site institucional corporativo: sem foto de banco de imagens apontando para gráfico, sem azul corporativo, sem texto que caberia em qualquer empresa. Se a peça passaria por outra agência sem trocar uma palavra, ela falhou.
- **Don't** usar branco sobre teal. É 1,3:1.
- **Don't** espalhar o acento. Teal em tudo é teal em nada.
- **Don't** inverter uma seção para fundo claro. O campo escuro é contínuo do topo ao rodapé.
- **Don't** aplicar `will-change` como configuração de base. É dica pontual para animação conhecida, não item de checklist — e já existe dívida registrada de 19 elementos promovidos em repouso.
- **Don't** animar `transform` num keyframe de entrada em elemento que também precisa de `transform` no hover. Use `translate` para a entrada; com `animation-fill-mode: both` o quadro final trava a propriedade e o hover morre em silêncio.
