"""Monta as 'cenas' (modos) do programa: painéis de imagem/histograma + textos.
Este módulo não depende de OpenGL, então também serve para exportar os resultados em PNG."""
import textwrap
import numpy as np
import processamento as P

LARGURA_TEXTO = 150


def par(txt):
    """Quebra um parágrafo em linhas."""
    return textwrap.wrap(txt, LARGURA_TEXTO)


def img(titulo, dados):
    return {"tipo": "img", "titulo": f"{titulo} ({dados.shape[1]}x{dados.shape[0]})", "dados": dados}


def hist(titulo, gray):
    h = P.histograma(gray)
    return {"tipo": "hist", "titulo": f"{titulo} | media={gray.mean():.1f} dp={gray.std():.1f}", "dados": h}


def rgb(a):
    """cinza/binária -> RGB uint8 para exibição."""
    a = np.asarray(a)
    if a.dtype == bool:
        a = a.astype(np.uint8) * 255
    return np.stack([a] * 3, -1) if a.ndim == 2 else a


def fmt_kernel(nome, k, casas=3):
    return [f"{nome}:"] + ["    " + " ".join(f"{v:8.{casas}f}" for v in lin) for lin in k]


# ----------------------------------------------------------------------------
def cena_original(base):
    g = P.para_cinza(base)
    return dict(
        nome="0) Imagem-base",
        paineis=[img("Imagem-base RGB", base), img("Em tons de cinza", g), hist("Histograma (cinza)", g)],
        paginas=[
            par("Imagem criada com NumPy (imagem_base.py): uma roda (anel + raios + cubo) com haste diagonal, "
                "fundo em gradiente de baixo contraste e ruido gaussiano leve (sigma=4). Todas as demonstracoes "
                "(modos 1 a 5) e a integracao (modo 6) usam exatamente esta imagem.")
            + [""] + par(f"Faixa de cinza: {g.min()} a {g.max()} (a escala completa seria 0 a 255), logo o contraste e baixo. "
                         "Teclas: 1 Zoom | 2 Histograma | 3 Esqueletizacao | 4 Convolucao | 5 Deformacoes | 6 Aplicacao integrada.")
        ])


def cena_zoom(base, fator=2.0):
    nn = P.zoom_vizinho_mais_proximo(base, fator)
    bl = P.zoom_bilinear(base, fator)
    y0, x0, t = 100, 20, 40  # recorte sobre a borda esquerda do anel (coordenadas da imagem ampliada)
    dn, db = nn[y0:y0 + t, x0:x0 + t], bl[y0:y0 + t, x0:x0 + t]
    gn, gb = P.para_cinza(dn), P.para_cinza(db)
    dist_n, dist_b = len(np.unique(gn)), len(np.unique(gb))
    # "degrau" medio entre pixels vizinhos horizontais no recorte
    deg_n = np.abs(np.diff(gn.astype(int), axis=1)).max()
    deg_b = np.abs(np.diff(gb.astype(int), axis=1)).max()
    return dict(
        nome="1) Zoom",
        paineis=[img("Original", base), img(f"Vizinho mais proximo {fator:g}x", nn),
                 img(f"Bilinear {fator:g}x", bl),
                 img("Detalhe 40x40 - vizinho", dn), img("Detalhe 40x40 - bilinear", db)],
        paginas=[
            ["PARAMETROS", f"  Fator de ampliacao = {fator:g}x  ({base.shape[1]}x{base.shape[0]} -> {nn.shape[1]}x{nn.shape[0]})",
             "  Vizinho mais proximo: pixel destino (i,j) copia origem (floor(i/f), floor(j/f)).",
             "  Bilinear: media ponderada dos 4 vizinhos em (i+0.5)/f-0.5, com pesos dados pela parte fracionaria.",
             "  Detalhe: recorte 40x40 na borda esquerda do anel, mostrado ampliado para comparar pixels."],
            ["ANALISE (valores medidos no recorte 40x40, em cinza)",
             f"  Valores de cinza distintos: vizinho = {dist_n}  |  bilinear = {dist_b}",
             f"  Maior salto entre pixels horizontais vizinhos: vizinho = {deg_n}  |  bilinear = {deg_b}",
             ""] + par("O vizinho mais proximo apenas repete valores ja existentes: a borda fica em 'degraus' (blocos "
                       f"{fator:g}x{fator:g}) mas e rapido e nao cria tons novos. A bilinear cria tons intermediarios, "
                       "a transicao fica mais suave (menor salto entre vizinhos), porem as bordas ficam levemente borradas.")
        ])


