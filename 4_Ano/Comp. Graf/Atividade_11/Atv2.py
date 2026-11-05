import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np

# Definição dos Shaders (Vertex e Fragment)
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
uniform vec3 uColor; // Usado para diferenciar visualmente os componentes

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

# Programa Principal
def main():
    if not glfw.init():
        return

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    window = glfw.create_window(800, 600, "Atividade 2 - Polígono de Controle", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    shader_program = compileProgram(
        compileShader(VERTEX_SHADER, GL_VERTEX_SHADER),
        compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
    )

    u_color_loc = glGetUniformLocation(shader_program, "uColor")

    # Definição dos 4 pontos de controle
    pontos_controle = np.array([
        [-0.7, -0.6], # P0
        [-0.3,  0.7], # P1
        [ 0.3,  0.7], # P2
        [ 0.7, -0.6]  # P3
    ], dtype=np.float32)

    # Gerar pontos da curva de Bézier
    pontos_curva = gerar_curva_bezier(*pontos_controle, resolucao=100)

    # Configuração do VAO/VBO da Curva
    vao_curva = glGenVertexArrays(1)
    vbo_curva = glGenBuffers(1)
    glBindVertexArray(vao_curva)
    glBindBuffer(GL_ARRAY_BUFFER, vbo_curva)
    glBufferData(GL_ARRAY_BUFFER, pontos_curva.nbytes, pontos_curva, GL_STATIC_DRAW)
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * 4, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)

    # Configuração do VAO/VBO do Polígono de Controle
    vao_controle = glGenVertexArrays(1)
    vbo_controle = glGenBuffers(1)
    glBindVertexArray(vao_controle)
    glBindBuffer(GL_ARRAY_BUFFER, vbo_controle)
    glBufferData(GL_ARRAY_BUFFER, pontos_controle.nbytes, pontos_controle, GL_STATIC_DRAW)
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * 4, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)

    # Ajustes de espessura para fins visuais
    glPointSize(10.0) # Tamanho dos vértices de controle
    glLineWidth(2.0)  # Espessura das linhas

    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClearColor(0.12, 0.12, 0.12, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(shader_program)

        # Desenho do Polígono de Controle (Vértices e Segmentos)
        glBindVertexArray(vao_controle)
        
        # Desenhar segmentos conectando os pontos (Laranja/Amarelado)
        glUniform3f(u_color_loc, 0.9, 0.6, 0.1)
        glDrawArrays(GL_LINE_STRIP, 0, 4)

        # Desenhar os 4 pontos de controle individualmente (Vermelho)
        glUniform3f(u_color_loc, 0.9, 0.2, 0.2)
        glDrawArrays(GL_POINTS, 0, 4)

        # Desenho da Curva de Bézier (Ciano)
        glBindVertexArray(vao_curva)
        
        glUniform3f(u_color_loc, 0.1, 0.8, 0.9)
        glDrawArrays(GL_LINE_STRIP, 0, len(pontos_curva))

        glfw.swap_buffers(window)

    glDeleteVertexArrays(2, [vao_curva, vao_controle])
    glDeleteBuffers(2, [vbo_curva, vbo_controle])
    glDeleteProgram(shader_program)
    glfw.terminate()

if __name__ == "__main__":
    main()