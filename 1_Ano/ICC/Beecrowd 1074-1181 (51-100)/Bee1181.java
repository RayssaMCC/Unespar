import java.io.IOException;
import java.util.Scanner;

public class Bee1181{
 
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        int L = s.nextInt();
        double soma = 0;
        char T = s.next().toUpperCase().charAt(0);
        
        double M[][] = new double [12][12];
        
        for(int i = 0; i<M.length; i++){
            for(int j = 0; j<M[i].length; j++){
                M[i][j] = s.nextDouble();
            }
        }
        
        for(int j = 0; j<M.length; j++){
            soma += M[L][j];
        }
        
        if(T == 'M'){
            soma /= M.length;
        }
        System.out.println(String.format("%.1f", soma));
    }
 
}