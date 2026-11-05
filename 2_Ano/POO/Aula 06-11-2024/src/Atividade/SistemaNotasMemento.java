package Atividade;

import javax.swing.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

// Classe Memento que guarda o estado das notas
class NotaMemento {
    private final List<Double> notasSalvas;

    public NotaMemento(List<Double> notas) {
        this.notasSalvas = new ArrayList<>(notas);
    }

    public List<Double> getNotasSalvas() {
        return notasSalvas;
    }
}

// Classe que faz o gerenciamento das notas
class NotaCalculador {
    private List<Double> notas = new ArrayList<>();

    public void adicionarNota(double nota) {
        notas.add(nota);
    }

    public void removerNota(double nota) {
        notas.remove(nota);
    }

    public List<Double> getNotas() {
        return notas;
    }

    public NotaMemento salvarEstado() {
        return new NotaMemento(notas);
    }

    public void restaurarEstado(NotaMemento memento) {
        notas = new ArrayList<>(memento.getNotasSalvas());
    }

    public String listarNotas() {
        if (notas.isEmpty()) return "Nenhuma nota disponível";
        StringBuilder sb = new StringBuilder("Notas: ");
        for (double nota : notas) {
            sb.append(nota).append(" ");
        }
        return sb.toString();
    }
}

// Classe CareTaker que guarda o histórico dos estados das notas
class CareTaker {
    private Stack<NotaMemento> historico = new Stack<>();

    public void salvar(NotaMemento memento) {
        historico.push(memento);
    }

    public NotaMemento desfazer() {
        if (!historico.isEmpty()) {
            return historico.pop();
        }
        return null;
    }
}

// Classe principal do aplicativo
public class SistemaNotasMemento {
    public static void main(String[] args) {
        NotaCalculador calculador = new NotaCalculador();
        CareTaker caretaker = new CareTaker();

        while (true) {
            String[] opcoes = {"Adicionar Nota", "Remover Nota", "Listar Notas", "Salvar Estado", "Desfazer", "Sair"};
            int escolha = JOptionPane.showOptionDialog(null,
                    "Escolha uma ação:",
                    "Gerenciamento de Notas",
                    JOptionPane.DEFAULT_OPTION,
                    JOptionPane.INFORMATION_MESSAGE,
                    null,
                    opcoes,
                    opcoes[0]);

            switch (escolha) {
                case 0 -> {
                    String notaStr = JOptionPane.showInputDialog("Digite a nota a ser adicionada:");
                    if (notaStr != null) {
                        try {
                            double nota = Double.parseDouble(notaStr);
                            calculador.adicionarNota(nota);
                            JOptionPane.showMessageDialog(null, "Nota adicionada!");
                        } catch (NumberFormatException e) {
                            JOptionPane.showMessageDialog(null, "Entrada inválida. Por favor, insira um número.");
                        }
                    }
                }
                case 1 -> {
                    String notaStr = JOptionPane.showInputDialog("Digite a nota a ser removida:");
                    if (notaStr != null) {
                        try {
                            double nota = Double.parseDouble(notaStr);
                            calculador.removerNota(nota);
                            JOptionPane.showMessageDialog(null, "Nota removida!");
                        } catch (NumberFormatException e) {
                            JOptionPane.showMessageDialog(null, "Entrada inválida. Por favor, insira um número.");
                        }
                    }
                }
                case 2 -> {
                    JOptionPane.showMessageDialog(null, calculador.listarNotas());
                }
                case 3 -> {
                    caretaker.salvar(calculador.salvarEstado());
                    JOptionPane.showMessageDialog(null, "Estado salvo!");
                }
                case 4 -> {
                    NotaMemento memento = caretaker.desfazer();
                    if (memento != null) {
                        calculador.restaurarEstado(memento);
                        JOptionPane.showMessageDialog(null, "Alteração desfeita!");
                    } else {
                        JOptionPane.showMessageDialog(null, "Nenhum estado para desfazer.");
                    }
                }
                case 5 -> {
                    JOptionPane.showMessageDialog(null, "Saindo do sistema...");
                    System.exit(0);
                }
            }
        }
    }
}
