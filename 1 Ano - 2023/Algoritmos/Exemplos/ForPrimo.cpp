#include <stdio.h>
#include <stdlib.h>

int main(){
	int x, cont=0; //contador sempre come�a em 0
	
	//for - la�o de repeti��o controlado por vari�vel
	//i vai de 1 at� o pr�prio x
	
	printf("Qual o valor? ");
	scanf("%i", &x);
	for(int i = 1; i<=x; i++){ //valor de inicializa��o; condi��o de repeti��o; incremento/decremento //n�o d� pra ser int i = 0 pq nenheum n�mero divide por 0, quebraria o c�digo
		printf("Valor de i = %i \n", i);
		if(x%i == 0){ 
			cont++; //se o resto da divis�o de x for 0, aumenta o contador
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
