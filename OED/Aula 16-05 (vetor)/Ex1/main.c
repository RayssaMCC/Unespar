/*Faça um programa que leia 5 valores inteiros, armazene-os em um vetor, calcule e apresente a soma desses vetores. Com alocação dinâmica*/

#include <stdio.h>
#include <stdlib.h>

int main(){
    int *vet;
    int n, soma;

    printf("Informe o tamanho do vetor: ");
    scanf("%d", &n);
    vet = malloc(n*sizeof(int));

    printf("\nInsira os valores do vetor:\n");
    for(int i = 0; i<n; i++){
        scanf("%d", &vet[i]);
        soma += vet[i];
    }
    printf("Soma dos valores: %d\n", soma);

    free(vet);
}
