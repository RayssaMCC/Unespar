package aula;

import javax.swing.JButton;
import javax.swing.JFrame;
public class Exemplo {
    public static void main(String[] args){
        JFrame frame = new JFrame ("Uso de Botões");
        frame.setDefaultCloseOperation (JFrame.EXIT_ON_CLOSE);
        frame.add (new GuiBotao());
        frame.setBounds(0,0,500,300);// medidas da frame;
        frame.setVisible (true);// torna visivel no freme;
    }
}