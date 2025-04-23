import javax.swing.*;
import java.awt.event.*;

public class CadastroCurso {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Cadastro de Cursos");
        frame.setSize(400, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(null);

        //Construção da interface para "Código"
        JLabel lblCodigo = new JLabel("Código:");
        lblCodigo.setBounds(10, 10, 100, 25);
        frame.add(lblCodigo);

        JTextField txtCodigo = new JTextField();
        txtCodigo.setBounds(120, 10, 160, 25);
        frame.add(txtCodigo);

        //Construção da interface para "Nome do Curso"
        JLabel lblNomeCurso = new JLabel("Nome do Curso:");
        lblNomeCurso.setBounds(10, 40, 100, 25);
        frame.add(lblNomeCurso);

        JTextField txtNomeCurso = new JTextField();
        txtNomeCurso.setBounds(120, 40, 160, 25);
        frame.add(txtNomeCurso);

        //Construção da interface para "Carga Horária"
        JLabel lblCargaHoraria = new JLabel("Carga Horária:");
        lblCargaHoraria.setBounds(10, 70, 100, 25);
        frame.add(lblCargaHoraria);

        JTextField txtCargaHoraria = new JTextField();
        txtCargaHoraria.setBounds(120, 70, 160, 25);
        frame.add(txtCargaHoraria);

        //Construção da interface para "Tipos de Cursos", usando caixa de seleção
        JLabel lblTipoCurso = new JLabel("Tipos de Cursos:");
        lblTipoCurso.setBounds(10, 100, 100, 25);
        frame.add(lblTipoCurso);

        JComboBox<String> cbTipoCurso = new JComboBox<>(new String[]{"", "Extensão", "Graduação", "Pós-Graduação"});
        cbTipoCurso.setBounds(120, 100, 160, 25);
        frame.add(cbTipoCurso);

        //Construção da interface para "Modalidade", usando caixa de seleção
        JLabel lblModalidade = new JLabel("Modalidade:");
        lblModalidade.setBounds(10, 130, 100, 25);
        frame.add(lblModalidade);

        JComboBox<String> cbModalidade = new JComboBox<>(new String[]{"", "Presencial", "EAD", "Presencial/EAD"});
        cbModalidade.setBounds(120, 130, 160, 25);
        frame.add(cbModalidade);

        //Construção da interface para o botão "Consultar"
        JButton btnConsultar = new JButton("Consultar");
        btnConsultar.setBounds(10, 170, 100, 25);
        frame.add(btnConsultar);

        //Construção da interface para o botão "Gravar"
        JButton btnGravar = new JButton("Gravar");
        btnGravar.setBounds(120, 170, 100, 25);
        frame.add(btnGravar);

        //Construção da interface para o botão "Limpar"
        JButton btnLimpar = new JButton("Limpar");
        btnLimpar.setBounds(230, 170, 100, 25);
        frame.add(btnLimpar);

        //Ação do botão "Gravar"
        btnGravar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if (txtCodigo.getText().isEmpty() || txtNomeCurso.getText().isEmpty() || txtCargaHoraria.getText().isEmpty() || cbTipoCurso.getSelectedItem().equals("") || cbModalidade.getSelectedItem().equals("")) {
                    JOptionPane.showMessageDialog(frame, "Todos os campos devem ser preenchidos.", "Erro", JOptionPane.ERROR_MESSAGE);
                    if (txtCodigo.getText().isEmpty()) {
                        txtCodigo.requestFocus();
                    } else if (txtNomeCurso.getText().isEmpty()) {
                        txtNomeCurso.requestFocus();
                    } else if (txtCargaHoraria.getText().isEmpty()) {
                        txtCargaHoraria.requestFocus();
                    } else if (cbTipoCurso.getSelectedItem().equals("")) {
                        cbTipoCurso.requestFocus();
                    } else {
                        cbModalidade.requestFocus();
                    }
                } else {
                    String codigo = txtCodigo.getText();
                    String nomeCurso = txtNomeCurso.getText();
                    String cargaHoraria = txtCargaHoraria.getText();
                    String tipoCurso = (String) cbTipoCurso.getSelectedItem();
                    String modalidade = (String) cbModalidade.getSelectedItem();
                    JOptionPane.showMessageDialog(frame, "Informações:\nCódigo: " + codigo + "\nNome do Curso: " + nomeCurso + "\nCarga Horária: " + cargaHoraria + "\nTipo de Curso: " + tipoCurso + "\nModalidade: " + modalidade);
                }
            }
        });

        //Ação do botão "Limpar"
        btnLimpar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                txtCodigo.setText("");
                txtNomeCurso.setText("");
                txtCargaHoraria.setText("");
                cbTipoCurso.setSelectedIndex(0);
                cbModalidade.setSelectedIndex(0);
            }
        });

        //Ação do botão "Consultar"
        btnConsultar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String codigo = JOptionPane.showInputDialog(frame, "Digite o código do curso:");
                if (codigo != null && !codigo.isEmpty()) {
                    JOptionPane.showMessageDialog(frame, "Código digitado: " + codigo);
                }
            }
        });

        frame.setVisible(true);
    }
}
