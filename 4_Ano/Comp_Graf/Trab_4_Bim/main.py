"""Trabalho do 4o bimestre - Computacao Grafica.
Visualizacao em OpenGL (PyOpenGL + GLUT) das cinco tecnicas e da aplicacao integrada.

Uso:
    python main.py                 # abre a janela OpenGL
    python main.py --exportar pasta  # (opcional) salva PNGs e relatorio.txt sem abrir janela
"""
import sys
import numpy as np
import imagem_base
import cenas as C
import exportar

# ----------------------------------------------------------------- estado global
LARG, ALT = 1280, 860
BARRA, AJUDA, LINHAS_TEXTO, ALT_LINHA = 28, 20, 11, 16
ALT_TEXTO = LINHAS_TEXTO * ALT_LINHA + 12

CENAS = []
modo = 0          # cena atual
pagina = 0        # pagina de texto atual
foco = None       # None = grade; inteiro = indice do painel em tela cheia
texturas = {}     # id(painel) -> textura OpenGL


def paginar(paginas):
    """Garante no maximo LINHAS_TEXTO linhas por pagina."""
    saida = []
    for p in paginas:
        for i in range(0, len(p), LINHAS_TEXTO):
            saida.append(p[i:i + LINHAS_TEXTO])
    return saida


# --------------------------------------------------------------- desenho (OpenGL)
def importa_gl():
    global GL, GLUT
    import OpenGL.GL as GL
    import OpenGL.GLUT as GLUT


def texto(x, y, s, cor=(1, 1, 1), fonte=None):
    GL.glColor3f(*cor)
    GL.glRasterPos2f(x, y)
    fonte = fonte or GLUT.GLUT_BITMAP_8_BY_13
    for ch in s:
        GLUT.glutBitmapCharacter(fonte, ord(ch) if ord(ch) < 256 else 63)


def retangulo(x, y, w, h, cor):
    GL.glDisable(GL.GL_TEXTURE_2D)
    GL.glColor3f(*cor)
    GL.glBegin(GL.GL_QUADS)
    GL.glVertex2f(x, y); GL.glVertex2f(x + w, y); GL.glVertex2f(x + w, y + h); GL.glVertex2f(x, y + h)
    GL.glEnd()


def textura_do_painel(p):
    chave = id(p)
    if chave not in texturas:
        a = np.ascontiguousarray(p["dados"], dtype=np.uint8)
        if a.ndim == 2:
            a = np.stack([a] * 3, -1)
        tex = GL.glGenTextures(1)
        GL.glBindTexture(GL.GL_TEXTURE_2D, tex)
        GL.glPixelStorei(GL.GL_UNPACK_ALIGNMENT, 1)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_NEAREST)  # pixels visiveis
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_NEAREST)
        GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, GL.GL_RGB, a.shape[1], a.shape[0], 0, GL.GL_RGB,
                        GL.GL_UNSIGNED_BYTE, a.tobytes())
        texturas[chave] = (tex, a.shape[1], a.shape[0])
    return texturas[chave]


def desenha_imagem(p, x, y, w, h):
    tex, iw, ih = textura_do_painel(p)
    s = min(w / iw, h / ih)
    dw, dh = iw * s, ih * s
    x0, y0 = x + (w - dw) / 2, y + (h - dh) / 2
    GL.glEnable(GL.GL_TEXTURE_2D)
    GL.glBindTexture(GL.GL_TEXTURE_2D, tex)
    GL.glColor3f(1, 1, 1)
    GL.glBegin(GL.GL_QUADS)  # eixo y para baixo: linha 0 da imagem fica no topo
    GL.glTexCoord2f(0, 0); GL.glVertex2f(x0, y0)
    GL.glTexCoord2f(1, 0); GL.glVertex2f(x0 + dw, y0)
    GL.glTexCoord2f(1, 1); GL.glVertex2f(x0 + dw, y0 + dh)
    GL.glTexCoord2f(0, 1); GL.glVertex2f(x0, y0 + dh)
    GL.glEnd()
    GL.glDisable(GL.GL_TEXTURE_2D)


def desenha_histograma(p, x, y, w, h):
    cont = p["dados"].astype(float)
    mx = max(cont.max(), 1)
    ml, mb = 8, 18
    gx, gy, gw, gh = x + ml, y + 4, w - 2 * ml, h - mb - 4
    retangulo(gx, gy, gw, gh, (0.12, 0.12, 0.15))
    bw = gw / 256.0
    GL.glColor3f(0.35, 0.65, 1.0)
    GL.glBegin(GL.GL_QUADS)
    for i, c in enumerate(cont):
        if c > 0:
            bh = c / mx * gh
            xi = gx + i * bw
            GL.glVertex2f(xi, gy + gh); GL.glVertex2f(xi + bw, gy + gh)
            GL.glVertex2f(xi + bw, gy + gh - bh); GL.glVertex2f(xi, gy + gh - bh)
    GL.glEnd()
    for v in (0, 64, 128, 192, 255):
        texto(gx + v * bw - (8 if v == 255 else 0), gy + gh + 14, str(v), (0.8, 0.8, 0.8))


