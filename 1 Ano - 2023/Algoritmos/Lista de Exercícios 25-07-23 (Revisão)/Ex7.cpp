/*7. Fa�a um programa que receba tr�s notas de um aluno, calcule e mostre a m�dia
aritm�tica, e a mensagem que segue abaixo. Para alunos de exame, calcule e mostre a
nota que dever� ser tirada no exame para aprova��o, considerando que a m�dia no exame
� 6.0.*/

#include <stdio.h>
#include <stdlib.h>

int main() {
    float n1 = 0, n2 = 0, n3 = 0;
    
    printf("Insira as notas: ");
    scanf("%f", &n1);
    scanf("%f", &n2);
    scanf("%f", &n3);
    float media = (n1+n2+n3) / 3;
    
    if (media >= 0.0 && media <= 2.9){
        printf("Reprovado!");
    }
    else if (media >= 3.0 && media <= 6.9){
        float exame = 12 - media;
        printf("Exame + %.2f", exame);
    }
    else if(media >= 7.0 && media <= 10){
        printf("Aprovado!");
    }
}
