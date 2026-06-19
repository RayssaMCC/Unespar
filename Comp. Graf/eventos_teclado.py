import glfw
from OpenGL.GL import *

largura = 800
altura = 600
pontos = []
cor = {"r": 1.0, "g": 1.0, "b": 1.0}

def atualizar_viewport(window):
    largura, altura = glfw.get_framebuffer_size(window)
    glViewport(0, 0, largura, altura)

def converter_para_opengl(x_mouse, y_mouse):
    x = (x_mouse/largura) * 2 - 1
    y = 1 - (y_mouse/altura) * 2
    return (x, y)

def mouse_button_callback(window, button, action, mods):        
    if(button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS):
        x_mouse, y_mouse = glfw.get_cursor_pos(window)
        x,y = converter_para_opengl(x_mouse, y_mouse)

        if len(pontos) < 3:
            pontos.append((x,y))

def key_callback(window, key, scancode, action, mods):
    global cor
    if (action == glfw.PRESS or action == glfw.REPEAT):
        # Fechar a janela quando a tecla ESC for pressionada
        if (key == glfw.KEY_ESCAPE):
            glfw.set_window_should_close(window, True)
        
        # Mudar a cor do triângulo usando as teclas R, G e B
        if (key == glfw.KEY_R):
            cor = {"r": 1.0, "g": 0.0, "b": 0.0}
        elif (key == glfw.KEY_G):
            cor = {"r": 0.0, "g": 1.0, "b": 0.0}
        elif (key == glfw.KEY_B):
            cor = {"r": 0.0, "g": 0.0, "b": 1.0}

def desenhar_pontos():
    glPointSize(8)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_POINTS)
    for p in pontos:
        glVertex2f(p[0], p[1])
    glEnd()

def desenhar_triangulo():
    if len(pontos) == 3:
        glColor3f(cor["r"], cor["g"], cor["b"])
        glBegin(GL_TRIANGLES)
        for p in pontos:
            glVertex2f(p[0], p[1])
        glEnd()

def main():
    if not glfw.init(): #inicializar a aplicação
        print("Erro ao inicializar o GLFW")
        return
    
    window = glfw.create_window(largura, altura, "Triângulo com eventos de mouse e teclado", None, None)

    if not window:
        print("Erro ao criar a janela principal.")
        return
    
    glfw.make_context_current(window)
    glfw.set_mouse_button_callback(window, mouse_button_callback)
    glfw.set_key_callback(window, key_callback)

    while not glfw.window_should_close(window):
        atualizar_viewport(window)
        glClear(GL_COLOR_BUFFER_BIT) # limpar a tela para não ter informações duplicadas.

        desenhar_pontos()
        desenhar_triangulo()

        glfw.swap_buffers(window)
        glfw.poll_events() # permite a captura de eventos de teclado e mouse

    glfw.terminate() # finaliza a execução do programa

if __name__ == "__main__":
    main()