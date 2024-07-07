#include <stdio.h>
#include <stdlib.h>

int main(){
	int n, t, mult;
	printf("Qual valor deseja obter a tabuada? ");
	scanf("%i", &n);
	//valor inicial de t=1 vai até 10 de 1 em 1
	for(t = 1; t<=10; t++){
		mult = n*t;
		printf("%i X %i = %i\n", n, t, mult);
	}
}
