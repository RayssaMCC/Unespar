import java.util.Scanner;

public class Bee1154{

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		double idade, soma=0;
		double media;
		int cont = 0;

		idade = s.nextDouble();
		
		while(idade >= 0){
			soma += idade;
			idade = s.nextDouble();
			cont++;
		}
		media = soma / cont;
		System.out.printf("%.2f\n", media);
	}
}