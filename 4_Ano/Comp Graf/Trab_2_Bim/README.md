# Trabalho 2 Bimestre - Computação Gráfica: Curvas de Bézier

Este projeto contém a implementação de uma aplicação interativa desenvolvida em Python e OpenGL que renderiza e permite a manipulação em tempo real de uma Curva de Bézier Cúbica.

O código foi desenvolvido de forma nativa, calculando a geometria da curva matematicamente sem o uso de bibliotecas prontas para curvas, e utilizando a GPU (VAO, VBO, Shaders e Uniforms) para a renderização gráfica.

## 📋 Pré-requisitos

Para executar este projeto, você precisará ter o Python 3.x instalado em sua máquina. Além disso, é necessário instalar as seguintes bibliotecas:

- **GLFW**: criação da janela e gerenciamento de eventos (teclado e mouse).
- **PyOpenGL**: interface com a API gráfica OpenGL.
- **NumPy**: processamento e manipulação eficiente dos arrays de vértices.

## ⚙️ Instruções de Instalação

1. Abra o terminal (ou prompt de comando).
2. Certifique-se de que o `pip` está atualizado:

```bash
python -m pip install --upgrade pip
```

3. Instale todas as dependências:

```bash
pip install glfw PyOpenGL numpy
```

## 🚀 Como Executar

1. Salve o código-fonte em um arquivo chamado `Trab_curva_bezier.py`.
2. Pelo terminal, navegue até o diretório onde o arquivo foi salvo.
3. Execute o script:

```bash
python Trab_curva_bezier.py
```

> **Nota:** Dependendo da configuração do sistema operacional, o comando pode ser `python3`.

## 🎮 Controles da Aplicação

Após abrir a janela gráfica, utilize o teclado para interagir com a curva em tempo real. As alterações de geometria, resolução e espessura são exibidas diretamente no terminal de execução.

### Alteração Visual

- **R / G / B / W**: altera a cor da curva para Vermelho, Verde, Azul ou Branco.
- **P**: oculta ou exibe o polígono de controle e os pontos.
- **] / [**: aumenta ou diminui a espessura da linha da curva.

### Manipulação da Curva

- **1, 2, 3 ou 4**: seleciona qual ponto de controle (`P0`, `P1`, `P2` ou `P3`) será ativado. O ponto selecionado ficará destacado em amarelo e com tamanho maior.
- **Setas direcionais**: movem o ponto de controle atualmente selecionado (cima, baixo, esquerda e direita).
- **+ / -**: aumenta ou diminui a resolução (quantidade de pontos calculados) da curva de Bézier, com mínimo de **100** e máximo de **2000** pontos.
