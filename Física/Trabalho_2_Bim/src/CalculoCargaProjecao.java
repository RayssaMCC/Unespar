import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.plot.XYPlot;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;
import java.awt.*;

public class CalculoCargaProjecao {

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

        JLabel labelCarga = new JLabel("Carga q (μC):");
        labelCarga.setBounds(10, 50, 200, 25);
        frame.add(labelCarga);
        JTextField fieldCarga = new JTextField("4.0");
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
        XYSeries series = new XYSeries("Movimento Circular");
        XYSeriesCollection dataset = new XYSeriesCollection(series);
        JFreeChart chart = ChartFactory.createXYLineChart(
                "Trajetória da Partícula",
                "Posição X (m)","Posição Y (m)",
                dataset, PlotOrientation.VERTICAL,
                true,true,false);

        XYPlot plot = chart.getXYPlot();
        plot.getRenderer().setSeriesPaint(0, Color.RED);

        ChartPanel chartPanel = new ChartPanel(chart);
        chartPanel.setBounds(10, 230, 760, 300);
        frame.add(chartPanel);

        //Ação do botão de cálculo
        buttonCalcular.addActionListener(new ActionListener() {
            Timer timer;
            double theta = 0;

            @Override
            public void actionPerformed(ActionEvent e) {
                //Obtenção dos valores de entrada
                double m = Double.parseDouble(fieldMassa.getText());
                double v = Double.parseDouble(fieldVelocidade.getText());
                double r = Double.parseDouble(fieldRaio.getText());
                double q = Double.parseDouble(fieldCarga.getText());

                //Constante eletrostática k
                double k = 8.99e9;

                //Cálculo de Q
                double Q = (m * v * v * r) / (k * q);

                //Exibição do resultado no campo de texto
                fieldResultado.setText(String.format("%.6e", Q));

                //Configuração do gráfico
                if (timer != null) {
                    timer.stop();
                    series.clear();
                }
                timer = new Timer(16, new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        theta += v / r * 0.016;
                        if (theta > 2 * Math.PI) {
                            theta -= 2 * Math.PI;
                        }

                        double x = r * Math.cos(theta);
                        double y = r * Math.sin(theta);

                        series.add(x, y);
                        if (series.getItemCount() > 1000) {
                            series.remove(0);
                        }
                    }
                });
                timer.start();
            }
        });

        //Exibe a janela
        frame.setVisible(true);
    }
}