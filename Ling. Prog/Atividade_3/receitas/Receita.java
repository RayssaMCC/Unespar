package receitas;

public abstract class Receita {

    protected String tipo;

    public Receita(String tipo) {
        this.tipo = tipo;
    }

    public abstract String getIngredientes();

    public abstract String getModoDeFazer();

    public String getTipo() {
        return tipo;
    }
}
