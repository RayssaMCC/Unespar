public class TestaLeilao {
    public static void main(String[] args) {
        Leiloeiro leiloeiro = new Leiloeiro();

        // Criando licitantes
        Licitante licitante1 = new LicitanteConcreto("Licitante 13");
        Licitante licitante2 = new LicitanteConcreto("Licitante 101");
        Licitante licitante3 = new LicitanteConcreto("Licitante 77");
        Licitante licitante4 = new LicitanteConcreto("Licitante 84");

        // Registrando os licitantes no leiloeiro
        leiloeiro.registrarLicitante(licitante1);
        leiloeiro.registrarLicitante(licitante2);
        leiloeiro.registrarLicitante(licitante3);
        leiloeiro.registrarLicitante(licitante4);

        // Aceitando lances
        leiloeiro.aceitarLance(50);
        leiloeiro.aceitarLance(120);
        leiloeiro.aceitarLance(110);  // Lance rejeitado
        leiloeiro.aceitarLance(150);
    }
}