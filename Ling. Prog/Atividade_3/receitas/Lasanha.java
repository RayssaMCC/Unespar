package receitas;

public class Lasanha extends Receita implements Cozido, Assado {

    public Lasanha() {
        super("Salgado");
    }

    @Override
    public String getIngredientes() {
        return "Massa de lasanha, molho de tomate, queijo e carne moída.";
    }

    @Override
    public String getModoDeFazer() {
        return "Prepare o molho, monte as camadas de massa, " + "molho e queijo e leve ao forno.";
    }

    @Override
    public void cozinhar() {
        System.out.println("O molho da lasanha está cozinhando.");
    }

    @Override
    public void assar() {
        System.out.println("A lasanha está assando.");
    }
}
