import java.io.IOException;
import java.util.Scanner;

public class Bee1113{

    public static void main(String[] args) throws IOException {
    	Scanner s = new Scanner(System.in);
    	int X, Y;
    	
    	do{
		    X = s.nextInt();
		    Y = s.nextInt();
		
		    if(X > Y){
		    	System.out.print("Decrescente\n");
		    }
		    else if(Y > X){
		    	System.out.print("Crescente\n");
		    }
		    	
	    } while(X != Y);
    }
}