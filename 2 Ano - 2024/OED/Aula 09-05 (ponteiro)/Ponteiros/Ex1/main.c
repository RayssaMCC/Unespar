#include <stdio.h>
#include <stdlib.h>

int main(){

    int valor = 27;
    int *ptr;// declarando o ponteiro.
    ptr = &valor;/* fazendo com que o ponteiro 'ptr' aponte para a vari�vel 'valor',
                    por isso o ponteiro deve ser do mesmo tipo que a vari�vel para o qual ele esta apontando.*/

    printf("Utilizando ponteiros\n\n");

    printf("conte�do da vari�vel valor: %d\n", valor);/* conte�do armazenado na vari�vel valor*/
    printf("Endere�o da vari�vel vlor: %x\n", &valor);/* Aqui o endere�o da vari�vel valor, %x mostra valores hexadecimais*/
    printf("Conte�do da vari�vel ponteiro ptr: %x\n", ptr);/* mostra o que esta armazenado no ponteiro*/
}
