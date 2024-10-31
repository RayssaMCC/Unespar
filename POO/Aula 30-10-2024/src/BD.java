import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class BD {
    private static BD instance;
    private Connection connection = null;
    private final String DRIVER = "com.mysql.cj.jdbc.Driver";
    private final String DBNAME = "banco";
    private final String URL = "jdbc:mysql://localhost:3306/" + DBNAME;
    private final String LOGIN = "root";
    private final String SENHA = "";

    // Construtor privado para evitar instanciamento externo
    private BD() {
        // Inicializa a conexão ao criar a instância
        getConnection();
    }

    // Método público para obter a instância do Singleton
    public static BD getInstance() {
        if (instance == null) {
            instance = new BD();
        }
        return instance;
    }

    /**
     * Método que faz a conexão com o banco de dados.
     * Retorna true se houve sucesso, ou false em caso negativo.
     */
    public boolean getConnection() {
        try {
            Class.forName(DRIVER);
            connection = DriverManager.getConnection(URL, LOGIN, SENHA);
            System.out.println("Conectou");
            return true;
        } catch (ClassNotFoundException erro) {
            System.out.println("Driver não encontrado: " + erro.toString());
            return false;
        } catch (SQLException erro) {
            System.out.println("Falha ao conectar: " + erro.toString());
            return false;
        }
    }

    public Connection getConnectionInstance() {
        return connection;
    }

    public void close() {
        try {
            if (connection != null && !connection.isClosed()) {
                connection.close();
                System.out.println("Desconectou");
            }
        } catch (SQLException erro) {
            System.out.println("Erro ao desconectar: " + erro.toString());
        }
    }
}