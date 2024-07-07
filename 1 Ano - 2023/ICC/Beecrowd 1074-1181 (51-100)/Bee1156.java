import java.io.IOException;

public class Bee1156{
	
    public static void main(String[] args) throws IOException {
    	double S = 1;
    	int cont = 2;
    	
    	for(int i = 3; i <= 39; i++){
    		if(i % 2 == 1) {
    			S += (double) i / cont;
        		cont *= 2.00;
    		}
    	}
    	System.out.printf("%.2f\n", S);
    }
}