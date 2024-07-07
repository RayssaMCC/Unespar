/*Faça um programa que receba o nome de um arquivo de entrada e outro de saída.
O arquivo de entrada contém em cada linha o nome de uma cidade (ocupando 40
caracteres) e o seu número de habitantes. O programa deverá ler o arquivo de
entrada e gerar um arquivo de saída onde aparece o nome da cidade mais populosa
seguida pelo seu número de habitantes.*/

#include <stdio.h>
#include <stdlib.h>

int main(){
    FILE *entrada, *saida;
    char cidade[41], cidadeMaisPopulosa[41], nomeArqE[50], nomeArqS[50];
    int habitantes = 0, maiorHabitantes = 0;

    printf("Digite o nome do arquivo de entrada: ");
    gets(nomeArqE);
    sprintf(nomeArqE, "%s.txt", nomeArqE);

    entrada = fopen(nomeArqE, "r");

    if(entrada == NULL){
        printf("Erro ao abrir o arquivo de entrada.\n");
        return 1;
    }

    printf("Digite o nome do arquivo de saida: ");
    gets(nomeArqS);
    sprintf(nomeArqS, "%s.txt", nomeArqS);

    saida = fopen(nomeArqS, "w");

    if(saida == NULL){
        printf("Erro ao abrir o arquivo de saida.\n");
        return 1;
    }

    while(fscanf(entrada, "%40s %d", cidade, &habitantes) != EOF){ //usa o &habitantes pq é uma variável simples (não é um vetor/matriz)
        if(habitantes > maiorHabitantes){
            maiorHabitantes = habitantes;
            strcpy(cidadeMaisPopulosa, cidade);
        }
    }

    fprintf(saida, "A cidade mais populosa eh %s, com %d habitantes.\n", cidadeMaisPopulosa, maiorHabitantes);

    fclose(entrada);
    fclose(saida);

    printf("Processo concluido, verifique o arquivo de saida.\n");

    return 0;
}
