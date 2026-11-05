import java.io.IOException;
 import java.util.Scanner;

public class Bee1011 {
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        double raio = s.nextDouble();
        double pi = 3.14159;
        double volume = (4.0/3) * pi * Math.pow(raio, 3.0);
        
        System.out.printf("VOLUME = %.3f\n", volume);
    }
 
}