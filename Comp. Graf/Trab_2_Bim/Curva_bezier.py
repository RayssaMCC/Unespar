"""
Trabalho 2 Bimestre - Computacao Grafica
Curvas de Bezier, Shaders, Uniforms e Interacao com o Teclado

Requisitos implementados:
1. Curva de Bezier cubica (GL_LINE_STRIP), calculada manualmente
2. Poligono de controle (4 pontos + segmentos)
3. Cor da curva via uniform: R (vermelho) / G (verde) / B (azul) / W (branco)
4. Selecao de ponto (teclas 1,2,3,4) + movimentacao com as setas,
   com recalculo da curva e atualizacao do VBO
5. Resolucao da curva ajustavel com + / - (100 a 2000 amostras)
6. Mostrar/ocultar poligono de controle com a tecla P
7. Espessura da linha com ] (aumenta) e [ (diminui)
8. Ponto selecionado destacado (cor e tamanho diferentes)
"""

import glfw
from OpenGL.GL import *
import ctypes
import numpy as np
from OpenGL.GL import *
from OpenGL.error import GLError  # Adicione esta linha de importação

# ---------------------------------------------------------------------------
# Shaders
# ---------------------------------------------------------------------------
VERTEX_SHADER_SOURCE = """
#version 330 core
layout(location = 0) in vec3 aPos;
void main(){
    gl_Position = vec4(aPos, 1.0);
}
"""

FRAGMENT_SHADER_SOURCE = """
#version 330 core
uniform vec3 uColor; // Cor enviada pela CPU (Requisitos 3 e 8)
out vec4 FragColor;
void main(){
    FragColor = vec4(uColor, 1.0);
}
"""

# ---------------------------------------------------------------------------
# Estado global da aplicacao
# ---------------------------------------------------------------------------
pontos_controle = [
    [-0.7, -0.5],
    [-0.3,  0.7],
    [ 0.3,  0.7],
    [ 0.7, -0.5],
]

ponto_selecionado = 0            # indice do ponto de controle ativo (Requisito 4)
num_amostras = 200               # resolucao da curva (Requisito 5)
MIN_AMOSTRAS = 100
MAX_AMOSTRAS = 2000

cor_curva = [1.0, 1.0, 1.0]      # cor atual da curva (Requisito 3), branco por padrao
mostrar_poligono = True          # Requisito 6
espessura_linha = 2.0            # Requisito 7
MIN_ESPESSURA = 1.0
MAX_ESPESSURA = 10.0

VELOCIDADE_MOVIMENTO = 0.6       # unidades/segundo ao mover ponto com as setas
VELOCIDADE_RES = 400.0           # amostras/segundo ao segurar +/-
VELOCIDADE_ESPESSURA = 4.0       # espessura/segundo ao segurar ]/[

precisa_atualizar = True         # sinaliza que a geometria mudou e o VBO precisa ser atualizado


# ---------------------------------------------------------------------------
# Shaders: compilacao e link
# ---------------------------------------------------------------------------
def compile_shader(source, shader_type):
    shader = glCreateShader(shader_type)
    glShaderSource(shader, source)
    glCompileShader(shader)
    if not glGetShaderiv(shader, GL_COMPILE_STATUS):
        erro = glGetShaderInfoLog(shader).decode()
        raise RuntimeError(f"Erro ao compilar shader: {erro}")
    return shader


def create_shader_program():
    vertex_shader = compile_shader(VERTEX_SHADER_SOURCE, GL_VERTEX_SHADER)
    fragment_shader = compile_shader(FRAGMENT_SHADER_SOURCE, GL_FRAGMENT_SHADER)

    program = glCreateProgram()
    glAttachShader(program, vertex_shader)
    glAttachShader(program, fragment_shader)
    glLinkProgram(program)

    if not glGetProgramiv(program, GL_LINK_STATUS):
        erro = glGetProgramInfoLog(program).decode()
        raise RuntimeError(f"Erro ao linkar programa: {erro}")

    glDeleteShader(vertex_shader)
    glDeleteShader(fragment_shader)
    return program


# ---------------------------------------------------------------------------
# Curva de Bezier cubica (implementação manual)
# ---------------------------------------------------------------------------
# Calcula 'num_amostras' pontos da curva de Bezier cubica definida por pontos_controle
def gerar_curva_bezier():
    p0, p1, p2, p3 = pontos_controle
    pontos = []
    for i in range(num_amostras):
        t = i / (num_amostras - 1)
        u = 1.0 - t
        x = (u**3) * p0[0] + 3 * (u**2) * t * p1[0] + 3 * u * (t**2) * p2[0] + (t**3) * p3[0]
        y = (u**3) * p0[1] + 3 * (u**2) * t * p1[1] + 3 * u * (t**2) * p2[1] + (t**3) * p3[1]
        pontos.extend([x, y, 0.0])
    return pontos

