# -*- coding: utf-8 -*-
"""
Gera as figuras conjuntas e individuais partir dos CSVs
exportados pelos cinco modelos. 
Execute este arquivo na mesma pasta dos cinco scripts e do dataset.
"""
from pathlib import Path
import warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

PASTA = Path(__file__).resolve().parent
PASTA_GRAFICOS = PASTA / "graficos"
CLASSES = ["Baixa", "Media", "Alta"]

MODELOS = {
    "Regressão Logística": "resultados_regressao_logistica",
    "Árvore de Decisão": "resultados_arvore_decisao",
    "SVM": "resultados_svm",
    "Gradient Boosting": "resultados_gradient_boosting",
    "Random Forest": "resultados_random_forest",
}
CORES = None  # Matplotlib escolhe a paleta padrão.

def ler_csv(modelo, arquivo):
    caminho = PASTA / MODELOS[modelo] / arquivo
    if not caminho.exists():
        raise FileNotFoundError(
            f"Não encontrei {caminho}. Execute primeiro os cinco scripts atualizados."
        )
    return pd.read_csv(caminho, encoding="utf-8-sig", index_col=0 if arquivo in
                       ("matriz_confusao.csv", "relatorio_por_classe.csv",
                        "importancia_atributos.csv") else None)

def salvar_figura(fig, nome):
    fig.tight_layout()
    fig.savefig(PASTA_GRAFICOS / nome, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print("Figura salva:", PASTA_GRAFICOS / nome)

def carregar_metricas():
    partes = []
    for nome, pasta in MODELOS.items():
        arq = PASTA / pasta / "metricas_resumo.csv"
        if not arq.exists():
            raise FileNotFoundError(f"Arquivo ausente: {arq}")
        df = pd.read_csv(arq, encoding="utf-8-sig")
        df["modelo"] = nome
        partes.append(df)
    return pd.concat(partes, ignore_index=True)

def grafico_metricas(metricas):
    colunas = ["acuracia", "precisao_macro", "recall_macro", "f1_macro"]
    rotulos = ["Acurácia", "Precisão (macro)", "Recall (macro)", "F1-score (macro)"]
    x = np.arange(len(metricas))
    largura = 0.19
    fig, ax = plt.subplots(figsize=(12, 6.5))
    for i, (col, rotulo) in enumerate(zip(colunas, rotulos)):
        barras = ax.bar(
            x + (i - 1.5) * largura,
            metricas[col],
            largura,
            label=rotulo,
        )
        # Exibe o valor exato (quatro casas decimais) acima de cada coluna.
        ax.bar_label(
            barras,
            labels=[f"{valor:.4f}" for valor in metricas[col]],
            padding=3,
            fontsize=7,
            rotation=90,
        )
    ax.set_xticks(x)
    ax.set_xticklabels(metricas["modelo"], rotation=15, ha="right")
    ax.set_ylabel("Valor")
    ax.set_ylim(0, 1.16)
    ax.set_title("Comparação das métricas de desempenho dos classificadores")
    ax.grid(axis="y", alpha=0.25)
    ax.legend(ncol=2)
    salvar_figura(fig, "01_comparacao_metricas.png")

def grafico_matrizes():
    fig, axes = plt.subplots(1, 5, figsize=(19, 4.8))
    for ax, (nome, pasta) in zip(axes, MODELOS.items()):
        df = pd.read_csv(PASTA / pasta / "matriz_confusao.csv",
                         encoding="utf-8-sig", index_col=0)
        matriz = df.loc[CLASSES, CLASSES].to_numpy()
        im = ax.imshow(matriz, cmap="Blues")
        ax.set_title(nome, fontsize=10)
        ax.set_xticks(range(3), ["Baixa", "Média", "Alta"], rotation=35, ha="right")
        ax.set_yticks(range(3), ["Baixa", "Média", "Alta"])
        ax.set_xlabel("Prevista")
        if ax is axes[0]:
            ax.set_ylabel("Real")
        limite = matriz.max() * 0.55 if matriz.max() else 0
        for i in range(3):
            for j in range(3):
                ax.text(j, i, f"{matriz[i, j]:,}".replace(",", "."),
                        ha="center", va="center",
                        color="white" if matriz[i, j] > limite else "black",
                        fontsize=8)
    fig.suptitle("Matrizes de confusão dos cinco classificadores", y=1.03)
    salvar_figura(fig, "02_matrizes_confusao.png")

    # Além da figura conjunta, salva uma matriz individual para cada modelo.
    for nome, pasta in MODELOS.items():
        df = pd.read_csv(
            PASTA / pasta / "matriz_confusao.csv",
            encoding="utf-8-sig",
            index_col=0,
        )
        matriz = df.loc[CLASSES, CLASSES].to_numpy()
        fig, ax = plt.subplots(figsize=(7, 5.8))
        im = ax.imshow(matriz, cmap="Blues")
        # Barra lateral que indica a quantidade de registros representada pelas cores de cada célula, como no exemplo enviado.
        cbar = fig.colorbar(im, ax=ax)
        cbar.set_label("Quantidade de registros")
        ax.set_title(f"Matriz de confusão — {nome}")
        ax.set_xticks(range(3), ["Baixa", "Média", "Alta"])
        ax.set_yticks(range(3), ["Baixa", "Média", "Alta"])
        ax.set_xlabel("Classe prevista")
        ax.set_ylabel("Classe real")
        limite = matriz.max() * 0.55 if matriz.max() else 0
        for i in range(3):
            for j in range(3):
                ax.text(
                    j, i, f"{matriz[i, j]:,}".replace(",", "."),
                    ha="center", va="center",
                    color="white" if matriz[i, j] > limite else "black",
                    fontsize=11,
                )
        nome_arquivo = (
            "matriz_confusao_" +
            pasta.replace("resultados_", "") + ".png"
        )
        salvar_figura(fig, nome_arquivo)

def carregar_previsoes():
    dados = {}
    referencia = None
    prob_cols = ["PROB_BAIXA", "PROB_MEDIA", "PROB_ALTA"]
    for nome, pasta in MODELOS.items():
        caminho = PASTA / pasta / "previsoes_teste.csv"
        if not caminho.exists():
            raise FileNotFoundError(f"Arquivo ausente: {caminho}")
        df = pd.read_csv(caminho, encoding="utf-8-sig")
        faltantes = [c for c in ["CLASSE_REAL"] + prob_cols if c not in df.columns]
        if faltantes:
            raise ValueError(
                f"{caminho} não contém {faltantes}. "
                "Execute novamente o script do modelo atualizado."
            )
        if referencia is None:
            referencia = df["CLASSE_REAL"].astype(str).tolist()
        elif referencia != df["CLASSE_REAL"].astype(str).tolist():
            raise ValueError(
                "Os conjuntos de teste/ordem das amostras diferem entre modelos. "
                "Verifique se todos usam a mesma divisão por projeto (SEMENTE_DIVISAO=7)."
            )
        dados[nome] = df
    return dados

def grafico_roc(previsoes):
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    prob_cols = ["PROB_BAIXA", "PROB_MEDIA", "PROB_ALTA"]
    for i, classe in enumerate(CLASSES):
        ax = axes[i]
        for nome, df in previsoes.items():
            y_bin = (df["CLASSE_REAL"].astype(str) == classe).astype(int)
            scores = df[prob_cols[i]].astype(float)
            fpr, tpr, _ = roc_curve(y_bin, scores)
            valor_auc = auc(fpr, tpr)
            ax.plot(fpr, tpr, label=f"{nome} (AUC={valor_auc:.3f})")
        ax.plot([0, 1], [0, 1], linestyle="--", linewidth=1, label="Aleatório")
        ax.set_title(f"Classe {classe}")
        ax.set_xlabel("Taxa de falsos positivos")
        ax.set_ylabel("Taxa de verdadeiros positivos")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1.02)
        ax.grid(alpha=0.25)
    axes[-1].legend(loc="lower right", fontsize=7)
    fig.suptitle("Curvas ROC por classe — abordagem One-vs-Rest", y=1.03)
    salvar_figura(fig, "03_curvas_roc_ovr.png")

    # Também gera uma figura ROC individual para cada classificador, contendo as curvas OvR das três classes.
    nomes_classes = ["Baixa", "Média", "Alta"]
    for nome, df in previsoes.items():
        fig, ax = plt.subplots(figsize=(7, 6))
        for i, classe in enumerate(CLASSES):
            y_bin = (df["CLASSE_REAL"].astype(str) == classe).astype(int)
            scores = df[prob_cols[i]].astype(float)
            fpr, tpr, _ = roc_curve(y_bin, scores)
            valor_auc = auc(fpr, tpr)
            ax.plot(
                fpr, tpr,
                label=f"{nomes_classes[i]} (AUC = {valor_auc:.4f})",
            )
        ax.plot(
            [0, 1], [0, 1],
            linestyle="--", linewidth=1, label="Classificador aleatório",
        )
        ax.set_title(f"Curvas ROC — {nome}")
        ax.set_xlabel("Taxa de falsos positivos")
        ax.set_ylabel("Taxa de verdadeiros positivos")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1.02)
        ax.grid(alpha=0.25)
        ax.legend(loc="lower right")
        pasta = MODELOS[nome].replace("resultados_", "")
        salvar_figura(fig, f"curva_roc_{pasta}.png")

