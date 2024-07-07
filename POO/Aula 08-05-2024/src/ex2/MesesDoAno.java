package ex2;
/*Crie uma classe que armazene os 12 meses do ano em um array. A seguir, gere um valor
randômico entre 0 e 11 e apresente o mês correspondente ao valor sorteado. Considere que o
valor 0 corresponde ao mês de janeiro e o valor 11, ao mês de dezembro.*/

import java.util.Random;

public class MesesDoAno {
    public static void main(String[] args) {
        String[] meses = {"Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho","Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"};

        // Gerando um valor aleatório entre 0 e 11
        Random aleatorio = new Random();
        int valorAleatorio = aleatorio.nextInt(12); // Gera um número entre 0 e 11

        // Obtendo o nome do mês correspondente ao valor aleatório gerado
        String mesSorteado = meses[valorAleatorio];

        System.out.printf("O mês sorteado é: %s", mesSorteado);
    }
}
