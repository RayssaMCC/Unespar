/*Escreva um programa que declare um inteiro, um real e um char, e ponteiros para inteiro,
real, e char. Associe as variáveis aos ponteiros (use &). Modifique os valores de cada
variável usando os ponteiros. Imprima os valores das variáveis antes e após a modificação.*/

#include <stdio.h>
#include <stdlib.h>

int main(){
	//declaração de variável simples
	int a = 1;
	float b =2.5;
	char c = 'c';
	
	//declaração dos ponteiros
	int *pa;
	float *pb;
	char *pc;
	
	//ponteiros recebendo onde vão apontar
	pa = &a;
	pb = &b;
	pc = &c;
	
	printf("Valores antes da modifcacao:\n");
	printf("Inteiro: %d\n",a);
	printf("Real: %f\n", b);
	printf("Caractere: %c\n\n", c);
	
	//edita os valores apontados pelos ponteiros
	*pa = 3;
	*pb = 12.25;
	*pc = 'f';
	
	printf("Valores  apos modifcacao:\n");
	printf("Inteiro: %d\n",a);
	printf("Real: %f\n", b);
	printf("Caractere: %c\n", c);
	
}
