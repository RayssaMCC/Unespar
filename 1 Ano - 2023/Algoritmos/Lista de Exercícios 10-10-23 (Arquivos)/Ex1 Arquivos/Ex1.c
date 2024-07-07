/*1. Escreva um programa que:
a. Crie/abra um arquivo texto de nome “arq.txt”
b. Permita que o usuário grave diversos caracteres nesse arquivo, até que o
usuário entre com o caractere ‘0’
c. Feche o arquivo
d. Agora, abra e leia o arquivo, caractere por caractere, e escreva na tela todos
os caracteres armazenados*/

#include <stdio.h>
#include <stdlib.h>

int main() {
	
	FILE *arq;
	char c;
	
	arq = fopen("arq.txt", "w");
	
	if (arq == NULL) {
        printf("Não foi possível abrir o arquivo.\n");
        return 1;
    }
	
	do{
		printf("Insira o caractere: ");
		fflush(stdin);
		scanf("%c", &c);
		fputc(c, arq);
		
	}while(c != '0');
	
	fclose(arq);
	
	arq = fopen("arq.txt", "r");
	
	while((c = fgetc(arq)) != EOF){
		printf("\nCaractere inserido: %c", c);
	}
	
	fclose(arq);
	return 0;
}
