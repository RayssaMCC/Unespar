import glfw
from OpenGL.GL import *

def desenhar_casa():
    # casa
    glColor(0.85, 0.55, 0.35)
    glBegin(GL_QUADS)
    glVertex2f(-0.6, -0.45)
    glVertex2f(-0.2, -0.45)
    glVertex2f(-0.2, -0.05)
    glVertex2f(-0.6, -0.05)
    glEnd()

    # porta
    glColor(0.35, 0.2, 0.1)
    glBegin(GL_QUADS)
    glVertex2f(-0.46, -0.45)
    glVertex2f(-0.34, -0.45)
    glVertex2f(-0.34, -0.2)
    glVertex2f(-0.46, -0.2)
    glEnd()

    # telhado
    glColor(0.8, 0.1, 0.1)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.65, -0.05)
    glVertex2f(-0.15, -0.05)
    glVertex2f(-0.4, 0.22)
    glEnd()

def desenhar_chao():
    glColor(0.25, 0.60, 0.25)
    glBegin(GL_QUADS)
    glVertex2f(-1.0, -1.0)
    glVertex2f(1.0, -1.0)
    glVertex2f(1.0, -0.45)
    glVertex2f(-1.0, -0.45)
    glEnd()

def display():
    glClearColor(0.53, 0.81, 0.98, 1.00)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    desenhar_chao()
    desenhar_casa()

def main():
    if not glfw.init():
        raise RuntimeError("Falha ao inicializar o OpenGL")
    
    window = glfw.create_window(900, 700, "Casa OpenGL", None, None)
    if not window:
        glfw.terminate()
        raise RuntimeError("Falha ao criar a janela")
    
    glfw.make_context_current(window)
    glfw.swap_interval(1)

    while not glfw.window_should_close(window):
        display()
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.destroy_window(window)
    glfw.terminate()


if __name__ == "__main__":
    main()

