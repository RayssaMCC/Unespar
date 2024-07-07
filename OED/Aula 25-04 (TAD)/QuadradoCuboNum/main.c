#include <stdio.h>
#include <stdlib.h>
#include "QC.h"

int main(){

	QuadradoCubo cuboQuadrado = criarQuadradoCubo(3.0);

	float quadrado = calcularQuadrado(cuboQuadrado);
	printf("Numero ao quadrado: %.2f\n", quadrado);

	float cubo = calcularCubo(cuboQuadrado);
	printf("Numero ao cubo: %.2f\n", cubo);

	return 0;
}
