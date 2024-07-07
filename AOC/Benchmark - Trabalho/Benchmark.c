#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TAMANHO 268000000 //tamanho do vetor a ser testado (~1GB) 268000000
#define EXECUCAO 5 //n�mero de vezes que o c�digo se repitir� para calcular a m�dia do tempo

//preenchimento sequencial do vetor
void sequencial(int *vetor, int tamanho){
    for(int i = 0; i<tamanho; i++){
        vetor[i] = i;
    }
}

//preenchimento aleat�rio do vetor
void aleatorio(int *vetor, int tamanho){
    srand(27); //valor definido para o preenchimento do vetor, a sequ�ncia ser� a mesma para todas as m�quinas que executarem o c�digo
    for(int i = 0; i<tamanho; i++){
        vetor[i] = rand() % tamanho;
    }
}

int main(){
    int *vetor; //ponteiro para o vetor
    clock_t inicio, fim; //clock_t usado para medir intervalos de tempo/ciclos, com "inicio" e "fim" sendo as vari�veis
    double tempoGastoTotalSequencial = 0;
    double tempoGastoTotalAleatorio = 0;

    vetor = (int*)malloc(TAMANHO * sizeof(int)); //aloca mem�ria dinamicamente, calculando o total de bytes necess�rio para armazenar o vetor
    if(vetor == NULL){
            printf("Erro ao alocar mem�ria\n"); //se a aloca��o n�o for bem sucedida, retorna NULL e printa a mensagem
            return 1;
    }

    printf("---------PREENCHIMENTO SEQUENCIAL DE VETORES---------\n");

    for(int i = 0; i < EXECUCAO; i++){ //quantidade de execu��es do preenchimento sequencial
        //preenchimento sequencial
        inicio = clock(); //obter o tempo atual do sistema
        sequencial(vetor, TAMANHO);
        fim = clock(); //obter o tempo de fim da execu��o da opera��o
        double tempoGastoSequencial = ((double)(fim - inicio)) / CLOCKS_PER_SEC * 1000; //tempo gasto nessa execu��o em milissegundos
        tempoGastoTotalSequencial += tempoGastoSequencial; //acumula o tempo gasto em todas as execu��es
        printf("Tempo para preenchimento sequencial %d: %.2f milissegundos\n", i+1, tempoGastoSequencial);
    }

    double tempoMedioSequencial = tempoGastoTotalSequencial / EXECUCAO;
    printf("\nTempo medio para preenchimento sequencial do vetor: %.2f milissegundos\n", tempoMedioSequencial);

    printf("\n---------PREENCHIMENTO ALEATORIO DE VETORES---------\n");

    for(int i = 0; i < EXECUCAO; i++){ //quantidade de execu��es do preenchimento aleat�rio
        //preenchimento aleat�rio
        inicio = clock();
        aleatorio(vetor, TAMANHO);
        fim = clock();
        double tempoGastoAleatorio = ((double)(fim - inicio)) / CLOCKS_PER_SEC * 1000; //tempo gasto nessa execu��o em milissegundos
        tempoGastoTotalAleatorio += tempoGastoAleatorio; //acumula o tempo gasto em todas as execu��es
        printf("Tempo para preenchimento aleatorio %d: %.2f milissegundos\n", i+1, tempoGastoAleatorio);
    }
    free(vetor); //libera o espa�o da mem�ria alocada dinamicamente

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

    //teste de qualidade do preenchimento aleat�rio
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

    getchar(); //aguarda a entrada do usu�rio para poder fechar o terminal
    return 0;
}
