/*Altere o programa anterior para calcular e apresentar a m�dia dos valores entrados e aqueles que s�o maiores e menores que a m�dia. 
Com aloca��o din�mica*/

#include <stdio.h>
#include <stdlib.h>

int main(){
    int *vet;
    int n, soma;
    double media;

    printf("Informe o tamanho do vetor: ");
    scanf("%d", &n);
    vet = malloc(n*sizeof(int));

    printf("\nInsira os valores do vetor:\n");
    for(int i = 0; i<n; i++){
        scanf("%d", &vet[i]);
        soma += vet[i];
    }

    printf("Soma dos valores: %d\n", soma);

    media = soma/5;

    printf("Media dos valores: %.2f\n", media);

    for(int i = 0; i<n; i++){
      if(vet[i] < media){
            printf("Valor menor que a media: %d\n", vet[i]);
        }
        else if(vet[i] > media){
            printf("Valor maior que a media: %d\n", vet[i]);
        }
    }
    free(vet);
}

