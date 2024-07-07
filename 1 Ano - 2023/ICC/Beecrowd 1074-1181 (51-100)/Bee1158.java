import java.io.IOException;
import java.util.Scanner;

public class Bee1158{

    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        int N = s.nextInt();
        int X, Y;
        int soma=0, cont=0;
        
        for(int i = 0; i < N; i++){
        	cont = 0;
        	soma = 0;
        	X = s.nextInt();
        	Y = s.nextInt();
        	
        	while(cont < Y){
        		if(X % 2 != 0){
        			soma += X;
        			cont++;
        		}
        		X++;
        	}
        	System.out.println(soma);
        }
    }
	
}