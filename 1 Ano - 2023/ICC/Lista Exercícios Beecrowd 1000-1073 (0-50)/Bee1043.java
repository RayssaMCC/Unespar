import java.io.IOException;
import java.util.Scanner;

public class Bee1043 {
    public static void main(String[] args) throws IOException {
        float A, B, C, areaTapezio, perimetroTriangulo;
		Scanner s = new Scanner(System.in);
		A = s.nextFloat();
		B = s.nextFloat();
		C = s.nextFloat();
		
		if ((A < (float)(B+C)) && (B < (float)(A+C)) && (C < (float)(B+A))) {
			perimetroTriangulo = A + B + C;
			System.out.printf("Perimetro = %.1f\n", perimetroTriangulo);
		}
		else {
			areaTapezio = ((A + B) * C) / 2;
			System.out.printf("Area = %.1f\n", areaTapezio);
		}
	}
}