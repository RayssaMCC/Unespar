package Atividade;

import javax.swing.*;

// Interface State
interface State {
    void proximoEstado(Pedido pedido);
    void cancelarPedido(Pedido pedido);
}

// Classe Pedido que mantém o estado atual
class Pedido {
    private State estadoAtual;

    public Pedido() {
        estadoAtual = new EmProcessamento();  // Estado inicial
    }

    public void setEstado(State novoEstado) {
        estadoAtual = novoEstado;
    }

    public void proximoEstado() {
        estadoAtual.proximoEstado(this);
    }

    public void cancelarPedido() {
        estadoAtual.cancelarPedido(this);
    }

    public String getStatus() {
        return estadoAtual.toString();
    }
}

// Estado EmProcessamento
class EmProcessamento implements State {
    @Override
    public void proximoEstado(Pedido pedido) {
        pedido.setEstado(new Enviado());
        JOptionPane.showMessageDialog(null, "Pedido agora está no estado: Enviado");
    }

    @Override
    public void cancelarPedido(Pedido pedido) {
        pedido.setEstado(new Cancelado());
        JOptionPane.showMessageDialog(null, "Pedido foi cancelado!");
    }

    @Override
    public String toString() {
        return "Em Processamento";
    }
}

// Estado Enviado
class Enviado implements State {
    @Override
    public void proximoEstado(Pedido pedido) {
        pedido.setEstado(new Entregue());
        JOptionPane.showMessageDialog(null, "Pedido agora está no estado: Entregue");
    }

    @Override
    public void cancelarPedido(Pedido pedido) {
        pedido.setEstado(new Cancelado());
        JOptionPane.showMessageDialog(null, "Pedido foi cancelado!");
    }

    @Override
    public String toString() {
        return "Enviado";
    }
}

// Estado Entregue
class Entregue implements State {
    @Override
    public void proximoEstado(Pedido pedido) {
        JOptionPane.showMessageDialog(null, "Pedido já foi entregue. Não é possível avançar para outro estado.");
    }

    @Override
    public void cancelarPedido(Pedido pedido) {
        JOptionPane.showMessageDialog(null, "Pedido já foi entregue e não pode ser cancelado.");
    }

    @Override
    public String toString() {
        return "Entregue";
    }
}

// Estado Cancelado
class Cancelado implements State {
    @Override
    public void proximoEstado(Pedido pedido) {
        JOptionPane.showMessageDialog(null, "Pedido foi cancelado e não pode avançar para outro estado.");
    }

    @Override
    public void cancelarPedido(Pedido pedido) {
        JOptionPane.showMessageDialog(null, "Pedido já está cancelado.");
    }

    @Override
    public String toString() {
        return "Cancelado";
    }
}

// Classe principal que testa o pedido e interage com o usuário
public class PedidoState {
    public static void main(String[] args) {
        Pedido pedido = new Pedido();

        while (true) {
            String[] opcoes = {"Próximo Estado", "Cancelar Pedido", "Sair"};
            int escolha = JOptionPane.showOptionDialog(null,
                    "Status atual do pedido: " + pedido.getStatus(),
                    "Processamento de Pedido",
                    JOptionPane.DEFAULT_OPTION,
                    JOptionPane.INFORMATION_MESSAGE,
                    null,
                    opcoes,
                    opcoes[0]);

            if (escolha == 0) { // Próximo Estado
                pedido.proximoEstado();
            } else if (escolha == 1) { // Cancelar Pedido
                pedido.cancelarPedido();
            } else if (escolha == 2) { // Sair
                JOptionPane.showMessageDialog(null, "Saindo do sistema...");
                break;
            }
        }
    }
}
