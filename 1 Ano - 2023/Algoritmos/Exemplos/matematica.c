#include<stdio.h> // Para printf e scanf
#include<math.h> // Biblioteca matem�tica
#include<stdlib.h> // Para system("pause")

main() {
    float x = 2;
    float y;
    printf("********** FORMULAS MATEMATICAS **********\n");
    y = sqrt(x); // Raiz quadrada
    printf("raiz = %f \n", y);

    y = pow(x, 2); // ao inv�s de fazer x*x
    printf("quadrado = %f \n", y);

    y = pow(x, 5); // x elevado a 5
    printf("potencia = %f \n", y);

    y = pow(x, 1.0/2.0); // x elevado a uma fra��o 1/2 (usa .0 para identificar como n�mero real)
    printf("potencia frac. = %f \n", y);

    y = log(x); // logaritmo natural (ln(x))
    printf("logaritmo = %f \n", y);

    y = log2(x); // logaritmo na base 2
    printf("logaritmo base 2 = %f \n", y);

    /* a partir daqui, o valor de x � alterado
    para testar outras f�rmulas matem�ticas */
    x = -10;
    y = abs(x); // valor absoluto (sem sinal)
    printf("valor absoluto = %f \n", y);

    printf("\n********** ARREDONDAMENTO **********\n");
    x = 1.4;
    printf("arredonda para cima = %f \n", ceil(x)); // 1.5 fica 2
    printf("arredonda para baixo = %f \n", floor(x)); // 1.5 fica 1
    // O round(x) se o valor depois da v�rgula for maior ou igual a 5, arredonda para cima, caso contr�rio, arredonda pra baixo
    printf("arredonda geral = %f \n", round(x));

    /*
    Aten��o, para c�lculo de fun��es trigonom�tricas, � necess�rio
    que o valor seja passado em radianos ao inv�s de graus.
    Para converter graus para radianos, basta fazer:
    rad = x*(pi/180).
    Considere x = 90 graus
    */
    x = 60; // Graus
    float rad = x*(M_PI/180); // Voc� pode usar M_PI para representar a constante pi
    printf("\n********** TRIGONOMETRIA **********\n");
    printf("seno de x = %f \n", sin(rad));
    printf("cosseno de x = %f \n", cos(rad));
    printf("tangente de x = %f \n", tan(rad));

    system("pause");
}
