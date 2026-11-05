package heranca;

class Cachorro extends Mamifero {

    private boolean tipoLatido;

    public Cachorro(String nome, int velocidade, boolean tipoLatido) {
        super(nome, velocidade);
        this.tipoLatido = tipoLatido;
    }

    public void setLateAlto() {
        this.tipoLatido = true;
    }

    public void setLateBaixo() {
        this.tipoLatido = false;
    }

    @Override
    public String falar() {
        if (tipoLatido) {
            return "AU, AU";
        } else {
            return "au, au";
        }
    }
}