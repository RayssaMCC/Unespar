/*6. Faça um programa que receba um número inteiro e verifique se esse número é par ou
ímpar.*/

#include <stdio.h>
#include <stdlib.h>

int main() {
    int x = 0;
    printf("Insira um valor inteiro: ");
    scanf("%d", &x);
    
    if(x%2 == 0){
        printf("%d eh par", x);
    }
    else{
        printf("%d eh impar", x);
    }
}
