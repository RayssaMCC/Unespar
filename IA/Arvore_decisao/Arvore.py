import pandas as pd
import numpy as np
from scipy.stats import entropy
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# ---------- DIVISÃO DO DATASET EM CONJUNTOS DE TREINO E TESTE -----------
try:
    df_categorizado = pd.read_excel(r'')  # Insira o caminho do arquivo aqui
except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado, verifique o nome e caminho do arquivo.")
    df_categorizado = pd.DataFrame() # df vazio para o resto do código não quebrar

if not df_categorizado.empty:
    x = df_categorizado.drop('Outcome', axis=1) # x são todas as colunas, exceto 'Outcome'
    y = df_categorizado['Outcome'] # y é apenas a coluna 'Outcome'

    # test_size= 0.3 define que o conjunto de teste terá 30% dos dados
    # random_state = 42 garante que a divisão seja sempre a mesma em todas as execuções, tornando seus resultados reprodutíveis.
    # stratify = y garante que a proporção de classes em 'Outcome' seja mantida nos conjuntos de treino e teste, evitando viés na distribuição das classes.
    # stratify não é necessário pois a diferença é baixa, mas foi mantido por "boas práticas"
    x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.3, random_state = 42, stratify = y) 

    print("Formato do conjunto de treino (dados/colunas):", x_treino.shape)
    print("Formato do conjunto de teste (dados/colunas):", x_teste.shape)
    # proporção de cada classe nos conjuntos para mostrar precisão na divisão dos dados e garantir que não há viés
    print("\nDistribuição do 'Outcome' no conjunto de treino (%):")
    print(y_treino.value_counts(normalize=True).to_string()) # to_string apenas para remover a linha de metadados do pandas
    print("\nDistribuição do 'Outcome' no conjunto de teste (%):")
    print(y_teste.value_counts(normalize=True).to_string())


# ---------- FUNÇÕES DE CÁLCULO DE ENTROPIA E GANHO DE INFORMAÇÃO -----------
def entropia(coluna): # calcula a entropia de um atributo
    proporcoes = coluna.value_counts(normalize=True) # calcula as frequências e normaliza para proporções.
    entropia_resultado = entropy(proporcoes, base=2) # calcula a entropia, base = 2 por causa do log.
    return entropia_resultado

def gini(coluna):
    proporcoes = coluna.value_counts(normalize=True) # conta as repetições de cada valor e normaliza.
    gini_resultado = 1 - sum(proporcoes ** 2) # aplica a fórmula do Gini
    return gini_resultado

def information_gain(df, atributo):
    entropia_conjunto = entropia(df['Outcome']) # cálculo da entropia do conjunto classificador
    valores, contagens = np.unique(df[atributo], return_counts=True) # unique retorna todos os valores únicos da coluna escolhida e quantas vezes ele aparece na variavel de contagem
    entropia_atributo = 0 # inicia a variável que ira acumular a entropia poderada do atributo

    for i in range(len(valores)):
        sub_conjunto = df[df[atributo] == valores[i]] # filtra para um valor especifico do vetor valores
        peso = contagens[i] / len(df) # calcula a proporção
        entropia_atributo += peso * entropia(sub_conjunto['Outcome']) # calcula a entropia desse conjunto com base nos valores da coluna usada como base Outcome

    IG = entropia_conjunto - entropia_atributo # fórmula do IG
    return IG # retorna o valor obtido

def gain_ratio(df, classe):
    IG_classe = information_gain(df, atributo = classe) # calculando o IG do da classe, como na fórmula
    proporcoes = df[classe].value_counts(normalize = True) # retorna as proporções de cada valor único
    entropia = entropy(proporcoes, base=2) # calculando a entropia de distribuição dos valores
    if entropia == 0: # evitar divisões por 0
        return 0

    GR = IG_classe / entropia # aplica a fórmula em si
    return GR # retorna o valor obtido

