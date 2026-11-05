import java.io.IOException;
import java.util.Scanner;

public class Bee1151{

    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        int N = s.nextInt();
        int proximo, anterior = 0, atual = 1;
        
        for(int i = 1; i <= N; i++) {
        	if(i == N){
        	    System.out.println(anterior);
        	}
        	else{
        	    System.out.print(anterior + " ");
        	}
        	proximo = anterior + atual;
        	anterior = atual;
        	atual = proximo;
        }
    }
}