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

def criar_buffer(pontos):
    vao = glGenVertexArrays(1)
    vbo = glGenBuffers(1)
    glBindVertexArray(vao)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, pontos.nbytes, pontos, GL_STATIC_DRAW)
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * 4, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)
    return vao, vbo

# Programa Principal (Atividade 3)
def main():
    if not glfw.init():
        return

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    window = glfw.create_window(800, 600, "Atividade 3 - Comparar Curvas", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    shader_program = compileProgram(
        compileShader(VERTEX_SHADER, GL_VERTEX_SHADER),
        compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
    )
    u_color_loc = glGetUniformLocation(shader_program, "uColor")

    # Mesmos pontos iniciais e finais para ambas as curvas
    p0 = np.array([-0.8, -0.2])
    p3 = np.array([ 0.8, -0.2])

    # Curva 1: Pontos intermediários puxando para cima
    p1_c1, p2_c1 = np.array([-0.4, 0.8]), np.array([0.4, 0.8])
    curva1 = gerar_curva_bezier(p0, p1_c1, p2_c1, p3)
    vao1, vbo1 = criar_buffer(curva1)

    # Curva 2: Pontos intermediários puxando para baixo
    p1_c2, p2_c2 = np.array([-0.4, -0.8]), np.array([0.4, -0.8])
    curva2 = gerar_curva_bezier(p0, p1_c2, p2_c2, p3)
    vao2, vbo2 = criar_buffer(curva2)

    glLineWidth(3.0)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClearColor(0.1, 0.1, 0.1, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(shader_program)

        # Desenhar Curva 1 (Ciano)
        glBindVertexArray(vao1)
        glUniform3f(u_color_loc, 0.0, 0.9, 0.9)
        glDrawArrays(GL_LINE_STRIP, 0, len(curva1))

        # Desenhar Curva 2 (Magenta)
        glBindVertexArray(vao2)
        glUniform3f(u_color_loc, 0.9, 0.0, 0.9)
        glDrawArrays(GL_LINE_STRIP, 0, len(curva2))

        glfw.swap_buffers(window)

    glDeleteVertexArrays(2, [vao1, vao2])
    glDeleteBuffers(2, [vbo1, vbo2])
    glDeleteProgram(shader_program)
    glfw.terminate()

if __name__ == "__main__":
    main()