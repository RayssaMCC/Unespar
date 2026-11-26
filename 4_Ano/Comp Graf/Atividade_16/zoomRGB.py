import ctypes
import sys

import glfw
import numpy as np
from OpenGL.GL import *


WIDTH = 1000
HEIGHT = 700

mode = 1
factor = 2


VERTEX_SHADER = """
#version 330 core

layout(location = 0) in vec2 aPos;
layout(location = 1) in vec3 aColor;

out vec3 vertexColor;

void main()
{
    gl_Position = vec4(aPos, 0.0, 1.0);
    vertexColor = aColor;
}
"""


FRAGMENT_SHADER = """
#version 330 core

in vec3 vertexColor;

out vec4 FragColor;

void main()
{
    FragColor = vec4(vertexColor, 1.0);
}
"""


# Imagem própria 6x6 criada diretamente como matriz RGB. Possui várias cores e um padrão geométrico simples
def create_demo_image():

    return np.array([
        [
            [1.0, 0.0, 0.0],  # vermelho
            [1.0, 0.5, 0.0],  # laranja
            [1.0, 1.0, 0.0],  # amarelo
            [0.0, 1.0, 0.0],  # verde
            [0.0, 1.0, 1.0],  # ciano
            [0.0, 0.0, 1.0],  # azul
        ],
        [
            [1.0, 0.5, 0.0],
            [1.0, 1.0, 1.0],
            [0.2, 0.2, 0.2],
            [0.2, 0.2, 0.2],
            [1.0, 1.0, 1.0],
            [0.0, 1.0, 1.0],
        ],
        [
            [1.0, 1.0, 0.0],
            [0.2, 0.2, 0.2],
            [1.0, 0.0, 1.0],
            [1.0, 0.0, 1.0],
            [0.2, 0.2, 0.2],
            [1.0, 1.0, 0.0],
        ],
        [
            [0.0, 1.0, 0.0],
            [0.2, 0.2, 0.2],
            [1.0, 0.0, 1.0],
            [1.0, 0.0, 1.0],
            [0.2, 0.2, 0.2],
            [0.0, 1.0, 0.0],
        ],
        [
            [0.0, 1.0, 1.0],
            [1.0, 1.0, 1.0],
            [0.2, 0.2, 0.2],
            [0.2, 0.2, 0.2],
            [1.0, 1.0, 1.0],
            [0.0, 1.0, 1.0],
        ],
        [
            [0.0, 0.0, 1.0],
            [0.0, 1.0, 1.0],
            [0.0, 1.0, 0.0],
            [1.0, 1.0, 0.0],
            [1.0, 0.5, 0.0],
            [1.0, 0.0, 0.0],
        ],
    ], dtype=np.float32)


def inspect_image(image):
    # Exibe as dimensões e três pixels escolhidos
    print("\n========== INSPECAO DA MATRIZ ==========")
    print("shape:", image.shape)
    print("altura =", image.shape[0])
    print("largura =", image.shape[1])
    print("quantidade de canais =", image.shape[2])

    samples = [
        (0, 0, "vermelho"),
        (0, 3, "verde"),
        (2, 2, "magenta"),
    ]

    print("\nTres pixels escolhidos:")
    for row, col, expected in samples:
        print(f"image[{row}, {col}] = {image[row, col]} -> aproximadamente {expected}")


def only_channel(image, channel_index):
    result = np.zeros_like(image)
    result[:, :, channel_index] = image[:, :, channel_index]
    return result

# Repete cada pixel horizontal e verticalmente
def zoom_in_quadrado(image, factor):
    zoomed = np.repeat(image, factor, axis=0)
    zoomed = np.repeat(zoomed, factor, axis=1)
    return zoomed


# Zoom bilinear. O mapeamento usa as extremidades da imagem original para que os pixels das bordas sejam preservados corretamente
def zoom_in_linear(image, factor):
    height, width, channels = image.shape
    new_height = height * factor
    new_width = width * factor

    result = np.zeros(
        (new_height, new_width, channels),
        dtype=np.float32
    )

    for new_row in range(new_height):
        if new_height == 1:
            source_y = 0.0
        else:
            source_y = new_row * (height - 1) / (new_height - 1)

        y0 = int(np.floor(source_y))
        y1 = min(y0 + 1, height - 1)
        ty = source_y - y0

        for new_col in range(new_width):
            if new_width == 1:
                source_x = 0.0
            else:
                source_x = new_col * (width - 1) / (new_width - 1)

            x0 = int(np.floor(source_x))
            x1 = min(x0 + 1, width - 1)
            tx = source_x - x0

            top = (
                (1.0 - tx) * image[y0, x0]
                + tx * image[y0, x1]
            )

            bottom = (
                (1.0 - tx) * image[y1, x0]
                + tx * image[y1, x1]
            )

            result[new_row, new_col] = (
                (1.0 - ty) * top
                + ty * bottom
            )

    return result

