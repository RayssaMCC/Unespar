# Visualizador e Manipulador de Objeto 3D (OpenGL + Python)

Este projeto é uma aplicação interativa desenvolvida em **Python** e **PyOpenGL** para a manipulação e visualização de um objeto 3D (cubo colorido), demonstrando conceitos essenciais de Computação Gráfica como transformações geométricas 2D e 3D, matrizes Model-View-Projection, projeções em perspectiva e paralela, e visualização auxiliar 2D (minimapa).

##  Requisitos Prévios do Sistema

Para executar esta aplicação, é necessário ter instalado:
- **Python 3.8** ou superior.
- Suporte a **OpenGL 3.3 Core Profile** na placa de vídeo.

##  Instalação das Dependências

Instale as bibliotecas necessárias utilizando o `pip`:

```bash
pip install PyOpenGL glfw numpy
```


## Como Executar o Projeto

1. Certifique-se de que o arquivo principal (`manipulador3d.py`) e suas dependências estão na mesma pasta.
2. Abra o terminal / prompt de comando no diretório do projeto.
3. Execute o script principal:

```bash
python manipulador3d.py
```

---

## Controles da Aplicação

| Ação | Tecla(s) |
| --- | --- |
| **Translação X / Y** | Setas direcionais (`←`, `→`, `↑`, `↓`) |
| **Translação Z (Profundidade)** | `W` (aproximar) / `S` (afastar) |
| **Rotação no Eixo X** | `I` / `K` |
| **Rotação no Eixo Y** | `J` / `L` |
| **Rotação no Eixo Z** | `U` / `O` |
| **Escala Uniforme** | `+` (aumentar) / `-` (diminuir) |
| **Projeção Paralela** | `1` |
| **Projeção Perspectiva** | `2` |
| **Ajustar FOV** | `Q` (diminuir) / `E` (aumentar) |
| **Mover Observador em X (View)** | `A` (esquerda) / `D` (direita) |
| **Alternar Pivô (Origem / Externo)** | `P` |
| **Alternar Ordem de Composição** | `3` (Modo 1: `T × R × S` \| Modo 2: `R × T × S`) |
| **Ativar/Desativar Órbita** | `B` |
| **Modo de Comparação Rápida** | `C` |
| **Resetar Transformações** | `Espaço` |
| **Sair da Aplicação** | `ESC` |

##  Funcionalidades Implementadas

1. **Transformações 3D Combinadas:** Composição correta da matriz `Model` englobando Translação, Rotação nos eixos X, Y e Z, e Escala uniforme.
2. **Comparação de Ordem de Composição:** Demonstração prática da não-comutatividade de matrizes ($A \times B \neq B \times A$).
3. **Rotação com Pivô Movel:** Suporte a rotação ao redor do centro do objeto ou em torno de um pivô externo $C = (1, 0, 0)$.
4. **Movimento de Órbita:** Rotação do objeto em torno de um ponto no espaço.
5. **Projeções 3D:** Comparações diretas entre projeção **Paralela (Ortográfica)** e **Perspectiva** alteráveis em tempo real.
6. **Controle de FOV:** Modificação do Field of View na projeção perspectiva (limite de 20° a 120°).
7. **Matriz View Explícita:** Movimentação da câmera/observador no eixo X.
8. **Minimapa 2D Auxiliar:** Rendering em viewport secundário exibindo visualização do topo (X-Z) aplicando transformações 2D.
9. **Painel On-Screen:** Display dinâmico de status das transformações atuais.

##  Identificação dos Integrantes

- **Nome do Aluno / Grupo:** Guilherme Fortunato da Silva, Paloma de Castro Leite e Rayssa Mara Caldini Costa
- **Disciplina:** Computação Gráfica