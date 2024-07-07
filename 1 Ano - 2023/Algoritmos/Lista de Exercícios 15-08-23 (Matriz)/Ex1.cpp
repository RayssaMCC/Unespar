/*1. Implemente um programa que:
* Preencha uma matriz 3 X 3 com valores inteiros, maiores que zero;
* Apresente todos os números da matriz;
* Encontre e apresente o maior valor da matriz.*/

#include <stdlib.h>
#include <stdio.h>

int main(){
	
	int m[3][3];
	int maior = m[0][0];

	printf("Digite a matriz 3x3:\n");
	
	for(int i = 0; i<3; i++){
		for(int j = 0; j<3; j++){
			scanf("%d", &m[i][j]); //scanf com espaço lê mais um número
			if(m[i][j] > maior){
				maior = m[i][j];
			}
		}
	}
	
	printf("\nMatriz lida:\n");
	
	for(int i = 0; i<3; i++){
		for(int j = 0; j<3; j++){
			printf("%d\t", m[i][j]);
		}
		printf("\n");
	}

	printf("\nO maior elemento da matriz eh: %d", maior);
	
}


