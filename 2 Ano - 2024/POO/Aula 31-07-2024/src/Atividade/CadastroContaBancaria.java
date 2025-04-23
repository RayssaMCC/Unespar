package Atividade;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class CadastroContaBancaria extends JFrame {
    private JLabel label1, label2, label3;
    private JButton btAbrir, btGravar, btLimpar;
    private JTextField tfNumero, tfTitular, tfSaldo;
    private ContaBancaria contaBancaria;

    public static void main(String[] args) {
        JFrame frame = new CadastroContaBancaria();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }

    public CadastroContaBancaria() {
        inicializarComponentes();
        definirEventos();
    }

    public void inicializarComponentes() {
        setTitle("Cadastro usando arquivo texto");
        setBounds(250, 50, 800, 400);
        setBackground(new Color(150, 150, 150));
        label1 = new JLabel("Número");
        label2 = new JLabel("Titular");
        label3 = new JLabel("Saldo");
        btAbrir = new JButton("Abrir");
        btGravar = new JButton("Gravar");
        btLimpar = new JButton("Limpar");
        tfNumero = new JTextField();
        tfTitular = new JTextField();
        tfSaldo = new JTextField();
        setLayout(null);
        label1.setBounds(10, 15, 60, 20);
        label2.setBounds(10, 40, 45, 20);
        label3.setBounds(10, 65, 45, 20);
        btAbrir.setBounds(10, 100, 75, 20);
        btGravar.setBounds(95, 100, 75, 20);
        btLimpar.setBounds(180, 100, 75, 20);
        tfNumero.setBounds(80, 15, 55, 20);
        tfTitular.setBounds(80, 40, 255, 20);
        tfSaldo.setBounds(80, 65, 255, 20);
        add(label1);
        add(label2);
        add(label3);
        add(btAbrir);
        add(btGravar);
        add(btLimpar);
        add(tfNumero);
        add(tfTitular);
        add(tfSaldo);
        contaBancaria = new ContaBancaria();
    }

    public void definirEventos() {
        btLimpar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                tfNumero.setText("");
                tfTitular.setText("");
                tfSaldo.setText("");
            }
        });

        btGravar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if (tfNumero.getText().equals("")) {
                    JOptionPane.showMessageDialog(null, "O número não pode estar vazio!");
                    tfNumero.requestFocus();
                } else if (tfTitular.getText().equals("")) {
                    JOptionPane.showMessageDialog(null, "O titular não pode estar vazio!");
                    tfTitular.requestFocus();
                } else if (tfSaldo.getText().equals("")) {
                    JOptionPane.showMessageDialog(null, "O saldo não pode estar vazio!");
                    tfSaldo.requestFocus();
                } else {
                    contaBancaria.numero = tfNumero.getText();
                    contaBancaria.titular = tfTitular.getText();
                    contaBancaria.saldo = Double.parseDouble(tfSaldo.getText());
                    JOptionPane.showMessageDialog(null, contaBancaria.gravar("C:/Users/rayss/OneDrive/Unespar/Disciplinas/POO/Aula 31-07-2024"));
                }
            }
        });

        btAbrir.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                contaBancaria.numero = JOptionPane.showInputDialog(null, "Forneça o número a abrir: ");
                contaBancaria = contaBancaria.ler("C:/Users/rayss/OneDrive/Unespar/Disciplinas/POO/Aula 31-07-2024");
                if (contaBancaria != null) {
                    tfNumero.setText(contaBancaria.numero);
                    tfTitular.setText(contaBancaria.titular);
                    tfSaldo.setText(String.valueOf(contaBancaria.saldo));
                } else {
                    JOptionPane.showMessageDialog(null, "Conta Bancária não encontrada");
                }
            }
        });
    }
}