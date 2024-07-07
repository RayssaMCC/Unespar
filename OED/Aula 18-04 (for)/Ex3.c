#include <stdio.h>
#include <Stdlib.h>

//Aluna: Rayssa Mara Caldini Costa
main(){
    int i;

    printf("Insira a idade em anos: ");
    scanf("%d", &i);

    if(i>=1 && i<=13){
        printf("Crianca");
    }
    else if(i>13 && i<=18){
        printf("Jovem");
    }
    else if(i>18 && i<=60){
        printf("Adulto");
    }
    else if(i>60){
        printf("Idoso");
    }
}
