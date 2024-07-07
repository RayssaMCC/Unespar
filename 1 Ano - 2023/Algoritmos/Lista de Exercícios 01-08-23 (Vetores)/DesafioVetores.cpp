/*DESAFIO - Uma pequena loja de artesanato possui apenas um vendedor e comercializa dez tipos de
objetos. O vendedor recebe, mensalmente, sal�rio de R$ 545,00, acrescido de 5% do valor
total de suas vendas. O valor unit�rio dos objetos deve ser informado e armazenado em um
vetor; a quantidade vendida de cada pe�a deve ficar em outro vetor, mas na mesma
posi��o. Crie um programa que receba os pre�os e as quantidades vendidas,
armazenando-os em seus respectivos vetores (ambos com tamanho dez). Depois,
determine e mostre:
 * um relat�rio contendo: quantidade vendida, valor unit�rio e valor total de cada
objeto. Ao final, dever�o ser mostrados o valor geral das vendas e o valor da
comiss�o que ser� paga ao vendedor; e
 * O valor do objeto mais vendido e sua posi��o no vetor (n�o se preocupe com
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
