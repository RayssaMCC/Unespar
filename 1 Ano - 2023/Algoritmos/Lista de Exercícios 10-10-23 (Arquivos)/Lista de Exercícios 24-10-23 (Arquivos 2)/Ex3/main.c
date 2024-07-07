/*Fa�a um programa que receba dois arquivos do usu�rio, e crie um terceiro arquivo
com o conte�do dos dois primeiros juntos (o conte�do do primeiro seguido do
conte�do do segundo).*/

#include <stdio.h>
#include <stdlib.h>

int main(){
    char nomeArq1[100], nomeArq2[100], nomeArqSaida[100], texto1[100], texto2[100];
    FILE *arq1, *arq2, *arqSaida;
    char caractere;

    //Informa��es do primeiro arquivo de entrada
    printf("Digite o nome do primeiro arquivo de entrada: ");
    gets(nomeArq1);

    arq1 = fopen(nomeArq1, "w");

    if(arq1 == NULL){
        printf("Erro ao abrir o arquivo.\n");
        return 1;
    }

    printf("Escreva as informacoes do arquivo 1: ");
    fflush(stdin);
    gets(texto1);
    fprintf(arq1, "%s", texto1);

    fclose(arq1);

    //Informa��es do segundo arquivo de entrada
    printf("Digite o nome do segundo arquivo de entrada: ");
    gets(nomeArq2);

    arq2 = fopen(nomeArq2, "w");

    if(arq2 == NULL){
        printf("Erro ao abrir o arquivo.\n");
        return 1;
    }

    printf("Escreva as informacoes do arquivo 2: ");
    fflush(stdin);
    gets(texto2);
    fprintf(arq2, "%s", texto2);

    fclose(arq2);

    arq1 = fopen(nomeArq1, "r");
    arq2 = fopen(nomeArq2, "r");

    if (arq1 == NULL || arq2 == NULL) {
        printf("N�o foi poss�vel abrir os arquivos de entrada.\n");
        return 1;
    }

    printf("Digite o nome do arquivo de saida: ");
    gets(nomeArqSaida);

    arqSaida = fopen(nomeArqSaida, "w");

    if (arqSaida == NULL) {
        printf("N�o foi poss�vel criar o arquivo de saida.\n");
        return 1;
    }

    // Copia o conte�do dos arquivos para o arquivo de sa�da
    while ((caractere = fgetc(arq1)) != EOF) {
        fputc(caractere, arqSaida);
    }
    while ((caractere = fgetc(arq2)) != EOF) {
        fputc(caractere, arqSaida);
    }

    fclose(arq1);
    fclose(arq2);
    fclose(arqSaida);

    printf("\nArquivos concatenados com sucesso em %s!\n", nomeArqSaida);

    return 0;
}
