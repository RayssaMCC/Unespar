import java.io.IOException;
import java.util.Scanner;
 
public class Bee1004 {
 
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        int A = s.nextInt();
        int B = s.nextInt();
        int PROD = A * B;
        System.out.println("PROD = " + PROD);
    }
}