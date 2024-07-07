#include <stdio.h>
#include <stdlib.h>

int main(){
	int n, fat = 1;
	
	printf("Insira um valor inteiro: ");
	scanf("%i", &n);
	while(n>1){
		fat = fat*n; //Multiplica por n e armazena em fat
		n--; //Decrementa n (subtrai 1)
	}
	printf("Fatorial: %i", fat);
}
