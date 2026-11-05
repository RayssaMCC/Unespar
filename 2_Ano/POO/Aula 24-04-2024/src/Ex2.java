import javax.swing.JOptionPane;

public class Ex2 {
    public static void main(String[] args) throws Exception {
        // Solicitar os valores das quatro resistências
        double[] resistencias = new double[4];
        for (int i = 0; i < 4; i++) {
            String input = JOptionPane.showInputDialog("Digite o valor da resistência " + (i + 1) + ":");
            resistencias[i] = Double.parseDouble(input);
        }

        // Calcular resistência equivalente, maior e menor resistência
        double resistenciaEquivalente = 0;
        double maiorResistencia = resistencias[0];
        double menorResistencia = resistencias[0];

        for (int i = 0; i < 4; i++) {
            resistenciaEquivalente += resistencias[i];
            if (resistencias[i] > maiorResistencia) {
                maiorResistencia = resistencias[i];
            }
            if (resistencias[i] < menorResistencia) {
                menorResistencia = resistencias[i];
            }
        }

        // Mostrar os resultados
        JOptionPane.showMessageDialog(null, 
        "Resistências fornecidas: " + resistencias[0] + ", "+ resistencias[1] + ", " + resistencias[2] + ", " + resistencias[3] + "\n" + 
        "Resistência Equivalente: " + resistenciaEquivalente + "\n" +
        "Maior Resistência: " + maiorResistencia + "\n" +
        "Menor Resistência: " + menorResistencia);
    }
}