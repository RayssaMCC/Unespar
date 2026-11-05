import ctypes
import sys

import glfw
import numpy as np
from OpenGL.GL import *

WIDTH = 900
HEIGHT = 700

# Global Transform Values
tx = 0.0
ty = 0.0
tz = 0.0

angle_x = 0.0
angle_y = 0.0
angle_z = 0.0

scale_value = 1.0

# Controles da Pessoa 1
transform_order_mode = 0  # 0: T * R * S, 1: R * T * S
pivot_mode = 0  # 0: Origem, 1: Pivô externo
orbit_mode = False  # Alterna o modo órbita
orbit_angle = 0.0  # Ângulo acumulado da órbita
projection_mode = 1  # 1: paralela, 2: perspectiva
fov = 60.0  # Campo de visão da projeção perspectiva (20° a 120°)
comparison_mode = False  # Modo de comparação entre projeções

# Estado das transformações antes de entrar no modo de comparação
comparison_previous_state = None

# Centro de projeção / posição do observador
center_of_projection = np.array([
    0.0,
    0.0,
    3.0
], dtype=np.float32)

YELLOW = (0.95, 0.78, 0.25)
RED = (0.88, 0.30, 0.30)
BLUE = (0.30, 0.50, 0.88)

ORANGE = (0.95, 0.55, 0.25)
PURPLE = (0.60, 0.35, 0.80)
GREEN = (0.30, 0.70, 0.40)

WHITE = (0.95, 0.95, 0.95)
CYAN = (0.20, 0.80, 0.95)
GRAY = (0.40, 0.40, 0.40)


def vertex(x, y, z, color):
    return [x, y, z, color[0], color[1], color[2]]


face_vertices = np.array(
    vertex(-0.5, -0.5, 0.5, YELLOW)
    + vertex(0.5, -0.5, 0.5, YELLOW)
    + vertex(0.5, 0.5, 0.5, YELLOW)
    + vertex(-0.5, -0.5, 0.5, YELLOW)
    + vertex(0.5, 0.5, 0.5, YELLOW)
    + vertex(-0.5, 0.5, 0.5, YELLOW)
    + vertex(-0.5, -0.5, -0.5, RED)
    + vertex(0.5, 0.5, -0.5, RED)
    + vertex(0.5, -0.5, -0.5, RED)
    + vertex(-0.5, -0.5, -0.5, RED)
    + vertex(-0.5, 0.5, -0.5, RED)
    + vertex(0.5, 0.5, -0.5, RED)
    + vertex(-0.5, -0.5, -0.5, BLUE)
    + vertex(-0.5, -0.5, 0.5, BLUE)
    + vertex(-0.5, 0.5, 0.5, BLUE)
    + vertex(-0.5, -0.5, -0.5, BLUE)
    + vertex(-0.5, 0.5, 0.5, BLUE)
    + vertex(-0.5, 0.5, -0.5, BLUE)
    + vertex(0.5, -0.5, -0.5, ORANGE)
    + vertex(0.5, 0.5, 0.5, ORANGE)
    + vertex(0.5, -0.5, 0.5, ORANGE)
    + vertex(0.5, -0.5, -0.5, ORANGE)
    + vertex(0.5, 0.5, -0.5, ORANGE)
    + vertex(0.5, 0.5, 0.5, ORANGE)
    + vertex(-0.5, 0.5, -0.5, PURPLE)
    + vertex(-0.5, 0.5, 0.5, PURPLE)
    + vertex(0.5, 0.5, 0.5, PURPLE)
    + vertex(-0.5, 0.5, -0.5, PURPLE)
    + vertex(0.5, 0.5, 0.5, PURPLE)
    + vertex(0.5, 0.5, -0.5, PURPLE)
    + vertex(-0.5, -0.5, -0.5, GREEN)
    + vertex(0.5, -0.5, 0.5, GREEN)
    + vertex(-0.5, -0.5, 0.5, GREEN)
    + vertex(-0.5, -0.5, -0.5, GREEN)
    + vertex(0.5, -0.5, -0.5, GREEN)
    + vertex(0.5, -0.5, 0.5, GREEN),
    dtype=np.float32,
)

