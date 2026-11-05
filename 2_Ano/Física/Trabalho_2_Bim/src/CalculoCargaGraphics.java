import javax.swing.*; 
import java.awt.*; 
import java.awt.event.ActionEvent; 
import java.awt.event.ActionListener;

public class CalculoCargaGraphics {
    public static void main(String[] args) {
        //Criação da janela principal
        JFrame frame = new JFrame("Calculadora e Simulação de Carga Q");
        frame.setSize(800, 600);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(null);

        //Rótulos e campos de texto para entrada
        JLabel labelMassa = new JLabel("Massa da partícula (kg):");
        labelMassa.setBounds(10, 20, 200, 25);
        frame.add(labelMassa);
        JTextField fieldMassa = new JTextField();
        fieldMassa.setBounds(220, 20, 165, 25);
        frame.add(fieldMassa);

        JLabel labelVelocidade = new JLabel("Velocidade (m/s):");
        labelVelocidade.setBounds(10, 110, 200, 25);
        frame.add(labelVelocidade);
        JTextField fieldVelocidade = new JTextField();
        fieldVelocidade.setBounds(220, 110, 165, 25);
        frame.add(fieldVelocidade);

        JLabel labelRaio = new JLabel("Raio (m):");
        labelRaio.setBounds(10, 80, 200, 25);
        frame.add(labelRaio);
        JTextField fieldRaio = new JTextField();
        fieldRaio.setBounds(220, 80, 165, 25);
        frame.add(fieldRaio);

        JLabel labelCarga = new JLabel("Carga q (μC):");
        labelCarga.setBounds(10, 50, 200, 25);
        frame.add(labelCarga);
        JTextField fieldCarga = new JTextField();
        fieldCarga.setBounds(220, 50, 165, 25);
        frame.add(fieldCarga);

        JLabel labelResultado = new JLabel("Carga Q (μC):");
        labelResultado.setBounds(10, 190, 200, 25);
        frame.add(labelResultado);
        JTextField fieldResultado = new JTextField();
        fieldResultado.setBounds(220, 190, 165, 25);
        fieldResultado.setEditable(false);
        frame.add(fieldResultado);

        JButton buttonCalcular = new JButton("Calcular e Simular");
        buttonCalcular.setBounds(10, 150, 150, 25);
        frame.add(buttonCalcular);

        //Criação do gráfico de movimento da partícula
        ParticlePanel particlePanel = new ParticlePanel();
        particlePanel.setBounds(10, 230, 760, 300);
        frame.add(particlePanel);

        //Ação do botão de cálculo
        buttonCalcular.addActionListener(new ActionListener() {
            Timer timer;
            double theta = 0;

            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    //Obtenção dos valores de entrada
                    double m = Double.parseDouble(fieldMassa.getText());
                    double v = Double.parseDouble(fieldVelocidade.getText());
                    double r = Double.parseDouble(fieldRaio.getText());
                    double q = Double.parseDouble(fieldCarga.getText());

                    // Verificação de valores inválidos
                    if (m <= 0 || v <= 0 || r <= 0 || q <= 0) {
                        throw new IllegalArgumentException("Todos os valores devem ser positivos.");
                    }

                    //Constante eletrostática k
                    double k = 8.99e9;

                    //Cálculo de Q
                    double Q = (m * v * v * r) / (k * q);

                    //Exibição do resultado no campo de texto
                    fieldResultado.setText(String.format("%.6e", Q));

                    //Configuração do gráfico
                    if (timer != null) {
                        timer.stop();
                        particlePanel.clear();
                    }
                    timer = new Timer(16, new ActionListener() {
                        @Override
                        public void actionPerformed(ActionEvent e) {
                            theta += ((v/100) / r) * 0.08;
                            if (theta > 2 * Math.PI) {
                                theta -= 2 * Math.PI;
                            }

                            double x = r * Math.cos(theta);
                            double y = r * Math.sin(theta);

                            particlePanel.setPoint(x, y);
                            particlePanel.repaint();
                        }
                    });
                    timer.start();
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(frame, "Por favor, insira valores numéricos válidos.", "Erro de Entrada", JOptionPane.ERROR_MESSAGE);
                } catch (IllegalArgumentException ex) {
                    JOptionPane.showMessageDialog(frame, ex.getMessage(), "Erro de Entrada", JOptionPane.ERROR_MESSAGE);
                }
            }
        });
        //Exibe a janela
        frame.setVisible(true);
    }

    //Classe para desenhar a partícula em movimento
    static class ParticlePanel extends JPanel {
        private Point ponto = new Point();
        private Point centro = new Point();

        public void setPoint(double x, double y) {
            ponto.setLocation((int) (x * 100 + getWidth() / 2), (int) (y * 100 + getHeight() / 2));
        }

        public void clear() {
            ponto.setLocation(0, 0);
        }

        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            //Desenha a partícula
            g.setColor(Color.RED);
            g.fillOval(ponto.x, ponto.y, 5, 5);

            //Desenha o centro
            centro.setLocation(getWidth() / 2, getHeight() / 2);
            g.setColor(Color.BLUE);
            g.fillOval(centro.x - 5, centro.y - 5, 7, 7);
        }
    }
}