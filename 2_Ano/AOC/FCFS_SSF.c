#include <stdio.h>
#include <stdlib.h>
#include <string.h> //incluída para usar o memset
#include <limits.h> //incluída para usar INT_MAX

//Função para imprimir o estado atual do cilindro
void printCilindro(int *cilindro, int tamanhoC){ 
    //Imprime os números dos cilindros
    for(int i = 0; i < tamanhoC; i++){
        printf("|%02d|\t", i); //%02 formata o número para 2 dígitos, preenchendo com 0 à esquerda se necessário
    }
    printf("\n");

    //Imprime o estado atual de cada cilindro (XX para ocupado, -- para livre)
    for(int i = 0; i < tamanhoC; i++){
        if(cilindro[i] == 1){
            printf("|XX|\t");
        }
        else{
            printf("|--|\t");
        }
    }
    printf("\n--------------------------------------------------------------------------------------------------------------------\n");
}

//Função para implementar o FCFS
void FCFS(int *pedidos, int *cilindro, int qtdPedidos, int tamanhoC) {
    printf("\nInicio do FCFS (ordem inserida): \n");
    for(int i = 0; i < qtdPedidos; i++){
        //Marca o cilindro como ocupado para o pedido atual
        cilindro[pedidos[i]] = 1;
        //Imprime o estado atual do cilindro
        printCilindro(cilindro, tamanhoC);
    }
}

//Função para encontrar o pedido mais próximo do último atendido
int acharMaisPerto(int *pedidos, int qtdPedidos, int ultimo){
    int perto = -1; //Inicializa com -1 para indicar não encontrado
    int distanciaMinima = INT_MAX; //Inicializa com o maior valor inteiro possível
    for(int i = 0; i < qtdPedidos; i++){
        if(pedidos[i] != -99){ //Ignora pedidos já atendidos, marcados com -99
            int distancia = abs(pedidos[i] - ultimo); //Calcula a distância mais curta
            if(distancia < distanciaMinima){
                distanciaMinima = distancia;
                perto = i;
            }
        }
    }
    return perto;
}

//Função para implementar o SSF
void SSF(int *pedidos, int *cilindro, int qtdPedidos, int tamanhoC){
    printf("\nInicio do SSF (mais proximo):\n");
    int ultimo = 0; //Inicializa o último cilindro atendido como 0
    for(int i = 0; i < qtdPedidos; i++){
        int perto = acharMaisPerto(pedidos, qtdPedidos, ultimo);
        cilindro[pedidos[perto]] = 1; //Marca o cilindro como ocupado para o pedido mais próximo
        ultimo = pedidos[perto]; //Atualiza o último cilindro atendido
        pedidos[perto] = -99; //Marca o pedido como atendido
        printCilindro(cilindro, tamanhoC); //Imprime o estado atual do cilindro
    }
}

int main(){
    int tamanhoC, qtdPedidos;
    
    //Solicita o tamanho do cilindro
    printf("Informe o tamanho do cilindro: ");
    scanf("%d", &tamanhoC);
    int *cilindro = malloc(tamanhoC * sizeof(int)); //Aloca memória para o cilindro

    //Solicita a quantidade de pedidos do cilindro
    printf("Informe a quantidade de pedidos do cilindro: ");
    scanf("%d", &qtdPedidos);
    int *pedidos = malloc(qtdPedidos * sizeof(int)); //Aloca memória para os pedidos

    //Solicita os pedidos do cilindro
    for(int i = 0; i < qtdPedidos; i++){
        printf("Informe o %d%c pedido do cilindro: ", i+1, 167);
        scanf("%d", &pedidos[i]);
    }

    //Imprime a representação inicial do cilindro
    printf("\n--------------------------------------------------------------------------------------------------------------------\n");
    printf("\nRepresentacao do cilindro:\n\n");
    for(int i = 0; i < tamanhoC; i++){
        printf("|%02d|\t", i); //%02 formata o número para 2 dígitos, preenchendo com 0 à esquerda se necessário
    }
    printf("\n");
    for(int i = 0; i < tamanhoC; i++){
        printf("|--|\t");
    }
    printf("\n--------------------------------------------------------------------------------------------------------------------\n");

    //Imprime o vetor de pedidos
    printf("Vetor de Pedidos: ");
    for(int i = 0; i < qtdPedidos; i++){
            printf("%d ", pedidos[i]);
        }
    printf("\n--------------------------------------------------------------------------------------------------------------------\n");

    //Executa o FCFS e o SSF
    memset(cilindro, 0, tamanhoC * sizeof(int)); //Marca todos os cilindros como livres para a operação FCFS
    FCFS(pedidos, cilindro, qtdPedidos, tamanhoC);
    memset(cilindro, 0, tamanhoC * sizeof(int));
    SSF(pedidos, cilindro, qtdPedidos, tamanhoC); //Marca todos os cilindros como livres para a operação FCFS

    //memset usado para inicializar o vetor de cilindros com 0, garantindo que não tenha lixo de memória

    //Libera a memória alocada
    free(cilindro);
    free(pedidos);
}