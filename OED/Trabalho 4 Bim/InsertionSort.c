#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//Estrutura para armazenar estatísticas de comparações e movimentações realizadas pelo algoritmo
typedef struct {
    long long int comparacoes;
    long long int movimentacoes;
} Estatisticas;

//Função que implementa o algoritmo de ordenação Insertion Sort
void insertionSort(int vet[], int n, Estatisticas *stats) {
    for (int i = 1; i < n; i++) {               //Começa do segundo elemento (índice 1) até o final do array
        int chave = vet[i];                     //Armazena o valor do elemento atual em uma variável temporária
        int j = i - 1;
        
        //Incrementa o contador de comparações ao entrar no laço
        stats->comparacoes++;
        
        //Laço para encontrar a posição correta da chave
        while (j >= 0 && vet[j] > chave) {      //Enquanto elementos maiores que 'chave' forem encontrados
            vet[j + 1] = vet[j];                //Desloca o elemento vet[j] uma posição à frente
            stats->movimentacoes++;             //Incrementa o contador de movimentações para cada deslocamento
            j--;
            
            //Incrementa comparações a cada nova verificação dentro do laço while
            if (j >= 0) {
                stats->comparacoes++;
            }
        }
        
        vet[j + 1] = chave;                     //Insere 'chave' em sua posição ordenada
        stats->movimentacoes++;                 //Incrementa o contador de movimentações para a inserção de 'chave'
    }
}

//Função que preenche o array com valores aleatórios (sem repetição)
void preencherAleatorio(int vet[], int n) {
    for (int i = 0; i < n; i++) {
        vet[i] = i + 1; //Preenche o array com valores de 1 até n em ordem crescente
    }
    for (int i = 0; i < n; i++) { //Embaralha o array
        int j = rand() % n; //Gera uma posição aleatória entre 0 e n-1
        int temp = vet[i];
        vet[i] = vet[j];
        vet[j] = temp; //Troca os elementos nas posições i e j
    }
}

//Função que preenche o array com valores ordenados (1 a n)
void preencherOrdenado(int vet[], int n) {
    for (int i = 0; i < n; i++) {
        vet[i] = i + 1; //Preenche o array com valores em ordem crescente
    }
}

//Função que preenche o array com valores em ordem decrescente (n a 1)
void preencherInverso(int vet[], int n) {
    for (int i = 0; i < n; i++) {
        vet[i] = n - i; //Preenche o array com valores em ordem decrescente
    }
}

//Função para testar o Insertion Sort com diferentes tipos de preenchimento
void testarInsertionSort(int n) {
    int *vet = malloc(n * sizeof(int));
    Estatisticas stats;
    clock_t inicio, fim;
    double tempo;

    printf("\nTestando com tamanho %d\n", n);

    //Teste com vetor aleatório
    preencherAleatorio(vet, n); //Preenche o array com valores aleatórios
    stats.comparacoes = 0;
    stats.movimentacoes = 0;
    inicio = clock();
    insertionSort(vet, n, &stats);
    fim = clock();
    tempo = ((double)(fim - inicio)) / CLOCKS_PER_SEC;
    printf("Aleatorio - Comparacoes de chaves: %lld, Movimentacoes de registros: %lld, Tempo de execucao: %f segundos\n", stats.comparacoes, stats.movimentacoes, tempo);

    //Teste com vetor ordenado
    preencherOrdenado(vet, n); //Preenche o array em ordem crescente
    stats.comparacoes = 0;
    stats.movimentacoes = 0;
    inicio = clock();
    insertionSort(vet, n, &stats);
    fim = clock();
    tempo = ((double)(fim - inicio)) / CLOCKS_PER_SEC;
    printf("Ordenado - Comparacoes de chaves: %lld, Movimentacoes de registros: %lld, Tempo de execucao: %f segundos\n", stats.comparacoes, stats.movimentacoes, tempo);

    //Teste com vetor inversamente ordenado
    preencherInverso(vet, n); //Preenche o array em ordem decrescente
    stats.comparacoes = 0;
    stats.movimentacoes = 0;
    inicio = clock();
    insertionSort(vet, n, &stats);
    fim = clock();
    tempo = ((double)(fim - inicio)) / CLOCKS_PER_SEC;
    printf("Inversamente ordenado - Comparacoes de chaves: %lld, Movimentacoes de registros: %lld, Tempo de execucao: %f segundos\n", stats.comparacoes, stats.movimentacoes, tempo);

    free(vet);
}

//Função principal que executa os testes com diferentes tamanhos de vetor
int main() {
    srand(time(NULL));

    printf("\n---------------------------------------------------- INSERTION SORT ---------------------------------------------------------\n");
    testarInsertionSort(100);
    printf("\n-----------------------------------------------------------------------------------------------------------------------------\n");
    testarInsertionSort(1000);
    printf("\n-----------------------------------------------------------------------------------------------------------------------------\n");
    testarInsertionSort(10000);
    printf("\n-----------------------------------------------------------------------------------------------------------------------------\n");
    testarInsertionSort(100000);
    printf("\n");

    return 0;
}
