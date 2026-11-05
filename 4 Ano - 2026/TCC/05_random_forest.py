# -*- coding: utf-8 -*-
"""Experimento de classificação de dívida técnica — Random Forest."""

from pathlib import Path
import sys

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
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


# Garante a exibição correta de caracteres acentuados no terminal.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

PASTA = Path(__file__).resolve().parent
ARQUIVOS_CANDIDATOS = [PASTA / "dataset_classificacao.csv"]
PASTA_RESULTADOS = PASTA / "resultados_random_forest"

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

COLUNA_PROJETO = "PROJECT_ID"
COLUNA_ID_ANALISE = "ANALYSIS_KEY"
COLUNA_ALVO = "CLASSE_DIVIDA"

CLASSES = ["Baixa", "Media", "Alta"]
CODIFICACAO_CLASSES = {"Baixa": 0, "Media": 1, "Alta": 2}

SEMENTE_DIVISAO = 7
SEMENTE_MODELO = 27


def carregar_csv():
    """Localiza e carrega o CSV, com ou sem cabeçalho."""
    caminho = next((p for p in ARQUIVOS_CANDIDATOS if p.exists()), None)
    if caminho is None:
        raise FileNotFoundError(
            "CSV não encontrado. Coloque dataset_classificacao.csv na mesma pasta deste script."
        )

    primeira_leitura = pd.read_csv(
        caminho, header=None, low_memory=False, encoding="utf-8-sig"
    )
    primeira_celula = (
        str(primeira_leitura.iloc[0, 0]).strip().upper().replace("\ufeff", "")
    )

    if primeira_celula == "PROJECT_ID":
        dados = pd.read_csv(caminho, low_memory=False, encoding="utf-8-sig")
        dados.columns = [
            str(col).strip().upper().replace("\ufeff", "")
            for col in dados.columns
        ]
    else:
        if primeira_leitura.shape[1] != len(COLUNAS):
            raise ValueError(
                f"O CSV tem {primeira_leitura.shape[1]} colunas, "
                f"mas eram esperadas {len(COLUNAS)}. "
                "Confira se exportou a consulta SQL correta."
            )
        dados = primeira_leitura
        dados.columns = COLUNAS

    dados.columns = [
        str(col).strip().upper().replace("\ufeff", "") for col in dados.columns
    ]

    colunas_ausentes = [col for col in COLUNAS if col not in dados.columns]
    if colunas_ausentes:
        raise ValueError(
            "Faltam colunas esperadas no CSV: " + ", ".join(colunas_ausentes)
        )

    return caminho, dados[COLUNAS].copy()


def salvar_tabela(df, nome, **kwargs):
    """Salva tabelas em formato compatível com planilhas."""
    df.to_csv(
        PASTA_RESULTADOS / nome,
        encoding="utf-8-sig",
        **kwargs,
    )


