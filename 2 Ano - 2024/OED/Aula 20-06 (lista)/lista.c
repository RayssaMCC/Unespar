/*1 - criar menu da lista (impress�o, ordenar. come�o, fim, contagem)
2 - contagem de n�s
3 - criar um m�todo para fazer a m�dia dos n�meros inseridos nos n�s*/


#include <stdio.h>
#include <stdlib.h>

typedef struct No{
    int num;
    struct No *prox; //ponteiro que aponta para algo que n�o foi definido ainda, inicio da lista
}no;

no *criar_no(){ //fun��o para alocar mem�ria dinamicamente
    no *novo = (no*)malloc(sizeof(no));//alocado mem�ria din�mica para o ponteiro n�
    return novo;
}

no *inserir_no_inicio(no *lista, int dado){ //fun��o para fazer com que a lista aponte para no, dado � um valor num�rico para preencher o n�
    no *novo_no = criar_no(); //recebe o return do criar_no()
    novo_no->num = dado; //atribuiu um n�mero(dado) para o inicio da lista

    if(lista == NULL){ //existem duas possibilidades: a lista estar vazia ou n�o
        lista = novo_no; //o ponteiro lista aponta para o ponteiro novo_no
        novo_no->prox = NULL; //o ponteiro novo_no aponta para o ponteiro prox
    }
    else{ //lista encadeada, cria uma nova lista na frente de lista
        novo_no->prox = lista;
        lista = novo_no;
    }
    return lista;
}

no *inserir_elemento_fim(no *lista, int dado){ //basicamente a mesma fun��o do inserir_no_inicio(), mas agora no final
    no *novo_fim = criar_no();
    novo_fim->num = dado;

    if(lista == NULL){ //�nico elemento da lista
        lista = novo_fim;
        novo_fim->prox = NULL;
    }
    else{
        no *aux = lista;

        while(aux->prox != NULL){
            aux = aux->prox;
        }
        novo_fim->prox = NULL;
        aux->prox = novo_fim;
    }
    return lista;
}

void imprimirLista(no *lista){
    no *aux = lista; //o auxiliar percorre a lista para que nenhum dado da lista seja perdido

    while(aux != NULL){ //a vari�vel num na fun��o inserir_no_inicio � atribuida ao ponteito novo_no
        printf("%d ", aux->num);
        aux = aux->prox;
    }
}

no *remover(no *lista, int dado){
    if(lista == NULL){ //lista vazia
        return NULL;
    }

    no *temp = lista;
    no *prev = NULL;

    if(temp != NULL && temp->num == dado){
        lista = temp->prox; //muda a cabe�a da lista para o pr�ximo n�
        free(temp); //libera a mem�ria do n�
        return lista;
    }

    while(temp != NULL && temp->num != dado){
        prev = temp;
        temp = temp->prox;
    }

    if(temp == NULL){
        return lista;
    }

    prev->prox = temp->prox;
    free(temp);

    return lista;
}

no *inserir_ordenado(no *lista, int dado){
    no *novoNo = malloc(sizeof(no)); //reserva mem�ria para a struct
    novoNo->num = dado;
    novoNo->prox = NULL;

    if(lista == NULL || lista->num >= dado){
        novoNo->prox = lista;
        lista = novoNo;

        return novoNo;
    }

    no *anterior = NULL;
    no *atual = lista;
    while(atual != NULL && atual->num < dado){
        anterior = atual;
        atual = atual->prox;
    }

    novoNo->prox = atual;
    anterior = atual->prox;

    return lista;
}

no *buscar(no *lista, int dado){
    no *atual = lista;
    while(atual != NULL){ //Percorre a lista
        if(atual->num == dado){
            return atual;
        }
        atual = atual->prox;
    }
    return NULL;
}

void liberar_lista(no *lista){
    no *atual = lista;
    no *prox_no;

    while(atual != NULL){
        prox_no = atual->prox;
        free(atual);
        atual = prox_no;
    }
}

int main(){
    no *lista = NULL; //criando um ponteiro de lista que aponta para null

    /*for(int i = 1; i<=10; i++){
        lista = inserir_no_inicio(lista, i);
    }
    lista = inserir_elemento_fim(lista, 30);
    imprimirLista(lista);

    printf("\n");
    printf("Escolha um numero entre os anteriores para ser excluido: ");
    int escolha;
    scanf("%d", &escolha);
    lista = remover(lista, escolha);
    imprimirLista(lista);*/

    lista = inserir_ordenado(lista, 3);
    lista = inserir_ordenado(lista, 2);
    lista = inserir_ordenado(lista, 1);
    imprimirLista(lista);

    return 0;
}

/*
case 6:
    printf("Digite o dado a ser buscado: ");
    scanf("%d", &dado);
    resultado = buscar(lista, dado);
    if(resultado != NULL){
        printf("Dado %d encontrado na lista.", dado);
    }
    else{
        printf("Dado %d nao encontrado na lista.", dado);
    }
    break
/*
