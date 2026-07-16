import glfw
from OpenGL.GL import *
import ctypes # uso de ponteiros para passar dados para os shaders
import numpy as np # para criar arrays de vértices e cores

# Shader que processa VBO e calcula poisção de cada vértice
VERTEX_SHADER_SOURCE = """
#version 330 core

layout(location = 0) in vec3 aPos; // Atributo de posição do vértice
layout(location = 1) in vec3 aColor; // Atributo de cor do vértice
out vec3 vColor; // Variável de saída para passar a cor para o fragment shader

void main(){
    gl_Position = vec4(aPos, 1.0); // Define a posição do vértice
    vColor = aColor; // Passa a cor para o fragment shader
    
}
"""
# Recebe a cor de cada vértice (processado no VERTEX_SHADER) e cria uma cor para os fragmentos (pixels)
FRAGMENT_SHADER_SOURCE = """
#version 330 core

in vec3 vColor;
out vec4 FragColor;

uniform float brightness; // Variável uniforme para ajustar o brilho da cor

void main(){
    FragColor = vec4(vColor * brightness, 1.0);
}
"""

# Função que compila o shader e verifica se houve erro na compilação
def compile_shader(source, shader_type):
    shader = glCreateShader(shader_type) # Cria o shader
    glShaderSource(shader, source) # Passa o código do shader para o OpenGL
    glCompileShader(shader) # Compila o shader

    # Verifica se houve erro na compilação do shader
    success = glGetShaderiv(shader, GL_COMPILE_STATUS)
    if not success:
        error_message = glGetShaderInfoLog(shader).decode() # Decodifica a mensagem de erro do shader para string
        shader_name = "VERTEX" if shader_type == GL_VERTEX_SHADER else "FRAGMENT"
        raise RuntimeError(f"Erro ao compilar o shader {shader_name}: {error_message}")

    return shader
    

# Cria o programa de shader e linka eles
def create_shader_program(vertex_source, fragment_source):
    vertex_shader = compile_shader(vertex_source, GL_VERTEX_SHADER) # Compila o shader de vértice
    fragment_shader = compile_shader(fragment_source, GL_FRAGMENT_SHADER) # Compila o shader de fragmento

    shader_program = glCreateProgram() # Cria o programa de shader
    glAttachShader(shader_program, vertex_shader) # Anexa o shader de vértice ao programa
    glAttachShader(shader_program, fragment_shader) # Anexa o shader de fragmento ao programa
    glLinkProgram(shader_program) # Linka o programa de shader

    success = glGetProgramiv(shader_program, GL_LINK_STATUS) # Verifica se houve erro no link do programa
    if not success:
        error_message = glGetProgramInfoLog(shader_program).decode() # Decodifica a mensagem de erro do link para string
        raise RuntimeError(f"Erro ao linkar o programa de shader: {error_message}")

    # Deleta os shaders de vértice e fragmento (não são mais necessários após o link) para limpar a memória
    glDeleteShader(vertex_shader) 
    glDeleteShader(fragment_shader)

    return shader_program


# Callback que é chamado sempre que a janela é redimensionada
def framebuffer_size_callback(window, width, height):
    glViewport(0, 0, width, height) # Atualiza a viewport do OpenGL para o tamanho da janela


