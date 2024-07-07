/*Soma de Arrays Dinâmicos. Peça ao usuário para inserir o tamanho de dois arrays
dinâmicos. Aloque memória dinâmica para esses arrays. Peça ao usuário para inserir
valores para ambos os arrays. Crie um terceiro array dinâmico para armazenar a soma dos
elementos dos dois arrays anteriores. Exiba o resultado.*/

#include <stdio.h>
#include <stdlib.h>

int main(){

    int tam;
    int *vet1, *vet2, *resultado;

    printf("Insira o tamanho do vetor: ");
    scanf("%d", &tam);

    //transforma em um vetor com o tamanho inserido pelo usuário
    vet1 = (int*) malloc(tam*sizeof(int));
    vet2 = (int*) malloc(tam*sizeof(int));
    resultado = (int*) malloc(tam*sizeof(int));

    printf("Insira os valores do vetor 1: ");
    for(int i = 0; i<tam; i++){
        scanf("%d", &vet1[i]);
    }
    printf("Insira os valores do vetor 2: ");
    for(int i = 0; i<tam; i++){
        scanf("%d", &vet2[i]);
    }

    for(int i = 0; i<tam; i++){
        resultado[i] = vet1[i] + vet2[i];
    }

    printf("Vetor resultante: (");

    for(int i = 0; i<tam; i++){
        if(i != tam-1){
            printf("%d, ", resultado[i]);
        }
        else{
            printf("%d)", resultado[i]);
        }
    }

    free(vet1);
    free(vet2);
    free(resultado);

    return 0;
}
