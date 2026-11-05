/*4. Crie uma sub-rotina que receba como parâmetro um vetor A de 25 números inteiros
e substitua todos os valores negativos de A por zero. O vetor resultante deverá ser
mostrado no programa principal.*/

#include <stdio.h>
#include <stdlib.h>

void substituicaoNegativos(int A[25]){
	
	for(int i = 0; i < 25; i++){
        if(A[i] < 0){ // Substitui valores negativos por zero
        	A[i] = 0;
		}
    }
}

int main(){
	int A[25];
	
	printf("Digite 25 numeros inteiros: ");
    for(int i = 0; i < 25; i++){
        scanf("%d", &A[i]);
    }
    
    substituicaoNegativos(A);
    
    printf("\nVetor resultante:\n");
    for(int i = 0; i < 25; i++){
        printf("%d ", A[i]);
    }
}
