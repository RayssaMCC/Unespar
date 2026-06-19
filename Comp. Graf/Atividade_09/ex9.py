import ctypes
import glfw
import numpy as np
from OpenGL.GL import *

# --- Shaders ---
vertex_shader_source = """
#version 330 core
layout(location = 0) in vec3 aPos;
layout(location = 1) in vec3 aColor;

out vec3 vColor;

void main()
{
    gl_Position = vec4(aPos, 1.0);
    vColor = aColor;
}
"""

fragment_shader_source = """
#version 330 core
in vec3 vColor;
out vec4 FragColor;

uniform float brightness; // Uniform exigido pela atividade

void main()
{
    // Modifica a cor final multiplicando pelo brilho recebido da CPU
    FragColor = vec4(vColor * brightness, 1.0);
}
"""


def compile_shader(source, shader_type):
    shader = glCreateShader(shader_type)
    glShaderSource(shader, source)
    glCompileShader(shader)

    success = glGetShaderiv(shader, GL_COMPILE_STATUS)
    if not success:
        info = glGetShaderInfoLog(shader).decode()
        raise Exception(f"Erro de compilação do shader:\n{info}")

    return shader


def init_program():
    vertex_shader = compile_shader(vertex_shader_source, GL_VERTEX_SHADER)
    fragment_shader = compile_shader(fragment_shader_source, GL_FRAGMENT_SHADER)

    program = glCreateProgram()
    glAttachShader(program, vertex_shader)
    glAttachShader(program, fragment_shader)
    glLinkProgram(program)

    success = glGetProgramiv(program, GL_LINK_STATUS)
    if not success:
        info = glGetProgramInfoLog(program).decode()
        raise Exception(f"Erro de linkedição do programa:\n{info}")

    glDeleteShader(vertex_shader)
    glDeleteShader(fragment_shader)

    return program


def setup_object(vertices):
    # Função para configurar VAO e VBO de um objeto (Desafio Extra B)
    vao = glGenVertexArrays(1)
    vbo = glGenBuffers(1)

    glBindVertexArray(vao)

    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    # Atributo de Posição (Location 0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * 4, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)

    # Atributo de Cor (Location 1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * 4, ctypes.c_void_p(3 * 4))
    glEnableVertexAttribArray(1)

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    return vao, vbo


def main():
    if not glfw.init():
        raise Exception("Falha ao inicializar o GLFW")

    window = glfw.create_window(
        800, 600, "Atividade 09 - Multiplos Objetos e Uniforms", None, None
    )
    if not window:
        glfw.terminate()
        raise Exception("Falha ao criar a janela")

    glfw.make_context_current(window)
    shader_program = init_program()

    # --- DEFINIÇÃO DOS VÉRTICES (X, Y, Z, R, G, B) ---

    # Objeto 1: Triângulo Colorido (Lado Esquerdo Superior)
    vertices_triangulo = np.array(
        [
            -0.7, 0.6, 0.0,
            1.0, 0.0, 0.0,  # Topo (Vermelho)
            -0.9, 0.1, 0.0,
            0.0, 1.0, 0.0,  # Esquerda (Verde)
            -0.5, 0.1, 0.0,
            0.0, 0.0, 1.0,  # Direita (Azul)
        ],
        dtype=np.float32,
    )

    # Objeto 2: Quadrado (Centro/Baixo) - Composto por 2 triângulos
    vertices_quadrado = np.array(
        [
            # Primeiro triângulo
            -0.2, -0.1, 0.0,
            1.0, 1.0, 0.0,  # Sup. Esquerdo (Amarelo)
            0.2, -0.1, 0.0,
            1.0, 1.0, 0.0,  # Sup. Direito (Amarelo)
            0.2, -0.5, 0.0,
            1.0, 1.0, 0.0,  # Inf. Direito (Amarelo)
            
            # Segundo triângulo
            -0.2, -0.1, 0.0,
            1.0, 1.0, 0.0,  # Sup. Esquerdo (Amarelo)
            0.2, -0.5, 0.0,
            1.0, 1.0, 0.0,  # Inf. Direito (Amarelo)
            -0.2, -0.5, 0.0,
            1.0, 1.0, 0.0,  # Inf. Esquerdo (Amarelo)
        ],
        dtype=np.float32,
    )

    # Objeto 3: Losango (Lado Direito Superior) - Composto por 2 triângulos
    vertices_losango = np.array(
        [
            # Triângulo Superior
            0.7, 0.7, 0.0, 
            0.0, 1.0, 1.0,  # Topo (Ciano)
            0.5, 0.3, 0.0,
            1.0, 0.0, 1.0,  # Esquerda (Magenta)
            0.9, 0.3, 0.0,
            1.0, 0.0, 1.0,  # Direita (Magenta)

            # Triângulo Inferior
            0.5, 0.3, 0.0,
            1.0, 0.0, 1.0,  # Esquerda (Magenta)
            0.9, 0.3, 0.0,
            1.0, 0.0, 1.0,  # Direita (Magenta)
            0.7, -0.1, 0.0,
            0.0, 1.0, 1.0,  # Baixo (Ciano)
        ],
        dtype=np.float32,
    )

    # --- CONFIGURAÇÃO DE VAOs e VBOs ---
    vao_tri, vbo_tri = setup_object(vertices_triangulo)
    vao_quad, vbo_quad = setup_object(vertices_quadrado)
    vao_los, vbo_los = setup_object(vertices_losango)

    # Localização do Uniform no Fragment Shader
    brightness_loc = glGetUniformLocation(shader_program, "brightness")

    # --- LOOP PRINCIPAL ---
    while not glfw.window_should_close(window):
        # Desafio Extra D: Cor de fundo customizada (Azul escuro acinzentado)
        glClearColor(0.05, 0.05, 0.1, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(shader_program)

        # 1. Desenhar Triângulo (Brilho Normal: 1.0)
        glUniform1f(brightness_loc, 1.0)
        glBindVertexArray(vao_tri)
        glDrawArrays(GL_TRIANGLES, 0, 3)

        # 2. Desenhar Quadrado (Brilho Reduzido: 0.5)
        glUniform1f(brightness_loc, 0.5)
        glBindVertexArray(vao_quad)
        glDrawArrays(GL_TRIANGLES, 0, 6)

        # 3. Desenhar Losango (Brilho Alto: 1.5)
        glUniform1f(brightness_loc, 1.5)
        glBindVertexArray(vao_los)
        glDrawArrays(GL_TRIANGLES, 0, 6)

        glfw.swap_buffers(window)
        glfw.poll_events()

    # --- LIMPEZA DOS RECURSOS ---
    glDeleteVertexArrays(3, [vao_tri, vao_quad, vao_los])
    glDeleteBuffers(3, [vbo_tri, vbo_quad, vbo_los])
    glDeleteProgram(shader_program)
    glfw.terminate()


if __name__ == "__main__":
    main()