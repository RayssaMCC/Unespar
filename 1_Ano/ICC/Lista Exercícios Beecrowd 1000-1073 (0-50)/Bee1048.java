import java.io.IOException;
import java.util.Scanner;

public class Bee1048 {
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
		double salario = s.nextDouble();
		double reajuste;
		double novoSalario;
		int porcento;
		
		if (salario >= 0 && salario <= 400) {
			reajuste = salario * 0.15;
			novoSalario = salario + reajuste;
			porcento = 15;
		} 
		else if (salario > 400 && salario <= 800) {
			reajuste = salario * 0.12;
			novoSalario = salario + reajuste;
			porcento = 12;
		} 
		else if (salario > 800 && salario <= 1200) {
			reajuste = salario * 0.10;
			novoSalario = salario + reajuste;
			porcento = 10;
		} 
		else if (salario > 1200 && salario <= 2000) {
			reajuste = salario * 0.07;
			novoSalario = salario + reajuste;
			porcento
			= 7;
		} 
		else {
			reajuste = salario * 0.04;
			novoSalario = salario + reajuste;
			porcento = 4;
		}
		
		System.out.printf("Novo salario: %.2f\n", novoSalario);
		System.out.printf("Reajuste ganho: %.2f\n", reajuste);
		System.out.println("Em percentual: " + porcento + " %");
	}
	
}