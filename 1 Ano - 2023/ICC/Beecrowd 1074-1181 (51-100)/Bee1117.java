import java.io.IOException;
import java.util.Scanner;

public class Bee1117{

	public static void main(String[] args)  throws IOException {
		Scanner s = new Scanner(System.in);
		
		double nota1 = -1, nota2 = -1;

		while (nota1 < 0 || nota1 > 10){
			nota1 = s.nextDouble();
			if (nota1 < 0 || nota1 > 10)
				System.out.println("nota invalida");
		}
		while (nota2 < 0 || nota2 > 10){
			nota2 = s.nextDouble();
			if (nota2 < 0 || nota2 > 10)
				System.out.println("nota invalida");
		}
		System.out.printf("media = %.2f\n", (nota1 + nota2) / 2);
	}
}