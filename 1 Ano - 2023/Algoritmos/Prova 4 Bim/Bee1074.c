#include <stdlib.h>
#include <stdio.h>

int main(){
    int N, X;

    scanf("%d", &X);

    for(int i = 0; i<X; i++){
        scanf("%d", &N);

        if(N>0 && (N%2)== 0){
            printf("EVEN POSITIVE\n");
        }
        else if(N>0 && (N%2)!=0){
            printf("ODD POSITIVE\n");
        }
        else if(N<0 && (N%2)==0){
            printf("EVEN NEGATIVE\n");
        }
        else if(N<0 && (N%2)!=0){
                printf("ODD NEGATIVE\n");
        }
        else if(N==0){
            printf("NULL\n");
        }
    }
    return 0;
}
