#include <stdio.h>
#include <stdlib.h>

int main(){
	int x = 0;
	while(x<10){
		printf("Hello world %i\n", x);
		x++; //incrementa x pra não virar looping infinito
	}
}
