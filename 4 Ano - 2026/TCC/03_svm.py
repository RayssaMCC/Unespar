# -*- coding: utf-8 -*-
"""Experimento de classificação de dívida técnica — SVM."""

from pathlib import Path
import sys
import warnings

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.inspection import permutation_importance
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import GroupShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC


# Garante a exibição correta de caracteres acentuados no terminal.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

warnings.filterwarnings("ignore", category=FutureWarning)

PASTA = Path(__file__).resolve().parent
ARQUIVOS_CANDIDATOS = [PASTA / "dataset_classificacao.csv"]
PASTA_RESULTADOS = PASTA / "resultados_svm"

COLUNAS = [
    "PROJECT_ID", "ANALYSIS_KEY", "CLASSE_DIVIDA",
    "COMPLEXITY", "COGNITIVE_COMPLEXITY", "COVERAGE",
    "DUPLICATED_LINES", "DUPLICATED_BLOCKS", "DUPLICATED_LINES_DENSITY",
    "CODE_SMELLS", "VIOLATIONS", "BLOCKER_VIOLATIONS",
    "CRITICAL_VIOLATIONS", "MAJOR_VIOLATIONS", "MINOR_VIOLATIONS",
    "LINES", "NCLOC", "CLASSES", "FUNCTIONS", "FILES", "DIRECTORIES",
    "COMMENT_LINES", "COMMENT_LINES_DENSITY", "AFFERENT_COUPLINGS",
    "EFFERENT_COUPLINGS", "NUMBER_OF_CLASSES_AND_INTERFACES",
    "PACKAGE_DEPENDENCY_CYCLES",
]

CLASSES = ["Baixa", "Media", "Alta"]
CODIFICACAO = {"Baixa": 0, "Media": 1, "Média": 1, "Alta": 2}
COLUNA_ALVO = "CLASSE_DIVIDA"
SEMENTE_DIVISAO = 7
SEMENTE_MODELO = 27


def carregar_csv():
    """Carrega o CSV, com ou sem cabeçalho."""
    caminho = next((p for p in ARQUIVOS_CANDIDATOS if p.exists()), None)
    if caminho is None:
        raise FileNotFoundError(
            "CSV não encontrado. Coloque dataset_classificacao.csv na mesma pasta deste script."
        )

    primeira = pd.read_csv(
        caminho, header=None, low_memory=False, encoding="utf-8-sig"
    )
    primeira_celula = (
        str(primeira.iloc[0, 0]).strip().upper().replace("\ufeff", "")
    )

    if primeira_celula == "PROJECT_ID":
        df = pd.read_csv(caminho, low_memory=False, encoding="utf-8-sig")
        df.columns = [
            str(col).strip().upper().replace("\ufeff", "") for col in df.columns
        ]
    else:
        if primeira.shape[1] != len(COLUNAS):
            raise ValueError(
                f"O CSV possui {primeira.shape[1]} colunas; eram esperadas "
                f"{len(COLUNAS)}. Confira a consulta exportada."
            )
        df = primeira
        df.columns = COLUNAS

    faltantes = [col for col in COLUNAS if col not in df.columns]
    if faltantes:
        raise ValueError("Faltam colunas no CSV: " + ", ".join(faltantes))

    return caminho, df[COLUNAS].copy()


def salvar_tabela(df, nome, **kwargs):
    """Salva tabelas em formato compatível com planilhas."""
    df.to_csv(PASTA_RESULTADOS / nome, encoding="utf-8-sig", **kwargs)


