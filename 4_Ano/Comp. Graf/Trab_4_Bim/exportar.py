"""Exporta todos os paineis (PNG) e os textos de analise (relatorio.txt) sem abrir janela."""
import os, re, struct, zlib
import numpy as np


def salvar_png(caminho, arr):
    arr = np.ascontiguousarray(arr, dtype=np.uint8)
    cor = 0 if arr.ndim == 2 else 2
    h, w = arr.shape[:2]
    bruto = b"".join(b"\x00" + arr[i].tobytes() for i in range(h))

    def chunk(t, d):
        return struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d) & 0xFFFFFFFF)

    dados = (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, cor, 0, 0, 0))
             + chunk(b"IDAT", zlib.compress(bruto)) + chunk(b"IEND", b""))
    with open(caminho, "wb") as f:
        f.write(dados)


def histograma_para_imagem(contagens, alt=140):
    img = np.full((alt, 256 * 2, 3), 255, np.uint8)
    topo = (contagens / max(contagens.max(), 1) * (alt - 1)).astype(int)
    for i, t in enumerate(topo):
        if t > 0:
            img[alt - t:, 2 * i:2 * i + 2] = (40, 80, 160)
    return img


def exportar(cenas, pasta):
    os.makedirs(pasta, exist_ok=True)
    with open(os.path.join(pasta, "relatorio.txt"), "w", encoding="utf-8") as rel:
        for n, c in enumerate(cenas):
            rel.write("=" * 100 + f"\n{c['nome']}\n" + "=" * 100 + "\n")
            for pag in c["paginas"]:
                rel.write("\n".join(pag) + "\n\n")
            for k, p in enumerate(c["paineis"]):
                slug = re.sub(r"[^a-z0-9]+", "_", p["titulo"].lower()).strip("_")[:40]
                im = p["dados"] if p["tipo"] == "img" else histograma_para_imagem(p["dados"])
                salvar_png(os.path.join(pasta, f"modo{n}_{k + 1:02d}_{slug}.png"), im)
                rel.write(f"[painel] {p['titulo']}\n")
            rel.write("\n")
