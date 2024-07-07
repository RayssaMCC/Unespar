/*Um vendedor recebe um sal�rio fixo mais 6% de comiss�o sobre suas vendas. Crie
um algoritmo que tenha um registro de vendedor, com o sal�rio fixo, valor total de
suas vendas, comiss�o e o sal�rio final. Crie uma sub-rotina que receba um
vendedor como par�metro (por valor ou por refer�ncia). Na subrotina, pe�a ao
usu�rio para digitar o valor do sal�rio fixo, o valor total de vendas e calcule (na
mesma subrotina) a comiss�o e o sal�rio final. Na fun��o principal, mostre todas as
informa��es. Fa�a isso para dois funcion�rios diferentes.*/

#include <stdio.h>
#include <stdlib.h>

struct infos{
	float salarioFixo;
	float valorTotalVendas;
	float comissao;
	float salarioFinal;
};
typedef struct infos Vend;

void calculo(Vend *vendedor){
	
	printf("Informe o salario fixo do vendedor: ");
	scanf("%f", &vendedor->salarioFixo);
	
	printf("Informe o valor total de vendas: ");
	scanf("%f", &vendedor->valorTotalVendas);
	
	vendedor->comissao = vendedor->valorTotalVendas * 0.06;
	vendedor->salarioFinal = vendedor->comissao + vendedor->salarioFixo;
}

int main(){
	
	int x = 0;
	
	do{
		printf("Para calcular o salario final de um vendedor, digite 1. Para encerrar o programa, digite 0: ");
		scanf("%d", &x);
		printf("\n");
		
		if(x == 1){
			Vend vendedor;
			calculo(&vendedor);
		
			printf("\nSalario fixo do vendedor: %.2f", vendedor.salarioFixo);
			printf("\nValor total de vendas do vendedor: %.2f", vendedor.valorTotalVendas);
			printf("\nValor de comissao do vendedor: %.2f", vendedor.comissao);
			printf("\nSalario final do vendedor: %.2f\n", vendedor.salarioFinal);
			printf("\n");
		}
		else{
			printf("Programa encerrado.");
		}
		
	} while(x == 1);
}
