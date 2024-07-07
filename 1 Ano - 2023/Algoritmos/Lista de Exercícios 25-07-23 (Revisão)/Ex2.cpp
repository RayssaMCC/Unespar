/*2. Faça um programa que receba o salário de um funcionário e o percentual de aumento
que ele terá. Calcule e mostre na tela o valor do aumento e o novo salário.*/

#include <stdio.h>
#include <stdlib.h>

int main() {
    float salario = 0;
    float porcentagem = 0;
    
    printf("Insira o salario: ");
    scanf("%f", &salario);
    
    printf("Insira o percentual de aumento: ");
    scanf("%f", &porcentagem);
    
    float aumento = salario*(porcentagem/100);
    float novosalario = salario + aumento;
    printf("voce tera um aumento de %.2f%% (R$%.2f), com um novo salario de R$%.2f", porcentagem, aumento, novosalario);
}
