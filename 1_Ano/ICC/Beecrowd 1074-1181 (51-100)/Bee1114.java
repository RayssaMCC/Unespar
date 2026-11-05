import java.io.IOException;
import java.util.Scanner;

public class Bee1114{

    public static void main(String[] args) throws IOException {
    	Scanner s = new Scanner(System.in);
    	int senha = s.nextInt();
    	
    	while(senha != 2002){
    		System.out.println("Senha Invalida");
        	senha = s.nextInt();
    	}
		System.out.println("Acesso Permitido");
    }
	
}