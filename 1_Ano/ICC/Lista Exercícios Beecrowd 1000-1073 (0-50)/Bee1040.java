import java.io.IOException;
import java.util.Scanner;

public class Bee1040 {
    public static void main(String[] args) throws IOException {
	float N1, N2, N3, N4, media, N5, mediaf;
		Scanner s = new Scanner(System.in);
		N1 = s.nextFloat();
		N2 = s.nextFloat();
		N3 = s.nextFloat();
		N4 = s.nextFloat();
		
		media = ((N1 * 2)+(N2 * 3)+( N3 * 4)+(N4 * 1))/10;
		
		if (media >= 7.0) {
			 System.out.printf("Media: %.1f\n", media);
			 System.out.print("Aluno aprovado.\n");
		}
		else if (media >= 5.0 && media <= 6.9) {
			
			System.out.printf("Media: %.1f\n", media);
			System.out.print("Aluno em exame.\n");
			N5 = s.nextFloat();
			System.out.printf("Nota do exame: %.1f\n",N5);
			mediaf =(media + N5) / 2;
			
			if (mediaf >= 5.0) {
				System.out.print("Aluno aprovado.\n");
			}
			else {
				System.out.print("Aluno reprovado.\n");
			}
			System.out.printf("Media final: %.1f\n", mediaf);
		}
		else if (media < 5.0) {
			System.out.printf("Media: %.1f\n", media);
			System.out.print("Aluno reprovado.\n");
		}
	}
}