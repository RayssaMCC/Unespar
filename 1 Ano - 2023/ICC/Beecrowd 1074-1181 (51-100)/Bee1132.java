import java.io.IOException;
import java.util.Scanner;

public class Bee1132{
	
    public static void main(String[] args) throws IOException {
		Scanner s = new Scanner(System.in);
		int X = s.nextInt();
		int Y = s.nextInt();
		int soma = 0;
		
		if(X > Y){
			for(int i = Y; i <= X; i++){
				if(i % 13 != 0){
				    soma += i;
				}
			}
		} 
		else{
			for(int i = X; i <= Y; i++){
				if(i % 13 != 0){
				    soma += i;
				}
			}
		}
		System.out.println(soma);
    }
	
}