def cena_histograma(base):
    g = P.para_cinza(base)
    eq = P.equalizar_histograma(g)
    return dict(
        nome="2) Histograma",
        paineis=[img("Original (cinza)", g), hist("Hist. original", g),
                 img("Equalizada", eq), hist("Hist. equalizado", eq)],
        paginas=[
            ["PARAMETROS", "  Conversao para cinza: Y = 0.299R + 0.587G + 0.114B",
             "  Equalizacao: T(i) = round((CDF(i) - CDFmin) / (N - CDFmin) * 255)"],
            ["ANALISE",
             f"  Original : min={g.min()} max={g.max()} media={g.mean():.1f} desvio-padrao={g.std():.1f}",
             f"  Equalizada: min={eq.min()} max={eq.max()} media={eq.mean():.1f} desvio-padrao={eq.std():.1f}",
             f"  Intensidades distintas usadas: {len(np.unique(g))} -> {len(np.unique(eq))}", ""]
            + par("O histograma original ocupa so uma faixa estreita (baixo contraste). A equalizacao espalha as "
                  "intensidades por toda a escala 0-255, aumentando o desvio-padrao e deixando as diferencas entre "
                  "fundo e partes do objeto bem mais visiveis. Como o mapeamento e uma tabela (LUT) monotonica, nao "
                  "surgem tons novos alem dos ja existentes: apenas sao redistribuidos (o histograma fica com 'buracos').")
        ])


def cena_esqueleto(base):
    g = P.para_cinza(base)
    t = P.limiar_otsu(g)
    mask = P.limpar_mascara(g > t)
    esq, it = P.esqueletizar(mask)
    sobre = rgb(mask).copy()
    sobre[esq] = (255, 0, 0)
    return dict(
        nome="3) Esqueletizacao",
        paineis=[img("Cinza", g), img(f"Mascara binaria (Otsu t={t})", rgb(mask)),
                 img("Esqueleto (Zhang-Suen)", rgb(esq)), img("Esqueleto sobre a mascara", sobre)],
        paginas=[
            ["PARAMETROS",
             f"  Criterio de binarizacao: pixel = objeto se cinza > t, com t = {t} escolhido pelo metodo de Otsu",
             "  (maximiza a variancia entre classes). Depois, filtro de maioria 3x3 remove ruido isolado.",
             "  Esqueletizacao: afinamento iterativo de Zhang-Suen (2 sub-iteracoes por passada) ate nao haver mudanca."],
            ["ANALISE",
             f"  Pixels do objeto: {int(mask.sum())}  |  pixels do esqueleto: {int(esq.sum())}  ({esq.sum() / mask.sum() * 100:.1f}% da area)",
             f"  Passadas ate convergir: {it}", ""]
            + par("O esqueleto reduz o objeto a linhas de 1 pixel que preservam a topologia: o anel continua fechado "
                  "(1 buraco interno por quadrante entre os raios) e os raios e a haste viram segmentos ligados ao "
                  "anel. Se a binarizacao falhasse (ruido, buracos), apareceriam ramos extras ou o anel ficaria aberto.")
        ])


def cena_convolucao(base):
    kg, ks = P.kernel_gaussiano(5, 1.0), P.KERNEL_NITIDEZ
    suav = P.para_uint8(P.convolucao(base, kg))
    nit = P.para_uint8(P.convolucao(base, ks))
    fundo = (slice(2, 22), slice(2, 22))  # região de fundo, sem objeto
    ref = lambda a: P.para_cinza(a)[fundo].std()
    return dict(
        nome="4) Convolucao",
        paineis=[img("Original", base), img("Suavizacao gaussiana 5x5", suav),
                 img("Nitidez (3x3)", nit)],
        paginas=[
            ["PARAMETROS (funcao generica convolucao(img, kernel); bordas replicadas)"]
            + fmt_kernel("  Gaussiano 5x5, sigma=1.0 (soma = 1)", kg) + fmt_kernel("  Nitidez (soma = 1)", ks, 0),
            ["ANALISE (desvio-padrao do ruido numa regiao de fundo 20x20)",
             f"  Original = {ref(base):.2f}  |  gaussiano = {ref(suav):.2f}  |  nitidez = {ref(nit):.2f}", ""]
            + par("Gaussiano: todos os pesos positivos, formam uma media ponderada -> reduz variacoes locais (ruido) "
                  "e suaviza bordas. Nitidez: peso central alto (5) e vizinhos negativos (-1): realca a diferenca entre "
                  "o pixel e a vizinhanca, destacando contornos mas tambem amplificando o ruido (desvio-padrao maior).")
        ])


