#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

//struct para representar o AFD
typedef struct {
    int estadoInicial;
    int qtdEstados;
    int qtdEstadosFinais;
    int *vetEstadosFinais;
    int qtdSimbolos;
    char *vetSimbolos;
    int **vetTransicoes;
} AFD;

//função para testar a palavra no AFD
bool testarPalavra(AFD afd, char *vetPalavra) {
    int estadoAtual = afd.estadoInicial;

    //percorre a palavra
    for (int i = 0; vetPalavra[i] != '\0'; i++) {
        //encontra o índice do símbolo na lista de símbolos                     
        int indiceSimbolo = -1;
        for (int j = 1; j <= afd.qtdSimbolos; j++) {  //ajustado para iniciar em 1
            if (afd.vetSimbolos[j] == vetPalavra[i]) { //compara o símbolo atual com cada símbolo no vetor de símbolos do AFD
                indiceSimbolo = j; //símbolo encontrado no alfabeto, seu índice vai ser usado na matriz de transições
                break;
            }
        }

        //verifica se o símbolo não está na lista de símbolos
        if (indiceSimbolo == -1) {
            printf("O simbolo '%c' nao pertence ao alfabeto do AFD.\n", vetPalavra[i]);
            return false; //palavra rejeitada
        }

        //obtém o próximo estado através da transição atual
        estadoAtual = afd.vetTransicoes[estadoAtual][indiceSimbolo];   //estado resultante da transição do estado atual com o símbolo atual
                                                                       //cada célula na matriz representa uma possível transição de estado
                                                                       //o valor armazenado na célula correspondente é o próximo estado após a transição
                                                                     
        //verifica se o estado atual é válido
        if (estadoAtual == -1) {
            printf("Nao ha transicao de estado com o simbolo '%c' em alguma posicao.\n", vetPalavra[i]);
            return false; //palavra rejeitada
        }
    }

    //verifica se o estado atual é final
    for (int i = 1; i <= afd.qtdEstadosFinais; i++) {  //ajustado para iniciar em 1
        if (estadoAtual == afd.vetEstadosFinais[i]) {
            return true; //palavra aceita
        }
    }
    
    printf("Palavra nao termina no estado final.\n");
    return false; //palavra rejeitada
}

int main() {
    AFD afd;
    char vetPalavra[100];
    char continuar;

    printf("-------------AUTOMATO FINITO DETERMINISTICO-------------\n"); //título
    printf("Informe o estado inicial (numero): "); //estado inicial
    scanf("%d", &afd.estadoInicial);

    printf("Informe a quantidade de estados (numero): "); //quantidade de estados totais
    scanf("%d", &afd.qtdEstados);

    printf("Informe a quantidade de estados finais (numero): "); //quantidade de estados finais
    scanf("%d", &afd.qtdEstadosFinais);

    //alocação do vetor de estados finais com índice iniciando em 1
    afd.vetEstadosFinais = (int *)malloc((afd.qtdEstadosFinais + 1) * sizeof(int));  //ajustado para alocar +1 espaço

    printf("Informe os estados finais (numero): "); //vetor para salvar os estados finais
    for (int i = 1; i <= afd.qtdEstadosFinais; i++) {  //ajustado para iniciar em 1
        scanf("%d", &afd.vetEstadosFinais[i]);
    }

    printf("Informe a quantidade de simbolos no alfabeto (numero): "); //quantidade de simbolos
    scanf("%d", &afd.qtdSimbolos);

    //alocação do vetor de símbolos com índice iniciando em 1
    afd.vetSimbolos = (char *)malloc((afd.qtdSimbolos + 1) * sizeof(char));  //ajustado para alocar +1 espaço

    printf("Informe os simbolos (letras do alfabeto): "); //vetor para salvar as letras
    for (int i = 1; i <= afd.qtdSimbolos; i++) {  //ajustado para iniciar em 1
        scanf(" %c", &afd.vetSimbolos[i]);
    }

    printf("\n-------------TABELA DE TRANSICOES-------------\n"); //mostra a matriz no terminal

    //imprime os símbolos (a, b ...)
    for (int c = 1; c <= afd.qtdSimbolos; c++) {  //ajustado para iniciar em 1
        printf("\t%c", afd.vetSimbolos[c]);
    }
    printf("\n");

    //imprime os estados (q1, q2 ...)
    for (int l = 1; l <= afd.qtdEstados; l++) {  //ajustado para iniciar em 1
        printf("q%d", l);

        //imprime as transições (1,1 1,2 ...)
        for (int c = 1; c <= afd.qtdSimbolos; c++) {  //ajustado para iniciar em 1
            printf("\t%d,%d", l, c);
        }
        printf("\n");
    }

    //alocação dinâmica para a matriz de transições com índice iniciando em 1
    afd.vetTransicoes = (int **)malloc((afd.qtdEstados + 1) * sizeof(int *));  //ajustado para alocar +1 espaço
    for (int i = 1; i <= afd.qtdEstados; i++) {  //ajustado para iniciar em 1
        afd.vetTransicoes[i] = (int *)malloc((afd.qtdSimbolos + 1) * sizeof(int));  //ajustado para alocar +1 espaço
    }

    //preenchimento das transições
    printf("\nPreencha as transicoes (valor para qual 'q' ira para mudanca de estado, -1 caso nao tenha mudanca de estado): ");
    for (int i = 1; i <= afd.qtdEstados; i++) {  //ajustado para iniciar em 1
        for (int j = 1; j <= afd.qtdSimbolos; j++) {  //ajustado para iniciar em 1
            printf("\nTransicao (%d,%d): ", i, j);
            scanf("%d", &afd.vetTransicoes[i][j]);
        }
    }

    //exibe a nova matriz de transições
    printf("\n-------------MATRIZ DE TRANSICOES-------------\n");
    
    //imprime os símbolos (a, b ...)
    for (int c = 1; c <= afd.qtdSimbolos; c++) {  //ajustado para iniciar em 1
        printf("\t%c", afd.vetSimbolos[c]);
    }
    printf("\n");

    //imprime os estados (q1, q2 ...)
    for (int i = 1; i <= afd.qtdEstados; i++) {  //ajustado para iniciar em 1
        printf("q%d", i);

        //imprime as transições preenchidas
        for (int j = 1; j <= afd.qtdSimbolos; j++) {  //ajustado para iniciar em 1
            printf("\t%d", afd.vetTransicoes[i][j]);
        }
        printf("\n");
    }

    //teste de palavra
    do {
        printf("\n-------------TESTE DE PALAVRAS-------------\n");
        printf("Informe a palavra a ser testada: ");
        
        scanf("%s", vetPalavra);

        //testa a palavra no AFD
        if (testarPalavra(afd, vetPalavra)) {
            printf("A palavra '%s' foi aceita pelo AFD.\n", vetPalavra);
        } else {
            printf("A palavra '%s' foi rejeitada pelo AFD.\n", vetPalavra);
        }

        //pergunta ao usuário se deseja testar outra palavra
        printf("\nDeseja testar outra palavra? (S/N): ");
        scanf(" %c", &continuar);

    } while(continuar == 'S' || continuar == 's');

    //libera a memória alocada para o AFD
    free(afd.vetEstadosFinais);
    free(afd.vetSimbolos);
    for(int i = 1; i <= afd.qtdEstados; i++) {  //ajustado para iniciar em 1
        free(afd.vetTransicoes[i]);
    }
    free(afd.vetTransicoes);

    return 0;
}