def grafico_f1_por_classe():
    partes = []
    for nome, pasta in MODELOS.items():
        df = pd.read_csv(PASTA / pasta / "relatorio_por_classe.csv",
                         encoding="utf-8-sig", index_col=0)
        df.index = df.index.astype(str).str.strip()
        for classe in CLASSES:
            if classe not in df.index:
                raise ValueError(f"Classe {classe} não encontrada em {pasta}/relatorio_por_classe.csv")
            partes.append({"Modelo": nome, "Classe": classe,
                           "F1-score": float(df.loc[classe, "f1-score"])})
    dados = pd.DataFrame(partes)
    fig, ax = plt.subplots(figsize=(11, 6))
    x = np.arange(len(MODELOS))
    w = 0.24
    for i, classe in enumerate(CLASSES):
        vals = dados[dados["Classe"] == classe]["F1-score"].to_numpy()
        barras = ax.bar(x + (i - 1) * w, vals, w, label=classe)
        # Exibe o valor exato do F1-score acima de cada coluna.
        ax.bar_label(
            barras,
            labels=[f"{valor:.4f}" for valor in vals],
            padding=3,
            fontsize=8,
        )
    ax.set_xticks(x)
    ax.set_xticklabels(list(MODELOS.keys()), rotation=15, ha="right")
    ax.set_ylabel("F1-score")
    ax.set_ylim(0, 1.12)
    ax.set_title("F1-score por classe para cada classificador")
    ax.grid(axis="y", alpha=0.25)
    ax.legend(title="Classe")
    salvar_figura(fig, "04_f1_por_classe.png")

