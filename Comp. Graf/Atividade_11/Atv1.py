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

// REQUISITO ATIVIDADE 1: Uniform para controlar a cor da curva
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

# Programa Principal (Atividade 1)
def main():
    if not glfw.init():
        return

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    window = glfw.create_window(800, 600, "Atividade 1 - Colorir Curva com Uniform", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    # Compilar Shaders
    shader_program = compileProgram(
        compileShader(VERTEX_SHADER, GL_VERTEX_SHADER),
        compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
    )

    # Localização do uniform
    u_color_loc = glGetUniformLocation(shader_program, "uColor")

    # Pontos de controle fixos para definir a curva
    p0, p1, p2, p3 = np.array([-0.8, -0.5]), np.array([-0.4, 0.8]), np.array([0.4, 0.8]), np.array([0.8, -0.5])
    pontos_curva = gerar_curva_bezier(p0, p1, p2, p3, resolucao=100)

    # Buffer da Curva
    vao_curva = glGenVertexArrays(1)
    vbo_curva = glGenBuffers(1)
    glBindVertexArray(vao_curva)
    glBindBuffer(GL_ARRAY_BUFFER, vbo_curva)
    glBufferData(GL_ARRAY_BUFFER, pontos_curva.nbytes, pontos_curva, GL_STATIC_DRAW)
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * 4, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)

    glLineWidth(3.0)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClearColor(0.1, 0.1, 0.1, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(shader_program)
        glBindVertexArray(vao_curva)

        # Atualização do uniform e teste de cores
        # Modifique os comentários para testar as 3 cores solicitadas:
        
        # Cor Teste 1: Ciano Vibrante (Padrão)
        glUniform3f(u_color_loc, 0.0, 0.9, 0.9) 
        
        # Cor Teste 2: Rosa Shock/Magenta
        # glUniform3f(u_color_loc, 0.9, 0.0, 0.6)
        
        # Cor Teste 3: Verde Limão
        # glUniform3f(u_color_loc, 0.4, 1.0, 0.1)

        # Desenhar curva
        glDrawArrays(GL_LINE_STRIP, 0, len(pontos_curva))

        glfw.swap_buffers(window)

    glDeleteVertexArrays(1, [vao_curva])
    glDeleteBuffers(1, [vbo_curva])
    glDeleteProgram(shader_program)
    glfw.terminate()

if __name__ == "__main__":
    main()