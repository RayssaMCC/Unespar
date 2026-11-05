/*Pilha dinâmica*/

#include <stdio.h>
#include <stdlib.h>

typedef struct elemento {
    int dado;
    struct elemento *prox;
} Elem;

typedef struct elemento *Pilha;


//Função que cria uma pilha
Pilha *criar_pilha(){
    Pilha *pilha = (Pilha*)malloc(sizeof(Pilha));
    if(pilha != NULL){
        *pilha = NULL;
    }
    return pilha;
}

//Função que insere um nó no início da pilha
int inserir_pilha(Pilha *pilha, int dado){
    if(pilha == NULL) return 0;
    Elem *no = (Elem*)malloc(sizeof(Elem));
    if(no == NULL) return 0;
    no->dado = dado;
    no->prox = *pilha;
    *pilha = no;
    return 1;
}

//Função que remove um nó do início da pilha
int remover_pilha(Pilha *pilha){
    if(pilha == NULL) return 0;
    if(*pilha == NULL) return 0;
    Elem *no = *pilha;
    *pilha = no->prox;
    free(no);
    return 1;
}

//Função que imprime a pilha
void imprimir_pilha(Pilha *pilha){
    if(pilha == NULL) return;
    Elem *no = *pilha;
    while (no != NULL){
        printf("%d ", no->dado);
        no = no->prox;
    }
    printf("\n");
}

int main(){
    Pilha *pilha = criar_pilha();
    printf("Inserindo na pilha: ");
    inserir_pilha(pilha, 1);
    inserir_pilha(pilha, 2);
    inserir_pilha(pilha, 3);
    imprimir_pilha(pilha);

    printf("Removendo da pilha: ");
    remover_pilha(pilha);
    imprimir_pilha(pilha);
    return 0;
}