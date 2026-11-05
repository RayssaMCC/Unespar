package Atividade.Conta;

import javax.swing.*;
import java.awt.event.*;
import java.awt.*;

public class GuiCadastroContas extends JFrame {
    JLabel label1, label2, label3, label4;
    JButton btGravar, btAlterar, btExcluir, btNovo, btLocalizar, btCancelar, btSair;
    static JTextField tfId, tfNome, tfSaldo, tfTipo;
    private ContaDAO contas;

    public static void main(String[] args) {
        JFrame janela = new GuiCadastroContas();
        janela.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        janela.setVisible(true);
    }

    public GuiCadastroContas() {
        inicializarComponentes();
        definirEventos();
    }

    public void inicializarComponentes() {
        setLayout(new FlowLayout(FlowLayout.LEFT));
        setBounds(200, 200, 400, 200);
        setTitle("Cadastramento de Contas");
        label1 = new JLabel("ID");
        label2 = new JLabel("Nome");
        label3 = new JLabel("Saldo");
        label4 = new JLabel("Tipo");
        tfId = new JTextField(8);
        tfNome = new JTextField(35);
        tfSaldo = new JTextField(10);
        tfTipo = new JTextField(10);
        btGravar = new JButton("Gravar");
        btGravar.setToolTipText("Gravar");
        btAlterar = new JButton("Alterar");
        btAlterar.setToolTipText("Alterar");
        btExcluir = new JButton("Excluir");
        btExcluir.setToolTipText("Excluir");
        btLocalizar = new JButton("Localizar");
        btLocalizar.setToolTipText("Localizar");
        btNovo = new JButton("Novo");
        btNovo.setToolTipText("Novo");
        btCancelar = new JButton("Cancelar");
        btCancelar.setToolTipText("Cancelar");
        btSair = new JButton("Sair");
        btSair.setToolTipText("Sair");
        add(label1);
        add(tfId);
        add(label2);
        add(tfNome);
        add(label3);
        add(tfSaldo);
        add(label4);
        add(tfTipo);
        add(btNovo);
        add(btLocalizar);
        add(btGravar);
        add(btAlterar);
        add(btExcluir);
        add(btCancelar);
        add(btSair);
        setResizable(false);
        setBotoes(true, true, false, false, false, false);
        contas = new ContaDAO();
        if (!contas.bd.getConnection()) {
            JOptionPane.showMessageDialog(null, "Falha na conexão, o sistema será fechado!");
            System.exit(0);
        }
    }

    public void definirEventos() {
        btSair.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                contas.bd.close();
                System.exit(0);
            }
        });

        btNovo.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                limparCampos();
                setBotoes(false, false, true, false, false, true);
            }
        });

        btCancelar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                limparCampos();
            }
        });

        btGravar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if (tfId.getText().equals("")) {
                    JOptionPane.showMessageDialog(null, "O campo ID não pode ser vazio!");
                    tfId.requestFocus();
                    return;
                }
                if (tfNome.getText().equals("")) {
                    JOptionPane.showMessageDialog(null, "O campo Nome não pode ser vazio!");
                    tfNome.requestFocus();
                    return;
                }
                if (tfSaldo.getText().equals("")) {
                    JOptionPane.showMessageDialog(null, "O campo Saldo não pode ser vazio!");
                    tfSaldo.requestFocus();
                    return;
                }
                if (tfTipo.getText().equals("")) {
                    JOptionPane.showMessageDialog(null, "O campo Tipo não pode ser vazio!");
                    tfTipo.requestFocus();
                    return;
                }
                contas.conta.setId(Integer.parseInt(tfId.getText()));
                contas.conta.setNome(tfNome.getText());
                contas.conta.setSaldo(Double.parseDouble(tfSaldo.getText()));
                contas.conta.setTipo(tfTipo.getText());
                JOptionPane.showMessageDialog(null, contas.atualizar(ContaDAO.INCLUSAO));
                limparCampos();
            }
        });

        btAlterar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                contas.conta.setId(Integer.parseInt(tfId.getText()));
                contas.conta.setNome(tfNome.getText());
                contas.conta.setSaldo(Double.parseDouble(tfSaldo.getText()));
                contas.conta.setTipo(tfTipo.getText());
                JOptionPane.showMessageDialog(null, contas.atualizar(ContaDAO.ALTERACAO));
                limparCampos();
            }
        });

        btExcluir.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                contas.conta.setId(Integer.parseInt(tfId.getText()));
                contas.localizar();
                int n = JOptionPane.showConfirmDialog(null, contas.conta.getNome(), "Excluir a Conta?",
                        JOptionPane.YES_NO_OPTION);
                if (n == JOptionPane.YES_OPTION) {
                    JOptionPane.showMessageDialog(null, contas.atualizar(ContaDAO.EXCLUSAO));
                    limparCampos();
                }
            }
        });

        btLocalizar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                atualizarCampos();
            }
        });
    }

    public void limparCampos() {
        tfId.setText("");
        tfNome.setText("");
        tfSaldo.setText("");
        tfTipo.setText("");
        tfId.requestFocus();
        setBotoes(true, true, false, false, false, false);
    }

    public void atualizarCampos() {
        contas.conta.setId(Integer.parseInt(tfId.getText()));
        if (contas.localizar()) {
            tfId.setText(String.valueOf(contas.conta.getId()));
            tfNome.setText(contas.conta.getNome());
            tfSaldo.setText(String.valueOf(contas.conta.getSaldo()));
            tfTipo.setText(contas.conta.getTipo());
            setBotoes(true, true, false, true, true, true);
        } else {
            JOptionPane.showMessageDialog(null, "Conta não encontrada!");
            limparCampos();
        }
    }

    public void setBotoes(boolean bNovo, boolean bLocalizar, boolean bGravar, boolean bAlterar,
                          boolean bExcluir, boolean bCancelar) {
        btNovo.setEnabled(bNovo);
        btLocalizar.setEnabled(bLocalizar);
        btGravar.setEnabled(bGravar);
        btAlterar.setEnabled(bAlterar);
        btExcluir.setEnabled(bExcluir);
        btCancelar.setEnabled(bCancelar);
    }
}