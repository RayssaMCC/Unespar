package Atividade.Curso;
import java.sql.*;

public class CursoDAO {
    public Curso curso;
    public BD bd;
    private PreparedStatement statement;
    private ResultSet resultSet;
    private String men, sql;
    public static final byte INCLUSAO = 1;
    public static final byte ALTERACAO = 2;
    public static final byte EXCLUSAO = 3;

    public CursoDAO() {
        bd = new BD();
        curso = new Curso();
    }

    public boolean localizar() {
        sql = "select * from cursos where id = ?";
        try {
            statement = bd.connection.prepareStatement(sql);
            statement.setInt(1, curso.getId());
            resultSet = statement.executeQuery();
            if (resultSet.next()) {
                curso.setId(resultSet.getInt(1));
                curso.setNome(resultSet.getString(2));
                curso.setDuracao(resultSet.getInt(3));
                curso.setDescricao(resultSet.getString(4));
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
                sql = "insert into cursos (id, nome, duracao, descricao) values (?,?,?,?)";
                statement = bd.connection.prepareStatement(sql);
                statement.setInt(1, curso.getId());
                statement.setString(2, curso.getNome());
                statement.setInt(3, curso.getDuracao());
                statement.setString(4, curso.getDescricao());
            } else if (operacao == ALTERACAO) {
                sql = "update cursos set nome = ?, duracao = ?, descricao = ? where id = ?";
                statement = bd.connection.prepareStatement(sql);
                statement.setString(1, curso.getNome());
                statement.setInt(2, curso.getDuracao());
                statement.setString(3, curso.getDescricao());
                statement.setInt(4, curso.getId());
            } else if (operacao == EXCLUSAO) {
                sql = "delete from cursos where id = ?";
                statement = bd.connection.prepareStatement(sql);
                statement.setInt(1, curso.getId());
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