def cena_deformacao(base):
    h, w = base.shape[:2]
    c = ((w - 1) / 2, (h - 1) / 2)
    shx, sx, sy = 0.35, 1.2, 0.8
    M = P.matriz_afim(shx=shx, sx=sx, sy=sy, centro=c)
    d_const = P.deformar(base, M, "constante", 0)
    d_clamp = P.deformar(base, M, "clamp")
    return dict(
        nome="5) Deformacoes",
        paineis=[img("Original", base), img("Deformada - fora = preto", d_const),
                 img("Deformada - fora = borda repetida", d_clamp)],
        paginas=[
            ["PARAMETROS (transformacao afim: cisalhamento horizontal + escala nao uniforme, centrada na imagem)",
             f"  Cisalhamento em x: shx = {shx}  (x' = x + shx*(y - cy))",
             f"  Escala nao uniforme: sx = {sx} (largura), sy = {sy} (altura)",
             "  Matriz origem->destino M (coordenadas homogeneas):"]
            + ["    " + " ".join(f"{v:9.3f}" for v in lin) for lin in M]
            + ["  Mapeamento inverso: para cada pixel destino calcula-se M^-1 * (x,y) e amostra-se a origem com interpolacao bilinear."],
            ["ANALISE", f"  Tamanho: {w}x{h} -> {d_const.shape[1]}x{d_const.shape[0]} (a tela de saida e ajustada para caber a figura inteira)", ""]
            + par("A deformacao muda onde cada pixel esta (geometria), nao a cor do pixel. Apos o cisalhamento, o destino "
                  "tem regioes cujas coordenadas de origem caem fora da imagem. Duas politicas: preencher com cor constante "
                  "(preto, painel central - triangulos visiveis) ou repetir o pixel da borda (painel direito - transicao "
                  "mais discreta, melhor para etapas seguintes como binarizacao).")
        ])


# ----------------------------------------------------------------------------
def executar_pipeline(base):
    """Aplicacao integrada: a saida de cada etapa e a entrada da seguinte."""
    e = {}
    e["cinza"] = P.para_cinza(base)
    k = P.kernel_gaussiano(5, 1.0)
    e["suavizada"] = P.para_uint8(P.convolucao(e["cinza"], k))                        # [1] convolucao
    e["contraste"] = P.expandir_contraste(e["suavizada"], 1, 99)                      # [2] histograma
    h, w = e["contraste"].shape
    M = P.matriz_afim(shx=-0.15, sx=1.0, sy=1.25, centro=((w - 1) / 2, (h - 1) / 2))
    e["deformada"] = P.deformar(e["contraste"], M, "clamp")                           # [3] deformacao
    d = e["deformada"]
    m0 = P.limpar_mascara(d > P.limiar_otsu(d))                                       # ROI automatica
    ys, xs = np.nonzero(m0)
    mg = 6
    y0, y1 = max(ys.min() - mg, 0), min(ys.max() + mg + 1, d.shape[0])
    x0, x1 = max(xs.min() - mg, 0), min(xs.max() + mg + 1, d.shape[1])
    e["roi"] = (y0, y1, x0, x1)
    e["zoom"] = P.zoom_bilinear(d[y0:y1, x0:x1], 2.0)                                 # [4] zoom
    e["limiar"] = P.limiar_otsu(e["zoom"])
    e["binaria"] = P.limpar_mascara(e["zoom"] > e["limiar"])                          # [5] binarizacao
    e["esqueleto"], e["iteracoes"] = P.esqueletizar(e["binaria"])                     # [6] esqueletizacao
    e["matriz"] = M
    sobre = rgb(e["zoom"]).copy()
    sobre[e["esqueleto"]] = (255, 0, 0)
    e["sobreposicao"] = sobre
    return e


