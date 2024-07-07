#include <stdlib.h>
#include <stdio.h>

int main(){
    int x, h, d, g;

    scanf("%d", &x);

    for(int i = 0; i<x; i++){
        scanf("%d %d %d", &h, &g, &d);

        if((h>=200 && h<=300) && (d>=50) && (g>=150)){
            printf("Sim\n");
        }
        else{
            printf("Nao\n");
        }
    }
}
