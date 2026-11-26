
"""
Atividade Pratica - Recuperacao e Esqueletizacao de Imagens Binarias
Disciplina: Computacao Grafica

Baseado no exemplo esqueletizacao_completo.py.

Requisitos:
    python -m pip install numpy glfw PyOpenGL

Controles:
    0 - Comparacao: original / recuperada / esqueleto
    1 - Imagem original
    2 - Elemento estruturante
    3 - Erosao
    4 - Dilatacao
    5 - Abertura
    6 - Fechamento
    7 - Erosoes sucessivas ([ e ])
    8 - Camada do esqueleto ([ e ])
    9 - Esqueleto final

    ESPACO - Alternar cruz/quadrado
    R - Alternar sequencia de recuperacao A/B
    [ e ] - Mudar etapa
    H - Ajuda
    ESC - Sair
"""

import ctypes
import sys
import numpy as np
import glfw

from OpenGL.GL import *


# ================================================================
# 1. CONFIGURACOES
# ================================================================

LARGURA = 1200
ALTURA = 760

MODO = 0
KERNEL = 'cruz'
SEQUENCIA = 'A'
ETAPA = 0
SUJO = True


MODOS = {
    0: 'Comparacao: original / recuperada / esqueleto',
    1: 'Imagem binaria original',
    2: 'Elemento estruturante',
    3: 'Erosao',
    4: 'Dilatacao',
    5: 'Abertura',
    6: 'Fechamento',
    7: 'Erosoes sucessivas',
    8: 'Camada do esqueleto',
    9: 'Esqueleto morfologico final'
}


# ================================================================
# 2. SHADERS OPENGL
# ================================================================

VERTEX_SHADER = """
#version 330 core

layout (location = 0) in vec2 aPosition;
layout (location = 1) in vec3 aColor;

out vec3 vColor;

void main() {
    gl_Position = vec4(aPosition, 0.0, 1.0);
    vColor = aColor;
}
"""


FRAGMENT_SHADER = """
#version 330 core

in vec3 vColor;
out vec4 FragColor;

void main() {
    FragColor = vec4(vColor, 1.0);
}
"""


# ================================================================
# 3. CONSTRUCAO DA IMAGEM BINARIA
# ================================================================

def imagem_binaria():
    """
    Cria manualmente uma letra P utilizando NumPy.

    0 = fundo
    1 = objeto

    Imperfeicoes inseridas:

    - Tres pixels isolados de ruido.
    - Interrupcao de um pixel em um traco horizontal.
    - Pequeno buraco em uma regiao do objeto.
    """

    h, w = 35, 35

    imagem = np.zeros((h, w), dtype=bool)

    # Haste vertical da letra P
    imagem[5:30, 6:10] = True

    # Barra horizontal superior
    imagem[5:9, 6:25] = True

    # Barra horizontal central
    imagem[15:19, 6:25] = True

    # Haste vertical direita
    imagem[5:19, 21:25] = True

    # ------------------------------------------------------------
    # IMPERFEICAO 1: interrupcao de um pixel no traco horizontal
    # Remove uma coluna de pixels, formando uma pequena abertura.
    # ------------------------------------------------------------

    imagem[5:9, 15] = False

    # ------------------------------------------------------------
    # IMPERFEICAO 2: pequeno buraco na regiao interna do objeto
    # ------------------------------------------------------------

    imagem[16, 22] = False

    # ------------------------------------------------------------
    # IMPERFEICAO 3: tres pixels isolados de ruido
    # ------------------------------------------------------------

    imagem[2, 3] = True
    imagem[3, 29] = True
    imagem[32, 17] = True

    return imagem


# ================================================================
# 4. ELEMENTOS ESTRUTURANTES
# ================================================================

def elemento_estruturante(nome='cruz'):

    if nome == 'cruz':

        return np.array([
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0]
        ], dtype=bool)

    if nome == 'quadrado':

        return np.ones((3, 3), dtype=bool)

    raise ValueError('Kernel desconhecido')


# ================================================================
# 5. VALIDACAO DAS MATRIZES
# ================================================================

