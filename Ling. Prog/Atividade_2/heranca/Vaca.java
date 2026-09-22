package heranca;

class Vaca extends Mamifero {

    private boolean permiteOrdenha;

    public Vaca(String nome, int velocidade, boolean permiteOrdenha) {
        super(nome, velocidade);
        this.permiteOrdenha = permiteOrdenha;
    }

    public boolean isPermiteOrdenha() {
        return permiteOrdenha;
    }

    public void setPermiteOrdenha(boolean permiteOrdenha) {
        this.permiteOrdenha = permiteOrdenha;
    }

    @Override
    public String falar() {
        return "Muuuu";
    }

    public String ordenhar() {
        if (permiteOrdenha) {
            return "ordenhando";
        } else {
            return "Nao é possível ordenhar a vaca";
        }
    }
}
