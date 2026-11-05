import javax.swing.*;

public class TestaSalarioMemento {
    public static void main(String[] args) {
        SalarioCalculador calculador = new SalarioCalculador(1000.0); // Salário inicial
        CareTaker careTaker = new CareTaker();

        while (true) {
            String opcao = JOptionPane.showInputDialog(null,
                    "Salário atual: R$" + calculador.getSalario() + "\n\n" +
                            "Escolha uma opção:\n" +
                            "1. Adicionar bônus\n" +
                            "2. Aplicar desconto\n" +
                            "3. Salvar estado\n" +
                            "4. Desfazer última alteração\n" +
                            "5. Sair");

            if (opcao == null || opcao.equals("5")) {
                break; // Sai do loop e encerra
            }

            switch (opcao) {
                case "1":
                    String bonusStr = JOptionPane.showInputDialog("Digite o valor do bônus:");
                    double bonus = Double.parseDouble(bonusStr);
                    calculador.adicionarBonus(bonus);
                    break;
                case "2":
                    String descontoStr = JOptionPane.showInputDialog("Digite o valor do desconto:");
                    double desconto = Double.parseDouble(descontoStr);
                    calculador.aplicarDesconto(desconto);
                    break;
                case "3":
                    careTaker.salvarMemento(calculador.salvarEstado());
                    JOptionPane.showMessageDialog(null, "Estado salvo com sucesso.");
                    break;
                case "4":
                    SalarioMemento estadoAnterior = careTaker.desfazer();
                    if (estadoAnterior != null) {
                        calculador.restaurarEstado(estadoAnterior);
                        JOptionPane.showMessageDialog(null, "Estado restaurado com sucesso.");
                    } else {
                        JOptionPane.showMessageDialog(null, "Nenhum estado anterior disponível.");
                    }
                    break;
                default:
                    JOptionPane.showMessageDialog(null, "Opção inválida.");
            }
        }
    }
}