edge_vertices = np.array(
    vertex(-0.5, -0.5, -0.5, WHITE)
    + vertex(0.5, -0.5, -0.5, WHITE)
    + vertex(0.5, -0.5, -0.5, WHITE)
    + vertex(0.5, 0.5, -0.5, WHITE)
    + vertex(0.5, 0.5, -0.5, WHITE)
    + vertex(-0.5, 0.5, -0.5, WHITE)
    + vertex(-0.5, 0.5, -0.5, WHITE)
    + vertex(-0.5, -0.5, -0.5, WHITE)
    + vertex(-0.5, -0.5, 0.5, WHITE)
    + vertex(0.5, -0.5, 0.5, WHITE)
    + vertex(0.5, -0.5, 0.5, WHITE)
    + vertex(0.5, 0.5, 0.5, WHITE)
    + vertex(0.5, 0.5, 0.5, WHITE)
    + vertex(-0.5, 0.5, 0.5, WHITE)
    + vertex(-0.5, 0.5, 0.5, WHITE)
    + vertex(-0.5, -0.5, 0.5, WHITE)
    + vertex(-0.5, -0.5, -0.5, WHITE)
    + vertex(-0.5, -0.5, 0.5, WHITE)
    + vertex(0.5, -0.5, -0.5, WHITE)
    + vertex(0.5, -0.5, 0.5, WHITE)
    + vertex(0.5, 0.5, -0.5, WHITE)
    + vertex(0.5, 0.5, 0.5, WHITE)
    + vertex(-0.5, 0.5, -0.5, WHITE)
    + vertex(-0.5, 0.5, 0.5, WHITE),
    dtype=np.float32,
)

arrow_vertices = np.array(
    vertex(0.0, 0.4, 0.0, CYAN)
    + vertex(-0.2, -0.3, 0.0, CYAN)
    + vertex(0.0, -0.1, 0.0, CYAN)
    + vertex(0.0, 0.4, 0.0, CYAN)
    + vertex(0.0, -0.1, 0.0, CYAN)
    + vertex(0.2, -0.3, 0.0, CYAN),
    dtype=np.float32,
)

map_border_vertices = np.array(
    vertex(-1.0, -1.0, 0.0, WHITE) + vertex(1.0, -1.0, 0.0, WHITE)
    + vertex(1.0, -1.0, 0.0, WHITE) + vertex(1.0, 1.0, 0.0, WHITE)
    + vertex(1.0, 1.0, 0.0, WHITE) + vertex(-1.0, 1.0, 0.0, WHITE)
    + vertex(-1.0, 1.0, 0.0, WHITE) + vertex(-1.0, -1.0, 0.0, WHITE)
    + vertex(-1.0, 0.0, 0.0, GRAY) + vertex(1.0, 0.0, 0.0, GRAY)
    + vertex(0.0, -1.0, 0.0, GRAY) + vertex(0.0, 1.0, 0.0, GRAY),
    dtype=np.float32,
)

panel_bg_vertices = np.array(
    vertex(-1.0, -1.0, 0.0, (0.05, 0.05, 0.07))
    + vertex(1.0, -1.0, 0.0, (0.05, 0.05, 0.07))
    + vertex(1.0, 1.0, 0.0, (0.05, 0.05, 0.07))
    + vertex(-1.0, -1.0, 0.0, (0.05, 0.05, 0.07))
    + vertex(1.0, 1.0, 0.0, (0.05, 0.05, 0.07))
    + vertex(-1.0, 1.0, 0.0, (0.05, 0.05, 0.07)),
    dtype=np.float32,
)

panel_border_vertices = np.array(
    vertex(-1.0, -1.0, 0.0, WHITE) + vertex(-1.0, 1.0, 0.0, WHITE),
    dtype=np.float32,
)

