import java.io.IOException;
import java.util.Scanner;

public class Bee1044 {
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        int a = s.nextInt();
        int b = s.nextInt();
        
        if (a % b == 0 || b % a == 0) {
            System.out.println("Sao Multiplos");
        } 
        else {
            System.out.println("Nao sao Multiplos");
        }
    }
}