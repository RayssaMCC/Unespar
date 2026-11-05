/*Faça um programa que receba como entrada o ano corrente e o nome de dois
arquivos: um de entrada e outro de saída. Cada linha do arquivo de entrada contém
o nome de uma pessoa (ocupando 40 caracteres) e o seu ano de nascimento. O
programa deverá ler o arquivo de entrada e gerar um arquivo de saída onde aparece
o nome da pessoa seguida por uma string que representa a sua idade.
• Se a idade for menor do que 18 anos, escreva “menor de idade”
• Se a idade for maior do que 18 anos, escreva “maior de idade”
• Se a idade for igual a 18 anos, escreva “entrando na maior idade”*/

#include <stdio.h>
#include <stdlib.h>

int main(){

    int ano, nascimento, idade, x;
    char nomeArqE[100], nomeArqS[100], nomePessoa[41];
    FILE *arqE, *arqS;

    printf("Informe o ano corrente: ");
    scanf("%d", &ano);
    fflush(stdin);

    //nome e informações do arquivo de entrada
    printf("Informe o nome do arquivo de entrada: ");
    gets(nomeArqE);
    sprintf(nomeArqE, "%s.txt", nomeArqE);

    arqE= fopen(nomeArqE, "w");

    if(arqE == NULL){
        printf("Erro ao abrir o arquivo de entrada.");
        return 1;
    }

    printf("\n");
    do{
        printf("Insira o nome da pessoa e o ano de nascimento: ");
        gets(nomePessoa);
        fflush(stdin);
        fprintf(arqE, "%s\n", nomePessoa);

        printf("Insira 1 para continuar ou 0 para parar: ");
        scanf("%d", &x);
        fflush(stdin);
        printf("\n");

    } while(x == 1);

    fclose(arqE);

    //nome do arquivo de saida
    printf("Informe o nome do arquivo de saida: ");
    gets(nomeArqS);
    sprintf(nomeArqS, "%s.txt", nomeArqS);

    arqE = fopen(nomeArqE, "r");
    arqS = fopen(nomeArqS, "w");

    if(arqE == NULL || arqS == NULL){
        printf("Erro ao abrir os arquivos.");
        return 1;
    }

    while(fscanf(arqE, "%40s %d", nomePessoa, &nascimento) != EOF){
        idade = ano - nascimento;

        if(idade < 18){
            fprintf(arqS,"%s eh menor de idade.\n", nomePessoa);
        }
        else if(idade > 18){
            fprintf(arqS,"%s eh maior de idade.\n", nomePessoa);
        }
        else if(idade == 18){
            fprintf(arqS,"%s esta entrando na maioridade.\n", nomePessoa);
        }
    }

    fclose(arqE);
    fclose(arqS);

    printf("Processo concluido, verifique o arquivo de saida.\n");

    return 0;
}
