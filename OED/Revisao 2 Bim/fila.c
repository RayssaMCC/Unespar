/*Fila dinâmica*/

#include <stdio.h>
#include <stdlib.h>

typedef struct fila {
    struct elemento *inicio;
    struct elemento *fim;
} Fila;

typedef struct elemento {
    int dado;
    struct elemento *prox;
} Elem;

//Função que cria uma fila
Fila *criar_fila(){
    Fila *fila = (Fila*)malloc(sizeof(Fila));
    if (fila != NULL){
        fila->inicio = NULL;
        fila->fim = NULL;
    }
    return fila;
}

//Função que insere um nó no final da fila
int inserir_fila(Fila *fila, int dado){
    if(fila == NULL) return 0;
    Elem *no = (Elem*)malloc(sizeof(Elem));
    if(no == NULL) return 0;
    no->dado = dado; 
    no->prox = NULL;
    if(fila->fim == NULL){ //Se a fila estiver vazia
        fila->inicio = no;
    } else {               //Se a fila não estiver vazia
        fila->fim->prox = no;
    }
    fila->fim = no;
    return 1;
}

//Função que remove um nó do início da fila
int remover_fila(Fila *fila){
    if(fila == NULL) return 0;
    if(fila->inicio == NULL) return 0; //Se a fila estiver vazia
    Elem *no = fila->inicio;
    fila->inicio = fila->inicio->prox; //O início da fila agora é o próximo nó
    if(fila->inicio == NULL){ //Se a fila ficar vazia
        fila->fim = NULL;
    }
    free(no);
    return 1;
}

//Função que imprime a fila
void imprimir_fila(Fila *fila){
    if(fila == NULL) return;
    Elem *no = fila->inicio;
    while (no != NULL){
        printf("%d ", no->dado);
        no = no->prox;
    }
}

int main(){
    Fila *fila = criar_fila();
    if(fila == NULL) return 0;

    printf("Inserindo fila: ");
    inserir_fila(fila, 1);
    inserir_fila(fila, 2);
    inserir_fila(fila, 3);
    inserir_fila(fila, 4);
    inserir_fila(fila, 5);
    imprimir_fila(fila);

    printf("\nRemovendo fila: ");
    remover_fila(fila);
    remover_fila(fila);
    imprimir_fila(fila);

    return 0;
}