# Responsável pelas configs iniciais do OpenGL, criação de shaders, buffers, etc.
def init():
    vertices = np.array([
        # Posições        # Cores
         0.0,  0.5, 0.0,  1.0, 0.0, 0.0,  # Vértice 1: vermelho
        -0.5, -0.5, 0.0,  0.0, 1.0, 0.0,  # Vértice 2: verde
         0.5, -0.5, 0.0,  0.0, 0.0, 1.0,  # Vértice 3: azul
    ], dtype=np.float32)

    # Gera um buffer para salvar os vértices na GPU
    VBO = glGenBuffers(1) 

    # Gera um objeto para armazenar as configurações de como os vértices são lidos (quantos atributos cada vértice possui, onde começa, qual é o tamanho de cada atributo, etc)
    VAO = glGenVertexArrays(1) 

    glBindVertexArray(VAO) # Ativa o VAO para configurar as definições de leitura dos vértices no OpenGL
    glBindBuffer(GL_ARRAY_BUFFER, VBO) # Ativa o VBO para enviar os dados dos vértices para a GPU
   
   # Envia os dados dos vértices para a GPU
    glBufferData(GL_ARRAY_BUFFER, 
                 vertices.nbytes, # Tamanho dos dados em bytes (número de vértices * número de atributos por vértice * tamanho de cada atributo)
                 vertices, # Os dados dos vértices em si (array de floats)
                 GL_STATIC_DRAW) # Indica que os dados dos vértices não serão alterados frequentemente (só serão enviados uma vez)

    # Configura o layout dos atributos dos vértices para o shader (posição e cor), como o VBO vai ser interpretado
    glVertexAttribPointer(0, # Índice do atributo (0 para posição)
                          3, # Número de componentes por vértice (3 para posição x, y, z)
                          GL_FLOAT, # Tipo dos dados (GL_FLOAT para floats)
                          GL_FALSE, # Indica se os dados devem ser normalizados (GL_FALSE para não normalizar, já que são coordenadas de posição)
                          6*4, # Stride: número de bytes entre o início de um vértice e o início do próximo (6 floats por vértice * 4 bytes por float)
                          ctypes.c_void_p(0)) # Offset: posição do primeiro atributo (posição) dentro do vértice (0 bytes, já que começa no início do vértice)

    glVertexAttribPointer(1, # Índice do atributo (1 para cor)
                          3, # Número de componentes por vértice (3 para cor r, g, b)
                          GL_FLOAT, # Tipo dos dados (GL_FLOAT para floats)
                          GL_FALSE, # Indica se os dados devem ser normalizados (GL_FALSE para não normalizar, já que são valores de cor entre 0 e 1)
                          6*4, # Stride: número de bytes entre o início de um vértice e o início do próximo (6 floats por vértice * 4 bytes por float)
                          ctypes.c_void_p(3*4)) # Offset: posição do segundo atributo (cor) dentro do vértice (3 floats * 4 bytes por float = 12 bytes)

    glEnableVertexAttribArray(0) # Habilita o atributo de posição
    glEnableVertexAttribArray(1) # Habilita o atributo de cor

    shader_program = create_shader_program(VERTEX_SHADER_SOURCE, FRAGMENT_SHADER_SOURCE) # Cria o programa de shader

    brightness_location = glGetUniformLocation(shader_program, "brightness") # Obtém a localização da variável uniforme de brilho

    # Desativa o VBO e VAO após a configuração, pois não é necessário mantê-los ativos
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    return shader_program, VBO, VAO, brightness_location # Retorna para uso posterior


# Responsável por renderizar a cena a cada frame
def render(shader_program, VAO, brightness_location, brightness_value):
    glClearColor(0.1, 0.1, 0.1, 1.0) # Define a cor de fundo da tela
    glClear(GL_COLOR_BUFFER_BIT) # Limpa o buffer de cor da tela

    glUseProgram(shader_program) # Ativa o programa de shader
    glBindVertexArray(VAO) # Ativa o VAO para desenhar os vértices
    glUniform1f(brightness_location, brightness_value) # Define o valor da variável uniforme de brilho
    glDrawArrays(GL_TRIANGLES, 0, 3) # Desenha os vértices como triângulos (3 vértices)
    glBindVertexArray(0) # Desativa o VAO após desenhar


# Função principal que inicializa a janela, o OpenGL e entra no loop de renderização
def main():
    if not glfw.init(): # Inicializa a biblioteca GLFW
        raise Exception("Falha ao inicializar GLFW")

    # Configurações da janela
    window = glfw.create_window(800, 600, "Exemplo Shader - Triângulo Colorido", None, None) # Cria a janela
    if not window: # Verifica se a janela foi criada com sucesso
        glfw.terminate() # Finaliza a biblioteca GLFW
        raise Exception("Falha ao criar a janela GLFW")
    
    glfw.make_context_current(window) # Define o contexto atual para a janela criada
    glfw.set_framebuffer_size_callback(window, framebuffer_size_callback) # Define a função de callback para redimensionamento da janela
    glViewport(0, 0, 800, 600) # Define a viewport inicial para a janela

    shader_program, VBO, VAO, brightness_location = init() # Inicializa o OpenGL e cria os shaders, VBO e VAO
    while not glfw.window_should_close(window): # Loop principal da aplicação

        brightness_value = (np.sin(glfw.get_time()) + 1) / 2 # Calcula o valor do brilho baseado no tempo (oscila entre 0 e 1)

        render(shader_program, VAO, brightness_location, brightness_value) # Renderiza a cena

        glfw.swap_buffers(window) # Troca os buffers da janela
        glfw.poll_events() # Processa os eventos da janela (teclado, mouse, etc.)

    # Limpeza de recursos após o loop principal
    glDeleteVertexArrays(1, [VAO]) # Deleta o VAO
    glDeleteBuffers(1, [VBO]) # Deleta o VBO
    glDeleteProgram(shader_program) # Deleta o programa de shader
    glfw.terminate() # Finaliza a biblioteca GLFW


if __name__ == "__main__":
    main()
