import javax.swing.JOptionPane;

public class Ex5 {
    public static void main(String[] args) throws Exception {
        // Solicitar uma frase ao usuário
        String frase = JOptionPane.showInputDialog(null, "Digite uma frase:");

        // Remover espaços em branco da frase
        String fraseSemEspacos = frase.replace(" ", "");

        // Reverter a frase
        StringBuilder fraseReversaBuilder = new StringBuilder(fraseSemEspacos).reverse();
        String fraseReversa = fraseReversaBuilder.toString();

        // Exibir a frase reversa
        JOptionPane.showMessageDialog(null, "Frase fornecida: " + frase + "\n" + "Frase reversa sem espaços: " + fraseReversa);
    }
}
