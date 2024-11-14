#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//Estrutura para armazenar estatísticas de comparações e movimentações realizadas pelo algoritmo
typedef struct {
    long long int comparacoes;
    long long int movimentacoes;
} Estatisticas;

//Função que implementa o algoritmo de ordenação Selection Sort (ordena o menor valor primeiro, comparando com os valores restantes)
void selectionSort(int vet[], int n, Estatisticas *stats) {
    for (int i = 0; i < n - 1; i++) {          //Laço para cada posição do vetor até a penúltima posição
        int minIdx = i;                        //Define o índice mínimo inicial como a posição atual
        for (int j = i + 1; j < n; j++) {      //Laço interno para encontrar o menor valor no subvetor
            stats->comparacoes++;              //Incrementa o contador de comparações para cada comparação
            if (vet[j] < vet[minIdx]) {        //Se encontrar um valor menor que o atual minIdx
                minIdx = j;                    //Atualiza o índice do menor valor
            }
        }
        if (minIdx != i) { //Se o índice mínimo encontrado não for o inicial
            //Troca vet[i] e vet[minIdx]
            int temp = vet[i];
            vet[i] = vet[minIdx];
            vet[minIdx] = temp;
            stats->movimentacoes += 3; //Cada troca de posições conta como 3 movimentações
        }
    }
}

//Função que preenche o vetor com valores aleatórios (sem repetição)
void preencherAleatorio(int vet[], int n) {
    for (int i = 0; i < n; i++) {
        vet[i] = i + 1; //Preenche o vetor com valores de 1 até n em ordem crescente
    }
    for (int i = 0; i < n; i++) { //Embaralha o vetor para deixá-lo aleatório
        int j = rand() % n; //Gera uma posição aleatória entre 0 e n-1
        int temp = vet[i];
        vet[i] = vet[j];
        vet[j] = temp; //Troca os elementos nas posições i e j
    }
}

//Função que preenche o vetor com valores ordenados (1 a n)
void preencherOrdenado(int vet[], int n) {
    for (int i = 0; i < n; i++) {
        vet[i] = i + 1; //Preenche o vetor com valores em ordem crescente
    }
}

//Função que preenche o vetor com valores em ordem decrescente (n a 1)
void preencherInverso(int vet[], int n) {
    for (int i = 0; i < n; i++) {
        vet[i] = n - i; //Preenche o vetor com valores em ordem decrescente
    }
}

//Função para testar o Selection Sort com diferentes tipos de preenchimento
void testarSelectionSort(int n) {
    int *vet = malloc(n * sizeof(int));
    Estatisticas stats;
    clock_t inicio, fim;
    double tempo;

    printf("\nTestando com tamanho %d\n", n);

    //Teste com vetor aleatório
    preencherAleatorio(vet, n); //Preenche o vetor com valores aleatórios
    stats.comparacoes = 0;
    stats.movimentacoes = 0;
    inicio = clock();
    selectionSort(vet, n, &stats);
    fim = clock();
    tempo = ((double)(fim - inicio)) / CLOCKS_PER_SEC;
    printf("Aleatorio - Comparacoes de chaves: %lld, Movimentacoes de registros: %lld, Tempo de execucao: %f segundos\n", stats.comparacoes, stats.movimentacoes, tempo);

    //Teste com vetor ordenado
    preencherOrdenado(vet, n); //Preenche o vetor em ordem crescente
    stats.comparacoes = 0;
    stats.movimentacoes = 0;
    inicio = clock();
    selectionSort(vet, n, &stats);
    fim = clock();
    tempo = ((double)(fim - inicio)) / CLOCKS_PER_SEC;
    printf("Ordenado - Comparacoes de chaves: %lld, Movimentacoes de registros: %lld, Tempo de execucao: %f segundos\n", stats.comparacoes, stats.movimentacoes, tempo);

    //Teste com vetor inversamente ordenado
    preencherInverso(vet, n); //Preenche o vetor em ordem decrescente
    stats.comparacoes = 0;
    stats.movimentacoes = 0;
    inicio = clock();
    selectionSort(vet, n, &stats);
    fim = clock();
    tempo = ((double)(fim - inicio)) / CLOCKS_PER_SEC;
    printf("Inversamente ordenado - Comparacoes de chaves: %lld, Movimentacoes de registros: %lld, Tempo de execucao: %f segundos\n", stats.comparacoes, stats.movimentacoes, tempo);

    free(vet);
}

//Função principal que executa os testes com diferentes tamanhos de vetor
int main() {
    srand(time(NULL));

    printf("\n---------------------------------------------------- SELECTION SORT ---------------------------------------------------------\n");
    testarSelectionSort(100);
    printf("\n-----------------------------------------------------------------------------------------------------------------------------\n");
    testarSelectionSort(1000);
    printf("\n-----------------------------------------------------------------------------------------------------------------------------\n");
    testarSelectionSort(10000);
    printf("\n-----------------------------------------------------------------------------------------------------------------------------\n");
    testarSelectionSort(100000);
    printf("\n");

    return 0;
}
