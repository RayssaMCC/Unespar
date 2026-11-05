package Atividade;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class CadastroProduto extends JFrame {
    private JLabel label1, label2, label3;
    private JButton btAbrir, btGravar, btLimpar;
    private JTextField tfCodigo, tfNome, tfPreco;
    private Produto produto;

    public static void main(String[] args) {
        JFrame frame = new CadastroProduto();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }

    public CadastroProduto() {
        inicializarComponentes();
        definirEventos();
    }

    public void inicializarComponentes() {
        setTitle("Cadastro usando arquivo texto");
        setBounds(250, 50, 800, 400);
        setBackground(new Color(150, 150, 150));
        label1 = new JLabel("Código");
        label2 = new JLabel("Nome");
        label3 = new JLabel("Preço");
        btAbrir = new JButton("Abrir");
        btGravar = new JButton("Gravar");
        btLimpar = new JButton("Limpar");
        tfCodigo = new JTextField();
        tfNome = new JTextField();
        tfPreco = new JTextField();
        setLayout(null);
        label1.setBounds(10, 15, 40, 20);
        label2.setBounds(10, 40, 45, 20);
        label3.setBounds(10, 65, 45, 20);
        btAbrir.setBounds(10, 100, 75, 20);
        btGravar.setBounds(95, 100, 75, 20);
        btLimpar.setBounds(180, 100, 75, 20);
        tfCodigo.setBounds(60, 15, 55, 20);
        tfNome.setBounds(60, 40, 255, 20);
        tfPreco.setBounds(60, 65, 255, 20);
        add(label1);
        add(label2);
        add(label3);
        add(btAbrir);
        add(btGravar);
        add(btLimpar);
        add(tfCodigo);
        add(tfNome);
        add(tfPreco);
        produto = new Produto();
    }

    public void definirEventos() {
        btLimpar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                tfCodigo.setText("");
                tfNome.setText("");
                tfPreco.setText("");
            }
        });

        btGravar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if (tfCodigo.getText().equals("")) {
                    JOptionPane.showMessageDialog(null, "O código não pode estar vazio!");
                    tfCodigo.requestFocus();
                } else if (tfNome.getText().equals("")) {
                    JOptionPane.showMessageDialog(null, "O nome não pode estar vazio!");
                    tfNome.requestFocus();
                } else if (tfPreco.getText().equals("")) {
                    JOptionPane.showMessageDialog(null, "O preço não pode estar vazio!");
                    tfPreco.requestFocus();
                } else {
                    produto.codigo = tfCodigo.getText();
                    produto.nome = tfNome.getText();
                    produto.descricao = ""; // Adicionei uma descrição vazia, pois não há campo para isso no formulário
                    produto.preco = Double.parseDouble(tfPreco.getText());
                    JOptionPane.showMessageDialog(null, produto.gravar("C:/Users/rayss/OneDrive/Unespar/Disciplinas/POO/Aula 31-07-2024"));
                }
            }
        });

        btAbrir.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                produto.codigo = JOptionPane.showInputDialog(null, "Forneça o código a abrir: ");
                produto = produto.ler("C:/Users/rayss/OneDrive/Unespar/Disciplinas/POO/Aula 31-07-2024");
                if (produto != null) {
                    tfCodigo.setText(produto.codigo);
                    tfNome.setText(produto.nome);
                    tfPreco.setText(String.valueOf(produto.preco));
                } else {
                    JOptionPane.showMessageDialog(null, "Produto não encontrado");
                }
            }
        });
    }
}