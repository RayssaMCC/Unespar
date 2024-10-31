class RealImagem implements Imagem {
    private final String fileName;

    public RealImagem(String fileName) {
        this.fileName = fileName;
        loadImageFromDisk();
    }

    private void loadImageFromDisk() {
        System.out.println("Carregando " + fileName);
        try {
            // Simula o tempo de carregamento da imagem
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void display() {
        System.out.println("Exibindo " + fileName);
    }
}