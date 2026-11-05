#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct{
    int dia, mes, ano;
} Data;

typedef struct{
    char nome[50];
    Data data;
} Pessoa;

typedef struct no{
    Pessoa p;
    struct no *proximo;
} No;

typedef struct{
    No *topo;
    int tam;
} Pilha;

Pessoa ler_pessoa(){
    Pessoa p;
    printf("\nDigite nome:\n");
    fgets(p.nome, 50, stdin);
    p.nome[strcspn(p.nome, "\n")] = '\0';  //Remove o \n do final da string

    printf("Digite data de nascimento (dd mm aaaa):\n");
    if(scanf("%d%d%d", &p.data.dia, &p.data.mes, &p.data.ano) != 3) {
        printf("Entrada de data invalida. Tente novamente.\n");
        while(getchar() != '\n'); //Limpando buffer de entrada
        return ler_pessoa();
    }
    while(getchar() != '\n'); //Limpa o buffer de entrada

    return p;
}

void imprimir_pessoa(Pessoa p){
    printf("\nNome: %s\nData: %02d/%02d/%04d\n", p.nome, p.data.dia, p.data.mes, p.data.ano);
}

void criar_pilha(Pilha *p){
    p->topo = NULL;
    p->tam = 0;
}

void empilhar(Pilha *p){
    No *novo = (No *)malloc(sizeof(No));

    if(novo){
        novo->p = ler_pessoa();
        novo->proximo = p->topo;
        p->topo = novo;
        p->tam++;
    } else {
        printf("\nErro ao alocar memoria\n");
    }
}

No* desempilhar(Pilha *p){
    if(p->topo){
        No *remover = p->topo;
        p->topo = remover->proximo;
        p->tam--;
        return remover;
    } else {
        printf("\nPilha vazia!\n");
    }
    return NULL;
}

void imprimir_pilha(Pilha *p){
    No *aux = p->topo;
    printf("\n----------- PILHA Tam: %d --------------\n", p->tam);
    while(aux){
        imprimir_pessoa(aux->p);
        aux = aux->proximo;
    }
    printf("\n--------- FIM PILHA ------------\n");
}

int main(){
    No *remover;
    Pilha p;
    int opcao;

    criar_pilha(&p);

    do{
        printf("\n0 - Sair\n1 - Empilhar\n2 - Desempilhar\n3 - Imprimir\n");
        scanf("%d", &opcao);
        getchar(); //Limpa o buffer de entrada

        switch(opcao){
        case 1:
            empilhar(&p);
            break;
        case 2:
            remover = desempilhar(&p);
            if(remover){
                printf("\nElemento removido com sucesso!\n");
                imprimir_pessoa(remover->p);
                free(remover);
            } else {
                printf("\nNada para remover\n");
            }
            break;
        case 3:
            imprimir_pilha(&p);
            break;
        default:
            if(opcao != 0)
                printf("\nOpcao invalida!\n");
        }
    } while(opcao != 0);

    return 0;
}