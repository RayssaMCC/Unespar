import java.io.IOException;
import java.util.Scanner;

public class Bee1116{
	
    public static void main(String[] args) throws IOException {
		Scanner s = new Scanner(System.in);
		int N = s.nextInt();
		int X, Y;
		
		for (int i = 0; i < N; i++) {
			X = s.nextInt();
			Y = s.nextInt();
			
			if(Y == 0){
			    System.out.println("divisao impossivel");
			}
			else{
			    System.out.println((double) X / Y);
			}
		}
    }
}