# Redução por seleção: mantém um pixel de cada bloco/fator e descarta os demais
def zoom_out_quadrado(image, factor):
    return image[::factor, ::factor]

# Redução calculando a média de cada bloco
def zoom_out_media(image, factor):
    height, width, channels = image.shape

    new_height = height // factor
    new_width = width // factor

    result = np.zeros(
        (new_height, new_width, channels),
        dtype=np.float32
    )

    for row in range(new_height):
        for col in range(new_width):
            block = image[
                row * factor:(row + 1) * factor,
                col * factor:(col + 1) * factor
            ]

            result[row, col] = block.mean(axis=(0, 1))

    return result


def create_window():
    if not glfw.init():
        raise RuntimeError("Nao foi possivel inicializar o GLFW.")

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    # Permite alterar livremente o tamanho da janela.
    glfw.window_hint(glfw.RESIZABLE, glfw.TRUE)

    if sys.platform == "darwin":
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)

    window = glfw.create_window(
        WIDTH,
        HEIGHT,
        "Laboratorio de Zoom e Representacao de Imagens",
        None,
        None
    )

    if not window:
        glfw.terminate()
        raise RuntimeError("Nao foi possivel criar a janela.")

    glfw.make_context_current(window)
    glfw.set_framebuffer_size_callback(window, framebuffer_size_callback)
    return window

# Atualiza o viewport sempre que a janela for redimensionada
def framebuffer_size_callback(window, width, height):
    width = max(1, width)
    height = max(1, height)
    glViewport(0, 0, width, height)


def compile_shader(source, shader_type):
    shader = glCreateShader(shader_type)
    glShaderSource(shader, source)
    glCompileShader(shader)

    success = glGetShaderiv(shader, GL_COMPILE_STATUS)

    if not success:
        error = glGetShaderInfoLog(shader).decode()
        glDeleteShader(shader)
        raise RuntimeError(f"Erro ao compilar shader:\n{error}")

    return shader


def create_shader_program():
    vertex_shader = compile_shader(VERTEX_SHADER, GL_VERTEX_SHADER)
    fragment_shader = compile_shader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)

    program = glCreateProgram()
    glAttachShader(program, vertex_shader)
    glAttachShader(program, fragment_shader)
    glLinkProgram(program)

    success = glGetProgramiv(program, GL_LINK_STATUS)

    if not success:
        error = glGetProgramInfoLog(program).decode()
        glDeleteShader(vertex_shader)
        glDeleteShader(fragment_shader)
        glDeleteProgram(program)
        raise RuntimeError(f"Erro ao linkar programa:\n{error}")

    glDeleteShader(vertex_shader)
    glDeleteShader(fragment_shader)

    return program


def add_cell(vertices, x0, y0, x1, y1, color):
    r, g, b = color

    vertices.extend([
        x0, y0, r, g, b,
        x1, y0, r, g, b,
        x1, y1, r, g, b,

        x0, y0, r, g, b,
        x1, y1, r, g, b,
        x0, y1, r, g, b,
    ])


def build_grid_vertices(
    image,
    center_x,
    center_y,
    cell_size,
    gap
):
    vertices = []

    height, width, _ = image.shape

    total_width = width * cell_size + (width - 1) * gap
    total_height = height * cell_size + (height - 1) * gap

    start_x = center_x - total_width / 2.0
    start_y = center_y + total_height / 2.0

    for row in range(height):
        for col in range(width):
            x0 = start_x + col * (cell_size + gap)
            y1 = start_y - row * (cell_size + gap)

            x1 = x0 + cell_size
            y0 = y1 - cell_size

            add_cell(
                vertices,
                x0,
                y0,
                x1,
                y1,
                image[row, col]
            )

    return np.array(vertices, dtype=np.float32)

# Escolhe tamanho de célula para caber na janela
def grid_cell_size(image, maximum_size=0.15):
    height, width, _ = image.shape
    return min(
        maximum_size,
        1.5 / max(height, width)
    )


