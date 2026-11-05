import javax.swing.JOptionPane;

public class TestaMaquinaVendas {
    public static void main(String[] args) {
        MaquinaVendas maquina = new MaquinaVendas();

        while (true) {
            int opcao = JOptionPane.showOptionDialog(null, "Escolha uma ação:",
                    "Máquina de Vendas", JOptionPane.DEFAULT_OPTION, JOptionPane.INFORMATION_MESSAGE,
                    null, new String[]{"Inserir Moeda", "Selecionar Produto", "Sair"}, null);

            if (opcao == 0) {
                maquina.inserirMoeda();
            } else if (opcao == 1) {
                maquina.selecionarProduto();
            } else {
                break;
            }
        }
    }
}