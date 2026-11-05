/*1. Implemente um programa que leia o nome de 5 pessoas e mostre os nomes
armazenados. Utilize vetores.*/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(){
    char nome1[30];
    char nome2[30];
    char nome3[30];
    char nome4[30];
    char nome5[30];
    
    printf("Digite seu nome:\n");
    gets(nome1);
    gets(nome2);
    gets(nome3);
    gets(nome4);
    gets(nome5);
    
    printf("\n");
    
    printf("%s \n", nome1);
    printf("%s \n", nome2);
    printf("%s \n", nome3);
    printf("%s \n", nome4);
    printf("%s \n", nome5);
}
