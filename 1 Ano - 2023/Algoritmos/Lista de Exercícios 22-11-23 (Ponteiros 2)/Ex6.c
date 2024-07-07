/*Implemente uma fun��o que calcule a �rea da superf�cie e o volume de uma esfera de
raio R. O resultado deve ser mostrado no programa principal. Al�m disso, a fun��o deve
obedecer ao prot�tipo:
void calc_esfera(float R, float *area, float *volume)
A �rea da superf�cie e o volume s�o dados, respectivamente, por:
A = 4 * pi * R^2
V = 4/3 * pi * R^3*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void calc_esfera(float R, float *area, float *volume){
    *area = 4 * 3.14 * pow(R,2);
    *volume = (4/3) * 3.14 * pow(R,3);
}

int main(){
    float R, area, volume;

    printf("Digite o raio da esfera: ");
    scanf("%f", &R);

    calc_esfera(R, &area, &volume);

    printf("\nArea da superficie: %.2f \nVolume da esfera: %.2f\n", area, volume);
}
