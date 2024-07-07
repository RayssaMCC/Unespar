/*Fa�a um programa que leia dois valores inteiros e chame uma fun��o que receba estes 2
valores de entrada e insira o maior valor na primeira vari�vel e o menor valor na segunda
vari�vel. No programa principal, escreva o conte�do das 2 vari�veis na tela.*/

#include <stdio.h>
#include <stdlib.h>

void Troca(int *a, int *b){

	if(*a < *b){
		int aux = *a;
		*a = *b;
		*b = aux;
	}
}


int main(){
    int a, b;

    printf("Insira os valores inteiros A e B respectivamente: ");
    scanf("%d %d", &a, &b);

    Troca(&a, &b);

    printf("Valores trocados:\n");
    printf("A: %d\nB: %d", a, b);
}
