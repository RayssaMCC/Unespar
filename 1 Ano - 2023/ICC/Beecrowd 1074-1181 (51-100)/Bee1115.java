import java.io.IOException;
import java.util.Scanner;

public class Bee1115{

	public static void main(String[] args)  throws IOException {
		Scanner s = new Scanner(System.in);
		int x=1, y=1;

		while (x != 0 && y != 0){
			x = s.nextInt();
			y = s.nextInt();
			
			if(x > 0 && y > 0){
				System.out.println("primeiro");
			}
			if(x < 0 && y > 0){
				System.out.println("segundo");
			}
			if(x < 0 && y < 0){
				System.out.println("terceiro");
			}
			if(x > 0 && y < 0){
				System.out.println("quarto");
			}
		}
	}
}