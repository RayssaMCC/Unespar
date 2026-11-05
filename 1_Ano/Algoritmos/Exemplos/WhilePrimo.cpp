#include <stdio.h>
int main(){
	int x, div;
	
	printf("Qual o valor? ");
	scanf("%i", &x);
	div = x-1;
	while(x%div != 0){
		div--;
	}
	if(div==1){
		printf("%i eh primo", x);
	}
	else{
		printf("%i nao eh primo", x);
	}
}
