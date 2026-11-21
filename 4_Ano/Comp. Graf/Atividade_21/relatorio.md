# Atividade 21 — Inspeção de peças por segmentação de imagens

**Disciplina:** Computação Gráfica  
**Métodos:** K-Médias e ISODATA simplificado  
**Cena:** 72 × 96 pixels, RGB, gerada diretamente com NumPy.

## 1. Implementação

A cena 1 foi integrada à função `criar_cena(variacao)`, preservando a cena 0 original. A nova cena contém duas peças avermelhadas desconectadas, uma peça amarelada e o fundo, com variação horizontal de iluminação e ruído gaussiano. A máscara de referência contém os pixels das duas peças vermelhas.

Foram concluídos os TODOs 04–08 com as implementações do estudo guiado: seleção reprodutível de pixels iniciais, atribuição pelo menor quadrado da distância RGB, atualização pela média de cada grupo, iteração de K-Médias e divisão/fusão do ISODATA didático. Também foram implementadas `mascara_por_cor` e `calcular_iou`.

## 2. Resultados quantitativos

Os experimentos foram executados com 20 passos para K-Médias e 12 etapas para ISODATA. A máscara estimada foi escolhida pelo centroide mais próximo de `(205, 95, 70)`. A referência possui 630 pixels.

| Método | Configuração | Grupos finais | IoU | Observação |
|---|---|---:|---:|---|
| K-Médias | K=2, seed=5 | 2 | 0,6745 | Agrupou as duas famílias de cores dos objetos no mesmo cluster; incluiu a peça amarela. |
| K-Médias | K=3, seed=5 | 3 | 0,6745 | O resultado convergiu para a mesma máscara do teste anterior. |
| K-Médias | K=5, seed=5 | 5 | 0,6745 | Os grupos adicionais dividiram principalmente o fundo, sem separar a peça amarela da vermelha. |
| K-Médias | K=3, seed=6 | 3 | 0,6745 | A inicialização mudou a ordem/posição dos centroides, mas não a máscara final. |
| ISODATA | inicial=2, seed=5 | 3 | 1,0000 | Uma divisão separou as cores dos objetos; demais etapas foram reajustes. |
| ISODATA | inicial=2, seed=6 | 3 | 1,0000 | Houve divisão, fusão e nova divisão, seguidas de reajustes. |

**Observação sobre os valores:** os resultados acima são da execução real do arquivo entregue, não estimativas. A métrica IoU compara a máscara estimada com a máscara booleana conhecida da cena.

## 3. Análise e questões conceituais

**1. Por que as duas peças vermelhas podem pertencer a um único cluster mesmo distantes?**  
Porque o K-Médias utilizado considera somente os valores RGB de cada pixel. A distância entre pixels na imagem não participa do cálculo. Assim, pixels de cores semelhantes recebem o mesmo rótulo, independentemente de estarem em regiões separadas.

**2. Diferença entre cluster de cor e objeto conectado.**  
Um cluster de cor reúne pixels próximos no espaço de características RGB. Um objeto conectado é uma região espacial contínua segundo uma regra de vizinhança. Um mesmo cluster pode conter vários objetos desconectados; inversamente, um objeto pode ser dividido em mais de um cluster.

**3. Quando aumentar K melhora ou piora a separação?**  
Aumentar K pode ajudar quando cores distintas que precisam ser separadas foram agrupadas juntas. Porém, também pode fragmentar uma mesma superfície em vários grupos por causa de iluminação e ruído. Mais grupos não garantem melhor identificação semântica dos objetos.

**4. Efeito da semente.**  
A semente determina quais pixels serão escolhidos como centroides iniciais. Ela pode alterar a trajetória de convergência e o resultado final. Neste experimento, seed=5 e seed=6 produziram a mesma máscara final para K=3, embora a ordem dos centroides tenha mudado. Portanto, nesta cena e configuração, a mudança não alterou o IoU.

**5. Eventos do ISODATA e papel dos limiares.**  
Com seed=5 ocorreu `divisao` na primeira etapa e `reajuste` nas onze seguintes. Com seed=6 ocorreram `divisao`, `fusao`, `divisao` e depois nove `reajuste`. A divisão é permitida quando o desvio padrão de algum canal RGB de um grupo suficientemente grande ultrapassa 25. A fusão ocorre quando a distância RGB entre o par de centroides mais próximo fica abaixo de 28 (e há mais de dois grupos). Esses critérios avaliam dispersão e proximidade de cores, não conectividade espacial.

**6. Melhor IoU e adequação visual.**  
O melhor resultado foi obtido pelo ISODATA nas duas sementes, com IoU=1,0. Ele também é o mais adequado visualmente para o objetivo desta atividade, pois isolou as duas peças vermelhas sem incluir a peça amarela. O K-Médias obteve IoU menor porque agrupou as duas cores de objetos no mesmo cluster selecionado.

## 4. Questão central

Não. Produzir mais grupos não significa necessariamente identificar melhor as peças. O K-Médias com K=5 teve cinco grupos, mas manteve a mesma máscara e o mesmo IoU dos testes com K=2 e K=3. O ISODATA terminou com três grupos e obteve IoU perfeito. O que importa é como os grupos correspondem às classes de interesse, e não apenas sua quantidade.

## 5. Capturas e execução

O diretório `capturas/` contém três visualizações geradas a partir das mesmas matrizes NumPy e dos resultados efetivamente calculados: cena original, máscara de K-Médias e máscara de ISODATA. **Elas são pré-visualizações em arquivo, não capturas da janela OpenGL.** Para produzir as capturas de tela exigidas literalmente pelo enunciado, execute `python segmentacao.py`, pressione `T` para selecionar a cena de inspeção e salve a janela nos modos `1`, `7` (K=3, seed=5) e `9`/`0` (ISODATA, seed=5; modo `0` compara os métodos). O ambiente de execução usado para preparar este pacote não disponibiliza uma janela gráfica OpenGL para capturar.

Para reproduzir os números, instale `numpy` e execute:

```bash
python experimentos.py
```

Para abrir a demonstração interativa, instale também `glfw` e `PyOpenGL` e execute:

```bash
python segmentacao.py
```

Teclas úteis: `T` seleciona a cena de inspeção; `5`, `6` e `7` mostram K-Médias; `8` e `9` mostram ISODATA; `N` avança a etapa nos modos 6 e 9; `R` altera a semente; `K` altera K.
