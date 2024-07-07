import javax.swing.*;
import java.awt.event.*;

public class CadastroConta {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Cadastro de Contas");
        frame.setSize(400, 250);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(null);

        //Construção da interface para "Num. Conta"
        JLabel lblNumConta = new JLabel("Num. Conta");
        lblNumConta.setBounds(10, 10, 80, 25);
        frame.add(lblNumConta);

        JTextField txtNumConta = new JTextField();
        txtNumConta.setBounds(100, 10, 160, 25);
        frame.add(txtNumConta);

        //Construção da interface para "Titular"
        JLabel lblTitular = new JLabel("Titular");
        lblTitular.setBounds(10, 40, 80, 25);
        frame.add(lblTitular);

        JTextField txtTitular = new JTextField();
        txtTitular.setBounds(100, 40, 160, 25);
        frame.add(txtTitular);

        //Construção da interface para "Saldo"
        JLabel lblSaldo = new JLabel("Saldo");
        lblSaldo.setBounds(10, 70, 80, 25);
        frame.add(lblSaldo);

        JTextField txtSaldo = new JTextField();
        txtSaldo.setBounds(100, 70, 160, 25);
        frame.add(txtSaldo);

        //Construção da interface para "Tipo de Conta"
        JLabel lblTipoConta = new JLabel("Selecione o Tipo de Conta:");
        lblTipoConta.setBounds(10, 100, 160, 25);
        frame.add(lblTipoConta);

        //Construção dos botões de seleção para tipo de conta
        JRadioButton rbContaCorrente = new JRadioButton("Conta Corrente");
        rbContaCorrente.setBounds(100, 120, 150, 25);
        rbContaCorrente.setSelected(true);
        frame.add(rbContaCorrente);

        JRadioButton rbPoupanca = new JRadioButton("Poupança");
        rbPoupanca.setBounds(100, 140, 150, 25);
        frame.add(rbPoupanca);

        ButtonGroup group = new ButtonGroup();
        group.add(rbContaCorrente);
        group.add(rbPoupanca);

        //Construção da interface para o botão "Consultar"
        JButton btnConsultar = new JButton("Consultar");
        btnConsultar.setBounds(10, 180, 100, 25);
        frame.add(btnConsultar);

        //Construção da interface para o botão "Gravar"
        JButton btnGravar = new JButton("Gravar");
        btnGravar.setBounds(120, 180, 100, 25);
        frame.add(btnGravar);

        //Construção da interface para o botão "Limpar"
        JButton btnLimpar = new JButton("Limpar");
        btnLimpar.setBounds(230, 180, 100, 25);
        frame.add(btnLimpar);

        //Ação do botão "Gravar"
        btnGravar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if (txtNumConta.getText().isEmpty() || txtTitular.getText().isEmpty() || txtSaldo.getText().isEmpty()) {
                    JOptionPane.showMessageDialog(frame, "Todos os campos devem ser preenchidos.", "Erro", JOptionPane.ERROR_MESSAGE);
                    if (txtNumConta.getText().isEmpty()) {
                        txtNumConta.requestFocus();
                    } else if (txtTitular.getText().isEmpty()) {
                        txtTitular.requestFocus();
                    } else {
                        txtSaldo.requestFocus();
                    }
                } else {
                    String numConta = txtNumConta.getText();
                    String titular = txtTitular.getText();
                    String saldo = txtSaldo.getText();
                    String tipoConta = rbContaCorrente.isSelected() ? "Conta Corrente" : "Poupança";
                    JOptionPane.showMessageDialog(frame, "Informações:\nNum. Conta: " + numConta + "\nTitular: " + titular + "\nSaldo: " + saldo + "\nTipo de Conta: " + tipoConta);
                }
            }
        });

        //Ação do botão "Limpar"
        btnLimpar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                txtNumConta.setText("");
                txtTitular.setText("");
                txtSaldo.setText("");
                rbContaCorrente.setSelected(true);
            }
        });

        //Ação do botão "Consultar"
        btnConsultar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String numConta = JOptionPane.showInputDialog(frame, "Digite o número da conta:");
                if (numConta != null && !numConta.isEmpty()) {
                    JOptionPane.showMessageDialog(frame, "Número da conta digitado: " + numConta);
                }
            }
        });

        frame.setVisible(true);
    }
}
