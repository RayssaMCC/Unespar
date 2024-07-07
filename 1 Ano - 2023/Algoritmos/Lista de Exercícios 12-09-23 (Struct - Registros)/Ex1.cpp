/*1. Crie um programa (utilizando registros) para ler o c�digo, o sexo (M � masculino; F � feminino) e o 
n�mero de horas--aula ministradas pelos professores de uma escola durante um m�s. 
Sabe-se que um professor ganha R$ 60,50 hora-aula e que a escola possui dez professores. 
Se o professor ministrar menos de 70 horas no m�s, deve ser descontado 8% do seu sal�rio bruto. 
Se o professor ministrar 70 horas no m�s ou mais, deve ser descontado 5% do sal�rio bruto. Ap�s a leitura, o programa dever� mostrar:

a) Uma listagem contendo o c�digo, o sal�rio bruto, o desconto e o sal�rio l�quido de todos os professores.
b) A m�dia aritm�tica dos sal�rios brutos dos professores do sexo masculino.
c) A m�dia aritm�tica dos sal�rios brutos dos professores do sexo feminino.*/

#include <stdlib.h>
#include <stdio.h>

struct infos{
	int codigo;
	char sexo;
	float hora_aula;
	float salarioB;
	float salarioL;
	float desconto;
};

typedef struct infos Professores;

int main(){
	
	Professores prof[10];
	float mediaM = 0, mediaF = 0;
	int masculino = 0, feminino = 0;
	
	for(int i = 0; i<10; i++){
		printf("Insira o codigo do professor: ");
		scanf("%d", &prof[i].codigo);
		fflush(stdin);
		
		printf("Insira o sexo do professor (M ou F): ");
		scanf("%c", &prof[i].sexo);
		
		printf("Insira a quantidade de horas-aula: ");
		scanf("%f", &prof[i].hora_aula);
		
		prof[i].salarioB = prof[i].hora_aula * 60.50;
		
		if(prof[i].hora_aula >= 70){
			prof[i].desconto = prof[i].salarioB * 0.05;
			prof[i].salarioL = prof[i].salarioB * 0.95; // desconto 5%
		}
		else{
			prof[i].desconto = prof[i].salarioB * 0.08;
			prof[i].salarioL = prof[i].salarioB * 0.92; //desconto 8%
		}
	}
	
	for(int i = 0; i<10; i++){
		if(prof[i].hora_aula >= 70){
			printf("\n Codigo: %d\n Salario bruto: %.2f\n Desconto de R$%.2f\n Salario liquido: %.2f\n", prof[i].codigo, prof[i].salarioB, prof[i].desconto, prof[i].salarioL);
		}
		else{
			printf("\n Codigo: %d\n Salario bruto: %.2f\n Desconto de R$%.2f\n Salario liquido: %.2f\n", prof[i].codigo, prof[i].salarioB, prof[i].desconto, prof[i].salarioL);
		}
	}
	
	for(int i = 0; i<10; i++){
		if(prof[i].sexo == 'M' || prof[i].sexo == 'm'){
			masculino++;
			mediaM = (mediaM + prof[i].salarioB)/ masculino;
		}
		else if(prof[i].sexo == 'F' || prof[i].sexo == 'f'){
			feminino++;
			mediaF = (mediaF + prof[i].salarioB) / feminino;
		}
	}
	
	printf("\nMedia aritmetica dos salarios brutos dos professores do sexo masculino: %.2f\n", mediaM);
	printf("Media aritmetica dos salarios brutos dos professores do sexo feminino: %.2f", mediaF);
}