def _verificar(imagem, se):

    if imagem.ndim != 2 or se.ndim != 2:
        raise ValueError(
            'Imagem e elemento estruturante devem ser matrizes 2D'
        )

    if min(se.shape) < 1 or any(t % 2 == 0 for t in se.shape):
        raise ValueError(
            'Elemento estruturante deve possuir dimensoes impares'
        )

    if not np.any(se):
        raise ValueError(
            'Elemento estruturante nao pode ser vazio'
        )

    return (
        np.asarray(imagem, dtype=bool),
        np.asarray(se, dtype=bool)
    )


# ================================================================
# 6. OPERACOES MORFOLOGICAS
# ================================================================

def erosao(imagem, se):
    """
    Erosao binaria.

    Um pixel permanece ativo quando todos os pontos ativos
    do elemento estruturante encontram pixels ativos na imagem.
    """

    imagem, se = _verificar(imagem, se)

    h, w = imagem.shape
    kh, kw = se.shape

    ph, pw = kh // 2, kw // 2

    padded = np.pad(
        imagem,
        ((ph, ph), (pw, pw)),
        constant_values=False
    )

    resultado = np.zeros_like(imagem)

    for row in range(h):

        for col in range(w):

            vizinhanca = padded[
                row:row + kh,
                col:col + kw
            ]

            resultado[row, col] = np.all(
                vizinhanca[se]
            )

    return resultado


def dilatacao(imagem, se):
    """
    Dilatacao binaria.

    Um pixel fica ativo quando pelo menos um dos pontos
    ativos do elemento estruturante encontra o objeto.
    """

    imagem, se = _verificar(imagem, se)

    h, w = imagem.shape
    kh, kw = se.shape

    ph, pw = kh // 2, kw // 2

    padded = np.pad(
        imagem,
        ((ph, ph), (pw, pw)),
        constant_values=False
    )

    resultado = np.zeros_like(imagem)

    for row in range(h):

        for col in range(w):

            vizinhanca = padded[
                row:row + kh,
                col:col + kw
            ]

            resultado[row, col] = np.any(
                vizinhanca[se]
            )

    return resultado


def abertura(imagem, se):
    """
    Abertura = erosao seguida de dilatacao.
    """

    return dilatacao(
        erosao(imagem, se),
        se
    )


def fechamento(imagem, se):
    """
    Fechamento = dilatacao seguida de erosao.
    """

    return erosao(
        dilatacao(imagem, se),
        se
    )


# ================================================================
# 7. PROCESSO DE RECUPERACAO
# ================================================================

def recuperar_imagem(imagem, se, sequencia='A'):
    """
    Realiza a recuperacao da imagem utilizando duas sequencias.

    Sequencia A:
        Imagem -> Abertura -> Fechamento

    Sequencia B:
        Imagem -> Fechamento -> Abertura
    """

    if sequencia == 'A':

        resultado = abertura(imagem, se)

        resultado = fechamento(
            resultado,
            se
        )

    elif sequencia == 'B':

        resultado = fechamento(imagem, se)

        resultado = abertura(
            resultado,
            se
        )

    else:

        raise ValueError('Sequencia desconhecida')

    return resultado


# ================================================================
# 8. ESQUELETIZACAO - METODO DE LANTUEJOUL
# ================================================================

def construir_camadas_esqueleto(imagem, se):
    """
    Esqueleto morfologico por erosoes e aberturas.

    A_k = erosao repetida k vezes.

    S_k = A_k - abertura(A_k).

    Esqueleto = uniao de todas as camadas S_k.

    IMPORTANTE:
    A imagem utilizada como entrada e a imagem recuperada.
    """

    current = np.asarray(
        imagem,
        dtype=bool
    ).copy()

    etapas = [current.copy()]

    camadas = []

    limite_seguro = current.size + 1

    for _ in range(limite_seguro):

        if not np.any(current):

            return etapas, camadas

        # Abertura da imagem erodida
        opened = abertura(current, se)

        # Diferenca entre imagem erodida e sua abertura
        camada = np.logical_and(
            current,
            np.logical_not(opened)
        )

        camadas.append(camada)

        # Proxima erosao
        prox = erosao(current, se)

        if np.array_equal(prox, current):

            raise RuntimeError(
                'Erosao nao progrediu: confira o kernel'
            )

        current = prox

        etapas.append(current.copy())

    raise RuntimeError(
        'Limite de iteracoes atingido'
    )


