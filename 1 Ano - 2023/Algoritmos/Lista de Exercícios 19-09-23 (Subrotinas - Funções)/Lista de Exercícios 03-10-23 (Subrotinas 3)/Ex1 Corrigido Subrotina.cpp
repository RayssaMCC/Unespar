/*Crie uma subrotina que preencha um vetor com números inteiros aleatórios (utilize a
função rand() ). Após o preenchimento, solicite um número qualquer ao usuário.
Invoque outra subrotina, passando o vetor e o número digitado pelo usuário como
parâmetros, e verifique se o número digitado pelo usuário está presente no vetor. Na
função principal, informe ao usuário se o número está presente no vetor ou não.*/

#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int numAleatorio(int vetor[5]){
	srand(time(NULL));
	
	int numero;
	
	for(int i = 0; i<5; i++){
		vetor[i] = rand() % 100; //valor aleatória entre 0 e 100
	}
	
	printf("Escolha um numero aleatorio entre 0 e 100: ");
	scanf("%d", &numero);
	
	return numero;
}

int verificar(int vetor[5], int numero){
	for(int i = 0; i<5; i++){
		if(vetor[i] == numero){
			return 1; //número encontrado no vetor
		}
	}
	return 0; //número não encontrado no vetor
}

int main(){
	int vetor[5];
	int numero = numAleatorio(vetor);
	int resultado = verificar(vetor, numero);
	
	if(resultado){
		printf("O numero %d esta presente no vetor.", numero);
	}
	else{
		printf("O numero %d nao esta presente no vetor.", numero);
	}
}
