import java.io.IOException;
import java.util.Scanner;

public class Bee1051 {
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        double salario = s.nextDouble();
        
        if (salario >= 0 && salario <= 2000) {
        	System.out.println("Isento");
        } 
        else if (salario > 2000 && salario <= 3000) {
           salario = ((salario - 2000) * 0.08);
        	System.out.printf("R$ %.2f\n", salario); 
        } 
        else if (salario > 3000 && salario <= 4500) {
            salario = ((salario - 3000)  * 0.18) + 80;
        	System.out.printf("R$ %.2f\n", salario);
        } 
        else {
           salario = ((salario - 4500) * 0.28) + 350;
        	System.out.printf("R$ %.2f\n", salario); 
        }
    }
}