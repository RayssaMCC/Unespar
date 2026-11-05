import glfw
from OpenGL.GL import *

# Lista para armazenar todas as formas desenhadas
formas = []

# Estados iniciais
modo_atual = "T" # Inicia com triângulo por padrão
cor_atual = {"r": 1.0, "g": 1.0, "b": 1.0} # Inicia com branco

def converter_para_opengl(x_mouse, y_mouse, janela):
    largura, altura = glfw.get_window_size(janela)
    x = (x_mouse / largura) * 2 - 1
    y = 1 - (y_mouse / altura) * 2
    return (x, y)

def atualizar_area_visualizacao(janela):
    largura, altura = glfw.get_framebuffer_size(janela)
    glViewport(0, 0, largura, altura)

def evento_mouse(janela, botao, acao, mods):
    global formas, modo_atual, cor_atual
    
    if acao == glfw.PRESS:
        # Clique esquerdo: desenha a forma atual
        if botao == glfw.MOUSE_BUTTON_LEFT:
            x_mouse, y_mouse = glfw.get_cursor_pos(janela)
            x, y = converter_para_opengl(x_mouse, y_mouse, janela)
            
            formas.append({
                "tipo": modo_atual,
                "x": x,
                "y": y,
                "r": cor_atual["r"],
                "g": cor_atual["g"],
                "b": cor_atual["b"]
            })
        
        # Clique direito: limpa a tela
        elif botao == glfw.MOUSE_BUTTON_RIGHT:
            formas.clear()
            print("Tela limpa! (Clique Direito)")

def evento_teclado(janela, tecla, scancode, acao, mods):
    global modo_atual, cor_atual, formas
    
    if acao == glfw.PRESS or acao == glfw.REPEAT:
        # --- TECLAS DE SISTEMA ---
        if tecla == glfw.KEY_ESCAPE:
            glfw.set_window_should_close(janela, True)
        
        elif tecla == glfw.KEY_C: # Limpar a tela
            formas.clear()
            print("Tela limpa! (Tecla C)")
            
        # --- TECLAS DE FORMA ---
        elif tecla == glfw.KEY_P:
            modo_atual = "P"
            print("Forma: PONTO")
        elif tecla == glfw.KEY_L:
            modo_atual = "L"
            print("Forma: LINHA")
        elif tecla == glfw.KEY_T:
            modo_atual = "T"
            print("Forma: TRIANGULO")
        elif tecla == glfw.KEY_Q:
            modo_atual = "Q"
            print("Forma: QUADRADO")
            
        # --- TECLAS DE COR ---
        elif tecla == glfw.KEY_R: # Vermelho
            cor_atual = {"r": 1.0, "g": 0.0, "b": 0.0}
            print("Cor atual: VERMELHO")
        elif tecla == glfw.KEY_G: # Verde 
            cor_atual = {"r": 0.0, "g": 1.0, "b": 0.0}
            print("Cor atual: VERDE")
        elif tecla == glfw.KEY_B: # Azul 
            cor_atual = {"r": 0.0, "g": 0.0, "b": 1.0}
            print("Cor atual: AZUL")
        elif tecla == glfw.KEY_Y: # Amarelo 
            cor_atual = {"r": 1.0, "g": 1.0, "b": 0.0}
            print("Cor atual: AMARELO")
        elif tecla == glfw.KEY_M: # Magenta
            cor_atual = {"r": 1.0, "g": 0.0, "b": 1.0}
            print("Cor atual: MAGENTA")
        elif tecla == glfw.KEY_W: # Branco
            cor_atual = {"r": 1.0, "g": 1.0, "b": 1.0}
            print("Cor atual: BRANCO")

        # --- APLICAR COR À ÚLTIMA FORMA ---
        elif tecla == glfw.KEY_ENTER:
            if len(formas) > 0:
                formas[-1]["r"] = cor_atual["r"]
                formas[-1]["g"] = cor_atual["g"]
                formas[-1]["b"] = cor_atual["b"]
                print("Cor aplicada a ultima forma desenhada!")

        # --- MOVER ÚLTIMA FORMA (SETAS) ---
        passo = 0.05 # velocidade de movimento
        if tecla == glfw.KEY_UP:
            if len(formas) > 0: formas[-1]["y"] += passo
        elif tecla == glfw.KEY_DOWN:
            if len(formas) > 0: formas[-1]["y"] -= passo
        elif tecla == glfw.KEY_LEFT:
            if len(formas) > 0: formas[-1]["x"] -= passo
        elif tecla == glfw.KEY_RIGHT:
            if len(formas) > 0: formas[-1]["x"] += passo

def renderizar_formas():
    tamanho = 0.08
    
    for forma in formas:
        cx, cy = forma["x"], forma["y"]
        
        # Define a cor específica da forma atual no loop
        glColor3f(forma["r"], forma["g"], forma["b"])

        if forma["tipo"] == "P":
            glPointSize(10)
            glBegin(GL_POINTS)
            glVertex2f(cx, cy)
            glEnd()

        elif forma["tipo"] == "L":
            glLineWidth(3)
            glBegin(GL_LINES)
            glVertex2f(cx - tamanho, cy)
            glVertex2f(cx + tamanho, cy)
            glEnd()

        elif forma["tipo"] == "T":
            glBegin(GL_TRIANGLES)
            glVertex2f(cx, cy + tamanho)          
            glVertex2f(cx - tamanho, cy - tamanho) 
            glVertex2f(cx + tamanho, cy - tamanho) 
            glEnd()

        elif forma["tipo"] == "Q":
            glBegin(GL_QUADS)
            glVertex2f(cx - tamanho, cy - tamanho) 
            glVertex2f(cx + tamanho, cy - tamanho) 
            glVertex2f(cx + tamanho, cy + tamanho) 
            glVertex2f(cx - tamanho, cy + tamanho) 
            glEnd()

def main():
    if not glfw.init():
        print("Erro ao inicializar o GLFW.")
        return
    
    janela = glfw.create_window(800, 600, "Mini Editor Grafico", None, None)

    if not janela:
        print("Erro ao criar a janela principal.")
        return

    glfw.make_context_current(janela)
    glfw.set_mouse_button_callback(janela, evento_mouse)
    glfw.set_key_callback(janela, evento_teclado)

    print("=== COMANDOS DO MINI EDITOR ===")
    print("Formas: P (Ponto), L (Linha), T (Triangulo), Q (Quadrado)")
    print("Cores: R (Vermelho), G (Verde), B (Azul), Y (Amarelo), M (Magenta), W (Branco)")
    print("Acoes:")
    print(" - Clique Esquerdo: Desenhar")
    print(" - Clique Direito ou Tecla C: Limpar a tela")
    print(" - Setas Direcionais: Mover a ultima forma")
    print(" - Tecla ENTER: Aplicar cor atual a ultima forma")

    while not glfw.window_should_close(janela):
        atualizar_area_visualizacao(janela)
        glClear(GL_COLOR_BUFFER_BIT)
        
        renderizar_formas()

        glfw.swap_buffers(janela)
        glfw.poll_events()
    
    glfw.terminate()

if __name__ == "__main__":
    main()