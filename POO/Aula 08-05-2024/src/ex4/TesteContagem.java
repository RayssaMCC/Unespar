package ex4;

public class TesteContagem {
    public static void main(String[] args) {
        Contagem contagem = new Contagem();

        System.out.println("Contagem de 0 a 10:");
        contagem.contar();

        System.out.println("Contagem até o número 15:");
        contagem.contar(15);

        System.out.println("Contagem de 5 até 19:");
        contagem.contar(5, 19);

        System.out.println("Contagem de 1 até 9 com pausa de 1 segundo:");
        contagem.contar(1, 9, 1);
    }
}
