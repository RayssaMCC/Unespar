import java.io.IOException;
import java.util.Scanner;
 
public class Bee1002 {
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        double R = s.nextDouble();
        double A = (3.14159 * (R*R));
        System.out.printf("A=%.4f\n", A);
    }
}