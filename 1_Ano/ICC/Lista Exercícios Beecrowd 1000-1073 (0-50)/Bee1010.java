import java.io.IOException;
import java.util.Scanner;

public class Bee1010 {
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        int code1 = s.nextInt();
        int qdt1 = s.nextInt();
        double preco1 = s.nextDouble();
        
        int code2 = s.nextInt();
        int qdt2 = s.nextInt();
        double preco2 = s.nextDouble();
        
        double resultado = (qdt1*preco1) + (qdt2*preco2);
        
        System.out.printf("VALOR A PAGAR: R$ %.2f\n", resultado);
    }
 
}