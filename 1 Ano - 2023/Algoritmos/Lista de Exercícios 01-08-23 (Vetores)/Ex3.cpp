/*Fa�a um programa que receba o n�mero sorteado por um dado de seis lados jogado
vinte vezes. Mostre os n�meros sorteados e a frequ�ncia com que apareceram.*/

#include <stdlib.h>
#include <stdio.h>
						//0, 1, 2, 3, 4, 5 posi��o no vetor
int main(){				//1, 2, 3, 4, 5, 6 lados do dado
	int qtdSorteios[6] = {0, 0, 0, 0, 0, 0};
	int num;

	for(int i=0; i<20; i++){ //qtd jogadas
		printf("Insira o numero sorteado: ");
		scanf("%d", &num);

		if(num>0 && num<7){	//entre 1 e 6
			qtdSorteios[num-1] = qtdSorteios[num-1] + 1; //[num-1] = num 1 na posi��o 0 
		} else{										 	 //e [num-1] + 1 = quando um numero for sorteado, incrementa o contador da posi��o correspondente a ele (que � num-1)
			printf("Numero invalido!\n");
			i--;	//Decrementa contador para compensar o numero invalido e ler mais um
		}
	}

	for(int i=0; i<6; i++){
		if(qtdSorteios[i] > 0){
			printf("O numero %d foi sorteado %d vez(es)\n", i+1, qtdSorteios[i]);
		}
	}
}

