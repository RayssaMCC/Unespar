#include <stdio.h>
#include <stdlib.h>

int main(){

    int valor = 27;
    int *ptr;// declarando o ponteiro.
    ptr = &valor;/* fazendo com que o ponteiro 'ptr' aponte para a variável 'valor',
                    por isso o ponteiro deve ser do mesmo tipo que a variável para o qual ele esta apontando.*/

    printf("Utilizando ponteiros\n\n");

    printf("conteúdo da variável valor: %d\n", valor);/* conteúdo armazenado na variável valor*/
    printf("Endereço da variável vlor: %x\n", &valor);/* Aqui o endereço da variável valor, %x mostra valores hexadecimais*/
    printf("Conteúdo da variável ponteiro ptr: %x\n", ptr);/* mostra o que esta armazenado no ponteiro*/
}
