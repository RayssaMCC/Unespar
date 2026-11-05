#include <stdio.h>

int main(){
	float x = 1, soma = 0, cont = 0;
	
	while(x!=0){
		printf("valor = ");
		scanf("%f", &x);
		soma = soma + x; //acumulador
		if(x!=0) cont++; //contador   //ele para de contar os valores quando x=0
	} //fim do laço
	
	printf("soma total = %f \n", soma);
	printf("contagem = %f \n", cont);
	printf("media = %f", soma/cont);  
}
