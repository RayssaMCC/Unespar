import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Particula {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Simulação de Partícula");
        ParticleSimulationPanel panel = new ParticleSimulationPanel();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(panel);
        frame.setSize(600, 600);
        frame.setVisible(true);
    }
}

class ParticleSimulationPanel extends JPanel implements ActionListener {
    private final Timer timer;
    private double angle = 0.0;  // Ângulo inicial em radianos
    private final double angularVelocity;  // Velocidade angular
    private final int radius = 100;  // Raio da trajetória circular
    private final int centerX = 300;  // Centro da circunferência (eixo x)
    private final int centerY = 300;  // Centro da circunferência (eixo y)

    public ParticleSimulationPanel() {
        double v = 50.0;  // Velocidade tangencial em m/s
        this.angularVelocity = v / radius;  // ω = v / r
        
        timer = new Timer(20, this);  // Atualiza a cada 20ms
        timer.start();
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        
        // Desenha a trajetória circular
        g.setColor(Color.LIGHT_GRAY);
        g.drawOval(centerX - radius, centerY - radius, 2 * radius, 2 * radius);

        // Calcula a posição da partícula
        int x = (int) (centerX + radius * Math.cos(angle));
        int y = (int) (centerY + radius * Math.sin(angle));

        // Desenha a partícula
        g.setColor(Color.RED);
        g.fillOval(x - 10, y - 10, 20, 20);  // Desenha a partícula como um círculo
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        angle += angularVelocity * 0.02;  // Atualiza o ângulo (0.02s é o intervalo do Timer)
        if (angle >= 2 * Math.PI) {
            angle -= 2 * Math.PI;  // Reseta o ângulo após completar uma volta
        }
        repaint();
    }
}
