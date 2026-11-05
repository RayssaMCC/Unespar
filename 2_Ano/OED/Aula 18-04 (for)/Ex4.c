#include <stdio.h>
#include <Stdlib.h>

//Aluna: Rayssa Mara Caldini Costa
main(){
    int n;

    printf("Insira um numero inteiro: ");
    scanf("%d", &n);

    if(n<10){
       printf("Numero menor que 10.");
    }
    else if(n==10){
        printf("Numero igual a 10.");
    }
    else if(n>10){
        printf("Numero maior que 10.");
    }
}
