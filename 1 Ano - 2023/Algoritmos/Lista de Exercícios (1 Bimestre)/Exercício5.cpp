#include <stdio.h>
#include <stdlib.h>
#include <math.h>

main(){
	int n100, n50, n20, n10, n5, n2, n1, v;
	printf("Insira um valor inteiro: ");
	scanf("%d", &v);
	
	n100 = v/100;
	v = v % 100;
	n50 = v/50;
	v = v % 50;
	n20 = v/20;
	v = v % 20;
	n10 = v/10;
	v = v % 10;
	n5 = v/5;
	v = v % 5;
	n2 = v/2;
	n1 = v % 2; 
	
	printf("Nota(s) de 100: %i \n", n100);
	printf("Nota(s) de 50: %i \n", n50);
	printf("Nota(s) de 20: %i \n", n20);
	printf("Nota(s) de 10: %i \n", n10);
	printf("Nota(s) de 5: %i \n", n5);
	printf("Nota(s) de 2: %i \n", n2);
	printf("Nota(s) de 1: %i \n", n1);
}

//printf("Nota(s) de 100: %i \nNota(s) de 50: %i \nNota(s) de 20: %i\nNota(s) de 10: %i\nNota(s) de 5: %i\nNota(s) de 2: %i\nNota(s) de 1: %i", n100, n50, n20, n10, n5, n2, n1);
