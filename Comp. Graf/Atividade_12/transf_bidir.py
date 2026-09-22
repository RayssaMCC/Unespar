import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import sys

# Variáveis globais para controlar as transformações
tx, ty = 0.0, 0.0  # Translação
angle = 0.0        # Rotação em graus
scale = 1.0        # Escala

# SHADERS
VERTEX_SHADER = """
#version 330 core
layout (location = 0) in vec2 position;

// Uniform que receberá a matriz final de transformações da CPU
uniform mat4 transform;

void main() {
    // Multiplica o vértice pela matriz para aplicar as transformações
    gl_Position = transform * vec4(position, 0.0, 1.0);
}
"""

FRAGMENT_SHADER = """
#version 330 core
out vec4 FragColor;

// Uniform para receber a cor da CPU e aplicar em partes diferentes do foguete
uniform vec4 u_color; 

void main() {
    FragColor = u_color;
}
"""

# ===================================================================
# 1. FUNÇÕES DE CÁLCULO DE TRANSFORMAÇÃO (MATRIZES)
# ===================================================================
def get_translation_matrix(x, y):
    return np.array([
        [1.0, 0.0, 0.0, x],
        [0.0, 1.0, 0.0, y],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ], dtype=np.float32)

def get_rotation_matrix(degrees):
    rad = np.radians(degrees)
    c = np.cos(rad)
    s = np.sin(rad)
    return np.array([
        [c,  -s, 0.0, 0.0],
        [s,   c, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ], dtype=np.float32)

def get_scale_matrix(s):
    return np.array([
        [s,   0.0, 0.0, 0.0],
        [0.0, s,   0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ], dtype=np.float32)

# ===================================================================
# 2. CONTROLE PELO TECLADO (CALLBACK)
# ===================================================================
def key_callback(window, key, scancode, action, mods):
    global tx, ty, angle, scale
    
    if action == glfw.PRESS or action == glfw.REPEAT:
        # Translação (Setas direcionais)
        if key == glfw.KEY_UP:      ty += 0.05
        elif key == glfw.KEY_DOWN:  ty -= 0.05
        elif key == glfw.KEY_RIGHT: tx += 0.05
        elif key == glfw.KEY_LEFT:  tx -= 0.05
        
        # Rotação (R para horário, r para anti-horário)
        elif key == glfw.KEY_R:
            if mods & glfw.MOD_SHIFT: angle -= 5.0
            else:                     angle += 5.0
                
        # Escala (E para aumentar, e para diminuir)
        elif key == glfw.KEY_E:
            if mods & glfw.MOD_SHIFT: scale += 0.05
            else:
                scale -= 0.05
                if scale < 0.05: scale = 0.05

# ===================================================================
# 3. FUNÇÃO PRINCIPAL
# ===================================================================
def main():
    if not glfw.init():
        sys.exit()

    window = glfw.create_window(800, 600, "Foguete Interativo - Shaders", None, None)
    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)

    # Compila os shaders
    shader_program = OpenGL.GL.shaders.compileProgram(
        OpenGL.GL.shaders.compileShader(VERTEX_SHADER, GL_VERTEX_SHADER),
        OpenGL.GL.shaders.compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
    )

    # -------------------------------------------------------------
    # DEFINIÇÃO DOS VÉRTICES (FOGUETE CENTRALIZADO)
    # -------------------------------------------------------------
    vertices = np.array([
        # PARTE 1: Corpo (4 vértices, início 0) - Será GL_LINE_LOOP
        -0.1, -0.2,
         0.1, -0.2,
         0.1,  0.2,
        -0.1,  0.2,
        
        # PARTE 2: Bico (3 vértices, início 4) - Será GL_LINE_STRIP
        -0.1,  0.2,
         0.0,  0.35,
         0.1,  0.2,
         
        # PARTE 3: Asas (8 vértices, início 7) - Será GL_LINES
        -0.1, -0.1,   -0.2, -0.25, # Asa Esquerda (Linha 1)
        -0.2, -0.25,  -0.1, -0.2,  # Asa Esquerda (Linha 2)
         0.1, -0.1,    0.2, -0.25, # Asa Direita (Linha 1)
         0.2, -0.25,   0.1, -0.2,  # Asa Direita (Linha 2)
         
        # PARTE 4: Fogo da propulsão (6 vértices, início 15) - Será GL_LINES
        -0.05, -0.2,  -0.08, -0.35, # Chama Esquerda
         0.0,  -0.2,   0.0,  -0.4,  # Chama Central
         0.05, -0.2,   0.08, -0.35  # Chama Direita
    ], dtype=np.float32)

    # Configuração do VAO e VBO
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, None)

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    # Posições dos Uniforms
    transform_loc = glGetUniformLocation(shader_program, "transform")
    color_loc = glGetUniformLocation(shader_program, "u_color")

    # Loop principal
    while not glfw.window_should_close(window):
        glfw.poll_events()

        # Fundo azul escuro mantido do código do foguete original
        glClearColor(0.05, 0.05, 0.1, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(shader_program)

        # CÁLCULO DAS TRANSFORMAÇÕES
        mat_T = get_translation_matrix(tx, ty)
        mat_R = get_rotation_matrix(angle)
        mat_S = get_scale_matrix(scale)
        model_matrix = mat_T @ mat_R @ mat_S

        glUniformMatrix4fv(transform_loc, 1, GL_TRUE, model_matrix)

        glBindVertexArray(vao)

        # DESENHO POR PARTES (Alterando a cor de cada etapa)

        # 1. Corpo (Branco)
        glUniform4f(color_loc, 1.0, 1.0, 1.0, 1.0)
        glDrawArrays(GL_LINE_LOOP, 0, 4)

        # 2. Bico (Vermelho)
        glUniform4f(color_loc, 1.0, 0.2, 0.2, 1.0)
        glDrawArrays(GL_LINE_STRIP, 4, 3)

        # 3. Asas (Azul)
        glUniform4f(color_loc, 0.2, 0.6, 1.0, 1.0)
        glDrawArrays(GL_LINES, 7, 8)

        # 4. Fogo (Laranja)
        glUniform4f(color_loc, 1.0, 0.5, 0.0, 1.0)
        glDrawArrays(GL_LINES, 15, 6)

        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()