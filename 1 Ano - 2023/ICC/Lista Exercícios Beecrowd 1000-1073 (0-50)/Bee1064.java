import java.io.IOException;
import java.util.Scanner;

public class Bee1064 {
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        int qdt = 0;
        double media = 0;
        double x;
        
        for (int i = 0; i < 6; i++) {
        	x = s.nextDouble();
        	if (x > 0) {
        		qdt++;
        		media += x;
        	}
        }
        
        media = media / qdt;
        System.out.println(qdt + " valores positivos");
        System.out.printf("%.1f\n", media);
    }
	
}