# Recalcula a curva e reenvia todos os vertices (curva + poligono) para a GPU
def atualizar_vbo(VBO):
    curva = gerar_curva_bezier()
    poligono = [coord for p in pontos_controle for coord in (p[0], p[1], 0.0)]
    vertices = np.array(curva + poligono, dtype=np.float32)

    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_DYNAMIC_DRAW)


# ---------------------------------------------------------------------------
# Callback de teclado: eventos discretos (um unico disparo por tecla)
# ---------------------------------------------------------------------------
def callback_teclado(janela, tecla, scancode, acao, modificadores):
    global ponto_selecionado, cor_curva, mostrar_poligono

    if acao != glfw.PRESS:
        return

    # Requisito 3: cor da curva via uniform
    if tecla == glfw.KEY_R:
        cor_curva = [1.0, 0.0, 0.0]
    elif tecla == glfw.KEY_G:
        cor_curva = [0.0, 1.0, 0.0]
    elif tecla == glfw.KEY_B:
        cor_curva = [0.0, 0.0, 1.0]
    elif tecla == glfw.KEY_W:
        cor_curva = [1.0, 1.0, 1.0]

    # Requisito 4: selecao do ponto de controle
    elif tecla == glfw.KEY_1:
        ponto_selecionado = 0
    elif tecla == glfw.KEY_2:
        ponto_selecionado = 1
    elif tecla == glfw.KEY_3:
        ponto_selecionado = 2
    elif tecla == glfw.KEY_4:
        ponto_selecionado = 3

    # Requisito 6: mostrar/ocultar poligono de controle
    elif tecla == glfw.KEY_P:
        mostrar_poligono = not mostrar_poligono


# ---------------------------------------------------------------------------
# Entrada continua (teclas mantidas pressionadas): movimento, resolucao, espessura
# ---------------------------------------------------------------------------
def processar_entrada(janela, variacao_tempo):
    global pontos_controle, num_amostras, espessura_linha, precisa_atualizar

    # Requisito 4: mover o ponto selecionado com as setas
    passo = VELOCIDADE_MOVIMENTO * variacao_tempo
    moveu = False
    if glfw.get_key(janela, glfw.KEY_UP) == glfw.PRESS:
        pontos_controle[ponto_selecionado][1] += passo
        moveu = True
    if glfw.get_key(janela, glfw.KEY_DOWN) == glfw.PRESS:
        pontos_controle[ponto_selecionado][1] -= passo
        moveu = True
    if glfw.get_key(janela, glfw.KEY_LEFT) == glfw.PRESS:
        pontos_controle[ponto_selecionado][0] -= passo
        moveu = True
    if glfw.get_key(janela, glfw.KEY_RIGHT) == glfw.PRESS:
        pontos_controle[ponto_selecionado][0] += passo
        moveu = True
    if moveu:
        precisa_atualizar = True

    # Requisito 5: resolucao da curva (numero de amostras) com + / -
    if glfw.get_key(janela, glfw.KEY_EQUAL) == glfw.PRESS or glfw.get_key(janela, glfw.KEY_KP_ADD) == glfw.PRESS:
        novo = min(MAX_AMOSTRAS, int(num_amostras + VELOCIDADE_RES * variacao_tempo) + 1)
        if novo != num_amostras:
            num_amostras = novo
            precisa_atualizar = True
            print(f"Resolucao: {num_amostras} pontos")
            
    if glfw.get_key(janela, glfw.KEY_MINUS) == glfw.PRESS or glfw.get_key(janela, glfw.KEY_KP_SUBTRACT) == glfw.PRESS:
        novo = max(MIN_AMOSTRAS, int(num_amostras - VELOCIDADE_RES * variacao_tempo) - 1)
        if novo != num_amostras:
            num_amostras = novo
            precisa_atualizar = True
            print(f"Resolucao: {num_amostras} pontos")

    # Requisito 7: espessura da linha com ] e [
    
    # A tecla ']' do teclado físico ABNT2 é lida pelo GLFW como KEY_BACKSLASH
    if glfw.get_key(janela, glfw.KEY_BACKSLASH) == glfw.PRESS:
        espessura_linha = min(MAX_ESPESSURA, espessura_linha + VELOCIDADE_ESPESSURA * variacao_tempo)
        print(f"Espessura interna: {espessura_linha:.2f}")
        
    # A tecla '[' do teclado físico ABNT2 é lida pelo GLFW como KEY_RIGHT_BRACKET
    if glfw.get_key(janela, glfw.KEY_RIGHT_BRACKET) == glfw.PRESS:
        espessura_linha = max(MIN_ESPESSURA, espessura_linha - VELOCIDADE_ESPESSURA * variacao_tempo)
        print(f"Espessura interna: {espessura_linha:.2f}")


