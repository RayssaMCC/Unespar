import glfw
from OpenGL.GL import *
import ctypes
import numpy as np

VERTEX_SHADER_SOURCE = """
#version 330 core
layout(location = 0) in vec3 aPos;
layout(location = 1) in vec3 aColor;
out vec3 vColor;
void main(){
    gl_Position = vec4(aPos, 1.0);
    vColor = aColor;
}
"""

FRAGMENT_SHADER_SOURCE = """
#version 330 core
in vec3 vColor;
out vec4 FragColor;
void main(){
    FragColor = vec4(vColor, 1.0);
}
"""

def compile_shader(source, shader_type):
    shader = glCreateShader(shader_type)
    glShaderSource(shader, source)
    glCompileShader(shader)
    if not glGetShaderiv(shader, GL_COMPILE_STATUS):
        raise RuntimeError(glGetShaderInfoLog(shader).decode())
    return shader

def create_shader_program(vertex_source, fragment_source):
    vertex_shader = compile_shader(vertex_source, GL_VERTEX_SHADER)
    fragment_shader = compile_shader(fragment_source, GL_FRAGMENT_SHADER)
    shader_program = glCreateProgram()
    glAttachShader(shader_program, vertex_shader)
    glAttachShader(shader_program, fragment_shader)
    glLinkProgram(shader_program)
    glDeleteShader(vertex_shader) 
    glDeleteShader(fragment_shader)
    return shader_program

def init():
    # 6 Vértices no total: 3 para o primeiro triângulo, 3 para o segundo
    vertices = np.array([
        # --- TRIÂNGULO 1 (Esquerda) - Tons quentes ---
        # Posições         # Cores
        -0.9,  0.5, 0.0,   1.0, 0.0, 0.0,  # Topo esquerdo (Vermelho)
        -0.9, -0.5, 0.0,   1.0, 0.5, 0.0,  # Base esquerda (Laranja)
        -0.1, -0.5, 0.0,   1.0, 1.0, 0.0,  # Base direita (Amarelo)
        
        # --- TRIÂNGULO 2 (Direita) - Tons frios ---
        # Posições         # Cores
         0.5,  0.5, 0.0,   0.0, 0.0, 1.0,  # Topo direito (Azul)
         0.1, -0.5, 0.0,   0.0, 1.0, 1.0,  # Base esquerda (Ciano)
         0.9, -0.5, 0.0,   0.0, 1.0, 0.0,  # Base direita (Verde)
    ], dtype=np.float32)

    VBO = glGenBuffers(1) 
    VAO = glGenVertexArrays(1) 

    glBindVertexArray(VAO)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6*4, ctypes.c_void_p(0))
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6*4, ctypes.c_void_p(3*4))

    glEnableVertexAttribArray(0)
    glEnableVertexAttribArray(1)

    shader_program = create_shader_program(VERTEX_SHADER_SOURCE, FRAGMENT_SHADER_SOURCE)

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    return shader_program, VBO, VAO

def render(shader_program, VAO):
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    
    glUseProgram(shader_program)
    glBindVertexArray(VAO)
    # Mudança aqui: renderizando 6 vértices agora
    glDrawArrays(GL_TRIANGLES, 0, 6) 
    glBindVertexArray(0)

def main():
    if not glfw.init(): raise Exception("Falha ao inicializar GLFW")
    window = glfw.create_window(800, 600, "Dois Triângulos", None, None)
    if not window:
        glfw.terminate()
        raise Exception("Falha ao criar janela")
    
    glfw.make_context_current(window)
    glViewport(0, 0, 800, 600)
    shader_program, VBO, VAO = init()
    
    while not glfw.window_should_close(window):
        render(shader_program, VAO)
        glfw.swap_buffers(window)
        glfw.poll_events()

    glDeleteVertexArrays(1, [VAO])
    glDeleteBuffers(1, [VBO])
    glDeleteProgram(shader_program)
    glfw.terminate()

if __name__ == "__main__":
    main()