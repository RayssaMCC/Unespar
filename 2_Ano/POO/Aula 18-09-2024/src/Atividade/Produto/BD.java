package Atividade.Produto;
import java.sql.*;

public class BD {
    public Connection connection = null;
    private final String DRIVER = "com.mysql.cj.jdbc.Driver";
    private final String DBNAME = "cadastrodb";
    private final String URL = "jdbc:mysql://localhost:3306/" + DBNAME;
    private final String LOGIN = "root";
    private final String SENHA = "";

    public boolean getConnection() {
        try {
            Class.forName(DRIVER);
            connection = DriverManager.getConnection(URL, LOGIN, SENHA);
            System.out.println("Conectou");
            return true;
        } catch (ClassNotFoundException erro) {
            System.out.println("Driver nao encontrado " + erro.toString());
            return false;
        } catch (SQLException erro) {
            System.out.println("Falha ao conectar " + erro.toString());
            return false;
        }
    }

    public void close() {
        try {
            if (connection != null && !connection.isClosed()) {
                connection.close();
                System.out.println("Desconectou");
            }
        } catch (SQLException erro) {
            System.out.println("Erro ao desconectar " + erro.toString());
        }
    }
}