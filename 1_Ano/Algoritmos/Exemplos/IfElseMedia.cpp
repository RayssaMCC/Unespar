#include <stdio.h>
#include <stdlib.h>


main(){
	float n1, n2, n3, n4, m;
	printf("Insira as notas: \n");
	scanf("%f %f %f %f", &n1, &n2, &n3, &n4);

	m = (n1+n2+n3+n4)/4;
	
	if (m >= 6) {
		printf("Aprovado com media %f!", m);
	}
	else {
		printf("Reprovado com media %f!", m);
	}
}
