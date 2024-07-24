package Atividades;

import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.*;

public class ImgBotao {
    public static void main(String[] args) {
        //Cria o frame
        JFrame frame = new JFrame("Mostra Imagem");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 200);

        //Cria o painel
        JPanel panel = new JPanel();
        panel.setLayout(new BorderLayout());
        frame.add(panel);

        //Cria o botão
        JButton button = new JButton("Passe o mouse");
        panel.add(button, BorderLayout.NORTH);

        //Carrega a imagem
        ImageIcon imageIcon = new ImageIcon("src/Atividades/peixe.jpg");
        JLabel imageLabel = new JLabel(imageIcon);
        imageLabel.setHorizontalAlignment(JLabel.CENTER);
        imageLabel.setVisible(false); // Inicialmente invisível
        panel.add(imageLabel, BorderLayout.CENTER);

        //Adiciona o MouseListener para mostrar/esconder a imagem
        button.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseEntered(MouseEvent e) {
                imageLabel.setVisible(true);
            }

            @Override
            public void mouseExited(MouseEvent e) {
                imageLabel.setVisible(false);
            }
        });

        //Exibe o frame
        frame.setVisible(true);
    }
}