def build_three_images_vertices(
    images,
    centers=None,
    maximum_cell_size=0.07
):
    """
    Monta três imagens lado a lado.

    O layout usa três regiões fixas da área normalizada:
        esquerda  -> -0.66
        centro    ->  0.00
        direita   ->  0.66

    O tamanho das células é calculado individualmente e limitado
    para que mesmo imagens grandes (ex: 18x18 no fator 3)
    permaneçam dentro de suas respectivas regiões
    """
    if len(images) != 3:
        raise ValueError("A comparação deve possuir exatamente 3 imagens.")

    # Cada imagem recebe aproximadamente 28% da largura total.
    # O espaço entre os painéis permanece livre.
    panel_centers = [-0.68, 0.0, 0.68]

    parts = []

    for image, center_x in zip(images, panel_centers):
        height, width, _ = image.shape

        # Limita a largura da imagem a aproximadamente 0.45
        # da área normalizada. Isso impede que ela invada o
        # painel vizinho.
        cell_from_width = 0.40 / width

        # Limita também a altura para manter tudo visível.
        cell_from_height = 1.55 / height

        cell_size = min(
            maximum_cell_size,
            cell_from_width,
            cell_from_height
        )

        parts.append(
            build_grid_vertices(
                image,
                center_x=center_x,
                center_y=0.0,
                cell_size=cell_size,
                gap=min(0.006, cell_size * 0.10)
            )
        )

    return np.concatenate(parts)


def build_scene_vertices(original_image):
    if mode == 1:
        return build_grid_vertices(
            original_image,
            center_x=0.0,
            center_y=0.0,
            cell_size=grid_cell_size(original_image, 0.18),
            gap=0.01
        )

    if mode == 2:
        red = only_channel(original_image, 0)
        green = only_channel(original_image, 1)
        blue = only_channel(original_image, 2)

        return build_three_images_vertices(
            [red, green, blue],
            maximum_cell_size=0.12
        )

    if mode == 3:
        image = zoom_in_quadrado(original_image, factor)
        return build_grid_vertices(
            image,
            center_x=0.0,
            center_y=0.0,
            cell_size=grid_cell_size(image, 0.11),
            gap=0.004
        )

    if mode == 4:
        image = zoom_in_linear(original_image, factor)
        return build_grid_vertices(
            image,
            center_x=0.0,
            center_y=0.0,
            cell_size=grid_cell_size(image, 0.11),
            gap=0.004
        )

    if mode == 5:
        image = zoom_out_quadrado(original_image, factor)
        return build_grid_vertices(
            image,
            center_x=0.0,
            center_y=0.0,
            cell_size=grid_cell_size(image, 0.20),
            gap=0.01
        )

    if mode == 6:
        image = zoom_out_media(original_image, factor)
        return build_grid_vertices(
            image,
            center_x=0.0,
            center_y=0.0,
            cell_size=grid_cell_size(image, 0.20),
            gap=0.01
        )

    if mode == 7:
        zoom_quadrado = zoom_in_quadrado(original_image, factor)
        zoom_linear = zoom_in_linear(original_image, factor)

        return build_three_images_vertices(
            [original_image, zoom_quadrado, zoom_linear],
            maximum_cell_size=0.055
        )

    if mode == 8:
        zoom_quadrado = zoom_out_quadrado(original_image, factor)
        zoom_media = zoom_out_media(original_image, factor)

        return build_three_images_vertices(
            [original_image, zoom_quadrado, zoom_media],
            maximum_cell_size=0.105
        )

    return build_grid_vertices(
        original_image,
        center_x=0.0,
        center_y=0.0,
        cell_size=grid_cell_size(original_image, 0.18),
        gap=0.01
    )

# Imprime dimensões dos resultados pedidos na atividade
def print_zoom_dimensions(image):
    zoom_quadrado = zoom_in_quadrado(image, factor)
    zoom_linear = zoom_in_linear(image, factor)
    out_quadrado = zoom_out_quadrado(image, factor)
    out_media = zoom_out_media(image, factor)

    print("\n========== DIMENSOES ==========")
    print("Fator atual:", factor)
    print("original.shape =", image.shape)
    print("zoom_quadrado.shape =", zoom_quadrado.shape)
    print("zoom_linear.shape =", zoom_linear.shape)
    print("zoom_out_quadrado.shape =", out_quadrado.shape)
    print("zoom_out_media.shape =", out_media.shape)

    # Demonstra um pixel interpolado do zoom linear
    # Para fator 2, a posição (1, 1) fica entre pixels da matriz original
    if factor == 2:
        row, col = 1, 1

        print("\n========== PIXEL INTERPOLADO ==========")
        print(f"zoom_linear[{row}, {col}] =", zoom_linear[row, col])

        print("\nPixels originais que influenciaram:")
        print("image[0, 0] =", image[0, 0])
        print("image[0, 1] =", image[0, 1])
        print("image[1, 0] =", image[1, 0])
        print("image[1, 1] =", image[1, 1])

        print("\nO pixel interpolado eh obtido pela combinacao das cores dos quatro pixels vizinhos")


