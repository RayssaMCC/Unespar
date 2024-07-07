/*Crie um programa em C que permita ao usu�rio inserir sequencialmente n�meros inteiros.
O programa deve alocar dinamicamente mem�ria para armazenar esses n�meros em um array.
Ap�s cada inser��o, o programa deve exibir a soma dos n�meros at� aquele ponto.
O programa deve continuar a pedir n�meros at� que o usu�rio insira 0, indicando o fim da entrada.
Finalmente, exiba a soma total dos n�meros inseridos e libere a mem�ria alocada.*/

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
