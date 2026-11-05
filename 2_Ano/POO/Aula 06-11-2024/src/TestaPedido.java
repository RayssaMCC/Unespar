import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class TestaPedido {
    public static void main(String[] args) {
        // Criação do pedido e dos observers
        Pedido pedido = new Pedido();
        pedido.addObserver(new Estoque());
        pedido.addObserver(new Faturamento());

        // Criar a janela
        JFrame frame = new JFrame("Confirmação de Pagamento");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 200);
        frame.setLayout(new FlowLayout());

        // Botão de confirmação de pagamento
        JButton btnConfirmarPagamento = new JButton("Confirmar Pagamento");

        btnConfirmarPagamento.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Quando o botão for pressionado, altera o status do pedido para "Pago"
                pedido.setStatus("Pago");

                // Exibe uma mensagem de confirmação
                JOptionPane.showMessageDialog(null, "Pagamento confirmado!", "Confirmação", JOptionPane.INFORMATION_MESSAGE);
            }
        });

        // Adicionar o botão à janela
        frame.add(btnConfirmarPagamento);

        // Tornar a janela visível
        frame.setVisible(true);
    }
}