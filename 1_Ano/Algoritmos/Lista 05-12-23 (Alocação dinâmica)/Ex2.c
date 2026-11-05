/*Média de Notas. Solicite ao usuário que insira a quantidade de notas que deseja calcular
a média. Aloque dinamicamente memória para armazenar as notas. Peça ao usuário para
inserir as notas. Calcule e exiba a média das notas.*/

#include <stdio.h>
#include <stdlib.h>

int main(){
    int qdtNotas;
    float *notas, media = 0.0;

    printf("Insira a quantidade de notas: ");
    scanf("%d", &qdtNotas);

    notas = (float*) malloc(qdtNotas*sizeof(float));

    printf("Insira as notas:\n");
    for(int i = 0; i < qdtNotas; i++){
        printf("Nota %d: ", i + 1);
        scanf("%f", &notas[i]);
        media = media + notas[i];
    }
    media = media / qdtNotas;

    printf("A media das notas eh: %.2f", media);

    free(notas);

    return 0;
}