def main():
    PASTA_RESULTADOS.mkdir(parents=True, exist_ok=True)

    print("=" * 72)
    print("EXPERIMENTO INICIAL: RANDOM FOREST")
    print("=" * 72)

    caminho, df = carregar_csv()
    print(f"Arquivo de entrada: {caminho.name}")
    print(f"\nDimensão inicial: {df.shape[0]:,} linhas x {df.shape[1]} colunas")

    # Padroniza os identificadores e os rótulos.
    df[COLUNA_ALVO] = df[COLUNA_ALVO].astype("string").str.strip()
    df[COLUNA_PROJETO] = df[COLUNA_PROJETO].astype("string").str.strip()
    df[COLUNA_ID_ANALISE] = df[COLUNA_ID_ANALISE].astype("string").str.strip()

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

    print("\n--- DISTRIBUIÇÃO INICIAL DAS CLASSES ---")
    print(df[COLUNA_ALVO].value_counts(dropna=False).to_string())
    salvar_tabela(
        df[COLUNA_ALVO].value_counts(dropna=False)
        .rename("quantidade")
        .to_frame(),
        "distribuicao_classes.csv",
    )

    # Remove registros sem classe ou projeto válido.
    antes = len(df)
    df = df.dropna(subset=[COLUNA_ALVO, COLUNA_PROJETO]).copy()
    df = df[df[COLUNA_ALVO].isin(CODIFICACAO_CLASSES)].copy()
    removidos = antes - len(df)
    print(
        f"\nRegistros removidos por alvo/projeto ausente ou classe inválida: "
        f"{removidos}"
    )

    if df.empty:
        raise ValueError("Não há registros válidos após a limpeza.")

    classes_presentes = set(df[COLUNA_ALVO].unique())
    if classes_presentes != set(CLASSES):
        raise ValueError(
            f"Esperava as classes {CLASSES}, mas encontrei "
            f"{sorted(classes_presentes)}."
        )

    # Define os atributos, a classe-alvo e os grupos de projeto.
    colunas_excluidas = [COLUNA_PROJETO, COLUNA_ID_ANALISE, COLUNA_ALVO]
    X = df.drop(columns=colunas_excluidas)
    y = df[COLUNA_ALVO].map(CODIFICACAO_CLASSES).astype(int)
    grupos = df[COLUNA_PROJETO]

    for coluna in X.columns:
        X[coluna] = pd.to_numeric(X[coluna], errors="coerce")

    conversoes_invalidas = X.isna().sum() - df[X.columns].isna().sum()
    conversoes_invalidas = conversoes_invalidas[conversoes_invalidas > 0]
    if not conversoes_invalidas.empty:
        print("\nValores convertidos para ausentes por não serem numéricos:")
        print(conversoes_invalidas.to_string())

    # Remove atributos totalmente vazios ou constantes.
    colunas_totalmente_vazias = X.columns[X.isna().all()].tolist()
    if colunas_totalmente_vazias:
        print("\nColunas totalmente vazias removidas:", colunas_totalmente_vazias)
        X = X.drop(columns=colunas_totalmente_vazias)

    colunas_constantes = [
        coluna for coluna in X.columns
        if X[coluna].nunique(dropna=True) <= 1
    ]
    if colunas_constantes:
        print("Colunas constantes removidas:", colunas_constantes)
        X = X.drop(columns=colunas_constantes)

    if X.shape[1] == 0:
        raise ValueError("Nenhum atributo de entrada válido permaneceu.")

    print(f"\nAtributos de entrada usados ({X.shape[1]}):")
    print(", ".join(X.columns))
    print("Identificadores removidos dos atributos:", colunas_excluidas)
    print("PROJECT_ID é usado somente para separar os grupos.")

    print("\n--- DISTRIBUIÇÃO DAS CLASSES APÓS LIMPEZA ---")
    print(df[COLUNA_ALVO].value_counts().reindex(CLASSES).to_string())

    # Divide os dados por projeto para evitar sobreposição entre conjuntos.
    separador = GroupShuffleSplit(
        n_splits=1,
        test_size=0.20,
        random_state=SEMENTE_DIVISAO,
    )
    indices_treino, indices_teste = next(
        separador.split(X, y, groups=grupos)
    )

    X_treino = X.iloc[indices_treino].copy()
    X_teste = X.iloc[indices_teste].copy()
    y_treino = y.iloc[indices_treino].copy()
    y_teste = y.iloc[indices_teste].copy()
    grupos_treino = grupos.iloc[indices_treino]
    grupos_teste = grupos.iloc[indices_teste]

    projetos_treino = set(grupos_treino.unique())
    projetos_teste = set(grupos_teste.unique())
    intersecao = projetos_treino.intersection(projetos_teste)

    print("\n--- DIVISÃO TREINO/TESTE POR PROJETO ---")
    print(f"Projetos no treino: {len(projetos_treino)}")
    print(f"Projetos no teste: {len(projetos_teste)}")
    print(f"Registros no treino: {len(X_treino):,}")
    print(f"Registros no teste: {len(X_teste):,}")
    print(f"Percentual de linhas no teste: {100 * len(X_teste) / len(df):.2f}%")
    print("Projetos compartilhados entre treino e teste:", len(intersecao))

    if intersecao:
        raise RuntimeError(
            "Erro: alguns projetos aparecem tanto no treino quanto no teste."
        )

    projetos_df = pd.DataFrame({
        "conjunto": (
            ["treino"] * len(projetos_treino)
            + ["teste"] * len(projetos_teste)
        ),
        "PROJECT_ID": (
            list(sorted(projetos_treino)) + list(sorted(projetos_teste))
        ),
    })
    salvar_tabela(projetos_df, "projetos_por_conjunto.csv", index=False)

    mapa_rotulos = {valor: classe for classe, valor in CODIFICACAO_CLASSES.items()}
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
            "Tente outra SEMENTE ou outra seleção de projetos."
        )
    if set(y_teste.unique()) != {0, 1, 2}:
        raise ValueError(
            "A divisão selecionada não colocou as três classes no teste. "
            "O AUC-ROC multiclasses exige exemplos das três classes. "
            "Tente outra SEMENTE ou outra seleção de projetos."
        )

    # Imputa valores ausentes e configura o Random Forest.
    modelo = Pipeline(steps=[
        ("imputacao", SimpleImputer(strategy="median")),
        (
            "classificador",
            RandomForestClassifier(
                n_estimators=200,
                random_state=SEMENTE_MODELO,
                class_weight="balanced",
                n_jobs=-1,
            ),
        ),
    ])

    print("\nTreinando Random Forest...")
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

    # Calcula as métricas de avaliação.
    nomes_classes_codificados = [CODIFICACAO_CLASSES[classe] for classe in CLASSES]
    matriz = confusion_matrix(
        y_teste,
        previsoes,
        labels=nomes_classes_codificados,
    )
    relatorio = classification_report(
        y_teste,
        previsoes,
        labels=nomes_classes_codificados,
        target_names=CLASSES,
        output_dict=True,
        zero_division=0,
    )

    metricas = {
        "modelo": "Random Forest",
        "acuracia": accuracy_score(y_teste, previsoes),
        "precisao_macro": precision_score(
            y_teste, previsoes, average="macro", zero_division=0
        ),
        "recall_macro": recall_score(
            y_teste, previsoes, average="macro", zero_division=0
        ),
        "f1_macro": f1_score(
            y_teste, previsoes, average="macro", zero_division=0
        ),
        "auc_roc_macro_ovr": auc_roc,
        "registros_treino": len(X_treino),
        "registros_teste": len(X_teste),
        "projetos_treino": len(projetos_treino),
        "projetos_teste": len(projetos_teste),
        "projetos_compartilhados": len(intersecao),
    }

    print("\n" + "=" * 72)
    print("RESULTADOS — RANDOM FOREST")
    print("=" * 72)
    print(f"Acurácia:       {metricas['acuracia']:.4f}")
    print(f"Precisão macro: {metricas['precisao_macro']:.4f}")
    print(f"Recall macro:   {metricas['recall_macro']:.4f}")
    print(f"F1-score macro: {metricas['f1_macro']:.4f}")
    print(f"AUC-ROC macro (OvR): {metricas['auc_roc_macro_ovr']:.4f}")

    print("\nRelatório por classe:")
    print(
        classification_report(
            y_teste,
            previsoes,
            labels=nomes_classes_codificados,
            target_names=CLASSES,
            zero_division=0,
        )
    )

    print("Matriz de confusão (linhas = classe real; colunas = prevista):")
    print(pd.DataFrame(
        matriz,
        index=[f"Real_{classe}" for classe in CLASSES],
        columns=[f"Prevista_{classe}" for classe in CLASSES],
    ).to_string())

    # Salva os resultados do experimento.
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

    # Registra a importância nativa de cada atributo no modelo.
    importancias = pd.DataFrame({
        "metrica": X.columns,
        "importancia": modelo.named_steps["classificador"].feature_importances_,
    }).sort_values("importancia", ascending=False)
    salvar_tabela(importancias, "importancia_atributos.csv", index=False)

    print(f"\nArquivos de resultados salvos em:\n{PASTA_RESULTADOS}")
    print("\nExperimento concluído.")


if __name__ == "__main__":
    try:
        main()
    except Exception as erro:
        print(f"\nERRO: {erro}")
        sys.exit(1)
