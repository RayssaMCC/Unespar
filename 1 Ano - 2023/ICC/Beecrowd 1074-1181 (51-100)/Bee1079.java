import java.io.IOException;
import java.util.Scanner;

public class Bee1079{
	
	public static void main(String[] args) throws IOException {
    	Scanner s = new Scanner(System.in);
    	int N = s.nextInt();
    	for (int i=0; i<N; i++) {
    	    
    		double n1 = s.nextDouble();
    		double n2 = s.nextDouble();
    		double n3 = s.nextDouble();
    		double media = ((n1*2) + (n2*3) + (n3*5)) / 10;
    		System.out.printf("%.1f\n", media);
    	}
    }
}