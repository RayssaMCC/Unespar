from geopy.distance import geodesic  # Biblioteca para cálculo de distância geográfica
import random
import math
import time

# Calcula a distância geográfica entre duas cidades usando latitude e longitude
def calcular_distancia_total(populacao, distancias):
    for i in range(len(populacao)):
        distancia_total = 0.0
        individuo = populacao[i][0]
        for j in range(1, len(individuo)):
            cidade_partida = individuo[j - 1] - 1  # Índice da cidade de partida
            cidade_destino = individuo[j] - 1     # Índice da cidade de destino
            distancia = distancias[cidade_partida][cidade_destino]
            distancia_total += distancia

        # Volta para a cidade inicial (fecha o ciclo)
        distancia_total += distancias[individuo[-1] - 1][individuo[0] - 1]
        populacao[i][1] = distancia_total
        populacao[i][2] = calcular_fitness(distancia_total)
    return populacao

# Calcula o fitness (aptidão), onde menor distância gera maior fitness
def calcular_fitness(distancia):
    return 1 / distancia

# Ordena a população com base no fitness (em ordem decrescente)
def ordenar_populacao(populacao):
    populacao.sort(key=lambda x: x[2], reverse=True)
    return populacao

# Verifica se o novo indivíduo já existe na nova população antes de adicioná-lo
# Se o percurso já existir, não adiciona o novo indivíduo
def conferir_duplicidade(novo_individuo, nova_pop):
    percursos = [ind[0] for ind in nova_pop]
    if novo_individuo[0] not in percursos:
        nova_pop.append(novo_individuo)
    return nova_pop

# Lê o arquivo .tsp e extrai os dados das cidades (número, latitude, longitude)
def ler_arquivo(arquivo):
    cidades = []
    lendo = False
    with open(arquivo, 'r') as f: # Permite abrir o arquivo 'r' somente para leitura e f é uma variável que referencia esse arquivo
        for linha in f: # A cada interação a variável linha irá conter uma linha do arquivo
            linha = linha.strip()

            # Lê todas as informações do arquivo até encontrar o que indica a inicialização das coordenadas
            if linha == "NODE_COORD_SECTION" or linha == "DISPLAY_DATA_SECTION":
                lendo = True
                continue # Pula a linha que contém o NODE_COORD_SECTION
            if lendo:
                if linha == "EOF": # Fim do arquivo
                    break
                partes = linha.split() # Divide a string toda vez que encontra um espaço em branco, no caso '\n' ou o espaço
                cidade = int(partes[0])
                latitude = float(partes[1])
                longitude = float(partes[2])
                cidades.append((cidade, latitude, longitude)) # Tupla de cidades
    return cidades

def gerar_matriz_distancias(cidades):
    n = len(cidades)
    matriz = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                matriz[i][j] = geodesic(
                    (cidades[i][1], cidades[i][2]), 
                    (cidades[j][1], cidades[j][2])
                ).kilometers
    return matriz

# Gera a população inicial de indivíduos (caminhos aleatórios entre cidades)
def gerar_populacao_inicial(numero_cidades, tamanho_populacao):
    populacao = []
    for _ in range(tamanho_populacao): # Usado '_' pois a variável de interação não é utilizada
        individuo = list(range(1, numero_cidades + 1))
        random.shuffle(individuo)  # Embaralha as cidades para formar um caminho aleatório
        populacao.append([individuo, 0.0, 0.0])  # [caminho, distância total/custo, fitness]
    return populacao

# Seleção por torneio: escolhe o melhor entre dois indivíduos aleatórios
def torneio(populacao):
    numeros = random.sample(range(len(populacao)), 2)
    if(populacao[numeros[0]][2] > populacao[numeros[1]][2]):
        vencedor = populacao[numeros[0]]
    else:
        vencedor = populacao[numeros[1]]
    return vencedor

# Retorna os 5% melhores indivíduos (elitismo)
def elitismo(populacao):
    k = math.ceil(len(populacao) * 0.05) # Arredonda quantidade de indivíduos para cima
    return populacao[:k]

