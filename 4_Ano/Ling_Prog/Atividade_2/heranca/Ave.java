package heranca;

class Ave extends Animal {

    public Ave(String nome) {
        super(nome);
        this.classe = "Ave";
    }

    @Override
    public String falar() {
        return "piu, piu";
    }

    public void voar(int n) {
        for (int i = 0; i < n; i++) {
            System.out.println("voando");
        }
    }
}
