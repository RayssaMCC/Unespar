/*Escreva um programa que contenha duas vari�veis inteiras. Leia essas vari�veis do
teclado. Em seguida, compare seus endere�os e exiba o conte�do do maior endere�o.*/

#include <stdio.h>
#include <stdlib.h>

int main(){
	int a = 0, b = 0;
	
	printf("Insira o valor de A e B respectivamente: ");
	scanf("%d %d", &a, &b);
	
	printf("Endereco de memoria deles:\n");
	printf("A: %d\n", &a);
	printf("B: %d\n", &b);
	
	
	if(&b < &a){
		printf("Conteudo do maior endereco (%d) eh: %d", &a, a);
	}
	else if(&b > &a){
		printf("Conteudo do maior endereco (%d) eh: %d", &b, b);
	}
}
