import java.io.IOException;
import java.util.Scanner;

public class Bee1047 {
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
		int h1 = s.nextInt();
		int m1 = s.nextInt();
		int h2 = s.nextInt();
		int m2 = s.nextInt();
		int hm1 = (h1*60) + m1;
		int hm2 = (h2*60) + m2;
		int H24 = 24*60;
		int resultado = 0;
		
		if (hm2 > hm1){
		    resultado = hm2 - hm1;
		    System.out.printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", (resultado / 60), (resultado % 60));
		}
		else if (hm1 > hm2){
		    resultado = (H24 - hm1) + hm2;
		    System.out.printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", (resultado / 60), (resultado % 60));
		}
		else{
		    System.out.printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", 24, 0);
		}
	}
}