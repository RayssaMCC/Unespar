import java.io.IOException;
import java.util.Scanner;

public class Bee1133{
	
    public static void main(String[] args) throws IOException {
		Scanner s = new Scanner(System.in);
		int X = s.nextInt();
		int Y = s.nextInt();
		
		if(X > Y){
			for(int i = Y+1; i < X; i++){
				if (i % 5 == 2 || i % 5 == 3){
				    System.out.println(i);
				}
			}
		}
		else{
			for(int i = X+1; i < Y; i++){
				if(i % 5 == 2 || i % 5 == 3){
				    System.out.println(i);
				}
			}
		}
    }
}