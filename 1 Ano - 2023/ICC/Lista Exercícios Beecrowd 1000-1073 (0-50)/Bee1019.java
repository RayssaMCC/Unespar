import java.io.IOException;
import java.util.Scanner;

public class Bee1019 {
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        int totalSegundos = s.nextInt();
        int horas = totalSegundos / 3600;
        totalSegundos = totalSegundos % 3600;
        
        int minutos = totalSegundos / 60;
        totalSegundos = totalSegundos % 60;
        
        int segundos = totalSegundos;
        
        System.out.println(horas + ":" + minutos + ":" + segundos);	
    }
 
}