import javax.swing.JOptionPane;

public class Ex3 {
    public static void main(String[] args) throws Exception {
        // Definindo o login e a senha corretos
        String correto = "java8";

        // Contador de tentativas
        int tentativasRestantes = 3;

        // Loop para solicitar login e senha até que sejam inseridos corretamente ou acabem as tentativas
        while (tentativasRestantes > 0) {
            // Solicitar login
            String login = JOptionPane.showInputDialog(null, "Digite o login:");

            // Solicitar senha
            String senha = JOptionPane.showInputDialog(null, "Digite a senha:");

            // Verificar se o login e a senha estão corretos
            if (login != null && senha != null && login.equals(correto) && senha.equals(correto)) {
                JOptionPane.showMessageDialog(null, "Login realizado com sucesso!");
                break; // Se as credenciais estiverem corretas, saia do loop
            } 
            else {
                tentativasRestantes--;
                if (tentativasRestantes > 0) {
                    JOptionPane.showMessageDialog(null, "Login ou senha incorretos. Tentativas restantes: " + tentativasRestantes);
                } 
                else {
                    JOptionPane.showMessageDialog(null, "Você excedeu o número de tentativas. Tente novamente mais tarde.");
                }
            }
        }
    }
}
