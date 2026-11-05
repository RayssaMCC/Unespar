#include <stdio.h>
#include <stdlib.h>

main(){
	int cod, qtd;
	float valor;
	printf("Insira o codigo do item: ");
	scanf("%d", &cod);
	printf("Insira a quantidade: ");
	scanf("%d", &qtd);
	
	if (cod == 100){
		valor = qtd*7.5;
		printf("o valor e de R$%f", valor);
	}
	else if (cod == 101){
		valor = qtd*5.5;
		printf("o valor e de R$%f", valor);
	}
	else if (cod == 103){
		valor = qtd*10.5;
		printf("o valor e de R$%f", valor);
	}
	else if (cod == 104){
		valor = qtd*11;
		printf("o valor e de R$%f", valor);
	}
	else if (cod == 105){
		valor = qtd*13.5;
		printf("o valor e de R$%f", valor);
	}
	else if (cod == 106){
		valor = qtd*3.5;
		printf("o valor e de R$%f", valor);
	}
	else{
		printf("Produto nao encontrado.");
	}
}
