#include <stdio.h>
#include <stdlib.h>

void fatorial(int x){
	int fat;
	
	for(fat = 1; x > 1; x = x - 1){      
		fat = fat * x;
	}
	printf("O fatorial eh %d", fat);
}

int main(){
	
	int x = 0;
	
	printf("Insira o numero que deseja saber o fatorial: ");
	scanf("%d", &x);
	
	fatorial(x);
}
