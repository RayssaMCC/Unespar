/*Crie uma fun��o para somar dois arrays. Esta fun��o deve receber dois arrays e
retornar a soma em um terceiro array. Caso o tamanho do primeiro e segundo array seja
diferente ent�o a fun��o retornar� ZERO (0). Caso a fun��o seja conclu�da com sucesso, a
mesma deve retornar o valor UM (1). Utilize aritm�tica de ponteiros para manipula��o do
array.*/

#include <stdio.h>
#include <stdlib.h>

int somarArrays(const int *array1, const int *array2, int *resultado, int tamanho1, int tamanho2){
    // Verifica se os tamanhos dos arrays s�o iguais
    if (tamanho1 != tamanho2) {
        printf("Os tamanhos dos arrays sao diferentes.\n");
        return 0; // Indica um erro
    }
    // Inicializa os ponteiros para os arrays
    const int *ptr1 = array1;
    const int *ptr2 = array2;
    int *ptrResultado = resultado;

    // Percorre os arrays usando aritm�tica de ponteiros e realiza a soma
    for (int i = 0; i < tamanho1; i++) {
        *ptrResultado = *ptr1 + *ptr2;

        // Move os ponteiros para os pr�ximos elementos
        ptr1++;
        ptr2++;
        ptrResultado++;
    }
    return 1; // Indica que a opera��o foi conclu�da com sucesso
}

int main() {
    int array1[] = {1, 2, 3, 4, 5};
    int array2[] = {6, 7, 8, 9, 10};
    int tamanho1 = sizeof(array1) / sizeof(array1[0]);
    int tamanho2 = sizeof(array2) / sizeof(array2[0]);
    int resultado[tamanho1];

    // Chama a fun��o para somar os arrays
    if(somarArrays(array1, array2, resultado, tamanho1, tamanho2)){
        printf("Resultado da soma dos arrays: ");
        for(int i = 0; i < tamanho1; i++){
            printf("%d ", resultado[i]);
        }
        printf("\n");
    }
}

