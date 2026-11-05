import java.io.IOException;

public class Bee1155{

    public static void main(String[] args) throws IOException {
    	double S = 1;
    	
    	for(int i = 2; i <= 100; i++){
    		S += 1.00 / i;
    	}
    	System.out.printf("%.2f\n", S);
    }
}