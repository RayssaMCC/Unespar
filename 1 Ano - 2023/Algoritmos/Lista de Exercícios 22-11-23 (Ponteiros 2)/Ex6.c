/*Implemente uma função que calcule a área da superfície e o volume de uma esfera de
raio R. O resultado deve ser mostrado no programa principal. Além disso, a função deve
obedecer ao protótipo:
void calc_esfera(float R, float *area, float *volume)
A área da superfície e o volume são dados, respectivamente, por:
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
