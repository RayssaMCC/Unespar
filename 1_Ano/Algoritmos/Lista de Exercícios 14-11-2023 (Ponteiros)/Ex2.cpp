/*Escreva um programa que contenha duas variáveis inteiras. Compare seus endereços e
exiba o maior endereço.*/

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
		printf("Ponteiro de A eh maior, %d.", &a);
	}
	else if(&b > &a){
		printf("Ponteiro de B eh maior, %d", &b);
	}
	
	
}
