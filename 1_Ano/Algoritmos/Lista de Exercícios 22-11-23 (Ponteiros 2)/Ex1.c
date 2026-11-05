/*Faça um programa que leia dois valores inteiros e chame uma função que receba estes 2
valores de entrada e insira o maior valor na primeira variável e o menor valor na segunda
variável. No programa principal, escreva o conteúdo das 2 variáveis na tela.*/

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
