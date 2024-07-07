import java.io.IOException;
import java.util.Scanner;

public class Bee1061 {
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        
        String di[] = s.nextLine().split(" ");
        String hi[] = s.nextLine().replaceAll(" ", "").split(":");
        String df[] = s.nextLine().split(" ");
        String hf[] = s.nextLine().replaceAll(" ", "").split(":");
        
        int d1 = Integer.parseInt(di[1]);
        int h1 = Integer.parseInt(hi[0]);
        int m1 = Integer.parseInt(hi[1]);
        int s1 = Integer.parseInt(hi[2]);
        int d2 = Integer.parseInt(df[1]);
        int h2 = Integer.parseInt(hf[0]);
        int m2 = Integer.parseInt(hf[1]);
        int s2 = Integer.parseInt(hf[2]);
        int q1, q2, tempo;
        
        q1 = (s1 + m1 * 60) + (h1 * 3600) + (d1 * 86400);
        q2 = (s2 + m2 * 60) + (h2 * 3600) + (d2 * 86400);
        tempo = q2 - q1;
        
        System.out.printf("%d dia(s)\n", (tempo / 86400));
        tempo = tempo % 86400;
        
        System.out.printf("%d hora(s)\n", (tempo / 3600));
        tempo = tempo % 3600;
        
        System.out.printf("%d minuto(s)\n", (tempo / 60));
        tempo = tempo % 60;
        
        System.out.printf("%d segundo(s)\n", tempo);
    }
 
}