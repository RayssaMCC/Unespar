/*5. Crie um programa que receba as vendas semanais (de um mês com quatro
semanas) de três vendedores de uma loja e armazene essas vendas em uma
matriz. O programa deverá calcular e mostrar:
* o total de vendas do mês de cada vendedor;
* o total de vendas de cada semana (todos os vendedores juntos);
* o total de vendas do mês somando todos os vendedores.*/

#include <stdio.h>
#include <stdlib.h>

int main(){
	
    float vendas[3][4];
    float vendasMensaisFunc[3];
    float vendasSemanais[] = {0,0,0,0};
    float soma = 0, vendasTotal = 0;

    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 4; j++){
            printf("Informe o valor de vendas da semana %d do vendedor %d: ", j+1, i+1);
            scanf("%f", &vendas[i][j]);
            soma += vendas[i][j];
        }
        vendasTotal += soma;
        vendasMensaisFunc[i] = soma;
        soma = 0;
    }

    for(int j = 0; j < 4; j++){
        for(int i = 0; i < 3; i++){
            vendasSemanais[j] += vendas[i][j];
        }
    }
    
    printf("\n");

    for(int i = 0; i < 3; i++){
        printf("Vendas totais por mes do vendedor %d: R$%.2f\n",i+1, vendasMensaisFunc[i]);
    }

    printf("\n");

    for(int i = 0; i < 4; i++){
        printf("Vendas totais da semana %d: R$%.2f\n",i+1, vendasSemanais[i]);
    }

    printf("\nVendas totais do mes: R$%.2f", vendasTotal);
}
