/*3. Fa�a um programa que calcule a �rea de um c�rculo recebendo o valor do seu raio. �rea
do c�rculo = pi * raio^2*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    float r = 0;
    printf("Insira o valor do raio: ");
    scanf("%f", &r);
    float area = 3.14*pow(r, 2);
    printf("A area do circulo sera: %.2f", area);
}