def cena_pipeline(base):
    e = executar_pipeline(base)
    g, s, c = e["cinza"], e["suavizada"], e["contraste"]
    y0, y1, x0, x1 = e["roi"]
    paineis = [
        img("Original", base), img("[1] Convolucao (gauss.)", s), hist("Hist. apos [1]", s),
        img("[2] Contraste expandido", c), hist("Hist. apos [2]", c),
        img("[3] Deformacao", e["deformada"]), img("[4] Zoom bilinear 2x na ROI", e["zoom"]),
        img(f"[5] Binarizacao (t={e['limiar']})", rgb(e["binaria"])),
        img("[6] Esqueleto", rgb(e["esqueleto"])), img("Resultado sobre o zoom", e["sobreposicao"]),
    ]
    pag1 = (["OBJETIVO"] + par(
        "Preparar a estrutura (esqueleto) do objeto para analise. A imagem de entrada tem baixo contraste "
        f"(cinza de {g.min()} a {g.max()}), ruido e proporcao inadequada para a analise. O fluxo suaviza o ruido, melhora o "
        "contraste, corrige a proporcao do objeto, amplia a regiao de interesse e extrai um esqueleto de 1 pixel que "
        "resume a topologia (anel, raios e haste). A imagem e adequada porque tem silhueta nitida, partes de tons "
        "diferentes e ruido suficiente para que cada etapa tenha efeito mensuravel."))
    pag2 = ["PARAMETROS E EFEITO DE CADA ETAPA",
            f"  [1] Convolucao: gaussiano 5x5, sigma=1.0 sobre o cinza. Desvio-padrao do fundo (20x20): {g[2:22, 2:22].std():.2f} -> {s[2:22, 2:22].std():.2f}",
            f"  [2] Histograma: expansao linear entre percentis 1% e 99%. Faixa {s.min()}-{s.max()} -> {c.min()}-{c.max()}; desvio-padrao {s.std():.1f} -> {c.std():.1f}",
            f"  [3] Deformacao: cisalhamento shx=-0.15 e escala sx=1.0, sy=1.25; borda 'clamp'. Tamanho {c.shape[1]}x{c.shape[0]} -> {e['deformada'].shape[1]}x{e['deformada'].shape[0]}",
            f"  [4] Zoom: ROI automatica (caixa do objeto + margem 6 px) linhas {y0}-{y1}, colunas {x0}-{x1}; bilinear 2x -> {e['zoom'].shape[1]}x{e['zoom'].shape[0]}",
            f"  [5] Binarizacao: Otsu t={e['limiar']} + filtro de maioria 3x3. Pixels do objeto: {int(e['binaria'].sum())}",
            f"  [6] Esqueletizacao: Zhang-Suen, {e['iteracoes']} passadas, {int(e['esqueleto'].sum())} pixels de esqueleto "
            f"({e['esqueleto'].sum() / e['binaria'].sum() * 100:.1f}% da area)"]
    pag3 = ["JUSTIFICATIVA DA ORDEM"] + par(
        "1) A suavizacao vem primeiro: ruido isolado distorceria o histograma, a escolha de percentis e, no final, o esqueleto "
        "(gerando ramos falsos). 2) O contraste e ajustado depois da suavizacao para que o ruido nao seja amplificado junto; "
        "foi usada expansao linear (e nao equalizacao) porque ela preserva o formato bimodal fundo/objeto, o que torna o "
        "limiar de Otsu confiavel. 3) A deformacao e feita antes do zoom e da binarizacao para que a interpolacao trabalhe "
        "uma unica vez sobre a geometria final, e a borda 'clamp' evita criar regioes pretas que viram uma terceira classe "
        "na binarizacao. 4) O zoom amplia apenas a ROI, dando mais pixels para a espessura das partes finas, o que "
        "melhora o afinamento. 5) A binarizacao e a ultima etapa antes do esqueleto, pois o afinamento exige imagem binaria "
        "e depende de bordas limpas vindas das etapas anteriores.")
    return dict(nome="6) Aplicacao integrada", paineis=paineis, paginas=[pag1, pag2, pag3])


def construir_cenas(base):
    return [cena_original(base), cena_zoom(base), cena_histograma(base), cena_esqueleto(base),
            cena_convolucao(base), cena_deformacao(base), cena_pipeline(base)]
