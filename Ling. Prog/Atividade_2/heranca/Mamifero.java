package heranca;

class Mamifero extends Animal {

    private int velocidade;

    public Mamifero(String nome, int velocidade) {
        super(nome);
        this.classe = "Mamífero";
        this.velocidade = velocidade;
    }

    public int getVelocidade() {
        return velocidade;
    }

    public void setVelocidade(int velocidade) {
        this.velocidade = velocidade;
    }

    public void correr() {
        for (int i = 0; i < velocidade; i++) {
            System.out.println("correndo");
        }
    }
}
