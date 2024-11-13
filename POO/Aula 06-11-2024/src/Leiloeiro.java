import javax.swing.*;
import java.util.ArrayList;
import java.util.List;


// Classe do Sujeito (ou Observable)
class Leiloeiro {
    private List<Licitante> licitantes = new ArrayList<>();
    private int lanceAtual = 0;

    // Método para registrar um licitante
    public void registrarLicitante(Licitante licitante) {
        licitantes.add(licitante);
    }

    // Método para aceitar um lance
    public void aceitarLance(int novoLance) {
        if (novoLance > lanceAtual) {
            lanceAtual = novoLance;
            JOptionPane.showMessageDialog(null, "Leiloeiro: Novo lance alto de " + lanceAtual);
            notificarLicitantes();
        } else {
            JOptionPane.showMessageDialog(null, "Leiloeiro: Lance de " + novoLance + " foi rejeitado. Menor que o lance atual.");
        }
    }

    // Método para notificar todos os licitantes
    private void notificarLicitantes() {
        for (Licitante licitante : licitantes) {
            licitante.atualizar(lanceAtual);
        }
    }
}
// Interface do Observador
interface Licitante {
    void atualizar(int lance);
}

// Classe concreta do Observador
class LicitanteConcreto implements Licitante {
    private String nome;

    public LicitanteConcreto(String nome) {
        this.nome = nome;
    }

    @Override
    public void atualizar(int lance) {
        JOptionPane.showMessageDialog(null, nome + " foi notificado: Novo lance alto é " + lance);
    }
}