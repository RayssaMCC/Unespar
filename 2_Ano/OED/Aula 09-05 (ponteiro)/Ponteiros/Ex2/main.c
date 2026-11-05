#include <stdio.h>
#include <stdlib.h>

int main(){
    int a = 10, b = 20;
    int *p, *q;
    p = &a;
    q = &b;

    //vai transformar os valores de a e b (10 e 20) nos valores apontados pelos ponteiros
    *p = 30;
    *q = 40;

    printf("%p, %d\n", &a, a); //&a = endere�o de mem�ria de 'a', a = valor de a (10)
    printf("%p, %d\n", &b, b); //&b = endere�o de mem�ria de 'b', b = valor de b (20)
    printf("%p, %p, %d\n", &p, p, *p); //&p = endere�o de mem�ria do ponteiro p, p = endere�o de mem�ria para qual p aponta, *p = valor apontado pelo ponteiro 'p'
    printf("%p, %p, %d\n", &q, q, *q); // ^^^^ igual ^^^^

    return 0;
}
