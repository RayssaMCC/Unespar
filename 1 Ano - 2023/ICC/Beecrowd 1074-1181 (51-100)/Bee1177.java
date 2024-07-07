import java.io.IOException;
import java.util.Scanner;

public class Bee1177{
 
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        int T = s.nextInt();
        int N[] = new int[1000];
        int pos = 0;
        
        while(pos<999){
            for(int j = 0; j<T; j++){
                if(pos>999){
                    break;
                }
                N[pos] = j;
                pos++;
            }
        }
        
        for(int i = 0; i<N.length; i++){
            System.out.printf("N[%d] = %d\n", i, N[i]);
        }
    }
 
}