FONT_5X7 = {
    'A': [(0,0,0,6),(0,6,4,6),(4,6,4,0),(0,3,4,3)],
    'B': [(0,0,0,6),(0,6,3,6),(3,6,4,5),(4,5,3,3),(0,3,3,3),(3,3,4,1),(4,1,3,0),(0,0,3,0)],
    'C': [(4,6,1,6),(1,6,0,5),(0,5,0,1),(0,1,1,0),(1,0,4,0)],
    'D': [(0,0,0,6),(0,6,3,6),(3,6,4,4),(4,4,4,2),(4,2,3,0),(0,0,3,0)],
    'E': [(4,6,0,6),(0,6,0,0),(0,0,4,0),(0,3,3,3)],
    'F': [(4,6,0,6),(0,6,0,0),(0,3,3,3)],
    'G': [(4,5,4,6),(4,6,1,6),(1,6,0,5),(0,5,0,1),(0,1,1,0),(1,0,4,0),(4,0,4,3),(4,3,2,3)],
    'H': [(0,0,0,6),(4,0,4,6),(0,3,4,3)],
    'I': [(1,6,3,6),(2,6,2,0),(1,0,3,0)],
    'J': [(3,6,3,1),(3,1,2,0),(2,0,1,0),(1,0,0,1)],
    'K': [(0,0,0,6),(0,3,4,6),(0,3,4,0)],
    'L': [(0,6,0,0),(0,0,4,0)],
    'M': [(0,0,0,6),(0,6,2,3),(2,3,4,6),(4,6,4,0)],
    'N': [(0,0,0,6),(0,6,4,0),(4,0,4,6)],
    'O': [(1,6,3,6),(3,6,4,5),(4,5,4,1),(4,1,3,0),(3,0,1,0),(1,0,0,1),(0,1,0,5),(0,5,1,6)],
    'P': [(0,0,0,6),(0,6,3,6),(3,6,4,5),(4,5,3,3),(3,3,0,3)],
    'Q': [(1,6,3,6),(3,6,4,5),(4,5,4,2),(4,2,3,1),(3,1,1,1),(1,1,0,2),(0,2,0,5),(0,5,1,6),(2,2,4,0)],
    'R': [(0,0,0,6),(0,6,3,6),(3,6,4,5),(4,5,3,3),(3,3,0,3),(2,3,4,0)],
    'S': [(4,5,3,6),(3,6,1,6),(1,6,0,5),(0,5,4,2),(4,2,3,0),(3,0,0,0)],
    'T': [(0,6,4,6),(2,6,2,0)],
    'U': [(0,6,0,1),(0,1,1,0),(1,0,3,0),(3,0,4,1),(4,1,4,6)],
    'V': [(0,6,2,0),(2,0,4,6)],
    'W': [(0,6,0,0),(0,0,2,3),(2,3,4,0),(4,0,4,6)],
    'X': [(0,0,4,6),(0,6,4,0)],
    'Y': [(0,6,2,3),(4,6,2,3),(2,3,2,0)],
    'Z': [(0,6,4,6),(4,6,0,0),(0,0,4,0)],
    '0': [(1,6,3,6),(3,6,4,5),(4,5,4,1),(4,1,3,0),(3,0,1,0),(1,0,0,1),(0,1,0,5),(0,5,1,6),(0,1,4,5)],
    '1': [(1,4,2,6),(2,6,2,0),(1,0,3,0)],
    '2': [(0,5,1,6),(1,6,3,6),(3,6,4,5),(4,5,0,1),(0,1,0,0),(0,0,4,0)],
    '3': [(0,5,1,6),(1,6,3,6),(3,6,4,5),(4,5,3,4),(3,4,4,3),(4,3,4,1),(4,1,3,0),(3,0,1,0),(1,0,0,1)],
    '4': [(3,0,3,6),(3,6,0,2),(0,2,4,2)],
    '5': [(4,6,0,6),(0,6,0,3),(0,3,3,3),(3,3,4,2),(4,2,4,1),(4,1,3,0),(3,0,0,0)],
    '6': [(3,6,1,6),(1,6,0,5),(0,5,0,1),(0,1,1,0),(1,0,3,0),(3,0,4,1),(4,1,4,2),(4,2,3,3),(3,3,0,3)],
    '7': [(0,6,4,6),(4,6,1,0)],
    '8': [(1,6,3,6),(3,6,4,5),(4,5,3,3),(3,3,1,3),(1,3,0,5),(0,5,1,6),(3,3,4,2),(4,2,3,0),(3,0,1,0),(1,0,0,1),(0,1,1,3)],
    '9': [(4,3,1,3),(1,3,0,4),(0,4,0,5),(0,5,1,6),(1,6,3,6),(3,6,4,5),(4,5,4,1),(4,1,3,0),(3,0,1,0)],
    ':': [(2,5,2,4),(2,2,2,1)],
    '-': [(1,3,3,3)],
    '.': [(2,1,2,0)],
    '*': [(1,5,3,1),(3,5,1,1),(2,6,2,0),(0,3,4,3)],
    '/': [(0,0,4,6)],
    '=': [(0,4,4,4),(0,2,4,2)],
    '>': [(0,5,3,3),(3,3,0,1)],
    '(': [(2,6,1,5),(1,5,1,1),(1,1,2,0)],
    ')': [(1,6,2,5),(2,5,2,1),(2,1,1,0)],
    ' ': []
}

