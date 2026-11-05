import java.io.IOException;
import java.util.Scanner;

public class Bee1036 {
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        double A = s.nextDouble();
        double B = s.nextDouble();
        double C = s.nextDouble();
        
        if ((A == 0) || (Math.pow(B, 2) - 4 * A * C < 0)) {
			System.out.println("Impossivel calcular");
		}
		else {
		    double bhaskara = Math.sqrt((B * B) - 4 * A * C);
            double R1 = (-B + bhaskara) / (2 * A);
            double R2 = (-B - bhaskara) / (2 * A);
            System.out.printf("R1 = %.5f\n", R1);
            System.out.printf("R2 = %.5f\n", R2);
		}
    }
}