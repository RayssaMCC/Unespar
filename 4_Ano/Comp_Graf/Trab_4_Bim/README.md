# Trabalho do 4º Bimestre — Computação Gráfica

**Tema:** Processamento e transformação de uma imagem utilizando Zoom, Histograma, Esqueletização, Convolução e Deformações.

**Aluna:** Rayssa Mara Caldini Costa

## Imagem utilizada
Gerada por código NumPy em `imagem_base.py` (128×128, RGB; não há arquivo externo): uma roda (anel + 4 raios + cubo central)
com uma haste diagonal. Foi escolhida porque tem:
- silhueta bem definida (permite binarização e esqueletização);
- baixo contraste de propósito (cinza de 61 a 191) e partes com tons diferentes;
- ruído gaussiano leve e bordas suavizadas.

A **mesma imagem** é usada em todas as demonstrações e na aplicação integrada.

## Dependências e execução
```bash
pip install numpy PyOpenGL PyOpenGL_accelerate    # numpy + PyOpenGL
python main.py                                    # abre a janela OpenGL
```
O PyOpenGL usa **GLUT**; ele precisa estar instalado no sistema
- Windows: `pip install PyOpenGL PyOpenGL_accelerate` costuma bastar (se faltar, instale o `freeglut.dll` e coloque-o na pasta do projeto);
- Ubuntu/Debian: `sudo apt install freeglut3-dev` (ou `libglut3.12`);
- macOS: já vem com o sistema.

Opcional, sem abrir janela: `python main.py --exportar saida` grava todos os painéis em PNG e um `relatorio.txt` com parâmetros e análises
(a pasta `saida` já acompanha o trabalho como exemplo dos resultados).

## Teclas / modos
| Tecla | Ação |
|---|---|
| `0` | Imagem-base (RGB, cinza e histograma) |
| `1` | **Zoom** 2×: original, vizinho mais próximo, bilinear e detalhes 40×40 da borda |
| `2` | **Histograma**: original × equalizada, com os dois histogramas |
| `3` | **Esqueletização**: cinza, máscara binária (Otsu), esqueleto e sobreposição |
| `4` | **Convolução**: original, gaussiano 5×5 (suavização) e nitidez 3×3 |
| `5` | **Deformações**: cisalhamento + escala não uniforme, com borda preta × borda repetida |
| `6` | **Aplicação integrada** (pipeline completo, todas as etapas em grade) |
| `←` / `→` | Coloca um painel em tela cheia / troca de painel |
| `G` | Volta para a grade |
| `T` | Próxima página de texto (parâmetros, análise, objetivo, justificativa) |
| `ESC` ou `Q` | Sair |

Os modos 1 a 5 são **independentes** (cada um parte da imagem-base original). Apenas o modo 6 encadeia as etapas.
Cada modo mostra: original e resultado (imagens), parâmetros e análise (nas páginas de texto `T`).

## Organização do código
| Arquivo | Conteúdo |
|---|---|
| `imagem_base.py` | `gerar_imagem_base()` — cria a imagem com NumPy |
| `processamento.py` | **Algoritmos** (só NumPy): `zoom_vizinho_mais_proximo`, `zoom_bilinear`, `histograma`, `equalizar_histograma`, `expandir_contraste`, `limiar_otsu`, `limpar_mascara`, `esqueletizar` (Zhang-Suen), `convolucao` (genérica, recebe o kernel), `kernel_gaussiano`, `matriz_afim`, `deformar` (mapeamento inverso + bilinear) |
| `cenas.py` | Monta cada modo (painéis + textos) e contém `executar_pipeline()`, a rotina da integração |
| `main.py` | Visualização em OpenGL (texturas, histogramas desenhados com `GL_QUADS`, texto, teclado) |
| `exportar.py` | Exportação opcional em PNG/relatório |

Não é usada nenhuma função pronta de `cv2`, `scipy` ou `skimage` para as cinco técnicas.

## Parte 2 — resumo dos parâmetros
- **Zoom:** fator 2×; vizinho mais próximo (`floor(i/f)`) e bilinear (4 vizinhos, alinhada pelos centros dos pixels).
- **Histograma:** cinza Y = 0,299R + 0,587G + 0,114B; equalização via CDF/LUT.
- **Esqueletização:** binarização por **Otsu** (t = 119) + filtro de maioria 3×3; afinamento iterativo **Zhang-Suen**.
- **Convolução:** função genérica `convolucao(img, kernel)`; gaussiano 5×5 (σ = 1) e nitidez `[[0,-1,0],[-1,5,-1],[0,-1,0]]`.
- **Deformação:** transformação afim com cisalhamento `shx = 0,35` e escala `sx = 1,2`, `sy = 0,8`, centrada na imagem; mapeamento inverso com interpolação bilinear; fora dos limites: cor constante preta × repetição da borda.

## Parte 3 — aplicação integrada (`executar_pipeline` em `cenas.py`)
**Objetivo:** preparar a estrutura do objeto para análise: a entrada tem baixo contraste, ruído e proporção inadequada; o fluxo
produz um esqueleto de 1 pixel que resume a topologia (anel, raios e haste).

**Fluxo (a saída de cada etapa alimenta a seguinte):**
`imagem cinza → [1] convolução gaussiana 5×5 → [2] expansão de contraste (percentis 1–99 %) → [3] deformação (shx = −0,15, sy = 1,25, borda "clamp") → [4] zoom bilinear 2× na ROI automática → [5] binarização (Otsu + maioria 3×3) → [6] esqueletização (Zhang-Suen)`

**Por que esta ordem:**
1. Suavizar primeiro evita que o ruído distorça o histograma e gere ramos falsos no esqueleto.
2. O contraste é ajustado após a suavização para não amplificar o ruído. Usado **expansão linear** (e não equalização) porque ela preserva o formato bimodal fundo/objeto, o que torna o limiar de Otsu confiável.
3. A deformação vem antes do zoom e da binarização para a interpolação trabalhar sobre a geometria final; a borda "clamp" evita regiões pretas que virariam uma terceira classe na binarização.
4. O zoom só na região de interesse dá mais pixels à espessura das partes finas, o que melhora o afinamento.
5. A binarização é a última etapa antes do esqueleto, que exige imagem binária com bordas limpas.

No modo `6`, a grade mostra a imagem original, cada etapa, os histogramas antes/depois do ajuste de contraste e o resultado final sobreposto; use `←/→` para ver qualquer etapa em tela cheia e `T` para as páginas de texto (objetivo, parâmetros, justificativa).
