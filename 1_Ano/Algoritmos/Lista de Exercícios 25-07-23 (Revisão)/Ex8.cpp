/*8. Faça um programa que receba dois números inteiros e mostre o maior deles.*/

#include <stdio.h>
#include <stdlib.h>

int main() {
    int x = 0, y = 0;
    
    printf("Insira dois numeros inteiros: ");
    scanf("%d", &x);
    scanf("%d", &y);
    
    if (x > y){
        printf("o maior numero eh: %d", x);
    }
    else{
        printf("o maior numero eh: %d", y);
    }
}