def desenha_painel(p, x, y, w, h):
    retangulo(x + 2, y + 2, w - 4, h - 4, (0.09, 0.09, 0.11))
    texto(x + 8, y + 16, p["titulo"][:max(10, int(w / 8) - 1)], (1, 0.9, 0.4))
    cx, cy, cw, ch = x + 6, y + 24, w - 12, h - 30
    if p["tipo"] == "img":
        desenha_imagem(p, cx, cy, cw, ch)
    else:
        desenha_histograma(p, cx, cy, cw, ch)


def display():
    GL.glClearColor(0.05, 0.05, 0.07, 1)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)
    cena = CENAS[modo]
    paineis = cena["paineis"]

    # barra superior
    paginas = cena["paginas"]
    texto(8, 19, f"{cena['nome']}   |   texto {pagina + 1}/{len(paginas)}"
                 + (f"   |   painel em foco {foco + 1}/{len(paineis)}" if foco is not None else "   |   grade"),
          (0.6, 1, 0.6), GLUT.GLUT_BITMAP_HELVETICA_18)

    # area dos paineis
    ay, ah = BARRA, ALT - BARRA - ALT_TEXTO - AJUDA
    if foco is None:
        n = len(paineis)
        cols = n if n <= 4 else (n + 1) // 2
        rows = (n + cols - 1) // cols
        cw, chh = LARG / cols, ah / rows
        for i, p in enumerate(paineis):
            desenha_painel(p, (i % cols) * cw, ay + (i // cols) * chh, cw, chh)
    else:
        desenha_painel(paineis[foco], 0, ay, LARG, ah)

    # area de texto
    ty = ALT - ALT_TEXTO - AJUDA
    retangulo(0, ty, LARG, ALT_TEXTO, (0.14, 0.14, 0.18))
    for i, linha in enumerate(paginas[pagina]):
        cor = (1, 0.9, 0.4) if linha.isupper() or linha[:8].isupper() else (0.92, 0.92, 0.92)
        texto(10, ty + 16 + i * ALT_LINHA, linha, cor)

    # ajuda
    texto(8, ALT - 6, "0 imagem | 1 zoom | 2 histograma | 3 esqueleto | 4 convolucao | 5 deformacao | 6 integrada"
                      " | setas <- -> foco | G grade | T pagina de texto | ESC sair", (0.7, 0.7, 0.7))
    GLUT.glutSwapBuffers()


def reshape(w, h):
    global LARG, ALT
    LARG, ALT = max(w, 1), max(h, 1)
    GL.glViewport(0, 0, LARG, ALT)
    GL.glMatrixMode(GL.GL_PROJECTION)
    GL.glLoadIdentity()
    GL.glOrtho(0, LARG, ALT, 0, -1, 1)   # origem no canto superior esquerdo
    GL.glMatrixMode(GL.GL_MODELVIEW)
    GL.glLoadIdentity()


def teclado(tecla, x, y):
    global modo, pagina, foco
    t = tecla.decode("latin-1").lower() if isinstance(tecla, bytes) else tecla
    if t in ("\x1b", "q"):
        GLUT.glutLeaveMainLoop() if bool(GLUT.glutLeaveMainLoop) else sys.exit(0)
    elif t.isdigit() and int(t) < len(CENAS):
        modo, pagina, foco = int(t), 0, None
    elif t == "t":
        pagina = (pagina + 1) % len(CENAS[modo]["paginas"])
    elif t == "g":
        foco = None
    GLUT.glutPostRedisplay()


def especiais(tecla, x, y):
    global foco
    n = len(CENAS[modo]["paineis"])
    if tecla == GLUT.GLUT_KEY_RIGHT:
        foco = 0 if foco is None else (foco + 1) % n
    elif tecla == GLUT.GLUT_KEY_LEFT:
        foco = n - 1 if foco is None else (foco - 1) % n
    GLUT.glutPostRedisplay()


def carregar_cenas():
    global CENAS
    base = imagem_base.gerar_imagem_base()
    CENAS = C.construir_cenas(base)
    for c in CENAS:
        c["paginas"] = paginar(c["paginas"])
    return CENAS


def main():
    if "--exportar" in sys.argv:
        i = sys.argv.index("--exportar")
        pasta = sys.argv[i + 1] if i + 1 < len(sys.argv) else "saida"
        exportar.exportar(carregar_cenas(), pasta)
        print(f"PNGs e relatorio.txt salvos em '{pasta}/'")
        return
    importa_gl()
    carregar_cenas()
    GLUT.glutInit()
    GLUT.glutInitDisplayMode(GLUT.GLUT_DOUBLE | GLUT.GLUT_RGB)
    GLUT.glutInitWindowSize(LARG, ALT)
    GLUT.glutCreateWindow(b"CG - Zoom, Histograma, Esqueletizacao, Convolucao e Deformacoes")
    GLUT.glutDisplayFunc(display)
    GLUT.glutReshapeFunc(reshape)
    GLUT.glutKeyboardFunc(teclado)
    GLUT.glutSpecialFunc(especiais)
    GLUT.glutMainLoop()


if __name__ == "__main__":
    main()