def obter_esqueleto(camadas):

    if not camadas:
        return np.zeros((35, 35), dtype=bool)

    resultado = np.zeros_like(
        camadas[0],
        dtype=bool
    )

    for camada in camadas:

        resultado = np.logical_or(
            resultado,
            camada
        )

    return resultado


# ================================================================
# 9. COMPARACAO DOS RESULTADOS NO TERMINAL
# ================================================================

def imprimir_comparacoes():

    original = imagem_binaria()

    print('\n' + '=' * 65)
    print('COMPARACAO DAS OPERACOES MORFOLOGICAS')
    print('=' * 65)

    print('\nPixels ativos na imagem original:',
          np.sum(original))

    for nome in ['cruz', 'quadrado']:

        se = elemento_estruturante(nome)

        print('\nElemento estruturante:', nome.upper())

        resultados = {
            'Erosao': erosao(original, se),
            'Dilatacao': dilatacao(original, se),
            'Abertura': abertura(original, se),
            'Fechamento': fechamento(original, se)
        }

        for operacao, resultado in resultados.items():

            print(
                f'{operacao:15} : '
                f'{np.sum(resultado)} pixels'
            )

        seq_a = recuperar_imagem(
            original, se, 'A'
        )

        seq_b = recuperar_imagem(
            original, se, 'B'
        )

        print('\nSequencia A (Abertura + Fechamento):',
              np.sum(seq_a), 'pixels')

        print('Sequencia B (Fechamento + Abertura):',
              np.sum(seq_b), 'pixels')

        print('Pixels diferentes entre A e B:',
              np.sum(seq_a != seq_b))

    print('\n' + '=' * 65)


# ================================================================
# 10. INFRAESTRUTURA DE VISUALIZACAO OPENGL
# ================================================================

def _retangulo(destino, x0, y0, x1, y1, cor):

    r, g, b = cor

    destino.extend((
        x0, y0, r, g, b,
        x1, y0, r, g, b,
        x1, y1, r, g, b,

        x0, y0, r, g, b,
        x1, y1, r, g, b,
        x0, y1, r, g, b
    ))


def painel_matriz(
    imagem,
    cx,
    cy,
    maxw,
    maxh,
    cor=(0.20, 0.82, 0.78)
):
    """
    Representa cada pixel como um quadrado em OpenGL.
    """

    imagem = np.asarray(
        imagem,
        dtype=bool
    )

    h, w = imagem.shape

    if h == 0 or w == 0:

        return np.empty(
            (0,),
            dtype=np.float32
        )

    gap = 0.0024 if min(h, w) > 10 else 0.011

    tamanho = min(
        (maxw - (w - 1) * gap) / w,
        (maxh - (h - 1) * gap) / h
    )

    tamanho = max(0.001, tamanho)

    totalw = w * tamanho + (w - 1) * gap
    totalh = h * tamanho + (h - 1) * gap

    esquerda = cx - totalw / 2
    topo = cy + totalh / 2

    bg = (0.11, 0.16, 0.21)

    vert = []

    for row in range(h):

        for col in range(w):

            x0 = esquerda + col * (tamanho + gap)

            y1 = topo - row * (tamanho + gap)

            cor_pixel = cor if imagem[row, col] else bg

            _retangulo(
                vert,
                x0,
                y1 - tamanho,
                x0 + tamanho,
                y1,
                cor_pixel
            )

    return np.asarray(
        vert,
        dtype=np.float32
    )


def unir(*partes):

    return np.concatenate(
        [p for p in partes if p.size],
        axis=0
    ) if any(p.size for p in partes) else np.empty(
        (0,),
        dtype=np.float32
    )


# ================================================================
# 11. CONSTRUCAO DAS CENAS
# ================================================================

