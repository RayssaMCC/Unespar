/*6. Fa�a um programa que receba um n�mero inteiro e verifique se esse n�mero � par ou
�mpar.*/

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
