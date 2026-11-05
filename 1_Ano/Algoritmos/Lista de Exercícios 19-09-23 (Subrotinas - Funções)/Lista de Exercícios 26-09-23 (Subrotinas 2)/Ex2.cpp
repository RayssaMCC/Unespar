/*2. Crie um programa que receba os valores antigo e atual de um produto. Chame uma
sub-rotina que determine o percentual de acréscimo entre esses valores. O
resultado deverá ser mostrado no programa principal. Utilize passagem por
referência.*/

#include <stdio.h>
#include <stdlib.h>

void percentualAcrescimo(float antigo, float atual, float *percentual){
	
	*percentual = ((atual - antigo) / antigo) * 100;
}

int main(){
	
	float antigo, atual, percentual;
	
	printf("Digite o valor antigo do produto: ");
    scanf("%f", &antigo);

    printf("Digite o valor atual do produto: ");
    scanf("%f", &atual);

    percentualAcrescimo(antigo, atual, &percentual);
    printf("O percentual de acrescimo eh de: %.2f%%", percentual);

}
