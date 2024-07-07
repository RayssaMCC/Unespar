/*11. Faça um programa que verifique e mostre o números entre 1.000 e 2.000 (inclusive) que
são divisíveis por 7.*/

#include <stdio.h>
#include <stdlib.h>

int main() {
    int x = 0;
	for(x=1000; x<=2000; x++){
	    if(x%7==0){
	        printf("%d \n", x);
		}
	}
}
