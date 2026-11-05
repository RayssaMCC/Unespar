import java.io.IOException;
import java.util.Scanner;

public class Bee1101{
	
    public static void main(String[] args) throws IOException {
    	Scanner s = new Scanner(System.in);
    	int M = s.nextInt();
    	int N = s.nextInt();
    	int soma=0;
    	
    	while(M > 0 && N > 0){
    		if(M > N){
        		for(int i = N; i <= M; i++){
        			soma += i;
        			System.out.print(i + " ");
        		}
    		}
    		else{
        		for(int i = M; i <= N; i++){
        			soma += i;
        			System.out.print(i + " ");
        		}
    		}
    		System.out.println("Sum=" + soma);
        	M = s.nextInt();
        	N = s.nextInt();
        	soma = 0;
    	}
    }
}