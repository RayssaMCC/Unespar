import java.io.IOException;
import java.util.Scanner;

public class Bee1060 {
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        int qdt = 0;
        for (int i = 0; i < 6; i++) {
        	double n = s.nextDouble();
        	if (n > 0) {
        	    qdt++;
        	}    
        }   
        System.out.println(qdt + " valores positivos");
    }
	
}