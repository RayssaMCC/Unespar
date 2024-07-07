#include <stdio.h>
#include <stdlib.h>

main(){
	float salario, nsalario;
	
	printf("Informe o salario: ");
	scanf("%f", &salario);
	
	if (salario >=0 && salario <= 400){
		nsalario = salario*0.15 + salario;
		printf("O salario com reajuste de 15%%: R$%f", nsalario);
	}
	else if (salario >= 400.01 && salario <= 800){
		nsalario = salario*0.12 + salario;
		printf("O salario com reajuste de 12%%: R$%f", nsalario);
	}
	else if (salario >= 800.01 && salario <= 1200.00){
		nsalario = salario*0.10 + salario;
		printf("O salario com reajuste de 10%%: R$%f", nsalario);
	}
	else if (salario >= 1200.01 && salario <= 2000.00){
		nsalario = salario*0.07 + salario;
		printf("o salario com reajuste de 7%%: R$%f", nsalario);
	}
	else if (salario > 2000){
		nsalario = salario*0.04 + salario;
		printf("o salario com reajuste de 4%%: R$%f", nsalario);
	}
}
