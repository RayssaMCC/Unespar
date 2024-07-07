/*Faça um programa que receba a temperatura média de cada mês do ano,
armazenando-as em um vetor. Calcule e mostre a maior e a menor temperatura do ano e
em que mês ocorreram (mostrar o mês por extenso: 1 – janeiro, 2 – fevereiro...).
Desconsidere empates.*/

#include <stdlib.h>
#include <stdio.h>

#define QTD_MESES 12

int main(){
	int temperatura[QTD_MESES];
	int indice = 0;
	int maiorTemp = -100;
	int menorTemp = 100;
	int indiceMaior, indiceMenor;
	
	for(indice=0; indice<QTD_MESES; indice++){
		scanf("%d", &temperatura[indice]);
	}
	for(indice = 0; indice<QTD_MESES; indice++){
		if(temperatura[indice] > maiorTemp){
			maiorTemp = temperatura[indice];
			indiceMaior = indice;
		}
		if(temperatura[indice] < menorTemp){
			menorTemp = temperatura[indice];
			indiceMenor = indice;
		}
	}
	switch(indiceMaior){
		case 0: 
			printf("Maior temperatura: %d graus C em janeiro.", maiorTemp);
			break;
		case 1: 
			printf("Maior temperatura: %d graus C em fevereiro.", maiorTemp);
			break;
		case 2: 
			printf("Maior temperatura: %d graus C em marco.", maiorTemp);
			break;
		case 3: 
			printf("Maior temperatura: %d graus C em abril.", maiorTemp);
			break;
		case 4: 
			printf("Maior temperatura: %d graus C em maio.", maiorTemp);
			break;
		case 5: 
			printf("Maior temperatura: %d graus C em junho.", maiorTemp);
			break;
		case 6: 
			printf("Maior temperatura: %d graus C em julho.", maiorTemp);
			break;
		case 7: 
			printf("Maior temperatura: %d graus C em agosto.", maiorTemp);
			break;
		case 8: 
			printf("Maior temperatura: %d graus C em setembro.", maiorTemp);
			break;
		case 9: 
			printf("Maior temperatura: %d graus C em outubro.", maiorTemp);
			break;
		case 10: 
			printf("Maior temperatura: %d graus C em novembro.", maiorTemp);
			break;
		case 11: 
			printf("Maior temperatura: %d graus C em dezembro.", maiorTemp);
			break;
	}
	printf("\n");
	switch(indiceMenor){
		case 0: 
			printf("Menor temperatura: %d graus C em janeiro.", menorTemp);
			break;
		case 1: 
			printf("Menor temperatura: %d graus C em fevereiro.", menorTemp);
			break;
		case 2: 
			printf("Menor temperatura: %d graus C em marco.", menorTemp);
			break;
				case 3: 
			printf("Menor temperatura: %d graus C em abril.", menorTemp);
			break;
		case 4: 
			printf("Menor temperatura: %d graus C em maio.", menorTemp);
			break;
		case 5: 
			printf("Menor temperatura: %d graus C em junho.", menorTemp);
			break;
		case 6: 
			printf("Menor temperatura: %d graus C em julho.", menorTemp);
			break;
		case 7: 
			printf("Menor temperatura: %d graus C em agosto.", menorTemp);
			break;
		case 8: 
			printf("Menor temperatura: %d graus C em setembro.", menorTemp);
			break;
		case 9: 
			printf("Menor temperatura: %d graus C em outubro.", menorTemp);
			break;
		case 10: 
			printf("Menor temperatura: %d graus C em novembro.", menorTemp);
			break;
		case 11: 
			printf("Menor temperatura: %d graus C em dezembro.", menorTemp);
			break;
	}
}
