import java.io.IOException;
import java.util.Scanner;

public class Bee1149{
	
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        int A = s.nextInt();
        int N = s.nextInt();
        int soma = 0;
        
        while(N <= 0){
        	N = s.nextInt();
        }
        for(int i = 1; i <= N; i++){
        	soma += A;
        	A++;
        }
        System.out.println(soma);
    }
}