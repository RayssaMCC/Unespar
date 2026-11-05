import ctypes
import sys

import glfw
import numpy as np
from OpenGL.GL import *


# ============================================================
# CONFIGURACAO
# ============================================================

WIDTH = 1100
HEIGHT = 800
LEVELS = 8
mode = 1

MODE_NAMES = {
    1: "Imagem RGB original",
    2: "Diagonal y = x",
    3: "Imagem em tons de cinza",
    4: "Histograma original",
    5: "Imagem equalizada",
    6: "Histograma equalizado",
    7: "Comparacao original x equalizada",
}

# Cada vertice possui: x, y, r, g, b
VERTEX_SHADER = """
#version 330 core
layout(location = 0) in vec2 aPos;
layout(location = 1) in vec3 aColor;
out vec3 vertexColor;
void main() {
    gl_Position = vec4(aPos, 0.0, 1.0);
    vertexColor = aColor;
}
"""

FRAGMENT_SHADER = """
#version 330 core
in vec3 vertexColor;
out vec4 FragColor;
void main() {
    FragColor = vec4(vertexColor, 1.0);
}
"""


# ============================================================
# PARTE 1 - IMAGEM RGB MANUAL 12 x 12
# ============================================================

def criar_imagem():
    """
    Usa como modelo o padrao RGB 6x6 do arquivo zoomRGB.py:
    cores primarias nas bordas e padrao geometrico no centro.
    Cada pixel e ampliado para um bloco 2x2, resultando em 12x12.
    Para esta atividade, os canais RGB sao comprimidos para uma
    faixa estreita, criando propositalmente baixo contraste.
    """
    modelo = np.array([
        [
            [1.0, 0.0, 0.0], [1.0, 0.5, 0.0], [1.0, 1.0, 0.0],
            [0.0, 1.0, 0.0], [0.0, 1.0, 1.0], [0.0, 0.0, 1.0],
        ],
        [
            [1.0, 0.5, 0.0], [1.0, 1.0, 1.0], [0.2, 0.2, 0.2],
            [0.2, 0.2, 0.2], [1.0, 1.0, 1.0], [0.0, 1.0, 1.0],
        ],
        [
            [1.0, 1.0, 0.0], [0.2, 0.2, 0.2], [1.0, 0.0, 1.0],
            [1.0, 0.0, 1.0], [0.2, 0.2, 0.2], [1.0, 1.0, 0.0],
        ],
        [
            [0.0, 1.0, 0.0], [0.2, 0.2, 0.2], [1.0, 0.0, 1.0],
            [1.0, 0.0, 1.0], [0.2, 0.2, 0.2], [0.0, 1.0, 0.0],
        ],
        [
            [0.0, 1.0, 1.0], [1.0, 1.0, 1.0], [0.2, 0.2, 0.2],
            [0.2, 0.2, 0.2], [1.0, 1.0, 1.0], [0.0, 1.0, 1.0],
        ],
        [
            [0.0, 0.0, 1.0], [0.0, 1.0, 1.0], [0.0, 1.0, 0.0],
            [1.0, 1.0, 0.0], [1.0, 0.5, 0.0], [1.0, 0.0, 0.0],
        ],
    ], dtype=np.float32)

    # Amplia o modelo 6x6 para 12x12, repetindo cada pixel em um bloco 2x2
    imagem_12x12 = np.repeat(np.repeat(modelo, 2, axis=0), 2, axis=1)

    # Reduz o contraste mantendo as diferencas de cor do padrao original
    imagem_baixo_contraste = 0.25 + 0.40 * imagem_12x12
    return imagem_baixo_contraste.astype(np.float32)


# PARTE 2 - DIAGONAL y = x
# ============================================================

def marcar_diagonal(image):
    resultado = image.copy()
    altura, largura, _ = resultado.shape

    for linha in range(altura):
        for coluna in range(largura):
            if linha == coluna:
                resultado[linha, coluna] = [1.0, 0.0, 0.0]  # vermelho

    return resultado


# ============================================================
# PARTE 3 - CONVERSAO RGB PARA INTENSIDADE
# ============================================================

def converter_para_cinza(image):
    r = image[:, :, 0]
    g = image[:, :, 1]
    b = image[:, :, 2]
    return 0.299 * r + 0.587 * g + 0.114 * b


def cinza_para_rgb(gray):
    return np.stack((gray, gray, gray), axis=2).astype(np.float32)


# ============================================================
# PARTE 4 - HISTOGRAMA E PROBABILIDADES
# ============================================================