# ---------- FUNÇÕES PARA SELEÇÃO DO MELHOR ATRIBUTO -----------
def gini_ponderado(df, atributo): # calcula impureza de Gini ponderada para um atributo específico, quanto menor o valor, melhor o atributo para a divisão (criação da regra)
    total_amostras = len(df)
    gini_total = 0
    valores_unicos = df[atributo].unique()
    
    for valor in valores_unicos:
        sub_conjunto = df[df[atributo] == valor] # filtra o dataframe para pegar apenas as linhas com o valor atual do atributo
        peso = len(sub_conjunto) / total_amostras # calcula o peso do sub-conjunto em relação ao total
        gini_sub_conjunto = gini(sub_conjunto['Outcome']) # calcula o Gini do sub-conjunto
        gini_total += peso * gini_sub_conjunto # acumula o Gini ponderado
        
    return gini_total

def encontrar_melhor_atributo(df, criterio): # encontra o melhor atributo para dividir o dataframe, sempre buscando a maior pontuação.
    
    atributos = df.columns.drop('Outcome') # pega todos os atributos, exceto 'Outcome'
    melhor_atributo = None
    maior_pontuacao = -1

    for atributo in atributos:
        # calcula a "pontuação" do atributo de acordo com o critério escolhido
        if criterio == 'gini': # pro Gini, maximiza 1 - impureza_ponderada
            pontuacao_atual = 1 - gini_ponderado(df, atributo)
        elif criterio == 'gain_ratio':
            pontuacao_atual = gain_ratio(df, atributo)
        else: # padrão será 'information_gain'
            pontuacao_atual = information_gain(df, atributo)
        
        # se a pontuação desse atributo for a melhor que já vimos, guardamos ele
        if pontuacao_atual > maior_pontuacao:
            maior_pontuacao = pontuacao_atual
            melhor_atributo = atributo
            
    return melhor_atributo

# ---------- FUNÇÃO PARA CRIAR A ÁRVORE DE DECISÃO -----------
def construir_arvore(df, criterio):

    # ---- CONDIÇÕES DE PARADA ----
    # Se todos os exemplos no dataframe pertencem à mesma classe (nó puro), retorna essa classe
    if len(np.unique(df['Outcome'])) <= 1:
        return int(np.unique(df['Outcome'])[0])
    # Se não há mais atributos para dividir, retorna a classe mais comum
    elif len(df.columns) == 1:
        return int(df['Outcome'].mode()[0])

    # ---- PASSO RECURSIVO ----
    else:
        melhor_atributo = encontrar_melhor_atributo(df, criterio) # Encontra o melhor atributo para dividir os dados atuais, retorna o nome dele

        # Se não for possível encontrar um bom atributo, retorna a classe mais comum, evitando erros onde todos os atributos tem ganho 0)
        if melhor_atributo is None:
            return int(df['Outcome'].mode()[0])

        arvore = {melhor_atributo: {}} # Cria a estrutura do nó da árvore como um dicionário, a chave do dicionário é o melhor atributo encontrado

        # Itera sobre cada valor único do melhor atributo para criar os galhos
        for valor in np.unique(df[melhor_atributo]):
            sub_df = df[df[melhor_atributo] == valor] # filtra o dataframe para pegar apenas as linhas com o valor atual do atributo
            sub_df = sub_df.drop(columns=[melhor_atributo]) # remove o atributo usado para dividir, pois não precisa mais dele na subárvore
            # Chama a função recursivamente e adiciona o resultado ao galho
            sub_arvore = construir_arvore(sub_df, criterio)
            arvore[melhor_atributo][valor] = sub_arvore
            
        return arvore

# ---------- FUNÇÕES DE PREVISÃO, AVALIAÇÃO E VISUALIZAÇÃO -----------
def prever_amostra(amostra, arvore):
    # Se o nó atual não for um dicionário, significa que chegamos a uma folha (previsão)
    if not isinstance(arvore, dict):
        return arvore

    atributo_raiz = next(iter(arvore)) # Pega o nome do atributo no nó atual
    galhos = arvore[atributo_raiz] # Pega os valores do atributo raiz
    valor_amostra = amostra.get(atributo_raiz) # Obtém o valor desse atributo na amostra de teste

    # Se o valor da amostra existe nos galhos da árvore (visto durante o treino), continue navegando
    if valor_amostra in galhos:
        return prever_amostra(amostra, galhos[valor_amostra])
    # Fallback: Se o valor não foi visto no treino, retorna a previsão da primeira folha que encontrar
    else:
        # Pega o primeiro galho disponível e retorna sua folha
        primeiro_galho = next(iter(galhos.values()))
        return prever_amostra(amostra, primeiro_galho)


