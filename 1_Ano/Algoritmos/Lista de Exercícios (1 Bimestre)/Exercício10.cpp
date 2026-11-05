#include <stdio.h>
#include <stdlib.h>

main(){
	int ddd;
	printf("Insira o DDD: ");
	scanf("%i", &ddd);
	
	if (ddd == 61) {
		printf("DDD 61 pertence a Brasilia.");
	}
	else if (ddd == 71) {
		printf("DDD 71 pertence a Salvador.");
	}
	else if (ddd == 11) {
		printf("DDD 11 pertence a Sao Paulo.");
	}
	else if (ddd == 21) {
		printf("DDD 21 pertence a Rio de Janeiro.");
	}
	else if (ddd == 32) {
		printf("DDD 32 pertence a Juiz de Fora.");
	}
	else if (ddd == 19) {
		printf("DDD 19 pertence a Campinas.");
	}
	else if (ddd == 27) {
		printf("DDD 27 pertence a Vitoria.");
	}
	else if (ddd == 31) {
		printf("DDD 31 pertence a Belo Horizonte.");
	}
	else {
		printf("DDD nao cadastrado.");
	}
}
