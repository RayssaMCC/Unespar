#include <stdio.h>
#include <stdlib.h>

main(){
	int x;
	printf("Insira a idade do nadador: ");
	scanf("%i", &x);
	
	if (x>=5 && x<=7){
		printf("Categoria Infantil A.");
	}
	else if (x>=8 && x<=10){
		printf("Categoria Infantil B.");
	}
	else if (x>=11 && x<=13){
		printf("Categoria Juvenil A.");
	}
	else if (x>=14 && x<=17){
		printf("Categoria Juvenil B.");
	}
	else if (x>=18) {
		printf("Categoria Senior.");
	}
}
