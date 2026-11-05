import java.io.IOException;
import java.util.Scanner;

public class Bee1180{
 
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        int menor = 0, posMenor = 0, N;
        N = s.nextInt();
        int X[] = new int [N];
        
        for(int i = 0; i<N; i++){
            X[i] = s.nextInt();
            
            if(i == 0){
                menor = X[i];
                posMenor = i;
            }
            else if(X[i]< menor){
                menor = X[i];
                posMenor = i;
            }
        }
        System.out.printf("Menor valor: %d\n", menor);
        System.out.printf("Posicao: %d\n", posMenor);
    }
 
}