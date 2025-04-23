import java.util.Scanner;

public class Ex1 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        
        System.out.printf("Insira a quantidade de pontos do time líder: ");
        int qdtPontoLider = s.nextInt();

        System.out.printf("Insira a quantidade de pontos do time lanterna: ");
        int qdtPontosLanterna = s.nextInt();

        double vitoria = Math.ceil((double)(qdtPontoLider - qdtPontosLanterna) / 3);

        System.out.printf("O time lanterna precisará de %.0f vitórias para ultrapassar o líder.", vitoria);

        s.close();
    }
}