/*Faça um programa que armazene, em um registro, os dados de um funcionário de
uma empresa, compostos de: Nome, Idade, Sexo (M/F), CPF, Data de Nascimento,
Codigo do Setor onde trabalha (0-99), Cargo que ocupa (string de até 30 caracteres)
e Salário. Em uma subrotina que recebe o registro como parâmetro passado por
referência, receba os dados digitados pelo usuário e armazene-os na estrutura. Na
função principal, exiba esses dados na tela.*/

#include <stdlib.h>
#include <stdio.h>

struct infos{
	char nome[50];
	int idade;
	char sexo;
	char cpf[12];
	char nascimento[11];
	int codSetor;
	char cargo[30];
	float salario;
};
typedef struct infos Func;

void cadastro(Func *dados){
	int i = 0;
	
	printf("Digite o nome: ");
	gets(dados->nome);
	fflush(stdin);
	
	printf("Digite a idade: ");
	scanf("%d", &dados->idade);
	fflush(stdin);
	
	printf("Digite o sexo (M ou F): ");
	scanf("%c", &dados->sexo);
	fflush(stdin);
	
	printf("Digite o CPF: ");
	gets(dados->cpf);
	fflush(stdin);
	
	printf("Digite a data de nascimento (xx/xx/xxxx): ");
	gets(dados->nascimento);
	fflush(stdin);
	
	do{
	printf("Digite o codigo do setor (0 - 99): ");
	scanf("%d", &dados->codSetor);
		if(dados->codSetor < 0 || dados->codSetor > 99){
			printf("Insira a o codigo novamente. \n");
		}
		else{
			i = 1;
		}
	} while (i != 1);
	fflush(stdin);

	
	printf("Digite o cargo: ");
	gets(dados->cargo);
	fflush(stdin);
	
	printf("Digite o salario: ");
	scanf("%f", &dados->salario);
	
}


int main(){
	
	Func dados;
	
	cadastro(&dados); //chama a subrotina
	
	printf("\nDados cadastrados:\n");
	
	printf("\nNome: %s", dados.nome);
	printf("\nIdade: %d", dados.idade);
	printf("\nSexo: %c", dados.sexo);
	printf("\nCPF: %s", dados.cpf);
	printf("\nData de Nascimento: %s", dados.nascimento);
	printf("\nCodigo do setor: %d", dados.codSetor);
	printf("\nCargo: %s", dados.cargo);
	printf("\nSalario: %.2f", dados.salario);

}
