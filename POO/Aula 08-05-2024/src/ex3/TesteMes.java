package ex3;

import javax.swing.JOptionPane;

public class TesteMes {
    public static void main(String[] args) {
        // Solicitando ao usuário o número do mês
        String numeroMesStr = JOptionPane.showInputDialog("Digite o número do mês (1 a 12):");
        int numeroMes = Integer.parseInt(numeroMesStr);

        // Solicitando ao usuário o código do idioma
        String codigoIdiomaStr = JOptionPane.showInputDialog("Digite o código do idioma (1 para português, 2 para inglês):");
        int codigoIdioma = Integer.parseInt(codigoIdiomaStr);

        // Obtendo o mês por extenso
        String mesPorExtenso = Mes.getMesPorExtenso(numeroMes, codigoIdioma);

        // Verificando se as informações são inválidas e exibindo a mensagem correspondente
        if (mesPorExtenso.equals("Código de idioma inválido") || mesPorExtenso.equals("Número do mês inválido")) {
            JOptionPane.showMessageDialog(null, mesPorExtenso);
        } 
        else {
            // Se as informações são válidas, exibe o mês por extenso
            JOptionPane.showMessageDialog(null, "Mês por extenso: " + mesPorExtenso);
        }
    }
}
