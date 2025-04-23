import javax.swing.*;
import java.awt.event.*;

public class CadastroProduto {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Cadastro de Produto");
        frame.setSize(400, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(null);

        //Construção da interface para "Código"
        JLabel lblCodigo = new JLabel("Código");
        lblCodigo.setBounds(10, 10, 80, 25);
        frame.add(lblCodigo);

        JTextField txtCodigo = new JTextField();
        txtCodigo.setBounds(100, 10, 160, 25);
        frame.add(txtCodigo);
        
        //Construção da interface para "Descrição"
        JLabel lblDescricao = new JLabel("Descrição");
        lblDescricao.setBounds(10, 40, 80, 25);
        frame.add(lblDescricao);

        JTextField txtDescricao = new JTextField();
        txtDescricao.setBounds(100, 40, 160, 25);
        frame.add(txtDescricao);

        //Construção da interface para "Preço"
        JLabel lblPreco = new JLabel("Preço");
        lblPreco.setBounds(10, 70, 80, 25);
        frame.add(lblPreco);

        JTextField txtPreco = new JTextField();
        txtPreco.setBounds(100, 70, 160, 25);
        frame.add(txtPreco);

        //Construção da interface para o botão "Consultar"
        JButton btnConsultar = new JButton("Consultar");
        btnConsultar.setBounds(10, 110, 100, 25);
        frame.add(btnConsultar);

        //Construção da interface para o botão "Gravar"
        JButton btnGravar = new JButton("Gravar");
        btnGravar.setBounds(120, 110, 100, 25);
        frame.add(btnGravar);

        //Construção da interface para o botão "Limpar"
        JButton btnLimpar = new JButton("Limpar");
        btnLimpar.setBounds(230, 110, 100, 25);
        frame.add(btnLimpar);

        //Ação do botão "Gravar"
        btnGravar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if (txtCodigo.getText().isEmpty() || txtDescricao.getText().isEmpty() || txtPreco.getText().isEmpty()) {
                    JOptionPane.showMessageDialog(frame, "Todos os campos devem ser preenchidos.", "Erro", JOptionPane.ERROR_MESSAGE);
                    if (txtCodigo.getText().isEmpty()) {
                        txtCodigo.requestFocus();
                    } else if (txtDescricao.getText().isEmpty()) {
                        txtDescricao.requestFocus();
                    } else {
                        txtPreco.requestFocus();
                    }
                } else {
                    String codigo = txtCodigo.getText();
                    String descricao = txtDescricao.getText();
                    String preco = txtPreco.getText();
                    JOptionPane.showMessageDialog(frame, "Informações:\nCódigo: " + codigo + "\nDescrição: " + descricao + "\nPreço: " + preco);
                }
            }
        });

        //Ação do botão "Limpar"
        btnLimpar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                txtCodigo.setText("");
                txtDescricao.setText("");
                txtPreco.setText("");
            }
        });

        //Ação do botão "Consultar"
        btnConsultar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String codigo = JOptionPane.showInputDialog(frame, "Digite o código do produto:");
                if (codigo != null && !codigo.isEmpty()) {
                    JOptionPane.showMessageDialog(frame, "Código digitado: " + codigo);
                }
            }
        });

        frame.setVisible(true);
    }
}