def calcular_histograma(gray, levels=LEVELS):
    hist = np.zeros(levels, dtype=np.int64)
    valores = np.clip(gray, 0.0, 1.0)
    indices = np.floor(valores * levels).astype(int)
    indices = np.clip(indices, 0, levels - 1)

    for linha in range(gray.shape[0]):
        for coluna in range(gray.shape[1]):
            hist[indices[linha, coluna]] += 1

    return hist


def imprimir_tabela_histograma(hist, titulo):
    total = int(hist.sum())
    print(f"\n{titulo}")
    print("-" * 43)
    print(f"{'Nivel':<12}{'Pixels':<12}{'Probabilidade':<15}")
    for nivel, quantidade in enumerate(hist):
        probabilidade = quantidade / total if total else 0.0
        print(f"{nivel:<12}{int(quantidade):<12}{probabilidade:.4f}")
    print(f"Total de pixels: {total}")


# ============================================================
# PARTE 5 - DIAGNOSTICO AUTOMATICO
# ============================================================

def diagnosticar_histograma(hist):
    total = int(hist.sum())
    if total == 0:
        mensagem = "Histograma vazio; nao ha pixels para diagnosticar."
        print("\nDiagnostico: INDEFINIDO")
        print("Justificativa:", mensagem)
        return "INDEFINIDO", mensagem

    probabilidades = hist / total
    baixos = float(probabilidades[:2].sum())       # niveis 0 e 1
    intermediarios = float(probabilidades[2:6].sum())  # niveis 2 a 5
    altos = float(probabilidades[6:].sum())        # niveis 6 e 7

    niveis_ocupados = int(np.count_nonzero(hist))
    maior_concentracao = float(probabilidades.max())

    if baixos >= 0.60:
        diagnostico = "IMAGEM PREDOMINANTEMENTE ESCURA"
        justificativa = f"{baixos:.1%} dos pixels estao nos niveis baixos (0 e 1)."
    elif altos >= 0.60:
        diagnostico = "IMAGEM PREDOMINANTEMENTE CLARA"
        justificativa = f"{altos:.1%} dos pixels estao nos niveis altos (6 e 7)."
    elif niveis_ocupados <= 4 or maior_concentracao >= 0.45:
        diagnostico = "IMAGEM COM NIVEIS CONCENTRADOS"
        nivel = int(np.argmax(hist))
        justificativa = (
            f"{niveis_ocupados} de {len(hist)} niveis estao ocupados; "
            f"o nivel {nivel} concentra {maior_concentracao:.1%} dos pixels."
        )
    else:
        diagnostico = "IMAGEM SEM PREDOMINANCIA TONAL"
        justificativa = (
            f"Distribuicao: {baixos:.1%} em niveis baixos, "
            f"{intermediarios:.1%} em niveis intermediarios e "
            f"{altos:.1%} em niveis altos. A imagem nao e predominantemente "
            "escura nem clara; a classificacao indica avaliar a distribuicao tonal."
        )

    print(f"\nDiagnostico: {diagnostico}")
    print(f"Justificativa: {justificativa}")
    return diagnostico, justificativa


# ============================================================
# PARTE 6 - EQUALIZACAO
# ============================================================

def equalizar(gray, levels=LEVELS):
    hist = calcular_histograma(gray, levels)
    total = int(hist.sum())
    if total == 0:
        return gray.copy()

    probabilidade = hist.astype(np.float64) / total
    acumulada = np.cumsum(probabilidade)

    # Mapeia cada pixel para o nivel quantizado da distribuicao acumulada
    indices = np.floor(np.clip(gray, 0.0, 1.0) * levels).astype(int)
    indices = np.clip(indices, 0, levels - 1)
    mapeamento = np.floor(acumulada * (levels - 1)).astype(np.float32)

    resultado = mapeamento[indices] / (levels - 1)
    return resultado.astype(np.float32)


# ============================================================
# OPENGL - GEOMETRIA DAS IMAGENS E HISTOGRAMAS
# ============================================================

def adicionar_retangulo(vertices, x0, y0, x1, y1, cor):
    r, g, b = cor
    vertices.extend([
        x0, y0, r, g, b,
        x1, y0, r, g, b,
        x1, y1, r, g, b,
        x0, y0, r, g, b,
        x1, y1, r, g, b,
        x0, y1, r, g, b,
    ])


