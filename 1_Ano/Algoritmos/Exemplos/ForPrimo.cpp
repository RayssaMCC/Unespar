#include <stdio.h>
#include <stdlib.h>

int main(){
	int x, cont=0; //contador sempre começa em 0
	
	//for - laço de repetição controlado por variável
	//i vai de 1 até o próprio x
	
	printf("Qual o valor? ");
	scanf("%i", &x);
	for(int i = 1; i<=x; i++){ //valor de inicialização; condição de repetição; incremento/decremento //não dá pra ser int i = 0 pq nenheum número divide por 0, quebraria o código
		printf("Valor de i = %i \n", i);
		if(x%i == 0){ 
			cont++; //se o resto da divisão de x for 0, aumenta o contador
		}
	}
	//mostrando o resultado
	if(cont==2){
		printf("%i eh primo", x);
	}
	else{
		printf("%i nao eh primo", x);
	}
}
