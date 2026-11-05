public class DrawingConfiguration {
    private static DrawingConfiguration instance;

    private DrawingConfiguration() {
        // Configurações de inicialização
    }

    public static synchronized DrawingConfiguration getInstance() {
        if (instance == null) {
            instance = new DrawingConfiguration();
        }
        return instance;
    }

    public void showConfig() {
        System.out.println("Configuração do programa de desenho 3D.");
    }
}