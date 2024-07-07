import java.io.IOException;
import java.util.Scanner;

public class Bee1144{
	
    public static void main(String[] args) throws IOException {
		Scanner s = new Scanner(System.in);
		int N = s.nextInt();
		
		for(int i = 1; i <= N; i++){
			System.out.println(i + " " + (i*i) + " " + (i*i*i));
			System.out.println(i + " " + ((i*i)+1) + " " + ((i*i*i)+1));
		}
    }
}