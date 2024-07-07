/*Escreva uma fun��o que aceita como par�metro um array de inteiros com N valores, e
determina o maior elemento do array e o n�mero de vezes que este elemento ocorreu no
array. Por exemplo, para um array com os seguintes elementos: 5, 2, 15, 3, 7, 15, 8, 6, 15, a
fun��o principal dever� mostrar o valor 15 e o n�mero 3 (indicando que o n�mero 15
ocorreu 3 vezes). A fun��o que verifica o array deve ser do tipo void.*/

#include <stdio.h>
#include <stdlib.h>

void maiorElemento(int array[], int N) {
    int maiorValor = array[0];  // Inicializa com o primeiro elemento
    int freq = 1;  // Inicializa a frequ�ncia como 1 para contar o primeiro elemento

    for (int i = 1; i < N; i++) {
        if (array[i] > maiorValor) {
            maiorValor = array[i];
            freq = 1;  // Reinicia a frequ�ncia se encontrar um elemento maior
        }
        else if(array[i] == maiorValor) {
            freq++;  // Incrementa a frequ�ncia se encontrar um elemento igual ao maior
        }
    }
    printf("\nMaior elemento: %d\n", maiorValor);
    printf("Frequencia do maior elemento: %d\n", freq);
}

int main() {
    int N;

    printf("Digite o tamanho da array: ");
    scanf("%d", &N);

    int A[N];

    printf("Digite os elementos da array:\n");
    for (int i = 0; i < N; i++) {
        scanf("%d", &A[i]);
    }
    maiorElemento(A, N);
}
