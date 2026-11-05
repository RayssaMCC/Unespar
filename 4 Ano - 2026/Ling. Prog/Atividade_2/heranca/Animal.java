package heranca;

class Animal {
    private String nome;
    protected String classe;

    public Animal(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    public void imprime() {
        System.out.println("Nome: " + nome);
        System.out.println("Classe: " + classe);
    }

    public String falar() {
        return "";
    }
}

