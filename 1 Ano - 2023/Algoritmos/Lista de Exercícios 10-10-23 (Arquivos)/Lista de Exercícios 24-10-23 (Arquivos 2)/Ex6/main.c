/*Uma loja possui 4 filiais, cada uma com um código de 1 a 4. Um arquivo contendo
todas as vendas feitas durante o dia nas quatro filiais é gerado a partir de uma
planilha, sendo que cada linha do arquivo contém o número da filial e o valor de uma
venda efetuada, separados por vírgula. Ex.:
1, 189.90
1, 45.70
3, 29.90
4, 55.00
No exemplo acima, a filial 1 fez duas vendas, a primeira totalizando R$ 189,90 e a
segunda R$ 45,70. A filial 3 fez uma venda de R$ 29,90 e a 4 também uma de R$
55,00. Faça um programa que leia este arquivo e informe, ao final, o total e o valor
médio das vendas de cada filial.*/

#include <stdio.h>
#include <stdlib.h>

int main(){

    FILE *arq;
    char nomeArq[100], texto[100], virgula[5];
    int filial, x;
    float venda, total, totalVendas;
    int cont[4] = {0, 0, 0, 0};
    float soma[4] = {0, 0, 0, 0};
    float media[4] = {0, 0, 0, 0};

    //nome e informações do arquivo
    printf("Informe o nome do arquivo: ");
    gets(nomeArq);
    sprintf(nomeArq, "%s.txt", nomeArq);

    arq = fopen(nomeArq, "w");

    if(arq == NULL){
        printf("Erro ao abrir o arquivo.");
        return 1;
    }

    do{
        printf("Insira o numero da filial e o valor de vendas: ");
        gets(texto);
        fflush(stdin);

        fprintf(arq, "%s\n", texto);

        printf("Insira 1 para continuar e 0 para parar: ");
        scanf("%d", &x);
        fflush(stdin);
        printf("\n");

    }while(x == 1);

    fclose(arq);

    //teste pra soma de vendas das filiais
    arq = fopen(nomeArq, "r+");

    if(arq == NULL){
        printf("Erro ao abrir o arquivo.");
        return 1;
    }

    while(fscanf(arq, "%d %s %f", &filial, virgula, &venda)!= EOF){
        if(filial == 1){
            cont[0]++;
            soma[0] = soma[0] + venda;
        }
        else if(filial == 2){
            cont[1]++;
            soma[1] = soma[1] + venda;
        }
        else if(filial == 3){
            cont[2]++;
            soma[2] = soma[2] + venda;
        }
        else if(filial == 4){
            cont[3]++;
            soma[3] = soma[3] + venda;
        }
    }

    for(int i = 0; i<4; i++){
        if(soma[i] > 0){
            media[i] = soma[i] / cont[i];
        }
        else{
            media[i] = 0;
        }
        totalVendas = totalVendas + soma[i];
    }

    for(int j = 0; j<4; j++){
        fprintf(arq, "A media de vendas da filial %d eh de R$%.2f.\n", j+1, media[j]);
    }
    fprintf(arq, "A soma de vendas de todas as filiais eh de R$%.2f", totalVendas);

    fclose(arq);

    printf("Processo concluido, verifique o arquivo de saida.\n");

    return 0;
}
