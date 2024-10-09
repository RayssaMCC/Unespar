import javax.swing.*;
import java.awt.event.*;

public class GuiCadastroCursos extends JPanel {
    JLabel label1, label2, label3, label4, label5, label6;
    JButton btGravar, btAlterar, btExcluir, btNovo, btLocalizar, btCancelar, btSair;
    static JTextField tfIdCurso, tfNome, tfCarga;
    JComboBox<String> cbTipo, cbModalidade, cbCodigo;
    private CursosDAO cursos;

    public GuiCadastroCursos() {
        inicializarComponentes();
        definirEventos();
    }

    public void inicializarComponentes() {
        setLayout(null);
    
        // Labels
        label1 = new JLabel("Id do Curso:");
        label1.setBounds(10, 10, 100, 20);
        label2 = new JLabel("Nome:");
        label2.setBounds(10, 40, 100, 20);
        label3 = new JLabel("Carga Horária:");
        label3.setBounds(10, 70, 100, 20);
        label4 = new JLabel("Tipo do Curso:");
        label4.setBounds(10, 100, 100, 20);
        label5 = new JLabel("Modalidade:");
        label5.setBounds(10, 130, 100, 20);
        label6 = new JLabel("Código do Depto:");
        label6.setBounds(10, 160, 100, 20);
    
        // TextFields
        tfIdCurso = new JTextField(8);
        tfIdCurso.setBounds(120, 10, 100, 20);
        tfNome = new JTextField(50);
        tfNome.setBounds(120, 40, 300, 20);
        tfCarga = new JTextField(10);
        tfCarga.setBounds(120, 70, 100, 20);
    
        // ComboBoxes
        cbTipo = new JComboBox<>(new String[]{"Graduação", "Pós-Graduação", "Extensão"});
        cbTipo.setBounds(120, 100, 300, 20);
        cbModalidade = new JComboBox<>(new String[]{"Presencial", "EAD", "Presencial/EAD"});
        cbModalidade.setBounds(120, 130, 300, 20);
        cbCodigo = new JComboBox<>(new String[]{"1", "2"});
        cbCodigo.setBounds(120, 160, 300, 20);
    
        // Botões
        btGravar = new JButton("Gravar");
        btGravar.setToolTipText("Gravar");
        btGravar.setBounds(10, 200, 100, 20);
    
        btAlterar = new JButton("Alterar");
        btAlterar.setToolTipText("Alterar");
        btAlterar.setBounds(120, 200, 100, 20);
    
        btExcluir = new JButton("Excluir");
        btExcluir.setToolTipText("Excluir");
        btExcluir.setBounds(230, 200, 100, 20);
    
        btLocalizar = new JButton("Localizar");
        btLocalizar.setToolTipText("Localizar");
        btLocalizar.setBounds(340, 200, 100, 20);
    
        btNovo = new JButton("Novo");
        btNovo.setToolTipText("Novo");
        btNovo.setBounds(450, 200, 100, 20);
    
        btCancelar = new JButton("Cancelar");
        btCancelar.setToolTipText("Cancelar");
        btCancelar.setBounds(560, 200, 100, 20);
    
        btSair = new JButton("Sair");
        btSair.setToolTipText("Sair");
        btSair.setBounds(670, 200, 100, 20);
    
        // Adicionando componentes
        add(label1);
        add(tfIdCurso);
        add(label2);
        add(tfNome);
        add(label3);
        add(tfCarga);
        add(label4);
        add(cbTipo);
        add(label5);
        add(cbModalidade);
        add(label6);
        add(cbCodigo);
        add(btNovo);
        add(btLocalizar);
        add(btGravar);
        add(btAlterar);
        add(btExcluir);
        add(btCancelar);
        add(btSair);
    
        setBotoes(true, true, false, false, false, false);
        cursos = new CursosDAO();
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
                if (validarCampos()) {
                    try {
                        int idCurso = Integer.parseInt(tfIdCurso.getText());
                        cursos.curso.setIdCurso(idCurso);
                        cursos.curso.setNomeCurso(tfNome.getText());
                        cursos.curso.setCargaHoraria(Integer.parseInt(tfCarga.getText()));
                        cursos.curso.setTipoCurso((String) cbTipo.getSelectedItem());
                        cursos.curso.setModalidadeCurso((String) cbModalidade.getSelectedItem());
                        cursos.curso.setCodigoCurso(Integer.parseInt((String) cbCodigo.getSelectedItem())); // Corrigido para converter para int
        
                        JOptionPane.showMessageDialog(null, cursos.atualizar(CursosDAO.INCLUSAO));
                        limparCampos();
                    } catch (NumberFormatException ex) {
                        JOptionPane.showMessageDialog(null, "Erro ao converter campos numéricos!");
                    }
                }
            }
        });
    
        btAlterar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if (validarCampos()) {
                    try {
                        int idCurso = Integer.parseInt(tfIdCurso.getText());
                        cursos.curso.setIdCurso(idCurso);
                        cursos.curso.setNomeCurso(tfNome.getText());
                        cursos.curso.setCargaHoraria(Integer.parseInt(tfCarga.getText()));
                        cursos.curso.setTipoCurso((String) cbTipo.getSelectedItem());
                        cursos.curso.setModalidadeCurso((String) cbModalidade.getSelectedItem());
    
                        JOptionPane.showMessageDialog(null, cursos.atualizar(CursosDAO.ALTERACAO));
                        limparCampos();
                    } catch (NumberFormatException ex) {
                        JOptionPane.showMessageDialog(null, "Erro ao converter campos numéricos!");
                    }
                }
            }
        });
    
        btExcluir.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if (tfIdCurso.getText().isEmpty()) {
                    JOptionPane.showMessageDialog(null, "O campo Id do curso não pode ser vazio!");
                    tfIdCurso.requestFocus();
                    return;
                }
    
                try {
                    int idCurso = Integer.parseInt(tfIdCurso.getText());
                    cursos.curso.setIdCurso(idCurso);
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(null, "O campo Id do curso deve ser número!");
                    tfIdCurso.requestFocus();
                    return;
                }
    
                cursos.localizar();
                int n = JOptionPane.showConfirmDialog(null, cursos.curso.getNomeCurso(), "Excluir o curso?", JOptionPane.YES_NO_OPTION);
                if (n == JOptionPane.YES_OPTION) {
                    JOptionPane.showMessageDialog(null, cursos.atualizar(CursosDAO.EXCLUSAO));
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
    
    public boolean validarCampos() {
        if (tfIdCurso.getText().isEmpty()) {
            JOptionPane.showMessageDialog(null, "O campo Id do curso não pode ser vazio!");
            tfIdCurso.requestFocus();
            return false;
        }
        if (tfNome.getText().isEmpty()) {
            JOptionPane.showMessageDialog(null, "O campo Nome não pode ser vazio!");
            tfNome.requestFocus();
            return false;
        }
        if (tfCarga.getText().isEmpty()) {
            JOptionPane.showMessageDialog(null, "O campo Carga Horária não pode ser vazio!");
            tfCarga.requestFocus();
            return false;
        }
        if (cbModalidade.getSelectedItem() == null) {
            JOptionPane.showMessageDialog(null, "O campo Modalidade não pode ser vazio!");
            cbModalidade.requestFocus();
            return false;
        }
        return true;
    }
    
    public void limparCampos() {
        tfIdCurso.setText("");
        tfNome.setText("");
        tfCarga.setText("");
        cbTipo.setSelectedIndex(-1);
        cbModalidade.setSelectedIndex(-1);
        cbCodigo.setSelectedIndex(-1);
        tfIdCurso.requestFocus();
        setBotoes(true, true, false, false, false, false);
    }
    
    public void atualizarCampos() {
        try {
            int idCurso = Integer.parseInt(tfIdCurso.getText());
            cursos.curso.setIdCurso(idCurso);
        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(null, "O campo Id do curso deve ser número!");
            tfIdCurso.requestFocus();
            return;
        }
    
        if (cursos.localizar()) {
            tfNome.setText(cursos.curso.getNomeCurso());
            tfCarga.setText(String.valueOf(cursos.curso.getCargaHoraria()));
            cbTipo.setSelectedItem(cursos.curso.getTipoCurso());
            cbModalidade.setSelectedItem(cursos.curso.getModalidadeCurso());
            cbCodigo.setSelectedItem(cursos.curso.getCodigoCurso());
            setBotoes(true, true, false, true, true, true);
        } else {
            JOptionPane.showMessageDialog(null, "Curso não encontrado!");
            limparCampos();
        }
    }

    public void setBotoes(boolean bNovo, boolean bLocalizar, boolean bGravar, boolean bAlterar, boolean bExcluir, boolean bCancelar) {
        btNovo.setEnabled(bNovo);
        btLocalizar.setEnabled(bLocalizar);
        btGravar.setEnabled(bGravar);
        btAlterar.setEnabled(bAlterar);
        btExcluir.setEnabled(bExcluir);
        btCancelar.setEnabled(bCancelar);
    }
}
