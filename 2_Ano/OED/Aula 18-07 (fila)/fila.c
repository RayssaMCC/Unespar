#include <stdio.h>
#include <stdlib.h>

// Implementação de fila 
// Implementação de fila com prioridade

typedef struct no {
    int valor;
    struct no *proximo;
    int valorPrioridade;
} No;

typedef struct {
    No *inicio;
    No *final;
    int tamanho;
} Fila;

void criarFila(Fila *fila){ // Criando uma fila
    fila->inicio = NULL;
    fila->final = NULL;
    fila->tamanho = 0;
}

void inserirFilaPrioridade(Fila *fila, int num, int prioridade){
    No *novo = malloc(sizeof(No));
    if(novo != NULL){
        novo->valor = num;
        novo->proximo = NULL;
        novo->valorPrioridade = prioridade;
        if (fila->inicio == NULL){
            fila->inicio = novo;
            fila->final = novo;
        } else {
            fila->final->proximo = novo;
            fila->final = novo;
        }
        fila->tamanho++;
    } else {
        printf("\nErro ao alocar memória.\n");
    }
}

No* removerFila(Fila *fila){
    No *remover = NULL;
    if(fila->inicio != NULL){
        remover = fila->inicio;
        fila->inicio = remover->proximo;
        fila->tamanho--;
        if (fila->inicio == NULL) {
            fila->final = NULL;
        }
    } else {
        printf("\tFila Vazia!\n");
    }
    return remover;
}

void imprimirFila(Fila *fila){
    No *aux = fila->inicio;
    printf("\t----FILA----\n");
    while(aux != NULL){
        printf("Valor: %d Prioridade: %d\n", aux->valor, aux->valorPrioridade);
        aux = aux->proximo;
    }
    printf("\n\t----FIM DA FILA----\n");
}

int main(){
    No *r1, *r2;
    Fila filaPrioridade1;
    Fila filaPrioridade2;
    criarFila(&filaPrioridade1); // Inicializa uma fila
    criarFila(&filaPrioridade2);
    int valor, entradaUsuario, prioridade, removerValor, imprimirFilaPrioridade;

    do {
        printf(" 0 - Sair \n 1 - Inserir \n 2 - Remover \n 3 - Imprimir \n");
        scanf("%d", &entradaUsuario);
        switch(entradaUsuario)
        {
        case 1:
            printf("Digite um valor a ser inserido na fila: ");
            scanf("%d", &valor);
            printf("Digite a prioridade do valor inserido (1 ou 2): ");
            scanf("%d", &prioridade);
            if(prioridade == 1){
                inserirFilaPrioridade(&filaPrioridade1, valor, prioridade);
            } else if(prioridade == 2){
                inserirFilaPrioridade(&filaPrioridade2, valor, prioridade);
            } else {
                printf("Prioridade inválida.\n");
            }
            break;
        case 2:
            printf("Escolha qual fila deseja remover (1 ou 2): ");
            scanf("%d", &removerValor);
            if (removerValor == 1){
                r1 = removerFila(&filaPrioridade1);
                if (r1 != NULL) {
                    printf("Removido: %d\n", r1->valor);
                    free(r1);
                }
            } else if (removerValor == 2){
                r2 = removerFila(&filaPrioridade2);
                if (r2 != NULL) {
                    printf("Removido: %d\n", r2->valor);
                    free(r2);
                } 
            } else {
                printf("Prioridade inválida.\n");
            }
            break;
        case 3:
            printf("Escolha qual fila deseja imprimir (1 ou 2): ");
            scanf("%d", &imprimirFilaPrioridade);
            if (imprimirFilaPrioridade == 1){
                imprimirFila(&filaPrioridade1);
            } else if (imprimirFilaPrioridade == 2){
                imprimirFila(&filaPrioridade2);
            } else {
                printf("Prioridade inválida.\n");
            }
            break;
        default:
            if(entradaUsuario != 0){
                printf("Opção inválida.\n");
            }
            break;
        }
    } while (entradaUsuario != 0);

    return 0;
}