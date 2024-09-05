#include <stdio.h>
#include <stdlib.h>

typedef struct no{
    int conteudo;
    struct no *esquerda, *direita;
} No;

typedef struct ArvB{
    No *raiz;
} ArvB;

//Insere o nó na esquerda
void inserirEsquerda(No *no, int valor){
    if(no->esquerda == NULL){ //Se o nó esquerdo for NULL
        No *novo = (No*)malloc(sizeof(No));
        novo->conteudo = valor;
        novo->esquerda = NULL;
        novo->direita = NULL;
        no->esquerda = novo;
    } else {
        if(valor < no->esquerda->conteudo){ //Se o valor for menor que o conteudo do nó esquerdo
            inserirEsquerda(no->esquerda, valor); 
        } else {
            inserirDireita(no->esquerda, valor);
        }
    }
}

//Insere o nó na direita
void inserirDireita(No *no, int valor){
    if(no->direita == NULL){ //Se o nó direito for NULL
        No *novo = (No*)malloc(sizeof(No));
        novo->conteudo = valor;
        novo->esquerda = NULL;
        novo->direita = NULL;
        no->direita = novo;
    } else {
        if(valor < no->direita->conteudo){ //Se o valor for menor que o conteudo do nó direito
            inserirEsquerda(no->direita, valor); 
        } else {
            inserirDireita(no->direita, valor);
        }
    }
}

//Insere o nó na arvore, considerando direita ou esquerda
void inserir(ArvB *arv, int valor){
    if(arv->raiz == NULL){ //Se a arvore estiver vazia
        No *novo = (No*)malloc(sizeof(No));
        novo->conteudo = valor;
        novo->esquerda = NULL;
        novo->direita = NULL;
        arv->raiz = novo; //A raiz da arvore recebe o novo nó invés de ser NULL
    } else { //Se a arvore não estiver vazia
        if(valor < arv->raiz->conteudo){
            inserirEsquerda(arv->raiz, valor); //insere um valor no ponto esquerdo do nó da arvore
        } else {
            inserirDireita(arv->raiz, valor); //insere um valor no ponto direito do nó da arvore
        }
    }
}

//Função para contar os números pares
int contarPares(No *raiz){
    if(raiz == NULL) return 0;
    int contador = (raiz->conteudo % 2 == 0) ? 1 : 0;
    return contador + contarPares(raiz->esquerda) + contarPares(raiz->direita);
}

//Função para imprimir a arvore em ordem
void imprimirOrdem(No *raiz){
    if(raiz != NULL){
        imprimirOrdem(raiz->esquerda);
        printf("%d ", raiz->conteudo);
        imprimirOrdem(raiz->direita);
    }
}

//Função para imprimir a arvore em pré-ordem
void imprimirPre(No *raiz){
    if(raiz != NULL){
        printf("%d ", raiz->conteudo);
        imprimirPre(raiz->esquerda);
        imprimirPre(raiz->direita);
    }
}

//Função para imprimir a arvore em pós-ordem
void imprimirPos(No *raiz){
    if(raiz != NULL){
        imprimirPos(raiz->esquerda);
        imprimirPos(raiz->direita);
        printf("%d ", raiz->conteudo);
    }
}

int main(){
    ArvB *arv = (ArvB*)malloc(sizeof(ArvB));
    arv->raiz = NULL;

    //Insere os valores fixos da árvore
    int opcao;
    int valores[] = {50, 5, 0, 15, -5, 1, 9, 16, 984, 207, 985, 63, 807, 96};
    int n = sizeof(valores) / sizeof(valores[0]);
    for(int i = 0; i < n; i++){
        inserir(arv, valores[i]);
    }

    //Imprime valores da árvore antes da ordenação
    printf("Valores da arvore antes da ordenacao: ");
    for(int i = 0; i < n; i++){
        printf("%d ", valores[i]);
    }
    printf("\n\n");

    //Imprime e contar pares de acordo com a opção escolhida
    do{
        //Menu de opções
        printf("Escolha o metodo de impressao:\n");
        printf("1. Em ordem\n");
        printf("2. Em pre ordem\n");
        printf("3. Em pos ordem\n");
        printf("0. Sair\n");
        scanf("%d", &opcao);

        switch(opcao){
            case 1:
                printf("\nImprimindo em ordem: ");
                imprimirOrdem(arv->raiz);
                printf("\nQuantidade de pares em ordem: %d\n\n", contarPares(arv->raiz));
                break;
            case 2:
                printf("\nImprimindo em pre ordem: ");
                imprimirPre(arv->raiz);
                printf("\nQuantidade de pares em pre ordem: %d\n\n", contarPares(arv->raiz));
                break;
            case 3:
                printf("\nImprimindo em pos ordem: ");
                imprimirPos(arv->raiz);
                printf("\nQuantidade de pares em pos ordem: %d\n\n", contarPares(arv->raiz));
                break;
            case 0: 
                printf("\nSaindo...\n");
                break;
            default:
                printf("\nOpcao invalida!\n\n");
        }
    } while(opcao != 0);

    //Libera a memória alocada
    free(arv);
    return 0;
}