def vertices_imagem(image, centro_x, centro_y, largura_max, altura_max, gap=0.004):
    vertices = []
    altura, largura, _ = image.shape
    celula_x = (largura_max - gap * (largura - 1)) / largura
    celula_y = (altura_max - gap * (altura - 1)) / altura
    celula = min(celula_x, celula_y)

    largura_total = largura * celula + (largura - 1) * gap
    altura_total = altura * celula + (altura - 1) * gap
    inicio_x = centro_x - largura_total / 2
    inicio_y = centro_y + altura_total / 2

    for linha in range(altura):
        for coluna in range(largura):
            x0 = inicio_x + coluna * (celula + gap)
            y1 = inicio_y - linha * (celula + gap)
            adicionar_retangulo(
                vertices, x0, y1 - celula, x0 + celula, y1, image[linha, coluna]
            )

    return vertices


def vertices_histograma(hist, centro_x, centro_y, largura_max, altura_max, cor):
    vertices = []
    if hist.size == 0:
        return vertices

    maximo = max(int(hist.max()), 1)
    largura_barra = largura_max / len(hist)
    base_y = centro_y - altura_max / 2

    for nivel, quantidade in enumerate(hist):
        x0 = centro_x - largura_max / 2 + nivel * largura_barra
        x1 = x0 + largura_barra * 0.82
        y1 = base_y + (int(quantidade) / maximo) * altura_max
        adicionar_retangulo(vertices, x0, base_y, x1, y1, cor)

    return vertices


def criar_vertices_cena(original, diagonal, gray, equalizada, hist_original, hist_equalizado):
    if mode == 1:
        return vertices_imagem(original, 0, 0, 1.25, 1.25)
    if mode == 2:
        return vertices_imagem(diagonal, 0, 0, 1.25, 1.25)
    if mode == 3:
        return vertices_imagem(cinza_para_rgb(gray), 0, 0, 1.25, 1.25)
    if mode == 4:
        return vertices_histograma(hist_original, 0, 0, 1.5, 1.25, (0.95, 0.65, 0.20))
    if mode == 5:
        return vertices_imagem(cinza_para_rgb(equalizada), 0, 0, 1.25, 1.25)
    if mode == 6:
        return vertices_histograma(hist_equalizado, 0, 0, 1.5, 1.25, (0.25, 0.75, 0.95))

    # Modo 7: duas imagens em cima e dois histogramas embaixo.
    vertices = []
    vertices += vertices_imagem(cinza_para_rgb(gray), -0.52, 0.43, 0.68, 0.58)
    vertices += vertices_imagem(cinza_para_rgb(equalizada), 0.52, 0.43, 0.68, 0.58)
    vertices += vertices_histograma(hist_original, -0.52, -0.48, 0.68, 0.48, (0.95, 0.65, 0.20))
    vertices += vertices_histograma(hist_equalizado, 0.52, -0.48, 0.68, 0.48, (0.25, 0.75, 0.95))
    return vertices


def compilar_shader(fonte, tipo):
    shader = glCreateShader(tipo)
    glShaderSource(shader, fonte)
    glCompileShader(shader)
    if not glGetShaderiv(shader, GL_COMPILE_STATUS):
        erro = glGetShaderInfoLog(shader).decode("utf-8", errors="replace")
        glDeleteShader(shader)
        raise RuntimeError(f"Erro ao compilar shader:\n{erro}")
    return shader


def criar_programa_shader():
    vs = compilar_shader(VERTEX_SHADER, GL_VERTEX_SHADER)
    fs = compilar_shader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
    programa = glCreateProgram()
    glAttachShader(programa, vs)
    glAttachShader(programa, fs)
    glLinkProgram(programa)

    if not glGetProgramiv(programa, GL_LINK_STATUS):
        erro = glGetProgramInfoLog(programa).decode("utf-8", errors="replace")
        glDeleteShader(vs)
        glDeleteShader(fs)
        glDeleteProgram(programa)
        raise RuntimeError(f"Erro ao linkar shaders:\n{erro}")

    glDeleteShader(vs)
    glDeleteShader(fs)
    return programa


def criar_janela():
    if not glfw.init():
        raise RuntimeError("Nao foi possivel inicializar o GLFW.")

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    glfw.window_hint(glfw.RESIZABLE, glfw.FALSE)

    if sys.platform == "darwin":
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)

    janela = glfw.create_window(WIDTH, HEIGHT, "Diagnostico e Equalizacao de Histograma", None, None)
    if not janela:
        glfw.terminate()
        raise RuntimeError("Nao foi possivel criar a janela OpenGL.")

    glfw.make_context_current(janela)
    glfw.set_key_callback(janela, callback_teclado)
    return janela


