#include <stdio.h>
#include <stdlib.h>
#include <math.h>

main(){
	float c1, c2, h;
	printf("Insira o valor do cateto 1: ");
	scanf("%f", &c1);
	
	printf("Insira o valor do cateto 2: ");
	scanf("%f", &c2);
	
	h = pow (c1, 2) + pow(c2, 2);
	h = sqrt(h);
	
	printf("Valor da hipotenusa: %f", h);
}
