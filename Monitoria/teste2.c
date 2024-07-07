/*Implemente a função main( ), declare as variáveis
e atribua valores para as variáveis declaradas.
Idade, sexo, salário, número de dependentes

scanf("tipo da variavel", &nomedavariavel) serve pra ler o que o usuário escrever
printf("alguma frase e tipo da variavel", nomedavariavel) vai mostrar no terminal o que estiver escrito




*/

#include <stdio.h>
#include <stdlib.h>

int main(){
    int idade;
    char sexo;
    float salario;
    int dependentes;

    printf("Insira a idade: ");
    scanf("%d", &idade);
    printf("Insira a sexo: ");
    scanf(" %c", &sexo);
    printf("Insira o salario: ");
    scanf("%f", &salario);
    printf("Insira os dependentes: ");
    scanf("%d", &dependentes);

    printf("A idade eh: %d\n", idade);
    printf("O sexo eh %c\n", sexo);
    printf("O salario eh: %.2f\n",salario);
    printf("Os dependentes eh: %d\n",dependentes);
}