VERTEX_SHADER = """
#version 330 core

layout(location = 0) in vec3 aPos;
layout(location = 1) in vec3 aColor;

out vec3 vertexColor;

uniform mat4 uModel;
uniform mat4 uView;
uniform mat4 uProjection;

void main()
{
    gl_Position = uProjection * uView * uModel * vec4(aPos, 1.0);
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


def create_window():
    if not glfw.init():
        raise RuntimeError("Não foi possível inicializar o GLFW.")

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    glfw.window_hint(glfw.RESIZABLE, glfw.FALSE)

    if sys.platform == "darwin":
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)

    window = glfw.create_window(
        WIDTH, HEIGHT, "Trabalho 3D - Módulo Pessoa 1", None, None
    )

    if not window:
        glfw.terminate()
        raise RuntimeError("Não foi possível criar a janela.")

    glfw.make_context_current(window)
    return window


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


def create_geometry(vertices):
    vao = glGenVertexArrays(1)
    vbo = glGenBuffers(1)

    glBindVertexArray(vao)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    float_size = np.dtype(np.float32).itemsize
    stride = 6 * float_size

    glVertexAttribPointer(
        0, 3, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(0)
    )
    glEnableVertexAttribArray(0)

    glVertexAttribPointer(
        1, 3, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(3 * float_size)
    )
    glEnableVertexAttribArray(1)

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    return vao, vbo


def draw_text_2d_ndc(text, start_x_px, start_y_px, char_size_px, color, model_loc, view_loc, proj_loc):
    lines = []
    curr_x = start_x_px

    for char in text.upper():
        if char in FONT_5X7:
            for stroke in FONT_5X7[char]:
                px1 = curr_x + stroke[0] * char_size_px
                py1 = start_y_px + stroke[1] * char_size_px
                px2 = curr_x + stroke[2] * char_size_px
                py2 = start_y_px + stroke[3] * char_size_px

                ndc_x1 = (px1 / WIDTH) * 2.0 - 1.0
                ndc_y1 = (py1 / HEIGHT) * 2.0 - 1.0
                ndc_x2 = (px2 / WIDTH) * 2.0 - 1.0
                ndc_y2 = (py2 / HEIGHT) * 2.0 - 1.0

                lines.extend(vertex(ndc_x1, ndc_y1, 0.0, color))
                lines.extend(vertex(ndc_x2, ndc_y2, 0.0, color))
        curr_x += 6 * char_size_px

    if lines:
        glUniformMatrix4fv(model_loc, 1, GL_TRUE, identity_matrix())
        glUniformMatrix4fv(view_loc, 1, GL_TRUE, identity_matrix())
        glUniformMatrix4fv(proj_loc, 1, GL_TRUE, identity_matrix())

        v_data = np.array(lines, dtype=np.float32)
        vao, vbo = create_geometry(v_data)
        glBindVertexArray(vao)
        glDrawArrays(GL_LINES, 0, len(lines) // 6)
        glBindVertexArray(0)
        glDeleteVertexArrays(1, [vao])
        glDeleteBuffers(1, [vbo])


def identity_matrix():
    return np.eye(4, dtype=np.float32)


def translation_matrix(tx, ty, tz):
    return np.array(
        [
            [1.0, 0.0, 0.0, tx],
            [0.0, 1.0, 0.0, ty],
            [0.0, 0.0, 1.0, tz],
            [0.0, 0.0, 0.0, 1.0],
        ],
        dtype=np.float32,
    )


def scale_matrix(sx, sy, sz):
    return np.array(
        [
            [sx, 0.0, 0.0, 0.0],
            [0.0, sy, 0.0, 0.0],
            [0.0, 0.0, sz, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ],
        dtype=np.float32,
    )


def rotation_x_matrix(angle_degress):
    angle = np.radians(angle_degress)
    c, s = np.cos(angle), np.sin(angle)
    return np.array(
        [
            [1.0, 0.0, 0.0, 0.0],
            [0.0, c, -s, 0.0],
            [0.0, s, c, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ],
        dtype=np.float32,
    )


def rotation_y_matrix(angle_degress):
    angle = np.radians(angle_degress)
    c, s = np.cos(angle), np.sin(angle)
    return np.array(
        [
            [c, 0.0, s, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [-s, 0.0, c, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ],
        dtype=np.float32,
    )


def rotation_z_matrix(angle_degress):
    angle = np.radians(angle_degress)
    c, s = np.cos(angle), np.sin(angle)
    return np.array(
        [
            [c, -s, 0.0, 0.0],
            [s, c, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ],
        dtype=np.float32,
    )


def orthographic_matrix(left, right, bottom, top, near, far):
    return np.array(
        [
            [2.0 / (right - left), 0.0, 0.0, -(right + left) / (right - left)],
            [0.0, 2.0 / (top - bottom), 0.0, -(top + bottom) / (top - bottom)],
            [0.0, 0.0, -2.0 / (far - near), -(far + near) / (far - near)],
            [0.0, 0.0, 0.0, 1.0],
        ],
        dtype=np.float32,
    )


def perspective_matrix(fov_degrees, aspect, near, far):
    f = 1.0 / np.tan(np.radians(fov_degrees) / 2.0)
    return np.array(
        [
            [f / aspect, 0.0, 0.0, 0.0],
            [0.0, f, 0.0, 0.0],
            [
                0.0,
                0.0,
                (far + near) / (near - far),
                (2.0 * far * near) / (near - far),
            ],
            [0.0, 0.0, -1.0, 0.0],
        ],
        dtype=np.float32,
    )


def reset_transformations():
    global tx, ty, tz, angle_x, angle_y, angle_z, scale_value, orbit_angle
    global transform_order_mode, pivot_mode, orbit_mode, projection_mode, fov
    global center_of_projection, comparison_mode, comparison_previous_state

    # Transformações do objeto
    tx, ty, tz = 0.0, 0.0, 0.0
    angle_x, angle_y, angle_z = 0.0, 0.0, 0.0
    scale_value = 1.0

    # Modos de transformação
    transform_order_mode = 0
    pivot_mode = 0
    orbit_mode = False
    orbit_angle = 0.0

    # Projeção
    projection_mode = 1
    fov = 60.0

    # Observador / centro de projeção
    center_of_projection[:] = [0.0, 0.0, 3.0]
    
    # Modo de comparação
    comparison_mode = False
    comparison_previous_state = None

# Estrutura para prevenir múltiplos cliques na mesma tecla
key_states = {}


def is_key_just_pressed(window, key):
    current = glfw.get_key(window, key) == glfw.PRESS
    previous = key_states.get(key, False)
    key_states[key] = current
    return current and not previous


def process_input(window):
    global tx, ty, tz, angle_x, angle_y, angle_z, scale_value
    global transform_order_mode, pivot_mode, orbit_mode, projection_mode, fov
    global center_of_projection, comparison_mode, comparison_previous_state

    movement_speed = 0.02
    rotation_speed = 1.0
    scale_speed = 0.01

    if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS:
        glfw.set_window_should_close(window, True)

    # Movimento do observador no eixo X
    # A -> move o observador para a esquerda
    # D -> move o observador para a direita
    observer_speed = 0.02
    if glfw.get_key(window, glfw.KEY_A) == glfw.PRESS:
        center_of_projection[0] -= observer_speed
    if glfw.get_key(window, glfw.KEY_D) == glfw.PRESS:
        center_of_projection[0] += observer_speed
    
    # Translação 3D
    if glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS:
        tx += movement_speed
    if glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS:
        tx -= movement_speed
    if glfw.get_key(window, glfw.KEY_UP) == glfw.PRESS:
        ty += movement_speed
    if glfw.get_key(window, glfw.KEY_DOWN) == glfw.PRESS:
        ty -= movement_speed
    
    # Experimento de profundidade (eixo Z)
    # W aproxima o objeto da câmera e S afasta o objeto.
    if glfw.get_key(window, glfw.KEY_W) == glfw.PRESS:
        tz += movement_speed
    if glfw.get_key(window, glfw.KEY_S) == glfw.PRESS:
        tz -= movement_speed

    # Rotação 3D
    if glfw.get_key(window, glfw.KEY_I) == glfw.PRESS:
        angle_x += rotation_speed
    if glfw.get_key(window, glfw.KEY_K) == glfw.PRESS:
        angle_x -= rotation_speed
    if glfw.get_key(window, glfw.KEY_J) == glfw.PRESS:
        angle_y += rotation_speed
    if glfw.get_key(window, glfw.KEY_L) == glfw.PRESS:
        angle_y -= rotation_speed
    if glfw.get_key(window, glfw.KEY_U) == glfw.PRESS:
        angle_z += rotation_speed
    if glfw.get_key(window, glfw.KEY_O) == glfw.PRESS:
        angle_z -= rotation_speed

    # Escala Uniforme
    if glfw.get_key(window, glfw.KEY_EQUAL) == glfw.PRESS:
        scale_value += scale_speed
    if glfw.get_key(window, glfw.KEY_MINUS) == glfw.PRESS:
        scale_value = max(scale_value - scale_speed, 0.1)

    # FOV da projeção em perspectiva
    # Q -> diminui FOV (visão mais fechada)
    # E -> aumenta FOV (visão mais aberta)
    fov_speed = 0.5
    if glfw.get_key(window, glfw.KEY_Q) == glfw.PRESS:
        fov = max(fov - fov_speed, 20.0)
    if glfw.get_key(window, glfw.KEY_E) == glfw.PRESS:
        fov = min(fov + fov_speed, 120.0)

    # Reset
    if glfw.get_key(window, glfw.KEY_SPACE) == glfw.PRESS:
        reset_transformations()

    # Controles de modo de projeção
    if is_key_just_pressed(window, glfw.KEY_1):
        projection_mode = 1
        print("[Projecao] Paralela")

    if is_key_just_pressed(window, glfw.KEY_2):
        projection_mode = 2
        print("[Projecao] Perspectiva")

    # Controles de modo de comparação
    if is_key_just_pressed(window, glfw.KEY_C):
        if not comparison_mode:
            comparison_previous_state = (
                tx, ty, tz,
                angle_x, angle_y, angle_z,
                scale_value
            )
            comparison_mode = True
            tx, ty, tz = 0.0, 0.0, -2.0
            angle_x, angle_y, angle_z = 0.0, 30.0, 0.0
            scale_value = 1.0
            print("[Comparacao] Ativado: X=0, Y=0, Z=-2, Rotacao Y=30 graus")
            print("[Comparacao] Use 1 para paralela e 2 para perspectiva")
        else:
            # Restaura as transformações que existiam antes da comparação
            if comparison_previous_state is not None:
                (
                    tx, ty, tz,
                    angle_x, angle_y, angle_z,
                    scale_value
                ) = comparison_previous_state
            comparison_mode = False
            comparison_previous_state = None
            print("[Comparacao] Desativado: transformacoes anteriores restauradas")

    # Alternar Ordem de Composição
    if is_key_just_pressed(window, glfw.KEY_3):
        transform_order_mode = 1 - transform_order_mode
        mode_str = "Modo 1 (T * R * S)" if transform_order_mode == 0 else "Modo 2 (R * T * S)"
        print(f"[Ordem Composicao] Alterada para: {mode_str}")

    # Alternar Modo de Pivô
    if is_key_just_pressed(window, glfw.KEY_P):
        pivot_mode = 1 - pivot_mode
        piv_str = "Origem (0,0,0)" if pivot_mode == 0 else "Pivo Externo (1,0,0)"
        print(f"[Modo Pivo] Alterado para: {piv_str}")

    # Alternar Modo de Órbita
    if is_key_just_pressed(window, glfw.KEY_B):
        orbit_mode = not orbit_mode
        print(f"[Modo Orbita] {'Ativado' if orbit_mode else 'Desativado'}")


def main():
    global orbit_angle, fov
    window = create_window()
    program = create_shader_program()

    face_vao, face_vbo = create_geometry(face_vertices)
    edge_vao, edge_vbo = create_geometry(edge_vertices)

    arrow_vao, arrow_vbo = create_geometry(arrow_vertices)
    border_vao, border_vbo = create_geometry(map_border_vertices)
    panel_bg_vao, panel_bg_vbo = create_geometry(panel_bg_vertices)
    panel_border_vao, panel_border_vbo = create_geometry(panel_border_vertices)

    model_location = glGetUniformLocation(program, "uModel")
    view_location = glGetUniformLocation(program, "uView")
    projection_location = glGetUniformLocation(program, "uProjection")

    view = translation_matrix(
        -center_of_projection[0],
        -center_of_projection[1],
        -center_of_projection[2]
    )

    aspect = WIDTH / HEIGHT
    projection_perspective = perspective_matrix(fov, aspect, 0.1, 100.0)
    projection_parallel = orthographic_matrix(-2.5 * aspect, 2.5 * aspect, -2.5, 2.5, -100.0, 100.0)

    glEnable(GL_DEPTH_TEST)
    glLineWidth(2.0)

    print("\\n======================================")
    print("             CONTROLES")
    print("  Setas             -> Translacao X / Y")
    print("  W / S             -> Profundidade Z (aproximar / afastar)")
    print("  I / K             -> Rotacao no eixo X")
    print("  J / L             -> Rotacao no eixo Y")
    print("  U / O             -> Rotacao no eixo Z")
    print("  + / -             -> Aumentar / diminuir escala")
    print("  Q / E             -> Diminuir / aumentar FOV")
    print("  A / D             -> Mover observador no eixo X")
    print("  Espaco            -> Resetar configuracoes")
    print("  1 / 2             -> Projecao paralela / perspectiva")
    print("  C                 -> Ativar/desativar comparacao")
    print("  3                 -> Alternar ordem T*R*S / R*T*S")
    print("  P                 -> Alternar pivo origem / externo")
    print("  B                 -> Ativar/desativar orbita")
    print("  ESC               -> Fechar a aplicacao")
    print("============================================================")
    print("  Na perspectiva, a distancia altera o tamanho aparente")
    print("  Na paralela, a distancia nao altera significativamente o tamanho")
    print("  FOV: 20 graus a 120 graus (somente na perspectiva)")
    print("  Reset completo: objeto, modos, projecao, FOV e observador")
    print("  O minimapa 2D e o painel de informacoes sao atualizados conforme as transformacoes")
    print("============================================================\n")

    while not glfw.window_should_close(window):
        process_input(window)

        view = translation_matrix(
            -center_of_projection[0],
            -center_of_projection[1],
            -center_of_projection[2]
        )

        glClearColor(0.08, 0.08, 0.10, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        T = translation_matrix(tx, ty, tz)
        S = scale_matrix(scale_value, scale_value, scale_value)
        Rx = rotation_x_matrix(angle_x)
        Ry = rotation_y_matrix(angle_y)
        Rz = rotation_z_matrix(angle_z)

        R_combined = Rz @ Ry @ Rx

        if orbit_mode:
            orbit_angle += 0.5
            C = np.array([1.0, 0.0, 0.0])
            T_c = translation_matrix(C[0], C[1], C[2])
            T_minus_c = translation_matrix(-C[0], -C[1], -C[2])
            R_orbit = rotation_y_matrix(orbit_angle)
            model = T_c @ R_orbit @ T_minus_c @ T @ R_combined @ S

        elif pivot_mode == 1:
            C = np.array([1.0, 0.0, 0.0])
            T_c = translation_matrix(C[0], C[1], C[2])
            T_minus_c = translation_matrix(-C[0], -C[1], -C[2])
            model = T @ T_c @ R_combined @ T_minus_c @ S

        else:
            if transform_order_mode == 0:
                model = T @ R_combined @ S
            else:
                model = R_combined @ T @ S

        glUseProgram(program)

        # RENDERIZAÇÃO DA CENA PRINCIPAL 3D
        glViewport(0, 0, WIDTH, HEIGHT)

        projection_perspective = perspective_matrix(fov, aspect, 0.1, 100.0)

        if projection_mode == 1:
            projection = projection_parallel
        else:
            projection = projection_perspective

        glUniformMatrix4fv(model_location, 1, GL_TRUE, model)
        glUniformMatrix4fv(view_location, 1, GL_TRUE, view)
        glUniformMatrix4fv(projection_location, 1, GL_TRUE, projection)

        glEnable(GL_POLYGON_OFFSET_FILL)
        glPolygonOffset(1.0, 1.0)
        glBindVertexArray(face_vao)
        glDrawArrays(GL_TRIANGLES, 0, len(face_vertices) // 6)
        glBindVertexArray(0)
        glDisable(GL_POLYGON_OFFSET_FILL)

        glBindVertexArray(edge_vao)
        glDrawArrays(GL_LINES, 0, len(edge_vertices) // 6)
        glBindVertexArray(0)

        # RENDERIZAÇÃO DA VISUALIZAÇÃO 2D AUXILIAR (MINIMAPA)
        glClear(GL_DEPTH_BUFFER_BIT)
        map_size = 230
        glViewport(10, 10, map_size, map_size)

        map_ortho = orthographic_matrix(-5.0, 5.0, -5.0, 5.0, -1.0, 1.0)
        identity_view = identity_matrix()

        glUniformMatrix4fv(model_location, 1, GL_TRUE, identity_matrix())
        glUniformMatrix4fv(view_location, 1, GL_TRUE, identity_view)
        glUniformMatrix4fv(projection_location, 1, GL_TRUE, map_ortho)

        glBindVertexArray(border_vao)
        glDrawArrays(GL_LINES, 0, len(map_border_vertices) // 6)
        glBindVertexArray(0)

        final_x = model[0, 3]
        final_z = model[2, 3]
        curr_rot_y = angle_y + (orbit_angle if orbit_mode else 0.0)

        T_2d = translation_matrix(final_x, final_z, 0.0)
        R_2d = rotation_z_matrix(-curr_rot_y)
        S_2d = scale_matrix(0.8, 0.8, 1.0)

        model_2d = T_2d @ R_2d @ S_2d

        glUniformMatrix4fv(model_location, 1, GL_TRUE, model_2d)
        glBindVertexArray(arrow_vao)
        glDrawArrays(GL_TRIANGLES, 0, len(arrow_vertices) // 6)
        glBindVertexArray(0)

        # PAINEL LATERAL DE INFORMAÇÕES E CONTROLES ATIVOS
        panel_w = 340
        panel_h = 250

        glViewport(WIDTH - panel_w - 10, 10, panel_w, panel_h)

        panel_ortho = orthographic_matrix(0, panel_w, 0, panel_h, -1.0, 1.0)
        glUniformMatrix4fv(view_location, 1, GL_TRUE, identity_view)
        glUniformMatrix4fv(projection_location, 1, GL_TRUE, panel_ortho)

        bg_model = translation_matrix(panel_w / 2, panel_h / 2, 0.0) @ scale_matrix(panel_w / 2, panel_h / 2, 1.0)
        glUniformMatrix4fv(model_location, 1, GL_TRUE, bg_model)
        glBindVertexArray(panel_bg_vao)
        glDrawArrays(GL_TRIANGLES, 0, 6)
        glBindVertexArray(0)

        border_model = translation_matrix(0.0, panel_h / 2, 0.0) @ scale_matrix(1.0, panel_h / 2, 1.0)
        glUniformMatrix4fv(model_location, 1, GL_TRUE, border_model)
        glBindVertexArray(panel_border_vao)
        glDrawArrays(GL_LINES, 0, 2)
        glBindVertexArray(0)

        # RENDERIZAÇÃO DOS TEXTOS SOBRE O PAINEL
        glViewport(0, 0, WIDTH, HEIGHT)
        glDisable(GL_DEPTH_TEST)

        proj_str = "PARALELA" if projection_mode == 1 else "PERSPECTIVA"
        ordem_str = "T x R x S" if transform_order_mode == 0 else "R x T x S"
        pivo_str = "EXTERNO (1,0,0)" if pivot_mode == 1 else "ORIGEM"

        info_lines = [
            ("INFORMACOES", CYAN),
            (f"PROJECAO: {proj_str}", WHITE),
            (f"FOV: {fov:.1f} GRAUS", WHITE),
            (f"PIVO: {pivo_str}", WHITE),
            (f"ORDEM: {ordem_str}", WHITE),
            (f"OBS X: {center_of_projection[0]:.1f}", WHITE),
            (f"Z OBJETO: {tz:.1f}", WHITE),
            ("------------------------", GRAY),
            ("1/2: PROJECAO", YELLOW),
            ("Q/E: ALTERAR FOV", YELLOW),
            ("P: PIVO | 3: ORDEM", YELLOW),
            ("B: ORBITA | C: COMPARAR", YELLOW),
            ("A/D: OBS X | W/S: Z", YELLOW),
        ]

        start_x = WIDTH - panel_w + 10
        y_pos = 235
        for text_line, color in info_lines:
            draw_text_2d_ndc(
                text_line, start_x, y_pos, 1.5, color,
                model_location, view_location, projection_location
            )
            y_pos -= 17

        glEnable(GL_DEPTH_TEST)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glDeleteVertexArrays(1, [face_vao])
    glDeleteBuffers(1, [face_vbo])
    glDeleteVertexArrays(1, [edge_vao])
    glDeleteBuffers(1, [edge_vbo])
    glDeleteVertexArrays(1, [arrow_vao])
    glDeleteBuffers(1, [arrow_vbo])
    glDeleteVertexArrays(1, [border_vao])
    glDeleteBuffers(1, [border_vbo])
    glDeleteVertexArrays(1, [panel_bg_vao])
    glDeleteBuffers(1, [panel_bg_vbo])
    glDeleteVertexArrays(1, [panel_border_vao])
    glDeleteBuffers(1, [panel_border_vbo])
    glDeleteProgram(program)

    glfw.destroy_window(window)
    glfw.terminate()


if __name__ == "__main__":
    main()