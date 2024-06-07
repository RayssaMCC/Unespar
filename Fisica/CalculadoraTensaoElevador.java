import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class CalculadoraTensaoElevador extends JFrame {

    //Declaração de componentes da interface gráfica
    private JLabel labelMassa, labelAceleracao, labelTensao, labelResultado;
    private JTextField campoMassa, campoAceleracao, campoTensao;
    private JButton botaoCalcular;

    //Construtor da classe CalculadoraTensaoElevador
    public CalculadoraTensaoElevador() {
        //Configuração da janela principal
        setTitle("Calculadora de Tensão do Cabo do Elevador");
        setSize(400, 250);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        //Criação do painel principal com layout em grade
        JPanel painel = new JPanel();
        painel.setLayout(new GridLayout(5, 2, 10, 10));
        painel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));

        //Definição de fontes para os labels e campos de texto
        Font fonteLabel = new Font(Font.SANS_SERIF, Font.BOLD, 14);
        Font fonteCampo = new Font(Font.SANS_SERIF, Font.PLAIN, 14);

        //Criação e configuração da interface
        labelMassa = new JLabel("Massa total (kg):");
        labelMassa.setFont(fonteLabel);
        painel.add(labelMassa);

        campoMassa = new JTextField(10);
        campoMassa.setFont(fonteCampo);
        painel.add(campoMassa);

        labelAceleracao = new JLabel("Aceleração (m/s²):");
        labelAceleracao.setFont(fonteLabel);
        painel.add(labelAceleracao);

        campoAceleracao = new JTextField(10);
        campoAceleracao.setFont(fonteCampo);
        painel.add(campoAceleracao);

        labelTensao = new JLabel("Tensão do cabo (N):");
        labelTensao.setFont(fonteLabel);
        painel.add(labelTensao);

        campoTensao = new JTextField(10);
        campoTensao.setFont(fonteCampo);
        campoTensao.setEditable(false);  //Campo de tensão é somente leitura
        painel.add(campoTensao);

        botaoCalcular = new JButton("Calcular");
        botaoCalcular.setFont(fonteLabel);
        botaoCalcular.setBackground(new Color(0, 153, 204));
        botaoCalcular.setForeground(Color.WHITE);
        //Adiciona um ActionListener para o botão Calcular (função será chamada/executada quando clicar nele)
        botaoCalcular.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                calcularTensao();
            }
        });
        painel.add(botaoCalcular);

        labelResultado = new JLabel("");
        labelResultado.setFont(fonteLabel);
        labelResultado.setForeground(Color.RED);
        painel.add(labelResultado);

        //Adiciona o painel à janela principal
        add(painel);
        setVisible(true);
    }

    //Método para calcular a tensão do cabo do elevador
    private void calcularTensao() {
        try {
            // Verifica se os campos não estão vazios
            if (campoMassa.getText().isEmpty() || campoAceleracao.getText().isEmpty()) {
                throw new NumberFormatException("Campos de entrada vazios.");
            }
    
            // Leitura e conversão dos valores de massa e aceleração
            double massa = Double.parseDouble(campoMassa.getText());
            double aceleracaoRelativa = Double.parseDouble(campoAceleracao.getText());
    
            // Verifica se a massa e a aceleração são valores válidos (não negativos)
            if (massa < 0 || aceleracaoRelativa < 0) {
                throw new NumberFormatException("Valores negativos não são permitidos.");
            }
    
            // Calcula a aceleração real do elevador
            double g = 9.8;
            double aceleracaoElevador = g - aceleracaoRelativa;
    
            // Calcula a tensão usando a segunda lei de Newton
            double tensao = (massa * aceleracaoElevador) - (massa * g);
            tensao = tensao * -1; // Ajusta o sinal da tensão
    
            // Exibe o resultado no campo de tensão
            campoTensao.setText(String.format("%.2f", tensao));
            labelResultado.setText("");
        } catch (NumberFormatException ex) {
            // Exibe mensagem de erro se os valores inseridos não forem válidos
            labelResultado.setText("Por favor, insira valores válidos para a massa e a aceleração.");
            campoTensao.setText("");
        }
    }

    //Método main para iniciar a aplicação
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new CalculadoraTensaoElevador();
            }
        });
    }
}