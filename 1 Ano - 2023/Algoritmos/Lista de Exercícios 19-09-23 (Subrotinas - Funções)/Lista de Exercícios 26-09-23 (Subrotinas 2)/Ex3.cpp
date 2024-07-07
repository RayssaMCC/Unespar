/*3. Crie uma sub-rotina que receba como parâmetro um valor inteiro e positivo e retorne
a soma dos divisores desse valor. Utilize passagem por referência.*/

#include <stdio.h>
#include <stdlib.h>

void somaDivisores(int numero, int *soma){
	
	*soma = 0;
	
	for(int i = 1; i <= numero; i++){
        if(numero % i == 0){
            *soma = *soma + i; //Se i for divisor do numero, adiciona i à soma
        }
    }
}

int main(){
	
	int numero, soma;

    printf("Digite um valor inteiro e positivo: ");
    scanf("%d", &numero);
    
    somaDivisores(numero, &soma);
    printf("A soma dos divisores de %d eh: %d", numero, soma);
}
