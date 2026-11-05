package Atividade.Produto;
import javax.swing.*;
import java.awt.event.*;
import java.awt.*;

public class GuiCadastroProdutos extends JFrame {
    JLabel label1, label2, label3, label4;
    JButton btGravar, btAlterar, btExcluir, btNovo, btLocalizar, btCancelar, btSair;
    static JTextField tfId, tfNome, tfPreco, tfQuantidade;
    private ProdutoDAO produtos;

    public static void main(String[] args) {
        JFrame janela = new GuiCadastroProdutos();
        janela.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        janela.setVisible(true);
    }

    public GuiCadastroProdutos() {
        inicializarComponentes();
        definirEventos();
    }

    public void inicializarComponentes() {
        setLayout(new FlowLayout(FlowLayout.LEFT));
        setBounds(200, 200, 400, 200);
        setTitle("Cadastramento de Produtos");
        label1 = new JLabel("ID");
        label2 = new JLabel("Nome");
        label3 = new JLabel("Preço");
        label4 = new JLabel("Quantidade");
        tfId = new JTextField(8);
        tfNome = new JTextField(35);
        tfPreco = new JTextField(10);
        tfQuantidade = new JTextField(10);
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
        add(tfPreco);
        add(label4);
        add(tfQuantidade);
        add(btNovo);
        add(btLocalizar);
        add(btGravar);
        add(btAlterar);
        add(btExcluir);
        add(btCancelar);
        add(btSair);
        setResizable(false);
        setBotoes(true, true, false, false, false, false);
        produtos = new ProdutoDAO();
        if (!produtos.bd.getConnection()) {
            JOptionPane.showMessageDialog(null, "Falha na conexão, o sistema será fechado!");
            System.exit(0);
        }
    }

    public void definirEventos() {
        btSair.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                produtos.bd.close();
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
                if (tfPreco.getText().equals("")) {
                    JOptionPane.showMessageDialog(null, "O campo Preço não pode ser vazio!");
                    tfPreco.requestFocus();
                    return;
                }
                if (tfQuantidade.getText().equals("")) {
                    JOptionPane.showMessageDialog(null, "O campo Quantidade não pode ser vazio!");
                    tfQuantidade.requestFocus();
                    return;
                }
                produtos.produto.setId(Integer.parseInt(tfId.getText()));
                produtos.produto.setNome(tfNome.getText());
                produtos.produto.setPreco(Double.parseDouble(tfPreco.getText()));
                produtos.produto.setQuantidade(Integer.parseInt(tfQuantidade.getText()));
                JOptionPane.showMessageDialog(null, produtos.atualizar(ProdutoDAO.INCLUSAO));
                limparCampos();
            }
        });

        btAlterar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                produtos.produto.setId(Integer.parseInt(tfId.getText()));
                produtos.produto.setNome(tfNome.getText());
                produtos.produto.setPreco(Double.parseDouble(tfPreco.getText()));
                produtos.produto.setQuantidade(Integer.parseInt(tfQuantidade.getText()));
                JOptionPane.showMessageDialog(null, produtos.atualizar(ProdutoDAO.ALTERACAO));
                limparCampos();
            }
        });

        btExcluir.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                produtos.produto.setId(Integer.parseInt(tfId.getText()));
                produtos.localizar();
                int n = JOptionPane.showConfirmDialog(null, produtos.produto.getNome(), "Excluir o Produto?",
                        JOptionPane.YES_NO_OPTION);
                if (n == JOptionPane.YES_OPTION) {
                    JOptionPane.showMessageDialog(null, produtos.atualizar(ProdutoDAO.EXCLUSAO));
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
        tfPreco.setText("");
        tfQuantidade.setText("");
        tfId.requestFocus();
        setBotoes(true, true, false, false, false, false);
    }

    public void atualizarCampos() {
        produtos.produto.setId(Integer.parseInt(tfId.getText()));
        if (produtos.localizar()) {
            tfId.setText(String.valueOf(produtos.produto.getId()));
            tfNome.setText(produtos.produto.getNome());
            tfPreco.setText(String.valueOf(produtos.produto.getPreco()));
            tfQuantidade.setText(String.valueOf(produtos.produto.getQuantidade()));
            setBotoes(true, true, false, true, true, true);
        } else {
            JOptionPane.showMessageDialog(null, "Produto não encontrado!");
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