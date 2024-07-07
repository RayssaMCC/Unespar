import java.io.IOException;
import java.util.Scanner;

public class Bee1008 {
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        int funcionario = s.nextInt();
        int horas = s.nextInt();
        double valorhora = s.nextDouble();
        double salario = horas * valorhora;
        System.out.println("NUMBER = " + funcionario);
        System.out.printf("SALARY = U$ %.2f\n", salario);
 
    }
 
}