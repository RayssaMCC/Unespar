import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
import math

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

# Programa Principal (Atividade 4)
def main():
    if not glfw.init():
        return

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    window = glfw.create_window(800, 600, "Atividade 4 - Cor Animada", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    shader_program = compileProgram(
        compileShader(VERTEX_SHADER, GL_VERTEX_SHADER),
        compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
    )
    u_color_loc = glGetUniformLocation(shader_program, "uColor")

    # Geometria fixa da curva
    pontos_curva = gerar_curva_bezier(
        np.array([-0.8, -0.5]), np.array([-0.4, 0.8]), 
        np.array([ 0.4,  0.8]), np.array([ 0.8, -0.5])
    )

    vao = glGenVertexArrays(1)
    vbo = glGenBuffers(1)
    glBindVertexArray(vao)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, pontos_curva.nbytes, pontos_curva, GL_STATIC_DRAW)
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * 4, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)

    glLineWidth(4.0)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClearColor(0.1, 0.1, 0.1, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(shader_program)
        glBindVertexArray(vao)

        # Calcular cores com base no tempo
        tempo = glfw.get_time()
        r = (math.sin(tempo) + 1.0) / 2.0
        g = (math.sin(tempo + 2.0) + 1.0) / 2.0
        b = (math.sin(tempo + 4.0) + 1.0) / 2.0

        # Atualizar o uniform a cada quadro
        glUniform3f(u_color_loc, r, g, b)

        glDrawArrays(GL_LINE_STRIP, 0, len(pontos_curva))

        glfw.swap_buffers(window)

    glDeleteVertexArrays(1, [vao])
    glDeleteBuffers(1, [vbo])
    glDeleteProgram(shader_program)
    glfw.terminate()

if __name__ == "__main__":
    main()