package Atividades;

import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MudarCorBotao {
    public static void main(String[] args) {
        //Cria o frame
        JFrame frame = new JFrame("Muda cor do botão");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 200);

        //Cria o painel
        JPanel panel = new JPanel();
        panel.setBackground(Color.WHITE);
        frame.add(panel);

        //Cria o botão
        JButton button = new JButton("Trocar");
        button.setBackground(Color.YELLOW);
        panel.add(button);

        //Adiciona o MouseListener para mudar a cor do botão
        button.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseEntered(MouseEvent e) {
                button.setBackground(Color.ORANGE);
            }

            @Override
            public void mouseExited(MouseEvent e) {
                button.setBackground(Color.YELLOW);
            }
        });

        //Exibe o frame
        frame.setVisible(true);
    }
}