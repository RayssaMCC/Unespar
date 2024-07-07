package ex1;
/*Elabore uma classe que receba 5 notas de alunos por meio de showInputDialog, armazene
essas notas em um array de cinco elementos, apresente em tela as cinco notas em ordem
decrescente (da maior para a menor) e a média aritmética das notas.*/

import javax.swing.JOptionPane;
import java.util.Arrays;

public class NotasAlunos {

    public static void main(String[] args) {
        double[] notas = new double[5];
        double[] notasDecrescente = new double[5];
        double soma = 0;

        // Solicitando as notas dos alunos e armazenando no array
        for (int i = 0; i < 5; i++) {
            String input = JOptionPane.showInputDialog("Digite a nota do aluno " + (i+1) + ":");
            notas[i] = Double.parseDouble(input);
        }

        // Ordenando o array em ordem decrescente
        Arrays.sort(notas); // Ordena em ordem crescente
        for (int i = 0; i < 5; i++) {
            notasDecrescente[i] = notas[4 - i]; // O primeiro elemento de 'notasDecrescente' será atribuído com o último elemento de 'notas'
        }

        // Exibindo as notas em ordem decrescente
        System.out.println("Notas em ordem decrescente:");
        for (int i = 0; i < 5; i++) {
            System.out.printf("Nota %d: %.2f\n", i+1, notasDecrescente[i]);
        }

        // Calculando a média das notas
        for (int i = 0; i < 5; i++) {
            soma += notas[i];
        }
        double media = soma / 5;

        System.out.printf("Média das notas: %.2f", media);
    }
}
