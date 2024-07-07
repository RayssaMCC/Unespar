/*2. Fa�a um programa que receba do usu�rio um arquivo texto e mostre na tela quantas
letras s�o vogais.*/

#include <stdio.h>
#include <locale.h> 

int main(){
	
	FILE *arq;
	int vogal = 0; 
	char c;
	
	arq = fopen("arquivo.txt", "r");
	
	if (arq == NULL) {
        printf("N�o foi possivel abrir o arquivo.\n");
        return 1;
    }
	
	while((c = fgetc(arq)) != EOF){	
		if(c == 'a' || c == 'A' || c == 'e' || c == 'E' || c == 'i' || c == 'I' || c == 'o' || c == 'O' || c == 'u' || c == 'U'){
			vogal++;
		}
	}
	
	fclose(arq);
	printf("O arquivo possui %d vogais", vogal);
	
	return 0;
}
