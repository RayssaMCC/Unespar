/*5. Fa�a um programa que receba o valor de cach� de um show e o pre�o do ingresso para
este show. Considere que o pre�o do ingresso � �nico. O programa dever� calcular e
mostrar a quantidade de convites que devem ser vendidos para que pelo menos o custo do
cach� seja alcan�ado.*/

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
