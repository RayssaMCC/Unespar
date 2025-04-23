import javax.swing.*;
import java.awt.*;

public class ProxyPadraoDemo extends JFrame {
    private final ProxyImagem proxyImage;

    public ProxyPadraoDemo() {
        setTitle("Proxy Padrao Demo");
        setSize(400, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // Configuração do JProgressBar
        JProgressBar progressBar = new JProgressBar(0, 100);
        progressBar.setStringPainted(true);

        proxyImage = new ProxyImagem("imagem_grande.jpg", progressBar);

        JButton loadButton = new JButton("Carregar Imagem");
        loadButton.addActionListener(e -> proxyImage.display());

        // Layout da interface gráfica
        add(progressBar, BorderLayout.CENTER);
        add(loadButton, BorderLayout.SOUTH);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            ProxyPadraoDemo demo = new ProxyPadraoDemo();
            demo.setVisible(true);
        });
    }
}