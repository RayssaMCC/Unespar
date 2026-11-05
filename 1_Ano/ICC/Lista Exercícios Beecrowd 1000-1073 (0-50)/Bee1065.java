import java.io.IOException;
import java.util.Scanner;

public class Bee1065 {
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        int x;
        int qdt = 0;
        
        for (int i = 0; i < 5; i++) {
        	x = s.nextInt();
        	if (x % 2 == 0 ) qdt++;
        }
        System.out.println(qdt + " valores pares");
    }
	
}