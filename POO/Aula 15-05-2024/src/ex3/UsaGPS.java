package ex3;

public class UsaGPS {
    public static void main(String[] args) {
        // Testando o construtor default
        GPS gps1 = new GPS();
        System.out.println("GPS 1:");
        gps1.mostrar();
        System.out.println();

        // Testando o construtor com parâmetros
        GPS gps2 = new GPS("Português", "Rota para casa");
        System.out.println("GPS 2:");
        gps2.mostrar();
        System.out.println();

        // Testando os métodos definirIdioma e definirRota
        gps1.definirIdioma("Inglês");
        gps1.definirRota("Rota para o trabalho");
        System.out.println("GPS 1 após definir idioma e rota:");
        gps1.mostrar();
    }
}