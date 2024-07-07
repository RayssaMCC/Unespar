/*1. Faça um programa que receba três notas de um aluno e seus respectivos pesos. Calcule
e mostre a média ponderada dessas notas.*/

#include <stdio.h>
#include <stdlib.h>

int main() {
    float n1 = 0, n2 = 0, n3 = 0, p1 = 0, p2 = 0, p3 = 0;
    
    printf("Insira as 3 notas: ");
    scanf("%f", &n1);
    scanf("%f", &n2);
    scanf("%f", &n3);
    
    printf("Insira o peso das notas: ");
    scanf("%f", &p1);
    scanf("%f", &p2);
    scanf("%f", &p3);
    
    float mediapond = (n1*p1 + n2*p2 + n3*p3) / (p1 + p2 + p3);
    printf("A media ponderada eh: %.2f", mediapond);
}
