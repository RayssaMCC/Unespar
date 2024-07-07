import java.io.IOException;
import java.util.Scanner;

public class Bee1015 {
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        double x1 = s.nextDouble();
        double y1 = s.nextDouble();
        double x2 = s.nextDouble();
        double y2 = s.nextDouble();
        double distancia = Math.sqrt(Math.pow((x2 - x1), 2) + Math.pow((y2 - y1), 2));
        
        System.out.printf("%.4f\n", distancia);
    }
 
}