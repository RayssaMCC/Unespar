import javax.swing.JOptionPane;

public class Ex1 {
    public static void main(String[] args) throws Exception {
        //Nome e valor do produto
        String nomeProduto = JOptionPane.showInputDialog("Digite o nome do produto:");
        String valorProdutoString = JOptionPane.showInputDialog("Digite o valor do produto:");
        double valorProduto = Double.parseDouble(valorProdutoString);

        //Valor final
        double valorFinal = 0;

        //Verificação de valor maior que 0 e descontos
        if(valorProduto < 0){
            JOptionPane.showMessageDialog(null, "O valor do produto não pode ser negativo.");
        }
        else if(valorProduto >= 50 && valorProduto < 200) {
            valorFinal = valorProduto * 0.95; //5% de desconto
        }
        else if(valorProduto >=200 && valorProduto < 500){
            valorFinal = valorProduto * 0.94; //6% de desconto
        }
        else if(valorProduto >=500 && valorProduto < 1000){
            valorFinal = valorProduto * 0.93; //7% de desconto
        }
        else if(valorProduto >= 1000){
            valorFinal = valorProduto * 0.92; //8% de desconto
        }

        // Exibir apenas se o valor do produto for válido
        if (valorProduto >= 0) {
            JOptionPane.showMessageDialog(null, "Nome do produto: " + nomeProduto + "\n" + "Preço inicial: " + valorProduto + "\n" + "Preço após o desconto: " + valorFinal);
        }
    }
}
