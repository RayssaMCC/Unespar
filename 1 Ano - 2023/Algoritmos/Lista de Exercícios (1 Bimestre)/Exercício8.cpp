#include <stdio.h>
#include <stdlib.h>

main(){
	int x, y;
	printf("Insira os valores: \n");
	scanf("%d", &x);
	scanf("%d", &y);
	
	if ((x+y)%2 == 0){
		printf("Par ganha!");
	}
	else {
		printf("Impar ganha!");
	}
}
