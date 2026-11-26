import pygame
from pygame.locals import *
from OpenGL.GL import *

def desenhar_casa():
    glClear(GL_COLOR_BUFFER_BIT)

    # Corpo
    glColor3f(0.7, 0.5, 0.3)
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.2)
    glVertex2f(-0.5, 0.2)
    glEnd()

    # Telhado
    glColor3f(0.8, 0.1, 0.1)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.6, 0.2)
    glVertex2f(0.6, 0.2)
    glVertex2f(0.0, 0.7)
    glEnd()

    # Linha do chão
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(-1.0, -0.5)
    glVertex2f(1.0, -0.5)
    glEnd()

    glFlush()


def main():
    pygame.init()
    display = (600, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # 🔥 Substitui gluOrtho2D
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, -1, 1)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        desenhar_casa()
        pygame.display.flip()


if __name__ == "__main__":
    main()