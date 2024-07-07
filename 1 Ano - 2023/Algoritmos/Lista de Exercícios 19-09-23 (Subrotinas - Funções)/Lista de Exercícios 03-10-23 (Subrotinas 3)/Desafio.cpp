/*Faça um programa que controle o estoque de uma loja de brinquedos.
Atualmente, no estoque há 40 itens, cada um contendo código, descrição, preço de
compra, preço de venda, quantidade em estoque e estoque mínimo. O programa
deverá:
a. Criar uma rotina para cadastrar os produtos.
b. Criar uma rotina para mostrar o valor do lucro obtido com a venda de
determinado produto (inserido pelo usuário) e o percentual que esse valor
representa.
c. Criar uma rotina que mostre os produtos com quantidade em estoque abaixo
do estoque mínimo permitido.*/

#include <stdio.h>
#include <stdlib.h>

struct infos{
	int codigo;
	char desc[100];
	float precoCompra;
	float precoVenda;
	int estoqueAtual;
	int estoqueMin;
};
typedef struct infos Item;

void cadastro(Item brinquedo[40]){
	
	for(int i = 0; i<40; i++){
		printf("Informe o codigo do brinquedo: ");
		scanf("%d", &brinquedo[i].codigo);
		fflush(stdin);
		
		printf("Informe a descricao do brinquedo: ");
		gets(brinquedo[i].desc);
		fflush(stdin);
		
		printf("Informe o preco de compra do brinquedo: ");
		scanf("%f", &brinquedo[i].precoCompra);
		fflush(stdin);
		
		printf("Informe o preco de venda do brinquedo: ");
		scanf("%f", &brinquedo[i].precoVenda);
		fflush(stdin);
		
		printf("Informe o estoque atual do brinquedo: ");
		scanf("%d", &brinquedo[i].estoqueAtual);
		fflush(stdin);
		
		printf("Informe o estoque minimo do brinquedo: ");
		scanf("%d", &brinquedo[i].estoqueMin);
		printf("\n");
	}
}

void lucro(Item brinquedo[40], int codigo){
	int x = 0;
	
	do{
		printf("\nInforme o codigo do brinquedo que deseja ver o lucro: ");
		scanf("%d", &codigo);
	
		for(int i = 0; i<40; i++){
			if(brinquedo[i].codigo == codigo){
				float diferenca = brinquedo[i].precoVenda - brinquedo[i].precoCompra;
				float percentual = (diferenca * 100) / brinquedo[i].precoVenda;
				
				printf("O lucro obtido com a venda desse brinquedo eh de: %.2f, sendo um percentual de %.2f%%\n", diferenca, percentual);
				
				diferenca = 0;
				percentual = 0;
				
				printf("\nCaso queira verificar o lucro de outro brinquedo, digite 1. Se quiser encerrar a verificacao, digite 0: ");
				scanf("%d", &x);
			}	
		}
		if(x == 0){
			printf("Verificacao encerrada.\n");
		}
	}while(x == 1);
}

void estoque(Item brinquedo[3]){
	
	for(int i = 0; i<40; i++){
		if(brinquedo[i].estoqueAtual < brinquedo[i].estoqueMin){
			printf("\nO brinquedo de codigo %d esta com estoque abaixo do permitido.", brinquedo[i].codigo);
		}
	}
}

int main(){
	
	int codigo = 0;
	Item brinquedo[40];
	
	cadastro(brinquedo);
	lucro(brinquedo, codigo);
    estoque(brinquedo);
}
