package Atividade.Curso;

import javax.swing.*;
import java.awt.event.*;
import java.awt.*;

public class GuiCadastroCursos extends JFrame {
    JLabel label1, label2, label3, label4;
    JButton btGravar, btAlterar, btExcluir, btNovo, btLocalizar, btCancelar, btSair;
    static JTextField tfId, tfNome, tfDuracao, tfDescricao;
    private CursoDAO cursos;

    public static void main(String[] args) {
        JFrame janela = new GuiCadastroCursos();
        janela.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        janela.setVisible(true);
    }

    public GuiCadastroCursos() {
        inicializarComponentes();
        definirEventos();
    }

    public void inicializarComponentes() {
        setLayout(new FlowLayout(FlowLayout.LEFT));
        setBounds(200, 200, 500, 200); // Ajustar a largura da janela
        setTitle("Cadastramento de Cursos");
        label1 = new JLabel("ID");
        label2 = new JLabel("Nome");
        label3 = new JLabel("Duração");
        label4 = new JLabel("Descrição");
        tfId = new JTextField(8);
        tfNome = new JTextField(35);
        tfDuracao = new JTextField(10);
        tfDescricao = new JTextField(30); // Aumentar o tamanho do campo de descrição
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
        add(tfDuracao);
        add(label4);
        add(tfDescricao);
        add(btNovo);
        add(btLocalizar);
        add(btGravar);
        add(btAlterar);
        add(btExcluir);
        add(btCancelar);
        add(btSair);
        setResizable(false);
        setBotoes(true, true, false, false, false, false);
        cursos = new CursoDAO();
        if (!cursos.bd.getConnection()) {
            JOptionPane.showMessageDialog(null, "Falha na conexão, o sistema será fechado!");
            System.exit(0);
        }
    }

    public void definirEventos() {
        btSair.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                cursos.bd.close();
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
                if (tfDuracao.getText().equals("")) {
                    JOptionPane.showMessageDialog(null, "O campo Duração não pode ser vazio!");
                    tfDuracao.requestFocus();
                    return;
                }
                if (tfDescricao.getText().equals("")) {
                    JOptionPane.showMessageDialog(null, "O campo Descrição não pode ser vazio!");
                    tfDescricao.requestFocus();
                    return;
                }
                cursos.curso.setId(Integer.parseInt(tfId.getText()));
                cursos.curso.setNome(tfNome.getText());
                cursos.curso.setDuracao(Integer.parseInt(tfDuracao.getText()));
                cursos.curso.setDescricao(tfDescricao.getText());
                JOptionPane.showMessageDialog(null, cursos.atualizar(CursoDAO.INCLUSAO));
                limparCampos();
            }
        });

        btAlterar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                cursos.curso.setId(Integer.parseInt(tfId.getText()));
                cursos.curso.setNome(tfNome.getText());
                cursos.curso.setDuracao(Integer.parseInt(tfDuracao.getText()));
                cursos.curso.setDescricao(tfDescricao.getText());
                JOptionPane.showMessageDialog(null, cursos.atualizar(CursoDAO.ALTERACAO));
                limparCampos();
            }
        });

        btExcluir.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                cursos.curso.setId(Integer.parseInt(tfId.getText()));
                cursos.localizar();
                int n = JOptionPane.showConfirmDialog(null, cursos.curso.getNome(), "Excluir o Curso?",
                        JOptionPane.YES_NO_OPTION);
                if (n == JOptionPane.YES_OPTION) {
                    JOptionPane.showMessageDialog(null, cursos.atualizar(CursoDAO.EXCLUSAO));
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
        tfDuracao.setText("");
        tfDescricao.setText("");
        tfId.requestFocus();
        setBotoes(true, true, false, false, false, false);
    }

    public void atualizarCampos() {
        cursos.curso.setId(Integer.parseInt(tfId.getText()));
        if (cursos.localizar()) {
            tfId.setText(String.valueOf(cursos.curso.getId()));
            tfNome.setText(cursos.curso.getNome());
            tfDuracao.setText(String.valueOf(cursos.curso.getDuracao()));
            tfDescricao.setText(cursos.curso.getDescricao());
            setBotoes(true, true, false, true, true, true);
        } else {
            JOptionPane.showMessageDialog(null, "Curso não encontrado!");
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