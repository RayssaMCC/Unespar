/*3. Faça um programa que receba uma frase, calcule e mostre a quantidade de
vogais da frase digitada. O programa deverá contar vogais maiúsculas e
minúsculas.*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(){
    char frase[50];
    int qtd_vogal = 0;

    printf("Informe uma frase: ");
    gets(frase);

    for(int i = 0; i < strlen(frase); i++){
        if(tolower(frase[i]) == tolower('a') || tolower(frase[i]) == tolower('e') || tolower(frase[i]) == tolower('i') || tolower(frase[i]) == tolower('o') || tolower(frase[i]) == tolower('u')){
            qtd_vogal++;
        }
    }

    printf("Quantidade de vogais: %d\n", qtd_vogal);
}

