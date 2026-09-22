package heranca;

public class Fazenda {

    public static void main(String[] args) {

        // BEM-TE-VI
        BemTeVi bemTeVi = new BemTeVi("Ben");

        System.out.println("===== BEM-TE-VI =====");
        bemTeVi.imprime();
        System.out.println("Fala: " + bemTeVi.falar());

        System.out.println("Voo:");
        bemTeVi.voar(3);

        // PAPAGAIO
        Papagaio papagaio = new Papagaio("Louro");

        System.out.println("\n===== PAPAGAIO =====");
        papagaio.setVocabulario("Louro José!");

        papagaio.imprime();
        System.out.println("Fala: " + papagaio.falar());

        System.out.println("Voo:");
        papagaio.voar(2);

        // VACA
        Vaca vaca = new Vaca("Mimosa", 3, false);

        System.out.println("\n===== VACA =====");
        vaca.imprime();
        System.out.println("Fala: " + vaca.falar());

        System.out.println("Correndo:");
        vaca.correr();

        System.out.println("Ordenha: " + vaca.ordenhar());

        // CACHORRO
        Cachorro cachorro = new Cachorro("Simba", 5, true);

        System.out.println("\n===== CACHORRO =====");
        cachorro.imprime();

        System.out.println("Correndo:");
        cachorro.correr();

        cachorro.setLateAlto();
        System.out.println("Latido alto: " + cachorro.falar());

        cachorro.setLateBaixo();
        System.out.println("Latido baixo: " + cachorro.falar());
    }
}