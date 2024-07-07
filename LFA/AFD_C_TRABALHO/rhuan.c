#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Afd{
    int estadoInicial, qtdEstados, qtdEstadosFinais, qtdSimbolos;
    int vetEstadosFinais[10];
    char vetSimbolos[10];
    int matTransicoes[10][10];
} Afd;

//Return symbol index or -1 if symbol not in alphabet
int findSymbolIndex(char c, char* symbols, int vetSize){
    for(int i = 1; i <= vetSize; i++){
        if(symbols[i] == c){
            return i;
        }        
    }
    return -1;
}

bool checkWord(Afd afd, char* word){
    int i = 0;
    int symbolIndex;
    int currentState = afd.estadoInicial;
    int nextState;

    //For each symbol until end of the word
    while(word[i] != '\0'){
        symbolIndex = findSymbolIndex(word[i], afd.vetSimbolos, afd.qtdSimbolos);

        if(symbolIndex == -1){
            printf("\nInvalid symbol: %c", word[i]);
            return false;  //Stop checking next symbols
        }

        nextState = afd.matTransicoes[currentState][symbolIndex];
        printf("\nq%d[%c]->q%d", currentState, word[i], nextState);

        if(nextState == -1){
            printf("\nTransition does not exist: q%d[%c]", currentState, word[i]);
            return false;  //Stop checking next symbols
        }

        currentState = nextState;
        i++;
    }

    //All symbols consumed. Check if stopped in final state
    for(i = 1; i <= afd.qtdEstadosFinais; i++){
        if(afd.vetEstadosFinais[i] == currentState){
            return true;  //Current state is in final state array
        }
    }

    return false;   //Did not find current state in final state array
}

int main(){
    char vetPalavra[100];
    Afd afd;

    printf("-------------AUTOMATO FINITO DETERMINISTICO-------------\n"); //t�tulo

    printf("Informe o estado inicial (numero): "); //estado inicial
    scanf("%d", &afd.estadoInicial);

    printf("Informe a quantidade de estados (numero): "); //quantidade de estados
    scanf("%d", &afd.qtdEstados);

    printf("Informe a quantidade de estados finais (numero): "); //quantidade de estados finais
    scanf("%d", &afd.qtdEstadosFinais);

    printf("Informe os estados finais (numeros): "); //vetor para salvar os estados
    for(int i = 1; i <= afd.qtdEstadosFinais; i++){
        scanf("%d", &afd.vetEstadosFinais[i]);
    }

    printf("Informe a quantidade de simbolos no alfabeto (numero): "); //quantidade de simbolos
    scanf("%d", &afd.qtdSimbolos);

    printf("Informe os simbolos (insira letras do alfabeto): "); //vetor para salvar as letras
    for(int i = 1; i <= afd.qtdSimbolos; i++){
        scanf(" %c", &afd.vetSimbolos[i]); //usando %c para ler apenas um caractere
    }

    //--------------------------- ^^^^ APARENTEMENTE FUNCIONAL AT� AQUI ^^^^ ---------------------------------

    printf("\n-------------TABELA DE TRANSICOES-------------\n"); //mostra a matriz no terminal

    //imprime os simbolos (a, b ...)
    for(int c = 0; c < afd.qtdSimbolos; c++){
        printf("\t%c", afd.vetSimbolos[c]);
    }
    printf("\n");

    //imprime os estados (q1, q2 ...)
    for(int l = 1; l <= afd.qtdEstados; l++){
        printf("q%d", l);

        //imprime as transi��es (1,1 1,2 ...)
        for(int c = 1; c <= afd.qtdSimbolos; c++){
            printf("\t%d,%d", l, c);
        }
        printf("\n");
    }

    //preenchimento das transi��es
    printf("\nPreencha as transicoes (estado destino, -1 caso nao tenha mudanca de estado)\n");
    for(int i = 1; i <= afd.qtdEstados; i++){
        for(int j = 1; j <= afd.qtdSimbolos; j++){
            printf("Transicao (%d,%d): ", i, j);
            scanf("%d", &afd.matTransicoes[i][j]);            
        }
    }

    //----------------------- ^^^^ TESTANDO AQUI ^^^^ -----------------

    printf("\n-------------TESTE DE PALAVRAS-------------\n");

    while(true){
        printf("\nInforme a palavra a ser testada: (letras do alfabeto)\n");
        scanf("%s", &vetPalavra);

        if(checkWord(afd, vetPalavra)){
            printf("\nPalavra aceita!");
        } else{
            printf("\nPalavra nao aceita!");
        }
    }   
}

