#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void raiz(float num1){
	
	sqrt(num1); 
	printf("A raiz de %.2f eh %.2f", num1, sqrt(num1));
}

int main(){
	
	float num1 = 0;
	
	printf("Insira o numero que deseja saber a raiz: ");
	scanf("%f", &num1);
	
	raiz(num1);
}
