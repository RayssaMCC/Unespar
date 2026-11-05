package numeros;

public class Main {
    public static void main(String[] args) {

        Double[] numeros = {
            10.5,
            -32.5,
            -0.1,
            -0.9,
            3.9,
            3.1
        };

        for (Double numero : numeros) {

            System.out.println("Número: " + numero);
            System.out.println("Valor absoluto: " + Math.abs(numero));
            System.out.println("Decimal mais baixo: " + Math.floor(numero));
            System.out.println("Decimal mais alto: " + Math.ceil(numero));
            System.out.println("Valor mais próximo: " + Math.rint(numero));
            System.out.println("Arredondamento aritmético: " + Math.round(numero));
            System.out.println("----------------------------");
        }
    }
}
