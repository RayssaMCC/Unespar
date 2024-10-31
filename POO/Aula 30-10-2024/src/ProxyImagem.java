import javax.swing.*;

class ProxyImagem implements Imagem {
    private RealImagem realImage;
    private final String fileName;
    private final JProgressBar progressBar;

    public ProxyImagem(String fileName, JProgressBar progressBar) {
        this.fileName = fileName;
        this.progressBar = progressBar;
    }

    @Override
    public void display() {
        if (realImage == null) {
            loadImageWithProgress();
            realImage = new RealImagem(fileName);
        }
        realImage.display();
    }

    private void loadImageWithProgress() {
        SwingUtilities.invokeLater(() -> {
            for (int i = 0; i <= 100; i++) {
                progressBar.setValue(i);
                try {
                    Thread.sleep(30); // Simula progresso de carregamento
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });
    }
}