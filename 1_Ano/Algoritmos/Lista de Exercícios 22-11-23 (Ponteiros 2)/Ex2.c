/*Elaborar um programa que leia dois valores inteiros (A e B). Em seguida, faça uma
função que retorne a soma do dobro dos dois números lidos. A função deverá armazenar o
dobro de A na própria variável A e o dobro de B na própria variável B. No programa principal
mostre o valor da soma, de A e também de B.*/

#include <stdio.h>
#include <stdlib.h>

int SomaDobro(int *a, int *b){
    *a = 2 * (*a);
    *b = 2 * (*b);

    return *a + *b;
}

int main(){
    int a, b;

    printf("Insira os valores inteiros A e B respectivamente: ");
    scanf("%d %d", &a, &b);

    int resultado = SomaDobro(&a, &b);

    printf("Soma do dobro: %d\n", resultado);
    printf("Dobro de A: %d\n", a);
    printf("Dobro de B: %d", b);

}
