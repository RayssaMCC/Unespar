import javax.swing.JOptionPane;

public class Ex4 {
    public static void main(String[] args) throws Exception {
        // Solicitar ao usuário o número desejado
        String input = JOptionPane.showInputDialog("Digite um número para ver a tabuada:");
        
        // Converter a entrada do usuário para um número inteiro
        int numero = Integer.parseInt(input);
                
        // Construir a tabuada
        StringBuilder tabuada = new StringBuilder();
        tabuada.append("Tabuada do ").append(numero).append(":\n");
        for (int i = 1; i <= 10; i++) {
             tabuada.append(numero).append(" x ").append(i).append(" = ").append(numero * i).append("\n");
         }
                
        // Exibir a tabuada
         JOptionPane.showMessageDialog(null, tabuada.toString());   
    }
}