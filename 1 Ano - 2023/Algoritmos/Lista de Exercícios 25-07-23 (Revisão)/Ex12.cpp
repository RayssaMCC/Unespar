/*12. Faça um programa que receba dez idades, pesos e alturas e calcule e mostre:
a) a média das idades das dez pessoas;
b) a quantidade de pessoas com peso superior a 90 quilos e altura inferior a 1,50.
c) a porcentagem de pessoas com idade entre 10 e 30 anos entre as pessoas que
medem mais de 1,90.*/

#include <stdio.h>
#include <stdlib.h>

int main() {
    int idade = 0, qdtpess = 0, a = 0, b = 0;
    float peso = 0, altura = 0, soma = 0;
    
    for(int i=1; i<=10; i++){
		printf("Digite a idade de uma pessoa: ");
		scanf("%d",&idade);
		printf("Digite o peso dessa pessoa em kg: ");
		scanf("%f",&peso);
		printf("Digite a altura dessa pessoa em metros: ");
		scanf("%f",&altura);
		soma = soma + idade;
		
		if (peso > 90 && altura < 1.50){
        	qdtpess++;
    	}
    	if (altura > 1.90){
    		a++;
    		if(idade > 10 && idade < 30){
    			b++;
			}
		}
    }
    
    float media = soma / 10;
    printf("A media de idade das pessoas eh: %.2f \n", media);
    printf("A quantidade de pessoas com peso maior que 90 kg e altura menor que 1.50 eh: %d \n", qdtpess);
    
    float porcentagem = (b*100) / a;
    printf("A porcentagem de pessoas com idade entre 10 e 30 anos entre as pessoas que  medem mais de 1.90 eh de %.2f \n", porcentagem);
}