# ---------------------------------------------------------------------------
# Inicializacao: VAO, VBO, shader program
# ---------------------------------------------------------------------------
def inicializar(janela):
    VAO = glGenVertexArrays(1)
    VBO = glGenBuffers(1)

    glBindVertexArray(VAO)
    atualizar_vbo(VBO)  # carrega os dados iniciais (curva + poligono)

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * 4, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)

    program_shader = create_shader_program()
    # Requisito 3: localizacao do uniform de cor (obtida uma unica vez)
    loc_uColor = glGetUniformLocation(program_shader, "uColor")

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    glfw.set_key_callback(janela, callback_teclado)

    return program_shader, VAO, VBO, loc_uColor


# ---------------------------------------------------------------------------
# Desenho
# ---------------------------------------------------------------------------
def desenhar_curva(loc_uColor):
    # Requisitos 1, 3 e 7: curva com cor e espessura configuráveis
    glUniform3f(loc_uColor, *cor_curva)
    
    # Tenta aplicar a espessura. Se a GPU não aceitar, ela apenas ignora e desenha com a espessura padrão (1.0) sem fechar o programa
    try:
        glLineWidth(espessura_linha)
    except GLError:
        glLineWidth(1.0)
        
    glDrawArrays(GL_LINE_STRIP, 0, num_amostras)


def desenhar_poligono(loc_uColor):
    # Requisitos 2 e 6: segmentos do poligono de controle (cinza), ocultavel
    if not mostrar_poligono:
        return
    glUniform3f(loc_uColor, 0.5, 0.5, 0.5)
    glLineWidth(1.0)
    glDrawArrays(GL_LINE_STRIP, num_amostras, 4)


def desenhar_pontos(loc_uColor):
    # Se o polígono estiver oculto, não desenha nenhum ponto (nem os normais, nem o selecionado)
    if not mostrar_poligono:
        return

    # Requisito 2: os 4 pontos de controle
    glPointSize(7.0)
    glUniform3f(loc_uColor, 0.8, 0.8, 0.8)
    glDrawArrays(GL_POINTS, num_amostras, 4)

    # Requisito 8: ponto selecionado destacado (amarelo, maior)
    glPointSize(14.0)
    glUniform3f(loc_uColor, 1.0, 1.0, 0.0)
    glDrawArrays(GL_POINTS, num_amostras + ponto_selecionado, 1)


def renderizar(program_shader, VAO, VBO, loc_uColor):
    global precisa_atualizar

    if precisa_atualizar:
        atualizar_vbo(VBO)
        precisa_atualizar = False

    glClearColor(0.08, 0.08, 0.1, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    glUseProgram(program_shader)
    glBindVertexArray(VAO)

    desenhar_curva(loc_uColor)
    desenhar_poligono(loc_uColor)
    desenhar_pontos(loc_uColor)

    glBindVertexArray(0)


# ---------------------------------------------------------------------------
# Loop principal
# ---------------------------------------------------------------------------
def main():
    if not glfw.init():
        raise Exception("Falha ao inicializar GLFW")

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)

    janela = glfw.create_window(900, 700, "Trabalho - Curvas de Bezier", None, None)
    if not janela:
        glfw.terminate()
        raise Exception("Falha ao criar a janela GLFW")

    glfw.make_context_current(janela)

    program_shader, VAO, VBO, loc_uColor = inicializar(janela)

    print("Controles:")
    print("  R / G / B / W  -> cor da curva")
    print("  1 2 3 4        -> selecionar ponto de controle")
    print("  Setas          -> mover o ponto selecionado")
    print("  + / -          -> aumentar/diminuir resolucao da curva")
    print("  P              -> mostrar/ocultar poligono de controle")
    print("  ] / [          -> aumentar/diminuir espessura da linha")

    ultimo_tempo = glfw.get_time()

    while not glfw.window_should_close(janela):
        tempo_atual = glfw.get_time()
        variacao_tempo = tempo_atual - ultimo_tempo
        ultimo_tempo = tempo_atual

        glfw.poll_events()
        processar_entrada(janela, variacao_tempo)
        renderizar(program_shader, VAO, VBO, loc_uColor)
        glfw.swap_buffers(janela)

    glfw.terminate()


if __name__ == "__main__":
    main()