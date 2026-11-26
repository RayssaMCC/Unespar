import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np

# Definição dos Shaders
VERTEX_SHADER = """
#version 330 core
layout (location = 0) in vec2 aPos;
void main() {
    gl_Position = vec4(aPos.x, aPos.y, 0.0, 1.0);
}
"""

FRAGMENT_SHADER = """
#version 330 core
out vec4 FragColor;
uniform vec3 uColor;

void main() {
    FragColor = vec4(uColor, 1.0);
}
"""

# Matemática da Curva de Bézier
def gerar_curva_bezier(p0, p1, p2, p3, resolucao=100):
    pontos = []
    for i in range(resolucao + 1):
        t = i / resolucao
        p = ( (1 - t)**3 * p0 + 
              3 * (1 - t)**2 * t * p1 + 
              3 * (1 - t) * t**2 * p2 + 
              t**3 * p3 )
        pontos.append(p)
    return np.array(pontos, dtype=np.float32)

# Programa Principal (Atividade 6)
def main():
    if not glfw.init():
        return

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    window = glfw.create_window(800, 600, "Atividade 6 - Controle por Teclado (W/A/S/D)", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    shader_program = compileProgram(
        compileShader(VERTEX_SHADER, GL_VERTEX_SHADER),
        compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
    )
    u_color_loc = glGetUniformLocation(shader_program, "uColor")

    # Pontos de Controle iniciais (O ponto P1 no índice 1 será o móvel)
    pontos_controle = np.array([
        [-0.8, -0.5], # P0
        [-0.3,  0.5], # P1 (Selecionado para controle)
        [ 0.3,  0.5], # P2
        [ 0.8, -0.5]  # P3
    ], dtype=np.float32)

    pontos_curva = gerar_curva_bezier(*pontos_controle, resolucao=100)

    # Setup do VAO/VBO da Curva
    vao_curva = glGenVertexArrays(1)
    vbo_curva = glGenBuffers(1)
    glBindVertexArray(vao_curva)
    glBindBuffer(GL_ARRAY_BUFFER, vbo_curva)
    glBufferData(GL_ARRAY_BUFFER, pontos_curva.nbytes, pontos_curva, GL_DYNAMIC_DRAW)
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * 4, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)

    # Setup do VAO/VBO do Polígono de Controle
    vao_ctrl = glGenVertexArrays(1)
    vbo_ctrl = glGenBuffers(1)
    glBindVertexArray(vao_ctrl)
    glBindBuffer(GL_ARRAY_BUFFER, vbo_ctrl)
    glBufferData(GL_ARRAY_BUFFER, pontos_controle.nbytes, pontos_controle, GL_DYNAMIC_DRAW)
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * 4, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)

    glPointSize(10.0)
    glLineWidth(2.0)
    velocidade_movimento = 0.002

    while not glfw.window_should_close(window):
        glfw.poll_events()

        # Entrada de teclado para mover o Ponto P1
        alterado = False
        if glfw.get_key(window, glfw.KEY_W) == glfw.PRESS or glfw.get_key(window, glfw.KEY_UP) == glfw.PRESS:
            pontos_controle[1][1] += velocidade_movimento
            alterado = True
        if glfw.get_key(window, glfw.KEY_S) == glfw.PRESS or glfw.get_key(window, glfw.KEY_DOWN) == glfw.PRESS:
            pontos_controle[1][1] -= velocidade_movimento
            alterado = True
        if glfw.get_key(window, glfw.KEY_A) == glfw.PRESS or glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS:
            pontos_controle[1][0] -= velocidade_movimento
            alterado = True
        if glfw.get_key(window, glfw.KEY_D) == glfw.PRESS or glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS:
            pontos_controle[1][0] += velocidade_movimento
            alterado = True

        # Recalcular e enviar novos vértices para a placa de vídeo se houver movimento
        if alterado:
            pontos_curva = gerar_curva_bezier(*pontos_controle, resolucao=100)
            
            glBindBuffer(GL_ARRAY_BUFFER, vbo_curva)
            glBufferSubData(GL_ARRAY_BUFFER, 0, pontos_curva.nbytes, pontos_curva)
            
            glBindBuffer(GL_ARRAY_BUFFER, vbo_ctrl)
            glBufferSubData(GL_ARRAY_BUFFER, 0, pontos_controle.nbytes, pontos_controle)

        glClearColor(0.12, 0.12, 0.12, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        glUseProgram(shader_program)

        # 1. Desenho do Polígono de Controle (Linhas Amarelas)
        glBindVertexArray(vao_ctrl)
        glUniform3f(u_color_loc, 0.8, 0.8, 0.2)
        glDrawArrays(GL_LINE_STRIP, 0, 4)

        # 2. Desenho dos Pontos Não-Selecionados (P0, P2, P3 em Vermelho)
        glUniform3f(u_color_loc, 0.9, 0.2, 0.2)
        glDrawArrays(GL_POINTS, 0, 1) # P0
        glDrawArrays(GL_POINTS, 2, 2) # P2 e P3

        # 3. Destaque visual do Ponto Selecionado P1 (Verde Brilhante)
        glUniform3f(u_color_loc, 0.1, 1.0, 0.1)
        glDrawArrays(GL_POINTS, 1, 1) # Apenas o P1

        # 4. Desenho da Curva de Bézier (Ciano)
        glBindVertexArray(vao_curva)
        glUniform3f(u_color_loc, 0.0, 0.9, 0.9)
        glDrawArrays(GL_LINE_STRIP, 0, len(pontos_curva))

        glfw.swap_buffers(window)

    glDeleteVertexArrays(2, [vao_curva, vao_ctrl])
    glDeleteBuffers(2, [vbo_curva, vbo_ctrl])
    glDeleteProgram(shader_program)
    glfw.terminate()

if __name__ == "__main__":
    main()