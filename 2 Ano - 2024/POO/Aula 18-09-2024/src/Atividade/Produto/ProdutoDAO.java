package Atividade.Produto;
import java.sql.*;

public class ProdutoDAO {
    public Produto produto;
    public BD bd;
    private PreparedStatement statement;
    private ResultSet resultSet;
    private String men, sql;
    public static final byte INCLUSAO = 1;
    public static final byte ALTERACAO = 2;
    public static final byte EXCLUSAO = 3;

    public ProdutoDAO() {
        bd = new BD();
        produto = new Produto();
        if (!bd.getConnection()) {
            throw new RuntimeException("Falha na conexão com o banco de dados!");
        }
    }

    public boolean localizar() {
        sql = "select * from produtos where id = ?";
        try {
            statement = bd.connection.prepareStatement(sql);
            statement.setInt(1, produto.getId());
            resultSet = statement.executeQuery();
            if (resultSet.next()) {
                produto.setId(resultSet.getInt(1));
                produto.setNome(resultSet.getString(2));
                produto.setPreco(resultSet.getDouble(3));
                produto.setQuantidade(resultSet.getInt(4));
                return true;
            }
            return false;
        } catch (SQLException erro) {
            men = "Falha na operação " + erro.toString();
            return false;
        }
    }

    public String atualizar(int operacao) {
        men = "Operação realizada com sucesso!";
        try {
            if (operacao == INCLUSAO) {
                sql = "insert into produtos (id, nome, preco, quantidade) values (?,?,?,?)";
                statement = bd.connection.prepareStatement(sql);
                statement.setInt(1, produto.getId());
                statement.setString(2, produto.getNome());
                statement.setDouble(3, produto.getPreco());
                statement.setInt(4, produto.getQuantidade());
            } else if (operacao == ALTERACAO) {
                sql = "update produtos set nome = ?, preco = ?, quantidade = ? where id = ?";
                statement = bd.connection.prepareStatement(sql);
                statement.setString(1, produto.getNome());
                statement.setDouble(2, produto.getPreco());
                statement.setInt(3, produto.getQuantidade());
                statement.setInt(4, produto.getId());
            } else if (operacao == EXCLUSAO) {
                sql = "delete from produtos where id = ?";
                statement = bd.connection.prepareStatement(sql);
                statement.setInt(1, produto.getId());
            }

            if (statement.executeUpdate() == 0) {
                men = "Falha na operação!";
            }
        } catch (SQLException erro) {
            men = "Falha na operação " + erro.toString();
        }
        return men;
    }
}