def criar_geometria():
    vao = glGenVertexArrays(1)
    vbo = glGenBuffers(1)
    glBindVertexArray(vao)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, 0, None, GL_DYNAMIC_DRAW)

    tamanho_float = np.dtype(np.float32).itemsize
    stride = 5 * tamanho_float

    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(2 * tamanho_float))
    glEnableVertexAttribArray(1)

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)
    return vao, vbo


def atualizar_vbo(vbo, vertices):
    dados = np.asarray(vertices, dtype=np.float32)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, dados.nbytes, dados, GL_DYNAMIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, 0)


def callback_teclado(janela, tecla, scancode, acao, mods):
    global mode
    if acao != glfw.PRESS:
        return
    if tecla == glfw.KEY_ESCAPE:
        glfw.set_window_should_close(janela, True)
    elif tecla == glfw.KEY_H:
        imprimir_ajuda()
    elif glfw.KEY_1 <= tecla <= glfw.KEY_7:
        mode = tecla - glfw.KEY_0
        glfw.set_window_title(janela, f"Modo {mode}: {MODE_NAMES[mode]}")


def imprimir_ajuda():
    print("\nTeclas:")
    for tecla, nome in MODE_NAMES.items():
        print(f"{tecla} - {nome}")
    print("H - mostrar ajuda | ESC - sair\n")


# ============================================================
# PARTE 8 - ANALISE E EXECUCAO
# ============================================================

def imprimir_analise(gray, equalizada, hist_original, hist_equalizado):
    print("\nANALISE DOS RESULTADOS")
    print("=" * 60)
    print(f"Niveis ocupados no histograma original: {np.count_nonzero(hist_original)} de {LEVELS}")
    print(f"Niveis ocupados no histograma equalizado: {np.count_nonzero(hist_equalizado)} de {LEVELS}")
    print(f"Pixels antes/depois: {gray.size}/{equalizada.size}")
    print(f"Resolucao antes/depois: {gray.shape[1]}x{gray.shape[0]} / {equalizada.shape[1]}x{equalizada.shape[0]}")
    print(f"Faixa de intensidade original: {gray.min():.3f} a {gray.max():.3f}")
    print(f"Faixa de intensidade equalizada: {equalizada.min():.3f} a {equalizada.max():.3f}")
    print("A equalizacao altera os valores de intensidade, nao a quantidade de pixels nem a resolucao.")
    print("O histograma permite observar a distribuicao tonal antes de modificar a imagem.")


def main():
    global mode
    original = criar_imagem()
    diagonal = marcar_diagonal(original)
    gray = converter_para_cinza(original)
    equalizada = equalizar(gray, LEVELS)
    hist_original = calcular_histograma(gray, LEVELS)
    hist_equalizado = calcular_histograma(equalizada, LEVELS)

    imprimir_tabela_histograma(hist_original, "HISTOGRAMA ORIGINAL")
    diagnosticar_histograma(hist_original)
    imprimir_tabela_histograma(hist_equalizado, "HISTOGRAMA EQUALIZADO")
    imprimir_analise(gray, equalizada, hist_original, hist_equalizado)

    janela = criar_janela()
    programa = criar_programa_shader()
    vao, vbo = criar_geometria()
    glViewport(0, 0, WIDTH, HEIGHT)
    imprimir_ajuda()

    modo_anterior = None
    vertices = np.array([], dtype=np.float32)

    try:
        while not glfw.window_should_close(janela):
            glfw.poll_events()

            if mode != modo_anterior:
                vertices = np.asarray(
                    criar_vertices_cena(original, diagonal, gray, equalizada, hist_original, hist_equalizado),
                    dtype=np.float32,
                )
                atualizar_vbo(vbo, vertices)
                modo_anterior = mode

            glClearColor(0.08, 0.08, 0.10, 1.0)
            glClear(GL_COLOR_BUFFER_BIT)
            glUseProgram(programa)
            glBindVertexArray(vao)
            glDrawArrays(GL_TRIANGLES, 0, len(vertices) // 5)
            glBindVertexArray(0)
            glfw.swap_buffers(janela)

    finally:
        glDeleteVertexArrays(1, [vao])
        glDeleteBuffers(1, [vbo])
        glDeleteProgram(programa)
        glfw.destroy_window(janela)
        glfw.terminate()


if __name__ == "__main__":
    main()