def construir_cena():

    original = imagem_binaria()

    se = elemento_estruturante(KERNEL)

    # Recuperacao conforme a sequencia selecionada
    tratada = recuperar_imagem(
        original,
        se,
        SEQUENCIA
    )

    esqueleto_cor = (1.0, 0.73, 0.20)

    # ------------------------------------------------------------
    # MODO 0: COMPARACAO DOS TRES RESULTADOS
    # ------------------------------------------------------------

    if MODO == 0:

        etapas, camadas = construir_camadas_esqueleto(
            tratada,
            se
        )

        esqueleto = obter_esqueleto(camadas)

        return unir(

            # Imagem original
            painel_matriz(
                original,
                -0.66, 0,
                0.53, 1.45
            ),

            # Imagem recuperada
            painel_matriz(
                tratada,
                0, 0,
                0.53, 1.45
            ),

            # Esqueleto final
            painel_matriz(
                esqueleto,
                0.66, 0,
                0.53, 1.45,
                cor=esqueleto_cor
            )
        )

    # ------------------------------------------------------------
    # MODO 1: IMAGEM ORIGINAL
    # ------------------------------------------------------------

    if MODO == 1:

        return painel_matriz(
            original,
            0, 0,
            1.75, 1.68
        )

    # ------------------------------------------------------------
    # MODO 2: ELEMENTO ESTRUTURANTE
    # ------------------------------------------------------------

    if MODO == 2:

        elemento_ampliado = np.pad(
            se,
            2,
            constant_values=False
        )

        return unir(

            painel_matriz(
                original,
                -0.52, 0,
                0.94, 1.55
            ),

            painel_matriz(
                elemento_ampliado,
                0.60, 0,
                0.78, 0.78,
                cor=esqueleto_cor
            )
        )

    # ------------------------------------------------------------
    # MODO 3: EROSAO
    # ------------------------------------------------------------

    if MODO == 3:

        imagem = erosao(original, se)

    # ------------------------------------------------------------
    # MODO 4: DILATACAO
    # ------------------------------------------------------------

    elif MODO == 4:

        imagem = dilatacao(original, se)

    # ------------------------------------------------------------
    # MODO 5: ABERTURA
    # ------------------------------------------------------------

    elif MODO == 5:

        imagem = abertura(original, se)

    # ------------------------------------------------------------
    # MODO 6: FECHAMENTO
    # ------------------------------------------------------------

    elif MODO == 6:

        imagem = fechamento(original, se)

    # ------------------------------------------------------------
    # MODOS 7, 8 E 9: ESQUELETIZACAO DA IMAGEM RECUPERADA
    # ------------------------------------------------------------

    elif MODO in (7, 8, 9):

        etapas, camadas = construir_camadas_esqueleto(
            tratada,
            se
        )

        if MODO == 7:

            index = min(
                ETAPA,
                len(etapas) - 1
            )

            imagem = etapas[index]

        elif MODO == 8:

            index = min(
                ETAPA,
                len(camadas) - 1
            )

            imagem = (
                camadas[index]
                if camadas
                else np.zeros_like(original)
            )

        else:

            imagem = obter_esqueleto(camadas)

    else:

        imagem = original

    return painel_matriz(
        imagem,
        0, 0,
        1.75, 1.68,
        cor=esqueleto_cor if MODO in (8, 9)
        else (0.20, 0.82, 0.78)
    )


# ================================================================
# 12. COMPILACAO DOS SHADERS
# ================================================================

def compilar_shader(codigo, tipo):

    shader = glCreateShader(tipo)

    glShaderSource(
        shader,
        codigo
    )

    glCompileShader(shader)

    if not glGetShaderiv(shader, GL_COMPILE_STATUS):

        erro = glGetShaderInfoLog(shader)

        glDeleteShader(shader)

        raise RuntimeError(
            f'Erro no shader: {erro}'
        )

    return shader


def programa_shaders():

    vs = compilar_shader(
        VERTEX_SHADER,
        GL_VERTEX_SHADER
    )

    fs = compilar_shader(
        FRAGMENT_SHADER,
        GL_FRAGMENT_SHADER
    )

    prog = glCreateProgram()

    glAttachShader(prog, vs)
    glAttachShader(prog, fs)

    glLinkProgram(prog)

    if not glGetProgramiv(prog, GL_LINK_STATUS):

        erro = glGetProgramInfoLog(prog)

        glDeleteProgram(prog)

        raise RuntimeError(
            f'Erro no programa: {erro}'
        )

    glDeleteShader(vs)
    glDeleteShader(fs)

    return prog


