/*2.A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário, idade, sexo e número de filhos.
Crie um programa em C (utilizando registros) que leia os dados de um número indeterminado de pessoas (assumir que idade=0 deve sair do programa) 
e, ao final, mostre:

a) A média de idade das mulheres com salário inferior a R$ 300,00;
b) A média de salário da população;
c) A média do número de filhos;
d) O maior salário;
e) A menor idade.*/

#include <stdlib.h>
#include <stdio.h>

struct infos{
	float salario;
	int idade;
	char sexo;
	int filhos;
};

typedef struct infos Populacao;

int main(){
	
	Populacao habitante;
	float mediaIdadeMulher = 0, mediaSalarioGeral = 0, mediaFilhos = 0, maior = 0;
	int cont[2] = {0.0};
	int menor = 1000;
	
	do{
		printf("Caso queira sair do programa, digite 0.\n\nInforme a idade da pessoa: ");
		scanf("%d", &habitante.idade);
		
		 if(habitante.idade != 0){
		 	printf("Informe o salario da pessoa: ");
			scanf("%f", &habitante.salario);
		
			printf("Informe a quantidade de filhos da pessoa: ");
			scanf("%d", &habitante.filhos);
			fflush(stdin);
		
			printf("Informe o sexo da pessoa: ");
			scanf("%c", &habitante.sexo);
			cont[0]++;
		
			printf("\n");
			
			mediaSalarioGeral = mediaSalarioGeral + habitante.salario;
			mediaFilhos = mediaFilhos + habitante.filhos;
			
			if(habitante.salario > maior){
				maior = habitante.salario;
			}
			
			if(habitante.idade <= menor){
				menor = habitante.idade;
			}
			
			if((habitante.sexo == 'F' || habitante.sexo == 'f') && habitante.salario < 300.00){
				cont[1]++;
				mediaIdadeMulher = mediaIdadeMulher + habitante.idade;
			}
		 }
		
	}while (habitante.idade != 0);
	
	printf("\nA media de idade das mulheres com salario inferior a R$ 300,00: %.2f\n", mediaIdadeMulher / cont[1]);
	printf("A media de salario da populacao: %.2f\n", mediaSalarioGeral / cont[0]);
	printf("A media do numero de filhos: %.2f\n", mediaFilhos / cont[0]);
	printf("O maior salario: %.2f\n", maior);
	printf("A menor idade: %d", menor);
}
