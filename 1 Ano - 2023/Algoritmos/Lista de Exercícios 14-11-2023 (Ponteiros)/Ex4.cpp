/*Fa�a um programa que leia 2 valores inteiros e chame uma fun��o que receba estas 2
vari�veis e troque o seu conte�do, ou seja, esta fun��o � chamada passando duas vari�veis
A e B por exemplo e, ap�s a execu��o da fun��o, A conter� o valor de B e B ter� o valor de
A. Realize essa troca utilizando ponteiros.*/

#include <stdio.h>
#include <stdlib.h>

void Troca(int *a, int *b){
	int aux = *a;
	
	*a = *b;
	*b = aux;
}

int main(){
	int a, b;
	
	 printf("Insira os valores de A e B respectivamente: ");
	 scanf("%d %d", &a, &b);
	 
	 Troca(&a,&b);
	 
	 printf("Valores trocados:\n");
	 printf("A: %d\nB: %d", a,b);
}
