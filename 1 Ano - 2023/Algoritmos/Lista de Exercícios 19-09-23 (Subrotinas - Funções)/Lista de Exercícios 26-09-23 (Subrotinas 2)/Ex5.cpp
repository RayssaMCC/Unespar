/*5. Crie um programa que carregue (em uma sub-rotina) uma matriz 3X4 com n�meros
reais. Utilize uma outra fun��o para copiar todos os valores da matriz para um vetor
de 12 posi��es. Esse vetor dever� ser mostrado no programa principal.*/

#include <stdio.h>
#include <stdlib.h>

void Matriz(float matriz[3][4]){
	
    printf("Digite os valores da matriz 3x4:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            scanf("%f", &matriz[i][j]);
        }
    }
}

void matrizParaVetor(float matriz[3][4], float vetor[12]){
	
    int k = 0;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            vetor[k] = matriz[i][j];
            k++;
        }
    }
}

int main(){
	
	float matriz[3][4];
    float vetor[12];

    Matriz(matriz);
    matrizParaVetor(matriz, vetor);

    printf("\nVetor resultante:\n");
    for(int i = 0; i < 12; i++){
        printf("%.2f ", vetor[i]);
    }
}
