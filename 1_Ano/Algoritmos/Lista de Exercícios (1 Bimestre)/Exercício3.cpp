#include <stdio.h>
#include <stdlib.h>

main(){
	int x;
	float y, m;
	
	printf("Insira a distancia percorrida em km. Utilize um valor inteiro: ");
	scanf("%d", &x);
	
	printf("Insira o combustivel gasto em litros. Utilize um valor real: ");
	scanf("%f", &y);
	
	m = x/y;
	
	printf("%.1f km/l", m);
}
