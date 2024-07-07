package aula;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class GuiMenuPrincipal extends JFrame {
    private Container contentPane;
    private JMenuBar mnBarra;
    private JMenu mnArquivo, mnExemplos;
    private JMenuItem miSair, miBotao, miRadio, miCaixaDeOpcao, miLabel, miLista, miCombo, miAreaDeTexto, miAbas, miMascara, miGridLayout1, 
    miFrameInterno, miFlayLayout3, miDialogoOpcao, miDialoMensagem, miDialogoConfirmacao, miBarraRolagem, miBarraProgresso, miBorderStyle, miBorderStyle2;

    public GuiMenuPrincipal() {
        inicializarComponentes();
        definirEventos();
    }

    private void inicializarComponentes() {
        setTitle("Menu Principal");
        setBounds(0, 0, 800, 600);
        contentPane = getContentPane();
        mnBarra = new JMenuBar();
        mnArquivo = new JMenu("Arquivo");
        mnArquivo.setMnemonic ('A');
        mnExemplos = new JMenu("Exemplos");
        mnExemplos.setMnemonic('E');
        String path = "HOO7.gif";
        miSair = new JMenuItem("Sair", new ImageIcon(getClass().getResource(path)));
        miSair.setAccelerator (KeyStroke.getKeyStroke(
                KeyEvent.VK_S, ActionEvent.ALT_MASK));
        miBotao = new JMenuItem("Botão");
        miRadio = new JMenuItem("Radio");
        miAreaDeTexto = new JMenuItem("Lista");
        miCaixaDeOpcao = new JMenuItem("Opcao");
        miCombo = new JMenuItem("Caixa de texto");
        miLabel = new JMenuItem("Label");
        miLista = new JMenuItem("Lista");
        miAbas = new JMenuItem("Abas");
        miMascara = new JMenuItem("Mascara");
        miGridLayout1 = new JMenuItem("GridLayout1");
        miFrameInterno = new JMenuItem("Frame interno");
        miFlayLayout3 = new JMenuItem("Flay Layout 3");
        miDialogoOpcao = new JMenuItem("Dialogo de Opcao");
        miDialoMensagem = new JMenuItem("Dialogo de mensagem");
        miDialogoConfirmacao = new JMenuItem("Dialogo de Confirmacao");
        miBarraRolagem = new JMenuItem("Barra de Rolagem");
        miBarraProgresso = new JMenuItem("Barra de Progresso");
        miBorderStyle = new JMenuItem("Border Style");
        miBorderStyle2 = new JMenuItem("Border Style 2");

        mnArquivo.add(miSair);
        mnExemplos.add (miBotao);
        mnExemplos.add(miRadio);
        mnExemplos.add(miAreaDeTexto);
        mnExemplos.add(miCaixaDeOpcao);
        mnExemplos.add(miCombo);
        mnExemplos.add(miLabel);
        mnExemplos.add(miLista);
        mnExemplos.add(miAbas);
        mnExemplos.add(miMascara);
        mnExemplos.add(miGridLayout1);
        mnExemplos.add(miFrameInterno);
        mnExemplos.add(miFlayLayout3);
        mnExemplos.add(miDialogoOpcao);
        mnExemplos.add(miDialoMensagem);
        mnExemplos.add(miDialogoConfirmacao);
        mnExemplos.add(miBarraRolagem);
        mnExemplos.add(miBarraProgresso);
        mnExemplos.add(miBorderStyle);
        mnExemplos.add(miBorderStyle2);

        mnBarra.add (mnArquivo);
        mnBarra.add(mnExemplos);
        setJMenuBar (mnBarra);
    }

    private void definirEventos() {
        miSair.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                System.exit(0);
            }
        });

        miBotao.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                GuiBotao botao = new GuiBotao();
                contentPane.removeAll();
                contentPane.add(botao);
                contentPane.validate();
            }
        });

        miRadio.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                GuiRadio radio = new GuiRadio();
                contentPane.removeAll();
                contentPane.add(radio);
                contentPane.validate();
            }
        });

        miAreaDeTexto.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                GuiAreaDeTexto areaDeTexto = new GuiAreaDeTexto();
                contentPane.removeAll();
                contentPane.add(areaDeTexto);
                contentPane.validate();
            }
        });

        miCaixaDeOpcao.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                GuiCaixaOpcao caixaDeOpcao = new GuiCaixaOpcao();
                contentPane.removeAll();
                contentPane.add(caixaDeOpcao);
                contentPane.validate();
            }
        });

        miCombo.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                GuiCombo combo = new GuiCombo();
                contentPane.removeAll();
                contentPane.add(combo);
                contentPane.validate();
            }
        });

        miLabel.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                GuiLabel label = new GuiLabel();
                contentPane.removeAll();
                contentPane.add(label);
                contentPane.validate();
            }
        });

        miLista.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                GuiLista lista = new GuiLista();
                contentPane.removeAll();
                contentPane.add(lista);
                contentPane.validate();
            }
        });

        miAbas.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                GuiAbas aba = new GuiAbas();
                contentPane.removeAll();
                contentPane.add(aba);
                contentPane.validate();
            }
        });

        miMascara.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                GuiMascara mascara = new GuiMascara();
                contentPane.removeAll();
                contentPane.add(mascara);
                contentPane.validate();
            }
        });

        miGridLayout1.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                GuiGridLayout1 gridLayout1 = new GuiGridLayout1();
                contentPane.removeAll();
                contentPane.add(gridLayout1);
                contentPane.validate();
            }
        });

        miFrameInterno.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                GuiFrameInterno frameInterno = new GuiFrameInterno();
                contentPane.removeAll();
                contentPane.add(frameInterno);
                contentPane.validate();
            }
        });

        miFrameInterno.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                GuiFlayLayout3 flayLayout3 = new GuiFlayLayout3();
                contentPane.removeAll();
                contentPane.add(flayLayout3);
                contentPane.validate();
            }
        });

        miDialogoOpcao.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                GuiDialogoOpcao dialogoOpcao = new GuiDialogoOpcao();
                contentPane.removeAll();
                contentPane.add(dialogoOpcao);
                contentPane.validate();
            }
        });

        miDialogoConfirmacao.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                GuiDialogoConfirmacao dialogoConfirmacao = new GuiDialogoConfirmacao();
                contentPane.removeAll();
                contentPane.add(dialogoConfirmacao);
                contentPane.validate();
            }
        });

        miBarraRolagem.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                GuiBarraRolagem barraRolagem = new GuiBarraRolagem();
                contentPane.removeAll();
                contentPane.add(barraRolagem);
                contentPane.validate();
            }
        });

        miBarraProgresso.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                GuiBarraProgresso barraProgresso = new GuiBarraProgresso();
                contentPane.removeAll();
                contentPane.add(barraProgresso);
                contentPane.validate();
            }
        });

        miBorderStyle.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                GuiBorderStyle borderStyle = new GuiBorderStyle();
                contentPane.removeAll();
                contentPane.add(borderStyle);
                contentPane.validate();
            }
        });

        miBorderStyle2.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                GuiBorderStyle2 borderStyle2 = new GuiBorderStyle2();
                contentPane.removeAll();
                contentPane.add(borderStyle2);
                contentPane.validate();
            }
        });

    }

    public static void abrir () {
        GuiMenuPrincipal frame = new GuiMenuPrincipal();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        Dimension tela = Toolkit.getDefaultToolkit().getScreenSize();
        frame.setLocation((tela.width - frame.getSize().width) / 2,
                (tela.height - frame.getSize().height) / 2);
        frame.setVisible(true);
    }
}