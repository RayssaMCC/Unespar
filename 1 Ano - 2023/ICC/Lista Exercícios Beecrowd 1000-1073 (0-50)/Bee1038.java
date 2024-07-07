import java.io.IOException;
import java.util.Scanner;

public class Bee1038 {
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
		int cod = s.nextInt();
		int qdt = s.nextInt();
		double total;
		
		switch (cod) {
			case 1:	total = qdt * 4.00; break;
			case 2: total = qdt * 4.50; break;
			case 3: total = qdt * 5.00; break;
			case 4: total = qdt * 2.00; break;
			case 5: total = qdt * 1.50; break;
			default: total = 0;
		}
		System.out.printf("Total: R$ %.2f\n", total);
    }
 
}