import java.util.Scanner;

public class CalculoDistancia {
    static class Ponto {
        float x;
        float y;

        Ponto(float x, float y) {
            this.x = x;
            this.y = y;
        }
    }

    static float calcularDistancia(Ponto p1, Ponto p2) {
        return (float) Math.sqrt(Math.pow(p2.x - p1.x, 2) + Math.pow(p2.y - p1.y, 2));
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Informe a quantidade de pontos: ");
        int n = scanner.nextInt();

        Ponto[] pontos = new Ponto[n];
        System.out.println("Digite os pontos no formato x y:");
        for (int i = 0; i < n; ++i) {
            float x = scanner.nextFloat();
            float y = scanner.nextFloat();
            pontos[i] = new Ponto(x, y);
        }

        float distanciaTotal = 0;
        for (int i = 0; i < n - 1; ++i) {
            distanciaTotal += calcularDistancia(pontos[i], pontos[i + 1]);
        }

        System.out.printf("Distancia total percorrida: %.2f\n", distanciaTotal);

        float deslocamento = calcularDistancia(pontos[0], pontos[n - 1]);
        System.out.printf("Deslocamento: %.2f\n", deslocamento);
        
        scanner.close();
    }
}
