/*Lista dinâmica que insere e remove dados*/

#include <stdio.h>
#include <stdlib.h>

//Estrutura do nó
typedef struct No {
    int num;
    struct No *prox;
} no;

no *criar_no(){
    no *novo = (no*)malloc(sizeof(no)); //Aloca memória para o novo nó
    if(novo != NULL){
        novo->prox = NULL; //O próximo nó é nulo
    }
    return novo; //Retorna o novo nó
}

//Função que insere um nó no início da lista
no *inserir_inicio(no *lista, int dado){
    no *novo_no = criar_no(); //Cria um novo nó
    if(novo_no == NULL) return lista; 
    novo_no->num = dado; //Atribui o dado ao novo nó
    novo_no->prox = lista; //O próximo nó do novo nó é a lista
    return novo_no; //Retorna o novo nó, que agora é o início da lista
}

//Função que insere um nó no final da lista
no *inserir_fim(no *lista, int dado){
    no *novo_fim = criar_no();
    if (novo_fim == NULL) return lista;
    novo_fim->num = dado; //Atribui o dado ao novo nó

    if (lista == NULL) {
        return novo_fim; //Se a lista for nula, o novo nó é o início da lista
    } else {
        no *aux = lista; //nó auxiliar pra percorrer a lista
        while (aux->prox != NULL) {
            aux = aux->prox; //Percorre a lista até o último nó
        }
        aux->prox = novo_fim; //O próximo nó do último nó é o novo nó
    }
    return lista; //Retorna a lista com o novo nó no final
}

//Função que insere um nó de forma ordenada
no *inserir_ordenado( no *lista, int dado){
    no *novo_no = criar_no();
    if (novo_no == NULL) return lista;
    novo_no->num = dado; //Atribui o dado ao novo nó

    if (lista == NULL || lista->num >= dado){
        novo_no->prox = lista; //Se a lista for nula ou o dado for menor que o primeiro nó, o novo nó é o início da lista
    } else {
        no *aux = lista; //nó auxiliar pra percorrer a lista
        while (aux->prox != NULL && aux->prox->num < dado){
            aux = aux->prox; //Percorre a lista até encontrar o nó que o dado é menor
        }
        novo_no->prox = aux->prox; //O nó que o dado é menor é o próximo nó do novo nó
        aux->prox = novo_no; //O nó anterior ao nó que o dado é menor é o novo nó
    }
    return lista; //Retorna a lista com o novo nó inserido
}

//Função que remove um nó do início da lista
no *remover_inicio(no *lista){
    if (lista == NULL) return lista; //Se a lista for nula, retorna a lista
    no *aux = lista; //nó auxiliar pra percorrer a lista
    lista = lista->prox; //O início da lista é o próximo nó
    free(aux); //Libera a memória do nó removido
    return lista; //Retorna a lista sem o nó removido
}

//Função que remove um nó do final da lista
no *remover_fim(no *lista){
    if (lista == NULL) return lista; //Se a lista for nula, retorna a lista
    if (lista->prox == NULL) {
        free(lista); //Se a lista tiver apenas um nó, libera a memória do nó
        return NULL; //Retorna a lista nula
    }
    no *aux = lista; //nó auxiliar pra percorrer a lista
    no *aux2 = lista->prox; //nó auxiliar pra percorrer a lista
    while (aux2->prox != NULL) {
        aux = aux->prox; //Percorre a lista até o penúltimo nó
        aux2 = aux2->prox; //Percorre a lista até o último nó
    }
    aux->prox = NULL; //O próximo nó do penúltimo nó é nulo
    free(aux2); //Libera a memória do último nó
    return lista; //Retorna a lista sem o último nó
}

//Função que remove um nó de forma ordenada
no *remover_ordenado(no *lista, int dado){
    if (lista == NULL) return lista; //Se a lista for nula, retorna a lista
    no *aux = lista; //nó auxiliar pra percorrer a lista
    if (lista->num == dado) {
        lista = lista->prox; //Se o dado for igual ao primeiro nó, o início da lista é o próximo nó
        free(aux); //Libera a memória do nó removido
        return lista; //Retorna a lista sem o nó removido
    }
    while (aux->prox != NULL && aux->prox->num != dado) {
        aux = aux->prox; //Percorre a lista até encontrar o nó com o dado
    }
    if (aux->prox == NULL) return lista; //Se o próximo nó for nulo, retorna a lista
    no *aux2 = aux->prox; //nó auxiliar pra percorrer a lista
    aux->prox = aux2->prox; //O próximo nó do nó anterior ao nó com o dado é o próximo nó do nó com o dado
    free(aux2); //Libera a memória do nó removido
    return lista; //Retorna a lista sem o nó removido
}

//Função para imprimir a lista
void imprimir_lista(no *lista){
    no *aux = lista; //nó auxiliar pra percorrer a lista
    while (aux != NULL) {
        printf("%d ", aux->num); //Imprime o número do nó
        aux = aux->prox; //Percorre a lista
    }
    printf("\n");
}

int main(){
    no *lista = NULL; //Cria uma lista nula
    printf("inserindo na lista: ");
    lista = inserir_inicio(lista, 1); //Insere o número 1 no início da lista
    lista = inserir_inicio(lista, 2); //Insere o número 2 no início da lista
    lista = inserir_fim(lista, 3); //Insere o número 3 no final da lista
    lista = inserir_fim(lista, 4); //Insere o número 4 no final da lista
    lista = inserir_ordenado(lista, 5); //Insere o número 5 de forma ordenada
    lista = inserir_ordenado(lista, 0); //Insere o número 0 de forma ordenada
    imprimir_lista(lista); //Imprime a lista
    printf("removendo da lista: ");
    lista = remover_inicio(lista); //Remove o primeiro nó da lista
    lista = remover_fim(lista); //Remove o último nó da lista
    lista = remover_ordenado(lista, 3); //Remove o nó com o número 3
    imprimir_lista(lista); //Imprime a lista
    return 0;
}