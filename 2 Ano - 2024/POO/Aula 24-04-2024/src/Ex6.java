import javax.swing.JOptionPane;

public class Ex6 {

    public static void main(String[] args) {
        // Solicitar uma frase ao usuário
        String frase = JOptionPane.showInputDialog(null, "Digite uma frase:");
        
        // Verifica o conteúdo da frase
        if(frase.toLowerCase().contains("sexo") || frase.toLowerCase().contains("sexual")) {
            JOptionPane.showMessageDialog(null, "Conteúdo impróprio");
        } 
        else {
            JOptionPane.showMessageDialog(null, "Conteúdo liberado");
        }
    }
}
