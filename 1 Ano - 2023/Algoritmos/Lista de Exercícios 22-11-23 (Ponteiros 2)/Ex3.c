/*Crie um programa que contenha um array de float contendo 10 elementos. Imprima o
endere�o de cada posi��o desse array.*/

#include <stdio.h>
#include <stdlib.h>

int main(){
    float *A[10];

    printf("Insira os valores do vetor: ");
    for(int i = 0; i < 10; ++i){
        scanf("%f", &A[i]);
    }

    for(int i = 0; i < 10; ++i){
        printf("Endereco do elemento %d: %p\n", i, &A[i]);
    }
}
