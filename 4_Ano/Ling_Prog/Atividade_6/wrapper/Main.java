package wrapper;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        System.out.print("Digite o ano de nascimento: ");
        Integer anoNascimento = teclado.nextInt();

        System.out.print("Digite o ano atual: ");
        Integer anoAtual = teclado.nextInt();

        if (!anoNascimento.equals(anoAtual)) {
            Integer idade = anoAtual - anoNascimento;

            System.out.println("A idade da pessoa é: " + idade + " anos.");
        } else {
            System.out.println("Os anos são iguais.");
        }

        teclado.close();
    }
}