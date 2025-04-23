#include <stdio.h>
#include <stdlib.h>

struct ficha_aluno{
    char nome[40];
    float nota[5];
};
typedef struct ficha_aluno Ficha;

int main(){
    Ficha aluno[5];

    printf("---------CADASTRO---------\n\n");
    // Leitura do nome e nota de cada aluno
    for(int i = 0; i<5; i++) {
        printf("Nome do aluno: ");
        fflush(stdin);
        fgets(aluno[i].nome, 40, stdin);

        for(int j = 0; j<2; j++) {
            printf("Informe a nota %d do aluno: ", j + 1);
            scanf("%f", &aluno[i].nota[j]);
        }
    }

    printf("\nLendo dados da struct:\n\n");
    // Impressão dos dados de cada aluno
    for(int i = 0; i<5; i++) {
        printf("Nome........ %s", aluno[i].nome);
        for(int j = 0; j<2; j++) {
            printf("Nota %d....... %.2f\n", j + 1, aluno[i].nota[j]);
        }
        printf("\n");
    }
}
