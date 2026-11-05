import java.io.IOException;
import java.util.Scanner;

public class Bee1145{
	
    public static void main(String[] args) throws IOException {
		Scanner s = new Scanner(System.in);
		int X = s.nextInt();
		int Y = s.nextInt();
		int cont = 1;
		
		for(int i = 1; i <= Y; i++){
			System.out.print(i);
			if(i % X == 0){
			    System.out.println("");
			}
			else{
			    System.out.print(" ");
			}
		}
    }
}