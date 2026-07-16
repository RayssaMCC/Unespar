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

# Programa Principal (Atividade 5)
def main():
    if not glfw.init():
        return

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    window = glfw.create_window(800, 600, "Atividade 5 - Múltiplas Curvas", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    shader_program = compileProgram(
        compileShader(VERTEX_SHADER, GL_VERTEX_SHADER),
        compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
    )
    u_color_loc = glGetUniformLocation(shader_program, "uColor")

    # Organização dos dados das 3 curvas para evitar repetição
    curvas_config = [
        {
            "ctrl": [[-0.8,  0.5], [-0.3,  0.9], [0.3,  0.9], [0.8,  0.5]],
            "cor": (0.2, 1.0, 0.3),  # Verde
            "espessura": 1.0
        },
        {
            "ctrl": [[-0.8,  0.0], [-0.3,  0.4], [0.3, -0.4], [0.8,  0.0]],
            "cor": (1.0, 0.5, 0.0),  # Laranja
            "espessura": 4.0
        },
        {
            "ctrl": [[-0.8, -0.5], [-0.3, -0.9], [0.3, -0.9], [0.8, -0.5]],
            "cor": (0.0, 0.8, 1.0),  # Azul Ciano
            "espessura": 8.0
        }
    ]

    # Gerar pontos e criar os buffers VAO/VBO para cada curva
    curvas_render = []
    for config in curvas_config:
        pts = gerar_curva_bezier(*[np.array(p) for p in config["ctrl"]])
        
        vao = glGenVertexArrays(1)
        vbo = glGenBuffers(1)
        glBindVertexArray(vao)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, pts.nbytes, pts, GL_STATIC_DRAW)
        glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * 4, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)
        
        curvas_render.append({
            "vao": vao,
            "vbo": vbo,
            "tamanho": len(pts),
            "cor": config["cor"],
            "espessura": config["espessura"]
        })

    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClearColor(0.1, 0.1, 0.1, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(shader_program)

        # Loop de desenho iterando pelas configurações individuais
        for curva in curvas_render:
            glBindVertexArray(curva["vao"])
            glLineWidth(curva["espessura"])
            glUniform3f(u_color_loc, *curva["cor"])
            glDrawArrays(GL_LINE_STRIP, 0, curva["tamanho"])

        glfw.swap_buffers(window)

    for curva in curvas_render:
        glDeleteVertexArrays(1, [curva["vao"]])
        glDeleteBuffers(1, [curva["vbo"]])
    glDeleteProgram(shader_program)
    glfw.terminate()

if __name__ == "__main__":
    main()