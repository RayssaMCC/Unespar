/*1 - criar menu da lista (impressão, ordenar, começo, fim, contagem)
2 - contagem de nós
3 - criar um método para fazer a média dos números inseridos nos nós

ADICIONAR AS FUNÇÕES DE BUSCAR NÓ, LIBERAR LISTA

*/

#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int num;
    struct No *prox;
} no;

//Função para criar um novo nó, inicializando o ponteiro do próximo nó como NULL
no *criar_no() {
    no *novo = (no*)malloc(sizeof(no)); //Aloca memória para o novo nó
    if (novo != NULL) {
        novo->prox = NULL;
    }
    return novo; //Retorna o novo nó criado
}

//Função para inserir um novo nó no início da lista
no *inserir_no_inicio(no *lista, int dado) {
    no *novo_no = criar_no();
    if (novo_no == NULL) return lista;
    novo_no->num = dado; //Define o dado do novo nó
    novo_no->prox = lista;
    return novo_no; // Retorna o novo nó, que agora é o primeiro da lista
}

// Função para inserir um novo nó no final da lista
no *inserir_elemento_fim(no *lista, int dado) {
    no *novo_fim = criar_no();
    if (novo_fim == NULL) return lista;
    novo_fim->num = dado;
    if (lista == NULL) {
        return novo_fim;
    } else {
        no *aux = lista;
        while (aux->prox != NULL) { //Encontra o último nó da lista
            aux = aux->prox;
        }
        aux->prox = novo_fim;
    }
    return lista; //Retorna a lista com o novo nó adicionado no final
}

//Função para imprimir todos os elementos da lista
void imprimirLista(no *lista) {
    no *aux = lista;
    while (aux != NULL) {
        printf("%d ", aux->num); //Imprime o dado do nó atual
        aux = aux->prox; //Move para o próximo nó
    }
    printf("\n");
}

//Função para remover um nó específico da lista baseado em um valor dado
no *remover(no *lista, int dado) {
    if (lista == NULL) {
        return NULL;
    }
    no *temp = lista, *prev = NULL; //Temp para percorrer a lista, prev para guardar o nó anterior
    while (temp != NULL && temp->num != dado) { //Encontra o nó a ser removido
        prev = temp;
        temp = temp->prox;
    }
    if (temp == NULL) return lista;
    if (prev == NULL) {
        lista = temp->prox;
    } else {
        prev->prox = temp->prox; //Remove o nó da lista
    }
    free(temp); //Libera a memória do nó removido
    return lista; //Retorna a lista atualizada
}

//Função para inserir um novo nó de forma ordenada na lista
no *inserir_ordenado(no *lista, int dado) {
    no *novoNo = criar_no();
    if (novoNo == NULL) return lista;
    novoNo->num = dado;
    if (lista == NULL || lista->num >= dado) {
        novoNo->prox = lista; //Se a lista estiver vazia ou o primeiro nó for maior ou igual ao dado, insere no início
        return novoNo;
    } else {
        no *aux = lista;
        while (aux->prox != NULL && aux->prox->num < dado) { //Encontra a posição de inserção
            aux = aux->prox;
        }
        novoNo->prox = aux->prox; //Insere o novo nó na posição encontrada
        aux->prox = novoNo;
    }
    return lista; //Retorna a lista atualizada
}

//Função para contar o número de nós na lista
int contar_nos(no *lista) {
    int contador = 0;
    no *aux = lista;
    while (aux != NULL) {
        contador++;
        aux = aux->prox;
    }
    return contador; //Retorna o total de nós na lista
}

//Função para calcular a média dos valores dos nós na lista
float calcular_media(no *lista) {
    if (lista == NULL) return 0.0f; //Se a lista estiver vazia, retorna 0.0
    int soma = 0, contador = 0;
    no *aux = lista; //Auxiliar para percorrer a lista
    while (aux != NULL) {
        soma += aux->num;
        contador++;
        aux = aux->prox;
    }
    if (contador == 0) return 0.0f; //Evita divisão por zero
    return (float)soma / contador; //Calcula e retorna a média
}

//Função para buscar um nó na lista pelo valor
no *buscar_no(no *lista, int valor) {
    no *aux = lista;
    while (aux != NULL) {
        if (aux->num == valor) {
            return aux; //Retorna o nó encontrado
        }
        aux = aux->prox;
    }
    return NULL; //Retorna NULL se o nó não for encontrado
}

//Função para liberar toda a memória alocada para a lista
void liberar_lista(no **lista) {
    no *aux = *lista;
    while (aux != NULL) {
        no *temp = aux;
        aux = aux->prox;
        free(temp); //Libera o nó atual
    }
    *lista = NULL; //Define a lista como NULL após liberar todos os nós
}

//Função para exibir o menu de opções e realizar operações na lista
void menu(no **lista) {
    int opcao, dado, quantidade, i;
    do {
        printf("\nMenu:\n");
        printf("1. Inserir numeros\n");
        printf("2. Imprimir lista\n");
        printf("3. Remover elemento\n");
        printf("4. Contar nos\n");
        printf("5. Calcular media\n");
        printf("6. Buscar elemento\n");
        printf("7. Liberar lista\n");
        printf("8. Sair\n");
        printf("Escolha uma opcao: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1: //Inserção de números
                printf("Quantos numeros deseja inserir? ");
                scanf("%d", &quantidade);
                for (i = 0; i < quantidade; i++) {
                    printf("Digite o numero %d: ", i + 1);
                    scanf("%d", &dado);
                    printf("Inserir no (1) Inicio, (2) Fim, (3) Ordenado? ");
                    int opcaoInserir;
                    scanf("%d", &opcaoInserir);
                    switch (opcaoInserir) {
                        case 1:
                            *lista = inserir_no_inicio(*lista, dado);
                            break;
                        case 2:
                            *lista = inserir_elemento_fim(*lista, dado);
                            break;
                        case 3:
                            *lista = inserir_ordenado(*lista, dado);
                            break;
                        default:
                            printf("Opcao invalida. Numero nao inserido.\n");
                            break;
                    }
                }
                break;
            case 2: //Impressão da lista
                imprimirLista(*lista);
                break;
            case 3: //Remoção de número
                printf("Digite um numero para remover: ");
                scanf("%d", &dado);
                *lista = remover(*lista, dado);
                break;
            case 4: //Contar nós
                printf("Total de nos na lista: %d\n", contar_nos(*lista));
                break;
            case 5: //Calcular média
                if (contar_nos(*lista) == 0) {
                    printf("Lista vazia. Nao e possivel calcular a media.\n");
                } else {
                    printf("Media dos elementos na lista: %.2f\n", calcular_media(*lista));
                }
                break;
            case 6: // Buscar elemento
                printf("Digite o valor do elemento a buscar: ");
                scanf("%d", &dado);
                no *encontrado = buscar_no(*lista, dado);
                if (encontrado != NULL) {
                    printf("Elemento %d encontrado na lista.\n", encontrado->num);
                } else {
                    printf("Elemento nao encontrado na lista.\n");
                }
                break;
            case 7: // Liberar lista
                liberar_lista(lista);
                lista = NULL;
                printf("Lista liberada.\n");
                break;
            case 8: // Sair do programa
                liberar_lista(lista); // Garante que a lista seja liberada antes de sair
                printf("Saindo do programa\n");
                break;
            default:
                printf("Opcao invalida!\n");
        }
    } while (opcao != 8);
}

int main() {
    no *lista = NULL;
    menu(&lista); //Chama a função menu passando o endereço da lista
    return 0;
}
