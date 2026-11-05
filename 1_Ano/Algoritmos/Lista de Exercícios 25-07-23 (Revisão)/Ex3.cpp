/*3. Faça um programa que calcule a área de um círculo recebendo o valor do seu raio. Área
do círculo = pi * raio^2*/

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
