#include <stdio.h>
#include <stdlib.h>

struct ficha_aluno{ //tipos de dado
    int numero;
    char nome[40];
    float nota;
};
typedef struct ficha_aluno Ficha;

int main(){
    Ficha aluno;

    printf("---------CADASTRO---------\n\n");

    printf("Nome do aluno: ");
    fflush(stdin);
    fgets(aluno.nome,40,stdin); //uso da estrutura

    printf("Digite o numero do aluno: ");
    scanf("%d", &aluno.numero);

    printf("Informe a nota do aluno: ");
    scanf("%f", &aluno.nota);

    printf("\nLendo dados da struct:\n\n");

    printf("Nome........ %s", aluno.nome);
    printf("Numero........ %d\n", aluno.numero);
    printf("Nota........ %.2f", aluno.nota);
}
