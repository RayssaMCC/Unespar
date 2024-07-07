/*Crie uma fun��o que receba dois par�metros: um array e um valor do mesmo tipo do
array. A fun��o dever� preencher os elementos de array com esse valor. N�o utilize �ndices
para percorrer o array, apenas aritm�tica de ponteiros.*/

#include <stdio.h>
#include <stdlib.h>

void preencher(int *vetor, int tamanho, int valor) {
    int *ptr = vetor;  // Inicializa um ponteiro para o in�cio do vetor

    // Percorre o vetor usando aritm�tica de ponteiros
    while (ptr < vetor + tamanho) {
        *ptr = valor;  // Atribui o valor atual ao elemento do vetor
        ptr++;         // Move para o pr�ximo elemento do vetor
    }
}

int main() {
    int tamanho = 5;  // Tamanho do vetor
    int A[tamanho];
    int valorPreencher;

    printf("Insira o valor para preencher o vetor: ");
    scanf("%d", &valorPreencher);

    preencher(A, tamanho, valorPreencher);

    printf("Vetor preenchido:\n");
    for (int i = 0; i < tamanho; i++) {
        printf("%d ", A[i]);
    }

    return 0;
}
