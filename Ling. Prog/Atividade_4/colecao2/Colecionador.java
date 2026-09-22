package colecao2;

import java.util.HashMap;
import java.util.Map;

public class Colecionador {

    private Map<String, LatinhaCerveja> latinhas;

    // Construtor
    public Colecionador() {
        latinhas = new HashMap<>();
    }

    // Método para associar uma latinha a um apelido
    public void adicionarLatinha(String apelido, LatinhaCerveja latinha) {
        latinhas.put(apelido, latinha);
    }

    // Método para buscar uma latinha pelo apelido
    public LatinhaCerveja buscarLatinha(String apelido) {
        return latinhas.get(apelido);
    }
}
