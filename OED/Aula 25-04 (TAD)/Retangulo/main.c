#include <stdio.h>
#include <stdlib.h>
#include "retan.h"

int main(){
    //Exemplo de uso do TAD Ret�ngulo
    Retangulo meuRetangulo = criarRetangulo(5.0,3.0); //ret�ngulo com essas dimens�es

    //c�lculo e exibi��o da �rea
    float area = calcularArea(meuRetangulo);
    printf("A area do retangulo e: %.2f", area);
    return 0;
}