def grafico_importancias():
    fig, axes = plt.subplots(1, 5, figsize=(20, 7))
    for ax, (nome, pasta) in zip(axes, MODELOS.items()):
        df = pd.read_csv(PASTA / pasta / "importancia_atributos.csv",
                         encoding="utf-8-sig")
        if not {"metrica", "importancia"}.issubset(df.columns):
            raise ValueError(f"Formato inesperado em {pasta}/importancia_atributos.csv")
        df = df.sort_values("importancia", ascending=False).head(10).sort_values("importancia")
        ax.barh(df["metrica"], df["importancia"])
        ax.set_title(nome, fontsize=10)
        ax.tick_params(axis="y", labelsize=7)
        ax.grid(axis="x", alpha=0.2)
        if ax is axes[0]:
            ax.set_xlabel("Importância")
    fig.suptitle("Dez atributos mais importantes em cada modelo", y=1.02)
    salvar_figura(fig, "05_importancia_atributos.png")

def main():
    PASTA_GRAFICOS.mkdir(parents=True, exist_ok=True)
    metricas = carregar_metricas()
    # Mantém uma ordem de apresentação consistente.
    metricas["modelo"] = pd.Categorical(metricas["modelo"], categories=list(MODELOS), ordered=True)
    metricas = metricas.sort_values("modelo")
    metricas.to_csv(PASTA_GRAFICOS / "tabela_metricas_consolidadas.csv",
                    index=False, encoding="utf-8-sig")
    grafico_metricas(metricas)
    grafico_matrizes()
    previsoes = carregar_previsoes()
    grafico_roc(previsoes)
    grafico_f1_por_classe()
    grafico_importancias()
    print(f"\nConcluído. Todas as figuras estão em: {PASTA_GRAFICOS}")

if __name__ == "__main__":
    main()
