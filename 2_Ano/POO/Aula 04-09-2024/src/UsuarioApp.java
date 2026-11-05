import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.sql.*;
import java.util.Stack;

public class UsuarioApp extends JFrame {
    private JTable tabela;
    private JButton btProximo, btAnterior, btPrimeiro, btUltimo, btSair, btAdicionar, btRemover, btDesfazer;
    private DefaultTableModel modeloTabela;
    private Connection conexao;
    private int indiceAtual = 0;
    private Stack<Object[]> deletedRowsStack = new Stack<>();

    public UsuarioApp() {
        //Configuração da Janela
        setTitle("Navegando na tabela de Usuários");
        setSize(600, 400);
        setLayout(new BorderLayout());
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //Conexão com o banco de dados
        try {
            conexao = DriverManager.getConnection("jdbc:mysql://localhost/UsuariosDB", "root", "");
            Statement stmt = conexao.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM Usuarios");

            modeloTabela = new DefaultTableModel(new String[]{"Codigo", "Nome", "CPF", "Data_Nascimento", "Endereco", "Sexo", "Email"}, 0);
            while (rs.next()) {
                modeloTabela.addRow(new Object[]{
                    rs.getInt("Codigo"),
                    rs.getString("Nome"),
                    rs.getString("CPF"),
                    rs.getDate("Data_Nascimento"),
                    rs.getString("Endereco"),
                    rs.getString("Sexo"),
                    rs.getString("Email")
                });
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        //Configuração da JTable
        tabela = new JTable(modeloTabela);
        add(new JScrollPane(tabela), BorderLayout.CENTER);

        //Painel de botões
        JPanel painelBotoes = new JPanel();
        btProximo = new JButton("Próximo");
        btAnterior = new JButton("Anterior");
        btPrimeiro = new JButton("Primeiro");
        btUltimo = new JButton("Último");
        btSair = new JButton("Sair");
        btAdicionar = new JButton("Adicionar");
        btRemover = new JButton("Remover");
        btDesfazer = new JButton("Desfazer");

        painelBotoes.add(btPrimeiro);
        painelBotoes.add(btAnterior);
        painelBotoes.add(btProximo);
        painelBotoes.add(btUltimo);
        painelBotoes.add(btSair);
        painelBotoes.add(btAdicionar);
        painelBotoes.add(btRemover);
        painelBotoes.add(btDesfazer);

        add(painelBotoes, BorderLayout.SOUTH);

        //Ações dos botões
        btProximo.addActionListener(e -> navegar(1));
        btAnterior.addActionListener(e -> navegar(-1));
        btPrimeiro.addActionListener(e -> navegarParaPrimeiro());
        btUltimo.addActionListener(e -> navegarParaUltimo());
        btSair.addActionListener(e -> System.exit(0));
        btAdicionar.addActionListener(e -> adicionarItem());
        btRemover.addActionListener(e -> removerItem());
        btDesfazer.addActionListener(e -> desfazerRemocao());
    }

    private void navegar(int offset) {
        indiceAtual += offset;
        if (indiceAtual >= 0 && indiceAtual < modeloTabela.getRowCount()) {
            tabela.setRowSelectionInterval(indiceAtual, indiceAtual);
        } else {
            indiceAtual -= offset; //Reverte se sair do intervalo
        }
    }

    private void navegarParaPrimeiro() {
        indiceAtual = 0;
        tabela.setRowSelectionInterval(indiceAtual, indiceAtual);
    }

    private void navegarParaUltimo() {
        indiceAtual = modeloTabela.getRowCount() - 1;
        tabela.setRowSelectionInterval(indiceAtual, indiceAtual);
    }

    //Adiciona um novo item na tabela
    private void adicionarItem() {
        try {
            //Define os valores dos novos dados
            String nome = JOptionPane.showInputDialog(this, "Digite o nome do usuário:");
            String cpf = JOptionPane.showInputDialog(this, "Digite o CPF do usuário:");
            String dataNascimento = JOptionPane.showInputDialog(this, "Digite a data de nascimento (yyyy-mm-dd):");
            String endereco = JOptionPane.showInputDialog(this, "Digite o endereço do usuário:");
            String sexo = JOptionPane.showInputDialog(this, "Digite o sexo do usuário (M/F):");
            String email = JOptionPane.showInputDialog(this, "Digite o e-mail do usuário:");
    
            if (nome == null || cpf == null || dataNascimento == null || endereco == null || sexo == null || email == null) {
                JOptionPane.showMessageDialog(this, "Operação cancelada.");
                return;
            }
    
            String sql = "INSERT INTO Usuarios (Nome, CPF, Data_Nascimento, Endereco, Sexo, Email) VALUES (?, ?, ?, ?, ?, ?)";
            PreparedStatement pstmt = conexao.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS);
            pstmt.setString(1, nome);
            pstmt.setString(2, cpf);
            pstmt.setDate(3, Date.valueOf(dataNascimento)); // Converte string para java.sql.Date
            pstmt.setString(4, endereco);
            pstmt.setString(5, sexo.toUpperCase());
            pstmt.setString(6, email);
            pstmt.executeUpdate();
    
            //Obtem o ID gerado automaticamente
            ResultSet rs = pstmt.getGeneratedKeys();
            if (rs.next()) {
                int novoCodigo = rs.getInt(1);
                //Atualiza a tabela com os novos dados
                modeloTabela.addRow(new Object[]{novoCodigo, nome, cpf, Date.valueOf(dataNascimento), endereco, sexo.toUpperCase(), email});
            }
        } catch (SQLException e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(this, "Erro ao adicionar usuário: " + e.getMessage(), "Erro", JOptionPane.ERROR_MESSAGE);
        } catch (IllegalArgumentException e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(this, "Data de nascimento inválida: " + e.getMessage(), "Erro", JOptionPane.ERROR_MESSAGE);
        }
    }

    //Remove o item selecionado
    private void removerItem() {
        int linhaSelecionada = tabela.getSelectedRow();
        if (linhaSelecionada >= 0 && linhaSelecionada < modeloTabela.getRowCount()) {
            try {
                int codigo = (int) modeloTabela.getValueAt(linhaSelecionada, 0);
                String sql = "DELETE FROM Usuarios WHERE Codigo = ?";
                PreparedStatement pstmt = conexao.prepareStatement(sql);
                pstmt.setInt(1, codigo);
                pstmt.executeUpdate();

                // Armazena a linha removida na pilha
                Object[] deletedRow = new Object[modeloTabela.getColumnCount()];
                for (int i = 0; i < modeloTabela.getColumnCount(); i++) {
                    deletedRow[i] = modeloTabela.getValueAt(linhaSelecionada, i);
                }
                deletedRowsStack.push(deletedRow);

                //Remove a linha da tabela
                modeloTabela.removeRow(linhaSelecionada);
                if (linhaSelecionada > 0) {
                    linhaSelecionada--;
                }
                if (modeloTabela.getRowCount() > 0) {
                    tabela.setRowSelectionInterval(linhaSelecionada, linhaSelecionada);
                }
            } catch (SQLException e) {
                e.printStackTrace();
            }
        } else {
            JOptionPane.showMessageDialog(this, "Nenhuma linha selecionada.", "Erro", JOptionPane.ERROR_MESSAGE);
        }
    }

    //Desfaz a última remoção
    private void desfazerRemocao() {
        if (!deletedRowsStack.isEmpty()) {
            Object[] rowData = deletedRowsStack.pop();
            try {
                String sql = "INSERT INTO Usuarios (Codigo, Nome, CPF, Data_Nascimento, Endereco, Sexo, Email) VALUES (?, ?, ?, ?, ?, ?, ?)";
                PreparedStatement pstmt = conexao.prepareStatement(sql);
                pstmt.setInt(1, (int) rowData[0]);
                pstmt.setString(2, (String) rowData[1]);
                pstmt.setString(3, (String) rowData[2]);
                pstmt.setDate(4, (Date) rowData[3]);
                pstmt.setString(5, (String) rowData[4]);
                pstmt.setString(6, (String) rowData[5]);
                pstmt.setString(7, (String) rowData[6]);
                pstmt.executeUpdate();

                modeloTabela.addRow(rowData);
            } catch (SQLException e) {
                e.printStackTrace();
                JOptionPane.showMessageDialog(this, "Erro ao desfazer remoção: " + e.getMessage(), "Erro", JOptionPane.ERROR_MESSAGE);
            }
        } else {
            JOptionPane.showMessageDialog(this, "Nenhuma remoção para desfazer.", "Erro", JOptionPane.ERROR_MESSAGE);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new UsuarioApp().setVisible(true));
    }
}