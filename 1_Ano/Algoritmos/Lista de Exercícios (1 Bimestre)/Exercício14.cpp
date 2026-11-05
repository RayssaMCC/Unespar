#include <stdio.h>
#include <stdlib.h>
#include <math.h>

main(){
	float A, B, C, delta, x1, x2;
	printf("Insira os valores de A, B e C, respectivamente: \n");
	scanf("%f %f %f", &A, &B, &C);
	
	delta = pow(B, 2) - 4*A*C;
	
	if (delta < 0){
		printf("Essa equacao nao possui raizes reais");
	}
	else if (delta > 0){
		x1 = ((-B) + sqrt(delta)) / (2*A);
		x2 = ((-B) - sqrt(delta)) / (2*A);
		printf("X1 e %f e X2 e %f", x1, x2);
	}
	else if (delta == 0){
		x1 = ((-B) + sqrt(delta)) / (2*A);
		printf("A raiz e: %f", x1);
	}
}
