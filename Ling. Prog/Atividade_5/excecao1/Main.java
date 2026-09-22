package excecao1;

import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        ArrayList<Usuario> usuarios = new ArrayList<>();

        int quantidade = 0;

        // Entrada da quantidade de usuários
        while (quantidade <= 0) {
            try {
                System.out.print("Digite a quantidade de usuários: ");
                quantidade = scanner.nextInt();

                if (quantidade <= 0) {
                    System.out.println("A quantidade deve ser maior que zero.");
                }

            } catch (InputMismatchException e) {
                System.out.println("Entrada inválida. Digite um número inteiro.");
                scanner.nextLine();
            }
        }

        scanner.nextLine();

        // Cadastro dos usuários
        for (int i = 0; i < quantidade; i++) {

            System.out.println("\n--- Cadastro do usuário " + (i + 1) + " ---");

            System.out.print("Digite o nome completo: ");
            String nome = scanner.nextLine();

            double peso = 0;
            double altura = 0;

            // Entrada do peso
            while (peso <= 0) {
                try {
                    System.out.print("Digite o peso (kg): ");
                    peso = scanner.nextDouble();

                    if (peso <= 0) {
                        System.out.println("O peso deve ser maior que zero.");
                    }

                } catch (InputMismatchException e) {
                    System.out.println("Peso inválido. Digite um valor numérico.");
                    scanner.nextLine();
                }
            }

            // Entrada da altura
            while (altura <= 0) {
                try {
                    System.out.print("Digite a altura (cm): ");
                    altura = scanner.nextDouble();

                    if (altura <= 0) {
                        System.out.println("A altura deve ser maior que zero.");
                    }

                } catch (InputMismatchException e) {
                    System.out.println("Altura inválida. Digite um valor numérico.");
                    scanner.nextLine();
                }
            }

            altura = altura / 100; // Converte altura de centímetros para metros

            scanner.nextLine();

            Usuario usuario = new Usuario(nome, peso, altura);
            usuarios.add(usuario);
        }

        // Exibição dos resultados
        System.out.println("\n===== RESULTADOS =====");

        for (Usuario usuario : usuarios) {

            try {
                usuario.mostrarDados();

            } catch (ArithmeticException e) {
                System.out.println("Erro ao calcular o IMC: " + e.getMessage());

            } finally {
                System.out.println("Cálculo finalizado.");
            }
        }

        scanner.close();
    }
}
