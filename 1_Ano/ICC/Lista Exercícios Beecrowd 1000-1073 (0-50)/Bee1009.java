import java.io.IOException;
import java.util.Scanner;

public class Bee1009 {
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        String nome = s.nextLine();
        double salariofixo = s.nextDouble();
        double vendas = s.nextDouble();
        double total = vendas * 0.15 + salariofixo;
        System.out.printf("TOTAL = R$ %.2f\n", total);
    }
}