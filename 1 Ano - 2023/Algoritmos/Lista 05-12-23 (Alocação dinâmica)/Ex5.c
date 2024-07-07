/*Crie um programa em C que permita ao usuário inserir sequencialmente números inteiros.
O programa deve alocar dinamicamente memória para armazenar esses números em um array.
Após cada inserção, o programa deve exibir a soma dos números até aquele ponto.
O programa deve continuar a pedir números até que o usuário insira 0, indicando o fim da entrada.
Finalmente, exiba a soma total dos números inseridos e libere a memória alocada.*/

#include <stdio.h>
#include <stdlib.h>

int main(){
    int *numeros = NULL;
    int tamanho = 0, somaTotal = 0, numero;

    do{
        printf("Insira um numero ou 0 para finalizar: ");
        scanf("%d", &numero);

        if(numero != 0){
            tamanho++;
            numeros = (int*) realloc(numeros, tamanho * sizeof(int));

            numeros[tamanho - 1] = numero;
            somaTotal = somaTotal + numero;

            printf("Soma: %d\n\n", somaTotal);
        }
    } while(numero != 0);

    printf("Soma total dos numeros inseridos: %d\n", somaTotal);

    free(numeros);

    return 0;
}
