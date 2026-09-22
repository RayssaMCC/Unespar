package heranca;

class Papagaio extends Ave {

    private String vocabulario;

    public Papagaio(String nome) {
        super(nome);
        this.vocabulario = "";
    }

    @Override
    public String falar() {
        return vocabulario;
    }

    public void setVocabulario(String vocabulario) {
        this.vocabulario = vocabulario;
    }
}