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

//Função para remover um nó da arvore
No* remover(No *raiz, int chave, int sucessor) {
    if (raiz == NULL) { //Quando a raiz é nula ou não existe arvore
        printf("Valor nao encontrado\n");
        return NULL;
    } else { //Quando a raiz não é nula
        if (raiz->conteudo == chave) { //Quando o valor é encontrado
            if (raiz->esquerda == NULL && raiz->direita == NULL) { //Nó folha (sem filhos)
                if (!sucessor) //Não imprime se for o sucessor
                    printf("Elemento folha removido: %d\n", chave);
                free(raiz);
                return NULL;
            } else if (raiz->esquerda == NULL) { //Tem apenas filho à direita
                No *temp = raiz->direita;
                if (!sucessor) //Não imprime se for o sucessor
                    printf("Elemento com um filho (direita) removido: %d\n", chave);
                free(raiz);
                return temp;
            } else if (raiz->direita == NULL) { //Tem apenas filho à esquerda
                No *temp = raiz->esquerda;
                if (!sucessor) //Não imprime se for o sucessor
                    printf("Elemento com um filho (esquerda) removido: %d\n", chave);
                free(raiz);
                return temp;
            } else { //Tem dois filhos
                No *temp = raiz->direita;
                //Encontra o menor valor na subárvore direita (sucessor in-order)
                while (temp->esquerda != NULL) {
                    temp = temp->esquerda;
                }
                // Substitui o conteúdo do nó pelo sucessor
                printf("Elemento com dois filhos removido: %d\n", chave);
                
                raiz->conteudo = temp->conteudo;
                //Remove o nó sucessor da subárvore direita, sem imprimir mensagens
                raiz->direita = remover(raiz->direita, temp->conteudo, 1); //Passa o flag 1 indicando que é sucessor
                return raiz;
            }
        } else { //Quando o valor não é encontrado no nó atual
            if (chave < raiz->conteudo) { //Busca na subárvore esquerda
                raiz->esquerda = remover(raiz->esquerda, chave, sucessor);
            } else { //Busca na subárvore direita
                raiz->direita = remover(raiz->direita, chave, sucessor);
            }
            return raiz;
        }
    }
}

//Função principal
int main(){
    int op, valor;
    ArvB *arv = (ArvB*)malloc(sizeof(ArvB));
    arv->raiz = NULL;

    //Menu de opções
    do{
        printf("\nEscolha uma opcao:\n");
        printf("1. Inserir valor\n");
        printf("2. Remover valor\n");
        printf("3. Imprimir em ordem\n");
        printf("4. Imprimir em pre ordem\n");
        printf("5. Imprimir em pos ordem\n");
        printf("0. Sair\n");
        scanf("%d", &op);

        switch(op){
            case 1:
                printf("\nDigite o valor a ser inserido: ");
                scanf("%d", &valor);
                inserir(arv, valor);
                break;
            case 2:
                printf("\nDigite o valor a ser removido: ");
                scanf("%d", &valor);
                arv->raiz = remover(arv->raiz, valor, 0);
                break;
            case 3:
                printf("\nImprimindo em ordem: ");
                imprimirOrdem(arv->raiz);
                printf("\n");
                break;
            case 4:
                printf("\nImprimindo em pre ordem: ");
                imprimirPre(arv->raiz);
                printf("\n");
                break;
            case 5:
                printf("\nImprimindo em pos ordem: ");
                imprimirPos(arv->raiz);
                printf("\n");
                break;
            case 0: 
                printf("\nSaindo...\n");
                break;
            default:
                printf("\nOpcao invalida!\n\n");
        }
    } while(op != 0);

    //Libera a memória alocada
    free(arv);
    return 0;
}