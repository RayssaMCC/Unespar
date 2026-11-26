"""Algoritmos das cinco técnicas, implementados apenas com NumPy.

Nenhuma função pronta de cv2/scipy/skimage é usada para zoom, histograma,
esqueletização, convolução ou deformação.
"""
import numpy as np


# ----------------------------------------------------------------- utilitários
def para_cinza(img):
    """RGB -> tons de cinza (luminância Y = 0.299R + 0.587G + 0.114B)."""
    if img.ndim == 2:
        return img.copy()
    g = 0.299 * img[..., 0] + 0.587 * img[..., 1] + 0.114 * img[..., 2]
    return np.clip(np.rint(g), 0, 255).astype(np.uint8)


def para_uint8(x):
    return np.clip(np.rint(x), 0, 255).astype(np.uint8)


# ------------------------------------------------------------------------ ZOOM
def zoom_vizinho_mais_proximo(img, fator):
    """Cada pixel de saída copia o pixel de origem mais próximo (sem criar valores novos)."""
    h, w = img.shape[:2]
    ho, wo = int(round(h * fator)), int(round(w * fator))
    ys = np.minimum((np.arange(ho) / fator).astype(int), h - 1)
    xs = np.minimum((np.arange(wo) / fator).astype(int), w - 1)
    return img[ys[:, None], xs[None, :]]


def zoom_bilinear(img, fator):
    """Cada pixel de saída é a média ponderada dos 4 vizinhos de origem mais próximos."""
    h, w = img.shape[:2]
    ho, wo = int(round(h * fator)), int(round(w * fator))
    # alinhamento pelos centros dos pixels
    y = np.clip((np.arange(ho) + 0.5) / fator - 0.5, 0, h - 1)
    x = np.clip((np.arange(wo) + 0.5) / fator - 0.5, 0, w - 1)
    y0, x0 = np.floor(y).astype(int), np.floor(x).astype(int)
    y1, x1 = np.minimum(y0 + 1, h - 1), np.minimum(x0 + 1, w - 1)
    fy, fx = y - y0, x - x0
    if img.ndim == 3:
        fy, fx = fy[:, None, None], fx[None, :, None]
    else:
        fy, fx = fy[:, None], fx[None, :]
    f = img.astype(float)
    topo = f[y0][:, x0] * (1 - fx) + f[y0][:, x1] * fx
    base = f[y1][:, x0] * (1 - fx) + f[y1][:, x1] * fx
    return para_uint8(topo * (1 - fy) + base * fy)


# ------------------------------------------------------------------- HISTOGRAMA
def histograma(gray):
    """Frequência de cada intensidade 0..255."""
    return np.bincount(gray.ravel(), minlength=256)


def equalizar_histograma(gray):
    """Equalização: T(i) = round((CDF(i)-CDFmin)/(N-CDFmin) * 255)."""
    cdf = np.cumsum(histograma(gray))
    cdf_min = cdf[cdf > 0][0]
    n = gray.size
    lut = np.clip(np.rint((cdf - cdf_min) / max(n - cdf_min, 1) * 255), 0, 255).astype(np.uint8)
    return lut[gray]


def expandir_contraste(gray, p_baixo=2.0, p_alto=98.0):
    """Expansão linear: leva o percentil p_baixo a 0 e o p_alto a 255."""
    cdf = np.cumsum(histograma(gray)) / gray.size * 100
    lo = int(np.searchsorted(cdf, p_baixo))
    hi = int(np.searchsorted(cdf, p_alto))
    hi = max(hi, lo + 1)
    lut = np.clip((np.arange(256) - lo) / (hi - lo) * 255, 0, 255)
    return np.rint(lut).astype(np.uint8)[gray]


# --------------------------------------------------------------- BINARIZAÇÃO
def limiar_otsu(gray):
    """Limiar que maximiza a variância entre classes (método de Otsu)."""
    p = histograma(gray).astype(float)
    p /= p.sum()
    omega = np.cumsum(p)
    mu = np.cumsum(p * np.arange(256))
    with np.errstate(divide="ignore", invalid="ignore"):
        sigma_b = (mu[-1] * omega - mu) ** 2 / (omega * (1 - omega))
    return int(np.argmax(np.nan_to_num(sigma_b)))


def limpar_mascara(mask):
    """Filtro de maioria 3x3: remove pixels isolados (ruído) e fecha pequenos buracos."""
    m = np.pad(mask.astype(np.int16), 1)
    h, w = mask.shape
    s = sum(m[i:i + h, j:j + w] for i in range(3) for j in range(3))
    return s >= 5


