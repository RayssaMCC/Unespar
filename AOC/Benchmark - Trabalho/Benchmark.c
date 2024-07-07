#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TAMANHO 268000000 //tamanho do vetor a ser testado (~1GB) 268000000
#define EXECUCAO 5 //número de vezes que o código se repitirá para calcular a média do tempo

//preenchimento sequencial do vetor
void sequencial(int *vetor, int tamanho){
    for(int i = 0; i<tamanho; i++){
        vetor[i] = i;
    }
}

//preenchimento aleatório do vetor
void aleatorio(int *vetor, int tamanho){
    srand(27); //valor definido para o preenchimento do vetor, a sequência será a mesma para todas as máquinas que executarem o código
    for(int i = 0; i<tamanho; i++){
        vetor[i] = rand() % tamanho;
    }
}

int main(){
    int *vetor; //ponteiro para o vetor
    clock_t inicio, fim; //clock_t usado para medir intervalos de tempo/ciclos, com "inicio" e "fim" sendo as variáveis
    double tempoGastoTotalSequencial = 0;
    double tempoGastoTotalAleatorio = 0;

    vetor = (int*)malloc(TAMANHO * sizeof(int)); //aloca memória dinamicamente, calculando o total de bytes necessário para armazenar o vetor
    if(vetor == NULL){
            printf("Erro ao alocar memória\n"); //se a alocação não for bem sucedida, retorna NULL e printa a mensagem
            return 1;
    }

    printf("---------PREENCHIMENTO SEQUENCIAL DE VETORES---------\n");

    for(int i = 0; i < EXECUCAO; i++){ //quantidade de execuções do preenchimento sequencial
        //preenchimento sequencial
        inicio = clock(); //obter o tempo atual do sistema
        sequencial(vetor, TAMANHO);
        fim = clock(); //obter o tempo de fim da execução da operação
        double tempoGastoSequencial = ((double)(fim - inicio)) / CLOCKS_PER_SEC * 1000; //tempo gasto nessa execução em milissegundos
        tempoGastoTotalSequencial += tempoGastoSequencial; //acumula o tempo gasto em todas as execuções
        printf("Tempo para preenchimento sequencial %d: %.2f milissegundos\n", i+1, tempoGastoSequencial);
    }

    double tempoMedioSequencial = tempoGastoTotalSequencial / EXECUCAO;
    printf("\nTempo medio para preenchimento sequencial do vetor: %.2f milissegundos\n", tempoMedioSequencial);

    printf("\n---------PREENCHIMENTO ALEATORIO DE VETORES---------\n");

    for(int i = 0; i < EXECUCAO; i++){ //quantidade de execuções do preenchimento aleatório
        //preenchimento aleatório
        inicio = clock();
        aleatorio(vetor, TAMANHO);
        fim = clock();
        double tempoGastoAleatorio = ((double)(fim - inicio)) / CLOCKS_PER_SEC * 1000; //tempo gasto nessa execução em milissegundos
        tempoGastoTotalAleatorio += tempoGastoAleatorio; //acumula o tempo gasto em todas as execuções
        printf("Tempo para preenchimento aleatorio %d: %.2f milissegundos\n", i+1, tempoGastoAleatorio);
    }
    free(vetor); //libera o espaço da memória alocada dinamicamente

    double tempoMedioAleatorio = tempoGastoTotalAleatorio / EXECUCAO;
    printf("\nTempo medio para preenchimento aleatorio do vetor: %.2f milissegundos\n", tempoMedioAleatorio);

    printf("\n-----------RESULTADOS-----------\n");
    //teste de qualidade do preenchimento sequencial
    if(tempoMedioSequencial < 250){
        printf("Desempenho da maquina no preenchimento sequencial: Excelente\n");
    }
    else if(tempoMedioSequencial >= 250 && tempoMedioSequencial <= 450){
        printf("Desempenho da maquina no preenchimento sequencial: Bom\n");
    }
    else if(tempoMedioSequencial > 450 && tempoMedioSequencial <= 700){
       printf("Desempenho da maquina no preenchimento sequencial: Medio\n");
    }
    else if(tempoMedioSequencial > 700){
        printf("Desempenho da maquina no preenchimento sequencial: Ruim\n");
    }

    //teste de qualidade do preenchimento aleatório
    if(tempoMedioAleatorio < 2100){
        printf("Desempenho da maquina no preenchimento aleatorio: Excelente\n");
    }
    else if(tempoMedioAleatorio >= 2100 && tempoMedioAleatorio <= 3000){
        printf("Desempenho da maquina no preenchimento aleatorio: Bom\n");
    }
    else if(tempoMedioAleatorio > 3000 && tempoMedioAleatorio <= 4100){
        printf("Desempenho da maquina no preenchimento aleatorio: Medio\n");
    }
    else if(tempoMedioAleatorio > 4100){
        printf("Desempenho da maquina no preenchimento aleatorio: Ruim\n");
    }

    printf("\nPressione qualquer tecla para finalizar a execucao do benchmark.");

    getchar(); //aguarda a entrada do usuário para poder fechar o terminal
    return 0;
}
