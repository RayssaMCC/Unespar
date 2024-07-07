#include <stdio.h>
#include <stdlib.h>

main(){
	float n;
	printf("Insira um numero: ");
	scanf("%f", &n);
	
	if (n > 50){
		n = n/2;
		printf("Metade do numero: %f", n);
	}
	else {
		n = n*2;
		printf("Dobro do numero: %f", n);
	}
}