def main():
    PASTA_RESULTADOS.mkdir(parents=True, exist_ok=True)

    print("=" * 72)
    print("EXPERIMENTO INICIAL: SVM (SUPPORT VECTOR MACHINE)")
    print("=" * 72)

    caminho, df = carregar_csv()
    print(f"Arquivo de entrada: {caminho.name}")
    print(f"Dimensão inicial: {df.shape[0]:,} linhas x {df.shape[1]} colunas")

    # Diagnóstico inicial dos dados.
    print("\n--- TIPOS DAS COLUNAS ---")
    print(df.dtypes.to_string())
    salvar_tabela(
        df.dtypes.astype(str).rename("tipo").to_frame(),
        "tipos_colunas.csv",
    )

    ausentes = df.isna().sum().sort_values(ascending=False)
    ausentes = ausentes[ausentes > 0]
    print("\n--- VALORES AUSENTES POR COLUNA ---")
    print(
        ausentes.to_string()
        if not ausentes.empty
        else "Nenhum valor ausente detectado."
    )
    print(f"Total de células ausentes: {int(df.isna().sum().sum()):,}")
    salvar_tabela(
        ausentes.rename("quantidade_ausente").to_frame(),
        "valores_ausentes.csv",
    )

    # Padroniza os rótulos e remove registros inválidos.
    df[COLUNA_ALVO] = (
        df[COLUNA_ALVO].astype("string").str.strip().replace({"Média": "Media"})
    )
    df["PROJECT_ID"] = df["PROJECT_ID"].astype("string").str.strip()
    df["ANALYSIS_KEY"] = df["ANALYSIS_KEY"].astype("string").str.strip()

    print("\n--- DISTRIBUIÇÃO INICIAL DAS CLASSES ---")
    print(df[COLUNA_ALVO].value_counts(dropna=False).to_string())
    salvar_tabela(
        df[COLUNA_ALVO].value_counts(dropna=False)
        .rename("quantidade")
        .to_frame(),
        "distribuicao_classes.csv",
    )

    antes = len(df)
    df = df.dropna(subset=[COLUNA_ALVO, "PROJECT_ID"]).copy()
    df = df[df[COLUNA_ALVO].isin(CLASSES)].copy()
    print(
        "\nRegistros removidos por alvo/projeto ausente ou classe inválida: "
        f"{antes - len(df)}"
    )

    if df.empty:
        raise ValueError("Não há registros válidos após a limpeza.")
    if set(df[COLUNA_ALVO].unique()) != set(CLASSES):
        raise ValueError(
            f"Esperava as classes {CLASSES}, mas encontrei "
            f"{sorted(df[COLUNA_ALVO].unique())}."
        )

    # Separa os identificadores dos atributos de entrada.
    y = df[COLUNA_ALVO].map(CODIFICACAO).astype(int)
    grupos = df["PROJECT_ID"].astype(str)
    X = df.drop(
        columns=["PROJECT_ID", "ANALYSIS_KEY", COLUNA_ALVO]
    ).copy()

    for coluna in X.columns:
        X[coluna] = pd.to_numeric(X[coluna], errors="coerce")

    conversoes_invalidas = X.isna().sum() - df[X.columns].isna().sum()
    conversoes_invalidas = conversoes_invalidas[conversoes_invalidas > 0]
    if not conversoes_invalidas.empty:
        print("\nValores convertidos para ausentes por não serem numéricos:")
        print(conversoes_invalidas.to_string())

    # Remove atributos sem dados ou sem variação.
    vazias = X.columns[X.isna().all()].tolist()
    if vazias:
        print("\nColunas totalmente vazias removidas:", vazias)
        X.drop(columns=vazias, inplace=True)

    constantes = [
        coluna for coluna in X.columns if X[coluna].nunique(dropna=True) <= 1
    ]
    if constantes:
        print("Colunas constantes removidas:", constantes)
        X.drop(columns=constantes, inplace=True)

    if X.empty:
        raise ValueError("Nenhum atributo de entrada válido permaneceu.")

    print(f"\nAtributos de entrada usados ({X.shape[1]}):")
    print(", ".join(X.columns))
    print(
        "Identificadores removidos dos atributos: "
        "PROJECT_ID, ANALYSIS_KEY, CLASSE_DIVIDA"
    )
    print("PROJECT_ID é usado somente para separar os grupos.")
    print("\n--- DISTRIBUIÇÃO DAS CLASSES APÓS LIMPEZA ---")
    print(df[COLUNA_ALVO].value_counts().reindex(CLASSES).to_string())

    # Divide por projeto para evitar sobreposição entre treino e teste.
    splitter = GroupShuffleSplit(
        n_splits=1,
        test_size=0.20,
        random_state=SEMENTE_DIVISAO,
    )
    idx_treino, idx_teste = next(splitter.split(X, y, groups=grupos))

    X_treino = X.iloc[idx_treino].copy()
    X_teste = X.iloc[idx_teste].copy()
    y_treino = y.iloc[idx_treino].copy()
    y_teste = y.iloc[idx_teste].copy()
    grupos_treino = grupos.iloc[idx_treino]
    grupos_teste = grupos.iloc[idx_teste]

    projetos_treino = set(grupos_treino.unique())
    projetos_teste = set(grupos_teste.unique())
    compartilhados = projetos_treino & projetos_teste

    print("\n--- DIVISÃO TREINO/TESTE POR PROJETO ---")
    print(f"Projetos no treino: {len(projetos_treino)}")
    print(f"Projetos no teste: {len(projetos_teste)}")
    print(f"Registros no treino: {len(X_treino):,}")
    print(f"Registros no teste: {len(X_teste):,}")
    print(f"Percentual de linhas no teste: {100 * len(X_teste) / len(df):.2f}%")
    print("Projetos compartilhados entre treino e teste:", len(compartilhados))

    if compartilhados:
        raise RuntimeError("Há projetos compartilhados entre treino e teste.")

    projetos_df = pd.DataFrame({
        "conjunto": (
            ["treino"] * len(projetos_treino)
            + ["teste"] * len(projetos_teste)
        ),
        "PROJECT_ID": sorted(projetos_treino) + sorted(projetos_teste),
    })
    salvar_tabela(projetos_df, "projetos_por_conjunto.csv", index=False)

    mapa_rotulos = {0: "Baixa", 1: "Media", 2: "Alta"}
    distribuicao_split = pd.DataFrame({
        "treino": (
            y_treino.map(mapa_rotulos)
            .value_counts(normalize=True)
            .reindex(CLASSES)
            .mul(100)
        ),
        "teste": (
            y_teste.map(mapa_rotulos)
            .value_counts(normalize=True)
            .reindex(CLASSES)
            .mul(100)
        ),
    }).round(2)

    print("\nPercentual de cada classe por conjunto:")
    print(distribuicao_split.to_string())
    salvar_tabela(
        distribuicao_split,
        "classes_por_conjunto_percentual.csv",
    )

    if set(y_treino.unique()) != {0, 1, 2}:
        raise ValueError(
            "A divisão selecionada não colocou as três classes no treino. "
            "Tente outra SEMENTE_DIVISAO."
        )
    if set(y_teste.unique()) != {0, 1, 2}:
        raise ValueError(
            "A divisão selecionada não colocou as três classes no teste. "
            "O AUC-ROC multiclasses exige exemplos das três classes. "
            "Tente outra SEMENTE_DIVISAO."
        )

    # Imputa valores ausentes, padroniza os atributos e configura o SVM.
    modelo = Pipeline(steps=[
        ("imputacao", SimpleImputer(strategy="median")),
        ("escala", StandardScaler()),
        (
            "classificador",
            SVC(
                kernel="rbf",
                class_weight="balanced",
                probability=True,
                random_state=SEMENTE_MODELO,
            ),
        ),
    ])

    print("\nTreinando SVM...")
    modelo.fit(X_treino, y_treino)
    previsoes = modelo.predict(X_teste)
    probabilidades = modelo.predict_proba(X_teste)

    # Calcula o AUC-ROC multiclasses pelo método One-vs-Rest.
    auc_roc = roc_auc_score(
        y_teste,
        probabilidades,
        labels=[0, 1, 2],
        multi_class="ovr",
        average="macro",
    )

    labels = [0, 1, 2]
    matriz = confusion_matrix(y_teste, previsoes, labels=labels)
    matriz_df = pd.DataFrame(
        matriz,
        index=[f"Real_{classe}" for classe in CLASSES],
        columns=[f"Prevista_{classe}" for classe in CLASSES],
    )
    relatorio = classification_report(
        y_teste,
        previsoes,
        labels=labels,
        target_names=CLASSES,
        output_dict=True,
        zero_division=0,
    )

    acc = accuracy_score(y_teste, previsoes)
    prec = precision_score(y_teste, previsoes, average="macro", zero_division=0)
    rec = recall_score(y_teste, previsoes, average="macro", zero_division=0)
    f1 = f1_score(y_teste, previsoes, average="macro", zero_division=0)

    metricas = {
        "modelo": "SVM (Support Vector Machine)",
        "acuracia": acc,
        "precisao_macro": prec,
        "recall_macro": rec,
        "f1_macro": f1,
        "auc_roc_macro_ovr": auc_roc,
        "registros_treino": len(X_treino),
        "registros_teste": len(X_teste),
        "projetos_treino": len(projetos_treino),
        "projetos_teste": len(projetos_teste),
        "projetos_compartilhados": len(compartilhados),
    }

    print("\n" + "=" * 72)
    print("RESULTADOS — SVM (SUPPORT VECTOR MACHINE)")
    print("=" * 72)
    print(f"Acurácia:       {acc:.4f}")
    print(f"Precisão macro: {prec:.4f}")
    print(f"Recall macro:   {rec:.4f}")
    print(f"F1-score macro: {f1:.4f}")
    print(f"AUC-ROC macro (OvR): {auc_roc:.4f}")
    print("\nRelatório por classe:")
    print(
        classification_report(
            y_teste,
            previsoes,
            labels=labels,
            target_names=CLASSES,
            zero_division=0,
        )
    )
    print("Matriz de confusão (linhas = classe real; colunas = prevista):")
    print(matriz_df.to_string())

    # Salva as métricas, o relatório, a matriz e as previsões.
    salvar_tabela(pd.DataFrame([metricas]), "metricas_resumo.csv", index=False)
    salvar_tabela(pd.DataFrame(relatorio).T, "relatorio_por_classe.csv")
    salvar_tabela(
        pd.DataFrame(matriz, index=CLASSES, columns=CLASSES),
        "matriz_confusao.csv",
    )

    previsoes_df = pd.DataFrame({
        "PROJECT_ID": grupos_teste.to_numpy(),
        "CLASSE_REAL": y_teste.map(mapa_rotulos).to_numpy(),
        "CLASSE_PREVISTA": (
            pd.Series(previsoes, index=y_teste.index)
            .map(mapa_rotulos)
            .to_numpy()
        ),
    }, index=y_teste.index)
    # Probabilidades por classe: necessárias para construir as curvas ROC OvR.
    # O modelo foi treinado com os rótulos codificados 0=Baixa, 1=Media e 2=Alta.
    probabilidades_df = pd.DataFrame(
        probabilidades,
        index=y_teste.index,
        columns=["PROB_BAIXA", "PROB_MEDIA", "PROB_ALTA"],
    )
    previsoes_df = pd.concat([previsoes_df, probabilidades_df], axis=1)
    salvar_tabela(previsoes_df, "previsoes_teste.csv", index=False)

    # Mede a importância dos atributos pela queda do F1 macro após permutação.
    print("\nCalculando importância por permutação (pode demorar)...")
    n_amostra = min(2000, len(X_teste))
    X_amostra = X_teste.iloc[:n_amostra]
    y_amostra = y_teste.iloc[:n_amostra]

    resultado = permutation_importance(
        modelo,
        X_amostra,
        y_amostra,
        scoring="f1_macro",
        n_repeats=3,
        random_state=SEMENTE_MODELO,
        n_jobs=-1,
    )
    importancia = pd.DataFrame({
        "metrica": X.columns,
        "importancia": resultado.importances_mean,
        "desvio_padrao": resultado.importances_std,
        "metodo": "permutation_importance_f1_macro",
    }).sort_values("importancia", ascending=False)
    salvar_tabela(importancia, "importancia_atributos.csv", index=False)

    print(f"\nArquivos de resultados salvos em: {PASTA_RESULTADOS}")
    print("Experimento concluído.")


if __name__ == "__main__":
    try:
        main()
    except Exception as erro:
        print(f"\nERRO: {erro}")
        sys.exit(1)
