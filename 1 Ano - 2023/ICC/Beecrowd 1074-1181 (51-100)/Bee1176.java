import java.io.IOException;
import java.util.Scanner;

public class Bee1176{
 
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        int T, N;
        long a = 0, b = 1, c = 0;
        long fib[] = new long[61];
        
        for(int i = 0; i<fib.length; i++){
            fib[i] = c;
            a = b;
            b = c;
            c = a+b;
        }
        
        T = s.nextInt();
        for(int i = 0; i<T; i++){
            N = s.nextInt();
            System.out.println("Fib("+ N +") = " + fib[N]);
        }
        
    }
 
}