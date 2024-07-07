/*3. Implemente um programa que receba números para uma matriz A 3x4. Apresente
como saída uma matriz B, em que os elementos são resultantes dos seguintes
cálculos:
* Os números ímpares da matriz A devem ser multiplicados por 3.
* Os números pares da matriz A devem ser multiplicados por 2.*/

#include <stdio.h>
#include <stdlib.h>

int main(){
	
	int mA[3][4];
	int mB[3][4];
	
	printf("Digite a matriz 3x4:\n");
	
	for(int i = 0; i<3; i++){
		for(int j = 0; j<4; j++){
			scanf("%d", &mA[i][j]);
			if(mA[i][j] % 2 != 0){
				mB[i][j] = mA[i][j] * 3; //ímpar
			}
			else{
				mB[i][j] = mA[i][j] * 2; //par
			}
		}
	}
	
	printf("\nMatriz A eh:\n");
	
	for(int i = 0; i<3; i++){
		for(int j = 0; j<4; j++){
			printf("%d\t", mA[i][j]);
		}
		printf("\n");
	}
	
	printf("\nNova matriz B:\n");
	
	for(int i = 0; i<3; i++){
		for(int j = 0; j<4; j++){
			printf("%d\t", mB[i][j]);
		}
		printf("\n");
	}
}
