//Faça um programa que leia 10 valores e mostre-os na ordem lida.

#include <stdlib.h>
#include <stdio.h>

int main(){
	int num[10];
	int i = 0;
	
	for(i=0; i<10; i++){
		scanf("%d", &num[i]);
	}
	for(i=0; i<10; i++){
		printf("%d \n", num[i]);
	}	
}

