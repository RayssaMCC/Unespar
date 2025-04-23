package Atividades;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;

public class PosicaoImgAleatoria {
    public static void main(String[] args) {
        // Cria o frame
        JFrame frame = new JFrame("Mostra Imagem");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 500);

        // Cria o painel
        JPanel panel = new JPanel();
        panel.setLayout(null); // Usamos layout nulo para definir posições manualmente
        frame.add(panel);

        // Cria os botões
        JButton showButton = new JButton("Mostrar");
        showButton.setBounds(150, 10, 100, 30);
        panel.add(showButton);

        JButton hideButton = new JButton("Ocultar");
        hideButton.setBounds(260, 10, 100, 30);
        panel.add(hideButton);

        // Carrega a imagem
        ImageIcon imageIcon = new ImageIcon("src/Atividades/peixe.jpg");
        JLabel imageLabel = new JLabel(imageIcon);
        imageLabel.setBounds(0, 0, imageIcon.getIconWidth(), imageIcon.getIconHeight());
        imageLabel.setVisible(false); // Inicialmente invisível
        panel.add(imageLabel);

        // Gerador de números randômicos
        Random random = new Random();

        // Ação do botão "Mostrar"
        showButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int x = random.nextInt(panel.getWidth() - imageIcon.getIconWidth());
                int y = random.nextInt(panel.getHeight() - imageIcon.getIconHeight());
                imageLabel.setBounds(x, y, imageIcon.getIconWidth(), imageIcon.getIconHeight());
                imageLabel.setVisible(true);
            }
        });

        // Ação do botão "Ocultar"
        hideButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                imageLabel.setVisible(false);
            }
        });

        // Exibe o frame
        frame.setVisible(true);
    }
}
