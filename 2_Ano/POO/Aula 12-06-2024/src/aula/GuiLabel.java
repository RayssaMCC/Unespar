package aula;

import java.awt.*;
import javax.swing.*;
public class GuiLabel extends JPanel {
    private JLabel label1, label2, label3, label4;
    private ImageIcon imageIcon1;

    public GuiLabel() {
        inicializarComponentes();
    }

    private void inicializarComponentes() {
        setLayout(new GridLayout(4, 1));// um layout com 4 linhas e uma coluna
        String path1 = "peixe.jpg";
        imageIcon1 = new ImageIcon(getClass().getResource(path1));
        setBackground(new Color(100, 220, 192));// cor do fundo da tela.
        label1 = new JLabel ("  Aprendendo", JLabel.LEFT);
        label1.setFont(new Font("Arial", Font.BOLD, 60));
        label1.setForeground(Color.white);
        label2 = new JLabel(imageIcon1);
        label3 = new JLabel("Inserir  ", JLabel.RIGHT);
        label3.setFont(new Font("Arial", Font.BOLD, 30));
        label3.setForeground(Color.blue);
        label4 = new JLabel("Labels e Imagens", imageIcon1, JLabel.CENTER);
        label4.setFont(new Font("Serif", Font.BOLD, 40));
        label4.setForeground (Color .black);
        add(label1);// aqui que o numero de linhas e colunas interfere, na disposição das labels na tela.
        add(label2);
        add(label3);
        add(label4);
    }
}