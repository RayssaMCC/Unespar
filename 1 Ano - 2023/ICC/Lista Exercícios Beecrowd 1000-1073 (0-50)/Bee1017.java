import java.io.IOException;
import java.util.Scanner;

public class Bee1017 {
    public static void main(String[] args) throws IOException {
       Scanner s = new Scanner(System.in);
       int tempo = s.nextInt();
       int vm = s.nextInt();
       double km = tempo * vm;
       double media = km / 12;
       
       System.out.printf("%.3f\n", media);
    }
 
}