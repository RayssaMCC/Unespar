#include <stdio.h>
#include <stdlib.h>

main(){
	int n;
	printf("Insira um numero: ");
	scanf("%d", &n);
	
	if (n%3 == 0){
		
		printf("%d eh multiplo de 3.",n);
	}
	else {
		printf("%d nao eh multilplo de 3.",n);
	}
	
}
