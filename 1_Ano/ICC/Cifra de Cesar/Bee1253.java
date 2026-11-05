import java.io.IOException;
import java.util.Scanner;

public class Bee1253{

	public static void main(String[] args) throws IOException {
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		
		for (int i=0 ; i<N ; i++){
			scan.nextLine();
			String str = scan.nextLine();
			int troca = scan.nextInt();
			char[] s = str.toCharArray();
			
			for (int x=0 ; x<s.length ; x++){
				if((s[x]-troca) < 65){
					s[x] += (26-troca);
				}
				else{
					s[x] -= troca;
				}
			}
			System.out.println(s);
		}
	}
}