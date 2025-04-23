package Atividade.Conta;
import java.sql.*;

public class ContaDAO {
    public Conta conta;
    public BD bd;
    private PreparedStatement statement;
    private ResultSet resultSet;
    private String men, sql;
    public static final byte INCLUSAO = 1;
    public static final byte ALTERACAO = 2;
    public static final byte EXCLUSAO = 3;

    public ContaDAO() {
        bd = new BD();
        conta = new Conta();
    }

    public boolean localizar() {
        sql = "select * from contas where id = ?";
        try {
            statement = bd.connection.prepareStatement(sql);
            statement.setInt(1, conta.getId());
            resultSet = statement.executeQuery();
            if (resultSet.next()) {
                conta.setId(resultSet.getInt(1));
                conta.setNome(resultSet.getString(2));
                conta.setSaldo(resultSet.getDouble(3));
                conta.setTipo(resultSet.getString(4));
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
                sql = "insert into contas (id, nome, saldo, tipo) values (?,?,?,?)";
                statement = bd.connection.prepareStatement(sql);
                statement.setInt(1, conta.getId());
                statement.setString(2, conta.getNome());
                statement.setDouble(3, conta.getSaldo());
                statement.setString(4, conta.getTipo());
            } else if (operacao == ALTERACAO) {
                sql = "update contas set nome = ?, saldo = ?, tipo = ? where id = ?";
                statement = bd.connection.prepareStatement(sql);
                statement.setString(1, conta.getNome());
                statement.setDouble(2, conta.getSaldo());
                statement.setString(3, conta.getTipo());
                statement.setInt(4, conta.getId());
            } else if (operacao == EXCLUSAO) {
                sql = "delete from contas where id = ?";
                statement = bd.connection.prepareStatement(sql);
                statement.setInt(1, conta.getId());
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