# ================================================================
# 13. CRIACAO DA GEOMETRIA
# ================================================================

def criar_geometria():

    vao = glGenVertexArrays(1)

    vbo = glGenBuffers(1)

    glBindVertexArray(vao)

    glBindBuffer(
        GL_ARRAY_BUFFER,
        vbo
    )

    glBufferData(
        GL_ARRAY_BUFFER,
        0,
        None,
        GL_DYNAMIC_DRAW
    )

    passo = 5 * np.dtype(np.float32).itemsize

    glVertexAttribPointer(
        0,
        2,
        GL_FLOAT,
        GL_FALSE,
        passo,
        ctypes.c_void_p(0)
    )

    glEnableVertexAttribArray(0)

    glVertexAttribPointer(
        1,
        3,
        GL_FLOAT,
        GL_FALSE,
        passo,
        ctypes.c_void_p(8)
    )

    glEnableVertexAttribArray(1)

    glBindVertexArray(0)

    glBindBuffer(
        GL_ARRAY_BUFFER,
        0
    )

    return vao, vbo


# ================================================================
# 14. AJUDA E CONTROLES
# ================================================================

def ajuda():

    print('\n' + '=' * 60)
    print('RECUPERACAO E ESQUELETIZACAO')
    print('=' * 60)

    for k in range(10):

        print(f'{k}: {MODOS[k]}')

    print('\nCONTROLES:')

    print('ESPACO: alternar SE cruz/quadrado')

    print('R: alternar sequencia de recuperacao A/B')

    print('[ e ]: escolher etapa de erosao/camada')

    print('H: ajuda')

    print('ESC: sair')

    print('\nSEQUENCIAS DE RECUPERACAO:')

    print('A: Abertura -> Fechamento')

    print('B: Fechamento -> Abertura')

    print('=' * 60)


def titulo(janela):

    adicional = (
        f' | SE={KERNEL}'
        f' | Sequencia={SEQUENCIA}'
    )

    if MODO in (7, 8):

        adicional += f' | etapa={ETAPA}'

    glfw.set_window_title(
        janela,
        f'Morfologia e Esqueletizacao | '
        f'{MODO}: {MODOS[MODO]}' + adicional
    )


# ================================================================
# 15. TECLADO
# ================================================================

def teclado(janela, tecla, scan, acao, modificadores):

    global MODO
    global KERNEL
    global SEQUENCIA
    global ETAPA
    global SUJO

    if acao not in (glfw.PRESS, glfw.REPEAT):

        return

    if tecla == glfw.KEY_ESCAPE:

        glfw.set_window_should_close(
            janela,
            True
        )

        return

    if acao == glfw.PRESS:

        mapa = {

            glfw.KEY_0: 0,
            glfw.KEY_1: 1,
            glfw.KEY_2: 2,
            glfw.KEY_3: 3,
            glfw.KEY_4: 4,
            glfw.KEY_5: 5,
            glfw.KEY_6: 6,
            glfw.KEY_7: 7,
            glfw.KEY_8: 8,
            glfw.KEY_9: 9,

            glfw.KEY_KP_0: 0,
            glfw.KEY_KP_1: 1,
            glfw.KEY_KP_2: 2,
            glfw.KEY_KP_3: 3,
            glfw.KEY_KP_4: 4,
            glfw.KEY_KP_5: 5,
            glfw.KEY_KP_6: 6,
            glfw.KEY_KP_7: 7,
            glfw.KEY_KP_8: 8,
            glfw.KEY_KP_9: 9
        }

        # Alteracao do modo de visualizacao
        if tecla in mapa:

            MODO = mapa[tecla]

            if MODO == 8:
                ETAPA = 1
            else:
                ETAPA = 0

            SUJO = True

        # Alternar elemento estruturante
        elif tecla == glfw.KEY_SPACE:

            KERNEL = (
                'quadrado'
                if KERNEL == 'cruz'
                else 'cruz'
            )

            ETAPA = 0

            SUJO = True

            print(
                '\nElemento estruturante:',
                KERNEL.upper()
            )

        # Alternar sequencia de recuperacao
        elif tecla == glfw.KEY_R:

            SEQUENCIA = (
                'B'
                if SEQUENCIA == 'A'
                else 'A'
            )

            ETAPA = 0

            SUJO = True

            print(
                '\nSequencia de recuperacao:',
                SEQUENCIA
            )

            if SEQUENCIA == 'A':

                print('Abertura -> Fechamento')

            else:

                print('Fechamento -> Abertura')

        # Exibir ajuda
        elif tecla == glfw.KEY_H:

            ajuda()

    # Diminuir etapa
    if tecla in (
        glfw.KEY_LEFT_BRACKET,
        glfw.KEY_KP_SUBTRACT
    ):

        ETAPA = max(
            0,
            ETAPA - 1
        )

        SUJO = True

    # Aumentar etapa
    elif tecla in (
        glfw.KEY_RIGHT_BRACKET,
        glfw.KEY_KP_ADD
    ):

        ETAPA += 1

        SUJO = True

    if SUJO:

        titulo(janela)

        print(
            f'Modo {MODO}: {MODOS[MODO]}'
            f' | SE {KERNEL}'
            f' | Sequencia {SEQUENCIA}'
            f' | Etapa {ETAPA}'
        )


