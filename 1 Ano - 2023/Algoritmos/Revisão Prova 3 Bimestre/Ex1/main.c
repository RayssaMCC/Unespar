/*Crie uma struct para controlar ações de uma bolsa de valores com as seguintes
informações:
● Nome da compania
● Área de atuação da compania
● Valor atual da ação (em reais)
● Valor anterior
● Variação da ação em porcentagem (double), ou seja, quanto a ação cresceu ou caiu
desde a abertura da bolsa no dia.

Faça um programa que:
a) Preencha os campos da struct
b) Imprima os campos da struct
c) Com um laço, preencha 3 structs (vetor de structs)
d) Dado um valor de ação pelo usuário, imprima as informações das ações que
estão abaixo do valor informado.*/

#include <stdio.h>
#include <stdlib.h>

struct infos{
    char nome[100];
    char area[100];
    float valorAtual;
    float valorAnterior;
    float variacao;
};
typedef struct infos Bolsa;

int main(){

    Bolsa acoes[3];
    float valorDesejado;

    for(int i=0; i<3; i++){
        printf("Acao %d:\n", i+1);

        printf("Nome da companhia: ");
        gets(acoes[i].nome);
        fflush(stdin);

        printf("Area de atuacao da companhia: ");
        gets(acoes[i].area);
        fflush(stdin);

        printf("Valor atual da acao (em reais): ");
        scanf("%f", &acoes[i].valorAtual);
        fflush(stdin);

        printf("Valor anterior da acao (em reais): ");
        scanf("%f", &acoes[i].valorAnterior);
        fflush(stdin);

        acoes[i].variacao = ((acoes[i].valorAtual - acoes[i].valorAnterior) / acoes[i].valorAnterior) * 100;
        printf("\n");
    }

    printf("Insira o valor de acao desejado: ");
    scanf("%f", &valorDesejado);

    printf("\nAcoes com valor abaixo do desejado:\n");
    for(int i=0; i<3; i++){
        if(acoes[i].valorAtual < valorDesejado){
            printf("Nome da companhia: %s\n", acoes[i].nome);
            printf("Area de atuacao da companhia: %s\n", acoes[i].area);
            printf("Valor atual da acao: R$%.2lf\n", acoes[i].valorAtual);
            printf("Variacao da acao: %.2f%%\n", acoes[i].variacao);
            printf("\n");
        }
    }
    return 0;
}
