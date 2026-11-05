/*13. Faça um programa que receba o valor de um carro e mostre uma tabela com os
seguintes dados: preço final, quantidade de parcela e valor de cada parcela. Considere o
seguinte:
1. O preço final para compra à vista tem um desconto de 5%.
2. A quantidade de parcelas pode ser: 12, 24, 48 ou 60.
3. Os percentuais de acréscimo no valor do veículo seguem a tabela a seguir.

Quantidade de parcelas - Percentual de acréscimo sobre o preço final
12 - 6%
24 - 12%
48 - 24%
60 - 30%*/

#include <stdio.h>
#include <stdlib.h>

int main() {
	float preco = 0, parcela = 0;
	printf("Digite o preco do carro: ");
	scanf("%f", &preco);
	
	printf("quantidade de parcelas \t\t\t preco final \t\t valor da parcela \n");
	printf("   a vista \t\t\t (desconto de 5%%) %.2f \t\t 0 \n", preco - (preco * 0.05));
	printf("      12 \t\t\t (juros de 6%%) %.2f \t\t %.2f \n", preco * 1.06, parcela = (preco * 1.06) / 12);
	printf("      24 \t\t\t (juros de 12%%) %.2f \t\t %.2f \n", preco * 1.12, parcela = (preco * 1.12)/ 24);
	printf("      48 \t\t\t (juros de 24%%) %.2f \t\t %.2f \n", preco * 1.24, parcela = (preco * 1.24) / 48);
	printf("      60 \t\t\t (juros de 30%%) %.2f \t\t %.2f", preco * 1.30, parcela = (preco * 1.30) / 60);
}
