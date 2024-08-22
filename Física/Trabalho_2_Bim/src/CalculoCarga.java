import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class CalculoCarga {
    public static void main(String[] args) {
        // Criando a janela principal
        JFrame frame = new JFrame("Calculadora de Carga Q");
        frame.setSize(400, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(null);

        // Rótulos e campos de texto para entrada
        JLabel labelMassa = new JLabel("Massa da partícula (kg):");
        labelMassa.setBounds(10, 20, 200, 25);
        frame.add(labelMassa);
        JTextField fieldMassa = new JTextField("0.8");
        fieldMassa.setBounds(220, 20, 165, 25);
        frame.add(fieldMassa);

        JLabel labelVelocidade = new JLabel("Velocidade (m/s):");
        labelVelocidade.setBounds(10, 110, 200, 25);
        frame.add(labelVelocidade);
        JTextField fieldVelocidade = new JTextField("50.0");
        fieldVelocidade.setBounds(220, 110, 165, 25);
        frame.add(fieldVelocidade);

        JLabel labelRaio = new JLabel("Distância ao longo do eixo x (m):");
        labelRaio.setBounds(10, 80, 200, 25);
        frame.add(labelRaio);
        JTextField fieldRaio = new JTextField("0.2");
        fieldRaio.setBounds(220, 80, 165, 25);
        frame.add(fieldRaio);

        JLabel labelCarga = new JLabel("Carga q da partícula (μC):");
        labelCarga.setBounds(10, 50, 200, 25);
        frame.add(labelCarga);
        JTextField fieldCarga = new JTextField("4.0");
        fieldCarga.setBounds(220, 50, 165, 25);
        frame.add(fieldCarga);

        // Botão de cálculo
        JButton buttonCalcular = new JButton("Calcular Q");
        buttonCalcular.setBounds(10, 150, 150, 25);
        frame.add(buttonCalcular);

        // Campo de texto para o resultado
        JLabel labelResultado = new JLabel("Carga Q (μC):");
        labelResultado.setBounds(10, 190, 200, 25);
        frame.add(labelResultado);
        JTextField fieldResultado = new JTextField();
        fieldResultado.setBounds(220, 190, 165, 25);
        fieldResultado.setEditable(false);
        frame.add(fieldResultado);

        // Ação do botão de cálculo
        buttonCalcular.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Obtenção dos valores de entrada
                double m = Double.parseDouble(fieldMassa.getText());
                double v = Double.parseDouble(fieldVelocidade.getText());
                double r = Double.parseDouble(fieldRaio.getText());
                double q = Double.parseDouble(fieldCarga.getText());

                // Constante eletrostática k
                double k = 8.99e9;

                // Cálculo de Q
                double Q = (m * v * v * r) / (k * q);

                // Exibição do resultado
                fieldResultado.setText(String.format("%.6e", Q));
            }
        });

        // Exibir a janela
        frame.setVisible(true);
    }
}