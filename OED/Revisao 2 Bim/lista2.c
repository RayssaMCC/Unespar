#include <stdio.h>
#include <stdlib.h>

//Estrutura do nó
typedef struct elemento {
    int dado;
    struct elemento *prox;
} Elem;

//Estrutura da lista
typedef struct elemento *Lista;

//Função que cria uma lista
Lista *criar_lista(){
    Lista *list = (Lista*)malloc(sizeof(Lista)); //Aloca memória para a nova lista
    if(list != NULL){
        *list = NULL; //A lista é nula
    }
    return list; //Retorna a nova lista
}

//Função que insere um nó no início da lista
int inserir_inicio(Lista *list, int dado){
    if(list == NULL) return 0; //Se a lista for nula, retorna 0
    Elem *no = (Elem*)malloc(sizeof(Elem)); //Aloca memória para o novo nó
    if(no == NULL) return 0; //Se o novo nó for nulo, retorna 0
    no->dado = dado; //Atribui o dado ao novo nó
    no->prox = *list; //O próximo nó do novo nó é a lista
    *list = no; //A lista agora é o novo nó
    return 1;
}

//Função que insere um nó no final da lista
int inserir_fim(Lista *list, int dado){
    if(list == NULL) return 0; //Se a lista for nula, retorna 0
    Elem *no = (Elem*)malloc(sizeof(Elem)); //Aloca memória para o novo nó
    if(no == NULL) return 0; //Se o novo nó for nulo, retorna 0
    no->dado = dado; //Atribui o dado ao novo nó
    no->prox = NULL; //O próximo nó do novo nó é nulo

    if(*list == NULL){
        *list = no; //Se a lista for nula, o novo nó é o início da lista
    } else {
        Elem *aux = *list; //nó auxiliar pra percorrer a lista
        while (aux->prox != NULL) {
            aux = aux->prox; //Percorre a lista até o último nó
        }
        aux->prox = no; //O próximo nó do último nó é o novo nó
    }
    return 1;
}

//Função que insere um nó de forma ordenada
int inserir_ordenado(Lista *list, int dado){
    if(list == NULL) return 0; //Se a lista for nula, retorna 0
    Elem *no = (Elem*)malloc(sizeof(Elem)); //Aloca memória para o novo nó
    if(no == NULL) return 0; //Se o novo nó for nulo, retorna 0
    no->dado = dado; //Atribui o dado ao novo nó

    if(*list == NULL || (*list)->dado >= dado){
        no->prox = *list; //Se a lista for nula ou o dado for menor que o primeiro nó, o novo nó é o início da lista
        *list = no; //A lista agora é o novo nó
    } else {
        Elem *ant = *list; //nó anterior ao nó auxiliar
        Elem *atual = (*list)->prox; //nó auxiliar
        while (atual != NULL && atual->dado < dado){
            ant = atual; //Percorre a lista até encontrar o nó que o dado é menor
            atual = atual->prox;
        }
        no->prox = atual; //O nó que o dado é menor é o próximo nó do novo nó
        ant->prox = no; //O nó anterior ao nó que o dado é menor é o novo nó
    }
    return 1;
}

//Função que remove um nó do início da lista
int remover_inicio(Lista *list){
    if(list == NULL) return 0; //Se a lista for nula, retorna 0
    if(*list == NULL) return 0; //Se a lista for vazia, retorna 0
    Elem *no = *list; //nó auxiliar
    *list = no->prox; //O próximo nó da lista é o próximo nó do nó auxiliar
    free(no); //Libera a memória do nó auxiliar
    return 1;
}

//Função que remove um nó do final da lista
int remover_fim(Lista *list){
    if(list == NULL) return 0; //Se a lista for nula, retorna 0
    if(*list == NULL) return 0; //Se a lista for vazia, retorna 0
    Elem *ant, *no = *list; //nó anterior e nó auxiliar
    while (no->prox != NULL) {
        ant = no; //Percorre a lista até o último nó
        no = no->prox;
    }
    if(no == *list){
        *list = no->prox; //Se o nó for o início da lista, o próximo nó é o início da lista
    } else {
        ant->prox = no->prox; //O próximo nó do nó anterior ao último nó é nulo
    }
    free(no); //Libera a memória do último nó
    return 1;
}

//Função que remove um nó de forma ordenada
int remover_ordenado(Lista *list, int dado){
    if(list == NULL) return 0; //Se a lista for nula, retorna 0
    Elem *ant, *no = *list; //nó anterior e nó auxiliar
    while (no != NULL && no->dado != dado){
        ant = no; //Percorre a lista até encontrar o nó com o dado
        no = no->prox;
    }
    if(no == NULL) return 0; //Se o nó for nulo, retorna 0
    if(no == *list){
        *list = no->prox; //Se o nó for o início da lista, o próximo nó é o início da lista
    } else {
        ant->prox = no->prox; //O próximo nó do nó anterior ao nó com o dado é o próximo nó do nó com o dado
    }
    free(no); //Libera a memória do nó com o dado
    return 1;
}

//Função que imprime a lista
void imprimir_lista(Lista *list){
    if(list == NULL) return; //Se a lista for nula, retorna
    Elem *no = *list; //nó auxiliar
    while (no != NULL) {
        printf("%d ", no->dado); //Imprime o dado do nó
        no = no->prox; //Percorre a lista
    }
}

int main(){
    Lista *list = criar_lista(); //Cria uma nova lista
    if(list == NULL) return 0; //Se a lista for nula, retorna 0

    printf("Inserindo lista: ");
    inserir_inicio(list, 1); //Insere um nó no início da lista
    inserir_inicio(list, 2); //Insere um nó no início da lista
    inserir_fim(list, 3); //Insere um nó no final da lista
    inserir_fim(list, 4); //Insere um nó no final da lista
    inserir_ordenado(list, 5); //Insere um nó de forma ordenada
    inserir_ordenado(list, 6); //Insere um nó de forma ordenada
    imprimir_lista(list); //Imprime a lista

    printf("\nRemovendo lista: ");
    remover_inicio(list); //Remove um nó do início da lista
    remover_ordenado(list, 4); //Remove um nó de forma ordenada
    remover_fim(list); //Remove um nó do final da lista
    imprimir_lista(list); //Imprime a lista

    return 0;
}