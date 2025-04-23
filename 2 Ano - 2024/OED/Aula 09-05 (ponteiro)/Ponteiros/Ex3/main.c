#include <stdio.h>
#include <stdlib.h>

int main(){
    int x = 0, *ptrx, **pptrx;

    printf("Valor de x: %d\n", x);
    printf("Endereco de x: %x\n\n", &x);

    ptrx = &x;
    pptrx = &ptrx;

    *ptrx = *ptrx + 10; //x se tornar� 10, pois o valor apontado por ptrx (o pr�prio x) recebeu +10
    printf("Novo valor de x: %d\n", x);
    printf("Endereco apontado por ptrx: %x\n", ptrx); //mostra o endere�o de mem�ria do que est� apontando (nesse caso o 'x')
    printf("Valor de x que esta sendo apontado por ptrx: %d\n", *ptrx); //mostra valor de x
    printf("Endereco de memoria da variavel ptrx: %x\n\n", &ptrx); //mostra o endere�o de mem�ria do ponteiro 'ptrx'

    **pptrx = **pptrx + 10; //o ponteiro (pptrx + 10) aponta para um ponteiro (ptrx + 10) que aponta pra x (pptrx + ptrx = 20)
    printf("Novo valor de x: %d\n", x);
    printf("Endereco apontado por pptrx: %x\n", pptrx); //mostra o endere�o de mem�ria do que est� apontando (nesse caso o 'ptrx')
    printf("Valor de x que esta sendo apontado por pptrx: %d\n", **pptrx); //mostra valor de x
    printf("Endereco de memoria da variavel pptrx: %x\n", &pptrx); //mostra o endere�o de mem�ria do ponteiro 'pptrx'
}
