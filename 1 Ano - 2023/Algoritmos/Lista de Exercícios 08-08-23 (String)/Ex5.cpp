/*5. Fa�a um programa que receba uma palavra e verifique se ela constitui um
pal�ndromo, ou seja, se a palavra escrita do fim para o come�o fica igual � palavra
escrita do come�o para o fim.*/

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int main(){
    char palavra[50];
    int verificador = 0;

    printf("Digite uma palavra: ");
    gets(palavra);

    for(int i = 0; i < strlen(palavra); i++){
        if(palavra[i] == palavra[strlen(palavra) -1 -i]){
            verificador++;
        }
		else{
            verificador = 0;
        }
    }

    if(verificador == strlen(palavra)){
        printf("A palavra %s e um palindromo\n", palavra);
    }
	else{
        printf("A palavra %s nao e um palindromo\n", palavra);
    }
}
