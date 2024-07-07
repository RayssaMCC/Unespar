/*Escreva uma sub-rotina medidas_retangulo, com o prot�tipo abaixo, que: recebe dois
par�metros com as medidas dos lados de um ret�ngulo; calcula a �rea e o per�metro deste
ret�ngulo; altera os conte�dos dos par�metros com os valores da �rea e do per�metro
calculados

void medidas_retangulo(double*var1,double*var2);*/

#include <stdio.h>
#include <stdlib.h>

#include <stdio.h>
#include <stdlib.h>

void medidas_retangulo(double *var1,double *var2){
    double area, per;
    area = (*var1) * (*var2);
    per = 2 * (*var1 + *var2);

    *var1 = area;
    *var2 = per;
}

int main(){
    double altura, base;

    printf("Digite a altura e a base do retangulo respectivamente: \n");
    scanf("%lf %lf", &altura, &base);

    medidas_retangulo(&altura, &base);

    printf("\nArea do retangulo: %.2lf\nPerimetro do retangulo: %.2lf\n", altura, base);
}