def reproducao(pai1):
    return pai1

# Crossover OX (Order Crossover): mantém uma parte do pai1 e completa com pai2
def crossover_ox(pai1, pai2):
    tamanho = len(pai1)
    ponto1, ponto2 = sorted(random.sample(range(tamanho), 2))  # Seleciona dois pontos de corte
    filho = [None] * tamanho # Inicializa o filho como lista vazia
    filho[ponto1:ponto2+1] = pai1[ponto1:ponto2+1]  # Copia segmento do pai1 entre os pontos de corte

    # Preenche os espaços restantes com os genes do pai2 que não estão no filho
    pos = (ponto2 + 1) % tamanho # % tamanho garante que se ponto2 for o último índice, o pos volte para o início da lista
    for gene in pai2:
        if gene not in filho:
            while filho[pos] is not None:
                pos = (pos + 1) % tamanho
            filho[pos] = gene
    return filho

# Mutação do tipo swap: troca dois genes de posição
def mutacao_swap(individuo):
    i, j = random.sample(range(len(individuo)), 2)
    individuo[i], individuo[j] = individuo[j], individuo[i]
    return individuo

# Função principal que executa o algoritmo genético
def executar_algoritmo_genetico(arquivo, geracoes=1000, taxa_mutacao=0.2, taxa_reproducao=0.05):
    cidades = ler_arquivo(arquivo)
    distancias = gerar_matriz_distancias(cidades)
    tamanho_populacao = 5 * len(cidades) 
    populacao = gerar_populacao_inicial(len(cidades), tamanho_populacao)
    populacao = calcular_distancia_total(populacao, distancias) 
    populacao = ordenar_populacao(populacao)

    melhor_geracao = populacao[0]
    historico_melhores = []

    inicio_tempo = time.time() # Início do tempo de execução

    print(f"\n=== EXECUTANDO PARA: {arquivo.split('\\')[-1]} ===\n")
    for geracao in range(geracoes):
        nova_pop = elitismo(populacao)
        while len(nova_pop) < tamanho_populacao:
            pai1 = torneio(populacao)[0]
            pai2 = torneio(populacao)[0]
            for _ in range(3): # Gera até 3 filhos por cruzamento
                if random.random() < taxa_reproducao:
                    filho = reproducao(pai1)
                else:
                    # Realiza o crossover OX entre os pais
                    filho = crossover_ox(pai1, pai2)
                    if random.random() < taxa_mutacao:
                        filho = mutacao_swap(filho)

                novo_individuo = [filho, 0.0, 0.0]
                nova_pop = conferir_duplicidade(novo_individuo, nova_pop)
                if len(nova_pop) >= tamanho_populacao:
                    break # Garante que não ultrapasse o limite da população inicial
        populacao = calcular_distancia_total(nova_pop, distancias)
        populacao = ordenar_populacao(populacao)

        melhor_geracao = populacao[0]
        historico_melhores.append(melhor_geracao[1])

        print(f"Geração {geracao+1}: Melhor da geração = {melhor_geracao[1]:.2f} km")

    fim_tempo = time.time() # Fim do tempo de execução
    tempo_execucao = fim_tempo - inicio_tempo

    print("\n=== MELHOR INDIVÍDUO GLOBAL ===")
    print(f"Percurso: {melhor_geracao[0]}")
    print(f"Distância total: {melhor_geracao[1]:.2f} km")
    print(f"Fitness: {melhor_geracao[2]:.10f}")
    print(f"Tempo de execução: {tempo_execucao:.2f} segundos")
    return historico_melhores

# Lista de instâncias a serem testadas (passar o caminho onde o arquivo está salvo)
instancias = [
    'burma14.tsp',
    'gr96.tsp',
    'gr202.tsp',
    'gr431.tsp'
]
# Executar o algoritmo genético para cada instância
for instancia in instancias:
    historico_melhores = executar_algoritmo_genetico(instancia)