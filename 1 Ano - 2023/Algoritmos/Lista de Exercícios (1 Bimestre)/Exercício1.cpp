#include <stdio.h>
#include <stdlib.h>

main(){
	float C, F;
	printf("Insira a temperatura em C: ");
	scanf("%f", &C);
	F = 1.8*C+32;
	printf("Temperatura em F: %.1f", F);
	}
