package Atividade;

import javax.swing.*;
import java.util.ArrayList;
import java.util.List;

// Interface Observer
interface Observador {
    void atualizar(String status);
}

// Classe Subject (Filme)
class Filme {
    private List<Observador> observadores = new ArrayList<>();
    private String status;
    private String nome;

    public Filme(String nome) {
        this.nome = nome;
        this.status = "Não disponível";
    }

    public void adicionarObservador(Observador observador) {
        observadores.add(observador);
    }

    public void removerObservador(Observador observador) {
        observadores.remove(observador);
    }

    public void setStatus(String status) {
        this.status = status;
        notificarObservadores();
    }

    private void notificarObservadores() {
        for (Observador observador : observadores) {
            observador.atualizar(status);
        }
    }

    public String getNome() {
        return nome;
    }

    public String getStatus() {
        return status;
    }
}

// Classe Observador específico para o Departamento de Marketing
class Marketing implements Observador {
    @Override
    public void atualizar(String status) {
        JOptionPane.showMessageDialog(null, "Marketing: O status do filme foi atualizado para: " + status);
    }
}

// Classe Observador específico para o Departamento de Bilheteira
class Bilheteira implements Observador {
    @Override
    public void atualizar(String status) {
        JOptionPane.showMessageDialog(null, "Bilheteira: O status do filme foi atualizado para: " + status);
    }
}

// Classe Observador específico para o Assistente de Projeção
class AssistenteProjecao implements Observador {
    @Override
    public void atualizar(String status) {
        JOptionPane.showMessageDialog(null, "Assistente de Projeção: O status do filme foi atualizado para: " + status);
    }
}

// Classe principal do aplicativo
public class CinemaNotificacaoObserver {
    public static void main(String[] args) {
        Filme filme = new Filme("Avatar");

        // Adiciona observadores
        filme.adicionarObservador(new Marketing());
        filme.adicionarObservador(new Bilheteira());
        filme.adicionarObservador(new AssistenteProjecao());

        // Menu de interação
        while (true) {
            String[] opcoes = {"Em cartaz", "Retirado de cartaz", "Sair"};
            int escolha = JOptionPane.showOptionDialog(null,
                    "Escolha o novo status para o filme: " + filme.getNome(),
                    "Atualizar Status do Filme",
                    JOptionPane.DEFAULT_OPTION,
                    JOptionPane.INFORMATION_MESSAGE,
                    null,
                    opcoes,
                    opcoes[0]);

            if (escolha == 0) {
                filme.setStatus("Em cartaz");
            } else if (escolha == 1) {
                filme.setStatus("Retirado de cartaz");
            } else if (escolha == 2) {
                JOptionPane.showMessageDialog(null, "Saindo do sistema...");
                break;
            }
        }
    }
}
