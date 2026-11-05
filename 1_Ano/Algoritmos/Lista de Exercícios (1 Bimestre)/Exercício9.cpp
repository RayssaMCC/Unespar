#include <stdio.h>
#include <stdlib.h>

main(){
	float n1, n2, f, m;
	printf("Insira as duas notas: \n");
	scanf("%f", &n1);
	scanf("%f", &n2);
	
	printf("Insira a frequencia(0 a 100): ");
	scanf("%f", &f);
	
	m = (n1+n2)/2;
	
	if (m>=7 && f>=75){
		printf("Aprovado com media %f e frequencia de %f", m, f);
	}
	else {
		printf("Reprovado com media %f e frequencia de %f", m, f);
	}
	
}
