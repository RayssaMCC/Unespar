import java.io.IOException;

public class Bee1097{
	
	public static void main(String[] args) throws IOException {
		int i=1, j=7;
		
		while(i <= 9){
			for(int k = 0; k < 3; k++){
				System.out.println("I=" + i + " J=" + j);
				j--;
			}
			j+=5;
			i+=2;
		}
	}
}