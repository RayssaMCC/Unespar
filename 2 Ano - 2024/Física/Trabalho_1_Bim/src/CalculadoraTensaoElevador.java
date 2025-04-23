/*QUESTÃO INICIAL:
Um elevador é puxado para cima por um cabo. O elevador e seu único ocupante têm uma massa toal de 2000 kg. 
Quando o ocupante deixa cair uma moeda, a aceleração da moeda em relação ao elevador é 8,00 m/s2 para baixo. 
Qual é a tensão do cabo? 

ALTERAÇÕES PARA A DIFICULTAÇÃO DO CÓDIGO:
- O elevador possui um peso fixo (2000kg)
- Peso médio por pessoa que entrará no elevador (75kg), usado para os cálculos futuros
- Número de pessoas no elevador
- Caso a quantidade de pessoas seja entre 0 e 8, calcula a tensão normalmente, 9 a 12 calcula a tensão e exibe mensagem de superlotação,
mais que 12 não calcula a tensão pois o cabo quebra. Valores negativos não serão aceitos
 -Aceleração da moeda é um valor aleatório entre 1.0 e 2.5
 - No final será mostrado a tensão do cabo e a aceleração do elevador*/

 import javax.swing.*;
 import java.awt.*;
 import java.awt.event.ActionEvent;
 import java.awt.event.ActionListener;
 import java.util.Random;
 
 public class CalculadoraTensaoElevador extends JFrame {
 
     // Declaração de componentes da interface gráfica
     private JLabel labelMassa, labelAceleracao, labelTensao, labelResultado, labelNumPessoas;
     private JLabel labelPesoElevador, labelPesoPessoa;
     private JTextField campoMassa, campoAceleracao, campoTensao, campoNumPessoas, campoAceleracaoElevador;
     private JButton botaoCalcular;
 
     // Variáveis fixas
     private final double pesoElevador = 2000.0;
     private final double pesoPessoa = 75.0;
 
     // Construtor da classe CalculadoraTensaoElevador
     public CalculadoraTensaoElevador() {
         // Configuração da janela principal
         setTitle("Calculadora de Tensão do Cabo do Elevador");
         setSize(400, 400); // Aumenta o tamanho da janela para acomodar os novos componentes
         setDefaultCloseOperation(EXIT_ON_CLOSE);
         setLocationRelativeTo(null);
 
         // Criação do painel principal com layout em grade
         JPanel painel = new JPanel();
         painel.setLayout(new GridLayout(9, 2, 10, 10)); // Aumenta o número de linhas para acomodar os novos componentes
         painel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
 
         // Definição de fontes para os labels e campos de texto
         Font fonteLabel = new Font(Font.SANS_SERIF, Font.BOLD, 14);
         Font fonteCampo = new Font(Font.SANS_SERIF, Font.PLAIN, 14);
 
         // Criação e configuração da interface
         labelNumPessoas = new JLabel("Número de pessoas:");
         labelNumPessoas.setFont(fonteLabel);
         painel.add(labelNumPessoas);
 
         campoNumPessoas = new JTextField(10);
         campoNumPessoas.setFont(fonteCampo);
         painel.add(campoNumPessoas);
 
         labelPesoElevador = new JLabel("Peso do elevador (kg):");
         labelPesoElevador.setFont(fonteLabel);
         painel.add(labelPesoElevador);
 
         JLabel valorPesoElevador = new JLabel(String.format("%.2f", pesoElevador));
         valorPesoElevador.setFont(fonteCampo);
         painel.add(valorPesoElevador);
 
         labelPesoPessoa = new JLabel("Peso médio de uma pessoa (kg):");
         labelPesoPessoa.setFont(fonteLabel);
         painel.add(labelPesoPessoa);
 
         JLabel valorPesoPessoa = new JLabel(String.format("%.2f", pesoPessoa));
         valorPesoPessoa.setFont(fonteCampo);
         painel.add(valorPesoPessoa);
 
         labelMassa = new JLabel("Massa total (kg):");
         labelMassa.setFont(fonteLabel);
         painel.add(labelMassa);
 
         campoMassa = new JTextField(10);
         campoMassa.setFont(fonteCampo);
         campoMassa.setEditable(false); // Campo de massa é somente leitura
         painel.add(campoMassa);
 
         labelAceleracao = new JLabel("Aceleração da moeda (m/s²):");
         labelAceleracao.setFont(fonteLabel);
         painel.add(labelAceleracao);
 
         campoAceleracao = new JTextField(10);
         campoAceleracao.setFont(fonteCampo);
         campoAceleracao.setEditable(false); // Campo de aceleração é somente leitura
         painel.add(campoAceleracao);
 
         JLabel labelAceleracaoElevador = new JLabel("Aceleração do elevador (m/s²):");
         labelAceleracaoElevador.setFont(fonteLabel);
         painel.add(labelAceleracaoElevador);
 
         campoAceleracaoElevador = new JTextField(10);
         campoAceleracaoElevador.setFont(fonteCampo);
         campoAceleracaoElevador.setEditable(false); // Campo de aceleração do elevador é somente leitura
         painel.add(campoAceleracaoElevador);
 
         labelTensao = new JLabel("Tensão do cabo (N):");
         labelTensao.setFont(fonteLabel);
         painel.add(labelTensao);
 
         campoTensao = new JTextField(10);
         campoTensao.setFont(fonteCampo);
         campoTensao.setEditable(false); // Campo de tensão é somente leitura
         painel.add(campoTensao);
 
         botaoCalcular = new JButton("Calcular");
         botaoCalcular.setFont(fonteLabel);
         botaoCalcular.setBackground(new Color(0, 153, 204));
         botaoCalcular.setForeground(Color.WHITE);
 
         // Adiciona um ActionListener para o botão Calcular
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
 
         // Adiciona o painel à janela principal
         add(painel);
         setVisible(true);
     }
 
     // Método para calcular a tensão do cabo do elevador
     private void calcularTensao() {
         try {
             // Verifica se o campo de número de pessoas não está vazio
             if (campoNumPessoas.getText().isEmpty()) {
                 throw new NumberFormatException("Campo de número de pessoas vazio.");
             }
 
             // Leitura e conversão do valor de número de pessoas
             int numPessoas = Integer.parseInt(campoNumPessoas.getText());
 
             // Verifica se o número de pessoas é um valor válido (não negativo)
             if (numPessoas < 0) {
                 throw new NumberFormatException("Número de pessoas negativo não é permitido.");
             }
 
             // Gera uma aceleração aleatória entre 1.0 e 2.5 m/s²
             Random random = new Random();
             double aceleracaoRelativa = 1.0 + (2.5 - 1.0) * random.nextDouble();
 
             // Calcula a massa total
             double massaTotal = pesoElevador + (numPessoas * pesoPessoa);
 
             // Calcula a aceleração real do elevador
             double g = 9.8;
             double aceleracaoElevador = g - aceleracaoRelativa;
 
             // Calcula a tensão usando a segunda lei de Newton
             double tensao = (massaTotal * aceleracaoElevador) - (massaTotal * g);
             tensao = tensao * -1; // Ajusta o sinal da tensão
 
             // Exibe as informações utilizadas para os cálculos
             campoMassa.setText(String.format("%.2f", massaTotal));
             campoAceleracao.setText(String.format("%.2f", aceleracaoRelativa));
             campoAceleracaoElevador.setText(String.format("%.2f", aceleracaoElevador));
 
             // Verifica o número de pessoas e exibe mensagens apropriadas
             if (numPessoas > 12) {
                 labelResultado.setText("O cabo quebrou! Número de pessoas: " + numPessoas);
                 campoTensao.setText("");
             } else if (numPessoas >= 9) {
                 labelResultado.setText("Superlotação! Número de pessoas: " + numPessoas);
                 campoTensao.setText(String.format("%.2f", tensao));
             } else {
                 labelResultado.setText("");
                 campoTensao.setText(String.format("%.2f", tensao));
             }
 
         } catch (NumberFormatException ex) {
             // Exibe mensagem de erro se os valores inseridos não forem válidos
             labelResultado.setText("Por favor, insira um número válido de pessoas.");
             campoMassa.setText("");
             campoAceleracao.setText("");
             campoTensao.setText("");
             campoAceleracaoElevador.setText("");
         }
     }
 
     // Método main para iniciar a aplicação
     public static void main(String[] args) {
         SwingUtilities.invokeLater(new Runnable() {
             @Override
             public void run() {
                 new CalculadoraTensaoElevador();
             }
         });
     }
 }