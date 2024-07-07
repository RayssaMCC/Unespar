/*5. Faça um programa que receba o valor de cachê de um show e o preço do ingresso para
este show. Considere que o preço do ingresso é único. O programa deverá calcular e
mostrar a quantidade de convites que devem ser vendidos para que pelo menos o custo do
cachê seja alcançado.*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
   float cache = 0, ingresso = 0;
   
   printf("Insira o custo do cache: ");
   scanf("%f", &cache);
   printf("Insira o preco do ingresso: ");
   scanf("%f", &ingresso);
   
   int convites = ceil(cache / ingresso);
   printf("Devem ser vendidos %d convites para cobrir o cache", convites);
}
