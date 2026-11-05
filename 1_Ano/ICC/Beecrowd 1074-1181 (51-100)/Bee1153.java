import java.io.IOException;
import java.util.Scanner;

public class Bee1153{
	
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        int N = s.nextInt();
        int fat = 1;
        
        for(int i = 1; i <= N; i++){
        	fat = fat*i;
        }
        System.out.println(fat);
    }
}