"""Gera a imagem-base do trabalho diretamente com NumPy (sem arquivo externo).

Objeto: uma "roda" (anel + raios + cubo central) com uma haste diagonal.
- Silhueta bem definida (ótima para binarização e esqueletização);
- Contraste propositalmente BAIXO (fundo ~70-110, objeto ~125-185), com partes
  de tonalidades diferentes (anel, raios, cubo, haste);
- Ruído gaussiano leve e bordas suaves (anti-aliasing) -> a convolução faz diferença.
"""
import numpy as np


def _alpha(sdf):
    """Converte distância com sinal (negativa = dentro) em cobertura 0..1 (borda de 1 px)."""
    return np.clip(0.5 - sdf, 0.0, 1.0)


def _dist_segmento(x, y, ax, ay, bx, by):
    abx, aby = bx - ax, by - ay
    t = np.clip(((x - ax) * abx + (y - ay) * aby) / (abx**2 + aby**2), 0, 1)
    return np.hypot(x - (ax + t * abx), y - (ay + t * aby))


def gerar_imagem_base(n=128, semente=7):
    rng = np.random.default_rng(semente)
    y, x = np.mgrid[0:n, 0:n].astype(float)
    cx, cy = n / 2, n / 2 - 4
    dx, dy = x - cx, y - cy
    r = np.hypot(dx, dy)

    # Fundo: gradiente diagonal suave, levemente azulado, de baixo contraste
    g = 70 + 40 * (x + y) / (2 * (n - 1))
    img = np.stack([0.90 * g, 1.00 * g, 1.10 * g], axis=-1)

    # Partes do objeto: (distância com sinal, cor RGB)
    Ro, Ri = 0.36 * n, 0.26 * n
    w = 0.045 * n
    partes = [
        (np.maximum(r - Ro, Ri - r), (160, 150, 135)),                         # anel
        (np.maximum(np.abs(dx) - (Ri + 2), np.abs(dy) - w), (185, 175, 150)),  # raio horizontal
        (np.maximum(np.abs(dx) - w, np.abs(dy) - (Ri + 2)), (185, 175, 150)),  # raio vertical
        (_dist_segmento(x, y, cx + 0.30 * n * 0.7071, cy + 0.30 * n * 0.7071,
                        cx + 0.48 * n * 0.7071, cy + 0.48 * n * 0.7071) - 0.05 * n,
         (150, 135, 110)),                                                      # haste diagonal
        (r - 0.07 * n, (195, 185, 160)),                                        # cubo central
    ]
    for sdf, cor in partes:
        a = _alpha(sdf)[..., None]
        sombra = 1.0 - 0.12 * (r / r.max())[..., None]  # leve sombreamento radial
        img = img * (1 - a) + a * (np.array(cor, float) * sombra)

    img += rng.normal(0, 4.0, img.shape)  # ruído
    return np.clip(np.rint(img), 0, 255).astype(np.uint8)


if __name__ == "__main__":
    im = gerar_imagem_base()
    print(im.shape, im.dtype, im.min(), im.max())
