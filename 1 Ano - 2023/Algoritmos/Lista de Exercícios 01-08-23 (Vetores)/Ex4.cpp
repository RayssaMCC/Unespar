/*Fa�a um programa que preencha um vetor com seis elementos num�ricos inteiros.
Calcule e mostre:
* todos os n�meros pares;
* a quantidade de n�meros pares;
* todos os n�meros �mpares;
* a quantidade de n�meros �mpares.*/

#include <stdlib.h>
#include <stdio.h>

int main(){
	int numero[6];
	int i = 0, par = 0, impar = 0;
	
	for(i=0; i<6; i++){
		printf("Informe o %d numero do vetor: ", i+1);
		scanf("%d", &numero[i]);
		
		if(numero[i] % 2 == 0){
			par++;
		}
		else{
			impar++;
		}
	}
	
	printf("\n");
	printf("Todos os numeros pares: \n");
	
	for(i=0; i<6; i++){
		if(numero[i] % 2 == 0){
			printf("%d ", numero[i]);
		}
	}
	
	printf("\nQuantidade de numeros pares: %d \n", par);
	printf("\nTodos os numeros impares: \n");
	
	for(i=0; i<6; i++){
		if(numero[i] % 2 != 0){
			printf("%d ", numero[i]);
		}
	}
	
	printf("\nQuantidade de numeros impares: %d", impar);
}
