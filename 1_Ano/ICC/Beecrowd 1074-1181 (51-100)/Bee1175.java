import java.io.IOException;
import java.util.Scanner;

public class Bee1175{
 
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        int aux;
        int N[] = new int[20];
        
        for(int i = 0; i<N.length; i++){
            N[i] = s.nextInt();
        }
        
        for(int i = 0; i<N.length/2; i++){
            aux = N[i];
            N[i] = N[N.length - 1 - i];
            N[N.length - 1 - i] = aux;
        }
        
        for(int i = 0; i<N.length; i++){
            System.out.printf("N[%d] = %d\n", i, N[i]);
        }
    }
 
}