def avaliar_modelo(arvore, x_dados, y_verdadeiro):
    y_previsto = x_dados.apply(prever_amostra, axis=1, args=(arvore,)) # Gera previsões para cada linha no dataframe x_dados

    # Calcula as métricas
    acuracia = accuracy_score(y_verdadeiro, y_previsto)
    precisao = precision_score(y_verdadeiro, y_previsto, zero_division=0)
    recall = recall_score(y_verdadeiro, y_previsto, zero_division=0)
    f1 = f1_score(y_verdadeiro, y_previsto, zero_division=0)
    matriz = confusion_matrix(y_verdadeiro, y_previsto)

    print(f"Acurácia: {acuracia:.4f}")
    print(f"Precisão: {precisao:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1-Score: {f1:.4f}")
    print("Matriz de Confusão:")
    print(matriz)

# ---------- IMPRESSÃO DA ÁRVORE -----------
def imprimir_arvore(arvore, nivel = 0):
    if isinstance(arvore, dict):
        # Pega o atributo raiz do nó atual
        for atributo, galhos in arvore.items():
            print("  " * nivel + f"[{atributo}]")
            # Para cada galho (valor do atributo), imprime e continua recursivamente
            for valor, sub_arvore in galhos.items():
                print("  " * (nivel + 1) + f"↳ {valor}:")
                imprimir_arvore(sub_arvore, nivel + 2)
    else:
        # Se não for um dicionário, é uma folha (classe)
        print("  " * nivel + f"→ Classe/Outcome: {arvore}")

# ---------- TREINAMENTO, VISUALIZAÇÃO E ANÁLISE DOS RESULTADOS -----------
if not df_categorizado.empty:
    df_treino = pd.concat([x_treino, y_treino], axis=1) # concatena x_treino e y_treino para formar o dataframe de treino

     # --- Árvore com Gini ---
    print("=" * 25)
    arvore_gini = construir_arvore(df_treino.copy(), criterio = 'gini')
    print("Árvore (Gini) construída.\n")
    print("--- ESTRUTURA DA ÁRVORE (Gini) ---")
    imprimir_arvore(arvore_gini)
    print("-" * 45)
    print("\nResultados para: Gini")
    print("--- CONJUNTO DE TREINO ---")
    avaliar_modelo(arvore_gini, x_treino, y_treino)
    print("\n--- CONJUNTO DE TESTE ---")
    avaliar_modelo(arvore_gini, x_teste, y_teste)
    print("=" * 25, "\n")

    # --- Árvore com Gain Ratio ---
    print("=" * 25)
    arvore_gr = construir_arvore(df_treino.copy(), criterio = 'gain_ratio')
    print("Árvore (Gain Ratio) construída.\n")
    print("--- ESTRUTURA DA ÁRVORE (Gain Ratio) ---")
    #imprimir_arvore(arvore_gr)
    print("-" * 45)
    print("\nResultados para: Gain Ratio")
    print("--- CONJUNTO DE TREINO ---")
    avaliar_modelo(arvore_gr, x_treino, y_treino)
    print("\n--- CONJUNTO DE TESTE ---")
    avaliar_modelo(arvore_gr, x_teste, y_teste)
    print("=" * 25, "\n")

   # --- Árvore com Information Gain ---
    print("=" * 25)
    arvore_ig = construir_arvore(df_treino.copy(), criterio = 'information_gain')
    print("Árvore (Information Gain) construída.\n")
    print("--- ESTRUTURA DA ÁRVORE (Information Gain) ---")
    #imprimir_arvore(arvore_ig)
    print("-" * 45)
    print("\nResultados para: Information Gain")
    print("--- CONJUNTO DE TREINO ---")
    avaliar_modelo(arvore_ig, x_treino, y_treino)
    print("\n--- CONJUNTO DE TESTE ---")
    avaliar_modelo(arvore_ig, x_teste, y_teste)
    print("=" * 25, "\n")