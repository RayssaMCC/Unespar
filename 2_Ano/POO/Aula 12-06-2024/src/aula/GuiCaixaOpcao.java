package aula;

import java.awt.event.*;
import javax.swing.*;
public class GuiCaixaOpcao extends JPanel {
    private JButton btVerificar, btMarcar, btDesmarcar;
    private JCheckBox ckIngles, ckInformatica;

    public GuiCaixaOpcao() {// construtor.
        inicializarComponentes();
        definirEventos ();
    }

    private void inicializarComponentes() {
        btVerificar = new JButton("Verificar");//Cada uma das opções.
        ckIngles = new JCheckBox("Inglês");
        ckInformatica = new JCheckBox("Informática");
        btMarcar = new JButton("Marcar");
        btDesmarcar = new JButton("Desmarcar");
        setLayout(null);
        add(btVerificar);//Adcionada as opções, a ordem que ela é add é a mesma que aparece na tela.
        add(ckIngles);
        add(ckInformatica);
        add(btMarcar);
        add(btDesmarcar);
        btVerificar.setBounds(20, 70, 100, 20);//Tamanho das caixas de opções.
        ckIngles.setBounds(15, 15, 100, 25);
        ckInformatica.setBounds(15, 40, 100, 25);
        btMarcar.setBounds(20, 100, 100, 20); 						
        btDesmarcar.setBounds(20, 130, 100, 20);
    }

    private void definirEventos() {
        btMarcar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent arg0) {
                ckInformatica.setSelected(true);
                ckIngles.setSelected(true);
            }
        });

        btDesmarcar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent arg0) {
                ckInformatica.setSelected(false); 						
                ckIngles.setSelected(false);
            }
        });

        btVerificar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent argO) {
                String selecao = "Selecionados: ";
                if (ckIngles.isSelected()) {
                    selecao += "\nInglês";
                }
                if (ckInformatica.isSelected()) {
                    selecao += "\nInformática";
                }
                JOptionPane.showMessageDialog(null, selecao);
            }
        });
    }
}