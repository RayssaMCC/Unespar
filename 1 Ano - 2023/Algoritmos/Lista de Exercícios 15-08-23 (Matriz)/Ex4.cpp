/*4. Crie um programa que leia um vetor vet contendo 18 elementos. A seguir, o
programa deverá distribuir ordenadamente esses elementos em uma matriz 3 × 6 e,
no final, mostrar a matriz.*/

#include <stdio.h>
#include <stdlib.h>

int main(){
	
	int vet[18];
	int m[3][6];
	int cont = 0;
	
	printf("Insira os 18 valores:\n");
	
	for(int n = 0; n<18; n++){
		scanf("%d", &vet[n]);
	}
	
	for(int i = 0; i<3; i++){
		for(int j = 0; j<6; j++){
			m[i][j] = vet[cont];
			cont++;
		}
	}
	
	printf("\nMatriz formada com os valores inseridos:\n");
	
	for(int i = 0; i<3; i++){
		for(int j = 0; j<6; j++){
			printf("%d\t", m[i][j]);
		}
		printf("\n");
	}
}
