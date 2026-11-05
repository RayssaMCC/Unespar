#include <stdio.h>
#include <stdlib.h>

void maior(int num1, int num2){
	
	if(num1>num2){
		printf("O numero %d e maior.", num1);
	}
	else{
		printf("O numero %d e maior.", num2);
	}
}

int main(){
	
	int num1 = 0, num2 = 0;
	
	printf("Insira o 1 numero: ");
	scanf("%d", &num1);
	printf("insira o 2 numero: ");
	scanf("%d", &num2);
	
	maior(num1, num2);
}
