package aula;

import javax.swing.JFrame;

public class CarregaGuiAreaDeTexto {
    public static void main(String[] args){
        JFrame frame = new JFrame ("Uso de Area de Texto");
        frame.setDefaultCloseOperation (JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().add (new GuiAreaDeTexto());
        frame.setBounds(0,0,500,300);
        frame.setVisible (true);
    }
}