# --------------------------------------------------------------- ESQUELETIZAÇÃO
def esqueletizar(binaria):
    """Afinamento iterativo de Zhang-Suen. Retorna (esqueleto bool, nº de iterações)."""
    img = np.pad((binaria > 0).astype(np.int16), 1)
    iteracoes = 0
    mudou = True
    while mudou:
        mudou = False
        for passo in (0, 1):
            P = img
            p2, p3, p4, p5 = P[:-2, 1:-1], P[:-2, 2:], P[1:-1, 2:], P[2:, 2:]
            p6, p7, p8, p9 = P[2:, 1:-1], P[2:, :-2], P[1:-1, :-2], P[:-2, :-2]
            viz = [p2, p3, p4, p5, p6, p7, p8, p9]
            B = sum(viz)                                            # vizinhos pretos->brancos
            A = sum(((viz[i] == 0) & (viz[(i + 1) % 8] == 1)).astype(np.int16) for i in range(8))
            if passo == 0:
                c = (p2 * p4 * p6 == 0) & (p4 * p6 * p8 == 0)
            else:
                c = (p2 * p4 * p8 == 0) & (p2 * p6 * p8 == 0)
            remover = (P[1:-1, 1:-1] == 1) & (B >= 2) & (B <= 6) & (A == 1) & c
            if remover.any():
                img[1:-1, 1:-1][remover] = 0
                mudou = True
        iteracoes += 1
    return img[1:-1, 1:-1].astype(bool), iteracoes


# -------------------------------------------------------------------- CONVOLUÇÃO
def convolucao(img, kernel, borda="edge"):
    """Convolução 2D genérica (kernel espelhado). Aceita imagem cinza ou RGB.
    Retorna float (sem recorte); use para_uint8() para exibir."""
    k = np.asarray(kernel, float)[::-1, ::-1]
    kh, kw = k.shape
    ph, pw = kh // 2, kw // 2
    f = img.astype(float)
    h, w = f.shape[:2]
    pad = ((ph, ph), (pw, pw)) + ((0, 0),) * (f.ndim - 2)
    p = np.pad(f, pad, mode=borda)
    saida = np.zeros_like(f)
    for i in range(kh):
        for j in range(kw):
            saida += k[i, j] * p[i:i + h, j:j + w]
    return saida


def kernel_gaussiano(tamanho=5, sigma=1.0):
    r = tamanho // 2
    yy, xx = np.mgrid[-r:r + 1, -r:r + 1]
    k = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    return k / k.sum()


KERNEL_MEDIA_3 = np.ones((3, 3)) / 9.0
KERNEL_NITIDEZ = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], float)


# -------------------------------------------------------------------- DEFORMAÇÃO
def matriz_afim(shx=0.0, shy=0.0, sx=1.0, sy=1.0, centro=(0.0, 0.0)):
    """Transformação (origem -> destino) = T(c) · Escala · Cisalhamento · T(-c)."""
    cx, cy = centro
    T1 = np.array([[1, 0, cx], [0, 1, cy], [0, 0, 1]], float)
    T2 = np.array([[1, 0, -cx], [0, 1, -cy], [0, 0, 1]], float)
    S = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]], float)
    H = np.array([[1, shx, 0], [shy, 1, 0], [0, 0, 1]], float)
    return T1 @ S @ H @ T2


def amostrar_bilinear(img, sx, sy, borda="constante", fill=0):
    """Lê a imagem de origem nas coordenadas reais (sx, sy).
    Política para coordenadas FORA dos limites:
      'constante' -> usa o valor `fill`;  'clamp' -> repete o pixel da borda."""
    h, w = img.shape[:2]
    dentro = (sx >= 0) & (sx <= w - 1) & (sy >= 0) & (sy <= h - 1)
    x = np.clip(sx, 0, w - 1)
    y = np.clip(sy, 0, h - 1)
    x0, y0 = np.floor(x).astype(int), np.floor(y).astype(int)
    x1, y1 = np.minimum(x0 + 1, w - 1), np.minimum(y0 + 1, h - 1)
    fx, fy = x - x0, y - y0
    if img.ndim == 3:
        fx, fy = fx[..., None], fy[..., None]
    f = img.astype(float)
    out = (f[y0, x0] * (1 - fx) * (1 - fy) + f[y0, x1] * fx * (1 - fy)
           + f[y1, x0] * (1 - fx) * fy + f[y1, x1] * fx * fy)
    if borda == "constante":
        d = dentro[..., None] if img.ndim == 3 else dentro
        out = np.where(d, out, fill)
    return para_uint8(out)


def deformar(img, M, borda="constante", fill=0):
    """Mapeamento INVERSO: para cada pixel do destino calcula-se de onde ele vem na origem.
    A tela de saída é dimensionada para conter a imagem transformada inteira."""
    h, w = img.shape[:2]
    cantos = np.array([[0, w - 1, w - 1, 0], [0, 0, h - 1, h - 1], [1, 1, 1, 1]], float)
    dst = (M @ cantos)[:2]
    xmin, ymin = dst.min(axis=1)
    xmax, ymax = dst.max(axis=1)
    wo, ho = int(np.ceil(xmax - xmin)) + 1, int(np.ceil(ymax - ymin)) + 1
    desloca = np.array([[1, 0, -xmin], [0, 1, -ymin], [0, 0, 1]], float)
    Minv = np.linalg.inv(desloca @ M)
    xs, ys = np.meshgrid(np.arange(wo), np.arange(ho))
    src = Minv @ np.stack([xs.ravel(), ys.ravel(), np.ones(xs.size)])
    return amostrar_bilinear(img, src[0].reshape(ho, wo), src[1].reshape(ho, wo), borda, fill)
