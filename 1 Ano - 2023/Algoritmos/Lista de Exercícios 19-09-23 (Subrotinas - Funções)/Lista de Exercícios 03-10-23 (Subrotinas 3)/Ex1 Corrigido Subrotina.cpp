/*Crie uma subrotina que preencha um vetor com n�meros inteiros aleat�rios (utilize a
fun��o rand() ). Ap�s o preenchimento, solicite um n�mero qualquer ao usu�rio.
Invoque outra subrotina, passando o vetor e o n�mero digitado pelo usu�rio como
par�metros, e verifique se o n�mero digitado pelo usu�rio est� presente no vetor. Na
fun��o principal, informe ao usu�rio se o n�mero est� presente no vetor ou n�o.*/

#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int numAleatorio(int vetor[5]){
	srand(time(NULL));
	
	int numero;
	
	for(int i = 0; i<5; i++){
		vetor[i] = rand() % 100; //valor aleat�ria entre 0 e 100
	}
	
	printf("Escolha um numero aleatorio entre 0 e 100: ");
	scanf("%d", &numero);
	
	return numero;
}

int verificar(int vetor[5], int numero){
	for(int i = 0; i<5; i++){
		if(vetor[i] == numero){
			return 1; //n�mero encontrado no vetor
		}
	}
	return 0; //n�mero n�o encontrado no vetor
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
