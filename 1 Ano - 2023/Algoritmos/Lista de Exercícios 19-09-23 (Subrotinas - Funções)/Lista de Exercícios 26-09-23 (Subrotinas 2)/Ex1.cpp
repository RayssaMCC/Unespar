/*1. Elabore um programa contendo uma sub-rotina que receba as tr�s notas de um
aluno como par�metros e uma letra. Se a letra for A, a sub-rotina dever� calcular a
m�dia aritm�tica das notas do aluno; se for P, dever� calcular a m�dia ponderada,
com pesos 5, 3 e 2. A m�dia calculada dever� ser mostrada no programa principal.
Utilize passagem por refer�ncia.*/

#include <stdio.h>
#include <stdlib.h>

void calculoMedia(float nota1, float nota2, float nota3, char opcao, float *media){
	
	if(opcao == 'A'){ //media aritmetica
		*media = (nota1 + nota2 + nota3) / 3;
	}
	else if(opcao == 'P'){ //media ponderada
		*media = (nota1*5 + nota2*3 + nota3*2) / 10;
	}
	else{
		printf("Opcao invalida. Escolha 'A' para media aritmetica ou 'P' para media ponderada.\n");
	}
}

int main(){
	
	float nota1, nota2, nota3, media;
	char opcao;
	
	printf("Informe as tres notas do aluno: ");
    scanf("%f %f %f", &nota1, &nota2, &nota3);
    
    printf("Escolha 'A' para media aritmetica ou 'P' para media ponderada: ");
    scanf(" %c", &opcao);
    
    calculoMedia(nota1, nota2, nota3, opcao, &media);
    printf("A media do aluno eh: %.2f", media);
}

