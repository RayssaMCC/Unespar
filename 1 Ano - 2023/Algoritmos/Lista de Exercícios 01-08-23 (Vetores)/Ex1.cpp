/*Fa�a um programa que preencha um vetor com nove n�meros inteiros, calcule e mostre
os n�meros pares e suas respectivas posi��es no vetor (�ndice).*/

#include <stdlib.h>
#include <stdio.h>

int main(){
	int num[9];
	int indice = 0;
	
	for(indice=0; indice<9; indice++){
		scanf("%d", &num[indice]);
	}
	for(indice=0; indice<9; indice++){
		if(num[indice]%2 == 0){
			printf("%d eh par e esta na posicao %d do vetor\n", num[indice], indice);
		}
	}
}
