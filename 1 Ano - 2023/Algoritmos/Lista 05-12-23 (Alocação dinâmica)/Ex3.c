/*C�pia de Strings. Pe�a ao usu�rio para inserir uma string. Aloque dinamicamente
mem�ria para armazenar essa string. Crie uma segunda string din�mica e copie a primeira
para a segunda. Exiba a string original e a c�pia*/

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
