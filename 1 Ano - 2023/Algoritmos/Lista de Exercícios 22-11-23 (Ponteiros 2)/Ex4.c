/*Faça um programa que leia três valores inteiros e chame uma função que receba estes 3
valores de entrada e os ordene, ou seja, o menor valor na primeira variável, o segundo
menor valor na variável do meio, e o maior valor na última variável. No programa principal,
exibir os valores ordenados na tela.*/

#include <stdio.h>
#include <stdlib.h>

void ordenar(int *a, int *b, int *c){
    int temp;

    if(*a > *b){
        temp = *a;
        *a = *b;
        *b = temp;
    }
    if(*b > *c){
        temp = *b;
        *b = *c;
        *c = temp;
    }
}

int main() {
    int a, b, c;

    printf("Digite o primeiro valor: ");
    scanf("%d", &a);

    printf("Digite o segundo valor: ");
    scanf("%d", &b);

    printf("Digite o terceiro valor: ");
    scanf("%d", &c);

    ordenar(&a, &b, &c);

    printf("Valores ordenados: %d, %d, %d\n", a, b, c);
}
