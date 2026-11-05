import javax.swing.JOptionPane;

public class Ex7 {

    public static void main(String[] args) {
        exibirMenu();
    }

    public static void exibirMenu() {
        String[] opcoes = {"Desconto", "Resistência", "Login", "Tabuada", "Inverter frase", "Verificar conteúdo", "Sair"};
        
        while (true) {
            // Exibir o menu e obter a escolha do usuário
            int escolha = JOptionPane.showOptionDialog(null, "Escolha uma opção:", "Menu Principal",
                            JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE, null, opcoes, opcoes[0]);

            // Realizar a ação de acordo com a escolha do usuário
            switch (escolha) {
                case 0: // Desconto
                    desconto();
                    break;
                case 1: // Resistência
                    resistencia();
                    break;
                case 2: // Login
                    login();
                    break;
                case 3: // Tabuada
                    exibirTabuada();
                    break;
                case 4: // Inverter frase
                    inverterFrase();
                    break;
                case 5: // Verificar conteúdo
                    verificarConteudo();
                    break;
                case 6: // Sair
                    JOptionPane.showMessageDialog(null, "Saindo do programa.");
                    return; // Encerra o programa
                default:
                    JOptionPane.showMessageDialog(null, "Opção inválida!");
            }
        }
    }
    
//------------------------------------------------------------------------------------------------------------------------------------------------

    public static void desconto() {
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

//------------------------------------------------------------------------------------------------------------------------------------------------

    public static void resistencia() {
        // Solicitar os valores das quatro resistências
        double[] resistencias = new double[4];
        for (int i = 0; i < 4; i++) {
            String input = JOptionPane.showInputDialog("Digite o valor da resistência " + (i + 1) + ":");
            try {
                resistencias[i] = Double.parseDouble(input);
            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(null, "Por favor, insira um número válido para a resistência.");
                return;
            }
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

//------------------------------------------------------------------------------------------------------------------------------------------------

    public static void login() {
        // Contador de tentativas
        int tentativasRestantes = 3;

        // Loop para solicitar login e senha até que sejam inseridos corretamente ou acabem as tentativas
        while (tentativasRestantes > 0) {
            // Solicitar login
            String login = JOptionPane.showInputDialog(null, "Digite o login:");

            // Solicitar senha
            String senha = JOptionPane.showInputDialog(null, "Digite a senha:");

            // Verificar se o login e a senha estão corretos
            if (login != null && senha != null && login.equals("java8") && senha.equals("java8")) {
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

//------------------------------------------------------------------------------------------------------------------------------------------------

    public static void exibirTabuada() {
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

//------------------------------------------------------------------------------------------------------------------------------------------------

    public static void inverterFrase() {
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

//------------------------------------------------------------------------------------------------------------------------------------------------

    public static void verificarConteudo() {
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
