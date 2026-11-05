import java.io.IOException;
import java.util.Scanner;

public class Bee1178{
 
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        int i, j;
        double x = s.nextDouble();
        double N[] = new double[100];
        
        for(i = 0, j = 0; i<N.length; x = x/2, i++, j++){
            N[j] = x;
            System.out.printf("N[%d] = %.4f\n", i, N[j]);
        }
    }
 
}