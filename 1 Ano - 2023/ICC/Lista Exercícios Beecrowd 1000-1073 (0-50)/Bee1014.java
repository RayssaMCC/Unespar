import java.io.IOException;
import java.util.Scanner;

public class Bee1014 {
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        int X = s.nextInt();
        double Y = s.nextDouble();
        double media = X / Y;
        
        System.out.printf("%.3f km/l\n", media);   
    }
	
}