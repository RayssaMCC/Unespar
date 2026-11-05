import java.io.IOException;
import java.util.Scanner;

public class Bee1165{
	
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        int N = s.nextInt();
        int X, cont;
        
        for(int i = 0; i < N; i++){
        	cont = 0;
        	X = s.nextInt();
        	
        	for(int j = 2; j < X; j++){
        		if(X % j == 0){
        		    cont++;
            	}
        	}
        	if(cont == 0){
        	    System.out.println(X + " eh primo");
        	}
        	else{
        	    System.out.println(X + " nao eh primo");
        	}
        }
    }
	
}