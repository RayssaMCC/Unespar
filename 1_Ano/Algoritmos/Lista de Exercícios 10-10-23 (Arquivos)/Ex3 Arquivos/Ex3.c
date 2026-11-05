/*3. Faça um programa que salvará dados de alunos em arquivos. Um aluno será
composto pelos seguintes campos: numero, nome, curso, nota1, nota2. Cada campo
será informado pelo usuário. O seu programa deverá criar um arquivo chamado
NomeDoAluno.txt (haverá um arquivo por aluno) e salvar as informações do aluno
neste arquivo. Teste seu programa com 3 alunos.*/

#include <stdio.h>
#include <stdlib.h>

struct cadastro {
    int numero;
    char nome[100];
    char curso[100];
    float nota1;
    float nota2;
};

typedef struct cadastro infos;

int main() {
    infos aluno;
    char nomeArquivo[100];
    
    printf("Informe os dados do aluno:\n");
        
    printf("\nNumero do aluno: ");
    scanf("%d", &aluno.numero);
	fflush(stdin);
        
    printf("Nome do aluno: ");
	gets(aluno.nome);
	fflush(stdin);
        
    printf("Curso do aluno: ");
    gets(aluno.curso);
	fflush(stdin);

    printf("Nota 1: ");
    scanf("%f", &aluno.nota1);
    fflush(stdin);
        
    printf("Nota 2: ");
    scanf("%f", &aluno.nota2);

    snprintf(nomeArquivo, 100, "%s.txt", aluno.nome); //pega do file e passa no arquivo ?
        
    FILE *arq = fopen(nomeArquivo, "w");

    if(arq == NULL){
		printf("Erro ao criar o arquivo para o aluno %s\n", aluno.nome);
		return 1;
    }

    fprintf(arq, "Número: %d\n", aluno.numero);
    fprintf(arq, "Nome: %s\n", aluno.nome);
    fprintf(arq, "Curso: %s\n", aluno.curso);
    fprintf(arq, "Nota 1: %.2f\n", aluno.nota1);
    fprintf(arq, "Nota 2: %.2f\n", aluno.nota2);
    
    fclose(arq);

    printf("\nDados do aluno salvos com sucesso!");
    return 0;
}

