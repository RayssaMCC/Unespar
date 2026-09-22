package colecao2;

public class Main {

    public static void main(String[] args) {

        // Criando o colecionador
        Colecionador colecionador = new Colecionador();

        // Criando algumas latinhas
        LatinhaCerveja latinha1 = new LatinhaCerveja(
                1,
                "Skol",
                350,
                "10/01/2026",
                "10/07/2026"
        );

        LatinhaCerveja latinha2 = new LatinhaCerveja(
                2,
                "Brahma",
                350,
                "15/02/2026",
                "15/08/2026"
        );

        LatinhaCerveja latinha3 = new LatinhaCerveja(
                3,
                "Antarctica",
                473,
                "20/03/2026",
                "20/09/2026"
        );


        // Associando as latinhas aos seus apelidos
        colecionador.adicionarLatinha("Latinha azul", latinha1);
        colecionador.adicionarLatinha("Latinha vermelha", latinha2);
        colecionador.adicionarLatinha("Latinha grande", latinha3);


        // Buscando uma latinha pelo apelido
        System.out.println("===== LATINHA ENCONTRADA =====");

        LatinhaCerveja encontrada =
                colecionador.buscarLatinha("Latinha grande");

        if (encontrada != null) {
            encontrada.imprimeDados();
        } else {
            System.out.println("Latinha nao encontrada.");
        }
    }
}
