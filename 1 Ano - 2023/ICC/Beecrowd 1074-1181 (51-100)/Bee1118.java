import java.io.IOException;
import java.util.Scanner;

public class Bee1118{
	
    public static void main(String[] args) throws IOException {
		Scanner s = new Scanner(System.in);
		double nota1, nota2, flag = 1;
		
		while (flag == 1) {
			nota1 = s.nextDouble();
			while (nota1 > 10 || nota1 < 0) {
				System.out.println("nota invalida");
				nota1 = s.nextDouble();
			}
			
			nota2 = s.nextDouble();
			while (nota2 > 10 || nota2 < 0) {
				System.out.println("nota invalida");
				nota2 = s.nextDouble();
			}
			
			double media = (nota1 + nota2) / 2;
			System.out.printf("media = %.2f\n", media);
			
			System.out.println("novo calculo (1-sim 2-nao)");
			flag = s.nextInt();
			while (flag != 1 && flag != 2) {
				System.out.println("novo calculo (1-sim 2-nao)");
				flag = s.nextInt();
			}
		}
    }
}