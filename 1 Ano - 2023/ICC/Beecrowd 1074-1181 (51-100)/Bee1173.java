import java.io.IOException;
import java.util.Scanner;

public class Bee1173{
 
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        
        int N[] = new int [10];
        N[0] = s.nextInt();
        
        for(int i = 1; i<10; i++){
            N[i] = N[i-1] * 2;
        }
        
        for(int i = 0; i<10; i++){
            System.out.printf("N[%d] = %d\n", i, N[i]);
        }
    }
 
}