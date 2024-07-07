/*4. João comprou um saco de ração com peso em quilos. João possui dois gatos para os
quais fornece a quantidade de rações em gramas. Faça um programa que receba o peso do
saco de ração comprado por João e a quantidade de ração fornecida para cada gato.
Calcule e mostre quanto restará de ração no saco após 3 dias.*/

#include <stdio.h>
#include <stdlib.h>

int main() {
   float saco = 0, gramas1 = 0, gramas2 = 0;
   printf("Insira o peso do saco de racao em kg: ");
   scanf("%f", &saco);
   float sacograma = saco*1000;
   
   printf("Insira a quantidade de racao em gramas para cada gato por dia: ");
   scanf("%f", &gramas1);
   scanf("%f", &gramas2);
   
   float saco3diasg = sacograma - ((gramas1+gramas2)*3);
   float saco3diaskg = saco3diasg / 1000;
   printf("Sobrara %.2f gramas ou %.2f kg de racao apos 3 dias", saco3diasg, saco3diaskg);
}
