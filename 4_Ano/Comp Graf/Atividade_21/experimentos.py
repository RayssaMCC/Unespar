"""Executa os seis experimentos quantitativos da Atividade 21."""
import numpy as np
from segmentacao import (criar_cena_inspecao, executar_kmedias,
                         executar_isodata, mascara_por_cor, calcular_iou)

imagem, referencia = criar_cena_inspecao()
print(f"Imagem: {imagem.shape}; pixels de referência: {referencia.sum()}")
for k, seed in [(2, 5), (3, 5), (5, 5), (3, 6)]:
    centros, rotulos = executar_kmedias(imagem, k=k, passos=20, seed=seed)
    mascara = mascara_por_cor(centros, rotulos)
    print(f"K-Médias K={k}, seed={seed}: grupos={len(centros)}, "
          f"pixels={mascara.sum()}, IoU={calcular_iou(mascara, referencia):.6f}")
for seed in [5, 6]:
    centros, rotulos, eventos = executar_isodata(
        imagem, k=2, passos=12, seed=seed, max_grupos=6)
    mascara = mascara_por_cor(centros, rotulos)
    print(f"ISODATA inicial=2, seed={seed}: grupos={len(centros)}, "
          f"pixels={mascara.sum()}, IoU={calcular_iou(mascara, referencia):.6f}, "
          f"eventos={eventos}")
