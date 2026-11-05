/*Cópia de Strings. Peça ao usuário para inserir uma string. Aloque dinamicamente
memória para armazenar essa string. Crie uma segunda string dinâmica e copie a primeira
para a segunda. Exiba a string original e a cópia*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    char *stringOriginal, *stringCopia;

    stringOriginal = (char*) malloc(50*sizeof(char));
    stringCopia = (char*) malloc(50 * sizeof(char));

    printf("Insira a string: ");
    gets(stringOriginal);

    strcpy(stringCopia, stringOriginal);

    printf("String original: %s\n", stringOriginal);
    printf("String copiada: %s", stringCopia);

    free(stringOriginal);
    free(stringCopia);

    return 0;
}
