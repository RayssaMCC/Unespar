#include <stdio.h>
#include <stdlib.h>

int main(){
    int *v;
    int n;

    printf("Digite o tamanho do vetor:\n");
    scanf("%d", &n);
    v = malloc(n*sizeof(int)); //aloca memória para o vetor

    printf("------------------------\n");

    printf("Insercao de elementos:\n");
    for(int i = 0; i<n; i++){
        scanf("%d", &v[i]);
    }

    printf("------------------------\n");

    printf("Impressao do vetor:\n");
    for(int i = 0; i<n; i++){
        printf("%d ", v[i]);
    }
    free(v); //libera a memória alocadaa
}
