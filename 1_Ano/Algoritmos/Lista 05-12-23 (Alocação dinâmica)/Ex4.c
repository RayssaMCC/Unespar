/*Matriz Dinâmica. Solicite ao usuário que insira o número de linhas e colunas para uma
matriz. Aloque dinamicamente memória para armazenar a matriz. Peça ao usuário para
inserir os elementos da matriz. Exiba a matriz.*/

#include <stdio.h>
#include <stdlib.h>

int main(){
    int linhas, colunas, **matriz;

    printf("Insira o numero de linhas da matriz: ");
    scanf("%d", &linhas);

    printf("Insira o numero de colunas da matriz: ");
    scanf("%d", &colunas);

    matriz = (int**) malloc(linhas * sizeof(int));
    for(int i = 0; i < linhas; i++){
        matriz[i] = (int*) malloc(colunas * sizeof(int));
    }

    printf("Insira os elementos da matriz:\n");
    for(int i = 0; i < linhas; i++){
        for(int j = 0; j < colunas; j++){
            printf("Elemento na posicao [%d][%d]: ", i + 1, j + 1);
            scanf("%d", &matriz[i][j]);
        }
    }

    printf("Matriz inserida:\n");
    for(int i = 0; i < linhas; i++){
        for(int j = 0; j < colunas; j++){
            printf("%d ", matriz[i][j]);
        }
        printf("\n");
    }

    for(int i = 0; i < linhas; i++){
        free(matriz[i]);
    }
    free(matriz);

    return 0;
}
