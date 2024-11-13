#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//Estrutura para armazenar as estatísticas de comparações e movimentações do Bubble Sort
typedef struct {
    long long int comparacoes;    //Contador de comparações realizadas
    long long int movimentacoes;  //Contador de movimentações realizadas (long long int usado para suportar vetores grandes)
} Estatisticas;

//Função que implementa o algoritmo de ordenação Bubble Sort
void bubbleSort(int vet[], int n, Estatisticas *stats) {
    for (int i = 0; i < n - 1; i++) {          //Laço externo percorre o array até o penúltimo elemento
        for (int j = 0; j < n - i - 1; j++) {  //Laço interno realiza comparações até o último elemento ordenado
            stats->comparacoes++;              //Incrementa o número de comparações
            if (vet[j] > vet[j + 1]) {         //Se o elemento atual é maior que o próximo, troca os elementos
                //Realiza a troca de posições entre vet[j] e vet[j + 1]
                int temp = vet[j];
                vet[j] = vet[j + 1];
                vet[j + 1] = temp;
                stats->movimentacoes += 3; //Cada troca conta como 3 movimentações (atribuição de variáveis)
            }
        }
    }
}

//Função que preenche o array com valores aleatórios (sem repetição)
void preencherAleatorio(int vet[], int n) {
    for (int i = 0; i < n; i++) {
        vet[i] = i + 1; //Preenche o array com valores de 1 até n, em ordem crescente
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

//Função para testar o Bubble Sort com diferentes tipos de preenchimento
void testarBubbleSort(int n) {
    int *vet = malloc(n * sizeof(int));
    Estatisticas stats;
    clock_t inicio, fim;
    double tempo;

    printf("\nTestando com tamanho %d\n", n);

    //Teste com vetor preenchido de forma aleatória
    preencherAleatorio(vet, n); //Preenche o array com valores aleatórios
    stats.comparacoes = 0;
    stats.movimentacoes = 0;
    inicio = clock();
    bubbleSort(vet, n, &stats);
    fim = clock();
    tempo = ((double)(fim - inicio)) / CLOCKS_PER_SEC;
    printf("Aleatorio - Comparacoes de chaves: %lld, Movimentacoes de registros: %lld, Tempo de execucao: %f segundos\n", stats.comparacoes, stats.movimentacoes, tempo);

    //Teste com vetor preenchido de forma ordenada
    preencherOrdenado(vet, n); //Preenche o array em ordem crescente
    stats.comparacoes = 0;
    stats.movimentacoes = 0;
    inicio = clock();
    bubbleSort(vet, n, &stats);
    fim = clock();
    tempo = ((double)(fim - inicio)) / CLOCKS_PER_SEC;
    printf("Ordenado - Comparacoes de chaves: %lld, Movimentacoes de registros: %lld, Tempo de execucao: %f segundos\n", stats.comparacoes, stats.movimentacoes, tempo);

    //Teste com vetor preenchido de forma inversamente ordenada
    preencherInverso(vet, n); //Preenche o array em ordem decrescente
    stats.comparacoes = 0;
    stats.movimentacoes = 0;
    inicio = clock();
    bubbleSort(vet, n, &stats);
    fim = clock();
    tempo = ((double)(fim - inicio)) / CLOCKS_PER_SEC;
    printf("Inversamente ordenado - Comparacoes de chaves: %lld, Movimentacoes de registros: %lld, Tempo de execucao: %f segundos\n", stats.comparacoes, stats.movimentacoes, tempo);

    free(vet);
}

//Função principal que executa os testes com diferentes tamanhos de vetor
int main() {
    srand(time(NULL));

    printf("\n-------------------------------------------------------- BUBBLE SORT --------------------------------------------------------\n");
    testarBubbleSort(100);
    printf("\n-----------------------------------------------------------------------------------------------------------------------------\n");
    testarBubbleSort(1000);
    printf("\n-----------------------------------------------------------------------------------------------------------------------------\n");
    testarBubbleSort(10000);
    printf("\n-----------------------------------------------------------------------------------------------------------------------------\n");
    testarBubbleSort(100000);
    printf("\n");

    return 0;
}
