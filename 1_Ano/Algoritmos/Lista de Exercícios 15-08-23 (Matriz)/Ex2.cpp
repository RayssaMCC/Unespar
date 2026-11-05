/*2. Implemente um programa que carregue uma matriz A 2x2. Em seguida, o maior
número da matriz deve ser encontrado. Por fim, uma matriz B deve ser apresentada,
com os elementos sendo resultantes do seguinte cálculo:
* elemento da matriz A * maior elemento da matriz A*/

#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int main(){
	
	int mA[2][2];
	int mB[2][2];
	int maior = mA[0][0];
	
	srand(time(NULL));
	
	for(int i = 0; i<2; i++){
		for(int j = 0; j<2; j++){
			mA[i][j] = rand() % 100; //valores aleatórios de 0 a 100
			if(mA[i][j] > maior){
				maior = mA[i][j];
			}
		}
	}
	
	printf("\nMatriz A eh:\n");
	
	for(int i = 0; i<2; i++){
		for(int j = 0; j<2; j++){
			printf("%d\t", mA[i][j]);
			mB[i][j] = mA[i][j] * maior;
		}
		printf("\n");
	}
	
	printf("\nO maior elemento da matriz A eh: %d\n", maior);
	
	printf("\nNova matriz B:\n");
	
	for(int i = 0; i<2; i++){
		for(int j = 0; j<2; j++){
			printf("%d\t", mB[i][j]);
		}
		printf("\n");
	}
}
