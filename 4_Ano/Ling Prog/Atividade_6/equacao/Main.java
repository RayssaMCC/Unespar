package equacao;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        System.out.print("Digite o valor de a: ");
        Double a = teclado.nextDouble();

        System.out.print("Digite o valor de b: ");
        Double b = teclado.nextDouble();

        System.out.print("Digite o valor de D: ");
        Double c = teclado.nextDouble();

        // x = a² + b²
        Double x = Math.pow(a, 2) + Math.pow(b, 2);

        // Calcula o Delta
        Double delta = Math.pow(b, 2) - (4 * a * c);

        // Calcula x positivo pela fórmula de Bhaskara
        Double xPositivo = (-b + Math.sqrt(delta)) / (2 * a);

        System.out.println("x = " + x);
        System.out.println("Delta = " + delta);
        System.out.println("xPositivo = " + xPositivo);

        teclado.close();
    }
}
