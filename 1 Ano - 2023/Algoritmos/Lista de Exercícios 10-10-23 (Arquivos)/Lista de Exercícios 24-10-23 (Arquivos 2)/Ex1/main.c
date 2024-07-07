/*1. Faça um programa que receba do usuário um arquivo texto e um caracter. Mostre na
tela quantas vezes aquele caractere ocorre dentro do arquivo*/

#include <stdio.h>
#include <stdlib.h>

int main(){

    FILE *arq;
    char nomeArq[100];
    char texto[100];
    char caractere, c;
    int cont;

    printf("Insira o nome do arquivo: ");
    gets(nomeArq);

    arq = fopen(nomeArq, "w");

    if(arq == NULL){
        printf("Erro ao abrir o arquivo.\n");
        return 1;
    }

    printf("Escreva as informacoes do arquivo: ");
    fflush(stdin);
    gets(texto);
    fprintf(arq, "%s", texto);

    fclose(arq);
    arq = fopen(nomeArq, "r");

    printf("Insira o caractere que deseja contar: ");
    scanf(" %c", &caractere);

    while((c = fgetc(arq)) != EOF){
        if(c == caractere){
            cont++;
        }
    }

    fclose(arq);

    printf("O caractere '%c' ocorre %d vezes no arquivo.\n", caractere, cont);

    return 0;
}
