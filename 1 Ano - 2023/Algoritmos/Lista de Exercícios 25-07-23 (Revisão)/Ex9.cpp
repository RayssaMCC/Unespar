/*9. Fa�a um programa que receba o pre�o de um produto e o seu c�digo de origem e mostre
sua proced�ncia. A proced�ncia obedece a tabela a seguir:
C�digo de origem Proced�ncia
1 - Norte
2 - Nordeste
3 - Sudeste
4 - Sul
5 - Centro-oeste*/

#include <stdio.h>
#include <stdlib.h>

int main() {
    float preco = 0;
    int codigo = 0;
    
    printf("Insira o preco do produto: ");
    scanf("%f", &preco);
    printf("Insira o codigo do produto: ");
    scanf("%d", &codigo);
    
    switch(codigo){
        case 1: printf("Procedencia: Norte");
        	break;
        case 2: printf("Procedencia: Nordeste");
        	break;
        case 3: printf("Procedencia: Sudeste");
        	break;
        case 4: printf("Procedencia: Sul");
        	break;
        case 5: printf("Procedencia: Centro-oeste");
        	break;
        default: printf("Procedencia desconhecida");
        	break;
    }
}
