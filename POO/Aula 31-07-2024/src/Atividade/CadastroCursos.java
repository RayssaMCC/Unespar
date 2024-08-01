package Atividade;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class CadastroCursos extends JFrame {
    private JLabel label1, label2, label3, label4;
    private JButton btAbrir, btGravar, btLimpar;
    private JTextField tfCodigo, tfNome, tfDescricao, tfDuracao;
    private Cursos cursos;

    public static void main(String[] args) {
        JFrame frame = new CadastroCursos();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }

    public CadastroCursos() {
        inicializarComponentes();
        definirEventos();
    }

    public void inicializarComponentes() {
        setTitle("Cadastro usando arquivo texto");
        setBounds(250, 50, 800, 400);
        setBackground(new Color(150, 150, 150));
        label1 = new JLabel("Código");
        label2 = new JLabel("Nome");
        label3 = new JLabel("Descrição");
        label4 = new JLabel("Duração (horas)");
        btAbrir = new JButton("Abrir");
        btGravar = new JButton("Gravar");
        btLimpar = new JButton("Limpar");
        tfCodigo = new JTextField();
        tfNome = new JTextField();
        tfDescricao = new JTextField();
        tfDuracao = new JTextField();
        setLayout(null);
        label1.setBounds(10, 15, 100, 20);
        label2.setBounds(10, 40, 100, 20);
        label3.setBounds(10, 65, 100, 20);
        label4.setBounds(10, 90, 100, 20);
        btAbrir.setBounds(10, 130, 75, 20);
        btGravar.setBounds(95, 130, 75, 20);
        btLimpar.setBounds(180, 130, 75, 20);
        tfCodigo.setBounds(120, 15, 255, 20);
        tfNome.setBounds(120, 40, 255, 20);
        tfDescricao.setBounds(120, 65, 255, 20);
        tfDuracao.setBounds(120, 90, 255, 20);
        add(label1);
        add(label2);
        add(label3);
        add(label4);
        add(btAbrir);
        add(btGravar);
        add(btLimpar);
        add(tfCodigo);
        add(tfNome);
        add(tfDescricao);
        add(tfDuracao);
        cursos = new Cursos();
    }

    public void definirEventos() {
        btLimpar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                tfCodigo.setText("");
                tfNome.setText("");
                tfDescricao.setText("");
                tfDuracao.setText("");
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
                } else if (tfDescricao.getText().equals("")) {
                    JOptionPane.showMessageDialog(null, "A descrição não pode estar vazia!");
                    tfDescricao.requestFocus();
                } else if (tfDuracao.getText().equals("")) {
                    JOptionPane.showMessageDialog(null, "A duração não pode estar vazia!");
                    tfDuracao.requestFocus();
                } else {
                    cursos.codigo = tfCodigo.getText();
                    cursos.nome = tfNome.getText();
                    cursos.descricao = tfDescricao.getText();
                    cursos.duracao = Integer.parseInt(tfDuracao.getText());
                    JOptionPane.showMessageDialog(null, cursos.gravar("C:/Users/rayss/OneDrive/Unespar/Disciplinas/POO/Aula 31-07-2024"));
                }
            }
        });

        btAbrir.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                cursos.codigo = JOptionPane.showInputDialog(null, "Forneça o código a abrir: ");
                cursos = cursos.ler("C:/Users/rayss/OneDrive/Unespar/Disciplinas/POO/Aula 31-07-2024");
                if (cursos != null) {
                    tfCodigo.setText(cursos.codigo);
                    tfNome.setText(cursos.nome);
                    tfDescricao.setText(cursos.descricao);
                    tfDuracao.setText(String.valueOf(cursos.duracao));
                } else {
                    JOptionPane.showMessageDialog(null, "Curso não encontrado");
                }
            }
        });
    }
}