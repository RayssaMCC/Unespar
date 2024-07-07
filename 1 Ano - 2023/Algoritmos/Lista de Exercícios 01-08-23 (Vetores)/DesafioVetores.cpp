/*DESAFIO - Uma pequena loja de artesanato possui apenas um vendedor e comercializa dez tipos de
objetos. O vendedor recebe, mensalmente, salário de R$ 545,00, acrescido de 5% do valor
total de suas vendas. O valor unitário dos objetos deve ser informado e armazenado em um
vetor; a quantidade vendida de cada peça deve ficar em outro vetor, mas na mesma
posição. Crie um programa que receba os preços e as quantidades vendidas,
armazenando-os em seus respectivos vetores (ambos com tamanho dez). Depois,
determine e mostre:
 * um relatório contendo: quantidade vendida, valor unitário e valor total de cada
objeto. Ao final, deverão ser mostrados o valor geral das vendas e o valor da
comissão que será paga ao vendedor; e
 * O valor do objeto mais vendido e sua posição no vetor (não se preocupe com
empates).*/

#include <stdlib.h>
#include <stdio.h>

int main(){
    float valorProd[10];
    int qdtProd[10];
    float qdtXprod = 0;
    float total = 0;
    float maior = 0;
    int i = 0;
    int j = 0;
    
    for(i = 0; i<2; i++){
        printf("Insira o valor do produto: ");
        scanf("%f", &valorProd[i]);
        printf("Insira a quantidade vendida: ");
        scanf("%d", &qdtProd[i]);
    }
    
    printf("Quantidade vendida         Valor unitario          Valor total\n");
    
    for(i = 0; i<2; i++){
        qdtXprod = valorProd[i] * qdtProd[i];
        printf("      %d                       %.2f                   %.2f\n", qdtProd[i], valorProd[i], qdtXprod);
        total += qdtXprod;
    }
    
    maior = qdtProd[0];
    for(i = 0; i<2; i++){
        if(maior < qdtProd[i]){
            j = i;
        }
    }
    
    printf("\nO produto mais vendido foi o de valor %.2f e seu indice eh %d\n", valorProd[j], j);
    printf("Valor total das vendas: %.2f\n", total);
    printf("Valor da comissao: %.2f \n", total*0.05);
}
