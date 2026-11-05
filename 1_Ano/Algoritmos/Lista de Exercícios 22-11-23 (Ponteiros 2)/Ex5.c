/*Considere a seguinte declaração: int A, *B, **C, ***D; Escreva um programa que leia a
variável A e calcule e exiba o dobro, o triplo e o quádruplo desse valor utilizando apenas os
ponteiros B, C e D. O ponteiro B deve ser usada para calcular o dobro, C o triplo e D o
quádruplo.*/

#include <stdio.h>
#include <stdlib.h>

int main(){
    int a;

    printf("Digite um valor inteiro: ");
    scanf("%d", &a);

    int *B = &a;
    int *C = &a;
    int *D = &a;

    *B = 2 * (*B);
    *C = 3 * (*C);
    *D = 4 * (*D);

    printf("Dobro: %d\n", *B);
    printf("Triplo: %d\n", *C);
    printf("Quadruplo: %d\n", *D);
}

