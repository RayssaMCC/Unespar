import java.io.IOException;
import java.util.Scanner;

public class Bee1049 {
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
		String palavra1 = s.next();
		String palavra2 = s.next();
		String palavra3 = s.next();
		
		if (palavra1.equalsIgnoreCase("vertebrado")) {
			if (palavra2.equalsIgnoreCase("ave")) {
				if (palavra3.equalsIgnoreCase("carnivoro")) {
					System.out.println("aguia");
				} 
				else {
					System.out.println("pomba");
				}
			} 
			else {
				if (palavra3.equalsIgnoreCase("onivoro")) {
					System.out.println("homem");
				} 
				else {
					System.out.println("vaca");
				}
			}
		} 
		else {
			if (palavra2.equalsIgnoreCase("inseto")) {
				if (palavra3.equalsIgnoreCase("hematofago")) {
					System.out.println("pulga");
				} 
				else {
					System.out.println("lagarta");
				}
			} 
			else {
				if (palavra3.equalsIgnoreCase("hematofago")) {
					System.out.println("sanguessuga");
				} 
				else {
					System.out.println("minhoca");
				}			
			}
		}
	}
}