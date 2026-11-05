/*Faça um programa que leia 2 valores inteiros e chame uma função que receba estas 2
variáveis e troque o seu conteúdo, ou seja, esta função é chamada passando duas variáveis
A e B por exemplo e, após a execução da função, A conterá o valor de B e B terá o valor de
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
