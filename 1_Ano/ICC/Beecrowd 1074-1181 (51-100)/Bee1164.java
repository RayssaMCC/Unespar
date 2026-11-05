import java.io.IOException;
import java.util.Scanner;

public class Bee1164{
 
    public static void main(String[] args) throws IOException {
       Scanner s = new Scanner(System.in);
        int N = s.nextInt();
        int X, soma;
        
        for(int i = 0; i < N; i++){
        	soma = 0;
        	X = s.nextInt();
        	
        	for(int j = 1; j < X; j++){
        		if (X % j == 0){
        		    soma += j;
        		}
        	}
        	if (soma == X){
        	    System.out.println(X + " eh perfeito");
        	}
        	else{
        	    System.out.println(X + " nao eh perfeito");
        	}
        }
    }
}