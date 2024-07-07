/*Faça um programa que preencha um vetor com os registros acadêmicos (RA) de sete
alunos e carregue outro vetor com a média final desses alunos. Calcule e mostre:
* o RA do aluno com maior média (desconsiderar empates);
* para cada aluno não aprovado, isto é, com média menor que 7, mostrar quanto esse
aluno precisa tirar na prova de exame final para ser aprovado. Considerar que a
média para aprovação no exame é 5.*/

#include <stdlib.h>
#include <stdio.h>

int main(){
	int ra[7];
	float media[7];
	float maiorMedia = 0, notaExame;
	int i = 0, indiceMaiorRA = 0;
	
	for(i=0; i<3; i++){
		printf("\nInforme o RA do aluno %d: ", i+1);
		scanf("%d", &ra[i]);
		
		printf("Informe a media do aluno %d: ", i+1);
        scanf("%f", &media[i]);
        
        if(media[i] > maiorMedia){
        	maiorMedia = media[i];
            indiceMaiorRA = i;
		}
		
		if (media[i] < 7.0){
		notaExame = 10.0 - media[i];
		printf("A media final foi menor que 7.0, entao o aluno %d precisa tirar %.1f de nota no exame.\n", i+1, notaExame);
		}
	}
	
	printf("\nA maior media foi de %.1f e o RA do aluno eh: %d", media[indiceMaiorRA], ra[indiceMaiorRA]);
}
