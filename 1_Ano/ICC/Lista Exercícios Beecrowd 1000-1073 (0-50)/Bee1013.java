import java.io.IOException;
import java.util.Scanner;

public class Bee1013 {
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        int A = s.nextInt();
        int B = s.nextInt();
        int C = s.nextInt();
 
        int maiorAB = (A + B + Math.abs(A - B)) / 2;
        int maiorABC = (maiorAB + C + Math.abs(maiorAB - C)) / 2;
        
        System.out.println(maiorABC + " eh o maior");
    }
 
}