def print_help():
    print()
    print("==========================================================")
    print("Laboratorio de Zoom e Representacao de Imagens")
    print("==========================================================")
    print("1 -> imagem original")
    print("2 -> canais RGB")
    print("3 -> Zoom In quadrado")
    print("4 -> Zoom In linear")
    print("5 -> Zoom Out quadrado")
    print("6 -> Zoom Out por media")
    print("7 -> comparacao Zoom In: Original | Quadrado | Linear")
    print("8 -> comparacao Zoom Out: Original | Quadrado | Media")
    print("F -> alternar fator entre 2 e 3")
    print("H -> ajuda")
    print("ESC -> sair")
    print("==========================================================")
    print()


def process_input(window):
    global mode, factor

    if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS:
        glfw.set_window_should_close(window, True)

    keys = [
        glfw.KEY_1,
        glfw.KEY_2,
        glfw.KEY_3,
        glfw.KEY_4,
        glfw.KEY_5,
        glfw.KEY_6,
        glfw.KEY_7,
        glfw.KEY_8,
    ]

    for index, key in enumerate(keys, start=1):
        if glfw.get_key(window, key) == glfw.PRESS:
            mode = index

    if glfw.get_key(window, glfw.KEY_F) == glfw.PRESS:
        # Pequeno debounce para não alternar muitas vezes por segundo
        factor = 3 if factor == 2 else 2
        print("\nFator alterado para:", factor)
        print_zoom_dimensions(create_demo_image())
        while glfw.get_key(window, glfw.KEY_F) == glfw.PRESS:
            glfw.poll_events()

    if glfw.get_key(window, glfw.KEY_H) == glfw.PRESS:
        print_help()
        while glfw.get_key(window, glfw.KEY_H) == glfw.PRESS:
            glfw.poll_events()


def create_geometry(vertices):
    vao = glGenVertexArrays(1)
    vbo = glGenBuffers(1)

    glBindVertexArray(vao)

    glBindBuffer(GL_ARRAY_BUFFER, vbo)

    glBufferData(
        GL_ARRAY_BUFFER,
        vertices.nbytes,
        vertices,
        GL_DYNAMIC_DRAW
    )

    float_size = np.dtype(np.float32).itemsize
    stride = 5 * float_size

    glVertexAttribPointer(
        0,
        2,
        GL_FLOAT,
        GL_FALSE,
        stride,
        ctypes.c_void_p(0)
    )

    glEnableVertexAttribArray(0)

    glVertexAttribPointer(
        1,
        3,
        GL_FLOAT,
        GL_FALSE,
        stride,
        ctypes.c_void_p(2 * float_size)
    )

    glEnableVertexAttribArray(1)

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    return vao, vbo


def update_vbo(vbo, vertices):
    glBindBuffer(GL_ARRAY_BUFFER, vbo)

    glBufferData(
        GL_ARRAY_BUFFER,
        vertices.nbytes,
        vertices,
        GL_DYNAMIC_DRAW
    )

    glBindBuffer(GL_ARRAY_BUFFER, 0)


def main():
    global factor

    window = create_window()
    program = create_shader_program()

    original_image = create_demo_image()

    # Parte 2 da atividade: inspeção da matriz
    inspect_image(original_image)

    # Dimensões dos quatro resultados
    print_zoom_dimensions(original_image)

    # Fator começa em 2
    factor = 2

    vertices = build_scene_vertices(original_image)
    vao, vbo = create_geometry(vertices)

    framebuffer_width, framebuffer_height = glfw.get_framebuffer_size(window)
    glViewport(
        0,
        0,
        max(1, framebuffer_width),
        max(1, framebuffer_height)
    )

    print_help()

    while not glfw.window_should_close(window):
        process_input(window)

        vertices = build_scene_vertices(original_image)
        update_vbo(vbo, vertices)

        glClearColor(0.08, 0.08, 0.10, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(program)

        glBindVertexArray(vao)

        glDrawArrays(
            GL_TRIANGLES,
            0,
            len(vertices) // 5
        )

        glBindVertexArray(0)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glDeleteVertexArrays(1, [vao])
    glDeleteBuffers(1, [vbo])
    glDeleteProgram(program)

    glfw.destroy_window(window)
    glfw.terminate()


if __name__ == "__main__":
    main()