# ================================================================
# 16. EXECUCAO OPENGL
# ================================================================

def executar():

    global SUJO

    if not glfw.init():

        raise RuntimeError(
            'GLFW nao inicializou. Verifique os drivers graficos.'
        )

    try:

        # Configuracao OpenGL 3.3
        glfw.window_hint(
            glfw.CONTEXT_VERSION_MAJOR,
            3
        )

        glfw.window_hint(
            glfw.CONTEXT_VERSION_MINOR,
            3
        )

        glfw.window_hint(
            glfw.OPENGL_PROFILE,
            glfw.OPENGL_CORE_PROFILE
        )

        if sys.platform == 'darwin':

            glfw.window_hint(
                glfw.OPENGL_FORWARD_COMPAT,
                glfw.TRUE
            )

        janela = glfw.create_window(
            LARGURA,
            ALTURA,
            'Recuperacao e Esqueletizacao',
            None,
            None
        )

        if not janela:

            raise RuntimeError(
                'Janela OpenGL 3.3 nao criada.'
            )

        glfw.make_context_current(janela)

        glfw.swap_interval(1)

        glfw.set_key_callback(
            janela,
            teclado
        )

        titulo(janela)

        prog = programa_shaders()

        vao, vbo = criar_geometria()

        ajuda()

        # Mostrar comparacoes no terminal
        imprimir_comparacoes()

        vertices = np.empty(
            (0,),
            dtype=np.float32
        )

        while not glfw.window_should_close(janela):

            glfw.poll_events()

            # Atualizar geometria quando necessario
            if SUJO:

                vertices = construir_cena()

                glBindBuffer(
                    GL_ARRAY_BUFFER,
                    vbo
                )

                glBufferData(
                    GL_ARRAY_BUFFER,
                    vertices.nbytes,
                    vertices,
                    GL_DYNAMIC_DRAW
                )

                glBindBuffer(
                    GL_ARRAY_BUFFER,
                    0
                )

                SUJO = False

            glViewport(
                0,
                0,
                LARGURA,
                ALTURA
            )

            glClearColor(
                0.045,
                0.065,
                0.09,
                1.0
            )

            glClear(
                GL_COLOR_BUFFER_BIT
            )

            glUseProgram(prog)

            glBindVertexArray(vao)

            glDrawArrays(
                GL_TRIANGLES,
                0,
                vertices.size // 5
            )

            glBindVertexArray(0)

            glfw.swap_buffers(janela)

        # Liberacao dos recursos
        glDeleteBuffers(
            1,
            [vbo]
        )

        glDeleteVertexArrays(
            1,
            [vao]
        )

        glDeleteProgram(prog)

        glfw.destroy_window(janela)

    finally:

        glfw.terminate()


# ================================================================
# 17. INICIO DO PROGRAMA
# ================================================================

if __name__ == '__main__':

    executar()
