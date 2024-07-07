#include <stdio.h>
#include <stdlib.h>
#include <math.h>

main(){
	float r, h, A, lata, custo;
	
	printf("Insira o raio do tanque: ");
	scanf("%f", &r);
	
	printf("Insira a altura do tanque: ");
	scanf("%f", &h);
	
	A = 3.14*pow(r, 2)+ 2*3.14*r*h;
	printf("Area do tanque: %f \n", A);
	
	lata = ceil(A/(5*3)); //5*3 quantiadde de m2 que a lata de 5L pinta
	printf("Qantidade de latas gastas: %f \n", lata);
	
	custo = lata*50;
	printf("O custo: %f", custo);
}
