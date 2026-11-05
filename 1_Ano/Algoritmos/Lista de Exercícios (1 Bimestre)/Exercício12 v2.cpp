#include <stdio.h>
#include <stdlib.h>

main(){
	int cod, qtd;
	float valor;
	float valorUn = 0;

	printf("Insira o codigo do item: ");
	scanf("%d", &cod);
	
	//Checa se item existe e salva valor unitario
	if (cod == 100){
		valorUn = 7.5;		
	}
	else if (cod == 101){
		valorUn = 5.5;
	}
	else if (cod == 103){
		valorUn = 10.5;
	}
	else if (cod == 104){
		valorUn = 11;
	}
	else if (cod == 105){
		valorUn = 13.5;
	}
	else if (cod == 106){
		valorUn = 3.5;
	}

	//Se produto existe, pergunta quantidade e calcula valor total
	if(valorUn != 0){
		printf("Insira a quantidade: ");
		scanf("%d", &qtd);
	
		valor  = valorUn * qtd;
		printf("o valor e de R$%f", valor);
	}
	else{
		printf("Produto nao encontrado.");
	}
}
