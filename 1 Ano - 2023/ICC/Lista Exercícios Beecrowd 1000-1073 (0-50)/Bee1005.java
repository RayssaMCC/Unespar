import java.io.IOException;
import java.util.Scanner;

public class Bee1005 {
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        double A = s.nextDouble();
        double B = s.nextDouble();
        double MEDIA = (A * 3.5 + B * 7.5) / 11;
        System.out.printf("MEDIA = %.5f\n", MEDIA);
    }
}