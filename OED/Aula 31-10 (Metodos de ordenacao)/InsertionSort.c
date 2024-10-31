#include <stdio.h>
#include <stdlib.h>

void imprimir(int vet[], int tam){
    int i;

    for(i = 0; i < tam; i++){
        printf("%d ", vet[i]);
    }
    printf("\n");
}
 
void inicio() {
    int vet[25] = {45,5,72,19,28,61,37,49,47,89,66,33,55,57,12,18,19,46,94,99,43,27,29,55,88};
    int copia, indice, i;

    imprimir(vet, 25);
   
    for(i = 1; i < 25; i++){
        copia = vet[i];
        indice = i;

        while(indice > 0 && vet[indice - 1] > copia){
            vet[indice] = vet[indice - 1]; //troca os vetores
            indice--;
        }
        vet[indice] = copia;  //ordena
    }

    imprimir(vet, 25);
}

int main() {
    inicio();
    return 0;
}